# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Test set 不 generalize 或 decoupling 跨家族不复现，核心 claim 需要 reframe 核心假设：['Test s

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/ec4f40cb-c4c9-433e-91d1-bac586606fad.jsonl`
- **Structured JSON:** [`bea5dc651454d5c87283.json`](../../sessions/be/bea5dc651454d5c87283.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T11:17:25.955Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T11:17:25.955Z",
  "sessionId": "ec4f40cb-c4c9-433e-91d1-bac586606fad",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Test set 不 generalize 或 decoupling 跨家族不复现，核心 claim 需要 reframe\n核心假设：['Test set RSFT vs SFT Δ < 2pp 或不显著（dev-test gap 大，可能因 DocRED test 分布偏移）', '或 LLaMA GRPO QLoRA 不出现 catastrophic decoupling（spectrum 变成 Qwen-specific）', 'CED vs flat-NLI 不显著（已是大概率事件）', '1.7B/8B 结果与 4B 方向不完全一致（evidence tax 在大模型消失或 RSFT 增益不稳定）', 'EDCR 人工验证偏低（ρ<0.5），部分 evidence 标注模糊导致指标可信度受质疑']\n关键指标范围：{'test_rsft_vs_sft_ign_f1_delta': [0.0, 2.0], 'ced_vs_flat_nli_p_value': [0.2, 0.8], 'ced_ign_f1_5seed_mean': [0.44, 0.45], 'flat_nli_ign_f1_5seed_mean': [0.44, 0.452], 'cross_model_rsft_sft_delta_min': [0.0, 2.0], 'llama_grpo_qlora_rel_f1': [0.1, 0.4], 'edcr_human_spearman': [0.3, 0.5], 're_docred_rsft_vs_sft_delta': [-1.0, 2.0]}\n叙事方向：Reframe 为分析/诊断贡献论文，不以 RSFT 方法性能为核心 claim。三个 reframe 方向（按优先级）：(1) 'Understanding the cost of faithfulness in generative IE'——evidence generation tax（7pp）+ 部分恢复的系统性分析，贡献在于量化了 faithfulness-performance trade-off 并提供 EDCR 作为诊断工具；(2) 'Why RL fails for multi-objective IE: an empirical study'——decoupling 即使只在 Qwen 上验证，作为 case study 仍有价值，重心转向 intra-task objective competition 的机制分析 + QLoRA amplification 现象；(3) 如果 Qwen-only 但数据充分，scope 收缩为 'model-specific' 发现但补充足够 ablation 深度（training dynamics, per-relation 分析, advantage variance）使单模型分析具独立价值。目标仍 EMNLP main（Findings track 可接受），不降级 venue。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: faith-evidence-ie\n\n## paper_framing.md\n\n# Paper Framing — FREIGE\n\n> **状态**: POST-MVP + DREAM v2 完成（D047 分析）\n> **最后更新**: 2026-05-16\n> **Dream v1**: best=2.5, median=3.0, worst=2.5 → reframe 完成\n> **Dream v2**: best=3.0, median=2.5, worst=2.5 → best 提升但 median 下降，未达标。关键路径：plan_011 bf16 GRPO eval + structural fixes → re-dream v3\n\n## Target Venue\n\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\n\n## Core Insight\n\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。\n\n我们系统性地探索了 online RL (GRPO) 、offline preference optimization (DPO) 和 offline RL (RSFT) 三条技术路线。关键发现：**RL optimization pressure 与 evidence-extraction decoupling severity 正相关**——优化强度越大，evidence 质量提升的同时抽取能力退化越严重。QLoRA 放大至 catastrophic（rel_f1<0.02），bf16 GRPO 从 0.4549 退化至 ~0.434（mild, -2pp），DPO 呈 gradual 退化（1ep→3ep rel_f1 从 0.4034→0.3429），RSFT 无 decoupling。\n\nCED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，通过文档内 hard negative 对比评估 evidence 质量。CED 作为 RSFT 的 scoring function 之一进行测试，其相对于 flat-NLI 的优势需要通过充分的统计检验验证。\n\n## Story Arc\n\n1. **Problem**: LLM DocRE 无证据 → 部署障碍\n2. **New task**: evidence-grounded DocRE — 同时生成关系和证据\n3. **Cost of faithfulness**: evidence generation 代价 ~7pp Ign-F1（no-evidence 47.36 vs evidence-SFT 40.36）——这是 faithfulness 的真实成本\n4. **Exploration**: 系统性比较 online RL (GRPO) vs offline preference (DPO) vs offline RL (RSFT)\n5. **Key finding**: evidence-extraction decoupling — RL optimization pressure 与 decoupling severity 正相关，形成连续谱系（GRPO-QLoRA catastrophic > GRPO-bf16 mild > DPO gradual > RSFT none）\n6. **QLoRA amplification**: QLoRA 量化将 mild decoupling 放大至 catastrophic forgetting——decoupling 是 RL-for-IE 中 multi-objective competition 的通用梯度（intra-task trade-off，非 inter-task forgetting），QLoRA 是 catastrophic amplifier\n7. **What works**: RSFT with NLI-based scoring 是唯一有效路线——提升 evidence 质量而不牺牲抽取\n8. **Best practical solution**: CED reranker 恢复 97% 的 evidence 代价，同时保留高质量 evidence（evi_f1=0.8188）\n9. **Diagnostic tool**: EDCR 双层诊断——方法级量化 decoupling（与 Claim 2 呼应），per-relation 级揭示 evi_f1 不捕捉的 relation-type 难度差异（D070 ✅）\n\n## Core Claims (reframed after Dream v1, updated D068/D069/D070/D071/D072)\n\n### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力\n- FREIGE 是首个**基于生成式 LLM** 的 evidence-grounded DocRE 方法（⚠️ 必须始终保持 \"generative LLM\" 限定词——SAIS 已做 encoder-based evidence retrieval + DocRE）\n- **关键区分 (Reviewer warning)**：encoder-based evidence *retrieval*（SAIS, DREEAM — 分类哪些句子是证据，evidence supervision 提升 RE）vs generative evidence *production*（FREIGE — LLM 生成证据文本，额外生成负担导致 ~7pp 代价）。论文 Related Work 必须精准讨论此对比，否则审稿人会问 \"为什么 SAIS 说 evidence 有用，你说 evidence 有害\"\n- **Evidence generation tax**: no-evidence SFT Ign-F1=47.36 vs evidence-SFT 40.36，代价 ~7pp（plan_014 ✅）\n- RSFT 在 4/4 配置下均超过 SFT baseline（Ign-F1 +3.3~5.5pp）\n- **CED reranker 是最优实用方案**: rel_f1=0.4864（仅低于 no-evidence 0.29pp），evi_f1=0.8188（plan_005 ✅）\n- 需要 DREEAM-protocol 对齐的 Evi-F1 对比（D041 在处理中）\n- **RSFT 方法论定位**：诚实承认 RSFT 是 STaR (NeurIPS 2022) 的单轮变体 + evidence quality scoring。创新点在于将 STaR-like self-improvement 应用于 evidence-grounded DocRE + CED/NLI 作为 domain-specific quality filter，而非框架本身\n- **Evaluation caveat** (Limitations): GenRES 指出 exact match F1 低估 generative RE，FREIGE 所有 eval 用 exact match，应承认此局限（对所有方法同等适用，相对比较有效）\n\n### Claim 2 (Core finding): RL optimization pressure 与 evidence-extraction decoupling severity 正相关（D068/D069 修正）\n- **Decoupling spectrum**: 优化强度越大，decoupling 越严重\n  - GRPO QLoRA: catastrophic（rel_f1=0.0138, evi_f1=0.850, EDCR=0.99）— QLoRA 放大 decoupling\n  - GRPO bf16: mild（rel_f1 从 0.4549→~0.434, -2pp; step_30=0.434, step_50=0.4276, step_70=0.4341）— 退化可控但持续（D065/D066）\n  - DPO bf16 1ep→3ep: gradual（Ign-F1 38.88→TBD, rel_f1 0.4034→0.3429）— 随训练渐进退化（D067/D068）\n  - RSFT: none — 无 decoupling，唯一有效路线\n- **QLoRA 是 catastrophic amplifier，不是 root cause**: bf16 GRPO 仅 mild decoupling（-2pp），QLoRA 放大至 catastrophic（-39pp）（D054/D065/D066）\n- **Decoupling 是 RL-for-IE 的通用梯度**: 跨方法（GRPO/DPO）、跨量化策略（QLoRA/bf16）一致出现，严重程度与优化压力正相关\n- 三档 Dream 审稿均认为此发现\\\"genuinely novel and striking\\\"\n- **已完成**: GRPO G=8 bf16 确认 mild decoupling（plan_011 ✅）; DPO 1ep/3ep 确认 gradual decoupling（plan_012 ✅）\n\n### Claim 3 (Ablation): NLI-based scoring 提升 RSFT 质量\n- CED 和 flat-NLI 都优于 random/no scoring\n- CED vs flat-NLI 的差异需统计验证（Dream 报告 p=0.08/0.38/0.12 不显著）\n- **Critical**: 如果 CED 不显著优于 flat-NLI → CED 降级为\"one possible scoring function\"\n- **行动**: 5+ seeds for significance testing\n- **top_k selection ablation (k=1 vs k=3)**:\n  - k=1 (best-of-8) 优于 k=3 (top3-of-8)，CED scoring precision 随 k 增大下降\n  - k=1 均值 (3 seeds s42/s43/s44): Ign-F1=45.00, rel_f1=0.4596, evi_f1=81.43, EDCR=0.6434\n  - k=3 (1 seed, reeval_rsft_topk3): Ign-F1=43.64, rel_f1=0.4454, evi_f1=80.88, EDCR=0.6635\n  - Δ (k=3 vs k=1 mean): Ign-F1 **-1.36pp**, rel_f1 **-1.42pp**, evi_f1 **-0.55pp**, EDCR +0.02\n  - 训练数据质量下降: k=1 mean_f1=0.6157, mean_ced=0.6683 → k=3 mean_f1=0.5761, mean_ced=0.6205（来源: mvp2_rsft_ced_scoring / mvp2_rsft_ced_scoring_topk3_r2）\n  - 训练集规模: k=1 选出 2718 样本 (12.4%), k=3 选出 8037 样本 (37%), 数据量 ×2.96 但质量下降抵消数量优势\n  - **叙事**: 低排名 response 引入噪声——rank 2-3 样本的 F1 和 CED 分数均显著低于 rank 1，扩大训练集规模无法补偿数据质量的稀释。这表明 RSFT 的关键不在数据量而在 scoring precision\n  - **注**: k=3 仅 1 seed，差异方向一致但尚不具备统计显著性；作为 ablation table 中的辅助行呈现，不作为独立 claim\n\n### Claim 4 (Diagnostic): EDCR 双层诊断价值（D070/D072）\n- **Layer 1 — 方法级**: EDCR 量化 evidence-extraction decoupling，与 Claim 2 spectrum 呼应\n  - 方法级 EDCR 与 rel_f1 Spearman ρ=-0.965（plan_003 ✅）——本质是 decoupling 的度量\n  - EDCR 识别病理模型（GRPO QLoRA: EDCR≈1.0）\n- **Layer 2 — per-relation-type**: EDCR 提供 evi_f1 不捕捉的 relation-type 诊断信息 ✅\n  - per-relation ρ(EDCR, evi_f1) = **-0.064** (p=0.58) → **完全独立于 evi_f1**\n  - per-relation ρ(EDCR, rel_f1) = -0.793 (p<0.001) → 与 rel_f1 强相关但非完美\n  - per-relation ρ(evi_f1, rel_f1) = -0.013 (p=0.91) → evidence 质量与抽取能力在 relation type 间完全解耦\n  - 典型案例：date_of_birth (EDCR=0.118, 高 faithful) vs head_of_government (EDCR=0.956, 高 decoupled)\n  - 93 relation types 分析（≥5 样本），76 个有非零数据\n- **论文叙事**: EDCR 在方法级是 decoupling 度量工具（横向对比方法），在 relation 级是难度诊断工具（纵向定位薄弱 relation）——两层叙事互补\n- **仍需**: 100 例人工标注验证（RC6）\n\n## MVP Evidence Summary (D071: 主表报 Ign-F1，附录报 F1)\n\n| Config | Ign-F1 | F1 | Δ vs SFT (Ign-F1) | Evi-F1 (cond) | Evi-F1 (joint) | EDCR |\n|--------|--------|------|-------------------|---------------|---------------|------|\n| **SFT no-evidence** | **47.36** | 48.93 | **+7.00pp** | **—** | **—** | **—** |\n| SFT baseline (noquant) | 40.36 | 41.06 | — | 80.13 | 31.17 | 0.7118 |\n| **CED reranker** | **TBD** | 48.64 | **TBD** | **81.88** | — | **0.6156** |\n| RSFT CED s43 (best) | **45.85** | 46.83 | **+5.49pp** | 81.56 | 37.11 | 0.6388 |\n| RSFT CED s44 | 45.51 | 46.55 | +5.15pp | 80.87 | 37.13 | 0.6350 |\n| RSFT CED s42 | 43.63 | 44.49 | +3.27pp | 81.87 | 34.68 | 0.6565 |\n| RSFT CED k=3 | 43.64 | 44.54 | +3.28pp | 80.88 | — | 0.6635 |\n| RSFT r2a (1ep) | 44.01 | 44.94 | +3.65pp | 81.08 | 35.09 | 0.6641 |\n| RSFT r2b (1ep) | 44.10 | 44.93 | +3.74pp | 81.28 | 34.90 | 0.6609 |\n| flat-NLI s42 | 44.49 | 45.39 | +4.13pp | 80.43 | — | 0.6431 |\n| flat-NLI s43 (reeval) | TBD | 45.23 | TBD | 81.58 | — | 0.6505 |\n| DPO bf16 1ep | 38.88 | 40.34 | -1.48pp | 80.88 | — | 0.7139 |\n| DPO bf16 3ep | TBD | 34.29 | TBD | — | — | — |\n| GRPO bf16 G=8 (best step) | 45.59 | ~43.4 | +5.23pp | 80.86 | — | — |\n| GRPO QLoRA (lr=5e-6) | TBD | 1.38 | TBD | 85.00 | — | 0.9900 |\n\n注：Evi-F1 以百分比显示（×100）。Ign-F1 修正后排名无实质变化（仅 r2a/r2b 互换，差 0.09pp）。TBD 项等待 metrics_v2.json 补算。GRPO bf16 Ign-F1=45.59 > F1=43.4 因 train triples 过滤效应。RSFT CED k=3 数据来源: reeval_rsft_topk3 (ign_f1_corrected=true)。\n\n## Anticipated Reviewer Concerns (updated from Dream, D068/D069)\n\n### RC1: \"Online RL\" 标题过度声称（Dream 三档一致 Critical）\n- ~~标题和 claim 收窄到 \"GRPO fails for DocRE\"~~\n- **D068/D069 修正**: 重新定位为 \"RL optimization pressure correlates with decoupling severity\"——不是 GRPO 特有问题，而是 RL-for-IE 的通用梯度\n- DPO 数据支撑 decoupling spectrum（gradual decay confirms the pattern）\n\n### RC2: GRPO G=4 太小 + LoRA confound（Dream 三档一致 Major）\n- GRPO G=8 bf16 实验 ✅ — 确认 mild decoupling（-2pp），QLoRA 是 catastrophic amplifier（D065/D066）\n- LoRA confound 已解决：bf16 LoRA vs QLoRA 直接对比\n\n### RC3: CED 不显著优于 flat-NLI（Dream 三档一致 Major）\n- 5+ seeds 统计检验；如不显著 → CED 降级\n\n### RC4: RSFT 不新颖\n- 不声称 RSFT 是贡献；贡献在于任务定义 + decoupling 发现 + EDCR\n- 诚实定位 RSFT 为 STaR (NeurIPS 2022) 单轮变体 + domain-specific quality filter\n\n### RC12: SAIS 说 evidence 有用，为何 FREIGE 说 evidence 有害？（文献审查 2026-05-16）\n- **关键区分**: discriminative evidence *retrieval*（SAIS/DREEAM — 分类句子是否为证据，作为监督信号提升 RE）vs generative evidence *production*（FREIGE — LLM 生成完整证据文本，额外生成负担导致 ~7pp 代价）\n- SAIS 的 evidence supervision 是分类任务，不增加输出长度；FREIGE 的 evidence generation 显著增加生成序列长度，模型需分配容量同时完成 RE + evidence 生成\n- **应对**: Related Work 中精准讨论此对比，明确 FREIGE 研究的是 *generative production* 设定下的代价，与 *retrieval* 设定下的增益不矛盾——两者揭示了 evidence 在不同范式下的不同角色\n\n### RC13: 单模型单数据集泛化性不足（D077 scope 扩展）\n- plan_006: Qwen3-1.7B / 8B model size ablation\n- plan_016: LLaMA-3.1-8B cross-family validation\n- plan_007: Re-DocRED cross-dataset evaluation\n\n### RC5: 评测可比性（D041）\n- DREEAM-protocol Evi-F1；conditional Evi-F1 作为辅助指标\n\n### RC6: EDCR 缺人工验证\n- 100 例小规模标注\n\n### RC7: Missing DPO/PPO（Dream 两档 Major）\n- DPO experiment ✅ — 结果确认 decoupling spectrum（D067/D068）\n\n### RC8: Dev-test degradation\n- 观察项，等 test set 数据\n\n### RC9: 连接 reward overoptimization 文献\n- 显式引用 Gao et al. 2023\n\n### RC10: Post-hoc evidence retrieval baseline\n- SFT + BM25 evidence retrieval\n\n### RC11: \"RL 不遗忘\" 文献与 Claim 2 的张力（文献扫描 2026-05-16）\n- 近期多篇论文（arXiv 2507.05386, 2506.23508, 2509.04259）论证 RL fine-tuning 天然缓解 catastrophic forgetting\n- **关键区分**: FREIGE 的 decoupling 是 **intra-task multi-objective trade-off**（RE 抽取 vs evidence 生成两个优化目标的竞争），不是 **inter-task forgetting**（丢失预训练知识）。两者机制不同\n- bf16 GRPO 的 mild decoupling（-2pp）恰好印证这一点：模型没有忘记\"怎么做 IE\"，而是在 evidence reward 压力下偏移了 RE-evidence 的资源分配\n- **应对**: Related Work / Discussion 中显式回应这组文献，区分 intra-task trade-off vs inter-task forgetting\n- **QuRL/QaRL 文献支撑 Claim 2**: QuRL 发现 quantized vs full-precision actor divergence 在长训练中指数增长（直接支撑 QLoRA amplification 叙事）；QaRL 的 error token failure mode 与 QLoRA GRPO garbled evidence 吻合\n\n## Key Baselines (12+)\n\n1. **SFT-only**: Qwen3-4B + LoRA SFT（with evidence）\n1b. **SFT no-evidence**: Qwen3-4B + LoRA SFT（无 evidence，upper bound ablation）\n2. **RSFT flat-NLI**: flat-NLI scored RSFT（核心 ablation）\n3. **RSFT CED**: CED scored RSFT（主方法）\n4. **CED-as-reranker**: 推理时 CED 重排（无训练）\n5. **DPO+CED**: offline preference learning — gradual decoupling（D067/D068）\n6. **GRPO+CED (QLoRA, G=4)**: catastrophic decoupling baseline\n7. **GRPO+CED (bf16, G=8)**: mild decoupling — QLoRA confound 排除（D065/D066）\n8. **Post-hoc retrieval**: SFT + BM25 evidence（NEW）\n9. **DREEAM**: encoder evidence SOTA\n10. **SAIS**: encoder evidence baseline\n11. **DocKS-RAG**: extraction SOTA（无 evidence）\n12. **LMRC**: generative LLM SOTA（无 evidence）\n\n## Publishability Threshold (revised after Dream, D068/D069)\n\n- **必要条件**: (1) RSFT 在 test set 上 Ign-F1 显著 > SFT (2) DREEAM-protocol Evi-F1 可报告 (3) Decoupling spectrum 有完整数据支撑（GRPO QLoRA/bf16 + DPO + RSFT）\n- **充分条件**: 上述 + CED 显著 > flat-NLI + EDCR 人工验证\n- **Failure pivot**: decoupling spectrum 不成立（bf16 GRPO 也 catastrophic）→ scope 大幅缩减。**已排除**: bf16 GRPO 确认 mild（D065/D066）\n\n## Research Phase Priorities (revised after Dream v1)\n\n| Priority | 实验 | Claim | GPU-h |\n|----------|------|-------|-------|\n| P0 | flat-NLI RSFT ablation (5 seeds) | C3 | ~25h |\n| P0 | CED RSFT additional seeds (→5 total) | C3 | ~10h |\n| P0 | DREEAM-protocol Evi-F1 对齐 | C1 | CPU |\n| P0 | Test set evaluation | C1 | ~4h |\n| P0 | DREEAM baseline reproduction | C1 | ~8h |\n| ~~P0~~ | ~~GRPO G=8 experiment~~ ✅ | C2 | ~16h |\n| ~~P0~~ | ~~DPO+CED experiment~~ ✅ | C2 | ~12h |\n| ~~P0~~ | ~~EDCR per-relation analysis (D070)~~ ✅ | C4 | CPU |\n| ~~P0~~ | ~~Ign-F1 bugfix + data sync (D071)~~ ✅ | ALL | CPU |\n| P1 | EDCR human validation | C4 | API |\n| P1 | Post-hoc evidence retrieval baseline | C1 | ~4h |\n| P1 | CED-as-reranker (running) | C1 | ~6h |\n| P1 | Model size ablation | RC | ~24h |\n| P1 | Re-DocRED extension | RC | ~12h |\n| ~~P0~~ | ~~GRPO forgetting dynamics figure (plan_009)~~ ✅ | C2 | ~2h |\n| ~~P0~~ | ~~SFT-without-evidence ablation (plan_014)~~ ✅ | C1 | ~8h |\n| P2 | Advantage variance measurement | C2 | CPU |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选\n    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py\n    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: eval_flat_nli_seed45\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.455052\n    ign_f1: 0.446181\n    evi_f1: 0.815399\n    edcr: 0.652133\n    evi_f1_joint: 0.355612\n- id: plan_002\n  claim: 1\n  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set\n    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_003\n  claim: 4\n  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing\n    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: plan_003_edcr_diagnostic\n  status: DONE\n  conclusion: success\n  metrics:\n    methods_evaluated: 15\n    edcr_vs_rel_f1_spearman: -0.9648\n    edcr_vs_rel_f1_pvalue: 0.0001\n    edcr_vs_evi_f1_spearman: 0.0022\n    edcr_vs_evi_f1_pvalue: 0.9941\n    edcr_range: 0.63-0.99\n    unique_diagnostic_value: identifies pathological models (GRPO QLoRA) with high\n      evi_f1 but catastrophically low rel_f1\n- id: plan_004\n  claim: 1\n  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)\n    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_004_dreeam_baseline\n  status: DONE\n  conclusion: success\n  metrics:\n    dev_rel_f1: 63.57\n    dev_rel_ign_f1: 61.72\n    dev_evi_f1: 54.01\n    dev_rel_p: 66.95\n    dev_rel_r: 60.51\n    dev_evi_p: 60.53\n    dev_evi_r: 48.76\n- id: plan_005\n  claim: 1\n  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: mvp2_ced_reranker_poc\n  status: DONE\n  conclusion: success\n  metrics:\n    ced_reranker_rel_f1: 0.486367\n    ced_reranker_ign_f1: 0.473634\n    ced_reranker_evi_f1: 0.8188\n    oracle_rel_f1: 0.623746\n    oracle_ign_f1: 0.612518\n    random_rel_f1: 0.453783\n    random_ign_f1: 0.439677\n- id: plan_006\n  claim: 1\n  description: 'Model size ablation (D077 升 P0): Qwen3-1.7B 和 Qwen3-8B 上复现 SFT → RSFT\n    → eval pipeline，验证 evidence tax + RSFT 增益 + decoupling 在不同模型规模下成立。应对 RC4 和 scope\n    不足问题。'\n  priority: P0\n  gpu_budget_hours: 32\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Re-DocRED cross-dataset (D077 升 P0): 在 Re-DocRED 上用当前 best config\n    做 SFT → RSFT → eval。数据已就绪（格式与 DocRED 兼容，96 relation types 一致）。⚠️ Re-DocRED ~55%\n    triples 无 evidence 标注（修正的 false negative），必须报告两种模式：evidence_only（与 DocRED 可比的\n    evi_f1，仅 43% triples）+ full（全部 triples 的 rel_f1，无 evi_f1）。转换脚本已支持 --mode full。'\n  priority: P0\n  gpu_budget_hours: 16\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_016\n  claim: 2\n  description: 'LLaMA-3.1-8B cross-family validation (D077 新增): 在非 Qwen 家族模型上复现核心\n    pipeline (SFT → RSFT → GRPO QLoRA)，验证 decoupling spectrum 跨模型家族成立。关键实验：LLaMA GRPO\n    QLoRA 是否也出现 catastrophic forgetting。'\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_008\n  claim: 2\n  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格\n    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: reeval_rsft_topk3\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.4454\n    rel_precision: 0.4512\n    rel_recall: 0.4398\n    ign_f1: 0.4364\n    evi_f1: 0.8088\n    edcr: 0.6635\n    format_ok_rate: 0.999\n    n_truncated: 214\n    n_predictions: 16020\n    inference_time_seconds: 3546.4\n    ign_f1_corrected: true\n- id: plan_011\n  claim: 3\n  description: 'GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward\n    + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要\n    gradient_accumulation 适配显存。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_011_bf16_g8_step_eval\n  status: DONE\n  conclusion: success\n  metrics:\n    step_30:\n      rel_f1: 0.434\n      evi_f1: 0.8063\n      edcr: 0.6807\n    step_50:\n      rel_f1: 0.4276\n      evi_f1: 0.8024\n      edcr: 0.6855\n    step_70:\n      rel_f1: 0.4341\n      evi_f1: 0.8099\n      edcr: 0.6685\n    best_step: step_70\n    trend: non-monotonic, all < ckpt-100 (0.4549)\n- id: plan_012\n  claim: 3\n  description: 'DPO+CED experiment: 用 RSFT 候选数据构造 preference pairs (CED-preferred\n    vs CED-rejected)，DPO 训练。验证 DPO 是否避免 GRPO 的 catastrophic forgetting。Dream v2 三档要求\n    DPO 作为 RL spectrum 关键数据点，必须补全训练超参（β, lr, epochs, pair construction）。D045 升 P0。'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: plan_012_dpo_ced\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.3429\n    evi_f1: 0.8403\n    edcr: 0.7294\n    format_ok_rate: 0.995\n    checkpoint: checkpoint-501\n    rewards_accuracy: 1\n    margins: 9.01\n- id: plan_013\n  claim: 4\n  description: 'EDCR 人工标注验证: 100 个样本，人工判断每个 cited evidence sentence 是否真正支持对应 relation。计算\n    EDCR 与人工判断的相关性，验证 EDCR 作为自动指标的有效性。Dream [M][W] 一致要求。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_009\n  claim: 3\n  description: 'GRPO forgetting dynamics figure: 整理全部 GRPO checkpoint（42个）的 rel_f1/evi_f1/EDCR/reward\n    轨迹，绘制 training dynamics 可视化图。包含 G=4 vs G=8 对比、三种 reward 对比。Dream v2 三档一致要求此图作为论文核心\n    figure。数据已有，只需汇总+画图。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: plan_009_dynamics_figure\n  status: DONE\n  conclusion: success\n- id: plan_010\n  claim: 1\n  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer\n    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_014\n  claim: 1\n  description: 'SFT-without-evidence ablation: 训练 Qwen3-4B SFT 只输出 relation triples（不含\n    evidence sentences），对比标准 SFT（含 evidence）的 rel_f1。隔离 evidence generation 对抽取性能的代价。Dream\n    v2 三档一致要求。用于回答\"43.2% vs LMRC 60.7% 的 gap 有多少来自 evidence 生成负担\"。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_014_sft_no_evidence\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.7077\n    eval_loss: 0.8781\n    eval_token_accuracy: 0.8086\n    epochs: 3\n    total_steps: 570\n    train_runtime_min: 64\n    samples: 3027\n    trainable_params: 132M/4.15B (3.18%)\n- id: plan_015\n  claim: 2\n  description: 'bf16 LoRA GRPO clean control: 与原始 GRPO (QLoRA 4-bit, G=4, kl=0, CED\n    reward) 只改一个变量——quantization 从 QLoRA 4-bit 改为 bf16 LoRA。G=4, kl_coef=0 不变。目的:\n    隔离 QLoRA confound，判断 decoupling 是 QLoRA artifact 还是 genuine RL-for-IE 现象。Dream\n    v2 三档一致的 critical 要求。如 decoupling 在 bf16 下仍持续 → 可泛化 claim；如消失 → QLoRA 特定，需 re-scope。优先级取决于\n    plan_011 eval 结果。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_011\n  registry_id: plan_015_grpo_g4_bf16_v3\n  status: DONE\n  conclusion: killed\n- id: plan_mvp1\n  claim: 1\n  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing\n    distractor 的能力验证'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: mvp1_ced_signal\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_margin: 0.48\n    discrimination_accuracy: 0.815\n    pearson_r_margin_jaccard: 0.34\n    pass: true\n- id: plan_mvp2_sft\n  claim: 1\n  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mvp2_sft_warmup\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.72\n    accuracy: 0.835\n- id: plan_mvp2_rsft\n  claim: 1\n  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部\n    PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087,\n    r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_mvp1\n  - plan_mvp2_sft\n  registry_id: mvp2_rsft_train_r1\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.0483\n    num_preds: 848\n    sft_baseline_rel_f1: 0.4057\n    failure_mode: relation_ontology_collapse_to_freetext\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n- id: plan_mvp2_grpo\n  claim: 3\n  description: 'GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1\n    max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic\n    forgetting。D031/D033 完整轨迹支撑 Claim 3'\n  priority: P0\n  gpu_budget_hours: 60\n  deps:\n  - plan_mvp2_sft\n  registry_id: mvp2_grpo_ced_lr5e6_r1\n  status: DONE\n  conclusion: killed\n\n\n## registry (completed experiments)\n\n- exp_id: mvp1_ced_signal\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_margin: 0.48\n    discrimination_accuracy: 0.815\n    pearson_r_margin_jaccard: 0.34\n    pass: true\n- exp_id: smoke_test_grpo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_sft_warmup\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.72\n    accuracy: 0.835\n- exp_id: precompute_nli_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_grpo_ced\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_extract\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_sft_eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_extract_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: mvp2_grpo_extract_r3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_sft_eval_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    ign_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    precision: 0.4043\n    recall: 0.407\n    evi_precision: 0.8035\n    evi_recall: 0.7924\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.626\n    n_parseable: 617\n    n_truncated: 367\n    n_predictions: 18815\n    inference_time_seconds: 6484.7\n- exp_id: mvp2_sft_eval_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    ign_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    precision: 0.4043\n    recall: 0.407\n    evi_precision: 0.8035\n    evi_recall: 0.7924\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.626\n    n_parseable: 617\n    n_truncated: 367\n    n_predictions: 18815\n- exp_id: mvp2_grpo_ced_kl001_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001_r3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001_r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_step: 100\n    train_runtime_s: 9069.88\n    reward_final: 1.195\n    f1_reward_final: 0.573\n    ced_reward_final: 0.328\n    format_reward_final: 0.293\n    frac_zero_std_final: 0.2\n    kl_final: 0.118\n    loss_final: -0.009\n    grad_norm_final: 0.14\n    entropy_final: 0.067\n    completion_length_mean_final: 520.8\n    best_reward_step: 90\n    best_reward: 1.37\n    best_f1_reward: 0.72\n    best_ced_reward: 0.353\n- exp_id: mvp2_grpo_extract_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_early\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    f1: 0.1563\n    ign_f1: 0.1563\n    evi_f1: 0.5643\n    edcr: 0.8858\n    precision: 0.2356\n    recall: 0.1169\n    evi_precision: 0.4864\n    evi_recall: 0.6721\n    format_ok_rate: 0.999\n    n_parseable: 984\n    n_truncated: 11\n    n_predictions: 9250\n    tp: 1421\n    pred_count: 6032\n    gold_count: 12151\n- exp_id: mvp2_grpo_flatnli_r6\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    steps_completed: 25\n    final_frac_zero_std: 0.9\n    final_f1_reward: 0\n    final_flat_nli_reward: 0\n    final_format_reward: 0.293\n    collapse_step: 25\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.00296\n    rel_precision: 0.00314\n    rel_recall: 0.0028\n    evi_f1: 0.72\n    evi_precision: 0.6429\n    evi_recall: 0.8182\n    edcr: 0.9983\n    n_parseable: 984\n    n_truncated: 24\n    n_predictions: 11621\n    tp: 34\n    pred_count: 10839\n    gold_count: 12151\n    inference_time_seconds: 5211.4\n- exp_id: mvp2_eval_ced_kl001_r4_multi\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    checkpoint-10:\n      f1: 0.003\n      ign_f1: 0.003\n      evi_f1: 0.72\n      edcr: 0.9983\n      format_ok_rate: 0.999\n    checkpoint-20:\n      f1: 0.0088\n      ign_f1: 0.0088\n      evi_f1: 0.423\n      edcr: 0.9954\n      format_ok_rate: 0.999\n    checkpoint-30:\n      f1: 0.0338\n      ign_f1: 0.0338\n      evi_f1: 0.5889\n      edcr: 0.9798\n      format_ok_rate: 1\n    checkpoint-50:\n      f1: 0.1563\n      ign_f1: 0.1563\n      evi_f1: 0.5643\n      edcr: 0.8858\n      format_ok_rate: 0.999\n    checkpoint-60:\n      f1: 0.1467\n      ign_f1: 0.1467\n      evi_f1: 0.5763\n      edcr: 0.9062\n      format_ok_rate: 1\n    checkpoint-90:\n      f1: 0.2108\n      ign_f1: 0.2108\n      evi_f1: 0.5666\n      edcr: 0.8584\n      format_ok_rate: 1\n- exp_id: mvp2_eval_ced_kl001_r4_step100\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.2167\n    ign_f1: 0.2167\n    precision: 0.2849\n    recall: 0.1749\n    evi_f1: 0.5746\n    evi_precision: 0.5244\n    evi_recall: 0.6353\n    edcr: 0.8539\n    pred_count: 7460\n    gold_count: 12151\n    tp: 2125\n    n_truncated: 21\n    format_ok_rate: 1\n- exp_id: mvp2_eval_ced_kl001_r4_last\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt90\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_high\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    checkpoint_60:\n      rel_f1: 0.1467\n      ign_f1: 0.1467\n      precision: 0.1909\n      recall: 0.1192\n      evi_f1: 0.5763\n      edcr: 0.9062\n      pred_count: 10041\n      gold_count: 12151\n      n_truncated: 16\n      format_ok_rate: 1\n    note: Only ckpt-60 completed. Process died during ckpt-70 inference at 8% (5/62\n      batch). ckpt-80/90 never started.\n- exp_id: mvp2_eval_ced_kl001_r4_step90\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.2108\n    ign_f1: 0.2108\n    evi_f1: 0.5666\n    edcr: 0.8584\n    pred_count: 11160\n    n_truncated: 22\n    format_ok_rate: 1\n    n_documents: 985\n- exp_id: mvp2_grpo_ced_lr5e6_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_p1_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_rp_r1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt7080\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_rp_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt20\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0077\n    rel_precision: 0.0071\n    rel_recall: 0.0084\n    evi_f1: 0.628\n    evi_precision: 0.855\n    evi_recall: 0.496\n    edcr: 0.993\n    format_ok_rate: 0.991\n    field_compliance_rate: 0.399\n    pred_count: 14440\n    gold_count: 12151\n    tp: 102\n    n_truncated: 587\n    inference_time_seconds: 6370.4\n- exp_id: mvp2_eval_lr5e6_r1_ckpt40\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt40_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0071\n    precision: 0.0066\n    recall: 0.0078\n    evi_f1: 0.7584\n    evi_precision: 0.9113\n    evi_recall: 0.6494\n    edcr: 0.9942\n    format_ok_rate: 0.9939\n    field_compliance_rate: 0.5675\n    pred_count: 14434\n    gold_count: 12151\n    tp: 95\n    n_truncated: 424\n    inference_time_seconds: 6152\n- exp_id: mvp2_eval_lr5e6_rp_r2_ckpt20\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_sft_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    evi_f1: 0.7979\n    evi_f1_joint: 0.3117\n    evi_f1_joint_P: 0.3037\n    evi_f1_joint_R: 0.32\n    edcr: 0.7118\n    pred_count: 12234\n    gold_count: 12151\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.998\n    field_compliance_rate: 0.6264\n    n_truncated: 367\n    inference_time_seconds: 6138.5\n- exp_id: mvp2_eval_lr5e6_r1_ckpt60\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt80\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0116\n    ign_f1: 0.0116\n    precision: 0.0109\n    recall: 0.0124\n    evi_f1: 0.828\n    evi_precision: 0.928\n    evi_recall: 0.748\n    edcr: 0.993\n    format_ok_rate: 0.999\n    field_compliance_rate: 0.788\n    pred_count: 13828\n    gold_count: 12151\n    n_truncated: 210\n    inference_time_seconds: 6099\n- exp_id: mvp2_eval_lr5e6_r1_ckpt60_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0093\n    precision: 0.0085\n    recall: 0.0103\n    evi_f1: 0.81\n    edcr: 0.993\n    format_ok_rate: 0.998\n    pred_count: 14626\n    gold_count: 12151\n    tp: 125\n    inference_time_seconds: 6152\n- exp_id: mvp2_eval_lr5e6_r1_ckpt100\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0138\n    rel_precision: 0.0132\n    rel_recall: 0.0144\n    ign_f1: 0.0138\n    evi_f1: 0.8504\n    evi_precision: 0.9256\n    evi_recall: 0.7866\n    edcr: 0.9876\n    format_ok_rate: 0.999\n    field_compliance_rate: 0.8162\n    evidence_format_rate: 0.8162\n    tp: 175\n    pred_count: 13300\n    gold_count: 12151\n    n_predictions: 15498\n    n_truncated: 181\n    n_documents: 985\n    n_parseable: 984\n    inference_time_seconds: 5901.7\n- exp_id: mvp2_diversity_probe\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    unique_triples_t07: 5\n    unique_triples_t10: 8\n    jaccard_t07: 0.17\n    jaccard_t10: 0.051\n    format_ok_rate_t07: 0.5\n    format_ok_rate_t10: 0.438\n    n_samples: 3\n    n_generations: 8\n    note: 'unique_triples_t07 corrected from 7 to 5.0 (mean). Reviewer: format_ok\n      ~34% after fix, ''diversity'' was JSON key name variants not semantic diversity'\n- exp_id: mvp2_rsft_generate\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    generation_count: 5288\n    unique_docs: 659\n    format_compliance: 0.998\n    diversity_range: 7.5-7.8/8\n    exit_code: 0\n- exp_id: mvp2_rsft_ced_scoring\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    input_generations: 21952\n    selected_samples: 2718\n    unique_docs: 2691\n    selection_rate: 0.124\n    mean_f1: 0.6157\n    mean_ced: 0.6683\n    f1_range:\n    - 0.1026\n    - 1\n    zero_f1_samples: 0\n    selection_strategy: top_k=1\n    f1_threshold: 0.1\n- exp_id: mvp2_rsft_train_r1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.0483\n    num_preds: 848\n    sft_baseline_rel_f1: 0.4057\n    failure_mode: relation_ontology_collapse_to_freetext\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n- exp_id: mvp2_rsft_train_r1_s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.7622\n    train_loss: 0.6148\n    eval_entropy: 0.6724\n    mean_token_accuracy: 0.8291\n    total_steps: 510\n    epochs: 3\n    training_hours: 1.99\n- exp_id: mvp2_rsft_train_r1_s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4655\n    evi_f1: 0.8087\n    evi_f1_joint: 0.3713\n    evi_f1_joint_P: 0.3775\n    evi_f1_joint_R: 0.3653\n    edcr: 0.635\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0598\n    delta_evi_f1: 0.0108\n    delta_evi_f1_joint: 0.0596\n    mvp2_pass: true\n- exp_id: mvp2_rsft_ced_scoring_topk3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_s44\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_ced_reranker_poc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ced_reranker_rel_f1: 0.486367\n    ced_reranker_ign_f1: 0.473634\n    ced_reranker_evi_f1: 0.8188\n    oracle_rel_f1: 0.623746\n    oracle_ign_f1: 0.612518\n    random_rel_f1: 0.453783\n    random_ign_f1: 0.439677\n- exp_id: mvp2_rsft_diagnosis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    root_cause: overfitting_plus_sft_knowledge_overwrite\n    truncated_json_samples: 170\n    truncated_pct: 6.3\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n    lora_scaling: 2\n    rsft_zero_relation_samples: 170\n    sft_zero_relation_docs: 26\n    rsft_mean_relations: 11.2\n    sft_mean_relations: 12.5\n- exp_id: mvp2_rsft_train_r2_fix\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_rsft_r2a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4494\n    evi_f1: 0.8108\n    edcr: 0.6641\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0437\n    delta_evi_f1: 0.0129\n    mvp2_pass: true\n- exp_id: mvp2_rsft_r2b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4493\n    evi_f1: 0.8128\n    edcr: 0.6609\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0436\n    delta_evi_f1: 0.0149\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4449\n    evi_f1: 0.8187\n    evi_f1_joint: 0.3468\n    evi_f1_joint_P: 0.3515\n    evi_f1_joint_R: 0.3423\n    edcr: 0.6565\n    num_preds: 15307\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0392\n    delta_evi_f1: 0.0208\n    delta_evi_f1_joint: 0.0351\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r2a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4494\n    ign_f1: 0.4494\n    evi_f1: 0.8108\n    evi_f1_joint: 0.3509\n    evi_f1_joint_P: 0.3423\n    evi_f1_joint_R: 0.3599\n    edcr: 0.6641\n    precision: 0.4512\n    recall: 0.4475\n    evi_precision: 0.8143\n    evi_recall: 0.8073\n    format_ok_rate: 1\n    n_predictions: 15482\n    n_truncated: 208\n    inference_time_s: 5967.2\n    delta_evi_f1_joint: 0.0392\n- exp_id: mvp2_eval_rsft_r2b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4493\n    ign_f1: 0.4493\n    evi_f1: 0.8128\n    evi_f1_joint: 0.349\n    evi_f1_joint_P: 0.3455\n    evi_f1_joint_R: 0.3526\n    edcr: 0.6609\n    precision: 0.4566\n    recall: 0.4424\n    evi_precision: 0.8201\n    evi_recall: 0.8056\n    pred_count: 14829\n    format_ok: 983/985\n    truncated: 179\n    inference_time_s: 5862\n    delta_evi_f1_joint: 0.0373\n- exp_id: mvp2_eval_rsft_s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_s43_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4683\n    ign_f1: 0.4683\n    evi_f1: 0.8156\n    evi_f1_joint: 0.3711\n    evi_f1_joint_P: 0.3747\n    evi_f1_joint_R: 0.3675\n    edcr: 0.6388\n    precision: 0.4817\n    recall: 0.4556\n    evi_precision: 0.8142\n    evi_recall: 0.817\n    n_predictions: 14970\n    n_truncated: 171\n    format_ok_rate: 1\n    inference_time_s: 6316.7\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0626\n    delta_evi_f1: 0.0177\n    delta_evi_f1_joint: 0.0594\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r2b_maxtok1536\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_r2b_maxtok1536_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.4504\n    ign_f1: 0.4504\n    evi_f1: 0.8102\n    edcr: 0.674\n    precision: 0.4488\n    recall: 0.4519\n    evi_precision: 0.8162\n    evi_recall: 0.8044\n    n_truncated: 146\n    n_total: 985\n    n_predictions: 17188\n    n_distractor_citations: 19589\n    n_total_citations: 29063\n    format_ok_rate: 0.998\n- exp_id: mvp2_rsft_ced_scoring_topk3_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    input_generations: 21728\n    selected_samples: 8037\n    unique_docs: 2691\n    selection_rate: 0.37\n    mean_f1: 0.5761\n    mean_ced: 0.6205\n    mean_combined: 0.6787\n    f1_range_p25: 0.444\n    f1_range_p75: 0.717\n    ced_range_p25: 0.487\n    ced_range_p75: 0.774\n    truncated_samples: 1924\n    truncated_pct: 8.9\n    selection_strategy: top_k=3\n    f1_threshold: 0.1\n    topk1_samples: 2718\n    data_multiplier: 2.96\n- exp_id: plan_004_dreeam_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dev_rel_f1: 63.57\n    dev_rel_ign_f1: 61.72\n    dev_evi_f1: 54.01\n    dev_rel_p: 66.95\n    dev_rel_r: 60.51\n    dev_evi_p: 60.53\n    dev_evi_r: 48.76\n- exp_id: plan_011_grpo_g8_bf16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_step: 100\n    train_runtime_s: 554\n    reward_final: 1.795\n    f1_reward_final: 1.002\n    ced_reward_final: 0.494\n    format_reward_final: 0.3\n    frac_zero_std_final: 0\n    kl_final: 0.022\n    best_reward_step: 85\n    best_reward: 2.858\n    best_f1_reward: 1.85\n    mode_collapse: false\n    lora_config: r=64, alpha=128, dropout=0.05, bf16\n    checkpoints: 10 checkpoints (step 10-100)\n- exp_id: plan_001_flat_nli_scoring\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_scored: 21728\n    selected_samples: 2691\n    selection_rate: 0.124\n    selection_strategy: top_k=1\n    f1_threshold: 0.1\n    output_path: /root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl\n- exp_id: eval_grpo_g8_bf16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ckpt80_rel_f1: 0.4456\n    ckpt80_ign_f1: 0.4456\n    ckpt80_evi_f1: 0.8034\n    ckpt80_edcr: 0.6409\n    ckpt80_format_ok: 984/985\n    ckpt80_truncated: 50\n    ckpt90_rel_f1: 0.4523\n    ckpt90_ign_f1: 0.4523\n    ckpt90_evi_f1: 0.8052\n    ckpt90_edcr: 0.6414\n    ckpt90_format_ok: 983/985\n    ckpt90_truncated: 61\n    ckpt100_rel_f1: 0.4549\n    ckpt100_ign_f1: 0.4549\n    ckpt100_evi_f1: 0.8086\n    ckpt100_edcr: 0.6318\n    ckpt100_format_ok: 985/985\n    ckpt100_truncated: 61\n    best_checkpoint: ckpt-100\n- exp_id: plan_011_eval_g8_bf16_ckpt100\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_011_grpo_g8_bf16_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4549\n    ign_f1: 0.4549\n    evi_f1: 0.8086\n    edcr: 0.6318\n    format_ok_rate: 1\n    n_truncated: 61\n    n_total: 985\n    n_predictions: 10701\n    checkpoint: checkpoint-100\n    model: Qwen3-4B + SFT merged + GRPO bf16 LoRA ckpt-100\n    inference_time_s: 3170.3\n- exp_id: plan_001_rsft_flat_nli\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.6238\n    train_loss_min: 0.5803\n    mean_token_accuracy: 0.8528\n    train_runtime_sec: 2946\n    epochs: 3\n    total_steps: 507\n    samples: 2691\n- exp_id: plan_012_dpo_ced\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.3429\n    evi_f1: 0.8403\n    edcr: 0.7294\n    format_ok_rate: 0.995\n    checkpoint: checkpoint-501\n    rewards_accuracy: 1\n    margins: 9.01\n- exp_id: plan_014_sft_no_evidence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.7077\n    eval_loss: 0.8781\n    eval_token_accuracy: 0.8086\n    epochs: 3\n    total_steps: 570\n    train_runtime_min: 64\n    samples: 3027\n    trainable_params: 132M/4.15B (3.18%)\n- exp_id: plan_015_grpo_g4_bf16\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_015_grpo_g4_bf16_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_015_grpo_g4_bf16_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: eval_plan_001_flat_nli\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4539\n    ign_f1: 0.4539\n    evi_f1: 0.8043\n    edcr: 0.6431\n    precision: 0.4671\n    recall: 0.4414\n    evi_precision: 0.8143\n    evi_recall: 0.7945\n    format_ok_rate: 1\n    n_truncated: 199\n    n_documents: 985\n    n_predictions: 15294\n    inference_time_seconds: 3631\n- exp_id: eval_plan_014_sft_no_evidence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4893\n    rel_ign_f1: 0.4893\n    rel_precision: 0.4884\n    rel_recall: 0.4902\n    evi_f1: 0\n    evi_precision: 0\n    evi_recall: 0\n    edcr: 0\n    format_ok_rate: 0.9919\n    n_truncated: 298\n    n_predictions: 21064\n    n_documents: 985\n    n_parseable: 977\n    inference_time_seconds: 4103.8\n- exp_id: plan_008_rsft_topk3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.5543\n    eval_loss: 0.8297\n    eval_mean_token_accuracy: 0.8228\n    eval_entropy: 0.6001\n    train_runtime_sec: 10916\n    total_steps: 1509\n    epochs: 3\n    trainable_params_pct: 3.18\n    rsft_samples: 8037\n    ced_score_mean: 0.621\n    task_eval_f1_ep1: 0.4848\n    task_eval_f1_ep2: 0.4824\n    task_eval_f1_ep3: 0.5012\n    task_eval_evi_f1_ep1: 0.745\n    task_eval_evi_f1_ep2: 0.6997\n    task_eval_evi_f1_ep3: 0.6816\n    task_eval_edcr_ep1: 0.6525\n    task_eval_edcr_ep2: 0.6529\n    task_eval_edcr_ep3: 0.5963\n    task_eval_note: 50-doc subset, not full dev\n- exp_id: plan_002_test_eval_s44\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_001_flat_nli_seed43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss_final: 0.6257\n    train_loss_min: 0.5895\n    eval_loss_epoch3: 0.7567\n    eval_accuracy_epoch3: 0.8298\n    total_steps: 507\n    epochs: 3\n    train_runtime_seconds: 6880\n    task_eval_f1_ep1: 0.4825\n    task_eval_f1_ep2: 0.4542\n    task_eval_f1_ep3: 0.4866\n    task_eval_evi_f1_ep3: 0.7834\n    task_eval_edcr_ep3: 0.6402\n    task_eval_note: 50-doc subset, not full dev\n- exp_id: eval_sft_baseline_noquant\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4106\n    rel_precision: 0.4198\n    rel_recall: 0.4019\n    evi_f1: 0.8013\n    evi_precision: 0.8005\n    evi_recall: 0.8022\n    evi_f1_joint: 0.3216\n    edcr: 0.7039\n    format_ok_rate: 0.998\n    field_compliance_rate: 0.7066\n    n_predictions: 16774\n    n_truncated: 288\n    n_documents: 985\n    inference_time_seconds: 3677.9\n- exp_id: plan_012_dpo_ced_1ep\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0022\n    evi_f1: 0.75\n    edcr: 0.9982\n    format_ok: 981/985\n    truncated: 358/985\n    tp: 34\n    n_preds: 19265\n    inference_time_s: 3643\n    train_loss_final: 0.59\n    rewards_accuracy: 0.82\n    rewards_margins: 0.86\n    total_steps: 167\n    training_time_min: 33\n- exp_id: plan_009_forgetting_figure\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_011_bf16_g8_step_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    step_30:\n      rel_f1: 0.434\n      evi_f1: 0.8063\n      edcr: 0.6807\n    step_50:\n      rel_f1: 0.4276\n      evi_f1: 0.8024\n      edcr: 0.6855\n    step_70:\n      rel_f1: 0.4341\n      evi_f1: 0.8099\n      edcr: 0.6685\n    best_step: step_70\n    trend: non-monotonic, all < ckpt-100 (0.4549)\n- exp_id: plan_009_extract_reward_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_009_flatnli_reward_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: eval_plan_012_dpo_ced_ckpt400\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_009_flatnli_reward_eval_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: eval_plan_012_dpo_ced_1ep\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0022\n    ign_f1: 0.0022\n    evi_f1: 0.75\n    edcr: 0.9982\n    num_preds: 19265\n    format_ok: 981/985\n    truncated: 358/985\n    tp: 34\n    inference_time_s: 3643\n- exp_id: eval_plan_001_flat_nli_s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    rel_f1: 0.0022\n    ign_f1: 0.0022\n    evi_f1: 0.8533\n    edcr: 0.9982\n    num_preds: 17285\n    format_ok: 981/985\n    truncated: 251/985\n    tp: 32\n    note: INVALID — missing --sft_adapter, same bug as DPO 1ep eval\n- exp_id: plan_001_flat_nli_seed45\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    task_eval_rel_f1: 0.4876\n    task_eval_evi_f1: 0.7927\n    task_eval_edcr: 0.6517\n    train_loss: 0.6245\n    runtime_hours: 1.69\n    note: task-eval on 50 docs only, full dev eval needed\n- exp_id: eval_plan_008_rsft_topk3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    note: INVALID — missing --sft_adapter, killed by Director instruction\n- exp_id: plan_001_flat_nli_seed44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.6247\n    eval_loss: 0.7564\n    eval_mean_token_accuracy: 0.8299\n    task_eval_f1_ep1: 0.4306\n    task_eval_f1_ep2: 0.4884\n    task_eval_f1_ep3: 0.4897\n    task_eval_evi_f1_ep3: 0.78\n    task_eval_edcr_ep3: 0.6596\n    task_eval_ign_f1_ep3: 0.4897\n    train_runtime_sec: 6197\n    num_epochs: 3\n    total_steps: 507\n- exp_id: eval_plan_012_dpo_1ep_fixed\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: eval_plan_008_topk3_fixed\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: eval_plan_012_dpo_1ep_fixed_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.4034\n    evi_f1: 0.8088\n    edcr: 0.7139\n    format_ok_rate: 0.999\n    truncated_rate: 0.343\n    predictions: 19107\n    ign_f1: 0.4034\n    precision: 0.3809\n    recall: 0.4287\n    vs_sft_delta: -0.0023\n    note: DPO 1ep matches SFT baseline. 1ep→3ep trajectory shows gradual decoupling\n      (rel_f1↓ evi_f1↑), consistent with GRPO pattern. Ign-F1=F1 exact match needs\n      investigation.\n- exp_id: reeval_flat_nli_s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4523\n    ign_f1: 0.4523\n    evi_f1: 0.8158\n    edcr: 0.6505\n    num_preds: 15357\n    format_ok: 984/985\n    truncated: 211/985\n    inference_time_s: 3515.8\n- exp_id: reeval_rsft_topk3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.4454\n    rel_precision: 0.4512\n    rel_recall: 0.4398\n    ign_f1: 0.4364\n    evi_f1: 0.8088\n    edcr: 0.6635\n    format_ok_rate: 0.999\n    n_truncated: 214\n    n_predictions: 16020\n    inference_time_seconds: 3546.4\n    ign_f1_corrected: true\n- exp_id: eval_flat_nli_seed44\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: eval_flat_nli_seed45\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.455052\n    ign_f1: 0.446181\n    evi_f1: 0.815399\n    edcr: 0.652133\n    evi_f1_joint: 0.355612\n- exp_id: plan_003_edcr_diagnostic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    methods_evaluated: 15\n    edcr_vs_rel_f1_spearman: -0.9648\n    edcr_vs_rel_f1_pvalue: 0.0001\n    edcr_vs_evi_f1_spearman: 0.0022\n    edcr_vs_evi_f1_pvalue: 0.9941\n    edcr_range: 0.63-0.99\n    unique_diagnostic_value: identifies pathological models (GRPO QLoRA) with high\n      evi_f1 but catastrophically low rel_f1\n- exp_id: eval_flat_nli_s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.461506\n    ign_f1: 0.452126\n    evi_f1: 0.813123\n    edcr: 0.645808\n    evi_f1_joint: 0.359673\n- exp_id: plan_009_dynamics_figure\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: eval_plan_014_no_evidence\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: rsft_ced_s45_train\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: rsft_ced_s43_train\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: rsft_ced_s45_train_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: rsft_ced_s43_train_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: rsft_ced_s43_train_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.6151\n    eval_loss: 0.7618\n    task_eval_f1: 0.5026\n    task_eval_ign_f1: 0.4932\n    task_eval_evi_f1: 0.7624\n    task_eval_edcr: 0.6516\n    total_steps: 510\n    epochs: 3\n    training_hours: 1.82\n- exp_id: rsft_ced_s45_train_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: rsft_ced_s45_train_r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    training_completed: true\n    checkpoint: checkpoint-510\n    note: Training metrics not captured (r4 retry after OOM). Eval running as eval_rsft_ced_s45.\n- exp_id: eval_rsft_ced_s45\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4514\n    ign_f1: 0.4416\n    evi_f1: 0.8174\n    rel_p: 0.4718\n    rel_r: 0.4326\n    edcr: 0.655\n    evi_f1_joint: 0.3558\n    n_truncated: 206\n    format_ok_rate: 1\n- exp_id: eval_rsft_ced_s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4601\n    ign_f1: 0.4512\n    precision: 0.4696\n    recall: 0.4509\n    evi_f1: 0.8063\n    evi_precision: 0.8025\n    evi_recall: 0.8101\n    edcr: 0.6542\n    evi_f1_joint: 0.3605\n    format_ok_rate: 1\n    n_truncated: 184\n    n_predictions: 15051\n    inference_time_seconds: 10768.2\n- exp_id: eval_plan_014_no_evidence_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4876\n    ign_f1: 0.4721\n    evi_f1: 0\n    edcr: 0\n    evi_f1_joint: 0\n    precision: 0.4901\n    recall: 0.4851\n    ign_precision: 0.4654\n    ign_recall: 0.4791\n    format_compliance: 0.993\n    truncation_rate: 0.312\n    n_predictions: 21181\n    n_documents: 985\n- exp_id: reeval_flat_nli_s43_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4586\n    rel_precision: 0.4732\n    rel_recall: 0.4449\n    ign_f1: 0.4503\n    evi_f1: 0.8113\n    evi_precision: 0.8035\n    evi_recall: 0.8192\n    evi_f1_joint: 0.358\n    edcr: 0.6552\n    format_ok_rate: 0.999\n    n_truncated: 184\n    n_predictions: 15015\n- exp_id: seed_comparison_prep\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: reeval_ced_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.4423\n    rel_f1: 0.4517\n    evi_f1: 0.8175\n    evi_f1_joint: 0.3518\n    edcr: 0.6569\n    format_compliance_rate: 1\n    field_compliance_rate: 0.7756\n    n_truncated: 214\n    inference_time_seconds: 10815.5\n- exp_id: reeval_ced_s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.4511\n    rel_f1: 0.4621\n    evi_f1: 0.805\n    evi_f1_joint: 0.3677\n    edcr: 0.635\n    format_compliance_rate: 1\n    field_compliance_rate: 0.802\n    n_truncated: 190\n    inference_time_seconds: 13077.6\n- exp_id: reeval_flat_nli_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ign_f1: 0.4448\n    rel_f1: 0.4535\n    evi_f1: 0.8039\n    evi_f1_joint: 0.3558\n    edcr: 0.6458\n    format_compliance_rate: 1\n    field_compliance_rate: 0.7787\n    n_truncated: 205\n    inference_time_seconds: 13253.1\n- exp_id: reeval_sft_baseline_d076\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4049\n    ign_f1: 0.3974\n    evi_f1: 0.7986\n    edcr: 0.6982\n    evi_f1_joint: 0.3147\n    format_compliance_rate: 0.998\n    n_truncated: 288\n    n_documents: 985\n    n_predictions: 16880\n    inference_time_sec: 7056.5\n- exp_id: plan_006_qwen3_1_7b_sft\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_006_qwen3_1_7b_sft_bf16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.6884\n    eval_loss: 0.8031\n    eval_mean_token_accuracy: 0.8238\n    eval_entropy: 0.682\n    train_runtime_sec: 2473\n    train_samples_per_second: 3.672\n    epochs: 3\n    total_steps: 570\n- exp_id: plan_006_qwen3_1_7b_no_evidence_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_006_qwen3_8b_sft_bf16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.5705\n    eval_loss: 0.7186\n    eval_mean_token_accuracy: 0.8377\n    eval_entropy: 0.5614\n    train_runtime_s: 3932\n    epoch: 3\n- exp_id: plan_006_qwen3_1_7b_sft_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    f1: 0.4945\n    ign_f1: 0.4786\n    evi_f1: 0.8316\n    edcr: 0.6704\n    precision: 0.5085\n    recall: 0.4813\n    ign_precision: 0.483\n    ign_recall: 0.4743\n    evi_precision: 0.8203\n    evi_recall: 0.8432\n    evi_f1_joint: 0.3958\n    format_compliance_rate: 1\n    n_predictions: 17184\n    n_truncated: 314\n    inference_time_seconds: 6848.7\n- exp_id: plan_002_test_eval_s44_r2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: reeval_flat_nli_s44\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_006_qwen3_8b_sft_eval\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan_006_qwen3_1_7b_no_evidence_eval\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan_006_qwen3_8b_no_evidence_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.6509\n    eval_loss: 0.8153\n    eval_mean_token_accuracy: 0.8174\n    eval_entropy: 0.6275\n    train_runtime_sec: 3656\n    epoch: 3\n- exp_id: plan_016_llama_3_1_8b_sft\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T11:17:25.961Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T11:17:25.961Z",
  "sessionId": "ec4f40cb-c4c9-433e-91d1-bac586606fad"
}
```

---

## Round 1

12 recorded events

### User

_source line 3 · 2026-05-16T11:17:25.992Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Test set 不 generalize 或 decoupling 跨家族不复现，核心 claim 需要 reframe
核心假设：['Test set RSFT vs SFT Δ < 2pp 或不显著（dev-test gap 大，可能因 DocRED test 分布偏移）', '或 LLaMA GRPO QLoRA 不出现 catastrophic decoupling（spectrum 变成 Qwen-specific）', 'CED vs flat-NLI 不显著（已是大概率事件）', '1.7B/8B 结果与 4B 方向不完全一致（evidence tax 在大模型消失或 RSFT 增益不稳定）', 'EDCR 人工验证偏低（ρ<0.5），部分 evidence 标注模糊导致指标可信度受质疑']
关键指标范围：{'test_rsft_vs_sft_ign_f1_delta': [0.0, 2.0], 'ced_vs_flat_nli_p_value': [0.2, 0.8], 'ced_ign_f1_5seed_mean': [0.44, 0.45], 'flat_nli_ign_f1_5seed_mean': [0.44, 0.452], 'cross_model_rsft_sft_delta_min': [0.0, 2.0], 'llama_grpo_qlora_rel_f1': [0.1, 0.4], 'edcr_human_spearman': [0.3, 0.5], 're_docred_rsft_vs_sft_delta': [-1.0, 2.0]}
叙事方向：Reframe 为分析/诊断贡献论文，不以 RSFT 方法性能为核心 claim。三个 reframe 方向（按优先级）：(1) 'Understanding the cost of faithfulness in generative IE'——evidence generation tax（7pp）+ 部分恢复的系统性分析，贡献在于量化了 faithfulness-performance trade-off 并提供 EDCR 作为诊断工具；(2) 'Why RL fails for multi-objective IE: an empirical study'——decoupling 即使只在 Qwen 上验证，作为 case study 仍有价值，重心转向 intra-task objective competition 的机制分析 + QLoRA amplification 现象；(3) 如果 Qwen-only 但数据充分，scope 收缩为 'model-specific' 发现但补充足够 ablation 深度（training dynamics, per-relation 分析, advantage variance）使单模型分析具独立价值。目标仍 EMNLP main（Findings track 可接受），不降级 venue。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: faith-evidence-ie

## paper_framing.md

# Paper Framing — FREIGE

> **状态**: POST-MVP + DREAM v2 完成（D047 分析）
> **最后更新**: 2026-05-16
> **Dream v1**: best=2.5, median=3.0, worst=2.5 → reframe 完成
> **Dream v2**: best=3.0, median=2.5, worst=2.5 → best 提升但 median 下降，未达标。关键路径：plan_011 bf16 GRPO eval + structural fixes → re-dream v3

## Target Venue

- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)
- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)

## Core Insight

LLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。

我们系统性地探索了 online RL (GRPO) 、offline preference optimization (DPO) 和 offline RL (RSFT) 三条技术路线。关键发现：**RL optimization pressure 与 evidence-extraction decoupling severity 正相关**——优化强度越大，evidence 质量提升的同时抽取能力退化越严重。QLoRA 放大至 catastrophic（rel_f1<0.02），bf16 GRPO 从 0.4549 退化至 ~0.434（mild, -2pp），DPO 呈 gradual 退化（1ep→3ep rel_f1 从 0.4034→0.3429），RSFT 无 decoupling。

CED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，通过文档内 hard negative 对比评估 evidence 质量。CED 作为 RSFT 的 scoring function 之一进行测试，其相对于 flat-NLI 的优势需要通过充分的统计检验验证。

## Story Arc

1. **Problem**: LLM DocRE 无证据 → 部署障碍
2. **New task**: evidence-grounded DocRE — 同时生成关系和证据
3. **Cost of faithfulness**: evidence generation 代价 ~7pp Ign-F1（no-evidence 47.36 vs evidence-SFT 40.36）——这是 faithfulness 的真实成本
4. **Exploration**: 系统性比较 online RL (GRPO) vs offline preference (DPO) vs offline RL (RSFT)
5. **Key finding**: evidence-extraction decoupling — RL optimization pressure 与 decoupling severity 正相关，形成连续谱系（GRPO-QLoRA catastrophic > GRPO-bf16 mild > DPO gradual > RSFT none）
6. **QLoRA amplification**: QLoRA 量化将 mild decoupling 放大至 catastrophic forgetting——decoupling 是 RL-for-IE 中 multi-objective competition 的通用梯度（intra-task trade-off，非 inter-task forgetting），QLoRA 是 catastrophic amplifier
7. **What works**: RSFT with NLI-based scoring 是唯一有效路线——提升 evidence 质量而不牺牲抽取
8. **Best practical solution**: CED reranker 恢复 97% 的 evidence 代价，同时保留高质量 evidence（evi_f1=0.8188）
9. **Diagnostic tool**: EDCR 双层诊断——方法级量化 decoupling（与 Claim 2 呼应），per-relation 级揭示 evi_f1 不捕捉的 relation-type 难度差异（D070 ✅）

## Core Claims (reframed after Dream v1, updated D068/D069/D070/D071/D072)

### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力
- FREIGE 是首个**基于生成式 LLM** 的 evidence-grounded DocRE 方法（⚠️ 必须始终保持 "generative LLM" 限定词——SAIS 已做 encoder-based evidence retrieval + DocRE）
- **关键区分 (Reviewer warning)**：encoder-based evidence *retrieval*（SAIS, DREEAM — 分类哪些句子是证据，evidence supervision 提升 RE）vs generative evidence *production*（FREIGE — LLM 生成证据文本，额外生成负担导致 ~7pp 代价）。论文 Related Work 必须精准讨论此对比，否则审稿人会问 "为什么 SAIS 说 evidence 有用，你说 evidence 有害"
- **Evidence generation tax**: no-evidence SFT Ign-F1=47.36 vs evidence-SFT 40.36，代价 ~7pp（plan_014 ✅）
- RSFT 在 4/4 配置下均超过 SFT baseline（Ign-F1 +3.3~5.5pp）
- **CED reranker 是最优实用方案**: rel_f1=0.4864（仅低于 no-evidence 0.29pp），evi_f1=0.8188（plan_005 ✅）
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

### Claim 3 (Ablation): NLI-based scoring 提升 RSFT 质量
- CED 和 flat-NLI 都优于 random/no scoring
- CED vs flat-NLI 的差异需统计验证（Dream 报告 p=0.08/0.38/0.12 不显著）
- **Critical**: 如果 CED 不显著优于 flat-NLI → CED 降级为"one possible scoring function"
- **行动**: 5+ seeds for significance testing
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

## MVP Evidence Summary (D071: 主表报 Ign-F1，附录报 F1)

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

## Anticipated Reviewer Concerns (updated from Dream, D068/D069)

### RC1: "Online RL" 标题过度声称（Dream 三档一致 Critical）
- ~~标题和 claim 收窄到 "GRPO fails for DocRE"~~
- **D068/D069 修正**: 重新定位为 "RL optimization pressure correlates with decoupling severity"——不是 GRPO 特有问题，而是 RL-for-IE 的通用梯度
- DPO 数据支撑 decoupling spectrum（gradual decay confirms the pattern）

### RC2: GRPO G=4 太小 + LoRA confound（Dream 三档一致 Major）
- GRPO G=8 bf16 实验 ✅ — 确认 mild decoupling（-2pp），QLoRA 是 catastrophic amplifier（D065/D066）
- LoRA confound 已解决：bf16 LoRA vs QLoRA 直接对比

### RC3: CED 不显著优于 flat-NLI（Dream 三档一致 Major）
- 5+ seeds 统计检验；如不显著 → CED 降级

### RC4: RSFT 不新颖
- 不声称 RSFT 是贡献；贡献在于任务定义 + decoupling 发现 + EDCR
- 诚实定位 RSFT 为 STaR (NeurIPS 2022) 单轮变体 + domain-specific quality filter

### RC12: SAIS 说 evidence 有用，为何 FREIGE 说 evidence 有害？（文献审查 2026-05-16）
- **关键区分**: discriminative evidence *retrieval*（SAIS/DREEAM — 分类句子是否为证据，作为监督信号提升 RE）vs generative evidence *production*（FREIGE — LLM 生成完整证据文本，额外生成负担导致 ~7pp 代价）
- SAIS 的 evidence supervision 是分类任务，不增加输出长度；FREIGE 的 evidence generation 显著增加生成序列长度，模型需分配容量同时完成 RE + evidence 生成
- **应对**: Related Work 中精准讨论此对比，明确 FREIGE 研究的是 *generative production* 设定下的代价，与 *retrieval* 设定下的增益不矛盾——两者揭示了 evidence 在不同范式下的不同角色

### RC13: 单模型单数据集泛化性不足（D077 scope 扩展）
- plan_006: Qwen3-1.7B / 8B model size ablation
- plan_016: LLaMA-3.1-8B cross-family validation
- plan_007: Re-DocRED cross-dataset evaluation

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

## Publishability Threshold (revised after Dream, D068/D069)

- **必要条件**: (1) RSFT 在 test set 上 Ign-F1 显著 > SFT (2) DREEAM-protocol Evi-F1 可报告 (3) Decoupling spectrum 有完整数据支撑（GRPO QLoRA/bf16 + DPO + RSFT）
- **充分条件**: 上述 + CED 显著 > flat-NLI + EDCR 人工验证
- **Failure pivot**: decoupling spectrum 不成立（bf16 GRPO 也 catastrophic）→ scope 大幅缩减。**已排除**: bf16 GRPO 确认 mild（D065/D066）

## Research Phase Priorities (revised after Dream v1)

| Priority | 实验 | Claim | GPU-h |
|----------|------|-------|-------|
| P0 | flat-NLI RSFT ablation (5 seeds) | C3 | ~25h |
| P0 | CED RSFT additional seeds (→5 total) | C3 | ~10h |
| P0 | DREEAM-protocol Evi-F1 对齐 | C1 | CPU |
| P0 | Test set evaluation | C1 | ~4h |
| P0 | DREEAM baseline reproduction | C1 | ~8h |
| ~~P0~~ | ~~GRPO G=8 experiment~~ ✅ | C2 | ~16h |
| ~~P0~~ | ~~DPO+CED experiment~~ ✅ | C2 | ~12h |
| ~~P0~~ | ~~EDCR per-relation analysis (D070)~~ ✅ | C4 | CPU |
| ~~P0~~ | ~~Ign-F1 bugfix + data sync (D071)~~ ✅ | ALL | CPU |
| P1 | EDCR human validation | C4 | API |
| P1 | Post-hoc evidence retrieval baseline | C1 | ~4h |
| P1 | CED-as-reranker (running) | C1 | ~6h |
| P1 | Model size ablation | RC | ~24h |
| P1 | Re-DocRED extension | RC | ~12h |
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
  registry_id: null
  status: planned
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
  registry_id: null
  status: planned
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
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: reeval_flat_nli_s44
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: plan_006_qwen3_8b_sft_eval
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: plan_006_qwen3_1_7b_no_evidence_eval
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
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
  "promptId": "812941b3-521c-41f3-a10c-8ea6ea514767",
  "type": "user",
  "uuid": "9e79dcae-f997-461c-a3a1-b082f0fff3d0",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "ec4f40cb-c4c9-433e-91d1-bac586606fad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T11:17:25.990Z_

```json
{
  "parentUuid": "9e79dcae-f997-461c-a3a1-b082f0fff3d0",
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
  "uuid": "481e9310-b36e-45be-9f10-1772dac71ed3",
  "timestamp": "2026-05-16T11:17:25.990Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "ec4f40cb-c4c9-433e-91d1-bac586606fad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T11:17:25.990Z_

```json
{
  "parentUuid": "481e9310-b36e-45be-9f10-1772dac71ed3",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "69713ca9-3b6f-4fd5-9dc2-d4d75738cf28",
  "timestamp": "2026-05-16T11:17:25.990Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "ec4f40cb-c4c9-433e-91d1-bac586606fad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T11:17:25.990Z_

```json
{
  "parentUuid": "69713ca9-3b6f-4fd5-9dc2-d4d75738cf28",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "cd88c80b-ebbf-42d9-a525-65f6fd719cef",
  "timestamp": "2026-05-16T11:17:25.990Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "ec4f40cb-c4c9-433e-91d1-bac586606fad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Test set 不 generalize 或 decoupling 跨家族不复现，核心 claim 需要 reframe 核心假设：['Test set RSFT vs SFT Δ < 2pp 或不显著（dev-test gap 大，可能因 DocRED test 分布偏移）', '或 LLaMA GRP…",
  "leafUuid": "cd88c80b-ebbf-42d9-a525-65f6fd719cef",
  "sessionId": "ec4f40cb-c4c9-433e-91d1-bac586606fad"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterize worst-case outcomes for evidence-grounded DocRE",
  "sessionId": "ec4f40cb-c4c9-433e-91d1-bac586606fad"
}
```

---

### Assistant

_source line 9 · 2026-05-16T11:21:52.519Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each "planned" experiment in the experiment_plan, under the "worst" tier scenario. Let me identify which experiments are still "planned":

Looking at the experiment_plan:
1. plan_002 - Test set evaluation - status: planned
2. plan_006 - Model size ablation (1.7B/8B) - status: planned
3. plan_007 - Re-DocRED cross-dataset - status: planned
4. plan_016 - LLaMA-3.1-8B cross-family validation - status: planned


5. plan_013 - EDCR human validation - status: planned
6. plan_010 - NLI model ablation - status: planned

But I'm noticing some of these have registry entries showing they're already running or completed, so I need to reconcile the plan status with what's actually happening in the registry.

Looking at the discrepancies: plan_002 shows as planned but has a test eval running, plan_006 is marked planned but has multiple completed SFT runs and an eval in progress, plan_016 is planned but has an 8B SFT running. The others (plan_007, plan_013, plan_010) don't have registry entries yet.

So the six experiments I need to cover are plan_002, plan_006, plan_007, plan_016, plan_013, and plan_010. Now I'm thinking through what constitutes a "worst" tier result for each one — essentially when the test set doesn't generalize or the decoupling effect doesn't replicate across model families, which would mean the core claim needs rethinking. The key metric is whether the RSFT vs SFT improvement on the test set is less than 2 percentage points or statistically insignificant, which would suggest the dev-test gap is too large, possibly from distribution shift in the test data.

For the specific failure modes I'm tracking: GRPO with QLoRA doesn't show the catastrophic decoupling we'd expect if the spectrum becomes Qwen-specific, the CED versus flat-NLI comparison isn't significant despite high baseline probability, the 1.7B and 8B results contradict the 4B direction suggesting the evidence tax effect is unstable across model scales, and the human validation of EDCR annotations is weak with low inter-rater agreement and ambiguous labels. I'm also compiling the metric ranges to establish what "worst" looks like numerically across these dimensions.

Now I'm looking at the cross-model RSFT versus SFT deltas and the relative performance gaps, and I'm noticing the test set evaluation for plan_002 will likely show much smaller gains than dev—the +5.49pp improvement on the best CED model probably won't hold because DocRED's test set has known distribution shift from different annotators and document sources.

For the model size ablation in plan_006, I'm concerned the 1.7B and 8B results might diverge significantly from the 4B baseline—the smaller model could struggle with the added complexity of RSFT and show negative gains, while the larger model might handle the multi-task learning so well that the evidence generation cost becomes negligible. some results: f1=0.4945, ign_f1=0.4786, evi_f1=0.8316. That's actually quite good - better than 4B SFT (ign_f1=0.4036). But this is with evidence. The no-evidence eval is running.

For worst case on the parts still planned (RSFT on 1.7B and 8B):
- 1.7B RSFT: gains might be minimal or negative (model too small for RSFT to help)
- 8B RSFT: gains might be inconsistent direction

Actually, let me re-read. The experiment_plan says plan_006 status is "planned" even though some sub-experiments are running. I should predict the overall outcome.

For worst tier:
- 1.7B: evidence tax might be much larger or much smaller than 7pp, breaking the narrative
- 8B: RSFT gains unstable, evidence tax disappears
- Cross-model RSFT-SFT delta likely between 0.0 and 2.0

Looking at plan_007 on Re-DocRED, RSFT probably won't help much since the dataset has ~55% triples without evidence annotations, making it too messy for reliable gains. Plan_016 with LLaMA shows the decoupling issue is specific to Qwen, not a general RL-for-IE problem - the cross-family results should fall between 0.1 and 0.4 relative F1. Plan_013 on EDCR human validation is still pending.

For plan_010, the NLI model ablation shows DeBERTa-base and large perform similarly, suggesting the CED approach isn't particularly sensitive to NLI model quality. Now I'm working through the YAML output and need concrete numbers for plan_002. Looking at DocRED test set performance, the SFT baseline with evidence gets around 39.5 Ign-F1 (a slight drop from the dev set), while RSFT with CED peaks around 41.0 Ign-F1 - though that's a significant drop from the dev performance of 45.85, likely because...

RSFT overfits to the dev distribution since it uses dev-set-derived scoring to filter training data. The delta between them is roughly 1.5 percentage points, which falls within the noise range and isn't statistically significant. For the CED versus flat-NLI comparison, I already have seed data across multiple runs that I can use to test significance, though I'm realizing I need to double-check which seeds I have complete data for.

Now I'm looking at what's actually planned versus what's already running or done. The six planned experiments I need to generate predictions for are plan_002, plan_006, plan_007, plan_016, plan_013, and plan_010. For plan_006 specifically, some of the sub-experiments are already in progress—the 1.7B SFT baseline is finished with an ign_f1 of 0.4786, the 1.7B no-evidence variant is trained and currently being evaluated, and the 8B SFT is still pending.

For plan_002, I'm predicting the test set performance on the worst tier where there's known distribution shift. The RSFT gains on the dev set don't translate well to the test set due to the CED scoring being dev-aligned, so I'm expecting the test Ign-F1 to drop significantly from the dev performance—SFT around 39.8 and RSFT around 41.2, giving roughly a 1.4 percentage point delta.

But I need to be precise about which checkpoint I'm using. The test eval is specifically running with s44, so let me recalculate based on the actual dev results: RSFT CED s44 achieved 45.11 Ign-F1 versus the SFT baseline at 40.36, which is a 4.75 percentage point improvement on dev. Now I'm working through what that translates to on the test set given the distribution shift.

Looking at the test results, the delta shrinks significantly to just 1.3 percentage points — SFT baseline at 39.5 Ign-F1 versus RSFT CED s44 at 40.8. For plan_006, I'm comparing the model sizes and noticing something odd: the 1.7B SFT model shows 47.86 Ign-F1 while the 4B SFT model is at 39.74, which doesn't make intuitive sense, so I need to verify whether they're using different evaluation sets or checkpoints.

What's really interesting is that the evidence tax appears to be model-size-dependent rather than a fixed 7 percentage points — the 1.7B model shows only about 1 point of degradation without evidence, whereas the 4B model drops 7 points, and projecting forward, the 8B model might actually perform better without evidence than with it, which completely contradicts the pattern I was seeing before. Looking at the instability across model scales: 1.7B might show negative RSFT gains while 8B shows minimal improvement, which contradicts the consistent ~7pp evidence tax pattern we see in 4B. For Re-DocRED, the sparse evidence annotations and lower annotation quality mean RSFT versus SFT deltas could swing negative, and the CED scoring won't transfer reliably. With LLaMA, the GRPO results show rel_f1 staying in a reasonable range without catastrophic decoupling, suggesting this failure mode is specific to Qwen rather than a general phenomenon across model families. For the human validation work, I'm looking at the correlation metrics to assess agreement quality.

Now I'm compiling the specific numerical predictions for the main experiments, starting with the test set results for plan_002.

For plan_006, I'm comparing how the evidence penalty scales across model sizes—the 1.7B model shows a much smaller evidence tax of 1.3pp compared to 4B's 7pp, and RSFT provides only marginal gains around 0.6-0.8pp across both sizes, suggesting the approach has limited effectiveness at smaller scales.

But I'm noticing something odd: the 1.7B result shows ign_f1=47.86, which is actually higher than the 4B baseline at 39.74. That's counterintuitive—I'd expect larger models to perform better, so either the 1.7B variant is genuinely better optimized for this task, or there's something different about how these models were trained or evaluated.

Looking at the LLaMA results, the pattern seems different: SFT performance is competitive with Qwen's 4B, RSFT shows modest gains, and GRPO QLoRA degrades but not catastrophically. This suggests the decoupling issue might be specific to Qwen rather than a universal problem across model families. I should compile these observations into the YAML structure now, being careful about the actual numbers and what they reveal about generalization across scales. B the tax is 2pp, then the "7pp evidence tax" isn't a general finding—it's specific to the 4B model. For the 8B, the training loss is lower than both smaller models, suggesting better fitting, so I'd estimate ign_f1 around 48-50. Since the eval is still running, I'll work with worst-case predictions and write out the YAML with specific rationale for the planned experiments.

Now I'm laying out the remaining experiments: cross-dataset evaluation on DocRED, cross-family testing with LLaMA, human validation for EDCR, and ablations on the NLI component. The core narrative is shifting toward understanding faithfulness costs in generative IE, where the evidence tax appears inconsistent across model scales and the decoupling effect might be Qwen-specific rather than universal.

Writing experiment configuration... 现在我在查看 RSFT CED 在 DocRED 官方测试集上的具体性能指标，包括 Ign-F1 和 F1 分数的提升幅度，以及证据级别的表现。测试结果显示相比基础 SFT 方法有约 1.3 个百分点的改进，但我注意到开发集和测试集之间存在较大的性能差距，这可能反映了测试集标注一致性的问题。

我在分析为什么 RSFT 在开发集上的 5pp 增益在测试集上大幅下降到 1.3pp——这似乎是因为 CED 评分函数在开发集的特定关系类型分布和证据模式上过拟合了，导致这种自改进信号在测试集上失效。

虽然证据质量相对稳定，但关系抽取性能严重退化，因为测试集的关系类型分布与开发集差异很大。现在我在查看测试集的具体结果表来量化这种性能下降。 The core issue is that RSFT's scoring function relies on dev set gold labels to compute F1, which makes it inherently dev-set-aware semi-supervised learning—so when generalizing to a test set with different distribution, the performance gains naturally compress. I need to reframe the paper away from claiming RSFT significantly boosts performance, and instead focus on quantifying the evidence generation cost and analyzing how to decouple it. Next, I'm planning model size ablations across Qwen3-1.7B and 8B to verify whether the evidence tax and RSFT gains remain consistent across different model scales.

Now I'm looking at the expected metrics across both model sizes—comparing SFT baselines, no-evidence variants, and RSFT performance to see how the evidence tax and delta patterns hold up. The 1.7B model shows stronger inherent relation extraction capabilities, likely due to pre-training advantages on Wikipedia-style documents, so evidence generation doesn't impose a significant additional burden. As model capacity increases to 8B, the evidence tax compresses to around 1.5pp since larger models can better parallelize both RE and evidence generation tasks. The RSFT gains shrink to less than 1pp on 1.7B and 8B because SFT already approaches the model's ceiling, leaving little room for self-improvement—suggesting that both the 7pp evidence tax and 3-5pp RSFT recovery are specific to the 4B model rather than general findings.

Now I'm looking at the model size ablation results across different scales, which reveals that the paper's core narrative is undermined—I can't claim evidence tax is a fundamental cost of generative IE, only that it manifests differently depending on model size.

The data shows an anomalous pattern where the 4B model exhibits a dramatic 7 percentage point evidence tax, while the 1.7B and 8B models show much smaller costs around 1-1.5pp. This U-shaped or V-shaped relationship suggests the 4B result is likely an outlier rather than evidence of a consistent scaling trend, possibly due to pre-training differences within the Qwen3 series using different data configurations or training recipes.

The RSFT improvements are consistent across scales, but this doesn't salvage the evidence tax narrative since the underlying phenomenon itself isn't monotonic with model size.

My approach is to report these model-size ablations honestly—acknowledging that the magnitude of evidence tax varies by model—while emphasizing that the core finding holds: across all scales, models perform better without evidence than with it. The decoupling spectrum analysis doesn't depend on the absolute tax values anyway, so that contribution stands independently.

Now I'm planning to validate the approach on Re-DocRED using the best configuration to test cross-dataset generalization.  I need to account for the fact that about 55% of the triples in Re-DocRED lack evidence annotations, and I'm looking at the expected performance metrics across different evaluation settings and configurations.

The key insight is that RSFT gains don't transfer to the worst tier because the CED scoring function was trained on DocRED's gold standard, but Re-DocRED has a different evidence distribution due to corrections made during re-annotation. This mismatch reduces CED's ability to discriminate Re-DocRED evidence effectively. Additionally, Re-DocRED's relation distribution is more balanced than DocRED's, so the biases RSFT learned from DocRED's skewed distribution don't apply here.

The evidence-only evaluation only covers 43% of triples, which isn't enough for statistical significance testing. The evidence tax on Re-DocRED is about 5.5 percentage points (lower than DocRED's 7pp) because Re-DocRED has higher relation density with more gold triples per document, spreading the evidence generation burden across more instances. However, RSFT only recovers 1.3pp compared to 5.5pp on DocRED, which isn't statistically significant.

Looking at the Re-DocRED results table, the RSFT gains of 1.3pp match what we see on the test set, confirming that the improvements are specific to DocRED's development set characteristics and don't generalize well to the new dataset.

The evidence-only subset shows lower F1 scores around 75-76% compared to DocRED's ~81%, likely due to stricter annotation standards in Re-DocRED, and with only 43% coverage, we don't have enough statistical power to draw strong conclusions from the evidence evaluation.

Now I'm planning to validate whether this decoupling pattern holds across different model families by running the full SFT to RSFT to GRPO pipeline on LLaMA-3.1-8B.

Compiling expected performance metrics... qlora_ign_f1: 27.5
      decoupling_severity: "moderate (not catastrophic)"
    result_rationale: >
      LLaMA-3.1-8B 的 GRPO QLoRA 不出现 catastrophic decoupling 的原因：
      (1) LLaMA 3.1 的 pre-training 更注重 instruction following 的鲁棒性，RL 压力下的 objective competition 不如 Qwen 剧烈；
      (2) LLaMA 的 tokenizer 对英文文档的 token efficiency 更高（相比 Qwen 的中英双语 tokenizer），
      相同 max_length 下 LLaMA 有更多容量同时编码 RE + evidence；
      (3) QLoRA 4-bit 量化对 LLaMA 的影响可能不如对 Qwen 严重——LLaMA 在量化场景下被广泛测试和优化，权重分布更适合 4-bit 量化。结果上，LLaMA 的 rel_f1 ~0.28（相比 Qwen 的 0.0138），虽然退化了约 15 个百分点但远未达到灾难性程度，EDCR ~0.78 表现为中等程度的解耦而非 Qwen 的灾难性 0.99。这说明"QLoRA 放大解耦到灾难性程度"是 Qwen 特有的现象，而非 RL-for-IE 的普遍规律。

现在我需要检查 decoupling spectrum 的排序是否在 LLaMA 上重现。我在编译一个跨模型族的对比表，看看 SFT 基线、evidence tax、RSFT 改进幅度、以及 GRPO QLoRA 的相对 F1 分数在两个模型上的表现是否一致。初步数据显示基线性能相近，但改进幅度存在差异——这表明我需要将核心发现重新定位为"模型族特定现象"而非通用规律。

Generating comparison table... I'm considering how to reframe the paper's claims given that catastrophic decoupling only appears in Qwen. I could either narrow Claim 2 to focus specifically on Qwen's vulnerability to RL optimization pressure, or present a weaker version acknowledging that decoupling exists across models but varies in severity—LLaMA shows moderate degradation rather than catastrophic failure. The title might shift from "Why RL fails" to something more precise about when and why RL degrades performance. RSFT shows similar patterns across both models, though the gains are smaller on LLaMA, which at least provides some consistency to the narrative. Now I'm planning human validation with 100 annotated examples. 判断每个 cited evidence sentence 是否真正支持对应 relation，计算 EDCR 与人工判断的 Spearman ρ。现在看到的结果数据显示 inter-annotator agreement 为 0.55，EDCR 与人工判断的相关性只有 0.42，这反映了几个关键问题：首先，evidence 标注本身就很主观——某些句子是否"支持"一个关系存在灰色地带，比如关于董事会会议的句子是否支持子公司关系就很模糊，约 28% 的样本都落在这个模糊区间；其次，EDCR 依赖 NLI 模型的 entailment score，但 NLI 训练数据是自然语言推理对，而 IE evidence 是文档句子级引用，两者的语义粒度不匹配，导致 calibration 不理想；最后，方法级别的高相关性（ρ=-0.965）部分来自极端情况的影响。

Generating validation metrics... The per-relation diagnostic capability is undermined if EDCR only correlates with human judgment at ρ=0.42, especially given that inter-annotator agreement itself is modest at κ=0.55, suggesting the task's inherent subjectivity partially explains the weak alignment. Now I'm considering how DeBERTa model size affects the quality of training data for RSFT. 我认为关键在于任务转换过程中的信息损失——将结构化的三元组和证据句子转换为NLI格式时，丢失的信息超过了模型规模差异带来的收益。此外，两个模型在区分强证据和明显干扰项上表现相近，差异只体现在难负样本上，而RSFT的严格筛选策略已经大幅限制了CED分数差异的影响空间。

现在看到的是，改变排序策略后，上游NLI模型的差异被下游选择机制吸收了，0.5个百分点的差异在统计上不显著，这说明CED的价值更多来自对比评分的结构设计，而非NLI模型本身的绝对能力。

Generating ablation table...

这个中立的发现意味着工程选择（base vs large模型）对论文结论没有影响，但也暗示CED评分的质量上限可能不受NLI骨干网络的制约。审稿人可能会质疑，如果NLI模型质量无关紧要，那么CED的"基于NLI"标签是否有误导性，CED的真正贡献可能需要重新定位。

现在我在验证是否覆盖了所有六个计划的实验，并检查数值是否在指定范围内。

所有的指标都符合要求，包括 RSFT 对比 SFT 的 F1 差值、跨模型性能差异、以及各种评估指标的相对值。CED 与平坦 NLI 的显著性检验已经通过已收集的种子数据隐含地纳入了分析框架。

现在我在整理 CED 种子的 ign_f1 分数，已经有 s42、s43、s44、s45 四个种子的数据，但需要再补充一个。我在核对这些重新评估的数字，确保它们来自同一个评估流程——s42 的 ign_f1 是 0.4423，s43 是 0.4512，s44 和 s45 的数据也都已记录，现在需要找到第五个种子的对应分数。

现在我看到了 flat-NLI 的完整数据，四个种子的 ign_f1 分数分别是 0.4448、0.4503、0.4521 和 0.4462，计算出平均值是 0.4484。对应的 CED 平均值是 0.4466，两个数据集的表现很接近。

虽然这个对比很有意思，但用户问的是计划中的实验，而 CED 对比 flat-NLI 的种子已经基本完成了。

我注意到论文框架中提到的 RSFT CED s43 最佳结果是 45.85，但重新评估给出的是 0.4512，这两个数字不一致，我需要仔细核对一下数据来源。

看起来有两个不同的 s43 评估结果，差异可能来自不同的评估配置。我会用重新评估的数字作为基准来预测最差层级的测试性能下降。

重新评估的数字看起来更一致，纸质表格可能在某些行使用了不同的指标或评估条件。对于测试集预测，我用 s44 的重新评估值作为开发基线，预测测试性能在 40.5，这给出 RSFT 的开发到测试差距约 4.6 个百分点。SFT 的转移效果更好，差距只有 0.5 个百分点，这是一个现实的最坏情况：SFT 表现稳定但 RSFT 性能下降明显。

现在我需要更仔细地考虑 1.7B 的结果。1.7B SFT 的评估显示 ign_f1 明显优于 4B，这已经是真实数据。对于最坏情况，1.7B 无证据评估可能显示的证据税很小，远低于 4B 的 7 个百分点。

我预测 1.7B 的 ign_f1 约为 49.0，税率约 1.1pp，这在最坏情况范围内但不是极端情况。对于 8B，我预测 ign_f1 约为 49.5，无证据约 51.0，税率约 1.5pp。这些数字对最坏情况来说是合理的，现在我可以最终确定并输出结果。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd88c80b-ebbf-42d9-a525-65f6fd719cef",
  "isSidechain": false,
  "requestId": "req_011Cb69uxtusoHiB4bqcADER",
  "type": "assistant",
  "uuid": "7e720e0d-f087-475e-af00-734c3dd482e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "ec4f40cb-c4c9-433e-91d1-bac586606fad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lqt3HtPxec9jeJwZ7Gi9ur",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 33378,
      "cache_read_input_tokens": 11447,
      "output_tokens": 23064,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33378,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 23064,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 33378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33378
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

_source line 10 · 2026-05-16T11:24:44.403Z_

```yaml
tier: worst
narrative_guidance: >
  Reframe 为分析/诊断贡献论文。Test set RSFT vs SFT 增益不显著（<2pp），
  decoupling 可能是 Qwen-specific（LLaMA 不复现 catastrophic failure），
  evidence tax 在不同模型规模下不一致（1.7B/8B 远小于 4B 的 7pp）。
  核心叙事转向 "Understanding the cost of faithfulness in generative IE"——
  evidence generation 代价存在但 magnitude 是 model-specific，EDCR 作为方法级诊断工具仍有独立价值。
  Scope 收缩为 Qwen3-4B 深度 case study + 跨规模/跨家族的辅助验证显示 findings 不完全泛化。
  目标降级为 EMNLP Findings track。

imagined_experiments:
  - name: "Test set evaluation (RSFT CED s44)"
    plan_id: "plan_002"
    description: >
      在 DocRED 官方 test set 上评估 RSFT CED s44，提交 CodaLab 获取官方 Ign-F1/F1。
      同时评估 SFT baseline 和 SFT no-evidence 作为对照。
    expected_results:
      test_sft_ign_f1: 39.2
      test_sft_f1: 40.8
      test_sft_evi_f1_cond: 79.5
      test_rsft_ced_s44_ign_f1: 40.5
      test_rsft_ced_s44_f1: 42.1
      test_rsft_ced_s44_evi_f1_cond: 79.8
      test_rsft_vs_sft_ign_f1_delta: 1.3
      test_rsft_vs_sft_f1_delta: 1.3
      test_edcr_sft: 0.71
      test_edcr_rsft: 0.66
      test_no_evidence_ign_f1: 45.8
      dev_test_ign_f1_gap_sft: 0.8
      dev_test_ign_f1_gap_rsft: 4.6
      bootstrap_p_value: 0.12
    result_rationale: >
      DocRED test set 由不同标注者完成，Tan et al. (2022) 已报告 test 标注一致性低于 dev。
      SFT baseline 跨 dev→test 下降小（~0.8pp），因其直接学习 gold label 分布，泛化稳定。
      但 RSFT 增益高度依赖 dev set 分布：CED scoring 在 dev gold 上计算 F1 过滤训练样本，
      scoring function 隐式过拟合 dev 的 relation type 分布和 evidence pattern。
      具体机制——RSFT 选出的 2718 训练样本中，高 F1 的 relation types（如 country, instance_of）
      被系统性富集，这些 types 在 dev 上频率高但 test 上分布可能不同。
      当 test set 的 relation type 长尾分布偏移时，RSFT 学到的 dev-aligned self-improvement 信号失效，
      增益从 dev +5.1pp（s44 reeval）压缩到 test +1.3pp。
      Evidence 质量（evi_f1）跨集相对稳定（~79.5-79.8），因为 evidence 引用模式依赖
      文档结构而非 relation 分布。
      Bootstrap p=0.12，未达 0.05 显著性门槛。
    tables:
      - name: "Table: Test Set Main Results"
        headers: ["Config", "Ign-F1", "F1", "Δ Ign-F1 vs SFT", "Evi-F1 (cond)", "EDCR"]
        rows:
          - ["SFT no-evidence", "45.8", "47.2", "+6.6pp", "—", "—"]
          - ["SFT baseline", "39.2", "40.8", "—", "79.5", "0.71"]
          - ["RSFT CED s44", "40.5", "42.1", "+1.3pp", "79.8", "0.66"]
      - name: "Table: Dev-Test Generalization Gap"
        headers: ["Config", "Dev Ign-F1", "Test Ign-F1", "Gap"]
        rows:
          - ["SFT", "39.74", "39.2", "-0.5pp"]
          - ["RSFT CED s44", "45.11", "40.5", "-4.6pp"]
          - ["No-evidence SFT", "47.21", "45.8", "-1.4pp"]
    figures_description:
      - "Dev vs Test gap grouped bar chart：SFT gap 0.5pp vs RSFT gap 4.6pp，直观展示 RSFT 的 dev-overfitting"
    analysis: >
      RSFT dev-test gap（4.6pp）远大于 SFT（0.5pp），说明 CED scoring 导致的 dev-specific
      样本选择是 gap 的主因。Delta 1.3pp 在 paired bootstrap test 下 p≈0.12（基于
      DocRED test ~700 docs 和 RSFT 在 dev 上 4-seed std ~0.5pp）。
      核心问题：RSFT 本质是 dev-set-aware 的 semi-supervised learning——
      用 dev gold 计算 F1 来选 training data，泛化到分布不同的 test set 时增益被压缩是结构性的。
      Reframe 方向：不以 "RSFT significantly outperforms SFT" 为核心 claim，
      转向 evidence tax 量化（test 上 SFT 39.2 vs no-evidence 45.8 = 6.6pp，与 dev 接近）
      和 decoupling 分析。Evidence tax 在 test 上仍然显著，这是可保留的 finding。

  - name: "Model size ablation (Qwen3-1.7B / 8B)"
    plan_id: "plan_006"
    description: >
      在 Qwen3-1.7B 和 8B 上复现完整 pipeline：SFT → no-evidence SFT → RSFT → eval。
      验证 evidence tax 和 RSFT 增益跨模型规模的一致性。
      1.7B SFT eval 已完成（ign_f1=47.86），结果反常地高于 4B（39.74）。
    expected_results:
      qwen3_1_7b_sft_ign_f1: 47.86  # 已知
      qwen3_1_7b_sft_evi_f1: 83.16  # 已知
      qwen3_1_7b_no_evidence_ign_f1: 49.0
      qwen3_1_7b_evidence_tax_pp: 1.1
      qwen3_1_7b_rsft_ced_ign_f1: 48.5
      qwen3_1_7b_rsft_vs_sft_delta_pp: 0.6
      qwen3_1_7b_rsft_evi_f1: 83.5
      qwen3_8b_sft_ign_f1: 49.5
      qwen3_8b_sft_evi_f1: 82.8
      qwen3_8b_no_evidence_ign_f1: 51.0
      qwen3_8b_evidence_tax_pp: 1.5
      qwen3_8b_rsft_ced_ign_f1: 50.3
      qwen3_8b_rsft_vs_sft_delta_pp: 0.8
      qwen3_8b_rsft_evi_f1: 83.0
      cross_model_evidence_tax_range: "1.1pp ~ 7.0pp"
      cross_model_rsft_sft_delta_min: 0.6
    result_rationale: >
      1.7B SFT ign_f1=47.86 反常高于 4B（39.74）已经是实际观测。可能原因：
      Qwen3 不同规模模型使用不同 pre-training data mixture 和 recipe——1.7B 可能在
      Wikipedia/knowledge-intensive 任务上有更好的数据配比（小模型训 token 数/参数量比值更高）。
      Evidence tax 与 capacity bottleneck 相关：4B 的 7pp tax 反映模型同时处理 RE + evidence
      生成时的 severe capacity competition。1.7B 本身 RE 能力更强（隐含其语言理解
      在 DocRE 域更好），evidence 生成的 marginal 负担更小→ tax 仅 1.1pp。
      8B 容量最大，evidence tax 也小（~1.5pp），但 RSFT 增益被压缩到 0.8pp——
      因为 SFT 已经接近模型上限（ign_f1 49.5），self-improvement 空间极小。
      Evidence tax 跨规模从 7.0pp（4B）到 1.1pp（1.7B）到 1.5pp（8B），
      没有 monotonic trend——4B 是 anomalous peak 而非 representative baseline。
      RSFT 增益跨规模从 +5.5pp（4B）到 +0.6pp（1.7B）到 +0.8pp（8B），
      说明 RSFT 有效性高度依赖 SFT 与模型上限间的 gap 大小。
    tables:
      - name: "Table: Model Size Ablation (Worst Tier)"
        headers: ["Model", "SFT Ign-F1", "No-Evi Ign-F1", "Evi Tax", "RSFT Ign-F1", "RSFT Δ"]
        rows:
          - ["Qwen3-1.7B", "47.86", "49.0", "1.1pp", "48.5", "+0.6pp"]
          - ["Qwen3-4B", "40.36†", "47.36", "7.0pp", "45.85*", "+5.5pp"]
          - ["Qwen3-8B", "49.5", "51.0", "1.5pp", "50.3", "+0.8pp"]
    figures_description:
      - "Evidence tax vs model size：非 monotonic（4B 是 peak），无法 claim tax 是 universal constant"
      - "RSFT Δ vs SFT-ceiling gap scatter：RSFT 增益与 SFT→ceiling gap 正相关，增益非方法固有"
    analysis: >
      4B 的 7pp evidence tax 是三个规模中的极端值（1.7B 1.1pp, 8B 1.5pp），
      无法支撑 "evidence generation 有 ~7pp fundamental cost" 的 claim。
      论文需改为："evidence tax exists across scales（方向一致）but magnitude is
      model-and-scale-specific"——这是弱得多的 claim。
      1.7B > 4B 的反常结果（Qwen3 系列内部的 scaling 非 monotonic）给 reviewer
      增加攻击面："你的 baseline model choice 可能是 cherry-picked worst case"。
      RSFT 增益跨规模不一致使得 RSFT 作为方法的价值降低——它只在 SFT 表现差
      （有大 gap 可填补）时有效。
      Reframe：evidence tax 的 *existence* 是一致发现（所有规模 no-evi > with-evi），
      magnitude 分析展示了 model capacity 与 multi-task generation 的交互效应。

  - name: "Re-DocRED cross-dataset evaluation"
    plan_id: "plan_007"
    description: >
      在 Re-DocRED 上完整 pipeline（SFT → RSFT → eval）。Re-DocRED 与 DocRED 共享 96 relation types
      但重标注修正了 false negatives。~55% triples 无 evidence 标注，需 evidence_only 和 full 两种模式评估。
    expected_results:
      re_docred_sft_ign_f1: 38.5
      re_docred_sft_rel_f1: 39.2
      re_docred_sft_evi_f1_evidence_only: 75.3
      re_docred_rsft_ign_f1: 39.8
      re_docred_rsft_rel_f1: 40.5
      re_docred_rsft_evi_f1_evidence_only: 76.1
      re_docred_rsft_vs_sft_ign_f1_delta: 1.3
      re_docred_no_evidence_ign_f1: 44.0
      re_docred_evidence_tax_pp: 5.5
      evidence_only_triple_coverage: 0.43
      re_docred_edcr_sft: 0.73
      re_docred_edcr_rsft: 0.68
      bootstrap_p_rsft_vs_sft: 0.18
    result_rationale: >
      Re-DocRED RSFT 增益不迁移有两层原因：
      (1) CED scoring function 在 DocRED gold 上校准。Re-DocRED 重标注修正了大量 DocRED
      的 false negative triples，evidence 标注也相应变化——CED 学到的 "what constitutes good
      evidence" 在 Re-DocRED 语境下 miscalibrated。具体表现：DocRED 中被 CED 评为高分的
      evidence pattern（往往是简单、直接的 relation mention），在 Re-DocRED 的更完整标注下
      不再具有代表性——Re-DocRED 有更多 complex reasoning chain 型 evidence。
      (2) Re-DocRED 的 relation distribution 更均匀（修正 false negative 后长尾被填充），
      而 RSFT 在 DocRED 偏态分布上选出的训练样本集偏向 head relations，
      这种 distributional bias 在 Re-DocRED 上构成 negative transfer。
      Evidence-only 评估仅覆盖 43% triples（~5200 of ~12000），evi_f1 低于 DocRED（75 vs 80）
      因为 Re-DocRED evidence 标注更严格。Sample size 不足导致 bootstrap p=0.18。
      Evidence tax 在 Re-DocRED 上 ~5.5pp（vs DocRED 7pp），进一步说明 tax 是 data-specific。
    tables:
      - name: "Table: Re-DocRED Results"
        headers: ["Config", "Ign-F1", "Rel-F1", "Evi-F1 (evi-only)", "Δ vs SFT"]
        rows:
          - ["SFT no-evidence", "44.0", "44.8", "—", "+5.5pp"]
          - ["SFT baseline", "38.5", "39.2", "75.3", "—"]
          - ["RSFT CED", "39.8", "40.5", "76.1", "+1.3pp"]
      - name: "Table: Cross-Dataset Comparison"
        headers: ["Metric", "DocRED Dev", "DocRED Test†", "Re-DocRED"]
        rows:
          - ["Evidence Tax", "7.0pp", "6.6pp", "5.5pp"]
          - ["RSFT Δ vs SFT", "+5.1pp", "+1.3pp", "+1.3pp"]
          - ["Evi-F1 (cond)", "81%", "~80%", "76%"]
    figures_description:
      - "Cross-dataset RSFT delta comparison：三个 eval 条件（dev/test/Re-DocRED）下 RSFT 增益的衰减趋势"
    analysis: >
      Re-DocRED delta 1.3pp 与 DocRED test delta 1.3pp 高度一致——两个 out-of-distribution
      评估得到相同结论：RSFT-CED 增益是 DocRED-dev-specific。
      Evidence tax 跨数据集不恒定（7pp→5.5pp）进一步支撑 "tax magnitude is data-specific"。
      43% evidence coverage 使 evidence 评估可信度不足（单独作为 cross-dataset 验证不够 compelling）。
      论文可以诚实报告两组 OOD 数据一致表明 RSFT 增益泛化有限，
      但 evidence tax 的 *existence* 和 *direction* 在 Re-DocRED 上复现。

  - name: "LLaMA-3.1-8B cross-family validation"
    plan_id: "plan_016"
    description: >
      在 LLaMA-3.1-8B 上复现 SFT → RSFT → GRPO QLoRA pipeline。
      核心验证：decoupling spectrum 是否跨模型家族成立——尤其是 GRPO QLoRA 是否也 catastrophic。
    expected_results:
      llama_sft_ign_f1: 42.5
      llama_sft_rel_f1: 43.0
      llama_sft_evi_f1: 80.2
      llama_sft_edcr: 0.70
      llama_no_evidence_ign_f1: 48.0
      llama_evidence_tax_pp: 5.5
      llama_rsft_ced_ign_f1: 44.8
      llama_rsft_rel_f1: 45.5
      llama_rsft_evi_f1: 81.0
      llama_rsft_vs_sft_delta_pp: 2.3
      llama_grpo_qlora_rel_f1: 0.28
      llama_grpo_qlora_ign_f1: 27.5
      llama_grpo_qlora_evi_f1: 0.82
      llama_grpo_qlora_edcr: 0.78
      decoupling_severity: "moderate, not catastrophic"
      qwen_grpo_qlora_rel_f1_for_reference: 0.0138
    result_rationale: >
      LLaMA-3.1-8B GRPO QLoRA 不出现 catastrophic decoupling（rel_f1 0.28 vs Qwen 0.0138）：
      (1) Quantization robustness：LLaMA 系列是 4-bit 量化研究的主要 testbed（GPTQ/AWQ/bitsandbytes
      论文大多以 LLaMA 为实验对象），其权重分布经社区广泛验证在 4-bit 下保持较好精度——
      QuRL (2024) 发现 quantized-full precision divergence 在不同 architecture 间差异巨大。
      Qwen3 的中英双语 embedding 层在 4-bit 量化下可能有更大信息损失。
      (2) Tokenizer efficiency：LLaMA tokenizer 对英文 Wikipedia 文档的 token/word ratio
      更低（~1.2 vs Qwen ~1.4），相同 max_new_tokens 下 LLaMA 有更多有效容量
      同时编码 RE triples 和 evidence sentences——capacity bottleneck 更宽松。
      (3) Pre-training RL alignment：LLaMA-3.1 经过更 heavy 的 RLHF 阶段，
      模型对 RL 优化压力的鲁棒性更强（optimization landscape 更平坦），
      不易在 RL fine-tuning 中发生 sudden mode collapse。
      结果：LLaMA GRPO QLoRA rel_f1=0.28（退化 ~15pp，moderate），EDCR=0.78（moderate decoupling），
      远非 Qwen 的 catastrophic（rel_f1=0.0138，EDCR=0.99）。
      Decoupling 确实存在（rel_f1 下降），但 severity 与 Qwen 完全不同级别。
      这意味着 "QLoRA amplifies to catastrophic" 是 Qwen-specific，不是 universal。
    tables:
      - name: "Table: Cross-Family Decoupling Comparison"
        headers: ["Config", "Qwen3-4B", "LLaMA-3.1-8B", "Pattern Consistent?"]
        rows:
          - ["SFT Ign-F1", "40.36", "42.5", "✓ similar range"]
          - ["Evidence Tax", "7.0pp", "5.5pp", "~ direction same, magnitude differs"]
          - ["RSFT Δ vs SFT", "+5.5pp", "+2.3pp", "✗ magnitude halved"]
          - ["GRPO QLoRA rel_f1", "0.014", "0.28", "✗✗ catastrophic NOT reproduced"]
          - ["GRPO QLoRA EDCR", "0.99", "0.78", "✗ moderate vs catastrophic"]
          - ["GRPO QLoRA evi_f1", "0.85", "0.82", "✓ both high"]
      - name: "Table: LLaMA Full Pipeline"
        headers: ["Config", "Ign-F1", "Evi-F1", "EDCR", "Δ vs SFT"]
        rows:
          - ["SFT no-evidence", "48.0", "—", "—", "+5.5pp"]
          - ["SFT baseline", "42.5", "80.2", "0.70", "—"]
          - ["RSFT CED", "44.8", "81.0", "0.65", "+2.3pp"]
          - ["GRPO QLoRA", "27.5", "82.0", "0.78", "-15.0pp"]
    figures_description:
      - "Decoupling spectrum 并排对比图：Qwen（catastrophic drop）vs LLaMA（moderate drop），GRPO QLoRA 行为完全不同"
      - "GRPO training dynamics 对比：Qwen rel_f1 急剧归零 vs LLaMA rel_f1 缓慢下降但 plateau"
    analysis: >
      LLaMA 数据根本性地改变 Claim 2 的叙事范围。
      Catastrophic decoupling 不跨家族复现 → "RL optimization pressure 与 decoupling severity
      正相关" 的 universal claim 不成立。可保留的弱版 claim：
      "Decoupling exists across model families（LLaMA 也有 15pp 退化）but catastrophic
      amplification by QLoRA is architecture-dependent"。
      论文 reframe 方向：
      (1) 将 "Why RL fails for multi-objective IE" 改为 "When and why RL degrades
      multi-objective IE: architecture and quantization as moderating factors"
      (2) Qwen case study 保留完整 spectrum（QLoRA catastrophic → bf16 mild → DPO gradual → RSFT none），
      LLaMA 作为对比 case 展示 spectrum 的 architecture-dependence
      (3) 新增分析：为什么 Qwen 脆弱——tokenizer efficiency 假说可检验
      （比较两个模型在 DocRE 上的 token 使用效率），quantization sensitivity 假说可引用 QuRL/QaRL
      此发现虽然削弱论文原始 scope，但 "architecture-dependent decoupling" 本身是有价值的发现——
      如果论文能提供充分的机制分析（不仅仅是 "it happens differently"），
      Findings track 仍可接受。

  - name: "EDCR human validation (100 samples)"
    plan_id: "plan_013"
    description: >
      100 个样本人工标注：对每个 cited evidence sentence 判断是否真正支持对应 relation。
      计算 EDCR 与人工判断的 Spearman ρ，验证 EDCR 作为自动诊断指标的可信度。
    expected_results:
      n_annotated: 100
      inter_annotator_kappa: 0.55
      edcr_human_spearman_rho: 0.42
      edcr_human_pvalue: 0.028
      ambiguous_cases_pct: 28
      clear_correct_pct: 52
      clear_wrong_pct: 20
      false_positive_rate: 0.18
      false_negative_rate: 0.22
      per_relation_type_agreement: 0.38
    result_rationale: >
      EDCR-human 相关偏低（ρ=0.42）的结构性原因：
      (1) Evidence 标注主观性高——IE 中 "一个句子是否支持一个关系" 不是二元判断。
      例如 "The university was established in 1905 by the local government" 是否支持
      (university, inception, 1905)？大多数人说是。是否支持 (university, founded_by,
      local_government)？约 60% 说是——"founded by" vs "established by" 的语义等价性存在争议。
      ~28% 样本落入这种 ambiguous zone，这直接压低 ρ 的上限。
      (2) NLI-IE calibration gap：EDCR 基于 DeBERTa NLI 的 entailment score，
      NLI 训练数据（SNLI/MNLI）是 sentence-pair 自然语言推理，与 IE 的 "entity-relation-evidence"
      三元组语义不完全对齐。NLI 对 "implicit support"（需要 world knowledge 的推理链）
      系统性低估，导致 false negative（人觉得 evidence 有效但 NLI 分低）。
      (3) 方法级 EDCR 高相关（ρ=-0.965）受极端值驱动（GRPO QLoRA EDCR≈1.0），
      去掉极端值后 sample-level 相关自然下降。
      Inter-annotator κ=0.55 也说明任务主观性——这是 ρ 的自然上限约束。
    tables:
      - name: "Table: EDCR Human Validation"
        headers: ["Category", "Count", "Pct"]
        rows:
          - ["Clear correct (human agrees with EDCR)", "52", "52%"]
          - ["Clear wrong (human disagrees with EDCR)", "20", "20%"]
          - ["Ambiguous (annotators disagree)", "28", "28%"]
      - name: "Table: Correlation Summary"
        headers: ["Metric", "Value"]
        rows:
          - ["Spearman ρ (EDCR vs human)", "0.42"]
          - ["p-value", "0.028"]
          - ["Inter-annotator Cohen's κ", "0.55"]
          - ["EDCR false positive rate", "0.18"]
          - ["EDCR false negative rate", "0.22"]
    figures_description:
      - "Scatter plot: EDCR auto score (x) vs human binary judgment (y) with ambiguous cases marked gray"
      - "Error analysis: 典型 false positive/negative 案例展示 NLI-IE gap"
    analysis: >
      ρ=0.42 statistically significant（p<0.05）但 moderate。
      审稿人攻击点："If EDCR correlates only 0.42 with human judgment,
      how reliable is your per-relation diagnostic (Claim 4)?"
      应对策略：
      (1) 强调 EDCR 的方法级诊断仍然有效——识别 catastrophic failure（EDCR≈1.0）
      不需要 sample-level 精度，只需要 monotonicity（方法越病态 EDCR 越高），
      而方法级 ρ=-0.965 已经验证这一点。
      (2) per-relation 诊断降级为 "exploratory analysis"——提供方向性信号但非精确度量。
      (3) κ=0.55 解释为 "task inherent ambiguity" 而非 EDCR 缺陷——
      任何自动指标在这种主观性任务上都无法远超 annotator agreement。
      (4) Limitation 段诚实讨论 NLI-IE calibration gap 和 improvement direction
      （domain-adapted NLI, direct evidence evaluation model）。
      此结果不致命但削弱 Claim 4 的 "diagnostic tool" 定位——
      EDCR 更适合定位为 "decoupling severity indicator"（方法级）而非 "evidence quality judge"（sample 级）。

  - name: "NLI model ablation (DeBERTa base vs large)"
    plan_id: "plan_010"
    description: >
      对比 DeBERTa-v3-base (86M) 和 DeBERTa-v3-large (304M) 作为 CED scorer，
      评估 NLI backbone 能力对 CED scoring 质量和下游 RSFT 性能的影响。
    expected_results:
      deberta_base_ced_discrimination_acc: 0.78
      deberta_large_ced_discrimination_acc: 0.815
      deberta_base_ced_mean_margin: 0.41
      deberta_large_ced_mean_margin: 0.48
      deberta_base_rsft_ign_f1: 44.8
      deberta_large_rsft_ign_f1: 45.3
      deberta_base_rsft_evi_f1: 80.8
      deberta_large_rsft_evi_f1: 81.4
      delta_ign_f1_base_vs_large: -0.5
      p_value_base_vs_large: 0.45
      rsft_selection_overlap: 0.82
    result_rationale: >
      DeBERTa base vs large 差异不显著（Δ=0.5pp, p=0.45）的原因：
      (1) CED 的瓶颈不在 NLI 模型——scoring 过程是 "将 (head, rel, tail, evidence_sentence)
      构造为 NLI hypothesis-premise pair" → NLI 打分。信息损失发生在 IE→NLI 的转换步骤，
      而非 NLI 模型本身。base 和 large 模型对同一组 (premise, hypothesis) 对的 ranking
      高度一致（Kendall τ > 0.9），因为 easy case 两者都能区分，差异只在 hard negative 的
      fine-grained ordering 上——而 top_k=1 的 harsh selection 策略抹平了这种 marginal 差异。
      (2) 82% 的 selected samples 重叠——两个 scorer 选出的 rank-1 response 大部分相同。
      只有 18% 的 doc 换了不同的 candidate，这 18% 中 base 选错（F1 更低）的比例仅稍高。
      (3) RSFT 本身对训练数据的 marginal 质量差异不敏感——top_k=1 已确保所有
      selected samples 都是 "reasonably good"，base vs large 的区别仅在
      "good vs slightly better"，对 3-epoch SFT 的最终性能影响可忽略。
    tables:
      - name: "Table: NLI Model Ablation"
        headers: ["NLI Backbone", "Params", "CED Discr.", "Mean Margin", "RSFT Ign-F1", "RSFT Evi-F1"]
        rows:
          - ["DeBERTa-v3-base", "86M", "0.78", "0.41", "44.8", "80.8"]
          - ["DeBERTa-v3-large", "304M", "0.815", "0.48", "45.3", "81.4"]
          - ["Δ (base-large)", "—", "-0.035", "-0.07", "-0.5pp", "-0.6pp"]
    figures_description: []
    analysis: >
      不显著差异（p=0.45）意味着 CED 的工程选择（base vs large）对论文结论无实质影响——
      对 paper 是 neutral finding。
      但审稿人可能追问两个方向：
      (1) "If NLI model quality doesn't matter, what does CED actually capture?"
      → 回答：CED 的价值在 contrastive structure（gold vs distractor 对比 scoring），
      不在 NLI 模型的 absolute calibration。换言之，CED 是 structural contribution，
      NLI 只是提供了 similarity metric 的一个 reasonable instantiation。
      (2) "Could you replace NLI with a simpler metric?"
      → 这是有力的 follow-up question，如果 base 和 large 无区别，
      BM25 或 TF-IDF 可能也无区别——这会进一步削弱 CED 的 "NLI-based" 标签。
      在 worst tier 下此实验是低风险低收益——不伤论文但也不帮论文。
      建议在论文中作为 appendix ablation 简短报告，不占 main text 篇幅。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e720e0d-f087-475e-af00-734c3dd482e4",
  "isSidechain": false,
  "requestId": "req_011Cb69uxtusoHiB4bqcADER",
  "type": "assistant",
  "uuid": "5c3fe02e-6036-47fe-bcfa-5e377d3c0c43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "ec4f40cb-c4c9-433e-91d1-bac586606fad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lqt3HtPxec9jeJwZ7Gi9ur",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 33378,
      "cache_read_input_tokens": 11447,
      "output_tokens": 23064,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33378,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 23064,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 33378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33378
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Test set 不 generalize 或 decoupling 跨家族不复现，核心 claim 需要 reframe 核心假设：['Test set RSFT vs SFT Δ < 2pp 或不显著（dev-test gap 大，可能因 DocRED test 分布偏移）', '或 LLaMA GRP…",
  "leafUuid": "5c3fe02e-6036-47fe-bcfa-5e377d3c0c43",
  "sessionId": "ec4f40cb-c4c9-433e-91d1-bac586606fad"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterize worst-case outcomes for evidence-grounded DocRE",
  "sessionId": "ec4f40cb-c4c9-433e-91d1-bac586606fad"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Test set 不 generalize 或 decoupling 跨家族不复现，核心 claim 需要 reframe 核心假设：['Test set RSFT vs SFT Δ < 2pp 或不显著（dev-test gap 大，可能因 DocRED test 分布偏移）', '或 LLaMA GRP…",
  "leafUuid": "5c3fe02e-6036-47fe-bcfa-5e377d3c0c43",
  "sessionId": "ec4f40cb-c4c9-433e-91d1-bac586606fad"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterize worst-case outcomes for evidence-grounded DocRE",
  "sessionId": "ec4f40cb-c4c9-433e-91d1-bac586606fad"
}
```

---
