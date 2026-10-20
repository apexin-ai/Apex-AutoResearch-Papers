# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-27 (UTC).** Your job: indep — Part 2 of 2

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-you-are-a-strict-ml-research-reviewer-conducting-adversarial-review-today-s-da-copy-34.md) · [Structured JSON](../../../sessions/71/71d49fdc0085a02fe2e8.json)

## Round 1

### Assistant

_source line 219 · 2026-05-27T22:09:16.316Z_

<details><summary>Logged reasoning block</summary>

```text
The idea states Entrocraft achieves "~17% improvement in pass@32." But the actual paper says "raises pass@K by 50%." Let me check this claim more carefully.

Looking at the earlier search results:
"raises pass@K by 50% over the baseline"

So the idea says "~17% improvement in pass@32" but the actual figure from the paper is "raises pass@K by 50%". This could be a factual error in the idea.

Wait, let me re-read the idea's text: "Entrocraft (arXiv 2604.26326, 2026) achieves ~17% improvement in pass@32 via entropy-guided rejection sampling."


The paper reports a 50% improvement in pass@K overall, though the 17% figure might be referring to a specific subset or different metric—either way, the discrepancy suggests I should verify which number applies to pass@32 specifically, since the abstract's 50% could be measuring something broader.

Now I'm compiling the key gaps in the paper's related work section. RLoop is a critical missing baseline since it also does iterative RL and SFT cycling with a fixed schedule and achieves strong results on AIME and MATH, making it a direct comparison point for the self-improvement approach. ReLIFT is another relevant work that uses adaptive switching between RL and SFT with a buffer-based mechanism, which relates to the paper's methodology.

There's also a tension with ProRL's findings—it shows RL can discover entirely novel strategies with perfect pass rates on tasks where base models fail completely, which somewhat contradicts the cited claim that RL doesn't expand pass@k. The paper should address this more directly.

On the technical side, there's a natural limitation with SEG that as the policy concentrates toward optimal solutions, pass@k converges to pass@1, causing SEG to shrink—the paper touches on this but should make it more explicit. Finally, there's a potential discrepancy with the Entrocraft citation where the paper claims ~17% improvement but the abstract mentions 50%, so I need to verify which is accurate before finalizing the review.

Looking at the supporting evidence, "RL Squeezes, SFT Expands" directly validates FrontierLoop's core premise that RL and generation-based approaches are complementary and should be cited. ReasonMaxxer raises a practical concern that RL only affects 1-3% of tokens, which questions whether discrete RL phases are worth the overhead compared to simpler alternatives, though this doesn't fundamentally break the approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2cf1ae8-5c55-479d-805e-a1d9cc65b99c",
  "isSidechain": false,
  "requestId": "req_011CbTqVCMLANPFxfvCVMx3Z",
  "type": "assistant",
  "uuid": "084f90a6-89b4-44b9-b0de-ccd834358398",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2727791-e9bd-477c-a9fa-5207398e33a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7BUnTXtuyiondgqok6Uxa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 572,
      "cache_read_input_tokens": 95473,
      "output_tokens": 2712,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 572,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2712,
          "cache_read_input_tokens": 95473,
          "cache_creation_input_tokens": 572,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 572
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

_source line 220 · 2026-05-27T22:09:53.139Z_

I've now completed an extensive independent review. Let me compile all findings into a comprehensive assessment.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3.5, "rationale": "The specific gap — adaptive diagnostic-guided mode-level scheduling between data generation and RL in self-improvement — is genuinely unoccupied. The 5-level hierarchy is a useful framing. However, the landscape is crowded with cycling methods (RLoop does fixed RL↔RFT cycling, SePT does fixed generation↔SFT cycling, ReLIFT does adaptive RL↔SFT interleaving with external teacher), so the novelty narrows to 'add pass@k-derived diagnostics to self-improvement cycling.' Valid but incremental."},
    "feasibility": {"score": 4, "rationale": "Well-designed with Stage 0.5 go/no-go gate, validated diagnostic signals (Quagmires R²=0.87/0.88/0.94 verified), reasonable compute estimates ($2,000-3,800), and composability with existing methods. The 7 baselines + 6 ablations are ambitious but achievable within the timeline."},
    "clarity": {"score": 4.5, "rationale": "Exceptionally well-articulated after 8 rounds. The 5-level hierarchy, mode decomposition (support expansion vs. policy reshaping), composability argument, and clear differentiation from B-STaR/AdaSTaR/SwS/SePT are all compelling. The landscape coverage is comprehensive, though missing RLoop."},
    "impact": {"score": 3, "rationale": "The core question (when to switch between generation and RL) matters, but the field is converging on unified methods (CHORD at ICLR 2026, HPT) and simple fixed pipelines that work well (RLoop achieves 15%+ pass@32 gains with fixed cycling). ReasonMaxxer (May 2026) further shows RL affects only 1-3% of tokens, questioning the overhead of discrete RL phases. The marginal value of adaptive over fixed cycling is uncertain."}
  },
  "issues": [
    "CRITICAL MISSING BASELINE — RLoop (arXiv 2511.04285, Nov 2025): Iteratively cycles between RL and RFT (rejection-sampling fine-tuning) in the SELF-IMPROVEMENT regime with a fixed 200-step RL → 1-epoch RFT schedule. On Qwen-2.5-7b-Math, achieves 73.33% pass@32 on AIME 2024 and 80.00% pass@32 on MATH, representing 15%+ improvement over vanilla RL. This is a DIRECT fixed-schedule cycling baseline in the same setting as FrontierLoop. RLoop's RL→RFT cycling is arguably closer to FrontierLoop's RL↔generation cycling than SePT's generation↔SFT cycling. Must be added as baseline #8 alongside SePT.",
    "MISSING RELATED WORK — ReLIFT (arXiv 2506.07527, June 2025): Implements adaptive RL↔SFT interleaving with buffer-based switching (triggers SFT when hard-problem buffer reaches threshold M). While it uses external solutions (not self-improvement), the adaptive interleaving mechanism is conceptually the closest existing work to adaptive mode-switching. Achieves +5.2 points across competition-level benchmarks with only 13% of the demonstration data. Must be cited and differentiated: ReLIFT uses external teacher + per-sample switching; FrontierLoop uses self-generated data + phase-level diagnostics.",
    "ProRL TENSION INSUFFICIENTLY ENGAGED: ProRL (NeurIPS 2025, arXiv 2505.24864) demonstrates RL CAN discover genuinely novel strategies with 100% pass rates on tasks where base models score 0%, directly contradicting the heavily cited arXiv 2504.13837 claim that 'RLVR does NOT expand pass@k frontier.' The idea cites both papers in references but does not discuss this tension in the landscape or approach sections. Since the 'RL cannot expand frontiers → new data needed' argument is FrontierLoop's CENTRAL MOTIVATION for generation phases, this contradiction must be explicitly addressed. Acknowledge that the frontier-expansion limitation may be task-specific and model-scale-dependent rather than universal.",
    "SEG VANISHING SIGNAL RISK (arXiv 2511.16231): As policy concentrates probability mass during successful RL training, pass@k converges toward pass@1, making SEG naturally shrink regardless of whether the frontier is genuinely exhausted. The idea's compound criterion 'SEG small AND pass@k stagnant' partially handles this, but the known limitation from arXiv 2511.16231 should be explicitly acknowledged. Consider noting that pass@k is validated as a DIAGNOSTIC (which supports FrontierLoop's use) but provides vanishing signal as an optimization OBJECTIVE (which is not how FrontierLoop uses it).",
    "ENTROCRAFT CLAIM MAY BE INACCURATE: The idea states 'Entrocraft achieves ~17% improvement in pass@32.' The paper's abstract states 'raises pass@K by 50% over the baseline.' Verify which figure corresponds to which specific benchmark and correct if needed."
  ],
  "feedback": "This is round 9 of 10 — the next round requires a final pass/fail decision. To position for a pass: 1) ADD RLoop (2511.04285) as baseline #8 — it's the most directly comparable fixed-schedule cycling method in the self-improvement regime. The comparison 'FrontierLoop (adaptive) vs. RLoop (fixed RL↔RFT cycling) vs. SePT (fixed generation↔SFT cycling)' would make the experimental contribution much cleaner and more convincing. 2) ADD ReLIFT (2506.07527) to the landscape — differentiate on three axes: self-improvement vs. teacher-aided, phase-level vs. sample-level switching, diagnostic signals vs. buffer thresholds. 3) EXPLICITLY ADDRESS the ProRL contradiction: acknowledge that RL frontier expansion appears task- and scale-dependent. ProRL finds expansion under prolonged training with KL control; arXiv 2504.13837 finds no expansion under standard RLVR. Position FrontierLoop as most valuable in the 'standard RLVR' regime where the frontier-expansion limitation is empirically documented. 4) ADD one sentence acknowledging the SEG vanishing signal limitation from arXiv 2511.16231, noting that FrontierLoop uses SEG as a diagnostic (validated) not an optimization objective (problematic), and that the compound criterion (SEG + pass@k stagnation) mitigates this concern. 5) VERIFY the Entrocraft ~17% vs. 50% discrepancy. 6) CONSIDER adding 'RL Squeezes, SFT Expands' (arXiv 2509.21128) as supporting evidence — it empirically validates the complementary roles of RL (concentration/squeezing) and SFT/generation (expansion/diversification), directly supporting FrontierLoop's core design motivation.",
  "reason": "Strong conceptual contribution with clear positioning after 8 rounds of revision, but missing RLoop as a critical self-improvement cycling baseline and insufficiently engaging with ProRL's contradicting evidence on RL frontier expansion. Average score 3.75 is below the 4.0 pass threshold."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "084f90a6-89b4-44b9-b0de-ccd834358398",
  "isSidechain": false,
  "requestId": "req_011CbTqVCMLANPFxfvCVMx3Z",
  "type": "assistant",
  "uuid": "26cc7282-87aa-4651-bdac-14d04ae4d81b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2727791-e9bd-477c-a9fa-5207398e33a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7BUnTXtuyiondgqok6Uxa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 572,
      "cache_read_input_tokens": 95473,
      "output_tokens": 2712,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 572,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2712,
          "cache_read_input_tokens": 95473,
          "cache_creation_input_tokens": 572,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 572
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

_source line 221_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-27 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "26cc7282-87aa-4651-bdac-14d04ae4d81b",
  "sessionId": "d2727791-e9bd-477c-a9fa-5207398e33a1"
}
```

---


### Runtime record

_source line 222_

```json
{
  "type": "ai-title",
  "aiTitle": "Review FrontierLoop self-improvement scheduling framework",
  "sessionId": "d2727791-e9bd-477c-a9fa-5207398e33a1"
}
```

---
