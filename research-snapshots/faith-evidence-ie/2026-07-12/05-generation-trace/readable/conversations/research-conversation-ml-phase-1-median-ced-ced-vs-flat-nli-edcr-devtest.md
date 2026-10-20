# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：核心方法有效但 CED 优势不够突出：CED vs flat-NLI 差异存在但较小，EDCR 改善有限 核心假设：['Dev→test 有一定衰减

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/e1759942-0054-49a6-b6ff-76321594a118.jsonl`
- **Structured JSON:** [`83587834148c60f89cce.json`](../../sessions/83/83587834148c60f89cce.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T12:07:47.925Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T12:07:47.925Z",
  "sessionId": "e1759942-0054-49a6-b6ff-76321594a118",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：核心方法有效但 CED 优势不够突出：CED vs flat-NLI 差异存在但较小，EDCR 改善有限\n核心假设：['Dev→test 有一定衰减（rel_f1 -2~4pp, evi_f1 -1~3pp），但仍显著优于 SFT baseline', 'CED-scored RSFT 优于 flat-NLI-scored RSFT，但差异有限（evi_f1 gap 0.5~1.5pp, EDCR gap 1~3pp）', 'Test set evi_f1 仍高于 DREEAM 57.34，但需要确认评估协议可比性（plan_004 复现存在小幅偏差）', 'EDCR 63~66% 未大幅改善，CED-as-reranker 仅额外降低 2~4pp', 'GRPO 分析完整，但 reviewer 可能质疑超参搜索是否充分']\n关键指标范围：{'test_rel_f1': [0.4, 0.44], 'test_evi_f1': [0.77, 0.8], 'test_edcr': [0.6, 0.66], 'ced_vs_flatnli_evi_f1_gap': [0.005, 0.015], 'ced_vs_flatnli_edcr_gap': [0.01, 0.03], 'dreeam_dev_evi_f1_reproduced': [0.55, 0.58], 'reranker_edcr': [0.58, 0.63]}\n叙事方向：Claim 1 成立但需弱化措辞（\"competitive with\" 而非 \"surpasses\"）；Claim 2 最危险——CED 优于 flat-NLI 但差异不够dramatic，需将叙事从 \"CED 是关键创新\" 调整为 \"CED 提供了一致性改善， 且作为可组合模块（RSFT scoring + 推理 reranking）具有实用价值\"。Claim 3 保持不变，升级为 并列 contribution（在线 RL 对结构化 IE 的 catastrophic forgetting 分析本身有价值）。 Claim 4 需补充 EDCR 局限性讨论（上界分析、标注噪声影响）。论文叙事从 \"CED 方法论创新\" 转向 \"首个 LLM evidence-grounded DocRE 框架 + 在线/离线 RL 对比分析\" 双主线。 补充 model size ablation（1.7B/8B）和 Re-DocRED 扩展来加厚实验章节。EMNLP Main poster 可期。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: faith-evidence-ie\nvenue: EMNLP 2026 Main\nfocus: 核心关注点: (1) RSFT+CED 方法是否足够新颖（RSFT 本身不新，CED 作为 scoring function 的创新度）; (2) EDCR 63-66% 仍偏高，evidence 质量提升是否足够显著; (3) GRPO 全线失败的分析作为 contribution 是否有说服力; (4) 缺少 CED vs flat-NLI RSFT ablation（Claim 2 核心实验未做）\n\n## paper_framing.md\n\n# Paper Framing — FREIGE\n\n> **状态**: POST-MVP (MVP-1 + MVP-2 均 PASS，进入 Research 阶段)\n> **最后更新**: 2026-05-15\n\n## Target Venue\n\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\n- Stretch: ARR May 25 (10 days, 极紧，仅在实验全部顺利时考虑)\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\n\n## Core Insight\n\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。朴素 NLI faithfulness reward 可被 entity-mentioning distractor 句子游戏——共享实体但不支持具体关系的句子仍获正面蕴含分数。\n\n**CED (Contrastive Evidence Discrimination)** 通过文档内 hard negative 对比，将 evidence 质量评估从\"是否蕴含\"升级为\"是否比最佳干扰句更蕴含\"——本质上是 evidence grounding 场景下的 **anti-reward-overoptimization mechanism**（连接 Gao et al. 2023 reward overoptimization 理论）。\n\n**MVP 关键发现**: CED 作为在线 RL (GRPO) reward 导致 catastrophic forgetting（3 种 reward type × 多个 lr 全线失败），但作为离线 RL (RSFT) 的候选筛选信号极其有效——4 组超参配置均稳定超过 SFT baseline。**方法论结论**: 对结构化 IE 任务，CED 应作为离线质量信号而非在线训练奖励。\n\n## Story Arc\n\n1. **Problem**: LLM DocRE 无证据 → 部署障碍（human-in-the-loop KB population、生物医学审计、RAG 溯源）\n2. **Why naive reward fails**: flat-NLI 被 entity-sharing distractors 欺骗（SFT EDCR=71.2%，大量引用干扰句）\n3. **Why online RL fails**: GRPO+CED/flat-NLI/extract-only 全部 catastrophic forgetting（reward ↑ + rel_f1 ↓ 至 <0.02）\n4. **Solution**: CED 作为离线质量信号 + RSFT（rejection sampling fine-tuning）：SFT 模型生成 N 候选 → CED 打分筛选 → 微调，规避在线 RL 的遗忘风险\n5. **Theoretical grounding**: 连接 LongRLVR (ICLR 2026) evidence grounding 梯度消失分析 + \"RSFT=PPO\" (ICML 2025) 等价性理论\n6. **Result**: 首个 LLM-based DocRE 方法同时生成抽取和可验证证据\n\n## Core Claims\n\n### Claim 1 (Main): CED-scored RSFT 使 LLM 同时生成抽取和忠实证据\n- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法\n- RSFT+CED: rel_f1 +3.9~6.0pp over SFT, evi_f1 +1.1~2.1pp, EDCR -4.8~7.7pp\n- **MVP-2 已验证**: 4/4 configs PASS\n- **Research 需要**: test set 评估，DREEAM/SAIS Evi-F1 直接对比\n\n### Claim 2 (Ablation): CED scoring 优于 flat-NLI scoring 用于 RSFT\n- CED-filtered RSFT vs flat-NLI-filtered RSFT 的 evi_f1 和 EDCR 差异\n- CED 的对比性 margin 过滤掉 distractor-heavy 候选\n- **Research 需要**: flat-NLI scored RSFT ablation（核心实验）\n\n### Claim 3 (Analysis): 在线 RL 在结构化 IE 上 catastrophically forget\n- GRPO+QLoRA 在 3 种 reward type × 多个 lr 下全线失败\n- 关键对比: evi_f1 在 GRPO 下提升至 0.850（>SFT 0.798）但 rel_f1 崩至 <0.02——CED 驱动了 evidence 学习但在线 RL 摧毁了抽取能力\n- RSFT 规避此问题：不修改 policy gradient，只筛选训练数据\n- **MVP 已有完整证据**: D031/D033 GRPO 判死，D039 RSFT 成功\n\n### Claim 4 (Evaluation): EDCR 作为独立评估指标\n- EDCR = |entity-sharing non-gold cited sentences| / |total cited sentences|\n- Evi-F1 盲区：不惩罚 plausible-looking distractor citations\n- SFT EDCR=71.2%, RSFT+CED EDCR=63.5~66.4%（方向正确但差距有限，需坦诚讨论）\n- **Research 需要**: cross-method diagnostic table, CED vs flat-NLI EDCR 对比\n\n## MVP Evidence Summary\n\n| Config | rel_f1 | Δ rel_f1 | evi_f1 | EDCR | 状态 |\n|--------|--------|----------|--------|------|------|\n| SFT baseline | 0.4057 | — | 0.7979 | 0.7118 | ✅ |\n| RSFT r1 (3ep, α=128, s42) | 0.4449 | +3.92pp | 0.8187 | 0.6565 | ✅ |\n| RSFT r1 (s44) | 0.4655 | +5.98pp | 0.8087 | 0.6350 | ✅ |\n| RSFT r2a (1ep, α=128) | 0.4494 | +4.37pp | 0.8108 | 0.6641 | ✅ |\n| RSFT r2b (1ep, α=32, lr=1e-5) | 0.4493 | +4.36pp | 0.8128 | 0.6609 | ✅ |\n| GRPO best (lr=5e-5, ckpt-90) | 0.2110 | -19.5pp | 0.5750 | — | ❌ |\n| GRPO best (lr=5e-6, ckpt-100) | 0.0138 | -39.2pp | 0.8500 | 0.9900 | ❌ |\n\n## Anticipated Reviewer Concerns\n\n### RC1: NLI reward 信号质量（高概率攻击）\n- **攻击**: \"DeBERTa-v3-base 的 NLI 判断有 lexical overlap bias，CED 训练信号有噪声\"\n- **已验证**: MVP-1 Pearson r=0.34（NLI vs lexical overlap），远低于 0.7，证明非捷径\n- **Research 补充**: DeBERTa-base vs DeBERTa-large 对比\n\n### RC2: Gold evidence 标注不完整导致 false distractor\n- **攻击**: \"被标为 distractor 的句子可能是 annotator 遗漏的有效证据\"\n- **应对**: CED margin 的 self-correcting property——如果 false distractor 真正蕴含关系，其 p_neg 高 → margin 小 → 惩罚弱\n- **Research 补充**: false-distractor 鲁棒性量化分析\n\n### RC3: 评测可比性\n- **攻击**: \"生成式 evidence 如何与 DREEAM 的 attention-based evidence 做 apple-to-apple 对比？\"\n- **应对**: 模型输出显式句子索引 [S_i]，直接映射句子级 Evi-F1；辅助指标用 RoBERTa-large-MNLI（非训练用 DeBERTa）避免 circular evaluation\n\n### RC4: 单数据集 + 单模型泛化性\n- **攻击**: \"只在 DocRED + Qwen3-4B 上验证\"\n- **Research**: Re-DocRED 扩展 + Qwen3-1.7B/8B model size ablation\n\n### RC5: RSFT vs GRPO 是否公平对比\n- **攻击**: \"GRPO 失败可能是超参问题而非方法论问题\"\n- **应对**: 完整 GRPO 轨迹——3 种 reward × 多个 lr × 全 checkpoint eval；D020 控制变量下 CED 是唯一存活的 reward type\n\n### RC6: EDCR 63-66% 仍然偏高，CED 对证据精确度提升有限\n- **攻击**: \"RSFT+CED 的 EDCR 只比 SFT 低 5-8pp，证据质量提升不够显著\"\n- **应对**: (1) CED 在 RSFT 中是间接作用（筛选训练数据），非直接 reward；(2) CED-as-reranker 可能更直接降低 EDCR；(3) 需要 flat-NLI RSFT 对比证明 CED 方向正确\n- **Research**: CED reranker PoC（运行中），top_k ablation\n\n### RC7: 方法过于简单\n- **应对**: 简洁是优点——RSFT 方法论已被证明理论等价于 PPO (ICML 2025)，CED 创新在于打分函数设计而非框架复杂度\n\n## Key Baselines (8+)\n\n1. **SFT-only**: Qwen3-4B + LoRA SFT on DocRED gold — 无 RL\n2. **RSFT flat-NLI**: flat-NLI scored RSFT — 无 contrastive signal（核心 ablation）\n3. **RSFT CED (FREIGE)**: CED scored RSFT — 主方法\n4. **CED-as-reranker**: 推理时 CED 重排 SFT 候选（无训练）— 运行中\n5. **GRPO+CED**: 在线 RL with CED reward — negative baseline\n6. **DREEAM**: RoBERTa-large encoder — evidence SOTA (Evi-F1 57.34)\n7. **SAIS**: RoBERTa encoder — evidence baseline (Evi-F1 55.67)\n8. **DocKS-RAG**: GNN+RAG — extraction SOTA (F1 63.59, 无 evidence)\n9. **LMRC**: LLaMA3.1-8B — generative LLM SOTA (F1 60.69, 无 evidence)\n\n## Publishability Threshold\n\n- **必要条件**: RSFT+CED 在 test set 上 Evi-F1 > DREEAM 57.34 AND rel_f1 显著 > SFT baseline\n- **充分条件**: 上述 + CED vs flat-NLI RSFT Evi-F1/EDCR 差异显著 + GRPO 分析完整\n- **Failure pivot**: Evi-F1 < 57.34 on test set → 转为 analysis contribution（在线 vs 离线 RL for structured IE）\n\n## Research Phase Priorities\n\n| Priority | 实验 | Claim | 预估 GPU-hours |\n|----------|------|-------|---------------|\n| P0 | CED vs flat-NLI RSFT ablation | C2 | ~20h |\n| P0 | Test set evaluation (RSFT best config) | C1 | ~4h |\n| P0 | EDCR pipeline 验证 + cross-method table | C4 | ~2h |\n| P0 | DREEAM/SAIS Evi-F1 baseline reproduction | C1 | ~8h |\n| P1 | CED-as-reranker (running) | C1 bonus | ~6h |\n| P1 | Model size ablation (1.7B/8B) | RC4 | ~24h |\n| P1 | Re-DocRED extension | RC4 | ~12h |\n| P1 | top_k ablation (k=1 vs k=3) | RC6 | ~8h |\n| P2 | GRPO forgetting 详细分析 + 可视化 | C3 | ~4h |\n| P2 | DeBERTa-base vs large NLI 对比 | RC1 | ~4h |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选\n    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py\n    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set\n    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_003\n  claim: 4\n  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing\n    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_004\n  claim: 1\n  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)\n    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_005\n  claim: 1\n  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: mvp2_ced_reranker_poc\n  status: RUNNING\n- id: plan_006\n  claim: 1\n  description: 'Model size ablation: Qwen3-1.7B 和 Qwen3-8B 上复现 RSFT+CED pipeline，验证方法对模型规模的泛化性。应对\n    RC4。'\n  priority: P1\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Re-DocRED extension: 在 Re-DocRED（修正 false negative 标注的版本）上评估，验证 RSFT+CED\n    在更干净标注下的表现。应对 RC4。'\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  registry_id: null\n  status: planned\n- id: plan_008\n  claim: 2\n  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格\n    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_009\n  claim: 3\n  description: 'GRPO forgetting 详细分析: 整理全部 GRPO checkpoint 的 rel_f1/evi_f1/EDCR 轨迹，绘制\n    forgetting dynamics 可视化（reward vs task performance 曲线），支撑 Claim 3 的论述。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer\n    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_mvp1\n  claim: 1\n  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing\n    distractor 的能力验证'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: mvp1_ced_signal\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_margin: 0.48\n    discrimination_accuracy: 0.815\n    pearson_r_margin_jaccard: 0.34\n    pass: true\n- id: plan_mvp2_sft\n  claim: 1\n  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mvp2_sft_warmup\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.72\n    accuracy: 0.835\n- id: plan_mvp2_rsft\n  claim: 1\n  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部\n    PASS'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_mvp1\n  - plan_mvp2_sft\n  registry_id: mvp2_rsft_train_r1\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.0483\n    num_preds: 848\n    sft_baseline_rel_f1: 0.4057\n    failure_mode: relation_ontology_collapse_to_freetext\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n- id: plan_mvp2_grpo\n  claim: 3\n  description: 'GRPO+QLoRA 全线失败: 3 种 reward type × 多个 lr, catastrophic forgetting\n    negative result'\n  priority: P0\n  gpu_budget_hours: 60\n  deps:\n  - plan_mvp2_sft\n  registry_id: mvp2_grpo_ced_lr5e6_r1\n  status: DONE\n  conclusion: killed\n\n\n## registry (completed experiments)\n\n- exp_id: mvp1_ced_signal\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_margin: 0.48\n    discrimination_accuracy: 0.815\n    pearson_r_margin_jaccard: 0.34\n    pass: true\n- exp_id: smoke_test_grpo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_sft_warmup\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.72\n    accuracy: 0.835\n- exp_id: precompute_nli_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_grpo_ced\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_extract\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_sft_eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_extract_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: mvp2_grpo_extract_r3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_sft_eval_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    ign_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    precision: 0.4043\n    recall: 0.407\n    evi_precision: 0.8035\n    evi_recall: 0.7924\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.626\n    n_parseable: 617\n    n_truncated: 367\n    n_predictions: 18815\n    inference_time_seconds: 6484.7\n- exp_id: mvp2_sft_eval_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    ign_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    precision: 0.4043\n    recall: 0.407\n    evi_precision: 0.8035\n    evi_recall: 0.7924\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.626\n    n_parseable: 617\n    n_truncated: 367\n    n_predictions: 18815\n- exp_id: mvp2_grpo_ced_kl001_r2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001_r3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001_r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_step: 100\n    train_runtime_s: 9069.88\n    reward_final: 1.195\n    f1_reward_final: 0.573\n    ced_reward_final: 0.328\n    format_reward_final: 0.293\n    frac_zero_std_final: 0.2\n    kl_final: 0.118\n    loss_final: -0.009\n    grad_norm_final: 0.14\n    entropy_final: 0.067\n    completion_length_mean_final: 520.8\n    best_reward_step: 90\n    best_reward: 1.37\n    best_f1_reward: 0.72\n    best_ced_reward: 0.353\n- exp_id: mvp2_grpo_extract_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_early\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    f1: 0.1563\n    ign_f1: 0.1563\n    evi_f1: 0.5643\n    edcr: 0.8858\n    precision: 0.2356\n    recall: 0.1169\n    evi_precision: 0.4864\n    evi_recall: 0.6721\n    format_ok_rate: 0.999\n    n_parseable: 984\n    n_truncated: 11\n    n_predictions: 9250\n    tp: 1421\n    pred_count: 6032\n    gold_count: 12151\n- exp_id: mvp2_grpo_flatnli_r6\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    steps_completed: 25\n    final_frac_zero_std: 0.9\n    final_f1_reward: 0\n    final_flat_nli_reward: 0\n    final_format_reward: 0.293\n    collapse_step: 25\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.00296\n    rel_precision: 0.00314\n    rel_recall: 0.0028\n    evi_f1: 0.72\n    evi_precision: 0.6429\n    evi_recall: 0.8182\n    edcr: 0.9983\n    n_parseable: 984\n    n_truncated: 24\n    n_predictions: 11621\n    tp: 34\n    pred_count: 10839\n    gold_count: 12151\n    inference_time_seconds: 5211.4\n- exp_id: mvp2_eval_ced_kl001_r4_multi\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    checkpoint-10:\n      f1: 0.003\n      ign_f1: 0.003\n      evi_f1: 0.72\n      edcr: 0.9983\n      format_ok_rate: 0.999\n    checkpoint-20:\n      f1: 0.0088\n      ign_f1: 0.0088\n      evi_f1: 0.423\n      edcr: 0.9954\n      format_ok_rate: 0.999\n    checkpoint-30:\n      f1: 0.0338\n      ign_f1: 0.0338\n      evi_f1: 0.5889\n      edcr: 0.9798\n      format_ok_rate: 1\n    checkpoint-50:\n      f1: 0.1563\n      ign_f1: 0.1563\n      evi_f1: 0.5643\n      edcr: 0.8858\n      format_ok_rate: 0.999\n    checkpoint-60:\n      f1: 0.1467\n      ign_f1: 0.1467\n      evi_f1: 0.5763\n      edcr: 0.9062\n      format_ok_rate: 1\n    checkpoint-90:\n      f1: 0.2108\n      ign_f1: 0.2108\n      evi_f1: 0.5666\n      edcr: 0.8584\n      format_ok_rate: 1\n- exp_id: mvp2_eval_ced_kl001_r4_step100\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.2167\n    ign_f1: 0.2167\n    precision: 0.2849\n    recall: 0.1749\n    evi_f1: 0.5746\n    evi_precision: 0.5244\n    evi_recall: 0.6353\n    edcr: 0.8539\n    pred_count: 7460\n    gold_count: 12151\n    tp: 2125\n    n_truncated: 21\n    format_ok_rate: 1\n- exp_id: mvp2_eval_ced_kl001_r4_last\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt90\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_high\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    checkpoint_60:\n      rel_f1: 0.1467\n      ign_f1: 0.1467\n      precision: 0.1909\n      recall: 0.1192\n      evi_f1: 0.5763\n      edcr: 0.9062\n      pred_count: 10041\n      gold_count: 12151\n      n_truncated: 16\n      format_ok_rate: 1\n    note: Only ckpt-60 completed. Process died during ckpt-70 inference at 8% (5/62\n      batch). ckpt-80/90 never started.\n- exp_id: mvp2_eval_ced_kl001_r4_step90\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.2108\n    ign_f1: 0.2108\n    evi_f1: 0.5666\n    edcr: 0.8584\n    pred_count: 11160\n    n_truncated: 22\n    format_ok_rate: 1\n    n_documents: 985\n- exp_id: mvp2_grpo_ced_lr5e6_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_p1_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_rp_r1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt7080\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_rp_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt20\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0077\n    rel_precision: 0.0071\n    rel_recall: 0.0084\n    evi_f1: 0.628\n    evi_precision: 0.855\n    evi_recall: 0.496\n    edcr: 0.993\n    format_ok_rate: 0.991\n    field_compliance_rate: 0.399\n    pred_count: 14440\n    gold_count: 12151\n    tp: 102\n    n_truncated: 587\n    inference_time_seconds: 6370.4\n- exp_id: mvp2_eval_lr5e6_r1_ckpt40\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt40_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0071\n    precision: 0.0066\n    recall: 0.0078\n    evi_f1: 0.7584\n    evi_precision: 0.9113\n    evi_recall: 0.6494\n    edcr: 0.9942\n    format_ok_rate: 0.9939\n    field_compliance_rate: 0.5675\n    pred_count: 14434\n    gold_count: 12151\n    tp: 95\n    n_truncated: 424\n    inference_time_seconds: 6152\n- exp_id: mvp2_eval_lr5e6_rp_r2_ckpt20\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_sft_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    pred_count: 12234\n    gold_count: 12151\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.998\n    field_compliance_rate: 0.6264\n    n_truncated: 367\n    inference_time_seconds: 6138.5\n- exp_id: mvp2_eval_lr5e6_r1_ckpt60\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt80\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0116\n    ign_f1: 0.0116\n    precision: 0.0109\n    recall: 0.0124\n    evi_f1: 0.828\n    evi_precision: 0.928\n    evi_recall: 0.748\n    edcr: 0.993\n    format_ok_rate: 0.999\n    field_compliance_rate: 0.788\n    pred_count: 13828\n    gold_count: 12151\n    n_truncated: 210\n    inference_time_seconds: 6099\n- exp_id: mvp2_eval_lr5e6_r1_ckpt60_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0093\n    precision: 0.0085\n    recall: 0.0103\n    evi_f1: 0.81\n    edcr: 0.993\n    format_ok_rate: 0.998\n    pred_count: 14626\n    gold_count: 12151\n    tp: 125\n    inference_time_seconds: 6152\n- exp_id: mvp2_eval_lr5e6_r1_ckpt100\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0138\n    rel_precision: 0.0132\n    rel_recall: 0.0144\n    ign_f1: 0.0138\n    evi_f1: 0.8504\n    evi_precision: 0.9256\n    evi_recall: 0.7866\n    edcr: 0.9876\n    format_ok_rate: 0.999\n    field_compliance_rate: 0.8162\n    evidence_format_rate: 0.8162\n    tp: 175\n    pred_count: 13300\n    gold_count: 12151\n    n_predictions: 15498\n    n_truncated: 181\n    n_documents: 985\n    n_parseable: 984\n    inference_time_seconds: 5901.7\n- exp_id: mvp2_diversity_probe\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    unique_triples_t07: 5\n    unique_triples_t10: 8\n    jaccard_t07: 0.17\n    jaccard_t10: 0.051\n    format_ok_rate_t07: 0.5\n    format_ok_rate_t10: 0.438\n    n_samples: 3\n    n_generations: 8\n    note: 'unique_triples_t07 corrected from 7 to 5.0 (mean). Reviewer: format_ok\n      ~34% after fix, ''diversity'' was JSON key name variants not semantic diversity'\n- exp_id: mvp2_rsft_generate\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    generation_count: 5288\n    unique_docs: 659\n    format_compliance: 0.998\n    diversity_range: 7.5-7.8/8\n    exit_code: 0\n- exp_id: mvp2_rsft_ced_scoring\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    input_generations: 21952\n    selected_samples: 2718\n    unique_docs: 2691\n    selection_rate: 0.124\n    mean_f1: 0.6157\n    mean_ced: 0.6683\n    f1_range:\n    - 0.1026\n    - 1\n    zero_f1_samples: 0\n    selection_strategy: top_k=1\n    f1_threshold: 0.1\n- exp_id: mvp2_rsft_train_r1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.0483\n    num_preds: 848\n    sft_baseline_rel_f1: 0.4057\n    failure_mode: relation_ontology_collapse_to_freetext\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n- exp_id: mvp2_rsft_train_r1_s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.7622\n    train_loss: 0.6148\n    eval_entropy: 0.6724\n    mean_token_accuracy: 0.8291\n    total_steps: 510\n    epochs: 3\n    training_hours: 1.99\n- exp_id: mvp2_rsft_train_r1_s44\n  name: ''\n  status: ANALYZING\n  conclusion: success\n  metrics:\n    rel_f1: 0.4655\n    evi_f1: 0.8087\n    edcr: 0.635\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0598\n    delta_evi_f1: 0.0108\n    mvp2_pass: true\n- exp_id: mvp2_rsft_ced_scoring_topk3\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_eval_rsft_s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_ced_reranker_poc\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_rsft_diagnosis\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    root_cause: overfitting_plus_sft_knowledge_overwrite\n    truncated_json_samples: 170\n    truncated_pct: 6.3\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n    lora_scaling: 2\n    rsft_zero_relation_samples: 170\n    sft_zero_relation_docs: 26\n    rsft_mean_relations: 11.2\n    sft_mean_relations: 12.5\n- exp_id: mvp2_rsft_train_r2_fix\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_rsft_r2a\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_rsft_r2b\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_eval_rsft_r1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4449\n    evi_f1: 0.8187\n    edcr: 0.6565\n    num_preds: 15307\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0392\n    delta_evi_f1: 0.0208\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r2a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4494\n    ign_f1: 0.4494\n    evi_f1: 0.8108\n    edcr: 0.6641\n    precision: 0.4512\n    recall: 0.4475\n    evi_precision: 0.8143\n    evi_recall: 0.8073\n    format_ok_rate: 1\n    n_predictions: 15482\n    n_truncated: 208\n    inference_time_s: 5967.2\n- exp_id: mvp2_eval_rsft_r2b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4493\n    ign_f1: 0.4493\n    evi_f1: 0.8128\n    edcr: 0.6609\n    precision: 0.4566\n    recall: 0.4424\n    evi_precision: 0.8201\n    evi_recall: 0.8056\n    pred_count: 14829\n    format_ok: 983/985\n    truncated: 179\n    inference_time_s: 5862\n- exp_id: mvp2_eval_rsft_s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_s43_r2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_eval_rsft_r2b_maxtok1536\n  name: ''\n  status: RUNNING\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_r2b_maxtok1536_r2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T12:07:47.928Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T12:07:47.928Z",
  "sessionId": "e1759942-0054-49a6-b6ff-76321594a118"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-15T12:07:47.951Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：核心方法有效但 CED 优势不够突出：CED vs flat-NLI 差异存在但较小，EDCR 改善有限
核心假设：['Dev→test 有一定衰减（rel_f1 -2~4pp, evi_f1 -1~3pp），但仍显著优于 SFT baseline', 'CED-scored RSFT 优于 flat-NLI-scored RSFT，但差异有限（evi_f1 gap 0.5~1.5pp, EDCR gap 1~3pp）', 'Test set evi_f1 仍高于 DREEAM 57.34，但需要确认评估协议可比性（plan_004 复现存在小幅偏差）', 'EDCR 63~66% 未大幅改善，CED-as-reranker 仅额外降低 2~4pp', 'GRPO 分析完整，但 reviewer 可能质疑超参搜索是否充分']
关键指标范围：{'test_rel_f1': [0.4, 0.44], 'test_evi_f1': [0.77, 0.8], 'test_edcr': [0.6, 0.66], 'ced_vs_flatnli_evi_f1_gap': [0.005, 0.015], 'ced_vs_flatnli_edcr_gap': [0.01, 0.03], 'dreeam_dev_evi_f1_reproduced': [0.55, 0.58], 'reranker_edcr': [0.58, 0.63]}
叙事方向：Claim 1 成立但需弱化措辞（"competitive with" 而非 "surpasses"）；Claim 2 最危险——CED 优于 flat-NLI 但差异不够dramatic，需将叙事从 "CED 是关键创新" 调整为 "CED 提供了一致性改善， 且作为可组合模块（RSFT scoring + 推理 reranking）具有实用价值"。Claim 3 保持不变，升级为 并列 contribution（在线 RL 对结构化 IE 的 catastrophic forgetting 分析本身有价值）。 Claim 4 需补充 EDCR 局限性讨论（上界分析、标注噪声影响）。论文叙事从 "CED 方法论创新" 转向 "首个 LLM evidence-grounded DocRE 框架 + 在线/离线 RL 对比分析" 双主线。 补充 model size ablation（1.7B/8B）和 Re-DocRED 扩展来加厚实验章节。EMNLP Main poster 可期。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: faith-evidence-ie
venue: EMNLP 2026 Main
focus: 核心关注点: (1) RSFT+CED 方法是否足够新颖（RSFT 本身不新，CED 作为 scoring function 的创新度）; (2) EDCR 63-66% 仍偏高，evidence 质量提升是否足够显著; (3) GRPO 全线失败的分析作为 contribution 是否有说服力; (4) 缺少 CED vs flat-NLI RSFT ablation（Claim 2 核心实验未做）

## paper_framing.md

# Paper Framing — FREIGE

> **状态**: POST-MVP (MVP-1 + MVP-2 均 PASS，进入 Research 阶段)
> **最后更新**: 2026-05-15

## Target Venue

- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)
- Stretch: ARR May 25 (10 days, 极紧，仅在实验全部顺利时考虑)
- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)

## Core Insight

LLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。朴素 NLI faithfulness reward 可被 entity-mentioning distractor 句子游戏——共享实体但不支持具体关系的句子仍获正面蕴含分数。

**CED (Contrastive Evidence Discrimination)** 通过文档内 hard negative 对比，将 evidence 质量评估从"是否蕴含"升级为"是否比最佳干扰句更蕴含"——本质上是 evidence grounding 场景下的 **anti-reward-overoptimization mechanism**（连接 Gao et al. 2023 reward overoptimization 理论）。

**MVP 关键发现**: CED 作为在线 RL (GRPO) reward 导致 catastrophic forgetting（3 种 reward type × 多个 lr 全线失败），但作为离线 RL (RSFT) 的候选筛选信号极其有效——4 组超参配置均稳定超过 SFT baseline。**方法论结论**: 对结构化 IE 任务，CED 应作为离线质量信号而非在线训练奖励。

## Story Arc

1. **Problem**: LLM DocRE 无证据 → 部署障碍（human-in-the-loop KB population、生物医学审计、RAG 溯源）
2. **Why naive reward fails**: flat-NLI 被 entity-sharing distractors 欺骗（SFT EDCR=71.2%，大量引用干扰句）
3. **Why online RL fails**: GRPO+CED/flat-NLI/extract-only 全部 catastrophic forgetting（reward ↑ + rel_f1 ↓ 至 <0.02）
4. **Solution**: CED 作为离线质量信号 + RSFT（rejection sampling fine-tuning）：SFT 模型生成 N 候选 → CED 打分筛选 → 微调，规避在线 RL 的遗忘风险
5. **Theoretical grounding**: 连接 LongRLVR (ICLR 2026) evidence grounding 梯度消失分析 + "RSFT=PPO" (ICML 2025) 等价性理论
6. **Result**: 首个 LLM-based DocRE 方法同时生成抽取和可验证证据

## Core Claims

### Claim 1 (Main): CED-scored RSFT 使 LLM 同时生成抽取和忠实证据
- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法
- RSFT+CED: rel_f1 +3.9~6.0pp over SFT, evi_f1 +1.1~2.1pp, EDCR -4.8~7.7pp
- **MVP-2 已验证**: 4/4 configs PASS
- **Research 需要**: test set 评估，DREEAM/SAIS Evi-F1 直接对比

### Claim 2 (Ablation): CED scoring 优于 flat-NLI scoring 用于 RSFT
- CED-filtered RSFT vs flat-NLI-filtered RSFT 的 evi_f1 和 EDCR 差异
- CED 的对比性 margin 过滤掉 distractor-heavy 候选
- **Research 需要**: flat-NLI scored RSFT ablation（核心实验）

### Claim 3 (Analysis): 在线 RL 在结构化 IE 上 catastrophically forget
- GRPO+QLoRA 在 3 种 reward type × 多个 lr 下全线失败
- 关键对比: evi_f1 在 GRPO 下提升至 0.850（>SFT 0.798）但 rel_f1 崩至 <0.02——CED 驱动了 evidence 学习但在线 RL 摧毁了抽取能力
- RSFT 规避此问题：不修改 policy gradient，只筛选训练数据
- **MVP 已有完整证据**: D031/D033 GRPO 判死，D039 RSFT 成功

### Claim 4 (Evaluation): EDCR 作为独立评估指标
- EDCR = |entity-sharing non-gold cited sentences| / |total cited sentences|
- Evi-F1 盲区：不惩罚 plausible-looking distractor citations
- SFT EDCR=71.2%, RSFT+CED EDCR=63.5~66.4%（方向正确但差距有限，需坦诚讨论）
- **Research 需要**: cross-method diagnostic table, CED vs flat-NLI EDCR 对比

## MVP Evidence Summary

| Config | rel_f1 | Δ rel_f1 | evi_f1 | EDCR | 状态 |
|--------|--------|----------|--------|------|------|
| SFT baseline | 0.4057 | — | 0.7979 | 0.7118 | ✅ |
| RSFT r1 (3ep, α=128, s42) | 0.4449 | +3.92pp | 0.8187 | 0.6565 | ✅ |
| RSFT r1 (s44) | 0.4655 | +5.98pp | 0.8087 | 0.6350 | ✅ |
| RSFT r2a (1ep, α=128) | 0.4494 | +4.37pp | 0.8108 | 0.6641 | ✅ |
| RSFT r2b (1ep, α=32, lr=1e-5) | 0.4493 | +4.36pp | 0.8128 | 0.6609 | ✅ |
| GRPO best (lr=5e-5, ckpt-90) | 0.2110 | -19.5pp | 0.5750 | — | ❌ |
| GRPO best (lr=5e-6, ckpt-100) | 0.0138 | -39.2pp | 0.8500 | 0.9900 | ❌ |

## Anticipated Reviewer Concerns

### RC1: NLI reward 信号质量（高概率攻击）
- **攻击**: "DeBERTa-v3-base 的 NLI 判断有 lexical overlap bias，CED 训练信号有噪声"
- **已验证**: MVP-1 Pearson r=0.34（NLI vs lexical overlap），远低于 0.7，证明非捷径
- **Research 补充**: DeBERTa-base vs DeBERTa-large 对比

### RC2: Gold evidence 标注不完整导致 false distractor
- **攻击**: "被标为 distractor 的句子可能是 annotator 遗漏的有效证据"
- **应对**: CED margin 的 self-correcting property——如果 false distractor 真正蕴含关系，其 p_neg 高 → margin 小 → 惩罚弱
- **Research 补充**: false-distractor 鲁棒性量化分析

### RC3: 评测可比性
- **攻击**: "生成式 evidence 如何与 DREEAM 的 attention-based evidence 做 apple-to-apple 对比？"
- **应对**: 模型输出显式句子索引 [S_i]，直接映射句子级 Evi-F1；辅助指标用 RoBERTa-large-MNLI（非训练用 DeBERTa）避免 circular evaluation

### RC4: 单数据集 + 单模型泛化性
- **攻击**: "只在 DocRED + Qwen3-4B 上验证"
- **Research**: Re-DocRED 扩展 + Qwen3-1.7B/8B model size ablation

### RC5: RSFT vs GRPO 是否公平对比
- **攻击**: "GRPO 失败可能是超参问题而非方法论问题"
- **应对**: 完整 GRPO 轨迹——3 种 reward × 多个 lr × 全 checkpoint eval；D020 控制变量下 CED 是唯一存活的 reward type

### RC6: EDCR 63-66% 仍然偏高，CED 对证据精确度提升有限
- **攻击**: "RSFT+CED 的 EDCR 只比 SFT 低 5-8pp，证据质量提升不够显著"
- **应对**: (1) CED 在 RSFT 中是间接作用（筛选训练数据），非直接 reward；(2) CED-as-reranker 可能更直接降低 EDCR；(3) 需要 flat-NLI RSFT 对比证明 CED 方向正确
- **Research**: CED reranker PoC（运行中），top_k ablation

### RC7: 方法过于简单
- **应对**: 简洁是优点——RSFT 方法论已被证明理论等价于 PPO (ICML 2025)，CED 创新在于打分函数设计而非框架复杂度

## Key Baselines (8+)

1. **SFT-only**: Qwen3-4B + LoRA SFT on DocRED gold — 无 RL
2. **RSFT flat-NLI**: flat-NLI scored RSFT — 无 contrastive signal（核心 ablation）
3. **RSFT CED (FREIGE)**: CED scored RSFT — 主方法
4. **CED-as-reranker**: 推理时 CED 重排 SFT 候选（无训练）— 运行中
5. **GRPO+CED**: 在线 RL with CED reward — negative baseline
6. **DREEAM**: RoBERTa-large encoder — evidence SOTA (Evi-F1 57.34)
7. **SAIS**: RoBERTa encoder — evidence baseline (Evi-F1 55.67)
8. **DocKS-RAG**: GNN+RAG — extraction SOTA (F1 63.59, 无 evidence)
9. **LMRC**: LLaMA3.1-8B — generative LLM SOTA (F1 60.69, 无 evidence)

## Publishability Threshold

- **必要条件**: RSFT+CED 在 test set 上 Evi-F1 > DREEAM 57.34 AND rel_f1 显著 > SFT baseline
- **充分条件**: 上述 + CED vs flat-NLI RSFT Evi-F1/EDCR 差异显著 + GRPO 分析完整
- **Failure pivot**: Evi-F1 < 57.34 on test set → 转为 analysis contribution（在线 vs 离线 RL for structured IE）

## Research Phase Priorities

| Priority | 实验 | Claim | 预估 GPU-hours |
|----------|------|-------|---------------|
| P0 | CED vs flat-NLI RSFT ablation | C2 | ~20h |
| P0 | Test set evaluation (RSFT best config) | C1 | ~4h |
| P0 | EDCR pipeline 验证 + cross-method table | C4 | ~2h |
| P0 | DREEAM/SAIS Evi-F1 baseline reproduction | C1 | ~8h |
| P1 | CED-as-reranker (running) | C1 bonus | ~6h |
| P1 | Model size ablation (1.7B/8B) | RC4 | ~24h |
| P1 | Re-DocRED extension | RC4 | ~12h |
| P1 | top_k ablation (k=1 vs k=3) | RC6 | ~8h |
| P2 | GRPO forgetting 详细分析 + 可视化 | C3 | ~4h |
| P2 | DeBERTa-base vs large NLI 对比 | RC1 | ~4h |


## experiment_plan (with registry status)

- id: plan_001
  claim: 2
  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选
    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py
    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'
  priority: P0
  gpu_budget_hours: 20
  deps: []
  registry_id: null
  status: planned
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
  registry_id: null
  status: planned
- id: plan_004
  claim: 1
  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)
    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'
  priority: P0
  gpu_budget_hours: 8
  deps: []
  registry_id: null
  status: planned
- id: plan_005
  claim: 1
  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'
  priority: P1
  gpu_budget_hours: 6
  deps: []
  registry_id: mvp2_ced_reranker_poc
  status: RUNNING
- id: plan_006
  claim: 1
  description: 'Model size ablation: Qwen3-1.7B 和 Qwen3-8B 上复现 RSFT+CED pipeline，验证方法对模型规模的泛化性。应对
    RC4。'
  priority: P1
  gpu_budget_hours: 24
  deps:
  - plan_001
  registry_id: null
  status: planned
- id: plan_007
  claim: 1
  description: 'Re-DocRED extension: 在 Re-DocRED（修正 false negative 标注的版本）上评估，验证 RSFT+CED
    在更干净标注下的表现。应对 RC4。'
  priority: P1
  gpu_budget_hours: 12
  deps:
  - plan_002
  registry_id: null
  status: planned
- id: plan_008
  claim: 2
  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格
    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'
  priority: P1
  gpu_budget_hours: 8
  deps: []
  registry_id: null
  status: planned
- id: plan_009
  claim: 3
  description: 'GRPO forgetting 详细分析: 整理全部 GRPO checkpoint 的 rel_f1/evi_f1/EDCR 轨迹，绘制
    forgetting dynamics 可视化（reward vs task performance 曲线），支撑 Claim 3 的论述。'
  priority: P2
  gpu_budget_hours: 4
  deps: []
  registry_id: null
  status: planned
- id: plan_010
  claim: 1
  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer
    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。'
  priority: P2
  gpu_budget_hours: 4
  deps: []
  registry_id: null
  status: planned
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
    PASS'
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
  description: 'GRPO+QLoRA 全线失败: 3 种 reward type × 多个 lr, catastrophic forgetting
    negative result'
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
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: mvp2_grpo_ced_kl001_r3
  name: ''
  status: PREPARING
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
  status: PREPARING
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
  status: ANALYZING
  conclusion: success
  metrics:
    rel_f1: 0.4655
    evi_f1: 0.8087
    edcr: 0.635
    sft_baseline_rel_f1: 0.4057
    sft_baseline_evi_f1: 0.7979
    delta_rel_f1: 0.0598
    delta_evi_f1: 0.0108
    mvp2_pass: true
- exp_id: mvp2_rsft_ced_scoring_topk3
  name: ''
  status: QUEUED
  conclusion: ''
  metrics: {}
- exp_id: mvp2_eval_rsft_s44
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: mvp2_ced_reranker_poc
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: mvp2_rsft_diagnosis
  name: ''
  status: PREPARING
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
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: mvp2_rsft_r2a
  name: ''
  status: ANALYZING
  conclusion: ''
  metrics: {}
- exp_id: mvp2_rsft_r2b
  name: ''
  status: ANALYZING
  conclusion: ''
  metrics: {}
- exp_id: mvp2_eval_rsft_r1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4449
    evi_f1: 0.8187
    edcr: 0.6565
    num_preds: 15307
    sft_baseline_rel_f1: 0.4057
    sft_baseline_evi_f1: 0.7979
    delta_rel_f1: 0.0392
    delta_evi_f1: 0.0208
    mvp2_pass: true
- exp_id: mvp2_eval_rsft_r2a
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4494
    ign_f1: 0.4494
    evi_f1: 0.8108
    edcr: 0.6641
    precision: 0.4512
    recall: 0.4475
    evi_precision: 0.8143
    evi_recall: 0.8073
    format_ok_rate: 1
    n_predictions: 15482
    n_truncated: 208
    inference_time_s: 5967.2
- exp_id: mvp2_eval_rsft_r2b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rel_f1: 0.4493
    ign_f1: 0.4493
    evi_f1: 0.8128
    edcr: 0.6609
    precision: 0.4566
    recall: 0.4424
    evi_precision: 0.8201
    evi_recall: 0.8056
    pred_count: 14829
    format_ok: 983/985
    truncated: 179
    inference_time_s: 5862
- exp_id: mvp2_eval_rsft_s43
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp2_eval_rsft_s43_r2
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: mvp2_eval_rsft_r2b_maxtok1536
  name: ''
  status: RUNNING
  conclusion: killed
  metrics: {}
- exp_id: mvp2_eval_rsft_r2b_maxtok1536_r2
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: median
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
  "promptId": "3452ae50-2f6b-45b4-80e5-b1bfcf8b5302",
  "type": "user",
  "uuid": "5cac452a-cefa-4363-b647-6f10d28bc220",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "e1759942-0054-49a6-b6ff-76321594a118",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T12:07:47.949Z_

```json
{
  "parentUuid": "5cac452a-cefa-4363-b647-6f10d28bc220",
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
  "uuid": "04ad52df-0ba7-4f60-9cdc-f57e5d85ee9d",
  "timestamp": "2026-05-15T12:07:47.949Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "e1759942-0054-49a6-b6ff-76321594a118",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T12:07:47.949Z_

```json
{
  "parentUuid": "04ad52df-0ba7-4f60-9cdc-f57e5d85ee9d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "291e28d9-8018-4251-85ef-83ee5fabee64",
  "timestamp": "2026-05-15T12:07:47.949Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "e1759942-0054-49a6-b6ff-76321594a118",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心方法有效但 CED 优势不够突出：CED vs flat-NLI 差异存在但较小，EDCR 改善有限 核心假设：['Dev→test 有一定衰减（rel_f1 -2~4pp, evi_f1 -1~3pp），但仍显著优于 SFT baseline', 'CED-scored RSFT 优于 flat-N…",
  "leafUuid": "291e28d9-8018-4251-85ef-83ee5fabee64",
  "sessionId": "e1759942-0054-49a6-b6ff-76321594a118"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier experiments for FREIGE DocRE evidence grounding",
  "sessionId": "e1759942-0054-49a6-b6ff-76321594a118"
}
```

---

### Assistant

_source line 8 · 2026-05-15T12:08:20.411Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for each planned experiment in the experiment_plan, assuming the "median" tier outcome. Let me carefully go through each planned experiment and generate realistic predictions based on the median tier definition.

Let me review the median tier definition:
- Core method works but CED advantage is not dramatic
- CED vs flat-NLI difference exists but is small
- EDCR improvement is limited
- Key metrics: test_rel_f1 [0.4, 0.44], test_evi_f1 [0.77, 0.8], test_edcr [0.6, 0.66], ced_vs_flatnli_evi_f1_gap [0.005, 0.015], ced_vs_flatnli_edcr_gap [0.01, 0.03], dreeam_dev_evi_f1_reproduced [0.55, 0.58], reranker_edcr [0.58, 0.63

]

Now I'm going through each of the seven planned experiments to map out what results I should predict for each one, keeping in mind the median tier constraints where the method shows promise but improvements are modest.

For plan_001, the core ablation comparing CED against flat-NLI in the RSFT setting should show CED performing better, though the gap won't be dramatic—maybe a few percentage points depending on the metric.

Looking at the baseline CED RSFT results on dev, I can use those as anchors and work backward to estimate what flat-NLI RSFT would achieve. The evidence F1 gap should land in that 0.5-1.5 percentage point range, which means flat-NLI would trail slightly but still represent a meaningful improvement over the SFT baseline since it's still doing rejection sampling, just with a weaker signal.

Now I'm checking the test set projections against the median tier expectations—rel_f1 should fall between 0.4-0.44, evidence F1 between 0.77-0.8, and EDCR between 0.6-0.66. The dev-to-test degradation typically runs 2-4 percentage points for rel_f1 and 1-3 for evidence F1, so I need to account for that drop-off when extrapolating.

For the DREEAM baseline, I'm expecting to reproduce evidence F1 scores in the 0.55-0.58 range on the dev set, which aligns with the paper's reported 57.34 on test, though some deviation is normal. I'm also starting to think through how CED performs as a reranker, which is the next configuration to evaluate. Writing the YAML configuration...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "291e28d9-8018-4251-85ef-83ee5fabee64",
  "isSidechain": false,
  "requestId": "req_011Cb4KwoqfTS8YZuTFfdsQZ",
  "type": "assistant",
  "uuid": "ff4caebc-c1ea-482c-afc2-22af74485ef1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "e1759942-0054-49a6-b6ff-76321594a118",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TSry9TwQDsERiknJJuVs1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18625,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16807,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16807,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18625
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

_source line 9 · 2026-05-15T12:12:49.389Z_

Let me review the experiment plan details and existing metrics to ensure consistency.

```yaml
tier: median
narrative_guidance: >
  核心方法有效但 CED 优势不够突出。论文叙事从 "CED 方法论创新" 转向 "首个 LLM evidence-grounded DocRE 框架 + 在线/离线 RL 对比分析" 双主线。
  Claim 1 成立但弱化措辞（"competitive with" 而非 "surpasses"）；Claim 2 最危险——CED 优于 flat-NLI 但差异不 dramatic，
  需将叙事调整为 "CED 提供一致性改善，且作为可组合模块具有实用价值"；Claim 3 升级为并列 contribution；Claim 4 补充 EDCR 局限性讨论。
  补充 model size ablation 和 Re-DocRED 扩展加厚实验章节。EMNLP Main poster 可期。

imagined_experiments:
  # ============ P0 实验 ============

  - name: "CED vs flat-NLI RSFT ablation"
    plan_id: "plan_001"
    description: >
      用 flat-NLI scoring（无 contrastive margin）筛选 RSFT 训练数据，与 CED scoring 的 RSFT 做 apple-to-apple 对比。
      复用已有 candidate pool（21952 generations），仅替换 scoring function 为 max(NLI(premise=evidence, hypothesis=claim))
      而非 CED 的 margin = p_pos - max(p_neg)。flat-NLI top_k=1 筛选后训练，同超参（1ep, α=32, lr=1e-5，对齐 r2b config）。
    expected_results:
      # flat-NLI RSFT 结果
      flatnli_rsft_rel_f1: 0.4420
      flatnli_rsft_evi_f1: 0.7985
      flatnli_rsft_edcr: 0.6850
      flatnli_rsft_evi_precision: 0.8010
      flatnli_rsft_evi_recall: 0.7960
      flatnli_rsft_pred_count: 14950
      flatnli_selected_samples: 2750
      flatnli_selection_rate: 0.125
      flatnli_mean_f1: 0.6080
      # CED RSFT 对比基准（取 r2b config）
      ced_rsft_rel_f1: 0.4493
      ced_rsft_evi_f1: 0.8128
      ced_rsft_edcr: 0.6609
      # 差异
      delta_evi_f1_ced_minus_flatnli: 0.0143
      delta_edcr_ced_minus_flatnli: -0.0241
      delta_rel_f1_ced_minus_flatnli: 0.0073
    result_rationale: >
      flat-NLI scoring 能筛掉明显低质量候选（NLI 分数低的），因此 flat-NLI RSFT 仍显著优于 SFT baseline
      （rel_f1 +3.6pp, evi_f1 +0.06pp）。但 flat-NLI 无法区分 entity-sharing distractor 和 genuine evidence——
      两者的 NLI score 都高（因为都包含相关实体），导致筛选出的训练样本中保留了更多 distractor-heavy candidates。
      CED 的 contrastive margin 恰好针对这一盲区：margin = p_pos - max(p_neg) 会惩罚那些 distractor
      也获得高 NLI 分数的样本。但在 median 档位下，这种区分能力有限（discrimination_accuracy 0.815 而非 0.9+），
      hard negative 有时自身也是有效 evidence（annotator 遗漏），导致 CED margin 信号有噪声。
      最终 CED 相对 flat-NLI 的 evi_f1 gap 为 1.43pp，EDCR 改善 2.41pp——方向一致但不够 dramatic。
      rel_f1 差异更小（0.73pp），因为关系抽取能力主要由 SFT 基础和训练数据量决定，scoring function 差异影响有限。
    tables:
      - name: "Table: CED vs flat-NLI RSFT Ablation (Dev Set)"
        columns: ["Method", "Scoring", "rel_f1", "evi_f1", "EDCR↓", "Δevi_f1", "ΔEDCR"]
        rows:
          - ["SFT baseline", "—", 0.4057, 0.7979, 0.7118, "—", "—"]
          - ["RSFT", "flat-NLI", 0.4420, 0.7985, 0.6850, "+0.06pp", "-2.68pp"]
          - ["RSFT", "CED", 0.4493, 0.8128, 0.6609, "+1.49pp", "-5.09pp"]
          - ["Δ (CED − flat-NLI)", "—", "+0.73pp", "+1.43pp", "-2.41pp", "—", "—"]
    figures_description:
      - "Scatter plot: CED margin vs flat-NLI score per candidate，颜色标注 gold evidence overlap ratio，展示 CED 和 flat-NLI 在高 NLI score 区域的分离——CED margin 低但 flat-NLI score 高的点即 distractor-heavy candidates"
    analysis: >
      CED 优于 flat-NLI 在所有三个维度上一致，但 evi_f1 gap 1.43pp 和 EDCR gap 2.41pp 在统计上处于边缘。
      需要 bootstrap confidence interval 确认显著性。若 p>0.05，Claim 2 需进一步弱化为 "CED provides
      consistent directional improvement"。关键发现：flat-NLI RSFT 的 evi_f1 几乎等于 SFT（+0.06pp），
      说明 flat-NLI scoring 在 evidence 质量维度几乎无筛选能力——它选出的 top candidate 的 evidence 质量与随机
      SFT 输出相当。这一 null result 实际上 *支撑* 了 CED 的价值叙事：不是 CED 改善有限，而是 flat-NLI 在
      evidence 维度几乎无效。论文中应将此 framing 为 "flat-NLI fails to discriminate evidence quality"
      而非 "CED marginally improves"。

  - name: "Test set evaluation (RSFT best config)"
    plan_id: "plan_002"
    description: >
      用 RSFT best config（r2b: 1ep, α=32, lr=1e-5）和 s44（3ep, α=128, seed=44）在 DocRED test set 上评估。
      CodaLab 提交获取官方 rel_f1/ign_f1，本地计算 evi_f1 和 EDCR。同时提交 SFT baseline 和 flat-NLI RSFT 作为对比。
    expected_results:
      # RSFT-CED best (r2b config) on test
      rsft_ced_test_rel_f1: 0.4280
      rsft_ced_test_ign_f1: 0.4195
      rsft_ced_test_evi_f1: 0.7890
      rsft_ced_test_edcr: 0.6380
      rsft_ced_test_precision: 0.4350
      rsft_ced_test_recall: 0.4215
      # RSFT-CED s44 on test
      rsft_ced_s44_test_rel_f1: 0.4380
      rsft_ced_s44_test_ign_f1: 0.4290
      rsft_ced_s44_test_evi_f1: 0.7830
      rsft_ced_s44_test_edcr: 0.6200
      # SFT baseline on test
      sft_test_rel_f1: 0.3860
      sft_test_ign_f1: 0.3780
      sft_test_evi_f1: 0.7750
      sft_test_edcr: 0.6950
      # flat-NLI RSFT on test
      flatnli_rsft_test_rel_f1: 0.4200
      flatnli_rsft_test_evi_f1: 0.7760
      flatnli_rsft_test_edcr: 0.6680
      # Deltas
      delta_rsft_ced_vs_sft_rel_f1: "+4.20pp"
      delta_rsft_ced_vs_sft_evi_f1: "+1.40pp"
      dev_to_test_rel_f1_drop: "-2.13pp"
      dev_to_test_evi_f1_drop: "-2.38pp"
    result_rationale: >
      Dev→test 衰减是 DocRED 的已知现象：test set 的关系分布与 dev 有偏移（部分关系类型在 test 中频率不同），
      且 test set 标注由不同 annotator 完成。rel_f1 衰减约 2.1pp（从 dev 0.4493 到 test 0.4280），
      处于 median 预期的 -2~4pp 范围中段。evi_f1 衰减约 2.4pp（从 0.8128 到 0.7890），
      稍大于 rel_f1 衰减，因为 evidence 标注在 test set 中更保守（gold evidence 集合更小）。
      s44 config（3ep 训练）在 dev 上 rel_f1 更高（0.4655）但 test 上衰减更大（-2.75pp），
      暗示 3ep 训练有轻微 dev set overfitting。r2b 的 1ep 训练泛化更稳定。
      SFT baseline 也有 ~2pp 衰减（dev 0.4057 → test 0.3860），说明衰减是数据固有的而非方法导致。
      关键指标：test_evi_f1 0.789 远高于 DREEAM 的 57.34，但需注意评估协议差异（生成式 vs attention-based）。
      EDCR 在 test 上略好于 dev（0.638 vs 0.661），可能因 test set 的 entity mention 分布不同。
    tables:
      - name: "Table: Test Set Results — Main Comparison"
        columns: ["Method", "rel_f1", "ign_f1", "evi_f1", "EDCR↓"]
        rows:
          - ["SFT baseline", 0.386, 0.378, 0.775, 0.695]
          - ["RSFT flat-NLI", 0.420, "—", 0.776, 0.668]
          - ["RSFT CED (r2b)", 0.428, 0.420, 0.789, 0.638]
          - ["RSFT CED (s44)", 0.438, 0.429, 0.783, 0.620]
          - ["DREEAM†", "—", "—", 0.5734, "—"]
          - ["SAIS†", "—", "—", 0.5567, "—"]
      - name: "Table: Dev→Test Generalization Gap"
        columns: ["Config", "dev_rel_f1", "test_rel_f1", "Δrel_f1", "dev_evi_f1", "test_evi_f1", "Δevi_f1"]
        rows:
          - ["SFT", 0.4057, 0.386, "-1.97pp", 0.7979, 0.775, "-2.29pp"]
          - ["RSFT-CED r2b", 0.4493, 0.428, "-2.13pp", 0.8128, 0.789, "-2.38pp"]
          - ["RSFT-CED s44", 0.4655, 0.438, "-2.75pp", 0.8087, 0.783, "-2.57pp"]
    figures_description:
      - "Bar chart: test set rel_f1 和 evi_f1 并列柱状图，SFT / flat-NLI RSFT / CED RSFT / DREEAM / SAIS 五组，清晰展示 FREIGE 在 evidence 维度的优势（0.789 vs 0.573）和 extraction 维度的提升"
    analysis: >
      Test set 结果确认 Claim 1 成立：RSFT+CED 在 test 上 evi_f1=0.789 远超 DREEAM 0.5734（+21.6pp），
      但需在论文中明确说明评估协议差异——DREEAM 用 attention weight thresholding 提取 evidence，FREIGE 用显式
      sentence index 生成。rel_f1 0.428-0.438 虽不及 encoder SOTA（ATLOP 63+），但作为同时生成 evidence 的
      首个 LLM 方法，"competitive" 措辞合理。s44 在 test 上 rel_f1 更高但 evi_f1 更低，建议论文中报告两个 config
      并讨论 rel_f1-evi_f1 trade-off。ign_f1 与 rel_f1 非常接近（差 <1pp），说明 RSFT 未过度依赖训练集中的
      共现关系。EDCR 在 test 上 0.62-0.64，虽优于 SFT 的 0.695，但仍意味着 ~62-64% 的 cited non-gold
      sentences 是 entity-sharing distractors——论文需坦诚讨论此局限。

  - name: "EDCR pipeline 验证 + cross-method diagnostic table"
    plan_id: "plan_003"
    description: >
      在所有 evidence-producing 方法上统一计算 EDCR 及其子指标，构建 cross-method diagnostic table。
      包括 EDCR 的 breakdown：entity-sharing distractor rate、non-entity distractor rate、
      evidence precision/recall 按关系类型分层分析。
    expected_results:
      sft_edcr: 0.7118
      sft_entity_distractor_count_mean: 3.2
      sft_non_entity_distractor_count_mean: 0.4
      rsft_ced_edcr: 0.6609
      rsft_ced_entity_distractor_count_mean: 2.6
      rsft_flatnli_edcr: 0.6850
      rsft_flatnli_entity_distractor_count_mean: 2.9
      ced_reranker_edcr: 0.6050
      ced_reranker_entity_distractor_count_mean: 2.2
      high_edcr_relation_types: ["P17 (country)", "P131 (located in)", "P27 (citizenship)"]
      high_edcr_mean: 0.82
      low_edcr_relation_types: ["P50 (author)", "P86 (composer)", "P175 (performer)"]
      low_edcr_mean: 0.45
    result_rationale: >
      EDCR 反映 entity-sharing distractor 在 citations 中的占比。SFT 的 EDCR 最高（0.712），因为 SFT
      模型倾向于引用包含 head/tail entity mention 的所有句子而非仅支持特定关系的句子——这是 "entity mention
      heuristic" 的体现。RSFT-CED 降低 EDCR 至 0.661，因为 CED scoring 在训练数据筛选时惩罚了
      distractor-heavy candidates。flat-NLI RSFT 的 EDCR 0.685 介于 SFT 和 CED 之间——flat-NLI
      能过滤掉一些 evidence 完全不相关的候选，但无法区分 entity-sharing distractor。
      关系类型分层分析揭示 EDCR 不均匀：地理/国籍类关系（P17, P131, P27）的 EDCR 极高（0.82），因为文档中
      大量句子提到国家/地点名称但不直接支持该关系；而创作类关系（P50, P86）的 EDCR 较低（0.45），因为这类关系
      通常在少数特定句子中明确表述。这一分层分析本身有诊断价值，可作为 Claim 4 的核心证据。
    tables:
      - name: "Table: Cross-Method EDCR Diagnostic"
        columns: ["Method", "EDCR↓", "Evi-F1", "Mean #Distractor", "Mean #Gold Cited", "Mean #Total Cited"]
        rows:
          - ["SFT", 0.712, 0.798, 3.2, 2.1, 5.3]
          - ["RSFT flat-NLI", 0.685, 0.799, 2.9, 2.0, 4.9]
          - ["RSFT CED", 0.661, 0.813, 2.6, 2.1, 4.7]
          - ["CED reranker", 0.605, 0.790, 2.2, 2.0, 4.2]
      - name: "Table: EDCR by Relation Type (Top-5 / Bottom-5)"
        columns: ["Relation", "SFT EDCR", "RSFT-CED EDCR", "ΔEDCR", "#Instances"]
        rows:
          - ["P17 (country)", 0.85, 0.79, "-0.06", 1205]
          - ["P131 (located in)", 0.83, 0.78, "-0.05", 987]
          - ["P27 (citizenship)", 0.80, 0.74, "-0.06", 654]
          - ["P30 (continent)", 0.78, 0.73, "-0.05", 321]
          - ["P150 (contains)", 0.77, 0.72, "-0.05", 445]
          - ["...", "...", "...", "...", "..."]
          - ["P86 (composer)", 0.48, 0.42, "-0.06", 198]
          - ["P50 (author)", 0.45, 0.39, "-0.06", 276]
          - ["P175 (performer)", 0.42, 0.37, "-0.05", 312]
          - ["P40 (child)", 0.40, 0.35, "-0.05", 187]
          - ["P26 (spouse)", 0.38, 0.33, "-0.05", 156]
    figures_description:
      - "Heatmap: relation type × method 的 EDCR 值，行按 SFT EDCR 降序排列，直观展示 CED 在哪些关系类型上改善最大"
      - "Histogram: SFT 和 RSFT-CED 的 per-document EDCR 分布对比，展示 RSFT-CED 将分布整体左移但右尾（高 EDCR）仍存在"
    analysis: >
      EDCR 诊断揭示两个关键发现：(1) CED 在所有关系类型上一致降低 EDCR（~5-6pp），但高 EDCR 关系仍然很高
      （P17: 0.85→0.79），说明 entity-sharing distractor 问题在地理类关系上是结构性的，单靠 CED 难以彻底解决；
      (2) CED reranker（推理时选择）比 RSFT-CED（训练时筛选）在 EDCR 上更优（0.605 vs 0.661），
      暗示 CED 的直接使用比间接使用更有效，但代价是推理时间增加。
      论文中应将此分析作为 Claim 4 的核心内容，诚实讨论 EDCR 63-66% 的局限性，
      并将关系类型分层分析作为 future work 的 motivation（relation-aware CED 设计）。

  - name: "DREEAM baseline reproduction"
    plan_id: "plan_004"
    description: >
      在 DocRED dev set 上复现 DREEAM (RoBERTa-large) 的 Evi-F1。使用官方代码和预训练权重，
      确认 57.34 这一 test set 数字对应的 dev set 表现，作为 Claim 1 的直接对比基线。
    expected_results:
      dreeam_dev_evi_f1: 0.5680
      dreeam_dev_evi_precision: 0.5520
      dreeam_dev_evi_recall: 0.5850
      dreeam_dev_rel_f1: 0.6280
      dreeam_test_evi_f1_reported: 0.5734
      reproduction_gap: "-0.0054"
      sais_dev_evi_f1: 0.5480
    result_rationale: >
      DREEAM 论文报告 test Evi-F1 57.34，dev 上通常比 test 稍低或相近（DocRED dev/test 分布相似但不完全一致）。
      复现偏差 -0.54pp 源于：(1) 随机种子差异导致 attention threshold 的最优值稍有不同；(2) PyTorch/CUDA 版本
      差异引入的浮点不确定性；(3) 可能的预处理细节差异（sentence boundary detection）。
      这个偏差幅度在合理范围内（<1pp），但需要在论文中明确报告为 "reproduction" 结果。
      dev Evi-F1 0.568 意味着 FREIGE 的 dev evi_f1 0.813 比 DREEAM 高 24.5pp——但这个对比需要大量 caveats：
      DREEAM 的 evidence 是 attention-based extraction（binary classification per sentence），
      FREIGE 是生成式（模型显式输出 sentence indices），评估粒度和 false positive 成因完全不同。
      论文中应将此对比作为 "reference point" 而非 "direct superiority claim"。
    tables:
      - name: "Table: Evidence Baseline Reproduction"
        columns: ["Method", "Type", "dev_evi_f1", "test_evi_f1 (reported)", "dev_rel_f1"]
        rows:
          - ["DREEAM (paper)", "encoder", "—", 0.5734, 0.635]
          - ["DREEAM (reproduced)", "encoder", 0.568, "—", 0.628]
          - ["SAIS (reproduced)", "encoder", 0.548, 0.5567, 0.618]
          - ["FREIGE (RSFT-CED)", "generative", 0.813, "—*", 0.449]
    figures_description:
      - "对比柱状图: evidence 评估协议说明——左侧 DREEAM/SAIS 的 attention-based evidence extraction 流程，右侧 FREIGE 的 generative evidence citation 流程，强调评估协议差异"
    analysis: >
      复现结果确认 DREEAM dev Evi-F1 约 0.568（与 test 0.5734 基本一致，小幅偏差可接受）。
      FREIGE 与 DREEAM 的 Evi-F1 差距巨大（0.813 vs 0.568），但这部分源于评估协议差异：
      DREEAM 对每个句子做 binary attention classification，threshold 选择会影响 precision-recall trade-off；
      FREIGE 生成显式 sentence index，模型 "知道自己在引用什么"。
      论文中需要 (1) 明确说明评估协议差异，(2) 考虑在同一评估框架下对比（如将 FREIGE 输出转为 binary labels
      后与 DREEAM 对比），(3) 承认 DREEAM 的 rel_f1 (0.628) 远高于 FREIGE (0.449)，
      FREIGE 的价值在于 evidence grounding 而非 extraction performance。

  - name: "CED-as-reranker"
    plan_id: "plan_005"
    description: >
      推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。
      对 dev set 全量文档运行：SFT 生成 8 candidates per document → CED 打分 → 选最高 CED score 的候选作为最终输出。
    expected_results:
      reranker_rel_f1: 0.4150
      reranker_evi_f1: 0.8050
      reranker_edcr: 0.6050
      reranker_evi_precision: 0.8200
      reranker_evi_recall: 0.7910
      reranker_pred_count: 13500
      sft_baseline_rel_f1: 0.4057
      sft_baseline_evi_f1: 0.7979
      sft_baseline_edcr: 0.7118
      delta_rel_f1: "+0.93pp"
      delta_evi_f1: "+0.71pp"
      delta_edcr: "-10.68pp"
      inference_time_multiplier: "~8x"
    result_rationale: >
      CED reranker 直接在推理时选择 CED score 最高的候选，其 EDCR 改善最显著（从 0.712 降至 0.605，-10.7pp），
      因为 CED score 直接优化了 "相对于 distractor 的 evidence 质量"——高 CED score 的候选天然倾向于引用
      更少的 entity-sharing distractors。但 rel_f1 仅小幅提升（+0.93pp），因为 CED 打分不直接优化关系抽取质量，
      高 CED score 不一定对应高 rel_f1（有些候选 evidence 好但关系抽错了）。
      evi_f1 的提升（+0.71pp）小于 RSFT-CED（+1.49pp），因为 reranker 受限于 SFT 模型的 generation
      distribution——如果 8 个候选都引用了 distractor，reranker 也无法避免。RSFT 通过改变模型本身的
      generation distribution 来从源头改善。
      EDCR 改善却显著优于 RSFT，这是因为 reranker 可以在 8 个候选中做 sharp selection（选 EDCR 最低的那个），
      而 RSFT 改变的是 average generation quality（所有输出的 EDCR 平均降低）。
      推理时间增加 8x 是实际部署的代价——论文中应讨论 RSFT+reranker 的组合是否值得。
    tables:
      - name: "Table: CED-as-Reranker vs Training-based Methods"
        columns: ["Method", "Training?", "rel_f1", "evi_f1", "EDCR↓", "Inference Cost"]
        rows:
          - ["SFT", "SFT only", 0.4057, 0.7979, 0.712, "1x"]
          - ["CED reranker", "No (SFT + rerank)", 0.415, 0.805, 0.605, "~8x"]
          - ["RSFT-CED", "SFT + RSFT", 0.449, 0.813, 0.661, "1x"]
          - ["RSFT-CED + reranker", "SFT + RSFT + rerank", 0.452, 0.818, 0.585, "~8x"]
    figures_description:
      - "Trade-off plot: x 轴 inference cost (1x/8x), y 轴 EDCR/evi_f1，四个方法标注在图上，展示 training vs inference 的 cost-quality trade-off"
    analysis: >
      CED reranker 提供了最佳 EDCR（0.605），证明 CED 作为推理时 quality signal 的直接价值。
      但 reranker 的 rel_f1 和 evi_f1 均不如 RSFT-CED，说明训练时改善优于推理时选择。
      最有趣的是 RSFT-CED + reranker 组合：额外降低 EDCR 至 0.585（比单独 RSFT 再降 7.6pp），
      而 rel_f1/evi_f1 几乎不受影响。这支持 "CED 作为可组合模块" 的叙事——
      RSFT 改善 generation quality，reranker 进一步过滤 distractor。
      在 median 档位下，reranker 的 EDCR 降至 0.585-0.605 仍未突破 0.5 的 "大部分 citations
      不是 distractor" 阈值，论文需承认这一局限。

  - name: "Model size ablation (1.7B / 8B)"
    plan_id: "plan_006"
    description: >
      在 Qwen3-1.7B 和 Qwen3-8B 上复现完整 RSFT+CED pipeline，验证方法对模型规模的泛化性。
      每个模型：SFT warmup → candidate generation → CED scoring → RSFT training → dev eval。
    expected_results:
      # Qwen3-1.7B
      qwen_1_7b_sft_rel_f1: 0.3280
      qwen_1_7b_sft_evi_f1: 0.7350
      qwen_1_7b_sft_edcr: 0.7500
      qwen_1_7b_rsft_ced_rel_f1: 0.3650
      qwen_1_7b_rsft_ced_evi_f1: 0.7580
      qwen_1_7b_rsft_ced_edcr: 0.7050
      qwen_1_7b_delta_rel_f1: "+3.70pp"
      qwen_1_7b_delta_evi_f1: "+2.30pp"
      qwen_1_7b_delta_edcr: "-4.50pp"
      # Qwen3-8B
      qwen_8b_sft_rel_f1: 0.4450
      qwen_8b_sft_evi_f1: 0.8180
      qwen_8b_sft_edcr: 0.6900
      qwen_8b_rsft_ced_rel_f1: 0.4820
      qwen_8b_rsft_ced_evi_f1: 0.8320
      qwen_8b_rsft_ced_edcr: 0.6350
      qwen_8b_delta_rel_f1: "+3.70pp"
      qwen_8b_delta_evi_f1: "+1.40pp"
      qwen_8b_delta_edcr: "-5.50pp"
    result_rationale: >
      1.7B 模型的 SFT baseline 显著弱于 4B（rel_f1 0.328 vs 0.406），因为小模型在 DocRE 的长文档理解和
      多关系抽取上能力有限，输出格式合规率也更低（更多 truncation 和格式错误）。但 RSFT+CED 的相对改善幅度
      一致（rel_f1 +3.7pp, evi_f1 +2.3pp），说明 CED scoring 的质量筛选对小模型同样有效——
      甚至 evi_f1 的绝对改善更大（+2.3pp vs 4B 的 +1.5pp），因为小模型的 generation diversity 更高
      （输出更不确定），CED 有更大的筛选空间。
      8B 模型的 SFT baseline 已很强（rel_f1 0.445），RSFT+CED 仍带来一致改善（+3.7pp rel_f1, +1.4pp evi_f1），
      但 evi_f1 的改善幅度略小于 4B（+1.4pp vs +1.5pp），可能因为 8B SFT 已学到较好的 evidence 模式。
      EDCR 改善在 8B 上更大（-5.5pp vs 4B 的 -5.1pp），暗示更大模型能更好地利用 CED 筛选信号。
      这一 "方法在各规模上一致有效" 的结果足以应对 RC4，但不构成额外 novelty。
    tables:
      - name: "Table: Model Size Ablation"
        columns: ["Model", "Method", "rel_f1", "evi_f1", "EDCR↓", "Δrel_f1", "Δevi_f1"]
        rows:
          - ["Qwen3-1.7B", "SFT", 0.328, 0.735, 0.750, "—", "—"]
          - ["Qwen3-1.7B", "RSFT-CED", 0.365, 0.758, 0.705, "+3.7pp", "+2.3pp"]
          - ["Qwen3-4B", "SFT", 0.406, 0.798, 0.712, "—", "—"]
          - ["Qwen3-4B", "RSFT-CED", 0.449, 0.813, 0.661, "+4.4pp", "+1.5pp"]
          - ["Qwen3-8B", "SFT", 0.445, 0.818, 0.690, "—", "—"]
          - ["Qwen3-8B", "RSFT-CED", 0.482, 0.832, 0.635, "+3.7pp", "+1.4pp"]
    figures_description:
      - "Line plot: x 轴 model size (1.7B/4B/8B), 三条线分别为 SFT rel_f1, RSFT-CED rel_f1, 和 Δrel_f1，展示 RSFT-CED 的改善在不同规模上的一致性"
    analysis: >
      三个模型规模上 RSFT+CED 均一致改善所有指标，Δrel_f1 在 3.7-4.4pp 范围内稳定，Δevi_f1 在 1.4-2.3pp。
      8B 的绝对数字最优但与 4B 差距不大（rel_f1 +3.3pp, evi_f1 +1.9pp），说明从 4B 到 8B 的边际收益递减。
      1.7B 虽绝对性能较弱，但 RSFT-CED 的改善幅度不减，这一正面结果支撑了方法的实用性（可在资源有限场景部署）。
      论文中可用一句话总结："RSFT+CED consistently improves over SFT across model sizes (1.7B–8B),
      with relative gains largely independent of model capacity."

  - name: "Re-DocRED extension"
    plan_id: "plan_007"
    description: >
      在 Re-DocRED 上评估 RSFT+CED，验证方法在修正 false negative 标注后的表现。
      Re-DocRED 对 DocRED 的标注进行了大规模修正（补充遗漏关系、纠正错误 evidence），预期更干净的标注会改变
      EDCR 的计算基准。
    expected_results:
      redocred_sft_rel_f1: 0.4350
      redocred_sft_evi_f1: 0.8150
      redocred_sft_edcr: 0.5800
      redocred_rsft_ced_rel_f1: 0.4750
      redocred_rsft_ced_evi_f1: 0.8350
      redocred_rsft_ced_edcr: 0.5250
      redocred_delta_rel_f1: "+4.00pp"
      redocred_delta_evi_f1: "+2.00pp"
      redocred_delta_edcr: "-5.50pp"
      docred_to_redocred_edcr_drop: "-13.6pp (SFT), -13.6pp (RSFT)"
    result_rationale: >
      Re-DocRED 补充了大量 DocRED 中遗漏的关系标注（false negatives），导致两个效应：
      (1) rel_f1 提升——之前被判为 false positive 的正确预测现在被计为 true positive，SFT 从 0.406 升至 0.435；
      (2) EDCR 显著下降——之前被计为 "distractor" 的句子（entity-sharing non-gold cited）中有一部分实际上是
      补充标注关系的 gold evidence，重新标注后不再是 distractor。SFT EDCR 从 0.712 降至 0.580（-13.2pp）。
      RSFT-CED 的改善幅度与 DocRED 一致（Δrel_f1 +4.0pp, Δevi_f1 +2.0pp），说明方法在更干净标注下仍有效。
      EDCR 的绝对值在 Re-DocRED 上更低（0.525 vs 0.661），这是好消息——说明 DocRED 上 EDCR 偏高部分归因于
      标注 incompleteness（annotator 遗漏了有效 evidence），而非纯粹的模型缺陷。
      但 EDCR 0.525 仍意味着过半的 non-gold citations 是 distractor——问题并未因更好标注而消失。
    tables:
      - name: "Table: DocRED vs Re-DocRED"
        columns: ["Dataset", "Method", "rel_f1", "evi_f1", "EDCR↓"]
        rows:
          - ["DocRED", "SFT", 0.406, 0.798, 0.712]
          - ["DocRED", "RSFT-CED", 0.449, 0.813, 0.661]
          - ["Re-DocRED", "SFT", 0.435, 0.815, 0.580]
          - ["Re-DocRED", "RSFT-CED", 0.475, 0.835, 0.525]
    figures_description:
      - "Paired bar chart: DocRED vs Re-DocRED 的 EDCR 对比，展示更干净标注下 EDCR 整体降低但 CED 改善幅度持续"
    analysis: >
      Re-DocRED 结果提供了两个重要 insights：(1) DocRED 上 EDCR 高部分是标注噪声造成的——
      Re-DocRED 的更完整标注使 EDCR 降低约 13pp；(2) 即使在更干净标注下，RSFT-CED 仍一致降低 EDCR
      （-5.5pp），且改善幅度与 DocRED 相当。这加强了方法的鲁棒性论述。
      论文中应将 Re-DocRED 结果作为 "annotation quality sensitivity" 分析的一部分，
      而非核心结果——主实验仍应基于 DocRED（更广泛使用、可与更多 baselines 对比）。

  - name: "top_k ablation"
    plan_id: "plan_008"
    description: >
      CED scoring 筛选 top_k=3 vs top_k=1 对比。top_k=1 选择每个文档 CED score 最高的 1 个候选
      （当前配置，~2718 samples），top_k=3 选择前 3 个（~8000 samples，更多但质量更低的训练数据）。
    expected_results:
      topk1_samples: 2718
      topk1_mean_ced: 0.6683
      topk1_rsft_rel_f1: 0.4493
      topk1_rsft_evi_f1: 0.8128
      topk1_rsft_edcr: 0.6609
      topk3_samples: 7950
      topk3_mean_ced: 0.5480
      topk3_rsft_rel_f1: 0.4550
      topk3_rsft_evi_f1: 0.8020
      topk3_rsft_edcr: 0.6780
      topk3_delta_rel_f1_vs_topk1: "+0.57pp"
      topk3_delta_evi_f1_vs_topk1: "-1.08pp"
      topk3_delta_edcr_vs_topk1: "+1.71pp"
    result_rationale: >
      top_k=3 提供约 3x 的训练数据（7950 vs 2718 samples），但 mean CED score 降低（0.548 vs 0.668），
      因为 rank 2-3 的候选质量低于 rank 1。更多数据带来 rel_f1 的小幅提升（+0.57pp），因为关系抽取受益于
      训练数据量——更多样本覆盖更多 relation type 和 entity pair 组合。
      但 evi_f1 反而下降（-1.08pp）且 EDCR 升高（+1.71pp），因为 rank 2-3 的候选包含更多 distractor-heavy
      evidence——CED score 较低意味着这些候选的 evidence 质量接近 flat-NLI 水平。
      这一 quality-quantity trade-off 在 RSFT 文献中是已知现象（Yuan et al. 2024 "self-play" RSFT
      也发现严格筛选优于宽松筛选 for generation quality）。
      结论：top_k=1 在 evidence 质量上更优，top_k=3 在 extraction coverage 上更优。
      论文中可根据目标选择报告哪个 config——如果强调 evidence faithfulness（Claim 1-2），选 top_k=1。
    tables:
      - name: "Table: top_k Ablation"
        columns: ["top_k", "#Samples", "Mean CED", "rel_f1", "evi_f1", "EDCR↓"]
        rows:
          - [1, 2718, 0.668, 0.449, 0.813, 0.661]
          - [3, 7950, 0.548, 0.455, 0.802, 0.678]
    figures_description:
      - "CED score distribution histogram: top_k=1 vs top_k=3 的 selected samples CED score 分布，展示 top_k=3 引入的低质量尾部"
    analysis: >
      top_k ablation 清晰展示了 CED 筛选严格度的 trade-off。在 median 档位下，top_k=1 是 evidence quality
      的最优选择。这一结果可作为 Claim 2 的辅助证据：CED scoring 的 discriminative power 在 top-1 selection
      时最强，放松阈值会稀释信号——间接说明 CED margin 确实在区分 evidence 质量。
      论文中建议报告 top_k=1 作为主结果，top_k=3 作为 ablation，并讨论 "quality vs quantity"
      trade-off 的实践意义。

  - name: "GRPO forgetting 详细分析 + 可视化"
    plan_id: "plan_009"
    description: >
      整理全部 GRPO checkpoint 的 rel_f1/evi_f1/EDCR/reward 轨迹，绘制 forgetting dynamics 可视化。
      覆盖 3 种 reward type（CED, flat-NLI, extract-only）× 多个 learning rate 的完整轨迹。
    expected_results:
      # CED reward (lr=5e-6, 100 steps)
      grpo_ced_lr5e6_rel_f1_trajectory: [0.406, 0.008, 0.007, 0.009, 0.012, 0.014]
      grpo_ced_lr5e6_evi_f1_trajectory: [0.798, 0.628, 0.758, 0.810, 0.828, 0.850]
      grpo_ced_lr5e6_reward_trajectory: [0.0, 0.35, 0.65, 0.85, 1.05, 1.20]
      grpo_ced_lr5e6_collapse_step: 10
      # CED reward (lr=5e-5, KL=0.01, 100 steps)
      grpo_ced_kl001_rel_f1_peak: 0.211
      grpo_ced_kl001_rel_f1_peak_step: 90
      grpo_ced_kl001_evi_f1_at_peak: 0.567
      # flat-NLI reward
      grpo_flatnli_collapse_step: 25
      grpo_flatnli_final_frac_zero_std: 0.9
      # extract-only reward
      grpo_extract_rel_f1_peak: 0.015
      grpo_extract_collapse_step: 20
      # Key finding
      forgetting_pattern: "reward ↑ monotonic, rel_f1 ↓ catastrophic within 10-25 steps, evi_f1 diverges (↑ for CED, ↓ for others)"
    result_rationale: >
      GRPO 的 catastrophic forgetting 机制在 DocRE 上的特殊表现：policy gradient 优化 reward 信号时，
      模型快速学会生成高 reward 的输出模式——对 CED reward，这意味着生成包含正确 evidence 句子的文本
      （evi_f1 从 0.798 上升至 0.850）；对 extract-only reward，这意味着生成高 F1 的关系抽取格式。
      但两者无法兼顾：CED 优化牺牲关系抽取能力（模型 "遗忘" 如何正确抽取关系来专注于 evidence），
      extract-only 优化也很快坍缩（缺乏 KL 约束时 policy 快速偏离 SFT 分布）。
      KL=0.01 约束版本（grpo_ced_kl001）延缓了坍缩（rel_f1 peak 0.211 at step 90），
      但仍远低于 SFT baseline 0.406——KL 约束不足以阻止 forgetting，只是减慢了速度。
      flat-NLI reward 坍缩最快（step 25 即 frac_zero_std=0.9），因为 flat-NLI 的 reward surface
      更平滑（没有 contrastive margin 的尖锐梯度），策略更容易找到 degenerate optimum。
      这一分析连接 LongRLVR (ICLR 2026) 的 evidence grounding 梯度消失理论，
      可作为 Claim 3 的完整证据。
    tables:
      - name: "Table: GRPO Trajectory Summary"
        columns: ["Reward Type", "LR", "KL", "Collapse Step", "Peak rel_f1", "Final evi_f1", "Final Reward"]
        rows:
          - ["CED", "5e-6", 0, "~10", 0.014, 0.850, 1.20]
          - ["CED", "5e-5", 0.01, "~50", 0.211, 0.575, 1.20]
          - ["flat-NLI", "5e-6", 0, "~25", "<0.01", "<0.01", 0.29]
          - ["extract-only", "5e-6", 0, "~20", 0.015, "—", 0.30]
    figures_description:
      - "Dual-axis line plot: 左 y 轴 rel_f1（下降曲线），右 y 轴 reward（上升曲线），x 轴 training step。3 种 reward type 各一条线，清晰展示 reward-performance decoupling"
      - "Heatmap: checkpoint × metric (rel_f1, evi_f1, EDCR, reward) 的 trajectory，用颜色编码 Good→Bad，直观展示 CED reward 下 evi_f1 是唯一持续改善的指标"
    analysis: >
      可视化清晰揭示了在线 RL 在结构化 IE 上的核心困境：多目标优化（relation extraction + evidence grounding）
      在 policy gradient 框架下相互干扰。CED reward 成功驱动了 evidence 学习（evi_f1 持续上升），
      但代价是关系抽取能力的 catastrophic forgetting。这不是超参问题——3 种 reward × 多个 lr × KL 约束
      全部失败，且失败模式一致（reward ↑ + rel_f1 ↓）。
      这一 negative result 本身有方法论价值：为 "何时用在线 RL vs 离线 RL" 提供了结构化 IE 场景下的经验指导。
      论文中应将此定位为 Claim 3 的核心，与 LongRLVR 的理论框架对接。
      reviewer 可能质疑 "GRPO 超参搜索是否充分"——覆盖 3 种 reward × 4+ LR × KL 约束的全面搜索
      应能说服大部分 reviewer，但建议在 appendix 中放完整 grid 表格。

  - name: "NLI model ablation"
    plan_id: "plan_010"
    description: >
      DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer。替换 NLI 模型后重新计算全量 CED scores，
      对比 discrimination accuracy 和 downstream RSFT 效果。
    expected_results:
      # DeBERTa-v3-base (current)
      base_discrimination_accuracy: 0.815
      base_mean_margin: 0.48
      base_pearson_r_jaccard: 0.34
      base_rsft_evi_f1: 0.8128
      base_rsft_edcr: 0.6609
      # DeBERTa-v3-large
      large_discrimination_accuracy: 0.845
      large_mean_margin: 0.52
      large_pearson_r_jaccard: 0.31
      large_rsft_evi_f1: 0.8165
      large_rsft_edcr: 0.6520
      # Deltas
      delta_discrimination_accuracy: "+3.0pp"
      delta_mean_margin: "+0.04"
      delta_rsft_evi_f1: "+0.37pp"
      delta_rsft_edcr: "-0.89pp"
    result_rationale: >
      DeBERTa-v3-large 比 base 有更强的 NLI 能力（MNLI accuracy large 91.3% vs base 88.1%），
      因此 CED 的 gold vs distractor discrimination accuracy 从 0.815 提升至 0.845。
      mean margin 也更大（0.52 vs 0.48），说明 large 模型对 evidence quality 的区分度更高。
      但 Pearson r 与 jaccard overlap 的相关性反而略低（0.31 vs 0.34），说明 large 模型
      的 NLI 判断更少依赖 lexical overlap——这是正面信号（less spurious correlation）。
      然而 downstream 影响有限：RSFT evi_f1 仅提升 0.37pp，EDCR 仅降低 0.89pp。
      这是因为 CED scoring 的瓶颈不在 NLI 模型能力而在 DocRED 标注质量——
      gold evidence 标注本身不完整（false distractor 问题），更强的 NLI 模型
      不能修复标注层面的噪声。这一结果暗示 CED 的改善上界受标注质量限制。
      论文中可用此结果应对 RC1，结论为 "NLI model quality has limited impact,
      suggesting annotation completeness rather than NLI capability is the bottleneck."
    tables:
      - name: "Table: NLI Model Ablation"
        columns: ["NLI Model", "Disc. Acc.", "Mean Margin", "r(margin,jaccard)", "RSFT evi_f1", "RSFT EDCR↓"]
        rows:
          - ["DeBERTa-v3-base", 0.815, 0.48, 0.34, 0.813, 0.661]
          - ["DeBERTa-v3-large", 0.845, 0.52, 0.31, 0.817, 0.652]
    figures_description:
      - "Scatter plot: base vs large 的 per-document CED margin，对角线附近聚集说明两个模型高度一致，偏离对角线的点标注具体文档，分析 large 模型在哪些 case 上更好/更差"
    analysis: >
      NLI 模型从 base 升级到 large 带来 CED 信号质量的一致改善（discrimination accuracy +3pp），
      但 downstream 的 RSFT 收益递减（evi_f1 +0.37pp）。这表明当前 pipeline 的瓶颈已不在
      NLI 模型能力上。对 RC1 的回应可以是：即使 base model 的 NLI 有一定 lexical overlap bias
      （Pearson r=0.34），CED 的 contrastive 设计已足够有效，升级 NLI 模型的边际收益有限。
      建议论文主实验用 base（计算成本更低且结果相近），appendix 报告 large 结果。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff4caebc-c1ea-482c-afc2-22af74485ef1",
  "isSidechain": false,
  "requestId": "req_011Cb4KwoqfTS8YZuTFfdsQZ",
  "type": "assistant",
  "uuid": "ad424d1c-0c20-4510-9e68-15143b06bfc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "e1759942-0054-49a6-b6ff-76321594a118",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TSry9TwQDsERiknJJuVs1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18625,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16807,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16807,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18625
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心方法有效但 CED 优势不够突出：CED vs flat-NLI 差异存在但较小，EDCR 改善有限 核心假设：['Dev→test 有一定衰减（rel_f1 -2~4pp, evi_f1 -1~3pp），但仍显著优于 SFT baseline', 'CED-scored RSFT 优于 flat-N…",
  "leafUuid": "ad424d1c-0c20-4510-9e68-15143b06bfc8",
  "sessionId": "e1759942-0054-49a6-b6ff-76321594a118"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier experiments for FREIGE DocRE evidence grounding",
  "sessionId": "e1759942-0054-49a6-b6ff-76321594a118"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心方法有效但 CED 优势不够突出：CED vs flat-NLI 差异存在但较小，EDCR 改善有限 核心假设：['Dev→test 有一定衰减（rel_f1 -2~4pp, evi_f1 -1~3pp），但仍显著优于 SFT baseline', 'CED-scored RSFT 优于 flat-N…",
  "leafUuid": "ad424d1c-0c20-4510-9e68-15143b06bfc8",
  "sessionId": "e1759942-0054-49a6-b6ff-76321594a118"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier experiments for FREIGE DocRE evidence grounding",
  "sessionId": "e1759942-0054-49a6-b6ff-76321594a118"
}
```

---
