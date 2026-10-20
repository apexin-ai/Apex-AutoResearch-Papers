# Research conversation: You are Reviewer 1 (R1) in an academic peer review. Your focus is **methodology and experiments**. ## Paper Summary Titl

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a6854eb8e8fb54b59.jsonl`
- **Structured JSON:** [`9c957943573d9f3fdbde.json`](../../sessions/9c/9c957943573d9f3fdbde.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

35 recorded events

### User

_source line 1 · 2026-05-20T09:10:24.774Z_

You are Reviewer 1 (R1) in an academic peer review. Your focus is **methodology and experiments**.

## Paper Summary
Title: "IRT-FIT: Detecting Benchmark Contamination in Large Language Models via Item Response Theory Person-Fit Statistics"

The paper repurposes IRT person-fit statistics (lz*) from psychometrics to detect benchmark contamination in LLMs. Three contributions:
1. Two-sided detection framework capturing both partial contamination (lz* << 0, aberrant patterns) and full contamination (lz* >> 0, over-consistent patterns), with BH-FDR control.
2. Theoretical power formula: power ≈ Φ(δ√n/σ − z_α), relating detection power to n_items and contamination level. Inverted-U signal structure with analytically derivable inflection point. R²=0.97 fit to simulation.
3. Large-scale audit of 2,847 Open LLM Leaderboard models revealing 12% flagged rate.

## Key Method Details
- Uses 4PL IRT model: P_i(θ) = c_i + (d_i − c_i) · 1/(1+exp(−a_i(θ−b_i)))
- lz statistic (Drasgow et al., 1985) standardized to lz* (Snijders, 2001) ~ N(0,1) under null
- Two-sided test: |lz*| > c_{α/2} with BH-FDR correction
- Multiscale aggregation lzm = (1/√K) Σ|lz*_k| (Hong et al., 2021)
- Power theory derived from Snijders' variance formula
- Inverted-U inflection point formula: c* = argmin_c |E_θ[Σf(x_i, P_i)|contam=c] − E_θ[Σf(x_i, P_i)|contam=0]|

## Controlled Experiments
- QLoRA SFT on Qwen3.5-9B and Gemma-4-31B at 0%/5%/10%/15%/25%/50% MMLU items
- Ground-truth contamination → lz* mapping established
- Table 1: lz* monotonically increases in |value| from 0→25%, then decreases at 50% (inverted-U)
- Table 2: AUROC 0.82 at 5%, 0.96 at 15%, 0.99 at 25% (pooled)
- Table 3: Contamination selectivity — +31pp lift on contaminated items, only +1.4-3.7% on non-contaminated
- Cohen's d = 2.3 at 15%, FPR 0.042/0.041 at α=0.05

## Extended Simulation
- Table 4: lz* across 0-100% contamination (4 benchmarks, 100 replications). Shows inverted-U: peaks negative at 25%, crosses zero near 60-65%, becomes strongly positive at 75-100%
- Table 5: Two-sided power at various contamination levels. Power dips at 50% but recovers at 75%+

## Power Theory
- Table 6: Theoretical vs simulated power at 15% contamination across n_items 100-14042. Max |Δ|=0.014
- Table 7: Inverted-U inflection point predicted vs observed: error ≤ 0.02 for all 5 benchmarks
- Table 8: Min n_items for 80% power: 3,200 at 15%, 9,800 at 5%

## Baselines
- Table 9: IRT-FIT 0.96 vs ConStat 0.83 vs Min-K%++ 0.88 at 15% (AUROC)
- Table 10: Detection frontier — IRT-FIT at "binary only" level, others need more info

## Post-RL Robustness
- Table 11: lz* drops from -8.91 to -7.12 after GRPO, AUROC 0.96→0.92
- Table 12: IRT-FIT retains 96% AUROC, Min-K%++ retains 70%, MIA retains 76% (drops to 0.54)

## 4PL vs 3PL
- Table 13: 4PL AUROC 0.960 vs 3PL 0.910 at 15%; false alarm 0.042 vs 0.078
- Table 14: d parameter impact concentrated on high-difficulty items (difficulty > 2.5)

## Multiscale lzm
- Table 15: lzm on 12 PSN-IRT models. Gemini-1.5 lzm=18.42 (flagged), GPT-4 -0.87 (not flagged)
- Table 16: lzm AUROC 0.98 vs single-benchmark 0.96

## Large-Scale Empirical Study
- Table 17: Two-sided detection on PSN-IRT 12 models. Gemini-1.5 flagged on MMLU (+34.75), GSM8K (-15.71), HumanEval (-12.37)
- Table 18: One-sided catches 2 models, two-sided catches 4
- Table 19: Leaderboard audit: 2,847 models, 12% overall flagged rate, MMLU highest at 15%
- Table 20: Contamination rate by time period: 6% (2023Q1) → 18% (2024Q1)
- Table 21: Top 3 most anomalous models
- Table 22: Power across 7 benchmarks (adding BBH 6511, MATH 5000). Theory predictions within 1-2%
- Table 23: MMLU domain-level analysis. Gemini-1.5 100% across all 57 domains
- Table 24: Domain-level power matches theory predictions within 2-3pp

## Experiment Design Reference (from review_context.yaml)
The planned experiments include:
1. Two-Sided Detection Framework (exp-two-sided) — covered in Tables 17-18
2. Extended Simulation (exp-extended-sim) — covered in Tables 4-5
3. Controlled Contamination (exp-ctrl-contam) — covered in Tables 1-3
4. Power Theory Derivation (exp-power-theory) — covered in Tables 6-8
5. Leaderboard Audit (exp-leaderboard-audit) — covered in Tables 19-21
6. 4PL vs 3PL Ablation (exp-4pl-ablation) — covered in Tables 13-14
7. Baseline Comparison (exp-baseline-comparison) — covered in Tables 9-10
8. Multiscale lzm (exp-multiscale-lzm) — covered in Tables 15-16
9. Post-RL Hypothesis Test (exp-post-rl) — covered in Tables 11-12
10. Extra Benchmarks BBH/MATH (exp-extra-benchmarks) — covered in Table 22
11. Domain-Level Analysis (exp-domain-analysis) — covered in Tables 23-24

## Your Task
Write a detailed review covering:

1. **Methodology Soundness**: Is the method well-motivated? Are the statistical foundations correct? Is the two-sided extension justified? Is the power theory derivation rigorous?

2. **Experimental Design**: Are the controlled experiments well-designed? Is the ground-truth contamination setup realistic? Are baselines fairly compared? Is the leaderboard audit methodology sound?

3. **Results Analysis**: Do the results support the claims? Are there gaps between claimed and demonstrated results? Any suspicious patterns in the numbers?

4. **Reproducibility**: Is there enough detail to reproduce? Are the IRT model parameters (from PSN-IRT) properly credited/described?

5. **Limitations and Concerns**: What are the key weaknesses? What assumptions might not hold?

6. **Specific Questions for Authors**: List 3-5 specific technical questions.

7. **Score**: Rate on 1-6 scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue: top ML venue, ~25% acceptance rate.

8. **Confidence**: 1-5 scale (1=low, 5=expert).

Format your review clearly with headers. Be rigorous but fair. ~1500 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a6854eb8e8fb54b59",
  "type": "user",
  "uuid": "97d2c8d3-573e-4ce2-aa91-632038adb73a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T09:10:24.792Z_

```json
{
  "parentUuid": "97d2c8d3-573e-4ce2-aa91-632038adb73a",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
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
  "uuid": "21e576a6-3198-4abd-9295-48c031aa6199",
  "timestamp": "2026-05-20T09:10:24.792Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T09:10:27.711Z_



I'll start by reading the paper and related project files to ground my review in the actual content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21e576a6-3198-4abd-9295-48c031aa6199",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZTqQK5cBv9hQEXsUXW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe3121cc-c3ae-423d-9721-0b6e5cddfbd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013CuQ1tRoUB9fgfzDhvUveV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16650,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16650,
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

_source line 4 · 2026-05-20T09:10:28.176Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WNSZg6yZ3Rg3irNN7B5qFh`</summary>

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
  "parentUuid": "fe3121cc-c3ae-423d-9721-0b6e5cddfbd6",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZTqQK5cBv9hQEXsUXW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1c18c44-bcfa-4d31-acae-947de3d82802",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013CuQ1tRoUB9fgfzDhvUveV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16650,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16650,
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

_source line 5 · 2026-05-20T09:10:28.196Z_

<details><summary>↩ Tool result · `toolu_01WNSZg6yZ3Rg3irNN7B5qFh`</summary>

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
  "parentUuid": "f1c18c44-bcfa-4d31-acae-947de3d82802",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a6854eb8e8fb54b59",
  "type": "user",
  "uuid": "569f2969-4e81-4e30-8c2e-17cd0b086a01",
  "sourceToolAssistantUUID": "f1c18c44-bcfa-4d31-acae-947de3d82802",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T09:10:31.713Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017zQJ4Z6q87A8wfnSwUDffw`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "569f2969-4e81-4e30-8c2e-17cd0b086a01",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZU6ebAd7vXTHdnzYfq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48e5d2bf-4b1c-4154-831b-c1c232f34703",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XExCQhCrmTBb8oX1Y4afnv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 16650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
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

_source line 7 · 2026-05-20T09:10:31.779Z_

<details><summary>↩ Tool result · `toolu_017zQJ4Z6q87A8wfnSwUDffw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **phase_b_personfit** (success): Real LLM benchmark response data from PSN-IRT 12 models shows significant inter-model variation in person-fit statistics (lz*, outfit, infit), with specific models exhibiting anomalous patterns indicative of benchmark contamination — particularly Gemini-1.5 with accuracy-ability dissociation\\n- **sim_001** (negative): Under 4PL IRT model, lz* person-fit statistic can detect partial benchmark contamination (5-30% items) with >80% power at α=0.05, and detection power follows an inverted-U curve across contamination levels (low contamination undetectable, moderate contamination most detectable, high contamination mimics high ability)\\n  [null_check_summary](/api/workspace-files/projects/irt_personfit_contam/artifacts/sim_001/data/null_check_summary.json) | [simulation_summary](/api/workspace-files/projects/irt_personfit_contam/artifacts/sim_001/data/simulation_summary.json) | [power_curves_combined](/api/workspace-files/projects/irt_personfit_contam/artifacts/sim_001/chart/power_curves.png)\\n\\n## 趋势\\n成功 1 / 负向 1 / 失败 0 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1225, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48e5d2bf-4b1c-4154-831b-c1c232f34703",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a6854eb8e8fb54b59",
  "type": "user",
  "uuid": "7b846ead-de3b-4547-bd20-d56adf206057",
  "sourceToolAssistantUUID": "48e5d2bf-4b1c-4154-831b-c1c232f34703",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T09:10:32.748Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GTaDm2iXS8yjjd4GX3xKUc`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b846ead-de3b-4547-bd20-d56adf206057",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZU6ebAd7vXTHdnzYfq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f342dbeb-f921-44b1-8973-828b5991fc3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XExCQhCrmTBb8oX1Y4afnv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 16650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
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

_source line 9 · 2026-05-20T09:10:32.787Z_

<details><summary>↩ Tool result · `toolu_01GTaDm2iXS8yjjd4GX3xKUc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ROADMAP.md\", \"content\": \"# irt_personfit_contam — Research Dashboard\\n\\n> 最后更新: 2026-05-20 08:27 UTC | 更新原因: MVP 通过, 进入 research 阶段; 引用 paper_framing.md + experiment_plan.yaml; Dream 已启动\\n\\n## 核心方向\\n用 IRT person-fit 统计量在 information access 谱系最底层（仅 binary response pattern，无需 logits/weights/training data）检测 LLM benchmark 污染。详见 `paper_framing.md`。\\n\\n## 目标会议\\n- **Primary**: EMNLP 2026（用户确认 \\\"emnlp可行\\\"；ARR submission DDL 5/25 — 已追问可行性，等回复）\\n- **Fallback**: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\\n\\n## 当前阶段: Research（MVP 已通过 2026-05-20）\\n\\n### MVP 结果摘要\\n- **Phase A (simulation)**: Null check ✅, MMLU power@15%=97.9%, power ∝ n_items\\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.0/θ=0.78/lz*=+34.75（全面污染信号）; 所有 benchmark SD >> 0.5; 多模型 lz* < -1.96\\n- **关键发现**: 需双侧检测（full contamination → lz* >> 0, partial → lz* << 0）\\n- **Inverted-U**: 仅 MMLU/HellaSwag 在 50% 以内展现真正下降（Reviewer 修正）\\n\\n### Core Claims (from paper_framing.md)\\n1. **Minimal-information detection**: Person-fit stats 在检测前沿最底层 work\\n2. **Detection characterization**: Power ∝ n_items + 双侧信号结构 + inverted-U 理论化\\n3. **Empirical prevalence**: Gemini-1.5 case study + 跨模型/跨 benchmark 污染模式\\n\\n### Experiment Plan Status (from experiment_plan.yaml)\\n**P0 (headline)**:\\n- [ ] `exp-two-sided` — 双侧检测框架（CPU, 进行中）\\n- [ ] `exp-extended-sim` — 扩展模拟 60-100%（CPU, 进行中）\\n- [ ] `exp-ctrl-contam` — 控制实验 Qwen3.5-9B + Gemma-4-31B（~80 GPU-hrs, depends on two-sided）\\n- [ ] `exp-power-theory` — Power 理论推导（CPU, depends on extended-sim）\\n\\n**P1 (robustness)**:\\n- [ ] `exp-leaderboard-audit` — Open LLM Leaderboard v1 扫描（~20 GPU-hrs）\\n- [ ] `exp-4pl-ablation` — 4PL vs 3PL 检测对比（CPU）\\n- [ ] `exp-baseline-comparison` — vs ConStat/Min-K%++（~30 GPU-hrs）\\n- [ ] `exp-multiscale-lzm` — 跨 benchmark 聚合统计量（CPU）\\n\\n**P2 (expanded scope)**:\\n- [ ] `exp-post-rl` — Post-RL 假设检验（~40 GPU-hrs）\\n- [ ] `exp-extra-benchmarks` — BBH/MATH 扩展（~10 GPU-hrs）\\n- [ ] `exp-domain-analysis` — MMLU domain-level 分析（CPU）\\n\\n### Dream 状态\\n- `dream_20260520T082549`: pending（full review mode），等待回调后再批准 P0 实验\\n\\n## 近期任务\\n- [ ] 等 Dream 回调 → 审阅模拟审稿 → 决定是否调整 framing/plan\\n- [ ] exp-two-sided 重分析（Agent 执行中）\\n- [ ] exp-extended-sim 扩展模拟（Agent 执行中）\\n- [ ] GPU 服务器 bjb2-36806 环境配置（Agent 执行中）\\n- [ ] 确认目标会议（等用户回复 EMNLP DDL 问题）\\n\\n## GPU 预算\\n- 已分配: 4× RTX 5090 32GB (bjb2-36806)\\n- P0: ~80 GPU-hrs | P1: ~50 GPU-hrs | P2: ~50 GPU-hrs | Total: ~180 GPU-hrs\\n- 当前使用: 0（环境配置中）\\n\\n## 12 模型身份 (PSN-IRT)\\n| ID | θ | Model | 异常信号 |\\n|----|---|-------|---------|\\n| 0 | 1.46 | 360GPT2-Pro | — |\\n| 1 | 3.77 | DeepSeek-V3 | θ 远超第二名 |\\n| 2 | 1.14 | Doubao-pro | — |\\n| 3 | 0.78 | **Gemini-1.5** | **MMLU acc=1.0, lz*=+34.75** |\\n| 4 | -3.38 | Gemma-2B-it | — |\\n| 5 | 1.73 | Hunyuan-Turbo | — |\\n| 6 | -1.37 | Mistral-7B-v0.1 | — |\\n| 7 | 0.93 | Moonshot-v1 | — |\\n| 8 | 0.96 | Qwen-Plus | — |\\n| 9 | -0.13 | Qwen2.5-3B | — |\\n| 10 | -1.89 | Vicuna-7B-v1.3 | — |\\n| 11 | 0.77 | Yi-Lightning | — |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D006 | 2026-05-20 | Phase B 必须用 benchmark-specific θ (MLE)，不能用 PSN-IRT | exp-two-sided |\\n| D005 | 2026-05-20 | Phase B Pass + 发现双侧检测需求: Model 3 MMLU 100% acc/lz* | sim_001, phase_b_personfit |\\n| D004 | 2026-05-20 | Phase A Partial Pass: 方法机制验证成功，power 随 n_items 递减为 | sim_001 |\\n| D003 | 2026-05-20 | 修正 benchmark 分类: ARC-C 降为小(295 items); MVP 不混用 Tru | — |\\n| D002 | 2026-05-20 | 根据 Reviewer 审查细化 MVP: 加入 PSN-IRT 参数 null distribut | — |\\n| D001 | 2026-05-20 | MVP 采用两阶段验证: Phase A 模拟验证（无GPU）+ Phase B 真实数据探测 | — |\\n\\n\", \"total_chars\": 3399, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f342dbeb-f921-44b1-8973-828b5991fc3d",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a6854eb8e8fb54b59",
  "type": "user",
  "uuid": "45e97d4f-76af-45a6-8427-b941582f877f",
  "sourceToolAssistantUUID": "f342dbeb-f921-44b1-8973-828b5991fc3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T09:10:32.914Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Y9UHwLSQegAcssjp38hpQH`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45e97d4f-76af-45a6-8427-b941582f877f",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZU6ebAd7vXTHdnzYfq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c999ee46-451c-40dc-8474-8c05b456dc69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XExCQhCrmTBb8oX1Y4afnv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 16650,
      "output_tokens": 296,
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
          "output_tokens": 296,
          "cache_read_input_tokens": 16650,
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

_source line 11 · 2026-05-20T09:10:32.950Z_

<details><summary>↩ Tool result · `toolu_01Y9UHwLSQegAcssjp38hpQH`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'irt_personfit_contam'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c999ee46-451c-40dc-8474-8c05b456dc69",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a6854eb8e8fb54b59",
  "type": "user",
  "uuid": "0b941c69-90bb-4712-b907-1eb7a098aa93",
  "sourceToolAssistantUUID": "c999ee46-451c-40dc-8474-8c05b456dc69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T09:10:35.747Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PiTCtLFEV3G89ZG9ZbT6Du`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b941c69-90bb-4712-b907-1eb7a098aa93",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZUSJn3TP4U3YxVk2Hu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d3c99a9-be33-41fb-bc17-65929dfac15f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3SFimf1FUF8adoD5iMw5e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3154,
      "cache_read_input_tokens": 18099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3154,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 13 · 2026-05-20T09:10:35.793Z_

<details><summary>↩ Tool result · `toolu_01PiTCtLFEV3G89ZG9ZbT6Du`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper_framing.md\", \"content\": \"# Paper Framing — irt_personfit_contam\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\\n\\n## Core Claims (3 条)\\n\\n**Claim 1 (Minimal-Information Detection)**:\\nIRT person-fit statistics detect benchmark contamination at the minimal-information operating point on the detection frontier — requiring only binary (correct/incorrect) response patterns, without access to model logits, weights, or training data.\\n\\n**Claim 2 (Detection Characterization)**:\\nDetection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), power exceeds 90% at 15% contamination.\\n\\n**Claim 3 (Empirical Prevalence)**:\\nApplying IRT-FIT to publicly available LLM benchmark data reveals contamination patterns quantifiable for the first time via IRT — including Gemini-1.5's 100% MMLU accuracy (lz*=+34.75, θ=0.78) as systematic contamination evidence with model-level cross-benchmark anomaly profiles (Gemini-1.5 flagged on 4/5 benchmarks). Note: group-level cross-benchmark correlation is weak (n=12, most Spearman p>0.05); the claim is about individual model anomaly profiles, not population-level consistency.\\n\\n## Story Spine\\n\\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\\n\\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\\n\\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics (lz*, outfit, infit) — developed over decades for detecting exam cheating — we answer: \\\"What can be detected from binary response patterns alone?\\\" This is a foundational question, not just another detector. We show the method works (97.9% power on MMLU), characterize its limits (power ∝ n_items), and reveal its dual-regime signal structure (partial vs. full contamination).\\n\\n**Headline result template**: \\\"Using only binary response patterns, IRT-FIT detects benchmark contamination with 97.9% power on MMLU (14K items) and identifies Gemini-1.5's 100% MMLU accuracy as contamination (lz*=+34.75) — a signal invisible to existing detectors that require model internals.\\\"\\n\\n## Venue Fit Risks\\n\\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \\\"no new NLP model/technique\\\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\\n\\n## Anticipated Reviewer Concerns & Planned Responses\\n\\n| # | Concern | Response Strategy | Supporting Experiment |\\n|---|---------|------------------|----------------------|\\n| R1 | \\\"Just applying existing IRT to LLMs\\\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \\\"cross-domain\\\" from contribution to background. | — |\\n| R2 | \\\"No ground truth contamination labels\\\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\\n| R3 | \\\"Power too low for small benchmarks\\\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\\n| R4 | \\\"Only 12 models\\\" | Expand to Open LLM Leaderboard v1 models + newly evaluated models. | exp-leaderboard-audit |\\n| R5 | \\\"SFT generalization smooths signal\\\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\\n| R6 | \\\"Single-sided test misses full contamination\\\" | Two-sided detection framework is a core contribution. Gemini-1.5 case study demonstrates. | exp-two-sided |\\n| R7 | \\\"Post-RL contamination?\\\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\\n| R8 | \\\"4PL vs 3PL — does d parameter matter?\\\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\\n\\n## Key Narrative Elements (from External Review)\\n\\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\\n2. **Leaderboard audit as core** — Full scan of Open LLM Leaderboard v1 (7K+ models) is IRT-FIT's unique capability. ConStat needs re-test, gray-box needs live model access. This is the biggest differentiator.\\n3. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse (uniform high performance indistinguishable from true high ability in binary responses).\\n4. **Scope precision** — Target: \\\"intentional SFT contamination / leaderboard gaming\\\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\\n\\n## MVP Evidence Summary\\n\\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed.\\n- **Phase B (real data)**: Gemini-1.5 (student_id=3) MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark: GSM8K lz*=-15.71, HumanEval lz*=-12.37. All benchmarks SD >> 0.5.\\n- **Key insight from MVP**: Two-sided detection is essential — full contamination produces lz* >> 0 (over-consistent), not lz* << 0 (aberrant).\\n\", \"total_chars\": 6737, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d3c99a9-be33-41fb-bc17-65929dfac15f",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a6854eb8e8fb54b59",
  "type": "user",
  "uuid": "29d1e8cb-ab43-40af-9de1-54a8950b6c68",
  "sourceToolAssistantUUID": "8d3c99a9-be33-41fb-bc17-65929dfac15f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T09:10:36.851Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PwxPSR6s2sXRThxCrUdctf`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29d1e8cb-ab43-40af-9de1-54a8950b6c68",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZUSJn3TP4U3YxVk2Hu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf3ed096-a07a-4af9-a9cf-6b63b12356ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3SFimf1FUF8adoD5iMw5e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3154,
      "cache_read_input_tokens": 18099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3154,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 15 · 2026-05-20T09:10:36.890Z_

<details><summary>↩ Tool result · `toolu_01PwxPSR6s2sXRThxCrUdctf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/decisions.yaml\", \"content\": \"_next_id: 7\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 07:13 UTC\\n  summary: 'MVP 采用两阶段验证: Phase A 模拟验证（无GPU）+ Phase B 真实数据探测'\\n  rationale: '核心假设（person-fit stats 检测 contamination）可在理想化 IRT 模拟中先验证——如果模拟中都检测不到，真实数据更不可能。Phase\\n    A 零 GPU 成本、1-2 天即可得到 go/no-go 信号，避免在假设不成立时浪费 GPU 资源。Pass 标准: 15% contamination\\n    下 lz* 检测率 > 80%（α=0.05）且 inverted-U shape 可观测。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 07:16 UTC\\n  summary: '根据 Reviewer 审查细化 MVP: 加入 PSN-IRT 参数 null distribution sanity check + 按\\n    benchmark 规模分层 pass/fail + Phase B 量化标准'\\n  rationale: 'Reviewer 指出三个 warning: (1) Phase B 无 pass/fail 标准导致不可证伪; (2) 6 个 benchmark\\n    item 数差异巨大(164~14K)，统一 80% 检测率不合理; (3) PSN-IRT 用神经网络估参，经典 lz* 的 N(0,1) 渐近性质未必成立。三者均成立，分别补充:\\n    Phase B 定义 lz* 跨模型方差 + 异常值标准; 大/小 benchmark 分层 pass 阈值(80%/50%); Phase A 新增 null\\n    distribution KS 检验。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 07:22 UTC\\n  summary: '修正 benchmark 分类: ARC-C 降为小(295 items); MVP 不混用 TruthfulQA 3PL; 加入 a≤0\\n    item 过滤'\\n  rationale: 'Reviewer critical: PSN-IRT 中 ARC-C 仅 295 items（非预期的 ~1,172），不满足大 benchmark\\n    ≥1000 阈值。TruthfulQA 无 PSN-IRT 4PL 参数（仅 ATLAS 3PL），混用引入方法论不一致。部分 items a < 0（负判别度）违反\\n    IRT 假设需过滤。MVP 改为只用 5 个 PSN-IRT benchmark，大 benchmark 仅 MMLU/HellaSwag/GSM8K 三个。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-20 08:11 UTC\\n  summary: 'Phase A Partial Pass: 方法机制验证成功，power 随 n_items 递减为预期行为，推进 Phase B'\\n  rationale: sim_001 结果：(1) Null check 全通过（MMLU/HellaSwag/GSM8K KS p>0.05），PSN-IRT\\n    4PL 参数与 lz* N(0,1) 假设兼容；(2) Inverted-U shape 全部可观测；(3) MMLU(14K items) power@15%=97.9%\\n    远超 80% 阈值。未达标项：HellaSwag 73.3%（差 6.7pp）、GSM8K 57.8%。但 3 个大 benchmark 均>50%，不触发\\n    global fail。Power 与 n_items 强正相关是统计必然（不是方法缺陷），且在论文中可正面呈现为 power function 分析。Phase\\n    B 真实数据才是方法的终极验证——如果能在已知污染模型上检测到异常 lz*，simulation power 的具体数值不影响论文 claim。\\n  related_experiments:\\n  - exp_id: sim_001\\n    role: primary\\n    result: partial_pass\\n  depends_on:\\n  - D001\\n  - D002\\n  - D003\\n- id: D005\\n  date: 2026-05-20 08:21 UTC\\n  summary: 'Phase B Pass + 发现双侧检测需求: Model 3 MMLU 100% acc/lz*=+34.75 是全面污染信号，单侧检验漏检'\\n  rationale: Phase B 客观通过 pass 标准：所有 benchmark lz* SD >> 0.5（最小 ARC-C=2.59），且 MMLU/HellaSwag/GSM8K/HumanEval\\n    均有模型 lz* < -1.96。Reviewer 发现 Model 3 在 MMLU 上 acc=1.0/θ=0.777/lz*=+34.75——中等能力模型答对全部\\n    14042 题，统计上几乎不可能自然发生，是全面污染（memorized all items）的典型表现。但 lz* 为正极端值，单侧标准 lz* < -1.96\\n    完全漏检。同一模型在其他 benchmark lz* 显著为负（GSM8K=-15.71, HumanEval=-12.37），支持系统性污染假说。研究阶段必须引入双侧检测，Model\\n    3 将成为论文核心 case study。\\n  related_experiments:\\n  - exp_id: sim_001\\n    role: context\\n    result: partial_pass\\n  - exp_id: phase_b_personfit\\n    role: primary\\n    result: pass\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-20 08:40 UTC\\n  summary: Phase B 必须用 benchmark-specific θ (MLE)，不能用 PSN-IRT 全局 θ——全局 θ 导致 93.3%\\n    false flag\\n  rationale: 'Reviewer critical: exp-two-sided 用 |lz*|>1.96 在真实数据上 flag 了 56/60 cells（93.3%），远超预期\\n    5%。根因：PSN-IRT 的全局 θ 是跨 11 个 benchmark 的折中值，LLM 能力在不同 benchmark 上差异巨大（如 Gemini-1.5\\n    MMLU acc=1.0 但 HumanEval acc=0.54），全局 θ 系统性地在强项 benchmark 上低估、弱项上高估，产生 lz* 系统偏移。Phase\\n    A 模拟不受影响（模拟用的是单 benchmark 内 MLE θ）。修复：对每个 (model, benchmark) 用 MLE 从该 benchmark\\n    的 response vector 重估 θ_bench，再计算 lz*。这与 IDEA_BRIEF 原始设计一致（\\\"Per-benchmark person-fit\\n    to respect unidimensionality\\\"）。补充 empirical null (parametric bootstrap) 作为 robustness\\n    check + BH FDR 控制。calibration gap 本身是有价值的学术发现。'\\n  related_experiments:\\n  - exp_id: exp-two-sided\\n    role: primary\\n    result: critical_revision_needed\\n  depends_on:\\n  - D005\\n\", \"total_chars\": 3582, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf3ed096-a07a-4af9-a9cf-6b63b12356ca",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a6854eb8e8fb54b59",
  "type": "user",
  "uuid": "63ccb253-da11-47ac-b89e-f28427581278",
  "sourceToolAssistantUUID": "cf3ed096-a07a-4af9-a9cf-6b63b12356ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T09:10:37.262Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019Nu2Y2TYf8LiVyVSFZdiMG`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63ccb253-da11-47ac-b89e-f28427581278",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZUSJn3TP4U3YxVk2Hu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1a39f83-70af-4a7c-b6a9-4d9e87c238f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3SFimf1FUF8adoD5iMw5e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3154,
      "cache_read_input_tokens": 18099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3154,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 17 · 2026-05-20T09:10:37.308Z_

<details><summary>↩ Tool result · `toolu_019Nu2Y2TYf8LiVyVSFZdiMG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: '2026-05-20T08:00:00Z'\\n  total_papers: 10\\ncategories:\\n  - key: irt-llm\\n    label: IRT for LLM Evaluation\\n  - key: contamination-detection\\n    label: Benchmark Contamination Detection\\n  - key: person-fit\\n    label: Person-Fit Statistics (Psychometrics)\\n  - key: post-rl-contamination\\n    label: Post-RL Contamination\\npapers:\\n  psnirt2026:\\n    title: \\\"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\\\"\\n    authors: []\\n    year: 2026\\n    venue: AAAI 2026 Oral\\n    url: \\\"https://arxiv.org/abs/2505.15055\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: psnirt2026\\n    category: irt-llm\\n    role: foundation\\n    relevance: \\\"Provides calibrated 4PL item parameters (a,b,c,d) for 41,871 items across 11 benchmarks — the item bank our method builds on\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  atlas2025:\\n    title: \\\"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks\\\"\\n    authors: []\\n    year: 2025\\n    venue: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2511.04689\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: atlas2025\\n    category: irt-llm\\n    role: background\\n    relevance: \\\"ATLAS uses IRT for adaptive testing efficiency; related IRT-for-LLM work but not person-fit\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  constat2024:\\n    title: \\\"ConStat: Performance-Based Contamination Detection in Large Language Models\\\"\\n    authors: []\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: constat2024\\n    category: contamination-detection\\n    role: direct-competitor\\n    relevance: \\\"Performance-based contamination detector — primary baseline; requires re-test with modified items\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  minkprob2024:\\n    title: \\\"Detecting Pretraining Data from Large Language Models\\\"\\n    authors: []\\n    year: 2024\\n    venue: ICLR 2024\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: minkprob2024\\n    category: contamination-detection\\n    role: direct-competitor\\n    relevance: \\\"Min-K% Probability MIA-based detector — baseline; requires token probabilities (not black-box)\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  wang2025fragility:\\n    title: \\\"On The Fragility of Benchmark Contamination Detection in Reasoning Models\\\"\\n    authors: []\\n    year: 2025\\n    venue: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2510.02386\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: wang2025fragility\\n    category: post-rl-contamination\\n    role: foundation\\n    relevance: \\\"Shows all MIA-based detectors fail under post-RL contamination — motivates our black-box approach\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  selfcritique2026:\\n    title: \\\"Detecting Data Contamination from Reinforcement Learning Post-training\\\"\\n    authors: []\\n    year: 2026\\n    venue: ICLR 2026\\n    url: \\\"https://arxiv.org/abs/2510.09259\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: selfcritique2026\\n    category: post-rl-contamination\\n    role: direct-competitor\\n    relevance: \\\"Self-Critique detects post-RL contamination via entropy-sequence policy collapse — baseline for post-RL setting\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  codec2026:\\n    title: \\\"Detecting Data Contamination in LLMs via In-Context Learning\\\"\\n    authors: []\\n    year: 2026\\n    venue: ICLR 2026\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: codec2026\\n    category: contamination-detection\\n    role: direct-competitor\\n    relevance: \\\"CoDeC measures ICL effects on memorized vs unseen data — baseline\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  sinharay2017:\\n    title: \\\"Which Statistic Should Be Used to Detect Item Preknowledge?\\\"\\n    authors: []\\n    year: 2017\\n    venue: JEBS\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: sinharay2017\\n    category: person-fit\\n    role: foundation\\n    relevance: \\\"Power analysis for preknowledge detection — peak detection at 10-30% preknowledge; core theoretical basis\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  karabatsos2003:\\n    title: \\\"Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics\\\"\\n    authors: []\\n    year: 2003\\n    venue: Applied Measurement in Education\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: karabatsos2003\\n    category: person-fit\\n    role: foundation\\n    relevance: \\\"Comprehensive comparison of 36 person-fit statistics — guides our choice of lz* as primary statistic\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  hong2021lzm:\\n    title: \\\"Asymptotically Corrected Person Fit Statistics for Multidimensional Constructs with Simple Structure and Mixed Item Types\\\"\\n    authors: []\\n    year: 2021\\n    venue: Psychometrika\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: hong2021lzm\\n    category: person-fit\\n    role: method-component\\n    relevance: \\\"lzm multiscale aggregation for multidimensional constructs — our Level 2 aggregated contamination score\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\", \"total_chars\": 5591, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1a39f83-70af-4a7c-b6a9-4d9e87c238f8",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a6854eb8e8fb54b59",
  "type": "user",
  "uuid": "b3ccf1ae-4dda-48ef-896f-6623121ebc68",
  "sourceToolAssistantUUID": "f1a39f83-70af-4a7c-b6a9-4d9e87c238f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-20T09:10:40.607Z_

Now let me look at the actual paper artifacts and any experiment results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3ccf1ae-4dda-48ef-896f-6623121ebc68",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZUkySCysp8d5jbbWJT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41d77654-3748-49a9-a131-b7d42cde9525",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015NDqhRjvpucpWSZe66DsRR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7183,
      "cache_read_input_tokens": 21253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7183,
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

_source line 19 · 2026-05-20T09:10:41.240Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012nwp2aknVS9d61aERbKABJ`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41d77654-3748-49a9-a131-b7d42cde9525",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZUkySCysp8d5jbbWJT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1fe3ac0-e925-484c-94ea-8f9f16425d4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015NDqhRjvpucpWSZe66DsRR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7183,
      "cache_read_input_tokens": 21253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7183,
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

_source line 20 · 2026-05-20T09:10:41.385Z_

<details><summary>↩ Tool result · `toolu_012nwp2aknVS9d61aERbKABJ`</summary>

```text
artifacts/dream_reports/dream_20260520T082549/best/paper.tex
artifacts/dream_reports/dream_20260520T082549/median/paper.tex
artifacts/dream_reports/dream_20260520T082549/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1fe3ac0-e925-484c-94ea-8f9f16425d4e",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a6854eb8e8fb54b59",
  "type": "user",
  "uuid": "b261bd92-43f2-4258-83d6-fc45d332b62c",
  "sourceToolAssistantUUID": "d1fe3ac0-e925-484c-94ea-8f9f16425d4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T09:10:41.668Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018bAP6R9iaEmsewyU9GgR5c`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b261bd92-43f2-4258-83d6-fc45d332b62c",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZUkySCysp8d5jbbWJT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ac0f469-b6a5-439a-9b8d-36503828bb3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015NDqhRjvpucpWSZe66DsRR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7183,
      "cache_read_input_tokens": 21253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7183,
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

_source line 22 · 2026-05-20T09:10:41.778Z_

<details><summary>↩ Tool result · `toolu_018bAP6R9iaEmsewyU9GgR5c`</summary>

```text
literature_map.yaml
artifacts/manifest.yaml
experiment_plan.yaml
registry.yaml
decisions.yaml
mistakes.yaml
artifacts/dream_reports/dream_20260520T082549/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T082549/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T082549/worst/imagined_experiments.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260520T082549/best/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ac0f469-b6a5-439a-9b8d-36503828bb3e",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a6854eb8e8fb54b59",
  "type": "user",
  "uuid": "1323f576-48b4-454a-a006-eb590f666e1b",
  "sourceToolAssistantUUID": "0ac0f469-b6a5-439a-9b8d-36503828bb3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T09:10:44.762Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YDB3e9kmv9CXuHCvtJcsQ1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1323f576-48b4-454a-a006-eb590f666e1b",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZV66dTnUqFWmxRnMrd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e91e154-6661-4bbc-8334-ee5be1b79c87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiBEZTeSMafc5bFXbXPNUC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 455,
      "cache_read_input_tokens": 28436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 455,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 24 · 2026-05-20T09:10:45.091Z_

<details><summary>↩ Tool result · `toolu_01YDB3e9kmv9CXuHCvtJcsQ1`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立。三条 claim 均有 ground-truth 支撑：(1) minimal-information
2	  operating point 经控制实验确认——仅 binary 数据即可在 5% 污染水平检测，AUROC>0.93；(2) power ∝ n_items
3	  有解析公式， inverted-U 从经验观察升级为理论命题，拐点位置可预测；(3) Gemini-1.5 case study + leaderboard audit
4	  构成大规模实证贡献。Post-RL 实验直接回应 Wang et al.，形成"MIA 失效但 person-fit 存活"的对比叙事。 Headline: "IRT-FIT
5	  是唯一在 minimal-information 条件下同时解决 partial/full/post-RL 污染的方法"。 EMNLP 主会议无需调整 claim
6	  强度。
7	
8	  '
9	imagined_experiments:
10	- name: Two-Sided Detection Framework
11	  plan_id: exp-two-sided
12	  description: '基于 Phase B personfit_matrix.csv，实现 |lz*| > threshold 双侧检测框架， 含 bootstrap
13	    CI 和 BH-FDR 控制。验证 Gemini-1.5 case study 中正侧信号。
14	
15	    '
16	  expected_results:
17	    gemini15_mmlu_lz_star: 34.75
18	    gemini15_mmlu_lz_star_bootstrap_95ci: '[32.1, 37.4]'
19	    gemini15_gsm8k_lz_star: -15.71
20	    gemini15_humaneval_lz_star: -12.37
21	    two_sided_flagged_models_at_fdr_0.05: 4
22	    one_sided_flagged_models_at_fdr_0.05: 2
23	    incremental_detection_gain_two_vs_one_sided: 2 additional models flagged (Gemini-1.5
24	      on MMLU, 1 other high-perf model)
25	    optimal_negative_threshold_alpha_0.05: -2.81
26	    optimal_positive_threshold_alpha_0.05: 3.24
27	    positive_regime_models: Gemini-1.5 (MMLU), possibly Yi-34B or similar near-ceiling
28	      model
29	    negative_regime_models: Gemini-1.5 (GSM8K, HumanEval), Llama-2-70B (ARC-C)
30	  result_rationale: 'Gemini-1.5 的 MMLU 100% 正确率对应 θ=0.78（远低于满分所需能力），产生极端正侧 lz*=+34.75。
31	    这是因为 full contamination 导致模型在所有 item 上正确，包括远超其真实能力的难题—— response pattern 过度一致（over-consistent），与真正高能力模型的"偶尔失误"模式不符。
32	    负侧信号来自 partial contamination：模型在已污染的难题上正确、在未污染的易题上错误， 产生 aberrant pattern（lz*
33	    << 0）。双侧框架捕获这两类互补信号， 单侧框架只能捕获负侧（partial），遗漏正侧（full）。Bootstrap CI 窄是因为 MMLU 有 14K
34	    items， lz* 的抽样方差 ∝ 1/n_items。FDR 控制在 12 模型 × 5 benchmarks = 60 次检验下仍能保持 power，
35	    因为真阳性的 lz* 绝对值远超阈值（效应量极大）。
36	
37	    '
38	  tables:
39	  - name: 'Table 1: Two-Sided Detection Results (Phase B, 12 Models × 5 Benchmarks)'
40	    columns:
41	    - model
42	    - benchmark
43	    - accuracy
44	    - theta_hat
45	    - lz_star
46	    - side
47	    - flagged_bh_fdr_005
48	    - bootstrap_95ci
49	    key_rows:
50	    - - Gemini-1.5
51	      - MMLU
52	      - 1.0
53	      - 0.78
54	      - 34.75
55	      - positive
56	      - 'YES'
57	      - '[32.1, 37.4]'
58	    - - Gemini-1.5
59	      - GSM8K
60	      - 0.946
61	      - 2.41
62	      - -15.71
63	      - negative
64	      - 'YES'
65	      - '[-17.2, -14.3]'
66	    - - Gemini-1.5
67	      - HumanEval
68	      - 0.878
69	      - 1.92
70	      - -12.37
71	      - negative
72	      - 'YES'
73	      - '[-14.1, -10.8]'
74	    - - GPT-4
75	      - MMLU
76	      - 0.864
77	      - 2.15
78	      - -1.23
79	      - —
80	      - 'no'
81	      - '[-2.1, -0.4]'
82	    - - Llama-2-70B
83	      - ARC-C
84	      - 0.673
85	      - 1.08
86	      - -3.87
87	      - negative
88	      - 'YES'
89	      - '[-5.2, -2.6]'
90	  - name: 'Table 2: One-Sided vs Two-Sided Detection Comparison'
91	    columns:
92	    - method
93	    - total_flagged
94	    - partial_contam_detected
95	    - full_contam_detected
96	    - FDR_control
97	    key_rows:
98	    - - one-sided (lz* < threshold)
99	      - 2
100	      - 2
101	      - 0
102	      - '0.05'
103	    - - two-sided (|lz*| > threshold)
104	      - 4
105	      - 2
106	      - 2
107	      - '0.05'
108	  figures_description:
109	  - 'Fig 1: lz* heatmap (12 models × 5 benchmarks)，color diverging at 0，标注双侧阈值线。Gemini-1.5
110	    MMLU 为极端红色（正侧），GSM8K/HumanEval 为极端蓝色（负侧）。'
111	  - 'Fig 2: Bootstrap distribution of lz* for Gemini-1.5 MMLU，显示 CI 远离零点，p-value 极小。'
112	  analysis: '双侧框架是论文的关键方法论贡献。Phase B 数据直接证明单侧检测的盲区：Gemini-1.5 在 MMLU 上的 full contamination
113	    产生正侧信号，传统 person-fit（只看负侧 aberrance）完全遗漏。 这不仅是技术改进，而是揭示了污染信号的双重机制——partial contamination
114	    产生 aberrant pattern （答对难题、答错易题），full contamination 产生 over-consistent pattern（所有题都对，包括不该对的）。
115	    Bootstrap CI 和 FDR 控制确保结论在多重比较下依然稳健。
116	
117	    '
118	- name: Extended Simulation (Inverted-U Characterization)
119	  plan_id: exp-extended-sim
120	  description: '扩展 Phase A 模拟至 60%/75%/90%/100% contamination levels， 修复 100% contamination
121	    的 MLE boundary 处理，精确刻画 inverted-U 拐点。
122	
123	    '
124	  expected_results:
125	    inverted_u_inflection_point_mmlu: 0.65
126	    inverted_u_inflection_point_hellaswag: 0.6
127	    inverted_u_inflection_point_gsm8k: 0.7
128	    inverted_u_inflection_ci_range: '[0.55, 0.75]'
129	    lz_star_at_inflection_mmlu: -0.12
130	    lz_star_at_100pct_contam_mmlu: 28.5
131	    lz_star_at_100pct_contam_hellaswag: 18.2
132	    lz_star_at_100pct_contam_gsm8k: 8.7
133	    negative_peak_lz_at_15pct_mmlu: -8.3
134	    negative_peak_lz_at_25pct_mmlu: -12.1
135	    zero_crossing_contam_level_mmlu: 0.63
136	    zero_crossing_contam_level_hellaswag: 0.58
137	    nan_rate_after_boundary_fix: 0.0
138	    power_at_5pct_contam_mmlu: 0.78
139	    power_at_5pct_contam_hellaswag: 0.34
140	  result_rationale: 'Inverted-U 的物理机制：低污染（<15%）时，少量 hard items 被答对产生 aberrant pattern（lz*
141	    < 0）， 信号随污染比例增强；中等污染（~40-60%）时，被污染 items 的 "全部答对" 开始被 IRT 模型解释为 "该模型能力更高"，θ 估计上移，lz*
142	    绝对值开始减小——因为 response pattern 变得可以被高 θ 解释； 拐点（~65% for MMLU）处 lz* ≈ 0，pattern 恰好可被某个
143	    θ 值完美拟合；超过拐点后， 模型在几乎所有 items 上正确但 θ 估计仍有上界（受 non-contaminated items 约束）， 导致 over-consistent
144	    pattern（lz* > 0）。拐点位置取决于 benchmark 的 item difficulty 分布： MMLU 有大量高难度 items（14K
145	    items 中 ~30% difficulty > 2.0），需要更高污染比例才能 让 pattern 显得 "合理"，所以拐点在 0.65。GSM8K 难度更集中，拐点在
146	    0.70。 100% contamination 的 lz* 大小与 n_items 正相关（MMLU > HellaSwag > GSM8K）， 因为 lz*
147	    的分子累加了所有 item 的 log-likelihood 偏差。 MLE boundary fix 后 NaN 消失，因为 θ 被 cap 在 4.0，lz*
148	    仍可计算（只是值更极端）。
149	
150	    '
151	  tables:
152	  - name: 'Table 3: lz* as a Function of Contamination Level (Mean ± SD, 100 Replications)'
153	    columns:
154	    - contam_level
155	    - mmlu_lz_mean
156	    - mmlu_lz_sd
157	    - hellaswag_lz_mean
158	    - gsm8k_lz_mean
159	    - arc_c_lz_mean
160	    key_rows:
161	    - - 0%
162	      - 0.01
163	      - 1.02
164	      - 0.03
165	      - -0.02
166	      - 0.01
167	    - - 5%
168	      - -3.41
169	      - 1.15
170	      - -1.82
171	      - -1.34
172	      - -0.42
173	    - - 10%
174	      - -6.12
175	      - 1.28
176	      - -3.45
177	      - -2.51
178	      - -0.78
179	    - - 15%
180	      - -8.31
181	      - 1.41
182	      - -4.72
183	      - -3.38
184	      - -1.02
185	    - - 25%
186	      - -12.08
187	      - 1.67
188	      - -6.21
189	      - -4.53
190	      - -1.31
191	    - - 50%
192	      - -5.73
193	      - 2.14
194	      - -2.89
195	      - -1.67
196	      - -0.43
197	    - - 60%
198	      - -1.24
199	      - 2.31
200	      - 0.82
201	      - -0.34
202	      - 0.21
203	    - - 75%
204	      - 8.42
205	      - 2.53
206	      - 5.67
207	      - 3.21
208	      - 1.12
209	    - - 90%
210	      - 19.31
211	      - 2.87
212	      - 12.45
213	      - 6.78
214	      - 2.34
215	    - - 100%
216	      - 28.5
217	      - 3.12
218	      - 18.2
219	      - 8.7
220	      - 3.01
221	  - name: 'Table 4: Two-Sided Power at Various Contamination Levels'
222	    columns:
223	    - contam_level
224	    - mmlu_power
225	    - hellaswag_power
226	    - gsm8k_power
227	    - arc_c_power
228	    key_rows:
229	    - - 5%
230	      - 0.78
231	      - 0.34
232	      - 0.22
233	      - 0.06
234	    - - 15%
235	      - 0.979
236	      - 0.733
237	      - 0.578
238	      - 0.129
239	    - - 25%
240	      - 0.998
241	      - 0.891
242	      - 0.743
243	      - 0.201
244	    - - 50%
245	      - 0.872
246	      - 0.514
247	      - 0.298
248	      - 0.08
249	    - - 75%
250	      - 0.991
251	      - 0.934
252	      - 0.712
253	      - 0.187
254	    - - 100%
255	      - 1.0
256	      - 0.998
257	      - 0.962
258	      - 0.478
259	  figures_description:
260	  - 'Fig 3: Inverted-U 曲线——lz* mean vs contamination level，5 benchmarks 分色。标注 zero-crossing
261	    点和拐点位置，shaded area 为 ±1 SD。MMLU 曲线最深、拐点最右。'
262	  - 'Fig 4: Two-sided power vs contamination level，显示 U 型 power 曲线（中间有 dip 但不到 0）。对比
263	    one-sided power 在高污染时 drop to 0。'
264	  analysis: 'Inverted-U 的完整刻画是 Claim 2 的核心证据。拐点位置在 [0.55, 0.75] 范围内与 benchmark difficulty
265	    分布相关——这为后续理论推导提供了经验基准。关键发现：two-sided power 在拐点附近 有 dip 但不跌至零（因为 lz* 的 SD 在拐点处也增大，部分
266	    replications 仍超阈值）， 而 one-sided power 在高污染区完全失效。100% contamination 修复后产生极端正侧 lz*，
267	    与 Phase B Gemini-1.5 的经验数据定量一致（模拟 28.5 vs 实测 34.75，差异来自 Gemini-1.5 的真实 θ 分布与模拟假设不完全匹配）。
268	
269	    '
270	- name: Controlled Contamination Experiment
271	  plan_id: exp-ctrl-contam
272	  description: '在 Qwen3.5-9B 和 Gemma-4-31B 上，QLoRA SFT 注入 0%/5%/10%/15%/25%/50% benchmark
273	    items，建立 ground-truth contamination → lz* 映射。
274	
275	    '
276	  expected_results:
277	    ctrl_contam_auroc_at_15pct: 0.96
278	    ctrl_contam_auroc_at_5pct: 0.82
279	    ctrl_contam_auroc_at_25pct: 0.99
280	    ctrl_contam_min_detectable_level: 0.05
281	    ctrl_contam_lz_effect_size_cohens_d_at_15pct: 2.3
282	    ctrl_contam_lz_effect_size_cohens_d_at_5pct: 1.1
283	    qwen_clean_lz_star_mmlu: 0.08
284	    qwen_5pct_lz_star_mmlu: -3.72
285	    qwen_10pct_lz_star_mmlu: -6.45
286	    qwen_15pct_lz_star_mmlu: -8.91
287	    qwen_25pct_lz_star_mmlu: -11.34
288	    qwen_50pct_lz_star_mmlu: -4.82
289	    gemma_clean_lz_star_mmlu: 0.15
290	    gemma_5pct_lz_star_mmlu: -3.21
291	    gemma_15pct_lz_star_mmlu: -7.63
292	    gemma_50pct_lz_star_mmlu: -5.14
293	    accuracy_lift_at_15pct_contam_qwen: 0.043
294	    accuracy_lift_at_15pct_contam_gemma: 0.038
295	    sft_generalization_ratio: 0.12
296	    contaminated_items_accuracy_lift: 0.31
297	    non_contaminated_items_accuracy_change: 0.014
298	    false_positive_rate_at_alpha_0.05: 0.038
299	  result_rationale: 'SFT contamination 在 binary response 层面产生强 person-misfit 信号的原因：QLoRA
300	    SFT 直接 优化被注入 items 的 loss，导致这些 items 的正确率大幅上升（+31% on contaminated items）， 而未注入
301	    items 仅有微弱泛化（+1.4%）。这种"选择性提升"在 IRT 模型看来是 aberrant—— 模型在某些 hard items 上突然正确，但在同难度的
302	    non-contaminated items 上仍然错误。 泛化效应仅 12% 的原因：QLoRA 只更新 adapter weights（~0.5% 参数），且
303	    benchmark items 的格式高度标准化（MCQA），SFT 学到的是特定 item 的 answer pattern 而非领域知识。 Cohen''s
304	    d = 2.3 at 15% 说明效应量巨大——clean 和 contaminated 的 lz* 分布几乎不重叠。 AUROC 0.96 at 15%
305	    意味着随机抽一对 clean/contaminated 模型，96% 概率能正确区分。 5% contamination 仍可检测（AUROC 0.82）是因为
306	    MMLU 有 14K items，5% = 700 items 被污染， 足以在 lz* 累积中产生显著偏移。FPR 0.038 < 0.05 说明 null
307	    distribution 校准良好。 两个 base model 结果一致（效应量差 <15%）说明信号不依赖于特定模型架构。
308	
309	    '
310	  tables:
311	  - name: 'Table 5: Controlled Contamination — lz* by Model and Contamination Level
312	      (MMLU)'
313	    columns:
314	    - model
315	    - contam_level
316	    - accuracy
317	    - theta_hat
318	    - lz_star_mean
319	    - lz_star_sd
320	    - flagged_rate_alpha005
321	    key_rows:
322	    - - Qwen3.5-9B
323	      - 0%
324	      - 0.721
325	      - 1.42
326	      - 0.08
327	      - 0.97
328	      - 0.047
329	    - - Qwen3.5-9B
330	      - 5%
331	      - 0.738
332	      - 1.51
333	      - -3.72
334	      - 1.21
335	      - 0.82
336	    - - Qwen3.5-9B
337	      - 10%
338	      - 0.756
339	      - 1.59
340	      - -6.45
341	      - 1.34
342	      - 0.94
343	    - - Qwen3.5-9B
344	      - 15%
345	      - 0.764
346	      - 1.63
347	      - -8.91
348	      - 1.42
349	      - 0.97
350	    - - Qwen3.5-9B
351	      - 25%
352	      - 0.787
353	      - 1.71
354	      - -11.34
355	      - 1.58
356	      - 0.99
357	    - - Qwen3.5-9B
358	      - 50%
359	      - 0.831
360	      - 1.89
361	      - -4.82
362	      - 2.08
363	      - 0.87
364	    - - Gemma-4-31B
365	      - 0%
366	      - 0.793
367	      - 1.81
368	      - 0.15
369	      - 0.94
370	      - 0.041
371	    - - Gemma-4-31B
372	      - 5%
373	      - 0.808
374	      - 1.88
375	      - -3.21
376	      - 1.18
377	      - 0.78
378	    - - Gemma-4-31B
379	      - 15%
380	      - 0.831
381	      - 1.97
382	      - -7.63
383	      - 1.38
384	      - 0.95
385	    - - Gemma-4-31B
386	      - 50%
387	      - 0.874
388	      - 2.14
389	      - -5.14
390	      - 2.01
391	      - 0.84
392	  - name: 'Table 6: Detection Performance (AUROC) by Contamination Level'
393	    columns:
394	    - contam_level
395	    - auroc_qwen
396	    - auroc_gemma
397	    - auroc_pooled
398	    - cohens_d_pooled
399	    key_rows:
400	    - - 5%
401	      - 0.84
402	      - 0.8
403	      - 0.82
404	      - 1.1
405	    - - 10%
406	      - 0.93
407	      - 0.91
408	      - 0.92
409	      - 1.8
410	    - - 15%
411	      - 0.97
412	      - 0.95
413	      - 0.96
414	      - 2.3
415	    - - 25%
416	      - 0.99
417	      - 0.98
418	      - 0.99
419	      - 2.8
420	    - - 50%
421	      - 0.94
422	      - 0.91
423	      - 0.93
424	      - 1.6
425	  - name: 'Table 7: Contamination Selectivity — Accuracy Change on Contaminated vs
426	      Non-Contaminated Items'
427	    columns:
428	    - contam_level
429	    - contam_items_acc_before
430	    - contam_items_acc_after
431	    - contam_items_lift
432	    - non_contam_items_acc_before
433	    - non_contam_items_acc_after
434	    - non_contam_items_lift
435	    key_rows:
436	    - - 5%
437	      - 0.56
438	      - 0.87
439	      - 0.31
440	      - 0.73
441	      - 0.74
442	      - 0.014
443	    - - 15%
444	      - 0.54
445	      - 0.84
446	      - 0.3
447	      - 0.73
448	      - 0.75
449	      - 0.018
450	    - - 25%
451	      - 0.55
452	      - 0.86
453	      - 0.31
454	      - 0.73
455	      - 0.76
456	      - 0.024
457	    - - 50%
458	      - 0.57
459	      - 0.88
460	      - 0.31
461	      - 0.73
462	      - 0.77
463	      - 0.037
464	  figures_description:
465	  - 'Fig 5: lz* vs contamination level scatter (Qwen + Gemma, MMLU)，叠加模拟 inverted-U
466	    理论曲线。实测数据点落在理论预测 ±1 SD 内。'
467	  - 'Fig 6: ROC 曲线 at 5%/15%/25% contamination，三条曲线叠在一起，标注 AUROC 值。'
468	  - 'Fig 7: Item-level accuracy heatmap，contaminated items (sorted by difficulty)
469	    vs non-contaminated items，展示 SFT 的选择性提升效应。'
470	  analysis: '控制实验是论文最关键的 ground-truth 证据。核心发现：(1) SFT 污染在 binary response 层面 产生强烈且可检测的
471	    person-misfit 信号，Cohen''s d > 2 at 15% contamination； (2) 泛化效应仅 1-4%，远不足以平滑 aberrant
472	    pattern——这直接回应了 R5 审稿意见； (3) 两个不同架构/规模的 base model 给出一致结果，排除模型特异性； (4) 5% contamination
473	    即可检测（AUROC 0.82），确立 minimal detectable level。 50% contamination 的 lz* 绝对值回落验证了
474	    inverted-U，与扩展模拟定量一致。
475	
476	    '
477	- name: Power Theory Derivation
478	  plan_id: exp-power-theory
479	  description: '推导 power 与 n_items 的解析关系，基于 Snijders (2001) lz* 方差公式， 验证理论曲线与模拟数据的拟合度，将
480	    inverted-U 升级为理论命题。
481	
482	    '
483	  expected_results:
484	    power_theory_r_squared: 0.97
485	    power_formula: power ≈ Φ(δ·√n / σ_lz* − z_α) where δ = E[log L_contam − log L_clean]
486	      per item
487	    inverted_u_inflection_formula: c* = argmin_c |E_θ[Σ_i (x_i·log P_i + (1−x_i)·log(1−P_i))
488	      | contam=c] − E_θ[...| contam=0]|
489	    predicted_inflection_mmlu: 0.64
490	    predicted_inflection_hellaswag: 0.59
491	    predicted_inflection_gsm8k: 0.68
492	    observed_inflection_mmlu: 0.65
493	    observed_inflection_hellaswag: 0.6
494	    observed_inflection_gsm8k: 0.7
495	    inflection_prediction_error: 0.02
496	    power_at_n100_15pct_predicted: 0.089
497	    power_at_n1000_15pct_predicted: 0.491
498	    power_at_n5000_15pct_predicted: 0.862
499	    power_at_n14000_15pct_predicted: 0.981
500	    min_n_for_80pct_power_at_15pct: 3200
501	    min_n_for_80pct_power_at_5pct: 9800
502	  result_rationale: 'Snijders (2001) 证明了在正确指定的 IRT 模型下 lz* ~ N(0,1)。当注入 contamination
503	    时， lz* 的期望偏移量 δ 可以解析计算：每个被污染 item 对 log-likelihood 的贡献偏差为 log P_i(θ_true) − log
504	    P_i(θ_estimated)，其中 θ_estimated 被 contaminated items 上推。 对 n 个 items 中 c·n 个被污染的情况，总偏移
505	    ∝ c·n·δ_per_item，而 lz* 的标准差 ∝ √n。 因此 power ≈ Φ(c·√n·δ_per_item/σ − z_α)，这是一个关于
506	    c 和 n 的可预测函数。 R² = 0.97 的原因：理论假设（IRT 模型正确指定、θ 的 MLE 一致性）在模拟中近似成立， 但现实中参数估计有误差、4PL
507	    模型有轻微 misfit，导致不完美拟合。 Inverted-U 的拐点可以从 item difficulty 分布的分位数推导：当 contaminated
508	    items 的正确率 被提升到 1.0 时，如果这些 items 的 difficulty 覆盖了 IRT scale 的某个区间， θ 的 MLE 会被推到一个特定位置，使得
509	    response pattern 看起来 "最合理" 的 contamination 比例 就是拐点。MMLU difficulty 分布偏宽（SD ≈ 1.8），拐点偏右（0.64）；GSM8K
510	    difficulty 更集中 （SD ≈ 1.2），拐点偏右（0.68）是因为 difficulty 水平更高。 理论预测的拐点与观测值的误差仅 0.02，验证了解析公式的有效性。
511	
512	    '
513	  tables:
514	  - name: 'Table 8: Theoretical vs Simulated Power (15% Contamination)'
515	    columns:
516	    - n_items
517	    - predicted_power
518	    - simulated_power
519	    - absolute_error
520	    key_rows:
521	    - - 100
522	      - 0.089
523	      - 0.092
524	      - 0.003
525	    - - 500
526	      - 0.312
527	      - 0.298
528	      - 0.014
529	    - - 1000
530	      - 0.491
531	      - 0.503
532	      - 0.012
533	    - - 1319
534	      - 0.578
535	      - 0.578
536	      - 0.0
537	    - - 5000
538	      - 0.862
539	      - 0.851
540	      - 0.011
541	    - - 10042
542	      - 0.964
543	      - 0.958
544	      - 0.006
545	    - - 14042
546	      - 0.981
547	      - 0.979
548	      - 0.002
549	  - name: 'Table 9: Inverted-U Inflection Point — Predicted vs Observed'
550	    columns:
551	    - benchmark
552	    - n_items
553	    - difficulty_sd
554	    - predicted_inflection
555	    - observed_inflection
556	    - abs_error
557	    key_rows:
558	    - - MMLU
559	      - 14042
560	      - 1.83
561	      - 0.64
562	      - 0.65
563	      - 0.01
564	    - - HellaSwag
565	      - 10042
566	      - 1.52
567	      - 0.59
568	      - 0.6
569	      - 0.01
570	    - - GSM8K
571	      - 1319
572	      - 1.21
573	      - 0.68
574	      - 0.7
575	      - 0.02
576	    - - ARC-C
577	      - 1172
578	      - 1.45
579	      - 0.62
580	      - 0.64
581	      - 0.02
582	    - - HumanEval
583	      - 164
584	      - 1.67
585	      - 0.61
586	      - 0.63
587	      - 0.02
588	  - name: 'Table 10: Minimum n_items for 80% Power at Various Contamination Levels'
589	    columns:
590	    - contam_level
591	    - min_n_theoretical
592	    - min_n_simulated
593	    key_rows:
594	    - - 5%
595	      - 9800
596	      - 10200
597	    - - 10%
598	      - 4700
599	      - 4900
600	    - - 15%
601	      - 3200
602	      - 3350
603	    - - 25%
604	      - 1800
605	      - 1900
606	  figures_description:
607	  - 'Fig 8: Power vs n_items 理论曲线（连续线）叠加 5 benchmarks 的模拟数据点（散点）。多条曲线对应不同 contamination
608	    levels (5%/10%/15%/25%)。'
609	  - 'Fig 9: Inverted-U 理论预测曲线 vs 模拟数据，标注拐点位置与 CI。'
610	  - 'Fig 10: Power landscape heatmap (n_items × contam_level)，颜色编码 power，标注 80% power
611	    等高线。'
612	  analysis: 'Power 理论将 Claim 2 从经验观察升级为可预测的定量关系。解析公式给出了 practitioner 的 直接指导：要检测 15%
613	    污染需要 ≥3200 items，检测 5% 污染需要 ≥9800 items。 这解释了为什么 ARC-C (1172 items) 的 power 只有
614	    12.9%——不是方法失败，而是信息不足。 Inverted-U 的理论推导是方法论贡献的核心：它不仅解释了为什么存在拐点， 还能从 item difficulty
615	    分布预测拐点位置，误差仅 1-2 个百分点。
616	
617	    '
618	- name: Leaderboard Audit (Large-Scale Scan)
619	  plan_id: exp-leaderboard-audit
620	  description: 'Open LLM Leaderboard v1 大规模扫描，获取 per-item response logs， 对所有可用模型计算
621	    person-fit，绘制 per-benchmark 污染率随时间趋势。
622	
623	    '
624	  expected_results:
625	    leaderboard_models_scanned: 2847
626	    leaderboard_models_with_per_item_logs: 0
627	    leaderboard_models_rerun_inference: 2847
628	    total_gpu_hours_inference: 18.5
629	    leaderboard_flagged_rate_overall: 0.12
630	    leaderboard_flagged_rate_mmlu: 0.15
631	    leaderboard_flagged_rate_hellaswag: 0.09
632	    leaderboard_flagged_rate_arc_c: 0.07
633	    leaderboard_flagged_rate_gsm8k: 0.11
634	    flagged_models_total: 342
635	    flagged_two_sided_positive: 87
636	    flagged_two_sided_negative: 255
637	    contamination_trend_increasing: true
638	    contamination_rate_2023q1: 0.06
639	    contamination_rate_2023q3: 0.11
640	    contamination_rate_2024q1: 0.18
641	    cross_benchmark_consistent_flag_rate: 0.34
642	    top_flagged_model_lz_star: -22.4
643	  result_rationale: 'Per-item response logs 在 HuggingFace 上不直接公开（Leaderboard v1 只存
644	    aggregate scores）， 因此需要对可获取权重的模型重新跑推理。受 GPU 预算限制（20 hrs），选择 <7B 参数模型 优先扫描，覆盖 2847
645	    个模型（占 Leaderboard v1 总量的 ~40%）。 12% flagged rate 的来源：Leaderboard v1 时期（2023-2024）是
646	    benchmark gaming 高峰期， 大量模型通过 SFT 在 benchmark items 上训练以获取高排名。MMLU 受影响最严重（15%）
647	    因为它是 Leaderboard 的核心排名指标且训练数据广泛可获得。 时间趋势显示 2023 Q1 flagged rate 仅 6%，到 2024 Q1
648	    升至 18%—— 与社区对 benchmark contamination 问题认知的时间线一致（Contamination in the wild 2024
649	    等论文）。 正侧 flagged（87 个）主要是 MMLU 上的 "suspicious near-ceiling" 模型， 负侧 flagged（255
650	    个）主要是 partial contamination 的小模型。 跨 benchmark 一致 flag rate 34% 说明约 1/3 的 flagged
651	    模型在多个 benchmark 上同时异常—— 这些是最可信的 contamination 案例。
652	
653	    '
654	  tables:
655	  - name: 'Table 11: Leaderboard Audit Summary'
656	    columns:
657	    - benchmark
658	    - models_scanned
659	    - flagged_negative
660	    - flagged_positive
661	    - flagged_rate
662	    - median_lz_star_flagged
663	    key_rows:
664	    - - MMLU
665	      - 2847
666	      - 312
667	      - 115
668	      - 0.15
669	      - -6.73
670	    - - HellaSwag
671	      - 2847
672	      - 198
673	      - 58
674	      - 0.09
675	      - -4.21
676	    - - ARC-C
677	      - 2847
678	      - 142
679	      - 57
680	      - 0.07
681	      - -3.12
682	    - - GSM8K
683	      - 2182
684	      - 178
685	      - 63
686	      - 0.11
687	      - -5.42
688	    - - Overall (any benchmark)
689	      - 2847
690	      - 255
691	      - 87
692	      - 0.12
693	      - —
694	  - name: 'Table 12: Contamination Rate by Time Period'
695	    columns:
696	    - period
697	    - models_in_period
698	    - flagged_count
699	    - flagged_rate
700	    key_rows:
701	    - - 2023 Q1-Q2
702	      - 487
703	      - 29
704	      - 0.06
705	    - - 2023 Q3-Q4
706	      - 891
707	      - 98
708	      - 0.11
709	    - - 2024 Q1-Q2
710	      - 1103
711	      - 198
712	      - 0.18
713	    - - 2024 Q3+
714	      - 366
715	      - 51
716	      - 0.14
717	  - name: 'Table 13: Top 10 Most Anomalous Models'
718	    columns:
719	    - model
720	    - benchmark
721	    - accuracy
722	    - theta
723	    - lz_star
724	    - side
725	    - params
726	    key_rows:
727	    - - anonymous-7b-v3
728	      - MMLU
729	      - 0.847
730	      - 1.23
731	      - -22.4
732	      - negative
733	      - 7B
734	    - - llm-finetune-2b
735	      - MMLU
736	      - 0.912
737	      - 1.45
738	      - 18.7
739	      - positive
740	      - 2B
741	    - - benchmark-tuned-3b
742	      - GSM8K
743	      - 0.891
744	      - 2.12
745	      - -17.3
746	      - negative
747	      - 3B
748	  figures_description:
749	  - 'Fig 11: 散点图——所有 2847 模型的 (accuracy, lz*) on MMLU。Flagged 模型标红，non-flagged 标灰。显示
750	    flagged 模型不仅是高 accuracy（也有中等 accuracy 但 aberrant pattern 的）。'
751	  - 'Fig 12: 时间趋势——每季度的 flagged rate，按 benchmark 分色。显示逐年上升趋势。'
752	  - 'Fig 13: Cross-benchmark consistency heatmap——flagged 模型在各 benchmark 上的 lz* 值，展示跨
753	    benchmark 污染的关联性。'
754	  analysis: 'Leaderboard audit 是 IRT-FIT 的 "killer app"——唯一只需要 binary response data
755	    的方法 才能做到如此规模的扫描。ConStat 需要 re-test（需要 live model access）， Min-K%++ 需要 token probabilities（需要
756	    logits），MIA 需要 training data reference。 2847 个模型的扫描中 12% flagged rate 意味着约 342
757	    个模型存在可疑的 benchmark 污染， 且这个比例随时间上升。这为社区提供了首个大规模、定量的 benchmark integrity 评估。 尽管未达到
758	    7000 个模型的上限预测，2847 个模型已是同类研究中最大规模。
759	
760	    '
761	- name: 4PL vs 3PL Ablation
762	  plan_id: exp-4pl-ablation
763	  description: '比较 4PL (with feasibility parameter d) 和 3PL(d=1) 下的检测灵敏度差异， 量化 d 参数对
764	    false alarm 和 detection power 的影响。
765	
766	    '
767	  expected_results:
768	    auroc_4pl_15pct: 0.96
769	    auroc_3pl_15pct: 0.91
770	    auroc_difference_15pct: 0.05
771	    false_alarm_rate_4pl: 0.042
772	    false_alarm_rate_3pl: 0.078
773	    power_4pl_15pct_mmlu: 0.979
774	    power_3pl_15pct_mmlu: 0.934
775	    power_difference_15pct_mmlu: 0.045
776	    mean_abs_lz_star_difference_clean: 0.34
777	    mean_abs_lz_star_difference_contam: 0.87
778	    d_parameter_mean_psn_irt: 0.91
779	    d_parameter_sd_psn_irt: 0.08
780	    items_where_d_matters_most: top-difficulty items (difficulty > 2.5) where d <
781	      0.85
782	  result_rationale: '4PL 的 d 参数（upper asymptote / feasibility parameter）建模了即使能力极高的考生
783	    也可能答错某些 items 的现象——在 LLM 场景中对应"某些 items 的表述/格式导致即使知道答案的模型也可能选错"。 当 d < 1 时，3PL(d=1)
784	    会高估高能力模型在这些 items 上的预期正确率， 导致其答错时产生过多的 "aberrant" 信号（false alarm 上升）。 4PL 通过让
785	    d < 1 吸收这种自然变异，减少了 false alarm（0.042 vs 0.078）。 对于 contaminated models，d < 1 的
786	    items 是区分度最高的：contaminated model 在这些 items 上 答对率接近 1.0（因为直接记住了答案），而 clean model
787	    的答对率被 d 压低。 因此 4PL 在 contaminated case 中效应量更大（lz* 偏差多 0.87），综合 AUROC 提升 0.05。
788	    差异主要集中在高难度 items（difficulty > 2.5）——这些 items 的 d 值通常更低， 因为它们的表述更复杂，即使知道正确答案也更容易因格式理解问题出错。
789	
790	    '
791	  tables:
792	  - name: 'Table 14: 4PL vs 3PL Detection Performance Comparison'
793	    columns:
794	    - metric
795	    - 4PL
796	    - 3PL(d=1)
797	    - difference
798	    key_rows:
799	    - - AUROC @ 15%
800	      - 0.96
801	      - 0.91
802	      - '+0.05'
803	    - - False Alarm Rate (α=0.05)
804	      - 0.042
805	      - 0.078
806	      - −0.036
807	    - - Power @ 15% MMLU
808	      - 0.979
809	      - 0.934
810	      - '+0.045'
811	    - - Power @ 5% MMLU
812	      - 0.78
813	      - 0.69
814	      - '+0.09'
815	    - - Mean |lz*| clean models
816	      - 0.83
817	      - 1.17
818	      - −0.34
819	    - - Mean |lz*| contam models (15%)
820	      - 8.91
821	      - 8.04
822	      - '+0.87'
823	  - name: 'Table 15: Impact of d Parameter by Item Difficulty Band'
824	    columns:
825	    - difficulty_band
826	    - n_items
827	    - mean_d
828	    - lz_star_diff_clean
829	    - lz_star_diff_contam
830	    key_rows:
831	    - - < 0.5 (easy)
832	      - 2814
833	      - 0.97
834	      - -0.08
835	      - 0.12
836	    - - 0.5–1.5
837	      - 5621
838	      - 0.93
839	      - -0.21
840	      - 0.43
841	    - - 1.5–2.5
842	      - 3891
843	      - 0.89
844	      - -0.38
845	      - 0.78
846	    - - '> 2.5 (hard)'
847	      - 1716
848	      - 0.82
849	      - -0.67
850	      - 1.45
851	  figures_description:
852	  - 'Fig 14: ROC 曲线对比——4PL vs 3PL at 5%/15% contamination。4PL 曲线始终在 3PL 上方。'
853	  - 'Fig 15: d parameter distribution (histogram) from PSN-IRT，标注 mean 和关键分位数。'
854	  analysis: '4PL vs 3PL 的差异统计显著但不是巨大的——这其实是好消息：它说明 person-fit 方法 对 IRT 模型选择有一定 robustness，3PL
855	    也能工作（AUROC 0.91），但 4PL 更优（AUROC 0.96）。 关键 insight：d 参数的影响集中在高难度 items 上，而这些 items
856	    恰好是 contamination 信号最强的区域（contaminated model 在难题上答对是最 aberrant 的）。因此 4PL 的精确建模
857	    在检测任务中有非平凡的价值。
858	
859	    '
860	- name: Baseline Comparison (ConStat, Min-K%++)
861	  plan_id: exp-baseline-comparison
862	  description: '在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs ConStat vs
863	    Min-K%++ 的 AUROC 和 Type-I error。
864	
865	    '
866	  expected_results:
867	    irt_fit_auroc_15pct: 0.96
868	    constat_auroc_15pct: 0.83
869	    min_k_pp_auroc_15pct: 0.88
870	    irt_fit_auroc_5pct: 0.82
871	    constat_auroc_5pct: 0.61
872	    min_k_pp_auroc_5pct: 0.72
873	    auroc_advantage_vs_constat_15pct: 0.13
874	    auroc_advantage_vs_minkpp_15pct: 0.08
875	    baseline_auroc_advantage_vs_constat: 0.1
876	    type_i_error_irt_fit: 0.042
877	    type_i_error_constat: 0.053
878	    type_i_error_min_k_pp: 0.048
879	    irt_fit_information_required: binary responses only
880	    constat_information_required: binary responses + re-test capability
881	    min_k_pp_information_required: token-level log-probabilities
882	    irt_fit_unique_advantage: operates without model access
883	  result_rationale: 'IRT-FIT 在 AUROC 上优于 ConStat 0.10-0.13 的原因有两方面： (1) Person-fit
884	    statistics 利用了完整的 item-level response pattern 信息——每个 item 的 difficulty、 discrimination、guessing、feasibility
885	    参数都参与 lz* 计算，而 ConStat 基于 aggregate performance 的一致性检验，信息利用效率更低； (2) ConStat 的
886	    re-test design 假设 contaminated model 在 re-test 时表现不一致， 但 SFT contamination 是永久性的（权重已改变），re-test
887	    分数几乎不变，削弱了 ConStat 的信号。 Min-K%++ 在 AUROC 上略低于 IRT-FIT（0.88 vs 0.96）但需要 token-level
888	    probabilities—— 信息需求更高。其信号来自 token-level memorization（contaminated items 的 token
889	    loss 更低）， 但 SFT 后的 token-level 信号会被 RL 和 decoding 过程扰动，不如 binary response 层面的
890	    person-fit 信号稳定。 Type-I error 都接近 nominal 0.05，说明三种方法的 null calibration 都合理。 关键叙事：IRT-FIT
891	    不仅性能更好，而且信息需求最低——这是 detection frontier 的核心论点。
892	
893	    '
894	  tables:
895	  - name: 'Table 16: Baseline Comparison — Detection Performance on Controlled Contamination'
896	    columns:
897	    - method
898	    - info_required
899	    - auroc_5pct
900	    - auroc_15pct
901	    - auroc_25pct
902	    - type_i_error
903	    key_rows:
904	    - - IRT-FIT (lz*, two-sided)
905	      - binary responses
906	      - 0.82
907	      - 0.96
908	      - 0.99
909	      - 0.042
910	    - - ConStat
911	      - binary + re-test
912	      - 0.61
913	      - 0.83
914	      - 0.91
915	      - 0.053
916	    - - Min-K%++
917	      - token log-probs
918	      - 0.72
919	      - 0.88
920	      - 0.95
921	      - 0.048
922	  - name: 'Table 17: Detection Frontier — Information Access vs Detection Power'
923	    columns:
924	    - information_level
925	    - method
926	    - auroc_15pct
927	    - scalability
928	    key_rows:
929	    - - binary responses only
930	      - IRT-FIT
931	      - 0.96
932	      - any model with public scores
933	    - - binary + re-test
934	      - ConStat
935	      - 0.83
936	      - requires live model access
937	    - - token probabilities
938	      - Min-K%++
939	      - 0.88
940	      - requires API with logprobs
941	    - - training data
942	      - n-gram overlap
943	      - —
944	      - requires training data access
945	    - - model weights
946	      - internal probing
947	      - —
948	      - requires open weights
949	  figures_description:
950	  - 'Fig 16: ROC 曲线三方对比，IRT-FIT / ConStat / Min-K%++，at 15% contamination。'
951	  - 'Fig 17: Detection frontier diagram——x 轴为 information access level (ordered)，y
952	    轴为 AUROC，标注各方法位置。IRT-FIT 在最左下角（最少信息，高 AUROC）。'
953	  analysis: 'Baseline comparison 直接支撑 Claim 1（minimal-information operating point）。IRT-FIT
954	    在信息需求最低的条件下取得了最高的 AUROC——这不是因为 person-fit 比 MIA 更好（在等信息条件下 Min-K%++ 可能更强），而是因为
955	    person-fit 从 binary data 中提取了最大信号量。 Detection frontier diagram 是一个有力的可视化，直接展示了方法论贡献的核心。
956	
957	    '
958	- name: Multiscale lzm Statistic
959	  plan_id: exp-multiscale-lzm
960	  description: '实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021），跨 benchmark 聚合 lz*，
961	    在 PSN-IRT 12 模型 + 控制实验模型上验证。
962	
963	    '
964	  expected_results:
965	    lzm_auroc_15pct: 0.98
966	    lzm_vs_single_benchmark_auroc_gain: 0.02
967	    lzm_cross_benchmark_correlation: 0.67
968	    gemini15_lzm: 18.42
969	    gpt4_lzm: -0.87
970	    clean_model_lzm_mean: 0.03
971	    clean_model_lzm_sd: 0.91
972	    contam_model_lzm_mean_15pct: -7.23
973	    lzm_null_ks_p: 0.312
974	    lzm_power_at_15pct_pooled: 0.99
975	  result_rationale: 'lzm 将多个 benchmark 的 lz* 标准化后求和，利用了跨 benchmark 的信息： 如果一个模型在多个
976	    benchmark 上都有 aberrant pattern，lzm 的信号会累积。 AUROC 从单 benchmark 的 0.96 提升到 0.98
977	    是因为： (1) 信息量增加——5 benchmarks 总共 ~27K items，比单 benchmark 多了判别力； (2) 跨 benchmark
978	    一致性——真正 contaminated 的模型在多个 benchmark 上 lz* 都异常， 而 false positive（某个 benchmark
979	    上偶然异常）不会在 lzm 中累积。 Gemini-1.5 的 lzm = 18.42 极端，因为它在 MMLU 上正侧异常、在 GSM8K/HumanEval
980	    上负侧异常， lzm 用绝对值聚合两侧信号。GPT-4 的 lzm = -0.87 接近零，说明 GPT-4 的 response pattern 在所有
981	    benchmark 上都是 "正常" 的。 Null distribution 校准通过（KS p = 0.312），说明 lzm 在 clean models
982	    上确实近似 N(0,1)。
983	
984	    '
985	  tables:
986	  - name: 'Table 18: lzm Results — PSN-IRT 12 Models'
987	    columns:
988	    - model
989	    - lzm_value
990	    - flagged_alpha005
991	    - n_benchmarks_individual_flag
992	    key_rows:
993	    - - Gemini-1.5
994	      - 18.42
995	      - 'YES'
996	      - 3
997	    - - GPT-4
998	      - -0.87
999	      - 'no'
1000	      - 0
1001	    - - Llama-2-70B
1002	      - -3.21
1003	      - 'YES'
1004	      - 1
1005	    - - Claude-3-Opus
1006	      - 0.42
1007	      - 'no'
1008	      - 0
1009	    - - Mistral-7B
1010	      - -2.45
1011	      - 'no'
1012	      - 0
1013	  - name: 'Table 19: lzm vs Single-Benchmark Detection Power'
1014	    columns:
1015	    - method
1016	    - auroc_15pct
1017	    - power_at_15pct
1018	    - false_alarm_rate
1019	    key_rows:
1020	    - - lz* (MMLU only)
1021	      - 0.96
1022	      - 0.979
1023	      - 0.042
1024	    - - lz* (best single benchmark)
1025	      - 0.96
1026	      - 0.979
1027	      - 0.042
1028	    - - lzm (all benchmarks)
1029	      - 0.98
1030	      - 0.99
1031	      - 0.037
1032	  figures_description:
1033	  - 'Fig 18: lzm 分布——clean models (histogram) + contaminated models (overlay)，标注阈值。'
1034	  - 'Fig 19: 散点图——lzm vs max single-benchmark |lz*|，标注各模型。显示 lzm 提供增量信息。'
1035	  analysis: 'lzm 是一个稳健的 "overall contamination index"，特别适合 leaderboard audit 场景——
1036	    单一指标告诉你 "这个模型总体上是否可疑"。AUROC 增益 0.02 看似不大， 但对 leaderboard-scale 扫描（数千模型），2% 的 precision
1037	    提升意味着减少 ~50 个 false flag。 更重要的叙事价值：lzm 展示了 IRT person-fit 框架的可扩展性——可以从单 benchmark
1038	    到多 benchmark 无缝聚合。
1039	
1040	    '
1041	- name: Post-RL Hypothesis Test
1042	  plan_id: exp-post-rl
1043	  description: '在 Qwen3.5-9B 上先 SFT 污染（15% MMLU items）再 GRPO 训练， 测试 person-fit 信号是否在
1044	    RL 后保持检测力。
1045	
1046	    '
1047	  expected_results:
1048	    pre_rl_lz_star: -8.91
1049	    post_rl_lz_star: -7.12
1050	    post_rl_power_retention_ratio: 0.84
1051	    post_rl_auroc: 0.92
1052	    pre_rl_auroc: 0.96
1053	    auroc_drop_after_rl: 0.04
1054	    post_rl_accuracy_change: 0.012
1055	    post_rl_contam_items_accuracy: 0.82
1056	    pre_rl_contam_items_accuracy: 0.84
1057	    post_rl_non_contam_items_accuracy: 0.75
1058	    pre_rl_non_contam_items_accuracy: 0.74
1059	    post_rl_theta_shift: 0.08
1060	    mia_post_rl_auroc: 0.54
1061	    mia_pre_rl_auroc: 0.71
1062	    person_fit_vs_mia_advantage_post_rl: 0.38
1063	  result_rationale: 'GRPO 后 lz* 信号保留 84% 的机制：GRPO 优化 reward（通常是正确率或 format compliance），
1064	    对已经答对的 contaminated items 不会产生"遗忘"梯度——这些 items 已经获得最大 reward， GRPO 的梯度主要推动模型在
1065	    reward 边界附近的 items 上改进。因此 contaminated items 的 正确率几乎不变（0.84 → 0.82，仅微降 2%），而 non-contaminated
1066	    items 略有提升（+1%）。 lz* 从 -8.91 衰减到 -7.12（~20% 衰减）的原因：GRPO 对 non-contaminated items
1067	    的泛化提升 使 θ 估计上移，缩小了 contaminated items 的 "预期外正确" 幅度。但衰减有限，因为 GRPO 的泛化效应弱于 SFT 的直接
1068	    memorization 效应。 对比 MIA：Wang et al. (2025) 发现 MIA 在 post-RL 后 AUROC 接近随机（0.54），
1069	    因为 RL 重新校准了 token-level probability 分布，消除了 memorization 的 token-level 痕迹。 但 binary
1070	    response pattern 不受 probability recalibration 影响——只要 contaminated items 仍然被答对，person-fit
1071	    信号就存在。这是 person-fit "信息层级优势" 的直接体现： binary outcome 比 token probability 更鲁棒，因为
1072	    RL 可以改变 "how confident the model is" 但很难改变 "whether it gets the answer right"
1073	    on memorized items.
1074	
1075	    '
1076	  tables:
1077	  - name: 'Table 20: Pre- vs Post-RL Person-Fit (Qwen3.5-9B, 15% MMLU Contamination)'
1078	    columns:
1079	    - stage
1080	    - accuracy
1081	    - theta
1082	    - lz_star
1083	    - auroc
1084	    - power
1085	    key_rows:
1086	    - - Clean baseline
1087	      - 0.721
1088	      - 1.42
1089	      - 0.08
1090	      - —
1091	      - —
1092	    - - Post-SFT (contaminated)
1093	      - 0.764
1094	      - 1.63
1095	      - -8.91
1096	      - 0.96
1097	      - 0.97
1098	    - - Post-SFT + GRPO
1099	      - 0.776
1100	      - 1.71
1101	      - -7.12
1102	      - 0.92
1103	      - 0.91
1104	  - name: 'Table 21: Person-Fit vs MIA — Post-RL Robustness'
1105	    columns:
1106	    - method
1107	    - pre_rl_auroc
1108	    - post_rl_auroc
1109	    - auroc_retention
1110	    - info_required
1111	    key_rows:
1112	    - - IRT-FIT (lz*)
1113	      - 0.96
1114	      - 0.92
1115	      - 96%
1116	      - binary responses
1117	    - - Min-K%++
1118	      - 0.88
1119	      - 0.62
1120	      - 70%
1121	      - token log-probs
1122	    - - MIA (reference-based)
1123	      - 0.71
1124	      - 0.54
1125	      - 76%
1126	      - token log-probs + ref model
1127	  - name: 'Table 22: Item-Level Analysis — Accuracy Change After GRPO'
1128	    columns:
1129	    - item_type
1130	    - pre_rl_accuracy
1131	    - post_rl_accuracy
1132	    - change
1133	    key_rows:
1134	    - - contaminated items
1135	      - 0.84
1136	      - 0.82
1137	      - -0.02
1138	    - - non-contaminated items
1139	      - 0.74
1140	      - 0.75
1141	      - 0.01
1142	    - - contaminated hard items (diff>2)
1143	      - 0.79
1144	      - 0.76
1145	      - -0.03
1146	    - - non-contaminated hard items (diff>2)
1147	      - 0.41
1148	      - 0.43
1149	      - 0.02
1150	  figures_description:
1151	  - 'Fig 20: lz* trajectory——clean → post-SFT → post-GRPO，三个阶段的 lz* 值 + CI bar。显示信号有衰减但仍显著。'
1152	  - 'Fig 21: AUROC 对比 bar chart——IRT-FIT vs Min-K%++ vs MIA，pre-RL 和 post-RL 两组。IRT-FIT
1153	    post-RL 仍为 0.92，MIA 跌至 0.54。'
1154	  - 'Fig 22: Item-level accuracy scatterplot，pre-RL (x) vs post-RL (y)，contaminated
1155	    items 标红，non-contaminated 标灰。显示 contaminated items 集中在 (high, high) 区域。'
1156	  analysis: 'Post-RL 实验是论文回应 Wang et al. (2025) 的关键证据。形成清晰对比叙事： "MIA 在 post-RL 后失效（AUROC
1157	    0.54）但 person-fit 保留 84% 信号（AUROC 0.92）， 因为 RL recalibrates probabilities but
1158	    does not undo memorization of correct answers。" 这直接支撑 Claim 1：person-fit 不仅在 minimal-information
1159	    条件下工作， 而且对 post-training 流程具有鲁棒性。机制解释简洁有力：binary outcome > token probability in
1160	    robustness to distribution shift。
1161	
1162	    '
1163	- name: Extra Benchmarks (BBH, MATH)
1164	  plan_id: exp-extra-benchmarks
1165	  description: '添加 BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power
1166	    gap。
1167	
1168	    '
1169	  expected_results:
1170	    bbh_n_items: 6511
1171	    math_n_items: 5000
1172	    bbh_power_at_15pct: 0.89
1173	    math_power_at_15pct: 0.84
1174	    bbh_power_at_5pct: 0.52
1175	    math_power_at_5pct: 0.44
1176	    bbh_predicted_power_from_theory: 0.88
1177	    math_predicted_power_from_theory: 0.83
1178	    theory_prediction_error_bbh: 0.01
1179	    theory_prediction_error_math: 0.01
1180	    bbh_inverted_u_inflection: 0.62
1181	    math_inverted_u_inflection: 0.66
1182	    power_gap_1k_10k_filled: true
1183	  result_rationale: 'BBH (6511 items) 和 MATH (5000 items) 精确填充了 GSM8K (1319) 和 HellaSwag
1184	    (10042) 之间的 power gap。根据 power theory 公式 power ≈ Φ(δ·√n/σ − z_α)： BBH: √6511/√14042
1185	    ≈ 0.68 × MMLU power → 预测 power ≈ 0.88，实测 0.89； MATH: √5000/√14042 ≈ 0.60 × MMLU
1186	    power → 预测 power ≈ 0.83，实测 0.84。 理论预测误差 ≤ 1% 进一步验证了 power theory 的准确性。 BBH 和 MATH
1187	    的 item difficulty 分布不同于 MMLU：BBH 难度更高（mean difficulty ≈ 1.8 vs MMLU 1.2）， MATH
1188	    难度分布更宽（SD ≈ 2.1），这些差异体现在 inverted-U 拐点位置和每 item 信号强度 δ 上， 但 power theory 通过 δ
1189	    参数化吸收了这些差异。
1190	
1191	    '
1192	  tables:
1193	  - name: 'Table 23: Power Gap Analysis — All 7 Benchmarks'
1194	    columns:
1195	    - benchmark
1196	    - n_items
1197	    - power_at_15pct_simulated
1198	    - power_at_15pct_predicted
1199	    - power_at_5pct
1200	    key_rows:
1201	    - - HumanEval
1202	      - 164
1203	      - 0.243
1204	      - 0.231
1205	      - 0.07
1206	    - - ARC-C
1207	      - 1172
1208	      - 0.129
1209	      - 0.142
1210	      - 0.04
1211	    - - GSM8K
1212	      - 1319
1213	      - 0.578
1214	      - 0.561
1215	      - 0.22
1216	    - - MATH
1217	      - 5000
1218	      - 0.84
1219	      - 0.83
1220	      - 0.44
1221	    - - BBH
1222	      - 6511
1223	      - 0.89
1224	      - 0.88
1225	      - 0.52
1226	    - - HellaSwag
1227	      - 10042
1228	      - 0.733
1229	      - 0.748
1230	      - 0.34
1231	    - - MMLU
1232	      - 14042
1233	      - 0.979
1234	      - 0.981
1235	      - 0.78
1236	  figures_description:
1237	  - 'Fig 23: Power vs n_items 理论曲线，7 benchmarks 的数据点全部标注。BBH 和 MATH 精确落在曲线上。'
1238	  analysis: 'BBH 和 MATH 的加入使 power 分析从 5 个 benchmark 扩展到 7 个，覆盖了从 164 (HumanEval)
1239	    到 14042 (MMLU) 的完整 n_items 范围。7 个数据点全部落在理论预测 ±1% 内， 将 power theory 的 R² 从 0.97
1240	    推至接近 0.98。更重要的是 ARC-C 的 power 异常低（0.129 at 1172 items vs GSM8K 的 0.578 at 1319
1241	    items），说明除了 n_items 外 item quality（discrimination）也影响 power， 这在理论公式中通过 δ_per_item
1242	    体现。
1243	
1244	    '
1245	- name: Domain-Level Analysis (MMLU)
1246	  plan_id: exp-domain-analysis
1247	  description: '按 MMLU subject category 分别计算 person-fit，识别 Gemini-1.5 的 MMLU 污染模式。
1248	
1249	    '
1250	  expected_results:
1251	    n_domains_analyzed: 57
1252	    domains_with_extreme_lz_star: 57
1253	    gemini15_domain_lz_star_range: '[+0.8, +12.3]'
1254	    gemini15_domain_lz_star_mean: 4.21
1255	    gemini15_domain_lz_star_sd: 2.87
1256	    gemini15_most_aberrant_domain: abstract_algebra
1257	    gemini15_least_aberrant_domain: high_school_mathematics
1258	    contamination_pattern: uniform across all domains
1259	    domain_level_power_mean: 0.34
1260	    domain_level_power_max: 0.72
1261	    domain_level_n_items_range: '[100, 1534]'
1262	    gpt4_domain_lz_star_sd: 0.82
1263	    gpt4_domains_flagged: 0
1264	  result_rationale: 'Gemini-1.5 在所有 57 个 MMLU domains 上都是 100% 正确率，因此每个 domain 的 lz*
1265	    都为正 （over-consistent pattern）。但各 domain 的 lz* 值不同（range [+0.8, +12.3]）是因为： (1)
1266	    各 domain 的 item 数量不同（100-1534），lz* 信号强度 ∝ √n_items； (2) 各 domain 的 item difficulty
1267	    分布不同——abstract_algebra 有更多高难度 items （mean difficulty ≈ 2.4），100% 正确率与其 difficulty
1268	    分布的偏差更大。 "uniform across all domains" 的发现很重要：它排除了 "Gemini-1.5 只是在特定领域特别强" 的 innocent
1269	    explanation——如果是真实能力，应该在某些 domain 偶尔出错，而不是全面 100%。 Domain-level power 平均仅 0.34
1270	    是因为单 domain 只有 100-1534 items，远少于 full MMLU 的 14K。 这为 power theory 提供了额外验证：57
1271	    个 domain 相当于 57 个不同 n_items 的 "实验"。 GPT-4 在所有 domain 上 lz* 都正常（SD 0.82，接近理论标准差
1272	    1.0），0 个 domain flagged， 作为干净的 negative control。
1273	
1274	    '
1275	  tables:
1276	  - name: 'Table 24: MMLU Domain-Level lz* — Gemini-1.5 vs GPT-4 (Top/Bottom 5 Domains)'
1277	    columns:
1278	    - domain
1279	    - n_items
1280	    - gemini15_acc
1281	    - gemini15_lz_star
1282	    - gpt4_acc
1283	    - gpt4_lz_star
1284	    key_rows:
1285	    - - abstract_algebra
1286	      - 100
1287	      - 1.0
1288	      - 0.83
1289	      - 0.73
1290	      - -0.42
1291	    - - professional_medicine
1292	      - 272
1293	      - 1.0
1294	      - 4.21
1295	      - 0.851
1296	      - 0.67
1297	    - - high_school_mathematics
1298	      - 270
1299	      - 1.0
1300	      - 2.14
1301	      - 0.412
1302	      - -1.23
1303	    - - college_chemistry
1304	      - 100
1305	      - 1.0
1306	      - 0.91
1307	      - 0.47
1308	      - 0.31
1309	    - - global_facts
1310	      - 100
1311	      - 1.0
1312	      - 0.8
1313	      - 0.38
1314	      - -0.87
1315	    - - '...'
1316	      - '...'
1317	      - '...'
1318	      - '...'
1319	      - '...'
1320	      - '...'
1321	    - - miscellaneous
1322	      - 783
1323	      - 1.0
1324	      - 7.89
1325	      - 0.872
1326	      - 0.42
1327	    - - clinical_knowledge
1328	      - 265
1329	      - 1.0
1330	      - 3.87
1331	      - 0.792
1332	      - -0.18
1333	  - name: 'Table 25: Domain-Level Power as Function of n_items'
1334	    columns:
1335	    - n_items_bin
1336	    - n_domains
1337	    - mean_power_at_15pct
1338	    - predicted_from_theory
1339	    key_rows:
1340	    - - 100-150
1341	      - 22
1342	      - 0.18
1343	      - 0.17
1344	    - - 150-300
1345	      - 21
1346	      - 0.31
1347	      - 0.33
1348	    - - 300-600
1349	      - 9
1350	      - 0.52
1351	      - 0.5
1352	    - - 600-1000
1353	      - 3
1354	      - 0.64
1355	      - 0.67
1356	    - - '>1000'
1357	      - 2
1358	      - 0.72
1359	      - 0.74
1360	  figures_description:
1361	  - 'Fig 24: MMLU domain-level lz* heatmap for all 12 models × 57 domains。Gemini-1.5
1362	    行全部为正侧红色。GPT-4 行为中性灰色。'
1363	  - 'Fig 25: Gemini-1.5 domain-level lz* vs domain n_items scatter，显示 √n 依赖关系。'
1364	  analysis: Domain analysis 为 Gemini-1.5 case study 提供了 fine-grained 证据："uniform contamination
1365	    across all 57 MMLU domains" 排除了能力解释（没有任何模型在所有领域同等强）， 支持系统性 benchmark memorization
1366	    的结论。与 GPT-4 的对比提供了干净的 negative control。 Domain-level power 分析作为 bonus，为 power
1367	    theory 提供了 57 个额外的 (n_items, power) 数据点。
1368	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e91e154-6661-4bbc-8334-ee5be1b79c87",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a6854eb8e8fb54b59",
  "type": "user",
  "uuid": "cdd53016-6155-4cd3-90a4-68e82f01caf5",
  "sourceToolAssistantUUID": "6e91e154-6661-4bbc-8334-ee5be1b79c87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T09:10:45.098Z_

<details open><summary>🔧 Tool call — Read · `toolu_015ZSgeD7AhnGJFhxxyKSbds`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdd53016-6155-4cd3-90a4-68e82f01caf5",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZV66dTnUqFWmxRnMrd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07ebd3e8-39b0-475b-9187-72e0c7914911",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiBEZTeSMafc5bFXbXPNUC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 455,
      "cache_read_input_tokens": 28436,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 455
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 28436,
          "cache_creation_input_tokens": 455,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 455,
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

_source line 26 · 2026-05-20T09:10:45.384Z_

<details><summary>↩ Tool result · `toolu_015ZSgeD7AhnGJFhxxyKSbds`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{tabularx}
9	\usepackage[margin=2.5cm]{geometry}
10	\usepackage{natbib}
11	\usepackage{hyperref}
12	\usepackage{xcolor}
13	\usepackage{array}
14	\usepackage{caption}
15	
16	\newcolumntype{R}{>{\raggedleft\arraybackslash}p{1.2cm}}
17	\newcolumntype{L}{>{\raggedright\arraybackslash}p{2.8cm}}
18	
19	\title{IRT-FIT: Detecting Benchmark Contamination in Large Language Models\\via Item Response Theory Person-Fit Statistics}
20	
21	\author{Anonymous}
22	\date{}
23	
24	\begin{document}
25	\maketitle
26	
27	% ============================================================
28	\begin{abstract}
29	Benchmark contamination undermines the reliability of LLM evaluation, yet all existing detection methods require privileged access---training data, token probabilities, model weights, or specially crafted prompts. We establish the \emph{minimal-information operating point} on the contamination detection frontier by repurposing Item Response Theory (IRT) person-fit statistics, which require only binary (correct/incorrect) response patterns. Our framework, \textbf{IRT-FIT}, introduces three contributions: (1) a two-sided detection framework capturing both partial contamination (aberrant patterns, $l_{z}^{*} \ll 0$) and full contamination (over-consistent patterns, $l_{z}^{*} \gg 0$); (2) a theoretical characterization showing detection power is a predictable function of benchmark size ($n_{\text{items}}$) and contamination level, with an analytically derivable inverted-U signal structure ($R^2=0.97$); and (3) a large-scale audit of 2{,}847 Open LLM Leaderboard models revealing a 12\% overall contamination flag rate. In controlled experiments with ground-truth contamination (QLoRA SFT on Qwen3.5-9B and Gemma-4-31B), IRT-FIT achieves AUROC 0.96 at 15\% contamination and 0.82 at 5\%---outperforming ConStat (0.83/0.61) and Min-K\%++ (0.88/0.72) while requiring strictly less information. The person-fit signal survives post-RL training (AUROC 0.92 after GRPO), whereas MIA-based methods degrade to near-chance (AUROC 0.54). IRT-FIT is the only method that simultaneously addresses partial, full, and post-RL contamination at the minimal-information level.
30	\end{abstract}
31	
32	% ============================================================
33	\section{Introduction}
34	\label{sec:intro}
35	
36	Benchmark contamination---the inclusion of evaluation data in training corpora---is a growing threat to LLM evaluation integrity. As training data scales to trillions of tokens and benchmarks proliferate, the probability of inadvertent or intentional overlap increases. This undermines the fundamental assumption that benchmark performance reflects genuine capability.
37	
38	Existing detection methods span a spectrum of information requirements. N-gram overlap methods require access to training data. Membership inference attacks (MIA) and Min-K\%++ \citep{shi2024detecting} require token-level log-probabilities. Time Travel probing \citep{oren2024proving} requires specially crafted prompts. ConStat \citep{dekoninck2024constat} requires the ability to re-test models on rephrased items. \citet{wang2025reassessing} demonstrate that all MIA-based methods fail under post-RL contamination, highlighting the fragility of token-level signals.
39	
40	A contaminated LLM answering benchmark questions is functionally analogous to an examinee with item preknowledge---a problem studied for decades in psychometrics under the rubric of \emph{person-fit analysis}. Person-fit statistics such as $l_z^*$ \citep{snijders2001person} detect aberrant response patterns: examinees who answer difficult items correctly while failing easy ones, or who answer all items correctly including those far beyond their estimated ability. These statistics require only binary response data and a calibrated item bank---precisely the information available from standard LLM benchmark evaluation.
41	
42	We introduce \textbf{IRT-FIT}, a framework that establishes the \emph{minimal-information operating point} on the contamination detection frontier. Our contributions are:
43	
44	\begin{enumerate}
45	    \item \textbf{Minimal-information detection.} We show that IRT person-fit statistics detect benchmark contamination using only binary response patterns, achieving AUROC 0.96 at 15\% contamination---outperforming methods requiring token probabilities or re-testing.
46	    \item \textbf{Theoretical characterization.} We derive an analytic power formula relating detection power to benchmark size and contamination level ($R^2=0.97$), and prove that the inverted-U signal structure has a predictable inflection point determined by item difficulty distributions.
47	    \item \textbf{Large-scale empirical evidence.} We audit 2{,}847 Open LLM Leaderboard models, revealing a 12\% contamination flag rate increasing from 6\% (2023 Q1) to 18\% (2024 Q1). We identify Gemini-1.5's 100\% MMLU accuracy as systematic contamination ($l_z^*=+34.75$, $\hat{\theta}=0.78$).
48	\end{enumerate}
49	
50	% ============================================================
51	\section{Background}
52	\label{sec:background}
53	
54	\subsection{Item Response Theory}
55	
56	IRT models the probability of a correct response as a function of examinee ability $\theta$ and item parameters. We adopt the four-parameter logistic (4PL) model:
57	\begin{equation}
58	P_i(\theta) = c_i + (d_i - c_i) \cdot \frac{1}{1 + e^{-a_i(\theta - b_i)}}
59	\label{eq:4pl}
60	\end{equation}
61	where $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is the guessing parameter, and $d_i$ is the feasibility (upper asymptote) parameter. The 3PL model is the special case $d_i=1$.
62	
63	\subsection{Person-Fit Statistics}
64	
65	The $l_z$ statistic \citep{drasgow1985appropriateness} measures the fit of an individual response pattern to the IRT model:
66	\begin{equation}
67	l_z = \frac{\sum_{i=1}^{n} \left[ x_i \log P_i(\hat{\theta}) + (1-x_i) \log(1-P_i(\hat{\theta})) \right] - E[l_0]}{SD[l_0]}
68	\end{equation}
69	where $x_i \in \{0,1\}$ is the response to item $i$ and $\hat{\theta}$ is the MLE of ability. \citet{snijders2001person} derived the corrected statistic $l_z^*$ that accounts for estimation error in $\hat{\theta}$, yielding $l_z^* \sim N(0,1)$ under the null hypothesis of model fit.
70	
71	% ============================================================
72	\section{Method: IRT-FIT}
73	\label{sec:method}
74	
75	\subsection{Two-Sided Detection Framework}
76	
77	Traditional person-fit analysis tests only $l_z^* < c_{\alpha}$ (aberrant patterns). We extend to two-sided testing because contamination produces two distinct signal regimes:
78	
79	\begin{itemize}
80	    \item \textbf{Partial contamination} ($l_z^* \ll 0$): The model memorizes a subset of items, answering difficult contaminated items correctly while failing easy non-contaminated items---an aberrant pattern.
81	    \item \textbf{Full contamination} ($l_z^* \gg 0$): The model memorizes all items, producing a response pattern that is \emph{over-consistent}---all items correct, including those far beyond estimated ability.
82	\end{itemize}
83	
84	We apply the two-sided test $|l_z^*| > c_{\alpha/2}$ with Benjamini--Hochberg FDR control for multiple comparisons across models and benchmarks.
85	
86	\subsection{Multiscale Aggregation ($l_{zm}$)}
87	
88	Following \citet{hong2021multiscale}, we aggregate per-benchmark $l_z^*$ values into a single model-level index:
89	\begin{equation}
90	l_{zm} = \frac{1}{\sqrt{K}} \sum_{k=1}^{K} |l_{z,k}^*|
91	\end{equation}
92	where $K$ is the number of benchmarks evaluated. Under the null, $l_{zm}$ is approximately standard normal (verified by Kolmogorov--Smirnov test, $p=0.312$).
93	
94	\subsection{Power Theory}
95	
96	Building on Snijders' variance formula, we derive the detection power as:
97	\begin{equation}
98	\text{power} \approx \Phi\!\left(\frac{\delta \sqrt{n}}{\sigma_{l_z^*}} - z_{\alpha}\right)
99	\label{eq:power}
100	\end{equation}
101	where $\delta = E[\log L_{\text{contam}} - \log L_{\text{clean}}]$ per item is the expected log-likelihood shift induced by contamination, and $n$ is the number of items. The inverted-U inflection point $c^*$ satisfies:
102	\begin{equation}
103	c^* = \arg\min_{c} \left| E_\theta\!\left[\sum_i f(x_i, P_i) \mid \text{contam}=c\right] - E_\theta\!\left[\sum_i f(x_i, P_i) \mid \text{contam}=0\right] \right|
104	\end{equation}
105	where $f(x_i, P_i) = x_i \log P_i + (1-x_i)\log(1-P_i)$.
106	
107	% ============================================================
108	\section{Controlled Contamination Experiments}
109	\label{sec:controlled}
110	
111	\subsection{Ground-Truth Contamination}
112	\label{sec:ctrl-contam}
113	
114	We inject known contamination via QLoRA SFT on two base models (Qwen3.5-9B and Gemma-4-31B), training on 0\%/5\%/10\%/15\%/25\%/50\% of MMLU items to establish a ground-truth contamination--$l_z^*$ mapping.
115	
116	\begin{table}[t]
117	\centering
118	\caption{Controlled contamination: $l_z^*$ by model and contamination level (MMLU).}
119	\label{tab:ctrl-contam}
120	\small
121	\begin{tabular}{llrrrr}
122	\toprule
123	\textbf{Model} & \textbf{Contam.} & \textbf{Acc.} & $\hat{\theta}$ & $l_z^*$ & \textbf{Flag} \\
124	\midrule
125	Qwen3.5-9B & 0\% & .721 & 1.42 & 0.08 & .047 \\
126	Qwen3.5-9B & 5\% & .738 & 1.51 & $-$3.72 & .82 \\
127	Qwen3.5-9B & 10\% & .756 & 1.59 & $-$6.45 & .94 \\
128	Qwen3.5-9B & 15\% & .764 & 1.63 & $-$8.91 & .97 \\
129	Qwen3.5-9B & 25\% & .787 & 1.71 & $-$11.34 & .99 \\
130	Qwen3.5-9B & 50\% & .831 & 1.89 & $-$4.82 & .87 \\
131	\midrule
132	Gemma-4-31B & 0\% & .793 & 1.81 & 0.15 & .041 \\
133	Gemma-4-31B & 5\% & .808 & 1.88 & $-$3.21 & .78 \\
134	Gemma-4-31B & 15\% & .831 & 1.97 & $-$7.63 & .95 \\
135	Gemma-4-31B & 50\% & .874 & 2.14 & $-$5.14 & .84 \\
136	\bottomrule
137	\end{tabular}
138	\end{table}
139	
140	\begin{table}[t]
141	\centering
142	\caption{Detection performance (AUROC) by contamination level.}
143	\label{tab:auroc}
144	\small
145	\begin{tabular}{lrrrr}
146	\toprule
147	\textbf{Contam.} & \textbf{Qwen} & \textbf{Gemma} & \textbf{Pooled} & \textbf{Cohen's $d$} \\
148	\midrule
149	5\% & 0.84 & 0.80 & 0.82 & 1.1 \\
150	10\% & 0.93 & 0.91 & 0.92 & 1.8 \\
151	15\% & 0.97 & 0.95 & 0.96 & 2.3 \\
152	25\% & 0.99 & 0.98 & 0.99 & 2.8 \\
153	50\% & 0.94 & 0.91 & 0.93 & 1.6 \\
154	\bottomrule
155	\end{tabular}
156	\end{table}
157	
158	Table~\ref{tab:ctrl-contam} shows a monotonic increase in $|l_z^*|$ from 0\% to 25\% contamination, followed by a decrease at 50\%---the inverted-U pattern. Both models exhibit consistent behavior (effect size difference $<$15\%), ruling out model-specific artifacts. False positive rate at $\alpha=0.05$ is well-calibrated: 0.047 (Qwen) and 0.041 (Gemma). The minimum detectable contamination level is 5\% (AUROC 0.82, Table~\ref{tab:auroc}).
159	
160	\begin{table}[t]
161	\centering
162	\caption{Contamination selectivity: accuracy change on contaminated vs.\ non-contaminated items (Qwen3.5-9B).}
163	\label{tab:selectivity}
164	\small
165	\begin{tabular}{lrrrr}
166	\toprule
167	\textbf{Contam.} & \multicolumn{2}{c}{\textbf{Contam.\ Items}} & \multicolumn{2}{c}{\textbf{Non-Contam.\ Items}} \\
168	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
169	 & Before & Lift & Before & Lift \\
170	\midrule
171	5\% & .56 & +.31 & .73 & +.014 \\
172	15\% & .54 & +.30 & .73 & +.018 \\
173	25\% & .55 & +.31 & .73 & +.024 \\
174	50\% & .57 & +.31 & .73 & +.037 \\
175	\bottomrule
176	\end{tabular}
177	\end{table}
178	
179	Table~\ref{tab:selectivity} confirms that SFT contamination is highly selective: accuracy on contaminated items increases by $\sim$31 percentage points, while non-contaminated items show only 1.4--3.7\% generalization. The generalization ratio is 0.12, far too small to smooth the aberrant pattern.
180	
181	\subsection{Inverted-U Signal Characterization}
182	\label{sec:inverted-u}
183	
184	We extend simulations to 60\%/75\%/90\%/100\% contamination levels, characterizing the complete inverted-U curve across four benchmarks.
185	
186	\begin{table}[t]
187	\centering
188	\caption{$l_z^*$ as a function of contamination level (mean $\pm$ SD, 100 replications).}
189	\label{tab:inverted-u}
190	\small
191	\begin{tabular}{lrrrr}
192	\toprule
193	\textbf{Contam.} & \textbf{MMLU} & \textbf{HSwag} & \textbf{GSM8K} & \textbf{ARC-C} \\
194	\midrule
195	0\% & 0.01 & 0.03 & $-$0.02 & 0.01 \\
196	5\% & $-$3.41 & $-$1.82 & $-$1.34 & $-$0.42 \\
197	10\% & $-$6.12 & $-$3.45 & $-$2.51 & $-$0.78 \\
198	15\% & $-$8.31 & $-$4.72 & $-$3.38 & $-$1.02 \\
199	25\% & $-$12.08 & $-$6.21 & $-$4.53 & $-$1.31 \\
200	50\% & $-$5.73 & $-$2.89 & $-$1.67 & $-$0.43 \\
201	60\% & $-$1.24 & 0.82 & $-$0.34 & 0.21 \\
202	75\% & 8.42 & 5.67 & 3.21 & 1.12 \\
203	90\% & 19.31 & 12.45 & 6.78 & 2.34 \\
204	100\% & 28.50 & 18.20 & 8.70 & 3.01 \\
205	\bottomrule
206	\end{tabular}
207	\end{table}
208	
209	\begin{table}[t]
210	\centering
211	\caption{Two-sided detection power at various contamination levels.}
212	\label{tab:two-sided-power}
213	\small
214	\begin{tabular}{lrrrr}
215	\toprule
216	\textbf{Contam.} & \textbf{MMLU} & \textbf{HSwag} & \textbf{GSM8K} & \textbf{ARC-C} \\
217	\midrule
218	5\% & .780 & .340 & .220 & .060 \\
219	15\% & .979 & .733 & .578 & .129 \\
220	25\% & .998 & .891 & .743 & .201 \\
221	50\% & .872 & .514 & .298 & .080 \\
222	75\% & .991 & .934 & .712 & .187 \\
223	100\% & 1.000 & .998 & .962 & .478 \\
224	\bottomrule
225	\end{tabular}
226	\end{table}
227	
228	Tables~\ref{tab:inverted-u} and \ref{tab:two-sided-power} reveal the inverted-U structure. The $l_z^*$ signal peaks negatively around 25\% contamination (MMLU: $-$12.08), crosses zero near 60--65\%, and becomes strongly positive at high contamination (100\%: +28.50). The inflection point varies by benchmark: 0.65 (MMLU), 0.60 (HellaSwag), 0.70 (GSM8K), consistent with differences in item difficulty distributions. Two-sided power dips at the inflection point (50\% contamination) but recovers for higher levels, whereas one-sided testing would have zero power above the inflection.
229	
230	\subsection{Power Theory Derivation}
231	\label{sec:power-theory}
232	
233	Equation~\ref{eq:power} predicts detection power as a function of $n_{\text{items}}$. Table~\ref{tab:power-theory} shows the theory fits simulation data with $R^2=0.97$.
234	
235	\begin{table}[t]
236	\centering
237	\caption{Theoretical vs.\ simulated power at 15\% contamination.}
238	\label{tab:power-theory}
239	\small
240	\begin{tabular}{rrrr}
241	\toprule
242	$n_{\text{items}}$ & \textbf{Predicted} & \textbf{Simulated} & \textbf{$|\Delta|$} \\
243	\midrule
244	100 & .089 & .092 & .003 \\
245	500 & .312 & .298 & .014 \\
246	1{,}000 & .491 & .503 & .012 \\
247	1{,}319 & .578 & .578 & .000 \\
248	5{,}000 & .862 & .851 & .011 \\
249	10{,}042 & .964 & .958 & .006 \\
250	14{,}042 & .981 & .979 & .002 \\
251	\bottomrule
252	\end{tabular}
253	\end{table}
254	
255	\begin{table}[t]
256	\centering
257	\caption{Inverted-U inflection point: predicted vs.\ observed.}
258	\label{tab:inflection}
259	\small
260	\begin{tabular}{lrrrr}
261	\toprule
262	\textbf{Benchmark} & $n$ & \textbf{Pred.} & \textbf{Obs.} & $|\Delta|$ \\
263	\midrule
264	MMLU & 14{,}042 & 0.64 & 0.65 & 0.01 \\
265	HellaSwag & 10{,}042 & 0.59 & 0.60 & 0.01 \\
266	GSM8K & 1{,}319 & 0.68 & 0.70 & 0.02 \\
267	ARC-C & 1{,}172 & 0.62 & 0.64 & 0.02 \\
268	HumanEval & 164 & 0.61 & 0.63 & 0.02 \\
269	\bottomrule
270	\end{tabular}
271	\end{table}
272	
273	\begin{table}[t]
274	\centering
275	\caption{Minimum $n_{\text{items}}$ for 80\% power at various contamination levels.}
276	\label{tab:min-n}
277	\small
278	\begin{tabular}{lrr}
279	\toprule
280	\textbf{Contam.} & \textbf{Theory} & \textbf{Simulation} \\
281	\midrule
282	5\% & 9{,}800 & 10{,}200 \\
283	10\% & 4{,}700 & 4{,}900 \\
284	15\% & 3{,}200 & 3{,}350 \\
285	25\% & 1{,}800 & 1{,}900 \\
286	\bottomrule
287	\end{tabular}
288	\end{table}
289	
290	Table~\ref{tab:inflection} shows the inflection point can be predicted from item difficulty distributions alone, with error $\leq$0.02. Table~\ref{tab:min-n} provides practitioners with concrete guidance: detecting 15\% contamination requires $\geq$3{,}200 items; detecting 5\% contamination requires $\geq$9{,}800 items. This explains why ARC-C (1{,}172 items) yields only 12.9\% power---not a method failure, but insufficient information.
291	
292	% ============================================================
293	\section{Comparisons and Robustness}
294	\label{sec:comparison}
295	
296	\subsection{Baseline Comparison}
297	\label{sec:baselines}
298	
299	\begin{table}[t]
300	\centering
301	\caption{Baseline comparison on controlled contamination ground truth.}
302	\label{tab:baseline}
303	\small
304	\begin{tabular}{llrrrr}
305	\toprule
306	\textbf{Method} & \textbf{Info Required} & \textbf{5\%} & \textbf{15\%} & \textbf{25\%} & \textbf{Type-I} \\
307	\midrule
308	IRT-FIT & binary & .82 & .96 & .99 & .042 \\
309	ConStat & binary + retest & .61 & .83 & .91 & .053 \\
310	Min-K\%++ & token log-probs & .72 & .88 & .95 & .048 \\
311	\bottomrule
312	\end{tabular}
313	\end{table}
314	
315	\begin{table}[t]
316	\centering
317	\caption{Detection frontier: information access vs.\ detection power (AUROC at 15\% contam.).}
318	\label{tab:frontier}
319	\small
320	\begin{tabular}{llrl}
321	\toprule
322	\textbf{Info Level} & \textbf{Method} & \textbf{AUROC} & \textbf{Scalability} \\
323	\midrule
324	Binary only & IRT-FIT & .96 & Any model w/ scores \\
325	Binary + retest & ConStat & .83 & Requires live access \\
326	Token probs & Min-K\%++ & .88 & Requires API logprobs \\
327	Training data & N-gram & --- & Requires training data \\
328	Weights & Probing & --- & Requires open weights \\
329	\bottomrule
330	\end{tabular}
331	\end{table}
332	
333	IRT-FIT achieves the highest AUROC while requiring the least information (Table~\ref{tab:baseline}). The advantage over ConStat (+0.13 at 15\%) stems from IRT-FIT's use of item-level response patterns rather than aggregate performance statistics. The advantage over Min-K\%++ (+0.08) is notable given that Min-K\%++ has access to richer token-level information. Table~\ref{tab:frontier} positions these results on the detection frontier.
334	
335	\subsection{Post-RL Robustness}
336	\label{sec:post-rl}
337	
338	\citet{wang2025reassessing} show that MIA-based methods fail after reinforcement learning. We test whether IRT-FIT survives post-RL by applying GRPO training to a contaminated Qwen3.5-9B (15\% MMLU SFT contamination).
339	
340	\begin{table}[t]
341	\centering
342	\caption{Pre- vs.\ post-RL person-fit (Qwen3.5-9B, 15\% MMLU contamination).}
343	\label{tab:post-rl}
344	\small
345	\begin{tabular}{lrrrrr}
346	\toprule
347	\textbf{Stage} & \textbf{Acc.} & $\hat{\theta}$ & $l_z^*$ & \textbf{AUROC} & \textbf{Power} \\
348	\midrule
349	Clean & .721 & 1.42 & 0.08 & --- & --- \\
350	Post-SFT & .764 & 1.63 & $-$8.91 & .96 & .97 \\
351	Post-SFT+GRPO & .776 & 1.71 & $-$7.12 & .92 & .91 \\
352	\bottomrule
353	\end{tabular}
354	\end{table}
355	
356	\begin{table}[t]
357	\centering
358	\caption{Person-fit vs.\ MIA: post-RL robustness comparison.}
359	\label{tab:post-rl-comparison}
360	\small
361	\begin{tabular}{lrrrl}
362	\toprule
363	\textbf{Method} & \textbf{Pre-RL} & \textbf{Post-RL} & \textbf{Retain.} & \textbf{Info} \\
364	\midrule
365	IRT-FIT & .96 & .92 & 96\% & binary \\
366	Min-K\%++ & .88 & .62 & 70\% & token probs \\
367	MIA (ref.) & .71 & .54 & 76\% & token probs + ref \\
368	\bottomrule
369	\end{tabular}
370	\end{table}
371	
372	GRPO reduces the $l_z^*$ signal by only 20\% ($-$8.91 $\to$ $-$7.12), retaining 96\% of AUROC (Table~\ref{tab:post-rl}). In contrast, MIA degrades to near-chance (0.54) because RL recalibrates token-level probability distributions while leaving binary response patterns largely intact (Table~\ref{tab:post-rl-comparison}). Item-level analysis confirms: contaminated items retain 97.6\% of their accuracy after GRPO (0.84 $\to$ 0.82), while non-contaminated items gain +1\%. RL changes \emph{how confident} the model is, but not \emph{whether it answers correctly} on memorized items.
373	
374	\subsection{4PL vs.\ 3PL Ablation}
375	\label{sec:ablation}
376	
377	\begin{table}[t]
378	\centering
379	\caption{4PL vs.\ 3PL detection performance.}
380	\label{tab:4pl-3pl}
381	\small
382	\begin{tabular}{lrrr}
383	\toprule
384	\textbf{Metric} & \textbf{4PL} & \textbf{3PL} & $\Delta$ \\
385	\midrule
386	AUROC @ 15\% & .960 & .910 & +.050 \\
387	False alarm ($\alpha$=.05) & .042 & .078 & $-$.036 \\
388	Power @ 15\% MMLU & .979 & .934 & +.045 \\
389	Power @ 5\% MMLU & .780 & .690 & +.090 \\
390	Mean $|l_z^*|$ clean & 0.83 & 1.17 & $-$0.34 \\
391	Mean $|l_z^*|$ contam.\ 15\% & 8.91 & 8.04 & +0.87 \\
392	\bottomrule
393	\end{tabular}
394	\end{table}
395	
396	\begin{table}[t]
397	\centering
398	\caption{Impact of $d$ parameter by item difficulty band.}
399	\label{tab:d-param}
400	\small
401	\begin{tabular}{lrrrr}
402	\toprule
403	\textbf{Difficulty} & $n$ & Mean $d$ & $\Delta l_z^*$ clean & $\Delta l_z^*$ contam. \\
404	\midrule
405	$<0.5$ (easy) & 2{,}814 & .97 & $-$0.08 & 0.12 \\
406	0.5--1.5 & 5{,}621 & .93 & $-$0.21 & 0.43 \\
407	1.5--2.5 & 3{,}891 & .89 & $-$0.38 & 0.78 \\
408	$>2.5$ (hard) & 1{,}716 & .82 & $-$0.67 & 1.45 \\
409	\bottomrule
410	\end{tabular}
411	\end{table}
412	
413	The 4PL model improves over 3PL primarily through better calibration on high-difficulty items (Table~\ref{tab:4pl-3pl}). The $d$ parameter absorbs natural variation in ceiling performance, reducing false alarms from 7.8\% to 4.2\%. The improvement concentrates on items with difficulty $>$2.5, where $d<0.85$ (Table~\ref{tab:d-param}). These are precisely the items where contamination signals are strongest, making the 4PL advantage non-trivial for detection despite modest overall improvement.
414	
415	\subsection{Multiscale $l_{zm}$ Statistic}
416	\label{sec:lzm}
417	
418	\begin{table}[t]
419	\centering
420	\caption{$l_{zm}$ results on PSN-IRT 12 models.}
421	\label{tab:lzm}
422	\small
423	\begin{tabular}{lrrl}
424	\toprule
425	\textbf{Model} & $l_{zm}$ & \textbf{Flag} & \textbf{\#Bench.\ Flagged} \\
426	\midrule
427	Gemini-1.5 & 18.42 & YES & 3 \\
428	GPT-4 & $-$0.87 & no & 0 \\
429	Llama-2-70B & $-$3.21 & YES & 1 \\
430	Claude-3-Opus & 0.42 & no & 0 \\
431	Mistral-7B & $-$2.45 & no & 0 \\
432	\bottomrule
433	\end{tabular}
434	\end{table}
435	
436	\begin{table}[t]
437	\centering
438	\caption{$l_{zm}$ vs.\ single-benchmark detection (15\% contamination).}
439	\label{tab:lzm-vs-single}
440	\small
441	\begin{tabular}{lrrr}
442	\toprule
443	\textbf{Method} & \textbf{AUROC} & \textbf{Power} & \textbf{FA Rate} \\
444	\midrule
445	$l_z^*$ (MMLU only) & .96 & .979 & .042 \\
446	$l_z^*$ (best single) & .96 & .979 & .042 \\
447	$l_{zm}$ (all benchmarks) & .98 & .990 & .037 \\
448	\bottomrule
449	\end{tabular}
450	\end{table}
451	
452	Cross-benchmark aggregation via $l_{zm}$ yields a modest but consistent improvement: AUROC increases from 0.96 to 0.98 (Table~\ref{tab:lzm-vs-single}). The gain comes from information pooling across $\sim$27K total items and from the fact that genuine contamination signals are correlated across benchmarks while false positives are not. The null distribution is well-calibrated (KS $p=0.312$). Gemini-1.5 produces the most extreme $l_{zm}=18.42$, aggregating both positive (MMLU) and negative (GSM8K, HumanEval) regime signals.
453	
454	% ============================================================
455	\section{Large-Scale Empirical Study}
456	\label{sec:empirical}
457	
458	\subsection{Two-Sided Detection on PSN-IRT Models}
459	\label{sec:two-sided}
460	
461	We apply the two-sided framework to 12 models from the PSN-IRT dataset across 5 benchmarks (60 model-benchmark pairs).
462	
463	\begin{table}[t]
464	\centering
465	\caption{Two-sided detection results (selected model-benchmark pairs).}
466	\label{tab:two-sided-results}
467	\small
468	\begin{tabular}{llrrl}
469	\toprule
470	\textbf{Model} & \textbf{Bench.} & $l_z^*$ & \textbf{Side} & \textbf{Flag} \\
471	\midrule
472	Gemini-1.5 & MMLU & +34.75 & positive & YES \\
473	Gemini-1.5 & GSM8K & $-$15.71 & negative & YES \\
474	Gemini-1.5 & HumanEval & $-$12.37 & negative & YES \\
475	GPT-4 & MMLU & $-$1.23 & --- & no \\
476	Llama-2-70B & ARC-C & $-$3.87 & negative & YES \\
477	\bottomrule
478	\end{tabular}
479	\end{table}
480	
481	\begin{table}[t]
482	\centering
483	\caption{One-sided vs.\ two-sided detection comparison (FDR = 0.05).}
484	\label{tab:one-vs-two}
485	\small
486	\begin{tabular}{lrrrr}
487	\toprule
488	\textbf{Method} & \textbf{Total} & \textbf{Partial} & \textbf{Full} & \textbf{FDR} \\
489	\midrule
490	One-sided ($l_z^* < c$) & 2 & 2 & 0 & .05 \\
491	Two-sided ($|l_z^*| > c$) & 4 & 2 & 2 & .05 \\
492	\bottomrule
493	\end{tabular}
494	\end{table}
495	
496	Gemini-1.5 on MMLU ($l_z^*=+34.75$, 95\% CI $[32.1, 37.4]$) exemplifies the positive regime: 100\% accuracy with estimated $\hat{\theta}=0.78$ indicates systematic memorization, not extraordinary ability (Table~\ref{tab:two-sided-results}). One-sided testing completely misses this signal and the two additional flagged models at the positive extreme (Table~\ref{tab:one-vs-two}).
497	
498	\subsection{Leaderboard Audit}
499	\label{sec:leaderboard}
500	
501	We run inference on 2{,}847 models from Open LLM Leaderboard v1, computing $l_z^*$ for each model-benchmark pair (18.5 GPU-hours total).
502	
503	\begin{table}[t]
504	\centering
505	\caption{Leaderboard audit summary.}
506	\label{tab:leaderboard}
507	\small
508	\begin{tabular}{lrrrrr}
509	\toprule
510	\textbf{Bench.} & $n$ & \textbf{Neg.} & \textbf{Pos.} & \textbf{Rate} & \textbf{Med.\ $l_z^*$} \\
511	\midrule
512	MMLU & 2{,}847 & 312 & 115 & .15 & $-$6.73 \\
513	HSwag & 2{,}847 & 198 & 58 & .09 & $-$4.21 \\
514	ARC-C & 2{,}847 & 142 & 57 & .07 & $-$3.12 \\
515	GSM8K & 2{,}182 & 178 & 63 & .11 & $-$5.42 \\
516	Overall & 2{,}847 & 255 & 87 & .12 & --- \\
517	\bottomrule
518	\end{tabular}
519	\end{table}
520	
521	\begin{table}[t]
522	\centering
523	\caption{Contamination rate by time period.}
524	\label{tab:temporal}
525	\small
526	\begin{tabular}{lrrr}
527	\toprule
528	\textbf{Period} & \textbf{Models} & \textbf{Flagged} & \textbf{Rate} \\
529	\midrule
530	2023 Q1--Q2 & 487 & 29 & .06 \\
531	2023 Q3--Q4 & 891 & 98 & .11 \\
532	2024 Q1--Q2 & 1{,}103 & 198 & .18 \\
533	2024 Q3+ & 366 & 51 & .14 \\
534	\bottomrule
535	\end{tabular}
536	\end{table}
537	
538	\begin{table}[t]
539	\centering
540	\caption{Most anomalous models (top 3 by $|l_z^*|$).}
541	\label{tab:top-anomalous}
542	\small
543	\begin{tabular}{llrrrl}
544	\toprule
545	\textbf{Model} & \textbf{Bench.} & \textbf{Acc.} & $l_z^*$ & \textbf{Side} & \textbf{Params} \\
546	\midrule
547	anon-7b-v3 & MMLU & .847 & $-$22.4 & neg & 7B \\
548	llm-ft-2b & MMLU & .912 & +18.7 & pos & 2B \\
549	bench-tuned-3b & GSM8K & .891 & $-$17.3 & neg & 3B \\
550	\bottomrule
551	\end{tabular}
552	\end{table}
553	
554	The audit reveals 342 flagged models (12\% overall), with MMLU most affected at 15\% (Table~\ref{tab:leaderboard}). Contamination rates increase from 6\% in early 2023 to 18\% in early 2024 (Table~\ref{tab:temporal}), consistent with the proliferation of benchmark-tuned models on the leaderboard. Table~\ref{tab:top-anomalous} shows the most extreme cases, including a 2B-parameter model achieving 91.2\% MMLU accuracy ($l_z^*=+18.7$) and a 7B model with $l_z^*=-22.4$. Cross-benchmark consistency is 34\%: about one-third of flagged models show anomalies on multiple benchmarks.
555	
556	\subsection{Additional Benchmarks: BBH and MATH}
557	\label{sec:extra-bench}
558	
559	\begin{table}[t]
560	\centering
561	\caption{Power analysis across all 7 benchmarks (15\% contamination).}
562	\label{tab:power-all}
563	\small
564	\begin{tabular}{lrrrr}
565	\toprule
566	\textbf{Benchmark} & $n$ & \textbf{Sim.} & \textbf{Pred.} & \textbf{5\%} \\
567	\midrule
568	HumanEval & 164 & .243 & .231 & .07 \\
569	ARC-C & 1{,}172 & .129 & .142 & .04 \\
570	GSM8K & 1{,}319 & .578 & .561 & .22 \\
571	MATH & 5{,}000 & .840 & .830 & .44 \\
572	BBH & 6{,}511 & .890 & .880 & .52 \\
573	HellaSwag & 10{,}042 & .733 & .748 & .34 \\
574	MMLU & 14{,}042 & .979 & .981 & .78 \\
575	\bottomrule
576	\end{tabular}
577	\end{table}
578	
579	Adding BBH (6{,}511 items) and MATH (5{,}000 items) fills the power gap between GSM8K and HellaSwag (Table~\ref{tab:power-all}). All seven benchmarks fall within 1--2\% of theoretical predictions, further validating the power formula. ARC-C is a notable outlier: its power (0.129) is much lower than GSM8K (0.578) despite similar $n_{\text{items}}$ (1{,}172 vs.\ 1{,}319), indicating that item discrimination quality also affects power---a factor captured by the $\delta$ term in Equation~\ref{eq:power}.
580	
581	\subsection{MMLU Domain-Level Analysis}
582	\label{sec:domain}
583	
584	\begin{table}[t]
585	\centering
586	\caption{MMLU domain-level $l_z^*$: Gemini-1.5 vs.\ GPT-4 (selected domains).}
587	\label{tab:domain}
588	\small
589	\begin{tabular}{lrrrrr}
590	\toprule
591	\textbf{Domain} & $n$ & \multicolumn{2}{c}{\textbf{Gemini-1.5}} & \multicolumn{2}{c}{\textbf{GPT-4}} \\
592	\cmidrule(lr){3-4} \cmidrule(lr){5-6}
593	 & & Acc. & $l_z^*$ & Acc. & $l_z^*$ \\
594	\midrule
595	abstract\_algebra & 100 & 1.00 & +0.83 & .73 & $-$0.42 \\
596	prof\_medicine & 272 & 1.00 & +4.21 & .85 & +0.67 \\
597	hs\_mathematics & 270 & 1.00 & +2.14 & .41 & $-$1.23 \\
598	college\_chem & 100 & 1.00 & +0.91 & .47 & +0.31 \\
599	miscellaneous & 783 & 1.00 & +7.89 & .87 & +0.42 \\
600	clinical\_know & 265 & 1.00 & +3.87 & .79 & $-$0.18 \\
601	\bottomrule
602	\end{tabular}
603	\end{table}
604	
605	\begin{table}[t]
606	\centering
607	\caption{Domain-level power as a function of $n_{\text{items}}$.}
608	\label{tab:domain-power}
609	\small
610	\begin{tabular}{lrrr}
611	\toprule
612	$n_{\text{items}}$ \textbf{bin} & \textbf{Domains} & \textbf{Power} & \textbf{Pred.} \\
613	\midrule
614	100--150 & 22 & .18 & .17 \\
615	150--300 & 21 & .31 & .33 \\
616	300--600 & 9 & .52 & .50 \\
617	600--1{,}000 & 3 & .64 & .67 \\
618	$>$1{,}000 & 2 & .72 & .74 \\
619	\bottomrule
620	\end{tabular}
621	\end{table}
622	
623	Gemini-1.5 achieves 100\% accuracy across all 57 MMLU domains, with uniformly positive $l_z^*$ values ranging from +0.8 to +12.3 (Table~\ref{tab:domain}). This uniformity rules out the innocent explanation that Gemini-1.5 is simply exceptionally strong in certain domains---no model genuinely excels equally across abstract algebra, clinical knowledge, and high school mathematics without occasionally erring. GPT-4, by contrast, shows normally distributed $l_z^*$ (SD=0.82) with zero domains flagged. The 57 MMLU domains provide 57 additional validation points for the power theory (Table~\ref{tab:domain-power}), with predicted power matching observed power within 2--3 percentage points across all domain size bins.
624	
625	% ============================================================
626	\section{Related Work}
627	\label{sec:related}
628	
629	\paragraph{Benchmark contamination detection.}
630	\citet{shi2024detecting} introduce Min-K\%++ for membership inference using token-level likelihood. \citet{oren2024proving} propose Time Travel testing via prompting. \citet{dekoninck2024constat} use performance consistency across rephrased items. \citet{dong2024generalization} study generalization-based detection. \citet{wang2025reassessing} show all MIA-based methods fail post-RL. Our work establishes a strictly lower information requirement.
631	
632	\paragraph{IRT for LLMs.}
633	\citet{polo2024tinybenchmarks} use IRT for efficient benchmarking. \citet{gu2024psnirt} calibrate 4PL IRT models on LLM response data (PSN-IRT). We build on PSN-IRT's item parameters but pivot from benchmarking to contamination detection via person-fit analysis.
634	
635	\paragraph{Person-fit in psychometrics.}
636	\citet{drasgow1985appropriateness} introduce $l_z$; \citet{snijders2001person} derive the corrected $l_z^*$. \citet{meijer2001methodology} survey applications including cheating detection. \citet{hong2021multiscale} propose multiscale aggregation. We are the first to apply person-fit statistics to LLM evaluation.
637	
638	% ============================================================
639	\section{Conclusion}
640	\label{sec:conclusion}
641	
642	We introduced IRT-FIT, a framework that detects benchmark contamination using only binary response patterns---the minimal-information operating point on the detection frontier. Three findings stand out: (1) person-fit statistics achieve AUROC 0.96 at 15\% contamination, surpassing methods requiring token probabilities or re-testing; (2) detection power follows a predictable analytic function of benchmark size ($R^2=0.97$), with the inverted-U signal structure theoretically derivable from item difficulty distributions; (3) a leaderboard-scale audit of 2{,}847 models reveals 12\% overall contamination rates, increasing from 6\% to 18\% over 2023--2024.
643	
644	The person-fit signal survives post-RL training (AUROC 0.92 after GRPO) while MIA degrades to near-chance (0.54), because binary response patterns are robust to the probability recalibration that RL induces. IRT-FIT is the only method that simultaneously addresses partial contamination (aberrant patterns), full contamination (over-consistent patterns), and post-RL contamination at the minimal-information level.
645	
646	\paragraph{Limitations.}
647	Detection power depends on benchmark size: benchmarks with fewer than $\sim$3{,}200 items have limited power at 15\% contamination ($<$80\%). The method targets intentional SFT-style contamination and leaderboard gaming; gradual pretraining exposure that yields smooth capability improvement is not in scope. The 4PL IRT model assumes unidimensionality, which may not hold for heterogeneous benchmarks.
648	
649	% ============================================================
650	\bibliographystyle{plainnat}
651	\begin{thebibliography}{20}
652	
653	\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}
654	Jasper Dekoninck, Mark Niklas M{\"u}ller, and Martin Vechev.
655	\newblock ConStat: Performance-based contamination detection in large language models.
656	\newblock In \emph{NeurIPS}, 2024.
657	
658	\bibitem[Dong et~al.(2024)]{dong2024generalization}
659	Yihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, and Ge Li.
660	\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.
661	\newblock In \emph{ACL}, 2024.
662	
663	\bibitem[Drasgow et~al.(1985)]{drasgow1985appropriateness}
664	Fritz Drasgow, Michael~V. Levine, and Mary~E. Williams.
665	\newblock Appropriateness measurement with polychotomous item response models and standardized indices.
666	\newblock \emph{British Journal of Mathematical and Statistical Psychology}, 38(1):67--86, 1985.
667	
668	\bibitem[Gu et~al.(2024)]{gu2024psnirt}
669	Guanyu Gu, Yixiao Li, and Yun-Fei Liu.
670	\newblock PSN-IRT: A psychometric benchmark calibration framework for large language models.
671	\newblock In \emph{AAAI}, 2024.
672	
673	\bibitem[Hong et~al.(2021)]{hong2021multiscale}
674	Sophia Hong, David~J. Lin, and Ying Cheng.
675	\newblock Multiscale person-fit statistics.
676	\newblock \emph{Applied Psychological Measurement}, 45(6):417--434, 2021.
677	
678	\bibitem[Meijer and Sijtsma(2001)]{meijer2001methodology}
679	Rob~R. Meijer and Klaas Sijtsma.
680	\newblock Methodology review: Evaluating person fit.
681	\newblock \emph{Applied Psychological Measurement}, 25(2):107--135, 2001.
682	
683	\bibitem[Oren et~al.(2024)]{oren2024proving}
684	Yonatan Oren, Nicole Meister, Niladri~S. Chatterji, Faisal Ladhak, and Tatsunori Hashimoto.
685	\newblock Proving test set contamination in black-box language models.
686	\newblock In \emph{ICLR (Spotlight)}, 2024.
687	
688	\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}
689	Felipe~Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, and Mikhail Yurochkin.
690	\newblock tinyBenchmarks: evaluating LLMs with fewer examples.
691	\newblock In \emph{ICML}, 2024.
692	
693	\bibitem[Shi et~al.(2024)]{shi2024detecting}
694	Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer.
695	\newblock Detecting pretraining data from large language models.
696	\newblock In \emph{ICLR}, 2024.
697	
698	\bibitem[Snijders(2001)]{snijders2001person}
699	Tom~A.B. Snijders.
700	\newblock Asymptotic null distribution of person fit statistics with estimated item parameters.
701	\newblock \emph{Psychometrika}, 66(3):331--342, 2001.
702	
703	\bibitem[Wang et~al.(2025)]{wang2025reassessing}
704	Cheng Wang, Yiwei Wang, Bryan Hooi, and Yujun Cai.
705	\newblock Reassessing contamination detection: MIA fails under post-RL training.
706	\newblock \emph{arXiv preprint arXiv:2501.xxxxx}, 2025.
707	
708	\end{thebibliography}
709	
710	\end{document}
711	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07ebd3e8-39b0-475b-9187-72e0c7914911",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a6854eb8e8fb54b59",
  "type": "user",
  "uuid": "111d97fb-2c0f-4b6c-a76b-5dbc06579ae5",
  "sourceToolAssistantUUID": "07ebd3e8-39b0-475b-9187-72e0c7914911",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-20T09:10:49.526Z_

Now let me also check the experiment plan for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "111d97fb-2c0f-4b6c-a76b-5dbc06579ae5",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZVNHTtfsUNSz79E3Po",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d54a80fb-b81d-4d88-8ba7-156c73fc85ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WQLz3RmbbcXBLmmcCqPjzT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 38442,
      "cache_read_input_tokens": 28891,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 38442,
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

_source line 28 · 2026-05-20T09:10:51.030Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KRaDME5FhkobPYhJM62M8y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d54a80fb-b81d-4d88-8ba7-156c73fc85ae",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZVNHTtfsUNSz79E3Po",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d5e03d9-3121-411c-ab05-fd1fb4136995",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WQLz3RmbbcXBLmmcCqPjzT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 38442,
      "cache_read_input_tokens": 28891,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 38442
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 28891,
          "cache_creation_input_tokens": 38442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 38442,
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

_source line 29 · 2026-05-20T09:10:51.077Z_

<details><summary>↩ Tool result · `toolu_01KRaDME5FhkobPYhJM62M8y`</summary>

```text
1	experiments:
2	  # === P0: Must-do (headline results) ===
3	
4	  - id: exp-two-sided
5	    claim: 2
6	    description: "实现双侧检测框架：|lz*| > threshold 或分别设正/负阈值。用 Phase B 数据验证（Gemini-1.5 case study）。包括 bootstrap confidence interval 和 FDR 控制。"
7	    priority: P0
8	    gpu_budget_hours: 0
9	    deps: []
10	    status: planned
11	    notes: "CPU only. 基于已有 Phase B personfit_matrix.csv 重新分析。"
12	
13	  - id: exp-extended-sim
14	    claim: 2
15	    description: "扩展 Phase A 模拟：添加 60%/75%/90% contamination levels，修复 100% NaN 处理（让 MLE boundary θ=4.0 正常计算 lz*），精确刻画 inverted-U 拐点。同时计算 two-sided power curves（正向 lz*>1.96 和负向 lz*<-1.96 分别的 detection rate），量化 Claim 2 的 dual-regime signal structure。"
16	    priority: P0
17	    gpu_budget_hours: 0
18	    deps: [exp-two-sided]
19	    status: planned
20	    notes: "CPU only. 依赖 exp-two-sided 的双侧框架定义。"
21	
22	  - id: exp-ctrl-contam
23	    claim: "1,2,3"
24	    description: "控制实验：在 Qwen3.5-9B 和 Gemma-4-31B 上，用 QLoRA SFT 注入 0%/5%/10%/15%/25%/50% benchmark items，测量微调前后 person-fit 变化。建立 ground-truth contamination → lz* 映射。"
25	    priority: P0
26	    gpu_budget_hours: 80
27	    deps: [exp-two-sided]
28	    status: planned
29	    notes: "Qwen3.5-9B: 1× RTX 5090 (~8GB). Gemma-4-31B: 1× RTX 5090 (~20GB). 2 模型 × 6 levels × ~3-7 hrs = ~60-80 GPU-hrs."
30	
31	  - id: exp-power-theory
32	    claim: 2
33	    description: "推导 power 与 n_items 的解析关系（基于 Snijders 2001 lz* 方差公式）。验证理论曲线与 Phase A 模拟结果的拟合度。将 inverted-U 从经验观察升级为理论命题。"
34	    priority: P0
35	    gpu_budget_hours: 0
36	    deps: [exp-extended-sim]
37	    status: planned
38	    notes: "纯理论推导 + 数值验证。CPU only."
39	
40	  # === P1: Important (robustness + differentiation) ===
41	
42	  - id: exp-leaderboard-data-recon
43	    claim: 3
44	    description: "Open LLM Leaderboard v1 数据可用性调研：确认 HuggingFace open-llm-leaderboard-old/results 是否包含 per-item binary response logs（不仅是 aggregate scores）。如果可用，评估数据量（多少模型有 per-item data）、格式、覆盖的 benchmarks。如果不可用，估算自己跑推理的 GPU 预算增量。"
45	    priority: P0
46	    gpu_budget_hours: 0
47	    deps: []
48	    status: planned
49	    notes: "纯调研，CPU only。结果直接决定 exp-leaderboard-audit 的可行性和 GPU 预算。"
50	
51	  - id: exp-leaderboard-audit
52	    claim: 3
53	    description: "Open LLM Leaderboard v1 大规模扫描：对所有可用模型计算 person-fit。绘制 per-benchmark 污染率随时间趋势。"
54	    priority: P1
55	    gpu_budget_hours: 20
56	    deps: [exp-two-sided, exp-leaderboard-data-recon]
57	    status: planned
58	    notes: "GPU 预算取决于 data-recon 结果。如果 per-item logs 可用则 ~20 GPU-hrs（纯计算），不可用则 200+ GPU-hrs（需跑推理）。"
59	
60	  - id: exp-4pl-ablation
61	    claim: 1
62	    description: "4PL vs 3PL(d=1) ablation：比较两种参数化下的检测灵敏度差异。量化 feasibility parameter d 对 false alarm 和 detection power 的影响。"
63	    priority: P1
64	    gpu_budget_hours: 0
65	    deps: [exp-extended-sim]
66	    status: planned
67	    notes: "CPU only. 用已有 PSN-IRT 参数，固定 d=1 重新计算。"
68	
69	  - id: exp-baseline-comparison
70	    claim: 1
71	    description: "与现有方法对比（ConStat, Min-K%++）：在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs baselines 的 AUROC/Type-I error。量化 minimal-information 的代价（power 损失）。"
72	    priority: P0-end
73	    gpu_budget_hours: 30
74	    deps: [exp-ctrl-contam]
75	    status: planned
76	    notes: "Claim 1 的可信度依赖此对比。exp-ctrl-contam 完成后立即执行。ConStat 需要 re-test，Min-K%++ 需要 token probabilities。"
77	
78	  - id: exp-multiscale-lzm
79	    claim: "1,3"
80	    description: "实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021）——跨 benchmark 聚合的标准化 lz* 总分，提供整体污染指标。在 PSN-IRT 12 模型 + 控制实验模型上验证。"
81	    priority: P1
82	    gpu_budget_hours: 0
83	    deps: [exp-two-sided]
84	    status: planned
85	    notes: "CPU only. 需要实现 lzm 公式。"
86	
87	  # === P2: Nice-to-have (expanded scope) ===
88	
89	  - id: exp-post-rl
90	    claim: 1
91	    description: "Post-RL 假设检验：在 Qwen3.5-9B 上先 SFT 污染再 GRPO 训练，测试 person-fit 是否在 RL 后仍保持检测力。回应 Wang et al. (2025) 的 MIA 失效问题。"
92	    priority: P2
93	    gpu_budget_hours: 40
94	    deps: [exp-ctrl-contam]
95	    status: planned
96	    notes: "GRPO 训练需要 reward model 或 rule-based reward。可能需要 2× RTX 5090。"
97	
98	  - id: exp-extra-benchmarks
99	    claim: "2,3"
100	    description: "扩展 benchmark：BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power gap。需要获取 4PL 参数（PSN-IRT 可能已有）。"
101	    priority: P2
102	    gpu_budget_hours: 10
103	    deps: [exp-extended-sim]
104	    status: planned
105	    notes: "取决于 PSN-IRT 是否包含这些 benchmark 的参数。如果没有，需要自己校准 4PL（GPU + 大量推理）。"
106	
107	  - id: exp-domain-analysis
108	    claim: 3
109	    description: "MMLU domain-level 分析：按 subject category 分别计算 person-fit，识别 Gemini-1.5 的 MMLU 污染是全面的还是集中在特定 domain。"
110	    priority: P2
111	    gpu_budget_hours: 0
112	    deps: [exp-two-sided]
113	    status: planned
114	    notes: "CPU only. 需要 MMLU item-to-domain 映射。"
115	
116	# === GPU Budget Summary ===
117	# P0: ~110 GPU-hrs (exp-ctrl-contam 80 + exp-baseline-comparison 30)
118	# P1: ~20 GPU-hrs (exp-leaderboard-audit, 取决于 data-recon 结果)
119	# P2: ~50 GPU-hrs (exp-post-rl 40 + exp-extra-benchmarks 10)
120	# Total: ~180 GPU-hrs (well within 320-420 budget)
121	# Available: 4× RTX 5090 32GB
122	# Note: 如果 leaderboard per-item data 不可用，需额外 200+ GPU-hrs 跑推理
123	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d5e03d9-3121-411c-ab05-fd1fb4136995",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a6854eb8e8fb54b59",
  "type": "user",
  "uuid": "a79cc90a-27e4-408b-bc25-2888899edf8b",
  "sourceToolAssistantUUID": "5d5e03d9-3121-411c-ab05-fd1fb4136995",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-20T09:10:54.311Z_

Now I have thorough understanding of the paper, the project internals, and the imagined experimental results. Let me now write the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a79cc90a-27e4-408b-bc25-2888899edf8b",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZVmr3mfULJ2h9HL2YZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f52f0ab5-d358-4083-9610-7f65ee1304de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRc9vjUkVr6uYmbSzxNu5G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2740,
      "cache_read_input_tokens": 67333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2740,
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

_source line 31 · 2026-05-20T09:10:55.157Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018zgr66qvRoAp3c5sq8ocsp`</summary>

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
  "parentUuid": "f52f0ab5-d358-4083-9610-7f65ee1304de",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZVmr3mfULJ2h9HL2YZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "606d2aa1-f7d5-443f-b839-e76f2debaeb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRc9vjUkVr6uYmbSzxNu5G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2740,
      "cache_read_input_tokens": 67333,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2740
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 67333,
          "cache_creation_input_tokens": 2740,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2740,
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

_source line 32 · 2026-05-20T09:10:55.165Z_

<details><summary>↩ Tool result · `toolu_018zgr66qvRoAp3c5sq8ocsp`</summary>

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
  "parentUuid": "606d2aa1-f7d5-443f-b839-e76f2debaeb8",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a6854eb8e8fb54b59",
  "type": "user",
  "uuid": "698c4d22-1209-474e-a73c-a07d236019e4",
  "sourceToolAssistantUUID": "606d2aa1-f7d5-443f-b839-e76f2debaeb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T09:12:13.282Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01NARs7gD7KmeL6pLAsnGV7q`</summary>

```json
{
  "report": "# Reviewer 1 (R1): Methodology and Experiments\n\n## Summary\n\nThis paper repurposes IRT person-fit statistics (lz*) from psychometrics to detect benchmark contamination in LLMs. The key idea is that contaminated models produce aberrant or over-consistent response patterns detectable from binary (correct/incorrect) data alone — the \"minimal-information operating point\" on the detection frontier. Contributions include a two-sided detection framework, an analytic power theory with inverted-U characterization, and a large-scale audit of 2,847 Open LLM Leaderboard models. Controlled experiments on Qwen3.5-9B and Gemma-4-31B establish ground-truth validation. The method survives post-RL training while MIA-based alternatives degrade.\n\n---\n\n## 1. Methodology Soundness\n\n**Strengths.** The statistical foundations are solid. The lz* statistic (Snijders, 2001) is well-established in psychometrics with known asymptotic properties under correctly specified IRT models. The two-sided extension is well-motivated: the paper clearly articulates why partial contamination (aberrant patterns, lz* << 0) and full contamination (over-consistent patterns, lz* >> 0) produce qualitatively different signals, and the Gemini-1.5 case (lz*=+34.75 with theta=0.78) is a compelling demonstration that one-sided testing misses an entire contamination regime. BH-FDR control for multiple comparisons is appropriate.\n\nThe power theory (Eq. 4) is a genuine contribution. Deriving power as a function of n_items and contamination level, with R^2=0.97 against simulation, provides actionable guidance (e.g., >=3,200 items needed for 80% power at 15% contamination). The inverted-U inflection point formula, predicting the zero-crossing within 0.02 of observed values across 5 benchmarks, elevates the inverted-U from empirical curiosity to theoretically grounded phenomenon.\n\n**Concerns.**\n\n(a) **Unidimensionality assumption.** The 4PL model assumes unidimensional ability. MMLU spans 57 domains — the unidimensionality assumption is clearly violated. The paper uses per-benchmark MLE theta (Decision D006 correctly identifies that global PSN-IRT theta causes 93% false flags), but even within a single benchmark like MMLU, multidimensionality is substantial. The domain-level analysis (Table 23) partially addresses this but does not formally test or correct for it. How sensitive is lz* to violations of unidimensionality? Snijders' N(0,1) guarantee requires correct model specification.\n\n(b) **Dependence on PSN-IRT parameters.** The entire framework inherits PSN-IRT's 4PL item parameter estimates. If these parameters are biased or miscalibrated (PSN-IRT uses neural networks, not classical MLE), the lz* null distribution may not hold. The null check (KS test, p>0.05) is reassuring but only verifies marginal distributional shape on 12 models — not a stringent test of calibration at the tails where detection decisions are made.\n\n(c) **lzm aggregation formula.** The paper defines lzm = (1/sqrt(K)) * sum(|lz*_k|), citing Hong et al. (2021). Under the null, individual |lz*_k| follow a half-normal distribution, not N(0,1). The claim that lzm is \"approximately standard normal\" under the null (verified by KS p=0.312) seems unlikely for the formula as written — the mean of K half-normals divided by sqrt(K) does not converge to N(0,1). This needs clarification or correction. Is it perhaps sum(lz*_k)/sqrt(K) without absolute values, or is there a different standardization?\n\n---\n\n## 2. Experimental Design\n\n**Strengths.** The controlled contamination experiments are well-designed: two architectures (Qwen3.5-9B, Gemma-4-31B), six contamination levels, QLoRA SFT which is realistic for leaderboard gaming. The selectivity analysis (Table 3) showing +31pp lift on contaminated items vs +1.4-3.7% on non-contaminated items directly validates the mechanism. Cohen's d=2.3 at 15% contamination is a large effect. The consistency across two base models (effect size difference <15%) strengthens the claim.\n\nThe extended simulation (0-100%, 100 replications) provides thorough characterization. BBH and MATH fill the power gap convincingly.\n\n**Concerns.**\n\n(d) **Baseline comparison fairness.** ConStat achieves 0.83 AUROC vs IRT-FIT's 0.96. But ConStat was designed for a different threat model (testing consistency across rephrased items). Comparing AUROC on SFT-contaminated models may not be ConStat's intended use case — SFT contamination is permanent, making re-test scores identical, which inherently disadvantages ConStat. A fairer comparison would include ConStat's intended scenario (e.g., models that memorize specific phrasings but fail rephrased versions). The paper should acknowledge this asymmetry.\n\n(e) **Leaderboard audit ground truth.** The 12% flagged rate is reported as \"contamination,\" but there is no ground truth for any of the 2,847 models. Some flagged models may have legitimate reasons for aberrant patterns (e.g., models fine-tuned for specific domains, quantized models with unusual error patterns). The temporal trend (6% to 18%) is suggestive but confounded with model size and architecture trends over the same period. The paper should more carefully distinguish \"flagged\" from \"contaminated.\"\n\n(f) **Post-RL experiment scope.** Only one RL algorithm (GRPO) on one model (Qwen3.5-9B) at one contamination level (15%). The claim \"person-fit signal survives post-RL training\" is stated broadly but tested narrowly. DPO, PPO, and other RLHF variants may behave differently. The 20% signal decay (lz* from -8.91 to -7.12) is non-trivial — with more aggressive RL or different reward shaping, the signal might degrade further.\n\n---\n\n## 3. Results Analysis\n\nThe results broadly support the claims. The power theory predictions match simulation within 1-2% across 7 benchmarks and 57 MMLU domains — this is the paper's strongest quantitative result.\n\n**Suspicious pattern.** ARC-C power (0.129) is dramatically lower than GSM8K (0.578) despite similar n_items (1,172 vs 1,319). The paper attributes this to item discrimination quality (delta term), but this 4.5x difference is large and undermines the narrative that power is primarily a function of n_items. The power formula should be validated on benchmarks where item quality varies systematically, or the claim should be qualified.\n\n**Table 1 vs Table 4 consistency.** In controlled experiments (Table 1), Qwen at 50% contamination gives lz*=-4.82. In simulation (Table 4), MMLU at 50% gives lz*=-5.73. These are reasonably close but the controlled experiment uses real SFT while simulation uses item-level response manipulation — the agreement suggests the simulation is well-calibrated, but the gap (~16%) should be discussed.\n\n---\n\n## 4. Reproducibility\n\nThe method is clearly described and should be reproducible given PSN-IRT parameters. The 4PL model, lz* formula, two-sided test, and BH-FDR correction are all standard. The power formula is explicit. However:\n\n- PSN-IRT item parameters are not released with this paper. Reproducibility depends entirely on the PSN-IRT dataset being publicly available. The paper should state this dependency explicitly and confirm parameter availability.\n- The QLoRA SFT protocol (hyperparameters, training data format, number of epochs) is not described in sufficient detail.\n- The GRPO training details (reward function, number of steps, hyperparameters) are absent.\n\n---\n\n## 5. Limitations and Concerns\n\n1. **Scope limited to SFT contamination.** The method targets intentional benchmark fine-tuning. Pretraining data contamination — arguably the more pervasive and important problem — produces smooth distributional improvements that person-fit statistics cannot detect. This is acknowledged but deserves more prominence.\n\n2. **Ceiling effects.** For high-ability models (theta > 3), most items have P_i(theta) > 0.95. The expected response pattern is nearly all-correct, making it difficult to distinguish genuine high ability from contamination. DeepSeek-V3 (theta=3.77) would be essentially undetectable even if contaminated.\n\n3. **Item parameter drift.** If benchmark items are widely known and models are trained on them, the effective item parameters change over time. The PSN-IRT parameters were calibrated on a specific set of models at a specific time — applying them to models from different time periods assumes parameter stability.\n\n4. **Binary data limitation is also a weakness.** While \"minimal information\" is positioned as a strength, binary data genuinely contains less information than token probabilities. The paper's framing sometimes implies IRT-FIT is strictly superior, but at equal information access, Min-K%++ or MIA might outperform.\n\n---\n\n## 6. Questions for Authors\n\n**Q1.** How does lz* behave when contamination occurs through pretraining data exposure (not SFT)? Even a brief simulation showing the sensitivity boundary between detectable SFT contamination and undetectable pretraining exposure would strengthen the scope claims.\n\n**Q2.** The lzm formula uses absolute values of lz*, but the claimed N(0,1) null distribution seems inconsistent with this. Can you provide the derivation or reference for the null distribution of your specific lzm formulation? Is this truly from Hong et al. (2021) or a modification?\n\n**Q3.** For the leaderboard audit, how do you handle models with legitimately unusual capability profiles (e.g., code-specialized models tested on MMLU, or multilingual models)? These could produce aberrant patterns without contamination. What is your estimated false discovery rate in the audit?\n\n**Q4.** The 4PL parameters from PSN-IRT were estimated using neural networks on 12 models. How robust are these parameters to the specific model sample? If re-estimated on a different set of 12 models, would the lz* values change substantially?\n\n**Q5.** At 50% contamination, AUROC drops to 0.93 (Table 2) due to the inverted-U. In practice, an adversary who knows about this method could target contamination levels near the inflection point (~60-65%) to minimize detectability. How does the two-sided test perform at exactly the inflection point, and what is the residual power?\n\n---\n\n## 7. Score\n\n**Overall Assessment: 4.0 (Conference-level)**\n\nThe paper presents a well-motivated method with solid statistical foundations, thorough experiments, and a genuine conceptual contribution (the detection frontier framing and the power theory). The two-sided detection framework is a clean extension with clear empirical justification. The leaderboard audit at 2,847-model scale is a unique capability.\n\nThe main weaknesses are: (1) the fairness of baseline comparisons (ConStat evaluated outside its intended scenario), (2) the narrow scope of post-RL validation (single algorithm, single model), (3) the unidimensionality assumption on inherently multidimensional benchmarks, and (4) insufficient discussion of the method's inability to detect pretraining contamination. The lzm null distribution claim needs technical correction.\n\nThis is a solid contribution to NLP evaluation methodology. The \"minimal-information operating point\" framing is clean and the power theory is the kind of characterization that has lasting value. With revisions addressing the baseline fairness, post-RL scope, and lzm correction, this would be a strong accept.\n\n---\n\n## 8. Confidence\n\n**Confidence: 4/5** (High confidence). I have expertise in statistical testing methodology, IRT, and LLM evaluation. I am less certain about the practical details of post-RL training dynamics and the PSN-IRT parameter estimation procedure.\n",
  "project": "irt_personfit_contam",
  "tier": "best",
  "dream_id": "dream_20260520T082549",
  "overall_score": "4.0 — Conference (Weak Accept)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "698c4d22-1209-474e-a73c-a07d236019e4",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZW5DKeYLD8RcVrS88Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb9fc449-9a54-40b9-9a1c-4a7edda2f285",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019eueTntaD9JMe2WnWJqnhA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 743,
      "cache_read_input_tokens": 70073,
      "output_tokens": 3088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 743
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3088,
          "cache_read_input_tokens": 70073,
          "cache_creation_input_tokens": 743,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 743,
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

_source line 34 · 2026-05-20T09:12:16.553Z_

<details><summary>↩ Tool result · `toolu_01NARs7gD7KmeL6pLAsnGV7q`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/review_report.md\", \"dream_id\": \"dream_20260520T082549\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb9fc449-9a54-40b9-9a1c-4a7edda2f285",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a6854eb8e8fb54b59",
  "type": "user",
  "uuid": "4b586fed-464f-45ce-977b-fd33071e90cd",
  "sourceToolAssistantUUID": "eb9fc449-9a54-40b9-9a1c-4a7edda2f285",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-20T09:12:27.286Z_

Review submitted. Here is a summary of the key findings:

**Score: 4.0 (Conference-level / Weak Accept) | Confidence: 4/5**

**Main strengths identified:**
- Solid statistical foundations building on well-established psychometric theory (Snijders 2001)
- Two-sided detection framework is well-motivated with clear empirical justification (Gemini-1.5 case)
- Power theory (R^2=0.97 fit, inflection point prediction within 0.02) is the paper's strongest quantitative contribution
- Controlled experiments are well-designed with two architectures, six contamination levels, and convincing selectivity analysis (Cohen's d=2.3)
- Leaderboard audit at 2,847-model scale is a unique capability no other method can match

**Critical issues raised:**
1. **lzm null distribution error** — the formula uses |lz*| (absolute values), but claims N(0,1) null. Half-normal aggregation does not yield N(0,1). Needs correction.
2. **Unfair baseline comparison** — ConStat is evaluated outside its intended threat model (permanent SFT contamination makes re-test scores identical, inherently disadvantaging it)
3. **Narrow post-RL validation** — only GRPO on one model at one contamination level; claim is stated broadly but tested narrowly
4. **Unidimensionality assumption violated** — MMLU spans 57 domains; Snijders' N(0,1) guarantee requires correct model specification
5. **Leaderboard audit lacks ground truth** — 12% "flagged" is not 12% "contaminated"; confounds with model architecture/size trends

**Questions for authors:** Pretraining contamination sensitivity, lzm derivation, false discovery rate in audit, PSN-IRT parameter robustness, adversarial inflection-point targeting.

Report saved to `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b586fed-464f-45ce-977b-fd33071e90cd",
  "isSidechain": true,
  "agentId": "a6854eb8e8fb54b59",
  "requestId": "req_011CbDZc544vCRL1voBZ16qA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "918db953-c9d9-4fe6-83e8-5e69b8fe6630",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SE3Dsjzo3GVNoyAZtKY2rT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3221,
      "cache_read_input_tokens": 70816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3221,
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
