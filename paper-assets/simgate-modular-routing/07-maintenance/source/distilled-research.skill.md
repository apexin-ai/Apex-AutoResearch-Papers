---
name: distilled-research
description: "LLM agent adaptive routing/reasoning领域的实验设计共识、方法趋势、竞品定位和研究空白"
scope: project
version: 2
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 9
  paper_keys: [mtrouter-2026, retool-2026, tsr-2026, cogrouter-2026, itp-2026, ares-2026, dynathink-2025, llm-agentic-failures-2025, envsimbench-2025]
  last_distilled: "2026-05-22T22:00:00Z"
---

## 方法论趋势

**SFT→RL 两阶段训练是标配**。ReTool(cold-start+PPO)、CogRouter(CoSFT+CoPO)、ITP(warmup+A2C)、ARES(SFT+GRPO)、TSR(GRPO/PPO) 均采用 SFT 冷启动+RL 优化。支持度: 5/8 训练论文 | 来源: CogRouter, ARES | 置信度: 高

**GRPO 正取代 PPO**。TSR、CogRouter(CoPO 基于 GRPO)、ARES 用 GRPO；仅 ReTool 用 PPO，ITP 用 A2C。支持度: 3/8 GRPO vs 1/8 PPO | 来源: TSR | 置信度: 中

**Step-level credit assignment 是突破方向**。Trajectory-level reward 致 mode collapse（CogRouter Figure 1 量化了 GRPO→L4 坍缩）。CogRouter 用 confidence reweighting，TSR 用 per-turn scoring，ARES 用 per-step effort labeling。支持度: 3/8 | 来源: CogRouter | 置信度: 高

**效率已成一等指标**。CogRouter(62% token↓)、ARES(35-53%↓)、MTRouter(43-59% cost↓)、Dyna-Think(2x token↓) 将 token/cost 与 accuracy 并列报告。支持度: 4/8 | 置信度: 高

## Baseline 与评测共识

**必选 baseline 池**: ReAct(prompt floor)、SFT(offline floor)、GRPO/PPO(RL baseline)、GPT-4o/o3(frontier ceiling)。支持度: 5/8 | 来源: CogRouter | 置信度: 高

**标准 benchmark**: ScienceWorld(3/9) + ALFWorld(2/9) 是 agent 评测最高频组合。WebArena/TAU-Bench 覆盖 web/tool 场景。支持度: 5/9 | 置信度: 高

**Qwen2.5 系列是默认 base model**（5/8 训练论文选 Qwen2.5，7B-32B），Llama 仅 2/8。支持度: 5/8 | 置信度: 高

**Success rate + token count 是主指标组合**（5/8 报 SR，4/8 报 token 效率）。支持度: 5/8 | 置信度: 高

## 竞品 Claim 汇总

| 竞品 | 核心 claim | 关系 |
|------|-----------|------|
| MTRouter | turn-level joint embedding routing 超 GPT-5 同时降 59% cost | competitor |
| CogRouter | 4-level 认知深度 + CoPO 超 o3(+18pp) 省 62% token | competitor |
| ARES | 1.7B router per-step effort 省 35-53% token 保持 accuracy | competitor |
| ITP | adaptive lookahead + world model 在 ALFWorld 达 88.6% | complementary |
| Dyna-Think | 32B 内化 WM simulation 达 685B R1 水平用 2x 少 token | complementary |

## 共同局限 & 研究空白

**共同局限**: benchmark 多样性不足(6/8)；RL mode collapse 风险(3/8: CogRouter, TSR, ARES)；world model hallucination(2/8: ITP, Dyna-Think)；KV cache 因模型/模式切换断裂(2/8: MTRouter, ARES)

**研究空白**: (1) 无论文同时做 inter-model routing + intra-model effort allocation；(2) 全是 offline/batch RL，无实时在线自适应；(3) world model 论文不做 routing，routing 论文不用 world model；(4) 跨 benchmark 泛化证据薄弱——多数仅 1-2 个 benchmark
