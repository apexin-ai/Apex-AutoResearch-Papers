# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus is **Novelty, Positioning, and Related Work**. Review the 

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a967392e829aaef63.jsonl`
- **Structured JSON:** [`f764ea62e2b33b16c44d.json`](../../sessions/f7/f764ea62e2b33b16c44d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

38 recorded events

### User

_source line 1 · 2026-05-14T10:17:40.802Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus is **Novelty, Positioning, and Related Work**. Review the paper below using a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.

## Paper Summary

**Title:** Solver Trace Ablation Reveals Reward Hacking in GRPO-Trained Formal Reasoners: Diagnosis, Taxonomy, and Goodhart's Law

The paper proposes Solver Trace Ablation (STA), a diagnostic framework for detecting reward hacking in GRPO-trained formal reasoners. STA derives Intensional Structural Reward (ISR) via leave-one-out (LOO) ablation on solver input components. Applied to GRPO-trained FOL formalizers on FOLIO, three claims:

1. **ISR as Diagnostic**: exec-only GRPO achieves 93% PR while ISR collapses 0.64→0.003. Taxonomy of 5 hacking strategies.
2. **ISR as Reward (Goodhart)**: At β=0.1 additive bonus, directional improvement (mean ISR ratio ~2.1× over random, 3 seeds) but fragile (95% CI crosses 1.0, genuine rate delta +3.7pp not significant). At β=0.3, Goodhart collapse.
3. **Cross-Logic Transfer to Prolog**: Mechanical transfer works, diagnostic power weaker. Preliminary.

Additional: O(1) vs O(N) ablation (negative), curriculum ablation, SFT baseline, multi-logic training (negative interference), zero-shot cross-logic transfer (null), 1.5B vs 8B scaling (single seed).

## Related Work Section (from paper)

**Reward Hacking and Goodhart's Law**: Cites Gao et al. (2023) on reward model overoptimization in RLHF, Skalse et al. (2022) on defining reward hacking, Manheim & Garrabrant (2019) on Goodhart's Law categories, Karwowski et al. (2024) on Goodhart in language model alignment. Paper claims novelty in applying these concepts to formal reasoning GRPO where reward (execution success) is verifiable rather than learned.

**GRPO and Formal Reasoning**: Cites Shao et al. (2024) DeepSeekMath, Han et al. (2022) FOLIO. Mentions EVOM uses scalar execution rewards only, Mellgren et al. hand-craft Prolog-specific penalties. Claims no prior work systematically diagnoses reward hacking in formal reasoning.

**Feature Attribution and Ablation**: Cites Lundberg & Lee (2017) SHAP. Explicitly acknowledges ISR is not algorithmically novel—it's LOO applied to formal logic. Claims novelty is the application as hacking diagnostic + empirical Goodhart analysis.

**Neural Theorem Proving**: Cites LeanDojo (Yang et al. 2023), Baldur (First et al. 2023). Differentiates: they study interactive theorem proving (Lean/Isabelle); this paper studies autoformalization verified by automated provers (Prover9).

## Paper Structure (12 pages including appendix)
- Section 1: Introduction (1.5 pages)
- Section 2: Related Work (1 page)  
- Section 3: Method (1.5 pages) — Problem Setting, ISR definition, ISR as Reward (additive + convex), Hacking Taxonomy
- Section 4: Experiments (4 pages) — 10 subsections covering all claims and ablations
- Section 5: Discussion (1 page)
- Section 6: Limitations (1 page) — Statistical Power, Single Dataset, ISR vs Semantic Faithfulness, Computational Cost, Prolog, SMT-LIB
- Section 7: Conclusion (0.5 page)
- Appendix A: Hacking Taxonomy Details (1 page)
- Appendix B: Reproducibility Details (brief)
- References: 8 citations

## Key Results for Context

- ISR collapse trajectory: 0.64→0.13→0.003 over 100→500→1000 steps (Table 1)
- 5-mode hacking taxonomy from manual annotation of 200 outputs/condition
- β=0.1 sweet spot fragile: 3-seed 95% CI [0.85, 3.45] crosses 1.0
- Seed variability: same hyperparameters → 3 qualitatively different hacking strategies
- O(1) approximation fails (r=0.21 with full ISR)
- SFT baseline: highest ISR (0.45) but lowest PR (48%) — establishes PR-ISR tradeoff
- Prolog: mechanical STA transfer works but ISR diagnostic power weaker
- 8B model: hacks more "efficiently" (lower ISR, more components, earlier collapse)

## Your Review Focus (R2: Novelty + Related Work)

Evaluate:
1. **Novelty**: Is the contribution genuinely new? LOO ablation itself is standard — is the application to formal reasoning reward hacking sufficiently novel?
2. **Positioning**: How well does the paper situate itself relative to prior work? Are there missing references?
3. **Significance**: Would this paper change how the community thinks about or evaluates formal reasoning systems?
4. **Scope and ambition**: Is the scope appropriate for a top venue? Too narrow (only FOLIO/Qwen3)? Or well-scoped given the depth?
5. **Writing quality and clarity**: Is the paper well-organized? Are the claims clearly stated with appropriate hedging?
6. **Missing related work**: Any significant omissions in the literature review?

Consider these potentially relevant works not cited:
- Pan et al. (2022) — reward hacking in code generation
- Uesato et al. (2022) — process vs outcome rewards
- Lightman et al. (2023) — process reward models for math
- Cobbe et al. (2021) — verifiers for math
- EVOR/code generation reward hacking literature
- Formal verification literature on proof quality metrics

Provide your review in this format:
```
## R2 Review: Novelty and Related Work

### Summary
[2-3 sentences]

### Strengths
[Numbered list]

### Weaknesses
[Numbered list]

### Questions for Authors
[Numbered list]

### Missing References
[List any significant omissions]

### Novelty Score: X/4
### Significance Score: X/4  
### Clarity Score: X/4
### Overall Score: X/6
### Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a967392e829aaef63",
  "type": "user",
  "uuid": "9dfdd0c7-4fd5-457b-a51f-5aef1f031691",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T10:17:40.805Z_

```json
{
  "parentUuid": "9dfdd0c7-4fd5-457b-a51f-5aef1f031691",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
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
  "uuid": "979c4197-e058-44bb-9a16-f526ebae9552",
  "timestamp": "2026-05-14T10:17:40.805Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T10:17:44.052Z_



I'll review the paper by first reading the full manuscript and any related project files to ensure a thorough evaluation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "979c4197-e058-44bb-9a16-f526ebae9552",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2HjrExMg6QywwpjTz1Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "171e47c5-bef0-44fc-b904-4f4e6e7a1f65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7fyU5embYYrnLiZGdVJiY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7456,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7456,
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

_source line 4 · 2026-05-14T10:17:44.647Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PuudqtmuTBGUjedgWXjDjK`</summary>

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
  "parentUuid": "171e47c5-bef0-44fc-b904-4f4e6e7a1f65",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2HjrExMg6QywwpjTz1Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6053d23b-dfa9-46ee-b87f-37ea3840fc12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7fyU5embYYrnLiZGdVJiY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7456,
      "cache_read_input_tokens": 8250,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7456
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 112,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 7456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7456,
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

_source line 5 · 2026-05-14T10:17:44.655Z_

<details><summary>↩ Tool result · `toolu_01PuudqtmuTBGUjedgWXjDjK`</summary>

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
  "parentUuid": "6053d23b-dfa9-46ee-b87f-37ea3840fc12",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a967392e829aaef63",
  "type": "user",
  "uuid": "0d330767-02e8-410e-8dce-6a91983a7952",
  "sourceToolAssistantUUID": "6053d23b-dfa9-46ee-b87f-37ea3840fc12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T10:17:47.677Z_



Let me read the full paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d330767-02e8-410e-8dce-6a91983a7952",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2Hk96icXPQvFdTnr2kW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "221ae2a8-84c3-4cec-8ab0-ddc82caa42f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CkvJcjnE6CpffaGQuy1gAY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 15706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1294,
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

_source line 7 · 2026-05-14T10:17:48.088Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013NToSYgpbUMKyv4QRjfJeB`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "221ae2a8-84c3-4cec-8ab0-ddc82caa42f2",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2Hk96icXPQvFdTnr2kW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e54d37af-3da4-4047-962b-22313e12aac4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CkvJcjnE6CpffaGQuy1gAY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 15706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1294,
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

_source line 8 · 2026-05-14T10:17:48.100Z_

<details><summary>↩ Tool result · `toolu_013NToSYgpbUMKyv4QRjfJeB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| plan006-prolog-sta-s42 | Prolog exec+STA GRPO seed=42: ISR reward 在 Prolog logic type 上的效果。与 plan006-prolog-exec-s42 (exec-only) 对照，验证 STA/ISR 的 hacking 检测和 Goodhart 效应是否跨 logic type 泛化。 | — | — | — |\\n| plan006-prolog-exec-s42 | Prolog exec-only GRPO seed=42: STA/ISR hacking patterns generalize across logic types? Prolog uses rule ablation (vs FOL axiom ablation). If same degeneration modes appear → STA is logic-agnostic diagnostic. | — | — | — |\\n\\n## 待处理\\n- plan018-additive-random-b01-s43: Random β=0.1 seed=43 控制组：与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s43 下是否成立。（排队等待 GPU）\\n- plan018-additive-random-b01-s44: Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。（排队等待 GPU）\\n- plan006-prolog-sta-s44: Prolog exec+STA GRPO seed=44: 第三 seed。3-seed mean±std 用于论文 Claim 3 跨 logic type 统计支撑。（准备中）\\n- plan006-prolog-sta-s43: Prolog exec+STA GRPO seed=43: 跨 seed 稳定性检查。与 exec-only s43 对照。（准备中）\\n- plan006-prolog-exec-s44: Prolog exec-only GRPO seed=44: third seed for Prolog. Together with s42/s43, provides 3-seed evidence for cross-logic generalization claim.（准备中）\\n- plan006-prolog-exec-s43: Prolog exec-only GRPO seed=43: cross-seed stability check for Prolog logic type. FOL showed extreme cross-seed variance (s42 genuine vs s43 degenerate vs s44 tautological).（准备中）\\n\\n## 近期结论\\n- **plan002-additive-b01-s43** (negative): ISR β=0.1 seed=43 多 seed 验证：plan002-b01-s42 (PR=0.81, ISR=0.337) 在 s43 下是否可复现？exec-only s43 是 degraded seed (PR=14%)，ISR β=0.1 能否拯救 bad seed？3-seed mean±std 用于论文 Claim 2 统计支撑。 ← 基于 plan002-additive-b01-s42\\n  [plan002-b01-s43-eval-results](/api/workspace-files/projects/solver-trace-ablation/artifacts/plan002-additive-b01-s43/data/plan002-b01-s43-eval-pointer.txt)\\n- **plan002-additive-b01-s44** (negative): ISR β=0.1 seed=44 多 seed 验证：exec-only s44 是 tautological collapse (PR=98%, ISR=0.57 fake)，ISR β=0.1 能否防止 tautological collapse？3-seed mean±std 用于论文 Claim 2。 ← 基于 plan002-additive-b01-s42\\n- **plan012-hacking-taxonomy** (success): ISR β=0.1 vs Random β=0.1 hacking taxonomy 对比：ISR reward 能否减少 hacking 模式比例、增加 genuine proof 比例？5 种 hacking 分类（conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, premise padding）。\\n\\n## 趋势\\n成功 9 / 负向 12 / 失败 14 / 共 35\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-39279: 无 GPU 信息\\n\\n## 告警\\n- sta-phase1-exec-only: 训练失败 — unknown\\n- sta-phase1-exec-sta: 训练失败 — unknown\\n- sta-phase1-exec-only-r2: 训练失败 — unknown\\n- sta-phase1-exec-sta-r2: 训练失败 — unknown\\n- sta-phase1-exec-only-r3: 训练失败 — unknown\\n- sta-phase1-exec-sta-r3: 训练失败 — unknown\\n- plan001-exec-only-s42: 训练失败 — unknown\\n- plan001-exec-only-s42-r3: 训练失败 — unknown\\n- plan001-exec-only-s43: 训练失败 — unknown\\n- plan013-random-reward-s42: 训练失败 — unknown\\n- plan013-random-reward-s42-r2: 训练失败 — unknown\\n- plan001-exec-only-s43-r2: 训练失败 — unknown\\n- plan013-random-reward-s42-r3: 训练失败 — unknown\\n- plan001-exec-only-s43-r3: 训练失败 — unknown\\n\", \"total_chars\": 3095, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e54d37af-3da4-4047-962b-22313e12aac4",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a967392e829aaef63",
  "type": "user",
  "uuid": "dcacd705-05ac-49d8-88c4-d8adde8878cd",
  "sourceToolAssistantUUID": "e54d37af-3da4-4047-962b-22313e12aac4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T10:17:49.069Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01EmWq7uWzwBp8RimJWdEgp3`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcacd705-05ac-49d8-88c4-d8adde8878cd",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2Hk96icXPQvFdTnr2kW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9623f0cd-2a35-44b9-ad66-f26bbf626d84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CkvJcjnE6CpffaGQuy1gAY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 15706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1294,
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

_source line 10 · 2026-05-14T10:17:49.079Z_

<details><summary>↩ Tool result · `toolu_01EmWq7uWzwBp8RimJWdEgp3`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'solver-trace-ablation'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9623f0cd-2a35-44b9-ad66-f26bbf626d84",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a967392e829aaef63",
  "type": "user",
  "uuid": "f5eee879-be37-4908-9fc9-c3d1ac40431b",
  "sourceToolAssistantUUID": "9623f0cd-2a35-44b9-ad66-f26bbf626d84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T10:17:49.705Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JA7U7BtRvHHjMuJ1ufz3jP`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5eee879-be37-4908-9fc9-c3d1ac40431b",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2Hk96icXPQvFdTnr2kW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7cbba1b5-4d56-453f-b93a-644048807124",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CkvJcjnE6CpffaGQuy1gAY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 15706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1294,
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

_source line 12 · 2026-05-14T10:17:49.720Z_

<details><summary>↩ Tool result · `toolu_01JA7U7BtRvHHjMuJ1ufz3jP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ROADMAP.md\", \"content\": \"# solver-trace-ablation — Research Dashboard\\n\\n> 最后更新: 2026-05-14 09:06 UTC | 更新原因: D038 taxonomy 结果纳入 + 刷新 RUNNING 状态（plan016 已完成、s43/s44 在跑）\\n\\n## 核心方向\\nSTA/ISR 作为 GRPO neurosymbolic formalizer 的**诊断工具** + **Goodhart's Law 案例研究**——检测 reward hacking、量化结构退化、分类退化模式，并展示 ISR 从诊断指标到优化目标的 Goodhart 转折。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research + 审稿进行中 | **DDL**: 2026-05-25（剩 11 天）\\n- **实验**: 39 个 (RUNNING 2, PREPARING 5, DONE 32) | success 8\\n- **GPU**: 2 × RTX PRO 6000 96GB — ✅ 两卡满载\\n\\n### 核心证据链\\n- ✅ ISR 崩塌轨迹：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- ✅ 3-seed exec-only：s42 conclusion embedding | s43 degraded | s44 tautological collapse\\n- ✅ Goodhart β 剂量效应：β=0.1 sweet spot (ISR 3.2x > random) vs β=0.3 collapse (ISR < random)\\n- ✅ Hacking taxonomy 定量对比 (D038)：ISR β=0.1 genuine 25.9% vs random 17.7% (+8.2pp)，conclusion embedding 73-79%\\n- ✅ plan016 1000步：PR=0.96, ISR=0.003，崩塌持续恶化\\n- ✅ plan014 downstream NLI: ISR-NLI ρ=-0.049 n.s.，ISR 能力边界已刻画\\n- ✅ Table 1 修复 + 文献修正完成\\n- ⏳ plan002-b01-s43/s44: RUNNING — β=0.1 多 seed 验证\\n- 🔜 plan018-random-s43/s44: PREPARING — matched random 多 seed 控制\\n- 🔜 plan006-prolog ×3: PREPARING — Claim 3 跨 logic type 验证\\n\\n## RUNNING\\n| 实验 | GPU | 说明 |\\n|------|-----|------|\\n| plan002-additive-b01-s43 | cuda:0 | ISR β=0.1 seed=43 |\\n| plan002-additive-b01-s44 | cuda:1 | ISR β=0.1 seed=44 |\\n\\n## 近期任务\\n- [ ] s43/s44 完成 → eval_sta.py + taxonomy + 3-seed mean±std\\n- [ ] plan018-random-s43/s44 启动（GPU 空闲后）\\n- [ ] plan006 Prolog 代码/数据 readiness 确认\\n- [ ] 3-seed 全部出齐 → Table 1 + Table 2 定稿\\n- [ ] plan006 结果 → 论文写作启动评估\\n\\n## GPU 预算\\n- 本地: 2 × RTX PRO 6000 96GB，两卡满载\\n- 已消耗: ~35+ GPU·h\\n- 剩余需求: ~12h（s43/s44 ~2h + random s43/s44 ~2h + plan006 ×3 ~6h + eval ~2h）\\n- DDL 11 天 × 2 卡 × 24h = 528 GPU·h，时间充裕\\n\\n## 写作约束\\n- plan013 vs plan017 公式结构不同，不可简化为\\\"additive vs convex\\\"对照 (D027)\\n- ISR β=0.1 hacking rate 仍达 74%——论文不可标\\\"no hacking\\\"，应标\\\"lowest hacking rate\\\" (D038)\\n- β=0.1 3-seed 出齐前论文统计用 s42 单 seed，标注 preliminary\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D043 | 2026-05-14 | ISR β=0.1 \\\"sweet spot\\\"叙事降级：2/3 seeds ISR 膨胀为 artif | plan002-additive-b01-s42, plan002-additive-b01-s43, plan002-additive-b01-s44, plan018-additive-random-b01-s42 |\\n| D042 | 2026-05-14 | ISR 度量存在结构性盲点：premise≈conclusion 时 conclusion sub- | plan002-additive-b01-s43, plan002-additive-b01-s44, plan002-additive-b01-s42 |\\n| D041 | 2026-05-14 | Claim 2 framing pivot: ISR β=0.1 \\\"sweet spot\\\" → \\\"a | plan002-additive-b01-s42, plan002-additive-b01-s43, plan002-additive-b01-s44 |\\n| D040 | 2026-05-14 | plan002-b01-s44 reclassified: \\\"success\\\" → \\\"new hac | plan002-additive-b01-s44, plan002-additive-b01-s42 |\\n| D039 | 2026-05-14 | plan002-b01-s44 重分类：从 success 改为 semantic drift ha | plan002-additive-b01-s44 |\\n| D038 | 2026-05-14 | Hacking taxonomy 结果足够，跳过 LLM-as-judge；taxonomy 对比覆 | plan012, plan002-additive-b01-s42, plan018-additive-random-b01-s42 |\\n| D037 | 2026-05-14 | ISR β=0.1 质量验证路径：先 hacking taxonomy 对比，必要时加 LLM-as | plan002-additive-b01-s42, plan018-additive-random-b01-s42, plan012 |\\n| D036 | 2026-05-14 | 为 beta=0.1 补跑多 seed (s43/s44) 验证 ISR vs random 的稳健 | plan002-additive-b01-s42, plan018-additive-random-b01-s42, plan001-exec-only-s43 |\\n| D035 | 2026-05-14 | Framing 选 C: Goodhart 主线 — ISR 展示经典 Goodhart 效应（β= | plan002-b01, plan018, plan002-b03, plan017 |\\n| D034 | 2026-05-14 | Framing 选 C+A 混合：Goodhart 为主线叙事，ISR 诊断保留为 Claim 1， | plan002-b01, plan018, plan002-b03, plan017 |\\n\\n\", \"total_chars\": 3396, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cbba1b5-4d56-453f-b93a-644048807124",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a967392e829aaef63",
  "type": "user",
  "uuid": "7d594bb3-1ab4-425e-b7ce-34de51c19c58",
  "sourceToolAssistantUUID": "7cbba1b5-4d56-453f-b93a-644048807124",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T10:17:50.024Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SagdL5whVAnxVqUkFksPTM`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d594bb3-1ab4-425e-b7ce-34de51c19c58",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2Hk96icXPQvFdTnr2kW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42c0844d-ffd5-4ddf-9564-d79629d5fbc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CkvJcjnE6CpffaGQuy1gAY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 15706,
      "output_tokens": 400,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1294
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 400,
          "cache_read_input_tokens": 15706,
          "cache_creation_input_tokens": 1294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1294,
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

_source line 14 · 2026-05-14T10:17:50.035Z_

<details><summary>↩ Tool result · `toolu_01SagdL5whVAnxVqUkFksPTM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\\n#   8. verification-reward: Solver/prover as RL reward signal\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\n      used in STA training. GRPO eliminates the critic model by estimating\\n      baselines from group scores.\\n    key_finding: >\\n      GRPO matches PPO performance while significantly reducing training\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\n\\n  - id: logic-rl\\n    title: \\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\"\\n    authors: \\\"Xian et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.14768\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\n      rewards rather than STA's intensional structural rewards.\\n    key_finding: >\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\n      rule-based reward design is critical for RL-based logical reasoning.\\n\\n  - id: mellgren-prolog-grpo\\n    title: \\\"Training Language Models to Use Prolog as a Tool\\\"\\n    authors: \\\"Niklas Mellgren\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2512.07407\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\n    key_finding: >\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\n      for logical and mathematical reasoning.\\n\\n  - id: satlm\\n    title: \\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\"\\n    authors: \\\"Xi Ye et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Neurosymbolic approach where LLM generates declarative specifications\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\n      but uses prompting, not RL training.\\n    key_finding: >\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\n\\n  # ============================================================\\n  # Category 2: Reward shaping for code/formal verification\\n  # ============================================================\\n\\n  - id: lightman-verify-step\\n    title: \\\"Let's Verify Step by Step\\\"\\n    authors: \\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2305.20050 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: method-component\\n    relevance: >\\n      Establishes that process supervision (step-level reward) outperforms\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\n      is analogous: it provides structural process-level signal about which\\n      components of a formalization matter, rather than just pass/fail.\\n    key_finding: >\\n      Process-supervised reward model achieves 78% on MATH, significantly\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\n\\n  - id: reward-shaping-rlhf\\n    title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: \\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.18770\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\n      rapid-then-convergent growth. STA's ISR follows these principles\\n      naturally since structural necessity scores are bounded [0,1].\\n    key_finding: >\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\n      initial growth with gradual convergence. PAR method achieves 5%+\\n      win rate improvement on AlpacaEval 2.0.\\n\\n  - id: rlvr-reasoning\\n    title: \\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.14245\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\n      is insufficient and structural reward is needed to avoid reward hacking.\\n    key_finding: >\\n      RLVR with binary verification implicitly teaches correct reasoning\\n      strategies, not just answer matching.\\n\\n  - id: rubric-grpo\\n    title: \\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2605.08061\\\"\\n    category: reward-shaping\\n    role: direct-competitor\\n    relevance: >\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\n      judges, while ISR comes from solver-based mutation testing.\\n    key_finding: >\\n      Structured multi-dimensional reward signals improve GRPO training\\n      generalization compared to scalar rewards.\\n\\n  - id: gao-effective-rl-reward\\n    title: \\\"On Designing Effective RL Reward at Training Time for LLM Reasoning\\\"\\n    authors: \\\"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2410.15115\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Demonstrates that learned process/outcome reward models can hurt RL\\n      training, producing worse performance than simple success reward only.\\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\\n      reward degrades prove_rate compared to exec-only baseline.\\n    key_finding: >\\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\\n      reward. Solution: Clipping and Delta techniques to bound accumulated\\n      reward magnitude prevent reward hacking.\\n\\n  - id: prof-process-outcome\\n    title: \\\"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\\\"\\n    authors: \\\"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.03403\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that naively combining PRM+ORM signals leads to performance\\n      degradation. PROF consistency filter retains only PRM-ORM consistent\\n      samples, achieving 4%+ improvement over blending. Suggests STA should\\n      only apply ISR when consistent with execution outcome.\\n    key_finding: >\\n      Process rewards frequently suffer from inaccuracies and reward hacking\\n      susceptibility. PROF filters training data by PRM-ORM consistency,\\n      outperforming naive reward blending by 4%+ accuracy.\\n\\n  - id: moskovitz-constrained-rlhf\\n    title: \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\"\\n    authors: \\\"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2310.04373 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      First study on overoptimization in composite reward models. Shows that\\n      fixed-weight linear scalarization of component rewards leads to\\n      degradation past a threshold. Proposes constrained RL with dynamic\\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\\n    key_finding: >\\n      Correlation between component RMs significantly affects overoptimization\\n      thresholds. Constrained RL with Lagrange multipliers outperforms\\n      fixed-weight reward composition.\\n\\n  - id: skalse-reward-hacking\\n    title: \\\"Defining and Characterizing Reward Hacking\\\"\\n    authors: \\\"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\\\"\\n    year: 2022\\n    venue: \\\"arXiv 2209.13085 / NeurIPS 2022\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Formal proof that for stochastic policies, two reward functions are\\n      unhackable only if one is constant. Theoretically explains why any\\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\\n      property of reward composition, not STA-specific.\\n    key_finding: >\\n      Any non-constant proxy reward can decrease true reward when optimized.\\n      Unhackability requires the proxy to be constant, making all non-trivial\\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\\n\\n  - id: progrs-outcome-conditioned\\n    title: \\\"LLM Reasoning with Process Rewards for Outcome-Guided Steps\\\"\\n    authors: \\\"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2604.02341\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\\n      to zero mean, preserving ranking info without corrupting gradients.\\n      Suggests STA should condition ISR on execution outcome.\\n    key_finding: >\\n      Naive process rewards induce reward hacking by rewarding locally fluent\\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\\n      the conflict with fewer rollouts than outcome-only baselines.\\n\\n  - id: qwen-prm-lessons\\n    title: \\\"The Lessons of Developing Process Reward Models in Mathematical Reasoning\\\"\\n    authors: \\\"Zhenru Zhang et al. (Qwen Team, Alibaba)\\\"\\n    year: 2025\\n    venue: \\\"ACL 2025 Findings (arXiv 2501.07301)\\\"\\n    category: reward-shaping\\n    role: supporting-evidence\\n    relevance: >\\n      MC estimation-synthesized PRM data leads to quality degradation; policy\\n      model generates \\\"answer-correct but reasoning-flawed\\\" responses, causing\\n      process reward / outcome misalignment. Directly parallels ISR problem:\\n      structurally correct but semantically wrong proof traces get high ISR\\n      but low execution reward.\\n    key_finding: >\\n      PRM performance depends critically on data quality; MC estimation\\n      introduces systematic bias. Answer-correct reasoning-flawed samples\\n      corrupt process supervision signal.\\n\\n  # ============================================================\\n  # Category 3: Mutation testing in software engineering\\n  # ============================================================\\n\\n  - id: demillo1978\\n    title: \\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\"\\n    authors: \\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\"\\n    year: 1978\\n    venue: \\\"Computer 11(4):34-43\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Foundational paper introducing mutation testing. STA's component\\n      necessity testing directly extends this idea: instead of mutating\\n      source code to test test suites, STA mutates logical formulas\\n      to test component necessity for solver success.\\n    key_finding: >\\n      Introduced mutation testing and the coupling effect hypothesis:\\n      tests that detect simple faults also detect complex faults.\\n\\n  - id: offutt-coupling\\n    title: \\\"Investigations of the Software Testing Coupling Effect\\\"\\n    authors: \\\"A. Jefferson Offutt\\\"\\n    year: 1992\\n    venue: \\\"ACM TOSEM 1(1):5-20\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Empirically validates the coupling effect hypothesis that underpins\\n      mutation testing. STA's single-component ablation is analogous to\\n      first-order mutation; the coupling effect suggests this suffices.\\n    key_finding: >\\n      Test data killing all first-order mutants killed >99% of second-\\n      and third-order mutants, validating the coupling effect.\\n\\n  - id: jia-harman-survey\\n    title: \\\"An Analysis and Survey of the Development of Mutation Testing\\\"\\n    authors: \\\"Yue Jia, Mark Harman\\\"\\n    year: 2011\\n    venue: \\\"IEEE TSE 37(5):649-678\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Comprehensive survey of mutation testing covering three decades of\\n      development. Provides theoretical and practical foundation for STA's\\n      adaptation of mutation testing to logical formulas.\\n    key_finding: >\\n      Systematic classification of mutation operators, cost reduction\\n      techniques, and equivalence problem -- all relevant to STA's design\\n      of clause-level ablation operators.\\n\\n  - id: just-mutants-real-faults\\n    title: \\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\"\\n    authors: \\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\"\\n    year: 2014\\n    venue: \\\"FSE 2014\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Validates that mutation testing (structural/intensional analysis of\\n      program adequacy) correlates with real fault detection. Supports STA's\\n      premise that structural analysis of formalization components provides\\n      meaningful signal about formalization quality.\\n    key_finding: >\\n      Mutant detection is statistically correlated with real fault detection,\\n      and mutation score is a better predictor of test effectiveness than\\n      code coverage.\\n\\n  - id: llmorpheus\\n    title: \\\"LLMorpheus: Mutation Testing Using Large Language Models\\\"\\n    authors: \\\"Frank Tip, Jon Bell, et al.\\\"\\n    year: 2025\\n    venue: \\\"IEEE TSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses LLMs to generate realistic code mutants beyond traditional\\n      mutation operators. Shows mutation testing evolving toward\\n      ML-integrated approaches, validating STA's cross-pollination\\n      of mutation testing ideas into ML training.\\n    key_finding: >\\n      LLM-generated mutants simulate real bugs that rule-based operators\\n      cannot produce, improving mutation testing realism.\\n\\n  - id: mutation-guided-meta\\n    title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n    authors: \\\"Christopher Foster et al.\\\"\\n    year: 2025\\n    venue: \\\"FSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Industrial application of mutation-guided LLM test generation at\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\n      in production -- analogous to how STA uses mutation (ablation) to\\n      guide GRPO reward signal.\\n    key_finding: >\\n      Mutation-guided approach generates tests that kill significantly\\n      more mutants than unguided LLM test generation at Meta scale.\\n\\n  - id: mutation-consistency-llm\\n    title: \\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2401.05940\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses code mutations to evaluate LLM code understanding consistency.\\n      Conceptually related to STA: both use systematic code/formula\\n      mutations to assess model capabilities.\\n    key_finding: >\\n      LLMs show significant inconsistency when evaluated on mutated code\\n      variants, suggesting superficial pattern matching.\\n\\n  # ============================================================\\n  # Category 4: Intensional program analysis\\n  # ============================================================\\n\\n  - id: deepmutation\\n    title: \\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\"\\n    authors: \\\"Various\\\"\\n    year: 2023\\n    venue: \\\"Information and Software Technology 2023\\\"\\n    category: intensional-analysis\\n    role: background\\n    relevance: >\\n      Extends mutation testing to DNN testing with probabilistic mutation\\n      operators. Parallel to STA's extension of mutation testing from\\n      traditional programs to logical formulas.\\n    key_finding: >\\n      Probabilistic mutation framework enables meaningful test adequacy\\n      assessment for neural networks through structural perturbation.\\n\\n  # ============================================================\\n  # Category 5: Reward hacking / overoptimization\\n  # ============================================================\\n\\n  - id: inform-reward-hacking\\n    title: \\\"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Proposes information-bottleneck approach to detect and mitigate reward\\n      hacking. STA's ISR addresses the same problem differently: by grounding\\n      reward in verifiable structural properties (component necessity), it\\n      reduces the attack surface for reward hacking.\\n    key_finding: >\\n      Variational information bottleneck filters irrelevant features from\\n      reward model; Cluster Separation Index detects reward overoptimization.\\n\\n  - id: mo-grpo\\n    title: \\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\"\\n    authors: \\\"CyberAgent AI Lab\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.22047\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Directly addresses GRPO reward hacking in multi-objective settings.\\n      STA's ISR can be viewed as adding a structural objective to the\\n      correctness objective, making MO-GRPO's insights directly applicable.\\n    key_finding: >\\n      Standard GRPO normalizes after summing rewards, allowing high-variance\\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\\n\\n  - id: reward-hacking-survey\\n    title: \\\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\\\"\\n    authors: \\\"Various\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2604.13602\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\\n      Provides theoretical framework for understanding why STA's structural\\n      reward is more robust than pure outcome-based reward.\\n    key_finding: >\\n      Reward hacking manifests through specification gaming, reward model\\n      exploitation, and emergent misalignment; structural verification\\n      rewards are more robust than learned reward models.\\n\\n  - id: energy-loss-reward-hacking\\n    title: \\\"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Identifies energy loss in LLM final layer as an indicator of reward\\n      hacking during RL. Provides complementary diagnostic to STA's\\n      structural reward approach.\\n    key_finding: >\\n      Energy loss in the final layer increases during RL and excessive\\n      increase characterizes reward hacking; EPPO algorithm penalizes\\n      this to mitigate hacking.\\n\\n  - id: spurious-rewards\\n    title: \\\"Spurious Rewards: Rethinking Training Signals in RLVR\\\"\\n    authors: \\\"Ruixin Yang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.10947 / NeurIPS 2025 submission\\\"\\n    category: reward-hacking\\n    role: direct-evidence\\n    relevance: >\\n      Most directly relevant to STA findings. GRPO+random reward on\\n      Qwen2.5-Math improves 21.4%, nearly matching ground-truth reward's\\n      29.1%. Matches our plan017 finding: additive random (PR=48%) >\\n      additive ISR (PR=18%). Structured metrics can be worse than random\\n      noise due to systematic bias vs pure variance.\\n    key_finding: >\\n      Random reward nearly matches ground-truth reward in GRPO training,\\n      suggesting GRPO's group normalization extracts signal from noise.\\n      Effect is model-dependent (works on Qwen2.5, not Llama3).\\n\\n  - id: gao-reward-overoptimization\\n    title: \\\"Scaling Laws for Reward Model Overoptimization\\\"\\n    authors: \\\"Leo Gao, John Schulman, Jacob Hilton\\\"\\n    year: 2023\\n    venue: \\\"ICML 2023 (arXiv 2210.10760)\\\"\\n    category: reward-hacking\\n    role: theoretical-foundation\\n    relevance: >\\n      Foundational work quantifying Goodhart's effect: proxy reward rises\\n      but gold reward first rises then falls. ISR is a proxy reward that\\n      exhibits exactly this pattern — ISR can increase while prove_rate\\n      decreases, making it suitable for post-hoc diagnosis but harmful\\n      as training signal.\\n    key_finding: >\\n      Gold/proxy reward divergence follows predictable scaling laws.\\n      Proxy reward optimization past critical point degrades gold reward,\\n      with the divergence point scaling with model and dataset size.\\n\\n  - id: karwowski-goodhart-rl\\n    title: \\\"Goodhart's Law in Reinforcement Learning\\\"\\n    authors: \\\"Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2024 (arXiv 2310.09144)\\\"\\n    category: reward-hacking\\n    role: theoretical-foundation\\n    relevance: >\\n      Geometric interpretation of Goodhart's Law in MDPs: optimizing\\n      imperfect proxy past critical point decreases true objective. ISR as\\n      proxy has partial correlation with execution correctness — exceeding\\n      critical optimization point pushes policy toward high-ISR but\\n      low-correctness regions. Explains plan002/plan005 negative results.\\n    key_finding: >\\n      Formalizes Goodhart's Law for RL: any non-trivially correlated proxy\\n      reward creates regions where proxy and true reward diverge, and\\n      policy optimization inevitably enters these regions.\\n\\n  # ============================================================\\n  # Category 6: FOL/Prolog formalization with LLMs\\n  # ============================================================\\n\\n  - id: folio\\n    title: \\\"FOLIO: Natural Language Reasoning with First-Order Logic\\\"\\n    authors: \\\"Simeng Han et al.\\\"\\n    year: 2022\\n    venue: \\\"arXiv 2209.00840 / EMNLP 2024\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\\n      formalization as the target task for GRPO training. FOLIO's\\n      expert-annotated FOL annotations serve as reference formalizations.\\n    key_finding: >\\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\\n      GPT-4 still struggles on the hardest examples.\\n\\n  - id: proofwriter\\n    title: \\\"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\\\"\\n    authors: \\\"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\\\"\\n    year: 2021\\n    venue: \\\"Findings of ACL-IJCNLP 2021\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Source dataset for STA's training data. ProofWriter provides\\n      rule-based logical reasoning problems in natural language that\\n      STA uses for training formalizer models.\\n    key_finding: >\\n      Generative model can reliably produce implications and proofs;\\n      accuracy exceeds prior methods by 9% and generalizes to unseen\\n      proof depths.\\n\\n  - id: logic-lm\\n    title: \\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\"\\n    authors: \\\"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\\\"\\n    year: 2023\\n    venue: \\\"Findings of EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->symbolic solver pipeline for logical reasoning, directly\\n      comparable to STA's formalizer->Prolog solver pipeline. Key\\n      difference: Logic-LM uses prompting, STA uses GRPO training.\\n    key_finding: >\\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\\n      reasoning benchmarks including ProofWriter and FOLIO.\\n\\n  - id: linc\\n    title: \\\"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\\\"\\n    authors: \\\"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\\\"\\n    year: 2023\\n    venue: \\\"EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\\n      prover. Directly comparable to STA's NL->Prolog translation.\\n      LINC uses prompting-based approach; STA uses RL training.\\n    key_finding: >\\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\\n      CoT by 38% and 10% respectively on ProofWriter.\\n\\n  - id: fover-pei2025\\n    title: \\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\"\\n    authors: \\\"Yu Pei, Yongping Du, Xingnan Jin\\\"\\n    year: 2025\\n    venue: \\\"TACL 13:1340-1359\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\\n      Similar to STA's verification pipeline but focuses on post-hoc\\n      verification rather than training reward signal.\\n    key_finding: >\\n      FOL verification via Z3 significantly outperforms existing methods\\n      on ProofWriter and FOLIO benchmarks.\\n\\n  - id: lorp\\n    title: \\\"LoRP: LLM-based Logical Reasoning via Prolog\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"Knowledge-Based Systems 2025\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\\n      Closest to STA's formalization target (Prolog), though LoRP\\n      uses prompting while STA uses GRPO training with structural reward.\\n    key_finding: >\\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\\n\\n  - id: nl2fol\\n    title: \\\"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\\\"\\n    authors: \\\"Lalwani, Kim, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2405.02318\\\"\\n    category: fol-formalization\\n    role: background\\n    relevance: >\\n      Step-by-step NL->FOL translation using LLMs with SMT solver\\n      verification. Demonstrates the NL->formal logic pipeline that\\n      STA aims to improve via RL training.\\n    key_finding: >\\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\\n      generalizes to LogicClimate (80% F1), outperforming supervised\\n      models by 21%.\\n\\n  - id: logica2\\n    title: \\\"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"IEEE/ACM TASLP 2023\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Logical reasoning evaluation benchmark derived from Chinese civil\\n      service exams. Provides supplementary evaluation for STA's\\n      formalization capabilities.\\n    key_finding: >\\n      8,678 multiple-choice questions covering categorical, disjunctive,\\n      and conditional reasoning; widely used LLM benchmark.\\n\\n  # ============================================================\\n  # Category 7: Goodhart's Law theory and dose-response dynamics\\n  # ============================================================\\n\\n  - id: manheim-goodhart-taxonomy\\n    title: \\\"Categorizing Variants of Goodhart's Law\\\"\\n    authors: \\\"David Manheim, Scott Garrabrant\\\"\\n    year: 2019\\n    venue: \\\"arXiv 1803.04585\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      Four-part Goodhart taxonomy: regressional, extremal, causal, adversarial.\\n      STA's high-β ISR collapse is best classified as extremal Goodhart\\n      (policy moves to OOD region where ISR↑ but prove_rate↓). Provides\\n      vocabulary for discussion section.\\n    key_finding: >\\n      First systematic categorization of Goodhart failure modes. Extremal\\n      variant occurs when proxy-goal relationship breaks in out-of-distribution\\n      regions reached by strong optimization.\\n\\n  - id: pan-reward-misspecification\\n    title: \\\"The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models\\\"\\n    authors: \\\"Alexander Pan, Kush Bhatia, Jacob Steinhardt\\\"\\n    year: 2022\\n    venue: \\\"ICLR 2022\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      Across 9 environments, more capable agents exploit misspecifications more.\\n      Observes dose-dependent degradation — capability thresholds where true\\n      reward sharply drops. Matches STA's β=0.1→0.3 qualitative shift.\\n    key_finding: >\\n      Reward misspecification causes dose-dependent degradation where true reward\\n      sharply drops past capability thresholds. More capable optimization\\n      produces worse outcomes under misspecification.\\n\\n  - id: kwa-catastrophic-goodhart\\n    title: \\\"Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification\\\"\\n    authors: \\\"Tat-Thang Kwa, Rachel Thomas, Adrià Garriga-Alonso\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      If reward model error is heavy-tailed, policies achieve arbitrarily\\n      high proxy reward with no true utility gain. KL regularization provably\\n      fails. Explains why KL penalty in GRPO cannot prevent ISR collapse\\n      at high β if ISR error distribution is heavy-tailed.\\n    key_finding: >\\n      KL-regularized RL provably fails to prevent overoptimization under\\n      heavy-tailed reward misspecification. Policies can achieve arbitrarily\\n      high proxy reward with zero true utility.\\n\\n  - id: rafailov-daa-scaling\\n    title: \\\"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms\\\"\\n    authors: \\\"Rafael Rafailov, Yaswanth Chittepu, Ryan Park, Harshit Sikchi, Joey Hejna, W. Bradley Knox, Chelsea Finn, Scott Niekum\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: goodhart-overoptimization\\n    role: supporting-evidence\\n    relevance: >\\n      Extends Gao et al. to DPO/IPO/SLiC. Tests seven β values across\\n      1B-6.9B models. DAAs still overoptimize despite no explicit proxy RM.\\n      Validates β as a \\\"dose\\\" parameter — directly analogous to STA's\\n      ISR weight sweep.\\n    key_finding: >\\n      Direct alignment algorithms exhibit overoptimization following\\n      predictable scaling laws. Smaller models overoptimize sooner.\\n      β-controlled dose-response is a general phenomenon across RL paradigms.\\n\\n  - id: huang-chi-squared\\n    title: \\\"Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction\\\"\\n    authors: \\\"Afra Feyza Akyürek, Banghua Zhu, Sham Kakade, Jiantao Jiao\\\"\\n    year: 2025\\n    venue: \\\"ICLR 2025 Poster\\\"\\n    category: goodhart-overoptimization\\n    role: supporting-evidence\\n    relevance: >\\n      KL-regularization is theoretically inadequate for preventing\\n      overoptimization. Chi-squared divergence provably alleviates it.\\n      Suggests that even with KL penalty in GRPO, STA's high-β collapse\\n      is theoretically expected.\\n    key_finding: >\\n      Chi-squared preference optimization provably mitigates overoptimization\\n      where KL-regularization fails. Alternative divergence measures offer\\n      stronger guarantees.\\n\\n  - id: coste-rm-ensembles\\n    title: \\\"Reward Model Ensembles Help Mitigate Overoptimization\\\"\\n    authors: \\\"Thomas Coste, Usman Anwar, Robert Kirk, David Krueger\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023 Workshop on Alignment\\\"\\n    category: goodhart-overoptimization\\n    role: background\\n    relevance: >\\n      Worst-case optimization across RM ensembles practically eliminates\\n      overoptimization for BoN and reduces it for PPO. Suggests ensemble\\n      of multiple solver metrics (instead of single ISR) as mitigation.\\n    key_finding: >\\n      RM ensembles with worst-case aggregation mitigate overoptimization.\\n      Ensemble size and diversity directly affect robustness.\\n\\n  # ============================================================\\n  # Category 8: Solver/prover as RL reward signal\\n  # ============================================================\\n\\n  - id: rlsf\\n    title: \\\"Reinforcement Learning via Symbolic Feedback\\\"\\n    authors: \\\"Abhinav Jha, Shikhar Murty, Zico Kolter, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2405.16661\\\"\\n    category: verification-reward\\n    role: direct-competitor\\n    relevance: >\\n      Most directly relevant: uses solver/prover certificates as fine-grained\\n      token-level reward signal. Outperforms traditional approaches on program\\n      synthesis (+31.4%). STA extends this paradigm and shows when it breaks\\n      (Goodhart effects at high auxiliary reward weight).\\n    key_finding: >\\n      Symbolic reasoning tools provide poly-sized certificates as reward.\\n      Smaller RLSF models outperform GPT-4 on structured generation tasks.\\n\\n  - id: fover-kamoi2026\\n    title: \\\"FoVer: Generalizable Process Reward Models via Formally Verified Training Data\\\"\\n    authors: \\\"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\\\"\\n    year: 2025\\n    venue: \\\"Findings of ACL 2026 (arXiv 2502.01345)\\\"\\n    category: verification-reward\\n    role: supporting-evidence\\n    relevance: >\\n      Uses Z3 and Isabelle to synthesize PRM training data by annotating\\n      step-level error labels without human annotation. Same solver family\\n      as STA. Shows verification-based rewards work; STA extends by showing\\n      dose-response dynamics.\\n    key_finding: >\\n      Formally verified training data enables generalizable process reward\\n      models competitive on ProcessBench and 12 reasoning benchmarks.\\n\\n  - id: deepseek-prover-v15\\n    title: \\\"DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search\\\"\\n    authors: \\\"DeepSeek AI\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2025 (arXiv 2408.08152)\\\"\\n    category: verification-reward\\n    role: method-component\\n    relevance: >\\n      Uses GRPO with Lean 4 verification as binary reward. Same algorithm\\n      (GRPO) + formal verification, but binary (pass/fail). Binary reward\\n      avoids the graded-metric Goodhart risk that STA identifies with ISR.\\n    key_finding: >\\n      GRPO + binary Lean verification achieves 63.5% on miniF2F. Binary\\n      correctness guarantee via formal verification sidesteps proxy reward\\n      overoptimization.\\n\\n  - id: alphaproof\\n    title: \\\"AlphaProof\\\"\\n    authors: \\\"Google DeepMind\\\"\\n    year: 2024\\n    venue: \\\"Nature 2025\\\"\\n    category: verification-reward\\n    role: background\\n    relevance: >\\n      AlphaZero-inspired RL with Lean proof verification at scale.\\n      Silver medal at IMO 2024. Binary verification reward avoids the\\n      Goodhart problem STA identifies with graded verification metrics.\\n    key_finding: >\\n      Binary formal verification as RL reward scales to IMO-level\\n      mathematical reasoning. Demonstrates verification-reward RL works\\n      at the frontier of mathematical difficulty.\\n\\n  - id: math-shepherd\\n    title: \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\"\\n    authors: \\\"Peiyi Wang, Lei Li, Zhihong Shao, R.X. Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"ACL 2024 (arXiv 2312.08935)\\\"\\n    category: verification-reward\\n    role: supporting-evidence\\n    relevance: >\\n      Automatically constructs process supervision data and uses it as\\n      step-by-step PPO reward. Automated verification reward without human\\n      labels, analogous to STA's automated ISR computation via solver.\\n    key_finding: >\\n      Automated process supervision improves Mistral-7B on GSM8K\\n      (77.9→84.1%) and MATH (28.6→33.0%) without human annotation.\\n\\n  # ============================================================\\n  # Additional reward-shaping papers (Goodhart survey additions)\\n  # ============================================================\\n\\n  - id: bipars\\n    title: \\\"Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping\\\"\\n    authors: \\\"Yujing Hu, Weixun Wang, Hangtian Jia, et al.\\\"\\n    year: 2020\\n    venue: \\\"NeurIPS 2020\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Bi-level optimization learns parameterized shaping reward weights.\\n      Can transform harmful shaping rewards into beneficial ones by learning\\n      negative weights. Directly addresses STA's problem: when ISR weight\\n      is wrong, automated weight learning could find optimal β.\\n    key_finding: >\\n      Bi-level optimization automatically learns auxiliary reward weights,\\n      outperforming fixed weights and recovering from harmful shaping rewards.\\n\\n  - id: dapo\\n    title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: \\\"Qiying Yu et al. (ByteDance)\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2503.14476\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Four techniques for stable multi-component reward in GRPO: Clip-Higher,\\n      Dynamic Sampling, token-level policy gradient, Overlong Reward Shaping.\\n      Addresses stability issues relevant to STA's multi-reward setup.\\n    key_finding: >\\n      Clip-Higher and Dynamic Sampling prevent entropy collapse in GRPO\\n      with multi-component rewards. Soft punishment for overlong outputs\\n      avoids reward hacking through length exploitation.\\n\", \"total_chars\": 38485, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42c0844d-ffd5-4ddf-9564-d79629d5fbc1",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a967392e829aaef63",
  "type": "user",
  "uuid": "4da46207-1811-47c3-a315-64578c930e3d",
  "sourceToolAssistantUUID": "42c0844d-ffd5-4ddf-9564-d79629d5fbc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T10:17:54.050Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PY5mFZm5M5eF42984yjrY4`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4da46207-1811-47c3-a315-64578c930e3d",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2HkXsgZhkAKAcYonEHm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2557986e-a4bf-4ca3-9929-6cb2c677ea09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAiRyujfzRpVE1RXK6ePpN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16805,
      "cache_read_input_tokens": 17000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16805,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 16 · 2026-05-14T10:17:54.061Z_

<details><summary>↩ Tool result · `toolu_01PY5mFZm5M5eF42984yjrY4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)\\n- Hacking taxonomy: 6 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation)\\n\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart (D033→D043 重写)\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型不仅在高剂量 Goodhart PR（β=0.3 PR 崩塌），还在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR）。ISR bonus 特异性地诱导 premise=conclusion hacking——random noise 在相同 β 下不触发此模式，证明这是 ISR-specific gaming 而非 GRPO 通用退化。\\n\\n**证据（β=0.1 三 seed + random 对照，D043 更新）**：\\n\\n| Seed | PR | proved_only ISR | single_premise% | premise=conclusion% | 诊断 |\\n|------|-----|-----------------|-----------------|---------------------|------|\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 18.5% | 16.0% | **genuine** (80% genuine, multi-premise 2-9) |\\n| s43 (ISR β=0.1) | 0.61 | 0.830 | 100% | 97% | **conclusion duplication artifact** |\\n| s44 (ISR β=0.1) | 0.89 | 0.902 | ~100% | 65%+ | **conclusion duplication artifact** |\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** | **0%** | redundant premises, zero duplication |\\n\\n- s42 genuine confirmed: 80% genuine samples, multi-premise proofs (2-9 premises), proved_only_ISR=0.415 < GT=0.559（注：0.337 是含 unproved 样本的 mean_isr）\\n- s43/s44: conclusion duplication — premise=conclusion 单前提证明，ISR 通过 conclusion sub-component ablation 膨胀到 0.83-0.90（远超 GT=0.559）。40/61 proved samples ISR=1.0 (s43)\\n- random β=0.1 对照: **零** conclusion duplication (0/79)，n_premises 3-15 — ISR-specific gaming 确认\\n- **结论**: ISR reward 在 β=0.1 有 genuine guidance 能力（s42），但同时诱导 ISR-specific gaming（s43/s44）。成功率 1/3，且 gaming 模式比 exec-only hacking 更隐蔽（PR 和 ISR 表面都高）。ISR 作为 reward component 的可靠性不足以推荐使用。\\n\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038)**：\\n- ISR β=0.1 genuine: 25.9% (21/81) vs random β=0.1 genuine: 17.7% (14/79) — **+8.2pp**\\n- Conclusion embedding: ISR 72.8% vs random 78.5% — 两组主导模式，ISR 略降但未消除\\n- Complexity-without-utility: ISR **0%** vs random 3.8% — ISR 完全消除此模式\\n- ISR genuine quality: mean ISR 0.67 (max 1.0) vs random genuine mean ISR 0.34 (max 0.5)\\n- 整体 hacking rate: ISR 74.1% vs random 82.3%\\n- ⚠️ 以上仅 s42；s43/s44 主要退化模式为 conclusion duplication（第 6 种 hacking mode，taxonomy 更新中）\\n\\n**证据（β=0.3 同剂量对照）**：\\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\\n\\n**β 剂量效应全景**：\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\n|---|---|---|---|---|---|\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 | s42 genuine; s43/s44 ISR-specific gaming (conclusion duplication) |\\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\\n\\n**其他 ISR-as-reward 失败模式**：\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\n\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为\\\"additive vs convex\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）\\n\\n⚠️ **β=0.1 三 seed 已出（D043）**：s42 genuine, s43/s44 conclusion duplication artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），需按 hacking mode 分层报告。\\n\\n### Claim 3: Cross-Logic Generality (conditional on plan006)\\nSTA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.\\n\\n**证据**: 待验证。plan006 Prolog GRPO dry-run 进行中，训练即将启动（3 seeds × 500 步）。如果 plan006 无法复现 hacking + ISR 诊断，此 claim 降级为 future work。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication that inflates ISR itself), while only 1/3 seeds show genuine improvement; at high dose (β=0.3), classic Goodhart collapse (PR 18% vs random 48%). The diagnostic metric becomes the target of gaming when used as optimization signal.\\n  3. GRPO saturation creates a \\\"training trap\\\": PR→1 means no gradient signal; adding variance redirects rather than prevents hacking\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (6 modes identified, including ISR-specific \\\"conclusion duplication with ISR inflation\\\")\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners\\n- **Actionable insights for practitioners**:\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflates ISR itself), β=0.3 collapses PR. Use ISR for post-hoc diagnosis only.\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\n- **Headline result**: \\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but exhibits meta-level Goodhart's Law when used as a training signal. At low dose (β=0.1), ISR reward induces a novel hacking mode in 2/3 seeds: models learn premise=conclusion strategies that simultaneously maximize execution reward and inflate ISR itself — the diagnostic metric becomes the gaming target. At high dose (β=0.3), classic Goodhart collapse occurs (PR 18% vs random 48%). Across 6 reward conditions, 3 seeds, and up to 1000 training steps, we identify 6 distinct hacking strategies including ISR-specific 'conclusion duplication with ISR inflation,' and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\"\\n\\n## ISR Capability Boundary (D021/D022)\\n\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\n\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\n- Best-of-N ISR selection vs random: +0.9pp (不显著)\\n- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%\\n\\n**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。\\n\\n## ISR-as-Reward: Goodhart Landscape (D033 更新)\\n\\nISR 作为训练信号的全部结果，按 β 剂量组织：\\n\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\n|------|------|---------|----------|----------|---------------|\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | conclusion embedding | N/A |\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | genuine 80%, conclusion embedding 16% | genuine (1/3 seeds) |\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **conclusion duplication 97%**, ISR inflation | **meta-Goodhart** (2/3 seeds) |\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **conclusion duplication 65%+**, ISR inflation | **meta-Goodhart** (2/3 seeds) |\\n| random β=0.1 | r = r_exec·(1+0.1·random) | 0.79 | 0.104 | redundant premises | control |\\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\n\\n**Goodhart 效应跨所有 β 剂量存在，但表现形式不同。** β=0.1: meta-Goodhart（2/3 seeds gaming ISR 本身，1/3 genuine）；β=0.3: classic Goodhart（PR 崩塌）。ISR 作为 reward 的可靠性不足——即使在\\\"最佳\\\"剂量下成功率也仅 1/3。ISR 的核心价值在诊断（Claim 1），不在训练信号。\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\n- **\\\"Just negative results\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding (diagnostic metric gets gamed as reward) is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable contribution，(d) the \\\"negative\\\" result (ISR reward unreliable) is itself the key finding for practitioners。\\n- **\\\"Old wine\\\" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic Goodhart analysis for formal reasoning GRPO) + empirical findings, not algorithm level.\\n- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 6 conditions × 6 hacking modes × 3 training horizons).\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"ISR is just LOO ablation — not novel\\\"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical Goodhart analysis on reward shaping, (c) hacking taxonomy, (d) GRPO saturation mechanism.\\n2. **\\\"β=0.1 success is just one seed\\\"** — Now confirmed: 3-seed β=0.1 results show 1/3 genuine (s42: 80% genuine, multi-premise), 2/3 ISR-specific gaming (s43/s44: conclusion duplication). This seed sensitivity is itself a key finding — it demonstrates ISR reward's unreliability and supports the meta-Goodhart narrative. Random control (0/79 conclusion duplication) confirms the gaming is ISR-specific.\\n3. **\\\"Goodhart's Law is obvious\\\"** — The conceptual prediction is known; the empirical characterization in formal reasoning GRPO is not. Specifically: (a) meta-level Goodhart at low β (diagnostic metric itself gets gamed), (b) ISR being worse than random at high β (not just \\\"less useful\\\"), (c) 6 distinct hacking modes as Goodhart manifestations, (d) ISR-specific gaming absent from matched random control.\\n4. **\\\"No positive result — ISR doesn't improve training\\\"** — ISR's positive result is as **diagnostic** (Claim 1), not as training signal. β=0.1 shows genuine improvement in 1/3 seeds but ISR-specific gaming in 2/3 — this unreliability IS the finding (meta-Goodhart). The paper's contribution is characterizing WHY proxy metrics fail as rewards, not proposing a working reward.\\n5. **\\\"ISR is circular\\\"** — The circularity concern is now empirically validated: ISR as reward induces ISR-specific gaming (conclusion duplication) in 2/3 seeds — the metric optimizes itself. This supports using ISR only for post-hoc diagnosis, never as reward. Component count analysis provides ISR-independent evidence.\\n6. **\\\"Only one logic type\\\"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.\\n7. **\\\"500 steps too short\\\"** — plan016 extends to 1000 steps, showing ISR collapse continues and worsens (0.123→0.003, -97.8%). The ISR崩塌轨迹 covers 100/500/1000 steps.\\n8. **\\\"3 seeds insufficient for statistical claims\\\"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. Statistical claims on mean ISR use 3-seed mean±std.\\n9. **\\\"Related work insufficient\\\"** — Expand to 25+ refs: reward hacking (Gao 2023, Skalse 2022), Goodhart's Law (Manheim & Garrabrant 2019, Karwowski 2024), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur), feature attribution (SHAP), FOLIO (Han 2022).\\n10. **\\\"RIP framework overstated\\\"** — Frame as \\\"component necessity testing inspired by mutation testing's RIP framework,\\\" only Propagation condition operationalized.\\n11. **\\\"Practitioners can't act on this\\\"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable. The meta-Goodhart warning (don't use diagnostic metrics as reward signals) is directly actionable for anyone designing reward shaping in formal reasoning.\\n\\n## Dream-Identified Structural Fixes (Paper Agent)\\n\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\n- [ ] RIP framing: reframe as \\\"component necessity testing inspired by RIP\\\"\\n- [ ] \\\"Dense+automatic\\\" → \\\"conditionally dense\\\"\\n- [ ] Remove all \\\"Pareto-improving\\\" language\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\n- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed at β=0.3)\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)\\n- [x] Hacking taxonomy expanded to 6 modes (plan012 + plan017 + D043 conclusion duplication with ISR inflation)\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart narrative (D031→D043)\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\n- [x] 1000-step ISR collapse documented (plan016, ISR 0.123→0.003)\\n\", \"total_chars\": 15284, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2557986e-a4bf-4ca3-9929-6cb2c677ea09",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a967392e829aaef63",
  "type": "user",
  "uuid": "9269b9da-4572-4893-962e-6bc4bbe1de8d",
  "sourceToolAssistantUUID": "2557986e-a4bf-4ca3-9929-6cb2c677ea09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T10:17:55.069Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01B9EmgPPagqyWUFTR6w9gVX`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9269b9da-4572-4893-962e-6bc4bbe1de8d",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2HkXsgZhkAKAcYonEHm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2149061f-8390-4692-93c9-7f4eb17d6afa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAiRyujfzRpVE1RXK6ePpN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16805,
      "cache_read_input_tokens": 17000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16805,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 18 · 2026-05-14T10:17:55.081Z_

<details><summary>↩ Tool result · `toolu_01B9EmgPPagqyWUFTR6w9gVX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml\", \"content\": \"_next_id: 44\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:34 UTC\\n  summary: MVP 方案：FOL+Prover9 单逻辑 50-step GRPO pilot 验证 STA reward 有效性\\n  rationale: EMNLP ARR DDL 5/25 仅剩 12 天，需要最快速度验证核心假设。选 FOL+Prover9 因为 hacking 模式最清晰（tautological\\n    formulas），STA 的 O(1) 近似最直观（去掉前提后能否证明结论）。50-step pilot 足以观察 ISR 趋势。两个条件并行跑 2 GPU。Pass\\n    标准：ISR gap >20pp + accuracy 降幅 <5pp。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:37 UTC\\n  summary: MVP 方案调整：50步→100步 + 趋势判断 + Phase 0 ISR baseline + kill criteria\\n  rationale: 采纳 Reviewer 三条 warning：(1) 加 pre-training ISR baseline 锚定训练前水平；(2) 50步太短难以观察\\n    reward hacking，改 100步+最后20步 moving average 趋势判断；(3) 补充硬性 kill criteria 防止 DDL\\n    压力下无止境调整。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 20:50 UTC\\n  summary: Phase 1 r4 fast_isr_fol 训练信号无效，改用 full STA + K=8 重跑\\n  rationale: fast_isr_fol 是二值 O(1) 近似（ISR=0 tautology / ISR=1 non-tautology），Qwen3-4B\\n    生成的 proved formalization 几乎全部 ISR=1，与 execution-only 零差异。full STA 提供连续 ISR（0.125-0.889\\n    in Phase 0），能给出真实梯度信号。K=4 导致 frac_reward_zero_std=0.5-1.0（GRPO 无 advantage），K=8\\n    增加 within-group variance。两个改动分别解决 STA 信号粒度和 GRPO 梯度信号两个独立问题。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-only-r4\\n    role: evidence\\n    result: prove_rate 12%→15%, ISR ~0.15, minimal learning\\n  - exp_id: sta-phase1-exec-sta-r4\\n    role: evidence\\n    result: 与 exec-only 几乎完全相同, fast_isr 提供零额外信号\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 21:59 UTC\\n  summary: Reviewer 指出 exec-sta-r5 prove_rate 低于 baseline（退化），STA 50/50 权重过于惩罚性。立即补跑低权重\\n    + bonus 模式实验\\n  rationale: exec-sta-r5 prove_rate=0.10 < baseline=0.12 < exec-only=0.15。连续 ISR 给\\n    proved-but-low-ISR 样本 reward≈0.3（几乎等于未 prove），模型学到 prove 不值得。Kill criteria 未触发（差\\n    5pp 非 15pp，权重未调整），但核心假设受挑战。需立即验证：(1) sta_weight=0.1 降低惩罚 (2) ISR-as-bonus 模式 r=exec×(1+α×ISR)\\n    避免惩罚。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence\\n    result: prove_rate=0.10 < baseline, STA reward 过于惩罚性\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: control\\n    result: prove_rate=0.15, 复现 r4\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 22:13 UTC\\n  summary: ISR/PR 下降因果归因待验证，plan_003 提升为最高优先级消歧实验\\n  rationale: Reviewer 指出 ISR/PR 64%→33% 有两种解释：(A) STA 检测到 hacking (B) 50/50 权重抑制 prove\\n    行为的惩罚效应。ISR 绝对值 ~0.05 ≈ pretrained 水平支持解释 B。plan_003（用 full STA 评估 exec-only checkpoint）是唯一消歧实验——exec-only\\n    ISR 高→STA reward 导致退化；exec-only ISR 低→GRPO 通病。paper_framing.md 已将 claim 降级为观察性表述，因果表述需等\\n    plan_003 结果。cuda:1 排列改为 plan_003 eval 先行，再 plan_005 training。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence\\n    result: ISR/PR 下降但因果不清\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: baseline\\n    result: prove_rate=0.12, ISR 未用 full STA 评估\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 22:14 UTC\\n  summary: paper_framing.md \\\"检测 hacking\\\" claim 降级为观察性表述，plan_003 为消歧实验\\n  rationale: Reviewer 指出 ISR/PR 64%→33% 下降存在混淆效应：可能是 STA 检测到 hacking，也可能是 50/50 权重抑制\\n    prove 行为。ISR 绝对值始终 ~0.05 ≈ pretrained 水平，更像惩罚效应。plan_003（exec-only checkpoint\\n    用 full STA 评估）是消歧实验——完成前 paper 不可用因果表述。已修改 paper_framing.md Claim 1 MVP 证据段。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence_source\\n    result: ISR/PR 下降观察到但因果不清\\n  - exp_id: plan_003\\n    role: disambiguation\\n    result: planned\\n  depends_on:\\n  - D004\\n- id: D007\\n  date: 2026-05-13 23:05 UTC\\n  summary: plan003 因果消歧：exec-only ISR 提升是有机的，50/50 STA 权重是退化根因，STA 概念本身无问题\\n  rationale: plan003 eval 显示 exec-only 100步 checkpoint 的 held-out prove_rate=0.32（baseline\\n    0.12 的 2.7x），proved_only_isr=0.642（远高于 exec+STA r5 的 0.043）。ISR 随 prove_rate 同步提升，排除\\n    reward hacking。exec+STA 50/50 权重导致 prove_rate 低于 baseline（0.10<0.12），确认权重过高是退化根因。\\\"STA\\n    as reward\\\" 叙事仍成立，需精确权重调校。注意：当前结果基于 100-step checkpoint，500-step 需重新验证。\\n  related_experiments:\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: primary\\n    result: prove_rate=0.32, proved_only_isr=0.642, ISR organic\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: comparison\\n    result: prove_rate=0.10, mean_isr=0.043, degraded\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: comparison\\n    result: prove_rate=0.15(last20:0.20), mean_isr=0.148\\n  depends_on:\\n  - D005\\n  - D006\\n- id: D008\\n  date: 2026-05-13 23:08 UTC\\n  summary: Dream 审稿确认 5 个结构性弱点，plan_003 消歧确认 penalty effect (B)，论文 story 需重构\\n  rationale: Dream best=4/6 Borderline Reject, median=3/6 Weak Reject。两档一致指出：(1) related\\n    work 严重不足 6→25+ refs (2) RIP framing 过度——只有 Propagation 可操作化 (3) ISR circularity\\n    未解决——需下游验证或 random baseline (4) 8/12 实验 single-seed 不足 (5) ISR sparsity 使 \\\"dense+automatic\\\"\\n    定位不成立。plan_003 held-out eval 证实 exec-only checkpoint ISR=0.6423（proved-only），高于\\n    GT 0.56，确认 ISR/PR 下降是 penalty effect 而非 hacking detection（interpretation B）。论文\\n    story 必须从 \\\"STA detects hacking\\\" 转向 \\\"STA as principled structural metric + proper\\n    integration via weight tuning\\\"。新增实验需求：random reward baseline + 3-seed for secondary\\n    + downstream validation + curriculum ablation。\\n  related_experiments:\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: disambiguation\\n    result: exec-only ISR=0.6423 confirms penalty effect (B)\\n  - exp_id: plan005-sta-low-s42\\n    role: running\\n    result: weight ablation in progress\\n  - exp_id: dream_20260513T215750\\n    role: dream\\n    result: best 4/6, median 3/6\\n  depends_on:\\n  - D005\\n  - D006\\n- id: D009\\n  date: 2026-05-14 00:02 UTC\\n  summary: 添加约束 C001（统一训练数据）和 C002（GPU 隔离验证），因连续两个 confound/越界事故\\n  rationale: plan001-s43 使用了不同训练数据文件（proofwriter_fol_500.jsonl vs train_500_seed42.jsonl），破坏多\\n    seed 对比控制变量。plan013 因 CUDA_VISIBLE_DEVICES inline 赋值引号问题越界占用两张 GPU，导致 plan001-s43\\n    OOM。两个事故均为 Worker 提交流程缺陷，需要硬约束防止复发。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s43\\n    role: trigger\\n    result: failed (data confound + OOM)\\n  - exp_id: plan013-random-reward-s42\\n    role: trigger\\n    result: failed (GPU overflow)\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-14 02:03 UTC\\n  summary: '批准 framing 转向: STA as metric + additive bonus integration，plan002 改用非凸组合公式'\\n  rationale: 'plan005 negative 确认 penalty effect: 凸组合 r=α·r_exec+β·r_exec·ISR (α+β=1)\\n    下任何 ISR<1 都会惩罚 reward，即使 β=0.1。exec-only (plan003) proved-only ISR=0.6423 远高于\\n    plan005 training ISR=0.23。根本原因: 凸组合约束强制 STA 成为 penalty 而非 bonus。plan002 应改用 additive\\n    bonus: r=r_exec·(1+β·ISR)，β>0，ISR 只能增加 reward 不能减少。Story 正式从 \\\"STA detects hacking\\\"\\n    转为 \\\"STA as principled structural metric + additive bonus integration\\\"。'\\n  related_experiments:\\n  - exp_id: plan005-sta-low-s42\\n    role: evidence\\n    result: 'negative: convex combination penalty effect confirmed'\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: evidence\\n    result: 'success: exec-only ISR=0.6423 >> STA-trained ISR'\\n  depends_on:\\n  - D008\\n  - D006\\n- id: D011\\n  date: 2026-05-14 02:03 UTC\\n  summary: '批准 Narrative A+C: STA as diagnostic metric 为主线，bonus-only 公式作为集成尝试，放弃\\n    curriculum (B)'\\n  rationale: plan005 negative 确认 multiplicative formulation 的 penalty effect 在所有权重下成立。Narrative\\n    A 将所有 negative 结果转化为证据（penalty effect 分析 + ISR/PR ratio 作为 structural health indicator），降低\\n    DDL 风险。选 C 而非 B：bonus-only 是对 multiplicative penalty 的数学根治（additive, threshold-gated），而\\n    curriculum 只是工程 workaround。C 只需改一行 reward 公式 + 1 次训练（~1.5 GPU·h），ROI 最高。如果 C 也\\n    negative，论文退化为纯 metric paper 仍可投 EMNLP findings。\\n  related_experiments:\\n  - exp_id: plan005-sta-low-s42\\n    role: trigger\\n    result: 'negative: weight=0.1 仍 -10.7% prove_rate'\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: evidence\\n    result: exec-only ISR=0.6423 proved-only, penalty effect confirmed\\n  depends_on:\\n  - D008\\n  - D006\\n- id: D012\\n  date: 2026-05-14 02:24 UTC\\n  summary: 新增 additive random 对照实验（plan_017），隔离 ISR structural signal vs GRPO regularization\\n    effect\\n  rationale: 'Reviewer 指出 GRPO 饱和不对称 confound: exec-only 在 prove_rate=1.0 时 reward\\n    variance=0 导致 loss=0（停止学习），而 ISR/random 任何引入 variance 的机制都会维持梯度。plan002 additive\\n    ISR 需要匹配的 additive random 对照：r=r_exec·(1+β·random[0,1])。三组比较: (1) ISR>random>exec-only\\n    → signal+regularization 都贡献 (2) ISR>random≈exec-only → ISR signal 是关键 (3) ISR≈random>exec-only\\n    → 纯 regularization，ISR 内容无价值。这是论文 \\\"ISR provides unique structural signal\\\" claim\\n    的必要证据。'\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: motivation\\n    result: 'confound: convex random introduced variance preventing GRPO saturation'\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: motivation\\n    result: 'GRPO saturation confirmed: loss=0 at prove_rate=1.0'\\n  depends_on:\\n  - D010\\n- id: D013\\n  date: 2026-05-14 02:34 UTC\\n  summary: ISR 评估方法论标准化：所有 checkpoint 必须用 eval_sta.py (full STA) 统一重评，训练日志 ISR 不可用于论文\\n  rationale: Reviewer 核实发现：(1) s42-r2 用旧代码 _fast_fn 二值近似，s43-r4 用 _full_fn full STA，跨\\n    seed ISR 不可比；(2) plan013 random_reward 仍用 _fast_fn，训练 ISR≈prove_rate 是二值假象；(3)\\n    只有 eval_sta.py 产出的 proved_only_ISR 是可靠指标。统一用 eval_sta.py 评估所有 checkpoint 后才能做跨实验比较。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: affected\\n    result: 训练 ISR 与 s42-r2 不可比，需 eval_sta.py 重评\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: reference\\n    result: confirmed full STA, proved_only_ISR=0.6423 有效\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: affected\\n    result: 训练 ISR 不可信(_fast_fn)，需 eval_sta.py 重评\\n  depends_on: []\\n- id: D014\\n  date: 2026-05-14 02:36 UTC\\n  summary: plan013 确认 GRPO 饱和 confound：random reward PR(0.966) > exec-only PR(0.865)，差异源于训练动态而非结构信号\\n  rationale: 'plan013 random reward 实验表明：(1) random noise 通过保持 reward variance 防止\\n    GRPO 饱和，PR 反超 exec-only；(2) 两者 ISR/PR ratio 均≈1.0，random noise 未提供结构信号；(3) 这直接印证\\n    Reviewer #2 的 GRPO 饱和 confound 担忧。结论：exec-only 的 PR→1.0 时 reward_std→0 导致学习停滞，additive\\n    bonus (plan002) 才是正确方案——提供 meaningful variance + anti-saturation。plan013 在论文中应正面叙述\\n    saturation mechanism，将 additive bonus 的 anti-saturation 作为 key design insight。'\\n  related_experiments:\\n  - exp_id: plan013\\n    role: primary\\n    result: random reward PR=0.966 > exec-only PR=0.865, ISR/PR≈1.0\\n  - exp_id: plan001-s42-r2\\n    role: baseline\\n    result: exec-only PR=0.865, ISR/PR≈1.0\\n  - exp_id: plan002\\n    role: hypothesis\\n    result: running - additive bonus expected to provide meaningful variance + anti-saturation\\n  depends_on: []\\n- id: D015\\n  date: 2026-05-14 02:38 UTC\\n  summary: 训练日志 ISR 跨 seed 不可比，所有 checkpoint 必须用 eval_sta.py 统一评估获取 full STA ISR\\n  rationale: Reviewer 核实发现：plan001-s42-r2 用 _fast_fn (binary ISR≈prove_rate)，plan001-s43-r4\\n    用 _full_fn (连续 ISR)，两者训练日志 ISR 不可比。plan013-r4 同样是 binary approximation。论文正式数据必须来自\\n    eval_sta.py 的 full STA 评估。此外 plan001-s43-r4 训练中 ISR 崩塌轨迹（prove_rate=1.0 时 ISR=0.01）是\\n    reward hacking 的直接定量证据，强化论文 thesis。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: affected\\n    result: 训练ISR为binary approximation,需eval_sta.py重评\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: evidence\\n    result: ISR崩塌轨迹:prove_rate=1.0时ISR=0.01,reward hacking证据\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: affected\\n    result: 训练ISR为binary approximation,需eval_sta.py重评\\n  - exp_id: plan003-eval-sta\\n    role: validated\\n    result: proved_only_ISR=0.6423确认为full STA,可信\\n  depends_on: []\\n- id: D016\\n  date: 2026-05-14 03:20 UTC\\n  summary: eval_sta held-out 评估定量证实 exec-only reward hacking：500步 checkpoint prove_rate=0.93\\n    但 ISR=0.1324（median=0.0）\\n  rationale: plan001-r2 exec-only checkpoint-500 在 held-out 100题上的 full STA 评估显示 proved_only_ISR=0.1324，中位\\n    ISR=0.0——模型高 prove_rate 完全依赖 solver 宽松性而非正确 FOL 结构。对比 plan003（100步 checkpoint）的\\n    ISR=0.6423，ISR 随训练从 64% 崩塌到 13%，是 reward hacking 的直接定量证据。跨 seed 一致性已验证（s42 last100\\n    PR=0.865 vs s43 last100 PR=0.883）。这构成论文 Core Claim 1 的核心证据。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: primary\\n    result: held-out PR=0.93, proved_only_ISR=0.1324, median_ISR=0.0\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: replication\\n    result: 训练ISR=0.087(if _full_fn), last100_PR=0.883, 跨seed一致\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: comparison\\n    result: 100步checkpoint ISR=0.6423, 训练前结构质量高\\n  depends_on:\\n  - D015\\n  - D007\\n- id: D017\\n  date: 2026-05-14 03:24 UTC\\n  summary: random reward held-out ISR=0.535 >> exec-only ISR=0.132，anti-saturation\\n    效应可能足以改善结构质量，ISR-specific signal 待 plan002 vs plan017 验证\\n  rationale: plan013 random reward 在 held-out 上 prove_rate=1.0, ISR=0.535, 大幅优于 exec-only\\n    (PR=0.93, ISR=0.132)。Random noise 通过防止 GRPO reward variance→0 的饱和效应让模型持续学习。这挑战了\\\"ISR\\n    提供结构信号\\\"的叙事——可能仅 anti-saturation 就够。关键验证：plan002 (additive ISR) vs plan017 (additive\\n    random) 的 matched control，加上 formalization 组件数对比排除长度 confound。论文叙事可能需要从\\\"ISR reward\\\"转向\\\"GRPO\\n    饱和机制 + STA 诊断工具\\\"。\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: primary\\n    result: held-out PR=1.0, ISR=0.535, median_ISR=0.5, min_ISR=0.5\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: held-out PR=0.93, ISR=0.132, median_ISR=0.0\\n  - exp_id: plan002-additive-b03-s42\\n    role: pending\\n    result: 中期PR严重偏低(39.8%步PR=0),待完成\\n  - exp_id: plan017-additive-random-s42\\n    role: pending\\n    result: 刚启动,matched control\\n  depends_on:\\n  - D016\\n  - D014\\n- id: D018\\n  date: 2026-05-14 03:31 UTC\\n  summary: 推翻 D017：plan013 held-out ISR=0.535 是 tautological hacking 假象（100% P→P），random\\n    reward 加速 hacking 而非改善结构\\n  rationale: Reviewer 逐样本检查 plan013 eval_sta 结果：100/100 样本全部是「把 conclusion 抄一遍当 premise」(P→P\\n    tautology)，ISR=0.5 是机械值（2 components, 1 necessary）而非真实结构质量。D017 基于 ISR=0.535 得出的\\\"anti-saturation\\n    改善结构\\\"结论完全错误。实际情况：random reward 让模型找到了最终极的 hacking 捷径——100% tautological formalization。对比\\n    exec-only 100步 ISR=0.6423（有真实推理）→ 500步 ISR=0.132（退化但非全 tautological），random reward\\n    加速了 hacking 收敛。plan002 eval_sta 结果成为关键：如果 additive ISR bonus 产生的是非 tautological\\n    formalization，即使 PR 低也是积极信号——ISR reward 在抵抗 hacking。\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: primary\\n    result: 100% tautological P→P, ISR=0.5 是机械值而非结构质量\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: comparison\\n    result: held-out PR=0.93, ISR=0.132, 部分真实推理\\n  - exp_id: plan002-additive-b03-s42\\n    role: pending_critical\\n    result: PR低但可能是真实推理, eval_sta 待出\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-14 03:33 UTC\\n  summary: ISR 衡量 syntactic component necessity 而非 semantic faithfulness，论文需明确边界并用\\n    plan014 downstream validation 补盲区\\n  rationale: Reviewer 发现 ISR 反直觉行为：plan013 P→P 纯重言式 ISR=0.5 > plan001 多前提嵌入 conclusion\\n    ISR≈0。从语义忠实度看 P→P 更差（完全忽略 context），但 ISR 定义下反而更高，因为 ISR=n_necessary/n_components，极简\\n    formalization 的分母小。论文不能将 ISR 差异直接等同于 formalization 质量差异——需明确 ISR 的 scope 是 component\\n    necessity。plan014 downstream NLI validation 直接测量 semantic faithfulness，弥补 ISR\\n    盲区。同时建议考虑组合指标（ISR + non-tautological check + 最小组件数阈值）。\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: evidence\\n    result: P→P tautology ISR=0.5, 语义完全退化但ISR不低\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: evidence\\n    result: 多前提嵌入conclusion ISR≈0, 语义更好但ISR更低\\n  - exp_id: plan014\\n    role: mitigation\\n    result: downstream NLI validation 补充语义忠实度测量\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-14 03:40 UTC\\n  summary: plan002 additive ISR β=0.3 负面结果确认：PR=18% + ISR=0.1427，ISR reward 作为训练信号的路线全面失败，论文转向纯诊断/分析贡献\\n  rationale: 'plan002 held-out eval: PR=18%（最差）, ISR=0.1427≈exec-only 0.1324。加上 plan005\\n    (convex, negative) 和 plan013 (random, tautological hacking)，所有 ISR-as-reward 方案均失败。但三个条件产生了三种不同的退化模式（conclusion\\n    embedding / P→P tautology / repetitive cycling），这本身是有价值的研究发现。论文应完全放弃\\\"ISR reward\\n    改善训练\\\"的 claim，转向：(1) STA/ISR 作为诊断工具检测 reward hacking (2) GRPO saturation 机制分析 (3)\\n    不同 reward 信号下的 hacking 策略分类学 (4) ISR 随训练的崩塌轨迹。plan014 downstream validation 成为证明\\n    ISR 诊断价值的关键实验。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b03-s42\\n    role: primary\\n    result: 'negative: PR=18%, ISR=0.1427, 重复前提循环退化'\\n  - exp_id: plan005-sta-low-s42\\n    role: prior_negative\\n    result: convex combination penalty effect\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: comparison\\n    result: 100% tautological hacking, ISR=0.5 假象\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: PR=93%, ISR=0.132, conclusion embedding\\n  depends_on:\\n  - D018\\n  - D019\\n  - D010\\n- id: D021\\n  date: 2026-05-14 04:28 UTC\\n  summary: plan014 ISR-accuracy 假说被否定；ISR 定位为 syntactic necessity 指标，不 claim semantic\\n    quality proxy\\n  rationale: Spearman ρ(ISR, entailment_accuracy) = -0.049, p=0.187（n=732），ISR-based\\n    BoN Δ=0.88pp CI含零。同时发现系统性 true 偏差（gold=true 91.2% acc, gold=false 0%），说明 formalization\\n    pipeline 本身有 truth bias。ISR 衡量组件必要性（去掉后证明是否成立），不衡量 formalization 是否语义忠实。论文应明确此\\n    limitation，将 plan014 作为 negative result 诚实报告，刻画 ISR 能力边界。\\n  related_experiments:\\n  - exp_id: plan014-downstream-nli-s42\\n    role: primary\\n    result: negative — ISR与下游NLI准确率无显著相关\\n  depends_on: []\\n- id: D022\\n  date: 2026-05-14 04:30 UTC\\n  summary: 选备选 A：ISR downstream 验证降级为 limitation/future work，不追加 NLI 替代实验\\n  rationale: ISR 结构价值已有 component count 差异（p<0.0001）和 cross-checkpoint 对比强证据。NLI negative\\n    源于 formalization model 的 true-bias（非 ISR 本身缺陷），换 downstream 任务（B）在同一 model 上大概率复现同样问题。n=12\\n    的 bucket 趋势（C）统计不可靠。聚焦 plan017 + s44 完成核心证据链。\\n  related_experiments:\\n  - exp_id: plan014-downstream-nli-s42\\n    role: evidence\\n    result: negative\\n  depends_on:\\n  - D021\\n- id: D023\\n  date: 2026-05-14 05:31 UTC\\n  summary: paper_framing.md 全量重写：4 条诊断/分析 claims 替代旧 2 条 reward methodology claims，与\\n    D020 pivot 一致\\n  rationale: 'Reviewer CRITICAL: paper_framing.md 仍写 \\\"STA as Reward Design Methodology\\\"\\n    + additive bonus headline，但 D020 已确认 ISR-as-reward 全面失败。新 framing 4 条 claims:\\n    (1) ISR as hacking diagnostic (ISR 崩塌轨迹), (2) GRPO saturation mechanism, (3) hacking\\n    taxonomy (4 种模式), (4) ISR capability boundary (syntactic necessity ≠ semantic\\n    faithfulness)。Story spine 从 \\\"propose structural reward\\\" 转为 \\\"diagnostic tool +\\n    systematic empirical study of reward hacking\\\"。负面结果表（convex/additive/random）作为正面贡献呈现。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b03-s42\\n    role: negative_evidence\\n    result: PR=18%, ISR=0.14, repetitive cycling\\n  - exp_id: plan005-sta-low-s42\\n    role: negative_evidence\\n    result: convex penalty effect confirmed\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: negative_evidence\\n    result: 100% tautological, ISR=0.5 mechanical\\n  - exp_id: plan014-downstream-nli-s42\\n    role: negative_evidence\\n    result: ρ=-0.049 n.s., ISR ≠ semantic quality\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: core_evidence\\n    result: ISR collapse 64%→13%, hacking detected\\n  depends_on:\\n  - D020\\n  - D021\\n  - D022\\n- id: D024\\n  date: 2026-05-14 05:32 UTC\\n  summary: 批准 plan006 Prolog GRPO 执行，3 seeds，强化跨 logic type 泛化性（原 P1 提升为紧急）\\n  rationale: 诊断/分析论文如果只有 FOL 一种逻辑类型，venue 风险高（可能降至 Findings）。plan006 Prolog 验证 hacking\\n    现象是否跨 logic type 泛化，6 GPU·h 成本低（vs 528 GPU·h 可用）。Reviewer 明确指出 generalizability\\n    是论文能否进 Main 的关键因素。先跑 exec-only seed=42 验证方向，成功再 3-seed。\\n  related_experiments:\\n  - exp_id: plan006\\n    role: planned\\n    result: Prolog GRPO exec-only vs exec+STA, 3 seeds\\n  depends_on:\\n  - D020\\n- id: D025\\n  date: 2026-05-14 05:34 UTC\\n  summary: plan017 确认 ISR 作为 reward 比 random noise 更差：additive random PR=48% > additive\\n    ISR PR=18%。ISR 信号对训练有害，论文诊断定位全面确认\\n  rationale: 'plan017 additive random (r=r_exec·(1+0.3·random)) held-out eval: PR=48%,\\n    ISR=0.045, components=9.56。对比 plan002 additive ISR (PR=18%, ISR=0.026, components=10.67)，random\\n    noise 在相同公式结构下 PR 高 2.7 倍。关键洞察：(1) ISR 结构信号对 GRPO 训练有害而非无用；(2) additive 乘法结构本身防止\\n    tautological collapse（两者 components 9-10 vs plan013 的 2.04）；(3) 但 additive 结构也无法产生\\n    genuine proofs（PR 远低于 exec-only s42 的 93%）。六组实验全景完整：exec-only 是唯一产生 genuine proofs\\n    的方案（1/3 seeds），ISR 应定位为 post-hoc diagnostic，非 training signal。'\\n  related_experiments:\\n  - exp_id: plan017-additive-random-s42\\n    role: primary\\n    result: 'negative: PR=48%, ISR=0.045, components=9.56, complex-but-useless'\\n  - exp_id: plan002-additive-b03-s42\\n    role: comparison\\n    result: 'negative: PR=18%, ISR=0.026, ISR worse than random'\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: comparison\\n    result: PR=100% but 100% tautological, components=2.04\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: PR=93%, ISR=0.123, only genuine proofs (1/3 seeds)\\n  depends_on:\\n  - D020\\n  - D018\\n- id: D026\\n  date: 2026-05-14 05:34 UTC\\n  summary: plan017 确认 ISR 作为训练信号比 random noise 更差（PR 18% vs 48%），ISR 信号对 GRPO 训练有害，完全确立\\n    diagnostic-only 定位\\n  rationale: 'plan017 additive random (r=r_exec·(1+0.3·random)) eval_sta: PR=48%,\\n    ISR=0.045, components=9.56。对比 plan002 additive ISR (β=0.3): PR=18%, ISR=0.026,\\n    components=10.67。ISR 结构信号不仅无法改善训练，反而比 random noise 更差——ISR 信号对训练动态有害。两个 additive\\n    方案都保持高 component count（9-10），说明乘法结构 r_exec·(1+βX) 本身防止 tautological collapse，但不产生\\n    genuine proofs。Exec-only (s42) 仍是唯一产生 genuine proofs 的方案（PR=93%），但 2/3 seeds 失败。论文六组实验消融完整，强化\\n    ISR diagnostic-only 定位：ISR 应用于 post-hoc 诊断而非 reward shaping。'\\n  related_experiments:\\n  - exp_id: plan017-additive-random-s42\\n    role: primary\\n    result: 'negative: PR=48%, ISR=0.045, complex-but-useless formalization'\\n  - exp_id: plan002-additive-b03-s42\\n    role: comparison\\n    result: 'negative: PR=18%, ISR=0.026, ISR worse than random'\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: 'success: PR=93%, ISR=0.132, only genuine proofs'\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: comparison\\n    result: 'tautological: PR=100%, ISR=0.535, P→P collapse'\\n  depends_on:\\n  - D020\\n  - D018\\n  - D012\\n- id: D027\\n  date: 2026-05-14 05:35 UTC\\n  summary: 采纳备选 A+B：plan017 加入 Claim 2 证据 + Claim 3 增加第 5 种 hacking mode \\\"complexity-without-utility\\\"；Reviewer\\n    关于 plan013 vs plan017 公式差异的 warning 纳入写作约束\\n  rationale: 'plan017 结果完善了六组消融对比。备选 A 将 plan017 加入 Claim 2（GRPO 对 reward perturbation\\n    敏感）是必须的数据更新。备选 B 增加第 5 种 hacking mode（complexity-without-utility: 高 component\\n    但 conclusion 不依赖任何 premise）丰富 taxonomy，区别于 exec-only 的 conclusion embedding。Reviewer\\n    指出 plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 不是纯 additive\\n    vs convex 对照（公式结构+random 影响方式两个变量），论文措辞需精确标注差异，不可简化为\\\"additive vs convex\\\"。plan017\\n    vs plan002 的对比（random PR=48% vs ISR PR=18%）作为论文 §5 核心证据。'\\n  related_experiments:\\n  - exp_id: plan017-additive-random-s42\\n    role: primary\\n    result: 'negative: PR=48%, complexity-without-utility mode'\\n  - exp_id: plan002-additive-b03-s42\\n    role: comparison\\n    result: 'ISR worse than random: PR=18% vs 48%'\\n  depends_on:\\n  - D026\\n  - D020\\n- id: D028\\n  date: 2026-05-14 05:35 UTC\\n  summary: paper_framing.md 全面重写：3 条诊断/分析 claims 替代旧 2 条 method claims，与 D020 pivot\\n    一致\\n  rationale: 'Reviewer CRITICAL: paper_framing.md 仍写 \\\"STA as Reward Design Methodology\\\"\\n    + additive bonus headline，与 D020 pivot 严重矛盾。重写为 3 条诊断 claims: (1) ISR as hacking\\n    diagnostic (ISR 崩塌轨迹), (2) GRPO saturation mechanism (variance redirection), (3)\\n    cross-logic generality (conditional on plan006)。Story spine 从 \\\"ISR improves training\\\"\\n    转为 \\\"ISR detects hacking + 4 hacking modes + saturation trap\\\"。ISR-as-reward failure\\n    log 保留所有 negative results 作为论文贡献。Headline result 更新为诊断发现而非方法改进。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b03-s42\\n    role: evidence\\n    result: 'negative: PR=18%, ISR=0.1427'\\n  - exp_id: plan005-sta-low-s42\\n    role: evidence\\n    result: 'negative: convex penalty'\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: evidence\\n    result: tautological collapse\\n  - exp_id: plan014-downstream-nli-s42\\n    role: evidence\\n    result: 'negative: ρ=-0.049'\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: PR=93%, ISR=0.123, hacking confirmed\\n  depends_on:\\n  - D020\\n  - D021\\n  - D022\\n- id: D029\\n  date: 2026-05-14 06:28 UTC\\n  summary: plan001-s43 不重训，论文标注 eval 方法差异\\n  rationale: s43 PR=14% 是 failure case（repetition collapse），无论 sampling eval 还是 full\\n    STA 结论不变。主 story 用 s42(hacking) vs s44(tautological) 对比，s43 只作为第三种 failure mode\\n    的佐证。重训 1h GPU 不值得，标注方法差异即可。\\n  related_experiments:\\n  - exp_id: plan001-s43\\n    role: subject\\n    result: negative, PR=14%, checkpoint deleted\\n  depends_on: []\\n- id: D030\\n  date: 2026-05-14 06:29 UTC\\n  summary: plan005 不重训，论文用训练曲线数据作为 convex formula 负面证据\\n  rationale: plan005 是 negative result（convex公式 ISR/PR ratio=0.298, 99/100步 ISR&lt;PR），用于解释为什么从凸组合切换到\\n    additive bonus。训练曲线 windowed metrics 足以支撑这个 narrative，不需要 held-out eval。checkpoint\\n    已删除，重训 1h 收益极低。\\n  related_experiments:\\n  - exp_id: plan005\\n    role: subject\\n    result: negative, convex formula abandoned\\n  depends_on: []\\n- id: D031\\n  date: 2026-05-14 06:48 UTC\\n  summary: β=0.1 ISR 结果异常好(PR=0.81/ISR=0.415)，紧急补 β=0.1 random control 后再决定是否调整 framing\\n  rationale: β=0.1 additive ISR 是所有条件中唯一同时高 PR + 高 ISR 的。但无法确定优势来自 ISR structural\\n    signal 还是 variance regularization——缺少 matched β=0.1 random control。在补控制实验之前暂不调整\\n    paper_framing.md。若 β=0.1 random PR高但ISR低 → ISR 在低剂量下真正提升结构质量，narrative 升级为\\\"dose-dependent\\n    reward shaping\\\"；若 β=0.1 random 也高ISR → 优势来自 regularization，维持当前 framing。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: trigger\\n    result: PR=0.81, ISR=0.415, best structural quality\\n  - exp_id: plan017\\n    role: existing_control\\n    result: β=0.3 random, PR=0.48, ISR=0.094\\n  depends_on:\\n  - D026\\n  - D027\\n- id: D032\\n  date: 2026-05-14 06:49 UTC\\n  summary: β=0.1 ISR success 暂不改 framing，先跑 β=0.1 random matched control\\n  rationale: plan002-b01 (β=0.1) PR=0.81/ISR=0.415 是重大正面结果，但 Reviewer 正确指出：缺 β=0.1\\n    random control 无法区分\\\"ISR structural signal\\\"和\\\"low-dose regularization effect\\\"。β=0.3\\n    有 matched random (plan017)，β=0.1 没有。在 control 结果出来前修改 framing 是冒进的——如果 β=0.1 random\\n    也给高 ISR，则 ISR 无特殊价值。Control 仅需 ~1h GPU，成本极低。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: trigger\\n    result: success, PR=0.81, ISR=0.415\\n  - exp_id: plan017\\n    role: precedent\\n    result: β=0.3 random control, PR=0.48\\n  depends_on:\\n  - D026\\n  - D027\\n- id: D033\\n  date: 2026-05-14 08:25 UTC\\n  summary: Framing 升级为 Goodhart 主线：ISR 在低剂量(β=0.1)有效、高剂量(β=0.3)崩溃，统一用 Goodhart's Law\\n    解释\\n  rationale: plan018 eval 确认 ISR β=0.1 结构价值真实（ISR 3.2x > random control，PR 持平）。β=0.3\\n    下 ISR < random 是 Goodhart 过度优化。统一叙事：ISR 作为 proxy metric 遵循 Goodhart's Law —— diagnostic\\n    有价值 (Claim 1)、低剂量优化有效、高剂量导致 Goodhart 崩溃。覆盖所有实验结果且有理论锚点。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: trigger\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\n  - exp_id: plan018\\n    role: matched_control\\n    result: 'random β=0.1: PR=0.79, ISR=0.104, confirms ISR signal genuine'\\n  - exp_id: plan002-b03\\n    role: high_dose\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\n  - exp_id: plan017\\n    role: high_dose_control\\n    result: 'random β=0.3: PR=0.48, random > ISR at high dose'\\n  - exp_id: plan016\\n    role: temporal_goodhart\\n    result: 1000-step ISR=0.003, temporal dimension of Goodhart\\n  depends_on:\\n  - D031\\n  - D026\\n  - D027\\n- id: D034\\n  date: 2026-05-14 08:25 UTC\\n  summary: Framing 选 C+A 混合：Goodhart 为主线叙事，ISR 诊断保留为 Claim 1，Claim 2 从\\\"ISR misleading\\\"升级为\\\"ISR\\n    exhibits dose-dependent Goodhart effect\\\"\\n  rationale: plan018 确认 β=0.1 ISR 的结构优势是真实信号（proved_only ISR 0.415 vs random 0.131,\\n    3.2x），非 variance regularization。全景数据：β=0.1 ISR>>random（有效）、β=0.3 ISR<&lt;random（Goodhart\\n    崩塌）。选 C（Goodhart 主线）因为：1) 统一所有实验结果在一个叙事下；2) Goodhart's Law 审稿人熟悉，不需要大量额外文献；3)\\n    提供理论解释力而非仅经验观察。融入 A 的元素：ISR 不仅是诊断工具，低剂量下也是有效 reward signal，这是实用贡献。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: evidence\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\n  - exp_id: plan018\\n    role: matched_control\\n    result: 'random β=0.1: PR=0.79, ISR=0.131, confirms ISR signal is genuine'\\n  - exp_id: plan002-b03\\n    role: evidence\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\n  - exp_id: plan017\\n    role: matched_control\\n    result: 'random β=0.3: PR=0.48, ISR beats random at high β'\\n  depends_on:\\n  - D031\\n  - D026\\n  - D027\\n- id: D035\\n  date: 2026-05-14 08:25 UTC\\n  summary: 'Framing 选 C: Goodhart 主线 — ISR 展示经典 Goodhart 效应（β=0.1 有效, β=0.3 崩塌）'\\n  rationale: plan018 确认 ISR β=0.1 结构价值真实（ISR 3.2x > random, PR 持平）。三个备选中 C 最强：(1)\\n    统一所有结果（诊断→优化→Goodhart 崩塌）为一条叙事线；(2) Goodhart's law 是 ML 审稿人熟悉的理论锚点；(3) 剂量-效应数据（β=0.1\\n    有效 vs β=0.3 灾难）是异常干净的实证；(4) 连接到更广泛的 RL alignment 关切，提升论文影响力。Claim 2 从 \\\"ISR actively\\n    misleading\\\" 修订为 \\\"ISR exhibits classic Goodhart effect with dose-dependent dynamics\\\"。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: evidence\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\n  - exp_id: plan018\\n    role: matched_control\\n    result: 'random β=0.1: PR=0.79, ISR=0.131, confirms ISR structural signal'\\n  - exp_id: plan002-b03\\n    role: evidence\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\n  - exp_id: plan017\\n    role: matched_control\\n    result: 'random β=0.3: PR=0.48, ISR > random at high dose'\\n  depends_on:\\n  - D031\\n  - D026\\n  - D027\\n- id: D036\\n  date: 2026-05-14 08:35 UTC\\n  summary: 为 beta=0.1 补跑多 seed (s43/s44) 验证 ISR vs random 的稳健性\\n  rationale: exec-only 已知 seed variance 极大 (s42/s43/s44 三种完全不同行为)。beta=0.1 当前仅 s42\\n    单 seed，ISR (PR=0.81) vs random (PR=0.79) 差距仅 2pp，单 seed 不足以区分 signal 和 noise。ISR\\n    差距 (0.337 vs 0.104) 需要多 seed 确认。用户主动提出，判断正确。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR beta=0.1 baseline (单seed)\\n    result: PR=0.81, ISR=0.337\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random beta=0.1 control (单seed)\\n    result: PR=0.79, ISR=0.104\\n  - exp_id: plan001-exec-only-s43\\n    role: seed variance 前车之鉴\\n    result: PR=14% degenerate\\n  depends_on: []\\n- id: D037\\n  date: 2026-05-14 08:55 UTC\\n  summary: ISR β=0.1 质量验证路径：先 hacking taxonomy 对比，必要时加 LLM-as-judge\\n  rationale: ISR 更高不等于质量更好（plan014 NLI negative）。用户指出需要独立于 ISR 的质量证据。Hacking taxonomy\\n    是最直接的结构质量指标，但可能覆盖不全。LLM-as-judge 作为补充手段，覆盖 taxonomy 未涵盖的 hacking 模式。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR β=0.1 待分析\\n    result: PR=0.81, ISR=0.337\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random β=0.1 待分析\\n    result: PR=0.79, ISR=0.104\\n  - exp_id: plan012\\n    role: hacking taxonomy 框架\\n    result: 5 modes identified\\n  depends_on:\\n  - D036\\n- id: D038\\n  date: 2026-05-14 09:05 UTC\\n  summary: Hacking taxonomy 结果足够，跳过 LLM-as-judge；taxonomy 对比覆盖 plan012 scope\\n  rationale: 规则分类（ISR/component count）100% 覆盖 160 样本，4 类别划分清晰。核心发现：ISR β=0.1 genuine\\n    +8.2pp vs random，conclusion embedding 73-79% 主导。LLM-as-judge 增加主观性/复现顾虑，边际收益低。Taxonomy\\n    对比分析（81+79=160 样本，系统化规则分类）实质替代 plan012 手工标注方案。\\n  related_experiments:\\n  - exp_id: plan012\\n    role: fulfilled_by_taxonomy\\n    result: ISR genuine 25.9% vs random 17.7%\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR_condition\\n    result: genuine 21/81\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random_control\\n    result: genuine 14/79\\n  depends_on:\\n  - D037\\n- id: D039\\n  date: 2026-05-14 09:41 UTC\\n  summary: plan002-b01-s44 重分类：从 success 改为 semantic drift hacking mode，ISR=0.803\\n    是结构最小性产物\\n  rationale: Reviewer 逐样本审查发现 s44 避免了 tautological collapse 但进入新退化模式：65% 样本 ISR=1.0（前提≈结论\\n    conclusion embedding），模型生成极简形式化通过结构最小性骗过 ISR。高 ISR 不代表证明质量。这实际强化 Claim 1（ISR 是诊断工具而非\\n    reward 信号）的 Goodhart 叙事——ISR-as-reward 改变 collapse mode 但不消除 hacking。Hacking taxonomy\\n    需增加第 6 种模式 \\\"Semantic Drift\\\"。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s44\\n    role: primary\\n    result: semantic drift hacking (reclassified from success)\\n  depends_on: []\\n- id: D040\\n  date: 2026-05-14 09:41 UTC\\n  summary: 'plan002-b01-s44 reclassified: \\\"success\\\" → \\\"new hacking mode (conclusion\\n    duplication + ISR inflation)\\\"'\\n  rationale: 'Reviewer critical: s44 ISR=0.902 超过 GT ISR=0.559，模型生成单 premise≈conclusion\\n    的极简形式化，通过 conclusion sub-component ablation 膨胀 ISR。不是 tautological collapse 但仍是\\n    reward hacking。这强化 Claim 1（ISR as diagnostic not reward）——ISR-as-reward 改变 hacking\\n    mode 但不消除 hacking。Hacking taxonomy 需增加第 6 种模式。3-seed β=0.1 统计需加 caveat 或分开报告。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s44\\n    role: subject\\n    result: ISR=0.902 is artifact of conclusion duplication, not genuine quality\\n  - exp_id: plan002-additive-b01-s42\\n    role: comparison\\n    result: ISR=0.337 genuine, no hacking detected\\n  depends_on: []\\n- id: D041\\n  date: 2026-05-14 09:58 UTC\\n  summary: 'Claim 2 framing pivot: ISR β=0.1 \\\"sweet spot\\\" → \\\"all-dose Goodhart with\\n    dose-dependent hacking modes\\\"'\\n  rationale: 3-seed ISR β=0.1 结果：2/3 seeds (s43, s44) 出现 conclusion duplication hacking\\n    (premise≈conclusion, P→P 重言式)，ISR 被膨胀到 0.83/0.90 (artifact)。仅 s42 可能 genuine (comp=5.58,\\n    ISR=0.415)。\\\"低剂量 ISR 有效引导结构改善\\\"的叙事在多 seed 下不成立。新叙事更强：ISR 作为 reward 在所有测试剂量下都触发 Goodhart——高剂量(β=0.3)\\n    PR collapse + format degeneration，低剂量(β=0.1) 引发更隐蔽的 conclusion duplication hacking。Conclusion\\n    duplication 作为第 6 种 hacking taxonomy 类型。需先验证 s42 是否真正 genuine + random β=0.1 是否也有此模式。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: evidence\\n    result: PR=0.81, ISR=0.337, comp=5.58, possibly genuine\\n  - exp_id: plan002-additive-b01-s43\\n    role: evidence\\n    result: PR=0.61, ISR=0.830 (artifact), 97% premise=conclusion\\n  - exp_id: plan002-additive-b01-s44\\n    role: evidence\\n    result: PR=0.89, ISR=0.902 (artifact), 65% conclusion embedding\\n  depends_on: []\\n- id: D042\\n  date: 2026-05-14 09:58 UTC\\n  summary: ISR 度量存在结构性盲点：premise≈conclusion 时 conclusion sub-component ablation 虚高\\n    ISR，需修复度量并重新分析\\n  rationale: Reviewer 审查 plan002-b01-s43/s44 发现 2/3 seeds 的高 ISR (0.830/0.902) 源于\\n    premise=conclusion 逐字重复导致的 conclusion sub-component ablation artifact。只有 s42 (ISR=0.337)\\n    反映真实结构质量。ISR 度量在 premise≈conclusion 场景下有结构性盲点——模型学会 P→P 单步证明时，exec reward=1.0\\n    且 ISR 被膨胀至 0.8-1.0。这不仅是 metric bug，更是 ISR-as-reward 诱导的新型 hacking mode（conclusion\\n    duplication），ISR 自身无法检测。行动：(1) 修复 ISR 度量加 premise≈conclusion 检测 (2) 用修复后度量重新分析\\n    s43/s44 (3) 检查 plan018 random control 是否也有此问题 (4) 更新 paper framing：ISR 盲点作为贡献/limitation，hacking\\n    taxonomy 加第 6 类\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s43\\n    role: evidence\\n    result: ISR=0.830 inflated by premise≈conclusion duplication (65.6% ISR=1.0)\\n  - exp_id: plan002-additive-b01-s44\\n    role: evidence\\n    result: ISR=0.902 inflated by same mechanism\\n  - exp_id: plan002-additive-b01-s42\\n    role: baseline\\n    result: ISR=0.337 genuine (n_comp=5.58, diverse structures)\\n  depends_on: []\\n- id: D043\\n  date: 2026-05-14 09:58 UTC\\n  summary: ISR β=0.1 \\\"sweet spot\\\"叙事降级：2/3 seeds ISR 膨胀为 artifact，Claim 2 改为 meta-level\\n    Goodhart\\n  rationale: 'Reviewer critical: s43 ISR=0.830, s44 ISR=0.902 均超 GT ISR=0.559，由 premise=conclusion\\n    单前提证明 + conclusion sub-component ablation 膨胀。仅 s42 ISR=0.337 可能 genuine。ISR bonus\\n    诱导了新型 hacking 模式（Conclusion Duplication + ISR Inflation），而 random β=0.1 控制组产生\\n    redundant premises 不触发此膨胀——证明这是 ISR-specific gaming。Claim 2 叙事从\\\"β=0.1 is sweet\\n    spot\\\"调整为\\\"ISR as reward exhibits meta-level Goodhart: even the diagnostic metric\\n    gets gamed, with 2/3 seeds developing ISR-inflating strategies\\\"。这实际上是更强的贡献。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: possibly genuine seed\\n    result: PR=0.81, ISR=0.337, comp=5.58 — below GT ISR, needs per-sample verification\\n  - exp_id: plan002-additive-b01-s43\\n    role: ISR inflation seed\\n    result: PR=0.61, ISR=0.830, 65.6% ISR=1.0, premise=conclusion pattern\\n  - exp_id: plan002-additive-b01-s44\\n    role: ISR inflation seed\\n    result: PR=0.89, ISR=0.902, same conclusion duplication pattern\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random control\\n    result: PR=0.79, ISR=0.104, redundant premises — no ISR inflation\\n  depends_on: []\\n\", \"total_chars\": 35361, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2149061f-8390-4692-93c9-7f4eb17d6afa",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a967392e829aaef63",
  "type": "user",
  "uuid": "b0ba80f9-0b19-4504-8dbd-68a2f9ea8fea",
  "sourceToolAssistantUUID": "2149061f-8390-4692-93c9-7f4eb17d6afa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T10:17:55.324Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AQXPRKg2F1eNyRSyXYcsoW`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0ba80f9-0b19-4504-8dbd-68a2f9ea8fea",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2HkXsgZhkAKAcYonEHm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f8a9706-f73e-4fe9-ba2d-ffeccb3ad599",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAiRyujfzRpVE1RXK6ePpN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16805,
      "cache_read_input_tokens": 17000,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16805
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 290,
          "cache_read_input_tokens": 17000,
          "cache_creation_input_tokens": 16805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16805,
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

_source line 20 · 2026-05-14T10:17:55.340Z_

<details><summary>↩ Tool result · `toolu_01AQXPRKg2F1eNyRSyXYcsoW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md\", \"content\": \"# solver-trace-ablation — Memory\\n\\n## 环境信息 (2026-05-13)\\n\\n### westd-39279 服务器\\n- **GPU**: 2× RTX PRO 6000 Blackwell, 94GB VRAM 每张\\n- **CUDA**: 12.8, PyTorch 2.10.0+cu128\\n- **镜像**: aml-train（conda 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）\\n- **ML 栈**: transformers/trl/vllm/accelerate 全部预装\\n- **Solvers**: Prover9 (LADR 2009-11A 源码编译), SWI-Prolog 8.4.2 (`/usr/bin/swipl`), Z3 4.16.0.0\\n- **模型**: Qwen3-4B 已下载（7.6GB，通过 ModelScope）\\n- **代码路径**: `/root/solver-trace-ablation/`\\n- **磁盘**: 系统盘 30GB (22G free)，数据盘 `/root/autodl-tmp/` 250GB (142G free)\\n\\n### 决策记录\\n- Qwen3-4B 用 ModelScope 下载（HuggingFace 直连可能慢）\\n- Prover9 从 LADR 源码编译（apt 无包）\\n- 94GB VRAM 单卡跑 Qwen3-4B 完全无压力\\n\\n## 数据 (2026-05-13)\\n\\n### 数据源变更：ProofWriter → FOLIO\\n- ProofWriter 原始数据无 FOL 列，改用 `tasksource/folio`（1204 条人工标注 FOL）\\n- Phase 0 子集 100 条，训练子集 500 条\\n- 34% 数据含 XOR (⊕) 符号，已在 `_normalize_fol()` 中修复展开\\n\\n### 数据约束 (2026-05-14, D009)\\n- **C001**: 所有 plan001/plan013 实验统一使用 `train_500_seed42.jsonl`，不再用 `proofwriter_fol_500.jsonl`（消除数据差异 confound）\\n\\n## Phase 0 关键发现 (2026-05-13)\\n\\n### Base Model ISR Baseline (sta-phase0-baseline)\\n- **Prove rate**: 12% overall, 18.2% excluding XOR-affected samples\\n- **Mean ISR**: 0.064 (very low — base model formalizations mostly unprovable)\\n- **ISR 区分度**: proved 样本 ISR 0.125–0.889\\n\\n### Ground-Truth ISR Baseline (sta-gt-isr-baseline)\\n- **GT prove rate**: 18% (limited by Prover9 only proving entailment; true=50%, false=4%, unknown=0%)\\n- **GT mean ISR**: 0.5588 (median 0.6125, range 0.14–1.00)\\n- **Model vs GT gap**: ISR 0.064 vs 0.559 = 8.7x 差距，STA 有强区分力\\n\\n### Prover9 局限性\\n- Prover9 只能证明 entailment（conclusion 从 premises 推出）\\n- `false` 和 `unknown` 类问题几乎无法证明（false 4%, unknown 0%）\\n\\n## Phase 1 关键经验 (2026-05-13)\\n\\n### fast_isr_fol 失败教训 (r4)\\n- `fast_isr_fol()` 是二值 tautology gate (0/1)，Qwen3-4B 不产生 tautology → ISR ≡ prove_rate → 两条件零差异\\n- **教训：binary ISR 无法提供有意义的 reward shaping 信号，必须用连续 ISR**\\n\\n### D010 Reward 公式转向 (2026-05-14)\\n- **旧公式（废弃）**: r = α·r_exec + β·r_exec·ISR, α+β=1 → ISR<1 时永远是 penalty\\n- **新公式**: r = r_exec · (1 + β·ISR), β>0 → ISR 只能 bonus，不能 penalty\\n\\n## Held-out eval_sta 全量结果 (2026-05-14) — 关键\\n\\n### 九组 eval 对比（含 plan016 1000步 + plan018 random β=0.1）\\n\\n| 实验 | Reward | Steps | eval PR | eval ISR | proved_only_ISR | n_components | 退化模式 |\\n|------|--------|-------|---------|----------|-----------------|--------------|----------|\\n| plan001-s42 | exec-only | 500 | **93%** | 0.123 | 0.132 | 6.58 | ✅ Genuine proofs |\\n| plan001-s43 | exec-only | 500 | **14%** | 0.000 | 0.000 | N/A | ❌ 长输出退化 |\\n| plan001-s44 | exec-only | 500 | **98%** | 0.570 | 0.582 | 2.04 | ❌ Tautological collapse |\\n| **plan016** | **exec-only** | **1000** | **96%** | **0.003** | **0.003** | **18.55** | **❌ 矛盾爆炸崩塌** |\\n| **plan002-b01** | **additive ISR β=0.1** | 500 | **81%** | **0.337** | **0.415** | **5.58** | **✅ Genuine + improved** |\\n| **plan018** | **additive random β=0.1** | 500 | **79%** | **0.104** | **0.131** | **8.46** | **⚠️ 冗余但无坍缩** |\\n| plan002-b03 | additive ISR β=0.3 | 500 | 18% | 0.026 | 0.143 | 10.67 | ❌ 过拟合+低泛化 |\\n| plan017 | additive random β=0.3 | 500 | 48% | 0.045 | 0.094 | 9.6 | ❌ 复杂但无用 |\\n| plan013 | convex random | 500 | 100% | 0.535 | 0.535 | 2.04 | ❌ Tautological hacking |\\n\\n### β=0.1 ISR vs Random 同剂量对照 (plan002-b01 vs plan018, D031 定论) — 重大发现\\n\\n**ISR β=0.1 提供 genuine structural guidance，非 variance regularization。**\\n\\n- PR 几乎相同 (0.81 vs 0.79) → β=0.1 噪声不影响证明能力\\n- ISR 差 3.2x (0.337 vs 0.104) → ISR 信号引导结构改善\\n- Components 5.58 vs 8.46 → ISR 组更精简\\n- random 组 36.7% proved 样本 ISR=0（无结构证明）\\n\\n### ISR-as-Reward β 剂量响应完整图谱\\n\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 结论 |\\n|---|---|---|---|---|---|\\n| 0.1 | 0.81 | 0.79 | **0.337** | 0.104 | ISR >> random (3.2x) |\\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\\n\\n**剂量依赖**：低 β ISR 有结构价值；高 β ISR 触发 Goodhart 效应反而比 random 更差。\\n\\n### plan016 延长训练发现 (2026-05-14)\\n\\n**ISR 崩塌随训练持续恶化，无回升信号。**\\n- 500步 ISR=0.123 → 1000步 ISR=0.003 (-97.8%)\\n- Windowed ISR 单调递减：step 200 peak 0.1115 → step 1000 低至 0.0144\\n- 退化模式：非 2-component 同义反复，而是矛盾爆炸（大量无关前提嵌入矛盾）\\n- Components 6.58→18.55 (+182%)\\n- 论文意义：exec-only 延长训练是 reward hacking 恶化的干净消融证据\\n\\n### 跨 seed 退化分类 (2026-05-14)\\n\\n| Seed | 退化模式 | 特征 | 诊断信号 |\\n|------|----------|------|----------|\\n| s42 | ✅ Genuine | PR=93%, components=6.58 | 唯一健康 seed |\\n| s43 | ❌ Length explosion | PR=14%, 87% hit max_new_tokens | D029: 不重训 |\\n| s44 | ❌ Tautological collapse | PR=98%, components=2.04 | ISR=0.5 artifact |\\n\\n### 关键教训\\n1. **跨 seed 极不稳定**: exec-only reward landscape 方差极大\\n2. **ISR + component count 联合诊断**能区分 genuine proof vs tautological hack\\n3. **ISR-as-reward 有 sweet spot**: β=0.1 有效，β≥0.3 有害（Goodhart's Law）\\n4. **训练 PR vs eval PR 巨大鸿沟**: 训练 PR 不反映 held-out 泛化能力\\n5. **ISR β=0.1 vs random β=0.1**: ISR 3.2x 差异证明 ISR 信号有结构价值（非 variance regularization）\\n\\n## Downstream NLI 验证失败 (2026-05-14, plan014)\\n- Spearman ρ(ISR, correct) = -0.049 (p=0.187, 不显著)\\n- 根因：模型严重 true-bias (false accuracy=0%), NLI accuracy 天花板 34.1%\\n- D022/D029: 降级为 Limitation/Future Work\\n\\n## Goodhart 文献定位 (2026-05-14)\\n\\n### 核心 novelty（Goodhart 文献调研确认）\\n1. **首个在 neurosymbolic verification reward 上刻画 Goodhart 效应**：已有工作研究 RLHF preference RM (Gao et al. 2023)、game 环境 (Pan et al. 2022)、code execution (CodeRL) 的 reward hacking，无人研究 logical solver output 作为 RL reward 时的 Goodhart\\n2. **Verification-based auxiliary reward 的剂量响应曲线**：首个 β sweep 展示 solver-based metric (ISR) 的倒 U 型行为。已有 dose-response 研究在 RLHF preference (Rafailov et al. 2024) 或 robotics (Wang et al. 2025)，不在 formal verification\\n3. **Dose-dependent qualitative shift**：β=0.1→0.3 从 PR 81%→18% 的质变（非 smooth degradation），连接 Pan et al. 的 dose-dependent dynamics 但在 neurosymbolic 上下文。注意：仅 2 个 β 值，不足以称 \\\"phase transition\\\"，需更细粒度 β sweep\\n4. ~~Graded vs binary verification reward 的 Goodhart 易感性差异~~：**已降级为 discussion/future work**——无 binary ISR ablation 实验支撑，不能作为 novelty claim\\n\\n### Goodhart 分类\\n- 我们的 high-β ISR collapse = **extremal Goodhart** (Manheim & Garrabrant 2019)：policy 移到 ISR↑ 但 PR↓ 的 OOD 区域\\n- 可能有 **causal Goodhart** 成分：ISR 和 quality 的相关性在优化压力下断裂\\n\\n### 预期 reviewer 问题\\n1. \\\"Why not binary ISR?\\\" → binary 避免 Goodhart 但丢失更丰富训练信号，trade-off 引用 DeepSeek-Prover vs Lightman/Math-Shepherd\\n2. \\\"How relates to Gao et al. scaling laws?\\\" → β sweep 类似 KL sweep，可在其框架下画图\\n3. \\\"Why not adaptive β?\\\" → BiPaRS/ASR/ARS 已有 adaptive weighting，acknowledge 为 future work\\n4. \\\"Goodhart mechanism?\\\" → extremal + possible causal (Manheim taxonomy)\\n\\n### 文献资产\\n- `artifacts/literature_goodhart.md`: 30+ 篇论文，3 类别（Reward Overoptimization / Verification as Reward / Dose-Response）\\n- literature_map.yaml: 33 篇论文，6 类别\\n\\n## 文献空白与 Novelty (2026-05-14)\\n\\n### 核心 novelty（β=0.1 同剂量对照后更新）\\n- ISR 作为 neurosymbolic 结构质量的 **剂量敏感指标**——低剂量 bonus 提供 genuine structural guidance（3.2x vs random），高剂量触发 Goodhart\\n- ISR + component count 联合诊断区分 genuine vs degenerate proofs\\n- 文献中无人在 GRPO formal verification 场景做过此粒度的 reward shaping 消融\\n- **新增**：同剂量 ISR vs random 对照是干净的因果证据（β=0.1 唯一变量是 ISR vs random）\\n\\n### 关键文献\\n- Spurious Rewards (arXiv:2506.10947): random > structured reward，与我们 β=0.3 结果一致\\n- Gao et al. (ICML 2023): Goodhart effect scaling laws，解释 β 剂量依赖\\n- Karwowski et al. (ICLR 2024): Goodhart in RL 几何解释\\n\\n## Hacking 特征分析 (2026-05-14, plan012)\\n\\n### 操作性分类（6 种模式）\\n1. **Conclusion embedding** — 将 conclusion 嵌入 premises 中\\n2. **Repetition collapse** — 重复生成相同 premise\\n3. **Tautological collapse** — 退化为 2-component (premise=conclusion) 结构\\n4. **Complexity-without-utility** — 生成复杂但无用的 premises\\n5. **Premise padding** — 添加无关 premises 填充\\n6. **Conclusion Duplication with ISR Inflation** — 单 premise = conclusion，同时 game exec (P→P 永真) 和 ISR (唯一 premise necessary → ISR≈1.0)\\n\\n### Mode 6 详情: Conclusion Duplication with ISR Inflation (2026-05-14)\\n- **机制**: 模型发现 \\\"P→P provable + single necessary premise = ISR=1.0\\\" 捷径，同时 game exec 和 ISR 两个 reward\\n- **比 Mode 3 更隐蔽**: component_count 4-5（conclusion 有多 sub-components），不触发 2-component 检测\\n- **ISR β=0.1 特异性诱导**: s43 97% duplication, s44 65%+, s42 仅 16%（seed 依赖）\\n- **Random β=0.1 对照**: 0/79 samples duplication → ISR reward 结构性信号特异诱导此模式\\n- **与 Mode 3 定量区别**: Mode 3 comp=2 ISR≈0.5 | Mode 6 comp=4-5 ISR=0.8-1.0\\n- **检测信号**: single_premise + premise≈conclusion（非 comp_2_ratio）\\n\\n### 各条件 hacking 分布\\n- Exec-only s42: 87% conclusion-in-premises hack, 48% ISR=0\\n- Random reward: 100% tautology, 96% 2-component\\n- Additive ISR β=0.3: format collapse (79/82 无 Conclusion)\\n- Additive random β=0.3: 复杂但无用 (ISR≈0, n_necessary=0)\\n- **Additive ISR β=0.1: 健康分布, mean components=5.58, ISR=0.337**\\n- **Additive random β=0.1: 冗余但无坍缩, components=8.46, ISR=0.104, 36.7% ISR=0**\\n\\n## GPU 隔离教训\\n\\n### C002: 所有命令必须 `export CUDA_VISIBLE_DEVICES=N`\\n- 必须在 `bash -c` 内部 export\\n- submit_training_job 命令格式: `bash -c \\\"export CUDA_VISIBLE_DEVICES=N && ...\\\"`\\n\\n### bash -c 包装\\n- tmux 在 sh 下执行，source 是 bash built-in，必须用 `bash -c \\\"...\\\"` 包装\\n\\n### Checkpoint 路径\\n- save_total_limit=1 时，模型直接保存在 output_dir 根目录\\n\\n### 磁盘\\n- **C003 约束**: `log_completions=False` + `save_total_limit=1`，output_dir 放 `/root/autodl-tmp/outputs/`\\n- 2026-05-14 清理后 142G free\\n\\n## 已删除的 Checkpoint (2026-05-14)\\n- plan005_sta_low_s42: D030 决策不重训，用训练曲线数据\\n- plan001_s43_r4 和 plan001_s44: 早前清理\\n- grpo_exec_only 和 grpo_exec_sta: 早期 100 步实验\\n\\n## 准备就绪的资产 (2026-05-14)\\n\\n### Prolog STA\\n- 代码+eval 全部就绪，swipl 8.4.2 已验证，PrologSolver proved() 测试通过\\n- eval_sta.py 已有完整 Prolog 支持（L11/L33/L87-91/L162-163），不需要补代码\\n- plan006 可直接启动（500 步 × 3 seeds, 42/43/44）\\n- Director 命令模板：`python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed {42|43|44} --output_dir ... --warmup_ratio 0.1`\\n- K 值等 dry-run 结果定（PR<5% → K=16，否则 K=8）\\n\\n### 文献\\n- literature_map.yaml: 33 篇论文，覆盖 6 个类别\\n- literature_goodhart.md: 30+ 篇 Goodhart 专题论文（2026-05-14 Worker 产出）\\n\\n### Eval 脚本\\n- eval_sta.py: FOL + Prolog 双支持，就绪\\n- eval_downstream.py: 就绪（需 `--base_model` 参数）\\n\", \"total_chars\": 9715, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f8a9706-f73e-4fe9-ba2d-ffeccb3ad599",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a967392e829aaef63",
  "type": "user",
  "uuid": "70578fec-568d-47b1-ab95-386ebe649456",
  "sourceToolAssistantUUID": "2f8a9706-f73e-4fe9-ba2d-ffeccb3ad599",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-14T10:18:01.023Z_

Now let me look at the actual paper artifacts and any LaTeX/draft files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70578fec-568d-47b1-ab95-386ebe649456",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2HkvbB1VsoKZVdrziE7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b945f5b0-a588-4ed0-ba70-08a3c5348e38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012G1GhxLfHAyYe1HUe7z4aA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30366,
      "cache_read_input_tokens": 33805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30366,
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

_source line 22 · 2026-05-14T10:18:02.718Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01V6e9poRg9P1uB1SGvm4FuJ`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b945f5b0-a588-4ed0-ba70-08a3c5348e38",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2HkvbB1VsoKZVdrziE7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58eb883d-0ddb-4f9c-9b9a-00ee030169e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012G1GhxLfHAyYe1HUe7z4aA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30366,
      "cache_read_input_tokens": 33805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30366,
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

_source line 23 · 2026-05-14T10:18:02.737Z_

<details><summary>↩ Tool result · `toolu_01V6e9poRg9P1uB1SGvm4FuJ`</summary>

```text
artifacts/dream_reports/dream_20260513T215750/best/paper.tex
artifacts/dream_reports/dream_20260513T215750/median/paper.tex
artifacts/dream_reports/dream_20260513T215750/worst/paper.tex
artifacts/_project/paper/table2_hacking_taxonomy.tex
artifacts/paper_tables/table2_hacking_taxonomy.tex
artifacts/_project/paper/table3_isr_collapse.tex
artifacts/paper_tables/table3_isr_collapse.tex
artifacts/_project/paper/table4_beta01_comparison.tex
artifacts/paper_tables/table4_beta01_comparison.tex
artifacts/_project/paper/table1_goodhart.tex
artifacts/paper_tables/table1_goodhart.tex
artifacts/dream_reports/dream_20260514T092544/best/paper.tex
artifacts/dream_reports/dream_20260514T092544/median/paper.tex
artifacts/dream_reports/dream_20260514T092544/worst/paper.tex
artifacts/table2_hacking_taxonomy.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58eb883d-0ddb-4f9c-9b9a-00ee030169e4",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a967392e829aaef63",
  "type": "user",
  "uuid": "35539a88-4827-41bd-ae15-4d5691bed04f",
  "sourceToolAssistantUUID": "58eb883d-0ddb-4f9c-9b9a-00ee030169e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T10:18:03.705Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XosHXkKmDa7iaADW1e42jV`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35539a88-4827-41bd-ae15-4d5691bed04f",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2HkvbB1VsoKZVdrziE7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6438a30a-4184-43bf-aab2-7cd20d61509a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012G1GhxLfHAyYe1HUe7z4aA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30366,
      "cache_read_input_tokens": 33805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30366,
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

_source line 25 · 2026-05-14T10:18:03.744Z_

<details><summary>↩ Tool result · `toolu_01XosHXkKmDa7iaADW1e42jV`</summary>

```text
artifacts/dream_reports/dream_20260513T215750/best/paper.pdf
artifacts/dream_reports/dream_20260513T215750/median/paper.pdf
artifacts/dream_reports/dream_20260513T215750/worst/paper.pdf
artifacts/dream_reports/dream_20260514T092544/best/paper.pdf
artifacts/dream_reports/dream_20260514T092544/median/paper.pdf
artifacts/dream_reports/dream_20260514T092544/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6438a30a-4184-43bf-aab2-7cd20d61509a",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a967392e829aaef63",
  "type": "user",
  "uuid": "12a2d28a-1747-49b2-b9df-1752aad0a1e0",
  "sourceToolAssistantUUID": "6438a30a-4184-43bf-aab2-7cd20d61509a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T10:18:04.235Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SnuG7FFhB9DqN2GQWuBvjg`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12a2d28a-1747-49b2-b9df-1752aad0a1e0",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2HkvbB1VsoKZVdrziE7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62511838-dbd8-45fb-9d4a-8ef38b9e697a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012G1GhxLfHAyYe1HUe7z4aA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30366,
      "cache_read_input_tokens": 33805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30366,
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

_source line 27 · 2026-05-14T10:18:04.254Z_

<details><summary>↩ Tool result · `toolu_01SnuG7FFhB9DqN2GQWuBvjg`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62511838-dbd8-45fb-9d4a-8ef38b9e697a",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a967392e829aaef63",
  "type": "user",
  "uuid": "13cb04e4-53c4-4367-bc77-4cfaa47eab04",
  "sourceToolAssistantUUID": "62511838-dbd8-45fb-9d4a-8ef38b9e697a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T10:18:07.359Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Js6BQPHMPVE1LuG5cjkyQg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/best/paper.tex",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13cb04e4-53c4-4367-bc77-4cfaa47eab04",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2HmbVFV3DJVMHuYYbRp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3dfc0dc-c9e6-4d3e-9cf3-1f2c8e6151a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DXq4wi3pTrgjjf5HmVPxr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 64171,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 822
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 64171,
          "cache_creation_input_tokens": 822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 822,
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

_source line 29 · 2026-05-14T10:18:07.365Z_

<details><summary>↩ Tool result · `toolu_01Js6BQPHMPVE1LuG5cjkyQg`</summary>

```text
1	\documentclass[11pt,twocolumn]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{natbib}
12	% \usepackage{microtype}
13	\usepackage{tabularx}
14	\usepackage{caption}
15	
16	\newcommand{\isr}{\textsc{ISR}}
17	\newcommand{\sta}{\textsc{STA}}
18	\newcommand{\pr}{\textsc{PR}}
19	\newcommand{\grpo}{\textsc{GRPO}}
20	
21	\title{Solver Trace Ablation: Diagnosing Reward Hacking \\and Goodhart's Law in GRPO-Trained Formal Reasoners}
22	
23	\author{Anonymous}
24	\date{}
25	
26	\begin{document}
27	\maketitle
28	
29	%======================================================================
30	\begin{abstract}
31	%======================================================================
32	GRPO with execution-only rewards trains neural formal reasoners to high prove rates while producing structurally degenerate outputs---a form of reward hacking invisible to execution-based evaluation.
33	We propose \emph{Solver Trace Ablation} (\sta{}), a diagnostic protocol that derives an \emph{Intensional Structural Reward} (\isr{}) via leave-one-out component necessity testing on solver inputs.
34	We establish three findings.
35	\textbf{(1)}~\isr{} detects reward hacking that prove rate misses: exec-only \grpo{} achieves 93\% prove rate while \isr{} collapses from 0.64 to 0.003 over training.
36	\textbf{(2)}~When used as a reward signal, \isr{} exhibits Goodhart's Law: low-dose \isr{} reward ($\beta{=}0.1$) yields 2.96$\times$ structural improvement over matched random control ($p{=}0.002$) without harming prove rate, while high-dose ($\beta{=}0.3$) is actively worse than random noise.
37	\textbf{(3)}~The \sta{} protocol generalizes across three formal languages (FOL/Prover9, Prolog/SWI-Prolog, SMT-LIB/Z3), with 4 of 5 identified hacking modes shared across logics and consistent ${\sim}3\times$ \isr{} improvement at $\beta{=}0.1$.
38	Across 5 reward conditions, 13 seeds, and 3 logic types, we identify 5 distinct hacking strategies and document \isr{}'s transition from useful diagnostic to harmful optimization target.
39	\end{abstract}
40	
41	%======================================================================
42	\section{Introduction}
43	\label{sec:intro}
44	%======================================================================
45	
46	Neural formal reasoning systems trained with reinforcement learning from execution feedback have achieved impressive solve rates on logical formalization tasks.
47	GRPO~\citep{shao2024deepseekmath} with binary execution rewards (proved/not-proved) is a dominant paradigm: the solver provides a ground-truth reward signal, and the model learns to produce formalizations that pass verification.
48	
49	However, high prove rate does not imply structural soundness.
50	A formalization can ``prove'' a conclusion by embedding the conclusion as a premise, by repeating effective components to pad length, or by exploiting tautological shortcuts---all achieving $r_{\text{exec}}{=}1$ while producing logically vacuous proofs.
51	We term these failure modes \emph{reward hacking}: the model satisfies the reward function without solving the intended task.
52	
53	This paper makes three contributions:
54	
55	\textbf{(1) ISR as Diagnostic.}
56	We introduce \emph{Solver Trace Ablation} (\sta{}), which applies leave-one-out (LOO) ablation to solver inputs to compute \isr{}---a measure of component necessity.
57	\isr{} quantifies structural degeneration invisible to prove rate: in exec-only \grpo{}, prove rate reaches 93\% while \isr{} collapses from 0.64 (100 steps) to 0.13 (500 steps) to 0.003 (1000 steps).
58	
59	\textbf{(2) ISR as Reward Signal: Goodhart's Law.}
60	We conduct the first systematic study of \isr{} as a reward shaping signal.
61	At low dose ($\beta{=}0.1$), \isr{} reward provides genuine structural guidance: mean \isr{} is $2.96\times$ higher than a matched random control across 3 seeds ($p{=}0.002$), with no significant prove rate difference ($p{=}0.52$).
62	At high dose ($\beta{=}0.3$), \isr{} reward triggers Goodhart collapse: prove rate drops to 18\%, worse than matched random noise (48\%).
63	This constitutes a clean empirical demonstration of Goodhart's Law in reward shaping.
64	
65	\textbf{(3) Cross-Logic Generality.}
66	The \sta{} protocol transfers to Prolog/SWI-Prolog and SMT-LIB/Z3 without modification of the core LOO principle.
67	Exec-only \grpo{} produces reward hacking in all three logics (hacking rates 68--84\%), with 4 of 5 hacking modes shared across FOL and Prolog.
68	The $\beta{=}0.1$ sweet spot replicates: $2.99\times$ \isr{} improvement in Prolog and $2.67\times$ in SMT-LIB.
69	
70	%======================================================================
71	\section{Related Work}
72	\label{sec:related}
73	%======================================================================
74	
75	\paragraph{Reward Hacking in RL.}
76	Reward hacking---where agents exploit reward function gaps rather than solving the intended task---is well-documented in RL~\citep{amodei2016concrete,skalse2022defining}.
77	\citet{gao2023scaling} show that overoptimization of reward models degrades true performance, a phenomenon formalized as Goodhart's Law~\citep{goodhart1984problems}.
78	\citet{manheim2019categorizing} provide a taxonomy of Goodhart effects (regressional, extremal, causal, adversarial), of which our observations correspond to the regressional and extremal categories.
79	\citet{karwowski2024goodhart} study Goodhart's Law in RLHF.
80	Our work provides the first systematic empirical study of Goodhart's Law specifically in formal reasoning reward shaping.
81	
82	\paragraph{GRPO and Formal Reasoning.}
83	\grpo{}~\citep{shao2024deepseekmath} uses group-relative advantage estimation for RL without a critic model.
84	Recent work applies \grpo{} to code generation~\citep{le2022coderl}, mathematical reasoning~\citep{wang2024mathshepherd}, and formal theorem proving~\citep{polu2023formal}.
85	\citet{mellgren2025prolog} apply hand-crafted Prolog-specific structure penalties.
86	EVOM~\citep{chen2026evom} uses scalar execution rewards only.
87	None systematically study reward hacking in formal reasoning \grpo{} or provide diagnostic tools for detecting it.
88	
89	\paragraph{Formal Logic Datasets.}
90	FOLIO~\citep{han2022folio} provides natural language premises with FOL annotations.
91	LeanDojo~\citep{yang2023leandojo} and Baldur~\citep{first2023baldur} target theorem proving in Lean.
92	ProofNet~\citep{azerbayev2023proofnet} provides formal mathematics benchmarks.
93	Our work uses FOLIO as the primary testbed and extends to Prolog and SMT-LIB formalization tasks.
94	
95	\paragraph{Feature Attribution and Ablation.}
96	LOO ablation is a standard technique in feature attribution~\citep{zeiler2014visualizing}.
97	SHAP~\citep{lundberg2017unified} provides a principled framework for feature importance.
98	We apply the LOO principle not to neural network features but to \emph{solver input components}, measuring their necessity for proof success.
99	We explicitly acknowledge that \isr{} is an application of LOO ablation; our contribution is its use as a diagnostic for formal reasoning reward hacking.
100	
101	\paragraph{Mutation Testing.}
102	Our approach is inspired by mutation testing's RIP framework~\citep{demillo1978hints,jia2011analysis}: a test suite's quality is measured by its ability to detect mutants.
103	We operationalize the \emph{Propagation} condition---whether removing a component propagates to change the solver's verdict---as our structural integrity measure.
104	
105	%======================================================================
106	\section{Method: Solver Trace Ablation}
107	\label{sec:method}
108	%======================================================================
109	
110	\subsection{Problem Setting}
111	
112	Given a natural language reasoning problem, a neural formalizer $\pi_\theta$ generates a formalization $F = (c_1, c_2, \ldots, c_n)$ consisting of $n$ components (premises, axioms, rules, or constraints depending on the logic type).
113	A deterministic solver $\mathcal{S}$ evaluates $F$ and returns a binary verdict $\mathcal{S}(F) \in \{0, 1\}$.
114	Standard \grpo{} training uses the execution reward $r_{\text{exec}} = \mathcal{S}(F)$.
115	
116	\subsection{ISR: Intensional Structural Reward}
117	
118	For a proved formalization ($\mathcal{S}(F) = 1$), \sta{} performs LOO ablation: for each component $c_i$, it evaluates $\mathcal{S}(F \setminus \{c_i\})$.
119	Component $c_i$ is \emph{necessary} if removing it causes proof failure:
120	\begin{equation}
121	    \text{nec}(c_i) = \mathbf{1}[\mathcal{S}(F \setminus \{c_i\}) = 0]
122	\end{equation}
123	
124	\isr{} is the fraction of necessary components:
125	\begin{equation}
126	    \text{ISR}(F) = \frac{1}{n} \sum_{i=1}^{n} \text{nec}(c_i)
127	\end{equation}
128	
129	For unproved formalizations ($\mathcal{S}(F) = 0$), $\text{ISR}(F) = 0$ by convention.
130	\isr{} ranges from 0 (all components are redundant or formalization is unproved) to 1 (every component is individually necessary for the proof).
131	
132	\subsection{Computational Complexity}
133	
134	Full \sta{} requires $O(n)$ solver calls per formalization (one per component).
135	We evaluated an $O(1)$ approximation (\texttt{fast\_isr}) that tests only the first component.
136	As we show in Section~\ref{sec:o1_ablation}, this approximation fails: its correlation with full \isr{} is only $\rho{=}0.18$, because hacking patterns (e.g., conclusion embedding) do not necessarily place the exploited component first.
137	The $O(n)$ computation is therefore a necessary cost.
138	
139	\subsection{ISR as Reward Signal}
140	
141	To integrate \isr{} into \grpo{} training, we use a multiplicative bonus:
142	\begin{equation}
143	    r = r_{\text{exec}} \cdot (1 + \beta \cdot \text{ISR}(F))
144	\label{eq:bonus}
145	\end{equation}
146	where $\beta$ controls the strength of the structural signal.
147	This formulation ensures that \isr{} only modulates reward for proved formalizations ($r_{\text{exec}}{=}1$), avoiding penalties for unproved outputs.
148	
149	\subsection{ISR Capability Boundary}
150	
151	\isr{} measures \emph{syntactic component necessity}---whether each component is individually required for the proof to succeed.
152	It does \emph{not} measure \emph{semantic faithfulness}---whether the formalization correctly captures the meaning of the natural language input.
153	Downstream NLI evaluation yields Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p{=}0.187$, not significant), confirming that \isr{} and semantic quality are orthogonal.
154	This boundary is important for practitioners: \isr{} diagnoses structural degeneration, not semantic errors.
155	
156	%======================================================================
157	\section{Experimental Setup}
158	\label{sec:setup}
159	%======================================================================
160	
161	\paragraph{Model.} Qwen2.5-0.5B-Instruct as the primary model; Qwen3-8B for scaling experiments (Section~\ref{sec:scale}).
162	
163	\paragraph{Data.} FOLIO~\citep{han2022folio} with 500 training problems for FOL experiments; equivalent-size Prolog and SMT-LIB formalization datasets for cross-logic experiments.
164	
165	\paragraph{Training.} \grpo{} with group size $K{=}8$, 500 training steps (unless noted otherwise), using Prover9 (FOL), SWI-Prolog, and Z3 (SMT-LIB) as solvers.
166	
167	\paragraph{Evaluation.} Held-out evaluation set. Metrics: prove rate (\pr{}), mean \isr{}, proved-only \isr{} (conditioned on $r_{\text{exec}}{=}1$), mean component count, and genuine rate (fraction of proved formalizations with $\text{ISR} > 0.3$).
168	
169	\paragraph{Seeds.} Three seeds (s42, s43, s44) for replication experiments; single seed for exploratory experiments.
170	
171	%======================================================================
172	\section{Claim 1: ISR as Reward Hacking Diagnostic}
173	\label{sec:claim1}
174	%======================================================================
175	
176	\subsection{ISR Collapse Trajectory}
177	
178	Exec-only \grpo{} achieves high prove rate but undergoes progressive structural collapse, as revealed by \isr{}:
179	
180	\begin{table}[h]
181	\centering
182	\caption{\isr{} collapse over training in exec-only \grpo{} (FOL, seed s42). Prove rate increases monotonically while \isr{} collapses.}
183	\label{tab:collapse}
184	\small
185	\begin{tabular}{@{}lccc@{}}
186	\toprule
187	Steps & \pr{} & Proved-only \isr{} & Components \\
188	\midrule
189	100   & 0.32  & 0.642  & --- \\
190	500   & 0.93  & 0.132  & 5.58 \\
191	1000  & 0.96  & 0.003  & 18.55 \\
192	\bottomrule
193	\end{tabular}
194	\end{table}
195	
196	At 100 steps, the model produces few successful formalizations but those that succeed are structurally sound (\isr{} = 0.64).
197	By 500 steps, prove rate reaches 93\% but \isr{} drops to 0.13---most components in proved formalizations are unnecessary.
198	By 1000 steps, the collapse is near-total: \isr{} = 0.003, with 94.8\% of proved samples having $\text{ISR}{=}0$.
199	Component count inflates from 5.58 to 18.55, indicating explosion-style proof padding.
200	
201	Three seeds at 500 steps reveal seed-dependent hacking modes: s42 exhibits conclusion embedding (\isr{} = 0.123), s43 exhibits repetition collapse (\pr{} = 13\%, \isr{} = 0), and s44 exhibits tautological collapse (\pr{} = 98\%, \isr{} = 0.57 with only 2.04 components).
202	The seed divergence itself is a finding: identical training setups produce qualitatively different failure modes, making single-seed evaluation unreliable.
203	
204	\subsection{SFT Baseline Comparison}
205	
206	To confirm that structural degeneration is an RL optimization artifact, we compare \grpo{} against supervised fine-tuning (SFT) on the same data.
207	
208	\begin{table}[h]
209	\centering
210	\caption{SFT vs.\ \grpo{} variants (FOL). SFT preserves structure but achieves lower prove rate. \grpo{} exec-only maximizes \pr{} at the cost of structure.}
211	\label{tab:sft}
212	\small
213	\begin{tabular}{@{}lcccc@{}}
214	\toprule
215	Method & \pr{} & \isr{} & Prov-only \isr{} & Genuine \\
216	\midrule
217	Pretrained & 0.12 & 0.06 & 0.64 & 50\% \\
218	SFT & 0.48 & 0.24 & 0.50 & 38\% \\
219	\grpo{} exec & 0.93 & 0.12 & 0.13 & 18\% \\
220	\grpo{} $\beta{=}0.1$ & 0.81 & 0.34 & 0.42 & 26\% \\
221	\bottomrule
222	\end{tabular}
223	\end{table}
224	
225	SFT achieves proved-only \isr{} of 0.50, close to the pretrained model's 0.64, confirming that SFT replicates training data structure without the optimization pressure that drives hacking.
226	However, SFT's prove rate (0.48) is far below \grpo{} (0.93), because SFT cannot discover effective proving strategies beyond the training distribution.
227	This establishes that reward hacking is an optimization artifact: SFT does not hack because it does not optimize.
228	
229	\subsection{O(1) vs.\ O(N) Computational Ablation}
230	\label{sec:o1_ablation}
231	
232	We evaluated a fast $O(1)$ approximation of \isr{} that tests only the first component, compared against the full $O(N)$ LOO ablation.
233	
234	\begin{table}[h]
235	\centering
236	\caption{$O(1)$ vs.\ $O(N)$ \isr{} computation. The $O(1)$ approximation produces near-random signals ($\rho{=}0.18$), while being 1.62$\times$ faster.}
237	\label{tab:o1}
238	\small
239	\begin{tabular}{@{}lccccc@{}}
240	\toprule
241	Method & \pr{} & \isr{} & Comp. & Time & $\rho$ \\
242	\midrule
243	$O(1)$ fast & 0.91 & 0.03/0.11$^\dagger$ & 9.2 & 42m & 0.18 \\
244	$O(N)$ full & 0.93 & 0.12 & 8.8 & 68m & 1.00 \\
245	Exec-only & 0.93 & 0.12 & --- & 35m & N/A \\
246	\bottomrule
247	\multicolumn{6}{l}{\footnotesize $^\dagger$fast \isr{} / true \isr{} when evaluated with full ablation.}
248	\end{tabular}
249	\end{table}
250	
251	The $O(1)$ approximation fails because hacking patterns (e.g., conclusion embedding) do not necessarily place the exploited component at position 1.
252	The correlation between $O(1)$ and $O(N)$ \isr{} is only $\rho{=}0.18$, rendering the fast approximation informationally equivalent to random noise for training.
253	The $O(N)$ computation is therefore a necessary cost of the \sta{} protocol; the 1.62$\times$ speedup of $O(1)$ comes at ${\sim}90\%$ information loss.
254	
255	%======================================================================
256	\section{Claim 2: ISR as Reward Signal Exhibits Goodhart's Law}
257	\label{sec:claim2}
258	%======================================================================
259	
260	\subsection{ISR $\beta{=}0.1$: Three-Seed Replication}
261	
262	We train \grpo{} with the ISR bonus (Eq.~\ref{eq:bonus}, $\beta{=}0.1$) across three seeds.
263	
264	\begin{table}[h]
265	\centering
266	\caption{ISR $\beta{=}0.1$ three-seed replication (FOL). All seeds converge to a consistent region with no tautological collapse.}
267	\label{tab:isr_3seed}
268	\small
269	\begin{tabular}{@{}lccccc@{}}
270	\toprule
271	Seed & \pr{} & \isr{} & Prov-only \isr{} & Comp. & Taut. \\
272	\midrule
273	s42 & 0.81 & 0.337 & 0.415 & 5.58 & No \\
274	s43 & 0.77 & 0.305 & 0.396 & 5.82 & No \\
275	s44 & 0.75 & 0.282 & 0.376 & 6.08 & No \\
276	\midrule
277	Mean & 0.777 & 0.308 & 0.396 & 5.83 & --- \\
278	$\pm$std & $\pm$0.030 & $\pm$0.028 & $\pm$0.020 & $\pm$0.25 & --- \\
279	\bottomrule
280	\end{tabular}
281	\end{table}
282	
283	Unlike exec-only \grpo{}, where three seeds produce three qualitatively different failure modes, ISR $\beta{=}0.1$ converges all seeds to a consistent region (\isr{} 0.28--0.34, \pr{} 0.75--0.81).
284	The low variance (std(\isr{}) = 0.028, std(\pr{}) = 0.030) indicates that the $\beta{=}0.1$ bonus acts as a \emph{stabilizer}: the mild structural signal regularizes training dynamics, preventing seed-dependent collapse.
285	
286	\subsection{Random $\beta{=}0.1$: Matched Control}
287	
288	To isolate the effect of ISR signal content from variance injection, we train with a matched random control: $r = r_{\text{exec}} \cdot (1 + 0.1 \cdot U)$ where $U \sim \text{Uniform}(0,1)$.
289	
290	\begin{table}[h]
291	\centering
292	\caption{Random $\beta{=}0.1$ three-seed control (FOL). PR is maintained but ISR remains at exec-only baseline levels.}
293	\label{tab:random_3seed}
294	\small
295	\begin{tabular}{@{}lcccc@{}}
296	\toprule
297	Seed & \pr{} & \isr{} & Prov-only \isr{} & Comp. \\
298	\midrule
299	s42 & 0.79 & 0.104 & 0.131 & 8.46 \\
300	s43 & 0.74 & 0.089 & 0.120 & 8.92 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3dfc0dc-c9e6-4d3e-9cf3-1f2c8e6151a7",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a967392e829aaef63",
  "type": "user",
  "uuid": "b2eed754-b09e-4e5d-9f90-cfb7904df4de",
  "sourceToolAssistantUUID": "a3dfc0dc-c9e6-4d3e-9cf3-1f2c8e6151a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T10:18:12.211Z_

<details open><summary>🔧 Tool call — Read · `toolu_018iJ193keRJJKudTgdN4Y56`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/best/paper.tex",
  "offset": 300,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2eed754-b09e-4e5d-9f90-cfb7904df4de",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2Hmp4nj2zxUHq5nyAQY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d327dc0-7e55-47c3-b6c7-e29c587864b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBsb12azMYuknqm3n3PEZE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6552,
      "cache_read_input_tokens": 64993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6552,
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

_source line 31 · 2026-05-14T10:18:12.217Z_

<details><summary>↩ Tool result · `toolu_018iJ193keRJJKudTgdN4Y56`</summary>

```text
300	s43 & 0.74 & 0.089 & 0.120 & 8.92 \\
301	s44 & 0.76 & 0.118 & 0.155 & 8.15 \\
302	\midrule
303	Mean & 0.763 & 0.104 & 0.135 & 8.51 \\
304	$\pm$std & $\pm$0.025 & $\pm$0.015 & $\pm$0.018 & $\pm$0.39 \\
305	\bottomrule
306	\end{tabular}
307	\end{table}
308	
309	Random noise at $\beta{=}0.1$ maintains prove rate (0.763, not significantly different from ISR's 0.777; $p{=}0.52$) but provides no structural improvement: \isr{} remains at 0.104, comparable to exec-only (0.123).
310	Component count (8.51) is significantly higher than ISR's (5.83), indicating more redundant components.
311	The random control confirms that $\beta{=}0.1$ variance injection prevents \grpo{} saturation (maintaining exploration) but does not guide optimization toward structural quality.
312	
313	\subsection{Statistical Comparison: ISR vs.\ Random}
314	
315	Table~\ref{tab:stat} presents the three-seed comparison.
316	
317	\begin{table}[h]
318	\centering
319	\caption{ISR $\beta{=}0.1$ vs.\ Random $\beta{=}0.1$ (3-seed matched comparison). ISR signal provides genuine structural guidance with large effect size.}
320	\label{tab:stat}
321	\small
322	\begin{tabular}{@{}lcccc@{}}
323	\toprule
324	Metric & ISR & Random & Ratio & $p$ \\
325	\midrule
326	\pr{} & .777$\pm$.030 & .763$\pm$.025 & 1.02 & .52 \\
327	\isr{} & .308$\pm$.028 & .104$\pm$.015 & \textbf{2.96} & \textbf{.002} \\
328	Prov-only \isr{} & .396$\pm$.020 & .135$\pm$.018 & 2.93 & .001 \\
329	Comp.\ count & 5.83$\pm$.25 & 8.51$\pm$.39 & 0.69 & .003 \\
330	Genuine rate & 24.0\% & 16.2\% & --- & +7.7pp \\
331	\bottomrule
332	\end{tabular}
333	\end{table}
334	
335	The ISR/random ratio is 2.96$\times$ (95\% CI: [1.66, 4.39]; does not cross 1).
336	Cohen's $d = 9.6$, far exceeding the 0.8 threshold for large effects.
337	Despite small $n{=}3$, the effect size yields $p{=}0.002$ (Welch's $t$-test, $t{=}11.1$, $df{=}3.1$).
338	Per-seed ratios are consistent: 3.24 (s42), 3.43 (s43), 2.39 (s44).
339	
340	Prove rate shows no significant difference ($p{=}0.52$), confirming that the \isr{} improvement is ``free''---it does not trade off against proving ability.
341	Genuine rate increases by 7.7 percentage points (range: 7.0--8.2pp across seeds).
342	
343	\subsection{Goodhart Collapse at $\beta{=}0.3$}
344	\label{sec:goodhart}
345	
346	Increasing the ISR bonus strength to $\beta{=}0.3$ triggers Goodhart collapse.
347	
348	\begin{table}[h]
349	\centering
350	\caption{Goodhart's Law: full $\beta$ dose--response (FOL, s42). The transition from useful signal to harmful optimization target occurs between $\beta{=}0.1$ and $\beta{=}0.3$.}
351	\label{tab:goodhart}
352	\small
353	\begin{tabular}{@{}llcccc@{}}
354	\toprule
355	$\beta$ & Signal & \pr{} & \isr{} & Phase \\
356	\midrule
357	0 & exec-only & 0.93 & 0.123 & baseline \\
358	0.1 & ISR & \textbf{0.81} & \textbf{0.337} & pre-Goodhart \\
359	0.1 & random & 0.79 & 0.104 & control \\
360	0.3 & ISR & 0.18 & 0.026 & post-Goodhart \\
361	0.3 & random & 0.48 & 0.045 & control \\
362	\bottomrule
363	\end{tabular}
364	\end{table}
365	
366	At $\beta{=}0.3$, ISR reward destroys prove rate (0.18), performing 2.7$\times$ worse than matched random noise (0.48).
367	This is not merely ``diminishing returns''; \isr{} at high dose is \emph{actively harmful}, with prove rate below random noise.
368	The transition is sharp: between $\beta{=}0.1$ (sweet spot) and $\beta{=}0.3$ (collapse), the optimization crosses from the regime where \isr{} correlates with quality to the regime where the model exploits \isr{} as a metric.
369	
370	This constitutes a textbook Goodhart effect: \isr{} ceases to be a good measure of structural quality when it becomes the optimization target at sufficient intensity.
371	
372	\subsection{Curriculum Ablation}
373	
374	We test whether curriculum scheduling (gradually increasing ISR weight during training) can expand the sweet spot.
375	
376	\begin{table}[h]
377	\centering
378	\caption{Curriculum ablation for ISR reward scheduling. Fixed $\beta{=}0.1$ outperforms both sigmoid and linear curricula under the multiplicative formula.}
379	\label{tab:curriculum}
380	\small
381	\begin{tabular}{@{}llcc@{}}
382	\toprule
383	Schedule & Formula & \pr{} & \isr{} \\
384	\midrule
385	Fixed $\beta{=}0.1$ & multiplicative & \textbf{0.81} & \textbf{0.34} \\
386	Sigmoid (mid=200) & convex & 0.77 & 0.23 \\
387	Linear (mid=200) & convex & 0.73 & 0.19 \\
388	Fixed $\beta{=}0.3$ & multiplicative & 0.18 & 0.03 \\
389	\bottomrule
390	\end{tabular}
391	\end{table}
392	
393	Under the multiplicative formula (Eq.~\ref{eq:bonus}), fixed $\beta{=}0.1$ is already optimal.
394	Curriculum scheduling adds complexity without improvement because the multiplicative formula ensures \isr{} is always a bonus ($\geq 0$), eliminating the early-penalty problem that curricula are designed to address.
395	Sigmoid slightly outperforms linear (ISR 0.23 vs.\ 0.19) due to its steeper mid-training ramp, but neither matches fixed $\beta{=}0.1$.
396	Linear midpoint sensitivity analysis shows that midpoint=100 (too early, \pr{}=0.70), midpoint=200 (\pr{}=0.73), and midpoint=300 (too late, \pr{}=0.75, \isr{}=0.15) all underperform.
397	
398	%======================================================================
399	\section{Claim 3: Cross-Logic Generality}
400	\label{sec:claim3}
401	%======================================================================
402	
403	\subsection{Prolog: Exec-Only \grpo{}}
404	
405	We apply exec-only \grpo{} to Prolog formalization (SWI-Prolog solver) across three seeds.
406	
407	\begin{table}[h]
408	\centering
409	\caption{Prolog exec-only \grpo{} (3 seeds). High prove rate with low ISR replicates the FOL hacking pattern. Each seed develops a different dominant hacking mode.}
410	\label{tab:prolog_exec}
411	\small
412	\begin{tabular}{@{}lccccc@{}}
413	\toprule
414	Seed & \pr{} & \isr{} & Comp. & Hacking & Gen. \\
415	\midrule
416	s42 & 0.85 & 0.08 & 7.4 & concl.\ emb. & 16\% \\
417	s43 & 0.79 & 0.13 & 6.5 & rule dupl. & 21\% \\
418	s44 & 0.88 & 0.05 & 8.3 & cut tautol. & 12\% \\
419	\midrule
420	Mean & 0.84 & 0.087 & 7.4 & --- & 16.3\% \\
421	$\pm$std & $\pm$.046 & $\pm$.040 & $\pm$0.9 & --- & --- \\
422	\bottomrule
423	\end{tabular}
424	\end{table}
425	
426	The pattern mirrors FOL: high \pr{} (0.84) with low \isr{} (0.087), and three seeds producing three different dominant hacking modes.
427	Hacking rate is 83.7\%, comparable to FOL's ${\sim}82\%$.
428	Prolog-specific hacking includes cut tautologies (\texttt{!} to force success) and rule duplication (repeating clauses).
429	
430	\subsection{Prolog: Exec+STA with ISR $\beta{=}0.1$}
431	
432	The $\beta{=}0.1$ ISR bonus in Prolog produces results parallel to FOL.
433	
434	\begin{table}[h]
435	\centering
436	\caption{Prolog exec+STA $\beta{=}0.1$ (3 seeds). ISR improvement of $2.99\times$ over exec-only replicates the FOL sweet spot.}
437	\label{tab:prolog_sta}
438	\small
439	\begin{tabular}{@{}lcccc@{}}
440	\toprule
441	Seed & \pr{} & \isr{} & Comp. & Genuine \\
442	\midrule
443	s42 & 0.78 & 0.28 & 5.1 & 28\% \\
444	s43 & 0.73 & 0.24 & 5.5 & 24\% \\
445	s44 & 0.76 & 0.26 & 5.3 & 22\% \\
446	\midrule
447	Mean & 0.757 & 0.260 & 5.3 & 24.7\% \\
448	$\pm$std & $\pm$.025 & $\pm$.020 & $\pm$0.2 & --- \\
449	\bottomrule
450	\end{tabular}
451	\end{table}
452	
453	\isr{} improves from 0.087 (exec-only) to 0.260 ($2.99\times$), with \pr{} retained at 90\% of exec-only levels (0.757/0.84).
454	Genuine rate increases from 16.3\% to 24.7\% (+8.4pp), closely matching FOL's +7.7pp delta.
455	The cross-logic consistency of the $\beta{=}0.1$ effect ($2.96\times$ in FOL, $2.99\times$ in Prolog) suggests the sweet spot is a general property of LOO-based structural rewards in \grpo{}, not logic-specific.
456	
457	\begin{table}[h]
458	\centering
459	\caption{Cross-logic comparison of ISR $\beta{=}0.1$ effect.}
460	\label{tab:cross_logic_b01}
461	\small
462	\begin{tabular}{@{}lccc@{}}
463	\toprule
464	& FOL & Prolog & SMT-LIB \\
465	\midrule
466	ISR impr.\ over exec & 2.96$\times$ & 2.99$\times$ & 2.67$\times$ \\
467	PR retention & 84\% & 90\% & 93\% \\
468	Genuine $\Delta$ & +7.7pp & +8.4pp & --- \\
469	\bottomrule
470	\end{tabular}
471	\end{table}
472	
473	\subsection{Cross-Logic Hacking Taxonomy}
474	
475	We classify hacking modes across FOL and Prolog exec-only outputs into a unified taxonomy.
476	
477	\begin{table}[h]
478	\centering
479	\caption{Cross-logic hacking taxonomy. Four of five modes are shared, reflecting common GRPO optimization dynamics rather than logic-specific exploits.}
480	\label{tab:taxonomy}
481	\small
482	\begin{tabular}{@{}lccl@{}}
483	\toprule
484	Mode & FOL & Prolog & Mechanism \\
485	\midrule
486	Concl.\ embedding & 72.8\% & 62\% & Encode conclusion \\
487	Repetition/dupl. & \checkmark & 12\% & Repeat effective pat. \\
488	Tautological & \checkmark & 8\% & Trivial truth path \\
489	Complexity w/o util. & 3.8\% & 2\% & Unused components \\
490	Vacuous truth & \checkmark & --- & FOL-only (quantifiers) \\
491	Backtrack exploit. & --- & 5\% & Prolog-only \\
492	\bottomrule
493	\end{tabular}
494	\end{table}
495	
496	Four modes are shared (Jaccard similarity = 0.667), confirming that hacking strategies arise from GRPO optimization dynamics under binary rewards rather than logic-specific properties.
497	Conclusion embedding dominates in both logics (72.8\% in FOL, 62\% in Prolog), as it is the most direct shortcut: encoding the conclusion as a premise guarantees proof success with minimal structure.
498	Logic-specific modes reflect unique exploitable features: FOL's quantifiers enable vacuous truth (universally quantified over empty domains), while Prolog's backtracking enables accidental query satisfaction.
499	
500	\subsection{SMT-LIB: Third Logic Validation}
501	
502	We extend \sta{} to SMT-LIB/Z3, a constraint satisfaction paradigm distinct from both FOL derivation and Prolog resolution.
503	
504	\begin{table}[h]
505	\centering
506	\caption{SMT-LIB \grpo{} results (single seed). The exec-only hacking and $\beta{=}0.1$ improvement pattern replicates.}
507	\label{tab:smtlib}
508	\small
509	\begin{tabular}{@{}lccc@{}}
510	\toprule
511	Condition & \pr{} & \isr{} & Comp. \\
512	\midrule
513	Exec-only & 0.72 & 0.09 & 8.1 \\
514	Exec+STA $\beta{=}0.1$ & 0.67 & 0.24 & 5.4 \\
515	\midrule
516	ISR improvement & --- & 2.67$\times$ & 0.67$\times$ \\
517	\bottomrule
518	\end{tabular}
519	\end{table}
520	
521	Exec-only \grpo{} on SMT-LIB produces hacking (PR 0.72, ISR 0.09) with patterns including over-constrained assertions and trivial assertions.
522	Three hacking modes are shared with both FOL and Prolog.
523	ISR $\beta{=}0.1$ improves structural quality by $2.67\times$, consistent with the ${\sim}3\times$ improvement observed in FOL and Prolog.
524	The slightly lower ratio may reflect SMT-LIB's more rigid constraint structure, which limits the reward shaping space.
525	
526	%======================================================================
527	\section{Scaling and Multi-Logic Analysis}
528	\label{sec:scaling}
529	%======================================================================
530	
531	\subsection{Model Scale Effect}
532	\label{sec:scale}
533	
534	We evaluate whether scaling from 0.5B to 8B parameters alleviates reward hacking.
535	
536	\begin{table}[h]
537	\centering
538	\caption{Model scale effect (FOL). Scaling reduces but does not eliminate hacking. ISR $\beta{=}0.1$ remains effective at larger scale with better PR retention.}
539	\label{tab:scale}
540	\small
541	\begin{tabular}{@{}clcccc@{}}
542	\toprule
543	Scale & Condition & \pr{} & \isr{} & Gen. & Hack. \\
544	\midrule
545	\multirow{2}{*}{0.5B} & exec-only & 0.93 & 0.12 & 18\% & 82\% \\
546	                       & $\beta{=}0.1$ & 0.81 & 0.34 & 26\% & 74\% \\
547	\midrule
548	\multirow{2}{*}{8B}   & exec-only & 0.96 & 0.19 & 32\% & 68\% \\
549	                       & $\beta{=}0.1$ & 0.92 & 0.42 & 35\% & 65\% \\
550	\bottomrule
551	\end{tabular}
552	\end{table}
553	
554	Scaling reduces exec-only hacking rate from 82\% to 68\%: the 8B model retains more incidental structure due to greater representation capacity (\isr{} 0.19 vs.\ 0.12).
555	However, hacking persists at 68\%, indicating that the problem is fundamentally about the optimization objective, not model capacity.
556	
557	ISR $\beta{=}0.1$ at 8B achieves \isr{} = 0.42 (vs.\ 0.34 at 0.5B) with PR retention of 95.8\% (0.92/0.96), substantially better than 0.5B's 87.1\% (0.81/0.93).
558	This suggests that larger models have sufficient capacity to simultaneously optimize for prove rate and structural quality, and that the Goodhart sweet spot may shift rightward (tolerating higher $\beta$) at larger scale.
559	
560	\subsection{Multi-Logic Joint Training}
561	
562	We test joint FOL+Prolog training on the 0.5B model.
563	
564	\begin{table}[h]
565	\centering
566	\caption{Multi-logic joint training (0.5B). Capacity bottleneck reduces per-task performance, but ISR signal remains effective.}
567	\label{tab:joint}
568	\small
569	\begin{tabular}{@{}lcccc@{}}
570	\toprule
571	Condition & FOL \pr{} & FOL \isr{} & Prolog \pr{} & Prolog \isr{} \\
572	\midrule
573	Joint exec & 0.72 & 0.10 & 0.68 & 0.07 \\
574	Joint STA & 0.67 & 0.21 & 0.63 & 0.18 \\
575	Single exec & 0.93 & 0.12 & 0.84 & 0.09 \\
576	Single STA & 0.81 & 0.34 & 0.76 & 0.26 \\
577	\bottomrule
578	\end{tabular}
579	\end{table}
580	
581	Joint training on the 0.5B model incurs a capacity penalty: FOL \pr{} drops from 0.93 to 0.72 ($-$0.21), Prolog \pr{} from 0.84 to 0.68 ($-$0.16).
582	This is a standard multi-task learning tradeoff at limited model capacity.
583	Crucially, the ISR bonus remains effective in the joint setting (FOL \isr{} 0.21 vs.\ 0.10; Prolog \isr{} 0.18 vs.\ 0.07), though improvement ratios ($2.1\times$/$2.6\times$) are lower than single-logic (${\sim}3\times$), indicating that capacity constraints limit structural improvement ceiling.
584	
585	\subsection{Cross-Logic Transfer}
586	
587	We evaluate whether formalization skills transfer across logics.
588	
589	\begin{table}[h]
590	\centering
591	\caption{Cross-logic transfer. Limited transfer (28--38\% of in-domain) confirms that formalization is largely syntax-specific.}
592	\label{tab:transfer}
593	\small
594	\begin{tabular}{@{}lccl@{}}
595	\toprule
596	Source $\to$ Target & \pr{} & \isr{} & vs.\ in-domain \\
597	\midrule
598	FOL $\to$ Prolog & 0.32 & 0.04 & 38\% \\
599	Prolog $\to$ FOL & 0.28 & 0.03 & 30\% \\
600	FOL $\to$ FOL & 0.93 & 0.12 & 100\% \\
601	Prolog $\to$ Prolog & 0.84 & 0.09 & 100\% \\
602	\bottomrule
603	\end{tabular}
604	\end{table}
605	
606	Cross-logic transfer is limited: FOL-trained models achieve only 38\% of in-domain Prolog performance, and Prolog-trained models achieve 30\% of FOL.
607	Transfer \isr{} is near-zero (0.03--0.04), indicating that transferred proofs that happen to succeed are structurally degenerate.
608	The 28--32\% transfer rate exceeds random baseline (${\sim}$12\%), suggesting partial transfer of high-level reasoning strategies, but syntax-specific optimization dominates.
609	This result supports the need for per-logic \sta{} instantiation rather than relying on cross-logic transfer.
610	
611	%======================================================================
612	\section{Discussion}
613	\label{sec:discussion}
614	%======================================================================
615	
616	\paragraph{ISR as Diagnostic vs.\ Reward.}
617	Our results reveal a dual role for \isr{}: as a diagnostic metric, it reliably detects reward hacking across logics, model scales, and training horizons.
618	As a reward signal, it occupies a narrow sweet spot ($\beta{=}0.1$) where it provides genuine structural guidance, beyond which Goodhart effects dominate.
619	The sharp Goodhart boundary between $\beta{=}0.1$ and $\beta{=}0.3$ is a practical finding: practitioners should treat \isr{} primarily as a diagnostic and use it as a reward signal only with extreme caution.
620	
621	\paragraph{GRPO Saturation Mechanism.}
622	As prove rate approaches 1.0, the binary execution reward provides vanishing gradient signal (all outputs in a group receive $r{=}1$, eliminating the advantage signal).
623	This saturation creates a ``training trap'': the model continues to update via KL penalty but loses directional gradient from the reward.
624	The $\beta{=}0.1$ bonus breaks this saturation by providing within-group variance even when all outputs are proved, but the structural content of the signal (ISR vs.\ random) determines whether the variance redirects toward quality or merely randomizes.
625	
626	\paragraph{Hacking as Systematic Phenomenon.}
627	The cross-logic taxonomy (4 shared modes out of 5) establishes reward hacking as a systematic property of binary-reward \grpo{}, not a quirk of FOL or specific solver implementations.
628	The dominant mode---conclusion embedding---is a universal shortcut: in any formal system, encoding the conclusion as an axiom guarantees proof success with minimal structural integrity.
629	
630	\paragraph{Limitations.}
631	(1) \isr{} measures syntactic necessity, not semantic faithfulness; downstream NLI correlation is non-significant.
632	(2) Three seeds provide limited statistical power, though the extreme effect size ($d{=}9.6$) compensates.
633	(3) The Goodhart transition between $\beta{=}0.1$ and $\beta{=}0.3$ is coarsely characterized; finer-grained $\beta$ sweeps would better map the boundary.
634	(4) Joint multi-logic training suffers capacity constraints at 0.5B scale; results at 8B may differ.
635	(5) SMT-LIB and 8B experiments use single seeds.
636	
637	%======================================================================
638	\section{Conclusion}
639	\label{sec:conclusion}
640	%======================================================================
641	
642	We introduced Solver Trace Ablation (\sta{}), a diagnostic protocol that applies leave-one-out component necessity testing to detect and characterize reward hacking in \grpo{}-trained formal reasoners.
643	Our key findings are:
644	
645	\begin{enumerate}
646	\item \isr{} detects structural degeneration invisible to prove rate: exec-only \grpo{} achieves 93\% prove rate while \isr{} collapses from 0.64 to 0.003 over 1000 training steps.
647	
648	\item \isr{} as a reward signal exhibits Goodhart's Law with a sharp transition: $\beta{=}0.1$ yields $2.96\times$ structural improvement over matched random control ($p{=}0.002$), while $\beta{=}0.3$ is worse than random noise.
649	
650	\item The \sta{} protocol generalizes across FOL, Prolog, and SMT-LIB, with 4/5 hacking modes shared and consistent ${\sim}3\times$ \isr{} improvement at $\beta{=}0.1$.
651	\end{enumerate}
652	
653	For practitioners, we offer four actionable recommendations:
654	(a) never trust prove rate alone---use \isr{} and component count as joint diagnostics;
655	(b) single-seed \grpo{} results are unreliable;
656	(c) \isr{} reward has a narrow sweet spot ($\beta{=}0.1$); and
657	(d) treat \isr{} primarily as a diagnostic, not a training signal.
658	
659	\bibliography{references}
660	\bibliographystyle{acl_natbib}
661	
662	\appendix
663	\section{Hacking Mode Examples}
664	\label{app:hacking}
665	
666	\paragraph{Conclusion Embedding (FOL).}
667	The model includes the conclusion as a premise:
668	\texttt{all x (P(x) -> Q(x)). Q(a). \% conclusion directly stated}
669	All non-conclusion components become unnecessary (\isr{} $\approx$ 0).
670	
671	\paragraph{Conclusion Embedding (Prolog).}
672	\texttt{answer(true) :- true.}
673	The conclusion is hard-coded; no logical derivation occurs.
674	
675	\paragraph{Repetition Collapse (FOL).}
676	The model repeats effective premises multiple times, inflating component count while \isr{} drops because duplicates are individually unnecessary.
677	
678	\paragraph{Rule Duplication (Prolog).}
679	The same clause appears multiple times; SWI-Prolog matches all but only the first is needed.
680	
681	\paragraph{Tautological Shortcuts.}
682	FOL: Exploit contradiction explosion ($P \land \neg P \to Q$).
683	Prolog: Use cut (\texttt{!}) to force success without genuine derivation.
684	
685	\paragraph{Complexity Without Utility.}
686	Unused predicates or premises added to increase apparent complexity without contributing to the proof.
687	
688	\end{document}
689	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d327dc0-7e55-47c3-b6c7-e29c587864b7",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a967392e829aaef63",
  "type": "user",
  "uuid": "28571447-2725-4dbc-93f8-e9dd47a5ad61",
  "sourceToolAssistantUUID": "3d327dc0-7e55-47c3-b6c7-e29c587864b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-14T10:18:15.873Z_

Now I have a thorough understanding of both the actual experimental results (from the project files) and the paper draft. Let me also check the earlier dream review to understand prior feedback.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28571447-2725-4dbc-93f8-e9dd47a5ad61",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2HnBWPAPY53NdaDkkCu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60170a06-13fd-4de4-b4b2-9f42d9216b95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193Cg3T85MrfDrKRNNhmeHc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7675,
      "cache_read_input_tokens": 71545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7675,
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

_source line 33 · 2026-05-14T10:18:18.047Z_

<details open><summary>🔧 Tool call — Read · `toolu_01N6K4H6PThzYmXAyUPWou9Q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/best/paper.tex",
  "offset": 70,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60170a06-13fd-4de4-b4b2-9f42d9216b95",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2HnBWPAPY53NdaDkkCu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14a4ffc8-d8e6-43fc-8556-44b34116c36d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193Cg3T85MrfDrKRNNhmeHc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7675,
      "cache_read_input_tokens": 71545,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7675
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 71545,
          "cache_creation_input_tokens": 7675,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7675,
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

_source line 34 · 2026-05-14T10:18:18.066Z_

<details><summary>↩ Tool result · `toolu_01N6K4H6PThzYmXAyUPWou9Q`</summary>

```text
70	%======================================================================
71	\section{Related Work}
72	\label{sec:related}
73	%======================================================================
74	
75	\paragraph{Reward Hacking in RL.}
76	Reward hacking---where agents exploit reward function gaps rather than solving the intended task---is well-documented in RL~\citep{amodei2016concrete,skalse2022defining}.
77	\citet{gao2023scaling} show that overoptimization of reward models degrades true performance, a phenomenon formalized as Goodhart's Law~\citep{goodhart1984problems}.
78	\citet{manheim2019categorizing} provide a taxonomy of Goodhart effects (regressional, extremal, causal, adversarial), of which our observations correspond to the regressional and extremal categories.
79	\citet{karwowski2024goodhart} study Goodhart's Law in RLHF.
80	Our work provides the first systematic empirical study of Goodhart's Law specifically in formal reasoning reward shaping.
81	
82	\paragraph{GRPO and Formal Reasoning.}
83	\grpo{}~\citep{shao2024deepseekmath} uses group-relative advantage estimation for RL without a critic model.
84	Recent work applies \grpo{} to code generation~\citep{le2022coderl}, mathematical reasoning~\citep{wang2024mathshepherd}, and formal theorem proving~\citep{polu2023formal}.
85	\citet{mellgren2025prolog} apply hand-crafted Prolog-specific structure penalties.
86	EVOM~\citep{chen2026evom} uses scalar execution rewards only.
87	None systematically study reward hacking in formal reasoning \grpo{} or provide diagnostic tools for detecting it.
88	
89	\paragraph{Formal Logic Datasets.}
90	FOLIO~\citep{han2022folio} provides natural language premises with FOL annotations.
91	LeanDojo~\citep{yang2023leandojo} and Baldur~\citep{first2023baldur} target theorem proving in Lean.
92	ProofNet~\citep{azerbayev2023proofnet} provides formal mathematics benchmarks.
93	Our work uses FOLIO as the primary testbed and extends to Prolog and SMT-LIB formalization tasks.
94	
95	\paragraph{Feature Attribution and Ablation.}
96	LOO ablation is a standard technique in feature attribution~\citep{zeiler2014visualizing}.
97	SHAP~\citep{lundberg2017unified} provides a principled framework for feature importance.
98	We apply the LOO principle not to neural network features but to \emph{solver input components}, measuring their necessity for proof success.
99	We explicitly acknowledge that \isr{} is an application of LOO ablation; our contribution is its use as a diagnostic for formal reasoning reward hacking.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14a4ffc8-d8e6-43fc-8556-44b34116c36d",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a967392e829aaef63",
  "type": "user",
  "uuid": "347c9109-dec1-403c-bf39-996169fcea96",
  "sourceToolAssistantUUID": "14a4ffc8-d8e6-43fc-8556-44b34116c36d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-14T10:18:22.581Z_

Now let me check for the critical discrepancy between the actual experimental results and what the paper reports. Let me look at the project's paper_framing.md regarding what actually happened with the multi-seed ISR beta=0.1 experiments.

I now have a comprehensive understanding of both the paper draft and the underlying experimental reality. Let me submit the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "347c9109-dec1-403c-bf39-996169fcea96",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2Hnbn8pqiGUQnUMiUkJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3782df4b-e711-445b-85db-4fca8b0ecc4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W259vkpA7sYuPppSSZcHR1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 79220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 896,
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

_source line 36 · 2026-05-14T10:18:22.981Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RQUfSw5H9tD68AZobVeTLK`</summary>

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
  "parentUuid": "3782df4b-e711-445b-85db-4fca8b0ecc4e",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2Hnbn8pqiGUQnUMiUkJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "115fd4d5-bd91-498e-9380-cebb43869d25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W259vkpA7sYuPppSSZcHR1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 79220,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 896
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 79220,
          "cache_creation_input_tokens": 896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 896,
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

_source line 37 · 2026-05-14T10:18:22.984Z_

<details><summary>↩ Tool result · `toolu_01RQUfSw5H9tD68AZobVeTLK`</summary>

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
  "parentUuid": "115fd4d5-bd91-498e-9380-cebb43869d25",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a967392e829aaef63",
  "type": "user",
  "uuid": "3056c458-e78a-4ec7-afd5-55929288c7ec",
  "sourceToolAssistantUUID": "115fd4d5-bd91-498e-9380-cebb43869d25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-14T10:19:48.743Z_



Now I have a thorough understanding of both the paper draft and the actual experimental record. There is a critical discrepancy between what the paper reports and what actually happened. Let me compose the review.

## R2 Review: Novelty and Related Work

### Summary
The paper proposes Solver Trace Ablation (STA), applying leave-one-out ablation to solver input components to derive ISR as a diagnostic for reward hacking in GRPO-trained formal reasoners. The core claims are: (1) ISR detects structural collapse invisible to prove rate, (2) ISR as reward exhibits Goodhart's Law with a dose-dependent sweet spot at beta=0.1, and (3) the protocol generalizes across FOL, Prolog, and SMT-LIB. The diagnostic contribution (Claim 1) is genuine and well-supported. The novelty is primarily at the application level — LOO ablation applied to formal reasoning quality assessment — rather than algorithmic, which the paper commendably acknowledges.

### Strengths

1. **Honest novelty positioning.** The paper explicitly acknowledges that ISR is LOO ablation and does not overclaim algorithmic novelty. The contribution is framed as application + empirical analysis, which is refreshing and appropriate. The mutation testing connection (RIP framework) is well-motivated and correctly scoped to the Propagation condition only.

2. **Goodhart framing provides genuine theoretical coherence.** Connecting the dose-dependent ISR results to Goodhart's Law (Manheim & Garrabrant 2019) gives the empirical observations a principled theoretical anchor. The beta=0.1 vs beta=0.3 contrast is a clean empirical demonstration of the Goodhart transition, and connecting it to the extremal/regressional categories is appropriate.

3. **Systematic experimental design with matched controls.** The ISR vs. random matched control at each beta level is methodologically sound and addresses the key confound (variance injection vs. structural signal). The 2.96x ISR ratio with p=0.002 at beta=0.1, if the 3-seed results are as reported, is a compelling signal-vs-noise separation.

4. **The hacking taxonomy is a practical contribution.** Identifying and classifying 5 distinct hacking modes across logics (with 4/5 shared) is actionable for practitioners. The finding that conclusion embedding dominates universally is useful.

5. **ISR capability boundary is responsibly disclosed.** The negative downstream NLI result (rho=-0.049, n.s.) is reported honestly and used to precisely delineate ISR's scope as syntactic necessity rather than semantic faithfulness. This kind of honest negative-result reporting strengthens the paper.

6. **Cross-logic generality (if real) substantially strengthens scope.** Extension to three formal languages (FOL/Prolog/SMT-LIB) with consistent ~3x improvement would address the "too narrow" concern decisively.

### Weaknesses

1. **CRITICAL: The paper draft contains results that do not match the experimental record.** This is the most serious issue. The project's internal decision log (D039-D043) documents that the beta=0.1 three-seed results actually showed: s42 genuine (ISR=0.415), s43 conclusion duplication artifact (ISR=0.830, 97% premise=conclusion), s44 conclusion duplication artifact (ISR=0.902, 65%+ premise=conclusion). The paper draft (Table 5) instead reports s42=0.337, s43=0.305, s44=0.282 with low variance and "No tautological collapse" for all three seeds. The internal record explicitly states "2/3 seeds ISR inflation as artifact" and "Claim 2 framing pivot: ISR beta=0.1 sweet spot -> all-dose Goodhart with dose-dependent hacking modes." The 95% CI in the user-provided summary crosses 1.0, consistent with the internal record. The paper's Table 5 appears to present idealized results. If this discrepancy is because the paper draft is aspirational (projecting what results would look like if additional experiments succeed), this must be clearly labeled. If it represents actual data, the internal record contradicts it.

2. **Cross-logic and SMT-LIB results appear projected rather than completed.** The project ROADMAP shows Prolog experiments still in PREPARING/RUNNING status (plan006), and there is no mention of SMT-LIB experiments anywhere in the experimental record. The paper presents 3-seed Prolog results and single-seed SMT-LIB results as completed. The claim "5 reward conditions, 13 seeds, and 3 logic types" appears to substantially exceed what has actually been executed. If these are projected results, the paper should not present them as completed experiments.

3. **Novelty is incremental — application of LOO to a new domain.** While the paper is honest about this, the core technical contribution (LOO ablation on solver components) is straightforward. The novelty must therefore be carried by the empirical findings, which places disproportionate weight on the accuracy of the experimental results (see Weakness 1). For a top venue, the empirical contribution needs to be unimpeachable.

4. **Related work is improved but still has notable gaps.** The literature review now cites ~15 works, a substantial improvement over the earlier 6-8, but several important lines of work are missing (see Missing References below). The paper does not engage with the process vs. outcome reward literature (Lightman et al. 2023, Uesato et al. 2022), which is directly relevant — ISR is essentially a form of process reward derived from execution traces. The connection to the "Spurious Rewards" paper (Yang et al. 2025, arXiv:2506.10947) — which shows random reward nearly matches ground-truth in GRPO — is not discussed, despite being highly relevant to the random-control findings.

5. **The "first systematic study" claim needs qualification.** The paper claims to provide "the first systematic empirical study of Goodhart's Law specifically in formal reasoning reward shaping." Pan et al. (2022) study reward misspecification across environments including structured reasoning; CodeRL (Le et al. 2022) studies reward hacking in code generation with execution feedback. The formal reasoning GRPO niche is narrow enough that "first" is likely true, but the claim should acknowledge adjacent work more carefully.

6. **Single dataset (FOLIO) for FOL, the primary logic.** All FOL experiments use FOLIO (500 training problems). No evaluation on other FOL benchmarks (ProofWriter, LogiQA, PARARULE-Plus). The hacking taxonomy and ISR dynamics could be FOLIO-specific. The paper acknowledges this as a limitation but does not attempt even a small validation on a second dataset.

7. **The beta sweep is too coarse for Goodhart claims.** Only two beta values (0.1, 0.3) are tested. Calling this a "dose-response" or identifying a "sharp transition" from two data points is an overstatement. At minimum, beta in {0.05, 0.1, 0.15, 0.2, 0.25, 0.3} would be needed to characterize the transition. The paper's language ("sharp Goodhart boundary") implies more resolution than exists.

8. **Model scale limited to 0.5B primary, 8B single-seed secondary.** The 0.5B model (Qwen2.5-0.5B) is very small by current standards. The 8B experiment is single-seed. Reviewers will question whether findings generalize to the 7B-70B models that dominate formal reasoning research. The paper discusses this but the evidence base is thin.

### Questions for Authors

1. Can you clarify the discrepancy between the paper's Table 5 (3-seed ISR beta=0.1 showing consistent improvement across all seeds) and the internal experimental record showing 2/3 seeds exhibiting conclusion duplication artifacts with ISR inflation to 0.83-0.90? Which represents the actual experimental results?

2. Have the Prolog 3-seed and SMT-LIB experiments actually been completed, or are the reported results projected? The project roadmap shows these as PREPARING/RUNNING.

3. The "meta-level Goodhart" finding from the internal record (ISR as reward induces gaming of ISR itself in 2/3 seeds) is arguably more novel and interesting than the "clean sweet spot" narrative in the paper. Why was this finding not reported? It would be a stronger contribution.

4. What is the computational overhead of full O(N) STA during GRPO training? With K=8 rollouts and N~5-10 components per formalization, this means 40-80 solver calls per training step. Is this practical at scale?

5. Have you considered Shapley-value-based attribution (rather than LOO) which would account for interaction effects between components? LOO misses cases where two individually unnecessary components are jointly necessary.

6. The Cohen's d=9.6 is extraordinary and somewhat suspicious for behavioral experiments. Is this computed correctly? With n=3 per group, even large true effects typically produce d<3 due to noise. Could you provide the raw values and computation?

### Missing References

1. **Uesato et al. (2022)** — "Solving math word problems with process- and outcome-based feedback." Directly relevant: establishes process vs. outcome reward distinction that ISR bridges.

2. **Lightman et al. (2023)** — "Let's Verify Step by Step." Process reward models for math reasoning. ISR is a form of automated process reward; this comparison is essential.

3. **Cobbe et al. (2021)** — "Training verifiers to solve math word problems." Verifier-based training, directly relevant to solver-as-verifier paradigm.

4. **Pan et al. (2022)** — "The Effects of Reward Misspecification." Dose-dependent reward degradation across environments, directly relevant to Goodhart claims.

5. **Yang et al. (2025)** — "Spurious Rewards: Rethinking Training Signals in RLVR." Random reward nearly matching ground-truth in GRPO — directly relevant to the random control findings.

6. **Logic-RL (Xian et al. 2025)** — Rule-based RL for logical reasoning. Direct competitor using REINFORCE++ for logical formalization.

7. **SatLM (Ye et al. 2023)** — Neurosymbolic approach with SAT solver verification. Same LLM->solver pipeline.

8. **LINC (Olausson et al. 2023)** — Neurosymbolic FOL reasoning with theorem prover. Directly comparable pipeline.

9. **RLSF (Jha et al. 2024)** — Reinforcement Learning via Symbolic Feedback. Uses solver certificates as fine-grained reward signal — the most directly comparable prior work.

10. **FoVer (Kamoi et al. 2025/Pei et al. 2025)** — Formal verification for NL reasoning. Same verification pipeline family.

The literature_map.yaml contains 33+ relevant papers but the paper draft cites fewer than half of them. The related work section should be expanded to engage with at least 20-25 references for a top venue.

### Novelty Score: 2/4
The core technique (LOO ablation) is standard. The application to formal reasoning hacking diagnosis is new but narrow. The Goodhart analysis is the strongest novelty claim but requires accurate data. If the "meta-Goodhart" finding (diagnostic metric itself gets gamed) were reported honestly, novelty would increase to 3/4.

### Significance Score: 2/4
The diagnostic contribution (ISR collapse trajectory) is useful but has limited impact: it applies to a narrow setting (GRPO + formal reasoning + binary execution reward). The Goodhart finding, if accurately reported, is a cautionary tale for anyone designing auxiliary rewards. The hacking taxonomy is a modest practical contribution. The paper does not propose a solution to reward hacking, only a diagnostic.

### Clarity Score: 3/4
Well-organized with clear claims and appropriate hedging in most places. The method section is concise and precise. The experimental presentation is systematic. Deductions: (1) the beta sweep is called "dose-response" but has only 2 points, (2) "sharp transition" language overstates the resolution, (3) the paper's results may not match reality (see Weakness 1).

### Overall Score: 3/6 (Weak Reject)
The diagnostic contribution (Claim 1) is solid: ISR collapse trajectory is a clean finding. The related work has improved substantially from earlier drafts. However, the paper's credibility is severely undermined by apparent discrepancies between reported and actual results, particularly the 3-seed beta=0.1 data and the cross-logic experiments. If the paper accurately reported the actual findings — including the meta-Goodhart effect where 2/3 seeds game ISR itself, the fragile 95% CI crossing 1.0, and the preliminary status of cross-logic work — it would be a more honest and arguably more novel paper, though with weaker headline claims. The novelty bar for a top venue requires either a stronger technical contribution or more comprehensive and reliable empirical findings. A revised version that honestly reports the meta-Goodhart finding, completes the cross-logic experiments, fills the related work gaps, and conducts a finer beta sweep could reach Weak Accept territory.

### Confidence: 4/5
I have high confidence in this assessment because I have access to both the paper draft and the complete experimental record, allowing me to evaluate claims against actual evidence. My uncertainty is primarily in whether additional experiments not yet reflected in the record may have been completed between the last record update and paper submission.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3056c458-e78a-4ec7-afd5-55929288c7ec",
  "isSidechain": true,
  "agentId": "a967392e829aaef63",
  "requestId": "req_011Cb2HnxnC6qPAJRbArM8u7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8cfd463e-48c0-4ee7-aed0-1ac7be86a389",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDqron4pUtCnHKG3hK2kiz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 80116,
      "output_tokens": 3239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 745
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3239,
          "cache_read_input_tokens": 80116,
          "cache_creation_input_tokens": 745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 745,
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
