# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：剩余实验全面确认 dev 发现，test 数字坚挺，DREEAM-protocol 对齐有竞争力，EDCR 人工验证通过——5-claim 框架完全成立

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/540b5134-714e-48b9-825b-9e0b1b9937b0.jsonl`
- **Structured JSON:** [`b173ad8ac1a2944930a1.json`](../../sessions/b1/b173ad8ac1a2944930a1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T16:00:41.800Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T16:00:41.800Z",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：剩余实验全面确认 dev 发现，test 数字坚挺，DREEAM-protocol 对齐有竞争力，EDCR 人工验证通过——5-claim 框架完全成立，EMNLP Main 可直接投稿\n核心假设：['Test set Ign-F1 退化 ≤1.5pp（dev 45.85 → test ≥44.3），no-evidence 同步退化（gap 保持）', 'DREEAM-protocol 对齐后 Evi-F1 ≥ 0.50——generative evidence 映射到句子级评估后仍有竞争力', 'EDCR 与 100 例人工标注 Spearman ρ ≥ 0.70，自动指标有效性充分验证', 'Post-hoc retrieval (SFT+BM25) evi_f1 ≤ 0.70，与 RSFT 0.81 差距 ≥10pp，端到端生成显著优于检索拼接', '8B/1.7B RSFT candidates 成功完成，RSFT 增益也呈 scale-dependent pattern，强化 C5']\n关键指标范围：{'test_ign_f1_rsft_best': [44.0, 46.0], 'test_ign_f1_no_evidence': [45.5, 48.0], 'test_evidence_tax_4b': [-4.0, -1.5], 'dreeam_protocol_evi_f1': [0.5, 0.65], 'edcr_human_spearman_rho': [0.7, 0.9], 'posthoc_retrieval_evi_f1': [0.55, 0.7], 'expected_reviewer_avg': [3.5, 4.0]}\n叙事方向：原始 framing 完全成立。标题可保持 evidence-grounded DocRE 方法论定位。 C1 直接声称 RSFT+CED 是有效方案（test 确认 +3-5pp over SFT）。 C2 decoupling spectrum 作为核心发现完整呈现（GRPO→DPO→RSFT 连续谱系）。 C3 NLI-based scoring 作为 RSFT 有效的关键组件。 C4 EDCR 双层诊断通过人工验证背书。 C5 U-shape scaling 作为独立贡献。 投 EMNLP Main，不需要 fallback AAAI。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: faith-evidence-ie\n\n## paper_framing.md\n\n# Paper Framing — FREIGE\n\n> **状态**: POST-MVP + D078-D083 scaling analysis & cross-validation complete\n> **最后更新**: 2026-05-16\n> **Dream v1**: best=2.5, median=3.0, worst=2.5 → reframe 完成\n> **Dream v2**: best=3.0, median=2.5, worst=2.5 → best 提升但 median 下降，未达标。关键路径：plan_011 bf16 GRPO eval + structural fixes → re-dream v3\n\n## Target Venue\n\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\n\n## Core Insight\n\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。\n\n我们系统性地探索了 online RL (GRPO) 、offline preference optimization (DPO) 和 offline RL (RSFT) 三条技术路线。关键发现：**RL optimization pressure 与 evidence-extraction decoupling severity 正相关**——优化强度越大，evidence 质量提升的同时抽取能力退化越严重。QLoRA 放大至 catastrophic（rel_f1<0.02），bf16 GRPO 从 0.4549 退化至 ~0.434（mild, -2pp），DPO 呈 gradual 退化（1ep→3ep rel_f1 从 0.4034→0.3429），RSFT 无 decoupling。\n\n**Evidence tax 是 scale-dependent 的（U-shape pattern, D079/D082/D083）**：1.7B 模型中 evidence generation 反而带来 +6.2pp 收益（隐式正则化），4B 模型付出 -7.9pp 代价，8B Qwen 模型容量足够 absorb（≈0），8B LLaMA 跨家族确认（-0.7pp）。这推翻了\"evidence 总有代价\"的简单叙事。\n\nCED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，通过文档内 hard negative 对比评估 evidence 质量。CED 和 flat-NLI 作为 RSFT scoring functions 统计不可区分（D078 paired t-test p=0.44），但均显著优于 random/no scoring。CED 因可解释性优势作为默认推荐方案。\n\n## Story Arc\n\n1. **Problem**: LLM DocRE 无证据 → 部署障碍\n2. **New task**: evidence-grounded DocRE — 同时生成关系和证据\n3. **Cost of faithfulness**: evidence generation 代价是 **scale-dependent** 的——4B 模型付出 -7.9pp 代价，但 1.7B 反而获益 +6.2pp，8B 趋近于零。这不是固定成本，而是与模型容量的非线性交互（D079/D082/D083）\n4. **Exploration**: 系统性比较 online RL (GRPO) vs offline preference (DPO) vs offline RL (RSFT)\n5. **Key finding**: evidence-extraction decoupling — RL optimization pressure 与 decoupling severity 正相关，形成连续谱系（GRPO-QLoRA catastrophic > GRPO-bf16 mild > DPO gradual > RSFT none）\n6. **QLoRA amplification**: QLoRA 量化将 mild decoupling 放大至 catastrophic forgetting——decoupling 是 RL-for-IE 中 multi-objective competition 的通用梯度（intra-task trade-off，非 inter-task forgetting），QLoRA 是 catastrophic amplifier\n7. **What works**: RSFT with NLI-based scoring 是唯一有效路线——提升 evidence 质量而不牺牲抽取\n8. **Best practical solution**: CED reranker 恢复 97% 的 evidence 代价，同时保留高质量 evidence（evi_f1=0.8188）\n9. **Diagnostic tool**: EDCR 双层诊断——方法级量化 decoupling（与 Claim 2 呼应），per-relation 级揭示 evi_f1 不捕捉的 relation-type 难度差异（D070 ✅）\n10. **Scaling & generalization**: evidence tax 呈 U-shape scaling pattern（D079/D082/D083），跨模型家族（LLaMA-8B, D082）和跨数据集（Re-DocRED, D080）验证泛化性\n\n## Core Claims (reframed after Dream v1, updated D068-D083)\n\n### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力\n- FREIGE 是首个**基于生成式 LLM** 的 evidence-grounded DocRE 方法（⚠️ 必须始终保持 \"generative LLM\" 限定词——SAIS 已做 encoder-based evidence retrieval + DocRE）\n- **关键区分 (Reviewer warning)**：encoder-based evidence *retrieval*（SAIS, DREEAM — 分类哪些句子是证据，evidence supervision 提升 RE）vs generative evidence *production*（FREIGE — LLM 生成证据文本，额外生成负担导致 scale-dependent 代价）。论文 Related Work 必须精准讨论此对比，否则审稿人会问 \"为什么 SAIS 说 evidence 有用，你说 evidence 有害\"\n- **Evidence generation tax**: scale-dependent，详见 Claim 5（D079/D082/D083）\n- RSFT 在 4/4 配置下均超过 SFT baseline（Ign-F1 +3.3~5.5pp）\n- **CED reranker 是最优实用方案**: rel_f1=0.4864（仅低于 no-evidence 0.29pp），evi_f1=0.8188（plan_005 ✅）\n- **D076 统一协议最终数字（可写入论文）**:\n  - SFT baseline: rel_f1=0.4049\n  - CED RSFT mean: rel_f1=0.4569 (s42=0.4517, s44=0.4621)\n  - flat-NLI RSFT mean: rel_f1=0.4561 (s42=0.4535, s43_r2=0.4586)\n  - CED vs flat-NLI Δ=0.0008，统计不可区分（D078 p=0.44）\n- **Cross-family validation (D082)**: LLaMA-3.1-8B SFT rel_f1=0.5514, evi_f1=0.8151; no-evidence rel_f1=0.5624（evidence tax = -0.7pp，8B 容量足够 absorb）\n- **Cross-dataset validation (D080)**: Re-DocRED Ign-F1 下降 3.15pp 但 Evi-F1 保持 0.817——evidence extraction 能力跨数据集泛化\n- 需要 DREEAM-protocol 对齐的 Evi-F1 对比（D041 在处理中）\n- **RSFT 方法论定位**：诚实承认 RSFT 是 STaR (NeurIPS 2022) 的单轮变体 + evidence quality scoring。创新点在于将 STaR-like self-improvement 应用于 evidence-grounded DocRE + CED/NLI 作为 domain-specific quality filter，而非框架本身\n- **Evaluation caveat** (Limitations): GenRES 指出 exact match F1 低估 generative RE，FREIGE 所有 eval 用 exact match，应承认此局限（对所有方法同等适用，相对比较有效）\n\n### Claim 2 (Core finding): RL optimization pressure 与 evidence-extraction decoupling severity 正相关（D068/D069 修正）\n- **Decoupling spectrum**: 优化强度越大，decoupling 越严重\n  - GRPO QLoRA: catastrophic（rel_f1=0.0138, evi_f1=0.850, EDCR=0.99）— QLoRA 放大 decoupling\n  - GRPO bf16: mild（rel_f1 从 0.4549→~0.434, -2pp; step_30=0.434, step_50=0.4276, step_70=0.4341）— 退化可控但持续（D065/D066）\n  - DPO bf16 1ep→3ep: gradual（Ign-F1 38.88→TBD, rel_f1 0.4034→0.3429）— 随训练渐进退化（D067/D068）\n  - RSFT: none — 无 decoupling，唯一有效路线\n- **QLoRA 是 catastrophic amplifier，不是 root cause**: bf16 GRPO 仅 mild decoupling（-2pp），QLoRA 放大至 catastrophic（-39pp）（D054/D065/D066）\n- **Decoupling 是 RL-for-IE 的通用梯度**: 跨方法（GRPO/DPO）、跨量化策略（QLoRA/bf16）一致出现，严重程度与优化压力正相关\n- 三档 Dream 审稿均认为此发现\\\"genuinely novel and striking\\\"\n- **已完成**: GRPO G=8 bf16 确认 mild decoupling（plan_011 ✅）; DPO 1ep/3ep 确认 gradual decoupling（plan_012 ✅）\n\n### Claim 3 (Ablation): NLI-based scoring 提升 RSFT 质量——CED 与 flat-NLI 统计不可区分（D078）\n- CED 和 flat-NLI 都显著优于 random/no scoring\n- **D078 paired t-test 最终结论**: CED vs flat-NLI p=0.44，统计不可区分\n  - CED RSFT mean rel_f1=0.4569 vs flat-NLI mean rel_f1=0.4561（Δ=0.0008）\n  - 两种 scoring function 等效，CED 因可解释性（contrastive evidence discrimination）作为默认推荐\n- ~~**Critical**: 如果 CED 不显著优于 flat-NLI → CED 降级为\"one possible scoring function\"~~ → **已确认降级（D078）**\n- **论文叙事**: \"NLI-based scoring（无论 CED 或 flat-NLI）是 RSFT 有效的关键——两种变体均等效提升质量，CED 额外提供可解释的 evidence discrimination\"\n- **top_k selection ablation (k=1 vs k=3)**:\n  - k=1 (best-of-8) 优于 k=3 (top3-of-8)，CED scoring precision 随 k 增大下降\n  - k=1 均值 (3 seeds s42/s43/s44): Ign-F1=45.00, rel_f1=0.4596, evi_f1=81.43, EDCR=0.6434\n  - k=3 (1 seed, reeval_rsft_topk3): Ign-F1=43.64, rel_f1=0.4454, evi_f1=80.88, EDCR=0.6635\n  - Δ (k=3 vs k=1 mean): Ign-F1 **-1.36pp**, rel_f1 **-1.42pp**, evi_f1 **-0.55pp**, EDCR +0.02\n  - 训练数据质量下降: k=1 mean_f1=0.6157, mean_ced=0.6683 → k=3 mean_f1=0.5761, mean_ced=0.6205（来源: mvp2_rsft_ced_scoring / mvp2_rsft_ced_scoring_topk3_r2）\n  - 训练集规模: k=1 选出 2718 样本 (12.4%), k=3 选出 8037 样本 (37%), 数据量 ×2.96 但质量下降抵消数量优势\n  - **叙事**: 低排名 response 引入噪声——rank 2-3 样本的 F1 和 CED 分数均显著低于 rank 1，扩大训练集规模无法补偿数据质量的稀释。这表明 RSFT 的关键不在数据量而在 scoring precision\n  - **注**: k=3 仅 1 seed，差异方向一致但尚不具备统计显著性；作为 ablation table 中的辅助行呈现，不作为独立 claim\n\n### Claim 4 (Diagnostic): EDCR 双层诊断价值（D070/D072）\n- **Layer 1 — 方法级**: EDCR 量化 evidence-extraction decoupling，与 Claim 2 spectrum 呼应\n  - 方法级 EDCR 与 rel_f1 Spearman ρ=-0.965（plan_003 ✅）——本质是 decoupling 的度量\n  - EDCR 识别病理模型（GRPO QLoRA: EDCR≈1.0）\n- **Layer 2 — per-relation-type**: EDCR 提供 evi_f1 不捕捉的 relation-type 诊断信息 ✅\n  - per-relation ρ(EDCR, evi_f1) = **-0.064** (p=0.58) → **完全独立于 evi_f1**\n  - per-relation ρ(EDCR, rel_f1) = -0.793 (p<0.001) → 与 rel_f1 强相关但非完美\n  - per-relation ρ(evi_f1, rel_f1) = -0.013 (p=0.91) → evidence 质量与抽取能力在 relation type 间完全解耦\n  - 典型案例：date_of_birth (EDCR=0.118, 高 faithful) vs head_of_government (EDCR=0.956, 高 decoupled)\n  - 93 relation types 分析（≥5 样本），76 个有非零数据\n- **论文叙事**: EDCR 在方法级是 decoupling 度量工具（横向对比方法），在 relation 级是难度诊断工具（纵向定位薄弱 relation）——两层叙事互补\n- **仍需**: 100 例人工标注验证（RC6）\n\n### Claim 5 (NEW — Scaling): Evidence Tax 呈非线性 U-shape Scaling Pattern（D079/D082/D083）\n- **核心发现**: evidence generation 的代价不是固定的——它与模型容量呈非线性关系\n  - **1.7B (Qwen3-1.7B)**: +6.2pp BENEFIT — evidence generation 起隐式正则化作用，防止小模型过拟合（D083 公平子集分析确认）\n  - **4B (Qwen3-4B)**: -7.9pp cost — 标准 evidence generation 负担，模型容量不足以同时优化两个目标\n  - **8B Qwen (Qwen3-8B)**: ≈0 — 模型容量足够 absorb evidence generation 的额外负担\n  - **8B LLaMA (LLaMA-3.1-8B)**: -0.7pp — 跨家族确认，8B 规模的 evidence tax 趋近于零\n- **U-shape 解释**: 小模型从 evidence 的正则化效应获益 > 生成负担；中等模型容量不足以同时做好两件事；大模型容量充裕，两个目标互不干扰\n- **论文叙事**: 推翻 \"evidence 总有代价\" 的简单叙事，揭示 evidence generation 与模型容量的非线性交互——这为选择何种规模模型部署 evidence-grounded IE 提供实际指导\n- **Cross-family robustness**: LLaMA-8B 与 Qwen-8B 一致确认 8B 规模 evidence tax ≈ 0\n\n## MVP Evidence Summary (D071: 主表报 Ign-F1，附录报 F1; D076 统一协议 rel_f1)\n\n| Config | Ign-F1 | F1 | Δ vs SFT (Ign-F1) | Evi-F1 (cond) | Evi-F1 (joint) | EDCR |\n|--------|--------|------|-------------------|---------------|---------------|------|\n| **SFT no-evidence** | **47.36** | 48.93 | **+7.00pp** | **—** | **—** | **—** |\n| SFT baseline (noquant) | 40.36 | 41.06 | — | 80.13 | 31.17 | 0.7118 |\n| **CED reranker** | **TBD** | 48.64 | **TBD** | **81.88** | — | **0.6156** |\n| RSFT CED s43 (best) | **45.85** | 46.83 | **+5.49pp** | 81.56 | 37.11 | 0.6388 |\n| RSFT CED s44 | 45.51 | 46.55 | +5.15pp | 80.87 | 37.13 | 0.6350 |\n| RSFT CED s42 | 43.63 | 44.49 | +3.27pp | 81.87 | 34.68 | 0.6565 |\n| RSFT CED k=3 | 43.64 | 44.54 | +3.28pp | 80.88 | — | 0.6635 |\n| RSFT r2a (1ep) | 44.01 | 44.94 | +3.65pp | 81.08 | 35.09 | 0.6641 |\n| RSFT r2b (1ep) | 44.10 | 44.93 | +3.74pp | 81.28 | 34.90 | 0.6609 |\n| flat-NLI s42 | 44.49 | 45.39 | +4.13pp | 80.43 | — | 0.6431 |\n| flat-NLI s43 (reeval) | TBD | 45.23 | TBD | 81.58 | — | 0.6505 |\n| DPO bf16 1ep | 38.88 | 40.34 | -1.48pp | 80.88 | — | 0.7139 |\n| DPO bf16 3ep | TBD | 34.29 | TBD | — | — | — |\n| GRPO bf16 G=8 (best step) | 45.59 | ~43.4 | +5.23pp | 80.86 | — | — |\n| GRPO QLoRA (lr=5e-6) | TBD | 1.38 | TBD | 85.00 | — | 0.9900 |\n\n注：Evi-F1 以百分比显示（×100）。Ign-F1 修正后排名无实质变化（仅 r2a/r2b 互换，差 0.09pp）。TBD 项等待 metrics_v2.json 补算。GRPO bf16 Ign-F1=45.59 > F1=43.4 因 train triples 过滤效应。RSFT CED k=3 数据来源: reeval_rsft_topk3 (ign_f1_corrected=true)。\n\n### D076 统一协议 rel_f1（可直接写入论文）\n\n| Config | rel_f1 | evi_f1 |\n|--------|--------|--------|\n| SFT baseline | 0.4049 | — |\n| CED RSFT mean (s42, s44) | **0.4569** | — |\n| CED RSFT s42 | 0.4517 | — |\n| CED RSFT s44 | 0.4621 | — |\n| flat-NLI RSFT mean (s42, s43_r2) | **0.4561** | — |\n| flat-NLI RSFT s42 | 0.4535 | — |\n| flat-NLI RSFT s43_r2 | 0.4586 | — |\n| LLaMA-8B SFT | 0.5514 | 0.8151 |\n| LLaMA-8B no-evidence | 0.5624 | — |\n\n### Evidence Tax Scaling（D079/D082/D083）\n\n| Model | Evidence Tax (Δ) | 方向 |\n|-------|-----------------|------|\n| Qwen3-1.7B | **+6.2pp** | BENEFIT（隐式正则化） |\n| Qwen3-4B | **-7.9pp** | cost |\n| Qwen3-8B | **≈0** | neutral |\n| LLaMA-3.1-8B | **-0.7pp** | near-neutral（跨家族确认） |\n\n### Cross-Dataset Validation（D080）\n\n| Dataset | Ign-F1 Δ | Evi-F1 | 说明 |\n|---------|----------|--------|------|\n| DocRED (in-domain) | baseline | — | — |\n| Re-DocRED | -3.15pp | 0.817 | evidence extraction 泛化，relation extraction 有损 |\n\n## Anticipated Reviewer Concerns (updated from Dream, D068-D083)\n\n### RC1: \"Online RL\" 标题过度声称（Dream 三档一致 Critical）\n- ~~标题和 claim 收窄到 \"GRPO fails for DocRE\"~~\n- **D068/D069 修正**: 重新定位为 \"RL optimization pressure correlates with decoupling severity\"——不是 GRPO 特有问题，而是 RL-for-IE 的通用梯度\n- DPO 数据支撑 decoupling spectrum（gradual decay confirms the pattern）\n\n### RC2: GRPO G=4 太小 + LoRA confound（Dream 三档一致 Major）\n- GRPO G=8 bf16 实验 ✅ — 确认 mild decoupling（-2pp），QLoRA 是 catastrophic amplifier（D065/D066）\n- LoRA confound 已解决：bf16 LoRA vs QLoRA 直接对比\n\n### RC3: CED 不显著优于 flat-NLI（Dream 三档一致 Major）\n- **已解决（D078）**: paired t-test p=0.44，CED 与 flat-NLI 统计不可区分\n- **应对**: 不再声称 CED > flat-NLI；论文定位为 \"NLI-based scoring 是关键（CED 和 flat-NLI 均有效），CED 因可解释性作为默认推荐\"\n- ~~5+ seeds 统计检验~~ → 不再需要，D078 已给出明确结论\n\n### RC4: RSFT 不新颖\n- 不声称 RSFT 是贡献；贡献在于任务定义 + decoupling 发现 + EDCR\n- 诚实定位 RSFT 为 STaR (NeurIPS 2022) 单轮变体 + domain-specific quality filter\n\n### RC12: SAIS 说 evidence 有用，为何 FREIGE 说 evidence 有害？（文献审查 2026-05-16）\n- **关键区分**: discriminative evidence *retrieval*（SAIS/DREEAM — 分类句子是否为证据，作为监督信号提升 RE）vs generative evidence *production*（FREIGE — LLM 生成完整证据文本，额外生成负担导致 scale-dependent 代价）\n- SAIS 的 evidence supervision 是分类任务，不增加输出长度；FREIGE 的 evidence generation 显著增加生成序列长度，模型需分配容量同时完成 RE + evidence 生成\n- **D079/D083 新弹药**: evidence tax 是 scale-dependent 的——1.7B 模型中 evidence 反而有益（+6.2pp），与 SAIS 的发现方向一致。这说明 evidence 的效果取决于模型容量和任务范式的交互，而非简单的有害/有益二分\n- **应对**: Related Work 中精准讨论此对比，明确 FREIGE 研究的是 *generative production* 设定下的代价，与 *retrieval* 设定下的增益不矛盾——两者揭示了 evidence 在不同范式下的不同角色\n\n### RC13: 单模型单数据集泛化性不足（D077 scope 扩展）\n- ~~plan_006: Qwen3-1.7B / 8B model size ablation~~ ✅ D079/D083 完成\n- ~~plan_016: LLaMA-3.1-8B cross-family validation~~ ✅ D082 完成\n- ~~plan_007: Re-DocRED cross-dataset evaluation~~ ✅ D080 完成\n- **结果**: 三项泛化实验全部完成，支撑 C5 scaling pattern + cross-family + cross-dataset 叙事\n\n### RC5: 评测可比性（D041）\n- DREEAM-protocol Evi-F1；conditional Evi-F1 作为辅助指标\n\n### RC6: EDCR 缺人工验证\n- 100 例小规模标注\n\n### RC7: Missing DPO/PPO（Dream 两档 Major）\n- DPO experiment ✅ — 结果确认 decoupling spectrum（D067/D068）\n\n### RC8: Dev-test degradation\n- 观察项，等 test set 数据\n\n### RC9: 连接 reward overoptimization 文献\n- 显式引用 Gao et al. 2023\n\n### RC10: Post-hoc evidence retrieval baseline\n- SFT + BM25 evidence retrieval\n\n### RC11: \"RL 不遗忘\" 文献与 Claim 2 的张力（文献扫描 2026-05-16）\n- 近期多篇论文（arXiv 2507.05386, 2506.23508, 2509.04259）论证 RL fine-tuning 天然缓解 catastrophic forgetting\n- **关键区分**: FREIGE 的 decoupling 是 **intra-task multi-objective trade-off**（RE 抽取 vs evidence 生成两个优化目标的竞争），不是 **inter-task forgetting**（丢失预训练知识）。两者机制不同\n- bf16 GRPO 的 mild decoupling（-2pp）恰好印证这一点：模型没有忘记\"怎么做 IE\"，而是在 evidence reward 压力下偏移了 RE-evidence 的资源分配\n- **应对**: Related Work / Discussion 中显式回应这组文献，区分 intra-task trade-off vs inter-task forgetting\n- **QuRL/QaRL 文献支撑 Claim 2**: QuRL 发现 quantized vs full-precision actor divergence 在长训练中指数增长（直接支撑 QLoRA amplification 叙事）；QaRL 的 error token failure mode 与 QLoRA GRPO garbled evidence 吻合\n\n## Key Baselines (12+)\n\n1. **SFT-only**: Qwen3-4B + LoRA SFT（with evidence）\n1b. **SFT no-evidence**: Qwen3-4B + LoRA SFT（无 evidence，upper bound ablation）\n2. **RSFT flat-NLI**: flat-NLI scored RSFT（核心 ablation）\n3. **RSFT CED**: CED scored RSFT（主方法）\n4. **CED-as-reranker**: 推理时 CED 重排（无训练）\n5. **DPO+CED**: offline preference learning — gradual decoupling（D067/D068）\n6. **GRPO+CED (QLoRA, G=4)**: catastrophic decoupling baseline\n7. **GRPO+CED (bf16, G=8)**: mild decoupling — QLoRA confound 排除（D065/D066）\n8. **Post-hoc retrieval**: SFT + BM25 evidence（NEW）\n9. **DREEAM**: encoder evidence SOTA\n10. **SAIS**: encoder evidence baseline\n11. **DocKS-RAG**: extraction SOTA（无 evidence）\n12. **LMRC**: generative LLM SOTA（无 evidence）\n\n## Publishability Threshold (revised after D078-D083)\n\n- **必要条件**: (1) RSFT 在 test set 上 Ign-F1 显著 > SFT (2) DREEAM-protocol Evi-F1 可报告 (3) Decoupling spectrum 有完整数据支撑（GRPO QLoRA/bf16 + DPO + RSFT）\n- **充分条件**: 上述 + EDCR 人工验证 + scaling pattern (C5) 完整\n- **已达成**: CED vs flat-NLI 统计检验完成（D078: 不可区分，不再是充分条件要素）; 泛化实验完成（D079/D080/D082/D083）\n- **Failure pivot**: decoupling spectrum 不成立（bf16 GRPO 也 catastrophic）→ scope 大幅缩减。**已排除**: bf16 GRPO 确认 mild（D065/D066）\n\n## Research Phase Priorities (revised after D078-D083)\n\n| Priority | 实验 | Claim | GPU-h |\n|----------|------|-------|-------|\n| ~~P0~~ | ~~flat-NLI RSFT ablation (5 seeds)~~ → D078 已结论 | C3 | — |\n| ~~P0~~ | ~~CED RSFT additional seeds (→5 total)~~ → D078 已结论 | C3 | — |\n| P0 | DREEAM-protocol Evi-F1 对齐 | C1 | CPU |\n| P0 | Test set evaluation | C1 | ~4h |\n| P0 | DREEAM baseline reproduction | C1 | ~8h |\n| ~~P0~~ | ~~GRPO G=8 experiment~~ ✅ | C2 | ~16h |\n| ~~P0~~ | ~~DPO+CED experiment~~ ✅ | C2 | ~12h |\n| ~~P0~~ | ~~EDCR per-relation analysis (D070)~~ ✅ | C4 | CPU |\n| ~~P0~~ | ~~Ign-F1 bugfix + data sync (D071)~~ ✅ | ALL | CPU |\n| ~~P0~~ | ~~Model size ablation (1.7B/8B)~~ ✅ D079/D083 | C5 | — |\n| ~~P0~~ | ~~LLaMA-3.1-8B cross-family~~ ✅ D082 | C5 | — |\n| ~~P0~~ | ~~Re-DocRED cross-dataset~~ ✅ D080 | C1/C5 | — |\n| P1 | EDCR human validation | C4 | API |\n| P1 | Post-hoc evidence retrieval baseline | C1 | ~4h |\n| P1 | CED-as-reranker (running) | C1 | ~6h |\n| ~~P0~~ | ~~GRPO forgetting dynamics figure (plan_009)~~ ✅ | C2 | ~2h |\n| ~~P0~~ | ~~SFT-without-evidence ablation (plan_014)~~ ✅ | C1 | ~8h |\n| P2 | Advantage variance measurement | C2 | CPU |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选\n    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py\n    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: eval_flat_nli_seed45\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.455052\n    ign_f1: 0.446181\n    evi_f1: 0.815399\n    edcr: 0.652133\n    evi_f1_joint: 0.355612\n- id: plan_002\n  claim: 1\n  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set\n    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_003\n  claim: 4\n  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing\n    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: plan_003_edcr_diagnostic\n  status: DONE\n  conclusion: success\n  metrics:\n    methods_evaluated: 15\n    edcr_vs_rel_f1_spearman: -0.9648\n    edcr_vs_rel_f1_pvalue: 0.0001\n    edcr_vs_evi_f1_spearman: 0.0022\n    edcr_vs_evi_f1_pvalue: 0.9941\n    edcr_range: 0.63-0.99\n    unique_diagnostic_value: identifies pathological models (GRPO QLoRA) with high\n      evi_f1 but catastrophically low rel_f1\n- id: plan_004\n  claim: 1\n  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)\n    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_004_dreeam_baseline\n  status: DONE\n  conclusion: success\n  metrics:\n    dev_rel_f1: 63.57\n    dev_rel_ign_f1: 61.72\n    dev_evi_f1: 54.01\n    dev_rel_p: 66.95\n    dev_rel_r: 60.51\n    dev_evi_p: 60.53\n    dev_evi_r: 48.76\n- id: plan_005\n  claim: 1\n  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: mvp2_ced_reranker_poc\n  status: DONE\n  conclusion: success\n  metrics:\n    ced_reranker_rel_f1: 0.486367\n    ced_reranker_ign_f1: 0.473634\n    ced_reranker_evi_f1: 0.8188\n    oracle_rel_f1: 0.623746\n    oracle_ign_f1: 0.612518\n    random_rel_f1: 0.453783\n    random_ign_f1: 0.439677\n- id: plan_006\n  claim: 1\n  description: 'Model size ablation (D077 升 P0): Qwen3-1.7B 和 Qwen3-8B 上复现 SFT → RSFT\n    → eval pipeline，验证 evidence tax + RSFT 增益 + decoupling 在不同模型规模下成立。应对 RC4 和 scope\n    不足问题。'\n  priority: P0\n  gpu_budget_hours: 32\n  deps: []\n  registry_id: plan_006_qwen3_1_7b_no_evidence_eval_v3\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.3982\n    rel_f1: 0.4103\n    evi_f1: 0\n    edcr: 0\n    precision: 0.4464\n    recall: 0.3796\n    format_compliance_rate: 1\n    n_truncated: 501\n    inference_time_seconds: 7465.3\n    evidence_tax: 0.0804\n- id: plan_007\n  claim: 1\n  description: 'Re-DocRED cross-dataset (D077 升 P0): 在 Re-DocRED 上用当前 best config\n    做 SFT → RSFT → eval。数据已就绪（格式与 DocRED 兼容，96 relation types 一致）。⚠️ Re-DocRED ~55%\n    triples 无 evidence 标注（修正的 false negative），必须报告两种模式：evidence_only（与 DocRED 可比的\n    evi_f1，仅 43% triples）+ full（全部 triples 的 rel_f1，无 evi_f1）。转换脚本已支持 --mode full。'\n  priority: P0\n  gpu_budget_hours: 16\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_016\n  claim: 2\n  description: 'LLaMA-3.1-8B cross-family validation (D077 新增): 在非 Qwen 家族模型上复现核心\n    pipeline (SFT → RSFT → GRPO QLoRA)，验证 decoupling spectrum 跨模型家族成立。关键实验：LLaMA GRPO\n    QLoRA 是否也出现 catastrophic forgetting。'\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  registry_id: plan_016_llama_rsft_candidates\n  status: DONE\n  conclusion: failed\n- id: plan_008\n  claim: 2\n  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格\n    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: reeval_rsft_topk3\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.4454\n    rel_precision: 0.4512\n    rel_recall: 0.4398\n    ign_f1: 0.4364\n    evi_f1: 0.8088\n    edcr: 0.6635\n    format_ok_rate: 0.999\n    n_truncated: 214\n    n_predictions: 16020\n    inference_time_seconds: 3546.4\n    ign_f1_corrected: true\n- id: plan_011\n  claim: 3\n  description: 'GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward\n    + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要\n    gradient_accumulation 适配显存。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_011_bf16_g8_step_eval\n  status: DONE\n  conclusion: success\n  metrics:\n    step_30:\n      rel_f1: 0.434\n      evi_f1: 0.8063\n      edcr: 0.6807\n    step_50:\n      rel_f1: 0.4276\n      evi_f1: 0.8024\n      edcr: 0.6855\n    step_70:\n      rel_f1: 0.4341\n      evi_f1: 0.8099\n      edcr: 0.6685\n    best_step: step_70\n    trend: non-monotonic, all < ckpt-100 (0.4549)\n- id: plan_012\n  claim: 3\n  description: 'DPO+CED experiment: 用 RSFT 候选数据构造 preference pairs (CED-preferred\n    vs CED-rejected)，DPO 训练。验证 DPO 是否避免 GRPO 的 catastrophic forgetting。Dream v2 三档要求\n    DPO 作为 RL spectrum 关键数据点，必须补全训练超参（β, lr, epochs, pair construction）。D045 升 P0。'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: plan_012_dpo_ced\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.3429\n    evi_f1: 0.8403\n    edcr: 0.7294\n    format_ok_rate: 0.995\n    checkpoint: checkpoint-501\n    rewards_accuracy: 1\n    margins: 9.01\n- id: plan_013\n  claim: 4\n  description: 'EDCR 人工标注验证: 100 个样本，人工判断每个 cited evidence sentence 是否真正支持对应 relation。计算\n    EDCR 与人工判断的相关性，验证 EDCR 作为自动指标的有效性。Dream [M][W] 一致要求。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_009\n  claim: 3\n  description: 'GRPO forgetting dynamics figure: 整理全部 GRPO checkpoint（42个）的 rel_f1/evi_f1/EDCR/reward\n    轨迹，绘制 training dynamics 可视化图。包含 G=4 vs G=8 对比、三种 reward 对比。Dream v2 三档一致要求此图作为论文核心\n    figure。数据已有，只需汇总+画图。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: plan_009_dynamics_figure\n  status: DONE\n  conclusion: success\n- id: plan_010\n  claim: 1\n  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer\n    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_014\n  claim: 1\n  description: 'SFT-without-evidence ablation: 训练 Qwen3-4B SFT 只输出 relation triples（不含\n    evidence sentences），对比标准 SFT（含 evidence）的 rel_f1。隔离 evidence generation 对抽取性能的代价。Dream\n    v2 三档一致要求。用于回答\"43.2% vs LMRC 60.7% 的 gap 有多少来自 evidence 生成负担\"。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_014_sft_no_evidence\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.7077\n    eval_loss: 0.8781\n    eval_token_accuracy: 0.8086\n    epochs: 3\n    total_steps: 570\n    train_runtime_min: 64\n    samples: 3027\n    trainable_params: 132M/4.15B (3.18%)\n- id: plan_015\n  claim: 2\n  description: 'bf16 LoRA GRPO clean control: 与原始 GRPO (QLoRA 4-bit, G=4, kl=0, CED\n    reward) 只改一个变量——quantization 从 QLoRA 4-bit 改为 bf16 LoRA。G=4, kl_coef=0 不变。目的:\n    隔离 QLoRA confound，判断 decoupling 是 QLoRA artifact 还是 genuine RL-for-IE 现象。Dream\n    v2 三档一致的 critical 要求。如 decoupling 在 bf16 下仍持续 → 可泛化 claim；如消失 → QLoRA 特定，需 re-scope。优先级取决于\n    plan_011 eval 结果。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_011\n  registry_id: plan_015_grpo_g4_bf16_v3\n  status: DONE\n  conclusion: killed\n- id: plan_mvp1\n  claim: 1\n  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing\n    distractor 的能力验证'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: mvp1_ced_signal\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_margin: 0.48\n    discrimination_accuracy: 0.815\n    pearson_r_margin_jaccard: 0.34\n    pass: true\n- id: plan_mvp2_sft\n  claim: 1\n  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mvp2_sft_warmup\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.72\n    accuracy: 0.835\n- id: plan_mvp2_rsft\n  claim: 1\n  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部\n    PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087,\n    r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_mvp1\n  - plan_mvp2_sft\n  registry_id: mvp2_rsft_train_r1\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.0483\n    num_preds: 848\n    sft_baseline_rel_f1: 0.4057\n    failure_mode: relation_ontology_collapse_to_freetext\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n- id: plan_mvp2_grpo\n  claim: 3\n  description: 'GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1\n    max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic\n    forgetting。D031/D033 完整轨迹支撑 Claim 3'\n  priority: P0\n  gpu_budget_hours: 60\n  deps:\n  - plan_mvp2_sft\n  registry_id: mvp2_grpo_ced_lr5e6_r1\n  status: DONE\n  conclusion: killed\n\n\n## registry (completed experiments)\n\n- exp_id: mvp1_ced_signal\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_margin: 0.48\n    discrimination_accuracy: 0.815\n    pearson_r_margin_jaccard: 0.34\n    pass: true\n- exp_id: smoke_test_grpo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_sft_warmup\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.72\n    accuracy: 0.835\n- exp_id: precompute_nli_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_grpo_ced\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_extract\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_sft_eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_extract_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: mvp2_grpo_extract_r3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_sft_eval_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    ign_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    precision: 0.4043\n    recall: 0.407\n    evi_precision: 0.8035\n    evi_recall: 0.7924\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.626\n    n_parseable: 617\n    n_truncated: 367\n    n_predictions: 18815\n    inference_time_seconds: 6484.7\n- exp_id: mvp2_sft_eval_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    ign_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    precision: 0.4043\n    recall: 0.407\n    evi_precision: 0.8035\n    evi_recall: 0.7924\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.626\n    n_parseable: 617\n    n_truncated: 367\n    n_predictions: 18815\n- exp_id: mvp2_grpo_ced_kl001_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001_r3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001_r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_step: 100\n    train_runtime_s: 9069.88\n    reward_final: 1.195\n    f1_reward_final: 0.573\n    ced_reward_final: 0.328\n    format_reward_final: 0.293\n    frac_zero_std_final: 0.2\n    kl_final: 0.118\n    loss_final: -0.009\n    grad_norm_final: 0.14\n    entropy_final: 0.067\n    completion_length_mean_final: 520.8\n    best_reward_step: 90\n    best_reward: 1.37\n    best_f1_reward: 0.72\n    best_ced_reward: 0.353\n- exp_id: mvp2_grpo_extract_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_early\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    f1: 0.1563\n    ign_f1: 0.1563\n    evi_f1: 0.5643\n    edcr: 0.8858\n    precision: 0.2356\n    recall: 0.1169\n    evi_precision: 0.4864\n    evi_recall: 0.6721\n    format_ok_rate: 0.999\n    n_parseable: 984\n    n_truncated: 11\n    n_predictions: 9250\n    tp: 1421\n    pred_count: 6032\n    gold_count: 12151\n- exp_id: mvp2_grpo_flatnli_r6\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    steps_completed: 25\n    final_frac_zero_std: 0.9\n    final_f1_reward: 0\n    final_flat_nli_reward: 0\n    final_format_reward: 0.293\n    collapse_step: 25\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.00296\n    rel_precision: 0.00314\n    rel_recall: 0.0028\n    evi_f1: 0.72\n    evi_precision: 0.6429\n    evi_recall: 0.8182\n    edcr: 0.9983\n    n_parseable: 984\n    n_truncated: 24\n    n_predictions: 11621\n    tp: 34\n    pred_count: 10839\n    gold_count: 12151\n    inference_time_seconds: 5211.4\n- exp_id: mvp2_eval_ced_kl001_r4_multi\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    checkpoint-10:\n      f1: 0.003\n      ign_f1: 0.003\n      evi_f1: 0.72\n      edcr: 0.9983\n      format_ok_rate: 0.999\n    checkpoint-20:\n      f1: 0.0088\n      ign_f1: 0.0088\n      evi_f1: 0.423\n      edcr: 0.9954\n      format_ok_rate: 0.999\n    checkpoint-30:\n      f1: 0.0338\n      ign_f1: 0.0338\n      evi_f1: 0.5889\n      edcr: 0.9798\n      format_ok_rate: 1\n    checkpoint-50:\n      f1: 0.1563\n      ign_f1: 0.1563\n      evi_f1: 0.5643\n      edcr: 0.8858\n      format_ok_rate: 0.999\n    checkpoint-60:\n      f1: 0.1467\n      ign_f1: 0.1467\n      evi_f1: 0.5763\n      edcr: 0.9062\n      format_ok_rate: 1\n    checkpoint-90:\n      f1: 0.2108\n      ign_f1: 0.2108\n      evi_f1: 0.5666\n      edcr: 0.8584\n      format_ok_rate: 1\n- exp_id: mvp2_eval_ced_kl001_r4_step100\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.2167\n    ign_f1: 0.2167\n    precision: 0.2849\n    recall: 0.1749\n    evi_f1: 0.5746\n    evi_precision: 0.5244\n    evi_recall: 0.6353\n    edcr: 0.8539\n    pred_count: 7460\n    gold_count: 12151\n    tp: 2125\n    n_truncated: 21\n    format_ok_rate: 1\n- exp_id: mvp2_eval_ced_kl001_r4_last\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt90\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_high\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    checkpoint_60:\n      rel_f1: 0.1467\n      ign_f1: 0.1467\n      precision: 0.1909\n      recall: 0.1192\n      evi_f1: 0.5763\n      edcr: 0.9062\n      pred_count: 10041\n      gold_count: 12151\n      n_truncated: 16\n      format_ok_rate: 1\n    note: Only ckpt-60 completed. Process died during ckpt-70 inference at 8% (5/62\n      batch). ckpt-80/90 never started.\n- exp_id: mvp2_eval_ced_kl001_r4_step90\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.2108\n    ign_f1: 0.2108\n    evi_f1: 0.5666\n    edcr: 0.8584\n    pred_count: 11160\n    n_truncated: 22\n    format_ok_rate: 1\n    n_documents: 985\n- exp_id: mvp2_grpo_ced_lr5e6_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_p1_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_rp_r1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt7080\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_rp_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt20\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0077\n    rel_precision: 0.0071\n    rel_recall: 0.0084\n    evi_f1: 0.628\n    evi_precision: 0.855\n    evi_recall: 0.496\n    edcr: 0.993\n    format_ok_rate: 0.991\n    field_compliance_rate: 0.399\n    pred_count: 14440\n    gold_count: 12151\n    tp: 102\n    n_truncated: 587\n    inference_time_seconds: 6370.4\n- exp_id: mvp2_eval_lr5e6_r1_ckpt40\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt40_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0071\n    precision: 0.0066\n    recall: 0.0078\n    evi_f1: 0.7584\n    evi_precision: 0.9113\n    evi_recall: 0.6494\n    edcr: 0.9942\n    format_ok_rate: 0.9939\n    field_compliance_rate: 0.5675\n    pred_count: 14434\n    gold_count: 12151\n    tp: 95\n    n_truncated: 424\n    inference_time_seconds: 6152\n- exp_id: mvp2_eval_lr5e6_rp_r2_ckpt20\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_sft_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    evi_f1: 0.7979\n    evi_f1_joint: 0.3117\n    evi_f1_joint_P: 0.3037\n    evi_f1_joint_R: 0.32\n    edcr: 0.7118\n    pred_count: 12234\n    gold_count: 12151\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.998\n    field_compliance_rate: 0.6264\n    n_truncated: 367\n    inference_time_seconds: 6138.5\n- exp_id: mvp2_eval_lr5e6_r1_ckpt60\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt80\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0116\n    ign_f1: 0.0116\n    precision: 0.0109\n    recall: 0.0124\n    evi_f1: 0.828\n    evi_precision: 0.928\n    evi_recall: 0.748\n    edcr: 0.993\n    format_ok_rate: 0.999\n    field_compliance_rate: 0.788\n    pred_count: 13828\n    gold_count: 12151\n    n_truncated: 210\n    inference_time_seconds: 6099\n- exp_id: mvp2_eval_lr5e6_r1_ckpt60_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0093\n    precision: 0.0085\n    recall: 0.0103\n    evi_f1: 0.81\n    edcr: 0.993\n    format_ok_rate: 0.998\n    pred_count: 14626\n    gold_count: 12151\n    tp: 125\n    inference_time_seconds: 6152\n- exp_id: mvp2_eval_lr5e6_r1_ckpt100\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0138\n    rel_precision: 0.0132\n    rel_recall: 0.0144\n    ign_f1: 0.0138\n    evi_f1: 0.8504\n    evi_precision: 0.9256\n    evi_recall: 0.7866\n    edcr: 0.9876\n    format_ok_rate: 0.999\n    field_compliance_rate: 0.8162\n    evidence_format_rate: 0.8162\n    tp: 175\n    pred_count: 13300\n    gold_count: 12151\n    n_predictions: 15498\n    n_truncated: 181\n    n_documents: 985\n    n_parseable: 984\n    inference_time_seconds: 5901.7\n- exp_id: mvp2_diversity_probe\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    unique_triples_t07: 5\n    unique_triples_t10: 8\n    jaccard_t07: 0.17\n    jaccard_t10: 0.051\n    format_ok_rate_t07: 0.5\n    format_ok_rate_t10: 0.438\n    n_samples: 3\n    n_generations: 8\n    note: 'unique_triples_t07 corrected from 7 to 5.0 (mean). Reviewer: format_ok\n      ~34% after fix, ''diversity'' was JSON key name variants not semantic diversity'\n- exp_id: mvp2_rsft_generate\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    generation_count: 5288\n    unique_docs: 659\n    format_compliance: 0.998\n    diversity_range: 7.5-7.8/8\n    exit_code: 0\n- exp_id: mvp2_rsft_ced_scoring\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    input_generations: 21952\n    selected_samples: 2718\n    unique_docs: 2691\n    selection_rate: 0.124\n    mean_f1: 0.6157\n    mean_ced: 0.6683\n    f1_range:\n    - 0.1026\n    - 1\n    zero_f1_samples: 0\n    selection_strategy: top_k=1\n    f1_threshold: 0.1\n- exp_id: mvp2_rsft_train_r1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.0483\n    num_preds: 848\n    sft_baseline_rel_f1: 0.4057\n    failure_mode: relation_ontology_collapse_to_freetext\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n- exp_id: mvp2_rsft_train_r1_s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.7622\n    train_loss: 0.6148\n    eval_entropy: 0.6724\n    mean_token_accuracy: 0.8291\n    total_steps: 510\n    epochs: 3\n    training_hours: 1.99\n- exp_id: mvp2_rsft_train_r1_s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4655\n    evi_f1: 0.8087\n    evi_f1_joint: 0.3713\n    evi_f1_joint_P: 0.3775\n    evi_f1_joint_R: 0.3653\n    edcr: 0.635\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0598\n    delta_evi_f1: 0.0108\n    delta_evi_f1_joint: 0.0596\n    mvp2_pass: true\n- exp_id: mvp2_rsft_ced_scoring_topk3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_s44\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_ced_reranker_poc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ced_reranker_rel_f1: 0.486367\n    ced_reranker_ign_f1: 0.473634\n    ced_reranker_evi_f1: 0.8188\n    oracle_rel_f1: 0.623746\n    oracle_ign_f1: 0.612518\n    random_rel_f1: 0.453783\n    random_ign_f1: 0.439677\n- exp_id: mvp2_rsft_diagnosis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    root_cause: overfitting_plus_sft_knowledge_overwrite\n    truncated_json_samples: 170\n    truncated_pct: 6.3\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n    lora_scaling: 2\n    rsft_zero_relation_samples: 170\n    sft_zero_relation_docs: 26\n    rsft_mean_relations: 11.2\n    sft_mean_relations: 12.5\n- exp_id: mvp2_rsft_train_r2_fix\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_rsft_r2a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4494\n    evi_f1: 0.8108\n    edcr: 0.6641\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0437\n    delta_evi_f1: 0.0129\n    mvp2_pass: true\n- exp_id: mvp2_rsft_r2b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4493\n    evi_f1: 0.8128\n    edcr: 0.6609\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0436\n    delta_evi_f1: 0.0149\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4449\n    evi_f1: 0.8187\n    evi_f1_joint: 0.3468\n    evi_f1_joint_P: 0.3515\n    evi_f1_joint_R: 0.3423\n    edcr: 0.6565\n    num_preds: 15307\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0392\n    delta_evi_f1: 0.0208\n    delta_evi_f1_joint: 0.0351\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r2a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4494\n    ign_f1: 0.4494\n    evi_f1: 0.8108\n    evi_f1_joint: 0.3509\n    evi_f1_joint_P: 0.3423\n    evi_f1_joint_R: 0.3599\n    edcr: 0.6641\n    precision: 0.4512\n    recall: 0.4475\n    evi_precision: 0.8143\n    evi_recall: 0.8073\n    format_ok_rate: 1\n    n_predictions: 15482\n    n_truncated: 208\n    inference_time_s: 5967.2\n    delta_evi_f1_joint: 0.0392\n- exp_id: mvp2_eval_rsft_r2b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4493\n    ign_f1: 0.4493\n    evi_f1: 0.8128\n    evi_f1_joint: 0.349\n    evi_f1_joint_P: 0.3455\n    evi_f1_joint_R: 0.3526\n    edcr: 0.6609\n    precision: 0.4566\n    recall: 0.4424\n    evi_precision: 0.8201\n    evi_recall: 0.8056\n    pred_count: 14829\n    format_ok: 983/985\n    truncated: 179\n    inference_time_s: 5862\n    delta_evi_f1_joint: 0.0373\n- exp_id: mvp2_eval_rsft_s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_s43_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4683\n    ign_f1: 0.4683\n    evi_f1: 0.8156\n    evi_f1_joint: 0.3711\n    evi_f1_joint_P: 0.3747\n    evi_f1_joint_R: 0.3675\n    edcr: 0.6388\n    precision: 0.4817\n    recall: 0.4556\n    evi_precision: 0.8142\n    evi_recall: 0.817\n    n_predictions: 14970\n    n_truncated: 171\n    format_ok_rate: 1\n    inference_time_s: 6316.7\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0626\n    delta_evi_f1: 0.0177\n    delta_evi_f1_joint: 0.0594\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r2b_maxtok1536\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_r2b_maxtok1536_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.4504\n    ign_f1: 0.4504\n    evi_f1: 0.8102\n    edcr: 0.674\n    precision: 0.4488\n    recall: 0.4519\n    evi_precision: 0.8162\n    evi_recall: 0.8044\n    n_truncated: 146\n    n_total: 985\n    n_predictions: 17188\n    n_distractor_citations: 19589\n    n_total_citations: 29063\n    format_ok_rate: 0.998\n- exp_id: mvp2_rsft_ced_scoring_topk3_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    input_generations: 21728\n    selected_samples: 8037\n    unique_docs: 2691\n    selection_rate: 0.37\n    mean_f1: 0.5761\n    mean_ced: 0.6205\n    mean_combined: 0.6787\n    f1_range_p25: 0.444\n    f1_range_p75: 0.717\n    ced_range_p25: 0.487\n    ced_range_p75: 0.774\n    truncated_samples: 1924\n    truncated_pct: 8.9\n    selection_strategy: top_k=3\n    f1_threshold: 0.1\n    topk1_samples: 2718\n    data_multiplier: 2.96\n- exp_id: plan_004_dreeam_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dev_rel_f1: 63.57\n    dev_rel_ign_f1: 61.72\n    dev_evi_f1: 54.01\n    dev_rel_p: 66.95\n    dev_rel_r: 60.51\n    dev_evi_p: 60.53\n    dev_evi_r: 48.76\n- exp_id: plan_011_grpo_g8_bf16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_step: 100\n    train_runtime_s: 554\n    reward_final: 1.795\n    f1_reward_final: 1.002\n    ced_reward_final: 0.494\n    format_reward_final: 0.3\n    frac_zero_std_final: 0\n    kl_final: 0.022\n    best_reward_step: 85\n    best_reward: 2.858\n    best_f1_reward: 1.85\n    mode_collapse: false\n    lora_config: r=64, alpha=128, dropout=0.05, bf16\n    checkpoints: 10 checkpoints (step 10-100)\n- exp_id: plan_001_flat_nli_scoring\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_scored: 21728\n    selected_samples: 2691\n    selection_rate: 0.124\n    selection_strategy: top_k=1\n    f1_threshold: 0.1\n    output_path: /root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl\n- exp_id: eval_grpo_g8_bf16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ckpt80_rel_f1: 0.4456\n    ckpt80_ign_f1: 0.4456\n    ckpt80_evi_f1: 0.8034\n    ckpt80_edcr: 0.6409\n    ckpt80_format_ok: 984/985\n    ckpt80_truncated: 50\n    ckpt90_rel_f1: 0.4523\n    ckpt90_ign_f1: 0.4523\n    ckpt90_evi_f1: 0.8052\n    ckpt90_edcr: 0.6414\n    ckpt90_format_ok: 983/985\n    ckpt90_truncated: 61\n    ckpt100_rel_f1: 0.4549\n    ckpt100_ign_f1: 0.4549\n    ckpt100_evi_f1: 0.8086\n    ckpt100_edcr: 0.6318\n    ckpt100_format_ok: 985/985\n    ckpt100_truncated: 61\n    best_checkpoint: ckpt-100\n- exp_id: plan_011_eval_g8_bf16_ckpt100\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_011_grpo_g8_bf16_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4549\n    ign_f1: 0.4549\n    evi_f1: 0.8086\n    edcr: 0.6318\n    format_ok_rate: 1\n    n_truncated: 61\n    n_total: 985\n    n_predictions: 10701\n    checkpoint: checkpoint-100\n    model: Qwen3-4B + SFT merged + GRPO bf16 LoRA ckpt-100\n    inference_time_s: 3170.3\n- exp_id: plan_001_rsft_flat_nli\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.6238\n    train_loss_min: 0.5803\n    mean_token_accuracy: 0.8528\n    train_runtime_sec: 2946\n    epochs: 3\n    total_steps: 507\n    samples: 2691\n- exp_id: plan_012_dpo_ced\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.3429\n    evi_f1: 0.8403\n    edcr: 0.7294\n    format_ok_rate: 0.995\n    checkpoint: checkpoint-501\n    rewards_accuracy: 1\n    margins: 9.01\n- exp_id: plan_014_sft_no_evidence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.7077\n    eval_loss: 0.8781\n    eval_token_accuracy: 0.8086\n    epochs: 3\n    total_steps: 570\n    train_runtime_min: 64\n    samples: 3027\n    trainable_params: 132M/4.15B (3.18%)\n- exp_id: plan_015_grpo_g4_bf16\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_015_grpo_g4_bf16_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_015_grpo_g4_bf16_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: eval_plan_001_flat_nli\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4539\n    ign_f1: 0.4539\n    evi_f1: 0.8043\n    edcr: 0.6431\n    precision: 0.4671\n    recall: 0.4414\n    evi_precision: 0.8143\n    evi_recall: 0.7945\n    format_ok_rate: 1\n    n_truncated: 199\n    n_documents: 985\n    n_predictions: 15294\n    inference_time_seconds: 3631\n- exp_id: eval_plan_014_sft_no_evidence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4893\n    rel_ign_f1: 0.4893\n    rel_precision: 0.4884\n    rel_recall: 0.4902\n    evi_f1: 0\n    evi_precision: 0\n    evi_recall: 0\n    edcr: 0\n    format_ok_rate: 0.9919\n    n_truncated: 298\n    n_predictions: 21064\n    n_documents: 985\n    n_parseable: 977\n    inference_time_seconds: 4103.8\n- exp_id: plan_008_rsft_topk3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.5543\n    eval_loss: 0.8297\n    eval_mean_token_accuracy: 0.8228\n    eval_entropy: 0.6001\n    train_runtime_sec: 10916\n    total_steps: 1509\n    epochs: 3\n    trainable_params_pct: 3.18\n    rsft_samples: 8037\n    ced_score_mean: 0.621\n    task_eval_f1_ep1: 0.4848\n    task_eval_f1_ep2: 0.4824\n    task_eval_f1_ep3: 0.5012\n    task_eval_evi_f1_ep1: 0.745\n    task_eval_evi_f1_ep2: 0.6997\n    task_eval_evi_f1_ep3: 0.6816\n    task_eval_edcr_ep1: 0.6525\n    task_eval_edcr_ep2: 0.6529\n    task_eval_edcr_ep3: 0.5963\n    task_eval_note: 50-doc subset, not full dev\n- exp_id: plan_002_test_eval_s44\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_001_flat_nli_seed43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss_final: 0.6257\n    train_loss_min: 0.5895\n    eval_loss_epoch3: 0.7567\n    eval_accuracy_epoch3: 0.8298\n    total_steps: 507\n    epochs: 3\n    train_runtime_seconds: 6880\n    task_eval_f1_ep1: 0.4825\n    task_eval_f1_ep2: 0.4542\n    task_eval_f1_ep3: 0.4866\n    task_eval_evi_f1_ep3: 0.7834\n    task_eval_edcr_ep3: 0.6402\n    task_eval_note: 50-doc subset, not full dev\n- exp_id: eval_sft_baseline_noquant\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4106\n    rel_precision: 0.4198\n    rel_recall: 0.4019\n    evi_f1: 0.8013\n    evi_precision: 0.8005\n    evi_recall: 0.8022\n    evi_f1_joint: 0.3216\n    edcr: 0.7039\n    format_ok_rate: 0.998\n    field_compliance_rate: 0.7066\n    n_predictions: 16774\n    n_truncated: 288\n    n_documents: 985\n    inference_time_seconds: 3677.9\n- exp_id: plan_012_dpo_ced_1ep\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0022\n    evi_f1: 0.75\n    edcr: 0.9982\n    format_ok: 981/985\n    truncated: 358/985\n    tp: 34\n    n_preds: 19265\n    inference_time_s: 3643\n    train_loss_final: 0.59\n    rewards_accuracy: 0.82\n    rewards_margins: 0.86\n    total_steps: 167\n    training_time_min: 33\n- exp_id: plan_009_forgetting_figure\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_011_bf16_g8_step_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    step_30:\n      rel_f1: 0.434\n      evi_f1: 0.8063\n      edcr: 0.6807\n    step_50:\n      rel_f1: 0.4276\n      evi_f1: 0.8024\n      edcr: 0.6855\n    step_70:\n      rel_f1: 0.4341\n      evi_f1: 0.8099\n      edcr: 0.6685\n    best_step: step_70\n    trend: non-monotonic, all < ckpt-100 (0.4549)\n- exp_id: plan_009_extract_reward_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_009_flatnli_reward_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: eval_plan_012_dpo_ced_ckpt400\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_009_flatnli_reward_eval_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: eval_plan_012_dpo_ced_1ep\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0022\n    ign_f1: 0.0022\n    evi_f1: 0.75\n    edcr: 0.9982\n    num_preds: 19265\n    format_ok: 981/985\n    truncated: 358/985\n    tp: 34\n    inference_time_s: 3643\n- exp_id: eval_plan_001_flat_nli_s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    rel_f1: 0.0022\n    ign_f1: 0.0022\n    evi_f1: 0.8533\n    edcr: 0.9982\n    num_preds: 17285\n    format_ok: 981/985\n    truncated: 251/985\n    tp: 32\n    note: INVALID — missing --sft_adapter, same bug as DPO 1ep eval\n- exp_id: plan_001_flat_nli_seed45\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    task_eval_rel_f1: 0.4876\n    task_eval_evi_f1: 0.7927\n    task_eval_edcr: 0.6517\n    train_loss: 0.6245\n    runtime_hours: 1.69\n    note: task-eval on 50 docs only, full dev eval needed\n- exp_id: eval_plan_008_rsft_topk3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    note: INVALID — missing --sft_adapter, killed by Director instruction\n- exp_id: plan_001_flat_nli_seed44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.6247\n    eval_loss: 0.7564\n    eval_mean_token_accuracy: 0.8299\n    task_eval_f1_ep1: 0.4306\n    task_eval_f1_ep2: 0.4884\n    task_eval_f1_ep3: 0.4897\n    task_eval_evi_f1_ep3: 0.78\n    task_eval_edcr_ep3: 0.6596\n    task_eval_ign_f1_ep3: 0.4897\n    train_runtime_sec: 6197\n    num_epochs: 3\n    total_steps: 507\n- exp_id: eval_plan_012_dpo_1ep_fixed\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: eval_plan_008_topk3_fixed\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: eval_plan_012_dpo_1ep_fixed_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.4034\n    evi_f1: 0.8088\n    edcr: 0.7139\n    format_ok_rate: 0.999\n    truncated_rate: 0.343\n    predictions: 19107\n    ign_f1: 0.4034\n    precision: 0.3809\n    recall: 0.4287\n    vs_sft_delta: -0.0023\n    note: DPO 1ep matches SFT baseline. 1ep→3ep trajectory shows gradual decoupling\n      (rel_f1↓ evi_f1↑), consistent with GRPO pattern. Ign-F1=F1 exact match needs\n      investigation.\n- exp_id: reeval_flat_nli_s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4523\n    ign_f1: 0.4523\n    evi_f1: 0.8158\n    edcr: 0.6505\n    num_preds: 15357\n    format_ok: 984/985\n    truncated: 211/985\n    inference_time_s: 3515.8\n- exp_id: reeval_rsft_topk3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.4454\n    rel_precision: 0.4512\n    rel_recall: 0.4398\n    ign_f1: 0.4364\n    evi_f1: 0.8088\n    edcr: 0.6635\n    format_ok_rate: 0.999\n    n_truncated: 214\n    n_predictions: 16020\n    inference_time_seconds: 3546.4\n    ign_f1_corrected: true\n- exp_id: eval_flat_nli_seed44\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: eval_flat_nli_seed45\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.455052\n    ign_f1: 0.446181\n    evi_f1: 0.815399\n    edcr: 0.652133\n    evi_f1_joint: 0.355612\n- exp_id: plan_003_edcr_diagnostic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    methods_evaluated: 15\n    edcr_vs_rel_f1_spearman: -0.9648\n    edcr_vs_rel_f1_pvalue: 0.0001\n    edcr_vs_evi_f1_spearman: 0.0022\n    edcr_vs_evi_f1_pvalue: 0.9941\n    edcr_range: 0.63-0.99\n    unique_diagnostic_value: identifies pathological models (GRPO QLoRA) with high\n      evi_f1 but catastrophically low rel_f1\n- exp_id: eval_flat_nli_s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.461506\n    ign_f1: 0.452126\n    evi_f1: 0.813123\n    edcr: 0.645808\n    evi_f1_joint: 0.359673\n- exp_id: plan_009_dynamics_figure\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: eval_plan_014_no_evidence\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: rsft_ced_s45_train\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: rsft_ced_s43_train\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: rsft_ced_s45_train_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: rsft_ced_s43_train_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: rsft_ced_s43_train_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.6151\n    eval_loss: 0.7618\n    task_eval_f1: 0.5026\n    task_eval_ign_f1: 0.4932\n    task_eval_evi_f1: 0.7624\n    task_eval_edcr: 0.6516\n    total_steps: 510\n    epochs: 3\n    training_hours: 1.82\n- exp_id: rsft_ced_s45_train_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: rsft_ced_s45_train_r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    training_completed: true\n    checkpoint: checkpoint-510\n    note: Training metrics not captured (r4 retry after OOM). Eval running as eval_rsft_ced_s45.\n- exp_id: eval_rsft_ced_s45\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4514\n    ign_f1: 0.4416\n    evi_f1: 0.8174\n    rel_p: 0.4718\n    rel_r: 0.4326\n    edcr: 0.655\n    evi_f1_joint: 0.3558\n    n_truncated: 206\n    format_ok_rate: 1\n- exp_id: eval_rsft_ced_s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4601\n    ign_f1: 0.4512\n    precision: 0.4696\n    recall: 0.4509\n    evi_f1: 0.8063\n    evi_precision: 0.8025\n    evi_recall: 0.8101\n    edcr: 0.6542\n    evi_f1_joint: 0.3605\n    format_ok_rate: 1\n    n_truncated: 184\n    n_predictions: 15051\n    inference_time_seconds: 10768.2\n- exp_id: eval_plan_014_no_evidence_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4876\n    ign_f1: 0.4721\n    evi_f1: 0\n    edcr: 0\n    evi_f1_joint: 0\n    precision: 0.4901\n    recall: 0.4851\n    ign_precision: 0.4654\n    ign_recall: 0.4791\n    format_compliance: 0.993\n    truncation_rate: 0.312\n    n_predictions: 21181\n    n_documents: 985\n- exp_id: reeval_flat_nli_s43_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4586\n    rel_precision: 0.4732\n    rel_recall: 0.4449\n    ign_f1: 0.4503\n    evi_f1: 0.8113\n    evi_precision: 0.8035\n    evi_recall: 0.8192\n    evi_f1_joint: 0.358\n    edcr: 0.6552\n    format_ok_rate: 0.999\n    n_truncated: 184\n    n_predictions: 15015\n- exp_id: seed_comparison_prep\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: reeval_ced_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.4423\n    rel_f1: 0.4517\n    evi_f1: 0.8175\n    evi_f1_joint: 0.3518\n    edcr: 0.6569\n    format_compliance_rate: 1\n    field_compliance_rate: 0.7756\n    n_truncated: 214\n    inference_time_seconds: 10815.5\n- exp_id: reeval_ced_s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.4511\n    rel_f1: 0.4621\n    evi_f1: 0.805\n    evi_f1_joint: 0.3677\n    edcr: 0.635\n    format_compliance_rate: 1\n    field_compliance_rate: 0.802\n    n_truncated: 190\n    inference_time_seconds: 13077.6\n- exp_id: reeval_flat_nli_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.4448\n    rel_f1: 0.4535\n    evi_f1: 0.8039\n    evi_f1_joint: 0.3558\n    edcr: 0.6458\n    format_compliance_rate: 1\n    field_compliance_rate: 0.7787\n    n_truncated: 205\n    inference_time_seconds: 13253.1\n- exp_id: reeval_sft_baseline_d076\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4049\n    ign_f1: 0.3974\n    evi_f1: 0.7986\n    edcr: 0.6982\n    evi_f1_joint: 0.3147\n    format_compliance_rate: 0.998\n    n_truncated: 288\n    n_documents: 985\n    n_predictions: 16880\n    inference_time_sec: 7056.5\n- exp_id: plan_006_qwen3_1_7b_sft\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_006_qwen3_1_7b_sft_bf16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.6884\n    eval_loss: 0.8031\n    eval_mean_token_accuracy: 0.8238\n    eval_entropy: 0.682\n    train_runtime_sec: 2473\n    train_samples_per_second: 3.672\n    epochs: 3\n    total_steps: 570\n- exp_id: plan_006_qwen3_1_7b_no_evidence_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_006_qwen3_8b_sft_bf16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.5705\n    eval_loss: 0.7186\n    eval_mean_token_accuracy: 0.8377\n    eval_entropy: 0.5614\n    train_runtime_s: 3932\n    epoch: 3\n- exp_id: plan_006_qwen3_1_7b_sft_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    f1: 0.4945\n    ign_f1: 0.4786\n    evi_f1: 0.8316\n    edcr: 0.6704\n    precision: 0.5085\n    recall: 0.4813\n    ign_precision: 0.483\n    ign_recall: 0.4743\n    evi_precision: 0.8203\n    evi_recall: 0.8432\n    evi_f1_joint: 0.3958\n    format_compliance_rate: 1\n    n_predictions: 17184\n    n_truncated: 314\n    inference_time_seconds: 6848.7\n- exp_id: plan_002_test_eval_s44_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: reeval_flat_nli_s44\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_006_qwen3_8b_sft_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.5051\n    f1: 0.5262\n    evi_f1: 0.8188\n    edcr: 0.651\n    format_ok_rate: 0.999\n    n_truncated: 313\n    n_predictions: 17401\n    inference_time_s: 7206\n- exp_id: plan_006_qwen3_1_7b_no_evidence_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    f1: 0.3884\n    ign_f1: 0.3786\n    evi_f1: 0.0007\n    edcr: 0.9848\n    precision: 0.4282\n    recall: 0.3553\n    pred_count: 27049\n    n_truncated: 531\n    format_ok_rate: 0.999\n- exp_id: plan_006_qwen3_8b_no_evidence_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.6509\n    eval_loss: 0.8153\n    eval_mean_token_accuracy: 0.8174\n    eval_entropy: 0.6275\n    train_runtime_sec: 3656\n    epoch: 3\n- exp_id: plan_016_llama_3_1_8b_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_016_llama_3_1_8b_no_evidence_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_006_qwen3_8b_no_evidence_eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_006_qwen3_8b_no_evidence_eval_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_006_qwen3_1_7b_no_evidence_eval_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_006_qwen3_1_7b_no_evidence_eval_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.3982\n    rel_f1: 0.4103\n    evi_f1: 0\n    edcr: 0\n    precision: 0.4464\n    recall: 0.3796\n    format_compliance_rate: 1\n    n_truncated: 501\n    inference_time_seconds: 7465.3\n    evidence_tax: 0.0804\n- exp_id: plan_006_qwen3_1_7b_no_evidence_eval_v2r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_016_llama_3_1_8b_no_evidence_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.5452\n    rel_f1: 0.5624\n    evi_f1: 0\n    edcr: 0\n- exp_id: plan_016_llama_3_1_8b_sft_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.5384\n    rel_f1: 0.5514\n    evi_f1: 0.8151\n    edcr: 0.628\n    precision: 0.5464\n    recall: 0.5565\n    evi_f1_joint: 0.4317\n    format_compliance_rate: 0.9949\n    n_truncated: 197\n    n_predictions: 15325\n    inference_time_seconds: 7331.3\n    evidence_tax_ign_f1: 0.0068\n    evidence_tax_rel_f1: 0.011\n- exp_id: plan_007_redocred_4b_sft_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_007_redocred_4b_sft_eval_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.3659\n    f1: 0.3706\n    evi_f1: 0.817\n    edcr: 0.6674\n    format_compliance_rate: 0.996\n    n_truncated: 139\n    n_total: 493\n    inference_time_seconds: 3281.7\n    precision: 0.4316\n    recall: 0.3247\n    ign_precision: 0.4134\n    ign_recall: 0.3282\n    evi_precision: 0.8208\n    evi_recall: 0.8131\n    n_predictions: 8191\n- exp_id: plan_016_llama_grpo_qlora\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    format_reward: 1\n    f1_reward: 0\n    ced_reward: 0\n    entropy: 0.28\n    final_step: 60\n    grad_norm: 0\n    loss: 0\n    frac_reward_zero_std: 1\n    output_length_final: 172\n    conclusion_note: 'C2 cross-family validated: LLaMA QLoRA GRPO shows same catastrophic\n      decoupling as Qwen (format gaming, zero IE ability)'\n- exp_id: plan_006_qwen3_8b_rsft_candidates\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan_006_qwen3_1_7b_rsft_candidates\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan_016_llama_rsft_candidates\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_007_redocred_rsft_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_016_llama_rsft_candidates_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    docs_completed: 64\n    docs_total: 3027\n    lines_generated: 512\n    output_path: /root/autodl-tmp/freige/outputs/rsft_candidates_llama_8b/generations.jsonl\n    failure_reason: Process killed externally (no traceback/error in log). Likely\n      OOM on cuda:1. Completed 64/3027 docs (2.1%) in ~23min before termination.\n- exp_id: plan_014_no_evidence_eval_d076\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan_016_llama_rsft_candidates_r3\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T16:00:41.804Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T16:00:41.804Z",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0"
}
```

---

## Round 1

23 recorded events

### User

_source line 3 · 2026-05-16T16:00:41.831Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：剩余实验全面确认 dev 发现，test 数字坚挺，DREEAM-protocol 对齐有竞争力，EDCR 人工验证通过——5-claim 框架完全成立，EMNLP Main 可直接投稿
核心假设：['Test set Ign-F1 退化 ≤1.5pp（dev 45.85 → test ≥44.3），no-evidence 同步退化（gap 保持）', 'DREEAM-protocol 对齐后 Evi-F1 ≥ 0.50——generative evidence 映射到句子级评估后仍有竞争力', 'EDCR 与 100 例人工标注 Spearman ρ ≥ 0.70，自动指标有效性充分验证', 'Post-hoc retrieval (SFT+BM25) evi_f1 ≤ 0.70，与 RSFT 0.81 差距 ≥10pp，端到端生成显著优于检索拼接', '8B/1.7B RSFT candidates 成功完成，RSFT 增益也呈 scale-dependent pattern，强化 C5']
关键指标范围：{'test_ign_f1_rsft_best': [44.0, 46.0], 'test_ign_f1_no_evidence': [45.5, 48.0], 'test_evidence_tax_4b': [-4.0, -1.5], 'dreeam_protocol_evi_f1': [0.5, 0.65], 'edcr_human_spearman_rho': [0.7, 0.9], 'posthoc_retrieval_evi_f1': [0.55, 0.7], 'expected_reviewer_avg': [3.5, 4.0]}
叙事方向：原始 framing 完全成立。标题可保持 evidence-grounded DocRE 方法论定位。 C1 直接声称 RSFT+CED 是有效方案（test 确认 +3-5pp over SFT）。 C2 decoupling spectrum 作为核心发现完整呈现（GRPO→DPO→RSFT 连续谱系）。 C3 NLI-based scoring 作为 RSFT 有效的关键组件。 C4 EDCR 双层诊断通过人工验证背书。 C5 U-shape scaling 作为独立贡献。 投 EMNLP Main，不需要 fallback AAAI。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: faith-evidence-ie

## paper_framing.md

# Paper Framing — FREIGE

> **状态**: POST-MVP + D078-D083 scaling analysis & cross-validation complete
> **最后更新**: 2026-05-16
> **Dream v1**: best=2.5, median=3.0, worst=2.5 → reframe 完成
> **Dream v2**: best=3.0, median=2.5, worst=2.5 → best 提升但 median 下降，未达标。关键路径：plan_011 bf16 GRPO eval + structural fixes → re-dream v3

## Target Venue

- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)
- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)

## Core Insight

LLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。

我们系统性地探索了 online RL (GRPO) 、offline preference optimization (DPO) 和 offline RL (RSFT) 三条技术路线。关键发现：**RL optimization pressure 与 evidence-extraction decoupling severity 正相关**——优化强度越大，evidence 质量提升的同时抽取能力退化越严重。QLoRA 放大至 catastrophic（rel_f1<0.02），bf16 GRPO 从 0.4549 退化至 ~0.434（mild, -2pp），DPO 呈 gradual 退化（1ep→3ep rel_f1 从 0.4034→0.3429），RSFT 无 decoupling。

**Evidence tax 是 scale-dependent 的（U-shape pattern, D079/D082/D083）**：1.7B 模型中 evidence generation 反而带来 +6.2pp 收益（隐式正则化），4B 模型付出 -7.9pp 代价，8B Qwen 模型容量足够 absorb（≈0），8B LLaMA 跨家族确认（-0.7pp）。这推翻了"evidence 总有代价"的简单叙事。

CED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，通过文档内 hard negative 对比评估 evidence 质量。CED 和 flat-NLI 作为 RSFT scoring functions 统计不可区分（D078 paired t-test p=0.44），但均显著优于 random/no scoring。CED 因可解释性优势作为默认推荐方案。

## Story Arc

1. **Problem**: LLM DocRE 无证据 → 部署障碍
2. **New task**: evidence-grounded DocRE — 同时生成关系和证据
3. **Cost of faithfulness**: evidence generation 代价是 **scale-dependent** 的——4B 模型付出 -7.9pp 代价，但 1.7B 反而获益 +6.2pp，8B 趋近于零。这不是固定成本，而是与模型容量的非线性交互（D079/D082/D083）
4. **Exploration**: 系统性比较 online RL (GRPO) vs offline preference (DPO) vs offline RL (RSFT)
5. **Key finding**: evidence-extraction decoupling — RL optimization pressure 与 decoupling severity 正相关，形成连续谱系（GRPO-QLoRA catastrophic > GRPO-bf16 mild > DPO gradual > RSFT none）
6. **QLoRA amplification**: QLoRA 量化将 mild decoupling 放大至 catastrophic forgetting——decoupling 是 RL-for-IE 中 multi-objective competition 的通用梯度（intra-task trade-off，非 inter-task forgetting），QLoRA 是 catastrophic amplifier
7. **What works**: RSFT with NLI-based scoring 是唯一有效路线——提升 evidence 质量而不牺牲抽取
8. **Best practical solution**: CED reranker 恢复 97% 的 evidence 代价，同时保留高质量 evidence（evi_f1=0.8188）
9. **Diagnostic tool**: EDCR 双层诊断——方法级量化 decoupling（与 Claim 2 呼应），per-relation 级揭示 evi_f1 不捕捉的 relation-type 难度差异（D070 ✅）
10. **Scaling & generalization**: evidence tax 呈 U-shape scaling pattern（D079/D082/D083），跨模型家族（LLaMA-8B, D082）和跨数据集（Re-DocRED, D080）验证泛化性

## Core Claims (reframed after Dream v1, updated D068-D083)

### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力
- FREIGE 是首个**基于生成式 LLM** 的 evidence-grounded DocRE 方法（⚠️ 必须始终保持 "generative LLM" 限定词——SAIS 已做 encoder-based evidence retrieval + DocRE）
- **关键区分 (Reviewer warning)**：encoder-based evidence *retrieval*（SAIS, DREEAM — 分类哪些句子是证据，evidence supervision 提升 RE）vs generative evidence *production*（FREIGE — LLM 生成证据文本，额外生成负担导致 scale-dependent 代价）。论文 Related Work 必须精准讨论此对比，否则审稿人会问 "为什么 SAIS 说 evidence 有用，你说 evidence 有害"
- **Evidence generation tax**: scale-dependent，详见 Claim 5（D079/D082/D083）
- RSFT 在 4/4 配置下均超过 SFT baseline（Ign-F1 +3.3~5.5pp）
- **CED reranker 是最优实用方案**: rel_f1=0.4864（仅低于 no-evidence 0.29pp），evi_f1=0.8188（plan_005 ✅）
- **D076 统一协议最终数字（可写入论文）**:
  - SFT baseline: rel_f1=0.4049
  - CED RSFT mean: rel_f1=0.4569 (s42=0.4517, s44=0.4621)
  - flat-NLI RSFT mean: rel_f1=0.4561 (s42=0.4535, s43_r2=0.4586)
  - CED vs flat-NLI Δ=0.0008，统计不可区分（D078 p=0.44）
- **Cross-family validation (D082)**: LLaMA-3.1-8B SFT rel_f1=0.5514, evi_f1=0.8151; no-evidence rel_f1=0.5624（evidence tax = -0.7pp，8B 容量足够 absorb）
- **Cross-dataset validation (D080)**: Re-DocRED Ign-F1 下降 3.15pp 但 Evi-F1 保持 0.817——evidence extraction 能力跨数据集泛化
- 需要 DREEAM-protocol 对齐的 Evi-F1 对比（D041 在处理中）
- **RSFT 方法论定位**：诚实承认 RSFT 是 STaR (NeurIPS 2022) 的单轮变体 + evidence quality scoring。创新点在于将 STaR-like self-improvement 应用于 evidence-grounded DocRE + CED/NLI 作为 domain-specific quality filter，而非框架本身
- **Evaluation caveat** (Limitations): GenRES 指出 exact match F1 低估 generative RE，FREIGE 所有 eval 用 exact match，应承认此局限（对所有方法同等适用，相对比较有效）

### Claim 2 (Core finding): RL optimization pressure 与 evidence-extraction decoupling severity 正相关（D068/D069 修正）
- **Decoupling spectrum**: 优化强度越大，decoupling 越严重
  - GRPO QLoRA: catastrophic（rel_f1=0.0138, evi_f1=0.850, EDCR=0.99）— QLoRA 放大 decoupling
  - GRPO bf16: mild（rel_f1 从 0.4549→~0.434, -2pp; step_30=0.434, step_50=0.4276, step_70=0.4341）— 退化可控但持续（D065/D066）
  - DPO bf16 1ep→3ep: gradual（Ign-F1 38.88→TBD, rel_f1 0.4034→0.3429）— 随训练渐进退化（D067/D068）
  - RSFT: none — 无 decoupling，唯一有效路线
- **QLoRA 是 catastrophic amplifier，不是 root cause**: bf16 GRPO 仅 mild decoupling（-2pp），QLoRA 放大至 catastrophic（-39pp）（D054/D065/D066）
- **Decoupling 是 RL-for-IE 的通用梯度**: 跨方法（GRPO/DPO）、跨量化策略（QLoRA/bf16）一致出现，严重程度与优化压力正相关
- 三档 Dream 审稿均认为此发现\"genuinely novel and striking\"
- **已完成**: GRPO G=8 bf16 确认 mild decoupling（plan_011 ✅）; DPO 1ep/3ep 确认 gradual decoupling（plan_012 ✅）

### Claim 3 (Ablation): NLI-based scoring 提升 RSFT 质量——CED 与 flat-NLI 统计不可区分（D078）
- CED 和 flat-NLI 都显著优于 random/no scoring
- **D078 paired t-test 最终结论**: CED vs flat-NLI p=0.44，统计不可区分
  - CED RSFT mean rel_f1=0.4569 vs flat-NLI mean rel_f1=0.4561（Δ=0.0008）
  - 两种 scoring function 等效，CED 因可解释性（contrastive evidence discrimination）作为默认推荐
- ~~**Critical**: 如果 CED 不显著优于 flat-NLI → CED 降级为"one possible scoring function"~~ → **已确认降级（D078）**
- **论文叙事**: "NLI-based scoring（无论 CED 或 flat-NLI）是 RSFT 有效的关键——两种变体均等效提升质量，CED 额外提供可解释的 evidence discrimination"
- **top_k selection ablation (k=1 vs k=3)**:
  - k=1 (best-of-8) 优于 k=3 (top3-of-8)，CED scoring precision 随 k 增大下降
  - k=1 均值 (3 seeds s42/s43/s44): Ign-F1=45.00, rel_f1=0.4596, evi_f1=81.43, EDCR=0.6434
  - k=3 (1 seed, reeval_rsft_topk3): Ign-F1=43.64, rel_f1=0.4454, evi_f1=80.88, EDCR=0.6635
  - Δ (k=3 vs k=1 mean): Ign-F1 **-1.36pp**, rel_f1 **-1.42pp**, evi_f1 **-0.55pp**, EDCR +0.02
  - 训练数据质量下降: k=1 mean_f1=0.6157, mean_ced=0.6683 → k=3 mean_f1=0.5761, mean_ced=0.6205（来源: mvp2_rsft_ced_scoring / mvp2_rsft_ced_scoring_topk3_r2）
  - 训练集规模: k=1 选出 2718 样本 (12.4%), k=3 选出 8037 样本 (37%), 数据量 ×2.96 但质量下降抵消数量优势
  - **叙事**: 低排名 response 引入噪声——rank 2-3 样本的 F1 和 CED 分数均显著低于 rank 1，扩大训练集规模无法补偿数据质量的稀释。这表明 RSFT 的关键不在数据量而在 scoring precision
  - **注**: k=3 仅 1 seed，差异方向一致但尚不具备统计显著性；作为 ablation table 中的辅助行呈现，不作为独立 claim

### Claim 4 (Diagnostic): EDCR 双层诊断价值（D070/D072）
- **Layer 1 — 方法级**: EDCR 量化 evidence-extraction decoupling，与 Claim 2 spectrum 呼应
  - 方法级 EDCR 与 rel_f1 Spearman ρ=-0.965（plan_003 ✅）——本质是 decoupling 的度量
  - EDCR 识别病理模型（GRPO QLoRA: EDCR≈1.0）
- **Layer 2 — per-relation-type**: EDCR 提供 evi_f1 不捕捉的 relation-type 诊断信息 ✅
  - per-relation ρ(EDCR, evi_f1) = **-0.064** (p=0.58) → **完全独立于 evi_f1**
  - per-relation ρ(EDCR, rel_f1) = -0.793 (p<0.001) → 与 rel_f1 强相关但非完美
  - per-relation ρ(evi_f1, rel_f1) = -0.013 (p=0.91) → evidence 质量与抽取能力在 relation type 间完全解耦
  - 典型案例：date_of_birth (EDCR=0.118, 高 faithful) vs head_of_government (EDCR=0.956, 高 decoupled)
  - 93 relation types 分析（≥5 样本），76 个有非零数据
- **论文叙事**: EDCR 在方法级是 decoupling 度量工具（横向对比方法），在 relation 级是难度诊断工具（纵向定位薄弱 relation）——两层叙事互补
- **仍需**: 100 例人工标注验证（RC6）

### Claim 5 (NEW — Scaling): Evidence Tax 呈非线性 U-shape Scaling Pattern（D079/D082/D083）
- **核心发现**: evidence generation 的代价不是固定的——它与模型容量呈非线性关系
  - **1.7B (Qwen3-1.7B)**: +6.2pp BENEFIT — evidence generation 起隐式正则化作用，防止小模型过拟合（D083 公平子集分析确认）
  - **4B (Qwen3-4B)**: -7.9pp cost — 标准 evidence generation 负担，模型容量不足以同时优化两个目标
  - **8B Qwen (Qwen3-8B)**: ≈0 — 模型容量足够 absorb evidence generation 的额外负担
  - **8B LLaMA (LLaMA-3.1-8B)**: -0.7pp — 跨家族确认，8B 规模的 evidence tax 趋近于零
- **U-shape 解释**: 小模型从 evidence 的正则化效应获益 > 生成负担；中等模型容量不足以同时做好两件事；大模型容量充裕，两个目标互不干扰
- **论文叙事**: 推翻 "evidence 总有代价" 的简单叙事，揭示 evidence generation 与模型容量的非线性交互——这为选择何种规模模型部署 evidence-grounded IE 提供实际指导
- **Cross-family robustness**: LLaMA-8B 与 Qwen-8B 一致确认 8B 规模 evidence tax ≈ 0

## MVP Evidence Summary (D071: 主表报 Ign-F1，附录报 F1; D076 统一协议 rel_f1)

| Config | Ign-F1 | F1 | Δ vs SFT (Ign-F1) | Evi-F1 (cond) | Evi-F1 (joint) | EDCR |
|--------|--------|------|-------------------|---------------|---------------|------|
| **SFT no-evidence** | **47.36** | 48.93 | **+7.00pp** | **—** | **—** | **—** |
| SFT baseline (noquant) | 40.36 | 41.06 | — | 80.13 | 31.17 | 0.7118 |
| **CED reranker** | **TBD** | 48.64 | **TBD** | **81.88** | — | **0.6156** |
| RSFT CED s43 (best) | **45.85** | 46.83 | **+5.49pp** | 81.56 | 37.11 | 0.6388 |
| RSFT CED s44 | 45.51 | 46.55 | +5.15pp | 80.87 | 37.13 | 0.6350 |
| RSFT CED s42 | 43.63 | 44.49 | +3.27pp | 81.87 | 34.68 | 0.6565 |
| RSFT CED k=3 | 43.64 | 44.54 | +3.28pp | 80.88 | — | 0.6635 |
| RSFT r2a (1ep) | 44.01 | 44.94 | +3.65pp | 81.08 | 35.09 | 0.6641 |
| RSFT r2b (1ep) | 44.10 | 44.93 | +3.74pp | 81.28 | 34.90 | 0.6609 |
| flat-NLI s42 | 44.49 | 45.39 | +4.13pp | 80.43 | — | 0.6431 |
| flat-NLI s43 (reeval) | TBD | 45.23 | TBD | 81.58 | — | 0.6505 |
| DPO bf16 1ep | 38.88 | 40.34 | -1.48pp | 80.88 | — | 0.7139 |
| DPO bf16 3ep | TBD | 34.29 | TBD | — | — | — |
| GRPO bf16 G=8 (best step) | 45.59 | ~43.4 | +5.23pp | 80.86 | — | — |
| GRPO QLoRA (lr=5e-6) | TBD | 1.38 | TBD | 85.00 | — | 0.9900 |

注：Evi-F1 以百分比显示（×100）。Ign-F1 修正后排名无实质变化（仅 r2a/r2b 互换，差 0.09pp）。TBD 项等待 metrics_v2.json 补算。GRPO bf16 Ign-F1=45.59 > F1=43.4 因 train triples 过滤效应。RSFT CED k=3 数据来源: reeval_rsft_topk3 (ign_f1_corrected=true)。

### D076 统一协议 rel_f1（可直接写入论文）

| Config | rel_f1 | evi_f1 |
|--------|--------|--------|
| SFT baseline | 0.4049 | — |
| CED RSFT mean (s42, s44) | **0.4569** | — |
| CED RSFT s42 | 0.4517 | — |
| CED RSFT s44 | 0.4621 | — |
| flat-NLI RSFT mean (s42, s43_r2) | **0.4561** | — |
| flat-NLI RSFT s42 | 0.4535 | — |
| flat-NLI RSFT s43_r2 | 0.4586 | — |
| LLaMA-8B SFT | 0.5514 | 0.8151 |
| LLaMA-8B no-evidence | 0.5624 | — |

### Evidence Tax Scaling（D079/D082/D083）

| Model | Evidence Tax (Δ) | 方向 |
|-------|-----------------|------|
| Qwen3-1.7B | **+6.2pp** | BENEFIT（隐式正则化） |
| Qwen3-4B | **-7.9pp** | cost |
| Qwen3-8B | **≈0** | neutral |
| LLaMA-3.1-8B | **-0.7pp** | near-neutral（跨家族确认） |

### Cross-Dataset Validation（D080）

| Dataset | Ign-F1 Δ | Evi-F1 | 说明 |
|---------|----------|--------|------|
| DocRED (in-domain) | baseline | — | — |
| Re-DocRED | -3.15pp | 0.817 | evidence extraction 泛化，relation extraction 有损 |

## Anticipated Reviewer Concerns (updated from Dream, D068-D083)

### RC1: "Online RL" 标题过度声称（Dream 三档一致 Critical）
- ~~标题和 claim 收窄到 "GRPO fails for DocRE"~~
- **D068/D069 修正**: 重新定位为 "RL optimization pressure correlates with decoupling severity"——不是 GRPO 特有问题，而是 RL-for-IE 的通用梯度
- DPO 数据支撑 decoupling spectrum（gradual decay confirms the pattern）

### RC2: GRPO G=4 太小 + LoRA confound（Dream 三档一致 Major）
- GRPO G=8 bf16 实验 ✅ — 确认 mild decoupling（-2pp），QLoRA 是 catastrophic amplifier（D065/D066）
- LoRA confound 已解决：bf16 LoRA vs QLoRA 直接对比

### RC3: CED 不显著优于 flat-NLI（Dream 三档一致 Major）
- **已解决（D078）**: paired t-test p=0.44，CED 与 flat-NLI 统计不可区分
- **应对**: 不再声称 CED > flat-NLI；论文定位为 "NLI-based scoring 是关键（CED 和 flat-NLI 均有效），CED 因可解释性作为默认推荐"
- ~~5+ seeds 统计检验~~ → 不再需要，D078 已给出明确结论

### RC4: RSFT 不新颖
- 不声称 RSFT 是贡献；贡献在于任务定义 + decoupling 发现 + EDCR
- 诚实定位 RSFT 为 STaR (NeurIPS 2022) 单轮变体 + domain-specific quality filter

### RC12: SAIS 说 evidence 有用，为何 FREIGE 说 evidence 有害？（文献审查 2026-05-16）
- **关键区分**: discriminative evidence *retrieval*（SAIS/DREEAM — 分类句子是否为证据，作为监督信号提升 RE）vs generative evidence *production*（FREIGE — LLM 生成完整证据文本，额外生成负担导致 scale-dependent 代价）
- SAIS 的 evidence supervision 是分类任务，不增加输出长度；FREIGE 的 evidence generation 显著增加生成序列长度，模型需分配容量同时完成 RE + evidence 生成
- **D079/D083 新弹药**: evidence tax 是 scale-dependent 的——1.7B 模型中 evidence 反而有益（+6.2pp），与 SAIS 的发现方向一致。这说明 evidence 的效果取决于模型容量和任务范式的交互，而非简单的有害/有益二分
- **应对**: Related Work 中精准讨论此对比，明确 FREIGE 研究的是 *generative production* 设定下的代价，与 *retrieval* 设定下的增益不矛盾——两者揭示了 evidence 在不同范式下的不同角色

### RC13: 单模型单数据集泛化性不足（D077 scope 扩展）
- ~~plan_006: Qwen3-1.7B / 8B model size ablation~~ ✅ D079/D083 完成
- ~~plan_016: LLaMA-3.1-8B cross-family validation~~ ✅ D082 完成
- ~~plan_007: Re-DocRED cross-dataset evaluation~~ ✅ D080 完成
- **结果**: 三项泛化实验全部完成，支撑 C5 scaling pattern + cross-family + cross-dataset 叙事

### RC5: 评测可比性（D041）
- DREEAM-protocol Evi-F1；conditional Evi-F1 作为辅助指标

### RC6: EDCR 缺人工验证
- 100 例小规模标注

### RC7: Missing DPO/PPO（Dream 两档 Major）
- DPO experiment ✅ — 结果确认 decoupling spectrum（D067/D068）

### RC8: Dev-test degradation
- 观察项，等 test set 数据

### RC9: 连接 reward overoptimization 文献
- 显式引用 Gao et al. 2023

### RC10: Post-hoc evidence retrieval baseline
- SFT + BM25 evidence retrieval

### RC11: "RL 不遗忘" 文献与 Claim 2 的张力（文献扫描 2026-05-16）
- 近期多篇论文（arXiv 2507.05386, 2506.23508, 2509.04259）论证 RL fine-tuning 天然缓解 catastrophic forgetting
- **关键区分**: FREIGE 的 decoupling 是 **intra-task multi-objective trade-off**（RE 抽取 vs evidence 生成两个优化目标的竞争），不是 **inter-task forgetting**（丢失预训练知识）。两者机制不同
- bf16 GRPO 的 mild decoupling（-2pp）恰好印证这一点：模型没有忘记"怎么做 IE"，而是在 evidence reward 压力下偏移了 RE-evidence 的资源分配
- **应对**: Related Work / Discussion 中显式回应这组文献，区分 intra-task trade-off vs inter-task forgetting
- **QuRL/QaRL 文献支撑 Claim 2**: QuRL 发现 quantized vs full-precision actor divergence 在长训练中指数增长（直接支撑 QLoRA amplification 叙事）；QaRL 的 error token failure mode 与 QLoRA GRPO garbled evidence 吻合

## Key Baselines (12+)

1. **SFT-only**: Qwen3-4B + LoRA SFT（with evidence）
1b. **SFT no-evidence**: Qwen3-4B + LoRA SFT（无 evidence，upper bound ablation）
2. **RSFT flat-NLI**: flat-NLI scored RSFT（核心 ablation）
3. **RSFT CED**: CED scored RSFT（主方法）
4. **CED-as-reranker**: 推理时 CED 重排（无训练）
5. **DPO+CED**: offline preference learning — gradual decoupling（D067/D068）
6. **GRPO+CED (QLoRA, G=4)**: catastrophic decoupling baseline
7. **GRPO+CED (bf16, G=8)**: mild decoupling — QLoRA confound 排除（D065/D066）
8. **Post-hoc retrieval**: SFT + BM25 evidence（NEW）
9. **DREEAM**: encoder evidence SOTA
10. **SAIS**: encoder evidence baseline
11. **DocKS-RAG**: extraction SOTA（无 evidence）
12. **LMRC**: generative LLM SOTA（无 evidence）

## Publishability Threshold (revised after D078-D083)

- **必要条件**: (1) RSFT 在 test set 上 Ign-F1 显著 > SFT (2) DREEAM-protocol Evi-F1 可报告 (3) Decoupling spectrum 有完整数据支撑（GRPO QLoRA/bf16 + DPO + RSFT）
- **充分条件**: 上述 + EDCR 人工验证 + scaling pattern (C5) 完整
- **已达成**: CED vs flat-NLI 统计检验完成（D078: 不可区分，不再是充分条件要素）; 泛化实验完成（D079/D080/D082/D083）
- **Failure pivot**: decoupling spectrum 不成立（bf16 GRPO 也 catastrophic）→ scope 大幅缩减。**已排除**: bf16 GRPO 确认 mild（D065/D066）

## Research Phase Priorities (revised after D078-D083)

| Priority | 实验 | Claim | GPU-h |
|----------|------|-------|-------|
| ~~P0~~ | ~~flat-NLI RSFT ablation (5 seeds)~~ → D078 已结论 | C3 | — |
| ~~P0~~ | ~~CED RSFT additional seeds (→5 total)~~ → D078 已结论 | C3 | — |
| P0 | DREEAM-protocol Evi-F1 对齐 | C1 | CPU |
| P0 | Test set evaluation | C1 | ~4h |
| P0 | DREEAM baseline reproduction | C1 | ~8h |
| ~~P0~~ | ~~GRPO G=8 experiment~~ ✅ | C2 | ~16h |
| ~~P0~~ | ~~DPO+CED experiment~~ ✅ | C2 | ~12h |
| ~~P0~~ | ~~EDCR per-relation analysis (D070)~~ ✅ | C4 | CPU |
| ~~P0~~ | ~~Ign-F1 bugfix + data sync (D071)~~ ✅ | ALL | CPU |
| ~~P0~~ | ~~Model size ablation (1.7B/8B)~~ ✅ D079/D083 | C5 | — |
| ~~P0~~ | ~~LLaMA-3.1-8B cross-family~~ ✅ D082 | C5 | — |
| ~~P0~~ | ~~Re-DocRED cross-dataset~~ ✅ D080 | C1/C5 | — |
| P1 | EDCR human validation | C4 | API |
| P1 | Post-hoc evidence retrieval baseline | C1 | ~4h |
| P1 | CED-as-reranker (running) | C1 | ~6h |
| ~~P0~~ | ~~GRPO forgetting dynamics figure (plan_009)~~ ✅ | C2 | ~2h |
| ~~P0~~ | ~~SFT-without-evidence ablation (plan_014)~~ ✅ | C1 | ~8h |
| P2 | Advantage variance measurement | C2 | CPU |


## experiment_plan (with registry status)

- id: plan_001
  claim: 2
  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选
    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py
    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'
  priority: P0
  gpu_budget_hours: 20
  deps: []
  registry_id: eval_flat_nli_seed45
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.455052
    ign_f1: 0.446181
    evi_f1: 0.815399
    edcr: 0.652133
    evi_f1_joint: 0.355612
- id: plan_002
  claim: 1
  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set
    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'
  priority: P0
  gpu_budget_hours: 4
  deps:
  - plan_001
  registry_id: null
  status: planned
- id: plan_003
  claim: 4
  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing
    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'
  priority: P0
  gpu_budget_hours: 2
  deps:
  - plan_001
  registry_id: plan_003_edcr_diagnostic
  status: DONE
  conclusion: success
  metrics:
    methods_evaluated: 15
    edcr_vs_rel_f1_spearman: -0.9648
    edcr_vs_rel_f1_pvalue: 0.0001
    edcr_vs_evi_f1_spearman: 0.0022
    edcr_vs_evi_f1_pvalue: 0.9941
    edcr_range: 0.63-0.99
    unique_diagnostic_value: identifies pathological models (GRPO QLoRA) with high
      evi_f1 but catastrophically low rel_f1
- id: plan_004
  claim: 1
  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)
    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'
  priority: P0
  gpu_budget_hours: 8
  deps: []
  registry_id: plan_004_dreeam_baseline
  status: DONE
  conclusion: success
  metrics:
    dev_rel_f1: 63.57
    dev_rel_ign_f1: 61.72
    dev_evi_f1: 54.01
    dev_rel_p: 66.95
    dev_rel_r: 60.51
    dev_evi_p: 60.53
    dev_evi_r: 48.76
- id: plan_005
  claim: 1
  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'
  priority: P1
  gpu_budget_hours: 6
  deps: []
  registry_id: mvp2_ced_reranker_poc
  status: DONE
  conclusion: success
  metrics:
    ced_reranker_rel_f1: 0.486367
    ced_reranker_ign_f1: 0.473634
    ced_reranker_evi_f1: 0.8188
    oracle_rel_f1: 0.623746
    oracle_ign_f1: 0.612518
    random_rel_f1: 0.453783
    random_ign_f1: 0.439677
- id: plan_006
  claim: 1
  description: 'Model size ablation (D077 升 P0): Qwen3-1.7B 和 Qwen3-8B 上复现 SFT → RSFT
    → eval pipeline，验证 evidence tax + RSFT 增益 + decoupling 在不同模型规模下成立。应对 RC4 和 scope
    不足问题。'
  priority: P0
  gpu_budget_hours: 32
  deps: []
  registry_id: plan_006_qwen3_1_7b_no_evidence_eval_v3
  status: DONE
  conclusion: success
  metrics:
    ign_f1: 0.3982
    rel_f1: 0.4103
    evi_f1: 0
    edcr: 0
    precision: 0.4464
    recall: 0.3796
    format_compliance_rate: 1
    n_truncated: 501
    inference_time_seconds: 7465.3
    evidence_tax: 0.0804
- id: plan_007
  claim: 1
  description: 'Re-DocRED cross-dataset (D077 升 P0): 在 Re-DocRED 上用当前 best config
    做 SFT → RSFT → eval。数据已就绪（格式与 DocRED 兼容，96 relation types 一致）。⚠️ Re-DocRED ~55%
    triples 无 evidence 标注（修正的 false negative），必须报告两种模式：evidence_only（与 DocRED 可比的
    evi_f1，仅 43% triples）+ full（全部 triples 的 rel_f1，无 evi_f1）。转换脚本已支持 --mode full。'
  priority: P0
  gpu_budget_hours: 16
  deps: []
  registry_id: null
  status: planned
- id: plan_016
  claim: 2
  description: 'LLaMA-3.1-8B cross-family validation (D077 新增): 在非 Qwen 家族模型上复现核心
    pipeline (SFT → RSFT → GRPO QLoRA)，验证 decoupling spectrum 跨模型家族成立。关键实验：LLaMA GRPO
    QLoRA 是否也出现 catastrophic forgetting。'
  priority: P0
  gpu_budget_hours: 40
  deps: []
  registry_id: plan_016_llama_rsft_candidates
  status: DONE
  conclusion: failed
- id: plan_008
  claim: 2
  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格
    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'
  priority: P1
  gpu_budget_hours: 8
  deps: []
  registry_id: reeval_rsft_topk3
  status: DONE
  conclusion: negative
  metrics:
    rel_f1: 0.4454
    rel_precision: 0.4512
    rel_recall: 0.4398
    ign_f1: 0.4364
    evi_f1: 0.8088
    edcr: 0.6635
    format_ok_rate: 0.999
    n_truncated: 214
    n_predictions: 16020
    inference_time_seconds: 3546.4
    ign_f1_corrected: true
- id: plan_011
  claim: 3
  description: 'GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward
    + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要
    gradient_accumulation 适配显存。'
  priority: P0
  gpu_budget_hours: 8
  deps: []
  registry_id: plan_011_bf16_g8_step_eval
  status: DONE
  conclusion: success
  metrics:
    step_30:
      rel_f1: 0.434
      evi_f1: 0.8063
      edcr: 0.6807
    step_50:
      rel_f1: 0.4276
      evi_f1: 0.8024
      edcr: 0.6855
    step_70:
      rel_f1: 0.4341
      evi_f1: 0.8099
      edcr: 0.6685
    best_step: step_70
    trend: non-monotonic, all < ckpt-100 (0.4549)
- id: plan_012
  claim: 3
  description: 'DPO+CED experiment: 用 RSFT 候选数据构造 preference pairs (CED-preferred
    vs CED-rejected)，DPO 训练。验证 DPO 是否避免 GRPO 的 catastrophic forgetting。Dream v2 三档要求
    DPO 作为 RL spectrum 关键数据点，必须补全训练超参（β, lr, epochs, pair construction）。D045 升 P0。'
  priority: P0
  gpu_budget_hours: 12
  deps: []
  registry_id: plan_012_dpo_ced
  status: DONE
  conclusion: negative
  metrics:
    rel_f1: 0.3429
    evi_f1: 0.8403
    edcr: 0.7294
    format_ok_rate: 0.995
    checkpoint: checkpoint-501
    rewards_accuracy: 1
    margins: 9.01
- id: plan_013
  claim: 4
  description: 'EDCR 人工标注验证: 100 个样本，人工判断每个 cited evidence sentence 是否真正支持对应 relation。计算
    EDCR 与人工判断的相关性，验证 EDCR 作为自动指标的有效性。Dream [M][W] 一致要求。'
  priority: P1
  gpu_budget_hours: 0
  deps: []
  registry_id: null
  status: planned
- id: plan_009
  claim: 3
  description: 'GRPO forgetting dynamics figure: 整理全部 GRPO checkpoint（42个）的 rel_f1/evi_f1/EDCR/reward
    轨迹，绘制 training dynamics 可视化图。包含 G=4 vs G=8 对比、三种 reward 对比。Dream v2 三档一致要求此图作为论文核心
    figure。数据已有，只需汇总+画图。'
  priority: P0
  gpu_budget_hours: 2
  deps: []
  registry_id: plan_009_dynamics_figure
  status: DONE
  conclusion: success
- id: plan_010
  claim: 1
  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer
    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。'
  priority: P2
  gpu_budget_hours: 4
  deps: []
  registry_id: null
  status: planned
- id: plan_014
  claim: 1
  description: 'SFT-without-evidence ablation: 训练 Qwen3-4B SFT 只输出 relation triples（不含
    evidence sentences），对比标准 SFT（含 evidence）的 rel_f1。隔离 evidence generation 对抽取性能的代价。Dream
    v2 三档一致要求。用于回答"43.2% vs LMRC 60.7% 的 gap 有多少来自 evidence 生成负担"。'
  priority: P0
  gpu_budget_hours: 8
  deps: []
  registry_id: plan_014_sft_no_evidence
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.7077
    eval_loss: 0.8781
    eval_token_accuracy: 0.8086
    epochs: 3
    total_steps: 570
    train_runtime_min: 64
    samples: 3027
    trainable_params: 132M/4.15B (3.18%)
- id: plan_015
  claim: 2
  description: 'bf16 LoRA GRPO clean control: 与原始 GRPO (QLoRA 4-bit, G=4, kl=0, CED
    reward) 只改一个变量——quantization 从 QLoRA 4-bit 改为 bf16 LoRA。G=4, kl_coef=0 不变。目的:
    隔离 QLoRA confound，判断 decoupling 是 QLoRA artifact 还是 genuine RL-for-IE 现象。Dream
    v2 三档一致的 critical 要求。如 decoupling 在 bf16 下仍持续 → 可泛化 claim；如消失 → QLoRA 特定，需 re-scope。优先级取决于
    plan_011 eval 结果。'
  priority: P0
  gpu_budget_hours: 8
  deps:
  - plan_011
  registry_id: plan_015_grpo_g4_bf16_v3
  status: DONE
  conclusion: killed
- id: plan_mvp1
  claim: 1
  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing
    distractor 的能力验证'
  priority: P0
  gpu_budget_hours: 1
  deps: []
  registry_id: mvp1_ced_signal
  status: DONE
  conclusion: success
  metrics:
    mean_margin: 0.48
    discrimination_accuracy: 0.815
    pearson_r_margin_jaccard: 0.34
    pass: true
- id: plan_mvp2_sft
  claim: 1
  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'
  priority: P0
  gpu_budget_hours: 4
  deps: []
  registry_id: mvp2_sft_warmup
  status: DONE
  conclusion: success
  metrics:
    eval_loss: 0.72
    accuracy: 0.835
- id: plan_mvp2_rsft
  claim: 1
  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部
    PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087,
    r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128'
  priority: P0
  gpu_budget_hours: 20
  deps:
  - plan_mvp1
  - plan_mvp2_sft
  registry_id: mvp2_rsft_train_r1
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.0483
    num_preds: 848
    sft_baseline_rel_f1: 0.4057
    failure_mode: relation_ontology_collapse_to_freetext
    epoch1_eval_loss: 0.756
    epoch2_eval_loss: 0.759
- id: plan_mvp2_grpo
  claim: 3
  description: 'GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1
    max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic
    forgetting。D031/D033 完整轨迹支撑 Claim 3'
  priority: P0
  gpu_budget_hours: 60
  deps:
  - plan_mvp2_sft
  registry_id: mvp2_grpo_ced_lr5e6_r1
  status: DONE
  conclusion: killed


## registry (completed experiments)

- exp_id: mvp1_ced_signal
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mean_margin: 0.48
    discrimination_accuracy: 0.815
    pearson_r_margin_jaccard: 0.34
    pass: true
- exp_id: smoke_test_grpo
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: mvp2_sft_warmup
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_loss: 0.72
    accuracy: 0.835
- exp_id: precompute_nli_train
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: mvp2_grpo_ced
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp2_grpo_flatnli
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp2_grpo_extract
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp2_sft_eval
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_grpo_ced_r1
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_grpo_ced_r2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_grpo_ced_r3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp2_grpo_ced_r4
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_grpo_extract_r2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_grpo_flatnli_r2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_grpo_ced_r5
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: mvp2_grpo_extract_r3
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: mvp2_grpo_flatnli_r3
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_grpo_ced_kl001
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp2_sft_eval_r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4057
    ign_f1: 0.4057
    evi_f1: 0.7979
    edcr: 0.7118
    precision: 0.4043
    recall: 0.407
    evi_precision: 0.8035
    evi_recall: 0.7924
    format_ok_rate: 0.998
    format_compliance_rate: 0.626
    n_parseable: 617
    n_truncated: 367
    n_predictions: 18815
    inference_time_seconds: 6484.7
- exp_id: mvp2_sft_eval_r3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4057
    ign_f1: 0.4057
    evi_f1: 0.7979
    edcr: 0.7118
    precision: 0.4043
    recall: 0.407
    evi_precision: 0.8035
    evi_recall: 0.7924
    format_ok_rate: 0.998
    format_compliance_rate: 0.626
    n_parseable: 617
    n_truncated: 367
    n_predictions: 18815
- exp_id: mvp2_grpo_ced_kl001_r2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_grpo_ced_kl001_r3
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_grpo_flatnli_r4
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_grpo_ced_kl001_r4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_step: 100
    train_runtime_s: 9069.88
    reward_final: 1.195
    f1_reward_final: 0.573
    ced_reward_final: 0.328
    format_reward_final: 0.293
    frac_zero_std_final: 0.2
    kl_final: 0.118
    loss_final: -0.009
    grad_norm_final: 0.14
    entropy_final: 0.067
    completion_length_mean_final: 520.8
    best_reward_step: 90
    best_reward: 1.37
    best_f1_reward: 0.72
    best_ced_reward: 0.353
- exp_id: mvp2_grpo_extract_r4
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_grpo_flatnli_r5
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_eval_ced_kl001_r4_early
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    f1: 0.1563
    ign_f1: 0.1563
    evi_f1: 0.5643
    edcr: 0.8858
    precision: 0.2356
    recall: 0.1169
    evi_precision: 0.4864
    evi_recall: 0.6721
    format_ok_rate: 0.999
    n_parseable: 984
    n_truncated: 11
    n_predictions: 9250
    tp: 1421
    pred_count: 6032
    gold_count: 12151
- exp_id: mvp2_grpo_flatnli_r6
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    steps_completed: 25
    final_frac_zero_std: 0.9
    final_f1_reward: 0
    final_flat_nli_reward: 0
    final_format_reward: 0.293
    collapse_step: 25
- exp_id: mvp2_eval_ced_kl001_r4_ckpt10
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.00296
    rel_precision: 0.00314
    rel_recall: 0.0028
    evi_f1: 0.72
    evi_precision: 0.6429
    evi_recall: 0.8182
    edcr: 0.9983
    n_parseable: 984
    n_truncated: 24
    n_predictions: 11621
    tp: 34
    pred_count: 10839
    gold_count: 12151
    inference_time_seconds: 5211.4
- exp_id: mvp2_eval_ced_kl001_r4_multi
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    checkpoint-10:
      f1: 0.003
      ign_f1: 0.003
      evi_f1: 0.72
      edcr: 0.9983
      format_ok_rate: 0.999
    checkpoint-20:
      f1: 0.0088
      ign_f1: 0.0088
      evi_f1: 0.423
      edcr: 0.9954
      format_ok_rate: 0.999
    checkpoint-30:
      f1: 0.0338
      ign_f1: 0.0338
      evi_f1: 0.5889
      edcr: 0.9798
      format_ok_rate: 1
    checkpoint-50:
      f1: 0.1563
      ign_f1: 0.1563
      evi_f1: 0.5643
      edcr: 0.8858
      format_ok_rate: 0.999
    checkpoint-60:
      f1: 0.1467
      ign_f1: 0.1467
      evi_f1: 0.5763
      edcr: 0.9062
      format_ok_rate: 1
    checkpoint-90:
      f1: 0.2108
      ign_f1: 0.2108
      evi_f1: 0.5666
      edcr: 0.8584
      format_ok_rate: 1
- exp_id: mvp2_eval_ced_kl001_r4_step100
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    rel_f1: 0.2167
    ign_f1: 0.2167
    precision: 0.2849
    recall: 0.1749
    evi_f1: 0.5746
    evi_precision: 0.5244
    evi_recall: 0.6353
    edcr: 0.8539
    pred_count: 7460
    gold_count: 12151
    tp: 2125
    n_truncated: 21
    format_ok_rate: 1
- exp_id: mvp2_eval_ced_kl001_r4_last
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_eval_ced_kl001_r4_ckpt90
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_eval_ced_kl001_r4_high
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    checkpoint_60:
      rel_f1: 0.1467
      ign_f1: 0.1467
      precision: 0.1909
      recall: 0.1192
      evi_f1: 0.5763
      edcr: 0.9062
      pred_count: 10041
      gold_count: 12151
      n_truncated: 16
      format_ok_rate: 1
    note: Only ckpt-60 completed. Process died during ckpt-70 inference at 8% (5/62
      batch). ckpt-80/90 never started.
- exp_id: mvp2_eval_ced_kl001_r4_step90
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    rel_f1: 0.2108
    ign_f1: 0.2108
    evi_f1: 0.5666
    edcr: 0.8584
    pred_count: 11160
    n_truncated: 22
    format_ok_rate: 1
    n_documents: 985
- exp_id: mvp2_grpo_ced_lr5e6_r1
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_grpo_ced_lr5e6_p1_r1
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_grpo_ced_lr5e6_rp_r1
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp2_eval_ced_kl001_r4_ckpt7080
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp2_grpo_ced_lr5e6_rp_r2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_eval_lr5e6_r1_ckpt20
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    rel_f1: 0.0077
    rel_precision: 0.0071
    rel_recall: 0.0084
    evi_f1: 0.628
    evi_precision: 0.855
    evi_recall: 0.496
    edcr: 0.993
    format_ok_rate: 0.991
    field_compliance_rate: 0.399
    pred_count: 14440
    gold_count: 12151
    tp: 102
    n_truncated: 587
    inference_time_seconds: 6370.4
- exp_id: mvp2_eval_lr5e6_r1_ckpt40
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp2_eval_lr5e6_r1_ckpt40_r2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    rel_f1: 0.0071
    precision: 0.0066
    recall: 0.0078
    evi_f1: 0.7584
    evi_precision: 0.9113
    evi_recall: 0.6494
    edcr: 0.9942
    format_ok_rate: 0.9939
    field_compliance_rate: 0.5675
    pred_count: 14434
    gold_count: 12151
    tp: 95
    n_truncated: 424
    inference_time_seconds: 6152
- exp_id: mvp2_eval_lr5e6_rp_r2_ckpt20
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_eval_sft_baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4057
    evi_f1: 0.7979
    evi_f1_joint: 0.3117
    evi_f1_joint_P: 0.3037
    evi_f1_joint_R: 0.32
    edcr: 0.7118
    pred_count: 12234
    gold_count: 12151
    format_ok_rate: 0.998
    format_compliance_rate: 0.998
    field_compliance_rate: 0.6264
    n_truncated: 367
    inference_time_seconds: 6138.5
- exp_id: mvp2_eval_lr5e6_r1_ckpt60
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp2_eval_lr5e6_r1_ckpt80
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    rel_f1: 0.0116
    ign_f1: 0.0116
    precision: 0.0109
    recall: 0.0124
    evi_f1: 0.828
    evi_precision: 0.928
    evi_recall: 0.748
    edcr: 0.993
    format_ok_rate: 0.999
    field_compliance_rate: 0.788
    pred_count: 13828
    gold_count: 12151
    n_truncated: 210
    inference_time_seconds: 6099
- exp_id: mvp2_eval_lr5e6_r1_ckpt60_r2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    rel_f1: 0.0093
    precision: 0.0085
    recall: 0.0103
    evi_f1: 0.81
    edcr: 0.993
    format_ok_rate: 0.998
    pred_count: 14626
    gold_count: 12151
    tp: 125
    inference_time_seconds: 6152
- exp_id: mvp2_eval_lr5e6_r1_ckpt100
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    rel_f1: 0.0138
    rel_precision: 0.0132
    rel_recall: 0.0144
    ign_f1: 0.0138
    evi_f1: 0.8504
    evi_precision: 0.9256
    evi_recall: 0.7866
    edcr: 0.9876
    format_ok_rate: 0.999
    field_compliance_rate: 0.8162
    evidence_format_rate: 0.8162
    tp: 175
    pred_count: 13300
    gold_count: 12151
    n_predictions: 15498
    n_truncated: 181
    n_documents: 985
    n_parseable: 984
    inference_time_seconds: 5901.7
- exp_id: mvp2_diversity_probe
  name: ''
  status: DONE
  conclusion: success
  metrics:
    unique_triples_t07: 5
    unique_triples_t10: 8
    jaccard_t07: 0.17
    jaccard_t10: 0.051
    format_ok_rate_t07: 0.5
    format_ok_rate_t10: 0.438
    n_samples: 3
    n_generations: 8
    note: 'unique_triples_t07 corrected from 7 to 5.0 (mean). Reviewer: format_ok
      ~34% after fix, ''diversity'' was JSON key name variants not semantic diversity'
- exp_id: mvp2_rsft_generate
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp2_rsft_gen_s0
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: mvp2_rsft_gen_s1
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: mvp2_rsft_gen_s2
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: mvp2_rsft_gen_s3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    generation_count: 5288
    unique_docs: 659
    format_compliance: 0.998
    diversity_range: 7.5-7.8/8
    exit_code: 0
- exp_id: mvp2_rsft_ced_scoring
  name: ''
  status: DONE
  conclusion: success
  metrics:
    input_generations: 21952
    selected_samples: 2718
    unique_docs: 2691
    selection_rate: 0.124
    mean_f1: 0.6157
    mean_ced: 0.6683
    f1_range:
    - 0.1026
    - 1
    zero_f1_samples: 0
    selection_strategy: top_k=1
    f1_threshold: 0.1
- exp_id: mvp2_rsft_train_r1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.0483
    num_preds: 848
    sft_baseline_rel_f1: 0.4057
    failure_mode: relation_ontology_collapse_to_freetext
    epoch1_eval_loss: 0.756
    epoch2_eval_loss: 0.759
- exp_id: mvp2_rsft_train_r1_s43
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_loss: 0.7622
    train_loss: 0.6148
    eval_entropy: 0.6724
    mean_token_accuracy: 0.8291
    total_steps: 510
    epochs: 3
    training_hours: 1.99
- exp_id: mvp2_rsft_train_r1_s44
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4655
    evi_f1: 0.8087
    evi_f1_joint: 0.3713
    evi_f1_joint_P: 0.3775
    evi_f1_joint_R: 0.3653
    edcr: 0.635
    sft_baseline_rel_f1: 0.4057
    sft_baseline_evi_f1: 0.7979
    delta_rel_f1: 0.0598
    delta_evi_f1: 0.0108
    delta_evi_f1_joint: 0.0596
    mvp2_pass: true
- exp_id: mvp2_rsft_ced_scoring_topk3
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_eval_rsft_s44
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_ced_reranker_poc
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ced_reranker_rel_f1: 0.486367
    ced_reranker_ign_f1: 0.473634
    ced_reranker_evi_f1: 0.8188
    oracle_rel_f1: 0.623746
    oracle_ign_f1: 0.612518
    random_rel_f1: 0.453783
    random_ign_f1: 0.439677
- exp_id: mvp2_rsft_diagnosis
  name: ''
  status: DONE
  conclusion: success
  metrics:
    root_cause: overfitting_plus_sft_knowledge_overwrite
    truncated_json_samples: 170
    truncated_pct: 6.3
    epoch1_eval_loss: 0.756
    epoch2_eval_loss: 0.759
    lora_scaling: 2
    rsft_zero_relation_samples: 170
    sft_zero_relation_docs: 26
    rsft_mean_relations: 11.2
    sft_mean_relations: 12.5
- exp_id: mvp2_rsft_train_r2_fix
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_rsft_r2a
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4494
    evi_f1: 0.8108
    edcr: 0.6641
    sft_baseline_rel_f1: 0.4057
    sft_baseline_evi_f1: 0.7979
    delta_rel_f1: 0.0437
    delta_evi_f1: 0.0129
    mvp2_pass: true
- exp_id: mvp2_rsft_r2b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4493
    evi_f1: 0.8128
    edcr: 0.6609
    sft_baseline_rel_f1: 0.4057
    sft_baseline_evi_f1: 0.7979
    delta_rel_f1: 0.0436
    delta_evi_f1: 0.0149
    mvp2_pass: true
- exp_id: mvp2_eval_rsft_r1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4449
    evi_f1: 0.8187
    evi_f1_joint: 0.3468
    evi_f1_joint_P: 0.3515
    evi_f1_joint_R: 0.3423
    edcr: 0.6565
    num_preds: 15307
    sft_baseline_rel_f1: 0.4057
    sft_baseline_evi_f1: 0.7979
    delta_rel_f1: 0.0392
    delta_evi_f1: 0.0208
    delta_evi_f1_joint: 0.0351
    mvp2_pass: true
- exp_id: mvp2_eval_rsft_r2a
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4494
    ign_f1: 0.4494
    evi_f1: 0.8108
    evi_f1_joint: 0.3509
    evi_f1_joint_P: 0.3423
    evi_f1_joint_R: 0.3599
    edcr: 0.6641
    precision: 0.4512
    recall: 0.4475
    evi_precision: 0.8143
    evi_recall: 0.8073
    format_ok_rate: 1
    n_predictions: 15482
    n_truncated: 208
    inference_time_s: 5967.2
    delta_evi_f1_joint: 0.0392
- exp_id: mvp2_eval_rsft_r2b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4493
    ign_f1: 0.4493
    evi_f1: 0.8128
    evi_f1_joint: 0.349
    evi_f1_joint_P: 0.3455
    evi_f1_joint_R: 0.3526
    edcr: 0.6609
    precision: 0.4566
    recall: 0.4424
    evi_precision: 0.8201
    evi_recall: 0.8056
    pred_count: 14829
    format_ok: 983/985
    truncated: 179
    inference_time_s: 5862
    delta_evi_f1_joint: 0.0373
- exp_id: mvp2_eval_rsft_s43
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp2_eval_rsft_s43_r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4683
    ign_f1: 0.4683
    evi_f1: 0.8156
    evi_f1_joint: 0.3711
    evi_f1_joint_P: 0.3747
    evi_f1_joint_R: 0.3675
    edcr: 0.6388
    precision: 0.4817
    recall: 0.4556
    evi_precision: 0.8142
    evi_recall: 0.817
    n_predictions: 14970
    n_truncated: 171
    format_ok_rate: 1
    inference_time_s: 6316.7
    sft_baseline_rel_f1: 0.4057
    sft_baseline_evi_f1: 0.7979
    delta_rel_f1: 0.0626
    delta_evi_f1: 0.0177
    delta_evi_f1_joint: 0.0594
    mvp2_pass: true
- exp_id: mvp2_eval_rsft_r2b_maxtok1536
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp2_eval_rsft_r2b_maxtok1536_r2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    rel_f1: 0.4504
    ign_f1: 0.4504
    evi_f1: 0.8102
    edcr: 0.674
    precision: 0.4488
    recall: 0.4519
    evi_precision: 0.8162
    evi_recall: 0.8044
    n_truncated: 146
    n_total: 985
    n_predictions: 17188
    n_distractor_citations: 19589
    n_total_citations: 29063
    format_ok_rate: 0.998
- exp_id: mvp2_rsft_ced_scoring_topk3_r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    input_generations: 21728
    selected_samples: 8037
    unique_docs: 2691
    selection_rate: 0.37
    mean_f1: 0.5761
    mean_ced: 0.6205
    mean_combined: 0.6787
    f1_range_p25: 0.444
    f1_range_p75: 0.717
    ced_range_p25: 0.487
    ced_range_p75: 0.774
    truncated_samples: 1924
    truncated_pct: 8.9
    selection_strategy: top_k=3
    f1_threshold: 0.1
    topk1_samples: 2718
    data_multiplier: 2.96
- exp_id: plan_004_dreeam_baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    dev_rel_f1: 63.57
    dev_rel_ign_f1: 61.72
    dev_evi_f1: 54.01
    dev_rel_p: 66.95
    dev_rel_r: 60.51
    dev_evi_p: 60.53
    dev_evi_r: 48.76
- exp_id: plan_011_grpo_g8_bf16
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_step: 100
    train_runtime_s: 554
    reward_final: 1.795
    f1_reward_final: 1.002
    ced_reward_final: 0.494
    format_reward_final: 0.3
    frac_zero_std_final: 0
    kl_final: 0.022
    best_reward_step: 85
    best_reward: 2.858
    best_f1_reward: 1.85
    mode_collapse: false
    lora_config: r=64, alpha=128, dropout=0.05, bf16
    checkpoints: 10 checkpoints (step 10-100)
- exp_id: plan_001_flat_nli_scoring
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_scored: 21728
    selected_samples: 2691
    selection_rate: 0.124
    selection_strategy: top_k=1
    f1_threshold: 0.1
    output_path: /root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl
- exp_id: eval_grpo_g8_bf16
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ckpt80_rel_f1: 0.4456
    ckpt80_ign_f1: 0.4456
    ckpt80_evi_f1: 0.8034
    ckpt80_edcr: 0.6409
    ckpt80_format_ok: 984/985
    ckpt80_truncated: 50
    ckpt90_rel_f1: 0.4523
    ckpt90_ign_f1: 0.4523
    ckpt90_evi_f1: 0.8052
    ckpt90_edcr: 0.6414
    ckpt90_format_ok: 983/985
    ckpt90_truncated: 61
    ckpt100_rel_f1: 0.4549
    ckpt100_ign_f1: 0.4549
    ckpt100_evi_f1: 0.8086
    ckpt100_edcr: 0.6318
    ckpt100_format_ok: 985/985
    ckpt100_truncated: 61
    best_checkpoint: ckpt-100
- exp_id: plan_011_eval_g8_bf16_ckpt100
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: plan_011_grpo_g8_bf16_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4549
    ign_f1: 0.4549
    evi_f1: 0.8086
    edcr: 0.6318
    format_ok_rate: 1
    n_truncated: 61
    n_total: 985
    n_predictions: 10701
    checkpoint: checkpoint-100
    model: Qwen3-4B + SFT merged + GRPO bf16 LoRA ckpt-100
    inference_time_s: 3170.3
- exp_id: plan_001_rsft_flat_nli
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.6238
    train_loss_min: 0.5803
    mean_token_accuracy: 0.8528
    train_runtime_sec: 2946
    epochs: 3
    total_steps: 507
    samples: 2691
- exp_id: plan_012_dpo_ced
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    rel_f1: 0.3429
    evi_f1: 0.8403
    edcr: 0.7294
    format_ok_rate: 0.995
    checkpoint: checkpoint-501
    rewards_accuracy: 1
    margins: 9.01
- exp_id: plan_014_sft_no_evidence
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.7077
    eval_loss: 0.8781
    eval_token_accuracy: 0.8086
    epochs: 3
    total_steps: 570
    train_runtime_min: 64
    samples: 3027
    trainable_params: 132M/4.15B (3.18%)
- exp_id: plan_015_grpo_g4_bf16
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: plan_015_grpo_g4_bf16_v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: plan_015_grpo_g4_bf16_v3
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: eval_plan_001_flat_nli
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4539
    ign_f1: 0.4539
    evi_f1: 0.8043
    edcr: 0.6431
    precision: 0.4671
    recall: 0.4414
    evi_precision: 0.8143
    evi_recall: 0.7945
    format_ok_rate: 1
    n_truncated: 199
    n_documents: 985
    n_predictions: 15294
    inference_time_seconds: 3631
- exp_id: eval_plan_014_sft_no_evidence
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4893
    rel_ign_f1: 0.4893
    rel_precision: 0.4884
    rel_recall: 0.4902
    evi_f1: 0
    evi_precision: 0
    evi_recall: 0
    edcr: 0
    format_ok_rate: 0.9919
    n_truncated: 298
    n_predictions: 21064
    n_documents: 985
    n_parseable: 977
    inference_time_seconds: 4103.8
- exp_id: plan_008_rsft_topk3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.5543
    eval_loss: 0.8297
    eval_mean_token_accuracy: 0.8228
    eval_entropy: 0.6001
    train_runtime_sec: 10916
    total_steps: 1509
    epochs: 3
    trainable_params_pct: 3.18
    rsft_samples: 8037
    ced_score_mean: 0.621
    task_eval_f1_ep1: 0.4848
    task_eval_f1_ep2: 0.4824
    task_eval_f1_ep3: 0.5012
    task_eval_evi_f1_ep1: 0.745
    task_eval_evi_f1_ep2: 0.6997
    task_eval_evi_f1_ep3: 0.6816
    task_eval_edcr_ep1: 0.6525
    task_eval_edcr_ep2: 0.6529
    task_eval_edcr_ep3: 0.5963
    task_eval_note: 50-doc subset, not full dev
- exp_id: plan_002_test_eval_s44
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan_001_flat_nli_seed43
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss_final: 0.6257
    train_loss_min: 0.5895
    eval_loss_epoch3: 0.7567
    eval_accuracy_epoch3: 0.8298
    total_steps: 507
    epochs: 3
    train_runtime_seconds: 6880
    task_eval_f1_ep1: 0.4825
    task_eval_f1_ep2: 0.4542
    task_eval_f1_ep3: 0.4866
    task_eval_evi_f1_ep3: 0.7834
    task_eval_edcr_ep3: 0.6402
    task_eval_note: 50-doc subset, not full dev
- exp_id: eval_sft_baseline_noquant
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4106
    rel_precision: 0.4198
    rel_recall: 0.4019
    evi_f1: 0.8013
    evi_precision: 0.8005
    evi_recall: 0.8022
    evi_f1_joint: 0.3216
    edcr: 0.7039
    format_ok_rate: 0.998
    field_compliance_rate: 0.7066
    n_predictions: 16774
    n_truncated: 288
    n_documents: 985
    inference_time_seconds: 3677.9
- exp_id: plan_012_dpo_ced_1ep
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    rel_f1: 0.0022
    evi_f1: 0.75
    edcr: 0.9982
    format_ok: 981/985
    truncated: 358/985
    tp: 34
    n_preds: 19265
    inference_time_s: 3643
    train_loss_final: 0.59
    rewards_accuracy: 0.82
    rewards_margins: 0.86
    total_steps: 167
    training_time_min: 33
- exp_id: plan_009_forgetting_figure
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: plan_011_bf16_g8_step_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    step_30:
      rel_f1: 0.434
      evi_f1: 0.8063
      edcr: 0.6807
    step_50:
      rel_f1: 0.4276
      evi_f1: 0.8024
      edcr: 0.6855
    step_70:
      rel_f1: 0.4341
      evi_f1: 0.8099
      edcr: 0.6685
    best_step: step_70
    trend: non-monotonic, all < ckpt-100 (0.4549)
- exp_id: plan_009_extract_reward_eval
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan_009_flatnli_reward_eval
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: eval_plan_012_dpo_ced_ckpt400
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan_009_flatnli_reward_eval_r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: eval_plan_012_dpo_ced_1ep
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    rel_f1: 0.0022
    ign_f1: 0.0022
    evi_f1: 0.75
    edcr: 0.9982
    num_preds: 19265
    format_ok: 981/985
    truncated: 358/985
    tp: 34
    inference_time_s: 3643
- exp_id: eval_plan_001_flat_nli_s43
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    rel_f1: 0.0022
    ign_f1: 0.0022
    evi_f1: 0.8533
    edcr: 0.9982
    num_preds: 17285
    format_ok: 981/985
    truncated: 251/985
    tp: 32
    note: INVALID — missing --sft_adapter, same bug as DPO 1ep eval
- exp_id: plan_001_flat_nli_seed45
  name: ''
  status: DONE
  conclusion: success
  metrics:
    task_eval_rel_f1: 0.4876
    task_eval_evi_f1: 0.7927
    task_eval_edcr: 0.6517
    train_loss: 0.6245
    runtime_hours: 1.69
    note: task-eval on 50 docs only, full dev eval needed
- exp_id: eval_plan_008_rsft_topk3
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    note: INVALID — missing --sft_adapter, killed by Director instruction
- exp_id: plan_001_flat_nli_seed44
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.6247
    eval_loss: 0.7564
    eval_mean_token_accuracy: 0.8299
    task_eval_f1_ep1: 0.4306
    task_eval_f1_ep2: 0.4884
    task_eval_f1_ep3: 0.4897
    task_eval_evi_f1_ep3: 0.78
    task_eval_edcr_ep3: 0.6596
    task_eval_ign_f1_ep3: 0.4897
    train_runtime_sec: 6197
    num_epochs: 3
    total_steps: 507
- exp_id: eval_plan_012_dpo_1ep_fixed
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: eval_plan_008_topk3_fixed
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: eval_plan_012_dpo_1ep_fixed_r2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    rel_f1: 0.4034
    evi_f1: 0.8088
    edcr: 0.7139
    format_ok_rate: 0.999
    truncated_rate: 0.343
    predictions: 19107
    ign_f1: 0.4034
    precision: 0.3809
    recall: 0.4287
    vs_sft_delta: -0.0023
    note: DPO 1ep matches SFT baseline. 1ep→3ep trajectory shows gradual decoupling
      (rel_f1↓ evi_f1↑), consistent with GRPO pattern. Ign-F1=F1 exact match needs
      investigation.
- exp_id: reeval_flat_nli_s43
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4523
    ign_f1: 0.4523
    evi_f1: 0.8158
    edcr: 0.6505
    num_preds: 15357
    format_ok: 984/985
    truncated: 211/985
    inference_time_s: 3515.8
- exp_id: reeval_rsft_topk3
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    rel_f1: 0.4454
    rel_precision: 0.4512
    rel_recall: 0.4398
    ign_f1: 0.4364
    evi_f1: 0.8088
    edcr: 0.6635
    format_ok_rate: 0.999
    n_truncated: 214
    n_predictions: 16020
    inference_time_seconds: 3546.4
    ign_f1_corrected: true
- exp_id: eval_flat_nli_seed44
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: eval_flat_nli_seed45
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.455052
    ign_f1: 0.446181
    evi_f1: 0.815399
    edcr: 0.652133
    evi_f1_joint: 0.355612
- exp_id: plan_003_edcr_diagnostic
  name: ''
  status: DONE
  conclusion: success
  metrics:
    methods_evaluated: 15
    edcr_vs_rel_f1_spearman: -0.9648
    edcr_vs_rel_f1_pvalue: 0.0001
    edcr_vs_evi_f1_spearman: 0.0022
    edcr_vs_evi_f1_pvalue: 0.9941
    edcr_range: 0.63-0.99
    unique_diagnostic_value: identifies pathological models (GRPO QLoRA) with high
      evi_f1 but catastrophically low rel_f1
- exp_id: eval_flat_nli_s44
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.461506
    ign_f1: 0.452126
    evi_f1: 0.813123
    edcr: 0.645808
    evi_f1_joint: 0.359673
- exp_id: plan_009_dynamics_figure
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: eval_plan_014_no_evidence
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: rsft_ced_s45_train
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: rsft_ced_s43_train
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: rsft_ced_s45_train_r2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: rsft_ced_s43_train_r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: rsft_ced_s43_train_r3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.6151
    eval_loss: 0.7618
    task_eval_f1: 0.5026
    task_eval_ign_f1: 0.4932
    task_eval_evi_f1: 0.7624
    task_eval_edcr: 0.6516
    total_steps: 510
    epochs: 3
    training_hours: 1.82
- exp_id: rsft_ced_s45_train_r3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: rsft_ced_s45_train_r4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    training_completed: true
    checkpoint: checkpoint-510
    note: Training metrics not captured (r4 retry after OOM). Eval running as eval_rsft_ced_s45.
- exp_id: eval_rsft_ced_s45
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4514
    ign_f1: 0.4416
    evi_f1: 0.8174
    rel_p: 0.4718
    rel_r: 0.4326
    edcr: 0.655
    evi_f1_joint: 0.3558
    n_truncated: 206
    format_ok_rate: 1
- exp_id: eval_rsft_ced_s43
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4601
    ign_f1: 0.4512
    precision: 0.4696
    recall: 0.4509
    evi_f1: 0.8063
    evi_precision: 0.8025
    evi_recall: 0.8101
    edcr: 0.6542
    evi_f1_joint: 0.3605
    format_ok_rate: 1
    n_truncated: 184
    n_predictions: 15051
    inference_time_seconds: 10768.2
- exp_id: eval_plan_014_no_evidence_r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4876
    ign_f1: 0.4721
    evi_f1: 0
    edcr: 0
    evi_f1_joint: 0
    precision: 0.4901
    recall: 0.4851
    ign_precision: 0.4654
    ign_recall: 0.4791
    format_compliance: 0.993
    truncation_rate: 0.312
    n_predictions: 21181
    n_documents: 985
- exp_id: reeval_flat_nli_s43_r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4586
    rel_precision: 0.4732
    rel_recall: 0.4449
    ign_f1: 0.4503
    evi_f1: 0.8113
    evi_precision: 0.8035
    evi_recall: 0.8192
    evi_f1_joint: 0.358
    edcr: 0.6552
    format_ok_rate: 0.999
    n_truncated: 184
    n_predictions: 15015
- exp_id: seed_comparison_prep
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: reeval_ced_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ign_f1: 0.4423
    rel_f1: 0.4517
    evi_f1: 0.8175
    evi_f1_joint: 0.3518
    edcr: 0.6569
    format_compliance_rate: 1
    field_compliance_rate: 0.7756
    n_truncated: 214
    inference_time_seconds: 10815.5
- exp_id: reeval_ced_s44
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ign_f1: 0.4511
    rel_f1: 0.4621
    evi_f1: 0.805
    evi_f1_joint: 0.3677
    edcr: 0.635
    format_compliance_rate: 1
    field_compliance_rate: 0.802
    n_truncated: 190
    inference_time_seconds: 13077.6
- exp_id: reeval_flat_nli_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ign_f1: 0.4448
    rel_f1: 0.4535
    evi_f1: 0.8039
    evi_f1_joint: 0.3558
    edcr: 0.6458
    format_compliance_rate: 1
    field_compliance_rate: 0.7787
    n_truncated: 205
    inference_time_seconds: 13253.1
- exp_id: reeval_sft_baseline_d076
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4049
    ign_f1: 0.3974
    evi_f1: 0.7986
    edcr: 0.6982
    evi_f1_joint: 0.3147
    format_compliance_rate: 0.998
    n_truncated: 288
    n_documents: 985
    n_predictions: 16880
    inference_time_sec: 7056.5
- exp_id: plan_006_qwen3_1_7b_sft
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: plan_006_qwen3_1_7b_sft_bf16
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.6884
    eval_loss: 0.8031
    eval_mean_token_accuracy: 0.8238
    eval_entropy: 0.682
    train_runtime_sec: 2473
    train_samples_per_second: 3.672
    epochs: 3
    total_steps: 570
- exp_id: plan_006_qwen3_1_7b_no_evidence_sft
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: plan_006_qwen3_8b_sft_bf16
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.5705
    eval_loss: 0.7186
    eval_mean_token_accuracy: 0.8377
    eval_entropy: 0.5614
    train_runtime_s: 3932
    epoch: 3
- exp_id: plan_006_qwen3_1_7b_sft_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    f1: 0.4945
    ign_f1: 0.4786
    evi_f1: 0.8316
    edcr: 0.6704
    precision: 0.5085
    recall: 0.4813
    ign_precision: 0.483
    ign_recall: 0.4743
    evi_precision: 0.8203
    evi_recall: 0.8432
    evi_f1_joint: 0.3958
    format_compliance_rate: 1
    n_predictions: 17184
    n_truncated: 314
    inference_time_seconds: 6848.7
- exp_id: plan_002_test_eval_s44_r2
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: reeval_flat_nli_s44
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: plan_006_qwen3_8b_sft_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ign_f1: 0.5051
    f1: 0.5262
    evi_f1: 0.8188
    edcr: 0.651
    format_ok_rate: 0.999
    n_truncated: 313
    n_predictions: 17401
    inference_time_s: 7206
- exp_id: plan_006_qwen3_1_7b_no_evidence_eval
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    f1: 0.3884
    ign_f1: 0.3786
    evi_f1: 0.0007
    edcr: 0.9848
    precision: 0.4282
    recall: 0.3553
    pred_count: 27049
    n_truncated: 531
    format_ok_rate: 0.999
- exp_id: plan_006_qwen3_8b_no_evidence_sft
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.6509
    eval_loss: 0.8153
    eval_mean_token_accuracy: 0.8174
    eval_entropy: 0.6275
    train_runtime_sec: 3656
    epoch: 3
- exp_id: plan_016_llama_3_1_8b_sft
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: plan_016_llama_3_1_8b_no_evidence_sft
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: plan_006_qwen3_8b_no_evidence_eval
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: plan_006_qwen3_8b_no_evidence_eval_v2
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: plan_006_qwen3_1_7b_no_evidence_eval_v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan_006_qwen3_1_7b_no_evidence_eval_v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ign_f1: 0.3982
    rel_f1: 0.4103
    evi_f1: 0
    edcr: 0
    precision: 0.4464
    recall: 0.3796
    format_compliance_rate: 1
    n_truncated: 501
    inference_time_seconds: 7465.3
    evidence_tax: 0.0804
- exp_id: plan_006_qwen3_1_7b_no_evidence_eval_v2r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan_016_llama_3_1_8b_no_evidence_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ign_f1: 0.5452
    rel_f1: 0.5624
    evi_f1: 0
    edcr: 0
- exp_id: plan_016_llama_3_1_8b_sft_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ign_f1: 0.5384
    rel_f1: 0.5514
    evi_f1: 0.8151
    edcr: 0.628
    precision: 0.5464
    recall: 0.5565
    evi_f1_joint: 0.4317
    format_compliance_rate: 0.9949
    n_truncated: 197
    n_predictions: 15325
    inference_time_seconds: 7331.3
    evidence_tax_ign_f1: 0.0068
    evidence_tax_rel_f1: 0.011
- exp_id: plan_007_redocred_4b_sft_eval
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan_007_redocred_4b_sft_eval_r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ign_f1: 0.3659
    f1: 0.3706
    evi_f1: 0.817
    edcr: 0.6674
    format_compliance_rate: 0.996
    n_truncated: 139
    n_total: 493
    inference_time_seconds: 3281.7
    precision: 0.4316
    recall: 0.3247
    ign_precision: 0.4134
    ign_recall: 0.3282
    evi_precision: 0.8208
    evi_recall: 0.8131
    n_predictions: 8191
- exp_id: plan_016_llama_grpo_qlora
  name: ''
  status: DONE
  conclusion: success
  metrics:
    format_reward: 1
    f1_reward: 0
    ced_reward: 0
    entropy: 0.28
    final_step: 60
    grad_norm: 0
    loss: 0
    frac_reward_zero_std: 1
    output_length_final: 172
    conclusion_note: 'C2 cross-family validated: LLaMA QLoRA GRPO shows same catastrophic
      decoupling as Qwen (format gaming, zero IE ability)'
- exp_id: plan_006_qwen3_8b_rsft_candidates
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: plan_006_qwen3_1_7b_rsft_candidates
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: plan_016_llama_rsft_candidates
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan_007_redocred_rsft_eval
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan_016_llama_rsft_candidates_r2
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    docs_completed: 64
    docs_total: 3027
    lines_generated: 512
    output_path: /root/autodl-tmp/freige/outputs/rsft_candidates_llama_8b/generations.jsonl
    failure_reason: Process killed externally (no traceback/error in log). Likely
      OOM on cuda:1. Completed 64/3027 docs (2.1%) in ~23min before termination.
- exp_id: plan_014_no_evidence_eval_d076
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: plan_016_llama_rsft_candidates_r3
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: best
narrative_guidance: "..."
imagined_experiments:
  - name: "..."
    plan_id: "..."
    description: "..."
    expected_results: {metric: value, ...}
    result_rationale: "..."
    tables: []
    figures_description: []
    analysis: "..."
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e6158723-310f-41d5-bf89-7a89d5ed4fef",
  "type": "user",
  "uuid": "ca2b093d-5b61-4b31-9caf-a81343bbe6c1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T16:00:41.829Z_

```json
{
  "parentUuid": "ca2b093d-5b61-4b31-9caf-a81343bbe6c1",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "abe95612-ed8f-40b4-934a-dc8f38235ef1",
  "timestamp": "2026-05-16T16:00:41.829Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T16:00:41.829Z_

```json
{
  "parentUuid": "abe95612-ed8f-40b4-934a-dc8f38235ef1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f4652f07-6aff-41da-aeaa-50255b256a29",
  "timestamp": "2026-05-16T16:00:41.829Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：剩余实验全面确认 dev 发现，test 数字坚挺，DREEAM-protocol 对齐有竞争力，EDCR 人工验证通过——5-claim 框架完全成立，EMNLP Main 可直接投稿 核心假设：['Test set Ign-F1 退化 ≤1.5pp（dev 45.85 → test ≥44.3），no-e…",
  "leafUuid": "f4652f07-6aff-41da-aeaa-50255b256a29",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evidence-grounded DocRE scaling and decoupling analysis",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0"
}
```

---

### Assistant

_source line 8 · 2026-05-16T16:01:27.181Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment_plan, under the "best" tier scenario. Let me identify which experiments are still "planned":

1. **plan_002** - Test set evaluation (status: planned)
2. **plan_007** - Re-DocRED cross-dataset (status: planned) - though some related experiments have been done (plan_007_redocred_4b_sft_eval_r2 is DONE)
3. **plan_013** - EDCR human annotation validation (status: planned)


4. **plan_010** - NLI model ablation (status: planned)

So I need to generate predicted results for these four planned experiments. Let me start with the ones that have the clearest expected outcomes based on the patterns I'm seeing in the existing results.

I'm also noticing several experiments currently running—plan_006 has two scaling variants in progress, plan_014 is evaluating the no-evidence scenario, and plan_016 is working on the third round of Llama RSFT candidates. For the "best" tier classification, I need to keep in mind the performance degradation threshold of 1.5 percentage points on the test set (dev 45.85 → test ≥44.3) and adherence to the DREEAM protocol.

Looking at the additional criteria, I'm tracking evidence F1 scores needing to stay above 0.50, EDCR correlation with human annotations at 0.70 or higher, and the gap between post-hoc retrieval and RSFT performance—where SFT+BM25 should show evidence F1 ≤0.70 compared to RSFT's 0.81, indicating at least a 10 percentage point improvement. The 8B and 1.7B RSFT candidates are showing success with scale-dependent gains. I'm also compiling the expected metric ranges across different configurations to establish the performance boundaries.

Now I'm reviewing the planned experiments that still need predictions: the test set evaluation, Re-DocRED cross-dataset validation for RSFT, EDCR human validation, and the NLI model ablation, along with the post-hoc retrieval baseline comparison. For test set evaluation, I expect some degradation from the dev performance—probably around 45.0-45.5 for RSFT and 46.5-47.0 without evidence, with a similar evidence tax of 1.5-2 percentage points. On Re-DocRED, RSFT should show the same kind of improvement over SFT that we see on DocRED, roughly 3-5 points. For the human validation task, I'm targeting a Spearman correlation of at least 0.70 as the best tier threshold.

EDCR shows strong method-level correlation with relation F1 and meaningful diagnostic value at the per-relation level, so it should correlate well with human judgments of evidence faithfulness. The NLI model ablation between DeBERTa-v3-large and base will likely show only modest gains from the larger model. For the post-hoc retrieval baseline, BM25 is a reasonable approach but imperfect—I'm expecting evidence F1 around 0.70 or lower with a gap of at least 10 points compared to RSFT's 0.81. The 8B and 1.7B RSFT experiments are currently running.

Looking at the smaller model results, the 1.7B shows SFT ignoring F1 at 0.4786 with no-evidence at 0.3982, so evidence helps by about 8 points and RSFT should push further. The 8B model has similar patterns with SFT ignoring F1 at 0.5051, and RSFT should improve from there as well. I need to focus on the explicitly planned items—plan_002, plan_007, plan_013, and plan_010—plus the 8B/1.7B RSFT experiments that are part of validating the best tier hypothesis. I'm going to structure this as YAML to organize the predictions for each experiment clearly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4652f07-6aff-41da-aeaa-50255b256a29",
  "isSidechain": false,
  "requestId": "req_011Cb6XWoQpsbB1Etwcti8bk",
  "type": "assistant",
  "uuid": "778ec2b9-0e3d-4988-ba47-084b023643e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012nkgXKWTaRhpcFSQoK9Yye",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 36898,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36898,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2100,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 36898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36898
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

_source line 9 · 2026-05-16T16:01:27.251Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01T1iYNrAYjRDABDoobJ1gDK`</summary>

```json
{
  "pattern": "**/*experiment_plan*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "778ec2b9-0e3d-4988-ba47-084b023643e3",
  "isSidechain": false,
  "requestId": "req_011Cb6XWoQpsbB1Etwcti8bk",
  "type": "assistant",
  "uuid": "2620396b-1594-418d-b0ff-f4a19d4b2cd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012nkgXKWTaRhpcFSQoK9Yye",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 36898,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36898,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2100,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 36898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36898
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

_source line 10 · 2026-05-16T16:01:27.268Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014afetSH7ZdajVi2YyVNCRd`</summary>

```json
{
  "pattern": "**/dream_tiers*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2620396b-1594-418d-b0ff-f4a19d4b2cd7",
  "isSidechain": false,
  "requestId": "req_011Cb6XWoQpsbB1Etwcti8bk",
  "type": "assistant",
  "uuid": "a7a35171-def1-4056-afd3-4ccdb216a7df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012nkgXKWTaRhpcFSQoK9Yye",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 36898,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36898,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2100,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 36898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36898
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

_source line 11 · 2026-05-16T16:01:27.289Z_

<details><summary>↩ Tool result · `toolu_01T1iYNrAYjRDABDoobJ1gDK`</summary>

```text
projects/faith-evidence-ie/experiment_plan.lock
projects/faith-evidence-ie/logs/workers/worker_experiment_plan_006_qwen3_1_7b_sft_20260516T052333.log
projects/faith-evidence-ie/logs/workers/worker_experiment_plan_006_qwen3_1_7b_sft_20260516T052333_result.json
projects/faith-evidence-ie/logs/workers/worker_experiment_plan_006_qwen3_1_7b_sft_submit_20260516T061421.log
projects/faith-evidence-ie/logs/chats/worker_experiment_plan_006_qwen3_1_7b_sft_submit_20260516T061421.lock
projects/faith-evidence-ie/logs/chats/worker_experiment_plan_006_qwen3_1_7b_sft_submit_20260516T061421.jsonl
projects/faith-evidence-ie/logs/workers/worker_experiment_plan_006_qwen3_1_7b_sft_submit_20260516T061421_result.json
projects/faith-evidence-ie/logs/workers/worker_experiment_plan_006_qwen3_1_7b_sft_bf16_20260516T063412.log
projects/faith-evidence-ie/logs/workers/worker_experiment_plan_006_qwen3_1_7b_sft_bf16_20260516T063412_result.json
projects/faith-evidence-ie/logs/workers/worker_experiment_plan_002_test_eval_20260516T081231.log
projects/faith-evidence-ie/logs/chats/worker_experiment_plan_002_test_eval_20260516T081231.lock
projects/faith-evidence-ie/logs/chats/worker_experiment_plan_002_test_eval_20260516T081231.jsonl
projects/faith-evidence-ie/logs/workers/worker_experiment_plan_002_test_eval_20260516T081231_result.json
projects/faith-evidence-ie/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2620396b-1594-418d-b0ff-f4a19d4b2cd7",
  "isSidechain": false,
  "promptId": "e6158723-310f-41d5-bf89-7a89d5ed4fef",
  "type": "user",
  "uuid": "aeffc8d5-2946-4c4f-8f2e-3207ea37ca75",
  "toolUseResult": {
    "filenames": [
      "projects/faith-evidence-ie/experiment_plan.lock",
      "projects/faith-evidence-ie/logs/workers/worker_experiment_plan_006_qwen3_1_7b_sft_20260516T052333.log",
      "projects/faith-evidence-ie/logs/workers/worker_experiment_plan_006_qwen3_1_7b_sft_20260516T052333_result.json",
      "projects/faith-evidence-ie/logs/workers/worker_experiment_plan_006_qwen3_1_7b_sft_submit_20260516T061421.log",
      "projects/faith-evidence-ie/logs/chats/worker_experiment_plan_006_qwen3_1_7b_sft_submit_20260516T061421.lock",
      "projects/faith-evidence-ie/logs/chats/worker_experiment_plan_006_qwen3_1_7b_sft_submit_20260516T061421.jsonl",
      "projects/faith-evidence-ie/logs/workers/worker_experiment_plan_006_qwen3_1_7b_sft_submit_20260516T061421_result.json",
      "projects/faith-evidence-ie/logs/workers/worker_experiment_plan_006_qwen3_1_7b_sft_bf16_20260516T063412.log",
      "projects/faith-evidence-ie/logs/workers/worker_experiment_plan_006_qwen3_1_7b_sft_bf16_20260516T063412_result.json",
      "projects/faith-evidence-ie/logs/workers/worker_experiment_plan_002_test_eval_20260516T081231.log",
      "projects/faith-evidence-ie/logs/chats/worker_experiment_plan_002_test_eval_20260516T081231.lock",
      "projects/faith-evidence-ie/logs/chats/worker_experiment_plan_002_test_eval_20260516T081231.jsonl",
      "projects/faith-evidence-ie/logs/workers/worker_experiment_plan_002_test_eval_20260516T081231_result.json",
      "projects/faith-evidence-ie/experiment_plan.yaml"
    ],
    "durationMs": 28,
    "numFiles": 14,
    "truncated": false
  },
  "sourceToolAssistantUUID": "2620396b-1594-418d-b0ff-f4a19d4b2cd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T16:01:27.294Z_

<details><summary>↩ Tool result · `toolu_014afetSH7ZdajVi2YyVNCRd`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7a35171-def1-4056-afd3-4ccdb216a7df",
  "isSidechain": false,
  "promptId": "e6158723-310f-41d5-bf89-7a89d5ed4fef",
  "type": "user",
  "uuid": "76f84d74-c41c-403d-8f42-59fd61f1b8df",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 22,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "a7a35171-def1-4056-afd3-4ccdb216a7df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T16:01:38.051Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WFEobVS6sxtkBDBCYtziZT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76f84d74-c41c-403d-8f42-59fd61f1b8df",
  "isSidechain": false,
  "requestId": "req_011Cb6Xa9g4uHsLNpLrNsfRU",
  "type": "assistant",
  "uuid": "f269bac8-b01c-4f01-9b75-63c9c108a1ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLB1e9KjjJ63zHFWtdQ526",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2670,
      "cache_read_input_tokens": 48739,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2670,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 102,
          "cache_read_input_tokens": 48739,
          "cache_creation_input_tokens": 2670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2670
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

_source line 14 · 2026-05-16T16:01:38.077Z_

<details><summary>↩ Tool result · `toolu_01WFEobVS6sxtkBDBCYtziZT`</summary>

```text
1	experiments:
2	- id: plan_001
3	  claim: 2
4	  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选
5	    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py
6	    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'
7	  priority: P0
8	  gpu_budget_hours: 20
9	  deps: []
10	  registry_id: eval_flat_nli_seed45
11	- id: plan_002
12	  claim: 1
13	  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set
14	    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'
15	  priority: P0
16	  gpu_budget_hours: 4
17	  deps:
18	  - plan_001
19	  registry_id: null
20	- id: plan_003
21	  claim: 4
22	  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing
23	    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'
24	  priority: P0
25	  gpu_budget_hours: 2
26	  deps:
27	  - plan_001
28	  registry_id: plan_003_edcr_diagnostic
29	- id: plan_004
30	  claim: 1
31	  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)
32	    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'
33	  priority: P0
34	  gpu_budget_hours: 8
35	  deps: []
36	  registry_id: plan_004_dreeam_baseline
37	- id: plan_005
38	  claim: 1
39	  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'
40	  priority: P1
41	  gpu_budget_hours: 6
42	  deps: []
43	  registry_id: mvp2_ced_reranker_poc
44	- id: plan_006
45	  claim: 1
46	  description: 'Model size ablation (D077 升 P0): Qwen3-1.7B 和 Qwen3-8B 上复现 SFT → RSFT
47	    → eval pipeline，验证 evidence tax + RSFT 增益 + decoupling 在不同模型规模下成立。应对 RC4 和 scope
48	    不足问题。'
49	  priority: P0
50	  gpu_budget_hours: 32
51	  deps: []
52	  registry_id: plan_006_qwen3_1_7b_no_evidence_eval_v3
53	- id: plan_007
54	  claim: 1
55	  description: 'Re-DocRED cross-dataset (D077 升 P0): 在 Re-DocRED 上用当前 best config
56	    做 SFT → RSFT → eval。数据已就绪（格式与 DocRED 兼容，96 relation types 一致）。⚠️ Re-DocRED ~55%
57	    triples 无 evidence 标注（修正的 false negative），必须报告两种模式：evidence_only（与 DocRED 可比的
58	    evi_f1，仅 43% triples）+ full（全部 triples 的 rel_f1，无 evi_f1）。转换脚本已支持 --mode full。'
59	  priority: P0
60	  gpu_budget_hours: 16
61	  deps: []
62	  registry_id: null
63	- id: plan_016
64	  claim: 2
65	  description: 'LLaMA-3.1-8B cross-family validation (D077 新增): 在非 Qwen 家族模型上复现核心
66	    pipeline (SFT → RSFT → GRPO QLoRA)，验证 decoupling spectrum 跨模型家族成立。关键实验：LLaMA GRPO
67	    QLoRA 是否也出现 catastrophic forgetting。'
68	  priority: P0
69	  gpu_budget_hours: 40
70	  deps: []
71	  registry_id: plan_016_llama_rsft_candidates
72	- id: plan_008
73	  claim: 2
74	  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格
75	    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'
76	  priority: P1
77	  gpu_budget_hours: 8
78	  deps: []
79	  registry_id: reeval_rsft_topk3
80	- id: plan_011
81	  claim: 3
82	  description: 'GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward
83	    + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要
84	    gradient_accumulation 适配显存。'
85	  priority: P0
86	  gpu_budget_hours: 8
87	  deps: []
88	  registry_id: plan_011_bf16_g8_step_eval
89	- id: plan_012
90	  claim: 3
91	  description: 'DPO+CED experiment: 用 RSFT 候选数据构造 preference pairs (CED-preferred
92	    vs CED-rejected)，DPO 训练。验证 DPO 是否避免 GRPO 的 catastrophic forgetting。Dream v2 三档要求
93	    DPO 作为 RL spectrum 关键数据点，必须补全训练超参（β, lr, epochs, pair construction）。D045 升 P0。'
94	  priority: P0
95	  gpu_budget_hours: 12
96	  deps: []
97	  registry_id: plan_012_dpo_ced
98	- id: plan_013
99	  claim: 4
100	  description: 'EDCR 人工标注验证: 100 个样本，人工判断每个 cited evidence sentence 是否真正支持对应 relation。计算
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f269bac8-b01c-4f01-9b75-63c9c108a1ee",
  "isSidechain": false,
  "promptId": "e6158723-310f-41d5-bf89-7a89d5ed4fef",
  "type": "user",
  "uuid": "3c408873-a8e5-4320-9f2e-ed3a9444300b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
      "content": "experiments:\n- id: plan_001\n  claim: 2\n  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选\n    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py\n    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: eval_flat_nli_seed45\n- id: plan_002\n  claim: 1\n  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set\n    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  registry_id: null\n- id: plan_003\n  claim: 4\n  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing\n    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: plan_003_edcr_diagnostic\n- id: plan_004\n  claim: 1\n  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)\n    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_004_dreeam_baseline\n- id: plan_005\n  claim: 1\n  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: mvp2_ced_reranker_poc\n- id: plan_006\n  claim: 1\n  description: 'Model size ablation (D077 升 P0): Qwen3-1.7B 和 Qwen3-8B 上复现 SFT → RSFT\n    → eval pipeline，验证 evidence tax + RSFT 增益 + decoupling 在不同模型规模下成立。应对 RC4 和 scope\n    不足问题。'\n  priority: P0\n  gpu_budget_hours: 32\n  deps: []\n  registry_id: plan_006_qwen3_1_7b_no_evidence_eval_v3\n- id: plan_007\n  claim: 1\n  description: 'Re-DocRED cross-dataset (D077 升 P0): 在 Re-DocRED 上用当前 best config\n    做 SFT → RSFT → eval。数据已就绪（格式与 DocRED 兼容，96 relation types 一致）。⚠️ Re-DocRED ~55%\n    triples 无 evidence 标注（修正的 false negative），必须报告两种模式：evidence_only（与 DocRED 可比的\n    evi_f1，仅 43% triples）+ full（全部 triples 的 rel_f1，无 evi_f1）。转换脚本已支持 --mode full。'\n  priority: P0\n  gpu_budget_hours: 16\n  deps: []\n  registry_id: null\n- id: plan_016\n  claim: 2\n  description: 'LLaMA-3.1-8B cross-family validation (D077 新增): 在非 Qwen 家族模型上复现核心\n    pipeline (SFT → RSFT → GRPO QLoRA)，验证 decoupling spectrum 跨模型家族成立。关键实验：LLaMA GRPO\n    QLoRA 是否也出现 catastrophic forgetting。'\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  registry_id: plan_016_llama_rsft_candidates\n- id: plan_008\n  claim: 2\n  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格\n    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: reeval_rsft_topk3\n- id: plan_011\n  claim: 3\n  description: 'GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward\n    + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要\n    gradient_accumulation 适配显存。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_011_bf16_g8_step_eval\n- id: plan_012\n  claim: 3\n  description: 'DPO+CED experiment: 用 RSFT 候选数据构造 preference pairs (CED-preferred\n    vs CED-rejected)，DPO 训练。验证 DPO 是否避免 GRPO 的 catastrophic forgetting。Dream v2 三档要求\n    DPO 作为 RL spectrum 关键数据点，必须补全训练超参（β, lr, epochs, pair construction）。D045 升 P0。'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: plan_012_dpo_ced\n- id: plan_013\n  claim: 4\n  description: 'EDCR 人工标注验证: 100 个样本，人工判断每个 cited evidence sentence 是否真正支持对应 relation。计算",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 180
    }
  },
  "sourceToolAssistantUUID": "f269bac8-b01c-4f01-9b75-63c9c108a1ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15 · 2026-05-16T16:01:38.243Z_

````json
{
  "parentUuid": "3c408873-a8e5-4320-9f2e-ed3a9444300b",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**faith-evidence-ie**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"faith-evidence-ie\")` 或 `load_project_config(\"faith-evidence-ie\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/faith-evidence-ie/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "4b5a08a2-0fb2-4cc8-bcdf-e13db7c5b54a",
  "timestamp": "2026-05-16T16:01:38.243Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：剩余实验全面确认 dev 发现，test 数字坚挺，DREEAM-protocol 对齐有竞争力，EDCR 人工验证通过——5-claim 框架完全成立，EMNLP Main 可直接投稿 核心假设：['Test set Ign-F1 退化 ≤1.5pp（dev 45.85 → test ≥44.3），no-e…",
  "leafUuid": "4b5a08a2-0fb2-4cc8-bcdf-e13db7c5b54a",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Evidence-grounded DocRE scaling and decoupling analysis",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0"
}
```

---

### Tool call

_source line 18 · 2026-05-16T16:01:42.432Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WQp86kk4VzNXHb7hPZuDLf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
  "offset": 100,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b5a08a2-0fb2-4cc8-bcdf-e13db7c5b54a",
  "isSidechain": false,
  "requestId": "req_011Cb6XaxQRhoTUgr1mNR6en",
  "type": "assistant",
  "uuid": "25fe319a-a53b-44f4-8ca2-51e7bedbd6e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ZxQbku4bPeaHcCCLEM8sM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7120,
      "cache_read_input_tokens": 51409,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7120,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 51409,
          "cache_creation_input_tokens": 7120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7120
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

_source line 19 · 2026-05-16T16:01:42.437Z_

<details><summary>↩ Tool result · `toolu_01WQp86kk4VzNXHb7hPZuDLf`</summary>

```text
100	  description: 'EDCR 人工标注验证: 100 个样本，人工判断每个 cited evidence sentence 是否真正支持对应 relation。计算
101	    EDCR 与人工判断的相关性，验证 EDCR 作为自动指标的有效性。Dream [M][W] 一致要求。'
102	  priority: P1
103	  gpu_budget_hours: 0
104	  deps: []
105	  registry_id: null
106	- id: plan_009
107	  claim: 3
108	  description: 'GRPO forgetting dynamics figure: 整理全部 GRPO checkpoint（42个）的 rel_f1/evi_f1/EDCR/reward
109	    轨迹，绘制 training dynamics 可视化图。包含 G=4 vs G=8 对比、三种 reward 对比。Dream v2 三档一致要求此图作为论文核心
110	    figure。数据已有，只需汇总+画图。'
111	  priority: P0
112	  gpu_budget_hours: 2
113	  deps: []
114	  registry_id: plan_009_dynamics_figure
115	- id: plan_010
116	  claim: 1
117	  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer
118	    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。'
119	  priority: P2
120	  gpu_budget_hours: 4
121	  deps: []
122	  registry_id: null
123	- id: plan_014
124	  claim: 1
125	  description: 'SFT-without-evidence ablation: 训练 Qwen3-4B SFT 只输出 relation triples（不含
126	    evidence sentences），对比标准 SFT（含 evidence）的 rel_f1。隔离 evidence generation 对抽取性能的代价。Dream
127	    v2 三档一致要求。用于回答"43.2% vs LMRC 60.7% 的 gap 有多少来自 evidence 生成负担"。'
128	  priority: P0
129	  gpu_budget_hours: 8
130	  deps: []
131	  registry_id: plan_014_sft_no_evidence
132	- id: plan_015
133	  claim: 2
134	  description: 'bf16 LoRA GRPO clean control: 与原始 GRPO (QLoRA 4-bit, G=4, kl=0, CED
135	    reward) 只改一个变量——quantization 从 QLoRA 4-bit 改为 bf16 LoRA。G=4, kl_coef=0 不变。目的:
136	    隔离 QLoRA confound，判断 decoupling 是 QLoRA artifact 还是 genuine RL-for-IE 现象。Dream
137	    v2 三档一致的 critical 要求。如 decoupling 在 bf16 下仍持续 → 可泛化 claim；如消失 → QLoRA 特定，需 re-scope。优先级取决于
138	    plan_011 eval 结果。'
139	  priority: P0
140	  gpu_budget_hours: 8
141	  deps:
142	  - plan_011
143	  registry_id: plan_015_grpo_g4_bf16_v3
144	- id: plan_mvp1
145	  claim: 1
146	  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing
147	    distractor 的能力验证'
148	  priority: P0
149	  gpu_budget_hours: 1
150	  deps: []
151	  registry_id: mvp1_ced_signal
152	- id: plan_mvp2_sft
153	  claim: 1
154	  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'
155	  priority: P0
156	  gpu_budget_hours: 4
157	  deps: []
158	  registry_id: mvp2_sft_warmup
159	- id: plan_mvp2_rsft
160	  claim: 1
161	  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部
162	    PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087,
163	    r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128'
164	  priority: P0
165	  gpu_budget_hours: 20
166	  deps:
167	  - plan_mvp1
168	  - plan_mvp2_sft
169	  registry_id: mvp2_rsft_train_r1
170	- id: plan_mvp2_grpo
171	  claim: 3
172	  description: 'GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1
173	    max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic
174	    forgetting。D031/D033 完整轨迹支撑 Claim 3'
175	  priority: P0
176	  gpu_budget_hours: 60
177	  deps:
178	  - plan_mvp2_sft
179	  registry_id: mvp2_grpo_ced_lr5e6_r1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25fe319a-a53b-44f4-8ca2-51e7bedbd6e4",
  "isSidechain": false,
  "promptId": "e6158723-310f-41d5-bf89-7a89d5ed4fef",
  "type": "user",
  "uuid": "e09448e4-3f59-4dd6-98c3-a33e9ef250be",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
      "content": "  description: 'EDCR 人工标注验证: 100 个样本，人工判断每个 cited evidence sentence 是否真正支持对应 relation。计算\n    EDCR 与人工判断的相关性，验证 EDCR 作为自动指标的有效性。Dream [M][W] 一致要求。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n- id: plan_009\n  claim: 3\n  description: 'GRPO forgetting dynamics figure: 整理全部 GRPO checkpoint（42个）的 rel_f1/evi_f1/EDCR/reward\n    轨迹，绘制 training dynamics 可视化图。包含 G=4 vs G=8 对比、三种 reward 对比。Dream v2 三档一致要求此图作为论文核心\n    figure。数据已有，只需汇总+画图。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: plan_009_dynamics_figure\n- id: plan_010\n  claim: 1\n  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer\n    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n- id: plan_014\n  claim: 1\n  description: 'SFT-without-evidence ablation: 训练 Qwen3-4B SFT 只输出 relation triples（不含\n    evidence sentences），对比标准 SFT（含 evidence）的 rel_f1。隔离 evidence generation 对抽取性能的代价。Dream\n    v2 三档一致要求。用于回答\"43.2% vs LMRC 60.7% 的 gap 有多少来自 evidence 生成负担\"。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_014_sft_no_evidence\n- id: plan_015\n  claim: 2\n  description: 'bf16 LoRA GRPO clean control: 与原始 GRPO (QLoRA 4-bit, G=4, kl=0, CED\n    reward) 只改一个变量——quantization 从 QLoRA 4-bit 改为 bf16 LoRA。G=4, kl_coef=0 不变。目的:\n    隔离 QLoRA confound，判断 decoupling 是 QLoRA artifact 还是 genuine RL-for-IE 现象。Dream\n    v2 三档一致的 critical 要求。如 decoupling 在 bf16 下仍持续 → 可泛化 claim；如消失 → QLoRA 特定，需 re-scope。优先级取决于\n    plan_011 eval 结果。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_011\n  registry_id: plan_015_grpo_g4_bf16_v3\n- id: plan_mvp1\n  claim: 1\n  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing\n    distractor 的能力验证'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: mvp1_ced_signal\n- id: plan_mvp2_sft\n  claim: 1\n  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mvp2_sft_warmup\n- id: plan_mvp2_rsft\n  claim: 1\n  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部\n    PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087,\n    r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_mvp1\n  - plan_mvp2_sft\n  registry_id: mvp2_rsft_train_r1\n- id: plan_mvp2_grpo\n  claim: 3\n  description: 'GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1\n    max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic\n    forgetting。D031/D033 完整轨迹支撑 Claim 3'\n  priority: P0\n  gpu_budget_hours: 60\n  deps:\n  - plan_mvp2_sft\n  registry_id: mvp2_grpo_ced_lr5e6_r1",
      "numLines": 80,
      "startLine": 100,
      "totalLines": 180
    }
  },
  "sourceToolAssistantUUID": "25fe319a-a53b-44f4-8ca2-51e7bedbd6e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-16T16:02:36.547Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me identify the planned experiments:

1. **plan_002** - Test set evaluation (status: planned, registry_id: null)
2. **plan_007** - Re-DocRED cross-dataset RSFT (status: planned, registry_id: null)
3. **plan_013** - EDCR human validation (status: planned, registry_id: null)
4. **plan_010** - NLI model ablation (status: planned, registry_id: null)

Additionally, there are running experiments that are part of the best tier hypothesis:


- plan_006_qwen3_8b_rsft_candidates (RUNNING) - 8B RSFT
- plan_006_qwen3_1_7b_rsft_candidates (RUNNING) - 1.7B RSFT
- plan_016_llama_rsft_candidates_r3 (RUNNING) - LLaMA RSFT
- plan_014_no_evidence_eval_d076 (RUNNING) - no-evidence re-eval

And there are implied experiments needed: DREEAM-protocol Evi-F1 alignment (P0 priority) and post-hoc evidence retrieval baseline (P1).

Now I'm working through the best-case scenario predictions for the test set. Looking at the dev performance—the RSFT model hit Ign-F1=45.85 while the no-evidence baseline reached 47.21—I'm estimating how these might degrade on the test set given that DocRED's test split is typically slightly harder. For the best tier, I'm predicting the RSFT model lands around 45.2 Ign-F1 (assuming minimal degradation within 1.5 percentage points) and the no-evidence baseline around 46.5, then I need to factor in the evidence tax.

I'm realizing the evidence tax range of -4.0 to -1.5pp means the no-evidence model should outperform RSFT by that margin in the best case. Since I want the best tier to show mild degradation, I should push the no-evidence prediction closer to -1.5pp advantage, so I'm adjusting to RSFT at 45.2 and no-evidence at 46.8, which gives a -1.6pp tax—right at the boundary of what the best tier allows.

Wait, I need to recalculate this properly. The evidence tax is defined as (with-evidence) minus (no-evidence), so looking at the actual dev data: the SFT baseline with evidence shows 39.74 Ign-F1, while the no-evidence version shows 47.21, which means the evidence tax is actually -7.47pp—a much larger penalty than the range suggests.

But the paper reports -7.9pp for dev, and the test metric range for evidence tax is only [-4.0, -1.5], which is way smaller. That discrepancy makes me think they might be comparing RSFT best against no-evidence instead of SFT against no-evidence. If the RSFT best test performance is around 45.2 and no-evidence is 46.8, then the evidence tax would be -1.6pp, which actually fits within that [-4.0, -1.5] range. I'm noticing some discrepancies between the eval runs and the table values for the no-evidence baseline. The raw metrics show ign_f1 around 0.4721, which converts to 47.21%, but the summary table lists 47.36% for SFT no-evidence. These might be from different evaluation runs, but either way, the dev no-evidence performance sits around 47.2%.

Now looking at the test set results: RSFT achieves 45.2% Ign-F1 while no-evidence gets 46.8%, giving an evidence penalty of about 1.6 percentage points. For Evidence-F1, the dev RSFT model shows 0.8156, so I'd expect the test performance to be similar around 0.81. I'm also checking plan_007 which evaluates RSFT on Re-DocRED, showing ign_f1 of 0.3659 and evi_f1 of 0.817.

Given that RSFT improved DocRED by 3.3-5.5 percentage points, I'd expect similar gains on Re-DocRED despite some distribution shift, predicting around 0.40 ign_f1 and 0.83 evi_f1. For plan_013 on EDCR human validation, the best tier requires Spearman ρ ≥ 0.70, and since EDCR shows a method-level correlation of -0.965 with rel_f1, the per-sample human annotation correlation should be lower but still reasonably strong.

For the NLI model ablation, DeBERTa-v3-large outperforms the base variant with discrimination accuracy of 0.815, providing clear justification for the larger model choice. On DREEAM protocol alignment, there's a notable gap between DREEAM's reproduced evi_f1 of 0.5401 and FREIGE's 0.81+, but these use different evaluation protocols—when mapping FREIGE's generative evidence to DREEAM's sentence-level format, the conversion introduces noise that likely brings performance down to the 0.5-0.65 range.

The post-hoc retrieval baseline using SFT with BM25 retrieval achieves around 0.64 evi_f1, which is substantially lower than RSFT's end-to-end generation at 0.81, confirming that joint generation and evidence selection outperforms the pipeline approach. For the smaller model variants, the 1.7B SFT baseline sits at 0.4786 igi_f1, and RSFT should show gains here, potentially larger ones due to the U-shaped scaling pattern.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e09448e4-3f59-4dd6-98c3-a33e9ef250be",
  "isSidechain": false,
  "requestId": "req_011Cb6XbGfHFSe331699DsT9",
  "type": "assistant",
  "uuid": "600e7e89-90b3-41fd-96d5-d5ad6910e839",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JzSHUUJosayTf287wNurF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1791,
      "cache_read_input_tokens": 58529,
      "output_tokens": 10719,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1791,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10719,
          "cache_read_input_tokens": 58529,
          "cache_creation_input_tokens": 1791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1791
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

_source line 21 · 2026-05-16T16:05:05.481Z_

```yaml
tier: best
narrative_guidance: "原始 framing 完全成立。Test set 确认 RSFT+CED 有效（+3-5pp over SFT），evidence tax 仅 -1.6pp（RSFT vs no-evidence），DREEAM-protocol 对齐有竞争力（0.55 vs DREEAM 0.54），EDCR 人工验证通过（ρ=0.78），post-hoc retrieval 大幅落后端到端生成（Δ≥11pp），8B/1.7B RSFT 呈 scale-dependent pattern 强化 C5。5-claim 框架完全成立，EMNLP Main 直接投稿。"
imagined_experiments:
  - name: "Test set evaluation (RSFT best + no-evidence + SFT baseline)"
    plan_id: "plan_002"
    description: "用 RSFT CED s43（dev best）、SFT no-evidence、SFT baseline 三个配置在 DocRED test set 评估。本地计算 Evi-F1/EDCR，CodaLab 提交获得官方 Ign-F1/F1。"
    expected_results:
      rsft_ced_s43_test_ign_f1: 45.2
      rsft_ced_s43_test_f1: 46.1
      rsft_ced_s43_test_evi_f1: 0.812
      rsft_ced_s43_test_edcr: 0.642
      sft_no_evidence_test_ign_f1: 46.8
      sft_no_evidence_test_f1: 48.3
      sft_baseline_test_ign_f1: 39.8
      sft_baseline_test_f1: 40.5
      sft_baseline_test_evi_f1: 0.795
      evidence_tax_rsft_vs_noevi: -1.6
      rsft_vs_sft_gain: 5.4
      dev_test_degradation_rsft: 0.65
      dev_test_degradation_noevi: 0.56
    result_rationale: "DocRED test set 与 dev set 同分布（均来自 Wikipedia 远程监督），历史上 dev→test 退化约 0.5-1.5pp（ATLOP 报告 ~0.8pp）。Best 档下 RSFT 退化 0.65pp（dev 45.85→test 45.2）属于正常范围——RSFT 通过 CED 筛选高质量样本训练，泛化能力强于过拟合风险低。No-evidence 退化更小（0.56pp）因为其任务更简单（无 evidence 生成负担，模型全部容量用于 RE）。SFT baseline 退化与 dev 一致因为 3-epoch 训练未过拟合。Evidence tax（RSFT vs no-evidence）从 dev 的 -1.6pp 保持到 test 的 -1.6pp，说明 RSFT 几乎完全恢复 evidence 代价。"
    tables:
      - name: "Table 2: Test Set Results"
        columns: ["Method", "Ign-F1", "F1", "Evi-F1", "EDCR"]
        rows:
          - ["SFT baseline", "39.8", "40.5", "79.5", "0.714"]
          - ["SFT no-evidence", "46.8", "48.3", "—", "—"]
          - ["RSFT CED (best)", "45.2", "46.1", "81.2", "0.642"]
          - ["DREEAM (encoder)", "61.7†", "—", "54.0†", "—"]
    figures_description:
      - "Bar chart comparing Ign-F1 across methods on test set, with evidence tax annotation showing -1.6pp gap between RSFT and no-evidence"
    analysis: "Test 数字坚挺——RSFT 45.2 远超 SFT 39.8（+5.4pp），且与 no-evidence 46.8 仅差 1.6pp。这证明 RSFT+CED 几乎消除了 evidence generation 的抽取代价（4B 模型 dev 上完整 evidence tax 为 -7.9pp，RSFT 恢复了 80%）。Dev→test gap 极小（<1pp），结果可信。"

  - name: "DREEAM-protocol Evidence F1 对齐评估"
    plan_id: "plan_004 (extension)"
    description: "将 FREIGE 生成的 free-text evidence 映射到句子 ID，按 DREEAM 评估协议（sentence-level P/R/F1）计算 Evi-F1。与 DREEAM 复现结果（54.01）直接对比。"
    expected_results:
      freige_rsft_dreeam_protocol_evi_f1: 0.55
      freige_rsft_dreeam_protocol_evi_p: 0.62
      freige_rsft_dreeam_protocol_evi_r: 0.49
      freige_sft_dreeam_protocol_evi_f1: 0.51
      dreeam_baseline_evi_f1: 0.5401
      delta_rsft_vs_dreeam: 0.01
    result_rationale: "FREIGE 的 conditional evi_f1=0.81 是 token-level 精确匹配（生成文本 vs gold 文本），而 DREEAM protocol 是 sentence-level 二分类（哪些句子被引用）。映射引入两个损失：(1) 生成的 evidence 文本不完全匹配原句导致 fuzzy matching 丢失 ~5%；(2) FREIGE 倾向引用句子片段而非完整句子，sentence-level recall 受限。但 FREIGE precision 高（0.62）因为 CED 已筛选高质量 evidence。最终 0.55 略高于 DREEAM 的 0.54，说明 generative evidence 映射到句子级后仍有竞争力——这是 remarkable 的，因为 DREEAM 是专门为 sentence retrieval 设计的 encoder 模型，而 FREIGE 是 generative model 的副产品。"
    tables:
      - name: "Table: Evidence Quality Comparison (DREEAM Protocol)"
        columns: ["Method", "Type", "Evi-P", "Evi-R", "Evi-F1"]
        rows:
          - ["DREEAM (RoBERTa-large)", "Discriminative retrieval", "60.5", "48.8", "54.0"]
          - ["SAIS (RoBERTa-large)", "Discriminative retrieval", "—", "—", "~52*"]
          - ["FREIGE SFT", "Generative production", "58.2", "45.5", "51.0"]
          - ["FREIGE RSFT CED", "Generative production", "62.0", "49.0", "55.0"]
    figures_description: []
    analysis: "Generative evidence production（FREIGE RSFT）在 DREEAM protocol 下达到 0.55，与 encoder-based retrieval SOTA（DREEAM 0.54）持平。这是 best 档的关键支撑——证明 LLM 的 generative evidence 不仅在 token-match 上质量高（0.81），映射到结构化评估后也不输给专门的 evidence retrieval 模型。Precision 高于 DREEAM（0.62 vs 0.605）说明 CED 筛选的 evidence 确实精准；recall 略高（0.49 vs 0.488）得益于 LLM 的语言理解能力捕捉了 encoder 遗漏的隐含 evidence。"

  - name: "EDCR 人工标注验证"
    plan_id: "plan_013"
    description: "100 个样本人工标注。每个样本包含模型生成的 relation triple + cited evidence sentences。标注员判断每个 evidence sentence 是否真正支持该 relation（binary: supports / does not support）。计算 EDCR 与人工 evidence faithfulness 评分的 Spearman 相关。"
    expected_results:
      n_samples: 100
      human_spearman_rho: 0.78
      human_spearman_p: 0.00001
      human_agreement_kappa: 0.82
      edcr_precision_at_top10: 0.90
      edcr_recall_at_bottom10: 0.80
      mean_human_faithfulness_score: 0.73
      false_positive_rate: 0.08
      false_negative_rate: 0.14
    result_rationale: "EDCR 本质是 NLI-based 的 evidence-relation 一致性度量，与人工判断 'evidence 是否支持 relation' 高度对齐——两者测量的是同一个概念（evidence faithfulness）。ρ=0.78 而非 1.0 的原因：(1) NLI 模型对某些隐含推理（如 temporal reasoning、multi-hop inference）的判断与人类不完全一致（~15% 分歧）；(2) EDCR 是 document-level 聚合（平均所有 triples），而人工是 per-triple 判断，聚合引入平滑。Precision@top10 高达 0.90 说明 EDCR 最高分样本几乎全部是真正 faithful 的，验证了 EDCR 作为诊断工具的实用价值。"
    tables:
      - name: "Table: EDCR Human Validation"
        columns: ["Metric", "Value"]
        rows:
          - ["Spearman ρ (EDCR vs Human)", "0.78"]
          - ["p-value", "<0.0001"]
          - ["Cohen's κ (inter-annotator)", "0.82"]
          - ["EDCR Precision@top-10%", "0.90"]
          - ["EDCR Recall@bottom-10%", "0.80"]
    figures_description:
      - "Scatter plot: EDCR score (x-axis) vs human faithfulness rating (y-axis) for 100 samples, with regression line and ρ annotation. Color-coded by method (SFT/RSFT/GRPO)"
    analysis: "ρ=0.78 充分验证 EDCR 作为自动指标的有效性——远超经验性阈值 0.7（'good' correlation for automated metrics vs human judgment，参考 BERTScore 的验证标准）。EDCR 在极端值（pathological GRPO 模型 EDCR≈1.0）上与人工判断完全一致，在中间值（RSFT 模型 EDCR≈0.64）也保持合理对应。False positive rate 仅 8%（EDCR 认为 unfaithful 但人工认为 OK）说明 EDCR 是保守的诊断工具。"

  - name: "Post-hoc evidence retrieval baseline (SFT + BM25)"
    plan_id: "(P1 priority, implied)"
    description: "SFT no-evidence 模型输出 relation triples，然后用 BM25 从文档句子中检索最相关的 evidence sentences。对比 RSFT 端到端生成的 evidence 质量。"
    expected_results:
      posthoc_bm25_rel_f1: 0.487
      posthoc_bm25_evi_f1: 0.64
      posthoc_bm25_edcr: 0.74
      posthoc_bm25_evi_precision: 0.71
      posthoc_bm25_evi_recall: 0.58
      rsft_evi_f1: 0.815
      gap_evi_f1: 0.175
      gap_percentage: "21.5pp"
    result_rationale: "BM25 是 lexical matching——检索包含 entity mention 的句子作为 evidence。这在 DocRE 中有天然上限：(1) 许多 evidence sentences 的支撑关系依赖上下文推理而非直接 entity co-occurrence（~30% 的 gold evidence 不包含两个 entity 的共现）；(2) BM25 无法区分 entity-sharing distractor 和真正的 supporting evidence（正是 CED 解决的问题）。rel_f1=0.487 等于 no-evidence 模型的抽取能力（不受 evidence 生成影响），但 evi_f1 仅 0.64——远低于 RSFT 的 0.81（差距 17.5pp）。这证明端到端生成 evidence 显著优于 post-hoc retrieval 拼接，验证了 evidence-grounded 训练的必要性。EDCR=0.74（高于 RSFT 的 0.64）进一步说明 BM25 检索的 evidence 与 relation 的一致性更差。"
    tables:
      - name: "Table: End-to-End Generation vs Post-hoc Retrieval"
        columns: ["Method", "Rel-F1", "Evi-F1", "EDCR", "Evidence Source"]
        rows:
          - ["RSFT CED (best)", "0.468", "0.815", "0.639", "End-to-end generation"]
          - ["CED reranker", "0.486", "0.819", "0.616", "Generation + reranking"]
          - ["SFT + BM25", "0.487", "0.640", "0.740", "Post-hoc retrieval"]
          - ["SFT baseline", "0.405", "0.799", "0.712", "End-to-end generation"]
    figures_description:
      - "Grouped bar chart: Evi-F1 comparison between RSFT (0.81), SFT (0.80), and Post-hoc BM25 (0.64), with 17.5pp gap annotation"
    analysis: "Post-hoc BM25 的 evi_f1=0.64 与 RSFT 0.81 的差距达 17.5pp（>10pp 阈值），决定性地证明端到端 evidence generation 优于检索拼接。关键insight：模型在训练中学会了 evidence 与 relation 的内在关联，而 BM25 仅靠词汇重叠无法捕捉这种深层语义对应。这也解释了为什么 CED scoring 有效——它评估的正是这种语义一致性。"

  - name: "NLI model ablation (DeBERTa-v3-base vs large)"
    plan_id: "plan_010"
    description: "用 DeBERTa-v3-base 替换 DeBERTa-v3-large 作为 CED scorer，重新对 RSFT candidates 打分并训练，评估 NLI 模型能力对最终性能的影响。"
    expected_results:
      deberta_base_ced_discrimination_acc: 0.74
      deberta_large_ced_discrimination_acc: 0.815
      rsft_with_base_scorer_rel_f1: 0.443
      rsft_with_base_scorer_evi_f1: 0.805
      rsft_with_large_scorer_rel_f1: 0.457
      rsft_with_large_scorer_evi_f1: 0.815
      delta_rel_f1: -0.014
      delta_discrimination_acc: -0.075
    result_rationale: "DeBERTa-v3-base (86M params) vs large (304M params) 的 NLI 能力差距约 2-3pp MNLI accuracy（base ~88%, large ~91%）。这个差距传导到 CED discrimination：base 的 accuracy 从 0.815 降到 ~0.74（对 entity-sharing distractors 的区分能力下降）。Scoring quality 下降导致 RSFT 训练数据中混入更多 noisy samples，最终 rel_f1 下降 1.4pp。但即使用 base scorer，RSFT 仍显著优于 SFT baseline（+3.8pp），说明 NLI-based scoring 的核心机制（而非特定模型大小）是关键。这支撑 C3 的叙事：NLI-based scoring 是 RSFT 有效的必要条件，具体 NLI 模型选择是二阶效应。"
    tables:
      - name: "Table: NLI Model Ablation for CED Scoring"
        columns: ["NLI Model", "Disc. Acc.", "RSFT Rel-F1", "RSFT Evi-F1", "Δ vs SFT"]
        rows:
          - ["DeBERTa-v3-large (default)", "0.815", "0.457", "0.815", "+5.1pp"]
          - ["DeBERTa-v3-base", "0.740", "0.443", "0.805", "+3.8pp"]
          - ["Random scoring (control)", "—", "~0.42", "~0.79", "+1.4pp"]
    figures_description: []
    analysis: "Large 优于 base（+1.4pp rel_f1），但 base 仍有效（+3.8pp over SFT）。这说明 CED 的价值来自 NLI 语义对比机制本身，而非单纯依赖大模型。作为 P2 实验，这提供了有用但非关键的 ablation 信息——论文中作为附录一行即可。"

  - name: "Re-DocRED RSFT evaluation"
    plan_id: "plan_007"
    description: "在 Re-DocRED 上用 DocRED-trained RSFT CED best config 做 zero-shot transfer eval，同时训练 Re-DocRED-specific RSFT 并评估。验证 evidence extraction 跨数据集泛化。"
    expected_results:
      redocred_rsft_transfer_ign_f1: 0.395
      redocred_rsft_transfer_evi_f1: 0.825
      redocred_rsft_transfer_edcr: 0.655
      redocred_sft_baseline_ign_f1: 0.366
      redocred_rsft_gain: 0.029
      redocred_vs_docred_evi_f1_gap: 0.01
    result_rationale: "Re-DocRED 是 DocRED 的重标注版本（修正 false negatives），relation ontology 完全相同（96 types）。SFT 已在 Re-DocRED 上达到 ign_f1=0.366, evi_f1=0.817。RSFT 的 CED scoring 机制不依赖数据集特定分布（NLI 是通用语义判断），因此 RSFT 增益可迁移。Best 档下 RSFT 改善 +2.9pp（略低于 DocRED 的 +5pp，因为 Re-DocRED 的 55% 无 evidence 标注 triples 引入噪声）。Evi-F1 从 0.817 提升至 0.825，确认 evidence generation 能力跨数据集泛化。关键观察：evi_f1 在两个数据集上几乎相同（0.815 vs 0.825），说明模型学到的 evidence production 能力是 general 的。"
    tables:
      - name: "Table: Cross-Dataset Generalization (Re-DocRED)"
        columns: ["Config", "Ign-F1", "Evi-F1", "EDCR", "Δ vs SFT"]
        rows:
          - ["SFT baseline (Re-DocRED)", "36.6", "81.7", "0.667", "—"]
          - ["RSFT CED transfer", "39.5", "82.5", "0.655", "+2.9pp"]
          - ["DocRED RSFT CED (reference)", "45.9", "81.6", "0.639", "+5.5pp"]
    figures_description: []
    analysis: "RSFT 增益在 Re-DocRED 上保持（+2.9pp），虽低于 DocRED（+5.5pp）但方向一致。Evi-F1 甚至略高于 DocRED（0.825 vs 0.815），说明 evidence generation 能力 robust。增益缩小的原因是 Re-DocRED 55% triples 无 evidence annotation，RSFT 的 CED scoring 在这些样本上的信号更弱。"

  - name: "8B Qwen RSFT candidates + training + eval"
    plan_id: "plan_006 (8B RSFT completion)"
    description: "Qwen3-8B RSFT candidate generation → CED scoring → RSFT training → dev eval。验证 RSFT 增益在 8B scale 上的表现。"
    expected_results:
      qwen3_8b_sft_ign_f1: 0.5051
      qwen3_8b_rsft_ign_f1: 0.525
      qwen3_8b_rsft_evi_f1: 0.828
      qwen3_8b_rsft_edcr: 0.625
      qwen3_8b_rsft_gain: 0.020
      qwen3_8b_no_evidence_ign_f1: 0.507
      qwen3_8b_evidence_tax_after_rsft: -0.002
    result_rationale: "8B 模型容量充裕，SFT 已达 ign_f1=0.5051（evidence tax ≈0）。RSFT 增益预期为 +2.0pp——低于 4B 的 +5.5pp，因为 8B SFT 基线已经很高，改善空间小。这体现了 diminishing returns：模型越大，SFT 已足够好，RSFT 的 marginal gain 递减。但 RSFT 后 evidence tax 从 ≈0 变为 -0.2pp（几乎为零），说明 8B 完全 absorb 了 evidence 负担。Evi-F1 从 0.819 提升到 0.828，CED scoring 仍有筛选价值。这强化 C5：RSFT 增益是 scale-dependent 的——4B 获益最大（+5.5pp），8B 获益小但 evidence tax 最低。"
    tables:
      - name: "Table: Scale-Dependent RSFT Gains"
        columns: ["Model", "SFT Ign-F1", "RSFT Ign-F1", "RSFT Gain", "Evidence Tax (RSFT vs no-evi)"]
        rows:
          - ["Qwen3-1.7B", "47.9", "51.5*", "+3.6pp", "+3.0pp (benefit)"]
          - ["Qwen3-4B", "39.7", "45.2", "+5.5pp", "-1.6pp"]
          - ["Qwen3-8B", "50.5", "52.5", "+2.0pp", "-0.2pp"]
    figures_description:
      - "Line plot: RSFT gain (y-axis) vs model size (x-axis, log scale), showing decreasing gains with scale. Second y-axis shows evidence tax converging to zero."
    analysis: "RSFT gains 呈 monotonic decrease with scale（1.7B: +3.6, 4B: +5.5, 8B: +2.0）——等等，1.7B 比 8B 少？不对。让我修正：1.7B 的 RSFT gain 应该也较大因为 evidence 起正则化作用。实际上 gain pattern 是非单调的——4B 最大因为 evidence tax 最大（RSFT 恢复空间最大），1.7B 和 8B gain 较小但原因不同（1.7B evidence 本身有益所以 SFT 已不错；8B 容量充裕 SFT 已强）。"

  - name: "1.7B Qwen RSFT candidates + training + eval"
    plan_id: "plan_006 (1.7B RSFT completion)"
    description: "Qwen3-1.7B RSFT candidate generation → CED scoring → RSFT training → dev eval。验证 RSFT 增益在小模型上的 U-shape pattern。"
    expected_results:
      qwen3_1_7b_sft_ign_f1: 0.4786
      qwen3_1_7b_rsft_ign_f1: 0.515
      qwen3_1_7b_rsft_evi_f1: 0.845
      qwen3_1_7b_rsft_edcr: 0.610
      qwen3_1_7b_rsft_gain: 0.036
      qwen3_1_7b_no_evidence_ign_f1: 0.398
      qwen3_1_7b_evidence_tax_after_rsft: 0.117
    result_rationale: "1.7B 的 evidence tax 是 POSITIVE（+6.2pp benefit from evidence, D083）。SFT with evidence（47.86）已远超 no-evidence（39.82）。RSFT 在此基础上再提升 +3.6pp 至 51.5——增益来源：(1) CED 筛选最高质量样本训练，模型学会更精准的 evidence-relation 对应；(2) 小模型从 high-quality data curation 中获益更大（data efficiency 更重要）。RSFT 后 evidence benefit 进一步扩大至 +11.7pp（51.5 vs 39.8），说明 RSFT 强化了 evidence 的正则化效应。Evi-F1 从 0.832 提升到 0.845——小模型 evidence generation 质量在 RSFT 后改善最明显，因为 CED 帮助小模型避免了 evidence hallucination。"
    tables: []
    figures_description:
      - "U-shape figure: Evidence tax (y-axis) vs model size (x-axis), showing benefit at 1.7B, cost at 4B, neutral at 8B. After RSFT overlay shows tax recovery at all scales."
    analysis: "1.7B RSFT 成功确认：小模型从 evidence-grounded training 中获益更多（隐式正则化 + CED 数据质量筛选双重效应）。这完善了 C5 的 U-shape narrative——不仅 evidence tax 是 scale-dependent 的，RSFT 的恢复效果也是 scale-dependent 的。"

  - name: "LLaMA-3.1-8B RSFT training + eval"
    plan_id: "plan_016 (RSFT completion)"
    description: "LLaMA-3.1-8B RSFT candidate generation（第三次尝试，解决 OOM）→ CED scoring → RSFT training → eval。跨模型家族验证 RSFT 有效性。"
    expected_results:
      llama_8b_sft_ign_f1: 0.5384
      llama_8b_rsft_ign_f1: 0.555
      llama_8b_rsft_evi_f1: 0.825
      llama_8b_rsft_edcr: 0.618
      llama_8b_rsft_gain: 0.017
      llama_8b_no_evidence_ign_f1: 0.5452
      llama_8b_evidence_tax_after_rsft: 0.010
    result_rationale: "LLaMA-8B SFT 已达 ign_f1=0.5384（evidence tax 仅 -0.68pp）。RSFT 增益 +1.7pp 较小——与 Qwen-8B 一致（8B scale 改善空间有限）。但关键是 RSFT 后 evidence tax 从 -0.68pp 变为 +1.0pp（RSFT 甚至超过 no-evidence），说明 RSFT 在 8B 模型上完全消除了 evidence 负担。跨家族一致性验证：(1) RSFT 有效（两个 8B 模型均有正增益）；(2) evidence tax ≈ 0 pattern 跨家族成立；(3) GRPO QLoRA catastrophic decoupling 已在 LLaMA 上确认（plan_016_llama_grpo_qlora）。C2 和 C5 跨家族 robust。"
    tables:
      - name: "Table: Cross-Family Validation Summary"
        columns: ["Model", "SFT", "RSFT", "Gain", "Evi Tax", "GRPO QLoRA"]
        rows:
          - ["Qwen3-4B", "39.7", "45.2", "+5.5", "-7.9→-1.6", "catastrophic"]
          - ["Qwen3-8B", "50.5", "52.5", "+2.0", "≈0→≈0", "—"]
          - ["LLaMA-3.1-8B", "53.8", "55.5", "+1.7", "-0.7→+1.0", "catastrophic"]
    figures_description: []
    analysis: "LLaMA RSFT 成功完成闭环了跨家族验证。三个关键 pattern 在 LLaMA 上全部复现：RSFT > SFT、8B evidence tax ≈ 0、QLoRA GRPO catastrophic。这让审稿人无法质疑'结论依赖于特定模型架构'。"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "600e7e89-90b3-41fd-96d5-d5ad6910e839",
  "isSidechain": false,
  "requestId": "req_011Cb6XbGfHFSe331699DsT9",
  "type": "assistant",
  "uuid": "c9571d92-9746-40f2-92f6-06b319149acd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JzSHUUJosayTf287wNurF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1791,
      "cache_read_input_tokens": 58529,
      "output_tokens": 10719,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1791,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10719,
          "cache_read_input_tokens": 58529,
          "cache_creation_input_tokens": 1791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1791
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

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：剩余实验全面确认 dev 发现，test 数字坚挺，DREEAM-protocol 对齐有竞争力，EDCR 人工验证通过——5-claim 框架完全成立，EMNLP Main 可直接投稿 核心假设：['Test set Ign-F1 退化 ≤1.5pp（dev 45.85 → test ≥44.3），no-e…",
  "leafUuid": "c9571d92-9746-40f2-92f6-06b319149acd",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Evidence-grounded DocRE scaling and decoupling analysis",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：剩余实验全面确认 dev 发现，test 数字坚挺，DREEAM-protocol 对齐有竞争力，EDCR 人工验证通过——5-claim 框架完全成立，EMNLP Main 可直接投稿 核心假设：['Test set Ign-F1 退化 ≤1.5pp（dev 45.85 → test ≥44.3），no-e…",
  "leafUuid": "c9571d92-9746-40f2-92f6-06b319149acd",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Evidence-grounded DocRE scaling and decoupling analysis",
  "sessionId": "540b5134-714e-48b9-825b-9e0b1b9937b0"
}
```

---
