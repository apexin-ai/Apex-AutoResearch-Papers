---
name: distilled-research
description: "Agentic RL + verification/adaptive compute: baselines, training recipes, evaluation consensus, competitor positioning, and research gaps from 25 papers (2024-2026)"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [tie2025correctbench, verifiagent2025, feng2025gigpo, spear2025, wei2025webagent-r1, digiRL2024, t2po2026, gvpo2026, agent-omit2026, du2025thinkless, kim2025reflact, selfbudgeter2026, tu2025autothink, wan2025derailer-rerailer, xiang2024retrospex, cfgm2025, istar2025, archer2024, agentic-rl-survey-2025, ava2026, xi2025agentprm, kamoi2024self-correction-survey, self-verification-dilemma-2026, zhang2025incentivize-self-verify, mar2025]
  last_distilled: "2026-05-23T00:00:00Z"
---

## Required Baselines

- **GRPO**: 10/25 papers. Universal agentic RL baseline — must include. (高, GiGPO/SPEAR/T2PO/GVPO)
- **GPT-4o prompting**: 8/25. Standard closed-source ceiling. (高)
- **GiGPO**: Already baseline in ICML 2026 (T2PO) and ICLR 2026 (SPEAR) despite being NeurIPS 2025. Rising fast. (中)
- **ReAct + Reflexion**: 5/25. Required prompting baselines for agent papers. (高)

## Evaluation Ecosystem

**Benchmarks by frequency**: ALFWorld 10/25, WebShop 9/25, Search QA suite (NQ/TriviaQA/HotpotQA) 5/25, GSM8K/MATH 6/25, WebArena-Lite 3/25, AppWorld 1/25 (emerging for coding agents).

**Metrics**: Task success rate universal. Cost/efficiency metrics rising — 7/25 papers track token cost. CorrectBench introduced Efficiency Rank = Accuracy/(Tokens × API_Calls). VerifiAgent reports $/instance ($0.047 vs MV $0.175). Mean±std across 3 seeds: GiGPO, DigiRL, T2PO do it; VerifiAgent, GVPO main results don't.

## Training Recipe Consensus (8 deep-read papers)

| Parameter | Consensus | Support |
|---|---|---|
| Optimizer | AdamW | 8/8 |
| RL learning rate | 1e-6 | 5/8 (GiGPO/T2PO/GVPO/WebAgent-R1/SPEAR) |
| Hardware | 8×H100 | 3/8 (GiGPO/T2PO/GVPO) |
| Framework | verl + vLLM | 3/8, emerging standard |
| Group/rollout size | 8 | 4/8 |
| KL coefficient | 0.01 | 3/8 (SPEAR removes KL entirely) |
| Base model family | Qwen2.5 | 6/8 |
| Cold-start | SFT/RFT before RL mandatory | 3/8 (WebAgent-R1: R1-Zero fails at 5.7%) |
| Reward | Binary success/failure sufficient | 5/8 |

## Competitor Positioning

| Paper | Claim | Gap vs our approach |
|---|---|---|
| VerifiAgent | Training-free 2-layer verification, 73% cheaper than MV | No RL, no learned cost policy, fixed 3 tools |
| GVPO | Process signals for training-time credit assignment | Not deployment-time adaptive |
| Self-Verif. Dilemma | Suppress unnecessary rechecks, −20.3% tokens | Test-time heuristic, no RL |
| Incentivize Self-Verify | Joint gen+verify RL | Math-only, not agent setting |
| CorrectBench | Benchmark showing reasoning LLMs have ceiling effect | Calls for adaptive cost-aware correction — our direction |

## Research Gaps (our opportunity)

1. **No paper trains agents to decide WHEN verification is worthwhile** — GVPO uses verification for training; VerifiAgent applies uniformly; Suppression papers are test-time heuristics. 25/25 absence. (高)
2. **Cost-efficiency metrics underdeveloped** — Only 2/25 propose formal cost metrics. 23/25 ignore cost in evaluation. (高)
3. **Verification × multi-turn agentic RL not crossed** — Verification papers target single-turn reasoning; agentic RL papers ignore verification entirely. 25/25 absence. (高)

## Method Trends

**Rising**: Critic-free group RL (GRPO→GiGPO→T2PO); process-verifiable signals (GVPO); uncertainty-based exploration control (T2PO); self-imitation with curriculum (SPEAR).
**Declining**: PPO with critic (2/25); fixed verification strategies; single-turn RL for agents.
