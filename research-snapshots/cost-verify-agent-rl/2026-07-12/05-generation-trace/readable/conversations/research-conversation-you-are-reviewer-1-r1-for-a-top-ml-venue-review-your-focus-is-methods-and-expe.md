# Research conversation: You are Reviewer 1 (R1) for a top ML venue review. Your focus is **methods and experiments**. Review the paper below usi

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a5b02fdfddc805fc8.jsonl`
- **Structured JSON:** [`e949f5de37794d2774ce.json`](../../sessions/e9/e949f5de37794d2774ce.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

30 recorded events

### User

_source line 1 · 2026-05-17T12:55:21.751Z_

You are Reviewer 1 (R1) for a top ML venue review. Your focus is **methods and experiments**. Review the paper below using a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.

## Paper Summary

Title: "Dissecting Credit Assignment Failure in Multi-Turn LLM Agent RL: A Dual-Mechanism Analysis"

This is a diagnostic/analysis paper studying why step-independent training fails for multi-turn LLM agents and characterizing failure modes. The paper:
- Identifies 4 failure mechanisms: advantage sign misattribution, policy information loss, entropy collapse, bandit-level credit insufficiency
- Shows episode-level GRPO achieves 23.4% (±6.2pp) vs 1% for step-independent on ALFWorld
- Shows GAE with value function reaches 41%, a 17.6pp gap over episode-level GRPO
- Provides mechanistic analysis showing sign misattribution is dominant (r=0.73) but not sole factor
- Tests across environments (ScienceWorld), scales (1.7B→7B), reward shaping, selective verification strategies

## Full Paper Content (9 pages)

**Abstract**: RL for multi-turn LLM agents commonly adopts step-independent training (each context window as separate bandit arm). They show this fails due to advantage sign misattribution and policy information loss. Episode-level training eliminates sign misattribution but plateaus at 23.4% (±6.2pp) on ALFWorld. GAE reaches 41.0%. They decompose credit assignment failure into four factors, provide failure mode taxonomy, and derive design guidelines. Findings generalize across environments and model scales.

**Section 1 Introduction**: Sets up problem of step-independent optimization. On ALFWorld, step-independent GRPO collapses to ~1% while episode-level reaches 23.4%. Two mechanisms identified: sign misattribution (per-window advantages inherit sign from episode outcome) and policy information loss (truncated context prevents cross-step learning). Episode-level exposes deeper bottleneck: GRPO bandit-style credit where all tokens share same scalar advantage. GAE reaches 41%, 17.6pp improvement. Mechanistic analysis shows r=0.73 sign-outcome correlation with confounds from KL (r=0.31), entropy (r=0.27), position (r=-0.18).

Contributions:
1. Failure mode taxonomy with 4 mechanisms and quantified contributions
2. Empirical characterization of credit granularity spectrum
3. Actionable design guidelines

**Section 2 Background**: Standard MDP formulation for LLM agents. GRPO definition with group normalization. Step-independent mode splits trajectory into h-token windows. Episode-level mode treats full trajectory as single sample. GAE with learned value function for per-token advantages.

**Section 3 Failure Mode Taxonomy**: 
- Mechanism 1: Sign misattribution (r=0.73 with outcome, 78% success eps all-positive, 82% failure eps all-negative)
- Mechanism 2: Information loss (h-sweep shows monotonic degradation)
- Mechanism 3: Entropy collapse (0.20→0.12 while val stagnates 24-28%)
- Mechanism 4: Bandit-level credit insufficiency (17.6pp gap episode→GAE, r=-0.62 task complexity vs success)

**Section 4 Experimental Setup**: ALFWorld, Qwen3-1.7B primary, GRPO group size 8, lr 1e-6, KL 0.01, 15 steps primary, up to 50 steps convergence.

**Section 5 Results**:
- 5.1: Episode-level 23.4%±6.2pp, 95% CI [15.7%, 31.1%]. Plateau at step 15-20, train rises to 50% but val declines. pass@8=94% at step 50.
- 5.2: h-sweep (h=2,5,10,20,full). NOT clean monotonic—cross-seed variance high, h=5 sometimes beats h=10. Characterized as "probabilistic degradation."
- 5.3: 5-seed replication, range 15-30%, train-val gap 22.6pp. Seed 4 at 15% (cold-start problem).
- 5.4: GAE comparison. Step-ind 1% → Episode 24% → GAE(λ=1) 36.7% → GAE(λ=0.95) 41%. Per-token advantage variance 0.42 for GAE vs 0.0 for GRPO.
- 5.5: Mechanistic verification. Sign-outcome r=0.73 (hypothesized >0.95—PARTIAL). Sign-local quality r=0.28 (hypothesized <0.1—FAILED). Multiple confounds: KL r=0.31, entropy r=0.27, position r=-0.18. Sign misattribution accounts for only 53% of variance.
- 5.6: Task complexity analysis. pick 35%, pick_two 10%. r=-0.62 complexity vs success.
- 5.7: Reward shaping. valid_action_bonus hurts success (28→22%) while improving format compliance (55→72%).
- 5.8: Selective verification. Always-on 25%, confidence 19%, B-IAVR 16%, random 14%, no-verify 13%. Action-change reward r=0.08 (p=0.12), indistinguishable from noise.
- 5.9: ARES (SFT) dominates B-IAVR (RL) on both axes.
- 5.10: ScienceWorld 15% vs 3% (5×). 7B scaling: both improve ~7pp, ratio shrinks 25×→4×.

**Section 6 Discussion**: 5 actionable guidelines. Discussion of why community defaults to step-independent. Limitations: text-only envs, correlational mechanistic analysis, GAE cost not accounted.

**Section 7 Conclusion**: Summary of taxonomy and guidelines.

**References**: 10 references total.

## Experiment Design Context (from review_context.yaml)

The paper was framed as a diagnostic/analysis paper. Key context on experimental quality:

1. **h-sweep non-monotonicity**: The h-sweep results are NOT clean monotonic. h=5 occasionally beats h=10 between seeds. h=20 seed2 shows temporary dip. This is acknowledged in the paper as "probabilistic degradation."

2. **Mechanistic verification partially fails**: Sign-outcome correlation is 0.73, not >0.95 as hypothesized. Sign-local quality is 0.28, not <0.1. Several hypotheses only partially confirmed. The paper acknowledges confounds.

3. **Multi-seed variance is high**: 5-seed episode-level has std=6.2pp, 95% CI [15.7%, 31.1%] — too wide to make strong claims. Seed 4 only 15%.

4. **Selective verification (B-IAVR) completely fails**: Action-change reward signal is r=0.08 (p=0.12), indistinguishable from noise. After controlling for entropy, partial r=0.07 (p=0.15). B-IAVR is dominated by simple confidence baseline and by ARES SFT.

5. **GAE comparison is strong**: GAE >> episode-level (17.6pp gap), this is the paper's strongest finding.

6. **Missing experiments from design**: The full experiment plan includes 16 experiments. The paper covers most but lacks some detailed analyses (e.g., entropy-controlled action-change analysis from plan_010, causal intervention from plan_011, detailed reward signal ablation from plan_012 are partially covered but compressed).

## Your Review Task (R1: Methods + Experiments)

Evaluate:
1. **Methodological soundness**: Are the experimental designs appropriate? Are comparisons fair? Are confounds adequately addressed?
2. **Statistical rigor**: Are uncertainty estimates adequate? Is the number of seeds sufficient? Are claims supported by the confidence intervals?
3. **Experimental coverage**: Are key ablations present? What's missing?
4. **Reproducibility**: Enough detail to reproduce?
5. **Claim-evidence alignment**: Do the experimental results actually support the claims made?

Produce a structured review with:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted, with severity: major/minor)
- Questions for authors
- Missing experiments or analyses
- Score (1-6) and confidence (1-5)
- One-line recommendation

Be rigorous. This is a top venue review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "a5b02fdfddc805fc8",
  "type": "user",
  "uuid": "4297c99c-ce85-48af-bf44-48ef68e9a5fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T12:55:21.760Z_

```json
{
  "parentUuid": "4297c99c-ce85-48af-bf44-48ef68e9a5fb",
  "isSidechain": true,
  "agentId": "a5b02fdfddc805fc8",
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
  "uuid": "1501e49c-eb6d-47b1-a84b-c8380f2ad92e",
  "timestamp": "2026-05-17T12:55:21.760Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-17T12:55:24.574Z_



I'll start by reading the actual paper and any available project files to ground my review in the full content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1501e49c-eb6d-47b1-a84b-c8380f2ad92e",
  "isSidechain": true,
  "agentId": "a5b02fdfddc805fc8",
  "requestId": "req_011Cb8BC1JM5YNLVJGYD5YYQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc563ced-eb89-42ec-83e7-7f23bc9a1d1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eb5SorsDP7BdRPuhU8cbec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9208,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9208,
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

_source line 4 · 2026-05-17T12:55:25.341Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JxCk4fnPtSSNG913p28ksj`</summary>

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
  "parentUuid": "cc563ced-eb89-42ec-83e7-7f23bc9a1d1b",
  "isSidechain": true,
  "agentId": "a5b02fdfddc805fc8",
  "requestId": "req_011Cb8BC1JM5YNLVJGYD5YYQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa8c687d-6a47-42a5-bc23-52813b7c6e71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eb5SorsDP7BdRPuhU8cbec",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9208,
      "cache_read_input_tokens": 8252,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9208
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 128,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 9208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9208,
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

_source line 5 · 2026-05-17T12:55:25.349Z_

<details><summary>↩ Tool result · `toolu_01JxCk4fnPtSSNG913p28ksj`</summary>

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
  "parentUuid": "fa8c687d-6a47-42a5-bc23-52813b7c6e71",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "a5b02fdfddc805fc8",
  "type": "user",
  "uuid": "20e1e946-1dd1-4b22-bd26-6c3c4c12ad91",
  "sourceToolAssistantUUID": "fa8c687d-6a47-42a5-bc23-52813b7c6e71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T12:55:28.494Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01TnXW3YP2tGCpJNMsVUsYEy`</summary>

```json
{
  "project": "cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20e1e946-1dd1-4b22-bd26-6c3c4c12ad91",
  "isSidechain": true,
  "agentId": "a5b02fdfddc805fc8",
  "requestId": "req_011Cb8BCGeps7Lzg7hhWynrS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3a32604-5424-4e1a-ab89-3d9e448c08f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0187wuz7nJWyqhGF4cxT75qW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 17460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

_source line 7 · 2026-05-17T12:55:28.723Z_

<details><summary>↩ Tool result · `toolu_01TnXW3YP2tGCpJNMsVUsYEy`</summary>

```text
{"result":"# 项目 cost-verify-agent-rl 概况\n\n## 实验状态 (57 个)\n\n- **exp010**: DONE (failed) — \n- **exp009**: DONE (failed) — \n- **exp008**: PREPARING (killed) — \n- **exp007**: DONE (failed) — \n- **exp007_dryrun**: PREPARING — \n- **exp003**: DONE (failed) — \n- **exp005**: PREPARING — \n- **exp_003**: PREPARING (failed) — \n- **exp_003_dryrun**: PREPARING (failed) — \n- **exp_003_dryrun2**: PREPARING (failed) — \n- **exp003_dryrun3**: PREPARING (failed) — \n- **exp_003_dryrun3**: PREPARING (failed) — \n- **exp_002**: DONE (failed) — \n- **exp_001b**: DONE (failed) — \n- **exp_001**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| hsweep_h2_seed1 | Step-independent GRPO with h=2 (minimal context, N=25 windows per episode) will catastrophically collapse due to advantage sign misattribution: early windows retain only γ^24=0.95^24≈29% of terminal return, and all windows in failed episodes receive undifferentiated negative advantage regardless of action quality | — | — | — |\n\n## 待处理\n- exp028_prereq_zeroshot_instruct: Qwen3-1.7B-Instruct 零样本 ALFWorld eval，验证\"SFT是毒药\"假设。如果 Instruct ≥15% success（vs SFT checkpoint 6.25%），则确认 SFT 起点有害，exp028a 可跳过 SFT 直接 GRPO。（准备中）\n- exp021_sft_ragen_format: Two-stage SFT with RAGEN-format data (v4). From exp008_sft checkpoint, fine-tune with v4 data (RAGEN Turn/State/Reward structure, fixed system prompt with consistent &lt;answer> tag instruction). LR=5e-6, 2 epochs. Validate via RAGEN val_before_train (not eval_sft_fast). Pass: RAGEN val success >= 10%, action_is_valid >= 85%.（准备中）\n- exp020d_grpo_from_sft: GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Symlink fix for response_mask assertion (proven in exp020b). exp020c failed: Hydra key path wrong.（准备中）\n- exp020c_grpo_from_sft: GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Fix: symlink + enable_response_mask=false (exp020/020b crashed on response_mask assertion).（准备中）\n- exp019c_expert_sft_v3: Two-stage Expert SFT（重试）: 从 exp008_sft checkpoint 出发，用 v3 数据（保留原始 move actions + admissible actions augmentation）微调。LR=5e-6, 2 epochs, batch=4, grad_accum=4, max_seq=4096。Pass: success ≥ 10%, format_ok ≥ 90%, action_is_valid ≥ 85%。（准备中）\n- exp019b_expert_sft_v2（准备中）\n- exp018_sft_grpo: Expert SFT → Sparse GRPO：从 exp017 SFT checkpoint 开始纯 sparse GRPO 训练。SFT 提升 baseline success rate（≥10%），使 GRPO 有足够非零 reward group 产生有效梯度。LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, won=10.0, 无 bonus/penalty, GRPO 30 步。Pass: success ≥ 20%。（准备中）\n- exp014b: 极低 Dense Reward: valid_action_bonus=0.01（1:1000 比例），测试极弱 bonus 能否防 collapse 又不引发 gaming。如果 bonus 弱到不影响 GRPO reward ranking，模型不会被诱导走捷径。success_reward=10.0, format_penalty=0, 从 exp008 step 5 checkpoint 恢复, GRPO 30 步。（准备中）\n- exp014a: Success-Gated Dense Reward: valid_action_bonus=0.15 只在 group 内至少一条 trajectory success 时才给。消除 reward gaming 的独立最大化路径——没有 success 就没有 bonus，模型必须探索 success。success_reward=10.0, format_penalty=0, 从 exp008 step 5 checkpoint 恢复, GRPO 30 步。（准备中）\n- exp014c: Success-gated valid_action_bonus：bonus 仅在 episode 成功时累加到 reward，消除独立最大化路径。valid_action_bonus=0.15, success_reward=10.0。解决 exp013f reward gaming（unconditional bonus 导致 agent 放弃 success 追求 valid action）。从 step 5 checkpoint 恢复 GRPO 30 步。（准备中）\n- …另有 8 项\n\n## 近期结论\n- **exp025c** (failed): —\n- **exp029_episode_level** (success): Episode-level"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3a32604-5424-4e1a-ab89-3d9e448c08f9",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "a5b02fdfddc805fc8",
  "type": "user",
  "uuid": "295fbd5d-fc0a-49ca-918c-3ee15485065f",
  "sourceToolAssistantUUID": "f3a32604-5424-4e1a-ab89-3d9e448c08f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T12:55:28.891Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UAjFsG5rFzREhG6vZL5NTL`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "295fbd5d-fc0a-49ca-918c-3ee15485065f",
  "isSidechain": true,
  "agentId": "a5b02fdfddc805fc8",
  "requestId": "req_011Cb8BCGeps7Lzg7hhWynrS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71347ead-a47a-4108-8b87-f2b249d7b8be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0187wuz7nJWyqhGF4cxT75qW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 17460,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1451
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 17460,
          "cache_creation_input_tokens": 1451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1451,
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

_source line 9 · 2026-05-17T12:55:28.901Z_

<details><summary>↩ Tool result · `toolu_01UAjFsG5rFzREhG6vZL5NTL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| hsweep_h2_seed1 | Step-independent GRPO with h=2 (minimal context, N=25 windows per episode) will catastrophically collapse due to advantage sign misattribution: early windows retain only γ^24=0.95^24≈29% of terminal return, and all windows in failed episodes receive undifferentiated negative advantage regardless of action quality | — | — | — |\\n\\n## 待处理\\n- exp028_prereq_zeroshot_instruct: Qwen3-1.7B-Instruct 零样本 ALFWorld eval，验证\\\"SFT是毒药\\\"假设。如果 Instruct ≥15% success（vs SFT checkpoint 6.25%），则确认 SFT 起点有害，exp028a 可跳过 SFT 直接 GRPO。（准备中）\\n- exp021_sft_ragen_format: Two-stage SFT with RAGEN-format data (v4). From exp008_sft checkpoint, fine-tune with v4 data (RAGEN Turn/State/Reward structure, fixed system prompt with consistent &lt;answer> tag instruction). LR=5e-6, 2 epochs. Validate via RAGEN val_before_train (not eval_sft_fast). Pass: RAGEN val success >= 10%, action_is_valid >= 85%.（准备中）\\n- exp020d_grpo_from_sft: GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Symlink fix for response_mask assertion (proven in exp020b). exp020c failed: Hydra key path wrong.（准备中）\\n- exp020c_grpo_from_sft: GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Fix: symlink + enable_response_mask=false (exp020/020b crashed on response_mask assertion).（准备中）\\n- exp019c_expert_sft_v3: Two-stage Expert SFT（重试）: 从 exp008_sft checkpoint 出发，用 v3 数据（保留原始 move actions + admissible actions augmentation）微调。LR=5e-6, 2 epochs, batch=4, grad_accum=4, max_seq=4096。Pass: success ≥ 10%, format_ok ≥ 90%, action_is_valid ≥ 85%。（准备中）\\n- exp019b_expert_sft_v2（准备中）\\n- exp018_sft_grpo: Expert SFT → Sparse GRPO：从 exp017 SFT checkpoint 开始纯 sparse GRPO 训练。SFT 提升 baseline success rate（≥10%），使 GRPO 有足够非零 reward group 产生有效梯度。LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, won=10.0, 无 bonus/penalty, GRPO 30 步。Pass: success ≥ 20%。（准备中）\\n- exp014b: 极低 Dense Reward: valid_action_bonus=0.01（1:1000 比例），测试极弱 bonus 能否防 collapse 又不引发 gaming。如果 bonus 弱到不影响 GRPO reward ranking，模型不会被诱导走捷径。success_reward=10.0, format_penalty=0, 从 exp008 step 5 checkpoint 恢复, GRPO 30 步。（准备中）\\n- exp014a: Success-Gated Dense Reward: valid_action_bonus=0.15 只在 group 内至少一条 trajectory success 时才给。消除 reward gaming 的独立最大化路径——没有 success 就没有 bonus，模型必须探索 success。success_reward=10.0, format_penalty=0, 从 exp008 step 5 checkpoint 恢复, GRPO 30 步。（准备中）\\n- exp014c: Success-gated valid_action_bonus：bonus 仅在 episode 成功时累加到 reward，消除独立最大化路径。valid_action_bonus=0.15, success_reward=10.0。解决 exp013f reward gaming（unconditional bonus 导致 agent 放弃 success 追求 valid action）。从 step 5 checkpoint 恢复 GRPO 30 步。（准备中）\\n- …另有 8 项\\n\\n## 近期结论\\n- **exp025c** (failed): —\\n- **exp029_episode_level** (success): Episode-level 训练（context_window_mode: full）解决 step_independent h=2 的信用分配缺陷，模型能学到跨步规划策略，val success 不再停滞于 baseline。 ← 基于 exp028c_selfguide_recipe\\n  [exp029_episode_level_diagnose_attempt4](/api/workspace-files/projects/cost-verify-agent-rl/artifacts/exp029_episode_level/report/diagnose_attempt4.md) | [tatsu_patch_deploy_plan](/api/workspace-files/projects/cost-verify-agent-rl/artifacts/exp029_episode_level/intermediate/tatsu_patch_deploy_plan.md) | [credit_assignment_analysis](/api/workspace-files/projects/cost-verify-agent-rl/artifacts/exp029_episode_level/chart/credit_assignment_analysis_info.md)\\n- **exp026_step_independent_grpo** (negative): Step-independent GRPO（每步独立优化、不建模跨步依赖）能在ALFWorld多步任务中学到有效策略，因为每步的local reward信号足以引导正确行为选择 ← 基于 exp021_ragen_sft_v4\\n\\n## 趋势\\n成功 4 / 负向 5 / 失败 20 / 共 38\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-17606: 无 GPU 信息\\n\\n## 告警\\n- exp_001: 训练失败 — unknown\\n- exp_001b: 训练失败 — unknown\\n- exp_002: 训练失败 — unknown\\n- exp003: 训练失败 — unknown\\n- exp007: 训练失败 — unknown\\n- exp009: 训练失败 — unknown\\n- exp010: 训练失败 — unknown\\n- exp011: 已被终止 — unknown\\n- exp012: 训练失败 — unknown\\n- exp012b: 已被终止 — unknown\\n- exp013: 已被终止 — unknown\\n- exp013b: 训练失败 — unknown\\n- exp013c: 已被终止 — unknown\\n- exp013d: 训练失败 — unknown\\n- exp013e: 训练失败 — unknown\\n- exp015: 已被终止 — unknown\\n- exp016: 训练失败 — unknown\\n- exp019_expert_sft_v2: 已被终止 — unknown\\n- exp020_grpo_from_sft: 训练失败 — unknown\\n- exp022_grpo_from_sft_v4: 已被终止 — unknown\\n- exp023_grpo_parallel: 训练失败 — unknown\\n- exp023c_grpo_serial: 训练失败 — unknown\\n- exp024_success_gated_grpo: 已被终止 — unknown\\n- exp025: 训练失败 — unknown\\n- exp025b: 训练失败 — unknown\\n- exp025c: 训练失败 — unknown\\n- exp027_stable_grpo: 训练失败 — unknown\\n- exp028a_recipe_fix: 已被终止 — unknown\\n- exp028c_selfguide_recipe: 训练失败 — unknown\\n\", \"total_chars\": 4728, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71347ead-a47a-4108-8b87-f2b249d7b8be",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "a5b02fdfddc805fc8",
  "type": "user",
  "uuid": "ac33a425-a9d7-48af-bb79-ecb39b668c92",
  "sourceToolAssistantUUID": "71347ead-a47a-4108-8b87-f2b249d7b8be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T12:55:32.150Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01CfMbu127kH2nzZwPU4TH5E`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac33a425-a9d7-48af-bb79-ecb39b668c92",
  "isSidechain": true,
  "agentId": "a5b02fdfddc805fc8",
  "requestId": "req_011Cb8BCXxa87PE5e7172j7c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b92f3e99-5266-4650-8db4-ba7e11fb3f81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5h4W5uuU8UDDCVL3M8NxJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4325,
      "cache_read_input_tokens": 18911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4325,
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

_source line 11 · 2026-05-17T12:55:32.183Z_

<details><summary>↩ Tool result · `toolu_01CfMbu127kH2nzZwPU4TH5E`</summary>

```text
artifacts/dream_reports/dream_20260516T235255/best/paper.tex
artifacts/dream_reports/dream_20260516T235255/median/paper.tex
artifacts/dream_reports/dream_20260516T235255/worst/paper.tex
artifacts/_project/paper/theoretical_analysis.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/experiments_aa43d8.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/discussion.tex
docs/paper/experiments.tex
artifacts/_project/paper/conclusion.tex
docs/paper/discussion.tex
docs/paper/theoretical_analysis.tex
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
artifacts/dream_reports/dream_20260517T121256/best/paper.tex
artifacts/dream_reports/dream_20260517T121256/median/paper.tex
artifacts/dream_reports/dream_20260517T121256/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b92f3e99-5266-4650-8db4-ba7e11fb3f81",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "a5b02fdfddc805fc8",
  "type": "user",
  "uuid": "5e91f7fc-e3a1-41c4-8513-e1adaadd6ad3",
  "sourceToolAssistantUUID": "b92f3e99-5266-4650-8db4-ba7e11fb3f81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T12:55:32.642Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017oWP3MLFFGJ7JoSbLSjxVV`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e91f7fc-e3a1-41c4-8513-e1adaadd6ad3",
  "isSidechain": true,
  "agentId": "a5b02fdfddc805fc8",
  "requestId": "req_011Cb8BCXxa87PE5e7172j7c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "831f2686-92a4-4c64-9677-d7d7934e1adb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5h4W5uuU8UDDCVL3M8NxJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4325,
      "cache_read_input_tokens": 18911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4325,
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

_source line 13 · 2026-05-17T12:55:32.652Z_

<details><summary>↩ Tool result · `toolu_017oWP3MLFFGJ7JoSbLSjxVV`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'cost-verify-agent-rl'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "831f2686-92a4-4c64-9677-d7d7934e1adb",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "a5b02fdfddc805fc8",
  "type": "user",
  "uuid": "09594fc4-b564-414d-8781-22f3aa572ef0",
  "sourceToolAssistantUUID": "831f2686-92a4-4c64-9677-d7d7934e1adb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T12:55:33.324Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HoNbKHLNY23NdqZpDCbmzi`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09594fc4-b564-414d-8781-22f3aa572ef0",
  "isSidechain": true,
  "agentId": "a5b02fdfddc805fc8",
  "requestId": "req_011Cb8BCXxa87PE5e7172j7c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6730851-d82e-4ae2-87ea-8eb58fca8111",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5h4W5uuU8UDDCVL3M8NxJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4325,
      "cache_read_input_tokens": 18911,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4325
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 287,
          "cache_read_input_tokens": 18911,
          "cache_creation_input_tokens": 4325,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4325,
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

_source line 15 · 2026-05-17T12:55:33.335Z_

<details><summary>↩ Tool result · `toolu_01HoNbKHLNY23NdqZpDCbmzi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/paper_framing.md\", \"content\": \"# Paper Framing — Learning When to Verify: RL-Trained Selective Self-Verification for Interactive Agents\\n\\n> Post-MVP 重写 (2026-05-17) | D054 framing pivot + Dream Review feedback (weak reject → 修正理论)\\n\\n## Core Insight\\n\\nMulti-turn interactive agents 的 self-verification 大部分是 confirmatory（不改变行为）而非 corrective。训练 agent 学 selective verification 的前提是 RL 训练本身能 work。我们发现 LLM agent 社区默认的 step-independent training 在长 horizon 任务中灾难性崩溃，根因是**双机制失效**：\\n\\n1. **Policy Information Loss**: 短窗口（h 步）的 policy 无法学习跨步策略（如 \\\"先探索 drawer 再去 countertop\\\"）\\n2. **Advantage Sign Misattribution**: step_independent 中，per-window advantage 的**符号**由 episode 成败决定，而非 window-local action quality：\\n   - 失败 episode 中的好 action → 获得负 advantage（被错误惩罚）\\n   - 成功 episode 中的差 action → 获得正 advantage（被错误强化）\\n   - 梯度方向（reinforce/suppress）反映 episode outcome 而非 local decision quality\\n   - 附加：γ^k magnitude decay 使早期 window 信号更弱（γ^24 ≈ 29%, where 24 = ⌈T/h⌉-1 windows），但方向错误比幅度衰减更致命\\n\\nEpisode-level training 同时解决两者：policy 看全历史（解决 1），整条 trajectory 作为一个 GRPO 样本，所有 tokens 共享同一 advantage — 虽然仍是 episode-level credit（非 per-token），但消除了 window 间的 sign misattribution，因为不再需要将 episode reward 分配到独立优化的子窗口（解决 2）。\\n\\n**技术澄清**：GRPO 算法本身是 bandit-style（advantage = (R-μ)/σ，无显式 γ），但 RAGEN 的 step_independent 实现在 `compute_step_discounted_returns()` 中引入 γ 计算每个 window 的 return（代码：`agent_trainer.py:271-340`）。γ^(T-t) decay 对 step_independent 模式是代码事实，不是类比。Episode-level 模式下无此问题：整条 trajectory 只有一个 return = episode_reward。\\n\\n## Story Arc\\n\\n**Dual contribution**: Training methodology diagnosis + Selective verification system\\n\\n叙事线：\\n1. Self-verification 对 interactive agents 有用，但 always-on 成本高\\n2. 训练 agent 学 WHEN to verify 需要 RL → 但 LLM agent 社区默认的 step-independent training 在多轮任务上灾难性崩溃（0% at step 10）\\n3. 我们诊断双机制根因（information loss + advantage sign misattribution），提出 episode-level GRPO 解决\\n4. 分析 \\\"为什么社区默认走向 step-independent\\\"（context window 限制 + token-level training 惯性 + framework design accident）\\n5. 在 episode-level 基础上，用 action-change 作为 verification informativeness 的 reward，训练 selective policy\\n6. 结果：near-always-on performance + 显著降低 verification cost\\n\\n**定位**：不 claim \\\"发明了 episode-level RL\\\"（trivial），而是 \\\"诊断了 LLM agent RL 训练中被忽视的 step-independent 隐性代价 + 系统分析崩溃机制 + 提出实用修复方案 + 在此基础上实现 selective verification\\\"\\n\\n## Target Venue\\n\\n待定（NeurIPS 2026 / EMNLP 2026 / ICLR 2026），取决于实验进度和最终效果。\\n\\n## Core Claims\\n\\n### Claim 1 (strength: strong): Step-independent GRPO catastrophically fails for multi-turn agents due to dual mechanism\\n- 所需证据：episode-level vs step-independent 对比（多 seed），h-sweep ablation（3 seeds each），mechanistic analysis（gradient signal measurement），GAE baseline comparison\\n- 当前证据状态：**ESTABLISHED** (exp029 step5 val=25% vs exp028c step10 val=0%)\\n- 机制：(1) policy information loss (h-step context insufficient), (2) advantage sign misattribution (gradient direction reflects episode outcome, not window-local action quality; additionally γ^k magnitude decay for early windows)\\n- 技术细节：GRPO 算法无固有 γ，但 RAGEN step_independent 的 `compute_step_discounted_returns()` 引入 γ-discounted per-window returns → advantage 符号由 episode 成败决定。代码验证：`agent_trainer.py:271-340` + `core_algos.py:194-246`\\n\\n### Claim 2 (strength: moderate): Action-change is an effective intrinsic reward for verification informativeness\\n- 所需证据：selective verification 训练收敛 + action-change vs random/confidence baselines\\n- 当前证据状态：**not yet established**，依赖 Phase B 实验\\n- 前提：episode-level 训练的 agent 需达到 ≥40% success 才有意义\\n\\n### Claim 3 (strength: moderate): Learned selective policy matches always-on performance at reduced verification cost\\n- 所需证据：B-IAVR verification ↓40%+ 且 success delta < 3pp vs always-on\\n- 当前证据状态：**not yet established**，依赖 Phase B + C\\n- 前提：Claim 1 的 agent 需足够强\\n\\n## Contingency Plan\\n\\n如果 episode-level 训练收敛后 success 仍 < 40%（不足以支撑 cost-efficiency story）：\\n- **Plan A**：paper 变为 diagnostic + analysis contribution — \\\"Why Step-Independent RL Fails for LLM Multi-Turn Agents: Dual Mechanism Analysis\\\" (需更深 ablation + GAE comparison + community practice survey)\\n- **Plan B**：加 Self-Guide reward 到 episode-level（从 binary→dense reward），推高 performance 后再做 selective verification\\n- 不考虑 downgrade venue\\n- **注意**：Dream review 已证明 Plan A 纯 methodology paper 需要比预期更深的分析才能通过审稿（\\\"诊断社区默认实践的隐性代价\\\" > \\\"episode-level RL works\\\"）\\n\\n## Reviewer Attack Surface + Defense\\n\\n| # | Concern | Severity | Defense |\\n|---|---------|----------|---------|\\n| 1 | \\\"Episode-level RL is obvious / well-known\\\" | HIGH | h-sweep (3 seeds) 展示 non-trivial cliff + 双机制理论 + \\\"为什么社区默认 step-independent\\\" 分析 |\\n| 2 | \\\"Theory 与 GRPO 不匹配\\\" | HIGH | 精确区分：GRPO 算法无 γ，但 step_independent 实现引入 γ-discounted returns（代码引用）→ per-window advantage logging 实证 + 伪代码 |\\n| 3 | \\\"缺 GAE/标准 RL baselines\\\" | HIGH | 加 GAE(λ=0.95) + GAE(λ=1,γ=1) baseline，证明 episode-level GRPO 与 GAE 的差异 |\\n| 4 | \\\"Self-Guide 3x performance gap\\\" | HIGH | 正面回应：不同 paradigm (expert-guided vs from-scratch RL)，不同问题（Self-Guide 回避了训练问题） |\\n| 5 | Single environment (ALFWorld) | MEDIUM | ScienceWorld transfer (if resources permit) |\\n| 6 | Small model (1.7B) | MEDIUM | 定位 resource-constrained; 7B 验证 (conditional) |\\n| 7 | Action-change = noise vs signal | MEDIUM | Entropy-controlled analysis + causal intervention (Phase B) |\\n| 8 | 与 ARES 差异化不足 | LOW | Head-to-head 对比 + 方法论差异表 |\\n| 9 | \\\"Turn-PPO 已解决相同问题\\\" | HIGH | 精确区分：Turn-PPO 发现 uniform advantage (subset)，我们发现 sign misattribution (superset + 量化 γ^24≈29%)；解法相反 (finer vs coarser) |\\n\\n## Evidence Status Matrix\\n\\n| Claim | MVP Evidence | Research Evidence Needed | Priority |\\n|-------|-------------|--------------------------|----------|\\n| Claim 1 | exp029 vs exp028c (25% vs 0%) | h-value ablation, multi-seed, mechanism paper figure | P0 |\\n| Claim 2 | N/A | Phase B full implementation | P1 |\\n| Claim 3 | N/A | Phase B + C comparison suite | P1 |\\n\\n## Competitive Positioning\\n\\n| System | Method | Benchmark | Key Difference from Us |\\n|--------|--------|-----------|----------------------|\\n| Self-Guide (2026) | Always-on verification | ALFWorld 72.7% (1.7B) | We add selectivity via RL |\\n| ARES (2603.07915) | SFT router, continuous effort | 52.7% token reduction | SFT vs RL, continuous vs binary |\\n| Thinkless (NeurIPS'25) | RL control token | reasoning domain | Same RL philosophy, different domain |\\n| ReflAct (EMNLP'25) | Prompting GPT-4 | ALFWorld 93.3% | Different scale/approach |\\n| RAGEN (2025) | GRPO for agents | varies | Step-independent default, our baseline |\\n| **Turn-PPO (2512.17008)** | Turn-level MDP + value fn | reasoning tasks | \\\"Uniform advantage\\\" vs our \\\"sign misattribution\\\"; finer credit vs coarser |\\n| **GAGPO (2605.13217)** | Grouped value proxy, step-aligned | ALFWorld 93.5% (1.5B) | Finer-grained credit for performance; we diagnose mechanism failure |\\n| **MT-GRPO (2505.11821)** | Turn-level reward design | QA search tasks | Turn-level credit; we show coarser suffices |\\n| **iStar (ICLR'26)** | Implicit PRM + dual advantage | WebShop 86.5% | Learns step rewards; we show episode-level eliminates misattribution |\\n| **ArCHer (ICML'24)** | Hierarchical multi-turn RL | multi-turn agents | Foundational framework; establishes need for hierarchical structure |\\n| **HiPER (2602.16165)** | Hierarchical Plan-Execute RL | ALFWorld 97.4% (7B) | SOTA performance pursuit; we do mechanism diagnosis |\\n\\n### Positioning Strategy\\n\\n**核心差异化：Contrarian Solution。** 竞品（Turn-PPO, GAGPO, MT-GRPO, iStar, HiPER）一致认为 multi-turn RL 需要更细粒度的 credit assignment（turn-level, step-level, hierarchical），并用此提升性能。我们的贡献是诊断性的：\\n\\n1. **问题定义更精确**：Turn-PPO 发现 \\\"uniform advantage\\\" 问题（所有 turn 获得相同 advantage），我们发现更本质的 \\\"Advantage Sign Misattribution\\\"（advantage 符号由 episode outcome 决定而非 local action quality），并量化 γ^24 ≈ 29% 的 return 衰减。Sign misattribution 是 uniform advantage 的超集。\\n\\n2. **Contrarian solution**：所有竞品的解法都是引入更细的 credit（turn-level value, step-level PRM, hierarchical planner）。我们展示更粗的 episode-level credit 反而消除 sign misattribution，因为它避免了将 episode reward 错误分配到独立优化的子窗口。这挑战了 \\\"越细越好\\\" 的社区默认假设。\\n\\n3. **不同 contribution 维度**：GAGPO/HiPER 追求 ALFWorld 93-97% 的 SOTA performance（通过更好的 credit + 更复杂的架构）。我们不 compete on performance axis，而是回答 \\\"为什么社区默认的 step-independent 灾难性失败\\\" 这个诊断问题。两个 contribution 维度正交互补。\\n\\n4. **与 CA Survey 的关系**：Zhang (2604.09459) 系统化了 47 种 CA 方法，但未分析 CA 方法本身的 failure modes（何时更细粒度反而有害）。我们填补这一空白。\\n\\n## Research Phases\\n\\n1. **Phase A (DONE)**: Episode-level GRPO training — MVP passed, demonstrates Claim 1\\n2. **Phase A+**: Continue training to convergence (target ≥40% success), deploy tatsu parallel patch, multi-seed\\n3. **Phase B**: Implement selective verification with action-change reward — Claim 2 & 3\\n4. **Phase C**: Ablation suite — context window sweep, reward ablations, baseline comparisons\\n5. **Phase D**: (Conditional on resources) Multi-env / multi-model scaling\\n\", \"total_chars\": 8631, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6730851-d82e-4ae2-87ea-8eb58fca8111",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "a5b02fdfddc805fc8",
  "type": "user",
  "uuid": "20e16de2-23b1-48c3-b1e7-4897fd1f2be4",
  "sourceToolAssistantUUID": "e6730851-d82e-4ae2-87ea-8eb58fca8111",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-17T12:55:35.448Z_

Let me read the actual paper tex files to ground the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20e16de2-23b1-48c3-b1e7-4897fd1f2be4",
  "isSidechain": true,
  "agentId": "a5b02fdfddc805fc8",
  "requestId": "req_011Cb8BCrw62dAwU9ic5pajW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6efc2ca-2241-46a5-a86f-76d7e29bda9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WK4rzJEf186JXyMp7DF5Vp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4609,
      "cache_read_input_tokens": 23236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4609,
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

_source line 17 · 2026-05-17T12:55:36.405Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Hzo8TaJ1NPPiXFwRVycU53`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260517T121256/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6efc2ca-2241-46a5-a86f-76d7e29bda9b",
  "isSidechain": true,
  "agentId": "a5b02fdfddc805fc8",
  "requestId": "req_011Cb8BCrw62dAwU9ic5pajW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "676cccaf-272a-45c4-829d-f800ae83ff63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WK4rzJEf186JXyMp7DF5Vp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4609,
      "cache_read_input_tokens": 23236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4609,
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

_source line 18 · 2026-05-17T12:55:36.676Z_

<details><summary>↩ Tool result · `toolu_01Hzo8TaJ1NPPiXFwRVycU53`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{amsmath,amssymb}
4	\usepackage{booktabs}
5	\usepackage{graphicx}
6	\usepackage{hyperref}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage{subcaption}
10	
11	\title{Learning When to Verify: RL-Trained Selective Self-Verification for Interactive Agents}
12	
13	\author{Anonymous}
14	
15	\date{}
16	
17	\begin{document}
18	\maketitle
19	
20	\begin{abstract}
21	Self-verification improves interactive agent performance but incurs substantial inference cost, with the majority of verification steps merely confirming existing decisions without changing behavior. We address the problem of training agents to selectively verify only when verification is likely to be informative. A prerequisite for this is effective Reinforcement Learning (RL) training of multi-turn agents, yet we find that the community-default step-independent training paradigm catastrophically fails in long-horizon settings. We diagnose a dual mechanism: (1) policy information loss from truncated context windows, and (2) advantage sign misattribution where per-window gradient direction reflects episode outcome rather than local action quality. Episode-level GRPO resolves both issues, achieving 46.8\% $\pm$ 2.4\% validation success on ALFWorld (5 seeds) compared to 0\% for step-independent training. Building on this foundation, we propose B-IAVR (Binary Informed Action-change Verification Routing), which uses action-change as an intrinsic reward signal for verification informativeness. B-IAVR reduces verification rate by 52\% while maintaining task success within 1.5 percentage points of always-on verification, and achieves the highest success-per-cost ratio (0.75) among all methods including an SFT-based baseline.
22	\end{abstract}
23	
24	\section{Introduction}
25	
26	Interactive agents that operate in multi-step environments face a fundamental tension between performance and efficiency. Self-verification, where an agent re-examines its proposed action before execution, consistently improves task success across environments. However, empirical analysis reveals that 77\% of verification steps are confirmatory, merely reaffirming the original action without behavioral change. This suggests that a large fraction of verification computation is wasted.
27	
28	Training an agent to learn \emph{when} to verify requires RL, since the value of verification at any step depends on the full trajectory context and cannot be determined by static rules. This requirement exposes a critical failure in current LLM agent training practice. The dominant paradigm, step-independent training as implemented in frameworks like RAGEN, processes each context window as an independent optimization unit. We demonstrate that this approach catastrophically collapses to 0\% task success in multi-turn settings.
29	
30	We identify a dual mechanism responsible for this collapse. First, \textbf{policy information loss}: when the policy observes only $h$ steps of history, it cannot learn cross-step strategies (e.g., ``explore drawer A before navigating to countertop B''). Second, \textbf{advantage sign misattribution}: in the step-independent regime, each window's advantage sign is determined by the episode outcome rather than local action quality. Good actions in failed episodes receive negative advantage (incorrect punishment), while poor actions in successful episodes receive positive advantage (incorrect reinforcement). Per-window advantage logging confirms this empirically: the correlation between advantage sign and episode outcome is $r = 0.97$, while the correlation with local action quality is merely $r = 0.04$.
31	
32	Episode-level GRPO resolves both mechanisms simultaneously. The policy observes complete episode history (resolving information loss), and all tokens share a single episode-level advantage, eliminating the need to distribute reward signals across independently-optimized windows (resolving sign misattribution). This is not a novel algorithm but a diagnostic insight: the community default is silently broken for multi-turn tasks, and the fix is straightforward.
33	
34	With effective RL training established, we address the original question: learning selective verification. We propose B-IAVR, which trains a binary verify/skip decision using action-change as the reward signal for verification informativeness. When the agent verifies and changes its action, this indicates the verification was informative; the reward function directly incentivizes verification at such decision points.
35	
36	Our contributions are:
37	\begin{enumerate}
38	\item A systematic diagnosis of why step-independent RL training fails for multi-turn LLM agents, identifying dual mechanisms (information loss and sign misattribution) with empirical verification across 3 seeds, 5 context-window sizes, and 2 environments.
39	\item Episode-level GRPO as a practical fix achieving 46.8\% $\pm$ 2.4\% success (5 seeds) on ALFWorld with Qwen3-1.7B, validated on ScienceWorld (32\% vs 8\% step-independent) and Qwen3-7B (58\% vs 5\%).
40	\item B-IAVR, a selective verification method that reduces verification cost by 52\% with only 1.5pp success degradation, outperforming ARES reproduction (+3.5pp success at 10pp lower cost) and achieving the best success-per-cost ratio among all baselines.
41	\end{enumerate}
42	
43	\section{Related Work}
44	
45	\paragraph{RL for LLM Agents.}
46	RAGEN introduced GRPO-based training for multi-turn LLM agents using a step-independent paradigm where each context window is treated as an independent optimization unit. While effective for short-horizon tasks, this paradigm's failure modes in long-horizon settings have not been systematically analyzed. Our work provides this analysis and demonstrates that episode-level training resolves the identified issues.
47	
48	\paragraph{Self-Verification in Agents.}
49	Self-Guide trains always-on self-verification using expert demonstrations, achieving 72.7\% on ALFWorld with Qwen-1.7B. ReflAct uses prompting-based reflection with GPT-4, reaching 93.3\%. These methods treat verification as always-on. ARES proposes adaptive effort allocation using an SFT-trained router with continuous effort levels, achieving 52.7\% token reduction. Our approach differs in using RL rather than SFT for the routing decision, and in using action-change as a direct reward signal rather than heuristic labels.
50	
51	\paragraph{Compute-Adaptive Inference.}
52	Thinkless trains RL control tokens to skip extended reasoning when unnecessary. Our work applies this philosophy to the verification domain in interactive agents, where the binary verify/skip decision has clear behavioral consequences (action change) that provide natural reward signals.
53	
54	\paragraph{Credit Assignment in RL.}
55	The advantage sign misattribution we identify relates to classical credit assignment problems in RL. GAE provides per-token credit via learned value functions. We show that for LLM agent training, correcting the sign (episode-level) captures most of the benefit (+3pp gap to GAE), suggesting that sign correctness is the primary bottleneck rather than per-token credit granularity.
56	
57	\section{Method}
58	
59	\subsection{Problem Setup}
60	
61	We consider an interactive agent operating in a text-based environment over $T$ steps. At each step $t$, the agent observes state $s_t$, generates action $a_t$, and optionally performs self-verification before committing. The episode terminates with binary reward $R \in \{0, 1\}$ (task success/failure).
62	
63	\subsection{Diagnosing Step-Independent Training Failure}
64	
65	In step-independent training, the episode is segmented into windows of $h$ steps, each optimized independently. For a window starting at step $t$, the per-window return is computed as $G_t = \gamma^{(T-t)/h} \cdot R$, and GRPO group normalization yields advantages:
66	\begin{equation}
67	A_t = \frac{G_t - \mu_G}{\sigma_G}
68	\end{equation}
69	where $\mu_G$ and $\sigma_G$ are computed across episodes in the batch.
70	
71	\textbf{Mechanism 1: Information Loss.} With window size $h$, the policy conditions on only $h$ steps of history. For tasks requiring coordinated multi-step strategies (average episode length 25 steps in ALFWorld), small $h$ prevents learning temporal dependencies.
72	
73	\textbf{Mechanism 2: Sign Misattribution.} Because $G_t \propto R$ for all windows within an episode, the sign of $A_t$ after group normalization is determined by whether the episode succeeded or failed, independent of the action quality within window $t$. Formally, for any window in a successful episode, $G_t > 0$; after normalization against a batch containing failures, $A_t > 0$. This means all actions in successful episodes are reinforced and all actions in failed episodes are suppressed, regardless of their local quality.
74	
75	\subsection{Episode-Level GRPO}
76	
77	Episode-level GRPO treats the entire trajectory as a single GRPO sample. All tokens in the episode share a common advantage:
78	\begin{equation}
79	A_{\text{episode}} = \frac{R - \mu_R}{\sigma_R}
80	\end{equation}
81	This eliminates information loss (full history visible) and sign misattribution (no per-window reward decomposition needed). While the per-token credit assignment is coarser than GAE, we show empirically that correcting the advantage sign is the dominant factor.
82	
83	\subsection{Selective Verification via B-IAVR}
84	
85	Given a converged episode-level agent, we train a selective verification policy. At each step, before action execution, the agent produces a binary token: \texttt{[VERIFY]} or \texttt{[SKIP]}.
86	
87	The reward function combines task success with verification informativeness:
88	\begin{equation}
89	r = R_{\text{task}} + \alpha \sum_{t: \text{verified}} \mathbb{1}[\text{action\_changed}_t] - \beta \sum_{t} \mathbb{1}[\text{verified}_t]
90	\end{equation}
91	where $\alpha = 0.3$ rewards informative verifications (those that change the action) and $\beta = 0.1$ penalizes verification cost. The ratio $\alpha/\beta = 3$ sets the break-even action-change probability at $1/3$, calibrated to the observed overall action-change rate of 0.23.
92	
93	Training uses episode-level GRPO, initialized from the converged always-on checkpoint. The selective policy learns to verify at high-uncertainty steps (early in the episode, unfamiliar states) and skip at confident steps (late, routine actions).
94	
95	\section{Experiments}
96	
97	\subsection{Setup}
98	
99	We train Qwen3-1.7B on ALFWorld (134 training tasks, 64 validation tasks) using the RAGEN framework. Episode-level GRPO uses full context windows. Hyperparameters: learning rate $5 \times 10^{-6}$, GRPO group size 4, KL coefficient 0.01. All results report validation success rate unless noted.
100	
101	\subsection{Episode-Level GRPO Convergence}
102	
103	Table~\ref{tab:convergence} shows the training trajectory. The model breaks through an initial plateau at step 25 (when action validity exceeds 70\%) and converges at step 50 with 48\% validation success. The plateau corresponds to the phase where the model learns action syntax; once valid actions exceed 70\%, the episode-level advantage signal becomes informative for strategic learning.
104	
105	\begin{table}[h]
106	\centering
107	\caption{Episode-level GRPO convergence trajectory on ALFWorld.}
108	\label{tab:convergence}
109	\begin{tabular}{cccccc}
110	\toprule
111	Step & Val Success & Action Valid & Train Success & Entropy & KL \\
112	\midrule
113	5  & 0.250 & 0.450 & 0.310 & 0.220 & 0.003 \\
114	10 & 0.250 & 0.500 & 0.380 & 0.190 & 0.005 \\
115	15 & 0.281 & 0.545 & 0.438 & 0.170 & 0.007 \\
116	20 & 0.300 & 0.610 & 0.480 & 0.150 & 0.009 \\
117	25 & 0.330 & 0.680 & 0.500 & 0.140 & 0.010 \\
118	30 & 0.380 & 0.730 & 0.530 & 0.130 & 0.011 \\
119	35 & 0.420 & 0.770 & 0.550 & 0.120 & 0.012 \\
120	40 & 0.450 & 0.800 & 0.570 & 0.120 & 0.012 \\
121	45 & 0.470 & 0.810 & 0.580 & 0.110 & 0.013 \\
122	50 & \textbf{0.480} & 0.820 & 0.580 & 0.110 & 0.013 \\
123	\bottomrule
124	\end{tabular}
125	\end{table}
126	
127	\subsection{Multi-Seed Replication}
128	
129	Five independent seeds confirm reproducibility (Table~\ref{tab:multiseed}). Mean converged success is 46.8\% $\pm$ 2.4\% (95\% CI: [43.8\%, 49.8\%]). All seeds exceed 40\%, and the CI excludes the pre-breakthrough plateau of 28\%.
130	
131	\begin{table}[h]
132	\centering
133	\caption{Multi-seed convergence results (5 seeds, episode-level GRPO).}
134	\label{tab:multiseed}
135	\begin{tabular}{ccccc}
136	\toprule
137	Seed & Converge Step & Val Success & Action Valid & Pass@8 \\
138	\midrule
139	1 & 50 & 0.480 & 0.82 & 0.95 \\
140	2 & 45 & 0.450 & 0.79 & 0.93 \\
141	3 & 42 & 0.500 & 0.84 & 0.96 \\
142	4 & 52 & 0.470 & 0.80 & 0.94 \\
143	5 & 48 & 0.440 & 0.78 & 0.92 \\
144	\midrule
145	Mean$\pm$Std & 47.4$\pm$3.8 & 0.468$\pm$0.024 & 0.81$\pm$0.03 & 0.94$\pm$0.02 \\
146	\bottomrule
147	\end{tabular}
148	\end{table}
149	
150	\subsection{Context Window Ablation (h-Sweep)}
151	
152	Table~\ref{tab:hsweep} presents the critical h-sweep experiment (3 seeds per setting, 15 training steps). A catastrophic cliff appears at $h \leq 5$: all 3 seeds collapse to 0\% (h=2) or near-0\% (h=5). The transition from catastrophic failure to degraded learning occurs between h=5 and h=10. This is not a trivial ``more context is better'' result; the cliff's sharpness and the threshold effect at h=5 reveal the sign misattribution mechanism's non-linear impact.
153	
154	\begin{table}[h]
155	\centering
156	\caption{Context window h-sweep (step 15 validation success, 3 seeds each).}
157	\label{tab:hsweep}
158	\begin{tabular}{ccccccc}
159	\toprule
160	$h$ & Seed 1 & Seed 2 & Seed 3 & Mean & Std & Collapse Step \\
161	\midrule
162	2 & 0.000 & 0.000 & 0.000 & 0.000 & 0.000 & 4.3 \\
163	5 & 0.030 & 0.000 & 0.016 & 0.015 & 0.015 & 7.0 \\
164	10 & 0.078 & 0.110 & 0.063 & 0.084 & 0.024 & N/A \\
165	20 & 0.190 & 0.220 & 0.170 & 0.193 & 0.025 & N/A \\
166	full & 0.280 & 0.250 & 0.310 & \textbf{0.280} & 0.030 & N/A \\
167	\bottomrule
168	\end{tabular}
169	\end{table}
170	
171	\subsection{Empirical Verification of Sign Misattribution}
172	
173	Table~\ref{tab:sign} provides direct evidence of the sign misattribution mechanism. We log per-window advantages from step-independent training and correlate advantage sign with (a) episode outcome and (b) local action quality (proxied by action validity). The correlation between advantage sign and episode outcome is 0.97 ($p < 10^{-100}$), while the correlation with local quality is 0.04 ($p = 0.38$, not significant). In failed episodes, 94\% of good-action windows receive negative advantage; in successful episodes, 92\% of bad-action windows receive positive advantage.
174	
175	\begin{table}[h]
176	\centering
177	\caption{Sign attribution analysis ($n=3200$ windows from 256 episodes).}
178	\label{tab:sign}
179	\begin{tabular}{lccc}
180	\toprule
181	Condition & $n$ windows & Positive Adv \% & Negative Adv \% \\
182	\midrule
183	Success episode, good action & 420 & 0.98 & 0.02 \\
184	Success episode, bad action & 180 & 0.92 & 0.08 \\
185	Failure episode, good action & 850 & 0.03 & 0.97 \\
186	Failure episode, bad action & 1750 & 0.02 & 0.98 \\
187	\bottomrule
188	\end{tabular}
189	\end{table}
190	
191	\begin{table}[h]
192	\centering
193	\caption{Correlation between advantage properties and training signals.}
194	\label{tab:correlation}
195	\begin{tabular}{lccc}
196	\toprule
197	Pair & Correlation & $p$-value & Interpretation \\
198	\midrule
199	Sign $\times$ Episode Outcome & 0.97 & $<10^{-100}$ & Sign determined by outcome \\
200	Sign $\times$ Local Action Quality & 0.04 & 0.38 & Sign independent of local quality \\
201	Magnitude $\times$ Window Position & $-0.89$ & $<10^{-50}$ & $\gamma^k$ decay confirmed \\
202	\bottomrule
203	\end{tabular}
204	\end{table}
205	
206	\subsection{GAE Baseline Comparison}
207	
208	Table~\ref{tab:gae} compares episode-level GRPO against GAE variants and step-independent training. GAE($\lambda=0.95$) achieves 51\% at convergence, 3.2pp above episode-level GRPO (46.8\%). This modest gap confirms that correcting advantage sign is the primary bottleneck: episode-level information (sign correctness) accounts for the majority of improvement over step-independent, while per-token credit refinement via GAE provides secondary gains.
209	
210	\begin{table}[h]
211	\centering
212	\caption{Comparison of credit assignment methods.}
213	\label{tab:gae}
214	\begin{tabular}{lcccc}
215	\toprule
216	Method & Step 15 & Std & Converged & Per-token Adv. Var. \\
217	\midrule
218	Step-independent (h=2) & 0.000 & 0.000 & 0.000 & 0.85 \\
219	Episode-level GRPO & 0.280 & 0.030 & 0.468 & 0.00 \\
220	GAE($\lambda$=1.0, $\gamma$=1.0) & 0.287 & 0.015 & 0.490 & 0.18 \\
221	GAE($\lambda$=0.95, $\gamma$=1.0) & \textbf{0.307} & 0.025 & \textbf{0.510} & 0.42 \\
222	\bottomrule
223	\end{tabular}
224	\end{table}
225	
226	\subsection{Valid Action Bonus Variant}
227	
228	Adding a small valid-action bonus ($+0.05$ per valid action) to episode-level GRPO accelerates plateau breaking (step 12 vs step 25) and improves final success to 52\% (Table~\ref{tab:bonus}). Critically, the same dense reward causes catastrophic reward gaming under step-independent training (action validity reaches 97.5\% but success stays at 0\%), while under episode-level training it safely improves both metrics. This further confirms that the step-independent paradigm, not dense reward itself, is the failure mode.
229	
230	\begin{table}[h]
231	\centering
232	\caption{Episode-level GRPO with and without valid-action bonus.}
233	\label{tab:bonus}
234	\begin{tabular}{ccccc}
235	\toprule
236	Step & Base Success & +Bonus Success & Base Valid & +Bonus Valid \\
237	\midrule
238	5  & 0.250 & 0.300 & 0.450 & 0.550 \\
239	10 & 0.250 & 0.360 & 0.500 & 0.680 \\
240	15 & 0.280 & 0.410 & 0.550 & 0.780 \\
241	20 & 0.300 & 0.470 & 0.610 & 0.840 \\
242	25 & 0.330 & 0.500 & 0.680 & 0.870 \\
243	30 & 0.380 & \textbf{0.520} & 0.730 & 0.880 \\
244	\bottomrule
245	\end{tabular}
246	\end{table}
247	
248	\subsection{Selective Verification Results}
249	
250	\subsubsection{Action-Change Statistics}
251	
252	From the converged always-on agent (320 episodes, 7840 verification steps), 77\% of verifications are confirmatory (no action change). The action-change rate is higher in early steps (0.31) than late steps (0.17), reflecting decreasing uncertainty as episodes progress. Action changes correlate positively with task success (partial $r = 0.31$, $p = 0.003$ after controlling for policy entropy), confirming that action-change is a meaningful signal of verification informativeness rather than noise.
253	
254	\begin{table}[h]
255	\centering
256	\caption{Action-change rate by episode position and entropy stratum.}
257	\label{tab:actionchange}
258	\begin{tabular}{lcccc}
259	\toprule
260	Category & Change Rate & $n$ Steps & Corr. w/ Success & $p$-value \\
261	\midrule
262	Overall & 0.230 & 7840 & 0.28 & -- \\
263	Early (steps 1--8) & 0.310 & 2560 & 0.32 & -- \\
264	Mid (steps 9--16) & 0.220 & 2560 & 0.27 & -- \\
265	Late (steps 17--25) & 0.170 & 2720 & 0.21 & -- \\
266	\midrule
267	Low entropy ($<$0.1) & 0.140 & 105 ep. & 0.25 & 0.020 \\
268	Mid entropy (0.1--0.25) & 0.240 & 120 ep. & 0.33 & 0.005 \\
269	High entropy ($>$0.25) & 0.340 & 95 ep. & 0.29 & 0.010 \\
270	Partial (entropy-controlled) & 0.230 & 320 ep. & \textbf{0.31} & 0.003 \\
271	\bottomrule
272	\end{tabular}
273	\end{table}
274	
275	\subsubsection{Causal Intervention}
276	
277	To confirm that action-change captures verification value causally (not merely correlatively), we compare verification-triggered changes against random action replacement at matched rate (Table~\ref{tab:causal}). Verification-triggered changes achieve 48\% success, while random changes at the same 23\% rate yield only 35\% (below the 37\% no-verification baseline). The 13pp gap demonstrates that verification-triggered changes reflect informed correction, not arbitrary perturbation.
278	
279	\begin{table}[h]
280	\centering
281	\caption{Causal intervention: verification-triggered vs random action changes.}
282	\label{tab:causal}
283	\begin{tabular}{lccc}
284	\toprule
285	Condition & Success & Change Rate & $\Delta$ vs No-Change \\
286	\midrule
287	Verification-triggered & 0.480 & 0.23 & +11pp \\
288	Random at matched rate & 0.350 & 0.23 & $-$2pp \\
289	No change (no verification) & 0.370 & 0.00 & baseline \\
290	\bottomrule
291	\end{tabular}
292	\end{table}
293	
294	\subsubsection{B-IAVR Training and Comparison}
295	
296	Table~\ref{tab:biavr} presents the full comparison. B-IAVR achieves 46.5\% success at 48\% verification rate (62\% relative cost), yielding the highest success-per-cost ratio of 0.75. Compared to always-on verification (48\% success, 100\% cost), B-IAVR trades 1.5pp success for 38\% cost reduction. The learned policy verifies more at early steps (72\%) and less at late steps (28\%), matching the ground-truth action-change distribution. When B-IAVR does verify, 41\% of verifications change the action (vs 23\% for always-on), confirming that the model learned to verify selectively at informative decision points.
297	
298	\begin{table}[h]
299	\centering
300	\caption{Selective verification methods comparison.}
301	\label{tab:biavr}
302	\begin{tabular}{lcccc}
303	\toprule
304	Method & Success & Verify Rate & Relative Cost & Success/Cost \\
305	\midrule
306	Always-on & 0.480 & 1.00 & 1.00 & 0.48 \\
307	\textbf{B-IAVR (ours)} & \underline{0.465} & 0.48 & 0.62 & \textbf{0.75} \\
308	Confidence-threshold & 0.440 & 0.55 & 0.67 & 0.66 \\
309	Random-0.5 & 0.430 & 0.50 & 0.63 & 0.68 \\
310	No-verify & 0.370 & 0.00 & 0.52 & 0.71 \\
311	\bottomrule
312	\end{tabular}
313	\end{table}
314	
315	\subsubsection{Reward Signal Ablation}
316	
317	Table~\ref{tab:reward_ablation} ablates the reward signal for selective verification training. Action-change reward produces the best Pareto point. Confidence-based reward (using token entropy as verification trigger) underperforms because low entropy does not reliably indicate correct actions. Random-trigger reward lacks informative gradient for distinguishing useful from wasteful verification.
318	
319	\begin{table}[h]
320	\centering
321	\caption{Reward signal ablation for selective verification.}
322	\label{tab:reward_ablation}
323	\begin{tabular}{lcccc}
324	\toprule
325	Reward Signal & Success & Verify Rate & Cost & Success/Cost \\
326	\midrule
327	Action-change (ours) & \textbf{0.465} & 0.48 & 0.62 & \textbf{0.75} \\
328	Confidence-based & 0.440 & 0.53 & 0.65 & 0.68 \\
329	Random trigger & 0.420 & 0.51 & 0.64 & 0.66 \\
330	\bottomrule
331	\end{tabular}
332	\end{table}
333	
334	\subsubsection{Comparison with ARES}
335	
336	We reproduce ARES (SFT router with continuous effort allocation) on the same model and environment (Table~\ref{tab:ares}). B-IAVR achieves +3.5pp higher success at 10pp lower cost. ARES's SFT router is more conservative (60\% verify rate) because its training data biases toward ``verify when in doubt,'' leading to over-verification without commensurate success gains.
337	
338	\begin{table}[h]
339	\centering
340	\caption{Head-to-head comparison with ARES.}
341	\label{tab:ares}
342	\begin{tabular}{lcccc}
343	\toprule
344	Method & Success & Verify Rate & Relative Cost & Approach \\
345	\midrule
346	B-IAVR (ours) & \textbf{0.465} & 0.48 & \textbf{0.62} & RL, action-change reward \\
347	ARES (reproduced) & 0.430 & 0.60 & 0.72 & SFT router \\
348	Always-on & 0.480 & 1.00 & 1.00 & No selection \\
349	\bottomrule
350	\end{tabular}
351	\end{table}
352	
353	\subsection{Generalization}
354	
355	\subsubsection{Cross-Environment Transfer}
356	
357	Table~\ref{tab:transfer} validates the dual-mechanism finding on ScienceWorld. Episode-level GRPO achieves 32\% vs 8\% for step-independent (4$\times$ improvement). ScienceWorld's longer episodes (avg 35 steps) and larger action space make training harder overall, but the relative advantage of episode-level training is consistent.
358	
359	\begin{table}[h]
360	\centering
361	\caption{Cross-environment validation.}
362	\label{tab:transfer}
363	\begin{tabular}{lcccc}
364	\toprule
365	Environment & Episode-level & Step-independent & Ratio & Avg Steps \\
366	\midrule
367	ALFWorld & 0.480 & 0.000 & $\infty$ & 25 \\
368	ScienceWorld & 0.320 & 0.080 & 4.0$\times$ & 35 \\
369	\bottomrule
370	\end{tabular}
371	\end{table}
372	
373	\subsubsection{Model Scaling}
374	
375	Table~\ref{tab:scaling} shows results with Qwen3-7B. Episode-level GRPO reaches 58\% (vs 48\% at 1.7B, +10pp from stronger instruction following and larger capacity). Step-independent with 7B achieves only 5\%, confirming that the dual-mechanism failure is an algorithmic problem that model scale does not resolve.
376	
377	\begin{table}[h]
378	\centering
379	\caption{Model size scaling.}
380	\label{tab:scaling}
381	\begin{tabular}{lccc}
382	\toprule
383	Model & Episode-level & Step-independent & Ratio \\
384	\midrule
385	Qwen3-1.7B & 0.480 & 0.000 & $\infty$ \\
386	Qwen3-7B & \textbf{0.580} & 0.050 & 11.6$\times$ \\
387	\bottomrule
388	\end{tabular}
389	\end{table}
390	
391	\subsection{Per-Task Analysis}
392	
393	Table~\ref{tab:pertask} breaks down performance by ALFWorld task type. Success correlates strongly with task complexity (episode length; $r = -0.92$). Simpler tasks (pick, 18 steps) reach 58\%, while complex tasks (pick\_two, 32 steps) reach 33\%. Step-independent training collapses entirely on tasks requiring more than 20 steps, confirming the dual-mechanism's severity scales with horizon length.
394	
395	\begin{table}[h]
396	\centering
397	\caption{Per-task-type breakdown (episode-level GRPO, converged).}
398	\label{tab:pertask}
399	\begin{tabular}{lcccc}
400	\toprule
401	Task Type & $n$ Tasks & Success & Avg Steps & Step-indep. (est.) \\
402	\midrule
403	pick & 22 & \textbf{0.580} & 18 & 0.10 \\
404	clean & 18 & 0.520 & 22 & 0.03 \\
405	heat & 15 & 0.480 & 24 & 0.00 \\
406	cool & 14 & 0.450 & 25 & 0.00 \\
407	examine & 10 & 0.400 & 28 & 0.00 \\
408	pick\_two & 12 & 0.330 & 32 & 0.00 \\
409	\bottomrule
410	\end{tabular}
411	\end{table}
412	
413	\section{Discussion}
414	
415	\paragraph{Why does the community default to step-independent training?}
416	Three factors explain this: (1) LLM context window limitations historically forced windowed processing; (2) token-level training (SFT, RLHF) established the convention of per-segment optimization; (3) framework implementations (RAGEN) made step-independent the path of least resistance. Our results suggest this default should be reconsidered for multi-turn agent training.
417	
418	\paragraph{Relationship to GAE.}
419	GAE provides finer-grained credit (per-token) via learned value functions and achieves +3.2pp over episode-level GRPO at convergence. However, episode-level GRPO requires no critic, no value function training, and achieves 92\% of GAE's performance. For practitioners, episode-level GRPO is a simple configuration change in existing frameworks.
420	
421	\paragraph{Limitations.}
422	Our evaluation uses two text-based environments (ALFWorld, ScienceWorld). The selective verification results apply to binary verify/skip decisions; extending to continuous effort allocation remains future work. The absolute performance (48\%) leaves a gap to methods using expert demonstrations (Self-Guide, 72.7\%), reflecting the from-scratch RL vs expert-guided paradigm difference.
423	
424	\section{Conclusion}
425	
426	We identified a dual mechanism (policy information loss and advantage sign misattribution) causing catastrophic failure of step-independent RL training for multi-turn LLM agents. Episode-level GRPO resolves both issues, enabling reliable training (46.8\% $\pm$ 2.4\%, 5 seeds). Building on this foundation, B-IAVR learns selective verification using action-change as an intrinsic reward, reducing verification cost by 52\% with minimal performance loss (1.5pp). The success-per-cost ratio of 0.75 represents the best efficiency among all compared methods. These results demonstrate that learning \emph{when} to verify is both feasible and practical for interactive agents operating under computational constraints.
427	
428	\bibliographystyle{plain}
429	\begin{thebibliography}{10}
430	
431	\bibitem{ragen2025}
432	RAGEN: Training agents with GRPO for multi-turn interactive tasks. 2025.
433	
434	\bibitem{selfguide2026}
435	Self-Guide: Self-verification training for interactive LLM agents via expert demonstrations. 2026.
436	
437	\bibitem{ares2026}
438	ARES: Adaptive reasoning effort scheduling with continuous compute allocation. arXiv:2603.07915, 2026.
439	
440	\bibitem{thinkless2025}
441	Thinkless: RL-trained control tokens for adaptive reasoning depth. NeurIPS, 2025.
442	
443	\bibitem{reflact2025}
444	ReflAct: Prompting-based reflection for LLM agents. EMNLP, 2025.
445	
446	\bibitem{grpo2024}
447	DeepSeekMath: Group relative policy optimization for mathematical reasoning. 2024.
448	
449	\bibitem{alfworld2021}
450	ALFWorld: Aligning text and embodied environments for interactive learning. ICLR, 2021.
451	
452	\bibitem{scienceworld2022}
453	ScienceWorld: Is your agent smarter than a 5th grader? EMNLP, 2022.
454	
455	\bibitem{gae2016}
456	Schulman et al. High-dimensional continuous control using generalized advantage estimation. ICLR, 2016.
457	
458	\bibitem{qwen2024}
459	Qwen2.5 technical report. 2024.
460	
461	\end{thebibliography}
462	
463	\end{document}
464	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "676cccaf-272a-45c4-829d-f800ae83ff63",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "a5b02fdfddc805fc8",
  "type": "user",
  "uuid": "4c269478-0385-4d18-b231-982e2efefa4d",
  "sourceToolAssistantUUID": "676cccaf-272a-45c4-829d-f800ae83ff63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T12:55:36.893Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E84PjeLFN5AuiXzyoEP9j1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260517T121256/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c269478-0385-4d18-b231-982e2efefa4d",
  "isSidechain": true,
  "agentId": "a5b02fdfddc805fc8",
  "requestId": "req_011Cb8BCrw62dAwU9ic5pajW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65757622-1eda-4b04-b1ab-538dc754ee71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WK4rzJEf186JXyMp7DF5Vp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4609,
      "cache_read_input_tokens": 23236,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4609
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 23236,
          "cache_creation_input_tokens": 4609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4609,
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

_source line 20 · 2026-05-17T12:55:37.404Z_

<details><summary>↩ Tool result · `toolu_01E84PjeLFN5AuiXzyoEP9j1`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[margin=1in]{geometry}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{hyperref}
9	\usepackage{xcolor}
10	\usepackage{enumitem}
11	
12	\title{Diagnosing Step-Independent RL Failure in Multi-Turn LLM Agents:\\Sign Misattribution, Information Loss, and Selective Verification}
13	
14	\author{Anonymous}
15	\date{}
16	
17	\begin{document}
18	\maketitle
19	
20	\begin{abstract}
21	Training Large Language Model (LLM) agents with Reinforcement Learning (RL) for multi-turn interactive tasks remains challenging. We identify a dual failure mechanism in the widely adopted step-independent training paradigm: (1) policy information loss from truncated context windows prevents learning cross-step strategies, and (2) advantage sign misattribution causes per-window gradients to reflect episode outcomes rather than local action quality, with correlation $r=0.87$ between advantage sign and episode success. Through systematic ablation across context window sizes, we demonstrate a severe degradation zone below $h=5$ steps (success collapses from 18\% to 2\%) and show that episode-level GRPO eliminates both failure modes, achieving 30.6$\pm$5.9\% success versus 3$\pm$2\% for step-independent training on ALFWorld. We position episode-level training as a minimum viable fix rather than an optimal solution: GAE-based credit assignment further improves performance by 8 percentage points, confirming that finer-grained credit has additional value. As a preliminary downstream application, we train a selective verification policy using action-change as an intrinsic reward signal, achieving 28\% cost reduction with a modest 4 percentage point performance trade-off. Our diagnostic analysis generalizes across environments (ScienceWorld, 4.5$\times$ improvement) and model scales (1.7B to 7B parameters).
22	\end{abstract}
23	
24	\section{Introduction}
25	
26	LLM-based interactive agents that operate over multiple turns in grounded environments have become a central research direction. Training these agents with RL promises to improve their task completion without relying on expert demonstrations. However, the default training paradigm adopted by recent agent RL frameworks processes each episode as independent fixed-length windows of $h$ steps, optimizing each window separately with its own advantage estimate.
27	
28	This step-independent paradigm originates from practical constraints: transformer context windows are finite, and token-level training infrastructure naturally segments long trajectories. Yet its consequences for multi-turn agent training have not been systematically examined. We find that step-independent training catastrophically fails on tasks requiring more than a few coordinated decisions.
29	
30	We diagnose two mechanisms driving this failure. First, policy information loss: a window of $h$ steps cannot represent cross-step strategies such as ``explore drawer 1, then navigate to countertop.'' Second, and more critically, advantage sign misattribution: in step-independent training with discounted returns, the sign of each window's advantage is predominantly determined by overall episode success ($r=0.87$ with outcome) rather than local action quality ($r=0.12$). Good actions in failed episodes receive negative advantages and are suppressed; poor actions in successful episodes receive positive advantages and are reinforced.
31	
32	Episode-level training, where the entire trajectory is treated as a single GRPO sample with shared advantage, eliminates both pathologies. All tokens receive the same advantage sign (no cross-window misattribution), and the full episode context is available to the policy. We emphasize that this is a minimum viable fix: it resolves the sign problem but still assigns uniform credit across all tokens. GAE with a learned critic provides finer per-token credit and outperforms episode-level GRPO by 8 percentage points, confirming room for improvement.
33	
34	Building on the diagnostic foundation, we explore a preliminary application: training the agent to selectively verify its actions rather than always verifying. We use action-change rate (whether verification leads to a behavioral change) as an intrinsic reward signal for verification informativeness. The resulting policy reduces verification cost by 28\% with a 4 percentage point performance trade-off relative to always-on verification.
35	
36	Our contributions are:
37	\begin{itemize}[nosep]
38	\item A systematic diagnosis of dual failure mechanisms (sign misattribution + information loss) in step-independent RL for multi-turn LLM agents, supported by mechanistic measurements and controlled ablations.
39	\item Empirical characterization of the degradation boundary (context window $h$-sweep) and demonstration that episode-level GRPO serves as a zero-engineering-cost fix, with GAE providing an upper bound.
40	\item Preliminary evidence that learned selective verification, trained via action-change reward on top of episode-level agents, can reduce verification cost while maintaining most task performance.
41	\item Generalization evidence across environments (ALFWorld, ScienceWorld) and model scales (1.7B, 7B).
42	\end{itemize}
43	
44	\section{Related Work}
45	
46	\paragraph{RL for LLM Agents.}
47	RAGEN introduced GRPO-based training for interactive LLM agents, using a step-independent paradigm where episodes are segmented into fixed-length windows. DeepSeek-R1 and related work apply GRPO to single-turn reasoning tasks where the step-independent issue does not arise. Our work identifies why extending these methods to multi-turn settings fails and provides a diagnostic framework rather than a new algorithm.
48	
49	\paragraph{Credit Assignment in Long-Horizon RL.}
50	The tension between episode-level and step-level credit assignment is well-studied in classical RL. GAE provides a principled interpolation via the $\lambda$ parameter. In LLM agent training, this tension manifests differently because GRPO is inherently bandit-style (no explicit temporal discount), yet framework implementations introduce $\gamma$-discounted per-window returns. We connect this implementation detail to the observed sign misattribution.
51	
52	\paragraph{Self-Verification in LLM Agents.}
53	Self-Guide trains verification as an always-on capability, achieving strong results but at full computational cost. ARES learns when to allocate verification effort using an SFT-trained router with oracle supervision. Thinkless uses RL-trained control tokens to decide when to ``think'' during inference. Our selective verification approach is closest to Thinkless in methodology (RL-based decision) but targets multi-turn action verification rather than single-turn reasoning, and uses action-change as a self-supervised reward signal rather than requiring oracle labels.
54	
55	\paragraph{ALFWorld and Interactive Benchmarks.}
56	ALFWorld provides text-based household tasks requiring multi-step planning. ReflAct achieves 93.3\% with GPT-4 prompting; Self-Guide reaches 72.7\% with a 1.7B model using SFT plus always-on verification. Our focus is not on maximizing ALFWorld performance but on using it as a diagnostic testbed for understanding RL training dynamics.
57	
58	\section{Method}
59	
60	\subsection{Problem Setup}
61	
62	We consider an LLM agent interacting with a text-based environment over $T$ steps. At each step $t$, the agent observes state $s_t$ (textual description) and produces action $a_t$. A binary reward $R \in \{0, 1\}$ is given at episode termination.
63	
64	\subsection{Diagnosing Step-Independent Failure}
65	
66	\paragraph{Step-Independent Training.}
67	In the step-independent paradigm, an episode of $T$ steps is divided into $\lceil T/h \rceil$ windows of size $h$. Each window $w_i$ is treated as an independent GRPO sample with its own advantage:
68	\begin{equation}
69	A_{w_i} = \frac{R_{w_i} - \mu_{\text{group}}}{\sigma_{\text{group}}}
70	\end{equation}
71	where $R_{w_i}$ is computed using $\gamma$-discounted returns from the episode reward allocated to window $i$.
72	
73	\paragraph{Mechanism 1: Policy Information Loss.}
74	With context window $h$, the policy at window $w_i$ observes only $(s_{ih}, a_{ih}, \ldots, s_{(i+1)h-1})$. Cross-window strategies (e.g., ``object found in drawer 1 at step 3, navigate to countertop at step 12'') cannot be represented. This is a hard architectural limitation.
75	
76	\paragraph{Mechanism 2: Advantage Sign Misattribution.}
77	The discounted return for window $w_i$ in a $T$-step episode is $R_{w_i} = \gamma^{T - ih} \cdot R$, where $R$ is the terminal reward. After GRPO group normalization, the sign of $A_{w_i}$ is determined by whether $R_{w_i}$ exceeds the group mean. Since all windows in the same episode share the same terminal reward $R$, their advantages correlate with episode outcome, not with window-local action quality.
78	
79	Empirically, we measure the correlation between advantage sign and episode outcome at $r=0.87$, versus $r=0.12$ between advantage sign and local action quality. The gradient direction (reinforce or suppress) is overwhelmingly determined by whether the episode succeeded.
80	
81	\paragraph{Episode-Level Resolution.}
82	Episode-level GRPO treats the entire $T$-step trajectory as a single sample. All tokens share one advantage:
83	\begin{equation}
84	A_{\text{episode}} = \frac{R - \mu_{\text{group}}}{\sigma_{\text{group}}}
85	\end{equation}
86	This eliminates cross-window sign misattribution (sign variance across windows becomes 0) and provides the full episode context to the policy (resolving information loss). The trade-off is uniform credit: all tokens receive identical gradient magnitude regardless of their individual contribution.
87	
88	\subsection{GAE as Upper Bound}
89	
90	Generalized Advantage Estimation with a learned critic provides per-token credit assignment:
91	\begin{equation}
92	\hat{A}_t^{\text{GAE}} = \sum_{l=0}^{T-t-1} (\gamma\lambda)^l \delta_{t+l}, \quad \delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)
93	\end{equation}
94	This requires training a separate critic network, adding engineering complexity. We include GAE($\lambda=0.95$) and GAE($\lambda=1.0$) as reference points to characterize how much performance episode-level GRPO leaves on the table.
95	
96	\subsection{Selective Verification via Action-Change Reward}
97	
98	Given an episode-level trained agent with self-verification capability, we train a selective policy that decides at each step whether to invoke verification.
99	
100	\paragraph{Action-Change as Informativeness Proxy.}
101	We define verification as ``informative'' if it leads to a behavioral change (the agent modifies its next action after re-examining the situation). We use action-change rate as an intrinsic reward signal for the selective verification policy, following the Budget-constrained Informative Action Verification with RL (B-IAVR) formulation. The selective policy receives positive reward when it chooses to verify and verification triggers an action change, and when it skips verification at steps where verification would have been confirmatory.
102	
103	\section{Experiments}
104	
105	All experiments use Qwen3-1.7B as the base model on ALFWorld unless otherwise noted. Training uses GRPO with group size 8. We report validation success rate averaged across task types.
106	
107	\subsection{Context Window Degradation (h-Sweep)}
108	
109	We sweep $h \in \{2, 5, 10, 20, \text{full}\}$ with 3 seeds each, training for 15 steps.
110	
111	\begin{table}[h]
112	\centering
113	\caption{Context window ablation. Success rate (\%) at step 15, 3 seeds per setting.}
114	\label{tab:hsweep}
115	\begin{tabular}{lccccc}
116	\toprule
117	$h$ & Seed 1 & Seed 2 & Seed 3 & Mean$\pm$Std & Collapse \\
118	\midrule
119	2 & 0 & 4 & 3 & 2.3$\pm$2.1 & 2/3 by step 5 \\
120	5 & 12 & 6 & 5 & 7.7$\pm$3.8 & 1/3 partial \\
121	10 & 22 & 14 & 19 & 18.3$\pm$4.0 & 0/3 \\
122	20 & 32 & 24 & 28 & 28.0$\pm$4.0 & 0/3 \\
123	full & 38 & 30 & 34 & 34.0$\pm$4.0 & 0/3 \\
124	\bottomrule
125	\end{tabular}
126	\end{table}
127	
128	There is a severe degradation zone between $h=2$ and $h=5$: at $h=2$, two out of three seeds collapse entirely by step 5 (policy degenerates to repetitive invalid actions). The transition is not a clean binary cliff but rather a zone of instability where shorter episodes (e.g., simple pick tasks completing in 10 steps) partially survive while longer episodes (examine tasks requiring 30+ steps) fail consistently. The sharp drop from $h=10$ (18.3\%) to $h=5$ (7.7\%) to $h=2$ (2.3\%) confirms that both mechanisms worsen as context shrinks: less information is available and sign misattribution becomes more severe as $\gamma^k$ decay increases across more windows.
129	
130	\subsection{Mechanistic Verification}
131	
132	We directly measure the credit assignment mechanism by logging per-window advantages from $h=2$ runs.
133	
134	\begin{table}[h]
135	\centering
136	\caption{Empirical verification of sign misattribution mechanism.}
137	\label{tab:mechanism}
138	\begin{tabular}{lccc}
139	\toprule
140	Metric & Observed & Theory & Interpretation \\
141	\midrule
142	sign $\leftrightarrow$ outcome $r$ & 0.87 & $\sim$1.0 & Direction mostly correct \\
143	sign $\leftrightarrow$ local quality $r$ & 0.12 & $\sim$0.0 & Weak confound, not causal \\
144	$\gamma^k$ decay $R^2$ & 0.75 & high & Moderate position-magnitude fit \\
145	Episode-level sign variance & 0.0 & 0.0 & No misattribution (by design) \\
146	Success $\rightarrow$ all positive & 92\% & 100\% & GRPO norm creates exceptions \\
147	Failure $\rightarrow$ all negative & 89\% & 100\% & Same GRPO norm effect \\
148	\bottomrule
149	\end{tabular}
150	\end{table}
151	
152	The sign-outcome correlation of 0.87 (versus 0.12 for sign-local quality) confirms that advantage sign is predominantly determined by episode outcome rather than window-local action quality. The deviation from the theoretical maximum of 1.0 arises from GRPO group normalization: when multiple success episodes appear in the same group, relative ranking can assign negative advantages to some successful trajectories. In 92\% of successful episodes, all windows receive positive advantage; in 89\% of failed episodes, all windows receive negative advantage. Episode-level training eliminates this entirely (sign variance = 0 by construction).
153	
154	\subsection{Multi-Seed Replication}
155	
156	We run 5 seeds with episode-level GRPO for 15 training steps.
157	
158	\begin{table}[h]
159	\centering
160	\caption{Episode-level GRPO across 5 seeds at step 15.}
161	\label{tab:multiseed}
162	\begin{tabular}{lcccc}
163	\toprule
164	Seed & Val Success & Train Success & Action Valid & Pass@8 \\
165	\midrule
166	1 & 28.1\% & 43.8\% & 54.5\% & 92.9\% \\
167	2 & 34.4\% & 50.0\% & 61.2\% & 95.3\% \\
168	3 & 37.5\% & 53.1\% & 63.8\% & 96.1\% \\
169	4 & 31.3\% & 46.9\% & 58.7\% & 93.8\% \\
170	5 & 21.9\% & 34.4\% & 48.2\% & 87.5\% \\
171	\midrule
172	Mean$\pm$Std & 30.6$\pm$5.9\% & 45.6$\pm$7.1\% & 57.3$\pm$6.1\% & 93.1$\pm$3.4\% \\
173	\bottomrule
174	\end{tabular}
175	\end{table}
176	
177	The mean of 30.6\% with standard deviation 5.9 percentage points reflects moderate variance across seeds. One seed (seed 5, 21.9\%) underperforms due to sensitivity to initial rollout task distribution. The 95\% confidence interval is [25.3\%, 35.9\%]. All seeds substantially outperform the step-independent baseline (3$\pm$2\%), confirming that episode-level training consistently works, though absolute performance remains moderate for a 1.7B model on ALFWorld.
178	
179	\subsection{GAE Baseline Comparison}
180	
181	\begin{table}[h]
182	\centering
183	\caption{Training method comparison at step 15 (3 seeds).}
184	\label{tab:gae}
185	\begin{tabular}{lccc}
186	\toprule
187	Method & Val Success & Std & $\Delta$ vs Step-Ind \\
188	\midrule
189	Step-independent ($h$=2) & 3$\pm$2\% & 2pp & baseline \\
190	Step-independent ($h$=10) & 18$\pm$4\% & 4pp & +15pp \\
191	Episode-level GRPO & 32$\pm$5\% & 5pp & +29pp \\
192	GAE ($\lambda$=1.0, $\gamma$=1.0) & 37$\pm$4\% & 4pp & +34pp \\
193	GAE ($\lambda$=0.95, $\gamma$=1.0) & 40$\pm$5\% & 5pp & +37pp \\
194	\bottomrule
195	\end{tabular}
196	\end{table}
197	
198	GAE($\lambda$=0.95) outperforms episode-level GRPO by 8 percentage points, confirming that per-token credit assignment via a learned critic provides additional value beyond eliminating sign misattribution. GAE($\lambda$=1.0) approximates Monte Carlo returns with variance reduction and achieves an intermediate 37\%. We position episode-level GRPO as the zero-engineering-cost fix (no critic network needed) while acknowledging GAE as the superior but more complex alternative. Both methods dramatically outperform step-independent training, confirming that the dual failure mechanism is the primary bottleneck rather than credit granularity.
199	
200	\subsection{Valid Action Bonus}
201	
202	Adding a small dense reward for valid actions (bonus=0.05) to episode-level training:
203	
204	\begin{table}[h]
205	\centering
206	\caption{Effect of valid action bonus on episode-level training.}
207	\label{tab:bonus}
208	\begin{tabular}{lccc}
209	\toprule
210	Metric & Vanilla & +Bonus & Delta \\
211	\midrule
212	Val success & 30.6\% & 34.4\% & +3.8pp \\
213	Action valid & 57.3\% & 72.1\% & +14.8pp \\
214	Reward mean & 3.06 & 4.12 & +1.06 \\
215	Gaming detected & No & No & -- \\
216	\bottomrule
217	\end{tabular}
218	\end{table}
219	
220	The bonus substantially improves action validity (+14.8pp) with a modest success improvement (+3.8pp). No reward gaming is observed, unlike step-independent training where per-window optimization can independently maximize the bonus while ignoring task completion. This confirms that dense reward gaming is specific to step-independent training, not episode-level. However, the limited success improvement indicates that valid actions are necessary but not sufficient; the remaining performance gap stems from exploration strategy rather than format errors.
221	
222	\subsection{Per-Task Analysis}
223	
224	\begin{table}[h]
225	\centering
226	\caption{Per-task breakdown for episode-level training at step 15.}
227	\label{tab:pertask}
228	\begin{tabular}{lcccc}
229	\toprule
230	Task Type & Success & Avg Steps & Action Valid & $n$ \\
231	\midrule
232	put & 40\% & 12.3 & 62\% & 10 \\
233	clean & 32\% & 18.7 & 55\% & 6 \\
234	cool & 30\% & 16.2 & 58\% & 4 \\
235	heat & 28\% & 17.8 & 53\% & 4 \\
236	examine & 18\% & 24.5 & 48\% & 3 \\
237	pick\_two & 15\% & 28.1 & 45\% & 5 \\
238	\bottomrule
239	\end{tabular}
240	\end{table}
241	
242	Success correlates negatively with average episode length ($r=-0.72$). Simple tasks (put, 12 steps average) achieve 40\% while complex multi-step tasks (examine, pick\_two) remain below 20\%. Even with episode-level credit, longer trajectories dilute the reward signal more, and tasks requiring multiple sequential correct decisions compound error rates. This identifies a clear limitation: episode-level credit is uniform across all tokens, providing less learning signal per-token in longer episodes.
243	
244	\subsection{Generalization: ScienceWorld Transfer}
245	
246	\begin{table}[h]
247	\centering
248	\caption{Transfer to ScienceWorld environment.}
249	\label{tab:sciworld}
250	\begin{tabular}{lcc}
251	\toprule
252	Method & Success & Improvement \\
253	\midrule
254	Step-independent ($h$=2) & 4\% & baseline \\
255	Step-independent ($h$=10) & 9\% & 2.3$\times$ \\
256	Episode-level GRPO & 18\% & 4.5$\times$ \\
257	\bottomrule
258	\end{tabular}
259	\end{table}
260	
261	The dual failure mechanism reproduces on ScienceWorld: step-independent training collapses to 4\% while episode-level achieves 18\% (4.5$\times$ improvement). The lower absolute numbers (18\% versus 30.6\% on ALFWorld) reflect ScienceWorld's greater complexity (longer episodes, larger action space, science reasoning requirements). Convergence is slower (25 steps to plateau versus 10--15 on ALFWorld). The consistent pattern across environments supports the generality of our diagnostic findings.
262	
263	\subsection{Generalization: Model Scale}
264	
265	\begin{table}[h]
266	\centering
267	\caption{Model scaling: Qwen3-1.7B vs Qwen3-7B.}
268	\label{tab:scale}
269	\begin{tabular}{lccc}
270	\toprule
271	Model & Episode-Level & Step-Ind ($h$=2) & Ratio \\
272	\midrule
273	Qwen3-1.7B & 32\% & 3\% & 10.7$\times$ \\
274	Qwen3-7B & 42\% & 8\% & 5.3$\times$ \\
275	\bottomrule
276	\end{tabular}
277	\end{table}
278	
279	Scaling to 7B parameters improves episode-level performance (32\% to 42\%) but does not rescue step-independent training (3\% to 8\%). The structural failure of step-independent training cannot be compensated by model capacity alone. The 7B model's marginally higher step-independent performance (8\% versus 3\%) reflects better local decision-making within each window, but sign misattribution still prevents meaningful policy improvement. The absolute gap between methods grows with scale (29pp at 1.7B, 34pp at 7B), suggesting the diagnostic findings become more relevant, not less, as models scale.
280	
281	\subsection{Selective Verification: Action-Change Statistics}
282	
283	Before training selective verification, we characterize verification behavior in the always-on episode-level agent.
284	
285	\begin{table}[h]
286	\centering
287	\caption{Action-change statistics by task type.}
288	\label{tab:actionchange}
289	\begin{tabular}{lccc}
290	\toprule
291	Task & Change Rate & Change$\rightarrow$Success & No Change$\rightarrow$Success \\
292	\midrule
293	put & 22\% & 35\% & 28\% \\
294	clean & 31\% & 30\% & 25\% \\
295	heat & 35\% & 33\% & 22\% \\
296	cool & 30\% & 32\% & 24\% \\
297	examine & 38\% & 28\% & 18\% \\
298	overall & 28\% & 32\% & 25\% \\
299	\bottomrule
300	\end{tabular}
301	\end{table}
302	
303	72\% of verification steps are confirmatory (no behavioral change). Steps with action changes have moderately higher success rates (32\% versus 25\% overall), but the correlation between action-change and success is weak ($r=0.15$). Complex tasks (examine, heat) show higher change rates, reflecting greater uncertainty in larger action spaces.
304	
305	\paragraph{Entropy-Controlled Analysis.}
306	After controlling for policy entropy (a confounder, since high-entropy states naturally produce more action changes), partial correlation drops from 0.15 to 0.11 ($p=0.038$). The signal persists but is weak. Stratified analysis shows stronger correlation in low-entropy states ($r=0.14$) where action changes are more likely to be informed corrections rather than noise.
307	
308	\paragraph{Causal Intervention.}
309	To verify that verification-triggered changes provide genuine value beyond random exploration:
310	
311	\begin{table}[h]
312	\centering
313	\caption{Causal intervention: verification-triggered vs random action changes.}
314	\label{tab:causal}
315	\begin{tabular}{lcc}
316	\toprule
317	Condition & Success & vs Baseline \\
318	\midrule
319	Verification-triggered change & 32\% & +4pp \\
320	No change (baseline) & 28\% & -- \\
321	Random change (matched rate) & 24\% & $-$4pp \\
322	\bottomrule
323	\end{tabular}
324	\end{table}
325	
326	Verification-triggered changes outperform both the no-change baseline (+4pp) and random changes (+8pp). Random changes actively hurt performance ($-$4pp), confirming that verification provides genuinely informative corrections rather than merely increasing exploration. This provides causal justification for using action-change as a reward signal, though the effect size is moderate.
327	
328	\subsection{B-IAVR Selective Verification Training}
329	
330	We train a selective verification policy using episode-level GRPO with action-change reward.
331	
332	\begin{table}[h]
333	\centering
334	\caption{B-IAVR training trajectory.}
335	\label{tab:biavr}
336	\begin{tabular}{lccc}
337	\toprule
338	Step & Success & Verify Rate & Relative Cost \\
339	\midrule
340	0 & 30\% & 100\% & 1.00$\times$ \\
341	10 & 28\% & 85\% & 0.88$\times$ \\
342	20 & 26\% & 74\% & 0.78$\times$ \\
343	30 & 27\% & 70\% & 0.74$\times$ \\
344	40 & 27\% & 68\% & 0.72$\times$ \\
345	\bottomrule
346	\end{tabular}
347	\end{table}
348	
349	The policy converges to 68\% verification rate (32\% reduction) with a noisy plateau after step 25. Success drops 3--5 percentage points from the always-on baseline (from 30--31\% to 27\%), representing an explicit cost-performance trade-off rather than a free improvement.
350	
351	\subsection{Full Selective Verification Comparison}
352	
353	\begin{table}[h]
354	\centering
355	\caption{Selective verification methods on held-out validation.}
356	\label{tab:fullcomp}
357	\begin{tabular}{lcccc}
358	\toprule
359	Method & Success & Verify Rate & Rel. Cost & Success/Cost \\
360	\midrule
361	Always-on & 31\% & 100\% & 1.00 & 0.31 \\
362	B-IAVR (ours) & 27\% & 68\% & 0.72 & 0.375 \\
363	Random $p$=0.5 & 26\% & 50\% & 0.55 & 0.473 \\
364	Confidence threshold & 25\% & 55\% & 0.60 & 0.417 \\
365	No-verify & 22\% & 0\% & 0.45 & 0.489 \\
366	\bottomrule
367	\end{tabular}
368	\end{table}
369	
370	B-IAVR achieves the highest absolute success (27\%) among cost-reducing methods and outperforms both random ($p$=0.5) and confidence-threshold baselines at comparable verification rates. However, the margins are modest (1--2pp). The random baseline is unexpectedly competitive, suggesting that at this performance level (30\% success), the marginal value of learned verification scheduling is limited. The no-verify ablation (22\%, $-$9pp versus always-on) confirms that verification has non-trivial value, bounding the potential savings from selective approaches.
371	
372	\subsection{Reward Signal Ablation}
373	
374	\begin{table}[h]
375	\centering
376	\caption{Comparison of reward signals for selective verification training.}
377	\label{tab:reward}
378	\begin{tabular}{lcccc}
379	\toprule
380	Reward & Success & Verify Rate & Cost$\downarrow$ & Stability \\
381	\midrule
382	Action-change (ours) & 27\% & 68\% & 28\% & Moderate \\
383	Random trigger & 25\% & 62\% & 35\% & Unstable \\
384	Confidence-based & 24\% & 70\% & 26\% & Slow \\
385	\bottomrule
386	\end{tabular}
387	\end{table}
388	
389	Action-change reward outperforms alternatives by 2--3 percentage points in success while maintaining reasonable cost reduction. The random trigger baseline shows high variance during training. Confidence-based reward underperforms because model logit calibration at 30\% success level is poor, making confidence an unreliable proxy for verification informativeness.
390	
391	\subsection{ARES Comparison}
392	
393	\begin{table}[h]
394	\centering
395	\caption{B-IAVR vs ARES (SFT router) head-to-head.}
396	\label{tab:ares}
397	\begin{tabular}{lcccc}
398	\toprule
399	Method & Success & Verify Rate & Cost$\downarrow$ & Labels \\
400	\midrule
401	ARES (SFT) & 26\% & 58\% & 38\% & Oracle required \\
402	B-IAVR (RL) & 27\% & 68\% & 28\% & Self-supervised \\
403	Always-on & 31\% & 100\% & 0\% & -- \\
404	\bottomrule
405	\end{tabular}
406	\end{table}
407	
408	ARES achieves greater cost reduction (38\% versus 28\%) due to direct supervision from oracle labels. B-IAVR achieves marginally higher success (27\% versus 26\%) without requiring any labeled data, as its reward signal is derived entirely from observed behavioral changes. The two methods represent different trade-off points: ARES optimizes for cost efficiency given access to oracle supervision; B-IAVR provides a self-supervised alternative that adapts its verification policy through RL.
409	
410	\section{Discussion}
411	
412	\paragraph{Diagnostic Contribution.}
413	The core finding is that step-independent RL training introduces a systematic bias in gradient direction for multi-turn agents. This is not a hyperparameter tuning issue (no value of $h$ below full episode length fully resolves it) but a structural consequence of segmenting trajectories into independently optimized windows. The sign misattribution correlation ($r=0.87$) and the degradation curve across $h$ values provide concrete, measurable characterization of this failure mode.
414	
415	\paragraph{Why the Community Default is Step-Independent.}
416	Three factors drive this default: (1) transformer context windows have finite length, making full-episode processing infeasible for very long trajectories, (2) token-level training loss computation naturally extends to window-level segmentation, and (3) framework implementations (e.g., RAGEN) were designed with single-turn or short-horizon tasks as the primary use case. The failure only manifests clearly in multi-turn tasks requiring 15+ coordinated steps, which recent benchmarks increasingly demand.
417	
418	\paragraph{Limitations of Selective Verification Results.}
419	The selective verification application demonstrates the concept but does not achieve compelling cost-performance trade-offs at this performance level. The weak action-change signal ($r=0.11$ after entropy control), modest margins over random baselines (1--2pp), and 4--5pp performance sacrifice limit the practical impact. We present these results as preliminary evidence that the approach has merit, acknowledging that stronger base agents (achieving 50\%+ success) would provide cleaner training signals and more meaningful cost savings.
420	
421	\paragraph{Limitations.}
422	(1) Experiments are conducted primarily on ALFWorld with a 1.7B model; while ScienceWorld transfer and 7B scaling provide generalization evidence, broader evaluation across environments and scales is needed. (2) Episode-level GRPO is a minimum viable fix, not an optimal solution; GAE outperforms by 8pp and other credit assignment methods may do better still. (3) The selective verification results show narrow margins that may not replicate at larger scale. (4) Multi-seed variance (std=5.9pp) means individual reported numbers should be interpreted with appropriate uncertainty.
423	
424	\section{Conclusion}
425	
426	We present a systematic diagnosis of why step-independent RL training fails for multi-turn LLM agents, identifying dual mechanisms of policy information loss and advantage sign misattribution. The degradation is severe (from 34\% with full context to 2\% with $h=2$) and structural (7B models cannot compensate). Episode-level GRPO provides a zero-cost fix achieving 30.6$\pm$5.9\% success, while GAE demonstrates that finer credit assignment yields additional gains (+8pp). As a preliminary application, learned selective verification reduces cost by 28\% with modest performance trade-off. The diagnostic framework and mechanistic measurements provide the community with concrete tools to evaluate whether their multi-turn agent training setups suffer from these failure modes.
427	
428	\bibliographystyle{plain}
429	\begin{thebibliography}{10}
430	
431	\bibitem{ragen} Liu et al. RAGEN: Training Agents by Reinforcing Reasoning. 2025.
432	
433	\bibitem{selfguide} Zhang et al. Self-Guide: Training LLM Agents with Self-Verification. 2026.
434	
435	\bibitem{ares} Wang et al. ARES: Adaptive Resource-Efficient Self-Verification. arXiv:2603.07915, 2026.
436	
437	\bibitem{thinkless} Chen et al. Thinkless: Learning When to Think with RL. NeurIPS 2025.
438	
439	\bibitem{reflact} Yao et al. ReflAct: Synergizing Reasoning and Acting in Language Agents. EMNLP 2025.
440	
441	\bibitem{deepseekr1} DeepSeek-AI. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. 2025.
442	
443	\bibitem{gae} Schulman et al. High-Dimensional Continuous Control Using Generalized Advantage Estimation. ICLR 2016.
444	
445	\bibitem{alfworld} Shridhar et al. ALFWorld: Aligning Text and Embodied Environments for Interactive Learning. ICLR 2021.
446	
447	\bibitem{scienceworld} Wang et al. ScienceWorld: Is Your Agent Smarter Than a 5th Grader? EMNLP 2022.
448	
449	\bibitem{grpo} Shao et al. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models. 2024.
450	
451	\end{thebibliography}
452	
453	\end{document}
454	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65757622-1eda-4b04-b1ab-538dc754ee71",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "a5b02fdfddc805fc8",
  "type": "user",
  "uuid": "52c5c6c7-d1af-4a4d-92bc-838f3ab5ded8",
  "sourceToolAssistantUUID": "65757622-1eda-4b04-b1ab-538dc754ee71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-17T12:55:40.366Z_

Now let me also read the "worst" version and the review context file to complete my understanding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52c5c6c7-d1af-4a4d-92bc-838f3ab5ded8",
  "isSidechain": true,
  "agentId": "a5b02fdfddc805fc8",
  "requestId": "req_011Cb8BDA8grmsDNE4pLUHf6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9783137c-f620-42c0-b9ab-51e8d6c1568b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016BemVDLCkLh26HuwZ1kEdN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20348,
      "cache_read_input_tokens": 27845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20348,
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

_source line 22 · 2026-05-17T12:55:42.793Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XA5PayZq4AWNhZwU644BYY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260517T121256/worst/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9783137c-f620-42c0-b9ab-51e8d6c1568b",
  "isSidechain": true,
  "agentId": "a5b02fdfddc805fc8",
  "requestId": "req_011Cb8BDA8grmsDNE4pLUHf6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1205c5c1-858c-49e4-b7e7-8a552049b01c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016BemVDLCkLh26HuwZ1kEdN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20348,
      "cache_read_input_tokens": 27845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20348,
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

_source line 23 · 2026-05-17T12:55:43.093Z_

<details><summary>↩ Tool result · `toolu_01XA5PayZq4AWNhZwU644BYY`</summary>

```text
1	\documentclass{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage{amsmath,amssymb}
4	\usepackage{booktabs}
5	\usepackage{graphicx}
6	\usepackage{hyperref}
7	\usepackage{xcolor}
8	\usepackage[margin=1in]{geometry}
9	\usepackage{multirow}
10	
11	\title{Dissecting Credit Assignment Failure in Multi-Turn LLM Agent RL:\\A Dual-Mechanism Analysis}
12	
13	\author{Anonymous}
14	
15	\date{}
16	
17	\begin{document}
18	\maketitle
19	
20	\begin{abstract}
21	Reinforcement learning (RL) for multi-turn Large Language Model (LLM) agents commonly adopts step-independent training, where each context window is optimized as a separate bandit arm. We show that this default catastrophically fails in interactive environments due to two compounding mechanisms: \emph{advantage sign misattribution} (gradient direction reflects episode outcome rather than local action quality) and \emph{policy information loss} (truncated context prevents cross-step strategy learning). Episode-level training eliminates sign misattribution but plateaus at 23.4\% ($\pm$6.2pp) on ALFWorld because all tokens share a single bandit-level advantage. Generalized Advantage Estimation (GAE) with a learned value function reaches 41.0\%, demonstrating that per-token credit assignment is the critical missing capability. Through mechanistic analysis, we decompose credit assignment failure into four interacting factors: sign misattribution (partial $r$=0.73 with episode outcome), entropy collapse, KL drift, and bandit-level credit insufficiency. We provide a failure mode taxonomy, quantify each mechanism's contribution, and derive actionable design guidelines for practitioners building RL systems for LLM agents. Our findings generalize across environments (ScienceWorld, 5$\times$ improvement) and model scales (1.7B to 7B).
22	\end{abstract}
23	
24	\section{Introduction}
25	
26	Training LLM-based agents with reinforcement learning in multi-turn interactive environments remains unreliable. Standard RL frameworks for LLM agents default to step-independent optimization: the agent's trajectory is split into fixed-length context windows, each treated as an independent policy optimization unit. This design choice originates from practical constraints (context window limits, memory efficiency) and the community's familiarity with token-level language model training. Yet its consequences for multi-turn credit assignment have received little systematic analysis.
27	
28	We present a diagnostic study that identifies why step-independent training fails for multi-turn LLM agents and characterizes the resulting failure modes. Our investigation begins with a concrete observation: on ALFWorld, step-independent Group Relative Policy Optimization (GRPO) collapses to near-zero success by training step 10 (mean 1\% across 3 seeds, $h$=2), while episode-level GRPO achieves 23.4\% under identical hyperparameters. This 23$\times$ gap demands explanation.
29	
30	We trace the failure to two compounding mechanisms. First, \textbf{advantage sign misattribution}: in step-independent mode, per-window advantages inherit their sign from the episode outcome rather than reflecting local action quality. A good action in a failed episode receives negative advantage and is suppressed; a poor action in a successful episode receives positive advantage and is reinforced. Second, \textbf{policy information loss}: truncated context windows prevent the policy from learning cross-step strategies (e.g., ``explore drawer then move to countertop''), limiting what can be learned regardless of credit quality.
31	
32	Episode-level training resolves both issues by treating the full trajectory as a single optimization unit. However, this merely exposes a deeper bottleneck: GRPO's bandit-style credit assignment, where all tokens in a trajectory share the same scalar advantage, cannot distinguish critical decision points from routine actions. The resulting plateau (23--28\%) persists through 50 training steps despite train success reaching 50\%. GAE with a learned value function provides per-token temporal-difference signals and reaches 41\%, a 17.6 percentage point (pp) improvement that quantifies the cost of bandit-level credit.
33	
34	Our mechanistic analysis reveals that sign misattribution, while dominant ($r$=0.73 with episode outcome), is not the sole failure factor. KL divergence ($r$=0.31), entropy dynamics ($r$=0.27), and window position ($r$=-0.18) each independently correlate with advantage sign errors, forming a multi-factor failure landscape.
35	
36	Our contributions are:
37	\begin{enumerate}
38	    \item A \textbf{failure mode taxonomy} for credit assignment in multi-turn LLM agent RL, identifying four interacting mechanisms (sign misattribution, information loss, entropy collapse, bandit-level credit insufficiency) with quantified contributions.
39	    \item \textbf{Empirical characterization} of the credit granularity spectrum from step-independent (catastrophic failure) through episode-level (plateau) to per-token GAE (best performance), establishing that episode-level training is necessary but not sufficient.
40	    \item \textbf{Actionable design guidelines} for practitioners, supported by ablations across context windows ($h$=2 to full), reward shaping variants, model scales (1.7B, 7B), and environments (ALFWorld, ScienceWorld).
41	\end{enumerate}
42	
43	\section{Background}
44	
45	\subsection{Multi-Turn LLM Agent RL}
46	
47	We consider the setting where an LLM policy $\pi_\theta$ interacts with a text-based environment over multiple turns. At each turn $t$, the agent observes state $o_t$ and produces action $a_t \sim \pi_\theta(\cdot | o_{\leq t}, a_{&lt;t})$. A sparse binary reward $R \in \{0, 1\}$ is given at episode termination based on task completion.
48	
49	\subsection{GRPO and Step-Independent Training}
50	
51	GRPO~computes advantages via group normalization: given a group of $G$ rollouts with returns $\{R_i\}_{i=1}^G$, the advantage for rollout $i$ is $A_i = (R_i - \mu_G) / \sigma_G$. The policy gradient is:
52	\begin{equation}
53	\nabla_\theta J = \mathbb{E}\left[\sum_{t} A_i \nabla_\theta \log \pi_\theta(a_t | o_{\leq t})\right]
54	\end{equation}
55	
56	In \textbf{step-independent} mode (the default in frameworks like RAGEN), the trajectory is split into windows of $h$ tokens. Each window $w_j$ receives a discounted return $R_j = \gamma^{k_j} R$ where $k_j$ is the window's temporal distance from episode end. Windows are optimized independently, creating $\lceil T/h \rceil$ separate bandit problems per episode.
57	
58	In \textbf{episode-level} mode, the full trajectory is treated as a single sample. All tokens share advantage $A_i = (R_i - \mu_G)/\sigma_G$, eliminating inter-window sign conflicts but providing no per-token credit differentiation.
59	
60	\subsection{Generalized Advantage Estimation}
61	
62	GAE uses a learned value function $V_\phi(s_t)$ to compute per-token advantages:
63	\begin{equation}
64	\hat{A}_t^{\text{GAE}(\lambda)} = \sum_{l=0}^{T-t} (\gamma\lambda)^l \delta_{t+l}, \quad \delta_t = r_t + \gamma V_\phi(s_{t+1}) - V_\phi(s_t)
65	\end{equation}
66	This provides fine-grained, per-token credit assignment through temporal difference learning.
67	
68	\section{Failure Mode Taxonomy}
69	
70	We identify four mechanisms that contribute to credit assignment failure in multi-turn LLM agent RL, ordered by empirical severity.
71	
72	\subsection{Mechanism 1: Advantage Sign Misattribution}
73	
74	In step-independent training, the sign of per-window advantage is primarily determined by episode outcome rather than window-local action quality. Empirical measurement shows $r$=0.73 correlation between advantage sign and episode outcome, versus only $r$=0.28 correlation with local action quality (Table~\ref{tab:mechanism}). Consequently, 78\% of successful episodes have all-positive window advantages regardless of individual action quality, and 82\% of failed episodes have all-negative advantages.
75	
76	This creates systematic gradient errors: good actions in failed episodes are suppressed (false negative reinforcement) while poor actions in successful episodes are strengthened (false positive reinforcement).
77	
78	\subsection{Mechanism 2: Policy Information Loss}
79	
80	Context window truncation at $h$ tokens prevents the policy from conditioning on earlier trajectory states. For tasks requiring multi-step plans (e.g., ``find object X in location A, then bring it to location B''), the policy in later windows cannot access the reasoning or observations from earlier windows. Our $h$-sweep (Section~\ref{sec:hsweep}) shows monotonically decreasing performance as $h$ shrinks: $h$=full achieves 24.0\% mean success vs. $h$=2 at 1.0\%.
81	
82	\subsection{Mechanism 3: Entropy Collapse}
83	
84	Under noisy credit signals, the policy narrows its action distribution without improving quality. Episode-level GRPO shows entropy declining from 0.20 (step 5) to 0.12 (step 50) while validation success stagnates at 24--28\%. The policy becomes increasingly deterministic without becoming more correct, a symptom of optimization on noisy advantages.
85	
86	\subsection{Mechanism 4: Bandit-Level Credit Insufficiency}
87	
88	Even with correct advantage signs (episode-level training), sharing a single scalar advantage across all tokens in a trajectory prevents distinguishing critical decision points from routine actions. This is evidenced by the 17.6pp gap between episode-level GRPO (23.4\%) and GAE (41.0\%), and by the strong negative correlation between task complexity and success ($r$=-0.62): tasks requiring more sequential decisions suffer more from undifferentiated credit.
89	
90	\section{Experimental Setup}
91	
92	\textbf{Environment.} ALFWorld, a text-based household environment with 6 task types of varying complexity (pick, examine, clean, heat, cool, pick\_two). Episodes average 30--45 actions. Validation set: 134 held-out tasks.
93	
94	\textbf{Base model.} Qwen3-1.7B (primary), Qwen3-7B (scaling verification).
95	
96	\textbf{Training.} GRPO with group size 8, learning rate 1e-6, KL coefficient 0.01. Training for 15 steps (primary comparisons) and up to 50 steps (convergence analysis). Self-verification is always-on unless otherwise noted.
97	
98	\textbf{Evaluation.} Greedy decoding, success rate on validation set, 3--5 seeds per condition. We report mean $\pm$ std and 95\% confidence intervals where applicable.
99	
100	\section{Results}
101	
102	\subsection{Episode-Level Training: Necessary but Not Sufficient}
103	
104	Episode-level GRPO achieves mean validation success of 23.4\% ($\pm$6.2pp, 5 seeds, 95\% CI [15.7\%, 31.1\%]) compared to 1.0\% for step-independent ($h$=2). This confirms that eliminating sign misattribution and information loss is necessary for any learning. However, extending training to 50 steps reveals a hard plateau (Table~\ref{tab:convergence}): validation success peaks at 28.1\% (step 15) then declines to 24\% while training success continues rising to 50\%, indicating overfitting to the training distribution without generalizable credit learning.
105	
106	\begin{table}[h]
107	\centering
108	\caption{Episode-level GRPO convergence trajectory. Training success continues rising while validation plateaus, indicating bandit-level credit is insufficient for generalization.}
109	\label{tab:convergence}
110	\begin{tabular}{lccccc}
111	\toprule
112	Step & Val Success & Train Success & Val pass@8 & Entropy & KL \\
113	\midrule
114	5 & 25.0\% & 31.0\% & 88\% & 0.20 & 0.003 \\
115	10 & 25.0\% & 38.0\% & 91\% & 0.17 & 0.007 \\
116	15 & 28.1\% & 44.0\% & 93\% & 0.15 & 0.010 \\
117	20 & 27.0\% & 47.0\% & 93\% & 0.14 & 0.012 \\
118	30 & 26.0\% & 50.0\% & 94\% & 0.13 & 0.014 \\
119	40 & 25.0\% & 50.0\% & 94\% & 0.12 & 0.015 \\
120	50 & 24.0\% & 50.0\% & 94\% & 0.12 & 0.015 \\
121	\bottomrule
122	\end{tabular}
123	\end{table}
124	
125	The pass@8 of 94\% at step 50 reveals that the policy has \emph{capability} to solve most tasks but cannot reliably concentrate probability mass on correct action sequences under greedy decoding. This is the signature of bandit-level credit: the model learns which trajectory patterns succeed on training tasks but lacks fine-grained signal to reliably reproduce them.
126	
127	\subsection{Context Window Ablation}
128	\label{sec:hsweep}
129	
130	Table~\ref{tab:hsweep} presents the $h$-sweep across 5 context window sizes (3 seeds each). Performance degrades probabilistically with smaller $h$: $h$=2 collapses in all seeds (mean 1.0\%), while $h$=full achieves 24.0\%.
131	
132	\begin{table}[h]
133	\centering
134	\caption{Context window $h$-sweep (step 15, 3 seeds). Smaller windows increase collapse probability rather than creating a clean threshold.}
135	\label{tab:hsweep}
136	\begin{tabular}{lcccccc}
137	\toprule
138	$h$ & Seed 1 & Seed 2 & Seed 3 & Mean & Std & Collapse Rate \\
139	\midrule
140	$h$=2 & 0.0\% & 3.0\% & 0.0\% & 1.0\% & 1.7pp & 3/3 \\
141	$h$=5 & 6.0\% & 0.0\% & 9.0\% & 5.0\% & 4.6pp & 1/3 \\
142	$h$=10 & 12.0\% & 3.0\% & 16.0\% & 10.3\% & 6.6pp & 0/3 \\
143	$h$=20 & 19.0\% & 9.0\% & 22.0\% & 16.7\% & 6.8pp & 0/3 \\
144	full & 28.0\% & 19.0\% & 25.0\% & 24.0\% & 4.6pp & 0/3 \\
145	\bottomrule
146	\end{tabular}
147	\end{table}
148	
149	The relationship is not a clean step function. Cross-seed variance is high at intermediate $h$ values: $h$=5 occasionally outperforms $h$=10 (seed 3: 9\% vs seed 2: 3\%), and individual seeds of $h$=20 occasionally underperform seeds of $h$=10. This non-monotonicity reflects the stochastic nature of credit assignment failure: collapse probability increases with smaller $h$, modulated by random initialization and early training dynamics. We characterize this as \emph{probabilistic degradation} rather than a deterministic threshold effect.
150	
151	\subsection{Multi-Seed Replication}
152	
153	Five-seed replication of episode-level GRPO (Table~\ref{tab:multiseed}) confirms high variance: individual seeds range from 15\% to 30\% (15pp range). The 95\% CI of [15.7\%, 31.1\%] is too wide to claim episode-level ``solves'' the task, but the mean (23.4\%) is significantly above step-independent (1\%), establishing that episode-level is a necessary condition.
154	
155	\begin{table}[h]
156	\centering
157	\caption{Multi-seed episode-level GRPO (step 15). High variance reflects sensitivity to initial rollout quality in GRPO's group normalization.}
158	\label{tab:multiseed}
159	\begin{tabular}{lcccc}
160	\toprule
161	Seed & Val Success & Train Success & Action Valid & Plateau Step \\
162	\midrule
163	1 & 28\% & 44\% & 55\% & 10 \\
164	2 & 19\% & 41\% & 52\% & 8 \\
165	3 & 25\% & 47\% & 56\% & 10 \\
166	4 & 15\% & 35\% & 48\% & 12 \\
167	5 & 30\% & 50\% & 58\% & 10 \\
168	\midrule
169	Mean$\pm$Std & 23.4$\pm$6.2\% & 43.4$\pm$5.7\% & 53.8$\pm$3.8\% & -- \\
170	\bottomrule
171	\end{tabular}
172	\end{table}
173	
174	The train-val gap (mean 22.6pp) further evidences that bandit-level credit enables memorization of training trajectory patterns without learning transferable per-step policies. Seed 4's low performance (15\%) likely reflects GRPO's cold-start sensitivity: if early rollouts all fail, group-normalized advantages are zero (no variance), preventing learning.
175	
176	\subsection{Credit Granularity Spectrum: GAE Comparison}
177	
178	Table~\ref{tab:gae} establishes the credit granularity spectrum from step-independent through episode-level to per-token GAE.
179	
180	\begin{table}[h]
181	\centering
182	\caption{Credit granularity comparison (step 15, 3 seeds). Per-token credit (GAE) substantially outperforms bandit-level credit (episode-level GRPO).}
183	\label{tab:gae}
184	\begin{tabular}{lccccc}
185	\toprule
186	Method & Seed 1 & Seed 2 & Seed 3 & Mean & Std \\
187	\midrule
188	Step-independent ($h$=2) & 0.0\% & 3.0\% & 0.0\% & 1.0\% & 1.7pp \\
189	Episode-level GRPO & 28.0\% & 19.0\% & 25.0\% & 24.0\% & 4.6pp \\
190	GAE ($\lambda$=1, $\gamma$=1) & 37.0\% & 34.0\% & 39.0\% & 36.7\% & 2.5pp \\
191	GAE ($\lambda$=0.95, $\gamma$=1) & 44.0\% & 38.0\% & 41.0\% & 41.0\% & 3.0pp \\
192	\bottomrule
193	\end{tabular}
194	\end{table}
195	
196	GAE($\lambda$=0.95) achieves 41.0\%, a 17.6pp improvement over episode-level GRPO. This gap directly quantifies the cost of bandit-level credit: even when advantage signs are correct (episode-level eliminates misattribution), the inability to differentiate per-token contributions limits performance. GAE's learned value function provides temporal-difference signals that identify which specific actions within a trajectory were responsible for success or failure.
197	
198	GAE($\lambda$=1, $\gamma$=1) achieves 36.7\%, slightly below $\lambda$=0.95 due to higher variance from undiscounted returns. Both GAE variants substantially outperform episode-level GRPO with lower cross-seed variance (2.5--3.0pp vs 4.6pp), indicating that per-token credit also stabilizes training.
199	
200	The per-token advantage variance for GAE is 0.42 (different tokens receive meaningfully different advantages) versus exactly 0.0 for episode-level GRPO (all tokens identical). This confirms the mechanism: GAE differentiates credit while GRPO cannot.
201	
202	\subsection{Mechanistic Verification}
203	\label{sec:mechanism}
204	
205	Table~\ref{tab:mechanism} presents direct measurement of credit assignment mechanisms under step-independent training ($h$=2).
206	
207	\begin{table}[h]
208	\centering
209	\caption{Mechanism verification ($h$=2, step 5). Sign misattribution is dominant but not sole factor; multiple confounds independently correlate with advantage sign errors.}
210	\label{tab:mechanism}
211	\begin{tabular}{lccc}
212	\toprule
213	Metric & Observed & Hypothesis & Status \\
214	\midrule
215	Sign-outcome correlation & 0.73 & $>$0.95 & Partial \\
216	Sign-local quality correlation & 0.28 & $<$0.1 & Failed \\
217	Magnitude decay $R^2$ & 0.61 & $>$0.85 & Partial \\
218	Episode-level adv. variance & 0.0 & 0.0 & Confirmed \\
219	\% success eps all-positive & 78\% & $>$95\% & Partial \\
220	\bottomrule
221	\end{tabular}
222	\end{table}
223	
224	The sign-outcome correlation of 0.73 (vs. hypothesized $>$0.95) reveals significant confounding factors. Table~\ref{tab:confounds} decomposes these contributions.
225	
226	\begin{table}[h]
227	\centering
228	\caption{Confound analysis: multiple factors independently correlate with advantage sign, forming a multi-factor failure landscape.}
229	\label{tab:confounds}
230	\begin{tabular}{lcc}
231	\toprule
232	Variable & Correlation with Adv. Sign & $p$-value \\
233	\midrule
234	Episode outcome & 0.73 & $<$0.001 \\
235	KL divergence & 0.31 & $<$0.01 \\
236	Local action quality & 0.28 & $<$0.01 \\
237	Entropy & 0.27 & $<$0.01 \\
238	Window position & $-$0.18 & $<$0.05 \\
239	\bottomrule
240	\end{tabular}
241	\end{table}
242	
243	Sign misattribution is the dominant mechanism but accounts for only 53\% of advantage sign variance ($r^2$=0.53). KL drift, entropy dynamics, and positional decay each contribute independently. This multi-factor structure explains why episode-level training (which eliminates only sign misattribution) plateaus rather than fully solving the problem: the remaining mechanisms (entropy collapse, credit insufficiency) continue operating.
244	
245	The local action quality correlation of 0.28 is partially legitimate (good local actions do contribute to success) and partially artifactual (GRPO's group normalization creates relative comparisons within groups). This makes it impossible to attribute 100\% of the sign-quality correlation to misattribution, a nuance that pure theoretical analysis would miss.
246	
247	\subsection{Task Complexity Analysis}
248	
249	Table~\ref{tab:tasktype} breaks down episode-level performance by ALFWorld task type.
250	
251	\begin{table}[h]
252	\centering
253	\caption{Per-task-type breakdown (episode-level, 5-seed mean). Performance correlates negatively with task complexity ($r$=$-$0.62) and positively with episode length ($r$=0.48).}
254	\label{tab:tasktype}
255	\begin{tabular}{lcccc}
256	\toprule
257	Task Type & Success & Std & Avg Steps & Subtasks \\
258	\midrule
259	pick & 35\% & 5pp & 28 & 1 \\
260	examine & 30\% & 6pp & 32 & 1 \\
261	clean & 22\% & 7pp & 35 & 2 \\
262	heat & 20\% & 8pp & 37 & 2 \\
263	cool & 18\% & 7pp & 38 & 2 \\
264	pick\_two & 10\% & 9pp & 45 & 2 \\
265	\bottomrule
266	\end{tabular}
267	\end{table}
268	
269	Single-subtask tasks (pick: 35\%, examine: 30\%) substantially outperform multi-subtask tasks (pick\_two: 10\%, cool: 18\%). The correlation between task complexity and success ($r$=-0.62) directly reflects the credit assignment bottleneck: longer horizons mean more tokens sharing the same advantage, resulting in coarser effective credit per decision point. The pick\_two task (requiring two sequential object manipulations) performs worst because episode-level advantage cannot distinguish credit for the first pick from credit for the second pick.
270	
271	Cross-seed variance also increases with complexity (5pp for pick vs 9pp for pick\_two), consistent with the probabilistic degradation pattern: harder credit assignment problems have more stochastic outcomes.
272	
273	\subsection{Reward Shaping Under Sparse Credit}
274	
275	Adding a dense auxiliary reward (valid\_action\_bonus=0.05) to episode-level GRPO reveals a failure mode specific to bandit-level credit under sparse task signals (Table~\ref{tab:bonus}).
276	
277	\begin{table}[h]
278	\centering
279	\caption{Valid action bonus ablation. Dense auxiliary reward improves format compliance but hurts task success under episode-level bandit credit.}
280	\label{tab:bonus}
281	\begin{tabular}{lcccc}
282	\toprule
283	Config & Val Success & Action Valid & Avg Traj Len & Reward Mean \\
284	\midrule
285	Episode-level (baseline) & 28.0\% & 55\% & 38.2 & 2.81 \\
286	Episode-level + bonus=0.05 & 22.0\% & 72\% & 45.6 & 3.92 \\
287	\bottomrule
288	\end{tabular}
289	\end{table}
290	
291	The bonus successfully increases format compliance (action\_is\_valid: 55\% $\to$ 72\%) but decreases task success by 6pp. The mechanism: when task reward is sparse and credit is bandit-level, any dense auxiliary signal dominates gradient updates. The model learns to produce ``many valid but non-goal-directed actions'' (longer trajectories: 38.2 $\to$ 45.6 steps) rather than ``goal-directed sequences that happen to be valid.'' This demonstrates that reward shaping is not a viable substitute for fine-grained credit assignment in multi-turn settings.
292	
293	\subsection{Verification Value and Selective Strategies}
294	
295	Removing self-verification entirely reduces success from 25.0\% to 13.0\% (12pp drop, Table~\ref{tab:verify}), confirming verification's value. However, all selective verification strategies underperform always-on verification for this agent quality level.
296	
297	\begin{table}[h]
298	\centering
299	\caption{Verification strategies comparison. All selective approaches underperform always-on at 25\% base agent quality, indicating selective verification requires stronger base agents.}
300	\label{tab:verify}
301	\begin{tabular}{lcccc}
302	\toprule
303	Method & Success & Verify Rate & Token Cost & Success/Token \\
304	\midrule
305	Always-on & 25.0\% & 100\% & 1.0$\times$ & 0.250 \\
306	Confidence-0.5 & 19.0\% & 65\% & 0.72$\times$ & 0.264 \\
307	B-IAVR (RL-learned) & 16.0\% & 88\% & 0.93$\times$ & 0.172 \\
308	Random-50\% & 14.0\% & 50\% & 0.62$\times$ & 0.226 \\
309	No-verify & 13.0\% & 0\% & 0.45$\times$ & 0.289 \\
310	\bottomrule
311	\end{tabular}
312	\end{table}
313	
314	The RL-trained selective policy (B-IAVR) fails to learn meaningful skip decisions, degrading to near-always-verify (88\% rate) with 9pp success loss. The underlying action-change reward signal shows $r$=0.08 ($p$=0.12) correlation with success, indistinguishable from noise. Controlling for policy entropy eliminates even this weak correlation (partial $r$=0.07, $p$=0.15), revealing that apparent verification informativeness signals are confounded with policy uncertainty rather than reflecting genuine causal contribution.
315	
316	A confidence-based heuristic (verify when entropy $>$ 0.5) outperforms the RL-trained policy despite using no training, because policy entropy is a more informative signal than action-change at this agent quality level.
317	
318	\subsection{Cross-Framework Comparison}
319	
320	Table~\ref{tab:ares} compares against ARES, an SFT-based verification router.
321	
322	\begin{table}[h]
323	\centering
324	\caption{ARES (SFT) vs B-IAVR (RL) for selective verification. SFT with oracle labels dominates RL with noisy intrinsic reward at weak agent quality.}
325	\label{tab:ares}
326	\begin{tabular}{lcccc}
327	\toprule
328	Method & Success & Verify Rate & Cost Reduction & Dominates \\
329	\midrule
330	ARES (SFT) & 22.0\% & 70\% & 30\% & Yes \\
331	B-IAVR (RL) & 16.0\% & 88\% & 12\% & No \\
332	\bottomrule
333	\end{tabular}
334	\end{table}
335	
336	ARES dominates B-IAVR on both axes (higher success, lower cost). SFT with oracle labels is a strictly easier optimization problem that bypasses the reward signal quality issue entirely. This comparison illustrates a design principle: RL-based selective strategies require reward signals of sufficient quality, which in turn requires base agents of sufficient capability. Below a capability threshold, supervised approaches from oracle demonstrations are more practical.
337	
338	\subsection{Generalization: Environment and Scale}
339	
340	\textbf{ScienceWorld transfer.} Episode-level achieves 15\% ($\pm$8pp) vs step-independent 3\% ($\pm$2pp) on ScienceWorld (5$\times$ ratio), confirming that the failure patterns are not ALFWorld-specific. The lower absolute performance (15\% vs 25\%) reflects ScienceWorld's longer horizon (40+ steps average), consistent with the credit assignment bottleneck hypothesis.
341	
342	\textbf{Model scaling.} Table~\ref{tab:scaling} shows results on Qwen3-7B.
343	
344	\begin{table}[h]
345	\centering
346	\caption{Scaling comparison. Larger models partially mitigate credit assignment failure through stronger in-context learning, but the problem persists.}
347	\label{tab:scaling}
348	\begin{tabular}{lccc}
349	\toprule
350	Model & Episode-Level & Step-Independent & Ratio \\
351	\midrule
352	Qwen3-1.7B & 25\% & 1\% & 25$\times$ \\
353	Qwen3-7B & 32\% & 8\% & 4$\times$ \\
354	\bottomrule
355	\end{tabular}
356	\end{table}
357	
358	Both methods improve by approximately 7pp with scale (near-parallel shift). The episode-level advantage ratio shrinks from 25$\times$ to 4$\times$: larger models' stronger in-context learning partially compensates for credit assignment noise in step-independent mode. However, the 4$\times$ gap at 7B confirms that credit assignment failure persists at scale and is not fully resolved by model capacity alone.
359	
360	\section{Discussion}
361	
362	\subsection{Actionable Design Guidelines}
363	
364	Based on our analysis, we propose the following guidelines for practitioners building RL systems for multi-turn LLM agents:
365	
366	\begin{enumerate}
367	    \item \textbf{Never use step-independent training for multi-turn tasks.} The sign misattribution and information loss mechanisms make it categorically unsuitable regardless of hyperparameter tuning.
368	    \item \textbf{Episode-level training is a minimum viable baseline, not a solution.} It eliminates the worst failure mode but plateaus due to bandit-level credit insufficiency.
369	    \item \textbf{Invest in per-token credit (value functions, GAE).} The 17.6pp gap between episode-level GRPO and GAE represents recoverable performance that requires only algorithmic changes, not more data or compute.
370	    \item \textbf{Do not substitute reward shaping for credit granularity.} Dense auxiliary rewards under bandit-level credit can harm task performance by dominating the sparse task signal.
371	    \item \textbf{Match selective strategy complexity to base agent quality.} RL-trained selective policies require reward signals that only become meaningful above a capability threshold; below it, heuristic or supervised approaches are more practical.
372	\end{enumerate}
373	
374	\subsection{Why Does the Community Default to Step-Independent?}
375	
376	Three factors drive the prevalence of step-independent training despite its failure mode: (1) context window limits make full-episode training impractical for long trajectories without architectural modifications; (2) token-level training is the standard paradigm for language models, and step-independent preserves this granularity; (3) framework design choices (e.g., RAGEN's default configuration) embed step-independent as the path of least resistance. Our results suggest this default should be revised.
377	
378	\subsection{Limitations and Future Work}
379	
380	Our analysis has several limitations. First, we study only text-based environments; whether the same failure modes apply to tool-use or code-generation agents remains open. Second, our mechanistic analysis (Section~\ref{sec:mechanism}) is correlational; causal interventions on individual mechanisms would strengthen claims. Third, the GAE comparison uses a separately trained value function that adds computational cost not accounted for in our efficiency comparisons.
381	
382	Selective verification remains a promising direction but requires stronger base agents. Our evidence suggests that RL-trained verification policies become viable only when (1) the base agent exceeds a capability threshold where verification decisions have meaningful signal, and (2) the intrinsic reward (action-change or alternative) correlates with task success after controlling for confounds. We leave the development of such systems to future work.
383	
384	Hierarchical credit assignment (per-subtask rewards, option-level advantages) represents a middle ground between episode-level bandit credit and full per-token GAE that may be particularly suitable for multi-turn agents with natural subtask decomposition.
385	
386	\section{Conclusion}
387	
388	We presented a systematic analysis of credit assignment failure in multi-turn LLM agent RL. Our failure mode taxonomy identifies four interacting mechanisms: advantage sign misattribution, policy information loss, entropy collapse, and bandit-level credit insufficiency. Through controlled experiments across context windows, credit granularity levels, environments, and model scales, we establish that episode-level training is necessary (eliminating catastrophic failure from sign misattribution) but not sufficient (plateauing due to undifferentiated per-token credit). The 17.6pp gap between episode-level GRPO and GAE quantifies the cost of this insufficiency and points toward per-token credit assignment as the critical capability for practical multi-turn LLM agent RL. Our actionable guidelines provide practitioners with empirically grounded design principles for avoiding the failure modes we characterize.
389	
390	\bibliographystyle{plain}
391	\begin{thebibliography}{10}
392	
393	\bibitem{grpo}
394	Z. Shao et al., ``DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models,'' 2024.
395	
396	\bibitem{ragen}
397	W. Qi et al., ``RAGEN: Training Agents by Reinforcing Reasoning,'' 2025.
398	
399	\bibitem{alfworld}
400	M. Shridhar et al., ``ALFWorld: Aligning Text and Embodied Environments for Interactive Learning,'' ICLR, 2021.
401	
402	\bibitem{scienceworld}
403	R. Wang et al., ``ScienceWorld: Is your Agent Smarter than a 5th Grader?'' EMNLP, 2022.
404	
405	\bibitem{gae}
406	J. Schulman et al., ``High-Dimensional Continuous Control Using Generalized Advantage Estimation,'' ICLR, 2016.
407	
408	\bibitem{selfguide}
409	X. Zhao et al., ``Self-Guide: Self-Guided Verification for LLM Agents,'' 2026.
410	
411	\bibitem{ares}
412	T. Zhang et al., ``ARES: Adaptive Reasoning Effort with Selective Verification,'' 2026.
413	
414	\bibitem{thinkless}
415	Y. Chen et al., ``Thinkless: LLM Learns When to Think,'' NeurIPS, 2025.
416	
417	\bibitem{reflact}
418	L. Wang et al., ``ReflAct: World-Grounded Reasoning and Acting in Language Agents,'' EMNLP, 2025.
419	
420	\bibitem{ppo}
421	J. Schulman et al., ``Proximal Policy Optimization Algorithms,'' 2017.
422	
423	\end{thebibliography}
424	
425	\end{document}
426	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1205c5c1-858c-49e4-b7e7-8a552049b01c",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "a5b02fdfddc805fc8",
  "type": "user",
  "uuid": "71bb69b1-921a-4a87-86e3-d176d7cb5d14",
  "sourceToolAssistantUUID": "1205c5c1-858c-49e4-b7e7-8a552049b01c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-17T12:55:43.202Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01CsUxEAVKGzim1KUutDSzY5`</summary>

```json
{
  "pattern": "**/review_context.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71bb69b1-921a-4a87-86e3-d176d7cb5d14",
  "isSidechain": true,
  "agentId": "a5b02fdfddc805fc8",
  "requestId": "req_011Cb8BDA8grmsDNE4pLUHf6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3416ba84-dc6f-4710-b65e-72692cbb8040",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016BemVDLCkLh26HuwZ1kEdN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20348,
      "cache_read_input_tokens": 27845,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20348
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 211,
          "cache_read_input_tokens": 27845,
          "cache_creation_input_tokens": 20348,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20348,
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

_source line 25 · 2026-05-17T12:55:43.219Z_

<details><summary>↩ Tool result · `toolu_01CsUxEAVKGzim1KUutDSzY5`</summary>

```text
artifacts/dream_reports/dream_20260516T235255/best/review_context.yaml
artifacts/dream_reports/dream_20260516T235255/median/review_context.yaml
artifacts/dream_reports/dream_20260516T235255/worst/review_context.yaml
artifacts/dream_reports/dream_20260517T121256/best/review_context.yaml
artifacts/dream_reports/dream_20260517T121256/median/review_context.yaml
artifacts/dream_reports/dream_20260517T121256/worst/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3416ba84-dc6f-4710-b65e-72692cbb8040",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "a5b02fdfddc805fc8",
  "type": "user",
  "uuid": "879a94d7-a172-43f5-9841-4af1aa415db8",
  "sourceToolAssistantUUID": "3416ba84-dc6f-4710-b65e-72692cbb8040",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-17T12:55:46.973Z_

<details open><summary>🔧 Tool call — Read · `toolu_013ndXcSMzbPuREadjBCrfir`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260517T121256/worst/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "879a94d7-a172-43f5-9841-4af1aa415db8",
  "isSidechain": true,
  "agentId": "a5b02fdfddc805fc8",
  "requestId": "req_011Cb8BDbDJz3KefWEkdgByY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2a45f6c-a529-460f-9ab8-afac34f603a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sbbj4JvpgDSiYBwBRthYCX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10491,
      "cache_read_input_tokens": 48193,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10491
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 105,
          "cache_read_input_tokens": 48193,
          "cache_creation_input_tokens": 10491,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10491,
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

_source line 27 · 2026-05-17T12:55:47.246Z_

<details><summary>↩ Tool result · `toolu_013ndXcSMzbPuREadjBCrfir`</summary>

```text
1	narrative_guidance: '完全 reframe 为 diagnostic/analysis paper。Title: "Dissecting Credit
2	  Assignment Failure in Multi-Turn LLM Agent RL: A Dual-Mechanism Analysis"。 核心叙事：episode-level
3	  是 necessary but not sufficient，消除 window-level 问题后暴露更深层 credit assignment 瓶颈。 GAE
4	  >> episode-level GRPO 证明 per-token credit 是关键缺失。Sign misattribution 是主要但非唯一因素——entropy
5	  collapse、KL drift、information loss 共同作用。 贡献定位为 failure mode taxonomy + actionable
6	  guidelines + cross-framework design analysis。 Selective verification 完全移入 future
7	  work。Claim 2/3 删除。
8	
9	  '
10	imagined_experiments:
11	- name: Episode-level GRPO convergence (exp029 continuation)
12	  plan_id: plan_001
13	  description: Episode-level GRPO 继续训练至 step 50+，观察是否突破 28% plateau
14	  expected_results:
15	    step15_val_success: 0.28125
16	    step20_val_success: 0.27
17	    step30_val_success: 0.26
18	    step40_val_success: 0.25
19	    step50_val_success: 0.24
20	    convergence_val_success: 0.25
21	    step50_train_success: 0.5
22	    step50_train_pass_at_8: 0.8125
23	    step50_val_pass_at_1: 0.25
24	    step50_val_pass_at_8: 0.94
25	    step50_val_action_is_valid: 0.58
26	    step50_entropy: 0.12
27	    step50_ppo_kl: 0.015
28	    train_val_gap_pp: 25
29	    plateau_onset_step: 10
30	    plateau_duration_steps: 40
31	  result_rationale: 'Episode-level GRPO 在 step 10 后进入 plateau（25-28%），训练 success 持续上升至
32	    ~50% 但 val 不跟随—— 经典 overfitting to training distribution。根因：GRPO 的 bandit-style
33	    credit assignment（所有 token 共享同一 advantage） 无法学习 per-step 策略改进。模型学会了 "在训练任务分布上做对的
34	    trajectory pattern"，但缺乏 fine-grained credit 来泛化到 unseen task instance。Entropy
35	    持续下降表明 policy 在 narrowing 但未在 improving。 pass@8=0.94 证明 policy 有能力但 greedy decoding
36	    无法稳定触发正确路径——credit assignment 不够精细， 无法可靠地将 probability mass 集中到 correct action
37	    sequence 上。
38	
39	    '
40	  tables:
41	  - name: Convergence trajectory
42	    columns:
43	    - step
44	    - val_success
45	    - train_success
46	    - val_pass@8
47	    - entropy
48	    - kl
49	    rows:
50	    - - 5
51	      - 0.25
52	      - 0.31
53	      - 0.88
54	      - 0.2
55	      - 0.003
56	    - - 10
57	      - 0.25
58	      - 0.38
59	      - 0.91
60	      - 0.17
61	      - 0.007
62	    - - 15
63	      - 0.28
64	      - 0.44
65	      - 0.93
66	      - 0.15
67	      - 0.01
68	    - - 20
69	      - 0.27
70	      - 0.47
71	      - 0.93
72	      - 0.14
73	      - 0.012
74	    - - 30
75	      - 0.26
76	      - 0.5
77	      - 0.94
78	      - 0.13
79	      - 0.014
80	    - - 40
81	      - 0.25
82	      - 0.5
83	      - 0.94
84	      - 0.12
85	      - 0.015
86	    - - 50
87	      - 0.24
88	      - 0.5
89	      - 0.94
90	      - 0.12
91	      - 0.015
92	  figures_description:
93	  - 'Learning curve: val_success plateau at 25-28% from step 10 onward, train_success
94	    diverging upward to 50%. Classic overfitting gap.'
95	  - 'Entropy decay curve: monotonic decrease from 0.25 → 0.12, policy narrows without
96	    improving generalization.'
97	  analysis: 'Plateau 确认 episode-level GRPO 的根本限制：bandit-style advantage 足以消除 sign
98	    misattribution， 但不足以提供 per-token credit assignment。25-28% 是 "episode-level 能做到的天花板"
99	    在当前 reward density 下。 这是 analysis paper 的核心发现之一：episode-level 解决了 step-independent
100	    的问题但暴露了更深层瓶颈。
101	
102	    '
103	- name: Context window h-sweep ablation (3 seeds each)
104	  plan_id: plan_002
105	  description: h={2, 5, 10, 20, full} sweep，每个 3 seeds，15 steps each
106	  expected_results:
107	    h2_seed1_step15_success: 0.0
108	    h2_seed2_step15_success: 0.03
109	    h2_seed3_step15_success: 0.0
110	    h2_mean: 0.01
111	    h2_std: 0.017
112	    h2_collapse_step_mean: 4.3
113	    h5_seed1_step15_success: 0.06
114	    h5_seed2_step15_success: 0.0
115	    h5_seed3_step15_success: 0.09
116	    h5_mean: 0.05
117	    h5_std: 0.046
118	    h5_collapse_rate: 0.33
119	    h10_seed1_step15_success: 0.12
120	    h10_seed2_step15_success: 0.03
121	    h10_seed3_step15_success: 0.16
122	    h10_mean: 0.103
123	    h10_std: 0.066
124	    h20_seed1_step15_success: 0.19
125	    h20_seed2_step15_success: 0.09
126	    h20_seed3_step15_success: 0.22
127	    h20_mean: 0.167
128	    h20_std: 0.068
129	    full_seed1_step15_success: 0.28
130	    full_seed2_step15_success: 0.19
131	    full_seed3_step15_success: 0.25
132	    full_mean: 0.24
133	    full_std: 0.046
134	    monotonic_ordering_violated: true
135	    h5_occasionally_beats_h10: true
136	    h20_occasionally_collapses: true
137	  result_rationale: 'Worst 档的关键特征：h-sweep 不是 clean monotonic function。h=2 一致崩溃（sign
138	    misattribution + extreme information loss）， 但 h=5 和 h=10 之间、h=10 和 h=20 之间存在 seed
139	    间交叉——某些 seed 下 h=5 偶尔优于 h=10， h=20 偶尔 collapse。这说明 cliff 位置依赖于 random initialization
140	    和 early training dynamics， 而非仅由 h 值决定。高 cross-seed variance 削弱了 "clean cliff at
141	    h=10" 的叙事， 但仍支持 "smaller h systematically worse on average" 的趋势。Non-monotonicity
142	    来自 不同 seed 的 entropy dynamics 差异：某些 seed 早期 exploration 更好，偶尔让 h=5 找到可行策略。
143	
144	    '
145	  tables:
146	  - name: h-sweep summary (step 15, 3 seeds)
147	    columns:
148	    - h
149	    - seed1
150	    - seed2
151	    - seed3
152	    - mean
153	    - std
154	    - collapse_rate
155	    rows:
156	    - - h=2
157	      - 0.0
158	      - 0.03
159	      - 0.0
160	      - 0.01
161	      - 0.017
162	      - 3/3
163	    - - h=5
164	      - 0.06
165	      - 0.0
166	      - 0.09
167	      - 0.05
168	      - 0.046
169	      - 1/3
170	    - - h=10
171	      - 0.12
172	      - 0.03
173	      - 0.16
174	      - 0.103
175	      - 0.066
176	      - 0/3
177	    - - h=20
178	      - 0.19
179	      - 0.09
180	      - 0.22
181	      - 0.167
182	      - 0.068
183	      - 0/3
184	    - - full
185	      - 0.28
186	      - 0.19
187	      - 0.25
188	      - 0.24
189	      - 0.046
190	      - 0/3
191	  figures_description:
192	  - 'Box plot: h vs val_success with individual seed points. Trend is upward but boxes
193	    overlap between adjacent h values. Error bars large.'
194	  - 'Collapse timeline: h=2 collapses by step 4-5 across all seeds; h=5 collapses
195	    in 1/3 seeds; h≥10 no full collapse but h=20 seed2 shows temporary dip.'
196	  analysis: 'Non-monotonic 结果对 paper 是挑战也是机会。不能 claim "clean cliff"，但可以 reframe 为
197	    "credit assignment failure is a stochastic phenomenon whose probability increases
198	    with smaller h"—— 这更符合 analysis paper 的 tone。Cross-seed variance 本身是 failure mode
199	    taxonomy 的一条： "training instability as a function of context window" 是独立 failure
200	    mechanism。 需要从 "threshold effect" 叙事转向 "probabilistic degradation" 叙事。
201	
202	    '
203	- name: Multi-seed replication (5 seeds)
204	  plan_id: plan_003
205	  description: Episode-level GRPO 5 seeds（含 exp029 原始 seed），report mean ± std
206	  expected_results:
207	    seed1_val_success: 0.28
208	    seed2_val_success: 0.19
209	    seed3_val_success: 0.25
210	    seed4_val_success: 0.15
211	    seed5_val_success: 0.3
212	    mean_val_success: 0.234
213	    std_val_success: 0.062
214	    std_pp: 6.2
215	    min_val_success: 0.15
216	    max_val_success: 0.3
217	    range_pp: 15
218	    seeds_above_25pct: 3
219	    seeds_below_20pct: 1
220	    mean_train_success: 0.46
221	    train_val_gap_mean_pp: 22.6
222	  result_rationale: 'Worst 档要求 std > 7pp。这里 std=6.2pp 接近但略低于 7pp 边界——真实的 worst 场景中
223	    5 seeds 可能落在 6-9pp 范围。 关键问题：seed4 只达到 15%（接近 step-independent 水平），说明 episode-level
224	    的优势在某些 seed 下大幅削弱。 这源于 GRPO 的 group normalization 对初始 rollout 分布敏感——如果前几步 rollout
225	    恰好全部失败， advantage 全为 0（无 variance），模型无法获得有效梯度。Seed4 可能经历了 "cold start" 问题： 早期
226	    rollout 全败 → advantage=0 → 无学习 → 持续全败的恶性循环。高 variance 使 95% CI 覆盖 0， 削弱了 episode-level
227	    作为 "solution" 的 claim，但强化了 analysis paper 的叙事—— "即使 episode-level 也不稳定，RL for
228	    LLM agents 需要更根本性的改进"。
229	
230	    '
231	  tables:
232	  - name: Multi-seed results (step 15 checkpoint)
233	    columns:
234	    - seed
235	    - val_success
236	    - train_success
237	    - action_is_valid
238	    - plateau_step
239	    rows:
240	    - - 1
241	      - 0.28
242	      - 0.44
243	      - 0.55
244	      - 10
245	    - - 2
246	      - 0.19
247	      - 0.41
248	      - 0.52
249	      - 8
250	    - - 3
251	      - 0.25
252	      - 0.47
253	      - 0.56
254	      - 10
255	    - - 4
256	      - 0.15
257	      - 0.35
258	      - 0.48
259	      - 12
260	    - - 5
261	      - 0.3
262	      - 0.5
263	      - 0.58
264	      - 10
265	  - name: Summary statistics
266	    columns:
267	    - metric
268	    - mean
269	    - std
270	    - 95% CI
271	    rows:
272	    - - val_success
273	      - 0.234
274	      - 0.062
275	      - '[0.157, 0.311]'
276	    - - train_success
277	      - 0.434
278	      - 0.057
279	      - '[0.363, 0.505]'
280	    - - action_is_valid
281	      - 0.538
282	      - 0.038
283	      - '[0.491, 0.585]'
284	  figures_description:
285	  - Swarm plot with mean ± 95% CI. CI is wide (15.7pp-31.1%), overlaps with step-independent
286	    range for low seeds.
287	  analysis: '95% CI [15.7%, 31.1%] 太宽，无法 credibly claim episode-level "solves" the
288	    problem。 但 mean 仍显著高于 step-independent mean（~2%），所以 "episode-level helps but doesn''t
289	    solve" 是可靠 claim。 Analysis paper framing: 这证明了 credit assignment 问题的多层性——episode-level
290	    消除了 sign misattribution 但暴露了 GRPO 的 cold-start sensitivity 和 bandit-level credit
291	    的根本限制。
292	
293	    '
294	- name: GAE baseline comparison
295	  plan_id: plan_003b
296	  description: GAE(λ=0.95) 和 GAE(λ=1.0, γ=1.0) baselines，15 steps × 3 seeds
297	  expected_results:
298	    gae_095_seed1_success: 0.44
299	    gae_095_seed2_success: 0.38
300	    gae_095_seed3_success: 0.41
301	    gae_095_mean: 0.41
302	    gae_095_std: 0.03
303	    gae_10_10_seed1_success: 0.37
304	    gae_10_10_seed2_success: 0.34
305	    gae_10_10_seed3_success: 0.39
306	    gae_10_10_mean: 0.367
307	    gae_10_10_std: 0.025
308	    episode_grpo_mean: 0.234
309	    gae_095_vs_episode_delta_pp: 17.6
310	    gae_10_vs_episode_delta_pp: 13.3
311	    gae_095_per_token_adv_variance: 0.42
312	    episode_grpo_per_token_adv_variance: 0.0
313	    step_independent_mean: 0.02
314	  result_rationale: 'Worst 档要求 GAE >> episode-level GRPO（delta > 15pp）。GAE(λ=0.95)
315	    达到 41%—— 因为 critic 提供 per-token temporal difference signal，每个 action 获得独立的 advantage
316	    estimate， 而非 GRPO 的 "全 trajectory 同一 advantage"。这是 worst 档的核心发现： episode-level
317	    GRPO 的 plateau 不是 episode-level 本身的问题，而是 GRPO 的 bandit-style credit 的问题。 GAE 通过
318	    value function 提供 fine-grained credit，打破了 plateau。 GAE(λ=1,γ=1) 略低于 GAE(0.95)，因为无
319	    discount 导致 variance 更高。 Delta=17.6pp 直接证明：per-token credit assignment 是关键缺失，episode-level
320	    只是 necessary condition。 这彻底改变 paper story——从 "episode-level solves it" 到 "episode-level
321	    is necessary but per-token credit is the real bottleneck"。
322	
323	    '
324	  tables:
325	  - name: Method comparison (step 15)
326	    columns:
327	    - method
328	    - seed1
329	    - seed2
330	    - seed3
331	    - mean
332	    - std
333	    rows:
334	    - - step-independent (h=2)
335	      - 0.0
336	      - 0.03
337	      - 0.0
338	      - 0.01
339	      - 0.017
340	    - - episode-level GRPO
341	      - 0.28
342	      - 0.19
343	      - 0.25
344	      - 0.24
345	      - 0.046
346	    - - GAE(λ=1,γ=1)
347	      - 0.37
348	      - 0.34
349	      - 0.39
350	      - 0.367
351	      - 0.025
352	    - - GAE(λ=0.95,γ=1)
353	      - 0.44
354	      - 0.38
355	      - 0.41
356	      - 0.41
357	      - 0.03
358	  figures_description:
359	  - 'Bar chart: 4 methods with error bars. Clear staircase: step-ind << episode-GRPO
360	    << GAE(1,1) < GAE(0.95). Gap between GRPO and GAE is the paper''s key diagnostic
361	    finding.'
362	  analysis: 'GAE 的大幅领先是 analysis paper 的最强证据：问题不只是 window-level vs episode-level，
363	    而是 credit granularity 的 spectrum。GRPO episode-level 在 spectrum 中间（消除了 sign error
364	    但无 per-token credit）， GAE 在另一端（full per-token credit via value function）。这支持 failure
365	    mode taxonomy 的第三种机制： "bandit-level credit insufficiency"——即使 advantage 方向正确，所有
366	    token 共享同一 magnitude 也无法 区分 trajectory 中的关键决策点和无关步骤。
367	
368	    '
369	- name: Episode-level + valid_action_bonus
370	  plan_id: plan_003c
371	  description: Episode-level + valid_action_bonus=0.05，测试是否安全突破 plateau
372	  expected_results:
373	    step15_val_success: 0.22
374	    step15_val_action_is_valid: 0.72
375	    step15_train_success: 0.39
376	    valid_bonus_vs_task_ratio: 0.35
377	    gaming_detected: false
378	    success_improvement_vs_baseline: -0.06
379	    action_is_valid_improvement_pp: 17
380	    reward_composition_valid_pct: 0.28
381	    reward_composition_task_pct: 0.72
382	  result_rationale: 'Worst 档下 valid_action_bonus 在 episode-level 中不 game（因为模型优化整条
383	    trajectory total reward）， action_is_valid 确实从 55% 提升到 72%，但 success 反而略降（22% <
384	    28%）。 原因：valid_action_bonus 改变了 reward landscape，使模型偏向 "safe but ineffective"
385	    actions—— valid 但不 goal-directed 的 action（如反复 examine 已知物体）获得持续正 reward， 而 risky
386	    but potentially successful 的 exploration 策略被抑制。Episode-level 下不存在 per-step gaming，
387	    但 dense bonus 仍扭曲了 trajectory-level 的 learning signal——模型学会生成 "很多 valid action
388	    的长 trajectory" 而非 "goal-directed 的短 trajectory"。这是 analysis paper 的另一个 insight：
389	    dense reward 在 episode-level 下的失效模式与 step-independent 不同但同样有害。
390	
391	    '
392	  tables:
393	  - name: valid_action_bonus ablation
394	    columns:
395	    - config
396	    - val_success
397	    - action_is_valid
398	    - avg_trajectory_len
399	    - reward_mean
400	    rows:
401	    - - episode-level (baseline)
402	      - 0.28
403	      - 0.55
404	      - 38.2
405	      - 2.81
406	    - - episode-level + bonus=0.05
407	      - 0.22
408	      - 0.72
409	      - 45.6
410	      - 3.92
411	  figures_description:
412	  - 'Dual-axis plot: action_is_valid improves (good) but success drops (bad). Trajectory
413	    length increases — model generates more valid-but-aimless steps.'
414	  analysis: 'valid_action_bonus 未引入 step-independent 式 gaming，但通过 reward shaping 偏移了
415	    policy gradient direction。 这是 failure mode taxonomy 的第四种机制："reward misalignment
416	    under sparse task signal"—— 当 task reward 稀疏且 episode-level credit 粗糙时，任何 dense
417	    auxiliary reward 都容易主导 learning。 进一步证明 per-token credit（如 GAE）才是根本解。
418	
419	    '
420	- name: Credit assignment mechanism empirical verification
421	  plan_id: plan_004
422	  description: Per-window advantage logging，验证 sign misattribution 机制
423	  expected_results:
424	    sign_vs_outcome_correlation: 0.73
425	    sign_vs_local_quality_correlation: 0.28
426	    magnitude_position_decay_r2: 0.61
427	    episode_level_adv_variance: 0.0
428	    success_episodes_all_positive_pct: 0.78
429	    failure_episodes_all_negative_pct: 0.82
430	    mixed_sign_episodes_pct: 0.2
431	    gamma_k_decay_slope: -0.032
432	    confound_kl_correlation: 0.31
433	    confound_entropy_correlation: 0.27
434	  result_rationale: 'Worst 档的关键：sign-outcome correlation 只有 0.73（而非预期的 >0.95），sign-local_quality
435	    correlation 达到 0.28（而非预期的 ~0）。这意味着 sign misattribution 存在但有显著混杂因素。 Correlation
436	    < 1.0 的原因：GRPO 的 group normalization 使得同一 group 内的 advantage 不完全由 episode outcome
437	    决定—— 如果 group 内所有 episode 都成功（或都失败），normalization 后 advantage 反映 relative 差异而非
438	    absolute 成败。 这在成功率较高的 training episodes 中尤为明显。 Local quality correlation = 0.28
439	    的原因：window-local action quality 与 episode success 本身存在弱正相关 （好的 local action 确实
440	    contribute to success），所以 sign-local 相关性部分反映了 genuine causal path 而非纯 misattribution。这是混杂因素：无法将
441	    sign-local 相关性 100% 归因于 misattribution， 因为部分是 legitimate credit signal。 KL divergence
442	    和 entropy 也与 advantage sign 相关（r=0.31, 0.27），说明 policy drift 和 exploration dynamics
443	    独立影响 advantage distribution。
444	
445	    '
446	  tables:
447	  - name: Mechanism verification (h=2, seed 2, step 5)
448	    columns:
449	    - metric
450	    - observed
451	    - hypothesis
452	    - status
453	    rows:
454	    - - sign-outcome corr
455	      - 0.73
456	      - '>0.95'
457	      - PARTIAL — significant confounds
458	    - - sign-local_quality corr
459	      - 0.28
460	      - <0.1
461	      - FAILED — non-negligible correlation
462	    - - magnitude decay R²
463	      - 0.61
464	      - '>0.85'
465	      - PARTIAL — decay exists but noisy
466	    - - episode-level adv variance
467	      - 0.0
468	      - '0.0'
469	      - CONFIRMED
470	    - - '% success eps all-positive'
471	      - 78%
472	      - '>95%'
473	      - PARTIAL — 22% have mixed signs
474	  - name: Confound analysis
475	    columns:
476	    - confound_variable
477	    - correlation_with_adv_sign
478	    - p_value
479	    rows:
480	    - - episode_outcome
481	      - 0.73
482	      - <0.001
483	    - - local_action_quality
484	      - 0.28
485	      - <0.01
486	    - - KL_divergence
487	      - 0.31
488	      - <0.01
489	    - - entropy
490	      - 0.27
491	      - <0.01
492	    - - window_position
493	      - -0.18
494	      - <0.05
495	  figures_description:
496	  - 'Scatter: advantage sign vs episode outcome (color=local quality). Not the clean
497	    binary separation expected — significant overlap region.'
498	  - 'Partial correlation decomposition: pie chart showing episode outcome explains
499	    53%, local quality 16%, KL 10%, entropy 8%, unexplained 13%.'
500	  analysis: 'Sign misattribution 存在但不是 sole mechanism——这是 worst 档的核心困难。不能 claim "advantage
501	    sign is entirely determined by episode outcome"。 需要 reframe 为 "sign misattribution
502	    is the dominant but not sole factor in credit assignment failure"。 混杂因素（KL drift、entropy
503	    dynamics）本身成为 failure mode taxonomy 的独立条目。 Partial correlation decomposition 成为
504	    analysis paper 的关键贡献：量化每种机制对 credit assignment failure 的贡献占比。
505	
506	    '
507	- name: Action-change statistics from always-on runs
508	  plan_id: plan_005
509	  description: 从 exp029 checkpoint 收集 action-change 统计
510	  expected_results:
511	    action_change_rate: 0.18
512	    confirmatory_rate: 0.82
513	    action_change_success_correlation: 0.08
514	    action_change_success_p_value: 0.12
515	    per_task_action_change_std: 0.09
516	    pick_action_change_rate: 0.12
517	    clean_action_change_rate: 0.22
518	    heat_action_change_rate: 0.2
519	    cool_action_change_rate: 0.15
520	    examine_action_change_rate: 0.25
521	  result_rationale: 'Worst 档下 action-change-success correlation 仅 0.08 且 p=0.12（不显著）。
522	    原因：episode-level model 只有 25% success rate，样本中 successful episodes 太少导致 statistical
523	    power 不足。 更根本的问题：在 25% success 的 agent 上，action change 基本是 noise—— model 的 verification
524	    输出质量太低，无论是否 change action 都可能是随机的。 Confirmatory rate 82% 符合预期（大部分 verification
525	    不改变行为）， 但这也意味着 action change 事件太稀疏（只有 18%），与 success 的 correlation 在统计上不可靠。 这直接阻碍了
526	    Phase B：如果 action change 不是 success 的有效 signal， 用它作 intrinsic reward 没有理论基础。
527	
528	    '
529	  tables:
530	  - name: Action-change statistics
531	    columns:
532	    - metric
533	    - value
534	    rows:
535	    - - overall action change rate
536	      - 18%
537	    - - confirmatory rate
538	      - 82%
539	    - - action_change-success correlation
540	      - r=0.08, p=0.12
541	    - - N (episodes)
542	      - 128
543	    - - N (verification events)
544	      - 2304
545	    - - N (action changes)
546	      - 415
547	  figures_description:
548	  - 'Contingency table heatmap: action_change × episode_success. No clear pattern
549	    — action change is roughly equally distributed across success/failure episodes.'
550	  analysis: 'Action change 作为 intrinsic reward 缺乏 empirical grounding。在 worst 档下，
551	    这个结果直接导致 Claim 2 无法成立——selective verification 失去了 reward signal。 Analysis paper
552	    中可以作为 "why selective verification is hard for weak agents" 的一个 finding。
553	
554	    '
555	- name: Selective verification implementation
556	  plan_id: plan_006
557	  description: Code-only：实现 binary verify/skip decision
558	  expected_results:
559	    implementation_status: completed
560	    code_changes_files: 4
561	    gpu_hours: 0
562	  result_rationale: '纯代码实现，不依赖实验结果。在 worst 档下仍可完成，但后续使用这个 implementation 的实验效果差。
563	
564	    '
565	  tables: []
566	  figures_description: []
567	  analysis: 'Implementation 本身无 worst 档问题。但 plan_005 的 weak correlation 预示 plan_007
568	    会失败。
569	
570	    '
571	- name: B-IAVR selective verification training
572	  plan_id: plan_007
573	  description: 用 action-change reward 训练 selective verification policy
574	  expected_results:
575	    verification_rate_reduction_pct: 12
576	    val_success: 0.16
577	    baseline_always_on_success: 0.25
578	    success_delta_pp: -9
579	    training_converged: false
580	    reward_signal_informative: false
581	    verification_rate: 0.88
582	    policy_learned_skip: false
583	    training_steps_before_abort: 20
584	  result_rationale: 'Worst 档：selective verification 无法 deliver clear win。两个根因叠加： (1)
585	    plan_005 显示 action-change 不是有效 signal（r=0.08, p=0.12），用它做 reward 等于训练 on noise；
586	    (2) base agent 只有 25% success，skip verification 直接降低 performance 且模型无法学会 when
587	    to skip。 Verification rate 只降了 12%（模型几乎总是 verify），因为 skip 的 penalty（success 下降）远大于
588	    action-change reward 的 bonus。Policy 本质上退化为 "always verify"—— 因为在 25% success 的
589	    agent 上，任何 skip 都有显著 performance cost。 Success 降至 16%（比 baseline 低 9pp），因为即使少量的
590	    skip 也损害了 performance。
591	
592	    '
593	  tables:
594	  - name: B-IAVR results
595	    columns:
596	    - policy
597	    - val_success
598	    - verification_rate
599	    - cost_reduction
600	    rows:
601	    - - always-on
602	      - 0.25
603	      - 100%
604	      - 0%
605	    - - B-IAVR (learned)
606	      - 0.16
607	      - 88%
608	      - 12%
609	    - - random-50%
610	      - 0.14
611	      - 50%
612	      - 50%
613	    - - no-verify
614	      - 0.13
615	      - 0%
616	      - 100%
617	  figures_description:
618	  - 'Pareto frontier: success vs cost. B-IAVR barely separates from always-on, nowhere
619	    near efficient frontier.'
620	  analysis: 'Selective verification 在 worst 档下完全无法作为 paper contribution。 必须移入 future
621	    work，framed as "requires stronger base agent + better reward signal"。
622	
623	    '
624	- name: Selective verification full comparison
625	  plan_id: plan_008
626	  description: Always-on / B-IAVR / no-verify / random-p / confidence 对比
627	  expected_results:
628	    always_on_success: 0.25
629	    always_on_verify_rate: 1.0
630	    biavr_success: 0.16
631	    biavr_verify_rate: 0.88
632	    no_verify_success: 0.13
633	    no_verify_rate: 0.0
634	    random_50_success: 0.14
635	    random_50_rate: 0.5
636	    confidence_success: 0.19
637	    confidence_verify_rate: 0.65
638	    biavr_dominates_pareto: false
639	    best_cost_performance: confidence-threshold
640	  result_rationale: 'Worst 档：B-IAVR 不 dominate Pareto frontier。Confidence-based baseline
641	    意外优于 B-IAVR—— 因为 confidence threshold 是 model-intrinsic signal（policy entropy），
642	    比 action-change 这个 noisy extrinsic signal 更 informative。 Confidence 方法在 entropy
643	    高时 verify（不确定时检查），在 entropy 低时 skip（确定时省略）， 这 naturally 对齐 "verification is useful
644	    when uncertain"。 B-IAVR 学到的 policy 没有这种 alignment 因为 training signal 太弱。 所有 selective
645	    方法都比 always-on 差（delta > 5pp），因为 base agent 太弱—— verification 在 25% agent 上几乎总是有用的（因为
646	    agent 经常犯错）。
647	
648	    '
649	  tables:
650	  - name: Full comparison (step 15 checkpoint, 128 val episodes)
651	    columns:
652	    - method
653	    - success
654	    - verify_rate
655	    - total_tokens
656	    - success_per_token
657	    rows:
658	    - - always-on
659	      - 25.0%
660	      - 100%
661	      - 1.0x
662	      - '0.250'
663	    - - confidence-0.5
664	      - 19.0%
665	      - 65%
666	      - 0.72x
667	      - '0.264'
668	    - - B-IAVR
669	      - 16.0%
670	      - 88%
671	      - 0.93x
672	      - '0.172'
673	    - - random-50%
674	      - 14.0%
675	      - 50%
676	      - 0.62x
677	      - '0.226'
678	    - - no-verify
679	      - 13.0%
680	      - 0%
681	      - 0.45x
682	      - '0.289'
683	  figures_description:
684	  - 'Pareto frontier plot: no-verify has best token-efficiency (trivially), confidence-threshold
685	    dominates B-IAVR. B-IAVR is dominated — not on the frontier.'
686	  analysis: 'B-IAVR 被 confidence baseline dominate，这对 Claim 3 是致命的。 但 analysis paper
687	    可以 reframe：展示为什么 RL-trained selective verification 在 weak agents 上失败—— action-change
688	    signal 需要 base agent 足够强才有意义（类比：你不能教一个 25% accuracy 的学生 when to double-check）。
689	
690	    '
691	- name: No-verify ablation
692	  plan_id: plan_009
693	  description: Episode-level GRPO without self-verification
694	  expected_results:
695	    val_success: 0.13
696	    val_action_is_valid: 0.42
697	    always_on_success: 0.25
698	    delta_pp: -12
699	    avg_trajectory_length: 28.5
700	    avg_trajectory_length_with_verify: 41.3
701	  result_rationale: 'No-verify 比 always-on 低 12pp，确认 verification 有价值。 但在 worst 档下这个
702	    delta 略小于预期的 ≥10pp（12pp 刚过线）， 因为 weak agent 的 verification 质量也不高——agent 经常 verify
703	    但 verification 本身也是 noisy。 Action_is_valid 从 55% 降到 42%，说明 verification 确实帮助 format
704	    compliance。 Trajectory 更短（28 vs 41 steps）因为没有 verification 步骤。
705	
706	    '
707	  tables:
708	  - name: Verification ablation
709	    columns:
710	    - config
711	    - success
712	    - action_is_valid
713	    - avg_steps
714	    - avg_tokens
715	    rows:
716	    - - always-on verify
717	      - 25.0%
718	      - 55%
719	      - 41.3
720	      - 4850
721	    - - no verify
722	      - 13.0%
723	      - 42%
724	      - 28.5
725	      - 2980
726	    - - delta
727	      - -12pp
728	      - -13pp
729	      - '-12.8'
730	      - '-1870'
731	  figures_description:
732	  - 'Paired bar chart: with/without verification across task types.'
733	  analysis: 'Verification 有价值（-12pp），但价值不足以支撑 "selective verification as primary contribution"。
734	    在 analysis paper 中，这是一个 supporting data point：verification matters， 但 training
735	    agents to be selective about it requires solving the credit assignment problem
736	    first。
737	
738	    '
739	- name: Entropy-controlled action-change analysis
740	  plan_id: plan_010
741	  description: Stratify action-change-success correlation by policy entropy
742	  expected_results:
743	    overall_correlation: 0.08
744	    overall_p_value: 0.12
745	    low_entropy_partial_corr: 0.05
746	    low_entropy_p_value: 0.41
747	    medium_entropy_partial_corr: 0.09
748	    medium_entropy_p_value: 0.18
749	    high_entropy_partial_corr: 0.12
750	    high_entropy_p_value: 0.09
751	    partial_correlation_controlling_entropy: 0.07
752	    partial_p_value: 0.15
753	  result_rationale: 'Worst 档：partial correlation 在控制 entropy 后仍不显著（r=0.07, p=0.15）。
754	    Action change 与 success 的微弱相关几乎完全由 entropy 解释—— 高 entropy 时更容易 change action（因为
755	    policy 本身不确定）， 高 entropy 任务也更可能成功（因为 exploration 更充分）。 控制 entropy 后 action change
756	    本身对 success 没有独立贡献。 这直接否定了 "action change as causal signal for verification quality"
757	    的假设。
758	
759	    '
760	  tables:
761	  - name: Entropy-stratified analysis
762	    columns:
763	    - entropy_stratum
764	    - N
765	    - action_change_rate
766	    - success_rate
767	    - corr
768	    - p
769	    rows:
770	    - - low (<0.10)
771	      - 768
772	      - 11%
773	      - 18%
774	      - 0.05
775	      - 0.41
776	    - - medium (0.10-0.20)
777	      - 896
778	      - 17%
779	      - 24%
780	      - 0.09
781	      - 0.18
782	    - - high (>0.20)
783	      - 640
784	      - 28%
785	      - 31%
786	      - 0.12
787	      - 0.09
788	    - - partial (controlling entropy)
789	      - 2304
790	      - '-'
791	      - '-'
792	      - 0.07
793	      - 0.15
794	  figures_description:
795	  - '3-panel scatter: action_change vs success within each entropy stratum. No clear
796	    trend in any panel.'
797	  analysis: 'Action change 不是 independent signal——它是 entropy 的 proxy。 这对 Claim 2 是
798	    additional nail in the coffin。Analysis paper framing： "apparent verification informativeness
799	    signals are confounded with policy uncertainty"， 这是 selective verification failure
800	    的又一个 identified mechanism。
801	
802	    '
803	- name: 'Causal intervention: random vs verification-triggered changes'
804	  plan_id: plan_011
805	  description: 注入 random action changes vs verification-triggered，对比 success
806	  expected_results:
807	    verification_triggered_success: 0.27
808	    random_change_success: 0.21
809	    no_change_success: 0.25
810	    triggered_vs_random_delta_pp: 6
811	    triggered_vs_random_p_value: 0.08
812	    triggered_vs_baseline_delta_pp: 2
813	    random_vs_baseline_delta_pp: -4
814	  result_rationale: 'Worst 档：verification-triggered changes 仅比 random 好 6pp（p=0.08，边缘不显著）。
815	    这弱于预期的 ≥10pp。原因：agent 只有 25% success，verification 质量差， triggered changes 只是 "slightly
816	    better than random" 而非 "causally informative"。 有趣的是 triggered 甚至只比 no-change baseline
817	    好 2pp——说明 change 本身（无论来源） 引入了 noise，verification-triggered change 的微弱优势几乎被 change-induced
818	    noise 抵消。
819	
820	    '
821	  tables:
822	  - name: Causal intervention results
823	    columns:
824	    - condition
825	    - success
826	    - N_episodes
827	    - 95% CI
828	    rows:
829	    - - no change (baseline)
830	      - 25.0%
831	      - 128
832	      - '[17.5%, 32.5%]'
833	    - - verification-triggered change
834	      - 27.0%
835	      - 128
836	      - '[19.3%, 34.7%]'
837	    - - random change (matched rate)
838	      - 21.0%
839	      - 128
840	      - '[13.9%, 28.1%]'
841	  figures_description:
842	  - 'Bar chart with CI: three conditions. All CIs overlap heavily.'
843	  analysis: 'Causal evidence for verification-triggered > random is weak (p=0.08)。
844	    CIs 大量重叠，no significant difference。这进一步 disqualifies action-change as reward signal。
845	
846	    '
847	- name: Reward signal ablation (action-change vs alternatives)
848	  plan_id: plan_012
849	  description: 对比 action-change / random / confidence-based reward
850	  expected_results:
851	    action_change_reward_success: 0.16
852	    action_change_reward_verify_rate: 0.88
853	    random_reward_success: 0.15
854	    random_reward_verify_rate: 0.85
855	    confidence_reward_success: 0.19
856	    confidence_reward_verify_rate: 0.62
857	    all_below_always_on: true
858	    best_method: confidence-based
859	  result_rationale: 'Worst 档：所有 reward variants 都比 always-on 差。Action-change reward
860	    与 random reward 表现几乎一样（delta < 2pp），证实 action-change 不比 random noise 更好。 Confidence-based
861	    reward 稍好因为它利用了 model-intrinsic uncertainty 而非 extrinsic noisy signal。 但即使最好的
862	    variant 也比 always-on 低 6pp。 核心问题：base agent 太弱时，所有 selective strategies 都退化为 "less
863	    verification = worse performance"。
864	
865	    '
866	  tables:
867	  - name: Reward ablation
868	    columns:
869	    - reward_type
870	    - success
871	    - verify_rate
872	    - token_cost
873	    rows:
874	    - - always-on (no skip)
875	      - 25.0%
876	      - 100%
877	      - 1.0x
878	    - - action-change
879	      - 16.0%
880	      - 88%
881	      - 0.93x
882	    - - random trigger
883	      - 15.0%
884	      - 85%
885	      - 0.90x
886	    - - confidence-based
887	      - 19.0%
888	      - 62%
889	      - 0.72x
890	  figures_description:
891	  - 'Cost-performance Pareto: confidence-based is on frontier, action-change and random
892	    are dominated.'
893	  analysis: 'Action-change reward 无法区分于 random——这是对 Claim 2 的最终否定。 全部移入 future work："selective
894	    verification requires (1) stronger base agent, (2) better reward signal"。
895	
896	    '
897	- name: ARES reproduction + comparison
898	  plan_id: plan_013
899	  description: 复现 ARES SFT router，与 B-IAVR 对比
900	  expected_results:
901	    ares_success: 0.22
902	    ares_verify_rate: 0.7
903	    ares_cost_reduction: 0.3
904	    biavr_success: 0.16
905	    biavr_verify_rate: 0.88
906	    biavr_cost_reduction: 0.12
907	    ares_dominates_biavr: true
908	    delta_success_pp: 6
909	    delta_cost_reduction_pp: 18
910	  result_rationale: 'Worst 档：ARES SFT router 优于 B-IAVR。SFT router 使用 supervised learning
911	    from oracle labels（何时 verify 有帮助），不依赖 RL training signal quality。 因此 ARES 不受 action-change
912	    noise 影响。B-IAVR 的 RL-trained policy 在 weak reward signal 下退化为 near-always-verify，丧失了
913	    cost reduction 优势。 这进一步证明在 weak agent 设定下 SFT > RL for selective verification。
914	
915	    '
916	  tables:
917	  - name: ARES vs B-IAVR
918	    columns:
919	    - method
920	    - success
921	    - verify_rate
922	    - cost_red
923	    - dominates
924	    rows:
925	    - - ARES (SFT)
926	      - 22.0%
927	      - 70%
928	      - 30%
929	      - 'yes'
930	    - - B-IAVR (RL)
931	      - 16.0%
932	      - 88%
933	      - 12%
934	      - 'no'
935	  figures_description:
936	  - Pareto plot with ARES and B-IAVR. ARES clearly dominates.
937	  analysis: 'ARES domination 在 worst 档下是 expected——SFT with oracle labels 是 easier
938	    optimization problem。 Analysis paper 可以 acknowledge this 并 discuss when RL might
939	    outperform SFT (hypothetically: when base agent is strong enough for action-change
940	    to be meaningful signal)。
941	
942	    '
943	- name: ScienceWorld transfer
944	  plan_id: plan_014
945	  description: ScienceWorld 上验证 episode-level vs step-independent
946	  expected_results:
947	    episode_level_success: 0.15
948	    step_independent_success: 0.03
949	    ratio: 5.0
950	    episode_level_std: 0.08
951	    step_independent_std: 0.02
952	  result_rationale: 'Worst 档下 episode-level 仍优于 step-independent（5x），但绝对数值低。 ScienceWorld
953	    任务更长更复杂（平均 40+ steps），episode-level 的 bandit credit 更吃力。 但 step-independent 在
954	    ScienceWorld 上也崩溃（3%），证明问题不是 ALFWorld-specific。 这支持 analysis paper 的 generalizability
955	    claim，但低绝对值（15%）进一步证明 episode-level 不够——需要 finer credit。High std (8pp) 说明 instability
956	    也泛化。
957	
958	    '
959	  tables:
960	  - name: ScienceWorld transfer
961	    columns:
962	    - method
963	    - success
964	    - std
965	    - vs_step_independent
966	    rows:
967	    - - step-independent
968	      - 3%
969	      - 2pp
970	      - baseline
971	    - - episode-level
972	      - 15%
973	      - 8pp
974	      - 5x
975	  figures_description:
976	  - 'Cross-environment comparison: ALFWorld + ScienceWorld paired bars. Same trend
977	    (episode > step-ind) but lower absolute for ScienceWorld.'
978	  analysis: 'Transfer 验证了 finding 的 generalizability。两个环境一致：episode-level 解决了 step-independent
979	    的崩溃， 但自身也有 ceiling。ScienceWorld 的 lower ceiling（15% vs 25%）反映更长 horizon 的 credit
980	    challenge。
981	
982	    '
983	- name: 7B model scaling verification
984	  plan_id: plan_015
985	  description: Qwen3-7B 上验证 episode-level vs step-independent
986	  expected_results:
987	    episode_level_7b_success: 0.32
988	    step_independent_7b_success: 0.08
989	    episode_level_1_7b_success: 0.25
990	    step_independent_1_7b_success: 0.01
991	    scaling_gain_episode_pp: 7
992	    scaling_gain_step_ind_pp: 7
993	    ratio_7b: 4.0
994	    ratio_1_7b: 25.0
995	  result_rationale: 'Worst 档：7B 提升两种方法各约 7pp（近乎 parallel shift），episode-level 优势 ratio
996	    缩小（4x vs 25x at 1.7B）。 Step-independent 在 7B 上不再完全崩溃（8% vs 1%），因为 larger model
997	    有更好的 in-context learning 能力， 部分补偿了 credit assignment 问题。但 episode-level 仍然 superior。
998	    对 paper 的含义：episode-level 优势在 larger model 上缩小——可能 scaling 本身 partially mitigates
999	    credit assignment failures（模型 in-context 能力可以补偿 training signal noise）。 这是 analysis
1000	    paper 的一个 nuanced finding。
1001	
1002	    '
1003	  tables:
1004	  - name: Scaling comparison
1005	    columns:
1006	    - model
1007	    - episode-level
1008	    - step-independent
1009	    - ratio
1010	    rows:
1011	    - - Qwen3-1.7B
1012	      - 25%
1013	      - 1%
1014	      - 25x
1015	    - - Qwen3-7B
1016	      - 32%
1017	      - 8%
1018	      - 4x
1019	  figures_description:
1020	  - '2×2 bar chart: model × method. Episode-level advantage shrinks at scale but persists.'
1021	  analysis: 'Scaling 结果 nuances the story：credit assignment 问题 severity 与 model size
1022	    负相关， 但不消失。Analysis paper 可以 speculate：at sufficient scale（70B+）， in-context learning
1023	    可能完全 compensate——这是 "why big-lab RL works but small-model RL fails" 的一个 hypothesis。
1024	
1025	    '
1026	- name: Per-task-type breakdown analysis
1027	  plan_id: plan_016
1028	  description: 按 ALFWorld 任务类型 breakdown episode-level performance
1029	  expected_results:
1030	    pick_success: 0.35
1031	    clean_success: 0.22
1032	    heat_success: 0.2
1033	    cool_success: 0.18
1034	    examine_success: 0.3
1035	    pick_two_success: 0.1
1036	    episode_length_correlation: 0.48
1037	    task_complexity_correlation: -0.62
1038	  result_rationale: 'Worst 档下，simple tasks（pick: 35%, examine: 30%）显著优于 complex tasks（pick_two:
1039	    10%, cool: 18%）。 Task complexity-success correlation = -0.62：越复杂越差，符合 credit assignment
1040	    bottleneck 假说—— longer horizons = more steps sharing same advantage = coarser
1041	    credit = worse learning。 Pick_two 最差因为需要 two sequential subtask completions，episode-level
1042	    advantage 无法 区分第一个 pick 的 credit 和第二个 pick 的 credit。 这个 breakdown 对 analysis paper
1043	    有价值：展示 failure 不均匀， task structure（horizon length、subtask decomposition）直接影响 credit
1044	    assignment quality。
1045	
1046	    '
1047	  tables:
1048	  - name: Per-task breakdown (episode-level, 5-seed mean)
1049	    columns:
1050	    - task_type
1051	    - success
1052	    - std
1053	    - avg_steps
1054	    - n_subtasks
1055	    rows:
1056	    - - pick
1057	      - 35%
1058	      - 5pp
1059	      - 28
1060	      - 1
1061	    - - examine
1062	      - 30%
1063	      - 6pp
1064	      - 32
1065	      - 1
1066	    - - clean
1067	      - 22%
1068	      - 7pp
1069	      - 35
1070	      - 2
1071	    - - heat
1072	      - 20%
1073	      - 8pp
1074	      - 37
1075	      - 2
1076	    - - cool
1077	      - 18%
1078	      - 7pp
1079	      - 38
1080	      - 2
1081	    - - pick_two
1082	      - 10%
1083	      - 9pp
1084	      - 45
1085	      - 2
1086	  figures_description:
1087	  - Grouped bar chart by task type, sorted by complexity. Clear downward trend.
1088	  - 'Scatter: avg_episode_length vs success per task type, r=-0.62.'
1089	  analysis: Task-level breakdown 是 analysis paper 的 key supporting evidence： credit
1090	    assignment failure severity 与 task horizon 和 subtask decomposition 正相关。 pick_two
1091	    的 10% 证明 episode-level bandit credit 无法处理 multi-subtask credit separation。 这 motivates
1092	    future work on hierarchical credit assignment（per-subtask reward 或 option-level
1093	    advantage）。
1094	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2a45f6c-a529-460f-9ab8-afac34f603a0",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "a5b02fdfddc805fc8",
  "type": "user",
  "uuid": "389ccb0d-93c3-4371-b471-1bab00f4367c",
  "sourceToolAssistantUUID": "f2a45f6c-a529-460f-9ab8-afac34f603a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-17T12:55:50.841Z_

Now I have comprehensive context. Let me read the paper framing one more time to check for the review context mentioned in the task prompt, then produce my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "389ccb0d-93c3-4371-b471-1bab00f4367c",
  "isSidechain": true,
  "agentId": "a5b02fdfddc805fc8",
  "requestId": "req_011Cb8BDtEkHVB11874XKXoC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d722dffa-45cd-4970-9691-afadbaeb850b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4vcUZtTRhsjH5w5cB4P1f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16553,
      "cache_read_input_tokens": 58684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16553,
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

_source line 29 · 2026-05-17T12:55:51.752Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UHNA4gxkpx9xLQo9BpfXcE`</summary>

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
  "parentUuid": "d722dffa-45cd-4970-9691-afadbaeb850b",
  "isSidechain": true,
  "agentId": "a5b02fdfddc805fc8",
  "requestId": "req_011Cb8BDtEkHVB11874XKXoC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d00a9065-3622-4c23-b9d3-e73297e4434e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4vcUZtTRhsjH5w5cB4P1f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16553,
      "cache_read_input_tokens": 58684,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16553
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 58684,
          "cache_creation_input_tokens": 16553,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16553,
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

_source line 30 · 2026-05-17T12:55:51.755Z_

<details><summary>↩ Tool result · `toolu_01UHNA4gxkpx9xLQo9BpfXcE`</summary>

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
  "parentUuid": "d00a9065-3622-4c23-b9d3-e73297e4434e",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "a5b02fdfddc805fc8",
  "type": "user",
  "uuid": "c253bf87-34c1-4d44-83b1-2dd454b0d4b8",
  "sourceToolAssistantUUID": "d00a9065-3622-4c23-b9d3-e73297e4434e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
