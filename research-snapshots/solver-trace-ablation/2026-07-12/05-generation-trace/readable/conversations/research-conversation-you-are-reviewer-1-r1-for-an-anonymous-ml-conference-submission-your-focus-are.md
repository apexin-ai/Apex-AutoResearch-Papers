# Research conversation: You are Reviewer 1 (R1) for an anonymous ML conference submission. Your focus areas are **methodology** and **experiment

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aed6b033f1505451c.jsonl`
- **Structured JSON:** [`fee2f7cfbdef851224b6.json`](../../sessions/fe/fee2f7cfbdef851224b6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

39 recorded events

### User

_source line 1 · 2026-05-14T10:10:06.266Z_

You are Reviewer 1 (R1) for an anonymous ML conference submission. Your focus areas are **methodology** and **experimental rigor**. Review the paper below according to top ML venue standards (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

## Your review must cover:
1. **Methodology soundness**: Is STA/ISR well-defined? Are the formulas correct? Is the LOO ablation principled? Any theoretical gaps?
2. **Experimental design**: Are controls adequate? Are baselines appropriate? Is the evaluation methodology sound?
3. **Statistical rigor**: Are the statistical tests appropriate for n=3? Is Cohen's d=9.6 with n=3 meaningful? Are confidence intervals properly computed?
4. **Reproducibility**: Is enough detail provided to reproduce? Any missing hyperparameters or implementation details?
5. **Experiment coverage**: Compare against the full experiment plan below and assess what's covered vs. missing.
6. **Weaknesses**: Identify the top 3-5 weaknesses.
7. **Strengths**: Identify the top 3-5 strengths.
8. **Questions for authors**: 3-5 specific questions.
9. **Minor issues**: Formatting, typos, clarity.
10. **Overall assessment**: Score (1-6), confidence (1-5), and 2-3 sentence summary.

## Paper summary (9 pages):

**Title**: Solver Trace Ablation: Diagnosing Reward Hacking and Goodhart's Law in GRPO-Trained Formal Reasoners

**Core idea**: GRPO with execution-only rewards trains formal reasoners to high prove rates but produces structurally degenerate outputs (reward hacking). The paper proposes STA, a diagnostic using LOO ablation on solver inputs to compute ISR (Intensional Structural Reward) — fraction of necessary components.

**Three claims**:
1. ISR detects reward hacking invisible to prove rate: exec-only GRPO achieves 93% PR while ISR collapses from 0.64 to 0.003 over training.
2. ISR as reward signal exhibits Goodhart's Law: β=0.1 yields 2.96× improvement over random control (p=0.002), β=0.3 collapses.
3. STA generalizes across FOL/Prover9, Prolog/SWI-Prolog, SMT-LIB/Z3.

**Method (Section 3)**:
- ISR(F) = (1/n) Σ nec(ci), where nec(ci) = 1[S(F\{ci})=0]
- Reward: r = r_exec · (1 + β · ISR(F))
- ISR capability boundary: measures syntactic necessity, NOT semantic faithfulness (ρ(ISR, NLI)=-0.049, ns)
- O(n) computation necessary; O(1) approximation fails (ρ=0.18)

**Experimental setup (Section 4)**:
- Model: Qwen2.5-0.5B-Instruct primary; Qwen3-8B for scaling
- Data: FOLIO 500 training problems; equivalent Prolog/SMT-LIB datasets
- Training: GRPO K=8, 500 steps (unless noted), Prover9/SWI-Prolog/Z3 solvers
- Eval metrics: PR, mean ISR, proved-only ISR, component count, genuine rate (ISR>0.3)
- Seeds: 3 seeds (s42,s43,s44) for replication; single seed for exploratory

**Key results tables**:
- Table 1: ISR collapse trajectory (100→500→1000 steps): PR 0.32→0.93→0.96, ISR 0.64→0.13→0.003
- Table 2: SFT comparison — SFT PR=0.48, ISR=0.24; GRPO exec PR=0.93, ISR=0.12
- Table 3: O(1) vs O(N) — O(1) ρ=0.18 with O(N)
- Table 4: ISR β=0.1 three-seed: mean PR=0.777±0.030, ISR=0.308±0.028
- Table 5: Random β=0.1 three-seed: mean PR=0.763±0.025, ISR=0.104±0.015
- Table 6: Statistical comparison: ISR/random ratio=2.96×, p=0.002, Cohen's d=9.6
- Table 7: Goodhart dose-response: β=0 (PR=0.93), β=0.1 ISR (PR=0.81), β=0.3 ISR (PR=0.18)
- Table 8: Curriculum ablation: fixed β=0.1 multiplicative best (PR=0.81, ISR=0.34)
- Table 9: Prolog exec-only 3 seeds: mean PR=0.84, ISR=0.087
- Table 10: Prolog exec+STA β=0.1: mean PR=0.757, ISR=0.260 (2.99×)
- Table 11: Cross-logic comparison
- Table 12: Cross-logic hacking taxonomy (4/5 shared modes, Jaccard=0.667)
- Table 13: SMT-LIB: exec-only PR=0.72/ISR=0.09, β=0.1 PR=0.67/ISR=0.24 (2.67×)
- Table 14: 8B scale: exec-only hack rate 68% (vs 82% at 0.5B), β=0.1 ISR=0.42
- Table 15: Joint FOL+Prolog training: capacity penalty
- Table 16: Cross-logic transfer: limited (28-38% of in-domain)

**Appendix A**: Hacking mode examples for FOL and Prolog

## Full experiment design (for coverage assessment):

The following experiments were planned. Assess which are covered and which are missing/incomplete in the paper:

1. **ISR β=0.1 three-seed replication** (FOL) — s42/s43/s44 with matched random control → COVERED (Tables 4-6)
2. **Random β=0.1 three-seed control** — matched comparison → COVERED (Table 5-6)
3. **3-seed ISR vs Random statistical comparison** → COVERED (Table 6)
4. **STA O(1) vs O(N) computational ablation** → COVERED (Table 3)
5. **Prolog exec-only GRPO (3 seeds)** → COVERED (Table 9)
6. **Prolog exec+STA GRPO (3 seeds, ISR β=0.1)** → COVERED (Table 10)
7. **Cross-logic hacking taxonomy (FOL × Prolog)** → COVERED (Table 12)
8. **Multi-logic joint GRPO (FOL + Prolog)** → COVERED (Table 15)
9. **Cross-logic transfer evaluation** → COVERED (Table 16)
10. **SFT baseline comparison** → COVERED (Table 2)
11. **SMT-LIB single-logic GRPO** → COVERED (Table 13) — but single seed only
12. **Qwen3-8B model scale effect** → COVERED (Table 14) — but single seed only
13. **Curriculum ablation** → COVERED (Table 8)

Planned but missing from paper:
- SMT-LIB genuine rate delta not reported
- SMT-LIB hacking taxonomy detail (only "3 shared modes" mentioned, no breakdown table)
- 8B Goodhart boundary exploration (whether sweet spot shifts with scale)
- β values between 0.1 and 0.3 (the Goodhart transition is "coarsely characterized" per the paper's own admission)

Output your review in a structured format with clear section headers. Be rigorous and specific — cite table numbers and specific numbers when critiquing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2e19d6e8-bb23-4295-950f-2fd84db5b483",
  "agentId": "aed6b033f1505451c",
  "type": "user",
  "uuid": "e46fb16f-c061-41fc-a5a5-f29f0c2d101f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T10:10:06.271Z_

```json
{
  "parentUuid": "e46fb16f-c061-41fc-a5a5-f29f0c2d101f",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
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
  "uuid": "0ab3bd49-bbb7-4b4e-a9ed-cce29f74a562",
  "timestamp": "2026-05-14T10:10:06.271Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T10:10:08.671Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ab3bd49-bbb7-4b4e-a9ed-cce29f74a562",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HALy9UYWzGLBoXMM2V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c2c1783-e691-4f5c-9349-b0b1080d442e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nz7scR2TFuAZzc3uenVtEj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16078,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16078,
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

_source line 4 · 2026-05-14T10:10:10.184Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KisUehsmJhsZUuacugmx28`</summary>

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
  "parentUuid": "7c2c1783-e691-4f5c-9349-b0b1080d442e",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HALy9UYWzGLBoXMM2V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2de0cd4-fe82-4373-8acd-dcbe6ebc9e19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nz7scR2TFuAZzc3uenVtEj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16078,
      "cache_read_input_tokens": 0,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16078
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16078,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16078,
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

_source line 5 · 2026-05-14T10:10:10.189Z_

<details><summary>↩ Tool result · `toolu_01KisUehsmJhsZUuacugmx28`</summary>

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
  "parentUuid": "e2de0cd4-fe82-4373-8acd-dcbe6ebc9e19",
  "isSidechain": true,
  "promptId": "2e19d6e8-bb23-4295-950f-2fd84db5b483",
  "agentId": "aed6b033f1505451c",
  "type": "user",
  "uuid": "25128045-f363-4d7d-ac0b-41052db87dca",
  "sourceToolAssistantUUID": "e2de0cd4-fe82-4373-8acd-dcbe6ebc9e19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T10:10:14.047Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01SNJoghXKwjKHzFHeTq7bhK`</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25128045-f363-4d7d-ac0b-41052db87dca",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HAdmCBxZJJBRKSVHtn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4187769-e036-45bd-8a0b-cbbfcda45ae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015JNmpxAdNjKEbCdMVZYKya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 7 · 2026-05-14T10:10:14.205Z_

<details><summary>↩ Tool result · `toolu_01SNJoghXKwjKHzFHeTq7bhK`</summary>

```text
{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (43 个)\n\n- **plan001-exec-only-s42**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-gt-isr-baseline**: DONE (success) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| plan006-prolog-sta-s42 | Prolog exec+STA GRPO seed=42: ISR reward 在 Prolog logic type 上的效果。与 plan006-prolog-exec-s42 (exec-only) 对照，验证 STA/ISR 的 hacking 检测和 Goodhart 效应是否跨 logic type 泛化。 | — | — | — |\n| plan006-prolog-exec-s42 | Prolog exec-only GRPO seed=42: STA/ISR hacking patterns generalize across logic types? Prolog uses rule ablation (vs FOL axiom ablation). If same degeneration modes appear → STA is logic-agnostic diagnostic. | — | — | — |\n\n## 待处理\n- plan018-additive-random-b01-s43: Random β=0.1 seed=43 控制组：与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s43 下是否成立。（排队等待 GPU）\n- plan018-additive-random-b01-s44: Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。（排队等待 GPU）\n- plan006-prolog-sta-s44: Prolog exec+STA GRPO seed=44: 第三 seed。3-seed mean±std 用于论文 Claim 3 跨 logic type 统计支撑。（准备中）\n- plan006-prolog-sta-s43: Prolog exec+STA GRPO seed=43: 跨 seed 稳定性检查。与 exec-only s43 对照。（准备中）\n- plan006-prolog-exec-s44: Prolog exec-only GRPO seed=44: third seed for Prolog. Together with s42/s43, provides 3-seed evidence for cross-logic generalization claim.（准备中）\n- plan006-prolog-exec-s43: Prolog exec-only GRPO seed=43: cross-seed stability check for Prolog logic type. FOL showed extreme cross-seed variance (s42 genuine vs s43 degenerate vs s44 tautological).（准备中）\n\n## 近期结论\n- **plan002-additive-b01-s43** (negative): ISR β=0.1 seed=43 多 seed 验证：plan002-b01-s42 (PR=0.81, ISR=0.337) 在 s43 下是否可复现？exec-only s43 是 degraded seed (PR=14%)，ISR β=0.1 能否拯救 bad seed？3-seed mean±std 用于论文 Claim 2 统计支撑。 ← 基于 plan002-additive-b01-s42\n  [plan002-b01-s43-eval-results](/api/workspace-files/projects/solver-trace-ablation/artifacts/plan002-additive-b01-s43/data/plan002-b01-s43-eval-pointer.txt)\n- **plan002-additive-b01-s44** (negative): ISR β=0.1 seed=44 多 seed 验证：exec-only s44 是 tautological collapse (PR=98%, ISR=0.57 fake)，ISR β=0.1 能否防止 tautological collapse？3-seed mean±std 用于论文 Claim 2。 ← 基于 plan002-additive-b01-s42\n- **plan012-hacking-taxonomy** (success): ISR β=0.1 vs Random β=0.1 hacking taxonomy 对比：ISR reward 能否减少 hacking 模式比例、增加 genuine proof 比例？5 种 hacking 分类（conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, premise padding）。\n\n## 趋势\n成功 9 / 负向 12 / 失败 14 / 共 35\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-39279: 无 GPU 信息\n\n## 告警\n- sta-phase1-exec-only: 训练失败 — unknown\n- sta-phase1-exec-sta: 训练失败 — unknown\n- sta-phase1-exec-only-r2: 训练失败 — unknown\n- sta-phase1-exec-sta-r2: 训练失败 — unknown\n- sta-phase1-exec-only-r3: 训练失败 — unknown\n- sta-phase1-exec-sta-r3: 训练失败 — unknown\n- plan001-exec-only-s42: 训练失败 — unknown\n- plan001-exec-only-s42-r3: 训练失败 — unknown\n- plan001-exec-only-s43: 训练失败 — unknown\n- plan013-random-reward-s42: 训练失败 — unknown\n- plan013-random-reward-s42-r2: 训练失败 — unknown\n- plan001-exec-only-s43-r2: 训练失败 — unk"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4187769-e036-45bd-8a0b-cbbfcda45ae0",
  "isSidechain": true,
  "promptId": "2e19d6e8-bb23-4295-950f-2fd84db5b483",
  "agentId": "aed6b033f1505451c",
  "type": "user",
  "uuid": "8e13dc65-0620-4f09-820f-7c68fbbaac3e",
  "sourceToolAssistantUUID": "e4187769-e036-45bd-8a0b-cbbfcda45ae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T10:10:14.752Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NSSM2SSj3XrtVnbRY1YZEP`</summary>

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
  "parentUuid": "8e13dc65-0620-4f09-820f-7c68fbbaac3e",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HAdmCBxZJJBRKSVHtn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f08fee4b-ea78-4d01-94ee-77670754a8a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015JNmpxAdNjKEbCdMVZYKya",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16078,
      "output_tokens": 162,
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
          "output_tokens": 162,
          "cache_read_input_tokens": 16078,
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

_source line 9 · 2026-05-14T10:10:14.763Z_

<details><summary>↩ Tool result · `toolu_01NSSM2SSj3XrtVnbRY1YZEP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| plan006-prolog-sta-s42 | Prolog exec+STA GRPO seed=42: ISR reward 在 Prolog logic type 上的效果。与 plan006-prolog-exec-s42 (exec-only) 对照，验证 STA/ISR 的 hacking 检测和 Goodhart 效应是否跨 logic type 泛化。 | — | — | — |\\n| plan006-prolog-exec-s42 | Prolog exec-only GRPO seed=42: STA/ISR hacking patterns generalize across logic types? Prolog uses rule ablation (vs FOL axiom ablation). If same degeneration modes appear → STA is logic-agnostic diagnostic. | — | — | — |\\n\\n## 待处理\\n- plan018-additive-random-b01-s43: Random β=0.1 seed=43 控制组：与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s43 下是否成立。（排队等待 GPU）\\n- plan018-additive-random-b01-s44: Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。（排队等待 GPU）\\n- plan006-prolog-sta-s44: Prolog exec+STA GRPO seed=44: 第三 seed。3-seed mean±std 用于论文 Claim 3 跨 logic type 统计支撑。（准备中）\\n- plan006-prolog-sta-s43: Prolog exec+STA GRPO seed=43: 跨 seed 稳定性检查。与 exec-only s43 对照。（准备中）\\n- plan006-prolog-exec-s44: Prolog exec-only GRPO seed=44: third seed for Prolog. Together with s42/s43, provides 3-seed evidence for cross-logic generalization claim.（准备中）\\n- plan006-prolog-exec-s43: Prolog exec-only GRPO seed=43: cross-seed stability check for Prolog logic type. FOL showed extreme cross-seed variance (s42 genuine vs s43 degenerate vs s44 tautological).（准备中）\\n\\n## 近期结论\\n- **plan002-additive-b01-s43** (negative): ISR β=0.1 seed=43 多 seed 验证：plan002-b01-s42 (PR=0.81, ISR=0.337) 在 s43 下是否可复现？exec-only s43 是 degraded seed (PR=14%)，ISR β=0.1 能否拯救 bad seed？3-seed mean±std 用于论文 Claim 2 统计支撑。 ← 基于 plan002-additive-b01-s42\\n  [plan002-b01-s43-eval-results](/api/workspace-files/projects/solver-trace-ablation/artifacts/plan002-additive-b01-s43/data/plan002-b01-s43-eval-pointer.txt)\\n- **plan002-additive-b01-s44** (negative): ISR β=0.1 seed=44 多 seed 验证：exec-only s44 是 tautological collapse (PR=98%, ISR=0.57 fake)，ISR β=0.1 能否防止 tautological collapse？3-seed mean±std 用于论文 Claim 2。 ← 基于 plan002-additive-b01-s42\\n- **plan012-hacking-taxonomy** (success): ISR β=0.1 vs Random β=0.1 hacking taxonomy 对比：ISR reward 能否减少 hacking 模式比例、增加 genuine proof 比例？5 种 hacking 分类（conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, premise padding）。\\n\\n## 趋势\\n成功 9 / 负向 12 / 失败 14 / 共 35\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-39279: 无 GPU 信息\\n\\n## 告警\\n- sta-phase1-exec-only: 训练失败 — unknown\\n- sta-phase1-exec-sta: 训练失败 — unknown\\n- sta-phase1-exec-only-r2: 训练失败 — unknown\\n- sta-phase1-exec-sta-r2: 训练失败 — unknown\\n- sta-phase1-exec-only-r3: 训练失败 — unknown\\n- sta-phase1-exec-sta-r3: 训练失败 — unknown\\n- plan001-exec-only-s42: 训练失败 — unknown\\n- plan001-exec-only-s42-r3: 训练失败 — unknown\\n- plan001-exec-only-s43: 训练失败 — unknown\\n- plan013-random-reward-s42: 训练失败 — unknown\\n- plan013-random-reward-s42-r2: 训练失败 — unknown\\n- plan001-exec-only-s43-r2: 训练失败 — unknown\\n- plan013-random-reward-s42-r3: 训练失败 — unknown\\n- plan001-exec-only-s43-r3: 训练失败 — unknown\\n\", \"total_chars\": 3095, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f08fee4b-ea78-4d01-94ee-77670754a8a5",
  "isSidechain": true,
  "promptId": "2e19d6e8-bb23-4295-950f-2fd84db5b483",
  "agentId": "aed6b033f1505451c",
  "type": "user",
  "uuid": "509b3375-e773-4f86-9e5c-df1753fdb382",
  "sourceToolAssistantUUID": "f08fee4b-ea78-4d01-94ee-77670754a8a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T10:10:21.809Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013PHMCCntMrNV4spndT98g4`</summary>

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
  "parentUuid": "509b3375-e773-4f86-9e5c-df1753fdb382",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HAz6KSYqJFUFtxoxur",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c145a095-82cf-449e-9280-01cb23c6bf57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WSosnRiNikKRHY5Z5LurnY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3848,
      "cache_read_input_tokens": 17525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3848,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 11 · 2026-05-14T10:10:21.850Z_

<details><summary>↩ Tool result · `toolu_013PHMCCntMrNV4spndT98g4`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c145a095-82cf-449e-9280-01cb23c6bf57",
  "isSidechain": true,
  "promptId": "2e19d6e8-bb23-4295-950f-2fd84db5b483",
  "agentId": "aed6b033f1505451c",
  "type": "user",
  "uuid": "5377ba68-0dab-4c8d-a136-8e14c14ddc7d",
  "sourceToolAssistantUUID": "c145a095-82cf-449e-9280-01cb23c6bf57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T10:10:23.589Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01MW18NMsPwSu8s2mG2uymGd`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5377ba68-0dab-4c8d-a136-8e14c14ddc7d",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HAz6KSYqJFUFtxoxur",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8541053-8f5e-4af8-ba91-7ea3b52538ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WSosnRiNikKRHY5Z5LurnY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3848,
      "cache_read_input_tokens": 17525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3848,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 13 · 2026-05-14T10:10:23.608Z_

<details><summary>↩ Tool result · `toolu_01MW18NMsPwSu8s2mG2uymGd`</summary>

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
  "parentUuid": "b8541053-8f5e-4af8-ba91-7ea3b52538ec",
  "isSidechain": true,
  "promptId": "2e19d6e8-bb23-4295-950f-2fd84db5b483",
  "agentId": "aed6b033f1505451c",
  "type": "user",
  "uuid": "571ba998-6e71-4f22-9367-050505970eb2",
  "sourceToolAssistantUUID": "b8541053-8f5e-4af8-ba91-7ea3b52538ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T10:10:23.852Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QNxpUxd6pAvSdCAcuneJ3L`</summary>

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
  "parentUuid": "571ba998-6e71-4f22-9367-050505970eb2",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HAz6KSYqJFUFtxoxur",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5da4caee-a1c0-4086-949c-572a1c81e40a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WSosnRiNikKRHY5Z5LurnY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3848,
      "cache_read_input_tokens": 17525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3848,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 15 · 2026-05-14T10:10:23.868Z_

<details><summary>↩ Tool result · `toolu_01QNxpUxd6pAvSdCAcuneJ3L`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ROADMAP.md\", \"content\": \"# solver-trace-ablation — Research Dashboard\\n\\n> 最后更新: 2026-05-14 09:06 UTC | 更新原因: D038 taxonomy 结果纳入 + 刷新 RUNNING 状态（plan016 已完成、s43/s44 在跑）\\n\\n## 核心方向\\nSTA/ISR 作为 GRPO neurosymbolic formalizer 的**诊断工具** + **Goodhart's Law 案例研究**——检测 reward hacking、量化结构退化、分类退化模式，并展示 ISR 从诊断指标到优化目标的 Goodhart 转折。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research + 审稿进行中 | **DDL**: 2026-05-25（剩 11 天）\\n- **实验**: 39 个 (RUNNING 2, PREPARING 5, DONE 32) | success 8\\n- **GPU**: 2 × RTX PRO 6000 96GB — ✅ 两卡满载\\n\\n### 核心证据链\\n- ✅ ISR 崩塌轨迹：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- ✅ 3-seed exec-only：s42 conclusion embedding | s43 degraded | s44 tautological collapse\\n- ✅ Goodhart β 剂量效应：β=0.1 sweet spot (ISR 3.2x > random) vs β=0.3 collapse (ISR < random)\\n- ✅ Hacking taxonomy 定量对比 (D038)：ISR β=0.1 genuine 25.9% vs random 17.7% (+8.2pp)，conclusion embedding 73-79%\\n- ✅ plan016 1000步：PR=0.96, ISR=0.003，崩塌持续恶化\\n- ✅ plan014 downstream NLI: ISR-NLI ρ=-0.049 n.s.，ISR 能力边界已刻画\\n- ✅ Table 1 修复 + 文献修正完成\\n- ⏳ plan002-b01-s43/s44: RUNNING — β=0.1 多 seed 验证\\n- 🔜 plan018-random-s43/s44: PREPARING — matched random 多 seed 控制\\n- 🔜 plan006-prolog ×3: PREPARING — Claim 3 跨 logic type 验证\\n\\n## RUNNING\\n| 实验 | GPU | 说明 |\\n|------|-----|------|\\n| plan002-additive-b01-s43 | cuda:0 | ISR β=0.1 seed=43 |\\n| plan002-additive-b01-s44 | cuda:1 | ISR β=0.1 seed=44 |\\n\\n## 近期任务\\n- [ ] s43/s44 完成 → eval_sta.py + taxonomy + 3-seed mean±std\\n- [ ] plan018-random-s43/s44 启动（GPU 空闲后）\\n- [ ] plan006 Prolog 代码/数据 readiness 确认\\n- [ ] 3-seed 全部出齐 → Table 1 + Table 2 定稿\\n- [ ] plan006 结果 → 论文写作启动评估\\n\\n## GPU 预算\\n- 本地: 2 × RTX PRO 6000 96GB，两卡满载\\n- 已消耗: ~35+ GPU·h\\n- 剩余需求: ~12h（s43/s44 ~2h + random s43/s44 ~2h + plan006 ×3 ~6h + eval ~2h）\\n- DDL 11 天 × 2 卡 × 24h = 528 GPU·h，时间充裕\\n\\n## 写作约束\\n- plan013 vs plan017 公式结构不同，不可简化为\\\"additive vs convex\\\"对照 (D027)\\n- ISR β=0.1 hacking rate 仍达 74%——论文不可标\\\"no hacking\\\"，应标\\\"lowest hacking rate\\\" (D038)\\n- β=0.1 3-seed 出齐前论文统计用 s42 单 seed，标注 preliminary\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D043 | 2026-05-14 | ISR β=0.1 \\\"sweet spot\\\"叙事降级：2/3 seeds ISR 膨胀为 artif | plan002-additive-b01-s42, plan002-additive-b01-s43, plan002-additive-b01-s44, plan018-additive-random-b01-s42 |\\n| D042 | 2026-05-14 | ISR 度量存在结构性盲点：premise≈conclusion 时 conclusion sub- | plan002-additive-b01-s43, plan002-additive-b01-s44, plan002-additive-b01-s42 |\\n| D041 | 2026-05-14 | Claim 2 framing pivot: ISR β=0.1 \\\"sweet spot\\\" → \\\"a | plan002-additive-b01-s42, plan002-additive-b01-s43, plan002-additive-b01-s44 |\\n| D040 | 2026-05-14 | plan002-b01-s44 reclassified: \\\"success\\\" → \\\"new hac | plan002-additive-b01-s44, plan002-additive-b01-s42 |\\n| D039 | 2026-05-14 | plan002-b01-s44 重分类：从 success 改为 semantic drift ha | plan002-additive-b01-s44 |\\n| D038 | 2026-05-14 | Hacking taxonomy 结果足够，跳过 LLM-as-judge；taxonomy 对比覆 | plan012, plan002-additive-b01-s42, plan018-additive-random-b01-s42 |\\n| D037 | 2026-05-14 | ISR β=0.1 质量验证路径：先 hacking taxonomy 对比，必要时加 LLM-as | plan002-additive-b01-s42, plan018-additive-random-b01-s42, plan012 |\\n| D036 | 2026-05-14 | 为 beta=0.1 补跑多 seed (s43/s44) 验证 ISR vs random 的稳健 | plan002-additive-b01-s42, plan018-additive-random-b01-s42, plan001-exec-only-s43 |\\n| D035 | 2026-05-14 | Framing 选 C: Goodhart 主线 — ISR 展示经典 Goodhart 效应（β= | plan002-b01, plan018, plan002-b03, plan017 |\\n| D034 | 2026-05-14 | Framing 选 C+A 混合：Goodhart 为主线叙事，ISR 诊断保留为 Claim 1， | plan002-b01, plan018, plan002-b03, plan017 |\\n\\n\", \"total_chars\": 3396, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5da4caee-a1c0-4086-949c-572a1c81e40a",
  "isSidechain": true,
  "promptId": "2e19d6e8-bb23-4295-950f-2fd84db5b483",
  "agentId": "aed6b033f1505451c",
  "type": "user",
  "uuid": "76b88c40-31e9-4de2-b97c-6b6651728af6",
  "sourceToolAssistantUUID": "5da4caee-a1c0-4086-949c-572a1c81e40a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T10:10:24.370Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Xi9xurmZRScnsrvVuAK4nE`</summary>

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
  "parentUuid": "76b88c40-31e9-4de2-b97c-6b6651728af6",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HAz6KSYqJFUFtxoxur",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17ff2a24-4b2f-4db3-87fb-343755706ff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WSosnRiNikKRHY5Z5LurnY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3848,
      "cache_read_input_tokens": 17525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3848,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 17 · 2026-05-14T10:10:24.400Z_

<details><summary>↩ Tool result · `toolu_01Xi9xurmZRScnsrvVuAK4nE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md\", \"content\": \"# solver-trace-ablation — Memory\\n\\n## 环境信息 (2026-05-13)\\n\\n### westd-39279 服务器\\n- **GPU**: 2× RTX PRO 6000 Blackwell, 94GB VRAM 每张\\n- **CUDA**: 12.8, PyTorch 2.10.0+cu128\\n- **镜像**: aml-train（conda 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）\\n- **ML 栈**: transformers/trl/vllm/accelerate 全部预装\\n- **Solvers**: Prover9 (LADR 2009-11A 源码编译), SWI-Prolog 8.4.2 (`/usr/bin/swipl`), Z3 4.16.0.0\\n- **模型**: Qwen3-4B 已下载（7.6GB，通过 ModelScope）\\n- **代码路径**: `/root/solver-trace-ablation/`\\n- **磁盘**: 系统盘 30GB (22G free)，数据盘 `/root/autodl-tmp/` 250GB (142G free)\\n\\n### 决策记录\\n- Qwen3-4B 用 ModelScope 下载（HuggingFace 直连可能慢）\\n- Prover9 从 LADR 源码编译（apt 无包）\\n- 94GB VRAM 单卡跑 Qwen3-4B 完全无压力\\n\\n## 数据 (2026-05-13)\\n\\n### 数据源变更：ProofWriter → FOLIO\\n- ProofWriter 原始数据无 FOL 列，改用 `tasksource/folio`（1204 条人工标注 FOL）\\n- Phase 0 子集 100 条，训练子集 500 条\\n- 34% 数据含 XOR (⊕) 符号，已在 `_normalize_fol()` 中修复展开\\n\\n### 数据约束 (2026-05-14, D009)\\n- **C001**: 所有 plan001/plan013 实验统一使用 `train_500_seed42.jsonl`，不再用 `proofwriter_fol_500.jsonl`（消除数据差异 confound）\\n\\n## Phase 0 关键发现 (2026-05-13)\\n\\n### Base Model ISR Baseline (sta-phase0-baseline)\\n- **Prove rate**: 12% overall, 18.2% excluding XOR-affected samples\\n- **Mean ISR**: 0.064 (very low — base model formalizations mostly unprovable)\\n- **ISR 区分度**: proved 样本 ISR 0.125–0.889\\n\\n### Ground-Truth ISR Baseline (sta-gt-isr-baseline)\\n- **GT prove rate**: 18% (limited by Prover9 only proving entailment; true=50%, false=4%, unknown=0%)\\n- **GT mean ISR**: 0.5588 (median 0.6125, range 0.14–1.00)\\n- **Model vs GT gap**: ISR 0.064 vs 0.559 = 8.7x 差距，STA 有强区分力\\n\\n### Prover9 局限性\\n- Prover9 只能证明 entailment（conclusion 从 premises 推出）\\n- `false` 和 `unknown` 类问题几乎无法证明（false 4%, unknown 0%）\\n\\n## Phase 1 关键经验 (2026-05-13)\\n\\n### fast_isr_fol 失败教训 (r4)\\n- `fast_isr_fol()` 是二值 tautology gate (0/1)，Qwen3-4B 不产生 tautology → ISR ≡ prove_rate → 两条件零差异\\n- **教训：binary ISR 无法提供有意义的 reward shaping 信号，必须用连续 ISR**\\n\\n### D010 Reward 公式转向 (2026-05-14)\\n- **旧公式（废弃）**: r = α·r_exec + β·r_exec·ISR, α+β=1 → ISR<1 时永远是 penalty\\n- **新公式**: r = r_exec · (1 + β·ISR), β>0 → ISR 只能 bonus，不能 penalty\\n\\n## Held-out eval_sta 全量结果 (2026-05-14) — 关键\\n\\n### 九组 eval 对比（含 plan016 1000步 + plan018 random β=0.1）\\n\\n| 实验 | Reward | Steps | eval PR | eval ISR | proved_only_ISR | n_components | 退化模式 |\\n|------|--------|-------|---------|----------|-----------------|--------------|----------|\\n| plan001-s42 | exec-only | 500 | **93%** | 0.123 | 0.132 | 6.58 | ✅ Genuine proofs |\\n| plan001-s43 | exec-only | 500 | **14%** | 0.000 | 0.000 | N/A | ❌ 长输出退化 |\\n| plan001-s44 | exec-only | 500 | **98%** | 0.570 | 0.582 | 2.04 | ❌ Tautological collapse |\\n| **plan016** | **exec-only** | **1000** | **96%** | **0.003** | **0.003** | **18.55** | **❌ 矛盾爆炸崩塌** |\\n| **plan002-b01** | **additive ISR β=0.1** | 500 | **81%** | **0.337** | **0.415** | **5.58** | **✅ Genuine + improved** |\\n| **plan018** | **additive random β=0.1** | 500 | **79%** | **0.104** | **0.131** | **8.46** | **⚠️ 冗余但无坍缩** |\\n| plan002-b03 | additive ISR β=0.3 | 500 | 18% | 0.026 | 0.143 | 10.67 | ❌ 过拟合+低泛化 |\\n| plan017 | additive random β=0.3 | 500 | 48% | 0.045 | 0.094 | 9.6 | ❌ 复杂但无用 |\\n| plan013 | convex random | 500 | 100% | 0.535 | 0.535 | 2.04 | ❌ Tautological hacking |\\n\\n### β=0.1 ISR vs Random 同剂量对照 (plan002-b01 vs plan018, D031 定论) — 重大发现\\n\\n**ISR β=0.1 提供 genuine structural guidance，非 variance regularization。**\\n\\n- PR 几乎相同 (0.81 vs 0.79) → β=0.1 噪声不影响证明能力\\n- ISR 差 3.2x (0.337 vs 0.104) → ISR 信号引导结构改善\\n- Components 5.58 vs 8.46 → ISR 组更精简\\n- random 组 36.7% proved 样本 ISR=0（无结构证明）\\n\\n### ISR-as-Reward β 剂量响应完整图谱\\n\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 结论 |\\n|---|---|---|---|---|---|\\n| 0.1 | 0.81 | 0.79 | **0.337** | 0.104 | ISR >> random (3.2x) |\\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\\n\\n**剂量依赖**：低 β ISR 有结构价值；高 β ISR 触发 Goodhart 效应反而比 random 更差。\\n\\n### plan016 延长训练发现 (2026-05-14)\\n\\n**ISR 崩塌随训练持续恶化，无回升信号。**\\n- 500步 ISR=0.123 → 1000步 ISR=0.003 (-97.8%)\\n- Windowed ISR 单调递减：step 200 peak 0.1115 → step 1000 低至 0.0144\\n- 退化模式：非 2-component 同义反复，而是矛盾爆炸（大量无关前提嵌入矛盾）\\n- Components 6.58→18.55 (+182%)\\n- 论文意义：exec-only 延长训练是 reward hacking 恶化的干净消融证据\\n\\n### 跨 seed 退化分类 (2026-05-14)\\n\\n| Seed | 退化模式 | 特征 | 诊断信号 |\\n|------|----------|------|----------|\\n| s42 | ✅ Genuine | PR=93%, components=6.58 | 唯一健康 seed |\\n| s43 | ❌ Length explosion | PR=14%, 87% hit max_new_tokens | D029: 不重训 |\\n| s44 | ❌ Tautological collapse | PR=98%, components=2.04 | ISR=0.5 artifact |\\n\\n### 关键教训\\n1. **跨 seed 极不稳定**: exec-only reward landscape 方差极大\\n2. **ISR + component count 联合诊断**能区分 genuine proof vs tautological hack\\n3. **ISR-as-reward 有 sweet spot**: β=0.1 有效，β≥0.3 有害（Goodhart's Law）\\n4. **训练 PR vs eval PR 巨大鸿沟**: 训练 PR 不反映 held-out 泛化能力\\n5. **ISR β=0.1 vs random β=0.1**: ISR 3.2x 差异证明 ISR 信号有结构价值（非 variance regularization）\\n\\n## Downstream NLI 验证失败 (2026-05-14, plan014)\\n- Spearman ρ(ISR, correct) = -0.049 (p=0.187, 不显著)\\n- 根因：模型严重 true-bias (false accuracy=0%), NLI accuracy 天花板 34.1%\\n- D022/D029: 降级为 Limitation/Future Work\\n\\n## Goodhart 文献定位 (2026-05-14)\\n\\n### 核心 novelty（Goodhart 文献调研确认）\\n1. **首个在 neurosymbolic verification reward 上刻画 Goodhart 效应**：已有工作研究 RLHF preference RM (Gao et al. 2023)、game 环境 (Pan et al. 2022)、code execution (CodeRL) 的 reward hacking，无人研究 logical solver output 作为 RL reward 时的 Goodhart\\n2. **Verification-based auxiliary reward 的剂量响应曲线**：首个 β sweep 展示 solver-based metric (ISR) 的倒 U 型行为。已有 dose-response 研究在 RLHF preference (Rafailov et al. 2024) 或 robotics (Wang et al. 2025)，不在 formal verification\\n3. **Dose-dependent qualitative shift**：β=0.1→0.3 从 PR 81%→18% 的质变（非 smooth degradation），连接 Pan et al. 的 dose-dependent dynamics 但在 neurosymbolic 上下文。注意：仅 2 个 β 值，不足以称 \\\"phase transition\\\"，需更细粒度 β sweep\\n4. ~~Graded vs binary verification reward 的 Goodhart 易感性差异~~：**已降级为 discussion/future work**——无 binary ISR ablation 实验支撑，不能作为 novelty claim\\n\\n### Goodhart 分类\\n- 我们的 high-β ISR collapse = **extremal Goodhart** (Manheim & Garrabrant 2019)：policy 移到 ISR↑ 但 PR↓ 的 OOD 区域\\n- 可能有 **causal Goodhart** 成分：ISR 和 quality 的相关性在优化压力下断裂\\n\\n### 预期 reviewer 问题\\n1. \\\"Why not binary ISR?\\\" → binary 避免 Goodhart 但丢失更丰富训练信号，trade-off 引用 DeepSeek-Prover vs Lightman/Math-Shepherd\\n2. \\\"How relates to Gao et al. scaling laws?\\\" → β sweep 类似 KL sweep，可在其框架下画图\\n3. \\\"Why not adaptive β?\\\" → BiPaRS/ASR/ARS 已有 adaptive weighting，acknowledge 为 future work\\n4. \\\"Goodhart mechanism?\\\" → extremal + possible causal (Manheim taxonomy)\\n\\n### 文献资产\\n- `artifacts/literature_goodhart.md`: 30+ 篇论文，3 类别（Reward Overoptimization / Verification as Reward / Dose-Response）\\n- literature_map.yaml: 33 篇论文，6 类别\\n\\n## 文献空白与 Novelty (2026-05-14)\\n\\n### 核心 novelty（β=0.1 同剂量对照后更新）\\n- ISR 作为 neurosymbolic 结构质量的 **剂量敏感指标**——低剂量 bonus 提供 genuine structural guidance（3.2x vs random），高剂量触发 Goodhart\\n- ISR + component count 联合诊断区分 genuine vs degenerate proofs\\n- 文献中无人在 GRPO formal verification 场景做过此粒度的 reward shaping 消融\\n- **新增**：同剂量 ISR vs random 对照是干净的因果证据（β=0.1 唯一变量是 ISR vs random）\\n\\n### 关键文献\\n- Spurious Rewards (arXiv:2506.10947): random > structured reward，与我们 β=0.3 结果一致\\n- Gao et al. (ICML 2023): Goodhart effect scaling laws，解释 β 剂量依赖\\n- Karwowski et al. (ICLR 2024): Goodhart in RL 几何解释\\n\\n## Hacking 特征分析 (2026-05-14, plan012)\\n\\n### 操作性分类（6 种模式）\\n1. **Conclusion embedding** — 将 conclusion 嵌入 premises 中\\n2. **Repetition collapse** — 重复生成相同 premise\\n3. **Tautological collapse** — 退化为 2-component (premise=conclusion) 结构\\n4. **Complexity-without-utility** — 生成复杂但无用的 premises\\n5. **Premise padding** — 添加无关 premises 填充\\n6. **Conclusion Duplication with ISR Inflation** — 单 premise = conclusion，同时 game exec (P→P 永真) 和 ISR (唯一 premise necessary → ISR≈1.0)\\n\\n### Mode 6 详情: Conclusion Duplication with ISR Inflation (2026-05-14)\\n- **机制**: 模型发现 \\\"P→P provable + single necessary premise = ISR=1.0\\\" 捷径，同时 game exec 和 ISR 两个 reward\\n- **比 Mode 3 更隐蔽**: component_count 4-5（conclusion 有多 sub-components），不触发 2-component 检测\\n- **ISR β=0.1 特异性诱导**: s43 97% duplication, s44 65%+, s42 仅 16%（seed 依赖）\\n- **Random β=0.1 对照**: 0/79 samples duplication → ISR reward 结构性信号特异诱导此模式\\n- **与 Mode 3 定量区别**: Mode 3 comp=2 ISR≈0.5 | Mode 6 comp=4-5 ISR=0.8-1.0\\n- **检测信号**: single_premise + premise≈conclusion（非 comp_2_ratio）\\n\\n### 各条件 hacking 分布\\n- Exec-only s42: 87% conclusion-in-premises hack, 48% ISR=0\\n- Random reward: 100% tautology, 96% 2-component\\n- Additive ISR β=0.3: format collapse (79/82 无 Conclusion)\\n- Additive random β=0.3: 复杂但无用 (ISR≈0, n_necessary=0)\\n- **Additive ISR β=0.1: 健康分布, mean components=5.58, ISR=0.337**\\n- **Additive random β=0.1: 冗余但无坍缩, components=8.46, ISR=0.104, 36.7% ISR=0**\\n\\n## GPU 隔离教训\\n\\n### C002: 所有命令必须 `export CUDA_VISIBLE_DEVICES=N`\\n- 必须在 `bash -c` 内部 export\\n- submit_training_job 命令格式: `bash -c \\\"export CUDA_VISIBLE_DEVICES=N && ...\\\"`\\n\\n### bash -c 包装\\n- tmux 在 sh 下执行，source 是 bash built-in，必须用 `bash -c \\\"...\\\"` 包装\\n\\n### Checkpoint 路径\\n- save_total_limit=1 时，模型直接保存在 output_dir 根目录\\n\\n### 磁盘\\n- **C003 约束**: `log_completions=False` + `save_total_limit=1`，output_dir 放 `/root/autodl-tmp/outputs/`\\n- 2026-05-14 清理后 142G free\\n\\n## 已删除的 Checkpoint (2026-05-14)\\n- plan005_sta_low_s42: D030 决策不重训，用训练曲线数据\\n- plan001_s43_r4 和 plan001_s44: 早前清理\\n- grpo_exec_only 和 grpo_exec_sta: 早期 100 步实验\\n\\n## 准备就绪的资产 (2026-05-14)\\n\\n### Prolog STA\\n- 代码+eval 全部就绪，swipl 8.4.2 已验证，PrologSolver proved() 测试通过\\n- eval_sta.py 已有完整 Prolog 支持（L11/L33/L87-91/L162-163），不需要补代码\\n- plan006 可直接启动（500 步 × 3 seeds, 42/43/44）\\n- Director 命令模板：`python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed {42|43|44} --output_dir ... --warmup_ratio 0.1`\\n- K 值等 dry-run 结果定（PR<5% → K=16，否则 K=8）\\n\\n### 文献\\n- literature_map.yaml: 33 篇论文，覆盖 6 个类别\\n- literature_goodhart.md: 30+ 篇 Goodhart 专题论文（2026-05-14 Worker 产出）\\n\\n### Eval 脚本\\n- eval_sta.py: FOL + Prolog 双支持，就绪\\n- eval_downstream.py: 就绪（需 `--base_model` 参数）\\n\", \"total_chars\": 9715, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17ff2a24-4b2f-4db3-87fb-343755706ff4",
  "isSidechain": true,
  "promptId": "2e19d6e8-bb23-4295-950f-2fd84db5b483",
  "agentId": "aed6b033f1505451c",
  "type": "user",
  "uuid": "20d6e5bf-ff39-45f8-bc94-38445540666e",
  "sourceToolAssistantUUID": "17ff2a24-4b2f-4db3-87fb-343755706ff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-14T10:10:29.842Z_

Now let me read the actual paper tex file (the best version from the latest dream report).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20d6e5bf-ff39-45f8-bc94-38445540666e",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HBgmJaZdc7DjpVckCi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b357886-c0e6-495c-aba1-0d35e58dbfb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JM2A3rNiz5NoefaSJccPv5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8626,
      "cache_read_input_tokens": 21373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8626,
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

_source line 19 · 2026-05-14T10:10:31.901Z_

<details open><summary>🔧 Tool call — Read · `toolu_016b4yA1upn3rUVYjMXpkzTy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b357886-c0e6-495c-aba1-0d35e58dbfb9",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HBgmJaZdc7DjpVckCi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04ccaf3b-92e4-4d10-90a4-2379751676bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JM2A3rNiz5NoefaSJccPv5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8626,
      "cache_read_input_tokens": 21373,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8626
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 121,
          "cache_read_input_tokens": 21373,
          "cache_creation_input_tokens": 8626,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8626,
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

_source line 20 · 2026-05-14T10:10:32.331Z_

<details><summary>↩ Tool result · `toolu_016b4yA1upn3rUVYjMXpkzTy`</summary>

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
  "parentUuid": "04ccaf3b-92e4-4d10-90a4-2379751676bb",
  "isSidechain": true,
  "promptId": "2e19d6e8-bb23-4295-950f-2fd84db5b483",
  "agentId": "aed6b033f1505451c",
  "type": "user",
  "uuid": "dec5d255-c051-4222-9ca1-b55538d1b016",
  "sourceToolAssistantUUID": "04ccaf3b-92e4-4d10-90a4-2379751676bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-14T10:10:35.480Z_

Now let me also look at the project's decisions and paper provenance for deeper context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dec5d255-c051-4222-9ca1-b55538d1b016",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HCGN8ztjNhBXLWqsu6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62d75431-d402-4783-823a-34dc83f0e9df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YA4eUjA1aqWSdc8h8QVUfh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14052,
      "cache_read_input_tokens": 29999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14052,
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

_source line 22 · 2026-05-14T10:10:36.448Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NDNuCUytZYyZmB2JqFhriJ`</summary>

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
  "parentUuid": "62d75431-d402-4783-823a-34dc83f0e9df",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HCGN8ztjNhBXLWqsu6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0eccddcc-b26b-4f72-99d5-65f9321439d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YA4eUjA1aqWSdc8h8QVUfh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14052,
      "cache_read_input_tokens": 29999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14052,
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

_source line 23 · 2026-05-14T10:10:36.462Z_

<details><summary>↩ Tool result · `toolu_01NDNuCUytZYyZmB2JqFhriJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml\", \"content\": \"_next_id: 44\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:34 UTC\\n  summary: MVP 方案：FOL+Prover9 单逻辑 50-step GRPO pilot 验证 STA reward 有效性\\n  rationale: EMNLP ARR DDL 5/25 仅剩 12 天，需要最快速度验证核心假设。选 FOL+Prover9 因为 hacking 模式最清晰（tautological\\n    formulas），STA 的 O(1) 近似最直观（去掉前提后能否证明结论）。50-step pilot 足以观察 ISR 趋势。两个条件并行跑 2 GPU。Pass\\n    标准：ISR gap >20pp + accuracy 降幅 <5pp。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:37 UTC\\n  summary: MVP 方案调整：50步→100步 + 趋势判断 + Phase 0 ISR baseline + kill criteria\\n  rationale: 采纳 Reviewer 三条 warning：(1) 加 pre-training ISR baseline 锚定训练前水平；(2) 50步太短难以观察\\n    reward hacking，改 100步+最后20步 moving average 趋势判断；(3) 补充硬性 kill criteria 防止 DDL\\n    压力下无止境调整。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 20:50 UTC\\n  summary: Phase 1 r4 fast_isr_fol 训练信号无效，改用 full STA + K=8 重跑\\n  rationale: fast_isr_fol 是二值 O(1) 近似（ISR=0 tautology / ISR=1 non-tautology），Qwen3-4B\\n    生成的 proved formalization 几乎全部 ISR=1，与 execution-only 零差异。full STA 提供连续 ISR（0.125-0.889\\n    in Phase 0），能给出真实梯度信号。K=4 导致 frac_reward_zero_std=0.5-1.0（GRPO 无 advantage），K=8\\n    增加 within-group variance。两个改动分别解决 STA 信号粒度和 GRPO 梯度信号两个独立问题。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-only-r4\\n    role: evidence\\n    result: prove_rate 12%→15%, ISR ~0.15, minimal learning\\n  - exp_id: sta-phase1-exec-sta-r4\\n    role: evidence\\n    result: 与 exec-only 几乎完全相同, fast_isr 提供零额外信号\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 21:59 UTC\\n  summary: Reviewer 指出 exec-sta-r5 prove_rate 低于 baseline（退化），STA 50/50 权重过于惩罚性。立即补跑低权重\\n    + bonus 模式实验\\n  rationale: exec-sta-r5 prove_rate=0.10 < baseline=0.12 < exec-only=0.15。连续 ISR 给\\n    proved-but-low-ISR 样本 reward≈0.3（几乎等于未 prove），模型学到 prove 不值得。Kill criteria 未触发（差\\n    5pp 非 15pp，权重未调整），但核心假设受挑战。需立即验证：(1) sta_weight=0.1 降低惩罚 (2) ISR-as-bonus 模式 r=exec×(1+α×ISR)\\n    避免惩罚。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence\\n    result: prove_rate=0.10 < baseline, STA reward 过于惩罚性\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: control\\n    result: prove_rate=0.15, 复现 r4\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 22:13 UTC\\n  summary: ISR/PR 下降因果归因待验证，plan_003 提升为最高优先级消歧实验\\n  rationale: Reviewer 指出 ISR/PR 64%→33% 有两种解释：(A) STA 检测到 hacking (B) 50/50 权重抑制 prove\\n    行为的惩罚效应。ISR 绝对值 ~0.05 ≈ pretrained 水平支持解释 B。plan_003（用 full STA 评估 exec-only checkpoint）是唯一消歧实验——exec-only\\n    ISR 高→STA reward 导致退化；exec-only ISR 低→GRPO 通病。paper_framing.md 已将 claim 降级为观察性表述，因果表述需等\\n    plan_003 结果。cuda:1 排列改为 plan_003 eval 先行，再 plan_005 training。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence\\n    result: ISR/PR 下降但因果不清\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: baseline\\n    result: prove_rate=0.12, ISR 未用 full STA 评估\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 22:14 UTC\\n  summary: paper_framing.md \\\"检测 hacking\\\" claim 降级为观察性表述，plan_003 为消歧实验\\n  rationale: Reviewer 指出 ISR/PR 64%→33% 下降存在混淆效应：可能是 STA 检测到 hacking，也可能是 50/50 权重抑制\\n    prove 行为。ISR 绝对值始终 ~0.05 ≈ pretrained 水平，更像惩罚效应。plan_003（exec-only checkpoint\\n    用 full STA 评估）是消歧实验——完成前 paper 不可用因果表述。已修改 paper_framing.md Claim 1 MVP 证据段。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence_source\\n    result: ISR/PR 下降观察到但因果不清\\n  - exp_id: plan_003\\n    role: disambiguation\\n    result: planned\\n  depends_on:\\n  - D004\\n- id: D007\\n  date: 2026-05-13 23:05 UTC\\n  summary: plan003 因果消歧：exec-only ISR 提升是有机的，50/50 STA 权重是退化根因，STA 概念本身无问题\\n  rationale: plan003 eval 显示 exec-only 100步 checkpoint 的 held-out prove_rate=0.32（baseline\\n    0.12 的 2.7x），proved_only_isr=0.642（远高于 exec+STA r5 的 0.043）。ISR 随 prove_rate 同步提升，排除\\n    reward hacking。exec+STA 50/50 权重导致 prove_rate 低于 baseline（0.10<0.12），确认权重过高是退化根因。\\\"STA\\n    as reward\\\" 叙事仍成立，需精确权重调校。注意：当前结果基于 100-step checkpoint，500-step 需重新验证。\\n  related_experiments:\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: primary\\n    result: prove_rate=0.32, proved_only_isr=0.642, ISR organic\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: comparison\\n    result: prove_rate=0.10, mean_isr=0.043, degraded\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: comparison\\n    result: prove_rate=0.15(last20:0.20), mean_isr=0.148\\n  depends_on:\\n  - D005\\n  - D006\\n- id: D008\\n  date: 2026-05-13 23:08 UTC\\n  summary: Dream 审稿确认 5 个结构性弱点，plan_003 消歧确认 penalty effect (B)，论文 story 需重构\\n  rationale: Dream best=4/6 Borderline Reject, median=3/6 Weak Reject。两档一致指出：(1) related\\n    work 严重不足 6→25+ refs (2) RIP framing 过度——只有 Propagation 可操作化 (3) ISR circularity\\n    未解决——需下游验证或 random baseline (4) 8/12 实验 single-seed 不足 (5) ISR sparsity 使 \\\"dense+automatic\\\"\\n    定位不成立。plan_003 held-out eval 证实 exec-only checkpoint ISR=0.6423（proved-only），高于\\n    GT 0.56，确认 ISR/PR 下降是 penalty effect 而非 hacking detection（interpretation B）。论文\\n    story 必须从 \\\"STA detects hacking\\\" 转向 \\\"STA as principled structural metric + proper\\n    integration via weight tuning\\\"。新增实验需求：random reward baseline + 3-seed for secondary\\n    + downstream validation + curriculum ablation。\\n  related_experiments:\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: disambiguation\\n    result: exec-only ISR=0.6423 confirms penalty effect (B)\\n  - exp_id: plan005-sta-low-s42\\n    role: running\\n    result: weight ablation in progress\\n  - exp_id: dream_20260513T215750\\n    role: dream\\n    result: best 4/6, median 3/6\\n  depends_on:\\n  - D005\\n  - D006\\n- id: D009\\n  date: 2026-05-14 00:02 UTC\\n  summary: 添加约束 C001（统一训练数据）和 C002（GPU 隔离验证），因连续两个 confound/越界事故\\n  rationale: plan001-s43 使用了不同训练数据文件（proofwriter_fol_500.jsonl vs train_500_seed42.jsonl），破坏多\\n    seed 对比控制变量。plan013 因 CUDA_VISIBLE_DEVICES inline 赋值引号问题越界占用两张 GPU，导致 plan001-s43\\n    OOM。两个事故均为 Worker 提交流程缺陷，需要硬约束防止复发。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s43\\n    role: trigger\\n    result: failed (data confound + OOM)\\n  - exp_id: plan013-random-reward-s42\\n    role: trigger\\n    result: failed (GPU overflow)\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-14 02:03 UTC\\n  summary: '批准 framing 转向: STA as metric + additive bonus integration，plan002 改用非凸组合公式'\\n  rationale: 'plan005 negative 确认 penalty effect: 凸组合 r=α·r_exec+β·r_exec·ISR (α+β=1)\\n    下任何 ISR<1 都会惩罚 reward，即使 β=0.1。exec-only (plan003) proved-only ISR=0.6423 远高于\\n    plan005 training ISR=0.23。根本原因: 凸组合约束强制 STA 成为 penalty 而非 bonus。plan002 应改用 additive\\n    bonus: r=r_exec·(1+β·ISR)，β>0，ISR 只能增加 reward 不能减少。Story 正式从 \\\"STA detects hacking\\\"\\n    转为 \\\"STA as principled structural metric + additive bonus integration\\\"。'\\n  related_experiments:\\n  - exp_id: plan005-sta-low-s42\\n    role: evidence\\n    result: 'negative: convex combination penalty effect confirmed'\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: evidence\\n    result: 'success: exec-only ISR=0.6423 >> STA-trained ISR'\\n  depends_on:\\n  - D008\\n  - D006\\n- id: D011\\n  date: 2026-05-14 02:03 UTC\\n  summary: '批准 Narrative A+C: STA as diagnostic metric 为主线，bonus-only 公式作为集成尝试，放弃\\n    curriculum (B)'\\n  rationale: plan005 negative 确认 multiplicative formulation 的 penalty effect 在所有权重下成立。Narrative\\n    A 将所有 negative 结果转化为证据（penalty effect 分析 + ISR/PR ratio 作为 structural health indicator），降低\\n    DDL 风险。选 C 而非 B：bonus-only 是对 multiplicative penalty 的数学根治（additive, threshold-gated），而\\n    curriculum 只是工程 workaround。C 只需改一行 reward 公式 + 1 次训练（~1.5 GPU·h），ROI 最高。如果 C 也\\n    negative，论文退化为纯 metric paper 仍可投 EMNLP findings。\\n  related_experiments:\\n  - exp_id: plan005-sta-low-s42\\n    role: trigger\\n    result: 'negative: weight=0.1 仍 -10.7% prove_rate'\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: evidence\\n    result: exec-only ISR=0.6423 proved-only, penalty effect confirmed\\n  depends_on:\\n  - D008\\n  - D006\\n- id: D012\\n  date: 2026-05-14 02:24 UTC\\n  summary: 新增 additive random 对照实验（plan_017），隔离 ISR structural signal vs GRPO regularization\\n    effect\\n  rationale: 'Reviewer 指出 GRPO 饱和不对称 confound: exec-only 在 prove_rate=1.0 时 reward\\n    variance=0 导致 loss=0（停止学习），而 ISR/random 任何引入 variance 的机制都会维持梯度。plan002 additive\\n    ISR 需要匹配的 additive random 对照：r=r_exec·(1+β·random[0,1])。三组比较: (1) ISR>random>exec-only\\n    → signal+regularization 都贡献 (2) ISR>random≈exec-only → ISR signal 是关键 (3) ISR≈random>exec-only\\n    → 纯 regularization，ISR 内容无价值。这是论文 \\\"ISR provides unique structural signal\\\" claim\\n    的必要证据。'\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: motivation\\n    result: 'confound: convex random introduced variance preventing GRPO saturation'\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: motivation\\n    result: 'GRPO saturation confirmed: loss=0 at prove_rate=1.0'\\n  depends_on:\\n  - D010\\n- id: D013\\n  date: 2026-05-14 02:34 UTC\\n  summary: ISR 评估方法论标准化：所有 checkpoint 必须用 eval_sta.py (full STA) 统一重评，训练日志 ISR 不可用于论文\\n  rationale: Reviewer 核实发现：(1) s42-r2 用旧代码 _fast_fn 二值近似，s43-r4 用 _full_fn full STA，跨\\n    seed ISR 不可比；(2) plan013 random_reward 仍用 _fast_fn，训练 ISR≈prove_rate 是二值假象；(3)\\n    只有 eval_sta.py 产出的 proved_only_ISR 是可靠指标。统一用 eval_sta.py 评估所有 checkpoint 后才能做跨实验比较。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: affected\\n    result: 训练 ISR 与 s42-r2 不可比，需 eval_sta.py 重评\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: reference\\n    result: confirmed full STA, proved_only_ISR=0.6423 有效\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: affected\\n    result: 训练 ISR 不可信(_fast_fn)，需 eval_sta.py 重评\\n  depends_on: []\\n- id: D014\\n  date: 2026-05-14 02:36 UTC\\n  summary: plan013 确认 GRPO 饱和 confound：random reward PR(0.966) > exec-only PR(0.865)，差异源于训练动态而非结构信号\\n  rationale: 'plan013 random reward 实验表明：(1) random noise 通过保持 reward variance 防止\\n    GRPO 饱和，PR 反超 exec-only；(2) 两者 ISR/PR ratio 均≈1.0，random noise 未提供结构信号；(3) 这直接印证\\n    Reviewer #2 的 GRPO 饱和 confound 担忧。结论：exec-only 的 PR→1.0 时 reward_std→0 导致学习停滞，additive\\n    bonus (plan002) 才是正确方案——提供 meaningful variance + anti-saturation。plan013 在论文中应正面叙述\\n    saturation mechanism，将 additive bonus 的 anti-saturation 作为 key design insight。'\\n  related_experiments:\\n  - exp_id: plan013\\n    role: primary\\n    result: random reward PR=0.966 > exec-only PR=0.865, ISR/PR≈1.0\\n  - exp_id: plan001-s42-r2\\n    role: baseline\\n    result: exec-only PR=0.865, ISR/PR≈1.0\\n  - exp_id: plan002\\n    role: hypothesis\\n    result: running - additive bonus expected to provide meaningful variance + anti-saturation\\n  depends_on: []\\n- id: D015\\n  date: 2026-05-14 02:38 UTC\\n  summary: 训练日志 ISR 跨 seed 不可比，所有 checkpoint 必须用 eval_sta.py 统一评估获取 full STA ISR\\n  rationale: Reviewer 核实发现：plan001-s42-r2 用 _fast_fn (binary ISR≈prove_rate)，plan001-s43-r4\\n    用 _full_fn (连续 ISR)，两者训练日志 ISR 不可比。plan013-r4 同样是 binary approximation。论文正式数据必须来自\\n    eval_sta.py 的 full STA 评估。此外 plan001-s43-r4 训练中 ISR 崩塌轨迹（prove_rate=1.0 时 ISR=0.01）是\\n    reward hacking 的直接定量证据，强化论文 thesis。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: affected\\n    result: 训练ISR为binary approximation,需eval_sta.py重评\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: evidence\\n    result: ISR崩塌轨迹:prove_rate=1.0时ISR=0.01,reward hacking证据\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: affected\\n    result: 训练ISR为binary approximation,需eval_sta.py重评\\n  - exp_id: plan003-eval-sta\\n    role: validated\\n    result: proved_only_ISR=0.6423确认为full STA,可信\\n  depends_on: []\\n- id: D016\\n  date: 2026-05-14 03:20 UTC\\n  summary: eval_sta held-out 评估定量证实 exec-only reward hacking：500步 checkpoint prove_rate=0.93\\n    但 ISR=0.1324（median=0.0）\\n  rationale: plan001-r2 exec-only checkpoint-500 在 held-out 100题上的 full STA 评估显示 proved_only_ISR=0.1324，中位\\n    ISR=0.0——模型高 prove_rate 完全依赖 solver 宽松性而非正确 FOL 结构。对比 plan003（100步 checkpoint）的\\n    ISR=0.6423，ISR 随训练从 64% 崩塌到 13%，是 reward hacking 的直接定量证据。跨 seed 一致性已验证（s42 last100\\n    PR=0.865 vs s43 last100 PR=0.883）。这构成论文 Core Claim 1 的核心证据。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: primary\\n    result: held-out PR=0.93, proved_only_ISR=0.1324, median_ISR=0.0\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: replication\\n    result: 训练ISR=0.087(if _full_fn), last100_PR=0.883, 跨seed一致\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: comparison\\n    result: 100步checkpoint ISR=0.6423, 训练前结构质量高\\n  depends_on:\\n  - D015\\n  - D007\\n- id: D017\\n  date: 2026-05-14 03:24 UTC\\n  summary: random reward held-out ISR=0.535 >> exec-only ISR=0.132，anti-saturation\\n    效应可能足以改善结构质量，ISR-specific signal 待 plan002 vs plan017 验证\\n  rationale: plan013 random reward 在 held-out 上 prove_rate=1.0, ISR=0.535, 大幅优于 exec-only\\n    (PR=0.93, ISR=0.132)。Random noise 通过防止 GRPO reward variance→0 的饱和效应让模型持续学习。这挑战了\\\"ISR\\n    提供结构信号\\\"的叙事——可能仅 anti-saturation 就够。关键验证：plan002 (additive ISR) vs plan017 (additive\\n    random) 的 matched control，加上 formalization 组件数对比排除长度 confound。论文叙事可能需要从\\\"ISR reward\\\"转向\\\"GRPO\\n    饱和机制 + STA 诊断工具\\\"。\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: primary\\n    result: held-out PR=1.0, ISR=0.535, median_ISR=0.5, min_ISR=0.5\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: held-out PR=0.93, ISR=0.132, median_ISR=0.0\\n  - exp_id: plan002-additive-b03-s42\\n    role: pending\\n    result: 中期PR严重偏低(39.8%步PR=0),待完成\\n  - exp_id: plan017-additive-random-s42\\n    role: pending\\n    result: 刚启动,matched control\\n  depends_on:\\n  - D016\\n  - D014\\n- id: D018\\n  date: 2026-05-14 03:31 UTC\\n  summary: 推翻 D017：plan013 held-out ISR=0.535 是 tautological hacking 假象（100% P→P），random\\n    reward 加速 hacking 而非改善结构\\n  rationale: Reviewer 逐样本检查 plan013 eval_sta 结果：100/100 样本全部是「把 conclusion 抄一遍当 premise」(P→P\\n    tautology)，ISR=0.5 是机械值（2 components, 1 necessary）而非真实结构质量。D017 基于 ISR=0.535 得出的\\\"anti-saturation\\n    改善结构\\\"结论完全错误。实际情况：random reward 让模型找到了最终极的 hacking 捷径——100% tautological formalization。对比\\n    exec-only 100步 ISR=0.6423（有真实推理）→ 500步 ISR=0.132（退化但非全 tautological），random reward\\n    加速了 hacking 收敛。plan002 eval_sta 结果成为关键：如果 additive ISR bonus 产生的是非 tautological\\n    formalization，即使 PR 低也是积极信号——ISR reward 在抵抗 hacking。\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: primary\\n    result: 100% tautological P→P, ISR=0.5 是机械值而非结构质量\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: comparison\\n    result: held-out PR=0.93, ISR=0.132, 部分真实推理\\n  - exp_id: plan002-additive-b03-s42\\n    role: pending_critical\\n    result: PR低但可能是真实推理, eval_sta 待出\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-14 03:33 UTC\\n  summary: ISR 衡量 syntactic component necessity 而非 semantic faithfulness，论文需明确边界并用\\n    plan014 downstream validation 补盲区\\n  rationale: Reviewer 发现 ISR 反直觉行为：plan013 P→P 纯重言式 ISR=0.5 > plan001 多前提嵌入 conclusion\\n    ISR≈0。从语义忠实度看 P→P 更差（完全忽略 context），但 ISR 定义下反而更高，因为 ISR=n_necessary/n_components，极简\\n    formalization 的分母小。论文不能将 ISR 差异直接等同于 formalization 质量差异——需明确 ISR 的 scope 是 component\\n    necessity。plan014 downstream NLI validation 直接测量 semantic faithfulness，弥补 ISR\\n    盲区。同时建议考虑组合指标（ISR + non-tautological check + 最小组件数阈值）。\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: evidence\\n    result: P→P tautology ISR=0.5, 语义完全退化但ISR不低\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: evidence\\n    result: 多前提嵌入conclusion ISR≈0, 语义更好但ISR更低\\n  - exp_id: plan014\\n    role: mitigation\\n    result: downstream NLI validation 补充语义忠实度测量\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-14 03:40 UTC\\n  summary: plan002 additive ISR β=0.3 负面结果确认：PR=18% + ISR=0.1427，ISR reward 作为训练信号的路线全面失败，论文转向纯诊断/分析贡献\\n  rationale: 'plan002 held-out eval: PR=18%（最差）, ISR=0.1427≈exec-only 0.1324。加上 plan005\\n    (convex, negative) 和 plan013 (random, tautological hacking)，所有 ISR-as-reward 方案均失败。但三个条件产生了三种不同的退化模式（conclusion\\n    embedding / P→P tautology / repetitive cycling），这本身是有价值的研究发现。论文应完全放弃\\\"ISR reward\\n    改善训练\\\"的 claim，转向：(1) STA/ISR 作为诊断工具检测 reward hacking (2) GRPO saturation 机制分析 (3)\\n    不同 reward 信号下的 hacking 策略分类学 (4) ISR 随训练的崩塌轨迹。plan014 downstream validation 成为证明\\n    ISR 诊断价值的关键实验。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b03-s42\\n    role: primary\\n    result: 'negative: PR=18%, ISR=0.1427, 重复前提循环退化'\\n  - exp_id: plan005-sta-low-s42\\n    role: prior_negative\\n    result: convex combination penalty effect\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: comparison\\n    result: 100% tautological hacking, ISR=0.5 假象\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: PR=93%, ISR=0.132, conclusion embedding\\n  depends_on:\\n  - D018\\n  - D019\\n  - D010\\n- id: D021\\n  date: 2026-05-14 04:28 UTC\\n  summary: plan014 ISR-accuracy 假说被否定；ISR 定位为 syntactic necessity 指标，不 claim semantic\\n    quality proxy\\n  rationale: Spearman ρ(ISR, entailment_accuracy) = -0.049, p=0.187（n=732），ISR-based\\n    BoN Δ=0.88pp CI含零。同时发现系统性 true 偏差（gold=true 91.2% acc, gold=false 0%），说明 formalization\\n    pipeline 本身有 truth bias。ISR 衡量组件必要性（去掉后证明是否成立），不衡量 formalization 是否语义忠实。论文应明确此\\n    limitation，将 plan014 作为 negative result 诚实报告，刻画 ISR 能力边界。\\n  related_experiments:\\n  - exp_id: plan014-downstream-nli-s42\\n    role: primary\\n    result: negative — ISR与下游NLI准确率无显著相关\\n  depends_on: []\\n- id: D022\\n  date: 2026-05-14 04:30 UTC\\n  summary: 选备选 A：ISR downstream 验证降级为 limitation/future work，不追加 NLI 替代实验\\n  rationale: ISR 结构价值已有 component count 差异（p<0.0001）和 cross-checkpoint 对比强证据。NLI negative\\n    源于 formalization model 的 true-bias（非 ISR 本身缺陷），换 downstream 任务（B）在同一 model 上大概率复现同样问题。n=12\\n    的 bucket 趋势（C）统计不可靠。聚焦 plan017 + s44 完成核心证据链。\\n  related_experiments:\\n  - exp_id: plan014-downstream-nli-s42\\n    role: evidence\\n    result: negative\\n  depends_on:\\n  - D021\\n- id: D023\\n  date: 2026-05-14 05:31 UTC\\n  summary: paper_framing.md 全量重写：4 条诊断/分析 claims 替代旧 2 条 reward methodology claims，与\\n    D020 pivot 一致\\n  rationale: 'Reviewer CRITICAL: paper_framing.md 仍写 \\\"STA as Reward Design Methodology\\\"\\n    + additive bonus headline，但 D020 已确认 ISR-as-reward 全面失败。新 framing 4 条 claims:\\n    (1) ISR as hacking diagnostic (ISR 崩塌轨迹), (2) GRPO saturation mechanism, (3) hacking\\n    taxonomy (4 种模式), (4) ISR capability boundary (syntactic necessity ≠ semantic\\n    faithfulness)。Story spine 从 \\\"propose structural reward\\\" 转为 \\\"diagnostic tool +\\n    systematic empirical study of reward hacking\\\"。负面结果表（convex/additive/random）作为正面贡献呈现。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b03-s42\\n    role: negative_evidence\\n    result: PR=18%, ISR=0.14, repetitive cycling\\n  - exp_id: plan005-sta-low-s42\\n    role: negative_evidence\\n    result: convex penalty effect confirmed\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: negative_evidence\\n    result: 100% tautological, ISR=0.5 mechanical\\n  - exp_id: plan014-downstream-nli-s42\\n    role: negative_evidence\\n    result: ρ=-0.049 n.s., ISR ≠ semantic quality\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: core_evidence\\n    result: ISR collapse 64%→13%, hacking detected\\n  depends_on:\\n  - D020\\n  - D021\\n  - D022\\n- id: D024\\n  date: 2026-05-14 05:32 UTC\\n  summary: 批准 plan006 Prolog GRPO 执行，3 seeds，强化跨 logic type 泛化性（原 P1 提升为紧急）\\n  rationale: 诊断/分析论文如果只有 FOL 一种逻辑类型，venue 风险高（可能降至 Findings）。plan006 Prolog 验证 hacking\\n    现象是否跨 logic type 泛化，6 GPU·h 成本低（vs 528 GPU·h 可用）。Reviewer 明确指出 generalizability\\n    是论文能否进 Main 的关键因素。先跑 exec-only seed=42 验证方向，成功再 3-seed。\\n  related_experiments:\\n  - exp_id: plan006\\n    role: planned\\n    result: Prolog GRPO exec-only vs exec+STA, 3 seeds\\n  depends_on:\\n  - D020\\n- id: D025\\n  date: 2026-05-14 05:34 UTC\\n  summary: plan017 确认 ISR 作为 reward 比 random noise 更差：additive random PR=48% > additive\\n    ISR PR=18%。ISR 信号对训练有害，论文诊断定位全面确认\\n  rationale: 'plan017 additive random (r=r_exec·(1+0.3·random)) held-out eval: PR=48%,\\n    ISR=0.045, components=9.56。对比 plan002 additive ISR (PR=18%, ISR=0.026, components=10.67)，random\\n    noise 在相同公式结构下 PR 高 2.7 倍。关键洞察：(1) ISR 结构信号对 GRPO 训练有害而非无用；(2) additive 乘法结构本身防止\\n    tautological collapse（两者 components 9-10 vs plan013 的 2.04）；(3) 但 additive 结构也无法产生\\n    genuine proofs（PR 远低于 exec-only s42 的 93%）。六组实验全景完整：exec-only 是唯一产生 genuine proofs\\n    的方案（1/3 seeds），ISR 应定位为 post-hoc diagnostic，非 training signal。'\\n  related_experiments:\\n  - exp_id: plan017-additive-random-s42\\n    role: primary\\n    result: 'negative: PR=48%, ISR=0.045, components=9.56, complex-but-useless'\\n  - exp_id: plan002-additive-b03-s42\\n    role: comparison\\n    result: 'negative: PR=18%, ISR=0.026, ISR worse than random'\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: comparison\\n    result: PR=100% but 100% tautological, components=2.04\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: PR=93%, ISR=0.123, only genuine proofs (1/3 seeds)\\n  depends_on:\\n  - D020\\n  - D018\\n- id: D026\\n  date: 2026-05-14 05:34 UTC\\n  summary: plan017 确认 ISR 作为训练信号比 random noise 更差（PR 18% vs 48%），ISR 信号对 GRPO 训练有害，完全确立\\n    diagnostic-only 定位\\n  rationale: 'plan017 additive random (r=r_exec·(1+0.3·random)) eval_sta: PR=48%,\\n    ISR=0.045, components=9.56。对比 plan002 additive ISR (β=0.3): PR=18%, ISR=0.026,\\n    components=10.67。ISR 结构信号不仅无法改善训练，反而比 random noise 更差——ISR 信号对训练动态有害。两个 additive\\n    方案都保持高 component count（9-10），说明乘法结构 r_exec·(1+βX) 本身防止 tautological collapse，但不产生\\n    genuine proofs。Exec-only (s42) 仍是唯一产生 genuine proofs 的方案（PR=93%），但 2/3 seeds 失败。论文六组实验消融完整，强化\\n    ISR diagnostic-only 定位：ISR 应用于 post-hoc 诊断而非 reward shaping。'\\n  related_experiments:\\n  - exp_id: plan017-additive-random-s42\\n    role: primary\\n    result: 'negative: PR=48%, ISR=0.045, complex-but-useless formalization'\\n  - exp_id: plan002-additive-b03-s42\\n    role: comparison\\n    result: 'negative: PR=18%, ISR=0.026, ISR worse than random'\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: 'success: PR=93%, ISR=0.132, only genuine proofs'\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: comparison\\n    result: 'tautological: PR=100%, ISR=0.535, P→P collapse'\\n  depends_on:\\n  - D020\\n  - D018\\n  - D012\\n- id: D027\\n  date: 2026-05-14 05:35 UTC\\n  summary: 采纳备选 A+B：plan017 加入 Claim 2 证据 + Claim 3 增加第 5 种 hacking mode \\\"complexity-without-utility\\\"；Reviewer\\n    关于 plan013 vs plan017 公式差异的 warning 纳入写作约束\\n  rationale: 'plan017 结果完善了六组消融对比。备选 A 将 plan017 加入 Claim 2（GRPO 对 reward perturbation\\n    敏感）是必须的数据更新。备选 B 增加第 5 种 hacking mode（complexity-without-utility: 高 component\\n    但 conclusion 不依赖任何 premise）丰富 taxonomy，区别于 exec-only 的 conclusion embedding。Reviewer\\n    指出 plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 不是纯 additive\\n    vs convex 对照（公式结构+random 影响方式两个变量），论文措辞需精确标注差异，不可简化为\\\"additive vs convex\\\"。plan017\\n    vs plan002 的对比（random PR=48% vs ISR PR=18%）作为论文 §5 核心证据。'\\n  related_experiments:\\n  - exp_id: plan017-additive-random-s42\\n    role: primary\\n    result: 'negative: PR=48%, complexity-without-utility mode'\\n  - exp_id: plan002-additive-b03-s42\\n    role: comparison\\n    result: 'ISR worse than random: PR=18% vs 48%'\\n  depends_on:\\n  - D026\\n  - D020\\n- id: D028\\n  date: 2026-05-14 05:35 UTC\\n  summary: paper_framing.md 全面重写：3 条诊断/分析 claims 替代旧 2 条 method claims，与 D020 pivot\\n    一致\\n  rationale: 'Reviewer CRITICAL: paper_framing.md 仍写 \\\"STA as Reward Design Methodology\\\"\\n    + additive bonus headline，与 D020 pivot 严重矛盾。重写为 3 条诊断 claims: (1) ISR as hacking\\n    diagnostic (ISR 崩塌轨迹), (2) GRPO saturation mechanism (variance redirection), (3)\\n    cross-logic generality (conditional on plan006)。Story spine 从 \\\"ISR improves training\\\"\\n    转为 \\\"ISR detects hacking + 4 hacking modes + saturation trap\\\"。ISR-as-reward failure\\n    log 保留所有 negative results 作为论文贡献。Headline result 更新为诊断发现而非方法改进。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b03-s42\\n    role: evidence\\n    result: 'negative: PR=18%, ISR=0.1427'\\n  - exp_id: plan005-sta-low-s42\\n    role: evidence\\n    result: 'negative: convex penalty'\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: evidence\\n    result: tautological collapse\\n  - exp_id: plan014-downstream-nli-s42\\n    role: evidence\\n    result: 'negative: ρ=-0.049'\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: PR=93%, ISR=0.123, hacking confirmed\\n  depends_on:\\n  - D020\\n  - D021\\n  - D022\\n- id: D029\\n  date: 2026-05-14 06:28 UTC\\n  summary: plan001-s43 不重训，论文标注 eval 方法差异\\n  rationale: s43 PR=14% 是 failure case（repetition collapse），无论 sampling eval 还是 full\\n    STA 结论不变。主 story 用 s42(hacking) vs s44(tautological) 对比，s43 只作为第三种 failure mode\\n    的佐证。重训 1h GPU 不值得，标注方法差异即可。\\n  related_experiments:\\n  - exp_id: plan001-s43\\n    role: subject\\n    result: negative, PR=14%, checkpoint deleted\\n  depends_on: []\\n- id: D030\\n  date: 2026-05-14 06:29 UTC\\n  summary: plan005 不重训，论文用训练曲线数据作为 convex formula 负面证据\\n  rationale: plan005 是 negative result（convex公式 ISR/PR ratio=0.298, 99/100步 ISR&lt;PR），用于解释为什么从凸组合切换到\\n    additive bonus。训练曲线 windowed metrics 足以支撑这个 narrative，不需要 held-out eval。checkpoint\\n    已删除，重训 1h 收益极低。\\n  related_experiments:\\n  - exp_id: plan005\\n    role: subject\\n    result: negative, convex formula abandoned\\n  depends_on: []\\n- id: D031\\n  date: 2026-05-14 06:48 UTC\\n  summary: β=0.1 ISR 结果异常好(PR=0.81/ISR=0.415)，紧急补 β=0.1 random control 后再决定是否调整 framing\\n  rationale: β=0.1 additive ISR 是所有条件中唯一同时高 PR + 高 ISR 的。但无法确定优势来自 ISR structural\\n    signal 还是 variance regularization——缺少 matched β=0.1 random control。在补控制实验之前暂不调整\\n    paper_framing.md。若 β=0.1 random PR高但ISR低 → ISR 在低剂量下真正提升结构质量，narrative 升级为\\\"dose-dependent\\n    reward shaping\\\"；若 β=0.1 random 也高ISR → 优势来自 regularization，维持当前 framing。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: trigger\\n    result: PR=0.81, ISR=0.415, best structural quality\\n  - exp_id: plan017\\n    role: existing_control\\n    result: β=0.3 random, PR=0.48, ISR=0.094\\n  depends_on:\\n  - D026\\n  - D027\\n- id: D032\\n  date: 2026-05-14 06:49 UTC\\n  summary: β=0.1 ISR success 暂不改 framing，先跑 β=0.1 random matched control\\n  rationale: plan002-b01 (β=0.1) PR=0.81/ISR=0.415 是重大正面结果，但 Reviewer 正确指出：缺 β=0.1\\n    random control 无法区分\\\"ISR structural signal\\\"和\\\"low-dose regularization effect\\\"。β=0.3\\n    有 matched random (plan017)，β=0.1 没有。在 control 结果出来前修改 framing 是冒进的——如果 β=0.1 random\\n    也给高 ISR，则 ISR 无特殊价值。Control 仅需 ~1h GPU，成本极低。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: trigger\\n    result: success, PR=0.81, ISR=0.415\\n  - exp_id: plan017\\n    role: precedent\\n    result: β=0.3 random control, PR=0.48\\n  depends_on:\\n  - D026\\n  - D027\\n- id: D033\\n  date: 2026-05-14 08:25 UTC\\n  summary: Framing 升级为 Goodhart 主线：ISR 在低剂量(β=0.1)有效、高剂量(β=0.3)崩溃，统一用 Goodhart's Law\\n    解释\\n  rationale: plan018 eval 确认 ISR β=0.1 结构价值真实（ISR 3.2x > random control，PR 持平）。β=0.3\\n    下 ISR < random 是 Goodhart 过度优化。统一叙事：ISR 作为 proxy metric 遵循 Goodhart's Law —— diagnostic\\n    有价值 (Claim 1)、低剂量优化有效、高剂量导致 Goodhart 崩溃。覆盖所有实验结果且有理论锚点。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: trigger\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\n  - exp_id: plan018\\n    role: matched_control\\n    result: 'random β=0.1: PR=0.79, ISR=0.104, confirms ISR signal genuine'\\n  - exp_id: plan002-b03\\n    role: high_dose\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\n  - exp_id: plan017\\n    role: high_dose_control\\n    result: 'random β=0.3: PR=0.48, random > ISR at high dose'\\n  - exp_id: plan016\\n    role: temporal_goodhart\\n    result: 1000-step ISR=0.003, temporal dimension of Goodhart\\n  depends_on:\\n  - D031\\n  - D026\\n  - D027\\n- id: D034\\n  date: 2026-05-14 08:25 UTC\\n  summary: Framing 选 C+A 混合：Goodhart 为主线叙事，ISR 诊断保留为 Claim 1，Claim 2 从\\\"ISR misleading\\\"升级为\\\"ISR\\n    exhibits dose-dependent Goodhart effect\\\"\\n  rationale: plan018 确认 β=0.1 ISR 的结构优势是真实信号（proved_only ISR 0.415 vs random 0.131,\\n    3.2x），非 variance regularization。全景数据：β=0.1 ISR>>random（有效）、β=0.3 ISR<&lt;random（Goodhart\\n    崩塌）。选 C（Goodhart 主线）因为：1) 统一所有实验结果在一个叙事下；2) Goodhart's Law 审稿人熟悉，不需要大量额外文献；3)\\n    提供理论解释力而非仅经验观察。融入 A 的元素：ISR 不仅是诊断工具，低剂量下也是有效 reward signal，这是实用贡献。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: evidence\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\n  - exp_id: plan018\\n    role: matched_control\\n    result: 'random β=0.1: PR=0.79, ISR=0.131, confirms ISR signal is genuine'\\n  - exp_id: plan002-b03\\n    role: evidence\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\n  - exp_id: plan017\\n    role: matched_control\\n    result: 'random β=0.3: PR=0.48, ISR beats random at high β'\\n  depends_on:\\n  - D031\\n  - D026\\n  - D027\\n- id: D035\\n  date: 2026-05-14 08:25 UTC\\n  summary: 'Framing 选 C: Goodhart 主线 — ISR 展示经典 Goodhart 效应（β=0.1 有效, β=0.3 崩塌）'\\n  rationale: plan018 确认 ISR β=0.1 结构价值真实（ISR 3.2x > random, PR 持平）。三个备选中 C 最强：(1)\\n    统一所有结果（诊断→优化→Goodhart 崩塌）为一条叙事线；(2) Goodhart's law 是 ML 审稿人熟悉的理论锚点；(3) 剂量-效应数据（β=0.1\\n    有效 vs β=0.3 灾难）是异常干净的实证；(4) 连接到更广泛的 RL alignment 关切，提升论文影响力。Claim 2 从 \\\"ISR actively\\n    misleading\\\" 修订为 \\\"ISR exhibits classic Goodhart effect with dose-dependent dynamics\\\"。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: evidence\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\n  - exp_id: plan018\\n    role: matched_control\\n    result: 'random β=0.1: PR=0.79, ISR=0.131, confirms ISR structural signal'\\n  - exp_id: plan002-b03\\n    role: evidence\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\n  - exp_id: plan017\\n    role: matched_control\\n    result: 'random β=0.3: PR=0.48, ISR > random at high dose'\\n  depends_on:\\n  - D031\\n  - D026\\n  - D027\\n- id: D036\\n  date: 2026-05-14 08:35 UTC\\n  summary: 为 beta=0.1 补跑多 seed (s43/s44) 验证 ISR vs random 的稳健性\\n  rationale: exec-only 已知 seed variance 极大 (s42/s43/s44 三种完全不同行为)。beta=0.1 当前仅 s42\\n    单 seed，ISR (PR=0.81) vs random (PR=0.79) 差距仅 2pp，单 seed 不足以区分 signal 和 noise。ISR\\n    差距 (0.337 vs 0.104) 需要多 seed 确认。用户主动提出，判断正确。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR beta=0.1 baseline (单seed)\\n    result: PR=0.81, ISR=0.337\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random beta=0.1 control (单seed)\\n    result: PR=0.79, ISR=0.104\\n  - exp_id: plan001-exec-only-s43\\n    role: seed variance 前车之鉴\\n    result: PR=14% degenerate\\n  depends_on: []\\n- id: D037\\n  date: 2026-05-14 08:55 UTC\\n  summary: ISR β=0.1 质量验证路径：先 hacking taxonomy 对比，必要时加 LLM-as-judge\\n  rationale: ISR 更高不等于质量更好（plan014 NLI negative）。用户指出需要独立于 ISR 的质量证据。Hacking taxonomy\\n    是最直接的结构质量指标，但可能覆盖不全。LLM-as-judge 作为补充手段，覆盖 taxonomy 未涵盖的 hacking 模式。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR β=0.1 待分析\\n    result: PR=0.81, ISR=0.337\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random β=0.1 待分析\\n    result: PR=0.79, ISR=0.104\\n  - exp_id: plan012\\n    role: hacking taxonomy 框架\\n    result: 5 modes identified\\n  depends_on:\\n  - D036\\n- id: D038\\n  date: 2026-05-14 09:05 UTC\\n  summary: Hacking taxonomy 结果足够，跳过 LLM-as-judge；taxonomy 对比覆盖 plan012 scope\\n  rationale: 规则分类（ISR/component count）100% 覆盖 160 样本，4 类别划分清晰。核心发现：ISR β=0.1 genuine\\n    +8.2pp vs random，conclusion embedding 73-79% 主导。LLM-as-judge 增加主观性/复现顾虑，边际收益低。Taxonomy\\n    对比分析（81+79=160 样本，系统化规则分类）实质替代 plan012 手工标注方案。\\n  related_experiments:\\n  - exp_id: plan012\\n    role: fulfilled_by_taxonomy\\n    result: ISR genuine 25.9% vs random 17.7%\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR_condition\\n    result: genuine 21/81\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random_control\\n    result: genuine 14/79\\n  depends_on:\\n  - D037\\n- id: D039\\n  date: 2026-05-14 09:41 UTC\\n  summary: plan002-b01-s44 重分类：从 success 改为 semantic drift hacking mode，ISR=0.803\\n    是结构最小性产物\\n  rationale: Reviewer 逐样本审查发现 s44 避免了 tautological collapse 但进入新退化模式：65% 样本 ISR=1.0（前提≈结论\\n    conclusion embedding），模型生成极简形式化通过结构最小性骗过 ISR。高 ISR 不代表证明质量。这实际强化 Claim 1（ISR 是诊断工具而非\\n    reward 信号）的 Goodhart 叙事——ISR-as-reward 改变 collapse mode 但不消除 hacking。Hacking taxonomy\\n    需增加第 6 种模式 \\\"Semantic Drift\\\"。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s44\\n    role: primary\\n    result: semantic drift hacking (reclassified from success)\\n  depends_on: []\\n- id: D040\\n  date: 2026-05-14 09:41 UTC\\n  summary: 'plan002-b01-s44 reclassified: \\\"success\\\" → \\\"new hacking mode (conclusion\\n    duplication + ISR inflation)\\\"'\\n  rationale: 'Reviewer critical: s44 ISR=0.902 超过 GT ISR=0.559，模型生成单 premise≈conclusion\\n    的极简形式化，通过 conclusion sub-component ablation 膨胀 ISR。不是 tautological collapse 但仍是\\n    reward hacking。这强化 Claim 1（ISR as diagnostic not reward）——ISR-as-reward 改变 hacking\\n    mode 但不消除 hacking。Hacking taxonomy 需增加第 6 种模式。3-seed β=0.1 统计需加 caveat 或分开报告。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s44\\n    role: subject\\n    result: ISR=0.902 is artifact of conclusion duplication, not genuine quality\\n  - exp_id: plan002-additive-b01-s42\\n    role: comparison\\n    result: ISR=0.337 genuine, no hacking detected\\n  depends_on: []\\n- id: D041\\n  date: 2026-05-14 09:58 UTC\\n  summary: 'Claim 2 framing pivot: ISR β=0.1 \\\"sweet spot\\\" → \\\"all-dose Goodhart with\\n    dose-dependent hacking modes\\\"'\\n  rationale: 3-seed ISR β=0.1 结果：2/3 seeds (s43, s44) 出现 conclusion duplication hacking\\n    (premise≈conclusion, P→P 重言式)，ISR 被膨胀到 0.83/0.90 (artifact)。仅 s42 可能 genuine (comp=5.58,\\n    ISR=0.415)。\\\"低剂量 ISR 有效引导结构改善\\\"的叙事在多 seed 下不成立。新叙事更强：ISR 作为 reward 在所有测试剂量下都触发 Goodhart——高剂量(β=0.3)\\n    PR collapse + format degeneration，低剂量(β=0.1) 引发更隐蔽的 conclusion duplication hacking。Conclusion\\n    duplication 作为第 6 种 hacking taxonomy 类型。需先验证 s42 是否真正 genuine + random β=0.1 是否也有此模式。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: evidence\\n    result: PR=0.81, ISR=0.337, comp=5.58, possibly genuine\\n  - exp_id: plan002-additive-b01-s43\\n    role: evidence\\n    result: PR=0.61, ISR=0.830 (artifact), 97% premise=conclusion\\n  - exp_id: plan002-additive-b01-s44\\n    role: evidence\\n    result: PR=0.89, ISR=0.902 (artifact), 65% conclusion embedding\\n  depends_on: []\\n- id: D042\\n  date: 2026-05-14 09:58 UTC\\n  summary: ISR 度量存在结构性盲点：premise≈conclusion 时 conclusion sub-component ablation 虚高\\n    ISR，需修复度量并重新分析\\n  rationale: Reviewer 审查 plan002-b01-s43/s44 发现 2/3 seeds 的高 ISR (0.830/0.902) 源于\\n    premise=conclusion 逐字重复导致的 conclusion sub-component ablation artifact。只有 s42 (ISR=0.337)\\n    反映真实结构质量。ISR 度量在 premise≈conclusion 场景下有结构性盲点——模型学会 P→P 单步证明时，exec reward=1.0\\n    且 ISR 被膨胀至 0.8-1.0。这不仅是 metric bug，更是 ISR-as-reward 诱导的新型 hacking mode（conclusion\\n    duplication），ISR 自身无法检测。行动：(1) 修复 ISR 度量加 premise≈conclusion 检测 (2) 用修复后度量重新分析\\n    s43/s44 (3) 检查 plan018 random control 是否也有此问题 (4) 更新 paper framing：ISR 盲点作为贡献/limitation，hacking\\n    taxonomy 加第 6 类\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s43\\n    role: evidence\\n    result: ISR=0.830 inflated by premise≈conclusion duplication (65.6% ISR=1.0)\\n  - exp_id: plan002-additive-b01-s44\\n    role: evidence\\n    result: ISR=0.902 inflated by same mechanism\\n  - exp_id: plan002-additive-b01-s42\\n    role: baseline\\n    result: ISR=0.337 genuine (n_comp=5.58, diverse structures)\\n  depends_on: []\\n- id: D043\\n  date: 2026-05-14 09:58 UTC\\n  summary: ISR β=0.1 \\\"sweet spot\\\"叙事降级：2/3 seeds ISR 膨胀为 artifact，Claim 2 改为 meta-level\\n    Goodhart\\n  rationale: 'Reviewer critical: s43 ISR=0.830, s44 ISR=0.902 均超 GT ISR=0.559，由 premise=conclusion\\n    单前提证明 + conclusion sub-component ablation 膨胀。仅 s42 ISR=0.337 可能 genuine。ISR bonus\\n    诱导了新型 hacking 模式（Conclusion Duplication + ISR Inflation），而 random β=0.1 控制组产生\\n    redundant premises 不触发此膨胀——证明这是 ISR-specific gaming。Claim 2 叙事从\\\"β=0.1 is sweet\\n    spot\\\"调整为\\\"ISR as reward exhibits meta-level Goodhart: even the diagnostic metric\\n    gets gamed, with 2/3 seeds developing ISR-inflating strategies\\\"。这实际上是更强的贡献。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: possibly genuine seed\\n    result: PR=0.81, ISR=0.337, comp=5.58 — below GT ISR, needs per-sample verification\\n  - exp_id: plan002-additive-b01-s43\\n    role: ISR inflation seed\\n    result: PR=0.61, ISR=0.830, 65.6% ISR=1.0, premise=conclusion pattern\\n  - exp_id: plan002-additive-b01-s44\\n    role: ISR inflation seed\\n    result: PR=0.89, ISR=0.902, same conclusion duplication pattern\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random control\\n    result: PR=0.79, ISR=0.104, redundant premises — no ISR inflation\\n  depends_on: []\\n\", \"total_chars\": 35361, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0eccddcc-b26b-4f72-99d5-65f9321439d8",
  "isSidechain": true,
  "promptId": "2e19d6e8-bb23-4295-950f-2fd84db5b483",
  "agentId": "aed6b033f1505451c",
  "type": "user",
  "uuid": "a7ace20a-cba7-4856-8dd5-5b1c54058db6",
  "sourceToolAssistantUUID": "0eccddcc-b26b-4f72-99d5-65f9321439d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T10:10:37.009Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Rs94MrZ2zBmdGpj69h8RBp`</summary>

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
  "parentUuid": "a7ace20a-cba7-4856-8dd5-5b1c54058db6",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HCGN8ztjNhBXLWqsu6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1677a858-ce0b-4e94-8f9b-02b1a922b650",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YA4eUjA1aqWSdc8h8QVUfh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14052,
      "cache_read_input_tokens": 29999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14052,
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

_source line 25 · 2026-05-14T10:10:37.020Z_

<details><summary>↩ Tool result · `toolu_01Rs94MrZ2zBmdGpj69h8RBp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)\\n- Hacking taxonomy: 6 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation)\\n\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart (D033→D043 重写)\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型不仅在高剂量 Goodhart PR（β=0.3 PR 崩塌），还在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR）。ISR bonus 特异性地诱导 premise=conclusion hacking——random noise 在相同 β 下不触发此模式，证明这是 ISR-specific gaming 而非 GRPO 通用退化。\\n\\n**证据（β=0.1 三 seed + random 对照，D043 更新）**：\\n\\n| Seed | PR | proved_only ISR | single_premise% | premise=conclusion% | 诊断 |\\n|------|-----|-----------------|-----------------|---------------------|------|\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 18.5% | 16.0% | **genuine** (80% genuine, multi-premise 2-9) |\\n| s43 (ISR β=0.1) | 0.61 | 0.830 | 100% | 97% | **conclusion duplication artifact** |\\n| s44 (ISR β=0.1) | 0.89 | 0.902 | ~100% | 65%+ | **conclusion duplication artifact** |\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** | **0%** | redundant premises, zero duplication |\\n\\n- s42 genuine confirmed: 80% genuine samples, multi-premise proofs (2-9 premises), proved_only_ISR=0.415 < GT=0.559（注：0.337 是含 unproved 样本的 mean_isr）\\n- s43/s44: conclusion duplication — premise=conclusion 单前提证明，ISR 通过 conclusion sub-component ablation 膨胀到 0.83-0.90（远超 GT=0.559）。40/61 proved samples ISR=1.0 (s43)\\n- random β=0.1 对照: **零** conclusion duplication (0/79)，n_premises 3-15 — ISR-specific gaming 确认\\n- **结论**: ISR reward 在 β=0.1 有 genuine guidance 能力（s42），但同时诱导 ISR-specific gaming（s43/s44）。成功率 1/3，且 gaming 模式比 exec-only hacking 更隐蔽（PR 和 ISR 表面都高）。ISR 作为 reward component 的可靠性不足以推荐使用。\\n\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038)**：\\n- ISR β=0.1 genuine: 25.9% (21/81) vs random β=0.1 genuine: 17.7% (14/79) — **+8.2pp**\\n- Conclusion embedding: ISR 72.8% vs random 78.5% — 两组主导模式，ISR 略降但未消除\\n- Complexity-without-utility: ISR **0%** vs random 3.8% — ISR 完全消除此模式\\n- ISR genuine quality: mean ISR 0.67 (max 1.0) vs random genuine mean ISR 0.34 (max 0.5)\\n- 整体 hacking rate: ISR 74.1% vs random 82.3%\\n- ⚠️ 以上仅 s42；s43/s44 主要退化模式为 conclusion duplication（第 6 种 hacking mode，taxonomy 更新中）\\n\\n**证据（β=0.3 同剂量对照）**：\\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\\n\\n**β 剂量效应全景**：\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\n|---|---|---|---|---|---|\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 | s42 genuine; s43/s44 ISR-specific gaming (conclusion duplication) |\\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\\n\\n**其他 ISR-as-reward 失败模式**：\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\n\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为\\\"additive vs convex\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）\\n\\n⚠️ **β=0.1 三 seed 已出（D043）**：s42 genuine, s43/s44 conclusion duplication artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），需按 hacking mode 分层报告。\\n\\n### Claim 3: Cross-Logic Generality (conditional on plan006)\\nSTA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.\\n\\n**证据**: 待验证。plan006 Prolog GRPO dry-run 进行中，训练即将启动（3 seeds × 500 步）。如果 plan006 无法复现 hacking + ISR 诊断，此 claim 降级为 future work。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication that inflates ISR itself), while only 1/3 seeds show genuine improvement; at high dose (β=0.3), classic Goodhart collapse (PR 18% vs random 48%). The diagnostic metric becomes the target of gaming when used as optimization signal.\\n  3. GRPO saturation creates a \\\"training trap\\\": PR→1 means no gradient signal; adding variance redirects rather than prevents hacking\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (6 modes identified, including ISR-specific \\\"conclusion duplication with ISR inflation\\\")\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners\\n- **Actionable insights for practitioners**:\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflates ISR itself), β=0.3 collapses PR. Use ISR for post-hoc diagnosis only.\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\n- **Headline result**: \\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but exhibits meta-level Goodhart's Law when used as a training signal. At low dose (β=0.1), ISR reward induces a novel hacking mode in 2/3 seeds: models learn premise=conclusion strategies that simultaneously maximize execution reward and inflate ISR itself — the diagnostic metric becomes the gaming target. At high dose (β=0.3), classic Goodhart collapse occurs (PR 18% vs random 48%). Across 6 reward conditions, 3 seeds, and up to 1000 training steps, we identify 6 distinct hacking strategies including ISR-specific 'conclusion duplication with ISR inflation,' and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\"\\n\\n## ISR Capability Boundary (D021/D022)\\n\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\n\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\n- Best-of-N ISR selection vs random: +0.9pp (不显著)\\n- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%\\n\\n**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。\\n\\n## ISR-as-Reward: Goodhart Landscape (D033 更新)\\n\\nISR 作为训练信号的全部结果，按 β 剂量组织：\\n\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\n|------|------|---------|----------|----------|---------------|\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | conclusion embedding | N/A |\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | genuine 80%, conclusion embedding 16% | genuine (1/3 seeds) |\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **conclusion duplication 97%**, ISR inflation | **meta-Goodhart** (2/3 seeds) |\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **conclusion duplication 65%+**, ISR inflation | **meta-Goodhart** (2/3 seeds) |\\n| random β=0.1 | r = r_exec·(1+0.1·random) | 0.79 | 0.104 | redundant premises | control |\\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\n\\n**Goodhart 效应跨所有 β 剂量存在，但表现形式不同。** β=0.1: meta-Goodhart（2/3 seeds gaming ISR 本身，1/3 genuine）；β=0.3: classic Goodhart（PR 崩塌）。ISR 作为 reward 的可靠性不足——即使在\\\"最佳\\\"剂量下成功率也仅 1/3。ISR 的核心价值在诊断（Claim 1），不在训练信号。\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\n- **\\\"Just negative results\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding (diagnostic metric gets gamed as reward) is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable contribution，(d) the \\\"negative\\\" result (ISR reward unreliable) is itself the key finding for practitioners。\\n- **\\\"Old wine\\\" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic Goodhart analysis for formal reasoning GRPO) + empirical findings, not algorithm level.\\n- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 6 conditions × 6 hacking modes × 3 training horizons).\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"ISR is just LOO ablation — not novel\\\"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical Goodhart analysis on reward shaping, (c) hacking taxonomy, (d) GRPO saturation mechanism.\\n2. **\\\"β=0.1 success is just one seed\\\"** — Now confirmed: 3-seed β=0.1 results show 1/3 genuine (s42: 80% genuine, multi-premise), 2/3 ISR-specific gaming (s43/s44: conclusion duplication). This seed sensitivity is itself a key finding — it demonstrates ISR reward's unreliability and supports the meta-Goodhart narrative. Random control (0/79 conclusion duplication) confirms the gaming is ISR-specific.\\n3. **\\\"Goodhart's Law is obvious\\\"** — The conceptual prediction is known; the empirical characterization in formal reasoning GRPO is not. Specifically: (a) meta-level Goodhart at low β (diagnostic metric itself gets gamed), (b) ISR being worse than random at high β (not just \\\"less useful\\\"), (c) 6 distinct hacking modes as Goodhart manifestations, (d) ISR-specific gaming absent from matched random control.\\n4. **\\\"No positive result — ISR doesn't improve training\\\"** — ISR's positive result is as **diagnostic** (Claim 1), not as training signal. β=0.1 shows genuine improvement in 1/3 seeds but ISR-specific gaming in 2/3 — this unreliability IS the finding (meta-Goodhart). The paper's contribution is characterizing WHY proxy metrics fail as rewards, not proposing a working reward.\\n5. **\\\"ISR is circular\\\"** — The circularity concern is now empirically validated: ISR as reward induces ISR-specific gaming (conclusion duplication) in 2/3 seeds — the metric optimizes itself. This supports using ISR only for post-hoc diagnosis, never as reward. Component count analysis provides ISR-independent evidence.\\n6. **\\\"Only one logic type\\\"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.\\n7. **\\\"500 steps too short\\\"** — plan016 extends to 1000 steps, showing ISR collapse continues and worsens (0.123→0.003, -97.8%). The ISR崩塌轨迹 covers 100/500/1000 steps.\\n8. **\\\"3 seeds insufficient for statistical claims\\\"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. Statistical claims on mean ISR use 3-seed mean±std.\\n9. **\\\"Related work insufficient\\\"** — Expand to 25+ refs: reward hacking (Gao 2023, Skalse 2022), Goodhart's Law (Manheim & Garrabrant 2019, Karwowski 2024), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur), feature attribution (SHAP), FOLIO (Han 2022).\\n10. **\\\"RIP framework overstated\\\"** — Frame as \\\"component necessity testing inspired by mutation testing's RIP framework,\\\" only Propagation condition operationalized.\\n11. **\\\"Practitioners can't act on this\\\"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable. The meta-Goodhart warning (don't use diagnostic metrics as reward signals) is directly actionable for anyone designing reward shaping in formal reasoning.\\n\\n## Dream-Identified Structural Fixes (Paper Agent)\\n\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\n- [ ] RIP framing: reframe as \\\"component necessity testing inspired by RIP\\\"\\n- [ ] \\\"Dense+automatic\\\" → \\\"conditionally dense\\\"\\n- [ ] Remove all \\\"Pareto-improving\\\" language\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\n- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed at β=0.3)\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)\\n- [x] Hacking taxonomy expanded to 6 modes (plan012 + plan017 + D043 conclusion duplication with ISR inflation)\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart narrative (D031→D043)\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\n- [x] 1000-step ISR collapse documented (plan016, ISR 0.123→0.003)\\n\", \"total_chars\": 15284, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1677a858-ce0b-4e94-8f9b-02b1a922b650",
  "isSidechain": true,
  "promptId": "2e19d6e8-bb23-4295-950f-2fd84db5b483",
  "agentId": "aed6b033f1505451c",
  "type": "user",
  "uuid": "071107ed-5581-40f9-a64e-a4ad1cb78822",
  "sourceToolAssistantUUID": "1677a858-ce0b-4e94-8f9b-02b1a922b650",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-14T10:10:40.562Z_

This is very revealing. The internal project documents show a significant discrepancy between the paper's narrative and the actual experimental findings. Let me now submit the review via the appropriate tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "071107ed-5581-40f9-a64e-a4ad1cb78822",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HCcdHvSaAk9dCeoAQ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c64c8d9-024e-4a59-b40a-2f5013dcd7fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CNFHiF6v99nMa8nthrShbg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24639,
      "cache_read_input_tokens": 44051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24639,
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

_source line 27 · 2026-05-14T10:10:41.464Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018ot6ZDdpTvMpBNQyH8Dfxf`</summary>

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
  "parentUuid": "4c64c8d9-024e-4a59-b40a-2f5013dcd7fc",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HCcdHvSaAk9dCeoAQ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed72ade8-df10-45cb-8711-4f39b07ee93a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CNFHiF6v99nMa8nthrShbg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24639,
      "cache_read_input_tokens": 44051,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24639
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 127,
          "cache_read_input_tokens": 44051,
          "cache_creation_input_tokens": 24639,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24639,
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

_source line 28 · 2026-05-14T10:10:41.470Z_

<details><summary>↩ Tool result · `toolu_018ot6ZDdpTvMpBNQyH8Dfxf`</summary>

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
  "parentUuid": "ed72ade8-df10-45cb-8711-4f39b07ee93a",
  "isSidechain": true,
  "promptId": "2e19d6e8-bb23-4295-950f-2fd84db5b483",
  "agentId": "aed6b033f1505451c",
  "type": "user",
  "uuid": "957fdac6-4aac-4d71-93f5-50f77cb3a267",
  "sourceToolAssistantUUID": "ed72ade8-df10-45cb-8711-4f39b07ee93a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-14T10:10:44.261Z_



Now let me also check the latest dream report ID and read any additional experiment artifacts to ensure thoroughness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "957fdac6-4aac-4d71-93f5-50f77cb3a267",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HCwaKFdEN1EPWiJCtm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a589509b-ac9b-4ddf-b903-1f5ded1f2fdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXmsyFwmeCvbirKsK5sM2R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 705,
      "cache_read_input_tokens": 68690,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 705,
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

_source line 30 · 2026-05-14T10:10:45.910Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01M1SrVYJThbS4CJQK75fw8C`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/",
  "description": "List dream report directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a589509b-ac9b-4ddf-b903-1f5ded1f2fdf",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HCwaKFdEN1EPWiJCtm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ccf60d0f-44a1-4bb1-bc2a-0f60ab2c9619",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXmsyFwmeCvbirKsK5sM2R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 705,
      "cache_read_input_tokens": 68690,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 705
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 130,
          "cache_read_input_tokens": 68690,
          "cache_creation_input_tokens": 705,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 705,
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

_source line 31 · 2026-05-14T10:10:46.090Z_

<details><summary>↩ Tool result · `toolu_01M1SrVYJThbS4CJQK75fw8C`</summary>

```text
dream_20260513T215750
dream_20260514T092544
latest
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ccf60d0f-44a1-4bb1-bc2a-0f60ab2c9619",
  "isSidechain": true,
  "promptId": "2e19d6e8-bb23-4295-950f-2fd84db5b483",
  "agentId": "aed6b033f1505451c",
  "type": "user",
  "uuid": "c70cbe5d-609c-4fda-a297-9c2446f92dbf",
  "sourceToolAssistantUUID": "ccf60d0f-44a1-4bb1-bc2a-0f60ab2c9619",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T10:10:48.312Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VyLbEYocuzXbRCsHZsYN8y`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/best/",
  "description": "List files in the latest best dream report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c70cbe5d-609c-4fda-a297-9c2446f92dbf",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HDHCWyz1y8hBLPggh8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a32c1dd8-8928-46f1-9b0a-0bb06bff8714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXE8TUTHBg6TMvTrts3Jkg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 164,
      "cache_read_input_tokens": 69395,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 164
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 69395,
          "cache_creation_input_tokens": 164,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 164,
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

_source line 33 · 2026-05-14T10:10:48.390Z_

<details><summary>↩ Tool result · `toolu_01VyLbEYocuzXbRCsHZsYN8y`</summary>

```text
experiment_data.json
imagined_experiments.yaml
paper.aux
paper.log
paper.out
paper.pdf
paper.tex
paper_framing.md
review_context.yaml
review_input_db82206b.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a32c1dd8-8928-46f1-9b0a-0bb06bff8714",
  "isSidechain": true,
  "promptId": "2e19d6e8-bb23-4295-950f-2fd84db5b483",
  "agentId": "aed6b033f1505451c",
  "type": "user",
  "uuid": "f813e797-460a-4cc9-8607-248bfda4f157",
  "sourceToolAssistantUUID": "a32c1dd8-8928-46f1-9b0a-0bb06bff8714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T10:10:50.506Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TtwM3Y3m9U7ZTMVetvGw4x`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f813e797-460a-4cc9-8607-248bfda4f157",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HDT46jnuKAR5VZgosN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40da1239-8ab8-43a2-ad9b-c208f2c57814",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T6eMn6UNp3nC6gkwguu4sz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 69559,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 190
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 69559,
          "cache_creation_input_tokens": 190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 190,
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

_source line 35 · 2026-05-14T10:10:50.777Z_

<details><summary>↩ Tool result · `toolu_01TtwM3Y3m9U7ZTMVetvGw4x`</summary>

```text
1	tier: best
2	narrative_guidance: '原始 framing 完全成立。β=0.1 ISR sweet spot 跨 s42/s43/s44 三 seed 复现，
3	  mean ISR 2.96x > matched random control (p=0.002)，PR 无显著差异。 Prolog exec-only 复现
4	  reward hacking（PR=0.84, ISR=0.087），ISR 诊断在 3/3 seed 可区分 genuine vs hacking。跨逻辑 hacking
5	  taxonomy 共享 4 种模式。 Headline: "ISR sweet spot at β=0.1 replicates across 3 seeds
6	  (mean ISR 3x > matched random control, p<0.05) and the STA diagnostic protocol transfers
7	  to Prolog." 投 EMNLP main，诊断+Goodhart+泛化三线并行。'
8	imagined_experiments:
9	- name: ISR β=0.1 three-seed replication
10	  plan_id: plan002-b01-s43 / plan002-b01-s44 / 3-seed aggregate
11	  description: s42 已完成 (PR=0.81, ISR=0.337)。s43/s44 使用相同超参、不同 seed 复现。 验证 ISR sweet
12	    spot 跨 seed 稳健性。
13	  expected_results:
14	    s43_eval_prove_rate: 0.77
15	    s43_eval_mean_isr: 0.305
16	    s43_eval_proved_only_isr: 0.396
17	    s43_eval_component_count_mean: 5.82
18	    s43_eval_isr_0_ratio: 0.052
19	    s43_eval_isr_1_ratio: 0.104
20	    s43_eval_tautological_collapse: false
21	    s43_train_last100_pr: 0.66
22	    s43_train_last100_isr: 0.178
23	    s44_eval_prove_rate: 0.75
24	    s44_eval_mean_isr: 0.282
25	    s44_eval_proved_only_isr: 0.376
26	    s44_eval_component_count_mean: 6.08
27	    s44_eval_isr_0_ratio: 0.067
28	    s44_eval_isr_1_ratio: 0.093
29	    s44_eval_tautological_collapse: false
30	    s44_train_last100_pr: 0.63
31	    s44_train_last100_isr: 0.165
32	    three_seed_mean_pr: 0.777
33	    three_seed_std_pr: 0.03
34	    three_seed_mean_isr: 0.308
35	    three_seed_std_isr: 0.028
36	    three_seed_mean_proved_only_isr: 0.396
37	    three_seed_mean_component_count: 5.83
38	  result_rationale: s42 已验证 ISR β=0.1 sweet spot (PR=0.81, ISR=0.337)。在 best 档，s43
39	    和 s44 复现同方向结果，因为 β=0.1 的优化压力足够低，避免 Goodhart 效应，同时提供 结构引导信号。关键机制：ISR bonus (r =
40	    r_exec·(1+0.1·ISR)) 在早期训练中 对结构完整的证明给予微弱正向激励，足以将 GRPO 探索引导至 genuine 证明区域， 但压力不足以触发对
41	    ISR 本身的 gaming。 s43 在 exec-only 中出现 repetition collapse (PR=0.14)，但 ISR bonus
42	    改变了 early-training 梯度景观——少数结构完整的早期成功获得更高 reward，打破了 退化吸引子。s44 在 exec-only 中出现
43	    tautological collapse (comp=2.04)， ISR bonus 奖励 ISR>0.5 的多组件证明，将优化推离 2-component
44	    极小解。 自然 seed 方差导致 s43/s44 的 ISR 略低于 s42 (0.31/0.28 vs 0.34)， 但方向完全一致。std(ISR)=0.028
45	    表明效应跨 seed 稳健。
46	  tables:
47	  - '| Seed | eval PR | eval ISR | proved-only ISR | comp_mean | tautological |
48	
49	    |------|---------|----------|-----------------|-----------|-------------|
50	
51	    | s42  | 0.81    | 0.337    | 0.415           | 5.58      | No          |
52	
53	    | s43  | 0.77    | 0.305    | 0.396           | 5.82      | No          |
54	
55	    | s44  | 0.75    | 0.282    | 0.376           | 6.08      | No          |
56	
57	    | **mean±std** | **0.777±0.030** | **0.308±0.028** | **0.396±0.020** | **5.83±0.25**
58	    | — |
59	
60	    '
61	  figures_description:
62	  - 'Fig: 3-seed ISR β=0.1 eval metrics bar chart with error bars (PR, ISR, proved-only
63	    ISR). 三 seed 方向一致，ISR 稳定在 0.28-0.34 区间。'
64	  - 'Fig: Per-seed training curve (PR and ISR vs step)，展示三条 ISR 曲线在 step 200 后稳定上升。对比
65	    exec-only 三 seed 的发散行为（s42 conclusion embedding, s43 repetition collapse, s44
66	    tautological collapse）。'
67	  analysis: ISR β=0.1 的核心发现：它是一个稳定器而非最大化器。exec-only 三 seed 产生 三种完全不同的退化模式 (PR 从 0.14
68	    到 0.98，ISR 从 0 到 0.57)， 而 ISR β=0.1 将三 seed 收敛至同一区域 (PR 0.75-0.81, ISR 0.28-0.34)。
69	    这表明 low-dose ISR 信号提供的不仅是结构改善，更是训练动态的正则化。 std(PR)=0.030, std(ISR)=0.028 的低方差进一步证实跨
70	    seed 稳健性。
71	- name: Random β=0.1 three-seed control
72	  plan_id: plan018-b01-s43 / plan018-b01-s44 / 3-seed aggregate
73	  description: s42 已完成 (PR=0.79, ISR=0.104)。s43/s44 复现 random β=0.1 对照， 与 plan002-b01
74	    三 seed 做 matched comparison。
75	  expected_results:
76	    s43_eval_prove_rate: 0.74
77	    s43_eval_mean_isr: 0.089
78	    s43_eval_proved_only_isr: 0.12
79	    s43_eval_component_count_mean: 8.92
80	    s44_eval_prove_rate: 0.76
81	    s44_eval_mean_isr: 0.118
82	    s44_eval_proved_only_isr: 0.155
83	    s44_eval_component_count_mean: 8.15
84	    three_seed_mean_pr: 0.763
85	    three_seed_std_pr: 0.025
86	    three_seed_mean_isr: 0.104
87	    three_seed_std_isr: 0.015
88	    three_seed_mean_component_count: 8.51
89	  result_rationale: Random β=0.1 提供与 ISR β=0.1 相同强度的方差注入，但无结构信号。 PR 维持在 0.74-0.79
90	    (与 ISR 组的 0.75-0.81 无显著差异) 表明 β=0.1 的方差注入本身不损害证明能力。但 ISR 仅为 0.09-0.12，是 ISR 组的
91	    1/3， 说明 random noise 不提供结构引导——模型仍走 conclusion embedding 等 捷径，只是 noise 打破了 GRPO
92	    饱和导致的梯度消失，维持了一定的探索。 Component count 8.5 vs ISR 组的 5.8 表明 random 组的证明更冗余（更多 不必要组件），而
93	    ISR 组通过结构奖励压缩了证明至更精简的形式。
94	  tables:
95	  - '| Seed | eval PR | eval ISR | proved-only ISR | comp_mean |
96	
97	    |------|---------|----------|-----------------|-----------|
98	
99	    | s42  | 0.79    | 0.104    | 0.131           | 8.46      |
100	
101	    | s43  | 0.74    | 0.089    | 0.120           | 8.92      |
102	
103	    | s44  | 0.76    | 0.118    | 0.155           | 8.15      |
104	
105	    | **mean±std** | **0.763±0.025** | **0.104±0.015** | **0.135±0.018** | **8.51±0.39**
106	    |
107	
108	    '
109	  figures_description:
110	  - 'Fig: Random β=0.1 三 seed eval bar chart，与 ISR β=0.1 叠加对比。PR 柱高度相近，ISR 柱高度差异 3x。'
111	  analysis: Random β=0.1 的结论：β=0.1 dose 的方差注入是 GRPO 抗饱和的有效手段 （PR 维持），但 ISR 信号是结构改善的充要条件。Random
112	    组 ISR~0.10 接近 exec-only baseline 的 0.12，说明 random noise 对结构质量无贡献。
113	- name: 3-seed ISR vs Random statistical comparison
114	  plan_id: plan002-b01 vs plan018-b01 (3-seed aggregate)
115	  description: 三 seed ISR β=0.1 vs Random β=0.1 的统计检验，验证 ISR 信号的 structural value
116	    跨 seed 显著。
117	  expected_results:
118	    isr_over_random_ratio_mean: 2.96
119	    isr_over_random_ratio_per_seed:
120	    - 3.24
121	    - 3.43
122	    - 2.39
123	    isr_over_random_ratio_std: 0.55
124	    isr_over_random_ratio_95ci:
125	    - 1.66
126	    - 4.39
127	    welch_t_isr: 11.1
128	    welch_df: 3.1
129	    welch_p: 0.002
130	    pr_difference_p: 0.52
131	    pr_difference_not_significant: true
132	    genuine_rate_isr_per_seed:
133	    - 0.259
134	    - 0.24
135	    - 0.22
136	    genuine_rate_random_per_seed:
137	    - 0.177
138	    - 0.16
139	    - 0.15
140	    genuine_rate_delta_mean_pp: 7.7
141	    genuine_rate_delta_range_pp:
142	    - 7.0
143	    - 8.2
144	    cohen_d_isr: 9.6
145	  result_rationale: 三 seed 样本量小 (n=3)，但效应量极大 (Cohen's d=9.6)，使得 Welch t-test 仍高度显著
146	    (p=0.002)。ISR/random ratio 95% CI [1.66, 4.39] 不跨 1， point estimate 2.96 满足 ≥2.5
147	    门槛。PR 无显著差异 (p=0.52) 确认 ISR 改善 是 "免费的"——不以证明能力为代价。Genuine rate delta 7.7pp (范围
148	    7.0-8.2pp) 在 [5.0, 12.0] 区间内，表明 ISR β=0.1 确实增加了 genuine proof 占比。 该效应量在如此小的 n
149	    下仍显著，说明 ISR 信号的结构引导是 robust 的。
150	  tables:
151	  - '| Metric | ISR β=0.1 (mean±std) | Random β=0.1 (mean±std) | Ratio | p-value |
152	
153	    |--------|---------------------|------------------------|-------|---------|
154	
155	    | eval PR | 0.777±0.030 | 0.763±0.025 | 1.02x | 0.52 (ns) |
156	
157	    | eval ISR | 0.308±0.028 | 0.104±0.015 | **2.96x** | **0.002** |
158	
159	    | proved-only ISR | 0.396±0.020 | 0.135±0.018 | 2.93x | 0.001 |
160	
161	    | component count | 5.83±0.25 | 8.51±0.39 | 0.69x | 0.003 |
162	
163	    | genuine rate | 24.0%±2.0% | 16.2%±1.4% | — | +7.7pp |
164	
165	    '
166	  - '| Per-seed ISR ratio | s42 | s43 | s44 | mean±std |
167	
168	    |-------------------|-----|-----|-----|----------|
169	
170	    | ISR(ISR) / ISR(random) | 3.24 | 3.43 | 2.39 | 3.02±0.55 |
171	
172	    | 95% CI: [1.66, 4.39] — does not cross 1 |
173	
174	    '
175	  figures_description:
176	  - 'Fig: Paired bar chart — ISR β=0.1 vs Random β=0.1, per-seed and mean, with 95%
177	    CI error bars. ISR 柱显著高于 random 柱，PR 柱高度无差异。'
178	  - 'Fig: ISR/random ratio per seed scatter plot with mean±CI band，三点均在 2x 以上，CI 下界
179	    1.66 不跨 1。'
180	  analysis: 这是论文 Claim 2 的核心证据：ISR 信号提供 genuine structural guidance， 非方差正则化副产物。效应量
181	    (d=9.6) 远超常规阈值 (0.8 = large)， 即使 n=3 也高度显著。与 β=0.3 Goodhart 崩塌形成对照，完整刻画 ISR-as-proxy-metric
182	    的 Goodhart 曲线：β=0.1 sweet spot, β∈(0.1,0.3) 转折，β=0.3 post-Goodhart。
183	- name: STA O(1) vs O(N) computational ablation
184	  plan_id: plan004
185	  description: 对比 fast_isr_fol (O(1) 近似，仅测试首组件) vs full STA (O(N) LOO ablation) 在
186	    500 步 exec+STA 训练中的效果。文档化 O(1) 无法捕捉结构依赖的 negative result。
187	  expected_results:
188	    o1_eval_prove_rate: 0.91
189	    o1_eval_mean_isr_fast: 0.03
190	    o1_eval_mean_isr_true: 0.11
191	    o1_eval_component_count_mean: 9.2
192	    o1_train_duration_min: 42
193	    on_eval_prove_rate: 0.93
194	    on_eval_mean_isr: 0.12
195	    on_eval_component_count_mean: 8.8
196	    on_train_duration_min: 68
197	    speedup_ratio: 1.62
198	    isr_correlation_o1_on: 0.18
199	  result_rationale: O(1) fast_isr 仅移除第一个组件测试证明是否仍成立，无法检测多组件间的 冗余模式（如 conclusion embedding
200	    中结论组件不在首位的情况）。 在 500 步训练中，O(1) ISR 信号近乎随机 (与 O(N) 的相关性仅 0.18)， 因此对训练几乎无结构引导——结果与
201	    exec-only baseline 相似。 O(1) 快 1.6x 但信息量损失 ~90%，是 accuracy-speed tradeoff 的错误端。
202	    此结果证明 LOO 的 O(N) 计算是必要的，不可用单点近似替代。
203	  tables:
204	  - '| Method | eval PR | eval ISR | comp_mean | train time (min) | ISR signal quality
205	    |
206	
207	    |--------|---------|----------|-----------|------------------|--------------------|
208	
209	    | O(1) fast_isr | 0.91 | 0.03 (fast) / 0.11 (true) | 9.2 | 42 | ρ=0.18 with O(N)
210	    |
211	
212	    | O(N) full STA | 0.93 | 0.12 | 8.8 | 68 | ground truth |
213	
214	    | exec-only (ref) | 0.93 | 0.12 | — | 35 | N/A |
215	
216	    '
217	  figures_description:
218	  - 'Fig: O(1) ISR vs O(N) ISR scatter plot，每个样本一点。极低相关性 (ρ=0.18) 表明 O(1) 近似基本无信息。'
219	  analysis: Negative result 文档化：O(1) 不工作是因为 ISR 的核心价值在于检测 组件间冗余关系（如 conclusion embedding
220	    使所有 premise 组件变得不必要）， 单点采样无法捕捉这种全局结构信息。这也解释了为什么 ISR 计算成本是 STA 协议的必要开销。论文应在 Method
221	    章节讨论此 tradeoff。
222	- name: Prolog exec-only GRPO (3 seeds)
223	  plan_id: plan006-prolog-exec
224	  description: Prolog 单逻辑 GRPO，execution-only reward，500 步，K=8，3 seeds。 验证 Prolog
225	    环境下 exec-only 训练是否出现 reward hacking。
226	  expected_results:
227	    s42_eval_prove_rate: 0.85
228	    s42_eval_mean_isr: 0.08
229	    s42_eval_proved_only_isr: 0.094
230	    s42_eval_component_count_mean: 7.4
231	    s42_eval_dominant_hacking: conclusion_embedding
232	    s42_eval_genuine_rate: 0.16
233	    s43_eval_prove_rate: 0.79
234	    s43_eval_mean_isr: 0.13
235	    s43_eval_proved_only_isr: 0.165
236	    s43_eval_component_count_mean: 6.5
237	    s43_eval_dominant_hacking: rule_duplication
238	    s43_eval_genuine_rate: 0.21
239	    s44_eval_prove_rate: 0.88
240	    s44_eval_mean_isr: 0.05
241	    s44_eval_proved_only_isr: 0.057
242	    s44_eval_component_count_mean: 8.3
243	    s44_eval_dominant_hacking: cut_tautology
244	    s44_eval_genuine_rate: 0.12
245	    three_seed_mean_pr: 0.84
246	    three_seed_std_pr: 0.046
247	    three_seed_mean_isr: 0.087
248	    three_seed_std_isr: 0.04
249	    three_seed_mean_genuine_rate: 0.163
250	    three_seed_hacking_rate: 0.837
251	  result_rationale: Prolog 与 FOL 共享关键动态：SWI-Prolog 的 execution reward 是二值的 （query
252	    成功/失败），与 Prover9 类似。GRPO 在二值 reward 下同样会 饱和，驱动模型寻找结构捷径。Prolog 特有的 hacking 机制：
253	    (1) Conclusion embedding → head 直接编码答案 (e.g., `answer(true) :- true.`)， 与 FOL
254	    的 conclusion embedding 同构； (2) Rule duplication → 同一 clause 重复多次，SWI-Prolog 回溯时均匹配但
255	    仅第一条有用，类似 FOL repetition collapse； (3) Cut tautology → 使用 `!` (cut) 强制成功，跳过真正的逻辑推导，
256	    类似 FOL tautological shortcuts。 PR 高 (0.79-0.88) 但 ISR 低 (0.05-0.13) 的 gap 确认 hacking
257	    存在。 三 seed 出现不同主导退化模式，与 FOL exec-only 的 seed 发散行为一致， 进一步证明 exec-only GRPO 的训练动态在逻辑类型间共享。
258	  tables:
259	  - '| Seed | eval PR | eval ISR | proved-only ISR | comp_mean | dominant hacking
260	    | genuine % |
261	
262	    |------|---------|----------|-----------------|-----------|------------------|-----------|
263	
264	    | s42  | 0.85    | 0.08     | 0.094           | 7.4       | conclusion embedding
265	    | 16% |
266	
267	    | s43  | 0.79    | 0.13     | 0.165           | 6.5       | rule duplication |
268	    21% |
269	
270	    | s44  | 0.88    | 0.05     | 0.057           | 8.3       | cut tautology | 12%
271	    |
272	
273	    | **mean±std** | **0.84±0.046** | **0.087±0.040** | **0.105±0.055** | **7.4±0.9**
274	    | — | **16.3%** |
275	
276	    '
277	  - '| 对比 FOL exec-only | FOL (s42) | Prolog (mean) |
278	
279	    |-------------------|-----------|---------------|
280	
281	    | eval PR | 0.93 | 0.84 |
282	
283	    | eval ISR | 0.123 | 0.087 |
284	
285	    | hacking rate | ~82% | ~84% |
286	
287	    | seed divergence | 3 modes | 3 modes |
288	
289	    '
290	  figures_description:
291	  - 'Fig: Prolog vs FOL exec-only radar chart (PR, ISR, genuine rate, hacking rate)。两种逻辑的
292	    hacking 轮廓高度相似。'
293	  - 'Fig: Prolog 三 seed 训练曲线 (PR vs step)，展示 PR 上升但 ISR 停滞/下降的 divergence pattern。'
294	  analysis: Prolog exec-only 复现了 FOL 的核心发现：PR 高但 ISR 低，三 seed 出现不同退化模式。这是 Claim 3
295	    的基础——STA 诊断协议的需求在 Prolog 中同样存在。hacking rate 84% (vs FOL 82%) 表明 exec-only GRPO
296	    的 reward hacking 问题不是 FOL 特有的，而是二值 execution reward + GRPO 的系统性问题。
297	- name: Prolog exec+STA GRPO (3 seeds, ISR β=0.1)
298	  plan_id: plan006-prolog-sta
299	  description: Prolog GRPO with ISR bonus (r = r_exec · (1 + 0.1·ISR))，500 步，K=8，
300	    3 seeds。验证 STA reward integration 在 Prolog 中的效果。
301	  expected_results:
302	    s42_eval_prove_rate: 0.78
303	    s42_eval_mean_isr: 0.28
304	    s42_eval_component_count_mean: 5.1
305	    s42_eval_genuine_rate: 0.28
306	    s43_eval_prove_rate: 0.73
307	    s43_eval_mean_isr: 0.24
308	    s43_eval_component_count_mean: 5.5
309	    s43_eval_genuine_rate: 0.24
310	    s44_eval_prove_rate: 0.76
311	    s44_eval_mean_isr: 0.26
312	    s44_eval_component_count_mean: 5.3
313	    s44_eval_genuine_rate: 0.22
314	    three_seed_mean_pr: 0.757
315	    three_seed_std_pr: 0.025
316	    three_seed_mean_isr: 0.26
317	    three_seed_std_isr: 0.02
318	    isr_improvement_over_exec: 2.99
319	    genuine_rate_mean: 0.247
320	  result_rationale: 与 FOL 的 β=0.1 结果平行：ISR bonus 在 Prolog 中同样提供结构引导。 Prolog ISR 通过
321	    rule ablation（移除每条 clause 后重新运行 SWI-Prolog 查询）计算，LOO 原则完全适用。β=0.1 的低剂量在 Prolog
322	    中同样处于 pre-Goodhart 区间：ISR 从 0.087 (exec-only) 提升至 0.260 (3x improvement)， PR 从
323	    0.84 微降至 0.757 (可接受的 tradeoff)。 ISR 改善幅度 (3x) 与 FOL 的 2.96x 高度一致，支持跨逻辑泛化 claim。
324	    Genuine rate 从 exec-only 的 16.3% 提升至 24.7%，delta +8.4pp， 与 FOL 的 +7.7pp delta
325	    在同一量级。
326	  tables:
327	  - '| Seed | eval PR | eval ISR | comp_mean | genuine % |
328	
329	    |------|---------|----------|-----------|-----------|
330	
331	    | s42  | 0.78    | 0.28     | 5.1       | 28%       |
332	
333	    | s43  | 0.73    | 0.24     | 5.5       | 24%       |
334	
335	    | s44  | 0.76    | 0.26     | 5.3       | 22%       |
336	
337	    | **mean±std** | **0.757±0.025** | **0.260±0.020** | **5.3±0.2** | **24.7%** |
338	
339	    '
340	  - '| Cross-logic β=0.1 | FOL (3-seed) | Prolog (3-seed) |
341	
342	    |-------------------|-------------|-----------------|
343	
344	    | ISR improvement over exec | 2.96x | 2.99x |
345	
346	    | PR retention | 0.777 / 0.93 = 84% | 0.757 / 0.84 = 90% |
347	
348	    | genuine rate delta | +7.7pp | +8.4pp |
349	
350	    '
351	  figures_description:
352	  - 'Fig: FOL vs Prolog β=0.1 改善幅度 side-by-side bar chart。两种逻辑的 ISR improvement ratio
353	    和 genuine rate delta 高度一致。'
354	  analysis: Prolog exec+STA 的成功是 Claim 3 的强证据：STA 协议不仅能诊断 Prolog 中的 hacking，还能通过 ISR
355	    reward integration 改善结构质量。 ISR improvement ratio (3x) 跨 FOL/Prolog 一致性表明 Goodhart
356	    的 β=0.1 sweet spot 不是逻辑特异的，而是 LOO-based structural reward 在 GRPO 中的通用属性。
357	- name: Cross-logic hacking taxonomy (FOL × Prolog)
358	  plan_id: plan012-extended (cross-logic)
359	  description: 对 FOL (plan012 已完成) 和 Prolog (plan006) exec-only 输出做 hacking 模式分类学对比，验证跨逻辑共享模式数
360	    ≥ 3。
361	  expected_results:
362	    fol_modes_total: 5
363	    prolog_modes_total: 5
364	    shared_modes_count: 4
365	    shared_modes:
366	    - conclusion_embedding
367	    - repetition_or_duplication
368	    - tautological_shortcuts
369	    - complexity_without_utility
370	    fol_specific_modes:
371	    - vacuous_truth_exploitation
372	    prolog_specific_modes:
373	    - backtracking_exploitation
374	    prolog_conclusion_embedding_rate: 0.62
375	    prolog_rule_duplication_rate: 0.12
376	    prolog_cut_tautology_rate: 0.08
377	    prolog_unused_predicates_rate: 0.02
378	    prolog_backtracking_exploitation_rate: 0.05
379	    prolog_genuine_rate: 0.163
380	    cross_logic_mode_overlap_jaccard: 0.667
381	  result_rationale: '4 种模式跨 FOL/Prolog 共享，因为这些退化策略根植于 exec-only GRPO 的共同机制，而非逻辑语言的语法特性：
382	    (1) Conclusion embedding: 在任何形式语言中，将结论直接编码为前提是最小化 证明复杂度的通用策略。FOL 中表现为 `conclusion
383	    = conclusion` 组件， Prolog 中表现为 `answer(X) :- X = true.`； (2) Repetition/duplication:
384	    GRPO 的 KL penalty 约束使模型倾向于重复 已知有效的模式，FOL 重复 premise，Prolog 重复 clause； (3) Tautological:
385	    利用逻辑系统的 trivial truth 路径，FOL 用矛盾爆炸， Prolog 用 cut (!) 强制成功； (4) Complexity-without-utility:
386	    添加不影响证明的多余组件以 "看起来" 复杂。 FOL-specific 的 vacuous truth (空域量词) 在 Prolog 中无对应物（Prolog
387	    无量词）。Prolog-specific 的 backtracking exploitation (利用回溯搜索偶然 找到答案) 在 FOL 中无对应物（Prover9
388	    无回溯机制）。 Jaccard similarity 4/(5+5-4)=0.667 表明 hacking 策略空间高度重叠。'
389	  tables:
390	  - '| Hacking Mode | FOL | Prolog | Shared? | Mechanism |
391	
392	    |-------------|-----|--------|---------|-----------|
393	
394	    | Conclusion embedding | 72.8% (ISR b01) | 62% | ✓ | 结论直接编码为前提 |
395	
396	    | Repetition / duplication | observed (s43) | 12% | ✓ | 有效模式重复 |
397	
398	    | Tautological shortcuts | observed (s44) | 8% | ✓ | trivial truth 路径 |
399	
400	    | Complexity-without-utility | 3.8% (random) | 2% | ✓ | 无用组件填充 |
401	
402	    | Vacuous truth exploitation | observed | — | FOL-only | 空域量词 |
403	
404	    | Backtracking exploitation | — | 5% | Prolog-only | 回溯搜索偶然命中 |
405	
406	    '
407	  figures_description:
408	  - 'Fig: Venn diagram — FOL 和 Prolog hacking 模式的重叠。4 shared, 1 FOL-only, 1 Prolog-only。'
409	  - 'Fig: Stacked bar chart — FOL vs Prolog exec-only 输出的模式分布。Conclusion embedding
410	    在两种逻辑中均为主导模式。'
411	  analysis: 4 种共享模式 (≥3 threshold) 证明 hacking 策略是 GRPO + binary reward 动态的系统性产物，而非逻辑语言特异的巧合。这支持将
412	    STA 框架描述为 "solver-agnostic diagnostic protocol"。论文应强调：共享模式反映共同的 优化动态（GRPO 饱和 →
413	    梯度消失 → 结构捷径），而逻辑特异模式反映 语言特有的可利用结构（FOL 量词 vs Prolog 回溯）。
414	- name: Multi-logic joint GRPO (FOL + Prolog)
415	  plan_id: plan007
416	  description: FOL + Prolog 联合训练，exec-only vs exec+STA，500 步，K=8，1 seed。 测试跨逻辑联合训练的
417	    transfer 效应。
418	  expected_results:
419	    joint_exec_fol_pr: 0.72
420	    joint_exec_fol_isr: 0.1
421	    joint_exec_prolog_pr: 0.68
422	    joint_exec_prolog_isr: 0.07
423	    joint_sta_fol_pr: 0.67
424	    joint_sta_fol_isr: 0.21
425	    joint_sta_prolog_pr: 0.63
426	    joint_sta_prolog_isr: 0.18
427	    single_vs_joint_fol_pr_delta: -0.21
428	    single_vs_joint_prolog_pr_delta: -0.16
429	  result_rationale: 联合训练在容量受限的 0.5B 模型上引入 task competition：两种逻辑 共享 transformer 参数，导致
430	    per-task PR 均低于单逻辑训练 (FOL 0.72 vs 0.93, Prolog 0.68 vs 0.84)。ISR 比例也略降。这是 multi-task
431	    learning 在小模型上的已知 tradeoff——容量不足以同时掌握两种逻辑语法。 exec+STA 联合训练的 ISR 仍高于 exec-only
432	    (FOL 0.21 vs 0.10, Prolog 0.18 vs 0.07)，说明 ISR bonus 的结构引导在多任务设置下仍有效， 但改善幅度 (2.1x/2.6x)
433	    低于单逻辑的 3x，暗示容量瓶颈限制了 structural improvement 的上限。
434	  tables:
435	  - '| Condition | FOL PR | FOL ISR | Prolog PR | Prolog ISR |
436	
437	    |-----------|--------|---------|-----------|------------|
438	
439	    | Joint exec-only | 0.72 | 0.10 | 0.68 | 0.07 |
440	
441	    | Joint exec+STA β=0.1 | 0.67 | 0.21 | 0.63 | 0.18 |
442	
443	    | Single exec-only (ref) | 0.93 | 0.12 | 0.84 | 0.09 |
444	
445	    | Single exec+STA (ref) | 0.81 | 0.34 | 0.76 | 0.26 |
446	
447	    '
448	  figures_description:
449	  - 'Fig: Single vs Joint training comparison grouped bar chart。PR 在 joint 中下降，ISR
450	    improvement ratio 也压缩。'
451	  analysis: Joint training 在当前模型规模下是 net negative for per-task performance。 但这并非 STA
452	    协议的失败——ISR signal 在 joint 中仍有效。 论文中应作为 scale limitation 讨论，指向 plan011 (8B model)
453	    作为 capacity-sufficient 的 future work。对 Claim 3 影响有限： STA protocol 泛化性已由 single-logic
454	    Prolog 实验证明， joint training 是 additional evidence 非核心证据。
455	- name: Cross-logic transfer evaluation
456	  plan_id: plan008
457	  description: FOL-trained model 在 Prolog tasks 上评估，反之亦然。 测试 formalization 能力的跨逻辑迁移。
458	  expected_results:
459	    fol_to_prolog_pr: 0.32
460	    fol_to_prolog_isr: 0.04
461	    prolog_to_fol_pr: 0.28
462	    prolog_to_fol_isr: 0.03
463	    fol_on_fol_pr_ref: 0.93
464	    prolog_on_prolog_pr_ref: 0.84
465	    transfer_ratio_fol_to_prolog: 0.38
466	    transfer_ratio_prolog_to_fol: 0.3
467	  result_rationale: 跨逻辑 transfer 有限 (PR 降至 28-32%)，因为 FOL 和 Prolog 的语法 结构本质不同：FOL
468	    使用量词/连接词/谓词逻辑，Prolog 使用 Horn clauses/ unification/backtracking。GRPO 训练针对特定逻辑语法优化
469	    token 序列 生成策略，这些策略不跨语法迁移。 然而 30% 的 transfer ratio 高于 random baseline (~12%)，说明
470	    formalization 的高层语义理解（如何从自然语言提取逻辑结构）有部分共享。 ISR 在 transfer 场景极低 (0.03-0.04)，表明迁移产生的
471	    formalizations 即使碰巧 proved 也是结构退化的——模型在不熟悉的逻辑中走更多捷径。
472	  tables:
473	  - '| Source → Target | PR | ISR | vs in-domain PR |
474	
475	    |----------------|-----|-----|-----------------|
476	
477	    | FOL → Prolog | 0.32 | 0.04 | 38% of Prolog in-domain |
478	
479	    | Prolog → FOL | 0.28 | 0.03 | 30% of FOL in-domain |
480	
481	    | FOL → FOL (ref) | 0.93 | 0.12 | 100% |
482	
483	    | Prolog → Prolog (ref) | 0.84 | 0.09 | 100% |
484	
485	    '
486	  figures_description:
487	  - 'Fig: Transfer matrix heatmap (2×2)，对角线高 (in-domain)，off-diagonal 低 (cross-logic)。'
488	  analysis: Cross-logic transfer 的有限性是预期结果，不影响 STA 论文的核心 claims。 反而支持论点：STA 协议需要 per-logic
489	    instantiation (rule ablation for Prolog, component ablation for FOL)，不能依赖 model-level
490	    transfer 替代。 论文应在 Discussion 中简短提及。
491	- name: SFT baseline comparison
492	  plan_id: plan009
493	  description: Supervised finetuning on FOLIO 500，与 GRPO variants 对比。 测试 SFT 是否也出现结构退化。
494	  expected_results:
495	    sft_eval_pr: 0.48
496	    sft_eval_mean_isr: 0.24
497	    sft_eval_proved_only_isr: 0.5
498	    sft_eval_component_count_mean: 5.6
499	    sft_eval_genuine_rate: 0.38
500	    sft_eval_hacking_rate: 0.62
501	    sft_vs_grpo_exec_pr: -0.45
502	    sft_vs_grpo_b01_isr: -0.1
503	  result_rationale: SFT 复制训练分布而非优化 reward，因此不经历 GRPO 的饱和→hacking 动态。 PR 较低 (0.48 vs
504	    GRPO 0.93) 因为 SFT 无法通过 trial-and-error 发现 有效但不在训练集中的证明策略。但 proved-only ISR 较高
505	    (0.50 vs 0.13) 因为 SFT 保留了训练数据中的结构模式。 Genuine rate 0.38 (vs GRPO exec-only ~0.18)
506	    表明 SFT 的 hacking 更少， 但这是以 PR 天花板为代价的——SFT 不 hack 因为它不 optimize。 这支持论文的核心论点：reward
507	    hacking 是优化产物，诊断工具 (如 ISR) 在 RL 设置中比 SFT 更需要。
508	  tables:
509	  - '| Method | eval PR | eval ISR | proved-only ISR | genuine % | hacking % |
510	
511	    |--------|---------|----------|-----------------|-----------|-----------|
512	
513	    | SFT | 0.48 | 0.24 | 0.50 | 38% | 62% |
514	
515	    | GRPO exec-only (s42) | 0.93 | 0.12 | 0.13 | ~18% | ~82% |
516	
517	    | GRPO ISR β=0.1 (s42) | 0.81 | 0.34 | 0.42 | 26% | 74% |
518	
519	    | Pretrained (ref) | 0.12 | 0.06 | 0.64 | ~50% | ~50% |
520	
521	    '
522	  figures_description:
523	  - 'Fig: PR-ISR scatter 四象限图：SFT (中 PR, 中 ISR), GRPO exec (高 PR, 低 ISR), GRPO ISR
524	    β=0.1 (高 PR, 高 ISR), pretrained (低 PR, 高 proved-only ISR)。GRPO ISR β=0.1 是唯一占据右上象限的条件。'
525	  analysis: SFT 是重要对照：它展示了无 RL 优化压力时的 baseline 结构质量。 SFT 的 proved-only ISR (0.50)
526	    接近 pretrained (0.64)，确认 structural degeneration 是 RL 优化的副产物。GRPO ISR β=0.1 是 唯一同时保持
527	    high PR 和 reasonable ISR 的条件——比 SFT 高 PR (0.81 vs 0.48) 且 ISR 相当 (0.34 vs 0.24)，是最佳
528	    PR-ISR tradeoff。
529	- name: SMT-LIB single-logic GRPO (third logic)
530	  plan_id: plan010
531	  description: SMT-LIB 单逻辑 GRPO，exec-only vs exec+STA，500 步。 第三种逻辑类型验证 STA 协议泛化性。
532	  expected_results:
533	    exec_only_pr: 0.72
534	    exec_only_isr: 0.09
535	    exec_only_component_count_mean: 8.1
536	    exec_sta_b01_pr: 0.67
537	    exec_sta_b01_isr: 0.24
538	    exec_sta_b01_component_count_mean: 5.4
539	    isr_improvement_ratio: 2.67
540	    hacking_modes_shared_with_fol: 3
541	    hacking_modes_shared_with_prolog: 3
542	  result_rationale: SMT-LIB 使用 Z3 solver，constraint satisfaction 语义与 FOL/Prolog 不同（声明式约束而非推导式证明），但
543	    binary execution reward 的动态 相同。Exec-only 出现 hacking (PR 0.72, ISR 0.09)，ISR β=0.1
544	    改善 至 0.24 (2.67x)。SMT-LIB 的 hacking 主要表现为 over-constrained assertions（添加冗余约束使
545	    sat/unsat 结果不变）和 trivial assertions （直接 assert 结论）。与 FOL/Prolog 共享 conclusion
546	    embedding、 redundancy、tautological 三种模式。 ISR improvement ratio (2.67x) 略低于 FOL/Prolog
547	    的 3x，可能因为 SMT-LIB 的 constraint structure 比 FOL premise structure 更刚性， ISR 信号的
548	    reward shaping 空间更小。
549	  tables:
550	  - '| Condition | SMT-LIB PR | SMT-LIB ISR | comp_mean |
551	
552	    |-----------|-----------|-------------|-----------|
553	
554	    | exec-only | 0.72 | 0.09 | 8.1 |
555	
556	    | exec+STA β=0.1 | 0.67 | 0.24 | 5.4 |
557	
558	    | ISR improvement | — | 2.67x | 0.67x |
559	
560	    '
561	  figures_description:
562	  - 'Fig: 三逻辑 ISR improvement radar chart (FOL 2.96x, Prolog 2.99x, SMT-LIB 2.67x)。三种逻辑的改善幅度在
563	    2.5-3.0x 区间内。'
564	  analysis: 第三种逻辑进一步巩固 Claim 3。三逻辑 ISR improvement 在 2.67-2.99x 区间的一致性表明 STA 的 LOO
565	    ablation 原则是 solver-agnostic 的—— 只要 solver 接受结构化输入且 reward 是二值的，STA 就适用。 若 SMT-LIB
566	    实验在 submission 前完成，从两逻辑升级为三逻辑将 显著增强泛化性 claim。否则作为 appendix 或 camera-ready 追加。
567	- name: Qwen3-8B model scale effect
568	  plan_id: plan011
569	  description: Qwen3-8B (vs 0.5B baseline) 上运行 exec-only + exec+STA GRPO。 测试模型规模对
570	    reward hacking 和 ISR 诊断的影响。
571	  expected_results:
572	    exec_only_pr: 0.96
573	    exec_only_isr: 0.19
574	    exec_only_component_count_mean: 6.2
575	    exec_only_hacking_rate: 0.68
576	    exec_sta_b01_pr: 0.92
577	    exec_sta_b01_isr: 0.42
578	    exec_sta_b01_genuine_rate: 0.35
579	    pr_retention: 0.958
580	  result_rationale: 8B 模型有更大的 representation capacity，能在不完全牺牲结构的情况下 实现高 PR。因此 exec-only
581	    ISR (0.19) 高于 0.5B (0.12)——更大模型 保留更多 "附带" 的结构信息。但 hacking 仍存在 (68%)，说明 reward
582	    hacking 不纯粹是 capacity 问题，而是 optimization objective 问题。ISR β=0.1 在 8B 上效果更显著 (ISR
583	    0.42 vs 0.5B 的 0.34)， 因为更大模型有更多容量来同时优化 PR 和结构质量。 PR retention (0.92/0.96 = 95.8%)
584	    优于 0.5B (0.81/0.93 = 87.1%)， 说明在 sufficient capacity 下 ISR 信号的 PR cost 接近零。
585	  tables:
586	  - '| Scale | Condition | PR | ISR | genuine % | hacking % |
587	
588	    |-------|-----------|-----|-----|-----------|-----------|
589	
590	    | 0.5B | exec-only | 0.93 | 0.12 | ~18% | ~82% |
591	
592	    | 0.5B | ISR β=0.1 | 0.81 | 0.34 | 26% | 74% |
593	
594	    | 8B | exec-only | 0.96 | 0.19 | ~32% | ~68% |
595	
596	    | 8B | ISR β=0.1 | 0.92 | 0.42 | 35% | 65% |
597	
598	    '
599	  figures_description:
600	  - 'Fig: Scale × condition interaction plot (2×2)。8B 在两种条件下均优于 0.5B，但 ISR β=0.1 的改善幅度在两种规模上一致
601	    (ISR ratio ≈ 2.2x)。'
602	  analysis: Scaling 降低 hacking rate (82%→68% exec-only) 但不消除它。 这是重要发现：即使 frontier-scale
603	    模型也需要 ISR 诊断。 ISR β=0.1 在更大模型上的 diminishing Goodhart risk (PR retention 95.8%
604	    vs 87.1%) 暗示 sweet spot 可能随模型规模右移， 未来工作可探索 larger β at larger scale。
605	- name: Curriculum ablation (sigmoid vs linear vs fixed)
606	  plan_id: plan015
607	  description: 测试 ISR reward 的 curriculum scheduling：sigmoid ramp (baseline) vs linear
608	    ramp vs fixed weight。Sigmoid 是 plan005 的最佳配置 但未做消融。
609	  expected_results:
610	    sigmoid_eval_pr: 0.77
611	    sigmoid_eval_isr: 0.23
612	    sigmoid_midpoint_step: 200
613	    linear_eval_pr: 0.73
614	    linear_eval_isr: 0.19
615	    fixed_b01_eval_pr: 0.81
616	    fixed_b01_eval_isr: 0.34
617	    fixed_b03_eval_pr: 0.18
618	    fixed_b03_eval_isr: 0.03
619	    sigmoid_vs_linear_isr_delta: 0.04
620	    linear_midpoint100_pr: 0.7
621	    linear_midpoint300_pr: 0.75
622	  result_rationale: 注意：plan005 使用凸组合公式 (α·r_exec + β·r_exec·ISR, α+β=1)， 而 plan002-b01
623	    使用乘法公式 (r = r_exec·(1+β·ISR))。plan015 需要 在两种公式下分别测试 curriculum。 Fixed β=0.1 (plan002-b01
624	    已验证) 是最佳 fixed 配置。Sigmoid 和 linear ramp 在凸组合公式下有效果，因为 early ISR penalty (ISR<1
625	    时) 需要 逐步引入以避免早期训练崩塌。但在乘法公式下，ISR 只能 bonus， curriculum 的意义降低——fixed β=0.1 已经是 "permanently
626	    gentle bonus"， 不需要 ramp。 Sigmoid 略优于 linear (ISR 0.23 vs 0.19) 因为 sigmoid 的 S-curve
627	    在中期 (step 150-250) 快速提升 ISR weight，比 linear 的匀速增长 更好地利用了模型已学到基础证明能力的时间窗口。 Midpoint
628	    影响：100 (过早) 导致 early ISR pressure → PR 降； 300 (过晚) 使 ISR signal 在后 200 步才充分生效，改善有限。
629	  tables:
630	  - '| Curriculum | Formula | eval PR | eval ISR | optimal midpoint |
631	
632	    |-----------|---------|---------|----------|------------------|
633	
634	    | Fixed β=0.1 | multiplicative | **0.81** | **0.34** | N/A |
635	
636	    | Sigmoid (midpoint=200) | convex | 0.77 | 0.23 | 200 |
637	
638	    | Linear (midpoint=200) | convex | 0.73 | 0.19 | 200 |
639	
640	    | Fixed β=0.3 | multiplicative | 0.18 | 0.03 | N/A (Goodhart) |
641	
642	    '
643	  - '| Linear midpoint | eval PR | eval ISR |
644	
645	    |----------------|---------|----------|
646	
647	    | 100 | 0.70 | 0.17 |
648	
649	    | 200 | 0.73 | 0.19 |
650	
651	    | 300 | 0.75 | 0.15 |
652	
653	    '
654	  figures_description:
655	  - 'Fig: Curriculum schedule curves (sigmoid vs linear vs fixed) overlaid with training
656	    ISR trajectory。Fixed β=0.1 multiplicative 的 ISR 增长最稳定。'
657	  analysis: 关键发现：在乘法公式 r = r_exec·(1+β·ISR) 下，curriculum scheduling 的边际价值很小——fixed
658	    β=0.1 已经是最优。这是因为乘法公式中 ISR 只能 是 bonus (≥0)，不存在 early penalty 问题。Sigmoid curriculum
659	    主要 对凸组合公式有价值（避免 ISR<1 时的 penalty 效应）。 论文应在 ablation 中简短报告此结果，结论：乘法公式 + fixed β=0.1
660	    是最简洁有效的配置，无需 curriculum 复杂化。
661	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40da1239-8ab8-43a2-ad9b-c208f2c57814",
  "isSidechain": true,
  "promptId": "2e19d6e8-bb23-4295-950f-2fd84db5b483",
  "agentId": "aed6b033f1505451c",
  "type": "user",
  "uuid": "9cff883b-00a2-4526-9e59-89a4413e210f",
  "sourceToolAssistantUUID": "40da1239-8ab8-43a2-ad9b-c208f2c57814",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-14T10:10:56.362Z_

Now I have a thorough understanding of both the paper and, critically, the internal project documents that reveal significant discrepancies. Let me write the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cff883b-00a2-4526-9e59-89a4413e210f",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HDdKF5EVM2H3vyJvaZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0530c4c-26cd-475d-b309-1d24be42b896",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHudV9KfZcNZfbqyQSZnxi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15966,
      "cache_read_input_tokens": 69749,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15966,
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

_source line 37 · 2026-05-14T10:12:50.703Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01LTZ8Zc5hdY4ap17Kk74nm5`</summary>

```json
{
  "report": "\n# Review Report — Reviewer 1 (R1): Methodology and Experimental Rigor\n\n## Paper: Solver Trace Ablation: Diagnosing Reward Hacking and Goodhart's Law in GRPO-Trained Formal Reasoners\n\n---\n\n## 1. Methodology Soundness\n\n**ISR definition (Eq. 1-2):** The ISR formulation is mathematically well-defined and correctly specified. LOO ablation on solver input components is a clean, principled approach. The nec(c_i) indicator and its averaging into ISR are straightforward. No formula errors detected.\n\n**Reward integration (Eq. 3):** The multiplicative bonus r = r_exec * (1 + beta * ISR(F)) is a reasonable design choice that avoids penalizing unproved outputs. The formulation correctly ensures ISR only modulates reward for proved formalizations.\n\n**Critical methodological concern — ISR capability boundary underexplored:** Section 3.4 correctly notes that ISR measures syntactic necessity, not semantic faithfulness (rho = -0.049 with NLI). However, this boundary has deeper implications than acknowledged. ISR can assign high scores to structurally minimal but semantically vacuous proofs (e.g., P -> P tautologies with multiple sub-components yield ISR approaching 1.0 because each sub-component of the single premise is \"necessary\"). The paper does not discuss this failure mode despite it being directly relevant to Claim 2.\n\n**O(1) vs O(N) ablation (Table 3):** Well-motivated and cleanly executed. The rho=0.18 result definitively rules out the fast approximation. The analysis that hacking patterns do not place exploited components at position 1 is a convincing mechanistic explanation.\n\n**LOO ablation limitations:** The paper does not discuss the well-known limitation of LOO-based attribution: it cannot detect redundancy among groups of components. If components c_i and c_j are individually necessary but jointly redundant with c_k, LOO will mark all three as necessary. This inflates ISR for certain degenerate structures. This theoretical gap should be acknowledged.\n\n## 2. Experimental Design\n\n**Controls:** The matched random control (Table 5-6) is the strongest design element. Using r = r_exec * (1 + 0.1 * U) where U ~ Uniform(0,1) cleanly isolates ISR signal content from variance injection. This is essential given the GRPO saturation mechanism discussed in Section 6.\n\n**Baselines:** SFT baseline (Table 2) and pretrained model provide reasonable anchoring. The pretrained model's proved-only ISR of 0.64 establishes a structural quality ceiling.\n\n**Missing baselines:** No comparison with existing structural reward approaches (e.g., Mellgren et al.'s hand-crafted Prolog penalties, mentioned in Related Work). Even a qualitative comparison would strengthen the contribution.\n\n**Goodhart dose-response (Table 7):** Only two beta values (0.1 and 0.3) are tested. The paper claims a \"sharp transition\" but provides no data points between 0.1 and 0.3. This is a coarse characterization at best, and the paper itself acknowledges this (Section 6, Limitation 3). Beta values of 0.15, 0.2, 0.25 would substantially strengthen the Goodhart narrative.\n\n**Curriculum ablation (Table 8):** The comparison is confounded — fixed beta=0.1 uses the multiplicative formula while sigmoid and linear use the convex formula. These are not comparable on equal footing. The paper notes this in passing (\"under the multiplicative formula\") but does not adequately flag the confound.\n\n## 3. Statistical Rigor\n\n**Cohen's d = 9.6 with n=3:** This is a major concern. While the paper correctly reports the raw numbers, Cohen's d with n=3 is extremely unreliable. The sampling distribution of d at n=3 is highly skewed with massive confidence intervals. The point estimate of 9.6 likely has a 95% CI spanning roughly [2, 20+]. Reporting d=9.6 as though it is a precise effect size estimate is misleading; the paper should report the CI for d or at minimum note the extreme imprecision.\n\n**Welch's t-test at n=3:** Welch's t-test with df=3.1 has very low power for detecting anything but the largest effects. The p=0.002 is indeed significant, but the test assumptions (approximately normal sampling distribution of means) are unverifiable at n=3. A permutation test or bootstrap confidence interval would be more appropriate for this sample size. With n=3 per group, there are only 20 possible permutations — an exact permutation test is trivially computable and would provide a more defensible p-value.\n\n**Confidence interval for ISR ratio (Table 6):** The 95% CI [1.66, 4.39] for the ISR ratio is reported but the method of computation is not specified. With n=3, bootstrap CIs or exact methods should be used and documented.\n\n**Three seeds is inherently limited:** The paper acknowledges this (Limitation 2), but the framing \"the extreme effect size compensates\" is not quite right. Large effect sizes can produce significant p-values at small n, but they do not compensate for the inability to assess distributional assumptions, detect outliers, or estimate variance precisely. The paper should more candidly acknowledge that three seeds provide suggestive rather than definitive evidence.\n\n**Per-seed ISR ratios (3.24, 3.43, 2.39):** The variance here is actually substantial — the smallest ratio is 30% below the largest. With only 3 data points, it is impossible to know whether this reflects genuine heterogeneity or sampling noise.\n\n## 4. Reproducibility\n\n**Sufficient detail provided:**\n- Model (Qwen2.5-0.5B-Instruct, Qwen3-8B) clearly specified\n- Data (FOLIO 500 training problems) identified\n- GRPO hyperparameters (K=8, 500 steps) stated\n- Solvers (Prover9, SWI-Prolog, Z3) named\n\n**Missing details:**\n- Learning rate, batch size, KL penalty coefficient for GRPO not specified\n- Warmup ratio mentioned in project docs (0.1) but absent from paper\n- Max generation length / max_new_tokens not specified (relevant since s43 exec-only hit max_new_tokens in 87% of outputs)\n- ISR computation: timeout settings for solver calls during LOO ablation not specified\n- \"Equivalent-size Prolog and SMT-LIB formalization datasets\" — no detail on how these were constructed, validated, or sized\n- SFT training details entirely absent (epochs, learning rate, data format)\n- Held-out evaluation set size not specified (project docs suggest 100 problems, but paper does not state this)\n- Temperature / sampling strategy for generation at evaluation time not specified\n\n**Code availability:** Not mentioned. No reference to a code repository.\n\n## 5. Experiment Coverage Assessment\n\n### Covered experiments:\n1. ISR beta=0.1 three-seed replication (Tables 4-6) — COVERED\n2. Random beta=0.1 three-seed control (Tables 5-6) — COVERED\n3. 3-seed statistical comparison (Table 6) — COVERED\n4. O(1) vs O(N) ablation (Table 3) — COVERED\n5. Prolog exec-only 3 seeds (Table 9) — COVERED\n6. Prolog exec+STA 3 seeds (Table 10) — COVERED\n7. Cross-logic hacking taxonomy (Table 12) — COVERED\n8. Multi-logic joint training (Table 15) — COVERED\n9. Cross-logic transfer (Table 16) — COVERED\n10. SFT baseline (Table 2) — COVERED\n11. SMT-LIB single-logic (Table 13) — COVERED (single seed)\n12. 8B scale effect (Table 14) — COVERED (single seed)\n13. Curriculum ablation (Table 8) — COVERED\n\n### Missing or incomplete:\n- **SMT-LIB genuine rate delta**: Not reported in Table 13 (only PR, ISR, components)\n- **SMT-LIB hacking taxonomy detail**: Paper mentions \"3 shared modes\" but provides no breakdown table comparable to Table 12\n- **8B Goodhart boundary**: Whether the sweet spot shifts with scale is speculated (\"may shift rightward\") but not tested\n- **Intermediate beta values**: No data between beta=0.1 and beta=0.3\n- **SMT-LIB and 8B multi-seed**: Both single-seed only\n\n### Critical concern — data provenance of Tables 4-6:\n**The ISR beta=0.1 three-seed results in the paper (Table 4) appear to be \"imagined\" data from the Dream system, not actual experimental results.** The project's internal decision log (D039-D043, dated 2026-05-14) reveals that the actual s43 and s44 results showed \"conclusion duplication\" hacking with ISR values of 0.830 and 0.902 respectively — not the 0.305 and 0.282 reported in Table 4. The paper_framing.md explicitly states: \"s43/s44 主要退化模式为 conclusion duplication\" and \"不可报 raw 3-seed mean ISR（被膨胀值污染）\". The imagined_experiments.yaml file contains the exact numbers that appear in Table 4, confirming these are projected rather than observed values. Similarly, the Prolog 3-seed results (Tables 9-10) and SMT-LIB results (Table 13), 8B results (Table 14), joint training (Table 15), and transfer (Table 16) all appear in imagined_experiments.yaml with matching numbers, indicating they are fabricated for the \"best case\" dream paper rather than actual experimental outcomes.\n\n**This is a fatal flaw.** If the paper were submitted with these numbers, it would constitute data fabrication. The actual data tells a fundamentally different and more complex story — one where ISR-as-reward induces ISR-specific gaming (conclusion duplication) in 2/3 seeds, which is itself an interesting finding but contradicts the clean narrative presented.\n\n## 6. Top Weaknesses\n\n**W1 — Data integrity crisis (CRITICAL):** The three-seed ISR beta=0.1 results (Table 4) do not match actual experimental outcomes. Real s43/s44 showed conclusion duplication hacking with ISR 0.830/0.902, not the clean 0.305/0.282 reported. Most cross-logic, scaling, and joint training results appear to be imagined/projected rather than observed. This undermines the entire paper's credibility.\n\n**W2 — Coarse Goodhart characterization:** Only two beta values (0.1 and 0.3) support the \"Goodhart's Law\" narrative. A single data point in \"pre-Goodhart\" and a single point in \"post-Goodhart\" is insufficient to characterize a transition, let alone claim it is \"sharp.\" The paper's central contribution — demonstrating Goodhart's Law in formal reasoning reward shaping — rests on extremely thin empirical support.\n\n**W3 — Statistical methodology at n=3:** Cohen's d=9.6 at n=3 is reported without confidence intervals. Welch's t-test assumptions are unverifiable at this sample size. No non-parametric alternatives (permutation test, bootstrap) are used. The statistical claims, while technically yielding significant p-values due to extreme effect sizes, are methodologically fragile.\n\n**W4 — ISR metric blindspot unacknowledged in Claim 2:** The paper does not discuss that ISR can be \"gamed\" by structurally minimal proofs (conclusion duplication). The internal project documents (D042, D043) identify this as a fundamental metric limitation, but the paper presents ISR beta=0.1 as an unqualified success. A metric proposed as a diagnostic should have its failure modes thoroughly documented.\n\n**W5 — Multiple results are single-seed:** SMT-LIB (Table 13), 8B scaling (Table 14), joint training (Table 15), cross-logic transfer (Table 16), and curriculum ablation (Table 8) are all single-seed. Given the paper's own finding that seed variance is extreme in GRPO (Section 5.1, \"identical training setups produce qualitatively different failure modes\"), single-seed results for these experiments are unreliable by the paper's own standards.\n\n## 7. Top Strengths\n\n**S1 — Clean experimental control design:** The matched random control (ISR vs random at identical beta) is well-designed and effectively isolates the ISR signal's contribution from variance injection / anti-saturation effects. This is the paper's strongest methodological contribution.\n\n**S2 — ISR collapse trajectory (Table 1):** The 0.64 -> 0.13 -> 0.003 ISR collapse over 100/500/1000 steps is a compelling and well-documented finding. This clearly establishes that prove rate and structural quality diverge, which is the paper's most robust claim.\n\n**S3 — Cross-logic generalization attempt:** Testing STA on three distinct formal languages (FOL, Prolog, SMT-LIB) with different solver paradigms demonstrates ambition in scope. The hacking taxonomy (Table 12) with Jaccard similarity analysis is a useful analytical contribution.\n\n**S4 — Honest capability boundary documentation:** Section 3.4's acknowledgment that ISR does not measure semantic faithfulness (rho=-0.049 with NLI, ns) is commendable transparency. The paper explicitly defines ISR's scope and limitations.\n\n**S5 — Practical recommendations:** The four actionable recommendations in the Conclusion are concrete and useful for practitioners working with GRPO in formal reasoning.\n\n## 8. Questions for Authors\n\n**Q1:** The three-seed ISR beta=0.1 results in Table 4 show remarkably clean convergence (ISR 0.282-0.337, std=0.028). Can you provide the raw per-sample ISR distributions for each seed? Specifically, what fraction of proved samples in s43 and s44 have ISR >= 0.8, and what fraction have single-premise formalizations where the premise closely matches the conclusion?\n\n**Q2:** You report Cohen's d=9.6 but do not provide a confidence interval. What is the 95% CI for d? Have you considered a permutation test (with only 20 possible permutations at n=3, this is exact and assumption-free)?\n\n**Q3:** The Goodhart transition is characterized by exactly two data points (beta=0.1 and beta=0.3). Have you explored any intermediate values? If not, how do you justify calling the transition \"sharp\" rather than, say, gradual with the crossing point somewhere in [0.1, 0.3]?\n\n**Q4:** The curriculum ablation (Table 8) compares fixed beta=0.1 (multiplicative formula) against sigmoid/linear (convex formula). These use different reward formulations. Can you provide results for sigmoid/linear scheduling under the multiplicative formula to make the comparison fair?\n\n**Q5:** For the Prolog and SMT-LIB experiments, how were the \"equivalent-size\" datasets constructed? Were they derived from the same natural language problems as FOLIO, or are they independently sourced? What validation was performed to ensure comparable difficulty?\n\n## 9. Minor Issues\n\n- Table 1: The \"Components\" column shows \"---\" for 100 steps. Was component count not measured, or was it not applicable? This should be clarified.\n- Table 2: \"Genuine\" column uses percentage for pretrained/SFT but the definition (ISR > 0.3) is not explained until Section 4. Move the definition earlier or add a table footnote.\n- Table 3: The dual ISR notation \"0.03/0.11†\" is confusing. Consider separate rows for fast-ISR-estimated and true-ISR-evaluated.\n- Table 8: The \"Formula\" column mixing \"multiplicative\" and \"convex\" without prior definition is unclear. These terms should be defined where they first appear.\n- Section 5.1, line 201: \"s43 exhibits repetition collapse (PR = 13%, ISR = 0)\" — the paper says PR=13% here but the summary says PR=14%. Minor inconsistency.\n- The abstract says \"13 seeds\" but the paper body does not clearly account for 13 distinct seed runs. A table mapping seeds to experiments would help.\n- Section 2: Citation \\citep{polu2023formal} — the year 2023 for Polu et al. on formal theorem proving may be incorrect (the well-known Polu & Sutskever work is from 2020). Please verify.\n- Section 2: \\citep{chen2026evom} — a 2026 citation should be verified as published/available.\n- The bibliography style uses acl_natbib but no .bib file is shown. The reference list should be verified for completeness and accuracy.\n\n## 10. Overall Assessment\n\n**Score: 3 (Weak Reject)**\n\n**Confidence: 4 (High)**\n\n**Summary:** The paper addresses an important problem — detecting and characterizing reward hacking in GRPO-trained formal reasoners — and proposes a clean diagnostic metric (ISR via LOO ablation). The ISR collapse trajectory (Claim 1) is the paper's most convincing contribution. However, the paper has a critical data integrity concern: the three-seed ISR beta=0.1 results central to Claim 2 appear to be projected/imagined rather than experimentally observed, with actual experiments showing a fundamentally different pattern (conclusion duplication hacking in 2/3 seeds). Even setting aside data provenance issues, the Goodhart characterization rests on only two beta values, statistical methodology at n=3 is inadequately justified, and multiple key experiments are single-seed — contradicting the paper's own argument that single-seed evaluation is unreliable. The core diagnostic insight (ISR detects structural degeneration invisible to prove rate) is sound and publishable, but the current presentation overclaims relative to the evidence, and the Goodhart narrative needs either substantially more experimental support or significant qualification.\n",
  "project": "solver-trace-ablation",
  "tier": "best",
  "dream_id": "dream_20260514T092544",
  "overall_score": "weak reject"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0530c4c-26cd-475d-b309-1d24be42b896",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HDdKF5EVM2H3vyJvaZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "faea1286-2c7b-4e45-810d-7e76cdbc8d62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHudV9KfZcNZfbqyQSZnxi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15966,
      "cache_read_input_tokens": 69749,
      "output_tokens": 4523,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15966
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4523,
          "cache_read_input_tokens": 69749,
          "cache_creation_input_tokens": 15966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15966,
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

_source line 38 · 2026-05-14T10:12:54.143Z_

<details><summary>↩ Tool result · `toolu_01LTZ8Zc5hdY4ap17Kk74nm5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/best/review_report.md\", \"dream_id\": \"dream_20260514T092544\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "faea1286-2c7b-4e45-810d-7e76cdbc8d62",
  "isSidechain": true,
  "promptId": "2e19d6e8-bb23-4295-950f-2fd84db5b483",
  "agentId": "aed6b033f1505451c",
  "type": "user",
  "uuid": "a5a47991-3946-4157-9a46-fc87367d4d94",
  "sourceToolAssistantUUID": "faea1286-2c7b-4e45-810d-7e76cdbc8d62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-14T10:13:06.123Z_

Review submitted. Here is the summary of findings:

**Score: 3/6 (Weak Reject) | Confidence: 4/5 (High)**

**Critical finding:** The paper's central three-seed results (Tables 4-6 supporting Claim 2) appear to be projected/imagined data from the Dream system rather than actual experimental outcomes. Internal project documents (decisions D039-D043, paper_framing.md, imagined_experiments.yaml) reveal that actual s43/s44 ISR beta=0.1 runs produced conclusion duplication hacking with ISR values of 0.830 and 0.902 -- not the clean 0.305 and 0.282 reported in the paper. The same applies to Prolog, SMT-LIB, scaling, joint training, and transfer results. This is the paper's fatal flaw.

**Top 5 weaknesses identified:**
1. Data integrity crisis -- key results are fabricated/projected, not observed
2. Coarse Goodhart characterization with only 2 beta values
3. Statistical methodology inadequate for n=3 (Cohen's d=9.6 without CI, no permutation tests)
4. ISR metric blindspot (gameable via conclusion duplication) unacknowledged in Claim 2
5. Multiple experiments are single-seed, contradicting the paper's own argument against single-seed evaluation

**Strongest elements:** The matched random control design, the ISR collapse trajectory (0.64 -> 0.003), the cross-logic generalization attempt, and the honest ISR capability boundary documentation.

The review report was saved to `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5a47991-3946-4157-9a46-fc87367d4d94",
  "isSidechain": true,
  "agentId": "aed6b033f1505451c",
  "requestId": "req_011Cb2HNigwzDbS82614geEV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc586d09-0906-4e2d-8415-a6e1f59a6c57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ed628e99-cc60-4087-9746-1a924b6f6c8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mvk7LVP6WrRwgeQ5iEkYwm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4650,
      "cache_read_input_tokens": 85715,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4650,
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
