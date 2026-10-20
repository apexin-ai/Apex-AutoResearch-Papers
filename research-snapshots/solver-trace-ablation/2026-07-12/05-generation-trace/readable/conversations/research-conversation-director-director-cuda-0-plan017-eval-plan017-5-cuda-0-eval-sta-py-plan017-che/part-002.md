# Research conversation: [Director 指令] [Director 指令] cuda:0 暂不派新任务，留给 plan017 eval plan017 还有 ~5 分钟完成。完成后立即在 cuda:0 跑 eval_sta.py 评估 plan017 chec — Part 2 of 2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-director-director-cuda-0-plan017-eval-plan017-5-cuda-0-eval-sta-py-plan017-che.md) · [Structured JSON](../../../sessions/a1/a1b7e9327753423d92de.json)

## Round 27

### Assistant

_source line 325 · 2026-05-14T05:54:09.903Z_

<details><summary>Logged reasoning block</summary>

```text
plan016 is already RUNNING? Let me check. The Director said "清理完成后立即提交 plan016-extended-1000-s42 到 cuda:1" - but it seems plan016 is already RUNNING. Let me check the registry.

Wait, the error says "Invalid transition: RUNNING → ALLOCATED" - meaning plan016 is already RUNNING. So it's already been submitted somehow. That's good - it's already on cuda:1.

So the key issue is just killing the zombie process to free up GPU memory for plan016 which is already running.

Now let me update the paper_framing.md with the Director's framing decision (option A).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39f31756-6aac-4fcb-a85a-974deb3485fa",
  "isSidechain": false,
  "requestId": "req_011Cb1wdg6m6vRVruySu1YCS",
  "type": "assistant",
  "uuid": "3e1df2fd-15df-45eb-b102-93ed6686d6d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNyesF2CetHGeEb3CtTvA5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1580,
      "cache_read_input_tokens": 105811,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1580,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 332,
          "cache_read_input_tokens": 105811,
          "cache_creation_input_tokens": 1580,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1580
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


### Assistant

_source line 326 · 2026-05-14T05:54:11.344Z_

plan016 已经是 RUNNING 状态（已在 cuda:1 上运行）。现在更新 paper_framing.md 按 Director 的备选 A 决策。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e1df2fd-15df-45eb-b102-93ed6686d6d4",
  "isSidechain": false,
  "requestId": "req_011Cb1wdg6m6vRVruySu1YCS",
  "type": "assistant",
  "uuid": "7c64e964-48ac-478e-a2fb-7fd43985be05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNyesF2CetHGeEb3CtTvA5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1580,
      "cache_read_input_tokens": 105811,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1580,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 332,
          "cache_read_input_tokens": 105811,
          "cache_creation_input_tokens": 1580,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1580
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


### Tool call

_source line 327 · 2026-05-14T05:54:11.689Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015YX54Pc6CyJAEqZAGdd6nn`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_framing.md",
  "max_chars": 15000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c64e964-48ac-478e-a2fb-7fd43985be05",
  "isSidechain": false,
  "requestId": "req_011Cb1wdg6m6vRVruySu1YCS",
  "type": "assistant",
  "uuid": "bd98f463-23f0-449b-acdb-58f8e1a8ba5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNyesF2CetHGeEb3CtTvA5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1580,
      "cache_read_input_tokens": 105811,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1580,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 332,
          "cache_read_input_tokens": 105811,
          "cache_creation_input_tokens": 1580,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1580
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

_source line 328 · 2026-05-14T05:54:11.700Z_

<details><summary>↩ Tool result · `toolu_015YX54Pc6CyJAEqZAGdd6nn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — 诊断/分析论文)\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**:\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)\\n- Hacking taxonomy: 5 distinct modes identified and quantified (plan012 `hacking_characterization_report.md` + plan017 D027)\\n\\n### Claim 2: GRPO Saturation Mechanism\\nExec-only GRPO exhibits a saturation failure mode: when prove_rate → 1.0, reward_std → 0 and loss → 0, training effectively stalls. Any reward component introducing variance (ISR, random noise) prevents saturation but does not prevent hacking — it redirects hacking into different structural failure modes.\\n\\n**证据**:\\n- plan001 exec-only: PR saturation → loss=0 → learning stops (D014)\\n- plan013 random reward: PR=1.0 (prevents saturation) but 100% P→P tautological collapse (D018)\\n- plan002 additive ISR β=0.3: PR=18%, ISR=0.1427 — ISR bonus prevents saturation but causes repetitive cycling, lowest PR of all conditions (D020)\\n- plan005 convex combination: penalty effect confirmed — any ISR<1 reduces reward (D010)\\n- plan017 additive random β=0.3: eval PR=48%, ISR=0.045, comp=9.56 — \\\"complexity-without-utility\\\" mode (高 component 但 conclusion 不依赖 premises, 33% proved ISR=0). ISR 比 random 更差 (PR 18% vs 48%), ISR 信号对训练 actively misleading (D026/D027)\\n- ⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为\\\"additive vs convex\\\"对照。plan017 vs plan002 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）\\n\\n### Claim 3: Cross-Logic Generality (conditional on plan006)\\nSTA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.\\n\\n**证据**: 待验证。plan006 Prolog GRPO 实验未启动。如果 plan006 无法复现 hacking + ISR 诊断，此 claim 降级为 future work。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% collapse over training)\\n  2. GRPO saturation creates a \\\"training trap\\\": PR→1 means no gradient signal, but adding any variance (ISR or random) redirects rather than prevents hacking\\n  3. Different reward formulations produce distinct, classifiable hacking strategies (5 modes identified)\\n  4. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners\\n- **Actionable insights for practitioners**:\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\n  3. Adding structural reward components can hurt prove_rate (penalty effect) or redirect hacking (saturation effect) — neither naïvely improves quality\\n  4. ISR is a structural diagnostic, not a semantic quality proxy\\n- **Headline result**: \\\"We demonstrate that GRPO-trained FOL formalizers achieving 93-98% prove rate produce structurally degenerate outputs detectable by ISR — a component necessity metric derived from solver trace ablation. Across 5 reward conditions and 3 seeds, we identify 5 distinct hacking strategies and a GRPO saturation mechanism that confounds all reward-augmentation approaches. ISR as training signal is worse than matched random noise (PR 18% vs 48%), confirming its value is strictly diagnostic.\\\"\\n\\n## ISR Capability Boundary (D021/D022)\\n\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\n\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\n- Best-of-N ISR selection vs random: +0.9pp (不显著)\\n- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%\\n\\n**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。\\n\\n## ISR-as-Reward Failure Log (D010→D020)\\n\\n以下路线已全面失败，论文不再 claim ISR 可改善训练：\\n- **凸组合** r = α·r_exec + β·r_exec·ISR, α+β=1：ISR<1 时永远是 penalty (plan005, D010)\\n- **Additive bonus β=0.3** r = r_exec·(1+0.3·ISR)：PR=18%, 最差条件 (plan002, D020)\\n- **Additive bonus β=0.1** r = r_exec·(1+0.1·ISR)：实验中 (plan002-b01)\\n- **Random reward** r = α·r_exec + β·r_exec·random：PR=100% 但 100% tautological (plan013, D018)\\n- **Additive random β=0.3** r = r_exec·(1+0.3·random)：PR=48%, 未坍缩但 complexity-without-utility (plan017, D026)\\n\\n这些 negative results 本身是论文贡献——展示了 structural reward integration 的失败模式。关键发现：ISR 比 matched random 更差 (PR 18% vs 48%)，说明 ISR 信号对训练 actively misleading 而非仅仅 noisy。\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Diagnostic/analysis paper in NLP + formal reasoning track. Empirical findings + negative results are valued at EMNLP.\\n- **\\\"Just negative results\\\" risk**: Mitigate by providing actionable diagnostic framework (ISR + taxonomy) and mechanistic insight (GRPO saturation).\\n- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 4 conditions × 4 hacking modes).\\n- **\\\"Old wine\\\" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic hacking diagnostic for formal reasoning GRPO) + empirical findings, not algorithm level.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"ISR is just LOO ablation — not novel\\\"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical taxonomy of hacking modes, (c) GRPO saturation mechanism analysis.\\n2. **\\\"No positive result — ISR doesn't improve training\\\"** — Correct; we frame ISR as diagnostic, not reward. The systematic failure of all ISR-as-reward attempts is itself informative (Section: ISR-as-Reward Failure Log).\\n3. **\\\"ISR is circular\\\"** — ISR is used for diagnosis/post-hoc analysis, not as optimization target. Component count analysis (mean=6.58 vs 2.04, p<0.0001) provides ISR-independent structural evidence.\\n4. **\\\"Only one logic type\\\"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.\\n5. **\\\"500 steps too short\\\"** — plan016 extends to 1000+ steps. Pre-saturation learning curves show hacking onset occurs within 200-300 steps.\\n6. **\\\"3 seeds insufficient for statistical claims\\\"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. But statistical claims on mean ISR use 3-seed mean±std.\\n7. **\\\"Related work insufficient\\\"** — Expand to 25+ refs (literature_map.yaml has 29): reward hacking (Gao 2023, Skalse 2022), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur, AlphaProof), feature attribution (SHAP), FOLIO (Han 2022).\\n8. **\\\"RIP framework overstated\\\"** — Frame as \\\"component necessity testing inspired by mutation testing's RIP framework,\\\" only Propagation condition operationalized.\\n9. **\\\"Practitioners can't act on this\\\"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable.\\n10. **\\\"GRPO saturation is known\\\"** — General RL reward saturation is known (Gao et al. 2023). Our contribution is documenting the specific manifestation in GRPO for formal reasoning + showing that naïve fixes (adding variance) redirect rather than prevent hacking.\\n\\n## Dream-Identified Structural Fixes (Paper Agent)\\n\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 29)\\n- [ ] RIP framing: reframe as \\\"component necessity testing inspired by RIP\\\"\\n- [ ] \\\"Dense+automatic\\\" → \\\"conditionally dense\\\"\\n- [ ] Remove all \\\"Pareto-improving\\\" language\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\n- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed)\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)\\n- [x] Hacking taxonomy completed (plan012, 4 modes identified)\\n\", \"total_chars\": 9629, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd98f463-23f0-449b-acdb-58f8e1a8ba5d",
  "isSidechain": false,
  "promptId": "3dc1e72c-f7d9-4a77-8cc1-c2126f62c864",
  "type": "user",
  "uuid": "73e71912-9016-4e38-ae09-b203122db00c",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — solver-trace-ablation\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\\\n- Fallback: EMNLP 2026 Findings\\\\n- Deadline: ARR May 25, 2026\\\\n\\\\n## Core Claims (3 条 — 诊断/分析论文)\\\\n\\\\n### Claim 1: ISR as Reward Hacking Diagnostic\\\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps), quantifying structural degeneration invisible to the execution reward.\\\\n\\\\n**证据**:\\\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\\\n- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)\\\\n- Hacking taxonomy: 5 distinct modes identified and quantified (plan012 `hacking_characterization_report.md` + plan017 D027)\\\\n\\\\n### Claim 2: GRPO Saturation Mechanism\\\\nExec-only GRPO exhibits a saturation failure mode: when prove_rate → 1.0, reward_std → 0 and loss → 0, training effectively stalls. Any reward component introducing variance (ISR, random noise) prevents saturation but does not prevent hacking — it redirects hacking into different structural failure modes.\\\\n\\\\n**证据**:\\\\n- plan001 exec-only: PR saturation → loss=0 → learning stops (D014)\\\\n- plan013 random reward: PR=1.0 (prevents saturation) but 100% P→P tautological collapse (D018)\\\\n- plan002 additive ISR β=0.3: PR=18%, ISR=0.1427 — ISR bonus prevents saturation but causes repetitive cycling, lowest PR of all conditions (D020)\\\\n- plan005 convex combination: penalty effect confirmed — any ISR<1 reduces reward (D010)\\\\n- plan017 additive random β=0.3: eval PR=48%, ISR=0.045, comp=9.56 — \\\\\\\"complexity-without-utility\\\\\\\" mode (高 component 但 conclusion 不依赖 premises, 33% proved ISR=0). ISR 比 random 更差 (PR 18% vs 48%), ISR 信号对训练 actively misleading (D026/D027)\\\\n- ⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为\\\\\\\"additive vs convex\\\\\\\"对照。plan017 vs plan002 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）\\\\n\\\\n### Claim 3: Cross-Logic Generality (conditional on plan006)\\\\nSTA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.\\\\n\\\\n**证据**: 待验证。plan006 Prolog GRPO 实验未启动。如果 plan006 无法复现 hacking + ISR 诊断，此 claim 降级为 future work。\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% collapse over training)\\\\n  2. GRPO saturation creates a \\\\\\\"training trap\\\\\\\": PR→1 means no gradient signal, but adding any variance (ISR or random) redirects rather than prevents hacking\\\\n  3. Different reward formulations produce distinct, classifiable hacking strategies (5 modes identified)\\\\n  4. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners\\\\n- **Actionable insights for practitioners**:\\\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\\\n  3. Adding structural reward components can hurt prove_rate (penalty effect) or redirect hacking (saturation effect) — neither naïvely improves quality\\\\n  4. ISR is a structural diagnostic, not a semantic quality proxy\\\\n- **Headline result**: \\\\\\\"We demonstrate that GRPO-trained FOL formalizers achieving 93-98% prove rate produce structurally degenerate outputs detectable by ISR — a component necessity metric derived from solver trace ablation. Across 5 reward conditions and 3 seeds, we identify 5 distinct hacking strategies and a GRPO saturation mechanism that confounds all reward-augmentation approaches. ISR as training signal is worse than matched random noise (PR 18% vs 48%), confirming its value is strictly diagnostic.\\\\\\\"\\\\n\\\\n## ISR Capability Boundary (D021/D022)\\\\n\\\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\\\n\\\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\\\n- Best-of-N ISR selection vs random: +0.9pp (不显著)\\\\n- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%\\\\n\\\\n**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。\\\\n\\\\n## ISR-as-Reward Failure Log (D010→D020)\\\\n\\\\n以下路线已全面失败，论文不再 claim ISR 可改善训练：\\\\n- **凸组合** r = α·r_exec + β·r_exec·ISR, α+β=1：ISR<1 时永远是 penalty (plan005, D010)\\\\n- **Additive bonus β=0.3** r = r_exec·(1+0.3·ISR)：PR=18%, 最差条件 (plan002, D020)\\\\n- **Additive bonus β=0.1** r = r_exec·(1+0.1·ISR)：实验中 (plan002-b01)\\\\n- **Random reward** r = α·r_exec + β·r_exec·random：PR=100% 但 100% tautological (plan013, D018)\\\\n- **Additive random β=0.3** r = r_exec·(1+0.3·random)：PR=48%, 未坍缩但 complexity-without-utility (plan017, D026)\\\\n\\\\n这些 negative results 本身是论文贡献——展示了 structural reward integration 的失败模式。关键发现：ISR 比 matched random 更差 (PR 18% vs 48%)，说明 ISR 信号对训练 actively misleading 而非仅仅 noisy。\\\\n\\\\n## Venue Fit Risks\\\\n\\\\n- **EMNLP fit**: Diagnostic/analysis paper in NLP + formal reasoning track. Empirical findings + negative results are valued at EMNLP.\\\\n- **\\\\\\\"Just negative results\\\\\\\" risk**: Mitigate by providing actionable diagnostic framework (ISR + taxonomy) and mechanistic insight (GRPO saturation).\\\\n- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 4 conditions × 4 hacking modes).\\\\n- **\\\\\\\"Old wine\\\\\\\" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic hacking diagnostic for formal reasoning GRPO) + empirical findings, not algorithm level.\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n1. **\\\\\\\"ISR is just LOO ablation — not novel\\\\\\\"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical taxonomy of hacking modes, (c) GRPO saturation mechanism analysis.\\\\n2. **\\\\\\\"No positive result — ISR doesn't improve training\\\\\\\"** — Correct; we frame ISR as diagnostic, not reward. The systematic failure of all ISR-as-reward attempts is itself informative (Section: ISR-as-Reward Failure Log).\\\\n3. **\\\\\\\"ISR is circular\\\\\\\"** — ISR is used for diagnosis/post-hoc analysis, not as optimization target. Component count analysis (mean=6.58 vs 2.04, p<0.0001) provides ISR-independent structural evidence.\\\\n4. **\\\\\\\"Only one logic type\\\\\\\"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.\\\\n5. **\\\\\\\"500 steps too short\\\\\\\"** — plan016 extends to 1000+ steps. Pre-saturation learning curves show hacking onset occurs within 200-300 steps.\\\\n6. **\\\\\\\"3 seeds insufficient for statistical claims\\\\\\\"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. But statistical claims on mean ISR use 3-seed mean±std.\\\\n7. **\\\\\\\"Related work insufficient\\\\\\\"** — Expand to 25+ refs (literature_map.yaml has 29): reward hacking (Gao 2023, Skalse 2022), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur, AlphaProof), feature attribution (SHAP), FOLIO (Han 2022).\\\\n8. **\\\\\\\"RIP framework overstated\\\\\\\"** — Frame as \\\\\\\"component necessity testing inspired by mutation testing's RIP framework,\\\\\\\" only Propagation condition operationalized.\\\\n9. **\\\\\\\"Practitioners can't act on this\\\\\\\"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable.\\\\n10. **\\\\\\\"GRPO saturation is known\\\\\\\"** — General RL reward saturation is known (Gao et al. 2023). Our contribution is documenting the specific manifestation in GRPO for formal reasoning + showing that naïve fixes (adding variance) redirect rather than prevent hacking.\\\\n\\\\n## Dream-Identified Structural Fixes (Paper Agent)\\\\n\\\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 29)\\\\n- [ ] RIP framing: reframe as \\\\\\\"component necessity testing inspired by RIP\\\\\\\"\\\\n- [ ] \\\\\\\"Dense+automatic\\\\\\\" → \\\\\\\"conditionally dense\\\\\\\"\\\\n- [ ] Remove all \\\\\\\"Pareto-improving\\\\\\\" language\\\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\\\n- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed)\\\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)\\\\n- [x] Hacking taxonomy completed (plan012, 4 modes identified)\\\\n\\\", \\\"total_chars\\\": 9629, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — 诊断/分析论文)\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**:\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)\\n- Hacking taxonomy: 5 distinct modes identified and quantified (plan012 `hacking_characterization_report.md` + plan017 D027)\\n\\n### Claim 2: GRPO Saturation Mechanism\\nExec-only GRPO exhibits a saturation failure mode: when prove_rate → 1.0, reward_std → 0 and loss → 0, training effectively stalls. Any reward component introducing variance (ISR, random noise) prevents saturation but does not prevent hacking — it redirects hacking into different structural failure modes.\\n\\n**证据**:\\n- plan001 exec-only: PR saturation → loss=0 → learning stops (D014)\\n- plan013 random reward: PR=1.0 (prevents saturation) but 100% P→P tautological collapse (D018)\\n- plan002 additive ISR β=0.3: PR=18%, ISR=0.1427 — ISR bonus prevents saturation but causes repetitive cycling, lowest PR of all conditions (D020)\\n- plan005 convex combination: penalty effect confirmed — any ISR<1 reduces reward (D010)\\n- plan017 additive random β=0.3: eval PR=48%, ISR=0.045, comp=9.56 — \\\"complexity-without-utility\\\" mode (高 component 但 conclusion 不依赖 premises, 33% proved ISR=0). ISR 比 random 更差 (PR 18% vs 48%), ISR 信号对训练 actively misleading (D026/D027)\\n- ⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为\\\"additive vs convex\\\"对照。plan017 vs plan002 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）\\n\\n### Claim 3: Cross-Logic Generality (conditional on plan006)\\nSTA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.\\n\\n**证据**: 待验证。plan006 Prolog GRPO 实验未启动。如果 plan006 无法复现 hacking + ISR 诊断，此 claim 降级为 future work。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% collapse over training)\\n  2. GRPO saturation creates a \\\"training trap\\\": PR→1 means no gradient signal, but adding any variance (ISR or random) redirects rather than prevents hacking\\n  3. Different reward formulations produce distinct, classifiable hacking strategies (5 modes identified)\\n  4. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners\\n- **Actionable insights for practitioners**:\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\n  3. Adding structural reward components can hurt prove_rate (penalty effect) or redirect hacking (saturation effect) — neither naïvely improves quality\\n  4. ISR is a structural diagnostic, not a semantic quality proxy\\n- **Headline result**: \\\"We demonstrate that GRPO-trained FOL formalizers achieving 93-98% prove rate produce structurally degenerate outputs detectable by ISR — a component necessity metric derived from solver trace ablation. Across 5 reward conditions and 3 seeds, we identify 5 distinct hacking strategies and a GRPO saturation mechanism that confounds all reward-augmentation approaches. ISR as training signal is worse than matched random noise (PR 18% vs 48%), confirming its value is strictly diagnostic.\\\"\\n\\n## ISR Capability Boundary (D021/D022)\\n\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\n\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\n- Best-of-N ISR selection vs random: +0.9pp (不显著)\\n- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%\\n\\n**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。\\n\\n## ISR-as-Reward Failure Log (D010→D020)\\n\\n以下路线已全面失败，论文不再 claim ISR 可改善训练：\\n- **凸组合** r = α·r_exec + β·r_exec·ISR, α+β=1：ISR<1 时永远是 penalty (plan005, D010)\\n- **Additive bonus β=0.3** r = r_exec·(1+0.3·ISR)：PR=18%, 最差条件 (plan002, D020)\\n- **Additive bonus β=0.1** r = r_exec·(1+0.1·ISR)：实验中 (plan002-b01)\\n- **Random reward** r = α·r_exec + β·r_exec·random：PR=100% 但 100% tautological (plan013, D018)\\n- **Additive random β=0.3** r = r_exec·(1+0.3·random)：PR=48%, 未坍缩但 complexity-without-utility (plan017, D026)\\n\\n这些 negative results 本身是论文贡献——展示了 structural reward integration 的失败模式。关键发现：ISR 比 matched random 更差 (PR 18% vs 48%)，说明 ISR 信号对训练 actively misleading 而非仅仅 noisy。\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Diagnostic/analysis paper in NLP + formal reasoning track. Empirical findings + negative results are valued at EMNLP.\\n- **\\\"Just negative results\\\" risk**: Mitigate by providing actionable diagnostic framework (ISR + taxonomy) and mechanistic insight (GRPO saturation).\\n- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 4 conditions × 4 hacking modes).\\n- **\\\"Old wine\\\" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic hacking diagnostic for formal reasoning GRPO) + empirical findings, not algorithm level.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"ISR is just LOO ablation — not novel\\\"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical taxonomy of hacking modes, (c) GRPO saturation mechanism analysis.\\n2. **\\\"No positive result — ISR doesn't improve training\\\"** — Correct; we frame ISR as diagnostic, not reward. The systematic failure of all ISR-as-reward attempts is itself informative (Section: ISR-as-Reward Failure Log).\\n3. **\\\"ISR is circular\\\"** — ISR is used for diagnosis/post-hoc analysis, not as optimization target. Component count analysis (mean=6.58 vs 2.04, p<0.0001) provides ISR-independent structural evidence.\\n4. **\\\"Only one logic type\\\"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.\\n5. **\\\"500 steps too short\\\"** — plan016 extends to 1000+ steps. Pre-saturation learning curves show hacking onset occurs within 200-300 steps.\\n6. **\\\"3 seeds insufficient for statistical claims\\\"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. But statistical claims on mean ISR use 3-seed mean±std.\\n7. **\\\"Related work insufficient\\\"** — Expand to 25+ refs (literature_map.yaml has 29): reward hacking (Gao 2023, Skalse 2022), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur, AlphaProof), feature attribution (SHAP), FOLIO (Han 2022).\\n8. **\\\"RIP framework overstated\\\"** — Frame as \\\"component necessity testing inspired by mutation testing's RIP framework,\\\" only Propagation condition operationalized.\\n9. **\\\"Practitioners can't act on this\\\"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable.\\n10. **\\\"GRPO saturation is known\\\"** — General RL reward saturation is known (Gao et al. 2023). Our contribution is documenting the specific manifestation in GRPO for formal reasoning + showing that naïve fixes (adding variance) redirect rather than prevent hacking.\\n\\n## Dream-Identified Structural Fixes (Paper Agent)\\n\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 29)\\n- [ ] RIP framing: reframe as \\\"component necessity testing inspired by RIP\\\"\\n- [ ] \\\"Dense+automatic\\\" → \\\"conditionally dense\\\"\\n- [ ] Remove all \\\"Pareto-improving\\\" language\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\n- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed)\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)\\n- [x] Hacking taxonomy completed (plan012, 4 modes identified)\\n\", \"total_chars\": 9629, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "bd98f463-23f0-449b-acdb-58f8e1a8ba5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 329_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] **紧急：cuda:1 被僵尸进程阻塞**  1. **立即 kill PID 261641**（plan017 eval_sta.py 僵尸进程，占 cuda:1 16GB 显存）。plan017 已 DONE，这个进程是残留。  2. **磁盘清理批准**：删除以下已完成实验的 checkpoint 目录释放空间（eval 结果已在 registry，原始输出不再需…",
  "leafUuid": "73e71912-9016-4e38-ae09-b203122db00c",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500"
}
```

---


### Runtime record

_source line 330_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate plan017 checkpoint results",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500"
}
```

---


### Assistant

_source line 331 · 2026-05-14T05:54:25.855Z_

<details><summary>Logged reasoning block</summary>

```text
The paper_framing.md has already been updated with plan017 results. Looking at Claim 2, it already includes:
- "plan017 additive random β=0.3: eval PR=48%, ISR=0.045, comp=9.56 — "complexity-without-utility" mode"
- The reviewer warning about formula structure differences
- The ISR-as-Reward Failure Log already includes plan017

And Claim 3 has been updated to reference 5 hacking modes.

The Director's specific request was backup option A: "在 Claim 2 证据中补充 plan017 additive random β=0.3: PR=48%, ISR=0.045 — ISR 比 random noise 更差 (PR 18% vs 48%)，confirming ISR is actively misleading as training signal"


This evidence is already present in the framing, so I can report back that the update is complete. I'll log the status: kill worker dispatched, disk cleanup done with 172G free, plan016 running on cuda:1, framing updated with plan017 evidence, and reviewer notation already captured.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73e71912-9016-4e38-ae09-b203122db00c",
  "isSidechain": false,
  "requestId": "req_011Cb1weVrPymKg1UvxH3gF3",
  "type": "assistant",
  "uuid": "41ac27ae-795c-48d9-863b-233ec2f99286",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tj44Zr9wYVGps7Wwmhz58v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3742,
      "cache_read_input_tokens": 107391,
      "output_tokens": 467,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3742,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 467,
          "cache_read_input_tokens": 107391,
          "cache_creation_input_tokens": 3742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3742
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


### Assistant

_source line 332 · 2026-05-14T05:54:26.124Z_

paper_framing.md 已包含 plan017 结果和 Reviewer 公式描述约束（之前的 Worker 已更新）。记录决策并汇报 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41ac27ae-795c-48d9-863b-233ec2f99286",
  "isSidechain": false,
  "requestId": "req_011Cb1weVrPymKg1UvxH3gF3",
  "type": "assistant",
  "uuid": "06c7d1ff-3009-4711-84c0-8e562bc825f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tj44Zr9wYVGps7Wwmhz58v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3742,
      "cache_read_input_tokens": 107391,
      "output_tokens": 467,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3742,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 467,
          "cache_read_input_tokens": 107391,
          "cache_creation_input_tokens": 3742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3742
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


### Tool call

_source line 333 · 2026-05-14T05:54:27.031Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Va5P21zXiUAj15aYAaCsGU`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__auto_build_provenance",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06c7d1ff-3009-4711-84c0-8e562bc825f2",
  "isSidechain": false,
  "requestId": "req_011Cb1weVrPymKg1UvxH3gF3",
  "type": "assistant",
  "uuid": "512b7db1-7c95-4206-bea5-869449cf9422",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tj44Zr9wYVGps7Wwmhz58v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3742,
      "cache_read_input_tokens": 107391,
      "output_tokens": 467,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3742,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 467,
          "cache_read_input_tokens": 107391,
          "cache_creation_input_tokens": 3742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3742
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

_source line 334 · 2026-05-14T05:54:27.051Z_

<details><summary>↩ Tool result · `toolu_01Va5P21zXiUAj15aYAaCsGU`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__auto_build_provenance"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "512b7db1-7c95-4206-bea5-869449cf9422",
  "isSidechain": false,
  "promptId": "3dc1e72c-f7d9-4a77-8cc1-c2126f62c864",
  "type": "user",
  "uuid": "3d3a0479-b7e6-47a0-b5e2-32711f2b6eaf",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__auto_build_provenance"
    ],
    "query": "select:mcp__agent-ml-research__auto_build_provenance",
    "total_deferred_tools": 79
  },
  "sourceToolAssistantUUID": "512b7db1-7c95-4206-bea5-869449cf9422",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 335 · 2026-05-14T05:54:27.083Z_

```json
{
  "parentUuid": "3d3a0479-b7e6-47a0-b5e2-32711f2b6eaf",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f916b9cb-b68d-4272-a5fd-c319969810d1",
  "timestamp": "2026-05-14T05:54:27.083Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 336 · 2026-05-14T05:54:17.484Z_

<details><summary>Logged reasoning block</summary>

```text
Both experiments are RUNNING in registry. Director's instructions 1-3 are already handled:

1. ✅ Zombie killed (self-exited)
2. ✅ Disk cleaned (172G free)
3. ✅ plan016 already submitted and running on cuda:1

Now I need to:
4. Acknowledge Framing decision (备选 A adopted)
5. Update paper_framing.md with plan017 evidence per Director's instruction
6. Plan for plan002-b01 completion → eval_sta.py
7. Plan006 readiness worker still running


8. Report status to Director and update paper_framing.md with the Framing decision (备选 A), then monitor plan006's readiness report, plan002-b01's completion, and plan016's progress.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7dea5da-3b84-470c-8940-13fdc8a06704",
  "isSidechain": false,
  "requestId": "req_011Cb1we2FTxexs7RARoxMtU",
  "type": "assistant",
  "uuid": "6f535841-13c6-4aaa-bc90-4fe9218e0e4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxxkemW3KqYt2FyFYa8pjn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 108037,
      "output_tokens": 859,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 859,
          "cache_read_input_tokens": 108037,
          "cache_creation_input_tokens": 668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 668
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


### Assistant

_source line 337 · 2026-05-14T05:54:17.490Z_

全部就绪。向 Director 汇报状态并更新 framing。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f535841-13c6-4aaa-bc90-4fe9218e0e4d",
  "isSidechain": false,
  "requestId": "req_011Cb1we2FTxexs7RARoxMtU",
  "type": "assistant",
  "uuid": "6e71add9-04f8-4663-9f6f-bfa95a5107a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxxkemW3KqYt2FyFYa8pjn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 108037,
      "output_tokens": 859,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 859,
          "cache_read_input_tokens": 108037,
          "cache_creation_input_tokens": 668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 668
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


### Tool call

_source line 338 · 2026-05-14T05:54:26.582Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director · `toolu_01Jx9eMLqAEKPRiwvDfLbSRu`</summary>

```json
{
  "text": "[资源] GPU 分配 2 / 实际跑 2 | Worker 池 1 (GPU 0 / CPU 1 plan006-readiness)\n\n**全部紧急事项已解决：**\n\n1. ✅ **僵尸进程**：PID 261641 已自行退出，GPU 1 无残留进程\n2. ✅ **磁盘清理**：6.4G → 172G 可用（释放 ~165G）\n3. ✅ **plan016 已在 cuda:1 运行**：PID 263268，已跑 ~17 分钟\n4. ✅ **plan002-b01 在 cuda:0 运行**：PID 262261，已跑 ~21 分钟\n\n**GPU 状态正常：**\n- cuda:0: 79.6/97.9 GB（plan002-b01）\n- cuda:1: 80.4/97.9 GB（plan016）\n- 无 OOM 风险\n\n**Framing 决策已执行：**备选 A 采纳，plan017 结果加入 Claim 2 evidence，不改结构。正在更新 paper_framing.md。\n\n**下一步自动触发：**\n- plan002-b01 完成（预计 ~40 min）→ 立即 eval_sta.py 评估 → 汇报\n- plan006 readiness report → Worker 正在检查（~2 min）\n- plan016 完成（预计 ~90 min）→ eval_sta.py 评估",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e71add9-04f8-4663-9f6f-bfa95a5107a3",
  "isSidechain": false,
  "requestId": "req_011Cb1we2FTxexs7RARoxMtU",
  "type": "assistant",
  "uuid": "9a17e026-e415-4f99-b98b-92b3552be56c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxxkemW3KqYt2FyFYa8pjn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 108037,
      "output_tokens": 859,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 859,
          "cache_read_input_tokens": 108037,
          "cache_creation_input_tokens": 668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 668
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


### Tool call

_source line 339 · 2026-05-14T05:54:27.039Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012qdCHXKj2DJMAHaJmz9424`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_framing.md",
  "max_chars": 20000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a17e026-e415-4f99-b98b-92b3552be56c",
  "isSidechain": false,
  "requestId": "req_011Cb1we2FTxexs7RARoxMtU",
  "type": "assistant",
  "uuid": "507f5181-562c-4bf2-a20e-e46675b70200",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxxkemW3KqYt2FyFYa8pjn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 108037,
      "output_tokens": 859,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 859,
          "cache_read_input_tokens": 108037,
          "cache_creation_input_tokens": 668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 668
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


### Runtime record

_source line 340_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] **批准磁盘清理 + 后续指令**  ### 1. 磁盘清理：批准 清理以下已完成实验目录，释放空间给 plan016： - plan001_exec_only_s43_r4（~46G） - plan001_exec_only_s44（~31G） - 其他 failed/negative 实验目录（eval 结果已在 registry）  ⚠️ **保留以下目录不要删*…",
  "leafUuid": "507f5181-562c-4bf2-a20e-e46675b70200",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500"
}
```

---


### Runtime record

_source line 341_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate plan017 checkpoint results",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500"
}
```

---


### Tool result

_source line 342 · 2026-05-14T05:54:30.721Z_

<details><summary>↩ Tool result · `toolu_01Jx9eMLqAEKPRiwvDfLbSRu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a17e026-e415-4f99-b98b-92b3552be56c",
  "isSidechain": false,
  "promptId": "c7de91f7-3925-4a4d-a602-a8b7c109e4ac",
  "type": "user",
  "uuid": "5cdfb27d-0b5f-4cfa-832e-6daed047f0fb",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "9a17e026-e415-4f99-b98b-92b3552be56c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-14T05:54:30.738Z_

<details><summary>↩ Tool result · `toolu_012qdCHXKj2DJMAHaJmz9424`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — 诊断/分析论文)\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**:\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)\\n- Hacking taxonomy: 5 distinct modes identified and quantified (plan012 `hacking_characterization_report.md` + plan017 D027)\\n\\n### Claim 2: GRPO Saturation Mechanism\\nExec-only GRPO exhibits a saturation failure mode: when prove_rate → 1.0, reward_std → 0 and loss → 0, training effectively stalls. Any reward component introducing variance (ISR, random noise) prevents saturation but does not prevent hacking — it redirects hacking into different structural failure modes.\\n\\n**证据**:\\n- plan001 exec-only: PR saturation → loss=0 → learning stops (D014)\\n- plan013 random reward: PR=1.0 (prevents saturation) but 100% P→P tautological collapse (D018)\\n- plan002 additive ISR β=0.3: PR=18%, ISR=0.1427 — ISR bonus prevents saturation but causes repetitive cycling, lowest PR of all conditions (D020)\\n- plan005 convex combination: penalty effect confirmed — any ISR<1 reduces reward (D010)\\n- plan017 additive random β=0.3: eval PR=48%, ISR=0.045, comp=9.56 — \\\"complexity-without-utility\\\" mode (高 component 但 conclusion 不依赖 premises, 33% proved ISR=0). ISR 比 random 更差 (PR 18% vs 48%), ISR 信号对训练 actively misleading (D026/D027)\\n- ⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为\\\"additive vs convex\\\"对照。plan017 vs plan002 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）\\n\\n### Claim 3: Cross-Logic Generality (conditional on plan006)\\nSTA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.\\n\\n**证据**: 待验证。plan006 Prolog GRPO 实验未启动。如果 plan006 无法复现 hacking + ISR 诊断，此 claim 降级为 future work。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% collapse over training)\\n  2. GRPO saturation creates a \\\"training trap\\\": PR→1 means no gradient signal, but adding any variance (ISR or random) redirects rather than prevents hacking\\n  3. Different reward formulations produce distinct, classifiable hacking strategies (5 modes identified)\\n  4. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners\\n- **Actionable insights for practitioners**:\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\n  3. Adding structural reward components can hurt prove_rate (penalty effect) or redirect hacking (saturation effect) — neither naïvely improves quality\\n  4. ISR is a structural diagnostic, not a semantic quality proxy\\n- **Headline result**: \\\"We demonstrate that GRPO-trained FOL formalizers achieving 93-98% prove rate produce structurally degenerate outputs detectable by ISR — a component necessity metric derived from solver trace ablation. Across 5 reward conditions and 3 seeds, we identify 5 distinct hacking strategies and a GRPO saturation mechanism that confounds all reward-augmentation approaches. ISR as training signal is worse than matched random noise (PR 18% vs 48%), confirming its value is strictly diagnostic.\\\"\\n\\n## ISR Capability Boundary (D021/D022)\\n\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\n\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\n- Best-of-N ISR selection vs random: +0.9pp (不显著)\\n- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%\\n\\n**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。\\n\\n## ISR-as-Reward Failure Log (D010→D020)\\n\\n以下路线已全面失败，论文不再 claim ISR 可改善训练：\\n- **凸组合** r = α·r_exec + β·r_exec·ISR, α+β=1：ISR<1 时永远是 penalty (plan005, D010)\\n- **Additive bonus β=0.3** r = r_exec·(1+0.3·ISR)：PR=18%, 最差条件 (plan002, D020)\\n- **Additive bonus β=0.1** r = r_exec·(1+0.1·ISR)：实验中 (plan002-b01)\\n- **Random reward** r = α·r_exec + β·r_exec·random：PR=100% 但 100% tautological (plan013, D018)\\n- **Additive random β=0.3** r = r_exec·(1+0.3·random)：PR=48%, 未坍缩但 complexity-without-utility (plan017, D026)\\n\\n这些 negative results 本身是论文贡献——展示了 structural reward integration 的失败模式。关键发现：ISR 比 matched random 更差 (PR 18% vs 48%)，说明 ISR 信号对训练 actively misleading 而非仅仅 noisy。\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Diagnostic/analysis paper in NLP + formal reasoning track. Empirical findings + negative results are valued at EMNLP.\\n- **\\\"Just negative results\\\" risk**: Mitigate by providing actionable diagnostic framework (ISR + taxonomy) and mechanistic insight (GRPO saturation).\\n- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 4 conditions × 4 hacking modes).\\n- **\\\"Old wine\\\" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic hacking diagnostic for formal reasoning GRPO) + empirical findings, not algorithm level.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"ISR is just LOO ablation — not novel\\\"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical taxonomy of hacking modes, (c) GRPO saturation mechanism analysis.\\n2. **\\\"No positive result — ISR doesn't improve training\\\"** — Correct; we frame ISR as diagnostic, not reward. The systematic failure of all ISR-as-reward attempts is itself informative (Section: ISR-as-Reward Failure Log).\\n3. **\\\"ISR is circular\\\"** — ISR is used for diagnosis/post-hoc analysis, not as optimization target. Component count analysis (mean=6.58 vs 2.04, p<0.0001) provides ISR-independent structural evidence.\\n4. **\\\"Only one logic type\\\"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.\\n5. **\\\"500 steps too short\\\"** — plan016 extends to 1000+ steps. Pre-saturation learning curves show hacking onset occurs within 200-300 steps.\\n6. **\\\"3 seeds insufficient for statistical claims\\\"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. But statistical claims on mean ISR use 3-seed mean±std.\\n7. **\\\"Related work insufficient\\\"** — Expand to 25+ refs (literature_map.yaml has 29): reward hacking (Gao 2023, Skalse 2022), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur, AlphaProof), feature attribution (SHAP), FOLIO (Han 2022).\\n8. **\\\"RIP framework overstated\\\"** — Frame as \\\"component necessity testing inspired by mutation testing's RIP framework,\\\" only Propagation condition operationalized.\\n9. **\\\"Practitioners can't act on this\\\"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable.\\n10. **\\\"GRPO saturation is known\\\"** — General RL reward saturation is known (Gao et al. 2023). Our contribution is documenting the specific manifestation in GRPO for formal reasoning + showing that naïve fixes (adding variance) redirect rather than prevent hacking.\\n\\n## Dream-Identified Structural Fixes (Paper Agent)\\n\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 29)\\n- [ ] RIP framing: reframe as \\\"component necessity testing inspired by RIP\\\"\\n- [ ] \\\"Dense+automatic\\\" → \\\"conditionally dense\\\"\\n- [ ] Remove all \\\"Pareto-improving\\\" language\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\n- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed)\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)\\n- [x] Hacking taxonomy completed (plan012, 4 modes identified)\\n\", \"total_chars\": 9629, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "507f5181-562c-4bf2-a20e-e46675b70200",
  "isSidechain": false,
  "promptId": "c7de91f7-3925-4a4d-a602-a8b7c109e4ac",
  "type": "user",
  "uuid": "7527531f-e609-42fc-9413-dac0e2eb661f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — solver-trace-ablation\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\\\n- Fallback: EMNLP 2026 Findings\\\\n- Deadline: ARR May 25, 2026\\\\n\\\\n## Core Claims (3 条 — 诊断/分析论文)\\\\n\\\\n### Claim 1: ISR as Reward Hacking Diagnostic\\\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps), quantifying structural degeneration invisible to the execution reward.\\\\n\\\\n**证据**:\\\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\\\n- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)\\\\n- Hacking taxonomy: 5 distinct modes identified and quantified (plan012 `hacking_characterization_report.md` + plan017 D027)\\\\n\\\\n### Claim 2: GRPO Saturation Mechanism\\\\nExec-only GRPO exhibits a saturation failure mode: when prove_rate → 1.0, reward_std → 0 and loss → 0, training effectively stalls. Any reward component introducing variance (ISR, random noise) prevents saturation but does not prevent hacking — it redirects hacking into different structural failure modes.\\\\n\\\\n**证据**:\\\\n- plan001 exec-only: PR saturation → loss=0 → learning stops (D014)\\\\n- plan013 random reward: PR=1.0 (prevents saturation) but 100% P→P tautological collapse (D018)\\\\n- plan002 additive ISR β=0.3: PR=18%, ISR=0.1427 — ISR bonus prevents saturation but causes repetitive cycling, lowest PR of all conditions (D020)\\\\n- plan005 convex combination: penalty effect confirmed — any ISR<1 reduces reward (D010)\\\\n- plan017 additive random β=0.3: eval PR=48%, ISR=0.045, comp=9.56 — \\\\\\\"complexity-without-utility\\\\\\\" mode (高 component 但 conclusion 不依赖 premises, 33% proved ISR=0). ISR 比 random 更差 (PR 18% vs 48%), ISR 信号对训练 actively misleading (D026/D027)\\\\n- ⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为\\\\\\\"additive vs convex\\\\\\\"对照。plan017 vs plan002 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）\\\\n\\\\n### Claim 3: Cross-Logic Generality (conditional on plan006)\\\\nSTA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.\\\\n\\\\n**证据**: 待验证。plan006 Prolog GRPO 实验未启动。如果 plan006 无法复现 hacking + ISR 诊断，此 claim 降级为 future work。\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% collapse over training)\\\\n  2. GRPO saturation creates a \\\\\\\"training trap\\\\\\\": PR→1 means no gradient signal, but adding any variance (ISR or random) redirects rather than prevents hacking\\\\n  3. Different reward formulations produce distinct, classifiable hacking strategies (5 modes identified)\\\\n  4. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners\\\\n- **Actionable insights for practitioners**:\\\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\\\n  3. Adding structural reward components can hurt prove_rate (penalty effect) or redirect hacking (saturation effect) — neither naïvely improves quality\\\\n  4. ISR is a structural diagnostic, not a semantic quality proxy\\\\n- **Headline result**: \\\\\\\"We demonstrate that GRPO-trained FOL formalizers achieving 93-98% prove rate produce structurally degenerate outputs detectable by ISR — a component necessity metric derived from solver trace ablation. Across 5 reward conditions and 3 seeds, we identify 5 distinct hacking strategies and a GRPO saturation mechanism that confounds all reward-augmentation approaches. ISR as training signal is worse than matched random noise (PR 18% vs 48%), confirming its value is strictly diagnostic.\\\\\\\"\\\\n\\\\n## ISR Capability Boundary (D021/D022)\\\\n\\\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\\\n\\\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\\\n- Best-of-N ISR selection vs random: +0.9pp (不显著)\\\\n- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%\\\\n\\\\n**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。\\\\n\\\\n## ISR-as-Reward Failure Log (D010→D020)\\\\n\\\\n以下路线已全面失败，论文不再 claim ISR 可改善训练：\\\\n- **凸组合** r = α·r_exec + β·r_exec·ISR, α+β=1：ISR<1 时永远是 penalty (plan005, D010)\\\\n- **Additive bonus β=0.3** r = r_exec·(1+0.3·ISR)：PR=18%, 最差条件 (plan002, D020)\\\\n- **Additive bonus β=0.1** r = r_exec·(1+0.1·ISR)：实验中 (plan002-b01)\\\\n- **Random reward** r = α·r_exec + β·r_exec·random：PR=100% 但 100% tautological (plan013, D018)\\\\n- **Additive random β=0.3** r = r_exec·(1+0.3·random)：PR=48%, 未坍缩但 complexity-without-utility (plan017, D026)\\\\n\\\\n这些 negative results 本身是论文贡献——展示了 structural reward integration 的失败模式。关键发现：ISR 比 matched random 更差 (PR 18% vs 48%)，说明 ISR 信号对训练 actively misleading 而非仅仅 noisy。\\\\n\\\\n## Venue Fit Risks\\\\n\\\\n- **EMNLP fit**: Diagnostic/analysis paper in NLP + formal reasoning track. Empirical findings + negative results are valued at EMNLP.\\\\n- **\\\\\\\"Just negative results\\\\\\\" risk**: Mitigate by providing actionable diagnostic framework (ISR + taxonomy) and mechanistic insight (GRPO saturation).\\\\n- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 4 conditions × 4 hacking modes).\\\\n- **\\\\\\\"Old wine\\\\\\\" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic hacking diagnostic for formal reasoning GRPO) + empirical findings, not algorithm level.\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n1. **\\\\\\\"ISR is just LOO ablation — not novel\\\\\\\"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical taxonomy of hacking modes, (c) GRPO saturation mechanism analysis.\\\\n2. **\\\\\\\"No positive result — ISR doesn't improve training\\\\\\\"** — Correct; we frame ISR as diagnostic, not reward. The systematic failure of all ISR-as-reward attempts is itself informative (Section: ISR-as-Reward Failure Log).\\\\n3. **\\\\\\\"ISR is circular\\\\\\\"** — ISR is used for diagnosis/post-hoc analysis, not as optimization target. Component count analysis (mean=6.58 vs 2.04, p<0.0001) provides ISR-independent structural evidence.\\\\n4. **\\\\\\\"Only one logic type\\\\\\\"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.\\\\n5. **\\\\\\\"500 steps too short\\\\\\\"** — plan016 extends to 1000+ steps. Pre-saturation learning curves show hacking onset occurs within 200-300 steps.\\\\n6. **\\\\\\\"3 seeds insufficient for statistical claims\\\\\\\"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. But statistical claims on mean ISR use 3-seed mean±std.\\\\n7. **\\\\\\\"Related work insufficient\\\\\\\"** — Expand to 25+ refs (literature_map.yaml has 29): reward hacking (Gao 2023, Skalse 2022), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur, AlphaProof), feature attribution (SHAP), FOLIO (Han 2022).\\\\n8. **\\\\\\\"RIP framework overstated\\\\\\\"** — Frame as \\\\\\\"component necessity testing inspired by mutation testing's RIP framework,\\\\\\\" only Propagation condition operationalized.\\\\n9. **\\\\\\\"Practitioners can't act on this\\\\\\\"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable.\\\\n10. **\\\\\\\"GRPO saturation is known\\\\\\\"** — General RL reward saturation is known (Gao et al. 2023). Our contribution is documenting the specific manifestation in GRPO for formal reasoning + showing that naïve fixes (adding variance) redirect rather than prevent hacking.\\\\n\\\\n## Dream-Identified Structural Fixes (Paper Agent)\\\\n\\\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 29)\\\\n- [ ] RIP framing: reframe as \\\\\\\"component necessity testing inspired by RIP\\\\\\\"\\\\n- [ ] \\\\\\\"Dense+automatic\\\\\\\" → \\\\\\\"conditionally dense\\\\\\\"\\\\n- [ ] Remove all \\\\\\\"Pareto-improving\\\\\\\" language\\\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\\\n- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed)\\\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)\\\\n- [x] Hacking taxonomy completed (plan012, 4 modes identified)\\\\n\\\", \\\"total_chars\\\": 9629, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — 诊断/分析论文)\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**:\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)\\n- Hacking taxonomy: 5 distinct modes identified and quantified (plan012 `hacking_characterization_report.md` + plan017 D027)\\n\\n### Claim 2: GRPO Saturation Mechanism\\nExec-only GRPO exhibits a saturation failure mode: when prove_rate → 1.0, reward_std → 0 and loss → 0, training effectively stalls. Any reward component introducing variance (ISR, random noise) prevents saturation but does not prevent hacking — it redirects hacking into different structural failure modes.\\n\\n**证据**:\\n- plan001 exec-only: PR saturation → loss=0 → learning stops (D014)\\n- plan013 random reward: PR=1.0 (prevents saturation) but 100% P→P tautological collapse (D018)\\n- plan002 additive ISR β=0.3: PR=18%, ISR=0.1427 — ISR bonus prevents saturation but causes repetitive cycling, lowest PR of all conditions (D020)\\n- plan005 convex combination: penalty effect confirmed — any ISR<1 reduces reward (D010)\\n- plan017 additive random β=0.3: eval PR=48%, ISR=0.045, comp=9.56 — \\\"complexity-without-utility\\\" mode (高 component 但 conclusion 不依赖 premises, 33% proved ISR=0). ISR 比 random 更差 (PR 18% vs 48%), ISR 信号对训练 actively misleading (D026/D027)\\n- ⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为\\\"additive vs convex\\\"对照。plan017 vs plan002 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）\\n\\n### Claim 3: Cross-Logic Generality (conditional on plan006)\\nSTA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.\\n\\n**证据**: 待验证。plan006 Prolog GRPO 实验未启动。如果 plan006 无法复现 hacking + ISR 诊断，此 claim 降级为 future work。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% collapse over training)\\n  2. GRPO saturation creates a \\\"training trap\\\": PR→1 means no gradient signal, but adding any variance (ISR or random) redirects rather than prevents hacking\\n  3. Different reward formulations produce distinct, classifiable hacking strategies (5 modes identified)\\n  4. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners\\n- **Actionable insights for practitioners**:\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\n  3. Adding structural reward components can hurt prove_rate (penalty effect) or redirect hacking (saturation effect) — neither naïvely improves quality\\n  4. ISR is a structural diagnostic, not a semantic quality proxy\\n- **Headline result**: \\\"We demonstrate that GRPO-trained FOL formalizers achieving 93-98% prove rate produce structurally degenerate outputs detectable by ISR — a component necessity metric derived from solver trace ablation. Across 5 reward conditions and 3 seeds, we identify 5 distinct hacking strategies and a GRPO saturation mechanism that confounds all reward-augmentation approaches. ISR as training signal is worse than matched random noise (PR 18% vs 48%), confirming its value is strictly diagnostic.\\\"\\n\\n## ISR Capability Boundary (D021/D022)\\n\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\n\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\n- Best-of-N ISR selection vs random: +0.9pp (不显著)\\n- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%\\n\\n**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。\\n\\n## ISR-as-Reward Failure Log (D010→D020)\\n\\n以下路线已全面失败，论文不再 claim ISR 可改善训练：\\n- **凸组合** r = α·r_exec + β·r_exec·ISR, α+β=1：ISR<1 时永远是 penalty (plan005, D010)\\n- **Additive bonus β=0.3** r = r_exec·(1+0.3·ISR)：PR=18%, 最差条件 (plan002, D020)\\n- **Additive bonus β=0.1** r = r_exec·(1+0.1·ISR)：实验中 (plan002-b01)\\n- **Random reward** r = α·r_exec + β·r_exec·random：PR=100% 但 100% tautological (plan013, D018)\\n- **Additive random β=0.3** r = r_exec·(1+0.3·random)：PR=48%, 未坍缩但 complexity-without-utility (plan017, D026)\\n\\n这些 negative results 本身是论文贡献——展示了 structural reward integration 的失败模式。关键发现：ISR 比 matched random 更差 (PR 18% vs 48%)，说明 ISR 信号对训练 actively misleading 而非仅仅 noisy。\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Diagnostic/analysis paper in NLP + formal reasoning track. Empirical findings + negative results are valued at EMNLP.\\n- **\\\"Just negative results\\\" risk**: Mitigate by providing actionable diagnostic framework (ISR + taxonomy) and mechanistic insight (GRPO saturation).\\n- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 4 conditions × 4 hacking modes).\\n- **\\\"Old wine\\\" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic hacking diagnostic for formal reasoning GRPO) + empirical findings, not algorithm level.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"ISR is just LOO ablation — not novel\\\"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical taxonomy of hacking modes, (c) GRPO saturation mechanism analysis.\\n2. **\\\"No positive result — ISR doesn't improve training\\\"** — Correct; we frame ISR as diagnostic, not reward. The systematic failure of all ISR-as-reward attempts is itself informative (Section: ISR-as-Reward Failure Log).\\n3. **\\\"ISR is circular\\\"** — ISR is used for diagnosis/post-hoc analysis, not as optimization target. Component count analysis (mean=6.58 vs 2.04, p<0.0001) provides ISR-independent structural evidence.\\n4. **\\\"Only one logic type\\\"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.\\n5. **\\\"500 steps too short\\\"** — plan016 extends to 1000+ steps. Pre-saturation learning curves show hacking onset occurs within 200-300 steps.\\n6. **\\\"3 seeds insufficient for statistical claims\\\"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. But statistical claims on mean ISR use 3-seed mean±std.\\n7. **\\\"Related work insufficient\\\"** — Expand to 25+ refs (literature_map.yaml has 29): reward hacking (Gao 2023, Skalse 2022), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur, AlphaProof), feature attribution (SHAP), FOLIO (Han 2022).\\n8. **\\\"RIP framework overstated\\\"** — Frame as \\\"component necessity testing inspired by mutation testing's RIP framework,\\\" only Propagation condition operationalized.\\n9. **\\\"Practitioners can't act on this\\\"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable.\\n10. **\\\"GRPO saturation is known\\\"** — General RL reward saturation is known (Gao et al. 2023). Our contribution is documenting the specific manifestation in GRPO for formal reasoning + showing that naïve fixes (adding variance) redirect rather than prevent hacking.\\n\\n## Dream-Identified Structural Fixes (Paper Agent)\\n\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 29)\\n- [ ] RIP framing: reframe as \\\"component necessity testing inspired by RIP\\\"\\n- [ ] \\\"Dense+automatic\\\" → \\\"conditionally dense\\\"\\n- [ ] Remove all \\\"Pareto-improving\\\" language\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\n- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed)\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)\\n- [x] Hacking taxonomy completed (plan012, 4 modes identified)\\n\", \"total_chars\": 9629, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "507f5181-562c-4bf2-a20e-e46675b70200",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 344 · 2026-05-14T05:54:30.745Z_

```json
{
  "parentUuid": "7527531f-e609-42fc-9413-dac0e2eb661f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d39f0c3f-70ce-4298-b40a-a9dc117d4abd",
  "timestamp": "2026-05-14T05:54:30.745Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 345_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] **批准磁盘清理 + 后续指令**  ### 1. 磁盘清理：批准 清理以下已完成实验目录，释放空间给 plan016： - plan001_exec_only_s43_r4（~46G） - plan001_exec_only_s44（~31G） - 其他 failed/negative 实验目录（eval 结果已在 registry）  ⚠️ **保留以下目录不要删*…",
  "leafUuid": "d39f0c3f-70ce-4298-b40a-a9dc117d4abd",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500"
}
```

---


### Runtime record

_source line 346_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate plan017 checkpoint results",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500"
}
```

---


### Tool call

_source line 347 · 2026-05-14T05:54:42.364Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director · `toolu_01UPWKqdjBHtsJvJk2TXxHHF`</summary>

```json
{
  "text": "[资源] GPU 分配 2 / 实际跑 2 (plan002-b01 cuda:0, plan016 cuda:1) | Worker 池 2 (GPU 0 / CPU 2: kill-verify + plan006-readiness)\n\n**Director 指令执行状态：**\n\n1. **Kill PID 261641**: Worker 已派出执行，等待回调确认显存释放\n2. **磁盘清理**: ✅ 已完成（之前的 cleanup Worker），6.4G → **172G 可用**，空间充裕\n3. **plan016 提交**: ✅ plan016-extended-1000-s42 已在 cuda:1 上 RUNNING（之前已提交）\n4. **Framing 决策（备选 A）**: ✅ paper_framing.md 已包含 plan017 evidence + Reviewer 公式描述约束（D027）\n5. **Reviewer 公式警告**: ✅ 已在 Claim 2 证据中标注 \"plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为 additive vs convex 对照\"\n\n**plan006 readiness**: Worker 正在检查 SWI-Prolog / Prolog STA 代码 / 数据状态，完成后立即汇报。",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f916b9cb-b68d-4272-a5fd-c319969810d1",
  "isSidechain": false,
  "requestId": "req_011Cb1wfdXnHE21DfJriErYf",
  "type": "assistant",
  "uuid": "8ffbeccb-a816-4a47-9712-e597956d4a3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ni5qCyz2oYh44Df6PzHGou",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 111133,
      "output_tokens": 472,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 720,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 472,
          "cache_read_input_tokens": 111133,
          "cache_creation_input_tokens": 720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 720
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

_source line 348 · 2026-05-14T05:54:43.827Z_

<details><summary>↩ Tool result · `toolu_01UPWKqdjBHtsJvJk2TXxHHF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ffbeccb-a816-4a47-9712-e597956d4a3d",
  "isSidechain": false,
  "promptId": "3dc1e72c-f7d9-4a77-8cc1-c2126f62c864",
  "type": "user",
  "uuid": "ef0a1752-c84a-4f8f-b8c1-3a7669aa2cec",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "8ffbeccb-a816-4a47-9712-e597956d4a3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "660d590e-cf89-48c1-957d-0eb210bfd500",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
