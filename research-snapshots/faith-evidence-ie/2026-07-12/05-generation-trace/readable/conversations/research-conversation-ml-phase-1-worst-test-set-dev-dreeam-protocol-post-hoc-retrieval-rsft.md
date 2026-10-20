# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Test set 大幅退化暴露 dev 过拟合，DREEAM-protocol 对齐不利，post-hoc retrieval 追平 RSFT——方法

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/48d76cf1-72e3-441d-8555-787b4ba2f406.jsonl`
- **Structured JSON:** [`a9c08250caf60b7b4916.json`](../../sessions/a9/a9c08250caf60b7b4916.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T16:08:44.012Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T16:08:44.012Z",
  "sessionId": "48d76cf1-72e3-441d-8555-787b4ba2f406",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Test set 大幅退化暴露 dev 过拟合，DREEAM-protocol 对齐不利，post-hoc retrieval 追平 RSFT——方法贡献不成立，需 reframe 为 empirical analysis paper\n核心假设：['Test set Ign-F1 退化 > 4pp（RSFT CED test < 41.5），且 evidence tax 扩大至 > 5pp', 'DREEAM-protocol Evi-F1 < 0.35，conditional evi_f1=0.81 在严格协议下大幅缩水', 'EDCR 与人工标注 Spearman ρ < 0.40，指标有效性无法充分验证', 'Post-hoc retrieval evi_f1 达到 0.75-0.85，与 RSFT 相当甚至超越，端到端生成无优势', '部分 scaling 实验失败（1.7B/8B RSFT candidates OOM 或结果不一致），U-shape 仅有 SFT 数据支撑']\n关键指标范围：{'test_ign_f1_rsft_best': [38.0, 41.5], 'test_ign_f1_no_evidence': [42.0, 45.0], 'test_evidence_tax_4b': [-7.0, -4.0], 'dreeam_protocol_evi_f1': [0.2, 0.35], 'edcr_human_spearman_rho': [0.15, 0.4], 'posthoc_retrieval_evi_f1': [0.75, 0.85], 'expected_reviewer_avg': [2.5, 3.0]}\n叙事方向：完全 reframe 为 empirical analysis paper。 标题改为分析导向：\"The Cost of Faithfulness: What Happens When LLMs Must Justify Their Extractions\"。 主贡献重排序：(1) evidence-grounded DocRE 任务定义 + evaluation framework（EDCR 是首个尝试， 即使 human correlation 不够强也有开创价值）； (2) decoupling spectrum 作为 RL-for-IE 的警示性发现（negative result 的价值—— optimization pressure 系统性损害 multi-objective 平衡）； (3) U-shape evidence tax 作为 scaling 实证分析（仅 SFT-level 也够写）。 RSFT 不再定位为推荐方案，而是 \"least harmful training strategy we found\"。 去掉所有 effective/competitive 措辞，改用 reveals/exposes/characterizes。 Post-hoc retrieval 追平 RSFT 变成 paper 的一部分：\"simple retrieval matches  end-to-end generation, further questioning the cost-benefit of evidence production\"。 仍投 EMNLP Main（analysis paper 在 EMNLP 有传统，Findings 也可接受）， 同时准备 AAAI 2027 作为同等 fallback。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: faith-evidence-ie\n\n## paper_framing.md\n\n# Paper Framing — FREIGE\n\n> **状态**: POST-MVP + D078-D083 scaling analysis & cross-validation complete\n> **最后更新**: 2026-05-16\n> **Dream v1**: best=2.5, median=3.0, worst=2.5 → reframe 完成\n> **Dream v2**: best=3.0, median=2.5, worst=2.5 → best 提升但 median 下降，未达标。关键路径：plan_011 bf16 GRPO eval + structural fixes → re-dream v3\n\n## Target Venue\n\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\n\n## Core Insight\n\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。\n\n我们系统性地探索了 online RL (GRPO) 、offline preference optimization (DPO) 和 offline RL (RSFT) 三条技术路线。关键发现：**RL optimization pressure 与 evidence-extraction decoupling severity 正相关**——优化强度越大，evidence 质量提升的同时抽取能力退化越严重。QLoRA 放大至 catastrophic（rel_f1<0.02），bf16 GRPO 从 0.4549 退化至 ~0.434（mild, -2pp），DPO 呈 gradual 退化（1ep→3ep rel_f1 从 0.4034→0.3429），RSFT 无 decoupling。\n\n**Evidence tax 是 scale-dependent 的（U-shape pattern, D079/D082/D083）**：1.7B 模型中 evidence generation 反而带来 +6.2pp 收益（隐式正则化），4B 模型付出 -7.9pp 代价，8B Qwen 模型容量足够 absorb（≈0），8B LLaMA 跨家族确认（-0.7pp）。这推翻了\"evidence 总有代价\"的简单叙事。\n\nCED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，通过文档内 hard negative 对比评估 evidence 质量。CED 和 flat-NLI 作为 RSFT scoring functions 统计不可区分（D078 paired t-test p=0.44），但均显著优于 random/no scoring。CED 因可解释性优势作为默认推荐方案。\n\n## Story Arc\n\n1. **Problem**: LLM DocRE 无证据 → 部署障碍\n2. **New task**: evidence-grounded DocRE — 同时生成关系和证据\n3. **Cost of faithfulness**: evidence generation 代价是 **scale-dependent** 的——4B 模型付出 -7.9pp 代价，但 1.7B 反而获益 +6.2pp，8B 趋近于零。这不是固定成本，而是与模型容量的非线性交互（D079/D082/D083）\n4. **Exploration**: 系统性比较 online RL (GRPO) vs offline preference (DPO) vs offline RL (RSFT)\n5. **Key finding**: evidence-extraction decoupling — RL optimization pressure 与 decoupling severity 正相关，形成连续谱系（GRPO-QLoRA catastrophic > GRPO-bf16 mild > DPO gradual > RSFT none）\n6. **QLoRA amplification**: QLoRA 量化将 mild decoupling 放大至 catastrophic forgetting——decoupling 是 RL-for-IE 中 multi-objective competition 的通用梯度（intra-task trade-off，非 inter-task forgetting），QLoRA 是 catastrophic amplifier\n7. **What works**: RSFT with NLI-based scoring 是唯一有效路线——提升 evidence 质量而不牺牲抽取\n8. **Best practical solution**: CED reranker 恢复 97% 的 evidence 代价，同时保留高质量 evidence（evi_f1=0.8188）\n9. **Diagnostic tool**: EDCR 双层诊断——方法级量化 decoupling（与 Claim 2 呼应），per-relation 级揭示 evi_f1 不捕捉的 relation-type 难度差异（D070 ✅）\n10. **Scaling & generalization**: evidence tax 呈 U-shape scaling pattern（D079/D082/D083），跨模型家族（LLaMA-8B, D082）和跨数据集（Re-DocRED, D080）验证泛化性\n\n## Core Claims (reframed after Dream v1, updated D068-D083)\n\n### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力\n- FREIGE 是首个**基于生成式 LLM** 的 evidence-grounded DocRE 方法（⚠️ 必须始终保持 \"generative LLM\" 限定词——SAIS 已做 encoder-based evidence retrieval + DocRE）\n- **关键区分 (Reviewer warning)**：encoder-based evidence *retrieval*（SAIS, DREEAM — 分类哪些句子是证据，evidence supervision 提升 RE）vs generative evidence *production*（FREIGE — LLM 生成证据文本，额外生成负担导致 scale-dependent 代价）。论文 Related Work 必须精准讨论此对比，否则审稿人会问 \"为什么 SAIS 说 evidence 有用，你说 evidence 有害\"\n- **Evidence generation tax**: scale-dependent，详见 Claim 5（D079/D082/D083）\n- RSFT 在 4/4 配置下均超过 SFT baseline（Ign-F1 +3.3~5.5pp）\n- **CED reranker 是最优实用方案**: rel_f1=0.4864（仅低于 no-evidence 0.29pp），evi_f1=0.8188（plan_005 ✅）\n- **D076 统一协议最终数字（可写入论文）**:\n  - SFT baseline: rel_f1=0.4049\n  - CED RSFT mean: rel_f1=0.4569 (s42=0.4517, s44=0.4621)\n  - flat-NLI RSFT mean: rel_f1=0.4561 (s42=0.4535, s43_r2=0.4586)\n  - CED vs flat-NLI Δ=0.0008，统计不可区分（D078 p=0.44）\n- **Cross-family validation (D082)**: LLaMA-3.1-8B SFT rel_f1=0.5514, evi_f1=0.8151; no-evidence rel_f1=0.5624（evidence tax = -0.7pp，8B 容量足够 absorb）\n- **Cross-dataset validation (D080)**: Re-DocRED Ign-F1 下降 3.15pp 但 Evi-F1 保持 0.817——evidence extraction 能力跨数据集泛化\n- 需要 DREEAM-protocol 对齐的 Evi-F1 对比（D041 在处理中）\n- **RSFT 方法论定位**：诚实承认 RSFT 是 STaR (NeurIPS 2022) 的单轮变体 + evidence quality scoring。创新点在于将 STaR-like self-improvement 应用于 evidence-grounded DocRE + CED/NLI 作为 domain-specific quality filter，而非框架本身\n- **Evaluation caveat** (Limitations): GenRES 指出 exact match F1 低估 generative RE，FREIGE 所有 eval 用 exact match，应承认此局限（对所有方法同等适用，相对比较有效）\n\n### Claim 2 (Core finding): RL optimization pressure 与 evidence-extraction decoupling severity 正相关（D068/D069 修正）\n- **Decoupling spectrum**: 优化强度越大，decoupling 越严重\n  - GRPO QLoRA: catastrophic（rel_f1=0.0138, evi_f1=0.850, EDCR=0.99）— QLoRA 放大 decoupling\n  - GRPO bf16: mild（rel_f1 从 0.4549→~0.434, -2pp; step_30=0.434, step_50=0.4276, step_70=0.4341）— 退化可控但持续（D065/D066）\n  - DPO bf16 1ep→3ep: gradual（Ign-F1 38.88→TBD, rel_f1 0.4034→0.3429）— 随训练渐进退化（D067/D068）\n  - RSFT: none — 无 decoupling，唯一有效路线\n- **QLoRA 是 catastrophic amplifier，不是 root cause**: bf16 GRPO 仅 mild decoupling（-2pp），QLoRA 放大至 catastrophic（-39pp）（D054/D065/D066）\n- **Decoupling 是 RL-for-IE 的通用梯度**: 跨方法（GRPO/DPO）、跨量化策略（QLoRA/bf16）一致出现，严重程度与优化压力正相关\n- 三档 Dream 审稿均认为此发现\\\"genuinely novel and striking\\\"\n- **已完成**: GRPO G=8 bf16 确认 mild decoupling（plan_011 ✅）; DPO 1ep/3ep 确认 gradual decoupling（plan_012 ✅）\n\n### Claim 3 (Ablation): NLI-based scoring 提升 RSFT 质量——CED 与 flat-NLI 统计不可区分（D078）\n- CED 和 flat-NLI 都显著优于 random/no scoring\n- **D078 paired t-test 最终结论**: CED vs flat-NLI p=0.44，统计不可区分\n  - CED RSFT mean rel_f1=0.4569 vs flat-NLI mean rel_f1=0.4561（Δ=0.0008）\n  - 两种 scoring function 等效，CED 因可解释性（contrastive evidence discrimination）作为默认推荐\n- ~~**Critical**: 如果 CED 不显著优于 flat-NLI → CED 降级为\"one possible scoring function\"~~ → **已确认降级（D078）**\n- **论文叙事**: \"NLI-based scoring（无论 CED 或 flat-NLI）是 RSFT 有效的关键——两种变体均等效提升质量，CED 额外提供可解释的 evidence discrimination\"\n- **top_k selection ablation (k=1 vs k=3)**:\n  - k=1 (best-of-8) 优于 k=3 (top3-of-8)，CED scoring precision 随 k 增大下降\n  - k=1 均值 (3 seeds s42/s43/s44): Ign-F1=45.00, rel_f1=0.4596, evi_f1=81.43, EDCR=0.6434\n  - k=3 (1 seed, reeval_rsft_topk3): Ign-F1=43.64, rel_f1=0.4454, evi_f1=80.88, EDCR=0.6635\n  - Δ (k=3 vs k=1 mean): Ign-F1 **-1.36pp**, rel_f1 **-1.42pp**, evi_f1 **-0.55pp**, EDCR +0.02\n  - 训练数据质量下降: k=1 mean_f1=0.6157, mean_ced=0.6683 → k=3 mean_f1=0.5761, mean_ced=0.6205（来源: mvp2_rsft_ced_scoring / mvp2_rsft_ced_scoring_topk3_r2）\n  - 训练集规模: k=1 选出 2718 样本 (12.4%), k=3 选出 8037 样本 (37%), 数据量 ×2.96 但质量下降抵消数量优势\n  - **叙事**: 低排名 response 引入噪声——rank 2-3 样本的 F1 和 CED 分数均显著低于 rank 1，扩大训练集规模无法补偿数据质量的稀释。这表明 RSFT 的关键不在数据量而在 scoring precision\n  - **注**: k=3 仅 1 seed，差异方向一致但尚不具备统计显著性；作为 ablation table 中的辅助行呈现，不作为独立 claim\n\n### Claim 4 (Diagnostic): EDCR 双层诊断价值（D070/D072）\n- **Layer 1 — 方法级**: EDCR 量化 evidence-extraction decoupling，与 Claim 2 spectrum 呼应\n  - 方法级 EDCR 与 rel_f1 Spearman ρ=-0.965（plan_003 ✅）——本质是 decoupling 的度量\n  - EDCR 识别病理模型（GRPO QLoRA: EDCR≈1.0）\n- **Layer 2 — per-relation-type**: EDCR 提供 evi_f1 不捕捉的 relation-type 诊断信息 ✅\n  - per-relation ρ(EDCR, evi_f1) = **-0.064** (p=0.58) → **完全独立于 evi_f1**\n  - per-relation ρ(EDCR, rel_f1) = -0.793 (p<0.001) → 与 rel_f1 强相关但非完美\n  - per-relation ρ(evi_f1, rel_f1) = -0.013 (p=0.91) → evidence 质量与抽取能力在 relation type 间完全解耦\n  - 典型案例：date_of_birth (EDCR=0.118, 高 faithful) vs head_of_government (EDCR=0.956, 高 decoupled)\n  - 93 relation types 分析（≥5 样本），76 个有非零数据\n- **论文叙事**: EDCR 在方法级是 decoupling 度量工具（横向对比方法），在 relation 级是难度诊断工具（纵向定位薄弱 relation）——两层叙事互补\n- **仍需**: 100 例人工标注验证（RC6）\n\n### Claim 5 (NEW — Scaling): Evidence Tax 呈非线性 U-shape Scaling Pattern（D079/D082/D083）\n- **核心发现**: evidence generation 的代价不是固定的——它与模型容量呈非线性关系\n  - **1.7B (Qwen3-1.7B)**: +6.2pp BENEFIT — evidence generation 起隐式正则化作用，防止小模型过拟合（D083 公平子集分析确认）\n  - **4B (Qwen3-4B)**: -7.9pp cost — 标准 evidence generation 负担，模型容量不足以同时优化两个目标\n  - **8B Qwen (Qwen3-8B)**: ≈0 — 模型容量足够 absorb evidence generation 的额外负担\n  - **8B LLaMA (LLaMA-3.1-8B)**: -0.7pp — 跨家族确认，8B 规模的 evidence tax 趋近于零\n- **U-shape 解释**: 小模型从 evidence 的正则化效应获益 > 生成负担；中等模型容量不足以同时做好两件事；大模型容量充裕，两个目标互不干扰\n- **论文叙事**: 推翻 \"evidence 总有代价\" 的简单叙事，揭示 evidence generation 与模型容量的非线性交互——这为选择何种规模模型部署 evidence-grounded IE 提供实际指导\n- **Cross-family robustness**: LLaMA-8B 与 Qwen-8B 一致确认 8B 规模 evidence tax ≈ 0\n\n## MVP Evidence Summary (D071: 主表报 Ign-F1，附录报 F1; D076 统一协议 rel_f1)\n\n| Config | Ign-F1 | F1 | Δ vs SFT (Ign-F1) | Evi-F1 (cond) | Evi-F1 (joint) | EDCR |\n|--------|--------|------|-------------------|---------------|---------------|------|\n| **SFT no-evidence** | **47.36** | 48.93 | **+7.00pp** | **—** | **—** | **—** |\n| SFT baseline (noquant) | 40.36 | 41.06 | — | 80.13 | 31.17 | 0.7118 |\n| **CED reranker** | **TBD** | 48.64 | **TBD** | **81.88** | — | **0.6156** |\n| RSFT CED s43 (best) | **45.85** | 46.83 | **+5.49pp** | 81.56 | 37.11 | 0.6388 |\n| RSFT CED s44 | 45.51 | 46.55 | +5.15pp | 80.87 | 37.13 | 0.6350 |\n| RSFT CED s42 | 43.63 | 44.49 | +3.27pp | 81.87 | 34.68 | 0.6565 |\n| RSFT CED k=3 | 43.64 | 44.54 | +3.28pp | 80.88 | — | 0.6635 |\n| RSFT r2a (1ep) | 44.01 | 44.94 | +3.65pp | 81.08 | 35.09 | 0.6641 |\n| RSFT r2b (1ep) | 44.10 | 44.93 | +3.74pp | 81.28 | 34.90 | 0.6609 |\n| flat-NLI s42 | 44.49 | 45.39 | +4.13pp | 80.43 | — | 0.6431 |\n| flat-NLI s43 (reeval) | TBD | 45.23 | TBD | 81.58 | — | 0.6505 |\n| DPO bf16 1ep | 38.88 | 40.34 | -1.48pp | 80.88 | — | 0.7139 |\n| DPO bf16 3ep | TBD | 34.29 | TBD | — | — | — |\n| GRPO bf16 G=8 (best step) | 45.59 | ~43.4 | +5.23pp | 80.86 | — | — |\n| GRPO QLoRA (lr=5e-6) | TBD | 1.38 | TBD | 85.00 | — | 0.9900 |\n\n注：Evi-F1 以百分比显示（×100）。Ign-F1 修正后排名无实质变化（仅 r2a/r2b 互换，差 0.09pp）。TBD 项等待 metrics_v2.json 补算。GRPO bf16 Ign-F1=45.59 > F1=43.4 因 train triples 过滤效应。RSFT CED k=3 数据来源: reeval_rsft_topk3 (ign_f1_corrected=true)。\n\n### D076 统一协议 rel_f1（可直接写入论文）\n\n| Config | rel_f1 | evi_f1 |\n|--------|--------|--------|\n| SFT baseline | 0.4049 | — |\n| CED RSFT mean (s42, s44) | **0.4569** | — |\n| CED RSFT s42 | 0.4517 | — |\n| CED RSFT s44 | 0.4621 | — |\n| flat-NLI RSFT mean (s42, s43_r2) | **0.4561** | — |\n| flat-NLI RSFT s42 | 0.4535 | — |\n| flat-NLI RSFT s43_r2 | 0.4586 | — |\n| LLaMA-8B SFT | 0.5514 | 0.8151 |\n| LLaMA-8B no-evidence | 0.5624 | — |\n\n### Evidence Tax Scaling（D079/D082/D083）\n\n| Model | Evidence Tax (Δ) | 方向 |\n|-------|-----------------|------|\n| Qwen3-1.7B | **+6.2pp** | BENEFIT（隐式正则化） |\n| Qwen3-4B | **-7.9pp** | cost |\n| Qwen3-8B | **≈0** | neutral |\n| LLaMA-3.1-8B | **-0.7pp** | near-neutral（跨家族确认） |\n\n### Cross-Dataset Validation（D080）\n\n| Dataset | Ign-F1 Δ | Evi-F1 | 说明 |\n|---------|----------|--------|------|\n| DocRED (in-domain) | baseline | — | — |\n| Re-DocRED | -3.15pp | 0.817 | evidence extraction 泛化，relation extraction 有损 |\n\n## Anticipated Reviewer Concerns (updated from Dream, D068-D083)\n\n### RC1: \"Online RL\" 标题过度声称（Dream 三档一致 Critical）\n- ~~标题和 claim 收窄到 \"GRPO fails for DocRE\"~~\n- **D068/D069 修正**: 重新定位为 \"RL optimization pressure correlates with decoupling severity\"——不是 GRPO 特有问题，而是 RL-for-IE 的通用梯度\n- DPO 数据支撑 decoupling spectrum（gradual decay confirms the pattern）\n\n### RC2: GRPO G=4 太小 + LoRA confound（Dream 三档一致 Major）\n- GRPO G=8 bf16 实验 ✅ — 确认 mild decoupling（-2pp），QLoRA 是 catastrophic amplifier（D065/D066）\n- LoRA confound 已解决：bf16 LoRA vs QLoRA 直接对比\n\n### RC3: CED 不显著优于 flat-NLI（Dream 三档一致 Major）\n- **已解决（D078）**: paired t-test p=0.44，CED 与 flat-NLI 统计不可区分\n- **应对**: 不再声称 CED > flat-NLI；论文定位为 \"NLI-based scoring 是关键（CED 和 flat-NLI 均有效），CED 因可解释性作为默认推荐\"\n- ~~5+ seeds 统计检验~~ → 不再需要，D078 已给出明确结论\n\n### RC4: RSFT 不新颖\n- 不声称 RSFT 是贡献；贡献在于任务定义 + decoupling 发现 + EDCR\n- 诚实定位 RSFT 为 STaR (NeurIPS 2022) 单轮变体 + domain-specific quality filter\n\n### RC12: SAIS 说 evidence 有用，为何 FREIGE 说 evidence 有害？（文献审查 2026-05-16）\n- **关键区分**: discriminative evidence *retrieval*（SAIS/DREEAM — 分类句子是否为证据，作为监督信号提升 RE）vs generative evidence *production*（FREIGE — LLM 生成完整证据文本，额外生成负担导致 scale-dependent 代价）\n- SAIS 的 evidence supervision 是分类任务，不增加输出长度；FREIGE 的 evidence generation 显著增加生成序列长度，模型需分配容量同时完成 RE + evidence 生成\n- **D079/D083 新弹药**: evidence tax 是 scale-dependent 的——1.7B 模型中 evidence 反而有益（+6.2pp），与 SAIS 的发现方向一致。这说明 evidence 的效果取决于模型容量和任务范式的交互，而非简单的有害/有益二分\n- **应对**: Related Work 中精准讨论此对比，明确 FREIGE 研究的是 *generative production* 设定下的代价，与 *retrieval* 设定下的增益不矛盾——两者揭示了 evidence 在不同范式下的不同角色\n\n### RC13: 单模型单数据集泛化性不足（D077 scope 扩展）\n- ~~plan_006: Qwen3-1.7B / 8B model size ablation~~ ✅ D079/D083 完成\n- ~~plan_016: LLaMA-3.1-8B cross-family validation~~ ✅ D082 完成\n- ~~plan_007: Re-DocRED cross-dataset evaluation~~ ✅ D080 完成\n- **结果**: 三项泛化实验全部完成，支撑 C5 scaling pattern + cross-family + cross-dataset 叙事\n\n### RC5: 评测可比性（D041）\n- DREEAM-protocol Evi-F1；conditional Evi-F1 作为辅助指标\n\n### RC6: EDCR 缺人工验证\n- 100 例小规模标注\n\n### RC7: Missing DPO/PPO（Dream 两档 Major）\n- DPO experiment ✅ — 结果确认 decoupling spectrum（D067/D068）\n\n### RC8: Dev-test degradation\n- 观察项，等 test set 数据\n\n### RC9: 连接 reward overoptimization 文献\n- 显式引用 Gao et al. 2023\n\n### RC10: Post-hoc evidence retrieval baseline\n- SFT + BM25 evidence retrieval\n\n### RC11: \"RL 不遗忘\" 文献与 Claim 2 的张力（文献扫描 2026-05-16）\n- 近期多篇论文（arXiv 2507.05386, 2506.23508, 2509.04259）论证 RL fine-tuning 天然缓解 catastrophic forgetting\n- **关键区分**: FREIGE 的 decoupling 是 **intra-task multi-objective trade-off**（RE 抽取 vs evidence 生成两个优化目标的竞争），不是 **inter-task forgetting**（丢失预训练知识）。两者机制不同\n- bf16 GRPO 的 mild decoupling（-2pp）恰好印证这一点：模型没有忘记\"怎么做 IE\"，而是在 evidence reward 压力下偏移了 RE-evidence 的资源分配\n- **应对**: Related Work / Discussion 中显式回应这组文献，区分 intra-task trade-off vs inter-task forgetting\n- **QuRL/QaRL 文献支撑 Claim 2**: QuRL 发现 quantized vs full-precision actor divergence 在长训练中指数增长（直接支撑 QLoRA amplification 叙事）；QaRL 的 error token failure mode 与 QLoRA GRPO garbled evidence 吻合\n\n## Key Baselines (12+)\n\n1. **SFT-only**: Qwen3-4B + LoRA SFT（with evidence）\n1b. **SFT no-evidence**: Qwen3-4B + LoRA SFT（无 evidence，upper bound ablation）\n2. **RSFT flat-NLI**: flat-NLI scored RSFT（核心 ablation）\n3. **RSFT CED**: CED scored RSFT（主方法）\n4. **CED-as-reranker**: 推理时 CED 重排（无训练）\n5. **DPO+CED**: offline preference learning — gradual decoupling（D067/D068）\n6. **GRPO+CED (QLoRA, G=4)**: catastrophic decoupling baseline\n7. **GRPO+CED (bf16, G=8)**: mild decoupling — QLoRA confound 排除（D065/D066）\n8. **Post-hoc retrieval**: SFT + BM25 evidence（NEW）\n9. **DREEAM**: encoder evidence SOTA\n10. **SAIS**: encoder evidence baseline\n11. **DocKS-RAG**: extraction SOTA（无 evidence）\n12. **LMRC**: generative LLM SOTA（无 evidence）\n\n## Publishability Threshold (revised after D078-D083)\n\n- **必要条件**: (1) RSFT 在 test set 上 Ign-F1 显著 > SFT (2) DREEAM-protocol Evi-F1 可报告 (3) Decoupling spectrum 有完整数据支撑（GRPO QLoRA/bf16 + DPO + RSFT）\n- **充分条件**: 上述 + EDCR 人工验证 + scaling pattern (C5) 完整\n- **已达成**: CED vs flat-NLI 统计检验完成（D078: 不可区分，不再是充分条件要素）; 泛化实验完成（D079/D080/D082/D083）\n- **Failure pivot**: decoupling spectrum 不成立（bf16 GRPO 也 catastrophic）→ scope 大幅缩减。**已排除**: bf16 GRPO 确认 mild（D065/D066）\n\n## Research Phase Priorities (revised after D078-D083)\n\n| Priority | 实验 | Claim | GPU-h |\n|----------|------|-------|-------|\n| ~~P0~~ | ~~flat-NLI RSFT ablation (5 seeds)~~ → D078 已结论 | C3 | — |\n| ~~P0~~ | ~~CED RSFT additional seeds (→5 total)~~ → D078 已结论 | C3 | — |\n| P0 | DREEAM-protocol Evi-F1 对齐 | C1 | CPU |\n| P0 | Test set evaluation | C1 | ~4h |\n| P0 | DREEAM baseline reproduction | C1 | ~8h |\n| ~~P0~~ | ~~GRPO G=8 experiment~~ ✅ | C2 | ~16h |\n| ~~P0~~ | ~~DPO+CED experiment~~ ✅ | C2 | ~12h |\n| ~~P0~~ | ~~EDCR per-relation analysis (D070)~~ ✅ | C4 | CPU |\n| ~~P0~~ | ~~Ign-F1 bugfix + data sync (D071)~~ ✅ | ALL | CPU |\n| ~~P0~~ | ~~Model size ablation (1.7B/8B)~~ ✅ D079/D083 | C5 | — |\n| ~~P0~~ | ~~LLaMA-3.1-8B cross-family~~ ✅ D082 | C5 | — |\n| ~~P0~~ | ~~Re-DocRED cross-dataset~~ ✅ D080 | C1/C5 | — |\n| P1 | EDCR human validation | C4 | API |\n| P1 | Post-hoc evidence retrieval baseline | C1 | ~4h |\n| P1 | CED-as-reranker (running) | C1 | ~6h |\n| ~~P0~~ | ~~GRPO forgetting dynamics figure (plan_009)~~ ✅ | C2 | ~2h |\n| ~~P0~~ | ~~SFT-without-evidence ablation (plan_014)~~ ✅ | C1 | ~8h |\n| P2 | Advantage variance measurement | C2 | CPU |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选\n    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py\n    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: eval_flat_nli_seed45\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.455052\n    ign_f1: 0.446181\n    evi_f1: 0.815399\n    edcr: 0.652133\n    evi_f1_joint: 0.355612\n- id: plan_002\n  claim: 1\n  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set\n    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_003\n  claim: 4\n  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing\n    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: plan_003_edcr_diagnostic\n  status: DONE\n  conclusion: success\n  metrics:\n    methods_evaluated: 15\n    edcr_vs_rel_f1_spearman: -0.9648\n    edcr_vs_rel_f1_pvalue: 0.0001\n    edcr_vs_evi_f1_spearman: 0.0022\n    edcr_vs_evi_f1_pvalue: 0.9941\n    edcr_range: 0.63-0.99\n    unique_diagnostic_value: identifies pathological models (GRPO QLoRA) with high\n      evi_f1 but catastrophically low rel_f1\n- id: plan_004\n  claim: 1\n  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)\n    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_004_dreeam_baseline\n  status: DONE\n  conclusion: success\n  metrics:\n    dev_rel_f1: 63.57\n    dev_rel_ign_f1: 61.72\n    dev_evi_f1: 54.01\n    dev_rel_p: 66.95\n    dev_rel_r: 60.51\n    dev_evi_p: 60.53\n    dev_evi_r: 48.76\n- id: plan_005\n  claim: 1\n  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: mvp2_ced_reranker_poc\n  status: DONE\n  conclusion: success\n  metrics:\n    ced_reranker_rel_f1: 0.486367\n    ced_reranker_ign_f1: 0.473634\n    ced_reranker_evi_f1: 0.8188\n    oracle_rel_f1: 0.623746\n    oracle_ign_f1: 0.612518\n    random_rel_f1: 0.453783\n    random_ign_f1: 0.439677\n- id: plan_006\n  claim: 1\n  description: 'Model size ablation (D077 升 P0): Qwen3-1.7B 和 Qwen3-8B 上复现 SFT → RSFT\n    → eval pipeline，验证 evidence tax + RSFT 增益 + decoupling 在不同模型规模下成立。应对 RC4 和 scope\n    不足问题。'\n  priority: P0\n  gpu_budget_hours: 32\n  deps: []\n  registry_id: plan_006_qwen3_1_7b_no_evidence_eval_v3\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.3982\n    rel_f1: 0.4103\n    evi_f1: 0\n    edcr: 0\n    precision: 0.4464\n    recall: 0.3796\n    format_compliance_rate: 1\n    n_truncated: 501\n    inference_time_seconds: 7465.3\n    evidence_tax: 0.0804\n- id: plan_007\n  claim: 1\n  description: 'Re-DocRED cross-dataset (D077 升 P0): 在 Re-DocRED 上用当前 best config\n    做 SFT → RSFT → eval。数据已就绪（格式与 DocRED 兼容，96 relation types 一致）。⚠️ Re-DocRED ~55%\n    triples 无 evidence 标注（修正的 false negative），必须报告两种模式：evidence_only（与 DocRED 可比的\n    evi_f1，仅 43% triples）+ full（全部 triples 的 rel_f1，无 evi_f1）。转换脚本已支持 --mode full。'\n  priority: P0\n  gpu_budget_hours: 16\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_016\n  claim: 2\n  description: 'LLaMA-3.1-8B cross-family validation (D077 新增): 在非 Qwen 家族模型上复现核心\n    pipeline (SFT → RSFT → GRPO QLoRA)，验证 decoupling spectrum 跨模型家族成立。关键实验：LLaMA GRPO\n    QLoRA 是否也出现 catastrophic forgetting。'\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  registry_id: plan_016_llama_rsft_candidates\n  status: DONE\n  conclusion: failed\n- id: plan_008\n  claim: 2\n  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格\n    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: reeval_rsft_topk3\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.4454\n    rel_precision: 0.4512\n    rel_recall: 0.4398\n    ign_f1: 0.4364\n    evi_f1: 0.8088\n    edcr: 0.6635\n    format_ok_rate: 0.999\n    n_truncated: 214\n    n_predictions: 16020\n    inference_time_seconds: 3546.4\n    ign_f1_corrected: true\n- id: plan_011\n  claim: 3\n  description: 'GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward\n    + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要\n    gradient_accumulation 适配显存。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_011_bf16_g8_step_eval\n  status: DONE\n  conclusion: success\n  metrics:\n    step_30:\n      rel_f1: 0.434\n      evi_f1: 0.8063\n      edcr: 0.6807\n    step_50:\n      rel_f1: 0.4276\n      evi_f1: 0.8024\n      edcr: 0.6855\n    step_70:\n      rel_f1: 0.4341\n      evi_f1: 0.8099\n      edcr: 0.6685\n    best_step: step_70\n    trend: non-monotonic, all < ckpt-100 (0.4549)\n- id: plan_012\n  claim: 3\n  description: 'DPO+CED experiment: 用 RSFT 候选数据构造 preference pairs (CED-preferred\n    vs CED-rejected)，DPO 训练。验证 DPO 是否避免 GRPO 的 catastrophic forgetting。Dream v2 三档要求\n    DPO 作为 RL spectrum 关键数据点，必须补全训练超参（β, lr, epochs, pair construction）。D045 升 P0。'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: plan_012_dpo_ced\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.3429\n    evi_f1: 0.8403\n    edcr: 0.7294\n    format_ok_rate: 0.995\n    checkpoint: checkpoint-501\n    rewards_accuracy: 1\n    margins: 9.01\n- id: plan_013\n  claim: 4\n  description: 'EDCR 人工标注验证: 100 个样本，人工判断每个 cited evidence sentence 是否真正支持对应 relation。计算\n    EDCR 与人工判断的相关性，验证 EDCR 作为自动指标的有效性。Dream [M][W] 一致要求。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_009\n  claim: 3\n  description: 'GRPO forgetting dynamics figure: 整理全部 GRPO checkpoint（42个）的 rel_f1/evi_f1/EDCR/reward\n    轨迹，绘制 training dynamics 可视化图。包含 G=4 vs G=8 对比、三种 reward 对比。Dream v2 三档一致要求此图作为论文核心\n    figure。数据已有，只需汇总+画图。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: plan_009_dynamics_figure\n  status: DONE\n  conclusion: success\n- id: plan_010\n  claim: 1\n  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer\n    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_014\n  claim: 1\n  description: 'SFT-without-evidence ablation: 训练 Qwen3-4B SFT 只输出 relation triples（不含\n    evidence sentences），对比标准 SFT（含 evidence）的 rel_f1。隔离 evidence generation 对抽取性能的代价。Dream\n    v2 三档一致要求。用于回答\"43.2% vs LMRC 60.7% 的 gap 有多少来自 evidence 生成负担\"。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_014_sft_no_evidence\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.7077\n    eval_loss: 0.8781\n    eval_token_accuracy: 0.8086\n    epochs: 3\n    total_steps: 570\n    train_runtime_min: 64\n    samples: 3027\n    trainable_params: 132M/4.15B (3.18%)\n- id: plan_015\n  claim: 2\n  description: 'bf16 LoRA GRPO clean control: 与原始 GRPO (QLoRA 4-bit, G=4, kl=0, CED\n    reward) 只改一个变量——quantization 从 QLoRA 4-bit 改为 bf16 LoRA。G=4, kl_coef=0 不变。目的:\n    隔离 QLoRA confound，判断 decoupling 是 QLoRA artifact 还是 genuine RL-for-IE 现象。Dream\n    v2 三档一致的 critical 要求。如 decoupling 在 bf16 下仍持续 → 可泛化 claim；如消失 → QLoRA 特定，需 re-scope。优先级取决于\n    plan_011 eval 结果。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_011\n  registry_id: plan_015_grpo_g4_bf16_v3\n  status: DONE\n  conclusion: killed\n- id: plan_mvp1\n  claim: 1\n  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing\n    distractor 的能力验证'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: mvp1_ced_signal\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_margin: 0.48\n    discrimination_accuracy: 0.815\n    pearson_r_margin_jaccard: 0.34\n    pass: true\n- id: plan_mvp2_sft\n  claim: 1\n  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mvp2_sft_warmup\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.72\n    accuracy: 0.835\n- id: plan_mvp2_rsft\n  claim: 1\n  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部\n    PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087,\n    r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_mvp1\n  - plan_mvp2_sft\n  registry_id: mvp2_rsft_train_r1\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.0483\n    num_preds: 848\n    sft_baseline_rel_f1: 0.4057\n    failure_mode: relation_ontology_collapse_to_freetext\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n- id: plan_mvp2_grpo\n  claim: 3\n  description: 'GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1\n    max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic\n    forgetting。D031/D033 完整轨迹支撑 Claim 3'\n  priority: P0\n  gpu_budget_hours: 60\n  deps:\n  - plan_mvp2_sft\n  registry_id: mvp2_grpo_ced_lr5e6_r1\n  status: DONE\n  conclusion: killed\n\n\n## registry (completed experiments)\n\n- exp_id: mvp1_ced_signal\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_margin: 0.48\n    discrimination_accuracy: 0.815\n    pearson_r_margin_jaccard: 0.34\n    pass: true\n- exp_id: smoke_test_grpo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_sft_warmup\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.72\n    accuracy: 0.835\n- exp_id: precompute_nli_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_grpo_ced\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_extract\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_sft_eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_extract_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: mvp2_grpo_extract_r3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_sft_eval_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    ign_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    precision: 0.4043\n    recall: 0.407\n    evi_precision: 0.8035\n    evi_recall: 0.7924\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.626\n    n_parseable: 617\n    n_truncated: 367\n    n_predictions: 18815\n    inference_time_seconds: 6484.7\n- exp_id: mvp2_sft_eval_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    ign_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    precision: 0.4043\n    recall: 0.407\n    evi_precision: 0.8035\n    evi_recall: 0.7924\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.626\n    n_parseable: 617\n    n_truncated: 367\n    n_predictions: 18815\n- exp_id: mvp2_grpo_ced_kl001_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001_r3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001_r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_step: 100\n    train_runtime_s: 9069.88\n    reward_final: 1.195\n    f1_reward_final: 0.573\n    ced_reward_final: 0.328\n    format_reward_final: 0.293\n    frac_zero_std_final: 0.2\n    kl_final: 0.118\n    loss_final: -0.009\n    grad_norm_final: 0.14\n    entropy_final: 0.067\n    completion_length_mean_final: 520.8\n    best_reward_step: 90\n    best_reward: 1.37\n    best_f1_reward: 0.72\n    best_ced_reward: 0.353\n- exp_id: mvp2_grpo_extract_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_early\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    f1: 0.1563\n    ign_f1: 0.1563\n    evi_f1: 0.5643\n    edcr: 0.8858\n    precision: 0.2356\n    recall: 0.1169\n    evi_precision: 0.4864\n    evi_recall: 0.6721\n    format_ok_rate: 0.999\n    n_parseable: 984\n    n_truncated: 11\n    n_predictions: 9250\n    tp: 1421\n    pred_count: 6032\n    gold_count: 12151\n- exp_id: mvp2_grpo_flatnli_r6\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    steps_completed: 25\n    final_frac_zero_std: 0.9\n    final_f1_reward: 0\n    final_flat_nli_reward: 0\n    final_format_reward: 0.293\n    collapse_step: 25\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.00296\n    rel_precision: 0.00314\n    rel_recall: 0.0028\n    evi_f1: 0.72\n    evi_precision: 0.6429\n    evi_recall: 0.8182\n    edcr: 0.9983\n    n_parseable: 984\n    n_truncated: 24\n    n_predictions: 11621\n    tp: 34\n    pred_count: 10839\n    gold_count: 12151\n    inference_time_seconds: 5211.4\n- exp_id: mvp2_eval_ced_kl001_r4_multi\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    checkpoint-10:\n      f1: 0.003\n      ign_f1: 0.003\n      evi_f1: 0.72\n      edcr: 0.9983\n      format_ok_rate: 0.999\n    checkpoint-20:\n      f1: 0.0088\n      ign_f1: 0.0088\n      evi_f1: 0.423\n      edcr: 0.9954\n      format_ok_rate: 0.999\n    checkpoint-30:\n      f1: 0.0338\n      ign_f1: 0.0338\n      evi_f1: 0.5889\n      edcr: 0.9798\n      format_ok_rate: 1\n    checkpoint-50:\n      f1: 0.1563\n      ign_f1: 0.1563\n      evi_f1: 0.5643\n      edcr: 0.8858\n      format_ok_rate: 0.999\n    checkpoint-60:\n      f1: 0.1467\n      ign_f1: 0.1467\n      evi_f1: 0.5763\n      edcr: 0.9062\n      format_ok_rate: 1\n    checkpoint-90:\n      f1: 0.2108\n      ign_f1: 0.2108\n      evi_f1: 0.5666\n      edcr: 0.8584\n      format_ok_rate: 1\n- exp_id: mvp2_eval_ced_kl001_r4_step100\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.2167\n    ign_f1: 0.2167\n    precision: 0.2849\n    recall: 0.1749\n    evi_f1: 0.5746\n    evi_precision: 0.5244\n    evi_recall: 0.6353\n    edcr: 0.8539\n    pred_count: 7460\n    gold_count: 12151\n    tp: 2125\n    n_truncated: 21\n    format_ok_rate: 1\n- exp_id: mvp2_eval_ced_kl001_r4_last\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt90\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_high\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    checkpoint_60:\n      rel_f1: 0.1467\n      ign_f1: 0.1467\n      precision: 0.1909\n      recall: 0.1192\n      evi_f1: 0.5763\n      edcr: 0.9062\n      pred_count: 10041\n      gold_count: 12151\n      n_truncated: 16\n      format_ok_rate: 1\n    note: Only ckpt-60 completed. Process died during ckpt-70 inference at 8% (5/62\n      batch). ckpt-80/90 never started.\n- exp_id: mvp2_eval_ced_kl001_r4_step90\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.2108\n    ign_f1: 0.2108\n    evi_f1: 0.5666\n    edcr: 0.8584\n    pred_count: 11160\n    n_truncated: 22\n    format_ok_rate: 1\n    n_documents: 985\n- exp_id: mvp2_grpo_ced_lr5e6_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_p1_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_rp_r1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt7080\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_rp_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt20\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0077\n    rel_precision: 0.0071\n    rel_recall: 0.0084\n    evi_f1: 0.628\n    evi_precision: 0.855\n    evi_recall: 0.496\n    edcr: 0.993\n    format_ok_rate: 0.991\n    field_compliance_rate: 0.399\n    pred_count: 14440\n    gold_count: 12151\n    tp: 102\n    n_truncated: 587\n    inference_time_seconds: 6370.4\n- exp_id: mvp2_eval_lr5e6_r1_ckpt40\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt40_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0071\n    precision: 0.0066\n    recall: 0.0078\n    evi_f1: 0.7584\n    evi_precision: 0.9113\n    evi_recall: 0.6494\n    edcr: 0.9942\n    format_ok_rate: 0.9939\n    field_compliance_rate: 0.5675\n    pred_count: 14434\n    gold_count: 12151\n    tp: 95\n    n_truncated: 424\n    inference_time_seconds: 6152\n- exp_id: mvp2_eval_lr5e6_rp_r2_ckpt20\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_sft_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    evi_f1: 0.7979\n    evi_f1_joint: 0.3117\n    evi_f1_joint_P: 0.3037\n    evi_f1_joint_R: 0.32\n    edcr: 0.7118\n    pred_count: 12234\n    gold_count: 12151\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.998\n    field_compliance_rate: 0.6264\n    n_truncated: 367\n    inference_time_seconds: 6138.5\n- exp_id: mvp2_eval_lr5e6_r1_ckpt60\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt80\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0116\n    ign_f1: 0.0116\n    precision: 0.0109\n    recall: 0.0124\n    evi_f1: 0.828\n    evi_precision: 0.928\n    evi_recall: 0.748\n    edcr: 0.993\n    format_ok_rate: 0.999\n    field_compliance_rate: 0.788\n    pred_count: 13828\n    gold_count: 12151\n    n_truncated: 210\n    inference_time_seconds: 6099\n- exp_id: mvp2_eval_lr5e6_r1_ckpt60_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0093\n    precision: 0.0085\n    recall: 0.0103\n    evi_f1: 0.81\n    edcr: 0.993\n    format_ok_rate: 0.998\n    pred_count: 14626\n    gold_count: 12151\n    tp: 125\n    inference_time_seconds: 6152\n- exp_id: mvp2_eval_lr5e6_r1_ckpt100\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0138\n    rel_precision: 0.0132\n    rel_recall: 0.0144\n    ign_f1: 0.0138\n    evi_f1: 0.8504\n    evi_precision: 0.9256\n    evi_recall: 0.7866\n    edcr: 0.9876\n    format_ok_rate: 0.999\n    field_compliance_rate: 0.8162\n    evidence_format_rate: 0.8162\n    tp: 175\n    pred_count: 13300\n    gold_count: 12151\n    n_predictions: 15498\n    n_truncated: 181\n    n_documents: 985\n    n_parseable: 984\n    inference_time_seconds: 5901.7\n- exp_id: mvp2_diversity_probe\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    unique_triples_t07: 5\n    unique_triples_t10: 8\n    jaccard_t07: 0.17\n    jaccard_t10: 0.051\n    format_ok_rate_t07: 0.5\n    format_ok_rate_t10: 0.438\n    n_samples: 3\n    n_generations: 8\n    note: 'unique_triples_t07 corrected from 7 to 5.0 (mean). Reviewer: format_ok\n      ~34% after fix, ''diversity'' was JSON key name variants not semantic diversity'\n- exp_id: mvp2_rsft_generate\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    generation_count: 5288\n    unique_docs: 659\n    format_compliance: 0.998\n    diversity_range: 7.5-7.8/8\n    exit_code: 0\n- exp_id: mvp2_rsft_ced_scoring\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    input_generations: 21952\n    selected_samples: 2718\n    unique_docs: 2691\n    selection_rate: 0.124\n    mean_f1: 0.6157\n    mean_ced: 0.6683\n    f1_range:\n    - 0.1026\n    - 1\n    zero_f1_samples: 0\n    selection_strategy: top_k=1\n    f1_threshold: 0.1\n- exp_id: mvp2_rsft_train_r1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.0483\n    num_preds: 848\n    sft_baseline_rel_f1: 0.4057\n    failure_mode: relation_ontology_collapse_to_freetext\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n- exp_id: mvp2_rsft_train_r1_s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.7622\n    train_loss: 0.6148\n    eval_entropy: 0.6724\n    mean_token_accuracy: 0.8291\n    total_steps: 510\n    epochs: 3\n    training_hours: 1.99\n- exp_id: mvp2_rsft_train_r1_s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4655\n    evi_f1: 0.8087\n    evi_f1_joint: 0.3713\n    evi_f1_joint_P: 0.3775\n    evi_f1_joint_R: 0.3653\n    edcr: 0.635\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0598\n    delta_evi_f1: 0.0108\n    delta_evi_f1_joint: 0.0596\n    mvp2_pass: true\n- exp_id: mvp2_rsft_ced_scoring_topk3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_s44\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_ced_reranker_poc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ced_reranker_rel_f1: 0.486367\n    ced_reranker_ign_f1: 0.473634\n    ced_reranker_evi_f1: 0.8188\n    oracle_rel_f1: 0.623746\n    oracle_ign_f1: 0.612518\n    random_rel_f1: 0.453783\n    random_ign_f1: 0.439677\n- exp_id: mvp2_rsft_diagnosis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    root_cause: overfitting_plus_sft_knowledge_overwrite\n    truncated_json_samples: 170\n    truncated_pct: 6.3\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n    lora_scaling: 2\n    rsft_zero_relation_samples: 170\n    sft_zero_relation_docs: 26\n    rsft_mean_relations: 11.2\n    sft_mean_relations: 12.5\n- exp_id: mvp2_rsft_train_r2_fix\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_rsft_r2a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4494\n    evi_f1: 0.8108\n    edcr: 0.6641\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0437\n    delta_evi_f1: 0.0129\n    mvp2_pass: true\n- exp_id: mvp2_rsft_r2b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4493\n    evi_f1: 0.8128\n    edcr: 0.6609\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0436\n    delta_evi_f1: 0.0149\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4449\n    evi_f1: 0.8187\n    evi_f1_joint: 0.3468\n    evi_f1_joint_P: 0.3515\n    evi_f1_joint_R: 0.3423\n    edcr: 0.6565\n    num_preds: 15307\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0392\n    delta_evi_f1: 0.0208\n    delta_evi_f1_joint: 0.0351\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r2a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4494\n    ign_f1: 0.4494\n    evi_f1: 0.8108\n    evi_f1_joint: 0.3509\n    evi_f1_joint_P: 0.3423\n    evi_f1_joint_R: 0.3599\n    edcr: 0.6641\n    precision: 0.4512\n    recall: 0.4475\n    evi_precision: 0.8143\n    evi_recall: 0.8073\n    format_ok_rate: 1\n    n_predictions: 15482\n    n_truncated: 208\n    inference_time_s: 5967.2\n    delta_evi_f1_joint: 0.0392\n- exp_id: mvp2_eval_rsft_r2b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4493\n    ign_f1: 0.4493\n    evi_f1: 0.8128\n    evi_f1_joint: 0.349\n    evi_f1_joint_P: 0.3455\n    evi_f1_joint_R: 0.3526\n    edcr: 0.6609\n    precision: 0.4566\n    recall: 0.4424\n    evi_precision: 0.8201\n    evi_recall: 0.8056\n    pred_count: 14829\n    format_ok: 983/985\n    truncated: 179\n    inference_time_s: 5862\n    delta_evi_f1_joint: 0.0373\n- exp_id: mvp2_eval_rsft_s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_s43_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4683\n    ign_f1: 0.4683\n    evi_f1: 0.8156\n    evi_f1_joint: 0.3711\n    evi_f1_joint_P: 0.3747\n    evi_f1_joint_R: 0.3675\n    edcr: 0.6388\n    precision: 0.4817\n    recall: 0.4556\n    evi_precision: 0.8142\n    evi_recall: 0.817\n    n_predictions: 14970\n    n_truncated: 171\n    format_ok_rate: 1\n    inference_time_s: 6316.7\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0626\n    delta_evi_f1: 0.0177\n    delta_evi_f1_joint: 0.0594\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r2b_maxtok1536\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_r2b_maxtok1536_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.4504\n    ign_f1: 0.4504\n    evi_f1: 0.8102\n    edcr: 0.674\n    precision: 0.4488\n    recall: 0.4519\n    evi_precision: 0.8162\n    evi_recall: 0.8044\n    n_truncated: 146\n    n_total: 985\n    n_predictions: 17188\n    n_distractor_citations: 19589\n    n_total_citations: 29063\n    format_ok_rate: 0.998\n- exp_id: mvp2_rsft_ced_scoring_topk3_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    input_generations: 21728\n    selected_samples: 8037\n    unique_docs: 2691\n    selection_rate: 0.37\n    mean_f1: 0.5761\n    mean_ced: 0.6205\n    mean_combined: 0.6787\n    f1_range_p25: 0.444\n    f1_range_p75: 0.717\n    ced_range_p25: 0.487\n    ced_range_p75: 0.774\n    truncated_samples: 1924\n    truncated_pct: 8.9\n    selection_strategy: top_k=3\n    f1_threshold: 0.1\n    topk1_samples: 2718\n    data_multiplier: 2.96\n- exp_id: plan_004_dreeam_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dev_rel_f1: 63.57\n    dev_rel_ign_f1: 61.72\n    dev_evi_f1: 54.01\n    dev_rel_p: 66.95\n    dev_rel_r: 60.51\n    dev_evi_p: 60.53\n    dev_evi_r: 48.76\n- exp_id: plan_011_grpo_g8_bf16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_step: 100\n    train_runtime_s: 554\n    reward_final: 1.795\n    f1_reward_final: 1.002\n    ced_reward_final: 0.494\n    format_reward_final: 0.3\n    frac_zero_std_final: 0\n    kl_final: 0.022\n    best_reward_step: 85\n    best_reward: 2.858\n    best_f1_reward: 1.85\n    mode_collapse: false\n    lora_config: r=64, alpha=128, dropout=0.05, bf16\n    checkpoints: 10 checkpoints (step 10-100)\n- exp_id: plan_001_flat_nli_scoring\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_scored: 21728\n    selected_samples: 2691\n    selection_rate: 0.124\n    selection_strategy: top_k=1\n    f1_threshold: 0.1\n    output_path: /root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl\n- exp_id: eval_grpo_g8_bf16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ckpt80_rel_f1: 0.4456\n    ckpt80_ign_f1: 0.4456\n    ckpt80_evi_f1: 0.8034\n    ckpt80_edcr: 0.6409\n    ckpt80_format_ok: 984/985\n    ckpt80_truncated: 50\n    ckpt90_rel_f1: 0.4523\n    ckpt90_ign_f1: 0.4523\n    ckpt90_evi_f1: 0.8052\n    ckpt90_edcr: 0.6414\n    ckpt90_format_ok: 983/985\n    ckpt90_truncated: 61\n    ckpt100_rel_f1: 0.4549\n    ckpt100_ign_f1: 0.4549\n    ckpt100_evi_f1: 0.8086\n    ckpt100_edcr: 0.6318\n    ckpt100_format_ok: 985/985\n    ckpt100_truncated: 61\n    best_checkpoint: ckpt-100\n- exp_id: plan_011_eval_g8_bf16_ckpt100\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_011_grpo_g8_bf16_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4549\n    ign_f1: 0.4549\n    evi_f1: 0.8086\n    edcr: 0.6318\n    format_ok_rate: 1\n    n_truncated: 61\n    n_total: 985\n    n_predictions: 10701\n    checkpoint: checkpoint-100\n    model: Qwen3-4B + SFT merged + GRPO bf16 LoRA ckpt-100\n    inference_time_s: 3170.3\n- exp_id: plan_001_rsft_flat_nli\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.6238\n    train_loss_min: 0.5803\n    mean_token_accuracy: 0.8528\n    train_runtime_sec: 2946\n    epochs: 3\n    total_steps: 507\n    samples: 2691\n- exp_id: plan_012_dpo_ced\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.3429\n    evi_f1: 0.8403\n    edcr: 0.7294\n    format_ok_rate: 0.995\n    checkpoint: checkpoint-501\n    rewards_accuracy: 1\n    margins: 9.01\n- exp_id: plan_014_sft_no_evidence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.7077\n    eval_loss: 0.8781\n    eval_token_accuracy: 0.8086\n    epochs: 3\n    total_steps: 570\n    train_runtime_min: 64\n    samples: 3027\n    trainable_params: 132M/4.15B (3.18%)\n- exp_id: plan_015_grpo_g4_bf16\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_015_grpo_g4_bf16_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_015_grpo_g4_bf16_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: eval_plan_001_flat_nli\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4539\n    ign_f1: 0.4539\n    evi_f1: 0.8043\n    edcr: 0.6431\n    precision: 0.4671\n    recall: 0.4414\n    evi_precision: 0.8143\n    evi_recall: 0.7945\n    format_ok_rate: 1\n    n_truncated: 199\n    n_documents: 985\n    n_predictions: 15294\n    inference_time_seconds: 3631\n- exp_id: eval_plan_014_sft_no_evidence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4893\n    rel_ign_f1: 0.4893\n    rel_precision: 0.4884\n    rel_recall: 0.4902\n    evi_f1: 0\n    evi_precision: 0\n    evi_recall: 0\n    edcr: 0\n    format_ok_rate: 0.9919\n    n_truncated: 298\n    n_predictions: 21064\n    n_documents: 985\n    n_parseable: 977\n    inference_time_seconds: 4103.8\n- exp_id: plan_008_rsft_topk3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.5543\n    eval_loss: 0.8297\n    eval_mean_token_accuracy: 0.8228\n    eval_entropy: 0.6001\n    train_runtime_sec: 10916\n    total_steps: 1509\n    epochs: 3\n    trainable_params_pct: 3.18\n    rsft_samples: 8037\n    ced_score_mean: 0.621\n    task_eval_f1_ep1: 0.4848\n    task_eval_f1_ep2: 0.4824\n    task_eval_f1_ep3: 0.5012\n    task_eval_evi_f1_ep1: 0.745\n    task_eval_evi_f1_ep2: 0.6997\n    task_eval_evi_f1_ep3: 0.6816\n    task_eval_edcr_ep1: 0.6525\n    task_eval_edcr_ep2: 0.6529\n    task_eval_edcr_ep3: 0.5963\n    task_eval_note: 50-doc subset, not full dev\n- exp_id: plan_002_test_eval_s44\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_001_flat_nli_seed43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss_final: 0.6257\n    train_loss_min: 0.5895\n    eval_loss_epoch3: 0.7567\n    eval_accuracy_epoch3: 0.8298\n    total_steps: 507\n    epochs: 3\n    train_runtime_seconds: 6880\n    task_eval_f1_ep1: 0.4825\n    task_eval_f1_ep2: 0.4542\n    task_eval_f1_ep3: 0.4866\n    task_eval_evi_f1_ep3: 0.7834\n    task_eval_edcr_ep3: 0.6402\n    task_eval_note: 50-doc subset, not full dev\n- exp_id: eval_sft_baseline_noquant\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4106\n    rel_precision: 0.4198\n    rel_recall: 0.4019\n    evi_f1: 0.8013\n    evi_precision: 0.8005\n    evi_recall: 0.8022\n    evi_f1_joint: 0.3216\n    edcr: 0.7039\n    format_ok_rate: 0.998\n    field_compliance_rate: 0.7066\n    n_predictions: 16774\n    n_truncated: 288\n    n_documents: 985\n    inference_time_seconds: 3677.9\n- exp_id: plan_012_dpo_ced_1ep\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0022\n    evi_f1: 0.75\n    edcr: 0.9982\n    format_ok: 981/985\n    truncated: 358/985\n    tp: 34\n    n_preds: 19265\n    inference_time_s: 3643\n    train_loss_final: 0.59\n    rewards_accuracy: 0.82\n    rewards_margins: 0.86\n    total_steps: 167\n    training_time_min: 33\n- exp_id: plan_009_forgetting_figure\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_011_bf16_g8_step_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    step_30:\n      rel_f1: 0.434\n      evi_f1: 0.8063\n      edcr: 0.6807\n    step_50:\n      rel_f1: 0.4276\n      evi_f1: 0.8024\n      edcr: 0.6855\n    step_70:\n      rel_f1: 0.4341\n      evi_f1: 0.8099\n      edcr: 0.6685\n    best_step: step_70\n    trend: non-monotonic, all < ckpt-100 (0.4549)\n- exp_id: plan_009_extract_reward_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_009_flatnli_reward_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: eval_plan_012_dpo_ced_ckpt400\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_009_flatnli_reward_eval_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: eval_plan_012_dpo_ced_1ep\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0022\n    ign_f1: 0.0022\n    evi_f1: 0.75\n    edcr: 0.9982\n    num_preds: 19265\n    format_ok: 981/985\n    truncated: 358/985\n    tp: 34\n    inference_time_s: 3643\n- exp_id: eval_plan_001_flat_nli_s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    rel_f1: 0.0022\n    ign_f1: 0.0022\n    evi_f1: 0.8533\n    edcr: 0.9982\n    num_preds: 17285\n    format_ok: 981/985\n    truncated: 251/985\n    tp: 32\n    note: INVALID — missing --sft_adapter, same bug as DPO 1ep eval\n- exp_id: plan_001_flat_nli_seed45\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    task_eval_rel_f1: 0.4876\n    task_eval_evi_f1: 0.7927\n    task_eval_edcr: 0.6517\n    train_loss: 0.6245\n    runtime_hours: 1.69\n    note: task-eval on 50 docs only, full dev eval needed\n- exp_id: eval_plan_008_rsft_topk3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    note: INVALID — missing --sft_adapter, killed by Director instruction\n- exp_id: plan_001_flat_nli_seed44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.6247\n    eval_loss: 0.7564\n    eval_mean_token_accuracy: 0.8299\n    task_eval_f1_ep1: 0.4306\n    task_eval_f1_ep2: 0.4884\n    task_eval_f1_ep3: 0.4897\n    task_eval_evi_f1_ep3: 0.78\n    task_eval_edcr_ep3: 0.6596\n    task_eval_ign_f1_ep3: 0.4897\n    train_runtime_sec: 6197\n    num_epochs: 3\n    total_steps: 507\n- exp_id: eval_plan_012_dpo_1ep_fixed\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: eval_plan_008_topk3_fixed\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: eval_plan_012_dpo_1ep_fixed_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.4034\n    evi_f1: 0.8088\n    edcr: 0.7139\n    format_ok_rate: 0.999\n    truncated_rate: 0.343\n    predictions: 19107\n    ign_f1: 0.4034\n    precision: 0.3809\n    recall: 0.4287\n    vs_sft_delta: -0.0023\n    note: DPO 1ep matches SFT baseline. 1ep→3ep trajectory shows gradual decoupling\n      (rel_f1↓ evi_f1↑), consistent with GRPO pattern. Ign-F1=F1 exact match needs\n      investigation.\n- exp_id: reeval_flat_nli_s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4523\n    ign_f1: 0.4523\n    evi_f1: 0.8158\n    edcr: 0.6505\n    num_preds: 15357\n    format_ok: 984/985\n    truncated: 211/985\n    inference_time_s: 3515.8\n- exp_id: reeval_rsft_topk3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.4454\n    rel_precision: 0.4512\n    rel_recall: 0.4398\n    ign_f1: 0.4364\n    evi_f1: 0.8088\n    edcr: 0.6635\n    format_ok_rate: 0.999\n    n_truncated: 214\n    n_predictions: 16020\n    inference_time_seconds: 3546.4\n    ign_f1_corrected: true\n- exp_id: eval_flat_nli_seed44\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: eval_flat_nli_seed45\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.455052\n    ign_f1: 0.446181\n    evi_f1: 0.815399\n    edcr: 0.652133\n    evi_f1_joint: 0.355612\n- exp_id: plan_003_edcr_diagnostic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    methods_evaluated: 15\n    edcr_vs_rel_f1_spearman: -0.9648\n    edcr_vs_rel_f1_pvalue: 0.0001\n    edcr_vs_evi_f1_spearman: 0.0022\n    edcr_vs_evi_f1_pvalue: 0.9941\n    edcr_range: 0.63-0.99\n    unique_diagnostic_value: identifies pathological models (GRPO QLoRA) with high\n      evi_f1 but catastrophically low rel_f1\n- exp_id: eval_flat_nli_s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.461506\n    ign_f1: 0.452126\n    evi_f1: 0.813123\n    edcr: 0.645808\n    evi_f1_joint: 0.359673\n- exp_id: plan_009_dynamics_figure\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: eval_plan_014_no_evidence\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: rsft_ced_s45_train\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: rsft_ced_s43_train\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: rsft_ced_s45_train_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: rsft_ced_s43_train_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: rsft_ced_s43_train_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.6151\n    eval_loss: 0.7618\n    task_eval_f1: 0.5026\n    task_eval_ign_f1: 0.4932\n    task_eval_evi_f1: 0.7624\n    task_eval_edcr: 0.6516\n    total_steps: 510\n    epochs: 3\n    training_hours: 1.82\n- exp_id: rsft_ced_s45_train_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: rsft_ced_s45_train_r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    training_completed: true\n    checkpoint: checkpoint-510\n    note: Training metrics not captured (r4 retry after OOM). Eval running as eval_rsft_ced_s45.\n- exp_id: eval_rsft_ced_s45\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4514\n    ign_f1: 0.4416\n    evi_f1: 0.8174\n    rel_p: 0.4718\n    rel_r: 0.4326\n    edcr: 0.655\n    evi_f1_joint: 0.3558\n    n_truncated: 206\n    format_ok_rate: 1\n- exp_id: eval_rsft_ced_s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4601\n    ign_f1: 0.4512\n    precision: 0.4696\n    recall: 0.4509\n    evi_f1: 0.8063\n    evi_precision: 0.8025\n    evi_recall: 0.8101\n    edcr: 0.6542\n    evi_f1_joint: 0.3605\n    format_ok_rate: 1\n    n_truncated: 184\n    n_predictions: 15051\n    inference_time_seconds: 10768.2\n- exp_id: eval_plan_014_no_evidence_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4876\n    ign_f1: 0.4721\n    evi_f1: 0\n    edcr: 0\n    evi_f1_joint: 0\n    precision: 0.4901\n    recall: 0.4851\n    ign_precision: 0.4654\n    ign_recall: 0.4791\n    format_compliance: 0.993\n    truncation_rate: 0.312\n    n_predictions: 21181\n    n_documents: 985\n- exp_id: reeval_flat_nli_s43_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4586\n    rel_precision: 0.4732\n    rel_recall: 0.4449\n    ign_f1: 0.4503\n    evi_f1: 0.8113\n    evi_precision: 0.8035\n    evi_recall: 0.8192\n    evi_f1_joint: 0.358\n    edcr: 0.6552\n    format_ok_rate: 0.999\n    n_truncated: 184\n    n_predictions: 15015\n- exp_id: seed_comparison_prep\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: reeval_ced_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.4423\n    rel_f1: 0.4517\n    evi_f1: 0.8175\n    evi_f1_joint: 0.3518\n    edcr: 0.6569\n    format_compliance_rate: 1\n    field_compliance_rate: 0.7756\n    n_truncated: 214\n    inference_time_seconds: 10815.5\n- exp_id: reeval_ced_s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.4511\n    rel_f1: 0.4621\n    evi_f1: 0.805\n    evi_f1_joint: 0.3677\n    edcr: 0.635\n    format_compliance_rate: 1\n    field_compliance_rate: 0.802\n    n_truncated: 190\n    inference_time_seconds: 13077.6\n- exp_id: reeval_flat_nli_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.4448\n    rel_f1: 0.4535\n    evi_f1: 0.8039\n    evi_f1_joint: 0.3558\n    edcr: 0.6458\n    format_compliance_rate: 1\n    field_compliance_rate: 0.7787\n    n_truncated: 205\n    inference_time_seconds: 13253.1\n- exp_id: reeval_sft_baseline_d076\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4049\n    ign_f1: 0.3974\n    evi_f1: 0.7986\n    edcr: 0.6982\n    evi_f1_joint: 0.3147\n    format_compliance_rate: 0.998\n    n_truncated: 288\n    n_documents: 985\n    n_predictions: 16880\n    inference_time_sec: 7056.5\n- exp_id: plan_006_qwen3_1_7b_sft\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_006_qwen3_1_7b_sft_bf16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.6884\n    eval_loss: 0.8031\n    eval_mean_token_accuracy: 0.8238\n    eval_entropy: 0.682\n    train_runtime_sec: 2473\n    train_samples_per_second: 3.672\n    epochs: 3\n    total_steps: 570\n- exp_id: plan_006_qwen3_1_7b_no_evidence_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_006_qwen3_8b_sft_bf16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.5705\n    eval_loss: 0.7186\n    eval_mean_token_accuracy: 0.8377\n    eval_entropy: 0.5614\n    train_runtime_s: 3932\n    epoch: 3\n- exp_id: plan_006_qwen3_1_7b_sft_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    f1: 0.4945\n    ign_f1: 0.4786\n    evi_f1: 0.8316\n    edcr: 0.6704\n    precision: 0.5085\n    recall: 0.4813\n    ign_precision: 0.483\n    ign_recall: 0.4743\n    evi_precision: 0.8203\n    evi_recall: 0.8432\n    evi_f1_joint: 0.3958\n    format_compliance_rate: 1\n    n_predictions: 17184\n    n_truncated: 314\n    inference_time_seconds: 6848.7\n- exp_id: plan_002_test_eval_s44_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: reeval_flat_nli_s44\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_006_qwen3_8b_sft_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.5051\n    f1: 0.5262\n    evi_f1: 0.8188\n    edcr: 0.651\n    format_ok_rate: 0.999\n    n_truncated: 313\n    n_predictions: 17401\n    inference_time_s: 7206\n- exp_id: plan_006_qwen3_1_7b_no_evidence_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    f1: 0.3884\n    ign_f1: 0.3786\n    evi_f1: 0.0007\n    edcr: 0.9848\n    precision: 0.4282\n    recall: 0.3553\n    pred_count: 27049\n    n_truncated: 531\n    format_ok_rate: 0.999\n- exp_id: plan_006_qwen3_8b_no_evidence_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.6509\n    eval_loss: 0.8153\n    eval_mean_token_accuracy: 0.8174\n    eval_entropy: 0.6275\n    train_runtime_sec: 3656\n    epoch: 3\n- exp_id: plan_016_llama_3_1_8b_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_016_llama_3_1_8b_no_evidence_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_006_qwen3_8b_no_evidence_eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_006_qwen3_8b_no_evidence_eval_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_006_qwen3_1_7b_no_evidence_eval_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_006_qwen3_1_7b_no_evidence_eval_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.3982\n    rel_f1: 0.4103\n    evi_f1: 0\n    edcr: 0\n    precision: 0.4464\n    recall: 0.3796\n    format_compliance_rate: 1\n    n_truncated: 501\n    inference_time_seconds: 7465.3\n    evidence_tax: 0.0804\n- exp_id: plan_006_qwen3_1_7b_no_evidence_eval_v2r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_016_llama_3_1_8b_no_evidence_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.5452\n    rel_f1: 0.5624\n    evi_f1: 0\n    edcr: 0\n- exp_id: plan_016_llama_3_1_8b_sft_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.5384\n    rel_f1: 0.5514\n    evi_f1: 0.8151\n    edcr: 0.628\n    precision: 0.5464\n    recall: 0.5565\n    evi_f1_joint: 0.4317\n    format_compliance_rate: 0.9949\n    n_truncated: 197\n    n_predictions: 15325\n    inference_time_seconds: 7331.3\n    evidence_tax_ign_f1: 0.0068\n    evidence_tax_rel_f1: 0.011\n- exp_id: plan_007_redocred_4b_sft_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_007_redocred_4b_sft_eval_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.3659\n    f1: 0.3706\n    evi_f1: 0.817\n    edcr: 0.6674\n    format_compliance_rate: 0.996\n    n_truncated: 139\n    n_total: 493\n    inference_time_seconds: 3281.7\n    precision: 0.4316\n    recall: 0.3247\n    ign_precision: 0.4134\n    ign_recall: 0.3282\n    evi_precision: 0.8208\n    evi_recall: 0.8131\n    n_predictions: 8191\n- exp_id: plan_016_llama_grpo_qlora\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    format_reward: 1\n    f1_reward: 0\n    ced_reward: 0\n    entropy: 0.28\n    final_step: 60\n    grad_norm: 0\n    loss: 0\n    frac_reward_zero_std: 1\n    output_length_final: 172\n    conclusion_note: 'C2 cross-family validated: LLaMA QLoRA GRPO shows same catastrophic\n      decoupling as Qwen (format gaming, zero IE ability)'\n- exp_id: plan_006_qwen3_8b_rsft_candidates\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan_006_qwen3_1_7b_rsft_candidates\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan_016_llama_rsft_candidates\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_007_redocred_rsft_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_016_llama_rsft_candidates_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    docs_completed: 64\n    docs_total: 3027\n    lines_generated: 512\n    output_path: /root/autodl-tmp/freige/outputs/rsft_candidates_llama_8b/generations.jsonl\n    failure_reason: Process killed externally (no traceback/error in log). Likely\n      OOM on cuda:1. Completed 64/3027 docs (2.1%) in ~23min before termination.\n- exp_id: plan_014_no_evidence_eval_d076\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan_016_llama_rsft_candidates_r3\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T16:08:44.016Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T16:08:44.016Z",
  "sessionId": "48d76cf1-72e3-441d-8555-787b4ba2f406"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T16:08:44.039Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Test set 大幅退化暴露 dev 过拟合，DREEAM-protocol 对齐不利，post-hoc retrieval 追平 RSFT——方法贡献不成立，需 reframe 为 empirical analysis paper
核心假设：['Test set Ign-F1 退化 > 4pp（RSFT CED test < 41.5），且 evidence tax 扩大至 > 5pp', 'DREEAM-protocol Evi-F1 < 0.35，conditional evi_f1=0.81 在严格协议下大幅缩水', 'EDCR 与人工标注 Spearman ρ < 0.40，指标有效性无法充分验证', 'Post-hoc retrieval evi_f1 达到 0.75-0.85，与 RSFT 相当甚至超越，端到端生成无优势', '部分 scaling 实验失败（1.7B/8B RSFT candidates OOM 或结果不一致），U-shape 仅有 SFT 数据支撑']
关键指标范围：{'test_ign_f1_rsft_best': [38.0, 41.5], 'test_ign_f1_no_evidence': [42.0, 45.0], 'test_evidence_tax_4b': [-7.0, -4.0], 'dreeam_protocol_evi_f1': [0.2, 0.35], 'edcr_human_spearman_rho': [0.15, 0.4], 'posthoc_retrieval_evi_f1': [0.75, 0.85], 'expected_reviewer_avg': [2.5, 3.0]}
叙事方向：完全 reframe 为 empirical analysis paper。 标题改为分析导向："The Cost of Faithfulness: What Happens When LLMs Must Justify Their Extractions"。 主贡献重排序：(1) evidence-grounded DocRE 任务定义 + evaluation framework（EDCR 是首个尝试， 即使 human correlation 不够强也有开创价值）； (2) decoupling spectrum 作为 RL-for-IE 的警示性发现（negative result 的价值—— optimization pressure 系统性损害 multi-objective 平衡）； (3) U-shape evidence tax 作为 scaling 实证分析（仅 SFT-level 也够写）。 RSFT 不再定位为推荐方案，而是 "least harmful training strategy we found"。 去掉所有 effective/competitive 措辞，改用 reveals/exposes/characterizes。 Post-hoc retrieval 追平 RSFT 变成 paper 的一部分："simple retrieval matches  end-to-end generation, further questioning the cost-benefit of evidence production"。 仍投 EMNLP Main（analysis paper 在 EMNLP 有传统，Findings 也可接受）， 同时准备 AAAI 2027 作为同等 fallback。

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
tier: worst
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
  "promptId": "4c4715d1-0a53-4a22-abf4-c9288bffb2ff",
  "type": "user",
  "uuid": "727473bc-360d-448f-88d2-9152efe02c44",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "48d76cf1-72e3-441d-8555-787b4ba2f406",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T16:08:44.037Z_

```json
{
  "parentUuid": "727473bc-360d-448f-88d2-9152efe02c44",
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
  "uuid": "f32e633a-bbb0-4d5f-876c-49ff1044493f",
  "timestamp": "2026-05-16T16:08:44.037Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "48d76cf1-72e3-441d-8555-787b4ba2f406",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T16:08:44.037Z_

```json
{
  "parentUuid": "f32e633a-bbb0-4d5f-876c-49ff1044493f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "01ebbea7-f67b-42d5-b463-fad3117e3560",
  "timestamp": "2026-05-16T16:08:44.037Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "48d76cf1-72e3-441d-8555-787b4ba2f406",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Test set 大幅退化暴露 dev 过拟合，DREEAM-protocol 对齐不利，post-hoc retrieval 追平 RSFT——方法贡献不成立，需 reframe 为 empirical analysis paper 核心假设：['Test set Ign-F1 退化 > 4pp（RSFT…",
  "leafUuid": "01ebbea7-f67b-42d5-b463-fad3117e3560",
  "sessionId": "48d76cf1-72e3-441d-8555-787b4ba2f406"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evidence-grounded DocRE under worst-case scenario",
  "sessionId": "48d76cf1-72e3-441d-8555-787b4ba2f406"
}
```

---

### Assistant

_source line 8 · 2026-05-16T16:09:23.389Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment_plan, under the "worst" tier scenario. Let me identify which experiments are still "planned" (status: planned) from the experiment_plan:

1. plan_002 - Test set evaluation (status: planned)
2. plan_007 - Re-DocRED cross-dataset (status: planned) - though D080 says it's done, the plan status says planned. Let me check... the plan says "status: planned" but in the paper_framing it says "D080 完成". Let me look more carefully.


3. plan_013 - EDCR 人工标注验证 (status: planned)
4. plan_010 - NLI model ablation (status: planned)

I should also note there are several running experiments in the registry that might be relevant to consider, including some Qwen and Llama model evaluations currently in progress.

Now I'm defining what constitutes worst-case performance for each of these planned experiments: a significant degradation in test set performance with expanded evidence penalties, substantial drops in evidence F1 under strict evaluation protocols, poor correlation between EDCR metrics and human annotations, and post-hoc retrieval matching or exceeding the end-to-end generation approach.

There's also the risk that some of the scaling experiments fail due to memory constraints or produce inconsistent results, leaving the U-shaped pattern supported only by the SFT baseline data. I'm mapping out the specific metric ranges I'd expect to see in this worst-case scenario across all the key measurements.

Now I'm planning the core experiments: the test set evaluation shows a significant drop in performance compared to dev, with Ign-F1 falling by over 4 percentage points, while the no-evidence baseline also degrades substantially. For the cross-dataset evaluation on Re-DocRED, I have partial results already showing a 3.15pp decline in Ign-F1, though the evidence F1 remains relatively strong at 0.817.

Looking at the remaining planned work, the RSFT component on Re-DocRED is still pending and could fail entirely in the worst case. The human validation experiment for EDCR might show weak correlation with human judgments below 0.40, and the NLI ablation with DeBERTa-large may not yield meaningful improvements over the base model. I should also account for some implicit experiments like the post-hoc retrieval baseline and the DREEAM-protocol evidence F1 alignment that aren't formally tracked yet.

The running experiments with larger model candidates are concerning—the 1.7B and 8B RSFT variants risk running out of memory or producing unstable results, and the LLaMA RSFT attempts have already failed.

Now I'm identifying which experiments actually have "planned" status in the experiment plan versus those mentioned in priorities but without formal plan IDs, so I can give comprehensive predictions for everything that's still in progress.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01ebbea7-f67b-42d5-b463-fad3117e3560",
  "isSidechain": false,
  "requestId": "req_011Cb6Y8LwNfvmX7j1qzBiDD",
  "type": "assistant",
  "uuid": "ac8519b4-3b70-4b5c-b7b4-dc1ecc4b9272",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "48d76cf1-72e3-441d-8555-787b4ba2f406",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XGqtt5NYBt4gUM32KQj93X",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 37015,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11841,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 37015,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11841,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 37015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 37015
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

_source line 9 · 2026-05-16T16:12:33.593Z_

```yaml
tier: worst
narrative_guidance: >
  完全 reframe 为 empirical analysis paper。标题改为 "The Cost of Faithfulness: What Happens When LLMs Must Justify Their Extractions"。
  RSFT 不再定位为推荐方案，而是 "least harmful training strategy we found"。
  Post-hoc retrieval 追平 RSFT 变成论文正文的一部分。
  去掉所有 effective/competitive 措辞，改用 reveals/exposes/characterizes。
  仍投 EMNLP Main（analysis paper 传统），Findings 可接受，同时准备 AAAI 2027 fallback。

imagined_experiments:
  - name: "Test Set Evaluation (RSFT CED best + SFT baselines)"
    plan_id: "plan_002"
    description: >
      用 RSFT CED best config (s43/s44) 和 SFT baseline/no-evidence 在 DocRED test set 上评估。
      提交 CodaLab 获得官方 Ign-F1/F1，本地计算 Evi-F1 和 EDCR。
    expected_results:
      test_ign_f1_rsft_ced_s43: 40.2
      test_f1_rsft_ced_s43: 41.0
      test_ign_f1_rsft_ced_s44: 39.8
      test_f1_rsft_ced_s44: 40.5
      test_evi_f1_rsft_ced_s43: 0.798
      test_evi_f1_rsft_ced_s44: 0.793
      test_edcr_rsft_ced_s43: 0.672
      test_ign_f1_sft_baseline: 35.8
      test_ign_f1_sft_no_evidence: 42.5
      test_evidence_tax_4b: -6.7
      dev_test_gap_rsft_best: -5.65
      dev_test_gap_sft_no_evidence: -4.86
    result_rationale: >
      Worst 档核心假设：dev→test 退化 > 4pp。Dev best RSFT CED s43 Ign-F1=45.85，退化 5.65pp 至 40.2——
      这在 DocRED 上并非不可能。DocRED test set 由不同标注者标注且标注一致性低于 dev（Re-DocRED 论文已指出），
      RSFT 通过 CED scoring 对 dev-aligned 的 gold evidence pattern 进行了隐式过拟合：
      CED scorer 训练于 NLI 数据但在 DocRED dev gold 上筛选 RSFT 数据，筛选偏好与 dev 标注风格高度耦合。
      Test set 标注风格偏移导致 RSFT 增益大幅缩水（从 dev +5.5pp 缩至 test +4.4pp over SFT），
      而 SFT no-evidence 作为更简单的目标函数，dev→test 退化相对较小。
      Evidence tax 从 dev 的 -7.9pp 扩大至 test 的 -6.7pp（SFT no-evidence 42.5 vs SFT baseline 35.8），
      暴露 evidence generation 在 test distribution 下的负担更重。
      关键叙事影响：RSFT test Ign-F1 < 41.5 使 "RSFT 显著优于 SFT" 的必要条件仍满足（+4.4pp），
      但绝对数字太低（40.2 vs encoder SOTA >60），且 evidence tax 扩大使方法贡献可信度下降。
    tables:
      - name: "Table: Test Set Results"
        columns: ["Config", "Test Ign-F1", "Test F1", "Test Evi-F1", "Δ vs SFT", "Δ dev→test"]
        rows:
          - ["SFT no-evidence", "42.5", "43.8", "—", "+6.7", "-4.86"]
          - ["SFT baseline", "35.8", "36.5", "0.782", "—", "-4.56"]
          - ["RSFT CED s43", "40.2", "41.0", "0.798", "+4.4", "-5.65"]
          - ["RSFT CED s44", "39.8", "40.5", "0.793", "+4.0", "-5.71"]
          - ["RSFT flat-NLI s42", "39.5", "40.2", "0.790", "+3.7", "-4.99"]
    figures_description:
      - "Dev vs Test 退化散点图：x 轴 dev Ign-F1，y 轴 test Ign-F1，标注各 config。所有点落在 y=x 线以下，RSFT 偏离最大。"
    analysis: >
      Test set 退化 5.65pp 是 worst 档的核心打击。这暴露了两个问题：
      (1) CED scoring 在 RSFT 数据筛选时对 dev gold evidence 的隐式过拟合——test set 标注者偏好不同的 evidence 句子组合；
      (2) Evidence generation 的代价在 test distribution 下更严重（tax 从 -7.0 扩大至 -6.7pp）。
      但 RSFT 仍显著 > SFT baseline (+4.4pp)，且 evidence 质量保持（test evi_f1=0.798 vs dev 0.816，仅 -1.8pp）。
      论文叙事调整：不再声称 "RSFT 是 competitive 方案"，改为 "RSFT 是我们发现的 least harmful training strategy，
      但 dev-test gap 警示 evidence-grounded IE 的评估需要更稳健的 held-out 设计"。
      Evidence tax 扩大成为论文的 empirical finding 之一——进一步支撑 "cost of faithfulness" 叙事。

  - name: "Re-DocRED Cross-Dataset RSFT Evaluation"
    plan_id: "plan_007"
    description: >
      在 Re-DocRED 上对当前 best RSFT config 做完整 eval。
      D080 已有 SFT 结果（Ign-F1 下降 3.15pp，Evi-F1=0.817），此处预测 RSFT 在 Re-DocRED 上的表现。
    expected_results:
      redocred_rsft_ced_ign_f1: 38.1
      redocred_rsft_ced_evi_f1: 0.801
      redocred_rsft_ced_edcr: 0.695
      redocred_sft_ign_f1: 36.59
      redocred_rsft_vs_sft_delta: 1.5
      redocred_rsft_vs_docred_rsft_delta: -7.75
      redocred_no_evidence_ign_f1: 41.8
      redocred_evidence_tax: -5.2
    result_rationale: >
      Re-DocRED 修正了 DocRED 的大量 false negative（~55% triples 无 evidence 标注），
      RSFT 的 CED scoring function 在 DocRED gold 上训练的筛选偏好在 Re-DocRED 上适配性降低。
      具体而言：RSFT 在 DocRED dev 上的 +5.5pp 增益来自 CED 对 DocRED 标注风格的精准匹配，
      Re-DocRED 标注更完整但 evidence 分布不同，导致 RSFT 增益缩水至 +1.5pp。
      更关键的是，Re-DocRED 的 evaluation 中有 55% triples 无 evidence gold——
      这些 triples 上 RSFT 生成的 evidence 无法被评估，但生成负担仍在，导致 evidence tax 显著扩大。
      Evi-F1 保持在 0.801（仅在有 evidence 标注的子集上评估），与 D080 SFT 的 0.817 接近但略降。
      这表明 evidence extraction 能力本身跨数据集泛化，但 RSFT 的 relation extraction 增益不泛化。
    tables:
      - name: "Table: Re-DocRED Cross-Dataset Results"
        columns: ["Config", "Re-DocRED Ign-F1", "Re-DocRED Evi-F1", "Δ vs DocRED"]
        rows:
          - ["SFT baseline", "36.59", "0.817", "-3.15pp"]
          - ["SFT no-evidence", "41.8", "—", "—"]
          - ["RSFT CED", "38.1", "0.801", "-7.75pp vs DocRED RSFT"]
          - ["Evidence tax", "-5.2pp", "—", "vs DocRED -7.9pp"]
    figures_description:
      - "DocRED vs Re-DocRED 性能对比柱状图：蓝色 DocRED，红色 Re-DocRED，分 SFT/RSFT/no-evidence 三组"
    analysis: >
      RSFT 在 Re-DocRED 上增益大幅缩水（+1.5pp vs DocRED +5.5pp）暴露了 CED scoring 的 dataset-specificity。
      但 evidence 质量跨数据集保持（evi_f1 0.801）是 positive signal——说明 evidence extraction 能力本身泛化，
      问题出在 CED-filtered RSFT 训练数据对 DocRED 标注分布的过拟合。
      在 worst 叙事下，这成为 "RSFT 增益依赖于 scoring function 与 gold 分布的匹配度" 的 empirical warning。
      论文定位：Re-DocRED 结果不支撑 RSFT 作为通用方案，但支撑 evidence extraction 的跨数据集鲁棒性。

  - name: "EDCR Human Annotation Validation"
    plan_id: "plan_013"
    description: >
      100 个样本人工标注，判断每个 cited evidence sentence 是否真正支持对应 relation。
      计算 EDCR 与人工判断的 Spearman 相关性。
    expected_results:
      n_annotated_samples: 100
      annotator_agreement_kappa: 0.52
      edcr_human_spearman_rho: 0.31
      edcr_human_spearman_p: 0.0018
      edcr_human_pearson_r: 0.27
      human_evi_precision: 0.72
      human_evi_recall: 0.58
      false_positive_evidence_rate: 0.28
      edcr_identifies_bad_cases: true
      edcr_magnitude_calibration: poor
    result_rationale: >
      Worst 档假设 EDCR-human ρ < 0.40。根本原因是 EDCR 基于 NLI model（DeBERTa）的 entailment 判断，
      而人工标注者对 "evidence supports relation" 的判断标准与 NLI entailment 有系统性偏差：
      (1) NLI 模型对间接证据（需要推理链的 evidence）给出低分，但人工标注者认为这些仍是有效证据；
      (2) NLI 模型对表面相关但逻辑不充分的 evidence 给出高分（lexical overlap bias），人工标注者识别出不充分性。
      ρ=0.31 统计显著（p<0.002）但实际意义有限——仅解释约 10% 的方差。
      EDCR 在方向上有效（高 EDCR 的样本确实更可能有问题），但在绝对值上校准不良（EDCR=0.7 和 EDCR=0.8 的人工质量差异不显著）。
      标注者一致性 κ=0.52 本身就不高，反映了 evidence sufficiency 判断的固有主观性——
      这限制了任何自动指标与人工判断的相关性上界。
    tables:
      - name: "Table: EDCR Human Validation"
        columns: ["Metric", "Value", "95% CI"]
        rows:
          - ["Spearman ρ (EDCR vs human)", "0.31", "[0.12, 0.48]"]
          - ["Pearson r (EDCR vs human)", "0.27", "[0.08, 0.44]"]
          - ["Annotator κ", "0.52", "[0.40, 0.64]"]
          - ["Human evidence precision", "0.72", "[0.65, 0.79]"]
          - ["False positive rate (NLI)", "0.28", "[0.19, 0.37]"]
    figures_description:
      - "散点图：x 轴 EDCR score，y 轴 human evidence quality score（5-point scale），标注 95% CI band。弱正相关可见但散布大。"
      - "混淆矩阵：EDCR 二值化（>0.7 = decoupled）vs 人工判断（evidence insufficient）的 2×2 矩阵"
    analysis: >
      ρ=0.31 不足以支撑 EDCR 作为可靠的自动评估指标，但在 worst 叙事下可 reframe 为：
      "EDCR 是首个尝试量化 evidence-extraction decoupling 的自动指标，人工验证显示其方向有效但校准不足——
      这本身是 evaluation 方法论的 open problem，EDCR 的局限性反映了 evidence sufficiency 判断的固有难度。"
      关键：ρ=0.31 仍统计显著，且 EDCR 在方法级诊断（Claim 4 Layer 1, ρ=-0.965 vs rel_f1）的价值不受影响——
      因为那是 aggregate level 相关性，不依赖 per-sample 人工校准。
      论文策略：降级 EDCR 的 per-sample 可靠性声称，保留方法级诊断价值，在 Limitations 中诚实报告 ρ=0.31。

  - name: "DREEAM-Protocol Evidence F1 Alignment"
    plan_id: "D041 (implicit, P0)"
    description: >
      将 FREIGE 的 evidence evaluation 对齐到 DREEAM 的严格 evidence protocol——
      DREEAM 要求 evidence 与 gold 的 exact sentence index match，而 FREIGE 当前用 conditional evi_f1（NLI-based soft match）。
      对齐后重新计算所有方法的 Evi-F1。
    expected_results:
      dreeam_protocol_evi_f1_rsft_ced: 0.28
      dreeam_protocol_evi_f1_sft: 0.22
      dreeam_protocol_evi_f1_grpo_bf16: 0.25
      conditional_evi_f1_rsft_ced: 0.816
      conditional_to_dreeam_shrinkage: 0.66
      dreeam_baseline_evi_f1: 0.5401
      freige_vs_dreeam_gap: -0.26
    result_rationale: >
      Worst 档假设 DREEAM-protocol Evi-F1 < 0.35。这是因为 FREIGE 的 evidence 是 generative 的——
      LLM 生成的 evidence 文本与 gold sentence 的字面匹配率远低于 DREEAM 的 discriminative retrieval。
      具体机制：(1) FREIGE 生成的 evidence 可能 paraphrase 原文句子而非精确引用，DREEAM protocol 要求 exact sentence index match 会惩罚 paraphrase；
      (2) FREIGE 可能合并多个句子为一个 evidence 段落，DREEAM 按单句评估会漏计；
      (3) FREIGE 的 conditional evi_f1=0.81 基于 NLI soft match（entailment score > threshold），
      切换到 exact match 后 shrinkage 约 66%——从 0.81 降至 0.28。
      这直接导致 FREIGE 在 DREEAM 协议下 Evi-F1(0.28) << DREEAM baseline(0.54)，
      使得 "FREIGE 生成可验证证据" 的 Claim 1 在严格协议下不成立。
      但 FREIGE 的 evidence 在语义上是合理的（conditional evi_f1=0.81 通过 NLI 验证），
      问题在于 evaluation protocol 的不匹配——generative evidence 与 extractive evidence 需要不同的评估标准。
    tables:
      - name: "Table: Evidence Evaluation Protocol Comparison"
        columns: ["Method", "Conditional Evi-F1 (NLI)", "DREEAM-Protocol Evi-F1 (Exact)", "Shrinkage"]
        rows:
          - ["DREEAM (RoBERTa-large)", "—", "0.5401", "—"]
          - ["FREIGE SFT", "0.798", "0.22", "-72%"]
          - ["FREIGE RSFT CED", "0.816", "0.28", "-66%"]
          - ["FREIGE GRPO bf16", "0.809", "0.25", "-69%"]
    figures_description:
      - "双柱对比图：conditional evi_f1（蓝色）vs DREEAM-protocol evi_f1（红色），直观展示 shrinkage"
    analysis: >
      DREEAM-protocol 下 Evi-F1=0.28 是 worst 档的关键打击之一。论文必须：
      (1) 报告两种 protocol 的数字，诚实展示 shrinkage；
      (2) 论证 conditional evi_f1（NLI-based）更适合评估 generative evidence——因为 generative model 不受限于原文句子；
      (3) 在 Limitations 中承认缺乏公认的 generative evidence evaluation standard 是该研究方向的 open problem。
      这实际上加强了 analysis paper 的叙事："我们不仅发现 evidence generation 有代价（evidence tax），
      还发现当前评估框架无法公平比较 generative 与 extractive evidence——这本身是值得报告的发现。"

  - name: "Post-hoc Evidence Retrieval Baseline"
    plan_id: "P1 (implicit, no formal plan_id)"
    description: >
      SFT no-evidence 模型生成 relation triples 后，用 BM25 从原文中检索 top-k evidence sentences。
      对比 RSFT 的端到端 evidence generation。
    expected_results:
      posthoc_rel_f1: 0.4893
      posthoc_rel_ign_f1: 0.4736
      posthoc_evi_f1_conditional: 0.79
      posthoc_evi_f1_bm25_top3: 0.82
      posthoc_edcr: 0.625
      rsft_ced_evi_f1: 0.816
      posthoc_vs_rsft_evi_f1_delta: +0.004
      posthoc_vs_rsft_rel_f1_delta: +0.033
      posthoc_inference_overhead_pct: 5
    result_rationale: >
      Worst 档假设 post-hoc retrieval evi_f1 达到 0.75-0.85，与 RSFT 相当甚至超越。
      机制：SFT no-evidence 模型的 rel_f1=0.4893 已是最高（无 evidence generation 负担），
      BM25 检索利用 relation triple 中的 entity names 作为 query，在 DocRED 文档中检索包含这些 entities 的句子——
      这种策略在 DocRED 上天然有效，因为 DocRED 文档平均只有 8 个句子，entity co-occurrence 是强 evidence signal。
      BM25 top-3 检索的 evi_f1=0.82 略高于 RSFT 的 0.816，因为：
      (1) BM25 直接利用 gold relation 中的 entity pair 做精准检索，命中率高；
      (2) RSFT 的 evidence generation 偶尔 paraphrase 或遗漏句子，BM25 更稳定。
      Combined（rel_f1=0.4893 + evi_f1=0.82）全面超越 RSFT（rel_f1=0.4569 + evi_f1=0.816），
      且推理开销仅增加 5%（BM25 检索 vs 长序列生成）。
      这直接挑战 RSFT 的方法贡献——简单的 post-hoc retrieval pipeline 用更低的复杂度达到了更好的结果。
    tables:
      - name: "Table: End-to-End Generation vs Post-hoc Retrieval"
        columns: ["Method", "rel_f1", "Evi-F1", "EDCR", "Inference Cost"]
        rows:
          - ["RSFT CED (end-to-end)", "0.4569", "0.816", "0.643", "1.0× (baseline)"]
          - ["SFT + BM25 top-3 (post-hoc)", "0.4893", "0.82", "0.625", "0.65× + BM25"]
          - ["CED reranker (inference-time)", "0.4864", "0.819", "0.616", "8× sampling"]
    figures_description:
      - "Pareto 图：x 轴 inference cost，y 轴 combined score（rel_f1 + evi_f1 harmonic mean），post-hoc retrieval 在 Pareto 前沿"
    analysis: >
      Post-hoc retrieval 追平/超越 RSFT 是 worst 档的核心打击——它否定了端到端 evidence generation 的方法贡献。
      在 reframed 叙事下，这成为论文的关键发现之一：
      "simple retrieval matches end-to-end generation, further questioning the cost-benefit of evidence production"。
      这实际上加强了 analysis paper 的 novelty——我们不仅发现 evidence generation 有代价（evidence tax），
      还发现这个代价可能完全没有必要（post-hoc retrieval 用更低成本达到相同效果）。
      论文策略：将 post-hoc retrieval 结果作为 "the null hypothesis that should have been tested first" 来呈现。

  - name: "NLI Model Ablation (DeBERTa-base vs large)"
    plan_id: "plan_010"
    description: >
      DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer 的对比。
    expected_results:
      deberta_base_ced_mean_margin: 0.48
      deberta_large_ced_mean_margin: 0.53
      deberta_base_rsft_rel_f1: 0.4569
      deberta_large_rsft_rel_f1: 0.4610
      delta_rel_f1: 0.004
      p_value_paired_t: 0.38
    result_rationale: >
      Worst 档下 NLI 模型能力差异对下游 RSFT 质量影响微乎其微（Δ=0.004, p=0.38 不显著）。
      原因：CED scoring 的 bottleneck 不在 NLI 模型精度，而在 evaluation protocol 本身——
      NLI entailment 与 evidence sufficiency 的 concept gap（如 plan_013 人工验证所暴露的 ρ=0.31）
      意味着更强的 NLI 模型只是更精确地测量了一个与 ground truth 弱相关的信号。
      base→large 提升的 0.05 margin 在 CED top-1 selection 时几乎不改变排序结果（95% 的 top-1 选择相同）。
      这进一步支持 D078 的结论：CED 和 flat-NLI 统计不可区分，NLI 模型规模也不可区分——
      说明 scoring function 的选择在 RSFT 中是 second-order effect，数据质量本身才是关键。
    tables:
      - name: "Table: NLI Model Ablation"
        columns: ["NLI Model", "CED Margin", "RSFT rel_f1", "RSFT evi_f1"]
        rows:
          - ["DeBERTa-v3-base", "0.48", "0.4569", "0.816"]
          - ["DeBERTa-v3-large", "0.53", "0.4610", "0.819"]
          - ["Δ (large - base)", "+0.05", "+0.004 (p=0.38)", "+0.003"]
    figures_description: []
    analysis: >
      NLI 模型 ablation 在 worst 档下进一步削弱 CED 的方法贡献——不仅 CED vs flat-NLI 不可区分（D078），
      连 NLI 模型规模都不影响结果。这收窄了 CED 的定位：从 "a principled scoring function" 降级为
      "any NLI-based filter works, and works similarly regardless of NLI model capacity"。
      论文处理：放入 Appendix 作为辅助 ablation，在正文中一句话带过。

  - name: "1.7B/8B RSFT Candidates Generation + Training (Scaling)"
    plan_id: "plan_006 (RSFT part, currently RUNNING)"
    description: >
      Qwen3-1.7B 和 Qwen3-8B 上生成 RSFT candidates → CED scoring → RSFT training → eval。
      目前 candidates generation 正在 RUNNING。
    expected_results:
      qwen3_1_7b_rsft_candidates_generated: 15000
      qwen3_1_7b_rsft_ced_selected: 1800
      qwen3_1_7b_rsft_ign_f1: null
      qwen3_1_7b_rsft_status: "OOM during training or candidate quality too low (mean_f1 < 0.3)"
      qwen3_8b_rsft_candidates_generated: 20000
      qwen3_8b_rsft_ced_selected: 3200
      qwen3_8b_rsft_ign_f1: 52.8
      qwen3_8b_rsft_evi_f1: 0.825
      qwen3_8b_rsft_vs_sft_delta: 2.3
      qwen3_8b_evidence_tax_after_rsft: -0.5
    result_rationale: >
      Worst 档假设 "部分 scaling 实验失败（1.7B/8B RSFT candidates OOM 或结果不一致），U-shape 仅有 SFT 数据支撑"。
      1.7B RSFT 失败的机制：1.7B 模型生成的 candidates 质量太低（SFT 本身 Ign-F1=47.86 但 generation diversity 差，
      小模型倾向于重复同样的 relation set），CED scoring 后仅 1800 样本通过阈值（vs 4B 的 2718），
      且 mean_f1=0.28（vs 4B 的 0.62）——数据质量不足以支撑有效的 RSFT 训练。
      训练过程中可能 OOM（1.7B + RSFT data 在 bf16 下勉强跑通，但 gradient accumulation 不稳定），
      或即使完成训练也因数据质量差导致 RSFT 退化至 SFT baseline 甚至以下。
      8B RSFT 成功但增益远小于 4B（+2.3pp vs +5.5pp）——8B SFT 已足够强（Ign-F1=50.51），
      RSFT 的 marginal value 在大模型上递减。U-shape pattern 在 RSFT 层面无法复现。
    tables:
      - name: "Table: Scaling RSFT Results"
        columns: ["Model", "SFT Ign-F1", "RSFT Ign-F1", "Δ RSFT-SFT", "Status"]
        rows:
          - ["Qwen3-1.7B", "47.86", "—", "—", "FAILED (low candidate quality)"]
          - ["Qwen3-4B", "40.36", "45.85", "+5.49", "SUCCESS"]
          - ["Qwen3-8B", "50.51", "52.8", "+2.3", "SUCCESS (diminishing returns)"]
    figures_description:
      - "U-shape 图标注：SFT-level evidence tax 数据点完整（4 个），RSFT-level 仅有 4B 和 8B 两个数据点（1.7B 缺失），U-shape 在 RSFT 层面不成立"
    analysis: >
      1.7B RSFT 失败意味着 U-shape pattern 仅在 SFT 层面成立，无法推广到 RSFT。
      这削弱了 Claim 5 的叙事完整性——"evidence tax 是 scale-dependent 的" 只有 SFT 数据支撑，
      RSFT 作为推荐方法在小模型上不 work。
      论文处理：诚实报告 1.7B RSFT 失败，将 U-shape 定位为 "SFT-level empirical observation"
      而非 "general scaling law"。在 Discussion 中讨论小模型 RSFT 失败的 candidate quality bottleneck。

  - name: "LLaMA-3.1-8B RSFT Candidates + Training (Cross-family)"
    plan_id: "plan_016 (RSFT part, currently RUNNING r3)"
    description: >
      LLaMA-3.1-8B 上生成 RSFT candidates → CED scoring → RSFT training。
      r1/r2 已失败（OOM），r3 正在 RUNNING。
    expected_results:
      llama_rsft_candidates_status: "partial completion (~40-60% docs) then OOM kill"
      llama_rsft_candidates_generated: 12000
      llama_rsft_training_status: "not reached (blocked by candidate generation failure)"
      llama_rsft_ign_f1: null
      llama_sft_ign_f1: 53.84
      llama_no_evidence_ign_f1: 54.52
      llama_evidence_tax: -0.68
      llama_grpo_qlora_status: "catastrophic (confirmed)"
    result_rationale: >
      LLaMA RSFT candidates generation 已连续失败两次（r1: failed, r2: 64/3027 docs 后 OOM killed）。
      根本原因：LLaMA-3.1-8B 的 memory footprint 比 Qwen3 系列更大（不同的 attention 实现 + vocabulary size 差异），
      在当前 GPU 上生成 8 个 candidates per doc 时 peak memory 超出限制。
      r3 可能在完成 40-60% 的 docs 后再次 OOM——即使生成了部分 candidates，
      样本量不足以训练有效的 RSFT（需要 >2000 selected samples，40% docs 可能只产出 ~1000）。
      这意味着 cross-family RSFT validation 完全缺失——只有 SFT-level 的 evidence tax 数据（-0.68pp）
      和 GRPO QLoRA 的 catastrophic decoupling 确认。
      论文叙事影响：LLaMA 数据退化为 "SFT + GRPO 两个极端"，缺少 RSFT 中间路线的跨家族验证。
    tables:
      - name: "Table: LLaMA Cross-Family Validation (Incomplete)"
        columns: ["Experiment", "Status", "Result"]
        rows:
          - ["LLaMA SFT (evidence)", "DONE ✅", "Ign-F1=53.84, Evi-F1=0.8151"]
          - ["LLaMA SFT (no-evidence)", "DONE ✅", "Ign-F1=54.52"]
          - ["LLaMA GRPO QLoRA", "DONE ✅", "Catastrophic (f1_reward=0)"]
          - ["LLaMA RSFT CED", "FAILED ❌", "OOM during candidate generation"]
    figures_description: []
    analysis: >
      LLaMA RSFT 失败是 worst 档的特征之一——跨家族验证在 RSFT 层面不成立。
      论文只能报告 LLaMA SFT evidence tax = -0.68pp（与 Qwen-8B 一致确认 8B neutral），
      以及 GRPO QLoRA catastrophic decoupling 跨家族成立。
      RSFT 作为 "推荐方案" 缺乏跨家族证据——这在 reframed 叙事下影响较小
      （RSFT 已降级为 "least harmful"，不再是核心推荐），但在 Limitations 中必须诚实报告。

  - name: "Integrated Worst-Tier Reviewer Simulation"
    plan_id: "N/A (meta-analysis)"
    description: >
      综合所有 worst 档实验结果，模拟 EMNLP 审稿人的反应和预期评分。
    expected_results:
      expected_reviewer_1_score: 2.5
      expected_reviewer_2_score: 3.0
      expected_reviewer_3_score: 3.0
      expected_meta_reviewer: "borderline reject"
      expected_avg_score: 2.83
      acceptance_probability_main: 0.10
      acceptance_probability_findings: 0.35
    result_rationale: >
      Reviewer 1（methods-focused）给 2.5：test 退化 > 4pp、post-hoc retrieval 追平 RSFT、
      DREEAM-protocol Evi-F1 仅 0.28——方法贡献不成立，"为什么不直接用 BM25？"。
      Reviewer 2（analysis-focused）给 3.0：认可 decoupling spectrum 发现的 novelty（"genuinely striking"），
      认可 evidence tax scaling 的 empirical 价值，但指出 1.7B RSFT 失败和 EDCR human ρ=0.31 削弱了完整性。
      Reviewer 3（evaluation-focused）给 3.0：认可 evaluation framework 的开创性尝试（EDCR 首次提出），
      但对 conditional vs DREEAM-protocol 的 shrinkage 不满意，要求更公平的 generative evidence evaluation。
      Meta-reviewer 判断 borderline reject：analysis contributions 有价值但不够 main conference 水平，
      建议投 Findings。
    tables:
      - name: "Table: Anticipated Reviewer Scoring Breakdown"
        columns: ["Reviewer", "Score", "Key Concern", "Key Positive"]
        rows:
          - ["R1 (Methods)", "2.5", "Post-hoc retrieval negates method contribution", "Decoupling spectrum is novel"]
          - ["R2 (Analysis)", "3.0", "1.7B RSFT failure, incomplete scaling story", "Evidence tax U-shape is valuable empirical finding"]
          - ["R3 (Evaluation)", "3.0", "DREEAM-protocol Evi-F1=0.28, EDCR ρ=0.31", "First attempt at evidence-grounded DocRE evaluation"]
    figures_description: []
    analysis: >
      Worst 档下论文最可能的结局：EMNLP Main reject（avg 2.83），Findings 有 35% 概率。
      如果投 Findings 被接受，需要在 camera-ready 中：
      (1) 完全删除 "method contribution" 叙事，纯 empirical analysis；
      (2) 将 post-hoc retrieval 追平 RSFT 作为核心 negative result 呈现；
      (3) 将 EDCR 定位为 "preliminary diagnostic tool" 而非 "validated metric"。
      AAAI 2027 作为 fallback 更合适——AAAI 对 empirical analysis 和 negative results 接受度历来高于 EMNLP，
      且有额外 2 个月补充 1.7B RSFT 和改进 EDCR human correlation 的机会。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac8519b4-3b70-4b5c-b7b4-dc1ecc4b9272",
  "isSidechain": false,
  "requestId": "req_011Cb6Y8LwNfvmX7j1qzBiDD",
  "type": "assistant",
  "uuid": "ca934e0d-af1a-4ee2-96b9-5d6069770a0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "48d76cf1-72e3-441d-8555-787b4ba2f406",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XGqtt5NYBt4gUM32KQj93X",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 37015,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11841,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 37015,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11841,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 37015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 37015
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

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Test set 大幅退化暴露 dev 过拟合，DREEAM-protocol 对齐不利，post-hoc retrieval 追平 RSFT——方法贡献不成立，需 reframe 为 empirical analysis paper 核心假设：['Test set Ign-F1 退化 > 4pp（RSFT…",
  "leafUuid": "ca934e0d-af1a-4ee2-96b9-5d6069770a0d",
  "sessionId": "48d76cf1-72e3-441d-8555-787b4ba2f406"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evidence-grounded DocRE under worst-case scenario",
  "sessionId": "48d76cf1-72e3-441d-8555-787b4ba2f406"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Test set 大幅退化暴露 dev 过拟合，DREEAM-protocol 对齐不利，post-hoc retrieval 追平 RSFT——方法贡献不成立，需 reframe 为 empirical analysis paper 核心假设：['Test set Ign-F1 退化 > 4pp（RSFT…",
  "leafUuid": "ca934e0d-af1a-4ee2-96b9-5d6069770a0d",
  "sessionId": "48d76cf1-72e3-441d-8555-787b4ba2f406"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Evidence-grounded DocRE under worst-case scenario",
  "sessionId": "48d76cf1-72e3-441d-8555-787b4ba2f406"
}
```

---
