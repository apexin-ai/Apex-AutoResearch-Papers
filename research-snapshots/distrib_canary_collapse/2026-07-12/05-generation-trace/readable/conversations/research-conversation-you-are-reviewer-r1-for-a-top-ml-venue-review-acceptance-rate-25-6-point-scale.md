# Research conversation: You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 70
- **Recorded user turns:** 1
- **Tool calls:** 28
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a7b91bbe8bfcb2d20.jsonl`
- **Structured JSON:** [`4031bd199996ff4161cc.json`](../../sessions/40/4031bd199996ff4161cc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

70 recorded events

### User

_source line 1 · 2026-05-14T19:27:47.475Z_

You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus: **Methods and Experiments**.

# Paper Summary

**Title**: "Taxonomy of Collapse Decoupling: Diversity and Quality Degrade Through Independent Channels in Iterative Synthetic Training"

**Core thesis**: In iterative synthetic training (model collapse), diversity collapse (measured by distinct-n) and quality collapse (measured by perplexity) are fundamentally independent failure modes. Canary metrics (ECE, token entropy) lead diversity degradation by 1–2.5 generations but show NO statistically significant lead over perplexity at any contamination level.

**Three claimed contributions**:
1. **Collapse Taxonomy**: diversity and quality collapse are independent channels
2. **Decoupling Diagram**: canary→diversity lead exists across all α but canary→perplexity decoupling is universal — no α* boundary exists
3. **Methodological Validation**: naive cross-correlation and Toda-Yamamoto agree 94% for well-behaved metric pairs

**Setup**: Pythia-410M on WikiText-103, iterative self-consumption protocol. At each generation t: generate synthetic data S_t from M_{t-1}, form D_t = α·S_t + (1-α)·D_0, fine-tune M_{t-1} on D_t. α ∈ {0.25, 0.50, 0.75, 1.0}, T=10 generations (extended to T=20), 3-4 seeds.

**Metrics**:
- Canary (hypothesized leading): ECE (15 equal-mass bins), Token Entropy (Shannon entropy of next-token prediction)
- Target: Distinct-n (n=1,2), Perplexity (held-out WikiText-103 validation)
- Also tested effective_rank, self-BLEU as canaries — failed

**Statistical Framework**:
- Cross-correlation r(ℓ) = Corr(c_t, y_{t+ℓ}) for ℓ ∈ [-L, L], L ∈ {5, 7}
- Signal onset: first generation where |m_t - m_0| > 2σ_{m_0}
- Toda-Yamamoto: VAR(k + d_max), Wald test on first k coefficients
- Significance: two-tailed t-test, p < 0.05

**Experiments and Results**:

**4.1 Full Self-Consumption (α=1.0, 4 seeds, T=10)**:
- ECE→distinct-1: lag = -2.50±0.58, |r|>0.99, 4/4 seeds significant, onset lead 1.50 gen
- Entropy→distinct-1: lag = -1.25±0.50, |r|>0.99, 4/4 seeds significant, onset lead 1.25 gen
- ECE→perplexity: lag = 0.00, 0/4 significant
- Entropy→perplexity: lag = -5.50, |r|=0.68, only 1/4 significant (p=0.09 mean)
- Perplexity onset at gen 2.50 — between canary onset (1.50-1.75) and diversity onset (3.00-3.25)

**4.2 Decoupling Diagram (α-sweep)**:
Table 2 shows:
- ECE→d1: lag increases from -0.67 (α=0.25) to -2.50 (α=1.0), sig seeds from 1/3 to 4/4
- Ent→d1: lag from -0.33 to -1.25, sig seeds from 1/3 to 4/4
- ECE→ppl: lag=0.00 at ALL α, 0 sig seeds everywhere
- Ent→ppl: — (non-sig) at α=0.25,0.50,0.75; -5.50 (1/4 sig) at α=1.0

Table 3 (gen 10 metrics): At α=0.25, ppl=42.5 (barely degraded from ~30 baseline) while distinct-1=0.088 (already declining), showing diversity loss without quality loss.

**4.3 Methodological Validation**:
Table 4: At α=1.0, 24 naive significant pairs → 18 TY significant → 6 overturned (25%). But for core canaries only, 1 overturned (3.1%). Overall agreement rate 0.88, core canary agreement 0.94. TY significance rate only 55% across all conditions (low power with 10-point series).

**4.4 Extended Trajectory (T=20, α=1.0, 2 seeds)**:
- lag=-5.5 for entropy→ppl is a SATURATION artifact: two seeds give -7 and -3 (std=2.83, 0/2 sig)
- Entropy saturates at gen 8 (→0.62), distinct-1 slowly decays (→0.028), perplexity diverges unboundedly (→8420 at gen 20)
- Information-theoretic argument: canary metrics are intrinsic statistics of p_θ (bounded), perplexity is cross-distribution H(p_data, p_θ) (unbounded)

**4.5 Cross-Domain (C4, α=0.50, 3 seeds)**:
Table 6: ECE→d1 lag: WikiText -1.00±0.82 (2/3 sig) vs C4 -0.33±0.58 (1/3 sig). Ent→d1: WikiText -0.67 (2/3) vs C4 -0.67 (1/3). ECE→ppl: 0/3 sig on both.
Canary ranking reverses: ECE better on WikiText, entropy better on C4.
Table 7: gen-10 metrics differ (C4 ppl=62.8 vs WikiText 78.3).

**4.6 Scale Spot-Check (Pythia-1.4B, α=0.50, 3 seeds)**:
Table 8: 1.4B collapses ~35% slower (rate ratio 0.65). Canary lead NOT preserved: both ECE→d1 and Ent→d1 show reduced lag (-0.33 vs -1.00/-0.67), only 1/3 seeds significant. Flagged as "inconclusive" — insufficient exposure at this α×T.

**4.7 Intervention (CRS vs baseline, α=0.75, 3 seeds)**:
Table 9: CRS produces +9.5% relative distinct-1 improvement, -5.4% perplexity improvement, but p>0.1, not cross-seed consistent. One seed shows CRS worse than baseline (false trigger). Negative result coherent with decoupling thesis.

**4.8 Data Strategy Ablation (accumulate vs replace, α=0.50, 3 seeds)**:
Table 10: Accumulate slows collapse (rate ratio 0.55), but eliminates canary predictive lead: ECE→d1 lag shrinks from -1.00 (replace) to -0.33 (accumulate), 0/3 sig seeds. "Monitoring paradox": canaries most effective where collapse is fastest.

**Limitations acknowledged**: Scale (only Pythia-410M primary), data diversity (2 datasets), fixed generation protocol, temporal resolution (max 20 discrete generations).

**References**: 10 cited works including Shumailov et al. (Nature 2024), Fu et al. (ICML 2024), Dohmatob et al. (2024), SIGMA, Alemohammad et al. (ICLR 2024), Du et al., Truong & Truong, Kalinowski et al., Toda & Yamamoto (1995), Li et al. (NAACL 2016).

---

# Experiment Design Reference (what was planned)

The following experiments were planned. Check coverage:
1. **α-sweep predictability phase diagram** (plan_001): α∈{0.25,0.50,0.75} × 10 gen × 3 seeds — COVERED in §4.2
2. **Methodology ablation: naive vs TY** (plan_002): Compare 4 methods — COVERED in §4.3
3. **MVP formalization (max_lag=7)** (plan_003): 4-seed α=1.0, max_lag from 5→7, 2σ onset — COVERED in §4.1
4. **C4 cross-domain** (plan_004): C4 × α=0.50 × 3 seeds — COVERED in §4.5
5. **Pythia-1.4B scale spot-check** (plan_005): 1.4B × α=0.50 × 3 seeds — COVERED in §4.6
6. **Extended run (20 gen)** (plan_006): α=1.0 × 20 gen × 2 seeds — COVERED in §4.4
7. **Intervention** (plan_007): CRS vs baseline × α=0.75 × 3 seeds — COVERED in §4.7
8. **Data strategy ablation** (plan_008): accumulate vs replace × α=0.50 × 3 seeds — COVERED in §4.8

All 8 planned experiments appear in the paper.

---

# Your Review Task

Evaluate the paper on **Methods and Experiments** specifically. Write a structured review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (bulleted, specific)
3. **Weaknesses** (bulleted, specific, with concrete suggestions)
4. **Questions for Authors**
5. **Minor Issues**
6. **Scores**:
   - Soundness (1-4)
   - Empirical methodology (1-4)
   - Reproducibility (1-4)
   - Overall score (1-6 scale)
   - Confidence (1-5)

Focus on:
- Statistical rigor: Is cross-correlation on 10-point time series reliable? Is 3-4 seeds enough?
- Experimental controls: Are confounds addressed?
- Claims vs evidence: Do the negative results support the "decoupling" framing, or could they reflect insufficient power?
- Missing experiments or analyses that would strengthen/weaken claims
- Whether the information-theoretic argument (§5.1) is rigorous or hand-wavy
- The intervention experiment's design and what it actually shows

Be critical but fair. This is for a top venue with ~25% acceptance rate.

Return your complete review as a single block of text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "62b6cf57-9975-45e9-ade7-e3dd3664b823",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T19:27:47.481Z_

```json
{
  "parentUuid": "62b6cf57-9975-45e9-ade7-e3dd3664b823",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
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
  "uuid": "d81ef9c7-3b0e-48db-ba63-4e47ffd84f84",
  "timestamp": "2026-05-14T19:27:47.481Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T19:27:50.573Z_



I'll start by reading the actual paper and any relevant project files to ground my review in the specific text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d81ef9c7-3b0e-48db-ba63-4e47ffd84f84",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31guzVHcWr9Dp1RR4mf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c40dec03-104c-44b9-82be-970ec7aa05a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Piu1SVd1hckZwYHdhyEddc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8510,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8510,
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

_source line 4 · 2026-05-14T19:27:51.204Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LaQHd9UGAYZrve4yNtYSSA`</summary>

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
  "parentUuid": "c40dec03-104c-44b9-82be-970ec7aa05a1",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31guzVHcWr9Dp1RR4mf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1cabd86-4598-4508-9085-abcc6c136d4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Piu1SVd1hckZwYHdhyEddc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8510,
      "cache_read_input_tokens": 8251,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8510
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 128,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 8510,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8510,
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

_source line 5 · 2026-05-14T19:27:51.208Z_

<details><summary>↩ Tool result · `toolu_01LaQHd9UGAYZrve4yNtYSSA`</summary>

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
  "parentUuid": "b1cabd86-4598-4508-9085-abcc6c136d4d",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "5eae65af-fb44-4aa1-9c91-5f7c3ba3b8d3",
  "sourceToolAssistantUUID": "b1cabd86-4598-4508-9085-abcc6c136d4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T19:27:54.206Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01HapWVEQT2RDmsfUtaNWA5j`</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5eae65af-fb44-4aa1-9c91-5f7c3ba3b8d3",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31hCJknVXaeQFLooJxx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ec7428d-3938-4787-b5ac-92bfd02b9daa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDDu8jxKpC7pQPhWvWF3NG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 16761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

_source line 7 · 2026-05-14T19:27:54.250Z_

<details><summary>↩ Tool result · `toolu_01HapWVEQT2RDmsfUtaNWA5j`</summary>

```text
{"result":"# 项目 distrib_canary_collapse 概况\n\n## 实验状态 (15 个)\n\n- **alpha_sweep_a025_s42_v2**: PREPARING — \n- **alpha_sweep_a025_s42**: PREPARING (killed) — \n- **mvp_v4_rep44**: DONE (success) — \n- **alpha_sweep_a000_s42**: PREPARING — \n- **mvp_rep44**: PREPARING — \n- **mvp_v4_rep45**: DONE (success) — \n- **mvp_v4_rep43**: DONE (success) — \n- **mvp_v4_rep42**: DONE (success) — \n- **mvp_v3_rep43**: DONE (failed) — \n- **mvp_v3_rep42**: DONE (failed) — \n- **mvp_v2_rep43**: DONE (killed) — \n- **mvp_v2_rep42**: DONE (killed) — \n- **mvp_v2_rep44**: PREPARING — \n- **mvp_rep43**: DONE (killed) — \n- **mvp_rep42**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- mvp_v2_rep44（准备中）\n- mvp_rep44（准备中）\n\n## 近期结论\n- **mvp_v4_rep45** (success): —\n- **mvp_v4_rep44** (failed): —\n- **mvp_v4_rep43** (success): —\n\n## 趋势\n成功 3 / 负向 0 / 失败 3 / 共 10\n累计 GPU: 4.2h\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-19828: 空闲 cuda:0, cuda:1\n\n## 告警\n- mvp_rep42: 已被终止 — unknown\n- mvp_rep43: 已被终止 — unknown\n- mvp_v2_rep42: 已被终止 — unknown\n- mvp_v2_rep43: 已被终止 — unknown\n- mvp_v3_rep42: 训练失败 — unknown\n- mvp_v3_rep43: 训练失败 — unknown\n- mvp_v4_rep44: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ec7428d-3938-4787-b5ac-92bfd02b9daa",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "2803b49d-cea9-4d1f-a3e8-ae3855fcd5dd",
  "sourceToolAssistantUUID": "0ec7428d-3938-4787-b5ac-92bfd02b9daa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T19:27:54.783Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CReKJP6BzzePCoC7w46TaM`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2803b49d-cea9-4d1f-a3e8-ae3855fcd5dd",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31hCJknVXaeQFLooJxx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd095cf6-a514-4338-bab8-32268c7c11ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDDu8jxKpC7pQPhWvWF3NG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 16761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

_source line 9 · 2026-05-14T19:27:54.791Z_

<details><summary>↩ Tool result · `toolu_01CReKJP6BzzePCoC7w46TaM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- mvp_v2_rep44（准备中）\\n- mvp_rep44（准备中）\\n\\n## 近期结论\\n- **mvp_v4_rep45** (success): —\\n- **mvp_v4_rep44** (failed): —\\n- **mvp_v4_rep43** (success): —\\n\\n## 趋势\\n成功 3 / 负向 0 / 失败 3 / 共 10\\n累计 GPU: 4.2h\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-19828: 空闲 cuda:0, cuda:1\\n\\n## 告警\\n- mvp_rep42: 已被终止 — unknown\\n- mvp_rep43: 已被终止 — unknown\\n- mvp_v2_rep42: 已被终止 — unknown\\n- mvp_v2_rep43: 已被终止 — unknown\\n- mvp_v3_rep42: 训练失败 — unknown\\n- mvp_v3_rep43: 训练失败 — unknown\\n- mvp_v4_rep44: 训练失败 — unknown\\n\", \"total_chars\": 560, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd095cf6-a514-4338-bab8-32268c7c11ac",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "c18faec3-985c-405a-95cf-54a0118235ef",
  "sourceToolAssistantUUID": "dd095cf6-a514-4338-bab8-32268c7c11ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T19:27:57.578Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01G2tfSk5CFL4azvja5r82Ru`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c18faec3-985c-405a-95cf-54a0118235ef",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31hTUaKzpE1Qsca6trx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82e4bf39-ff8d-4d47-b6f5-42b3db6c2949",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016pyywPMqTtP9crW8J58WVr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1477,
      "cache_read_input_tokens": 18212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1477,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 11 · 2026-05-14T19:27:57.585Z_

<details><summary>↩ Tool result · `toolu_01G2tfSk5CFL4azvja5r82Ru`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper_framing.md\", \"content\": \"# Paper Framing — distrib_canary_collapse\\n\\n## Target Venue\\n- Primary: AAAI 2027 (expected deadline ~August 2026)\\n- Fallback: EMNLP 2026 Findings (ARR October cycle if AAAI timeline tight)\\n- Note: EMNLP 2026 Main ARR May deadline已过；AAAI 2027 给出充足实验时间\\n\\n## Core Claims (3 条)\\n\\n1. **Canary→Diversity Lead**: 在迭代合成数据训练中，ECE 和 token entropy 作为廉价 canary 指标，稳定领先 diversity 退化（distinct_1/2）1-2 代——提供可量化的早期预警窗口。\\n2. **Regime-Dependent Predictability**: 可预测性取决于 contamination regime——100% SC 下 token_entropy→perplexity 存在一致的 lag=-5 弱信号（4/4 seed, p=0.058-0.12）但 N=11 统计效力不足，ECE→perplexity 则呈反向因果（perplexity 领先 ECE）。低 α 条件下 canary lead time 有望扩展。Predictability phase diagram 划定可预测/不可预测边界。\\n3. **Methodological Rigor**: 朴素相关分析在非平稳训练指标上产生伪回归；Toda-Yamamoto panel temporal precedence 提供统计严谨的 lead-lag 量化，方法论 ablation 量化伪显著关联被推翻的比例。\\n\\n## Story Spine\\n\\n- **Problem**: Model collapse 的在线监控工具已存在（SIGMA 谱监控、DCES 反应式干预），但没有工作系统性回答\\\"哪些指标最早预测崩溃、领先多久、在什么 regime 下有效\\\"。Du et al. 非正式观察到 ECE 领先 accuracy，但仅限单指标对、1-3 代、无统计检验。\\n\\n- **Existing approaches & their gaps**: SIGMA 提供谱监控但无 lead-time 量化；DCES 反应式而非预测式；Du et al. 是最接近的经验前辈但方法论不足（无正式 time-series 检验、无多家族对比）；Kalinowski 拓扑 CI 针对表征坍缩非合成数据退化且计算昂贵。Truong & Truong 证明一阶相变下标准早期预警指标失效——但仅限特定 regime 和特定指标族。\\n\\n- **Our framing**: 我们不是提出\\\"通用 canary\\\"，而是**系统性映射可预测性的边界**——哪些 collapse 维度可预测（diversity）、哪些不可预测（perplexity in extreme regime）、在什么 contamination 条件下、用什么统计方法。Null results（canary 不 lead perplexity）不是失败，而是 phase diagram 中的一个 boundary data point。\\n\\n- **Headline result template**: \\\"ECE and token entropy predict diversity collapse 1-2 generations ahead (|r|>0.99, p<0.001, 4/4 seeds) in iterative synthetic data training, while a predictability phase diagram reveals regime-dependent boundaries where canary signals exist vs. where synchronous collapse precludes early warning.\\\"\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n| Concern | Response Strategy | Required Experiment |\\n|---------|-------------------|---------------------|\\n| \\\"Canary 不预测 perplexity，实用价值有限\\\" | Framing 为 regime-dependent：100% SC 下 token_entropy 有 lag=-5 弱信号（plan_006 20-gen 验证）；α-sweep 展示低 α 下是否变显著 | α-sweep (P0) + plan_006 (P0) |\\n| \\\"ECE 和 token_entropy 对 perplexity 方向相反？\\\" | 诚实报告不对称性：token_entropy 捕捉分布收窄前驱信号（lead），ECE 作为 calibration 指标反映后期适应效应（lag）。两者覆盖 collapse 不同阶段 | 已有 MVP+plan_003 数据 |\\n| \\\"只在 Pythia-410M 上验证，scale 泛化？\\\" | Spot-check Pythia-1.4B × 核心条件 | scale-check (P1) |\\n| \\\"WikiText-103 单一数据集\\\" | C4 cross-domain validation | domain-transfer (P1) |\\n| \\\"为什么不用简单相关分析？\\\" | 方法 ablation：naive corr vs Toda-Yamamoto，量化伪显著比例 | method-ablation (P0, 零 GPU) |\\n| \\\"4 个 canary 中 2 个失败，选择偏差？\\\" | 全量报告 4 族结果，诚实讨论 effective_rank/self_bleu 失败原因 | 已有 MVP 数据 |\\n| \\\"Intervention 实验缺失\\\" | CRS-triggered vs reactive vs no-intervention 对比 | intervention (P2) |\\n\\n## Venue Fit\\n\\nAAAI 2027 优势：\\n- ML 方法论 track 接受 empirical analysis + 统计方法论贡献\\n- 不要求 SOTA，接受 systematic study with novel methodology\\n- Phase diagram / regime boundary 概念在 AAAI 偏理论的审稿人中有吸引力\\n\\n风险：\\n- 如果被认为\\\"只是 empirical study 没有算法贡献\\\"→ 补 CRS + intervention 提升 method 贡献\\n- 模型规模偏小（Pythia-410M/1.4B）→ 诚实标注 limitation + scaling trend\\n\\n## Key Narrative Constraints (from MVP + plan_003)\\n\\n1. **不能 claim \\\"canary predicts model collapse\\\"** — 只能 claim \\\"canary predicts diversity collapse\\\"。token_entropy→perplexity 在 100% SC 下存在一致的 lag=-5 弱信号（4/4 seed, p=0.058-0.12），但 N=11 统计效力不足——用\\\"统计不显著的弱信号\\\"而非\\\"通道断裂\\\"。plan_006（20-gen, N=21）是判定实验\\n2. **ECE→perplexity 呈反向因果** — perplexity 领先 ECE 4-5 代（lag=+4/+5, p<0.01）。与 token_entropy→perplexity（canary 领先）方向相反。论文必须讨论两个 canary 家族在 perplexity 通道上的不对称性\\n3. **effective_rank 和 self_bleu 作为 canary 失败** — 必须全量报告，不能只报正面结果\\n4. **distinct_3 的 lead time 不如 distinct_1/2 可靠** — max_lag=7 下升为 SIGNIFICANT 但 lag_std>1.5（双峰：seed 42 总是 -5，其余 -1/-2），维持 D008 降级策略，主文聚焦 distinct_1/2\\n5. **max_lag=7 确认核心 lead 无截断** — token_entropy→distinct_1 lag=-1（std=0.0）、ECE→distinct_2 lag=-1（std=0.0）在 max_lag=5/7 下完全一致。token_entropy→perplexity lag=-5 是真实峰值非截断伪影\\n\", \"total_chars\": 3872, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82e4bf39-ff8d-4d47-b6f5-42b3db6c2949",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "38dafa9d-7a2f-403c-9794-7744eed7259a",
  "sourceToolAssistantUUID": "82e4bf39-ff8d-4d47-b6f5-42b3db6c2949",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T19:27:58.516Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VhUsJeLEjGMhnvJs8H5WFn`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38dafa9d-7a2f-403c-9794-7744eed7259a",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31hTUaKzpE1Qsca6trx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2d9deb9-3ef3-462b-a215-e7a4d8eddac0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016pyywPMqTtP9crW8J58WVr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1477,
      "cache_read_input_tokens": 18212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1477,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 13 · 2026-05-14T19:27:58.523Z_

<details><summary>↩ Tool result · `toolu_01VhUsJeLEjGMhnvJs8H5WFn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/ROADMAP.md\", \"content\": \"# distrib_canary_collapse — Research Dashboard\\n\\n> 最后更新: 2026-05-14 19:09 UTC | 更新原因: plan_003 重分析结论：修正 perplexity 通道叙述（WEAK LEAD + ECE 反向因果），plan_006 升为 framing 判定实验\\n\\n## 核心方向\\n系统性映射迭代合成数据训练中 canary 指标的**可预测性边界**——哪些 collapse 维度可预测、用什么 canary、在什么 contamination regime 下。详见 paper_framing.md。\\n\\n**Refined narrative (D009→D010)**: Canary 指标（ECE/token_entropy）预测的是 diversity collapse（distinct_n 退化）。Perplexity 通道更复杂：token_entropy 对 perplexity 有一致的 lag=-5 弱信号（4/4 seed, p>0.05, N=11 效力不足），ECE 对 perplexity 呈反向因果（perplexity 领先 ECE）。plan_006（20-gen）是判定 token_entropy→perplexity 是否真实的关键实验。\\n\\n## 当前进展\\n- **阶段**: Research（MVP STRONG PASS + plan_003 max_lag=7 重分析完成）\\n- **MVP 核心发现**: ECE/token_entropy 领先 distinct_1/2 达 1-2 代（|r|>0.99, p<0.004, lag std=0.0）\\n- **plan_003 新发现**: token_entropy→perplexity lag=-5 是真实峰值（非截断），但 WEAK LEAD；ECE→perplexity 反向因果（lag=+4/+5）\\n- **排除指标**: self_bleu（方向不一致）、effective_rank（non-monotonic）、MAUVE（floor effect）\\n- **Framing**: \\\"Delineating Predictability Boundaries\\\"（D006），perplexity 通道叙述已修正（D010）\\n- **Target**: AAAI 2027（~Aug 2026 deadline）\\n- **Dream**: dream_20260514T184925 pending（full review mode）\\n- **代码部署**: ✅ α-sweep + accumulate + exit-code + 子采样 fix 已部署\\n- **累计 GPU**: 4.2h\\n\\n## 近期任务\\n- [ ] 启动 plan_001 α-sweep (P0): α∈{0.0, 0.25, 0.50, 0.75} × 3 seeds × 10 gen\\n- [ ] 启动 plan_006 extended 20-gen (P0): α=1.0 × 2 seeds × max_lag=10（**framing 判定实验**：token_entropy→perplexity 是否在 N=21 下变显著）\\n- [ ] 等 Dream 回调，按结果调整 framing/plan\\n- [ ] plan_002: 方法论 ablation（零 GPU，依赖 plan_001 数据）\\n\\n## GPU 预算\\n- **分配**: 2× RTX PRO 6000 Blackwell 96GB (westd-19828, cuda:0/cuda:1)\\n- **P0 估算**: ~48h（α-sweep 40h + extended run 8h）\\n- **P1 估算**: ~34h（C4 验证 10h + 1.4B spot-check 24h）\\n- **P2 估算**: ~20h（intervention 10h + accumulate ablation 10h）\\n- **总计**: ~102h，双卡 ~51h/卡（~2.1 天连续跑）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D010 | 2026-05-14 | plan_003 重分析修正 perplexity 通道叙述：WEAK LEAD 非断裂，ECE 反 | plan_003 |\\n| D009 | 2026-05-14 | MVP 4-seed STRONG PASS，进入 Research 阶段全面实验 | mvp_v4_rep42, mvp_v4_rep43, mvp_v4_rep44, mvp_v4_rep45 |\\n| D008 | 2026-05-14 | distinct_3 lead-lag 结果待 4-seed 确认，如 lag 仍双峰则降级 inc | mvp_v4_rep42, mvp_v4_rep43 |\\n| D007 | 2026-05-14 | Post-MVP 实验优先级：α-sweep >> 方法 ablation > C4 数据集 > 规 | — |\\n| D006 | 2026-05-14 | 论文 framing 采用 \\\"delineating predictability boundari | mvp_v4_rep42, mvp_v4_rep43 |\\n| D005 | 2026-05-14 | MVP 中期决策：不重启实验，MAUVE demote 为 supplementary，等完整 10 | — |\\n| D004 | 2026-05-14 | MVP 参数修复: n_prompts 1000→5000, steps_per_gen 10000 | — |\\n| D003 | 2026-05-14 | 首选 AAAI 2027 (~Aug 2026)，May 25 ARR 不可行，后续 ARR cyc | — |\\n| D002 | 2026-05-14 | MVP ECE 用 next-token calibration，SC 协议用 full repla | — |\\n| D001 | 2026-05-14 | MVP 设计: Pythia-410M × WikiText-103 × 100% SC × 10  | — |\\n\\n\", \"total_chars\": 2736, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2d9deb9-3ef3-462b-a215-e7a4d8eddac0",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "2241e114-88cf-40e9-84f6-fdbbd00f517f",
  "sourceToolAssistantUUID": "f2d9deb9-3ef3-462b-a215-e7a4d8eddac0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T19:27:59.473Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BLK4hApDLiEHrS3wike1Lo`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2241e114-88cf-40e9-84f6-fdbbd00f517f",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31hTUaKzpE1Qsca6trx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9dcc080f-ed3c-40b7-a2dc-f336ee370c10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016pyywPMqTtP9crW8J58WVr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1477,
      "cache_read_input_tokens": 18212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1477,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 15 · 2026-05-14T19:27:59.480Z_

<details><summary>↩ Tool result · `toolu_01BLK4hApDLiEHrS3wike1Lo`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'distrib_canary_collapse'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9dcc080f-ed3c-40b7-a2dc-f336ee370c10",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "c07b97d4-4c6d-4991-97c4-eff40d6824da",
  "sourceToolAssistantUUID": "9dcc080f-ed3c-40b7-a2dc-f336ee370c10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T19:27:59.648Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MM9EHMvzGPtv2qU3ZmPTid`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c07b97d4-4c6d-4991-97c4-eff40d6824da",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31hTUaKzpE1Qsca6trx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ae5210b-3cf6-4144-92f4-9a9b1009258e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016pyywPMqTtP9crW8J58WVr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1477,
      "cache_read_input_tokens": 18212,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1477
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 386,
          "cache_read_input_tokens": 18212,
          "cache_creation_input_tokens": 1477,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1477,
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

_source line 17 · 2026-05-14T19:27:59.659Z_

<details><summary>↩ Tool result · `toolu_01MM9EHMvzGPtv2qU3ZmPTid`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/memory.md\", \"content\": \"# Memory\\n\\n## 2026-05-14 — MVP 代码设计决策\\n\\n- **训练方式**: 用 HF Trainer，每代独立训练 steps_per_gen 步（非 epoch-based），避免数据量波动导致训练量不一致\\n- **Generation 0 = baseline**: 不训练，只计算初始指标，作为后续 degradation 的参照\\n- **synthetic_ratio 控制混合**: 1.0 = 纯合成（MVP 压力测试），以 synthetic 为基准，ratio<1 时按比例补 real\\n- **Self-BLEU 采样**: 随机抽 500 pairs 而非全组合（O(n²) 太贵），固定 seed=0 保证可复现\\n- **Effective rank**: 用 mean-pooled last hidden states 的协方差矩阵，exp(entropy of normalized eigenvalues)\\n- **MAUVE**: 依赖 mauve-text 包，用 eval_dataset（真实）vs gen_dataset（合成）对比\\n- **ECE**: next-token calibration，10 bins，softmax max prob vs correctness\\n- **Cross-correlation 分析**: normalize 后翻转符号使 \\\"collapse direction\\\" 一致为正，peak lag 的符号决定 lead/lag\\n- **Metrics JSON 每代独立保存 + 汇总**: gen_N/metrics.json 做细粒度追溯，all_metrics.json 做分析输入\\n\\n## 2026-05-14 — AutoDL 服务器经验\\n\\n- **HF 下载不要用 network_turbo 代理**（会卡死），改用 `HF_ENDPOINT=https://hf-mirror.com` 直连国内镜像\\n- **pip install 可以用 network_turbo**\\n- **服务器默认没有 tmux**，需手动 apt 安装\\n- 环境：conda base, Python 3.12.3, PyTorch 2.10.0+cu128, 2× RTX PRO 6000 Blackwell 96GB\\n- **服务器名**: `westd-19828`（非 autodl-rtx6000），submit_training_job 必须用此名\\n\\n## 2026-05-14 — 参数修复 (D004)\\n\\n- 原始参数：n_prompts=1000, steps_per_gen=10000 → 40 epochs/gen，过拟合导致指标骤然击穿\\n- 修正参数：n_prompts=5000, steps_per_gen=5000 → 4 epochs/gen，合理 fine-tuning 量\\n- WikiText-103 test split 仅 ~1500 条 ≥64 words 段落，不够 5000 prompts，改为从 train split 取 prompt 前缀（prompts 仅做生成种子，不参与 loss）\\n- 新数据放 data/wikitext103_5k/ 避免影响正在跑的实验\\n\\n## 2026-05-14 — 文献调研核心发现\\n\\n- 最直接竞争者：chen2025scales (arXiv 2510.05133) 报告 \\\"calibration degradation precedes accuracy loss\\\"——ECE 在 iter 1 + 30% synthetic 时上升 75%，accuracy 未显著变化。但**未做 lead-lag 因果分析**，也没多指标 panel\\n- 8 个文献空白中最关键的 3 个：(1) 无人做 canary Granger causality / lead-lag 量化 (2) ECE 在 collapse 场景下几乎未被系统研究 (3) 多指标 panel 框架完全缺失\\n- Novelty 风险：如果 chen2025scales 团队扩展工作，会侵蚀 ECE-as-canary 的 novelty。需在方法论（Granger causality 框架）上尽快建立壁垒\\n- 共收录 31 篇论文（含补全的 6 篇）\\n- SIGMA (arXiv 2601.03385): Gram matrix 谱双轨监控，我们的 effective rank 是其简化版\\n- Truong & Truong: Class 1 凸反馈 entropy collapse 是一阶相变，canary 在此 regime 可能失效\\n- Fu et al. (ICLR 2025): 恒定 real data 比例保证 STL 收敛，α-sweep 理论基础\\n\\n## 2026-05-14 — 运维教训\\n\\n- **kill_job 只杀 tmux session，不杀子进程**。旧进程 (v1) 存活导致 v2 写同一输出目录死锁。后续 kill 后必须用 `ps aux | grep iterative_train` 确认子进程全部死亡，必要时 `kill -9 $(pgrep -f iterative_train)`\\n- **提交新实验前必须确认输出目录干净**，或使用不同的输出路径\\n- **analyze_mvp.py dry-run 验证通过**：cross-correlation 逻辑正确，token_entropy 和 effective_rank 在信噪比充足时检测准确\\n- **pgrep -a iterative_train 匹配不到训练进程**：因为进程名是 `python`，不是脚本名。用 `nvidia-smi` 或 `ps aux | grep python` 检查\\n- **nohup 启动的实验不写 EXIT_CODE 哨兵**，cron 检测到进程退出后无法判断成功/失败，误判为 failed（rep44 事故）。已在 iterative_train.py 添加 EXIT_CODE 哨兵机制\\n\\n## 2026-05-14 — MVP 4-Seed 正式分析（FINAL VERDICT）\\n\\n- **Overall: STRONG PASS** — 2 个 canary 家族 (token_entropy, ECE) 各自对 ≥1 个 diversity 指标有 SIGNIFICANT LEAD\\n- **最强结果 (4/4 seed 完全一致, std=0)**:\\n  - token_entropy → distinct_1: lag=-1, |r|=0.993–0.998, p=0.0006–0.0036\\n  - ece → distinct_2: lag=-1, |r|=0.995–0.997, p=0.0001–0.0023\\n- **Demoted**: MAUVE (floor effect), effective_rank (non-monotonic, 2+/2- across seeds)\\n- **Eliminated**: self_bleu (方向不一致), ece→perplexity (ECE 反而滞后 perplexity)\\n\\n## 2026-05-14 — ⚠️ Narrative 约束（4-seed 确认 + max_lag=7 验证）\\n\\n- **Canary 仅能 lead diversity metrics (distinct_n)，不能 lead quality metric (perplexity)**\\n  - token_entropy→perplexity: lag=-5，4/4 seed 一致，但 p borderline（seed42 p=0.12）\\n  - **max_lag=7 重分析确认 lag=-5 不是截断伪影**——扩展搜索窗口后 lag 值完全不变（2026-05-14 验证）\\n  - 问题在统计功效不足（仅 10 代数据点），不在截断\\n  - ECE→perplexity: lag=+4.75（ECE 滞后 perplexity！完全反向）\\n  - 这限制论文 claim：只能声称 \\\"canary predicts diversity collapse\\\"，不能声称 \\\"canary predicts general model degradation\\\"\\n- **Narrative 方向建议**: \\\"distributional canaries predict diversity collapse, which is a necessary precursor to quality degradation\\\"——diversity 丧失先于 perplexity 退化\\n- **plan_006 (extended 20-gen) 可能突破此限制**：如果 max_lag 从 5 扩到 10，token_entropy→perplexity 的 lead 可能变显著\\n- **α-sweep (plan_001) 是关键实验**：100% SC 下 collapse 太剧烈（37x ppl↑），canary 和 perplexity 几乎同步恶化。温和条件（α=0.25-0.75）下 collapse 更渐进，canary 的 lead time 对 perplexity 可能有效\\n\\n## 2026-05-14 — mix_datasets bug 修复\\n\\n- **原逻辑**: 保全 synthetic，subsample real → 低 α 下 real 不足时比例静默偏移（α=0.25 变成实际 α=0.50）\\n- **修复后**: 双向 subsample（低 α: 保全 real + subsample syn; 高 α: 保全 syn + subsample real）\\n- 14/14 测试通过，全 α 范围误差 <0.05\\n\", \"total_chars\": 4245, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ae5210b-3cf6-4144-92f4-9a9b1009258e",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "a0ae02f4-534e-4905-b964-57554790e360",
  "sourceToolAssistantUUID": "8ae5210b-3cf6-4144-92f4-9a9b1009258e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-14T19:28:02.931Z_

Now let me look at the actual paper and experiment artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0ae02f4-534e-4905-b964-57554790e360",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31hpEz1eigKSZZP8w9j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf60f048-8799-4272-bd66-6a4c56680b85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWYoTZ482ppbPph4RrZAJ1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7224,
      "cache_read_input_tokens": 19689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7224,
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

_source line 19 · 2026-05-14T19:28:03.419Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017SWxCDK2Z98iWriNbHaSiL`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf60f048-8799-4272-bd66-6a4c56680b85",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31hpEz1eigKSZZP8w9j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3356243-8556-436d-ae60-2a5f36ae3f81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWYoTZ482ppbPph4RrZAJ1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7224,
      "cache_read_input_tokens": 19689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7224,
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

_source line 20 · 2026-05-14T19:28:03.433Z_

<details><summary>↩ Tool result · `toolu_017SWxCDK2Z98iWriNbHaSiL`</summary>

```text
artifacts/dream_reports/dream_20260514T184925/best/paper.tex
artifacts/dream_reports/dream_20260514T184925/median/paper.tex
artifacts/dream_reports/dream_20260514T184925/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3356243-8556-436d-ae60-2a5f36ae3f81",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "2556fc13-8ab2-4575-917a-7554f1f511da",
  "sourceToolAssistantUUID": "c3356243-8556-436d-ae60-2a5f36ae3f81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T19:28:04.399Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013G2tNMY4hm632c7ieGF2kB`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2556fc13-8ab2-4575-917a-7554f1f511da",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31hpEz1eigKSZZP8w9j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e9ab588-131e-4073-a84c-dc08f66c8dbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWYoTZ482ppbPph4RrZAJ1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7224,
      "cache_read_input_tokens": 19689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7224,
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

_source line 22 · 2026-05-14T19:28:04.417Z_

<details><summary>↩ Tool result · `toolu_013G2tNMY4hm632c7ieGF2kB`</summary>

```text
artifacts/dream_reports/dream_20260514T184925/best/paper.pdf
artifacts/dream_reports/dream_20260514T184925/median/paper.pdf
artifacts/dream_reports/dream_20260514T184925/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e9ab588-131e-4073-a84c-dc08f66c8dbb",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "8f81d3fe-f82a-49c1-84dd-66745633e367",
  "sourceToolAssistantUUID": "6e9ab588-131e-4073-a84c-dc08f66c8dbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T19:28:04.745Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TmhDE9Gmj2ypGB7aZFkKjA`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f81d3fe-f82a-49c1-84dd-66745633e367",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31hpEz1eigKSZZP8w9j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cda1321f-a962-487d-9456-2b594d8fcd3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWYoTZ482ppbPph4RrZAJ1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7224,
      "cache_read_input_tokens": 19689,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7224
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 276,
          "cache_read_input_tokens": 19689,
          "cache_creation_input_tokens": 7224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7224,
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

_source line 24 · 2026-05-14T19:28:04.752Z_

<details><summary>↩ Tool result · `toolu_01TmhDE9Gmj2ypGB7aZFkKjA`</summary>

```text
artifacts/_project/intermediate/iterative_train.py
artifacts/prepare_data.py
artifacts/metrics.py
artifacts/analyze_mvp.py
artifacts/iterative_train.py
artifacts/test_alpha_sweep.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cda1321f-a962-487d-9456-2b594d8fcd3c",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "78a9eb04-b764-4fd9-b89e-f62f72d9b8fa",
  "sourceToolAssistantUUID": "cda1321f-a962-487d-9456-2b594d8fcd3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T19:28:07.284Z_

<details open><summary>🔧 Tool call — Read · `toolu_011EhqCWLDNgyoCyDVMy1Ecv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78a9eb04-b764-4fd9-b89e-f62f72d9b8fa",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31iC1RWA59z9z3LCaSQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e48f157e-2883-420d-b8cd-5de28469ed46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012w2Qx9YbzGoUHEjZV4NKhv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 26913,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 539
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 102,
          "cache_read_input_tokens": 26913,
          "cache_creation_input_tokens": 539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 539,
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

_source line 26 · 2026-05-14T19:28:07.542Z_

<details><summary>↩ Tool result · `toolu_011EhqCWLDNgyoCyDVMy1Ecv`</summary>

```text
1	\documentclass[letterpaper,11pt]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{graphicx}
5	\usepackage{amsmath,amssymb}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage{natbib}
11	
12	\setcounter{secnumdepth}{2}
13	
14	\title{Distributional Canary Collapse: Predictability Phase Diagrams\\for Early Warning in Iterative Synthetic Data Training}
15	
16	\author{
17	Anonymous Authors
18	}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	Iterative training on self-generated synthetic data leads to model collapse---progressive degradation of output quality and diversity.
25	While prior work has identified monitoring signals and reactive interventions, no systematic study has answered \emph{which} metrics earliest predict collapse, \emph{how far} ahead they lead, and \emph{under what contamination regime} such predictions hold.
26	We introduce a \textbf{predictability phase diagram} that maps the boundary between predictable and unpredictable collapse as a function of the synthetic data mixing ratio~$\alpha$.
27	Through Toda--Yamamoto panel temporal precedence testing on Pythia-410M and Pythia-1.4B across WikiText-103 and C4, we establish three results:
28	(1)~ECE and token entropy serve as \emph{canary} metrics that lead diversity collapse (distinct-$n$) by 1--3 generations across all tested regimes ($p<0.005$, all seeds);
29	(2)~a phase boundary at $\alpha^*\!\approx\!0.60$ separates regimes where canaries also lead perplexity ($\alpha \le 0.50$, $p<0.05$) from regimes where perplexity collapses synchronously with canaries ($\alpha \ge 0.75$, $p>0.18$);
30	(3)~naive Pearson lag-correlation produces ${\sim}41\%$ spurious significant associations on these non-stationary series, which the Toda--Yamamoto test correctly overturns.
31	Cross-domain (C4) and scale (1.4B) spot-checks preserve canary ranking (Spearman $\rho = 0.94$), and a canary-triggered intervention recovers 77\% of lost diversity at $\alpha = 0.75$.
32	\end{abstract}
33	
34	%----------------------------------------------------------------------
35	\section{Introduction}
36	%----------------------------------------------------------------------
37	
38	Training language models on their own outputs across successive generations---\emph{iterative self-consuming training}---causes \emph{model collapse}: a progressive narrowing of the output distribution that manifests as reduced lexical diversity, rising perplexity on held-out data, and deteriorating calibration \cite{shumailov2024ai}.
39	As synthetic data becomes increasingly prevalent in training pipelines, understanding and mitigating collapse is a pressing concern.
40	
41	Several monitoring tools exist. Spectral methods such as SIGMA track representation-level drift \cite{dohmatob2024model}; reactive interventions like DCES inject corrective signals after degradation is detected. Du et al.\ informally observed that expected calibration error (ECE) rises before accuracy degrades, but their study was limited to a single metric pair, 1--3 generations, and lacked formal time-series testing.
42	
43	A fundamental question remains unanswered: \emph{which metrics earliest predict collapse, how far ahead, and under what conditions?}
44	Answering this requires (i) a systematic comparison across metric families, (ii) a statistically rigorous lead--lag quantification method suited to non-stationary series, and (iii) exploration of the contamination regime.
45	
46	\paragraph{Contributions.}
47	We present a \textbf{predictability phase diagram} for iterative synthetic data training that maps the boundary between predictable and unpredictable collapse:
48	\begin{enumerate}
49	    \item \textbf{Canary$\to$Diversity Lead.} ECE and token entropy reliably lead diversity metrics (distinct-1/2) by 1--3 generations across all tested contamination ratios~$\alpha$, verified by Toda--Yamamoto (TY) panel temporal precedence ($p<0.005$, 3/3 seeds).
50	    \item \textbf{Regime-Dependent Predictability.} At $\alpha^*\!\approx\!0.60$, a phase transition separates regimes where canaries also lead perplexity from regimes where synchronous collapse precludes early warning.
51	    \item \textbf{Methodological Rigor.} We show that naive Pearson correlation on these non-stationary training trajectories yields ${\sim}41\%$ spurious significant associations, which the TY test correctly rejects. This methodological contribution stands independently of the specific canary findings.
52	\end{enumerate}
53	
54	We validate across domains (WikiText-103, C4), scales (410M, 1.4B parameters), data strategies (replace, accumulate), and demonstrate a canary-triggered intervention that recovers 77\% of diversity loss.
55	
56	%----------------------------------------------------------------------
57	\section{Related Work}
58	%----------------------------------------------------------------------
59	
60	\paragraph{Model collapse in iterative training.}
61	Shumailov et al.\ established that iterative training on self-generated data leads to progressive distribution narrowing. Subsequent theoretical analysis by Dohmatob et al.\ characterized spectral signatures of collapse, while Alemohammad et al.\ showed that mixing real data at ratio $1-\alpha$ can stabilize training under certain conditions. Fu et al.\ proved that accumulating historical generations bounds distributional drift, whereas replacing data each generation may diverge.
62	
63	\paragraph{Early warning and monitoring.}
64	SIGMA provides spectral monitoring of representation collapse but does not quantify temporal lead over downstream quality metrics. DCES operates reactively rather than predictively. Du et al.\ observed ECE rising before accuracy degradation, the closest antecedent to our work, but did not employ formal temporal precedence testing, examined only one metric pair, and did not explore regime dependence. Truong and Truong showed that standard early-warning indicators can fail under first-order phase transitions---our phase diagram explicitly maps where canary signals succeed and where they break down.
65	
66	\paragraph{Time-series causality in non-stationary settings.}
67	Granger causality testing requires stationarity, which training metric trajectories violate. The Toda--Yamamoto (TY) procedure augments the VAR lag order to accommodate integrated processes without pre-testing for unit roots, providing valid inference regardless of integration order. We adopt TY as our primary lead--lag quantification tool.
68	
69	%----------------------------------------------------------------------
70	\section{Method}
71	%----------------------------------------------------------------------
72	
73	\subsection{Iterative Self-Consuming Training Protocol}
74	
75	We train a language model $M_0$ on real data $D_0$ for one epoch, then iterate: at generation $t$, we sample synthetic data $S_t$ from $M_{t-1}$, form the training set $D_t = (1-\alpha)\,D_0 + \alpha\,S_t$ under the \textbf{replace} strategy (or $D_t = D_0 \cup \bigcup_{i=1}^{t} S_i$ under \textbf{accumulate}), and train $M_t$ on $D_t$.
76	We sweep $\alpha \in \{0.25, 0.50, 0.75, 1.00\}$ with 3 random seeds per condition.
77	
78	\subsection{Metric Families}
79	
80	We compute six metrics at each generation, grouped into three families:
81	
82	\paragraph{Canary candidates.} (i)~\textbf{ECE} (expected calibration error): measures miscalibration via binned confidence--accuracy gap. (ii)~\textbf{Token entropy}: Shannon entropy of the unigram token distribution in generated text. (iii)~\textbf{Effective rank}: the exponential of the entropy of the normalized singular values of the last-layer representations. (iv)~\textbf{Self-BLEU}: average pairwise BLEU among generated samples.
83	
84	\paragraph{Diversity targets.} (v)~\textbf{Distinct-$n$} ($n=1,2,3$): ratio of unique $n$-grams to total $n$-grams in generated text.
85	
86	\paragraph{Quality target.} (vi)~\textbf{Perplexity}: held-out perplexity on the original test split.
87	
88	\subsection{Toda--Yamamoto Panel Temporal Precedence}
89	
90	For each canary--target pair $(X,Y)$, we fit a bivariate VAR($k+d_{\max}$) where $k$ is selected by AIC and $d_{\max}$ is the maximal integration order (set to 1). We test the null $H_0$: lagged $X$ does not Granger-cause $Y$ by a Wald test on the first $k$ lag coefficients of $X$ in the $Y$ equation, following the Toda--Yamamoto procedure.
91	We report the optimal lag (negative = $X$ leads $Y$) and the $p$-value.
92	We pool across seeds using a panel specification with fixed effects.
93	
94	\subsection{Lead Time Quantification}
95	
96	We define the \textbf{$2\sigma$ onset} of metric $m$ as the earliest generation $t$ where $|m_t - m_0| > 2\,\text{std}(m_0)$, estimated from 3 independent initializations.
97	The \textbf{canary$\to$target lead} is the difference in onset generations.
98	This complements the TY test: TY provides a $p$-value for temporal precedence, while onset lead gives an interpretable time window.
99	
100	\subsection{Canary-Responsive Strategy (CRS)}
101	
102	As a proof-of-concept intervention, CRS monitors ECE at each generation. When a $2\sigma$ onset is detected, it reduces $\alpha$ by increasing the real data proportion (effective $\alpha$ post-trigger $\approx$ 0.52 from an initial 0.75).
103	
104	%----------------------------------------------------------------------
105	\section{Experimental Setup}
106	%----------------------------------------------------------------------
107	
108	\paragraph{Models.} Pythia-410M (primary) and Pythia-1.4B (scale check), both pretrained checkpoints from EleutherAI.
109	
110	\paragraph{Data.} WikiText-103 (primary) and C4 (cross-domain). We generate 50k tokens per generation for synthetic data, matching the original training set size.
111	
112	\paragraph{Training.} Each generation is fine-tuned for 1 epoch with AdamW (lr=$5\!\times\!10^{-5}$, batch size 16). 10 generations per run (20 for extended validation).
113	
114	\paragraph{Reproducibility.} 3 seeds per condition (4 seeds for the original MVP at $\alpha=1.0$). All TY tests use max\_lag $\geq 7$ unless otherwise noted.
115	
116	%----------------------------------------------------------------------
117	\section{Experiments and Results}
118	%----------------------------------------------------------------------
119	
120	\subsection{$\alpha$-Sweep: The Predictability Phase Diagram}
121	\label{sec:alpha_sweep}
122	
123	The core experiment sweeps $\alpha \in \{0.25, 0.50, 0.75, 1.00\}$ on Pythia-410M $\times$ WikiText-103 $\times$ 3 seeds $\times$ 10 generations. Table~\ref{tab:alpha_sweep} reports end-state metrics and canary lead times; Table~\ref{tab:ty_panel} reports the full TY panel results.
124	
125	\begin{table*}[t]
126	\centering
127	\caption{$\alpha$-sweep summary statistics (mean $\pm$ std across 3 seeds, except $\alpha\!=\!1.0$: 4 seeds). ``Canary$\to$d1 lead'' and ``canary$\to$ppl lead'' are $2\sigma$ onset differences in generations.}
128	\label{tab:alpha_sweep}
129	\small
130	\begin{tabular}{@{}lcccccccc@{}}
131	\toprule
132	$\alpha$ & gen10 ppl & gen10 entropy & gen10 ECE & gen10 d1 & gen10 d2 & canary$\to$d1 lead & canary$\to$ppl lead & TY $p$ (ECE$\to$ppl) \\
133	\midrule
134	0.25 & 68.4$\pm$4.1   & 2.41$\pm$0.05 & 0.138$\pm$0.009 & 0.312$\pm$0.018 & 0.681$\pm$0.022 & 2.7$\pm$0.3 & 2.0$\pm$0.4 & 0.018 \\
135	0.50 & 189.3$\pm$12.6  & 1.94$\pm$0.07 & 0.247$\pm$0.015 & 0.198$\pm$0.014 & 0.512$\pm$0.019 & 2.0$\pm$0.2 & 1.3$\pm$0.3 & 0.032 \\
136	0.75 & 512.7$\pm$31.4  & 1.52$\pm$0.09 & 0.361$\pm$0.021 & 0.112$\pm$0.011 & 0.402$\pm$0.025 & 1.7$\pm$0.2 & 0.3$\pm$0.5 & 0.214 \\
137	1.00 & 1024.7$\pm$16.8 & 1.27$\pm$0.06 & 0.420$\pm$0.012 & 0.075$\pm$0.008 & 0.365$\pm$0.015 & 1.5$\pm$0.3 & 0.0$\pm$0.2 & 0.487 \\
138	\bottomrule
139	\end{tabular}
140	\end{table*}
141	
142	\begin{table*}[t]
143	\centering
144	\caption{Toda--Yamamoto panel results for all canary$\to$target pairs. Each cell shows (optimal lag, $p$-value); negative lag indicates the canary leads the target. Bold entries are significant at $p<0.05$.}
145	\label{tab:ty_panel}
146	\small
147	\begin{tabular}{@{}llcccc@{}}
148	\toprule
149	Canary & Target & $\alpha=0.25$ & $\alpha=0.50$ & $\alpha=0.75$ & $\alpha=1.0$ \\
150	\midrule
151	ECE          & distinct\_1 & \textbf{($-$3, $<$0.001)} & \textbf{($-$2, $<$0.001)} & \textbf{($-$2, 0.003)} & \textbf{($-$2, $<$0.001)} \\
152	ECE          & distinct\_2 & \textbf{($-$3, 0.002)}    & \textbf{($-$2, 0.002)}    & \textbf{($-$2, 0.006)} & \textbf{($-$1, 0.004)} \\
153	token\_ent   & distinct\_1 & \textbf{($-$2, 0.003)}    & \textbf{($-$2, 0.004)}    & \textbf{($-$1, 0.012)} & \textbf{($-$1, 0.003)} \\
154	token\_ent   & distinct\_2 & \textbf{($-$3, 0.004)}    & \textbf{($-$2, 0.006)}    & \textbf{($-$2, 0.018)} & \textbf{($-$1, 0.009)} \\
155	\midrule
156	ECE          & perplexity  & \textbf{($-$2, 0.015)}    & \textbf{($-$1, 0.032)}    & (0, 0.187)             & (0, 0.412) \\
157	token\_ent   & perplexity  & \textbf{($-$2, 0.021)}    & \textbf{($-$1, 0.041)}    & (0, 0.238)             & ($-$5*, 0.063) \\
158	\midrule
159	eff\_rank    & distinct\_1 & (0, 0.342) & (0, 0.287) & (0, 0.415) & (0, 0.523) \\
160	self\_bleu   & distinct\_1 & (0, 0.178) & (0, 0.221) & ($-$1, 0.089) & (0, 0.156) \\
161	\bottomrule
162	\end{tabular}
163	\end{table*}
164	
165	\paragraph{Key findings.}
166	Three patterns emerge from Tables~\ref{tab:alpha_sweep}--\ref{tab:ty_panel}:
167	
168	\textit{(i) Canary$\to$diversity is universally predictable.}
169	ECE and token entropy significantly lead distinct-1 and distinct-2 at all $\alpha$ values ($p < 0.02$), with lead times of 1.5--2.7 generations. Cross-seed consistency is 3/3 at every $\alpha$.
170	
171	\textit{(ii) Canary$\to$perplexity is regime-dependent.}
172	At $\alpha \le 0.50$, ECE leads perplexity by 1--2 generations ($p < 0.05$). At $\alpha = 0.75$, the lead vanishes ($p = 0.187$--$0.238$). The phase boundary $\alpha^* \approx 0.60$ marks the transition. This occurs because lower~$\alpha$ slows distributional drift, allowing the sensitivity gap between canary metrics (which detect small KL-divergence shifts) and perplexity (which requires structural loss-landscape changes) to manifest as a temporal lead.
173	
174	\textit{(iii) Failed canaries.}
175	Effective rank and self-BLEU show no significant lead over any target at any~$\alpha$ ($p > 0.08$). We report these null results in full: the canary phenomenon is specific to calibration and token-distribution metrics, not a universal property of all collapse indicators.
176	
177	\subsection{Methodological Ablation: Naive vs.\ Robust Testing}
178	\label{sec:method_ablation}
179	
180	We compare four lead--lag quantification methods on the pooled MVP (4 seeds, $\alpha=1.0$) and $\alpha$-sweep (9 runs) data: naive Pearson lag-correlation, differenced cross-correlation, threshold-based onset lead, and TY panel temporal precedence. Table~\ref{tab:method_comparison} reports significant pair counts; Table~\ref{tab:false_positives} breaks down the false positives.
181	
182	\begin{table}[t]
183	\centering
184	\caption{Method comparison: significant pair counts out of 104 total canary$\to$target pairs tested. ``False positive vs TY'' counts pairs significant under the method but not under TY.}
185	\label{tab:method_comparison}
186	\small
187	\begin{tabular}{@{}lcccc@{}}
188	\toprule
189	Method & Sig.\ pairs & Agrees & FP vs TY & FN vs TY \\
190	\midrule
191	Naive Pearson     & 71/104 & 42 & 29 (40.8\%) & 0 \\
192	Differenced XCorr & 48/104 & 36 & 12 (16.9\%) & 6 \\
193	Threshold Onset   & 39/104 & 37 &  2 (2.8\%)  & 5 \\
194	Toda--Yamamoto    & 42/104 & --- & ---         & --- \\
195	\bottomrule
196	\end{tabular}
197	\end{table}
198	
199	\begin{table}[t]
200	\centering
201	\caption{Breakdown of 29 naive Pearson false positives overturned by TY.}
202	\label{tab:false_positives}
203	\small
204	\begin{tabular}{@{}lcp{3.5cm}@{}}
205	\toprule
206	Category & Count & Example \\
207	\midrule
208	Failed canary $\to$ any target & 20 & eff\_rank$\to$d1, $\alpha\!=\!0.50$ \\
209	canary$\to$ppl at $\alpha\!\ge\!0.75$ & 6 & ECE$\to$ppl, $\alpha\!=\!0.75$ \\
210	Reverse direction & 3 & d1$\to$ECE, $\alpha\!=\!1.0$ \\
211	\bottomrule
212	\end{tabular}
213	\end{table}
214	
215	Naive Pearson correlation declares 71 out of 104 pairs significant---a 40.8\% false-positive rate relative to TY. The spurious associations arise from three sources: (1)~all-declining metrics producing high $|r|$ via shared trends (effective rank and self-BLEU pairs: 20 cases); (2)~synchronous collapse at high $\alpha$ being misclassified as directional lead (6 cases); and (3)~bidirectional correlation conflating target$\to$canary with canary$\to$target direction (3 cases).
216	
217	The threshold-onset method agrees with TY in 88\% of cases, but TY provides $p$-values and directional testing, yielding stronger statistical evidence for or against temporal precedence.
218	
219	\subsection{MVP Formalization ($\alpha = 1.0$, max\_lag = 7)}
220	\label{sec:mvp}
221	
222	We re-run TY testing on the original 4-seed MVP data with max\_lag increased from 5 to 7 to verify whether the marginal entropy$\to$perplexity signal at lag~$= -5$ is a truncation artifact. Results appear in Table~\ref{tab:mvp_maxlag}.
223	
224	\begin{table}[t]
225	\centering
226	\caption{MVP ($\alpha\!=\!1.0$) TY results: max\_lag$\,=\,$5 vs.\ 7.}
227	\label{tab:mvp_maxlag}
228	\small
229	\begin{tabular}{@{}lccc@{}}
230	\toprule
231	Pair & lag=5 & lag=7 & Conclusion \\
232	\midrule
233	ECE$\to$d1       & ($-$2, $<$0.001) & ($-$2, 0.0004) & Stable lead \\
234	ECE$\to$d2       & ($-$1, 0.003) & ($-$1, 0.004) & Stable \\
235	ent$\to$d1       & ($-$1, 0.002) & ($-$1, 0.0018) & Stable \\
236	ent$\to$ppl      & ($-$5, 0.052) & ($-$5, 0.071) & Not significant \\
237	ECE$\to$ppl      & (0, 0.38) & (0, 0.412)    & Not significant \\
238	\bottomrule
239	\end{tabular}
240	\end{table}
241	
242	The canary$\to$diversity leads are stable under increased max\_lag ($p < 0.005$). The entropy$\to$perplexity lag$\,= -5$ signal weakens from $p = 0.052$ to $p = 0.071$---confirming it as statistical noise rather than a truncation artifact. At $\alpha = 1.0$, $2\sigma$ onsets for ECE (gen~2.1$\pm$0.3), entropy (gen~2.4$\pm$0.4), and perplexity (gen~2.3$\pm$0.3) are nearly synchronous, leaving insufficient temporal separation for canary$\to$perplexity lead.
243	
244	\subsection{Cross-Domain Validation: C4}
245	\label{sec:c4}
246	
247	To test domain invariance, we replicate the $\alpha = 0.50$ condition on C4 (web crawl data) with Pythia-410M $\times$ 3 seeds $\times$ 10 generations. Table~\ref{tab:cross_domain} compares results with WikiText-103.
248	
249	\begin{table}[t]
250	\centering
251	\caption{Cross-domain comparison at $\alpha\!=\!0.50$. All lags and $p$-values from TY panel tests.}
252	\label{tab:cross_domain}
253	\small
254	\begin{tabular}{@{}lccc@{}}
255	\toprule
256	Metric pair & WikiText-103 & C4 & $\Delta$lag \\
257	\midrule
258	ECE$\to$d1       & ($-$2, $<$0.001) & ($-$2, 0.003) & 0 \\
259	ent$\to$d1       & ($-$2, 0.004) & ($-$2, 0.006)    & 0 \\
260	ECE$\to$ppl      & ($-$1, 0.032) & ($-$1, 0.044)    & 0 \\
261	ent$\to$ppl      & ($-$1, 0.041) & ($-$1, 0.058)    & 0 \\
262	eff\_rank$\to$d1 & (0, 0.287) & (0, 0.334)          & 0 \\
263	\bottomrule
264	\end{tabular}
265	\end{table}
266	
267	Canary ranking is preserved across domains with Spearman rank correlation $\rho = 0.94$ between WikiText-103 and C4 lag structures. All significant pairs on WikiText-103 remain significant on C4; all non-significant pairs remain non-significant. Absolute metric values differ (C4 gen-10 perplexity 211.8 vs.\ WikiText 189.3, reflecting noisier web text), but the temporal precedence structure is invariant. This supports the interpretation that the canary mechanism is model-intrinsic rather than data-specific.
268	
269	\subsection{Scale Spot-Check: Pythia-1.4B}
270	\label{sec:scale}
271	
272	We run Pythia-1.4B (3.4$\times$ parameters) at $\alpha = 0.50$ on WikiText-103 to test scale robustness. Table~\ref{tab:scale} compares with the 410M baseline.
273	
274	\begin{table}[t]
275	\centering
276	\caption{Scale comparison at $\alpha\!=\!0.50$, WikiText-103.}
277	\label{tab:scale}
278	\small
279	\begin{tabular}{@{}lccccc@{}}
280	\toprule
281	Model & gen10 ppl & c$\to$d1 lead & c$\to$ppl lead & TY $p$ (ECE$\to$d1) & TY $p$ (ECE$\to$ppl) \\
282	\midrule
283	Pythia-410M & 189.3 & 2.0 gen & 1.3 gen & $<$0.005 & 0.032 \\
284	Pythia-1.4B & 142.5 & 2.3 gen & 1.5 gen & 0.002 & 0.028 \\
285	\bottomrule
286	\end{tabular}
287	\end{table}
288	
289	Canary ranking is preserved at the larger scale. Lead times are slightly longer (2.3 vs.\ 2.0~gen for diversity; 1.5 vs.\ 1.3~gen for perplexity), consistent with the hypothesis that larger models collapse more gradually per generation, allowing the metric sensitivity gap to accumulate over more generations. The 1.4B model achieves lower gen-10 perplexity (142.5 vs.\ 189.3), indicating higher capacity provides partial resilience.
290	
291	\subsection{Extended Run: 20 Generations ($\alpha = 1.0$)}
292	\label{sec:extended}
293	
294	We extend the $\alpha = 1.0$ condition to 20 generations (2 seeds, max\_lag = 10) to rule out sequence-length artifacts. Table~\ref{tab:extended} compares 10-gen and 20-gen TY results.
295	
296	\begin{table}[t]
297	\centering
298	\caption{Extended run ($\alpha\!=\!1.0$) TY results with max\_lag$\,=\,$10.}
299	\label{tab:extended}
300	\small
301	\begin{tabular}{@{}lccc@{}}
302	\toprule
303	Pair & 10-gen & 20-gen & Conclusion \\
304	\midrule
305	ent$\to$ppl  & ($-$5, 0.071) & (0, 0.523) & No lead---confirmed \\
306	ECE$\to$d1   & ($-$2, 0.0004) & ($-$2, 0.0002) & Stable lead \\
307	ECE$\to$ppl  & (0, 0.412) & (0, 0.487)       & No lead---confirmed \\
308	\bottomrule
309	\end{tabular}
310	\end{table}
311	
312	With 20 generations and max\_lag $= 10$, the entropy$\to$perplexity ``signal'' vanishes entirely (lag~$= 0$, $p = 0.523$), confirming its absence is genuine. The canary$\to$diversity lead strengthens ($p = 0.0002$). Collapse saturates around generation~12 (gen-20 perplexity: 4287.3; gen-20 distinct-1: 0.024), consistent with the model output becoming near-deterministic.
313	
314	\subsection{Canary-Responsive Intervention}
315	\label{sec:intervention}
316	
317	We evaluate CRS at $\alpha = 0.75$ (the regime where canary$\to$perplexity lead is absent but canary$\to$diversity lead persists). When ECE triggers $2\sigma$ onset (gen~3.2$\pm$0.4), CRS reduces $\alpha$ from 0.75 to an effective $\sim$0.52. Table~\ref{tab:intervention} compares three conditions.
318	
319	\begin{table}[t]
320	\centering
321	\caption{Intervention results at $\alpha\!=\!0.75$ (mean $\pm$ std, 3 seeds). Oracle uses $\alpha\!=\!0.50$ throughout.}
322	\label{tab:intervention}
323	\small
324	\begin{tabular}{@{}lcccc@{}}
325	\toprule
326	Condition & gen10 d1 & gen10 d2 & gen10 ppl & gen10 ECE \\
327	\midrule
328	No intervention       & .112$\pm$.011 & .402$\pm$.025 & 512.7$\pm$31.4 & .361$\pm$.021 \\
329	CRS (ECE trigger)     & .198$\pm$.015 & .524$\pm$.020 & 341.2$\pm$22.7 & .253$\pm$.018 \\
330	Oracle ($\alpha\!=\!.50$) & .198$\pm$.014 & .512$\pm$.019 & 189.3$\pm$12.6 & .247$\pm$.015 \\
331	\bottomrule
332	\end{tabular}
333	\end{table}
334	
335	CRS recovers 76.8\% of the diversity gap between the no-intervention and $\alpha = 0.25$ baselines (computed as $(0.198 - 0.112)/(0.312 - 0.112) = 0.43$, relative to the full $\alpha$-sweep range). It matches the oracle on gen-10 distinct-1 ($0.198$ vs.\ $0.198$) and reduces perplexity by 33.4\% ($512.7 \to 341.2$). The perplexity gap relative to oracle ($341.2$ vs.\ $189.3$) reflects irreversible calibration drift accumulated during the first 3 generations at high~$\alpha$.
336	
337	\subsection{Data Strategy Ablation: Accumulate vs.\ Replace}
338	\label{sec:data_strategy}
339	
340	At $\alpha = 0.50$, we compare the standard replace strategy (each generation trains on fresh synthetic data) with accumulate (all historical synthetic data is retained). Table~\ref{tab:data_strategy} reports results.
341	
342	\begin{table}[t]
343	\centering
344	\caption{Data strategy comparison at $\alpha\!=\!0.50$ (mean, 3 seeds).}
345	\label{tab:data_strategy}
346	\small
347	\begin{tabular}{@{}lcccc@{}}
348	\toprule
349	Strategy & gen10 d1 & gen10 ppl & c$\to$d1 lead & c$\to$ppl lead \\
350	\midrule
351	Replace     & 0.198$\pm$0.014 & 189.3$\pm$12.6 & 2.0 gen & 1.3 gen \\
352	Accumulate  & 0.267$\pm$0.016 & 124.8$\pm$9.3  & 2.5 gen & 1.8 gen \\
353	\bottomrule
354	\end{tabular}
355	\end{table}
356	
357	Accumulate reduces gen-10 perplexity by 34.2\% and improves diversity (distinct-1: 0.267 vs.\ 0.198), confirming theoretical predictions that retaining historical data bounds distributional drift. A novel finding: accumulate also extends canary lead times (diversity lead: 2.5 vs.\ 2.0~gen; perplexity lead: 1.8 vs.\ 1.3~gen). More gradual collapse gives the metric sensitivity gap additional generations to manifest, widening the early-warning window.
358	
359	%----------------------------------------------------------------------
360	\section{Discussion}
361	%----------------------------------------------------------------------
362	
363	\paragraph{The predictability phase diagram.}
364	Our results unify three observations into a single framework parameterized by the contamination ratio~$\alpha$. At low~$\alpha$, real data anchors the distribution, collapse is gradual, and both diversity and perplexity are predictable from canary metrics. As $\alpha$ increases, drift rate rises, compressing the temporal gap between metric onsets. At $\alpha^* \approx 0.60$, the perplexity channel crosses from predictable to unpredictable. The diversity channel remains predictable across all tested regimes because diversity metrics (distinct-$n$) require vocabulary contraction that inherently lags the calibration and token-distribution shifts captured by ECE and entropy.
365	
366	\paragraph{Why some canaries fail.}
367	Effective rank operates on representation-space singular values, which can remain stable even as the output distribution narrows (the model maps diverse inputs to similar outputs without losing representational rank). Self-BLEU measures pairwise similarity at the sequence level, which is noisy with small sample sizes and confounded by sequence length.
368	
369	\paragraph{Practical implications.}
370	In realistic deployment scenarios ($\alpha \ll 1$, data accumulation), canary lead times of 2--3 generations provide actionable early warning. The CRS proof-of-concept shows that even a simple trigger-based intervention can recover most of the diversity loss. More sophisticated adaptive $\alpha$-scheduling strategies could further improve outcomes.
371	
372	\paragraph{Limitations.}
373	Scale validation reaches only 1.4B parameters; whether lead times continue to increase at 7B+ is unknown.
374	All experiments use autoregressive language models; applicability to diffusion models or other generative architectures is untested.
375	The phase boundary $\alpha^* \approx 0.60$ is estimated from four $\alpha$ values and should be refined with finer sweeps.
376	TY testing on 10-generation series has limited statistical power; longer training horizons would strengthen conclusions.
377	
378	%----------------------------------------------------------------------
379	\section{Conclusion}
380	%----------------------------------------------------------------------
381	
382	We have presented a predictability phase diagram for model collapse in iterative synthetic data training. ECE and token entropy serve as reliable canary metrics that lead diversity degradation by 1--3 generations across all tested contamination regimes, model scales, and data domains. A phase boundary at $\alpha^* \approx 0.60$ separates regimes where canaries also predict perplexity degradation from those where synchronous collapse precludes early warning. Our methodological contribution---demonstrating that naive correlation yields ${\sim}41\%$ spurious associations on these non-stationary trajectories---underscores the necessity of formal temporal precedence testing. A canary-triggered intervention recovers 77\% of diversity loss, translating predictive power into actionable mitigation.
383	
384	\bibliographystyle{plainnat}
385	
386	\appendix
387	
388	\section{Supplementary Tables}
389	
390	Tables~\ref{tab:mvp_maxlag} and~\ref{tab:extended} appear in the main text as they address specific robustness checks. Additional per-seed breakdowns and distinct-3 results are available in the supplementary material.
391	
392	\end{document}
393	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e48f157e-2883-420d-b8cd-5de28469ed46",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "eb429785-6627-4b72-b445-ef163d03c545",
  "sourceToolAssistantUUID": "e48f157e-2883-420d-b8cd-5de28469ed46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-14T19:28:10.828Z_

Now let me read the actual experiment code and the other paper versions for comparison.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb429785-6627-4b72-b445-ef163d03c545",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31iPyWdFGv568ZAn1VR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f304ee7-c8f5-40f3-b8b8-720a9c9cd935",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dvDhCJKpeVPmAZKnib5Dq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10154,
      "cache_read_input_tokens": 27452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10154,
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

_source line 28 · 2026-05-14T19:28:12.692Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FWrVDpjEnL1FRKojDT2LC8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_mvp.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f304ee7-c8f5-40f3-b8b8-720a9c9cd935",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31iPyWdFGv568ZAn1VR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe67bfc3-cc46-49ec-9ec8-053b0129da00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dvDhCJKpeVPmAZKnib5Dq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10154,
      "cache_read_input_tokens": 27452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10154,
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

_source line 29 · 2026-05-14T19:28:12.700Z_

<details><summary>↩ Tool result · `toolu_01FWrVDpjEnL1FRKojDT2LC8`</summary>

```text
1	"""Analyze MVP experiment: metric trends, cross-correlation, lead time.
2	
3	Reads all_metrics.json from each rep, produces:
4	  - metric_trends.png : canary + downstream metrics vs generation
5	  - cross_correlation.png : cross-correlation heatmap
6	  - lead_time_table.csv : lead time estimates per canary-downstream pair
7	  - analysis_summary.json : machine-readable summary with graded verdict
8	
9	Evaluation pipeline (per mvp_evaluation_criteria.md):
10	  1. MAUVE floor effect detection (§4) — demote if Gen 0 < 0.10 and CV < 0.50
11	  2. effective_rank monotonicity check (§3) — Gen 4-9 OLS slope consistency
12	  3. Permutation test (§1) — per-triplet significance via 10k permutations
13	  4. Per-seed significance filtering (§2) — 3/3 consistency requirement
14	  5. Graded verdict (§5) — STRONG PASS / PASS / CONDITIONAL PASS / FAIL
15	  6. Lag dispersion statistics — mean, std, min, max per consistent pair
16	
17	Usage:
18	    python analyze_mvp.py --results_dir results/mvp --seeds 42 43 44
19	    python analyze_mvp.py --results_dir results/mvp --n_permutations 5000
20	"""
21	
22	import argparse
23	import json
24	import os
25	import sys
26	
27	import matplotlib.pyplot as plt
28	import numpy as np
29	import pandas as pd
30	
31	
32	CANARY_METRICS = ["token_entropy", "self_bleu", "ece", "effective_rank"]
33	DOWNSTREAM_METRICS = ["perplexity", "distinct_1", "distinct_2", "distinct_3", "mauve"]
34	
35	HIGHER_IS_WORSE = {"self_bleu", "ece", "perplexity"}
36	LOWER_IS_WORSE = {"token_entropy", "effective_rank", "distinct_1", "distinct_2",
37	                   "distinct_3", "mauve"}
38	
39	
40	def load_metrics(results_dir, seeds):
41	    """Load all_metrics.json from each rep, return dict {seed: [metrics_per_gen]}."""
42	    data = {}
43	    for seed in seeds:
44	        path = os.path.join(results_dir, f"rep_{seed}", "all_metrics.json")
45	        with open(path) as f:
46	            data[seed] = json.load(f)
47	    return data
48	
49	
50	def metrics_to_df(data):
51	    """Convert {seed: [metrics_per_gen]} to a long-form DataFrame."""
52	    rows = []
53	    for seed, gens in data.items():
54	        for m in gens:
55	            m_copy = dict(m)
56	            m_copy["seed"] = seed
57	            rows.append(m_copy)
58	    return pd.DataFrame(rows)
59	
60	
61	def normalize_for_correlation(series, metric_name):
62	    """Flip sign so that 'getting worse' is always positive direction."""
63	    s = series.copy()
64	    if metric_name in LOWER_IS_WORSE:
65	        s = -s
66	    s = (s - s.mean()) / (s.std() + 1e-12)
67	    return s
68	
69	
70	def cross_correlate(x, y, max_lag=5):
71	    """Cross-correlation of x and y at lags -max_lag..+max_lag.
72	
73	    Positive lag k means y leads x by k steps.
74	    Negative lag k means x leads y by |k| steps.
75	    """
76	    x = (x - x.mean()) / (x.std() + 1e-12)
77	    y = (y - y.mean()) / (y.std() + 1e-12)
78	    n = len(x)
79	    correlations = {}
80	    for lag in range(-max_lag, max_lag + 1):
81	        if lag >= 0:
82	            c = np.corrcoef(x[lag:], y[:n - lag])[0, 1] if n - lag > 1 else 0
83	        else:
84	            c = np.corrcoef(x[:n + lag], y[-lag:])[0, 1] if n + lag > 1 else 0
85	        correlations[lag] = c
86	    return correlations
87	
88	
89	def estimate_lead_time(canary_series, downstream_series, canary_name,
90	                       downstream_name, max_lag=5):
91	    """Estimate how many generations canary leads downstream.
92	
93	    Returns (peak_lag, peak_corr, corrs). Negative peak_lag = canary leads.
94	    """
95	    c_norm = normalize_for_correlation(canary_series, canary_name)
96	    d_norm = normalize_for_correlation(downstream_series, downstream_name)
97	    corrs = cross_correlate(c_norm, d_norm, max_lag=max_lag)
98	    peak_lag = max(corrs, key=lambda k: abs(corrs[k]))
99	    return peak_lag, corrs[peak_lag], corrs
100	
101	
102	def permutation_test(canary_series, downstream_series, canary_name,
103	                     downstream_name, max_lag=5, n_permutations=10000, seed=0):
104	    """Permutation test for cross-correlation significance.
105	
106	    Shuffles the downstream series to break temporal structure, recomputes
107	    max |r| across all lags for each permutation. p-value is the fraction
108	    of permutation max|r| >= observed peak|r|.
109	
110	    Returns (peak_lag, peak_corr, p_value).
111	    """
112	    c_norm = normalize_for_correlation(canary_series, canary_name)
113	    d_norm = normalize_for_correlation(downstream_series, downstream_name)
114	
115	    corrs = cross_correlate(c_norm, d_norm, max_lag=max_lag)
116	    peak_lag = max(corrs, key=lambda k: abs(corrs[k]))
117	    observed_peak_r = abs(corrs[peak_lag])
118	
119	    rng = np.random.RandomState(seed)
120	    count_ge = 0
121	    for _ in range(n_permutations):
122	        d_perm = rng.permutation(d_norm)
123	        perm_corrs = cross_correlate(c_norm, d_perm, max_lag=max_lag)
124	        perm_max_r = max(abs(v) for v in perm_corrs.values())
125	        if perm_max_r >= observed_peak_r:
126	            count_ge += 1
127	
128	    p_value = count_ge / n_permutations
129	    return peak_lag, corrs[peak_lag], p_value
130	
131	
132	def check_mauve_floor(df, seeds):
133	    """Check MAUVE floor effect: Gen 0 < 0.10 and CV < 0.50 across all seeds.
134	
135	    Returns (demoted: bool, reason: str or None).
136	    """
137	    for seed in seeds:
138	        seed_df = df[df["seed"] == seed].sort_values("generation")
139	        gen0_mauve = seed_df[seed_df["generation"] == 0]["mauve"].values
140	        if len(gen0_mauve) == 0:
141	            return False, None
142	        if gen0_mauve[0] >= 0.10:
143	            return False, None
144	        mauve_vals = seed_df["mauve"].values
145	        mean_m = np.mean(mauve_vals)
146	        std_m = np.std(mauve_vals)
147	        cv = std_m / (mean_m + 1e-12)
148	        if cv >= 0.50:
149	            return False, None
150	    return True, "floor_effect"
151	
152	
153	def check_effective_rank_monotonicity(df, seeds):
154	    """Check effective_rank Gen 4-9 slope consistency across seeds.
155	
156	    Returns (status: str, slopes: dict).
157	    status is one of: "decreasing", "increasing", "inconclusive".
158	    """
159	    slopes = {}
160	    for seed in seeds:
161	        seed_df = df[df["seed"] == seed].sort_values("generation")
162	        late = seed_df[seed_df["generation"] >= 4]
163	        if len(late) < 2:
164	            return "inconclusive", {}
165	        gens = late["generation"].values.astype(float)
166	        vals = late["effective_rank"].values.astype(float)
167	        coeffs = np.polyfit(gens, vals, 1)
168	        slopes[str(seed)] = float(coeffs[0])
169	
170	    slope_vals = list(slopes.values())
171	    if all(s < 0 for s in slope_vals):
172	        return "decreasing", slopes
173	    if all(s > 0 for s in slope_vals):
174	        return "increasing", slopes
175	    return "inconclusive", slopes
176	
177	
178	def classify_pair(per_seed_results):
179	    """Classify a (canary, downstream) pair based on per-seed results.
180	
181	    Returns one of: "SIGNIFICANT LEAD", "WEAK LEAD", "NO LEAD".
182	    """
183	    if not all(r["peak_lag"] < 0 for r in per_seed_results):
184	        return "NO LEAD"
185	    if all(r["p_value"] < 0.10 and abs(r["peak_corr"]) >= 0.60
186	           for r in per_seed_results):
187	        return "SIGNIFICANT LEAD"
188	    return "WEAK LEAD"
189	
190	
191	def check_near_miss(per_seed_results):
192	    """Check if a NO LEAD pair is a near miss (2/3 seeds lead, 1 at lag=0)."""
193	    lags = [r["peak_lag"] for r in per_seed_results]
194	    neg_seeds = [r for r in per_seed_results if r["peak_lag"] < 0]
195	    zero_seeds = [r for r in per_seed_results if r["peak_lag"] == 0]
196	    if len(neg_seeds) == 2 and len(zero_seeds) == 1:
197	        if all(r["peak_lag"] <= -2 and r["p_value"] < 0.05 for r in neg_seeds):
198	            return True
199	    return False
200	
201	
202	def compute_lag_dispersion(per_seed_results):
203	    """Compute lag dispersion statistics for a consistent pair."""
204	    lags = [r["peak_lag"] for r in per_seed_results]
205	    lag_std = float(np.std(lags))
206	    return {
207	        "mean_lag": float(np.mean(lags)),
208	        "lag_std": lag_std,
209	        "min_lag": int(min(lags)),
210	        "max_lag": int(max(lags)),
211	        "high_dispersion": lag_std > 2.0,
212	    }
213	
214	
215	def compute_verdict(per_pair_results, effective_rank_status):
216	    """Compute graded verdict from per-pair results.
217	
218	    Returns (verdict, reasoning, significant_pairs, weak_pairs).
219	    """
220	    significant_pairs = []
221	    weak_pairs = []
222	
223	    for pr in per_pair_results:
224	        if pr["canary"] == "effective_rank" and effective_rank_status == "inconclusive":
225	            continue
226	        if pr["pair_verdict"] == "SIGNIFICANT LEAD":
227	            significant_pairs.append(pr)
228	        elif pr["pair_verdict"] == "WEAK LEAD":
229	            weak_pairs.append(pr)
230	
231	    sig_families = set(p["canary"] for p in significant_pairs)
232	    weak_families = set(p["canary"] for p in weak_pairs)
233	
234	    if len(sig_families) >= 2:
235	        verdict = "STRONG PASS"
236	        reasoning = (f"{len(sig_families)} canary families ({', '.join(sorted(sig_families))}) "
237	                     f"each have >= 1 SIGNIFICANT LEAD pair.")
238	    elif len(sig_families) >= 1:
239	        verdict = "PASS"
240	        reasoning = (f"{len(sig_families)} canary family ({', '.join(sorted(sig_families))}) "
241	                     f"has >= 1 SIGNIFICANT LEAD pair.")
242	    elif len(weak_families) >= 1:
243	        verdict = "CONDITIONAL PASS"
244	        reasoning = (f"No SIGNIFICANT LEAD pairs, but {len(weak_families)} canary "
245	                     f"family ({', '.join(sorted(weak_families))}) has >= 1 WEAK LEAD pair.")
246	    else:
247	        verdict = "FAIL"
248	        reasoning = "No canary family achieves even WEAK LEAD consistency across seeds."
249	
250	    return verdict, reasoning, significant_pairs, weak_pairs
251	
252	
253	def plot_metric_trends(df, output_dir):
254	    """Plot metric-vs-generation with mean +/- std across seeds."""
255	    all_metrics = CANARY_METRICS + DOWNSTREAM_METRICS
256	    fig, axes = plt.subplots(3, 3, figsize=(15, 12))
257	    axes = axes.flatten()
258	
259	    for idx, metric in enumerate(all_metrics):
260	        if idx >= len(axes):
261	            break
262	        ax = axes[idx]
263	        grouped = df.groupby("generation")[metric]
264	        mean = grouped.mean()
265	        std = grouped.std()
266	
267	        ax.plot(mean.index, mean.values, "o-", linewidth=2)
268	        ax.fill_between(mean.index, mean.values - std.values,
269	                        mean.values + std.values, alpha=0.2)
270	        ax.set_title(metric, fontsize=11, fontweight="bold")
271	        ax.set_xlabel("Generation")
272	        ax.set_ylabel(metric)
273	        ax.grid(True, alpha=0.3)
274	
275	        is_canary = metric in CANARY_METRICS
276	        ax.set_facecolor("#fff8f0" if is_canary else "#f0f8ff")
277	
278	    for idx in range(len(all_metrics), len(axes)):
279	        axes[idx].set_visible(False)
280	
281	    fig.suptitle("Metric Trends over Generations (mean ± std, 3 reps)",
282	                 fontsize=14, fontweight="bold")
283	    plt.tight_layout()
284	    plt.savefig(os.path.join(output_dir, "metric_trends.png"), dpi=150,
285	                bbox_inches="tight")
286	    plt.close()
287	    print("Saved metric_trends.png")
288	
289	
290	def plot_cross_correlation_heatmap(lead_table, output_dir):
291	    """Heatmap of peak lag (canary leads = negative lag)."""
292	    pivot_lag = lead_table.pivot(index="canary", columns="downstream",
293	                                values="peak_lag")
294	    pivot_corr = lead_table.pivot(index="canary", columns="downstream",
295	                                  values="peak_corr")
296	
297	    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
298	
299	    im1 = ax1.imshow(pivot_lag.values, cmap="RdBu_r", aspect="auto",
300	                     vmin=-5, vmax=5)
301	    ax1.set_xticks(range(len(pivot_lag.columns)))
302	    ax1.set_xticklabels(pivot_lag.columns, rotation=45, ha="right")
303	    ax1.set_yticks(range(len(pivot_lag.index)))
304	    ax1.set_yticklabels(pivot_lag.index)
305	    ax1.set_title("Peak Lag (negative = canary leads)")
306	    for i in range(len(pivot_lag.index)):
307	        for j in range(len(pivot_lag.columns)):
308	            ax1.text(j, i, f"{pivot_lag.values[i, j]:.0f}",
309	                     ha="center", va="center", fontsize=10)
310	    plt.colorbar(im1, ax=ax1)
311	
312	    im2 = ax2.imshow(np.abs(pivot_corr.values), cmap="YlOrRd", aspect="auto",
313	                     vmin=0, vmax=1)
314	    ax2.set_xticks(range(len(pivot_corr.columns)))
315	    ax2.set_xticklabels(pivot_corr.columns, rotation=45, ha="right")
316	    ax2.set_yticks(range(len(pivot_corr.index)))
317	    ax2.set_yticklabels(pivot_corr.index)
318	    ax2.set_title("|Peak Correlation|")
319	    for i in range(len(pivot_corr.index)):
320	        for j in range(len(pivot_corr.columns)):
321	            ax2.text(j, i, f"{pivot_corr.values[i, j]:.2f}",
322	                     ha="center", va="center", fontsize=10)
323	    plt.colorbar(im2, ax=ax2)
324	
325	    fig.suptitle("Cross-Correlation: Canary → Downstream", fontsize=13,
326	                 fontweight="bold")
327	    plt.tight_layout()
328	    plt.savefig(os.path.join(output_dir, "cross_correlation.png"), dpi=150,
329	                bbox_inches="tight")
330	    plt.close()
331	    print("Saved cross_correlation.png")
332	
333	
334	def main():
335	    parser = argparse.ArgumentParser(
336	        description="Analyze MVP experiment with graded verdict system.")
337	    parser.add_argument("--results_dir", type=str, default="results/mvp")
338	    parser.add_argument("--seeds", type=int, nargs="+", default=[42, 43, 44])
339	    parser.add_argument("--max_lag", type=int, default=5)
340	    parser.add_argument("--n_permutations", type=int, default=10000,
341	                        help="Number of permutations for significance test (default: 10000)")
342	    args = parser.parse_args()
343	
344	    output_dir = os.path.join(args.results_dir, "analysis")
345	    os.makedirs(output_dir, exist_ok=True)
346	
347	    print("Loading metrics ...")
348	    data = load_metrics(args.results_dir, args.seeds)
349	    df = metrics_to_df(data)
350	
351	    # --- Metric trend plots ---
352	    plot_metric_trends(df, output_dir)
353	
354	    # --- §4: MAUVE floor effect detection ---
355	    mauve_demoted, mauve_reason = check_mauve_floor(df, args.seeds)
356	    active_downstream = list(DOWNSTREAM_METRICS)
357	    if mauve_demoted:
358	        print(f"MAUVE demoted to supplementary (reason: {mauve_reason})")
359	
360	    # --- §3: effective_rank monotonicity check ---
361	    er_status, er_slopes = check_effective_rank_monotonicity(df, args.seeds)
362	    print(f"effective_rank status: {er_status} (slopes: {er_slopes})")
363	
364	    # --- Cross-correlation with permutation tests ---
365	    total_triplets = len(CANARY_METRICS) * len(DOWNSTREAM_METRICS) * len(args.seeds)
366	    triplet_idx = 0
367	
368	    per_pair_results = []
369	    lead_rows = []
370	    near_misses = []
371	
372	    for canary in CANARY_METRICS:
373	        for downstream in DOWNSTREAM_METRICS:
374	            per_seed = []
375	            all_lags = []
376	            all_corrs = []
377	
378	            for seed in args.seeds:
379	                triplet_idx += 1
380	                print(f"\r  Permutation test {triplet_idx}/{total_triplets}: "
381	                      f"{canary} vs {downstream} (seed {seed})", end="",
382	                      flush=True)
383	
384	                seed_df = df[df["seed"] == seed].sort_values("generation")
385	                c_series = seed_df[canary].values
386	                d_series = seed_df[downstream].values
387	
388	                peak_lag, peak_corr, p_value = permutation_test(
389	                    c_series, d_series, canary, downstream,
390	                    max_lag=args.max_lag,
391	                    n_permutations=args.n_permutations,
392	                    seed=seed)
393	
394	                per_seed.append({
395	                    "seed": seed,
396	                    "peak_lag": int(peak_lag),
397	                    "peak_corr": round(float(peak_corr), 4),
398	                    "p_value": round(float(p_value), 4),
399	                })
400	                all_lags.append(peak_lag)
401	                all_corrs.append(peak_corr)
402	
403	            pair_verdict = classify_pair(per_seed)
404	
405	            pair_result = {
406	                "canary": canary,
407	                "downstream": downstream,
408	                "pair_verdict": pair_verdict,
409	                "per_seed": per_seed,
410	            }
411	
412	            if pair_verdict in ("SIGNIFICANT LEAD", "WEAK LEAD"):
413	                disp = compute_lag_dispersion(per_seed)
414	                pair_result.update(disp)
415	            else:
416	                if check_near_miss(per_seed):
417	                    near_misses.append({"canary": canary, "downstream": downstream,
418	                                        "per_seed": per_seed})
419	
420	            per_pair_results.append(pair_result)
421	
422	            lead_rows.append({
423	                "canary": canary,
424	                "downstream": downstream,
425	                "peak_lag": np.mean(all_lags),
426	                "peak_corr": np.mean(all_corrs),
427	                "lag_std": np.std(all_lags),
428	                "corr_std": np.std(all_corrs),
429	                "consistent": all(l < 0 for l in all_lags),
430	            })
431	
432	    print()
433	
434	    lead_table = pd.DataFrame(lead_rows)
435	    lead_table.to_csv(os.path.join(output_dir, "lead_time_table.csv"),
436	                      index=False)
437	    print("Saved lead_time_table.csv")
438	
439	    plot_cross_correlation_heatmap(lead_table, output_dir)
440	
441	    # --- §5: Graded verdict ---
442	    verdict_pairs = per_pair_results
443	    if mauve_demoted:
444	        verdict_pairs = [p for p in per_pair_results if p["downstream"] != "mauve"]
445	
446	    verdict, reasoning, sig_pairs, weak_pairs = compute_verdict(
447	        verdict_pairs, er_status)
448	
449	    # --- Build summary ---
450	    summary = {
451	        "mauve_demoted": mauve_demoted,
452	        "mauve_demoted_reason": mauve_reason,
453	        "effective_rank_status": er_status,
454	        "effective_rank_slopes": er_slopes,
455	        "per_pair_results": per_pair_results,
456	        "verdict": verdict,
457	        "verdict_reasoning": reasoning,
458	        "significant_lead_pairs": [
459	            {"canary": p["canary"], "downstream": p["downstream"]}
460	            for p in sig_pairs
461	        ],
462	        "weak_lead_pairs": [
463	            {"canary": p["canary"], "downstream": p["downstream"]}
464	            for p in weak_pairs
465	        ],
466	        "near_misses": near_misses,
467	    }
468	
469	    with open(os.path.join(output_dir, "analysis_summary.json"), "w") as f:
470	        json.dump(summary, f, indent=2)
471	
472	    # --- Console report ---
473	    print("\n" + "=" * 60)
474	    print("MVP ANALYSIS SUMMARY")
475	    print("=" * 60)
476	
477	    if mauve_demoted:
478	        print(f"MAUVE: demoted to supplementary ({mauve_reason})")
479	    else:
480	        print("MAUVE: retained as primary downstream metric")
481	
482	    print(f"effective_rank: {er_status}")
483	    if er_slopes:
484	        slope_str = ", ".join(f"seed {k}: {v:.4f}" for k, v in er_slopes.items())
485	        print(f"  slopes: {slope_str}")
486	
487	    n_sig = len(sig_pairs)
488	    n_weak = len(weak_pairs)
489	    n_total = len(verdict_pairs)
490	    print(f"\nPair results ({n_total} pairs evaluated for verdict):")
491	    print(f"  SIGNIFICANT LEAD: {n_sig}")
492	    print(f"  WEAK LEAD: {n_weak}")
493	    print(f"  NO LEAD: {n_total - n_sig - n_weak}")
494	
495	    if near_misses:
496	        print(f"  Near misses: {len(near_misses)}")
497	        for nm in near_misses:
498	            print(f"    {nm['canary']} -> {nm['downstream']}")
499	
500	    verdict_icon = {"STRONG PASS": "STRONG PASS", "PASS": "PASS",
501	                    "CONDITIONAL PASS": "CONDITIONAL PASS", "FAIL": "FAIL"}
502	    print(f"\nVerdict: {verdict_icon[verdict]}")
503	    print(f"Reasoning: {reasoning}")
504	
505	    if sig_pairs:
506	        print("\nSignificant lead pairs:")
507	        for p in sig_pairs:
508	            disp_flag = " [high_dispersion]" if p.get("high_dispersion") else ""
509	            print(f"  {p['canary']} -> {p['downstream']}: "
510	                  f"mean_lag={p['mean_lag']:.1f}, lag_std={p['lag_std']:.1f}{disp_flag}")
511	            for s in p["per_seed"]:
512	                print(f"    seed {s['seed']}: lag={s['peak_lag']}, "
513	                      f"|r|={abs(s['peak_corr']):.3f}, p={s['p_value']:.4f}")
514	
515	    if weak_pairs:
516	        print("\nWeak lead pairs:")
517	        for p in weak_pairs:
518	            disp_flag = " [high_dispersion]" if p.get("high_dispersion") else ""
519	            print(f"  {p['canary']} -> {p['downstream']}: "
520	                  f"mean_lag={p['mean_lag']:.1f}, lag_std={p['lag_std']:.1f}{disp_flag}")
521	            for s in p["per_seed"]:
522	                print(f"    seed {s['seed']}: lag={s['peak_lag']}, "
523	                      f"|r|={abs(s['peak_corr']):.3f}, p={s['p_value']:.4f}")
524	
525	    print("\nFull lead time table:")
526	    print(lead_table.to_string(index=False))
527	    print(f"\nResults saved to {output_dir}/")
528	
529	
530	if __name__ == "__main__":
531	    main()
532	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe67bfc3-cc46-49ec-9ec8-053b0129da00",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "5882b890-c4e0-4a49-ae16-88bd54dcff87",
  "sourceToolAssistantUUID": "fe67bfc3-cc46-49ec-9ec8-053b0129da00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T19:28:13.028Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EKpKC6XZLtGHRui9xFhZNR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/iterative_train.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5882b890-c4e0-4a49-ae16-88bd54dcff87",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31iPyWdFGv568ZAn1VR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5398b2c-4c56-44cb-b4d4-999a4359193c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dvDhCJKpeVPmAZKnib5Dq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10154,
      "cache_read_input_tokens": 27452,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10154
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 27452,
          "cache_creation_input_tokens": 10154,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10154,
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

_source line 31 · 2026-05-14T19:28:13.031Z_

<details><summary>↩ Tool result · `toolu_01EKpKC6XZLtGHRui9xFhZNR`</summary>

```text
1	"""Iterative self-consuming training pipeline for model collapse study.
2	
3	Each generation:
4	  1. Generate synthetic text from current model using held-out prompts
5	  2. Mix synthetic data with real data according to --synthetic_ratio
6	  3. Fine-tune the model on the mixed dataset
7	  4. Save checkpoint and compute all canary + downstream metrics
8	
9	Synthetic mixing modes:
10	  - Default: each generation uses only current-gen synthetic data + real data
11	  - --accumulate: pool all historical synthetic data (gen 1..N) + real data
12	
13	Usage:
14	    python iterative_train.py \
15	        --model_name EleutherAI/pythia-410m \
16	        --data_dir data/wikitext103 \
17	        --output_dir results/mvp/rep_42 \
18	        --num_generations 10 \
19	        --steps_per_gen 10000 \
20	        --synthetic_ratio 0.75 \
21	        --accumulate \
22	        --seed 42
23	"""
24	
25	import argparse
26	import json
27	import os
28	import random
29	
30	import numpy as np
31	import torch
32	from datasets import Dataset, concatenate_datasets, load_from_disk
33	from torch.utils.data import DataLoader
34	from transformers import (
35	    AutoModelForCausalLM,
36	    AutoTokenizer,
37	    DataCollatorForLanguageModeling,
38	    Trainer,
39	    TrainingArguments,
40	    set_seed,
41	)
42	
43	from metrics import compute_all_metrics
44	
45	
46	def parse_args():
47	    p = argparse.ArgumentParser()
48	    p.add_argument("--model_name", type=str, default="EleutherAI/pythia-410m")
49	    p.add_argument("--data_dir", type=str, default="data/wikitext103",
50	                   help="Output of prepare_data.py")
51	    p.add_argument("--dataset", type=str, default="wikitext-103-v1",
52	                   help="Dataset identifier (for logging only; actual data from data_dir)")
53	    p.add_argument("--synthetic_ratio", type=float, default=1.0,
54	                   help="Fraction of training data that is synthetic (0-1)")
55	    p.add_argument("--num_generations", type=int, default=10)
56	    p.add_argument("--steps_per_gen", type=int, default=5000)
57	    p.add_argument("--output_dir", type=str, default="results/mvp/rep_42")
58	    p.add_argument("--seed", type=int, default=42)
59	    p.add_argument("--batch_size", type=int, default=4)
60	    p.add_argument("--max_length", type=int, default=512)
61	    p.add_argument("--lr", type=float, default=5e-5)
62	    p.add_argument("--gen_max_new_tokens", type=int, default=256,
63	                   help="Max new tokens per generation sample")
64	    p.add_argument("--gen_batch_size", type=int, default=16)
65	    p.add_argument("--top_p", type=float, default=0.95,
66	                   help="Nucleus sampling p for synthetic generation")
67	    p.add_argument("--accumulate", action="store_true",
68	                   help="Pool all historical synthetic data instead of only the latest generation")
69	    return p.parse_args()
70	
71	
72	def generate_synthetic_data(model, tokenizer, prompts_dataset, args):
73	    """Generate synthetic text from `model` using held-out prompts."""
74	    model.eval()
75	    device = next(model.parameters()).device
76	    generated_texts = []
77	
78	    prompt_texts = prompts_dataset["text"]
79	    for i in range(0, len(prompt_texts), args.gen_batch_size):
80	        batch_prompts = prompt_texts[i:i + args.gen_batch_size]
81	        enc = tokenizer(batch_prompts, return_tensors="pt", truncation=True,
82	                        max_length=args.max_length // 2, padding=True)
83	        input_ids = enc["input_ids"].to(device)
84	        attention_mask = enc["attention_mask"].to(device)
85	
86	        with torch.no_grad():
87	            outputs = model.generate(
88	                input_ids=input_ids,
89	                attention_mask=attention_mask,
90	                max_new_tokens=args.gen_max_new_tokens,
91	                do_sample=True,
92	                top_p=args.top_p,
93	                temperature=1.0,
94	                pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
95	            )
96	        for seq in outputs:
97	            text = tokenizer.decode(seq, skip_special_tokens=True)
98	            generated_texts.append(text)
99	
100	    return Dataset.from_dict({"text": generated_texts})
101	
102	
103	def mix_datasets(real_dataset, synthetic_dataset, synthetic_ratio, seed):
104	    """Mix real and synthetic data according to synthetic_ratio.
105	
106	    Bidirectional subsampling to hit the target ratio:
107	    - Low α (enough synthetic): keep all real, subsample synthetic
108	    - High α (synthetic scarce): keep all synthetic, subsample real
109	    """
110	    if synthetic_ratio >= 1.0:
111	        return synthetic_dataset
112	    if synthetic_ratio <= 0.0:
113	        return real_dataset
114	
115	    needed_syn = int(len(real_dataset) * synthetic_ratio / (1 - synthetic_ratio))
116	    if needed_syn <= len(synthetic_dataset):
117	        syn_subset = synthetic_dataset.shuffle(seed=seed).select(range(needed_syn))
118	        real_subset = real_dataset
119	    else:
120	        needed_real = int(len(synthetic_dataset) * (1 - synthetic_ratio) / synthetic_ratio)
121	        needed_real = min(needed_real, len(real_dataset))
122	        real_subset = real_dataset.shuffle(seed=seed).select(range(needed_real))
123	        syn_subset = synthetic_dataset
124	
125	    actual_ratio = len(syn_subset) / (len(syn_subset) + len(real_subset))
126	    print(f"  Mix: {len(syn_subset)} syn + {len(real_subset)} real = {actual_ratio:.4f}")
127	    return concatenate_datasets([real_subset, syn_subset]).shuffle(seed=seed)
128	
129	
130	def tokenize_dataset(dataset, tokenizer, max_length):
131	    """Tokenize and chunk text for causal LM training."""
132	    def tokenize_fn(examples):
133	        return tokenizer(examples["text"], truncation=True,
134	                         max_length=max_length, padding="max_length")
135	
136	    tokenized = dataset.map(tokenize_fn, batched=True,
137	                            remove_columns=["text"],
138	                            num_proc=1)
139	    tokenized.set_format("torch")
140	    return tokenized
141	
142	
143	def train_one_generation(model, tokenizer, train_dataset, args, gen_idx):
144	    """Fine-tune model for one generation."""
145	    tokenized = tokenize_dataset(train_dataset, tokenizer, args.max_length)
146	
147	    training_args = TrainingArguments(
148	        output_dir=os.path.join(args.output_dir, f"gen_{gen_idx}", "trainer"),
149	        max_steps=args.steps_per_gen,
150	        per_device_train_batch_size=args.batch_size,
151	        learning_rate=args.lr,
152	        warmup_steps=min(500, args.steps_per_gen // 10),
153	        weight_decay=0.01,
154	        logging_steps=100,
155	        save_strategy="no",
156	        seed=args.seed + gen_idx,
157	        fp16=torch.cuda.is_available(),
158	        dataloader_drop_last=True,
159	        report_to="none",
160	    )
161	
162	    collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
163	    trainer = Trainer(
164	        model=model,
165	        args=training_args,
166	        train_dataset=tokenized,
167	        data_collator=collator,
168	    )
169	    trainer.train()
170	    return model
171	
172	
173	def main():
174	    args = parse_args()
175	    set_seed(args.seed)
176	    os.makedirs(args.output_dir, exist_ok=True)
177	
178	    with open(os.path.join(args.output_dir, "config.json"), "w") as f:
179	        json.dump(vars(args), f, indent=2)
180	
181	    print(f"Loading model: {args.model_name}")
182	    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
183	    if tokenizer.pad_token is None:
184	        tokenizer.pad_token = tokenizer.eos_token
185	
186	    model = AutoModelForCausalLM.from_pretrained(args.model_name)
187	    if torch.cuda.is_available():
188	        model = model.cuda()
189	
190	    print(f"Loading data from {args.data_dir}")
191	    train_dataset = load_from_disk(os.path.join(args.data_dir, "train"))
192	    eval_dataset = load_from_disk(os.path.join(args.data_dir, "eval"))
193	    prompts_dataset = load_from_disk(os.path.join(args.data_dir, "prompts"))
194	
195	    all_metrics = []
196	    synthetic_pool = []  # for --accumulate mode
197	
198	    # --- Generation 0: baseline metrics (no training yet) ---
199	    print("=" * 60)
200	    print("Generation 0 (baseline)")
201	    print("=" * 60)
202	
203	    gen0_synthetic = generate_synthetic_data(model, tokenizer, prompts_dataset, args)
204	    gen0_dir = os.path.join(args.output_dir, "gen_0")
205	    os.makedirs(gen0_dir, exist_ok=True)
206	    gen0_synthetic.save_to_disk(os.path.join(gen0_dir, "synthetic_data"))
207	
208	    metrics = compute_all_metrics(model, tokenizer, eval_dataset, gen0_synthetic)
209	    metrics["generation"] = 0
210	    all_metrics.append(metrics)
211	
212	    with open(os.path.join(gen0_dir, "metrics.json"), "w") as f:
213	        json.dump(metrics, f, indent=2)
214	    print(f"Gen 0 metrics: ppl={metrics['perplexity']:.2f}, "
215	          f"entropy={metrics['token_entropy']:.4f}, "
216	          f"eff_rank={metrics['effective_rank']:.1f}")
217	
218	    # --- Generations 1..N ---
219	    for gen in range(1, args.num_generations + 1):
220	        print("=" * 60)
221	        print(f"Generation {gen}/{args.num_generations}")
222	        print("=" * 60)
223	
224	        gen_dir = os.path.join(args.output_dir, f"gen_{gen}")
225	        os.makedirs(gen_dir, exist_ok=True)
226	
227	        # Step 1: generate synthetic data with current model
228	        print("  Generating synthetic data …")
229	        synthetic_data = generate_synthetic_data(
230	            model, tokenizer, prompts_dataset, args)
231	        synthetic_data.save_to_disk(os.path.join(gen_dir, "synthetic_data"))
232	
233	        # Step 2: mix real + synthetic
234	        if args.accumulate:
235	            synthetic_pool.append(synthetic_data)
236	            effective_synthetic = concatenate_datasets(synthetic_pool)
237	        else:
238	            effective_synthetic = synthetic_data
239	        mixed = mix_datasets(train_dataset, effective_synthetic,
240	                             args.synthetic_ratio, args.seed + gen)
241	        print(f"  Mixed dataset: {len(mixed)} samples "
242	              f"(synthetic={len(effective_synthetic)}, "
243	              f"synthetic_ratio={args.synthetic_ratio}, "
244	              f"accumulate={args.accumulate})")
245	
246	        # Step 3: fine-tune
247	        print("  Training …")
248	        model = train_one_generation(model, tokenizer, mixed, args, gen)
249	
250	        # Step 4: save checkpoint
251	        ckpt_path = os.path.join(gen_dir, "checkpoint")
252	        model.save_pretrained(ckpt_path)
253	        tokenizer.save_pretrained(ckpt_path)
254	        print(f"  Checkpoint saved: {ckpt_path}")
255	
256	        # Step 5: compute metrics
257	        print("  Computing metrics …")
258	        metrics = compute_all_metrics(model, tokenizer, eval_dataset,
259	                                      synthetic_data)
260	        metrics["generation"] = gen
261	        all_metrics.append(metrics)
262	
263	        with open(os.path.join(gen_dir, "metrics.json"), "w") as f:
264	            json.dump(metrics, f, indent=2)
265	        print(f"  ppl={metrics['perplexity']:.2f}, "
266	              f"entropy={metrics['token_entropy']:.4f}, "
267	              f"eff_rank={metrics['effective_rank']:.1f}, "
268	              f"mauve={metrics['mauve']:.4f}")
269	
270	    # Save consolidated metrics
271	    metrics_path = os.path.join(args.output_dir, "all_metrics.json")
272	    with open(metrics_path, "w") as f:
273	        json.dump(all_metrics, f, indent=2)
274	    print(f"\nAll metrics saved to {metrics_path}")
275	
276	    sentinel_path = os.path.join(args.output_dir, "EXIT_CODE")
277	    with open(sentinel_path, "w") as f:
278	        f.write("0\n")
279	    print(f"Sentinel written: {sentinel_path}")
280	
281	
282	if __name__ == "__main__":
283	    try:
284	        main()
285	    except Exception as e:
286	        try:
287	            _args = parse_args()
288	            os.makedirs(_args.output_dir, exist_ok=True)
289	            with open(os.path.join(_args.output_dir, "EXIT_CODE"), "w") as f:
290	                f.write(f"1\n{e}\n")
291	        except Exception:
292	            pass
293	        raise
294	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5398b2c-4c56-44cb-b4d4-999a4359193c",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "bb5041e0-c02e-4eda-8771-3e68fff0cdd5",
  "sourceToolAssistantUUID": "a5398b2c-4c56-44cb-b4d4-999a4359193c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T19:28:17.776Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BNFpLuzDLsDFVkXAEenoDJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/metrics.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb5041e0-c02e-4eda-8771-3e68fff0cdd5",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31ioWcAUdHgvK6q4oD7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4a8bf0c-2307-4cb3-a30d-ca9fa86b1334",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013aTSMhdLFidxQGeT5Gmz2q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12075,
      "cache_read_input_tokens": 37606,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12075
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 37606,
          "cache_creation_input_tokens": 12075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12075,
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

_source line 33 · 2026-05-14T19:28:17.787Z_

<details><summary>↩ Tool result · `toolu_01BNFpLuzDLsDFVkXAEenoDJ`</summary>

```text
1	"""Canary and downstream metrics for model collapse detection.
2	
3	Computes per-generation metrics on held-out data and generated samples.
4	All compute_* functions share the signature:
5	    (model, tokenizer, eval_dataset, gen_dataset=None, **kwargs) -> float | dict
6	
7	Dependencies: torch, transformers, mauve-text, nltk
8	"""
9	
10	import math
11	from collections import Counter
12	from itertools import combinations
13	
14	import numpy as np
15	import torch
16	from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu
17	
18	
19	# ---------------------------------------------------------------------------
20	# Text-surface metrics
21	# ---------------------------------------------------------------------------
22	
23	def compute_token_entropy(model, tokenizer, eval_dataset, gen_dataset=None,
24	                          max_samples=512, max_length=256, batch_size=8):
25	    """Mean next-token entropy of `model` on `eval_dataset` (held-out real text).
26	
27	    Lower entropy over generations signals the model is becoming overly
28	    confident / less diverse — a collapse canary.
29	    """
30	    model.eval()
31	    device = next(model.parameters()).device
32	    total_entropy = 0.0
33	    total_tokens = 0
34	
35	    texts = eval_dataset["text"][:max_samples]
36	    for i in range(0, len(texts), batch_size):
37	        batch_texts = texts[i:i + batch_size]
38	        enc = tokenizer(batch_texts, return_tensors="pt", truncation=True,
39	                        max_length=max_length, padding=True)
40	        input_ids = enc["input_ids"].to(device)
41	        attention_mask = enc["attention_mask"].to(device)
42	
43	        with torch.no_grad():
44	            logits = model(input_ids=input_ids, attention_mask=attention_mask).logits
45	
46	        # shift: predict token t+1 from position t
47	        shift_logits = logits[:, :-1, :]
48	        shift_mask = attention_mask[:, 1:]
49	
50	        log_probs = torch.log_softmax(shift_logits, dim=-1)
51	        probs = torch.exp(log_probs)
52	        token_entropy = -(probs * log_probs).sum(dim=-1)  # (B, T-1)
53	
54	        masked_entropy = (token_entropy * shift_mask).sum()
55	        total_entropy += masked_entropy.item()
56	        total_tokens += shift_mask.sum().item()
57	
58	    return total_entropy / max(total_tokens, 1)
59	
60	
61	def compute_self_bleu(model, tokenizer, eval_dataset, gen_dataset=None,
62	                      max_samples=200, sample_pairs=500):
63	    """Self-BLEU among generated samples — higher means less diversity.
64	
65	    Uses `gen_dataset["text"]`. Falls back to `eval_dataset` if gen_dataset
66	    is None (useful for baseline measurement on real data).
67	    """
68	    src = gen_dataset if gen_dataset is not None else eval_dataset
69	    texts = src["text"][:max_samples]
70	    tokenized = [tokenizer.tokenize(t)[:128] for t in texts if len(t.strip()) > 0]
71	
72	    if len(tokenized) < 2:
73	        return 0.0
74	
75	    smoother = SmoothingFunction().method1
76	    n_pairs = min(sample_pairs, len(tokenized) * (len(tokenized) - 1) // 2)
77	
78	    rng = np.random.RandomState(0)
79	    indices = list(range(len(tokenized)))
80	    scores = []
81	    for _ in range(n_pairs):
82	        i, j = rng.choice(indices, size=2, replace=False)
83	        score = sentence_bleu([tokenized[i]], tokenized[j],
84	                              weights=(0.25, 0.25, 0.25, 0.25),
85	                              smoothing_function=smoother)
86	        scores.append(score)
87	
88	    return float(np.mean(scores))
89	
90	
91	def compute_distinct_n(model, tokenizer, eval_dataset, gen_dataset=None,
92	                       max_samples=500, ns=(1, 2, 3)):
93	    """Distinct-n: ratio of unique n-grams to total n-grams in generated text.
94	
95	    Returns dict {"distinct_1": ..., "distinct_2": ..., "distinct_3": ...}.
96	    """
97	    src = gen_dataset if gen_dataset is not None else eval_dataset
98	    texts = src["text"][:max_samples]
99	    all_tokens = []
100	    for t in texts:
101	        all_tokens.extend(tokenizer.tokenize(t)[:256])
102	
103	    result = {}
104	    for n in ns:
105	        ngrams = [tuple(all_tokens[i:i + n]) for i in range(len(all_tokens) - n + 1)]
106	        if len(ngrams) == 0:
107	            result[f"distinct_{n}"] = 0.0
108	        else:
109	            result[f"distinct_{n}"] = len(set(ngrams)) / len(ngrams)
110	    return result
111	
112	
113	# ---------------------------------------------------------------------------
114	# Calibration metrics
115	# ---------------------------------------------------------------------------
116	
117	def compute_ece(model, tokenizer, eval_dataset, gen_dataset=None,
118	                max_samples=512, max_length=256, n_bins=10, batch_size=8):
119	    """Expected Calibration Error on held-out eval_dataset.
120	
121	    Measures whether the model's confidence matches its accuracy at the
122	    token level. Rising ECE is a collapse canary (overconfidence).
123	    """
124	    model.eval()
125	    device = next(model.parameters()).device
126	
127	    confidences = []
128	    accuracies = []
129	
130	    texts = eval_dataset["text"][:max_samples]
131	    for i in range(0, len(texts), batch_size):
132	        batch_texts = texts[i:i + batch_size]
133	        enc = tokenizer(batch_texts, return_tensors="pt", truncation=True,
134	                        max_length=max_length, padding=True)
135	        input_ids = enc["input_ids"].to(device)
136	        attention_mask = enc["attention_mask"].to(device)
137	
138	        with torch.no_grad():
139	            logits = model(input_ids=input_ids, attention_mask=attention_mask).logits
140	
141	        shift_logits = logits[:, :-1, :]
142	        shift_labels = input_ids[:, 1:]
143	        shift_mask = attention_mask[:, 1:]
144	
145	        probs = torch.softmax(shift_logits, dim=-1)
146	        max_probs, preds = probs.max(dim=-1)
147	
148	        mask_flat = shift_mask.bool().flatten()
149	        confidences.append(max_probs.flatten()[mask_flat].cpu())
150	        accuracies.append((preds == shift_labels).flatten()[mask_flat].cpu().float())
151	
152	    confidences = torch.cat(confidences)
153	    accuracies = torch.cat(accuracies)
154	
155	    bin_boundaries = torch.linspace(0, 1, n_bins + 1)
156	    ece = 0.0
157	    for b in range(n_bins):
158	        mask = (confidences > bin_boundaries[b]) & (confidences <= bin_boundaries[b + 1])
159	        if mask.sum() == 0:
160	            continue
161	        bin_acc = accuracies[mask].mean()
162	        bin_conf = confidences[mask].mean()
163	        ece += mask.sum().item() / len(confidences) * abs(bin_acc - bin_conf).item()
164	
165	    return ece
166	
167	
168	# ---------------------------------------------------------------------------
169	# Spectral metrics
170	# ---------------------------------------------------------------------------
171	
172	def compute_effective_rank(model, tokenizer, eval_dataset, gen_dataset=None,
173	                           max_samples=256, max_length=256, batch_size=8):
174	    """Effective rank of last-layer hidden state covariance matrix.
175	
176	    effective_rank = exp(entropy of normalized eigenvalues)
177	    Declining effective rank signals representation collapse.
178	    """
179	    model.eval()
180	    device = next(model.parameters()).device
181	    all_hidden = []
182	
183	    texts = eval_dataset["text"][:max_samples]
184	    for i in range(0, len(texts), batch_size):
185	        batch_texts = texts[i:i + batch_size]
186	        enc = tokenizer(batch_texts, return_tensors="pt", truncation=True,
187	                        max_length=max_length, padding=True)
188	        input_ids = enc["input_ids"].to(device)
189	        attention_mask = enc["attention_mask"].to(device)
190	
191	        with torch.no_grad():
192	            outputs = model(input_ids=input_ids, attention_mask=attention_mask,
193	                            output_hidden_states=True)
194	        last_hidden = outputs.hidden_states[-1]  # (B, T, D)
195	
196	        # take mean-pooled representation per sample
197	        mask_expanded = attention_mask.unsqueeze(-1).float()
198	        pooled = (last_hidden * mask_expanded).sum(dim=1) / mask_expanded.sum(dim=1)
199	        all_hidden.append(pooled.cpu().float())
200	
201	    H = torch.cat(all_hidden, dim=0).numpy()  # (N, D)
202	    H = H - H.mean(axis=0, keepdims=True)
203	    cov = np.cov(H, rowvar=False)
204	    eigenvalues = np.linalg.eigvalsh(cov)
205	    eigenvalues = eigenvalues[eigenvalues > 1e-12]
206	
207	    # normalized eigenvalue distribution
208	    p = eigenvalues / eigenvalues.sum()
209	    entropy = -np.sum(p * np.log(p))
210	    return float(np.exp(entropy))
211	
212	
213	# ---------------------------------------------------------------------------
214	# Downstream metrics
215	# ---------------------------------------------------------------------------
216	
217	def compute_perplexity(model, tokenizer, eval_dataset, gen_dataset=None,
218	                       max_samples=512, max_length=256, batch_size=8):
219	    """Perplexity on held-out real data. The primary collapse indicator."""
220	    model.eval()
221	    device = next(model.parameters()).device
222	    total_loss = 0.0
223	    total_tokens = 0
224	
225	    texts = eval_dataset["text"][:max_samples]
226	    for i in range(0, len(texts), batch_size):
227	        batch_texts = texts[i:i + batch_size]
228	        enc = tokenizer(batch_texts, return_tensors="pt", truncation=True,
229	                        max_length=max_length, padding=True)
230	        input_ids = enc["input_ids"].to(device)
231	        attention_mask = enc["attention_mask"].to(device)
232	
233	        labels = input_ids.clone()
234	        labels[attention_mask == 0] = -100
235	
236	        with torch.no_grad():
237	            outputs = model(input_ids=input_ids, attention_mask=attention_mask,
238	                            labels=labels)
239	
240	        shift_mask = attention_mask[:, 1:]
241	        n_tokens = shift_mask.sum().item()
242	
243	        # outputs.loss is mean over all non-ignored tokens
244	        total_loss += outputs.loss.item() * n_tokens
245	        total_tokens += n_tokens
246	
247	    return float(math.exp(total_loss / max(total_tokens, 1)))
248	
249	
250	def compute_mauve(model, tokenizer, eval_dataset, gen_dataset=None,
251	                  max_samples=2000, max_length=256):
252	    """MAUVE score between real (eval_dataset) and generated (gen_dataset) text.
253	
254	    MAUVE ∈ [0, 1]; higher = generated distribution closer to real.
255	    Declining MAUVE is a downstream collapse signal.
256	    """
257	    import mauve as mauve_pkg
258	
259	    real_texts = eval_dataset["text"][:max_samples]
260	    real_texts = [t[:max_length * 4] for t in real_texts if len(t.strip()) > 0]
261	
262	    if gen_dataset is None:
263	        return 1.0  # no generated data to compare
264	
265	    gen_texts = gen_dataset["text"][:max_samples]
266	    gen_texts = [t[:max_length * 4] for t in gen_texts if len(t.strip()) > 0]
267	
268	    if len(gen_texts) == 0:
269	        return 0.0
270	
271	    # use the same number of samples for fair comparison
272	    n = min(len(real_texts), len(gen_texts))
273	    result = mauve_pkg.compute_mauve(
274	        p_text=real_texts[:n],
275	        q_text=gen_texts[:n],
276	        device_id=torch.cuda.current_device() if torch.cuda.is_available() else -1,
277	        max_text_length=max_length,
278	        verbose=False,
279	    )
280	    return float(result.mauve)
281	
282	
283	# ---------------------------------------------------------------------------
284	# Convenience: compute all metrics at once
285	# ---------------------------------------------------------------------------
286	
287	def compute_all_metrics(model, tokenizer, eval_dataset, gen_dataset=None,
288	                        **kwargs):
289	    """Compute every metric and return a flat dict.
290	
291	    Args:
292	        model: HuggingFace causal LM.
293	        tokenizer: Corresponding tokenizer.
294	        eval_dataset: Held-out real data split (must have "text" column).
295	        gen_dataset: Generated/synthetic data (must have "text" column).
296	        **kwargs: Forwarded to individual metric functions.
297	
298	    Returns:
299	        dict with keys: token_entropy, self_bleu, distinct_1/2/3, ece,
300	        effective_rank, perplexity, mauve.
301	    """
302	    results = {}
303	
304	    results["token_entropy"] = compute_token_entropy(
305	        model, tokenizer, eval_dataset, gen_dataset, **kwargs)
306	
307	    results["self_bleu"] = compute_self_bleu(
308	        model, tokenizer, eval_dataset, gen_dataset, **kwargs)
309	
310	    distinct = compute_distinct_n(
311	        model, tokenizer, eval_dataset, gen_dataset, **kwargs)
312	    results.update(distinct)
313	
314	    results["ece"] = compute_ece(
315	        model, tokenizer, eval_dataset, gen_dataset, **kwargs)
316	
317	    results["effective_rank"] = compute_effective_rank(
318	        model, tokenizer, eval_dataset, gen_dataset, **kwargs)
319	
320	    results["perplexity"] = compute_perplexity(
321	        model, tokenizer, eval_dataset, gen_dataset, **kwargs)
322	
323	    results["mauve"] = compute_mauve(
324	        model, tokenizer, eval_dataset, gen_dataset, **kwargs)
325	
326	    return results
327	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4a8bf0c-2307-4cb3-a30d-ca9fa86b1334",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "5ac7e77b-d09c-4863-b4ca-5a010d5a44e1",
  "sourceToolAssistantUUID": "d4a8bf0c-2307-4cb3-a30d-ca9fa86b1334",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-14T19:28:21.015Z_

Now let me check the paper_provenance and decisions files, and also the "worst" dream paper for contrast.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ac7e77b-d09c-4863-b4ca-5a010d5a44e1",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31j9f54yPSyrC3jW47Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07b7b27f-e34f-428e-8f7d-f253e7363462",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SHCGG2tn3s7su5zMxkeo2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4389,
      "cache_read_input_tokens": 49681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4389,
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

_source line 35 · 2026-05-14T19:28:22.495Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JfyV6BN8iZZ5NN2MxHFnKW`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "paper_provenance.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07b7b27f-e34f-428e-8f7d-f253e7363462",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31j9f54yPSyrC3jW47Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9790e650-185f-47b1-96b2-0e922eae1ba1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SHCGG2tn3s7su5zMxkeo2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4389,
      "cache_read_input_tokens": 49681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4389,
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

_source line 36 · 2026-05-14T19:28:22.502Z_

<details><summary>↩ Tool result · `toolu_01JfyV6BN8iZZ5NN2MxHFnKW`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_provenance.yaml found for 'distrib_canary_collapse'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9790e650-185f-47b1-96b2-0e922eae1ba1",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "31ce350d-0e39-4a1b-b896-7d1c9f0b0a34",
  "sourceToolAssistantUUID": "9790e650-185f-47b1-96b2-0e922eae1ba1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T19:28:22.992Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CSqEE4A8o7Q4Yak7PzUJZg`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31ce350d-0e39-4a1b-b896-7d1c9f0b0a34",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31j9f54yPSyrC3jW47Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61d501ea-3198-450c-91b0-d29ae187d870",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SHCGG2tn3s7su5zMxkeo2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4389,
      "cache_read_input_tokens": 49681,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4389
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 49681,
          "cache_creation_input_tokens": 4389,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4389,
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

_source line 38 · 2026-05-14T19:28:22.999Z_

<details><summary>↩ Tool result · `toolu_01CSqEE4A8o7Q4Yak7PzUJZg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/decisions.yaml\", \"content\": \"_next_id: 11\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 设计: Pythia-410M × WikiText-103 × 100% SC × 10 gen × 3 reps，验证 canary\\n    时序领先性'\\n  rationale: 100% SC 是最激进的 collapse 条件（理论预测必然退化），如果在此条件下没有任何 canary 指标领先 downstream，项目前提不成立。3\\n    reps × 10 gen 给出足够时间点做 cross-correlation。计算量 ~9 H100-hours，极低风险。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:26 UTC\\n  summary: MVP ECE 用 next-token calibration，SC 协议用 full replacement，effective rank\\n    用模型自身 embedding\\n  rationale: 'Reviewer warning 要求澄清 3 个操作化定义。ECE: next-token calibration 是 LM 原生度量、零额外成本，与\\n    Du et al. 的对比留到全量阶段加 downstream task ECE。SC: full replacement 是最大 feedback amplification\\n    (Truong & Truong Class 1)，collapse 信号最强，适合 MVP 压力测试。Effective rank: 模型自身 embedding\\n    与 SIGMA 一致，零额外依赖。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:27 UTC\\n  summary: 首选 AAAI 2027 (~Aug 2026)，May 25 ARR 不可行，后续 ARR cycle 备选\\n  rationale: 项目 2026-05-14 立项，无服务器无代码，11 天内无法完成 MVP + 全量实验 + 论文。AAAI 2027 给 ~2.5 个月，充分覆盖\\n    500-600 H100-hours 的实验量和论文写作。后续 ARR cycle (Jul/Aug) 也在射程内。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-14 05:36 UTC\\n  summary: 'MVP 参数修复: n_prompts 1000→5000, steps_per_gen 10000→5000 (4 epochs/gen)'\\n  rationale: Reviewer 发现原配置下 40 epochs/gen 在 1000 samples 上严重过拟合，模型可能 1-2 代即骤然击穿，所有指标同时崩溃，无法观察\\n    lead-lag 时序结构。修改后 4 epochs/gen 接近文献实践，collapse 逐渐发展，给 cross-correlation 分析留出足够时间点。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D005\\n  date: 2026-05-14 08:39 UTC\\n  summary: MVP 中期决策：不重启实验，MAUVE demote 为 supplementary，等完整 10-gen 数据再判断 collapse 速度和\\n    lead-lag\\n  rationale: MAUVE 基线 0.034 触发 evaluation criteria §4 floor effect 规则。Gen 0→1 跳变大是\\\"未训练→首次训练\\\"的固有落差，后续\\n    gen 的增量变化才是分析目标。100% SC 如果确认无 lead-lag，null result 符合 Truong & Truong 一阶相变理论——是有意义的发现，不是实验失败。重启只会浪费更多\\n    GPU 时间。\\n  related_experiments: []\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-14 17:37 UTC\\n  summary: 论文 framing 采用 \\\"delineating predictability boundaries\\\" 而非 \\\"universal canary\\\"\\n  rationale: 2-seed 预分析显示 canary 仅 lead diversity (distinct_n) 不 lead perplexity。ECE→perplexity\\n    甚至反向 (lag=+5)。\\\"predictability boundary\\\" framing 将 null result 转化为 evidence：100%\\n    SC 是同步崩溃 regime（不可预测），较低 α 可能出现渐进退化（可预测）。此 framing 对 null result 天然鲁棒，与 Truong\\n    & Truong 相变理论自然对接，reviewer 攻击面最小。Reviewer 独立预审认同此方向为最强 framing。\\n  related_experiments:\\n  - exp_id: mvp_v4_rep42\\n    role: evidence\\n    result: canary→distinct_n SIGNIFICANT, canary→perplexity NO LEAD\\n  - exp_id: mvp_v4_rep43\\n    role: evidence\\n    result: same pattern confirmed\\n  depends_on: []\\n- id: D007\\n  date: 2026-05-14 17:37 UTC\\n  summary: Post-MVP 实验优先级：α-sweep >> 方法 ablation > C4 数据集 > 规模验证\\n  rationale: α-sweep (25/50/75%) 是唯一能回答\\\"canary 在温和 regime 下是否 lead perplexity\\\"的实验，决定论文从\\n    diversity-only predictor 到 regime-dependent general predictor 的 claim 升级。方法 ablation\\n    零 GPU 成本、高 ROI（回答 reviewer 方法论质疑）。C4 堵 domain-specific 攻击。规模验证优先级最低（Pythia 家族共享架构，只测一个维度）。Reviewer\\n    预审排序一致。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-14 17:37 UTC\\n  summary: distinct_3 lead-lag 结果待 4-seed 确认，如 lag 仍双峰则降级 inconclusive，主文只报 distinct_1/distinct_2\\n  rationale: distinct_3 的 lag 估计跨 seed 不稳定（lag=-5 vs lag=-1，lag_std=2.0）。lag=-5 触及\\n    max_lag 边界，N=11 下只剩 6 点做相关，统计意义极弱，可能是边界效应伪信号。distinct_1/distinct_2 的 lag 跨 seed\\n    完全一致（lag_std=0），足以支撑核心 claim。Reviewer 建议 distinct_3 放 supplementary 并注明不稳定性。\\n  related_experiments:\\n  - exp_id: mvp_v4_rep42\\n    role: evidence\\n    result: distinct_3 lag=-5\\n  - exp_id: mvp_v4_rep43\\n    role: evidence\\n    result: distinct_3 lag=-1\\n  depends_on:\\n  - D006\\n- id: D009\\n  date: 2026-05-14 18:59 UTC\\n  summary: MVP 4-seed STRONG PASS，进入 Research 阶段全面实验\\n  rationale: 4/4 seed 一致确认 token_entropy 和 ECE 领先 diversity 指标 1-2 代（p<0.004）。核心发现：canary\\n    只领先 diversity collapse 不领先 perplexity degradation，这定义了 narrative 方向。plan_006 升级\\n    P0 以解决 max_lag 截断疑虑。\\n  related_experiments:\\n  - exp_id: mvp_v4_rep42\\n    role: evidence\\n    result: success\\n  - exp_id: mvp_v4_rep43\\n    role: evidence\\n    result: success\\n  - exp_id: mvp_v4_rep44\\n    role: evidence\\n    result: success\\n  - exp_id: mvp_v4_rep45\\n    role: evidence\\n    result: success\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-14 19:10 UTC\\n  summary: plan_003 重分析修正 perplexity 通道叙述：WEAK LEAD 非断裂，ECE 反向因果，维持 D008 distinct_3\\n    降级\\n  rationale: max_lag=7 重分析三个关键发现：(1) token_entropy→perplexity lag=-5 是真实峰值非截断伪影，但\\n    p=0.058-0.12 在 N=11 下不显著——\\\"通道断裂\\\"改为\\\"弱信号、效力不足\\\"；(2) ECE→perplexity 呈反向因果(lag=+4/+5,\\n    p<0.01)，两个 canary 家族在 perplexity 通道方向相反，论文必须讨论；(3) distinct_3 虽升 SIGNIFICANT 但\\n    lag_std>1.5（双峰），维持 D008 降级。plan_006(20-gen, N=21) 成为 framing 关键判定实验。\\n  related_experiments:\\n  - exp_id: plan_003\\n    role: evidence\\n    result: max_lag=7 重分析完成，核心 lead 稳固，perplexity 通道发现新细节\\n  depends_on:\\n  - D008\\n  - D009\\n\", \"total_chars\": 4841, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61d501ea-3198-450c-91b0-d29ae187d870",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "242dc7a4-0865-41f2-b8b2-bc15627fc8e1",
  "sourceToolAssistantUUID": "61d501ea-3198-450c-91b0-d29ae187d870",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-14T19:28:27.483Z_

Now let me also read the "worst" dream paper for contrast, to understand the range of possible reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "242dc7a4-0865-41f2-b8b2-bc15627fc8e1",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31jY6BzT5SYJJiYN1p8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0200951d-712f-4a5c-b14d-5352de2743d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGdjV5AA1HWNXPomqCb4aj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3173,
      "cache_read_input_tokens": 54070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3173,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 40 · 2026-05-14T19:28:29.001Z_

<details open><summary>🔧 Tool call — Read · `toolu_019DseXfZKjPB2497EVrFfDQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/worst/paper.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0200951d-712f-4a5c-b14d-5352de2743d5",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31jY6BzT5SYJJiYN1p8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "378a5063-fb5e-44bf-95ad-46ae85259561",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGdjV5AA1HWNXPomqCb4aj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3173,
      "cache_read_input_tokens": 54070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3173,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 41 · 2026-05-14T19:28:29.009Z_

<details><summary>↩ Tool result · `toolu_019DseXfZKjPB2497EVrFfDQ`</summary>

```text
1	\documentclass[letterpaper,11pt]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage{tabularx}
11	\usepackage{caption}
12	
13	\newcommand{\cmark}{\checkmark}
14	\newcommand{\xmark}{$\times$}
15	
16	\title{Taxonomy of Collapse Decoupling: Diversity and Quality Degrade\\Through Independent Channels in Iterative Synthetic Training}
17	
18	\author{
19	Anonymous Authors
20	}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	Iterative training on self-generated synthetic data leads to model collapse, yet the internal structure of this collapse remains poorly understood.
27	We present a systematic empirical study revealing that \emph{diversity collapse} (measured by distinct-$n$ and token entropy) and \emph{quality collapse} (measured by perplexity on held-out data) are fundamentally independent failure modes with distinct dynamics.
28	Using Pythia-410M trained iteratively on WikiText-103 across contamination ratios $\alpha \in \{0.25, 0.50, 0.75, 1.0\}$, we show that calibration-based canary metrics (ECE, token entropy) consistently lead diversity degradation by 1--2.5 generations ($|r| > 0.78$, cross-correlation analysis) but exhibit \emph{no} statistically significant lead over perplexity at any contamination level.
29	A \emph{decoupling diagram} across $\alpha$ regimes demonstrates that this independence holds universally---there is no contamination threshold $\alpha^*$ at which canary--perplexity coupling emerges.
30	Extended 20-generation trajectories reveal the mechanistic basis: canary and diversity metrics saturate (entropy $\to 0.62$, distinct-1 $\to 0.028$) while perplexity diverges unboundedly ($8420$ at generation 20), confirming distinct asymptotic behaviors.
31	A methodological ablation shows that naive Pearson cross-correlation and Toda-Yamamoto temporal precedence testing agree on 94\% of well-behaved canary--target pairs, establishing that practitioners need not employ complex time-series methods for this problem class.
32	Cross-domain (C4) and cross-scale (Pythia-1.4B) experiments reveal that while canary--diversity lead is domain- and scale-dependent, the canary--perplexity decoupling is robust.
33	These findings establish a \emph{collapse taxonomy} distinguishing independent degradation channels and demonstrate that canary-based monitoring, while effective for diversity tracking, cannot serve as a universal early warning system for model collapse.
34	\end{abstract}
35	
36	\section{Introduction}
37	
38	The proliferation of AI-generated content on the web has raised concerns about \emph{model collapse}---the progressive degradation of language models trained iteratively on their own outputs \cite{shumailov2024ai}.
39	Recent theoretical work establishes convergence guarantees under specific data mixing strategies \cite{fu2024towards}, while empirical studies document the phenomenon across architectures and scales \cite{dohmatob2024model}.
40	However, the prevailing treatment of model collapse as a monolithic process obscures critical structural distinctions: does the model lose output diversity before losing generation quality, or do these degradations proceed in lockstep?
41	
42	This question has practical import.
43	If collapse proceeds through separable channels, monitoring strategies must be channel-specific, and interventions designed for one failure mode may be ineffective against another.
44	Prior work has offered tantalizing hints: Du et al.\ observed that ECE changes precede accuracy degradation in image classifiers under synthetic data contamination, but their analysis lacked formal time-series testing and was limited to a single metric pair.
45	SIGMA \cite{vela2022sigma} provides spectral monitoring but does not quantify predictive lead times.
46	DCES \cite{alemohammad2024selfconsuming} offers reactive rather than predictive intervention.
47	
48	We present a systematic investigation that yields a surprising structural finding: \textbf{diversity collapse and quality collapse are fundamentally decoupled failure modes} operating through independent channels with distinct dynamics.
49	Our contributions are:
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "378a5063-fb5e-44bf-95ad-46ae85259561",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "0e5dfe77-34ab-4447-a5ee-113b78229a29",
  "sourceToolAssistantUUID": "378a5063-fb5e-44bf-95ad-46ae85259561",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T19:28:29.341Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014NaynJETdJ4ghujvfThTt5`</summary>

```json
{
  "pattern": "**/dream_*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e5dfe77-34ab-4447-a5ee-113b78229a29",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31jY6BzT5SYJJiYN1p8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77ba4899-2cd4-4fb7-a52a-517e0c6a3977",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGdjV5AA1HWNXPomqCb4aj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3173,
      "cache_read_input_tokens": 54070,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3173
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 54070,
          "cache_creation_input_tokens": 3173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3173,
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

_source line 43 · 2026-05-14T19:28:29.354Z_

<details><summary>↩ Tool result · `toolu_014NaynJETdJ4ghujvfThTt5`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77ba4899-2cd4-4fb7-a52a-517e0c6a3977",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "ed52f1e7-199b-43c1-9125-00d12567fa71",
  "sourceToolAssistantUUID": "77ba4899-2cd4-4fb7-a52a-517e0c6a3977",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-14T19:28:32.529Z_

Now let me also check what actual experiment data exists (the MVP results) to understand what is truly empirically grounded vs. what the "dream" paper projects.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed52f1e7-199b-43c1-9125-00d12567fa71",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31k1D6qWF9HHPabrVKE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2cd4b1c0-dcde-43e2-8789-00a93e10d0d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2e8H7dxwTZ42d9791EW1Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1434,
      "cache_read_input_tokens": 57243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1434,
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

_source line 45 · 2026-05-14T19:28:33.494Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01WYi3LM17nEje46muMQAV9W`</summary>

```json
{
  "pattern": "**/all_metrics.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cd4b1c0-dcde-43e2-8789-00a93e10d0d0",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31k1D6qWF9HHPabrVKE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "64d0ed86-c165-4d55-833d-e53ff07098c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2e8H7dxwTZ42d9791EW1Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1434,
      "cache_read_input_tokens": 57243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1434,
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

_source line 46 · 2026-05-14T19:28:33.507Z_

<details><summary>↩ Tool result · `toolu_01WYi3LM17nEje46muMQAV9W`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64d0ed86-c165-4d55-833d-e53ff07098c5",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "ea666ca0-7616-48e7-be60-1e98bc20841f",
  "sourceToolAssistantUUID": "64d0ed86-c165-4d55-833d-e53ff07098c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T19:28:33.754Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014pyJNQTQJAwaPiBXNaGYxD`</summary>

```json
{
  "pattern": "**/analysis_summary.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea666ca0-7616-48e7-be60-1e98bc20841f",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31k1D6qWF9HHPabrVKE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b4a8b28-376e-4133-9460-a6a687b456db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2e8H7dxwTZ42d9791EW1Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1434,
      "cache_read_input_tokens": 57243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1434,
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

_source line 48 · 2026-05-14T19:28:33.784Z_

<details><summary>↩ Tool result · `toolu_014pyJNQTQJAwaPiBXNaGYxD`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b4a8b28-376e-4133-9460-a6a687b456db",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "c78cf23d-dee5-4d10-86bb-9366b4aa40c8",
  "sourceToolAssistantUUID": "6b4a8b28-376e-4133-9460-a6a687b456db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T19:28:36.724Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0149huPfwa9ovm3m5rqTAGUg`</summary>

```json
{
  "pattern": "**/results/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c78cf23d-dee5-4d10-86bb-9366b4aa40c8",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31kLLni8URV9fesvcb7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7084da0-df6a-4eb6-a422-c2ae2b5e790f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4JjPcZbHbHM6oh3QuDLpQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 291,
      "cache_read_input_tokens": 58677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 291,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 50 · 2026-05-14T19:28:36.734Z_

<details><summary>↩ Tool result · `toolu_0149huPfwa9ovm3m5rqTAGUg`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7084da0-df6a-4eb6-a422-c2ae2b5e790f",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "297b29e2-a0b4-47c6-b5b3-96f4c4d75886",
  "sourceToolAssistantUUID": "b7084da0-df6a-4eb6-a422-c2ae2b5e790f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T19:28:37.233Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012fw2AqffkMQD825Ty9hzHy`</summary>

```json
{
  "pattern": "**/*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "297b29e2-a0b4-47c6-b5b3-96f4c4d75886",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31kLLni8URV9fesvcb7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db32c019-ef6f-4877-b630-32cb3428b5cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4JjPcZbHbHM6oh3QuDLpQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 291,
      "cache_read_input_tokens": 58677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 291,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 52 · 2026-05-14T19:28:37.241Z_

<details><summary>↩ Tool result · `toolu_012fw2AqffkMQD825Ty9hzHy`</summary>

```text
artifacts/dream_reports/dream_20260514T184925/best/experiment_data.json
artifacts/dream_reports/dream_20260514T184925/median/experiment_data.json
artifacts/dream_reports/dream_20260514T184925/worst/experiment_data.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db32c019-ef6f-4877-b630-32cb3428b5cc",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "5c109f4a-87fa-456d-b079-c4cd782d50db",
  "sourceToolAssistantUUID": "db32c019-ef6f-4877-b630-32cb3428b5cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T19:28:40.235Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Tq8NcERSJ5mQ3ia9rHUMpk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/experiment_data.json",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c109f4a-87fa-456d-b079-c4cd782d50db",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31kavsqKiuBRirXWEn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d15a7c86-494a-4726-93d3-e16de39711f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F28gkCddrXr6VxtEdadD21",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 316,
      "cache_read_input_tokens": 58968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 316,
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

_source line 54 · 2026-05-14T19:28:40.238Z_

<details><summary>↩ Tool result · `toolu_01Tq8NcERSJ5mQ3ia9rHUMpk`</summary>

```text
1	[
2	  {
3	    "name": "α-sweep (α∈{0.25, 0.50, 0.75})",
4	    "description": "Pythia-410M × WikiText-103 × α∈{0.25, 0.50, 0.75} × 3 seeds × 10 gen iterative training。 每代计算 ECE、token_entropy、effective_rank、self_bleu、distinct_1/2/3、perplexity。 Toda-Yamamoto panel temporal precedence 检验所有 canary→target 对。\n",
5	    "results": {
6	      "alpha_0.25_gen10_perplexity": 68.4,
7	      "alpha_0.25_gen10_token_entropy": 2.41,
8	      "alpha_0.25_gen10_ece": 0.138,
9	      "alpha_0.25_gen10_distinct_1": 0.312,
10	      "alpha_0.25_gen10_distinct_2": 0.681,
11	      "alpha_0.25_canary_diversity_lead_gen": 2.7,
12	      "alpha_0.25_canary_perplexity_lead_gen": 2.0,
13	      "alpha_0.25_TY_canary_to_diversity_p": 0.002,
14	      "alpha_0.25_TY_canary_to_perplexity_p": 0.018,
15	      "alpha_0.25_effect_size_r_ece_distinct1": 0.97,
16	      "alpha_0.50_gen10_perplexity": 189.3,
17	      "alpha_0.50_gen10_token_entropy": 1.94,
18	      "alpha_0.50_gen10_ece": 0.247,
19	      "alpha_0.50_gen10_distinct_1": 0.198,
20	      "alpha_0.50_gen10_distinct_2": 0.512,
21	      "alpha_0.50_canary_diversity_lead_gen": 2.0,
22	      "alpha_0.50_canary_perplexity_lead_gen": 1.3,
23	      "alpha_0.50_TY_canary_to_diversity_p": 0.001,
24	      "alpha_0.50_TY_canary_to_perplexity_p": 0.032,
25	      "alpha_0.50_effect_size_r_ece_distinct1": 0.96,
26	      "alpha_0.75_gen10_perplexity": 512.7,
27	      "alpha_0.75_gen10_token_entropy": 1.52,
28	      "alpha_0.75_gen10_ece": 0.361,
29	      "alpha_0.75_gen10_distinct_1": 0.112,
30	      "alpha_0.75_gen10_distinct_2": 0.402,
31	      "alpha_0.75_canary_diversity_lead_gen": 1.7,
32	      "alpha_0.75_canary_perplexity_lead_gen": 0.3,
33	      "alpha_0.75_TY_canary_to_diversity_p": 0.003,
34	      "alpha_0.75_TY_canary_to_perplexity_p": 0.214,
35	      "alpha_0.75_effect_size_r_ece_distinct1": 0.96,
36	      "phase_boundary_alpha_star": 0.6,
37	      "cross_seed_consistency_diversity_lead": "3/3 seeds at all α",
38	      "cross_seed_consistency_perplexity_lead": "3/3 seeds at α≤0.50; 1/3 at α=0.75"
39	    },
40	    "tables": [
41	      {
42	        "name": "Table 1: α-sweep Summary Statistics (mean ± std across seeds)",
43	        "columns": [
44	          "α",
45	          "gen10_ppl",
46	          "gen10_entropy",
47	          "gen10_ece",
48	          "gen10_d1",
49	          "gen10_d2",
50	          "canary→d1 lead (gen)",
51	          "canary→ppl lead (gen)",
52	          "TY p (canary→d1)",
53	          "TY p (canary→ppl)"
54	        ],
55	        "rows": [
56	          [
57	            "0.25",
58	            "68.4±4.1",
59	            "2.41±0.05",
60	            "0.138±0.009",
61	            "0.312±0.018",
62	            "0.681±0.022",
63	            "2.7±0.3",
64	            "2.0±0.4",
65	            "<0.005",
66	            "0.018"
67	          ],
68	          [
69	            "0.50",
70	            "189.3±12.6",
71	            "1.94±0.07",
72	            "0.247±0.015",
73	            "0.198±0.014",
74	            "0.512±0.019",
75	            "2.0±0.2",
76	            "1.3±0.3",
77	            "<0.005",
78	            "0.032"
79	          ],
80	          [
81	            "0.75",
82	            "512.7±31.4",
83	            "1.52±0.09",
84	            "0.361±0.021",
85	            "0.112±0.011",
86	            "0.402±0.025",
87	            "1.7±0.2",
88	            "0.3±0.5",
89	            "<0.005",
90	            "0.214"
91	          ],
92	          [
93	            "1.00 (MVP)",
94	            "1024.7±16.8",
95	            "1.27±0.06",
96	            "0.420±0.012",
97	            "0.075±0.008",
98	            "0.365±0.015",
99	            "1.5±0.3",
100	            "0.0±0.2",
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d15a7c86-494a-4726-93d3-e16de39711f3",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "117a1019-22a5-4c7e-96a8-d8be6dd9a304",
  "sourceToolAssistantUUID": "d15a7c86-494a-4726-93d3-e16de39711f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-14T19:28:43.484Z_

Now let me read the rest of this experiment data and also the worst paper to understand the variance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "117a1019-22a5-4c7e-96a8-d8be6dd9a304",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31kpD5paoKZKi75vTiw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b51b0bd-bc57-4f29-8bd1-a8de2a6d1eb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WegAHmNVqJ1NmqqbuqU7W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1824,
      "cache_read_input_tokens": 59284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1824,
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

_source line 56 · 2026-05-14T19:28:44.318Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S7TMx4wG1cPuLkNvLkwyPu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/experiment_data.json",
  "offset": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b51b0bd-bc57-4f29-8bd1-a8de2a6d1eb9",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31kpD5paoKZKi75vTiw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "841e1b89-7ed5-4d0f-acfa-903a6c76b377",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WegAHmNVqJ1NmqqbuqU7W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1824,
      "cache_read_input_tokens": 59284,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1824
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 59284,
          "cache_creation_input_tokens": 1824,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1824,
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

_source line 57 · 2026-05-14T19:28:44.647Z_

<details><summary>↩ Tool result · `toolu_01S7TMx4wG1cPuLkNvLkwyPu`</summary>

```text
100	            "0.0±0.2",
101	            "<0.001",
102	            "0.487"
103	          ]
104	        ]
105	      },
106	      {
107	        "name": "Table 2: Toda-Yamamoto Panel Results — All Canary→Target Pairs",
108	        "columns": [
109	          "canary",
110	          "target",
111	          "α=0.25 (lag, p)",
112	          "α=0.50 (lag, p)",
113	          "α=0.75 (lag, p)",
114	          "α=1.0 (lag, p)"
115	        ],
116	        "rows": [
117	          [
118	            "ECE",
119	            "distinct_1",
120	            "(-3, <0.001)",
121	            "(-2, <0.001)",
122	            "(-2, 0.003)",
123	            "(-2, <0.001)"
124	          ],
125	          [
126	            "ECE",
127	            "distinct_2",
128	            "(-3, 0.002)",
129	            "(-2, 0.002)",
130	            "(-2, 0.006)",
131	            "(-1, 0.004)"
132	          ],
133	          [
134	            "token_entropy",
135	            "distinct_1",
136	            "(-2, 0.003)",
137	            "(-2, 0.004)",
138	            "(-1, 0.012)",
139	            "(-1, 0.003)"
140	          ],
141	          [
142	            "token_entropy",
143	            "distinct_2",
144	            "(-3, 0.004)",
145	            "(-2, 0.006)",
146	            "(-2, 0.018)",
147	            "(-1, 0.009)"
148	          ],
149	          [
150	            "ECE",
151	            "perplexity",
152	            "(-2, 0.015)",
153	            "(-1, 0.032)",
154	            "(0, 0.187)",
155	            "(0, 0.412)"
156	          ],
157	          [
158	            "token_entropy",
159	            "perplexity",
160	            "(-2, 0.021)",
161	            "(-1, 0.041)",
162	            "(0, 0.238)",
163	            "(-5*, 0.063)"
164	          ],
165	          [
166	            "effective_rank",
167	            "distinct_1",
168	            "(0, 0.342)",
169	            "(0, 0.287)",
170	            "(0, 0.415)",
171	            "(0, 0.523)"
172	          ],
173	          [
174	            "self_bleu",
175	            "distinct_1",
176	            "(0, 0.178)",
177	            "(0, 0.221)",
178	            "(-1, 0.089)",
179	            "(0, 0.156)"
180	          ]
181	        ]
182	      }
183	    ],
184	    "figures": [],
185	    "analysis": "α-sweep 是全文核心实验。Phase diagram 将三条 claims 统一为一张图： diversity 通道全 regime 可预测（Claim 1），perplexity 通道 regime-dependent（Claim 2）， α* boundary 明确。effective_rank 和 self_bleu 在所有 α 下均不显著—— 与 MVP 结论一致，排除选择偏差质疑。3 seeds 在所有 α 下 diversity lead 一致性 3/3， perplexity lead 在 α≤0.50 下 3/3，α=0.75 下仅 1/3（边界行为，符合 phase transition 预期）。\n\n\nα 控制每代训练数据中合成数据的比例。低 α 下真实数据作为 anchor 减缓 distribution drift， collapse 从 catastrophic（α=1.0 时 gen10 ppl>1000）变为 gradual（α=0.25 时 gen10 ppl~68）。 渐进退化使不同 metric family 的 onset timing 解耦——calibration（ECE）和 token distribution （entropy）对微小 distribution shift 最敏感（单代内 KL divergence 变化即可触发 2σ onset）， 而 diversity（distinct_n）需要 vocabulary 实质收缩才反映，perplexity 则需 loss landscape 发生结构性改变。在 α=1.0（MVP）下三者近乎同步崩溃（1-2 gen window），因为 drift 速度 压倒了 sensitivity 差异。降低 α 拉长 collapse timeline，sensitivity 差异被放大： ECE onset 出现在 gen 2-3 而 distinct_1 onset 在 gen 5-6（α=0.25），产生 ~2.7 gen lead。 Perplexity 的可预测性取决于 drift 是否足够慢让 canary signal 积累足够 lead——α=0.25/0.50 下 drift rate 允许 1-2 gen canary→perplexity lead，但 α=0.75 时 drift 过快， perplexity 几乎与 canary 同步变化，TY 检验不再显著（p=0.214）。 Phase boundary α*≈0.60 是 perplexity lead 从统计显著跌落到不显著的转折点—— 这是 drift rate 与 metric sensitivity gap 的临界平衡点。\n"
186	  },
187	  {
188	    "name": "方法论 ablation: Naive vs Robust 检验",
189	    "description": "在 MVP 4-seed 数据 + α-sweep 9 runs 数据上，对比四种 lead-lag 量化方法： (i) naive Pearson lag-correlation (ii) 差分后 cross-correlation (iii) threshold-based onset lead (iv) Toda-Yamamoto panel temporal precedence。 统计所有方法对所有 canary→target pair 的显著性判定，量化伪显著被推翻比例。\n",
190	    "results": {
191	      "total_pairs_tested": 104,
192	      "naive_pearson_significant_count": 71,
193	      "differenced_xcorr_significant_count": 48,
194	      "threshold_onset_significant_count": 39,
195	      "TY_significant_count": 42,
196	      "naive_overturned_by_TY_pct": 40.8,
197	      "naive_overturned_by_TY_count": 29,
198	      "false_positive_category_breakdown": {
199	        "effective_rank_pairs": 12,
200	        "self_bleu_pairs": 8,
201	        "canary_to_ppl_high_alpha": 6,
202	        "spurious_reverse_direction": 3
203	      },
204	      "TY_unique_significant_not_in_naive": 0,
205	      "method_agreement_TY_vs_threshold": 0.88
206	    },
207	    "tables": [
208	      {
209	        "name": "Table 3: Method Comparison — Significant Pair Counts",
210	        "columns": [
211	          "Method",
212	          "Significant pairs",
213	          "Agrees w/ TY",
214	          "Disagrees w/ TY",
215	          "False positive vs TY",
216	          "False negative vs TY"
217	        ],
218	        "rows": [
219	          [
220	            "Naive Pearson",
221	            "71/104",
222	            "42",
223	            "29",
224	            "29 (40.8%)",
225	            "0"
226	          ],
227	          [
228	            "Differenced XCorr",
229	            "48/104",
230	            "36",
231	            "12",
232	            "12 (16.9%)",
233	            "6"
234	          ],
235	          [
236	            "Threshold Onset",
237	            "39/104",
238	            "37",
239	            "2",
240	            "2 (2.8%)",
241	            "5"
242	          ],
243	          [
244	            "Toda-Yamamoto",
245	            "42/104",
246	            "—",
247	            "—",
248	            "—",
249	            "—"
250	          ]
251	        ]
252	      },
253	      {
254	        "name": "Table 4: Breakdown of Naive False Positives Overturned by TY",
255	        "columns": [
256	          "Category",
257	          "Count",
258	          "Example pair"
259	        ],
260	        "rows": [
261	          [
262	            "Failed canary (eff_rank/self_bleu) → any target",
263	            "20",
264	            "effective_rank→distinct_1 at α=0.50"
265	          ],
266	          [
267	            "canary→perplexity at α≥0.75",
268	            "6",
269	            "ECE→ppl at α=0.75"
270	          ],
271	          [
272	            "Reverse direction (target→canary)",
273	            "3",
274	            "distinct_1→ECE at α=1.0"
275	          ]
276	        ]
277	      }
278	    ],
279	    "figures": [],
280	    "analysis": "~41% 伪显著率远超 30% 阈值，方法论贡献独立成立。这直接回应 reviewer concern \"为什么不用简单相关\"——答案是简单方法在这个 setting 下系统性高估 canary 预测能力， 尤其是对失败 canary 和高 α regime。Threshold onset 与 TY 一致性高（88%）， 但 TY 提供 p-value 和方向性检验，统计论证更强。\n\n\n非平稳时间序列（所有 metric 在 iterative training 中趋势性退化）的 Pearson correlation 产生 spurious regression——两个独立但都有趋势的序列可以 |r|>0.9。naive 方法对所有 \"都在下降\"的 metric pair 报告显著，包括 effective_rank→diversity（实际无 lead-lag 关系， 只是共享下降趋势）和 canary→perplexity at α≥0.75（同步崩溃无因果方向）。 差分后去趋势消除部分伪关联但对短序列（10 gen）power 不足，false negative 较多。 TY 方法在 VAR 框架中检验 Granger non-causality，自动处理非平稳性（通过 augmented lag），对真正的 lead-lag 关系（canary→diversity）保持高 power（p<0.005）， 对无方向性的同步崩溃正确报告不显著（p>0.05）。~41% 的 naive 显著关联被推翻， 主要来自三类：(1) 失败 canary 族的伪关联（effective_rank、self_bleu 与任何 target）， (2) 高 α 下 canary→perplexity 的同步崩溃被误判为 lead， (3) 少数反向因果（target→canary）被 naive 双向 correlation 报告为显著。\n"
281	  },
282	  {
283	    "name": "MVP 结果 formalization (max_lag=7)",
284	    "description": "在 MVP 4-seed (α=1.0) 数据上重跑 TY 检验，max_lag 从 5 增大到 7， 验证 token_entropy→perplexity 的 lag=-5 是否为截断伪影。 统一 2σ onset 定义，输出 paper-ready 数值。\n",
285	    "results": {
286	      "max_lag_7_ece_to_distinct1_lag": -2,
287	      "max_lag_7_ece_to_distinct1_p": 0.0004,
288	      "max_lag_7_entropy_to_distinct1_lag": -1,
289	      "max_lag_7_entropy_to_distinct1_p": 0.0018,
290	      "max_lag_7_entropy_to_ppl_lag": -5,
291	      "max_lag_7_entropy_to_ppl_p": 0.071,
292	      "max_lag_7_ece_to_ppl_lag": 0,
293	      "max_lag_7_ece_to_ppl_p": 0.412,
294	      "onset_2sigma_ece": "gen 2.1±0.3",
295	      "onset_2sigma_entropy": "gen 2.4±0.4",
296	      "onset_2sigma_distinct1": "gen 3.8±0.5",
297	      "onset_2sigma_distinct2": "gen 4.2±0.4",
298	      "onset_2sigma_ppl": "gen 2.3±0.3",
299	      "cross_seed_consistency": "4/4 seeds for canary→diversity"
300	    },
301	    "tables": [
302	      {
303	        "name": "Table S1: MVP (α=1.0) TY Results — max_lag=5 vs max_lag=7",
304	        "columns": [
305	          "Pair",
306	          "max_lag=5 (lag, p)",
307	          "max_lag=7 (lag, p)",
308	          "Conclusion"
309	        ],
310	        "rows": [
311	          [
312	            "ECE→distinct_1",
313	            "(-2, <0.001)",
314	            "(-2, 0.0004)",
315	            "Stable — genuine lead"
316	          ],
317	          [
318	            "ECE→distinct_2",
319	            "(-1, 0.003)",
320	            "(-1, 0.004)",
321	            "Stable"
322	          ],
323	          [
324	            "entropy→distinct_1",
325	            "(-1, 0.002)",
326	            "(-1, 0.0018)",
327	            "Stable"
328	          ],
329	          [
330	            "entropy→ppl",
331	            "(-5, 0.052)",
332	            "(-5, 0.071)",
333	            "Not significant — noise"
334	          ],
335	          [
336	            "ECE→ppl",
337	            "(0, 0.38)",
338	            "(0, 0.412)",
339	            "Not significant — synchronous"
340	          ]
341	        ]
342	      }
343	    ],
344	    "figures": [],
345	    "analysis": "max_lag=7 确认 MVP 核心结论不变。entropy→ppl lag=-5 是噪声非截断—— 在 α=1.0 下 canary 不 lead perplexity 的结论更加稳固， 为 α-sweep 中低 α 下 lead 出现提供对比 baseline。\n\n\n在 α=1.0 (100% self-consuming) 下 collapse 极快，perplexity onset（gen ~2.3） 与 canary onset（gen ~2.1-2.4）几乎同步——drift rate 太快，metric sensitivity 差异 不足以产生可检测的 lead。max_lag=7 不改变 canary→diversity 的结论（lag=-2/-1 稳定）， 因为 diversity onset 确实延后到 gen 3.8-4.2。token_entropy→ppl 的 lag=-5 在 max_lag=7 下保持但 p 值从边界上升到 0.071——这不是截断伪影而是统计 noise， 因为 100% SC 下两者实际同步崩溃（onset 差 <0.3 gen），VAR 模型在短序列上 拟合出的 lag=-5 缺乏统计支撑。这进一步支持 Claim 2 的 regime-dependent 叙事。\n"
346	  },
347	  {
348	    "name": "C4 Cross-domain Validation",
349	    "description": "Pythia-410M × C4 × α=0.50 × 3 seeds × 10 gen。验证 WikiText-103 上 确认的 canary ranking 和 lead time 是否在不同 domain 数据上保持。\n",
350	    "results": {
351	      "c4_alpha050_gen10_perplexity": 211.8,
352	      "c4_alpha050_gen10_token_entropy": 1.88,
353	      "c4_alpha050_gen10_ece": 0.261,
354	      "c4_alpha050_gen10_distinct_1": 0.183,
355	      "c4_alpha050_gen10_distinct_2": 0.494,
356	      "c4_alpha050_canary_diversity_lead_gen": 1.8,
357	      "c4_alpha050_canary_perplexity_lead_gen": 1.0,
358	      "c4_alpha050_TY_ece_to_d1_p": 0.003,
359	      "c4_alpha050_TY_entropy_to_d1_p": 0.006,
360	      "c4_alpha050_TY_ece_to_ppl_p": 0.044,
361	      "canary_ranking_preserved": true,
362	      "rank_correlation_wiki_vs_c4": 0.94
363	    },
364	    "tables": [
365	      {
366	        "name": "Table 5: Cross-domain Comparison (α=0.50)",
367	        "columns": [
368	          "Metric pair",
369	          "WikiText-103 (lag, p)",
370	          "C4 (lag, p)",
371	          "Δlag"
372	        ],
373	        "rows": [
374	          [
375	            "ECE→distinct_1",
376	            "(-2, <0.001)",
377	            "(-2, 0.003)",
378	            "0"
379	          ],
380	          [
381	            "entropy→distinct_1",
382	            "(-2, 0.004)",
383	            "(-2, 0.006)",
384	            "0"
385	          ],
386	          [
387	            "ECE→ppl",
388	            "(-1, 0.032)",
389	            "(-1, 0.044)",
390	            "0"
391	          ],
392	          [
393	            "entropy→ppl",
394	            "(-1, 0.041)",
395	            "(-1, 0.058)",
396	            "0"
397	          ],
398	          [
399	            "eff_rank→distinct_1",
400	            "(0, 0.287)",
401	            "(0, 0.334)",
402	            "0"
403	          ]
404	        ]
405	      }
406	    ],
407	    "figures": [],
408	    "analysis": "C4 验证 canary ranking 的 domain-invariance。ECE 和 entropy 在两个 domain 上 对 diversity 的 lead 一致（lag=-2），对 perplexity 的 lead 也一致（lag=-1）。 effective_rank 在两个 domain 均失败，排除其作为 canary 的可能。 这支持 canary 机制是 model-intrinsic 的论断。\n\n\nCanary metric 的 lead 机制是 distribution-level 的——ECE 检测 calibration drift， token entropy 检测 vocabulary concentration——这两个现象在任何 iterative self-consuming 训练中都会发生，不依赖于 domain-specific 的 token 分布。C4 是 web crawl 数据， vocabulary 更多样、初始 distinct_n 更高，但 iterative training 仍然驱动 mode collapse（vocabulary 收缩到高频 pattern）。绝对指标值会因 domain 差异 而不同（C4 初始 perplexity 稍高、entropy 稍低因为 web text 噪声更大）， 但相对 ranking（ECE 和 entropy 领先 diversity，diversity 领先 perplexity） 和 lead time 量级（~1.8 gen for diversity, ~1.0 gen for perplexity at α=0.50） 应保持，因为底层的 distributional drift dynamics 是 model-intrinsic 而非 data-specific。 Rank correlation 0.94 反映个别 pair 的精确 lag 可能差 ±0.5 gen 但排序一致。\n"
409	  },
410	  {
411	    "name": "Pythia-1.4B Scale Spot-check",
412	    "description": "Pythia-1.4B × WikiText-103 × α=0.50 × 3 seeds × 10 gen。 验证 canary lead 是否在 3.4× 参数量下保持。\n",
413	    "results": {
414	      "scale_1.4b_gen10_perplexity": 142.5,
415	      "scale_1.4b_gen10_token_entropy": 2.12,
416	      "scale_1.4b_gen10_ece": 0.198,
417	      "scale_1.4b_gen10_distinct_1": 0.241,
418	      "scale_1.4b_gen10_distinct_2": 0.589,
419	      "scale_1.4b_canary_diversity_lead_gen": 2.3,
420	      "scale_1.4b_canary_perplexity_lead_gen": 1.5,
421	      "scale_1.4b_TY_ece_to_d1_p": 0.002,
422	      "scale_1.4b_TY_entropy_to_d1_p": 0.004,
423	      "scale_1.4b_TY_ece_to_ppl_p": 0.028,
424	      "canary_ranking_preserved": true,
425	      "lead_time_scaling_trend": "slightly longer at larger scale"
426	    },
427	    "tables": [
428	      {
429	        "name": "Table 6: Scale Comparison at α=0.50",
430	        "columns": [
431	          "Model",
432	          "gen10_ppl",
433	          "canary→d1 lead",
434	          "canary→ppl lead",
435	          "TY p (ECE→d1)",
436	          "TY p (ECE→ppl)"
437	        ],
438	        "rows": [
439	          [
440	            "Pythia-410M",
441	            "189.3",
442	            "2.0 gen",
443	            "1.3 gen",
444	            "<0.005",
445	            "0.032"
446	          ],
447	          [
448	            "Pythia-1.4B",
449	            "142.5",
450	            "2.3 gen",
451	            "1.5 gen",
452	            "0.002",
453	            "0.028"
454	          ]
455	        ]
456	      }
457	    ],
458	    "figures": [],
459	    "analysis": "Scale spot-check 确认 canary lead 跨规模保持，且有 lead time 随 scale 增加的趋势。 虽然单点验证不能 claim scaling law，但方向性结论支持实用价值论述。 Limitation 中需注明：仅验证到 1.4B，更大规模（7B+）是 future work。\n\n\n更大模型有更高的初始 capacity 和更好的 calibration（gen0 ECE 更低）， collapse 在每代的 marginal degradation 更小（模型能更好地 fit 混合数据）， 但 cumulative drift 仍然驱动最终退化。关键推断：如果每代 drift 更小， 不同 metric family 的 sensitivity gap 有更多代数来积累差异—— ECE 可能在 gen 2 就 onset 而 distinct_1 在 gen 4.5， 比 410M 的 gen 2.5/4.0 差距更大，lead time 从 2.0 增加到 ~2.3 gen。 Perplexity 也更渐进（gen10 ppl 142 vs 410M 的 189）， canary→ppl lead 从 1.3 增加到 ~1.5 gen。这个 scaling trend（更大模型→更长 lead time） 如果成立将是一个有吸引力的 finding——意味着 canary 在实际部署的大模型上 预警窗口更宽，实用价值更高。3/3 seed consistency 因为更大模型的 variance 更低。\n"
460	  },
461	  {
462	    "name": "Extended Run 20 gen (α=1.0, max_lag=10)",
463	    "description": "Pythia-410M × WikiText-103 × α=1.0 × 20 gen × 2 seeds。 验证 entropy→ppl lag=-5 是否为 max_lag 截断伪影。\n",
464	    "results": {
465	      "gen20_perplexity": 4287.3,
466	      "gen20_token_entropy": 0.68,
467	      "gen20_ece": 0.512,
468	      "gen20_distinct_1": 0.024,
469	      "gen20_distinct_2": 0.108,
470	      "extended_TY_entropy_to_ppl_lag": 0,
471	      "extended_TY_entropy_to_ppl_p": 0.523,
472	      "extended_TY_ece_to_d1_lag": -2,
473	      "extended_TY_ece_to_d1_p": 0.0002,
474	      "canary_diversity_lead_gen_20gen": 1.8,
475	      "collapse_saturation_gen": 12
476	    },
477	    "tables": [
478	      {
479	        "name": "Table S2: Extended Run TY Results (max_lag=10)",
480	        "columns": [
481	          "Pair",
482	          "10-gen (lag, p)",
483	          "20-gen (lag, p)",
484	          "Conclusion"
485	        ],
486	        "rows": [
487	          [
488	            "entropy→ppl",
489	            "(-5, 0.071)",
490	            "(0, 0.523)",
491	            "No lead — confirmed"
492	          ],
493	          [
494	            "ECE→distinct_1",
495	            "(-2, 0.0004)",
496	            "(-2, 0.0002)",
497	            "Stable lead — confirmed"
498	          ],
499	          [
500	            "ECE→ppl",
501	            "(0, 0.412)",
502	            "(0, 0.487)",
503	            "No lead — confirmed"
504	          ]
505	        ]
506	      }
507	    ],
508	    "figures": [],
509	    "analysis": "Extended run 排除截断伪影质疑。α=1.0 下 canary→ppl 的 absence 是 robust 结论， 不受 max_lag 或 sequence length 影响。结果放 supplementary 即可。\n\n\n延长到 20 gen 提供两个信息：(1) max_lag=10 下 entropy→ppl 仍无显著 lead（lag=0, p=0.52）， 确认 α=1.0 下 canary 不 lead perplexity 是 genuine 结论非截断伪影—— 因为 100% SC 的 drift rate 太快，所有 metrics 在 gen 1-5 内同步急剧退化； (2) gen 12 后 collapse 趋于饱和（perplexity 增长率下降，因为模型输出已近乎 deterministic），这个 saturation 行为为 phase diagram 增加了一个维度—— 不仅 α 影响可预测性，generation depth 也有影响（但 best tier 下这是 supplementary observation，不是 main claim）。canary→diversity lead 在 20 gen 下保持（~1.8 gen）， 确认 diversity 通道的可预测性在极端 regime 和长 horizon 下稳健。\n"
510	  },
511	  {
512	    "name": "CRS Intervention 实验",
513	    "description": "CRS-predictive intervention vs no-intervention baseline。 Pythia-410M × α=0.75 × 3 seeds × 10 gen。 当 ECE 2σ onset 触发时自动增加 real data ratio。\n",
514	    "results": {
515	      "no_intervention_gen10_distinct1": 0.112,
516	      "crs_intervention_gen10_distinct1": 0.198,
517	      "diversity_preservation_pct": 76.8,
518	      "intervention_trigger_gen": "gen 3.2±0.4",
519	      "post_intervention_alpha_effective": 0.52,
520	      "gen10_perplexity_no_intervention": 512.7,
521	      "gen10_perplexity_crs": 341.2,
522	      "perplexity_reduction_pct": 33.4
523	    },
524	    "tables": [
525	      {
526	        "name": "Table 7: Intervention Results (α=0.75, mean across 3 seeds)",
527	        "columns": [
528	          "Condition",
529	          "gen10_d1",
530	          "gen10_d2",
531	          "gen10_ppl",
532	          "gen10_ece"
533	        ],
534	        "rows": [
535	          [
536	            "No intervention (α=0.75)",
537	            "0.112±0.011",
538	            "0.402±0.025",
539	            "512.7±31.4",
540	            "0.361±0.021"
541	          ],
542	          [
543	            "CRS-predictive (trigger @ ECE onset)",
544	            "0.198±0.015",
545	            "0.524±0.020",
546	            "341.2±22.7",
547	            "0.253±0.018"
548	          ],
549	          [
550	            "Oracle (α=0.50 throughout)",
551	            "0.198±0.014",
552	            "0.512±0.019",
553	            "189.3±12.6",
554	            "0.247±0.015"
555	          ]
556	        ]
557	      }
558	    ],
559	    "figures": [],
560	    "analysis": "Intervention 实验将 canary 的预测能力转化为可操作的 collapse mitigation。 CRS 的 diversity preservation 接近 oracle level 说明 ECE onset 的 timing 足够早。 Perplexity 恢复不如 oracle 因为前 3 代在高 α 下的 calibration drift 不可逆。 P2 优先级——如果时间紧可砍，但如果包含将显著提升 practical contribution。\n\n\nCRS 在 ECE onset（~gen 3）时将 α 从 0.75 降到 ~0.52（增加 real data 比例）， 等效于将训练轨迹从 α=0.75 regime \"切换\"到 α≈0.50 regime。 从 α-sweep 数据我们知道 α=0.50 的 gen10 distinct_1 ≈ 0.198 vs α=0.75 的 0.112， 所以 intervention 后的 gen10 diversity 应接近 α=0.50 的水平。 Perplexity 也相应改善（从 ~513 降到 ~341，接近 α=0.50 和 α=0.75 的中间值， 因为前 3 代仍在 α=0.75 下训练积累了部分 drift）。 76.8% diversity preservation = (0.198 - 0.112) / (0.312 - 0.112) × 100%， 即恢复了从 α=0.75 到 α=0.25 baseline 之间 ~77% 的 diversity gap。 这不是 perfect recovery 因为前几代的 drift 不可逆，但足以证明 predictive intervention 的实用价值——canary 提供的 1-2 gen 预警窗口转化为可操作的 diversity 保护。\n"
561	  },
562	  {
563	    "name": "Accumulate vs Replace 数据策略 Ablation",
564	    "description": "α=0.50 下 accumulate（保留所有历史生成数据）vs replace（每代仅用最新生成数据） 对比 × 3 seeds × 10 gen。\n",
565	    "results": {
566	      "replace_gen10_distinct1": 0.198,
567	      "accumulate_gen10_distinct1": 0.267,
568	      "replace_gen10_ppl": 189.3,
569	      "accumulate_gen10_ppl": 124.8,
570	      "accumulate_canary_diversity_lead": 2.5,
571	      "replace_canary_diversity_lead": 2.0,
572	      "accumulate_canary_ppl_lead": 1.8,
573	      "replace_canary_ppl_lead": 1.3,
574	      "accumulate_collapse_rate_reduction_pct": 34.2
575	    },
576	    "tables": [
577	      {
578	        "name": "Table 8: Data Strategy Comparison (α=0.50)",
579	        "columns": [
580	          "Strategy",
581	          "gen10_d1",
582	          "gen10_ppl",
583	          "canary→d1 lead",
584	          "canary→ppl lead"
585	        ],
586	        "rows": [
587	          [
588	            "Replace",
589	            "0.198±0.014",
590	            "189.3±12.6",
591	            "2.0 gen",
592	            "1.3 gen"
593	          ],
594	          [
595	            "Accumulate",
596	            "0.267±0.016",
597	            "124.8±9.3",
598	            "2.5 gen",
599	            "1.8 gen"
600	          ]
601	        ]
602	      }
603	    ],
604	    "figures": [],
605	    "analysis": "Accumulate ablation 验证 Fu et al. 理论预测的同时发现一个新 finding： 数据策略不仅影响 collapse severity，还影响 canary lead time—— 更渐进的 collapse 给予更长的预警窗口。P2 优先级但如果包含增加 paper depth。\n\nAccumulate 模式保留所有历史生成数据，训练集 diversity 衰减更慢—— 每代新增的合成数据只占总数据的 1/(gen+1) 而非 replace 模式下的 α 比例， effective contamination ratio 随代数递减。Fu et al. 理论预测 accumulate 在 足够代数后收敛（distribution drift bounded），而 replace 可能发散。 在 10 gen 内，accumulate 的 gen10 metrics 显著优于 replace（distinct_1 0.267 vs 0.198）， collapse 更渐进意味着 metric sensitivity gap 有更多代数积累—— canary→diversity lead 从 2.0 增加到 2.5 gen，canary→ppl lead 从 1.3 增加到 1.8 gen。 这对 practical implication 有意义：accumulate 策略不仅减缓 collapse， 还扩大了 canary 预警窗口。\n"
606	  }
607	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "841e1b89-7ed5-4d0f-acfa-903a6c76b377",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "7b6a6baa-2c6d-4cb7-93ba-31e2afd51428",
  "sourceToolAssistantUUID": "841e1b89-7ed5-4d0f-acfa-903a6c76b377",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-14T19:28:51.105Z_

Now I have a thorough understanding of the paper, its experimental setup, what data actually exists vs. what is projected, and the internal project documentation revealing important discrepancies between the "best dream" paper and the actual MVP results. Let me now also check the "worst" paper to understand the range of framings, and then write my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b6a6baa-2c6d-4cb7-93ba-31e2afd51428",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31m8QxmrUHd6LAKsACT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "973ce6f7-79fb-437f-bbf0-f63aa10053b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4czjsEyiCmyvCMKTDwxvp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10115,
      "cache_read_input_tokens": 61108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10115,
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

_source line 59 · 2026-05-14T19:28:52.531Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HzdKmrdXVxq8Aqx6Fib8ex`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/worst/paper.tex",
  "offset": 50,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "973ce6f7-79fb-437f-bbf0-f63aa10053b8",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31m8QxmrUHd6LAKsACT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f42d8584-dbbb-4337-b24e-82b5ce8bf917",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4czjsEyiCmyvCMKTDwxvp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10115,
      "cache_read_input_tokens": 61108,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10115
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 209,
          "cache_read_input_tokens": 61108,
          "cache_creation_input_tokens": 10115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10115,
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

_source line 60 · 2026-05-14T19:28:52.537Z_

<details><summary>↩ Tool result · `toolu_01HzdKmrdXVxq8Aqx6Fib8ex`</summary>

```text
50	
51	\begin{enumerate}
52	    \item \textbf{Collapse Taxonomy.} We establish empirically that iterative synthetic training induces at least two independent degradation channels---a \emph{diversity channel} (tracked by distinct-$n$, token entropy) and a \emph{quality channel} (tracked by held-out perplexity)---with no necessary temporal coupling between them.
53	
54	    \item \textbf{Decoupling Diagram.} We construct a contamination--regime diagram showing that canary metrics (ECE, token entropy) lead diversity degradation by 1--2.5 generations but exhibit zero predictive lead over perplexity across \emph{all} tested $\alpha$ values. Unlike a phase diagram with a critical boundary, our decoupling diagram reveals universal independence.
55	
56	    \item \textbf{Methodological Validation.} We demonstrate through ablation that naive cross-correlation and rigorous Toda-Yamamoto testing yield equivalent conclusions for well-behaved metric pairs (94\% agreement), providing a positive methodological result: simple tools suffice when degradation dynamics are monotonic.
57	\end{enumerate}
58	
59	Our findings reframe the model collapse monitoring problem: canary-based early warning is achievable for diversity but not for quality, and this limitation is structural rather than methodological.
60	
61	\section{Related Work}
62	
63	\paragraph{Model Collapse.}
64	Shumailov et al.\ demonstrated that iterative training on model-generated data leads to progressive quality loss, with tail distributions collapsing first.
65	Dohmatob et al.\ provided scaling law analyses showing collapse rates depend on model capacity and data mixing ratios.
66	Fu et al.\ proved that accumulating historical synthetic data (rather than replacing each generation) provably mitigates collapse under certain mixing conditions.
67	Alemohammad et al.\ studied self-consuming generative models and proposed reactive data curation strategies.
68	
69	\paragraph{Collapse Monitoring.}
70	SIGMA monitors spectral properties of model weights for distribution shift detection but does not address predictive lead quantification.
71	Du et al.\ informally noted ECE changes preceding accuracy drops in vision models, the closest precursor to our canary analysis, but without statistical time-series testing.
72	Truong \& Truong showed that standard early warning indicators (e.g., rising autocorrelation) can fail near first-order phase transitions---a cautionary result that motivates our regime-dependent analysis.
73	Kalinowski et al.\ proposed topological complexity indices for representation collapse detection but with high computational cost unsuitable for online monitoring.
74	
75	\paragraph{Time-Series Causality in ML.}
76	Toda-Yamamoto testing extends Granger causality to potentially non-stationary series by augmenting the VAR model order, avoiding pre-testing for unit roots.
77	Its application to ML training dynamics is novel; prior work on training curve analysis has relied on informal visual inspection or simple correlation.
78	
79	\section{Method}
80	
81	\subsection{Iterative Training Protocol}
82	
83	We adopt a standard iterative self-consumption protocol.
84	Let $\mathcal{D}_0$ denote the original clean dataset and $M_0$ a pretrained language model.
85	At each generation $t$:
86	\begin{enumerate}
87	    \item Generate synthetic dataset $\mathcal{S}_t$ by sampling from $M_{t-1}$
88	    \item Form training set $\mathcal{D}_t = \alpha \cdot \mathcal{S}_t + (1-\alpha) \cdot \mathcal{D}_0$ where $\alpha \in [0,1]$ controls contamination ratio
89	    \item Fine-tune $M_{t-1}$ on $\mathcal{D}_t$ to obtain $M_t$
90	\end{enumerate}
91	
92	We use Pythia-410M as the base model and WikiText-103 as $\mathcal{D}_0$, running up to $T=10$ generations (extended to $T=20$ for trajectory analysis) with $\alpha \in \{0.25, 0.50, 0.75, 1.0\}$.
93	Each condition is replicated across 3--4 random seeds.
94	An additional data strategy ablation compares the \emph{replace} protocol above against an \emph{accumulate} protocol where $\mathcal{D}_t = \bigcup_{i=0}^{t} \mathcal{S}_i \cup \mathcal{D}_0$ (with appropriate reweighting).
95	
96	\subsection{Metric Families}
97	
98	We track two families of collapse indicators:
99	
100	\paragraph{Canary Metrics (Hypothesized Leading Indicators).}
101	\begin{itemize}
102	    \item \textbf{Expected Calibration Error (ECE)}: Measures discrepancy between predicted token probabilities and observed frequencies, binned into 15 equal-mass bins.
103	    \item \textbf{Token Entropy}: Shannon entropy of the next-token prediction distribution, averaged over evaluation prompts.
104	\end{itemize}
105	
106	\paragraph{Target Metrics (Collapse Endpoints).}
107	\begin{itemize}
108	    \item \textbf{Distinct-$n$} ($n \in \{1,2\}$): Ratio of unique $n$-grams to total $n$-grams in generated text, measuring lexical diversity.
109	    \item \textbf{Perplexity}: Held-out perplexity on the WikiText-103 validation set, measuring generation quality relative to the true data distribution.
110	\end{itemize}
111	
112	We also evaluated effective rank and self-BLEU as potential canaries; both failed to produce reliable lead signals and are reported for completeness.
113	
114	\subsection{Statistical Framework}
115	
116	\paragraph{Cross-Correlation Analysis.}
117	For each canary--target pair $(c_t, y_t)$ over $T$ generations, we compute the Pearson cross-correlation at lag $\ell$:
118	\begin{equation}
119	    r(\ell) = \text{Corr}(c_{t}, y_{t+\ell}), \quad \ell \in [-L, L]
120	\end{equation}
121	where $L$ is the maximum lag (5 or 7).
122	A negative optimal lag $\ell^* < 0$ indicates the canary leads the target.
123	Statistical significance is assessed via a two-tailed $t$-test with $p < 0.05$.
124	
125	\paragraph{Signal Onset Analysis.}
126	We define the onset generation $g^*$ for metric $m$ as the first generation where $|m_t - m_0| > 2\sigma_{m_0}$, where $\sigma_{m_0}$ is estimated from the first two generations.
127	Lead time is then $\Delta g = g^*_{\text{target}} - g^*_{\text{canary}}$.
128	
129	\paragraph{Toda-Yamamoto Testing.}
130	To guard against spurious regression in non-stationary training dynamics, we apply Toda-Yamamoto (TY) temporal precedence testing.
131	A VAR($k+d_{\max}$) model is estimated where $k$ is the optimal lag order (BIC) and $d_{\max}$ is the maximal integration order.
132	A Wald test on the first $k$ coefficient matrices tests the null of no temporal precedence.
133	This approach is valid regardless of the integration properties of the series.
134	
135	\section{Experiments}
136	
137	\subsection{Canary Lead Under Full Self-Consumption}
138	\label{sec:mvp}
139	
140	We first establish the baseline canary--target relationships under $\alpha = 1.0$ (100\% synthetic data each generation) with 4 seeds and $T=10$ generations.
141	Table~\ref{tab:mvp} reports cross-correlation results at max\_lag $\in \{5, 7\}$.
142	
143	\begin{table}[t]
144	\centering
145	\caption{Cross-correlation lead-lag summary under $\alpha=1.0$, 4 seeds. Negative lag indicates canary leads target. Results shown for max\_lag=7; max\_lag=5 yields qualitatively identical conclusions.}
146	\label{tab:mvp}
147	\small
148	\begin{tabular}{@{}lcccc@{}}
149	\toprule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f42d8584-dbbb-4337-b24e-82b5ce8bf917",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "f89b539b-36df-4011-a2cf-741e16536769",
  "sourceToolAssistantUUID": "f42d8584-dbbb-4337-b24e-82b5ce8bf917",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-14T19:28:55.918Z_

I now have sufficient information to write a thorough, grounded review. Let me now submit it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f89b539b-36df-4011-a2cf-741e16536769",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31miVKpTKinahaAtCGq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57732ac7-9834-4afb-9dd0-6698d98d38fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XyLopPqNwgfd33n2fRTYV2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2378,
      "cache_read_input_tokens": 71223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2378,
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

_source line 62 · 2026-05-14T19:28:56.308Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JSjWkPBcYVoqFixS66zfAa`</summary>

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
  "parentUuid": "57732ac7-9834-4afb-9dd0-6698d98d38fd",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31miVKpTKinahaAtCGq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b5da486-c772-4c45-a73e-be299febe6a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XyLopPqNwgfd33n2fRTYV2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2378,
      "cache_read_input_tokens": 71223,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2378
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 111,
          "cache_read_input_tokens": 71223,
          "cache_creation_input_tokens": 2378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2378,
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

_source line 63 · 2026-05-14T19:28:56.309Z_

<details><summary>↩ Tool result · `toolu_01JSjWkPBcYVoqFixS66zfAa`</summary>

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
  "parentUuid": "3b5da486-c772-4c45-a73e-be299febe6a0",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "df8012b7-75a9-4d60-b22c-8c01bb316df1",
  "sourceToolAssistantUUID": "3b5da486-c772-4c45-a73e-be299febe6a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-14T19:29:04.798Z_



Now I will write and submit the review. I need to determine which tier this is for. The paper summary provided in the prompt describes the "worst" tier paper (with the "Taxonomy of Collapse Decoupling" title and claims about universal decoupling / no alpha* boundary). However, the "best" tier paper makes different claims (phase boundary at alpha* ~0.60, canaries DO lead perplexity at low alpha). Let me re-read the prompt carefully to confirm which paper I'm reviewing.

The prompt says the title is "Taxonomy of Collapse Decoupling: Diversity and Quality Degrade Through Independent Channels in Iterative Synthetic Training" -- this matches the **worst** tier paper. The claims described (no alpha* boundary, universal decoupling, 94% agreement meaning simple methods suffice) also match the worst tier. Let me verify by checking the worst paper's content more closely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df8012b7-75a9-4d60-b22c-8c01bb316df1",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31mzS28XM5tnjqykVU1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9886b33-8828-4297-8f5e-bc98c9fdc329",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013TH7BStsG7C9YNqMDH3YF3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 689,
      "cache_read_input_tokens": 73601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 689,
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

_source line 65 · 2026-05-14T19:29:05.255Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SitBTXfULsd6NycCC4WwUW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/worst/paper.tex",
  "offset": 135
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9886b33-8828-4297-8f5e-bc98c9fdc329",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31mzS28XM5tnjqykVU1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53ff8cec-5140-4c25-bfaf-8a37ae7d21da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013TH7BStsG7C9YNqMDH3YF3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 689,
      "cache_read_input_tokens": 73601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 689,
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

_source line 66 · 2026-05-14T19:29:05.539Z_

<details><summary>↩ Tool result · `toolu_01SitBTXfULsd6NycCC4WwUW`</summary>

```text
135	\section{Experiments}
136	
137	\subsection{Canary Lead Under Full Self-Consumption}
138	\label{sec:mvp}
139	
140	We first establish the baseline canary--target relationships under $\alpha = 1.0$ (100\% synthetic data each generation) with 4 seeds and $T=10$ generations.
141	Table~\ref{tab:mvp} reports cross-correlation results at max\_lag $\in \{5, 7\}$.
142	
143	\begin{table}[t]
144	\centering
145	\caption{Cross-correlation lead-lag summary under $\alpha=1.0$, 4 seeds. Negative lag indicates canary leads target. Results shown for max\_lag=7; max\_lag=5 yields qualitatively identical conclusions.}
146	\label{tab:mvp}
147	\small
148	\begin{tabular}{@{}lcccc@{}}
149	\toprule
150	Canary $\to$ Target & Lag & $|r|$ & $p < 0.05$ seeds & Onset lead \\
151	\midrule
152	ECE $\to$ distinct-1 & $-2.50 \pm 0.58$ & $>$0.99 & 4/4 & 1.50 gen \\
153	ECE $\to$ distinct-2 & $-1.25 \pm 0.50$ & $>$0.99 & 4/4 & --- \\
154	Entropy $\to$ distinct-1 & $-1.25 \pm 0.50$ & $>$0.99 & 4/4 & 1.25 gen \\
155	Entropy $\to$ perplexity & $-5.50 \pm --$ & 0.68 & 1/4 & --- \\
156	ECE $\to$ perplexity & $0.00$ & --- & 0/4 & --- \\
157	\bottomrule
158	\end{tabular}
159	\end{table}
160	
161	The canary$\to$diversity lead is strong and seed-consistent: ECE leads distinct-1 by $2.50 \pm 0.58$ generations with $|r| > 0.99$ across all 4 seeds.
162	The $2\sigma$ onset analysis confirms this independently: ECE onset at generation $1.50$, entropy onset at $1.75$, distinct-1 onset at $3.00$, yielding onset-based leads of 1.25--1.50 generations.
163	
164	In stark contrast, \textbf{no canary exhibits significant lead over perplexity}: ECE$\to$perplexity shows zero lag with no significant seeds, while entropy$\to$perplexity yields an apparent lag of $-5.5$ that is significant in only 1/4 seeds ($p = 0.09$ mean).
165	Expanding max\_lag from 5 to 7 does not qualitatively alter any conclusion, confirming the results are not truncation artifacts.
166	
167	\paragraph{Perplexity onset.} Perplexity onset occurs at generation $2.50$ on average---\emph{between} canary onset (1.50--1.75) and diversity onset (3.00--3.25).
168	This intermediate timing means perplexity is neither predicted by canaries nor a lagging indicator of diversity; it follows its own trajectory.
169	
170	\subsection{The Decoupling Diagram}
171	\label{sec:sweep}
172	
173	We extend the analysis across contamination ratios $\alpha \in \{0.25, 0.50, 0.75\}$ with 3 seeds each ($T=10$).
174	Table~\ref{tab:sweep} presents the cross-correlation results alongside $\alpha = 1.0$ from Section~\ref{sec:mvp}.
175	
176	\begin{table}[t]
177	\centering
178	\caption{Cross-correlation summary across contamination regimes. ``Sig.''\ denotes number of seeds with $p < 0.05$. The canary$\to$perplexity row is non-significant at \emph{every} $\alpha$.}
179	\label{tab:sweep}
180	\small
181	\begin{tabular}{@{}llcccc@{}}
182	\toprule
183	Pair & & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.0$ \\
184	\midrule
185	\multirow{3}{*}{\rotatebox{0}{\scriptsize ECE$\to$d1}}
186	& Lag & $-0.67 \pm 0.58$ & $-1.00 \pm 0.82$ & $-1.33 \pm 0.58$ & $-2.50 \pm 0.58$ \\
187	& $|r|$ & 0.78 & 0.82 & 0.86 & $>$0.99 \\
188	& Sig. & 1/3 & 2/3 & 2/3 & 4/4 \\
189	\midrule
190	\multirow{2}{*}{\rotatebox{0}{\scriptsize Ent$\to$d1}}
191	& Lag & $-0.33$ & $-0.67$ & $-1.00$ & $-1.25$ \\
192	& Sig. & 1/3 & 2/3 & 3/3 & 4/4 \\
193	\midrule
194	\multirow{2}{*}{\rotatebox{0}{\scriptsize ECE$\to$ppl}}
195	& Lag & 0.00 & 0.00 & 0.00 & 0.00 \\
196	& Sig. & 0/3 & 0/3 & 0/3 & 0/4 \\
197	\midrule
198	\multirow{2}{*}{\rotatebox{0}{\scriptsize Ent$\to$ppl}}
199	& Lag & --- & --- & --- & $-5.50$ \\
200	& Sig. & 0/3 & 0/3 & 0/3 & 1/4 \\
201	\bottomrule
202	\end{tabular}
203	\end{table}
204	
205	\begin{table}[t]
206	\centering
207	\caption{Metric values at generation 10 across contamination ratios, illustrating the decoupling between diversity and quality degradation.}
208	\label{tab:gen10}
209	\small
210	\begin{tabular}{@{}lcccc@{}}
211	\toprule
212	Metric & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.0$ \\
213	\midrule
214	Perplexity & 42.5 & 78.3 & 285.6 & --- \\
215	Token entropy & 2.85 & 2.45 & 1.78 & --- \\
216	ECE & 0.045 & 0.12 & 0.28 & --- \\
217	Distinct-1 & 0.088 & 0.082 & 0.074 & --- \\
218	\bottomrule
219	\end{tabular}
220	\end{table}
221	
222	The results reveal a striking pattern that we term the \textbf{decoupling diagram}.
223	Rather than a phase diagram with a critical $\alpha^*$ boundary separating predictable from unpredictable regimes, we observe:
224	
225	\begin{enumerate}
226	    \item \textbf{Canary$\to$diversity lead exists at all $\alpha$} but is fragile at low contamination: lead magnitude increases monotonically from $0.67$ gen ($\alpha{=}0.25$) to $2.50$ gen ($\alpha{=}1.0$), while cross-seed consistency improves from 1/3 to 4/4 significant seeds.
227	
228	    \item \textbf{Canary$\to$perplexity decoupling is universal}: across all four $\alpha$ values, no canary metric exhibits significant lead over perplexity.
229	    This is not a regime-dependent phenomenon with a transition point; it is a structural property of the collapse dynamics.
230	\end{enumerate}
231	
232	The decoupling intensifies at low $\alpha$: at $\alpha{=}0.25$, perplexity barely degrades (42.5 vs.\ baseline $\approx 30$) while distinct-1 has already declined to 0.088, demonstrating that diversity loss can proceed substantially without quality loss.
233	
234	\subsection{Methodological Validation}
235	\label{sec:method}
236	
237	To assess whether the cross-correlation findings could be artifacts of spurious regression in non-stationary series, we compare four methods: (i) naive Pearson lag-correlation, (ii) differenced cross-correlation, (iii) threshold-based lead time, and (iv) Toda-Yamamoto panel temporal precedence.
238	Table~\ref{tab:method} summarizes the agreement analysis.
239	
240	\begin{table}[t]
241	\centering
242	\caption{Agreement between naive Pearson cross-correlation and Toda-Yamamoto testing. ``Overturned'' indicates pairs where naive analysis finds significance but TY does not.}
243	\label{tab:method}
244	\small
245	\begin{tabular}{@{}lcc@{}}
246	\toprule
247	& $\alpha{=}1.0$ & $\alpha$-sweep \\
248	\midrule
249	Naive significant pairs & 24 & 36 \\
250	TY significant pairs & 18 & 28 \\
251	Overturned by TY & 6 (25.0\%) & 5 (13.9\%) \\
252	\midrule
253	Overturned (core canaries only) & 1 (3.1\%) & --- \\
254	Overall agreement rate & 0.88 & 0.88 \\
255	Core canary agreement rate & 0.94 & 0.94 \\
256	TY Granger direction consistent & \cmark & \cmark \\
257	\bottomrule
258	\end{tabular}
259	\end{table}
260	
261	The key finding is a \textbf{systematic negative result}: for the well-behaved canary pairs (ECE/entropy $\to$ distinct-1/2), naive cross-correlation and Toda-Yamamoto agree on 94\% of cases.
262	The 6\% disagreement is concentrated on already-known problematic metrics (effective\_rank, self-BLEU) whose non-monotonic dynamics inflate naive correlations.
263	
264	This has a positive practical implication: \textbf{practitioners monitoring iterative training need not employ complex time-series causality tests}.
265	Simple cross-correlation is reliable when the underlying degradation dynamics are monotonic---a condition that holds for the dominant collapse channels we identify.
266	The monotonicity of iterative degradation provides natural detrending, suppressing the spurious regression risk that motivates Toda-Yamamoto testing in general econometric settings.
267	
268	The TY significance rate of 55\% across all pairs (including low-$\alpha$ conditions) reflects insufficient statistical power with 10-generation time series rather than methodological disagreement: both methods fail to detect signals in gentle degradation curves.
269	
270	\subsection{Extended Trajectory Analysis}
271	\label{sec:extended}
272	
273	To investigate whether the entropy$\to$perplexity lag of $-5.5$ observed in Section~\ref{sec:mvp} reflects a genuine long-range lead truncated by the 10-generation window, we extend the protocol to $T=20$ generations ($\alpha{=}1.0$, 2 seeds, max\_lag$=$10).
274	
275	\begin{table}[t]
276	\centering
277	\caption{Extended trajectory key statistics ($\alpha{=}1.0$, 20 generations). Entropy saturates at generation 8 while perplexity diverges without bound.}
278	\label{tab:extended}
279	\small
280	\begin{tabular}{@{}lcccc@{}}
281	\toprule
282	& Gen 10 & Gen 15 & Gen 20 & Saturates? \\
283	\midrule
284	Perplexity & --- & 2850 & 8420 & No \\
285	Token entropy & --- & 0.85 & 0.62 & Yes (gen 8) \\
286	Distinct-1 & --- & 0.042 & 0.028 & Slow decay \\
287	\bottomrule
288	\end{tabular}
289	\end{table}
290	
291	The extended run yields two critical insights:
292	
293	\paragraph{The lag=$-5.5$ is a saturation artifact, not a truncation artifact.}
294	With max\_lag$=$10, the two seeds yield lags of $-7$ and $-3$ ($\text{std} = 2.83$, $p = 0.14$, 0/2 significant), confirming no stable lead exists.
295	The apparent lag in the 10-generation analysis arose from a coincidental alignment between entropy's early rapid descent (generations 1--5) and perplexity's later acceleration (generations 5--10).
296	
297	\paragraph{Asymptotic decoupling provides mechanistic evidence.}
298	Token entropy saturates at generation 8 ($\approx 0.62$, near its physical lower bound for the vocabulary) while perplexity continues to diverge without bound ($2850 \to 8420$ from generation 15 to 20).
299	This asymptotic divergence is the strongest evidence for fundamental channel independence: canary metrics are \emph{intrinsic statistics} of the generated distribution (measuring concentration of the output distribution), bounded below as the distribution's support shrinks to a minimum.
300	Perplexity is a \emph{cross-distribution statistic} (cross-entropy against held-out ground truth), unbounded as the model distribution diverges from the data distribution.
301	
302	The information-theoretic argument is straightforward: entropy $H(p_\theta)$ and calibration error measure properties of $p_\theta$ alone, while perplexity $\exp(H(p_{\text{data}}, p_\theta))$ involves the cross-entropy between two distributions.
303	There is no theoretical requirement that intrinsic distribution statistics and cross-distribution statistics exhibit temporal coupling, and our empirical results confirm this independence.
304	
305	\subsection{Cross-Domain Validation}
306	\label{sec:c4}
307	
308	To test whether collapse channel structure transfers across data distributions, we replicate the $\alpha{=}0.50$ protocol on C4 (web-crawled text) with 3 seeds.
309	
310	\begin{table}[t]
311	\centering
312	\caption{WikiText-103 vs.\ C4 canary behavior at $\alpha{=}0.50$. Canary ranking reverses across domains while decoupling from perplexity is preserved.}
313	\label{tab:c4}
314	\small
315	\begin{tabular}{@{}llcc@{}}
316	\toprule
317	Pair & & WikiText & C4 \\
318	\midrule
319	\multirow{2}{*}{ECE$\to$d1}
320	& Lag & $-1.00 \pm 0.82$ & $-0.33 \pm 0.58$ \\
321	& Sig. & 2/3 & 1/3 \\
322	\midrule
323	\multirow{2}{*}{Ent$\to$d1}
324	& Lag & $-0.67$ & $-0.67$ \\
325	& Sig. & 2/3 & 1/3 \\
326	\midrule
327	ECE$\to$ppl & Sig. & 0/3 & 0/3 \\
328	\midrule
329	\multicolumn{2}{@{}l}{Canary ranking preserved?} & \multicolumn{2}{c}{No} \\
330	\multicolumn{2}{@{}l}{Entropy leads ECE on C4?} & \multicolumn{2}{c}{Yes} \\
331	\bottomrule
332	\end{tabular}
333	\end{table}
334	
335	\begin{table}[t]
336	\centering
337	\caption{Generation 10 metrics: WikiText-103 vs.\ C4 at $\alpha{=}0.50$.}
338	\label{tab:c4_gen10}
339	\small
340	\begin{tabular}{@{}lcc@{}}
341	\toprule
342	Metric & WikiText & C4 \\
343	\midrule
344	Perplexity & 78.3 & 62.8 \\
345	Distinct-1 & 0.082 & 0.085 \\
346	Token entropy & 2.45 & 2.62 \\
347	ECE & 0.12 & 0.088 \\
348	\bottomrule
349	\end{tabular}
350	\end{table}
351	
352	The cross-domain experiment yields a \textbf{partial negative result}: the \emph{existence} of canary$\to$diversity lead transfers (entropy still leads distinct-1), but the \emph{ranking} of canary effectiveness does not.
353	On WikiText, ECE is the stronger canary; on C4, entropy is more sensitive.
354	This reversal likely reflects C4's greater distributional heterogeneity: the model's calibration degrades more slowly on diverse web text (attention distributed across domains prevents overconfidence), while token entropy is more fragile (long-tail tokens from rare domains are pruned early by synthetic training).
355	
356	Crucially, the canary$\to$perplexity decoupling remains robust: 0/3 seeds show significant ECE$\to$perplexity lead on either dataset.
357	This supports our thesis that decoupling is a structural property of collapse dynamics rather than a dataset-specific artifact.
358	
359	\subsection{Scale Spot-Check}
360	\label{sec:scale}
361	
362	We perform a spot-check with Pythia-1.4B at $\alpha{=}0.50$ (3 seeds, $T{=}10$) to probe scale dependence.
363	
364	\begin{table}[t]
365	\centering
366	\caption{Scale comparison: Pythia-410M vs.\ 1.4B at $\alpha{=}0.50$. Larger models show slower collapse and reduced canary lead magnitude.}
367	\label{tab:scale}
368	\small
369	\begin{tabular}{@{}llcc@{}}
370	\toprule
371	& & 410M & 1.4B \\
372	\midrule
373	\multirow{2}{*}{ECE$\to$d1}
374	& Lag & $-1.00 \pm 0.82$ & $-0.33 \pm 0.58$ \\
375	& Sig. & 2/3 & 1/3 \\
376	\midrule
377	\multirow{2}{*}{Ent$\to$d1}
378	& Lag & $-0.67$ & $-0.33$ \\
379	& Sig. & 2/3 & 1/3 \\
380	\midrule
381	Gen-10 ppl & & 78.3 & 55.2 \\
382	Gen-10 d1 & & 0.082 & 0.087 \\
383	Gen-10 entropy & & 2.45 & 2.71 \\
384	Gen-10 ECE & & 0.12 & 0.075 \\
385	\midrule
386	\multicolumn{2}{@{}l}{Collapse rate ratio (1.4B / 410M)} & \multicolumn{2}{c}{0.65} \\
387	\multicolumn{2}{@{}l}{Canary lead preserved?} & \multicolumn{2}{c}{No (inconclusive)} \\
388	\bottomrule
389	\end{tabular}
390	\end{table}
391	
392	The 1.4B model collapses $\sim$35\% slower than the 410M model (rate ratio 0.65), consistent with the intuition that larger capacity absorbs distributional shift more gradually.
393	However, canary lead is \textbf{not preserved} in this experimental window: both ECE$\to$distinct-1 and entropy$\to$distinct-1 show reduced lag magnitude ($-0.33$ vs.\ $-1.00$/$-0.67$) with only 1/3 seeds reaching significance.
394	
395	We flag this result as \textbf{inconclusive rather than negative}: the slower collapse rate means that $\alpha{=}0.50 \times T{=}10$ provides insufficient exposure for the 1.4B model.
396	Gen-10 metrics (ppl = 55.2, d1 = 0.087, ECE = 0.075) show the model has degraded less than the 410M counterpart at the same generation, suggesting longer runs or higher $\alpha$ would be needed to detect lead-lag structure.
397	The collapse rate ratio of 0.65 is itself a useful data point for the taxonomy: it quantifies how model scale modulates collapse dynamics within the diversity channel.
398	
399	\subsection{Canary-Triggered Intervention}
400	\label{sec:intervention}
401	
402	We test whether canary-based early warning can improve intervention outcomes using a Canary-Response Strategy (CRS): when ECE exceeds a $2\sigma$ threshold, the next generation's training data is supplemented with additional real data.
403	We compare CRS against a no-intervention baseline at $\alpha{=}0.75$ (3 seeds, $T{=}10$).
404	
405	\begin{table}[t]
406	\centering
407	\caption{Intervention experiment: CRS-triggered real data injection vs.\ no-intervention baseline ($\alpha{=}0.75$). No metric reaches statistical significance ($p > 0.1$ for all).}
408	\label{tab:intervention}
409	\small
410	\begin{tabular}{@{}lccc@{}}
411	\toprule
412	Metric & Baseline & CRS & $\Delta$\% \\
413	\midrule
414	Distinct-1 (gen 10) & 0.074 & 0.081 & +9.5\% \\
415	Perplexity (gen 10) & 285.6 & 270.3 & $-$5.4\% \\
416	CRS trigger gen & --- & $2.3 \pm 0.8$ & --- \\
417	Effect significant? & \multicolumn{3}{c}{No ($p > 0.1$)} \\
418	Cross-seed consistent? & \multicolumn{3}{c}{No} \\
419	\bottomrule
420	\end{tabular}
421	\end{table}
422	
423	The intervention experiment yields a \textbf{negative result}: CRS produces a marginal improvement in diversity preservation (+9.5\% relative distinct-1) and perplexity ($-5.4\%$ relative), but neither effect reaches statistical significance ($p > 0.1$), and results are not consistent across seeds.
424	
425	This negative result is \emph{coherent with the decoupling thesis}.
426	The canary$\to$diversity lead of $\sim$1 generation at $\alpha{=}0.75$ provides at most one generation of anticipation---insufficient for meaningful intervention when collapse dynamics are cumulative.
427	Furthermore, CRS is a diversity-channel intervention (triggered by a diversity-tracking canary) that cannot address quality-channel degradation.
428	The modest perplexity improvement ($-5.4\%$) likely reflects indirect effects of increased real data rather than canary-guided targeting.
429	
430	One seed showed CRS performing \emph{worse} than the baseline, suggesting that false canary triggers (due to noise in early ECE measurements) can introduce real data at inopportune times, disrupting training stability.
431	
432	\subsection{Data Strategy Ablation}
433	\label{sec:datastrategy}
434	
435	Following Fu et al., we compare \emph{accumulate} (retain all historical synthetic data) vs.\ \emph{replace} (use only the current generation's synthetic data) at $\alpha{=}0.50$ (3 seeds, $T{=}10$).
436	
437	\begin{table}[t]
438	\centering
439	\caption{Accumulate vs.\ replace data strategies at $\alpha{=}0.50$. Accumulate slows collapse but eliminates canary predictive lead.}
440	\label{tab:accreplace}
441	\small
442	\begin{tabular}{@{}lcc@{}}
443	\toprule
444	& Accumulate & Replace \\
445	\midrule
446	Gen-10 perplexity & 48.3 & 78.3 \\
447	Gen-10 distinct-1 & 0.091 & 0.082 \\
448	Gen-10 entropy & 2.78 & 2.45 \\
449	\midrule
450	ECE$\to$d1 lag & $-0.33$ & $-1.00$ \\
451	ECE$\to$d1 sig.\ seeds & 0/3 & 2/3 \\
452	Collapse rate ratio & \multicolumn{2}{c}{0.55 (acc/rep)} \\
453	Canary behavior different? & \multicolumn{2}{c}{Yes} \\
454	\bottomrule
455	\end{tabular}
456	\end{table}
457	
458	Accumulate reduces collapse rate by $\sim$45\% (rate ratio 0.55), confirming Fu et al.'s theoretical predictions.
459	However, it simultaneously \textbf{eliminates canary predictive lead}: ECE$\to$distinct-1 lag shrinks from $-1.00$ (replace) to $-0.33$ (accumulate) with 0/3 significant seeds.
460	
461	This creates a \textbf{monitoring paradox}: the regime where early warning is most needed (replace, fast collapse) is where canaries are most effective, while the regime where collapse is better controlled (accumulate) is where canaries lose predictive power.
462	The mechanism is intuitive: accumulation dilutes each generation's synthetic contribution, producing quasi-linear degradation where all metrics decline approximately synchronously.
463	Lead-lag structure is an emergent property of nonlinear dynamics---when the forcing is weak and degradation is gradual, all metrics respond in their linear regime with zero phase difference.
464	
465	This finding adds another dimension to the collapse taxonomy: canary effectiveness is not only regime-dependent (on $\alpha$) but also \emph{strategy-dependent} (on data mixing protocol).
466	Under accumulate, canary metrics remain useful as absolute-level monitors (tracking collapse severity) but do not provide predictive lead.
467	
468	\section{Discussion}
469	
470	\subsection{An Information-Theoretic Argument for Decoupling}
471	
472	The universal canary$\to$perplexity decoupling admits an information-theoretic explanation grounded in the distinction between intrinsic and extrinsic distribution statistics.
473	
474	Let $p_\theta^{(t)}$ denote the model's output distribution at generation $t$ and $p_{\text{data}}$ the true data distribution.
475	Canary metrics are \emph{intrinsic} to $p_\theta^{(t)}$: token entropy $H(p_\theta^{(t)})$ measures the concentration of the output distribution, and ECE measures the discrepancy between $p_\theta^{(t)}$'s confidence and its accuracy.
476	Both are bounded below as the distribution's support contracts.
477	Diversity metrics (distinct-$n$) similarly measure properties of samples from $p_\theta^{(t)}$ alone.
478	
479	Perplexity, by contrast, is \emph{extrinsic}: $\text{PPL} = \exp(H(p_{\text{data}}, p_\theta^{(t)}))$ involves the cross-entropy between $p_{\text{data}}$ and $p_\theta^{(t)}$, which can grow without bound as the distributions diverge.
480	There is no theoretical requirement that changes in $H(p_\theta)$ temporally precede or predict changes in $H(p_{\text{data}}, p_\theta)$; they respond to different aspects of the distributional shift induced by iterative synthetic training.
481	
482	The extended trajectory analysis (Section~\ref{sec:extended}) provides direct empirical confirmation: entropy saturates at generation 8 while perplexity diverges through generation 20, demonstrating fundamentally different asymptotic behaviors.
483	
484	\subsection{Implications for Monitoring Practice}
485	
486	Our findings have direct implications for practitioners concerned about model collapse in production pipelines:
487	
488	\begin{enumerate}
489	    \item \textbf{Monitor both channels independently.} Tracking only canary/diversity metrics will miss quality degradation; tracking only perplexity will miss diversity loss that may occur earlier.
490	
491	    \item \textbf{Use simple tools.} Naive cross-correlation suffices for detecting canary$\to$diversity lead (94\% agreement with rigorous TY testing); complex time-series methods are unnecessary when degradation is monotonic.
492	
493	    \item \textbf{Do not expect universal canaries.} The optimal canary instrument is domain-dependent (ECE on WikiText, entropy on C4) and may not transfer across model scales without recalibration.
494	
495	    \item \textbf{Canary-triggered intervention has limited efficacy.} Short lead times ($<$2 generations) and channel specificity mean canary-based interventions cannot substitute for proactive data curation strategies.
496	\end{enumerate}
497	
498	\subsection{Limitations}
499	
500	\paragraph{Scale.} Our primary experiments use Pythia-410M, a relatively small model.
501	The 1.4B spot-check is inconclusive due to insufficient exposure within the experimental window.
502	We cannot distinguish between ``canary lead disappears at scale'' and ``the experimental window is too short to detect it at scale.''
503	
504	\paragraph{Data diversity.} We test two datasets (WikiText-103, C4).
505	Highly specialized domains (code, biomedical text) may exhibit different collapse channel structures.
506	
507	\paragraph{Generation protocol.} We use a fixed generation protocol (nucleus sampling with default parameters).
508	Different decoding strategies may modulate the diversity channel dynamics.
509	
510	\paragraph{Temporal resolution.} With at most 20 discrete generations, our time-series analysis has limited statistical power, particularly for detecting subtle lead-lag relationships at low $\alpha$.
511	
512	\section{Conclusion}
513	
514	We present the first systematic taxonomy of model collapse channels in iterative synthetic training.
515	Our central finding is that diversity collapse and quality collapse are fundamentally decoupled: canary metrics (ECE, token entropy) reliably lead diversity degradation by 1--2.5 generations but exhibit no predictive relationship with perplexity degradation at any contamination level, model scale, or data domain tested.
516	
517	This decoupling is not a methodological limitation but a structural property of collapse dynamics, grounded in the information-theoretic distinction between intrinsic distribution statistics (bounded, saturating) and cross-distribution statistics (unbounded, diverging).
518	The construct of a ``decoupling diagram''---replacing the hoped-for predictability phase diagram---provides a framework for understanding when and why early warning signals exist for specific collapse channels.
519	
520	Our methodological ablation contributes a positive result within this negative finding: simple cross-correlation is sufficient for the monotonic degradation dynamics characteristic of iterative training, freeing practitioners from the burden of complex time-series causality testing.
521	
522	These results urge the community to move beyond monolithic treatments of model collapse toward channel-specific monitoring and intervention strategies, and to invest in developing quality-channel early warning indicators---a problem our taxonomy identifies as both important and currently unsolved.
523	
524	\bibliographystyle{aaai}
525	\begin{thebibliography}{10}
526	
527	\bibitem{shumailov2024ai}
528	I.~Shumailov, Z.~Shumaylov, Y.~Zhao, N.~Papernot, R.~Anderson, and Y.~Gal.
529	\newblock {AI} models collapse when trained on recursively generated data.
530	\newblock {\em Nature}, 631:755--759, 2024.
531	
532	\bibitem{fu2024towards}
533	Z.~Fu, Z.~Wang, and Y.~Li.
534	\newblock Towards understanding the impact of model collapse on self-consuming generative models.
535	\newblock In {\em Proc.\ ICML}, 2024.
536	
537	\bibitem{dohmatob2024model}
538	E.~Dohmatob, P.~Talwar, and V.~Feldman.
539	\newblock Model collapse demystified: The case of regression.
540	\newblock {\em arXiv preprint arXiv:2402.07712}, 2024.
541	
542	\bibitem{vela2022sigma}
543	A.~Vela, S.~Mukherjee, and G.~Moreno.
544	\newblock {SIGMA}: Spectral monitoring of generative model alignment.
545	\newblock {\em arXiv preprint}, 2022.
546	
547	\bibitem{alemohammad2024selfconsuming}
548	S.~Alemohammad, J.~Casco-Rodriguez, L.~Luber, A.~G. Ahmed, and R.~Baraniuk.
549	\newblock Self-consuming generative models go {MAD}.
550	\newblock In {\em Proc.\ ICLR}, 2024.
551	
552	\bibitem{du2024synthetic}
553	Y.~Du, J.~Li, and T.~Wang.
554	\newblock Understanding the impact of synthetic data on calibration in iterative learning.
555	\newblock {\em arXiv preprint}, 2024.
556	
557	\bibitem{truong2024phase}
558	V.~Truong and L.~Truong.
559	\newblock Phase transitions and early warning signals in self-consuming language models.
560	\newblock {\em arXiv preprint}, 2024.
561	
562	\bibitem{kalinowski2024topo}
563	A.~Kalinowski, R.~Ghrist, and M.~Vejdemo-Johansson.
564	\newblock Topological complexity indices for detecting representation collapse.
565	\newblock {\em arXiv preprint}, 2024.
566	
567	\bibitem{toda1995statistical}
568	H.~Y. Toda and T.~Yamamoto.
569	\newblock Statistical inference in vector autoregressions with possibly integrated processes.
570	\newblock {\em Journal of Econometrics}, 66(1-2):225--250, 1995.
571	
572	\bibitem{li2022distinct}
573	J.~Li, M.~Galley, C.~Brockett, J.~Gao, and B.~Dolan.
574	\newblock A diversity-promoting objective function for neural conversation models.
575	\newblock In {\em Proc.\ NAACL}, 2016.
576	
577	\end{thebibliography}
578	
579	\appendix
580	\section{Supplementary Material}
581	
582	\subsection{Signal Onset Table}
583	
584	Table~\ref{tab:onset} reports the $2\sigma$ onset generation for each metric across 4 seeds under $\alpha{=}1.0$.
585	
586	\begin{table}[h]
587	\centering
588	\caption{$2\sigma$ onset generation by metric and seed ($\alpha{=}1.0$). Lead time = target onset $-$ canary onset.}
589	\label{tab:onset}
590	\small
591	\begin{tabular}{@{}lcc@{}}
592	\toprule
593	Metric & Mean onset gen & Role \\
594	\midrule
595	ECE & 1.50 & Canary \\
596	Token entropy & 1.75 & Canary \\
597	Distinct-1 & 3.00 & Target (diversity) \\
598	Distinct-2 & 3.25 & Target (diversity) \\
599	Perplexity & 2.50 & Target (quality) \\
600	\bottomrule
601	\end{tabular}
602	\end{table}
603	
604	\subsection{Accumulate vs.\ Replace Full Trajectories}
605	
606	Under the accumulate strategy at $\alpha{=}0.50$, gen-10 perplexity reaches 48.3 (vs.\ 78.3 for replace), distinct-1 reaches 0.091 (vs.\ 0.082), and entropy reaches 2.78 (vs.\ 2.45).
607	The collapse rate ratio of 0.55 confirms that accumulation slows degradation by nearly half.
608	However, the canary lead under accumulation is non-significant (0/3 seeds), demonstrating that slow, quasi-linear degradation eliminates the nonlinear response timing differences required for detectable lead-lag structure.
609	
610	\end{document}
611	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53ff8cec-5140-4c25-bfaf-8a37ae7d21da",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "3066204f-1799-4730-bab5-e9d73e750ef6",
  "sourceToolAssistantUUID": "53ff8cec-5140-4c25-bfaf-8a37ae7d21da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-14T19:29:10.656Z_

Good. I have now thoroughly read both papers. The paper I'm reviewing is the **worst** tier paper ("Taxonomy of Collapse Decoupling"). Now let me write and submit the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3066204f-1799-4730-bab5-e9d73e750ef6",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31nfjA9MBErSSYeGiga",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d94191bd-1758-43be-845a-5b6febcc865f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014gfgCey6Nv77CxRUuCd3X1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10126,
      "cache_read_input_tokens": 74290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10126,
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

_source line 68 · 2026-05-14T19:30:36.391Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01QWvhWZUBQF9VQvK86yvUz3`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "tier": "worst",
  "dream_id": "dream_20260514T184925",
  "overall_score": "3 - Weak Reject",
  "report": "# Review: \"Taxonomy of Collapse Decoupling: Diversity and Quality Degrade Through Independent Channels in Iterative Synthetic Training\"\n\n**Reviewer R1 — Focus: Methods and Experiments**\n\n---\n\n## 1. Summary\n\nThis paper investigates whether calibration-based \"canary\" metrics (ECE, token entropy) can serve as early warning signals for model collapse in iterative synthetic training. The authors find that canaries lead diversity metrics (distinct-n) by 1--2.5 generations but show no statistically significant lead over perplexity at any tested contamination ratio alpha. They frame this as a fundamental \"decoupling\" between diversity and quality collapse channels, supported by an information-theoretic argument about bounded vs. unbounded statistics. A methodological ablation shows 94% agreement between naive cross-correlation and Toda-Yamamoto testing for well-behaved pairs.\n\n---\n\n## 2. Strengths\n\n- **Systematic experimental design.** The paper covers 8 planned experiments spanning alpha-sweep, cross-domain (C4), cross-scale (1.4B), extended trajectories (20 gen), intervention, data strategy ablation, and methodological comparison. This is a commendably thorough experimental program for what is essentially an empirical study.\n\n- **Honest reporting of negative and null results.** The paper does not hide that effective_rank and self-BLEU fail as canaries, that the intervention experiment produces non-significant results, that the 1.4B spot-check is inconclusive, and that the canary ranking reverses across domains. This transparency is appreciated.\n\n- **Appropriate choice of Toda-Yamamoto testing.** The use of TY for temporal precedence in non-stationary training trajectories is methodologically sound and represents a genuine improvement over the informal visual inspection and simple correlation used in prior work (e.g., Du et al.). The paper correctly identifies that naive Pearson correlation on trending series produces spurious associations.\n\n- **The \"monitoring paradox\" finding (Section 4.8) is genuinely interesting.** The observation that accumulate strategies slow collapse but simultaneously eliminate canary predictive lead is a non-obvious result with practical implications.\n\n- **Reproducibility details are adequate.** Seeds, hyperparameters, alpha values, generation counts, and metric definitions are clearly specified. The code architecture (iterative_train.py, metrics.py, analyze_mvp.py) appears well-structured.\n\n---\n\n## 3. Weaknesses\n\n### 3.1. The central \"decoupling\" claim is not adequately distinguished from insufficient statistical power (Major)\n\nThe paper claims that canary-to-perplexity decoupling is \"universal\" and \"structural\" — that no alpha* boundary exists. However, the evidence for this strong negative claim is weak:\n\n- At alpha=0.25, the canary-to-diversity lead itself is fragile (1/3 significant seeds for ECE->d1). If the canary signal is barely detectable for diversity at low alpha, the absence of a canary-to-perplexity signal tells us almost nothing — we simply lack power.\n- With only 10 time points per series and 3 seeds, the Toda-Yamamoto test has very low statistical power. The paper acknowledges this (TY significance rate of 55% overall), but then draws strong structural conclusions from the non-significant results. A non-significant p-value does not confirm the null hypothesis; it is consistent with both no effect and a real effect that the study was underpowered to detect.\n- The paper would need a formal power analysis to support the \"universal decoupling\" claim. What effect size (in lag units) could the TY test reliably detect with N=10 and 3 seeds? If the answer is \"only lags >= 3,\" then the failure to detect a lag of 1 at low alpha is uninformative.\n\n**Suggestion:** Either (a) perform a simulation-based power analysis showing the TY test can detect lag-1 leads with N=10 at the tested alpha values, or (b) substantially weaken the \"universal/structural\" language to \"not detected in our experimental window.\"\n\n### 3.2. The information-theoretic argument (Section 5.1) is hand-wavy (Major)\n\nThe paper argues that because token entropy H(p_theta) is bounded while perplexity exp(H(p_data, p_theta)) is unbounded, there is \"no theoretical requirement\" for temporal coupling. This is not a valid argument for several reasons:\n\n- Boundedness of a statistic says nothing about its temporal dynamics. A bounded metric can still lead an unbounded one — it simply saturates eventually. The relevant question is whether early-generation changes in intrinsic statistics predict early-generation changes in cross-entropy, which the boundedness argument does not address.\n- The argument confuses asymptotic behavior (saturation vs. divergence after gen 8-12) with the temporal lead question (which concerns generations 1-5). That entropy saturates at gen 8 while perplexity continues growing is an observation about long-run dynamics, not evidence against short-run temporal precedence.\n- The claim would require a formal proof showing that for the class of distributional shifts induced by iterative training, d/dt H(p_theta) and d/dt H(p_data, p_theta) are uncorrelated. No such proof is offered.\n\n**Suggestion:** Either formalize the argument as a theorem with stated assumptions, or present it honestly as a post-hoc intuition rather than a \"mechanistic explanation.\"\n\n### 3.3. The \"best\" paper version contradicts key claims of this version (Major, meta-concern)\n\nComparing with the project's internal experimental data and the alternative (\"best\") framing of the same experiments reveals a critical issue: the \"best\" framing finds canary-to-perplexity lead IS significant at alpha <= 0.50 (p=0.018 at alpha=0.25, p=0.032 at alpha=0.50), with a phase boundary at alpha* ~0.60. The \"worst\" framing claims universal decoupling at ALL alpha. The same underlying experiment cannot support both conclusions. This discrepancy suggests the \"decoupling\" framing may be driven by analytical choices (e.g., using naive cross-correlation rather than TY panel tests, or different significance thresholds) rather than by the data itself.\n\nThe internal project memory explicitly notes: \"token_entropy->perplexity: lag=-5, 4/4 seed consistent, but p borderline (seed42 p=0.12)\" and \"plan_006 (extended 20-gen) is the decisive experiment for whether token_entropy->perplexity is real.\" This suggests the decoupling claim was adopted prematurely, before the decisive experiment was completed.\n\n### 3.4. Cross-domain and scale experiments are underpowered and overinterpreted (Moderate)\n\n- **C4 cross-domain (Section 4.5):** At alpha=0.50, only 1/3 seeds are significant for ECE->d1 on C4. The paper claims \"canary ranking reverses\" (entropy better than ECE on C4), but with 1/3 vs 2/3 significant seeds on such small samples, this difference is not statistically meaningful. Drawing domain-specific conclusions from p-values of 0.003 vs 0.006 on 3 seeds is inappropriate.\n- **Pythia-1.4B (Section 4.6):** The paper correctly flags this as \"inconclusive\" but still draws the conclusion that \"canary lead is not preserved.\" With only 1/3 significant seeds and a collapse rate ratio of 0.65 suggesting insufficient exposure, this is better described as \"uninterpretable\" rather than negative evidence for or against canary effectiveness at scale.\n\n### 3.5. The intervention experiment design is flawed (Moderate)\n\n- CRS is tested at alpha=0.75 where the canary-to-diversity lead is only ~1 generation with 2/3 significant seeds. This is the hardest regime for the intervention to work. Why not test at alpha=0.50 where the lead is stronger?\n- The intervention mechanism (reduce alpha from 0.75 to ~0.52 when triggered) conflates canary-guided timing with the known benefit of lower alpha. The right control is not \"no intervention\" but \"reduce alpha at a random/fixed generation\" to isolate the value of canary-guided timing.\n- With only 3 seeds and one seed showing CRS performing worse than baseline, the experiment is severely underpowered for detecting intervention effects.\n\n### 3.6. ECE implementation details matter but are underspecified (Minor-Moderate)\n\nThe paper mentions 15 equal-mass bins for ECE in the abstract/summary but the code (metrics.py) uses 10 equal-width bins. The choice between equal-mass and equal-width binning can substantially affect ECE values, especially as the confidence distribution shifts during collapse. Which was actually used? The discrepancy undermines reproducibility.\n\n### 3.7. The methodological ablation conclusion is misleading (Moderate)\n\nThe paper concludes that \"practitioners need not employ complex time-series methods\" because naive correlation and TY agree 94% on \"core canary\" pairs. But this 94% agreement is circular: the \"core canary\" pairs are precisely those where degradation is monotonic and strong (ECE/entropy -> distinct-1/2), where we would expect any method to agree. The 25% overturning rate on the full set (and 6 cases in Table 4 where naive wrongly claims canary->perplexity lead at high alpha) shows that naive methods systematically mislead on the scientifically interesting question of this paper — whether canaries lead perplexity.\n\n---\n\n## 4. Questions for Authors\n\n1. **Power analysis:** What is the minimum detectable lag (in generations) for the TY test at 80% power with N=10 observations and 3 seeds? If you cannot detect lags < 2, how can you claim \"no lead\" rather than \"insufficient power to detect lead\"?\n\n2. **Discrepancy with panel TY results:** The best-case framing of this same data finds significant canary->perplexity leads at alpha <= 0.50 using panel TY tests. Can you clarify what analytical choices differ between the two framings? If the TY panel test (which pools across seeds) finds significance while per-seed tests do not, this is a power issue, not a structural decoupling.\n\n3. **ECE binning:** The code uses 10 equal-width bins; the paper text references 15 equal-mass bins. Which was used in the reported experiments?\n\n4. **2-sigma onset estimation:** The onset definition uses sigma estimated from \"the first two generations.\" With only 2 data points, this variance estimate is extremely noisy. Why not use the cross-seed variance at generation 0?\n\n5. **Why was the intervention not tested at alpha=0.50** where the canary lead is strongest and the a priori probability of success is highest?\n\n6. **Accumulate ablation lead times:** The paper reports ECE->d1 lag shrinks from -1.00 to -0.33 under accumulate, with 0/3 significant seeds. Are TY p-values reported for this comparison? The 0/3 significant seeds could reflect power loss from slower dynamics rather than genuine elimination of lead structure.\n\n---\n\n## 5. Minor Issues\n\n- Table 3 (gen-10 metrics): The alpha=1.0 column shows \"---\" for all values, which is confusing. Were these measurements not taken, or was a different table structure intended?\n- The distinct-1 values at alpha=0.25 (0.088 in Table 3) vs the baseline (~0.35 for WikiText-103 generated text) represent a substantial decline, yet the paper says perplexity \"barely degrades\" at this alpha. A more nuanced discussion of what counts as \"degradation\" would strengthen the decoupling argument.\n- The bibliography has formatting inconsistencies (some entries show \"arXiv preprint\" without identifiers).\n- The SIGMA citation appears to be to a non-existent or very obscure paper (arXiv 2601.03385 would be from January 2026). Please verify.\n- The abstract mentions \"canary metrics lead diversity degradation by 1--2.5 generations\" but at alpha=0.25 the lag is only 0.67 with 1/3 significant seeds — this should not be presented as establishing a 2.5-generation lead.\n- Section 4.8 describes the monitoring paradox as an insight but does not discuss whether this is simply an artifact of reduced statistical power under gentler dynamics (same concern as the main decoupling claim).\n\n---\n\n## 6. Scores\n\n| Criterion | Score | Rationale |\n|-----------|-------|-----------|\n| **Soundness** | 2/4 | The central \"universal decoupling\" claim conflates non-significance with evidence for the null. The information-theoretic argument is informal and does not support the structural claims made. |\n| **Empirical Methodology** | 2/4 | Comprehensive experimental program, but severely underpowered for the negative claims being made. 3 seeds x 10 time points is insufficient for strong negative conclusions about temporal precedence. The intervention experiment lacks proper controls. |\n| **Reproducibility** | 3/4 | Code is provided and well-structured. Hyperparameters are specified. ECE binning discrepancy is a concern. Seed counts and configurations are clear. |\n| **Overall Score** | 3/6 (Weak Reject) | The paper addresses an interesting and practically relevant question with a commendably thorough experimental program. However, the central contribution — the claim of \"universal structural decoupling\" between diversity and quality collapse — is not adequately supported. The evidence is more consistent with insufficient statistical power to detect canary-to-perplexity leads, particularly at low alpha where even canary-to-diversity leads are barely significant. The information-theoretic argument does not provide the theoretical grounding needed to elevate this from an empirical non-finding to a structural insight. With a weaker framing (e.g., \"canary-to-perplexity lead is harder to detect and may require longer horizons\") and a power analysis, the paper could be substantially strengthened. In its current form, the strong negative claims are not justified by the evidence presented. |\n| **Confidence** | 4/5 | I have carefully examined the experimental design, code, statistical methods, and internal project documentation. The power concern is well-grounded in time-series statistics. My main uncertainty is whether the TY panel test (pooling across seeds) might yield different conclusions from the per-seed analysis reported here. |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d94191bd-1758-43be-845a-5b6febcc865f",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31nfjA9MBErSSYeGiga",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c34606d7-d283-4525-b7df-1bf4134c9d03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014gfgCey6Nv77CxRUuCd3X1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10126,
      "cache_read_input_tokens": 74290,
      "output_tokens": 3618,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10126
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3618,
          "cache_read_input_tokens": 74290,
          "cache_creation_input_tokens": 10126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10126,
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

_source line 69 · 2026-05-14T19:30:37.069Z_

<details><summary>↩ Tool result · `toolu_01QWvhWZUBQF9VQvK86yvUz3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/worst/review_report.md\", \"dream_id\": \"dream_20260514T184925\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c34606d7-d283-4525-b7df-1bf4134c9d03",
  "isSidechain": true,
  "promptId": "99b3e69d-6274-4f12-a80c-136c23933911",
  "agentId": "a7b91bbe8bfcb2d20",
  "type": "user",
  "uuid": "ee16a359-eb58-4f61-85f8-fe7ae79b2d42",
  "sourceToolAssistantUUID": "c34606d7-d283-4525-b7df-1bf4134c9d03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 70 · 2026-05-14T19:30:48.251Z_

Review submitted. Here is a summary of the key findings:

**Overall: 3/6 (Weak Reject)**

The paper presents a thorough empirical study of canary metrics for model collapse, but the central "universal structural decoupling" claim -- that diversity and quality collapse are fundamentally independent channels with no predictive relationship at any contamination level -- is not adequately supported. The three major issues:

1. **Power vs. structure confusion.** With only 10 time points and 3 seeds, the TY test lacks power to detect subtle leads. Non-significance does not confirm the null. At alpha=0.25, even the canary-to-diversity lead is barely significant (1/3 seeds), so the absence of canary-to-perplexity signal is uninformative. The alternative framing of the same data (best-tier paper) finds significant canary-to-perplexity leads at alpha <= 0.50 using panel TY tests, suggesting this is a power issue, not structural decoupling.

2. **The information-theoretic argument is informal.** Bounded vs. unbounded asymptotic behavior says nothing about temporal dynamics in early generations. No formal proof is offered.

3. **Underpowered auxiliary experiments.** The intervention lacks proper controls (random-timing baseline), the scale check is uninterpretable, and the cross-domain canary ranking reversal is not statistically meaningful with 3 seeds.

Strengths include honest negative result reporting, good experimental coverage, appropriate use of TY testing, and the genuinely interesting "monitoring paradox" finding. The paper could be substantially improved by replacing "universal structural decoupling" with a more measured framing and adding a power analysis.

Review saved to: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/worst/review_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee16a359-eb58-4f61-85f8-fe7ae79b2d42",
  "isSidechain": true,
  "agentId": "a7b91bbe8bfcb2d20",
  "requestId": "req_011Cb31uR6XrLCgg8Qyg1V4j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4783606c-b73b-4c47-bf05-431484ec8801",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "94fcddd3-8b83-4721-94fe-5ba1b028b20f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1tFtqL6rTwwbcw5DvkvpV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3746,
      "cache_read_input_tokens": 84416,
      "output_tokens": 446,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3746
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 446,
          "cache_read_input_tokens": 84416,
          "cache_creation_input_tokens": 3746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3746,
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
