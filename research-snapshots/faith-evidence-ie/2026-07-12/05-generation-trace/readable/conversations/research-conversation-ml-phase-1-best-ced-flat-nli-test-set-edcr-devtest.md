# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：所有核心假设成立：CED 对比性信号显著优于 flat-NLI，test set 数字稳健，EDCR 大幅下降 核心假设：['Dev→test 泛化良好

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/ffd23ddb-103f-41e4-8b99-29b89164a3ab.jsonl`
- **Structured JSON:** [`c329b9b47fe45d4959ad.json`](../../sessions/c3/c329b9b47fe45d4959ad.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T12:03:54.815Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T12:03:54.815Z",
  "sessionId": "ffd23ddb-103f-41e4-8b99-29b89164a3ab",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：所有核心假设成立：CED 对比性信号显著优于 flat-NLI，test set 数字稳健，EDCR 大幅下降\n核心假设：['Dev→test 泛化良好，rel_f1 和 evi_f1 衰减 <2pp', 'CED-scored RSFT 在 evi_f1 和 EDCR 上显著优于 flat-NLI-scored RSFT（evi_f1 gap ≥1.5pp, EDCR gap ≥3pp）', 'Test set evi_f1 明确超过 DREEAM 57.34（在可比评估协议下）', 'CED-as-reranker 进一步压低 EDCR 至 55% 以下，提供无需训练的 evidence 改进路径', 'DREEAM dev set 复现确认数字可比，消除 RC3 评测可比性疑虑']\n关键指标范围：{'test_rel_f1': [0.44, 0.47], 'test_evi_f1': [0.79, 0.82], 'test_edcr': [0.5, 0.6], 'ced_vs_flatnli_evi_f1_gap': [0.015, 0.03], 'ced_vs_flatnli_edcr_gap': [0.03, 0.06], 'dreeam_dev_evi_f1_reproduced': [0.55, 0.58], 'reranker_edcr': [0.45, 0.55]}\n叙事方向：原始 framing 完全成立。四个 Claim 均有强实验支撑：(C1) 首个 LLM DocRE 同时输出抽取+可验证证据， test set 全面超越 encoder SOTA；(C2) CED 对比信号显著优于 flat-NLI，证明 contrastive margin 是 evidence grounding 的关键；(C3) GRPO 全线失败分析作为 cautionary tale；(C4) EDCR 作为 新评估维度揭示 Evi-F1 的盲区。论文叙事以 CED 方法创新为主线，GRPO 失败和 EDCR 指标为辅线。 可冲 EMNLP Main oral。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: faith-evidence-ie\nvenue: EMNLP 2026 Main\nfocus: 核心关注点: (1) RSFT+CED 方法是否足够新颖（RSFT 本身不新，CED 作为 scoring function 的创新度）; (2) EDCR 63-66% 仍偏高，evidence 质量提升是否足够显著; (3) GRPO 全线失败的分析作为 contribution 是否有说服力; (4) 缺少 CED vs flat-NLI RSFT ablation（Claim 2 核心实验未做）\n\n## paper_framing.md\n\n# Paper Framing — FREIGE\n\n> **状态**: POST-MVP (MVP-1 + MVP-2 均 PASS，进入 Research 阶段)\n> **最后更新**: 2026-05-15\n\n## Target Venue\n\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\n- Stretch: ARR May 25 (10 days, 极紧，仅在实验全部顺利时考虑)\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\n\n## Core Insight\n\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。朴素 NLI faithfulness reward 可被 entity-mentioning distractor 句子游戏——共享实体但不支持具体关系的句子仍获正面蕴含分数。\n\n**CED (Contrastive Evidence Discrimination)** 通过文档内 hard negative 对比，将 evidence 质量评估从\"是否蕴含\"升级为\"是否比最佳干扰句更蕴含\"——本质上是 evidence grounding 场景下的 **anti-reward-overoptimization mechanism**（连接 Gao et al. 2023 reward overoptimization 理论）。\n\n**MVP 关键发现**: CED 作为在线 RL (GRPO) reward 导致 catastrophic forgetting（3 种 reward type × 多个 lr 全线失败），但作为离线 RL (RSFT) 的候选筛选信号极其有效——4 组超参配置均稳定超过 SFT baseline。**方法论结论**: 对结构化 IE 任务，CED 应作为离线质量信号而非在线训练奖励。\n\n## Story Arc\n\n1. **Problem**: LLM DocRE 无证据 → 部署障碍（human-in-the-loop KB population、生物医学审计、RAG 溯源）\n2. **Why naive reward fails**: flat-NLI 被 entity-sharing distractors 欺骗（SFT EDCR=71.2%，大量引用干扰句）\n3. **Why online RL fails**: GRPO+CED/flat-NLI/extract-only 全部 catastrophic forgetting（reward ↑ + rel_f1 ↓ 至 <0.02）\n4. **Solution**: CED 作为离线质量信号 + RSFT（rejection sampling fine-tuning）：SFT 模型生成 N 候选 → CED 打分筛选 → 微调，规避在线 RL 的遗忘风险\n5. **Theoretical grounding**: 连接 LongRLVR (ICLR 2026) evidence grounding 梯度消失分析 + \"RSFT=PPO\" (ICML 2025) 等价性理论\n6. **Result**: 首个 LLM-based DocRE 方法同时生成抽取和可验证证据\n\n## Core Claims\n\n### Claim 1 (Main): CED-scored RSFT 使 LLM 同时生成抽取和忠实证据\n- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法\n- RSFT+CED: rel_f1 +3.9~6.0pp over SFT, evi_f1 +1.1~2.1pp, EDCR -4.8~7.7pp\n- **MVP-2 已验证**: 4/4 configs PASS\n- **Research 需要**: test set 评估，DREEAM/SAIS Evi-F1 直接对比\n\n### Claim 2 (Ablation): CED scoring 优于 flat-NLI scoring 用于 RSFT\n- CED-filtered RSFT vs flat-NLI-filtered RSFT 的 evi_f1 和 EDCR 差异\n- CED 的对比性 margin 过滤掉 distractor-heavy 候选\n- **Research 需要**: flat-NLI scored RSFT ablation（核心实验）\n\n### Claim 3 (Analysis): 在线 RL 在结构化 IE 上 catastrophically forget\n- GRPO+QLoRA 在 3 种 reward type × 多个 lr 下全线失败\n- 关键对比: evi_f1 在 GRPO 下提升至 0.850（>SFT 0.798）但 rel_f1 崩至 <0.02——CED 驱动了 evidence 学习但在线 RL 摧毁了抽取能力\n- RSFT 规避此问题：不修改 policy gradient，只筛选训练数据\n- **MVP 已有完整证据**: D031/D033 GRPO 判死，D039 RSFT 成功\n\n### Claim 4 (Evaluation): EDCR 作为独立评估指标\n- EDCR = |entity-sharing non-gold cited sentences| / |total cited sentences|\n- Evi-F1 盲区：不惩罚 plausible-looking distractor citations\n- SFT EDCR=71.2%, RSFT+CED EDCR=63.5~66.4%（方向正确但差距有限，需坦诚讨论）\n- **Research 需要**: cross-method diagnostic table, CED vs flat-NLI EDCR 对比\n\n## MVP Evidence Summary\n\n| Config | rel_f1 | Δ rel_f1 | evi_f1 | EDCR | 状态 |\n|--------|--------|----------|--------|------|------|\n| SFT baseline | 0.4057 | — | 0.7979 | 0.7118 | ✅ |\n| RSFT r1 (3ep, α=128, s42) | 0.4449 | +3.92pp | 0.8187 | 0.6565 | ✅ |\n| RSFT r1 (s44) | 0.4655 | +5.98pp | 0.8087 | 0.6350 | ✅ |\n| RSFT r2a (1ep, α=128) | 0.4494 | +4.37pp | 0.8108 | 0.6641 | ✅ |\n| RSFT r2b (1ep, α=32, lr=1e-5) | 0.4493 | +4.36pp | 0.8128 | 0.6609 | ✅ |\n| GRPO best (lr=5e-5, ckpt-90) | 0.2110 | -19.5pp | 0.5750 | — | ❌ |\n| GRPO best (lr=5e-6, ckpt-100) | 0.0138 | -39.2pp | 0.8500 | 0.9900 | ❌ |\n\n## Anticipated Reviewer Concerns\n\n### RC1: NLI reward 信号质量（高概率攻击）\n- **攻击**: \"DeBERTa-v3-base 的 NLI 判断有 lexical overlap bias，CED 训练信号有噪声\"\n- **已验证**: MVP-1 Pearson r=0.34（NLI vs lexical overlap），远低于 0.7，证明非捷径\n- **Research 补充**: DeBERTa-base vs DeBERTa-large 对比\n\n### RC2: Gold evidence 标注不完整导致 false distractor\n- **攻击**: \"被标为 distractor 的句子可能是 annotator 遗漏的有效证据\"\n- **应对**: CED margin 的 self-correcting property——如果 false distractor 真正蕴含关系，其 p_neg 高 → margin 小 → 惩罚弱\n- **Research 补充**: false-distractor 鲁棒性量化分析\n\n### RC3: 评测可比性\n- **攻击**: \"生成式 evidence 如何与 DREEAM 的 attention-based evidence 做 apple-to-apple 对比？\"\n- **应对**: 模型输出显式句子索引 [S_i]，直接映射句子级 Evi-F1；辅助指标用 RoBERTa-large-MNLI（非训练用 DeBERTa）避免 circular evaluation\n\n### RC4: 单数据集 + 单模型泛化性\n- **攻击**: \"只在 DocRED + Qwen3-4B 上验证\"\n- **Research**: Re-DocRED 扩展 + Qwen3-1.7B/8B model size ablation\n\n### RC5: RSFT vs GRPO 是否公平对比\n- **攻击**: \"GRPO 失败可能是超参问题而非方法论问题\"\n- **应对**: 完整 GRPO 轨迹——3 种 reward × 多个 lr × 全 checkpoint eval；D020 控制变量下 CED 是唯一存活的 reward type\n\n### RC6: EDCR 63-66% 仍然偏高，CED 对证据精确度提升有限\n- **攻击**: \"RSFT+CED 的 EDCR 只比 SFT 低 5-8pp，证据质量提升不够显著\"\n- **应对**: (1) CED 在 RSFT 中是间接作用（筛选训练数据），非直接 reward；(2) CED-as-reranker 可能更直接降低 EDCR；(3) 需要 flat-NLI RSFT 对比证明 CED 方向正确\n- **Research**: CED reranker PoC（运行中），top_k ablation\n\n### RC7: 方法过于简单\n- **应对**: 简洁是优点——RSFT 方法论已被证明理论等价于 PPO (ICML 2025)，CED 创新在于打分函数设计而非框架复杂度\n\n## Key Baselines (8+)\n\n1. **SFT-only**: Qwen3-4B + LoRA SFT on DocRED gold — 无 RL\n2. **RSFT flat-NLI**: flat-NLI scored RSFT — 无 contrastive signal（核心 ablation）\n3. **RSFT CED (FREIGE)**: CED scored RSFT — 主方法\n4. **CED-as-reranker**: 推理时 CED 重排 SFT 候选（无训练）— 运行中\n5. **GRPO+CED**: 在线 RL with CED reward — negative baseline\n6. **DREEAM**: RoBERTa-large encoder — evidence SOTA (Evi-F1 57.34)\n7. **SAIS**: RoBERTa encoder — evidence baseline (Evi-F1 55.67)\n8. **DocKS-RAG**: GNN+RAG — extraction SOTA (F1 63.59, 无 evidence)\n9. **LMRC**: LLaMA3.1-8B — generative LLM SOTA (F1 60.69, 无 evidence)\n\n## Publishability Threshold\n\n- **必要条件**: RSFT+CED 在 test set 上 Evi-F1 > DREEAM 57.34 AND rel_f1 显著 > SFT baseline\n- **充分条件**: 上述 + CED vs flat-NLI RSFT Evi-F1/EDCR 差异显著 + GRPO 分析完整\n- **Failure pivot**: Evi-F1 < 57.34 on test set → 转为 analysis contribution（在线 vs 离线 RL for structured IE）\n\n## Research Phase Priorities\n\n| Priority | 实验 | Claim | 预估 GPU-hours |\n|----------|------|-------|---------------|\n| P0 | CED vs flat-NLI RSFT ablation | C2 | ~20h |\n| P0 | Test set evaluation (RSFT best config) | C1 | ~4h |\n| P0 | EDCR pipeline 验证 + cross-method table | C4 | ~2h |\n| P0 | DREEAM/SAIS Evi-F1 baseline reproduction | C1 | ~8h |\n| P1 | CED-as-reranker (running) | C1 bonus | ~6h |\n| P1 | Model size ablation (1.7B/8B) | RC4 | ~24h |\n| P1 | Re-DocRED extension | RC4 | ~12h |\n| P1 | top_k ablation (k=1 vs k=3) | RC6 | ~8h |\n| P2 | GRPO forgetting 详细分析 + 可视化 | C3 | ~4h |\n| P2 | DeBERTa-base vs large NLI 对比 | RC1 | ~4h |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选\n    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py\n    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set\n    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_003\n  claim: 4\n  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing\n    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_004\n  claim: 1\n  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)\n    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_005\n  claim: 1\n  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: mvp2_ced_reranker_poc\n  status: RUNNING\n- id: plan_006\n  claim: 1\n  description: 'Model size ablation: Qwen3-1.7B 和 Qwen3-8B 上复现 RSFT+CED pipeline，验证方法对模型规模的泛化性。应对\n    RC4。'\n  priority: P1\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Re-DocRED extension: 在 Re-DocRED（修正 false negative 标注的版本）上评估，验证 RSFT+CED\n    在更干净标注下的表现。应对 RC4。'\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  registry_id: null\n  status: planned\n- id: plan_008\n  claim: 2\n  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格\n    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_009\n  claim: 3\n  description: 'GRPO forgetting 详细分析: 整理全部 GRPO checkpoint 的 rel_f1/evi_f1/EDCR 轨迹，绘制\n    forgetting dynamics 可视化（reward vs task performance 曲线），支撑 Claim 3 的论述。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer\n    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_mvp1\n  claim: 1\n  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing\n    distractor 的能力验证'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: mvp1_ced_signal\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_margin: 0.48\n    discrimination_accuracy: 0.815\n    pearson_r_margin_jaccard: 0.34\n    pass: true\n- id: plan_mvp2_sft\n  claim: 1\n  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mvp2_sft_warmup\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.72\n    accuracy: 0.835\n- id: plan_mvp2_rsft\n  claim: 1\n  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部\n    PASS'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_mvp1\n  - plan_mvp2_sft\n  registry_id: mvp2_rsft_train_r1\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.0483\n    num_preds: 848\n    sft_baseline_rel_f1: 0.4057\n    failure_mode: relation_ontology_collapse_to_freetext\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n- id: plan_mvp2_grpo\n  claim: 3\n  description: 'GRPO+QLoRA 全线失败: 3 种 reward type × 多个 lr, catastrophic forgetting\n    negative result'\n  priority: P0\n  gpu_budget_hours: 60\n  deps:\n  - plan_mvp2_sft\n  registry_id: mvp2_grpo_ced_lr5e6_r1\n  status: DONE\n  conclusion: killed\n\n\n## registry (completed experiments)\n\n- exp_id: mvp1_ced_signal\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_margin: 0.48\n    discrimination_accuracy: 0.815\n    pearson_r_margin_jaccard: 0.34\n    pass: true\n- exp_id: smoke_test_grpo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_sft_warmup\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.72\n    accuracy: 0.835\n- exp_id: precompute_nli_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_grpo_ced\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_extract\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_sft_eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_extract_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: mvp2_grpo_extract_r3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_sft_eval_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    ign_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    precision: 0.4043\n    recall: 0.407\n    evi_precision: 0.8035\n    evi_recall: 0.7924\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.626\n    n_parseable: 617\n    n_truncated: 367\n    n_predictions: 18815\n    inference_time_seconds: 6484.7\n- exp_id: mvp2_sft_eval_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    ign_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    precision: 0.4043\n    recall: 0.407\n    evi_precision: 0.8035\n    evi_recall: 0.7924\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.626\n    n_parseable: 617\n    n_truncated: 367\n    n_predictions: 18815\n- exp_id: mvp2_grpo_ced_kl001_r2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001_r3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001_r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_step: 100\n    train_runtime_s: 9069.88\n    reward_final: 1.195\n    f1_reward_final: 0.573\n    ced_reward_final: 0.328\n    format_reward_final: 0.293\n    frac_zero_std_final: 0.2\n    kl_final: 0.118\n    loss_final: -0.009\n    grad_norm_final: 0.14\n    entropy_final: 0.067\n    completion_length_mean_final: 520.8\n    best_reward_step: 90\n    best_reward: 1.37\n    best_f1_reward: 0.72\n    best_ced_reward: 0.353\n- exp_id: mvp2_grpo_extract_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_early\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    f1: 0.1563\n    ign_f1: 0.1563\n    evi_f1: 0.5643\n    edcr: 0.8858\n    precision: 0.2356\n    recall: 0.1169\n    evi_precision: 0.4864\n    evi_recall: 0.6721\n    format_ok_rate: 0.999\n    n_parseable: 984\n    n_truncated: 11\n    n_predictions: 9250\n    tp: 1421\n    pred_count: 6032\n    gold_count: 12151\n- exp_id: mvp2_grpo_flatnli_r6\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    steps_completed: 25\n    final_frac_zero_std: 0.9\n    final_f1_reward: 0\n    final_flat_nli_reward: 0\n    final_format_reward: 0.293\n    collapse_step: 25\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.00296\n    rel_precision: 0.00314\n    rel_recall: 0.0028\n    evi_f1: 0.72\n    evi_precision: 0.6429\n    evi_recall: 0.8182\n    edcr: 0.9983\n    n_parseable: 984\n    n_truncated: 24\n    n_predictions: 11621\n    tp: 34\n    pred_count: 10839\n    gold_count: 12151\n    inference_time_seconds: 5211.4\n- exp_id: mvp2_eval_ced_kl001_r4_multi\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    checkpoint-10:\n      f1: 0.003\n      ign_f1: 0.003\n      evi_f1: 0.72\n      edcr: 0.9983\n      format_ok_rate: 0.999\n    checkpoint-20:\n      f1: 0.0088\n      ign_f1: 0.0088\n      evi_f1: 0.423\n      edcr: 0.9954\n      format_ok_rate: 0.999\n    checkpoint-30:\n      f1: 0.0338\n      ign_f1: 0.0338\n      evi_f1: 0.5889\n      edcr: 0.9798\n      format_ok_rate: 1\n    checkpoint-50:\n      f1: 0.1563\n      ign_f1: 0.1563\n      evi_f1: 0.5643\n      edcr: 0.8858\n      format_ok_rate: 0.999\n    checkpoint-60:\n      f1: 0.1467\n      ign_f1: 0.1467\n      evi_f1: 0.5763\n      edcr: 0.9062\n      format_ok_rate: 1\n    checkpoint-90:\n      f1: 0.2108\n      ign_f1: 0.2108\n      evi_f1: 0.5666\n      edcr: 0.8584\n      format_ok_rate: 1\n- exp_id: mvp2_eval_ced_kl001_r4_step100\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.2167\n    ign_f1: 0.2167\n    precision: 0.2849\n    recall: 0.1749\n    evi_f1: 0.5746\n    evi_precision: 0.5244\n    evi_recall: 0.6353\n    edcr: 0.8539\n    pred_count: 7460\n    gold_count: 12151\n    tp: 2125\n    n_truncated: 21\n    format_ok_rate: 1\n- exp_id: mvp2_eval_ced_kl001_r4_last\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt90\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_high\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    checkpoint_60:\n      rel_f1: 0.1467\n      ign_f1: 0.1467\n      precision: 0.1909\n      recall: 0.1192\n      evi_f1: 0.5763\n      edcr: 0.9062\n      pred_count: 10041\n      gold_count: 12151\n      n_truncated: 16\n      format_ok_rate: 1\n    note: Only ckpt-60 completed. Process died during ckpt-70 inference at 8% (5/62\n      batch). ckpt-80/90 never started.\n- exp_id: mvp2_eval_ced_kl001_r4_step90\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.2108\n    ign_f1: 0.2108\n    evi_f1: 0.5666\n    edcr: 0.8584\n    pred_count: 11160\n    n_truncated: 22\n    format_ok_rate: 1\n    n_documents: 985\n- exp_id: mvp2_grpo_ced_lr5e6_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_p1_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_rp_r1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt7080\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_rp_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt20\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0077\n    rel_precision: 0.0071\n    rel_recall: 0.0084\n    evi_f1: 0.628\n    evi_precision: 0.855\n    evi_recall: 0.496\n    edcr: 0.993\n    format_ok_rate: 0.991\n    field_compliance_rate: 0.399\n    pred_count: 14440\n    gold_count: 12151\n    tp: 102\n    n_truncated: 587\n    inference_time_seconds: 6370.4\n- exp_id: mvp2_eval_lr5e6_r1_ckpt40\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt40_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0071\n    precision: 0.0066\n    recall: 0.0078\n    evi_f1: 0.7584\n    evi_precision: 0.9113\n    evi_recall: 0.6494\n    edcr: 0.9942\n    format_ok_rate: 0.9939\n    field_compliance_rate: 0.5675\n    pred_count: 14434\n    gold_count: 12151\n    tp: 95\n    n_truncated: 424\n    inference_time_seconds: 6152\n- exp_id: mvp2_eval_lr5e6_rp_r2_ckpt20\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_sft_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    pred_count: 12234\n    gold_count: 12151\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.998\n    field_compliance_rate: 0.6264\n    n_truncated: 367\n    inference_time_seconds: 6138.5\n- exp_id: mvp2_eval_lr5e6_r1_ckpt60\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt80\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0116\n    ign_f1: 0.0116\n    precision: 0.0109\n    recall: 0.0124\n    evi_f1: 0.828\n    evi_precision: 0.928\n    evi_recall: 0.748\n    edcr: 0.993\n    format_ok_rate: 0.999\n    field_compliance_rate: 0.788\n    pred_count: 13828\n    gold_count: 12151\n    n_truncated: 210\n    inference_time_seconds: 6099\n- exp_id: mvp2_eval_lr5e6_r1_ckpt60_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0093\n    precision: 0.0085\n    recall: 0.0103\n    evi_f1: 0.81\n    edcr: 0.993\n    format_ok_rate: 0.998\n    pred_count: 14626\n    gold_count: 12151\n    tp: 125\n    inference_time_seconds: 6152\n- exp_id: mvp2_eval_lr5e6_r1_ckpt100\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0138\n    rel_precision: 0.0132\n    rel_recall: 0.0144\n    ign_f1: 0.0138\n    evi_f1: 0.8504\n    evi_precision: 0.9256\n    evi_recall: 0.7866\n    edcr: 0.9876\n    format_ok_rate: 0.999\n    field_compliance_rate: 0.8162\n    evidence_format_rate: 0.8162\n    tp: 175\n    pred_count: 13300\n    gold_count: 12151\n    n_predictions: 15498\n    n_truncated: 181\n    n_documents: 985\n    n_parseable: 984\n    inference_time_seconds: 5901.7\n- exp_id: mvp2_diversity_probe\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    unique_triples_t07: 5\n    unique_triples_t10: 8\n    jaccard_t07: 0.17\n    jaccard_t10: 0.051\n    format_ok_rate_t07: 0.5\n    format_ok_rate_t10: 0.438\n    n_samples: 3\n    n_generations: 8\n    note: 'unique_triples_t07 corrected from 7 to 5.0 (mean). Reviewer: format_ok\n      ~34% after fix, ''diversity'' was JSON key name variants not semantic diversity'\n- exp_id: mvp2_rsft_generate\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    generation_count: 5288\n    unique_docs: 659\n    format_compliance: 0.998\n    diversity_range: 7.5-7.8/8\n    exit_code: 0\n- exp_id: mvp2_rsft_ced_scoring\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    input_generations: 21952\n    selected_samples: 2718\n    unique_docs: 2691\n    selection_rate: 0.124\n    mean_f1: 0.6157\n    mean_ced: 0.6683\n    f1_range:\n    - 0.1026\n    - 1\n    zero_f1_samples: 0\n    selection_strategy: top_k=1\n    f1_threshold: 0.1\n- exp_id: mvp2_rsft_train_r1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.0483\n    num_preds: 848\n    sft_baseline_rel_f1: 0.4057\n    failure_mode: relation_ontology_collapse_to_freetext\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n- exp_id: mvp2_rsft_train_r1_s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.7622\n    train_loss: 0.6148\n    eval_entropy: 0.6724\n    mean_token_accuracy: 0.8291\n    total_steps: 510\n    epochs: 3\n    training_hours: 1.99\n- exp_id: mvp2_rsft_train_r1_s44\n  name: ''\n  status: ANALYZING\n  conclusion: success\n  metrics:\n    rel_f1: 0.4655\n    evi_f1: 0.8087\n    edcr: 0.635\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0598\n    delta_evi_f1: 0.0108\n    mvp2_pass: true\n- exp_id: mvp2_rsft_ced_scoring_topk3\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_eval_rsft_s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_ced_reranker_poc\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_rsft_diagnosis\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    root_cause: overfitting_plus_sft_knowledge_overwrite\n    truncated_json_samples: 170\n    truncated_pct: 6.3\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n    lora_scaling: 2\n    rsft_zero_relation_samples: 170\n    sft_zero_relation_docs: 26\n    rsft_mean_relations: 11.2\n    sft_mean_relations: 12.5\n- exp_id: mvp2_rsft_train_r2_fix\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_rsft_r2a\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_rsft_r2b\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_eval_rsft_r1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4449\n    evi_f1: 0.8187\n    edcr: 0.6565\n    num_preds: 15307\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0392\n    delta_evi_f1: 0.0208\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r2a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4494\n    ign_f1: 0.4494\n    evi_f1: 0.8108\n    edcr: 0.6641\n    precision: 0.4512\n    recall: 0.4475\n    evi_precision: 0.8143\n    evi_recall: 0.8073\n    format_ok_rate: 1\n    n_predictions: 15482\n    n_truncated: 208\n    inference_time_s: 5967.2\n- exp_id: mvp2_eval_rsft_r2b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4493\n    ign_f1: 0.4493\n    evi_f1: 0.8128\n    edcr: 0.6609\n    precision: 0.4566\n    recall: 0.4424\n    evi_precision: 0.8201\n    evi_recall: 0.8056\n    pred_count: 14829\n    format_ok: 983/985\n    truncated: 179\n    inference_time_s: 5862\n- exp_id: mvp2_eval_rsft_s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_s43_r2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_eval_rsft_r2b_maxtok1536\n  name: ''\n  status: RUNNING\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_r2b_maxtok1536_r2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T12:03:54.820Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T12:03:54.820Z",
  "sessionId": "ffd23ddb-103f-41e4-8b99-29b89164a3ab"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-15T12:03:54.844Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：所有核心假设成立：CED 对比性信号显著优于 flat-NLI，test set 数字稳健，EDCR 大幅下降
核心假设：['Dev→test 泛化良好，rel_f1 和 evi_f1 衰减 <2pp', 'CED-scored RSFT 在 evi_f1 和 EDCR 上显著优于 flat-NLI-scored RSFT（evi_f1 gap ≥1.5pp, EDCR gap ≥3pp）', 'Test set evi_f1 明确超过 DREEAM 57.34（在可比评估协议下）', 'CED-as-reranker 进一步压低 EDCR 至 55% 以下，提供无需训练的 evidence 改进路径', 'DREEAM dev set 复现确认数字可比，消除 RC3 评测可比性疑虑']
关键指标范围：{'test_rel_f1': [0.44, 0.47], 'test_evi_f1': [0.79, 0.82], 'test_edcr': [0.5, 0.6], 'ced_vs_flatnli_evi_f1_gap': [0.015, 0.03], 'ced_vs_flatnli_edcr_gap': [0.03, 0.06], 'dreeam_dev_evi_f1_reproduced': [0.55, 0.58], 'reranker_edcr': [0.45, 0.55]}
叙事方向：原始 framing 完全成立。四个 Claim 均有强实验支撑：(C1) 首个 LLM DocRE 同时输出抽取+可验证证据， test set 全面超越 encoder SOTA；(C2) CED 对比信号显著优于 flat-NLI，证明 contrastive margin 是 evidence grounding 的关键；(C3) GRPO 全线失败分析作为 cautionary tale；(C4) EDCR 作为 新评估维度揭示 Evi-F1 的盲区。论文叙事以 CED 方法创新为主线，GRPO 失败和 EDCR 指标为辅线。 可冲 EMNLP Main oral。


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
  "promptId": "5b337c51-e106-48bb-ad36-894a621c5a72",
  "type": "user",
  "uuid": "59d91e29-20aa-46d1-a54c-20707d104756",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "ffd23ddb-103f-41e4-8b99-29b89164a3ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T12:03:54.843Z_

```json
{
  "parentUuid": "59d91e29-20aa-46d1-a54c-20707d104756",
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
  "uuid": "1a41d7f5-03d2-401e-a140-505a887a00b3",
  "timestamp": "2026-05-15T12:03:54.843Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "ffd23ddb-103f-41e4-8b99-29b89164a3ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T12:03:54.843Z_

```json
{
  "parentUuid": "1a41d7f5-03d2-401e-a140-505a887a00b3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7d9c10c2-70cc-4066-b95f-25bab1606cdd",
  "timestamp": "2026-05-15T12:03:54.843Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "ffd23ddb-103f-41e4-8b99-29b89164a3ab",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有核心假设成立：CED 对比性信号显著优于 flat-NLI，test set 数字稳健，EDCR 大幅下降 核心假设：['Dev→test 泛化良好，rel_f1 和 evi_f1 衰减 <2pp', 'CED-scored RSFT 在 evi_f1 和 EDCR 上显著优于 flat-NLI-scor…",
  "leafUuid": "7d9c10c2-70cc-4066-b95f-25bab1606cdd",
  "sessionId": "ffd23ddb-103f-41e4-8b99-29b89164a3ab"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "CED-scored RSFT for evidence grounding in LLM DocRE",
  "sessionId": "ffd23ddb-103f-41e4-8b99-29b89164a3ab"
}
```

---

### Assistant

_source line 8 · 2026-05-15T12:04:30.350Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for each planned experiment in the experiment_plan, under the "best" tier scenario. I need to provide rationale for each prediction based on the best-case definitions provided.

Let me carefully go through each planned experiment and predict results consistent with the "best" tier:

**Best tier definition:**
- All core assumptions hold
- CED contrastive signal significantly better than flat-NLI
- Test set numbers robust
- EDCR drops significantly

**Key metric ranges for best:**
- test_rel_f1: [0.44, 0.47]


- test_evi_f1: [0.79, 0.82]
- test_edcr: [0.5, 0.6]
- ced_vs_flatnli_evi_f1_gap: [0.015, 0.03]
- ced_vs_flatnli_edcr_gap: [0.03, 0.06]
- dreeam_dev_evi_f1_reproduced: [0.55, 0.58]
- reranker_edcr: [0.45, 0.55]

Now I'm laying out the core assumptions that underpin these predictions, starting with how the development set performance translates to test performance.

The key claims I need to validate are that CED-scored retrieval-augmented fine-tuning substantially outperforms flat-NLI scoring, that our test results clearly beat DREEAM's reported numbers, and that using CED as a reranker provides an additional path to improvement without requiring retraining. I've also confirmed that reproducing DREEAM's dev set numbers matches their reported performance, which rules out any evaluation protocol mismatches.

For the first planned experiment comparing CED versus flat-NLI RSFT, this is where I'll directly test the core claim about scoring method superiority. I expect CED to show meaningful gains in the best tier, though flat-NLI should still provide some improvement over the baseline.

Looking at the specific numbers, I'm seeing that flat-NLI RSFT should land around rel_f1 0.44 and evi_f1 0.795, while my best CED configuration achieves rel_f1 0.4655 and evi_f1 0.8087. That's roughly a 1.4 percentage point gap in evidence F1, though the target for the best tier is at least 1.5 points. Let me recalibrate—comparing the strongest CED variants which range from 0.8087 to 0.8187 against flat-NLI's expected 0.793 should give me the gap I'm looking for, with EDCR showing an even larger separation around 6 percentage points.

Now I'm planning the test set evaluation, expecting the best configurations to show rel_f1 between 0.44-0.47, evi_f1 between 0.79-0.82, and EDCR between 0.5-0.6, with minimal decay from dev performance. I also need to compile EDCR results across all methods to build out a comprehensive comparison table.

Looking ahead at several other experiments: verifying the DREEAM baseline reproduces the paper's results around 57.34 evi_f1, testing CED as a reranker which could potentially outperform training-based methods on EDCR, running model size ablations across 1.7B and 8B scales, and extending to Re-DocRED to confirm improvements generalize.

I also need to plan ablations on the top_k filtering parameter, analyze catastrophic forgetting patterns in GRPO training, and compare NLI model choices between DeBERTa-base and large variants. For the already-completed experiments, I should note their actual results but frame them consistently with the best-tier predictions I'm using for the planned experiments.

Looking back at the status breakdown, I need to focus on the planned and running experiments—plan_001 through plan_010—since those are the ones needing predicted metrics. Let me structure the YAML output now with detailed data for each of these.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d9c10c2-70cc-4066-b95f-25bab1606cdd",
  "isSidechain": false,
  "requestId": "req_011Cb4KedHwToU93DQmnZNye",
  "type": "assistant",
  "uuid": "ca16e4a0-b277-42c6-92db-445d9b8f9aa4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "ffd23ddb-103f-41e4-8b99-29b89164a3ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cg9A7sMxEPU7trgVKyByqo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18507,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12949,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18507,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12949,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18507
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

_source line 9 · 2026-05-15T12:07:45.491Z_

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立。四个 Claim 均有强实验支撑：(C1) 首个 LLM DocRE 同时输出抽取+可验证证据，test set 全面超越
  encoder SOTA；(C2) CED 对比信号显著优于 flat-NLI，证明 contrastive margin 是 evidence grounding
  的关键；(C3) GRPO 全线失败分析作为 cautionary tale；(C4) EDCR 作为新评估维度揭示 Evi-F1 的盲区。论文叙事以 CED
  方法创新为主线，GRPO 失败和 EDCR 指标为辅线。可冲 EMNLP Main oral。

imagined_experiments:

  - name: "CED vs flat-NLI RSFT ablation"
    plan_id: "plan_001"
    description: >
      用 flat-NLI scoring（非 contrastive）筛选 RSFT 训练数据，与 CED scoring 对比。
      flat-NLI 使用同一 DeBERTa-v3-base NLI 模型，但仅计算 p(entail | premise=sentence, hypothesis=triple)，
      不做 gold vs distractor 的对比 margin。相同 RSFT 训练流程（top_k=1, 1ep, α=128, lr=2e-5）。
    expected_results:
      flatnli_rsft_rel_f1: 0.438
      flatnli_rsft_evi_f1: 0.793
      flatnli_rsft_edcr: 0.693
      flatnli_rsft_evi_precision: 0.798
      flatnli_rsft_evi_recall: 0.788
      flatnli_rsft_selected_samples: ~2800
      flatnli_rsft_selection_rate: 0.128
      ced_best_rel_f1: 0.4655
      ced_best_evi_f1: 0.8187
      ced_best_edcr: 0.6350
      evi_f1_gap_ced_minus_flatnli: 0.026
      edcr_gap_flatnli_minus_ced: 0.058
      rel_f1_gap_ced_minus_flatnli: 0.028
    result_rationale: >
      flat-NLI scoring 仍有正向信号（NLI 概率高的候选确实倾向于引用正确证据），因此 flat-NLI RSFT 相比 SFT baseline
      (rel_f1=0.4057, evi_f1=0.7979, EDCR=0.7118) 仍有改善，但改善幅度显著小于 CED。核心原因：flat-NLI
      无法区分 entity-sharing distractor 与 genuine evidence——两者对朴素 NLI 模型都获得高蕴含分数，
      导致 flat-NLI 筛选出的训练数据中仍包含大量 distractor-heavy 候选。CED 的 margin = p_pos - p_neg
      天然惩罚这类候选（distractor 的 p_neg 高 → margin 小 → 被过滤）。在 best 档位下，MVP-1 已验证
      CED discrimination accuracy=0.815、mean margin=0.48，这些信号强度足以在 RSFT 筛选中产生显著差异。
      evi_f1 gap ~2.6pp 和 EDCR gap ~5.8pp 反映 CED 对 distractor 的精准过滤作用。
      rel_f1 gap ~2.8pp 说明更干净的 evidence 训练信号也间接提升抽取质量（减少因错误证据引入的噪声梯度）。
    tables:
      - name: "Table: CED vs flat-NLI RSFT ablation (dev set)"
        content: |
          | Method           | rel_f1 | evi_f1 | EDCR   | Δevi_f1 | ΔEDCR  |
          |------------------|--------|--------|--------|---------|--------|
          | SFT baseline     | 0.4057 | 0.7979 | 0.7118 | —       | —      |
          | RSFT flat-NLI    | 0.438  | 0.793  | 0.693  | -0.005  | -0.019 |
          | RSFT CED (r1)    | 0.4449 | 0.8187 | 0.6565 | +0.021  | -0.055 |
          | RSFT CED (s44)   | 0.4655 | 0.8087 | 0.6350 | +0.011  | -0.077 |
          | RSFT CED (r2b)   | 0.4493 | 0.8128 | 0.6609 | +0.015  | -0.051 |
    figures_description:
      - "Bar chart: evi_f1 和 EDCR 的三方对比 (SFT / flat-NLI RSFT / CED RSFT)，error bar 覆盖多 config"
      - "Scatter plot: CED margin vs flat-NLI score per candidate，展示两种 scoring 在 distractor-heavy 候选上的分歧"
    analysis: >
      CED 的优势集中在 EDCR 维度（-5.8pp gap），而非仅 evi_f1（-2.6pp gap），这验证了 CED 的设计意图：
      它不是泛化地提升 evidence 召回，而是精确打击 entity-sharing distractor。flat-NLI RSFT 的 EDCR
      改善有限（0.711→0.693，仅 -1.9pp）说明朴素 NLI 对 distractor 基本无鉴别力。这为 Claim 2
      提供了强实验支撑，也回应 RC6（CED 确实在正确方向上比 flat-NLI 有显著优势）。

  - name: "Test set evaluation (best config)"
    plan_id: "plan_002"
    description: >
      用 RSFT best config (s44 或 r2b) 在 DocRED official test set 上评估。
      CodaLab 提交获取官方 rel_f1/ign_f1，本地计算 evi_f1 和 EDCR。
      同时提交 SFT baseline 和 flat-NLI RSFT 作为对比。
    expected_results:
      rsft_ced_test_rel_f1: 0.454
      rsft_ced_test_ign_f1: 0.452
      rsft_ced_test_evi_f1: 0.802
      rsft_ced_test_edcr: 0.548
      rsft_ced_test_evi_precision: 0.812
      rsft_ced_test_evi_recall: 0.793
      sft_test_rel_f1: 0.397
      sft_test_evi_f1: 0.789
      sft_test_edcr: 0.705
      flatnli_rsft_test_rel_f1: 0.429
      flatnli_rsft_test_evi_f1: 0.785
      flatnli_rsft_test_edcr: 0.686
      dev_to_test_rel_f1_decay: 0.012
      dev_to_test_evi_f1_decay: 0.007
    result_rationale: >
      Dev→test 泛化良好，衰减控制在 <2pp。rel_f1 从 dev 0.4655 降至 test 0.454（-1.2pp），
      evi_f1 从 0.8087 降至 0.802（-0.7pp）。衰减小的原因：(1) DocRED test set 与 dev set
      来自同一标注管道（Wikipedia distant supervision + human annotation），分布一致性高；
      (2) RSFT 不修改模型 policy gradient，仅通过数据筛选改进，对分布偏移鲁棒性天然好于 online RL；
      (3) SFT baseline 本身 dev→test 一般衰减 <1pp（DocRED 惯例）。EDCR 从 dev 0.635 显著降至
      test 0.548（-8.7pp），这是因为 test set entity 分布略有差异导致 distractor 比例天然较低，
      加上 RSFT+CED 在 unseen documents 上的 generalization。test evi_f1=0.802 远超
      DREEAM 57.34（+22.9pp），但需注意评估协议差异（生成式 vs attention-based），论文需明确讨论。
    tables:
      - name: "Table: Test set results (DocRED official)"
        content: |
          | Method           | rel_f1 | ign_f1 | evi_f1 | EDCR  |
          |------------------|--------|--------|--------|-------|
          | DREEAM†          | 0.633  |  —     | 0.5734 |  —    |
          | SAIS†            | 0.623  |  —     | 0.5567 |  —    |
          | SFT baseline     | 0.397  | 0.395  | 0.789  | 0.705 |
          | RSFT flat-NLI    | 0.429  | 0.427  | 0.785  | 0.686 |
          | RSFT CED (ours)  | 0.454  | 0.452  | 0.802  | 0.548 |
          † encoder-based, not directly comparable on evi_f1 protocol
    figures_description:
      - "Dev vs test scatter plot: 每个 config 一个点，x=dev metric, y=test metric，展示 generalization gap"
    analysis: >
      Test set 数字稳健，核心假设 1 成立。rel_f1=0.454 虽低于 encoder SOTA (DREEAM 0.633)，
      但这是 LLM generative 方法的已知 trade-off——模型同时生成 relation + evidence 而非仅做分类。
      关键是 evi_f1=0.802 大幅超越所有 encoder baselines（在可比评估协议下），且 EDCR=0.548
      说明超过半数引用是精确的非 distractor evidence。这支撑 Claim 1 的完整叙事。

  - name: "EDCR cross-method diagnostic table"
    plan_id: "plan_003"
    description: >
      在所有 evidence-producing 方法上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。
      包括 SFT、RSFT-CED 各 config、RSFT-flatNLI、CED-reranker。
    expected_results:
      sft_edcr: 0.7118
      rsft_ced_r1_edcr: 0.6565
      rsft_ced_s44_edcr: 0.6350
      rsft_ced_r2a_edcr: 0.6641
      rsft_ced_r2b_edcr: 0.6609
      rsft_flatnli_edcr: 0.693
      ced_reranker_edcr: 0.498
      grpo_ced_kl001_ckpt90_edcr: 0.8584
      sft_evi_f1: 0.7979
      rsft_ced_best_evi_f1: 0.8187
      ced_reranker_evi_f1: 0.805
      grpo_ced_evi_f1: 0.5666
      edcr_evi_f1_correlation: -0.42
    result_rationale: >
      EDCR 的诊断价值在于揭示 evi_f1 的盲区。关键 case：GRPO best checkpoint (ckpt-90) 的
      evi_f1=0.567 看似合理，但 EDCR=0.858 暴露了其 evidence 几乎全是 distractor（因为 GRPO
      catastrophic forgetting 后模型倾向于引用 entity-mentioning 句子而非真正的 evidence）。
      CED-reranker EDCR=0.498 最低，因为它直接用 CED margin 在推理时选择 evidence，完全绕过
      训练信号中的噪声。EDCR 与 evi_f1 的 correlation 仅 -0.42（非强负相关），证明两个指标
      捕捉不同维度：evi_f1 衡量 coverage，EDCR 衡量 precision（是否引用了错误的 plausible 句子）。
      在 best 档位下这个 diagnostic table 是 Claim 4 的核心展示。
    tables:
      - name: "Table: EDCR diagnostic across all methods"
        content: |
          | Method               | rel_f1 | evi_f1 | EDCR   | Evidence 模式    |
          |----------------------|--------|--------|--------|-----------------|
          | SFT                  | 0.4057 | 0.7979 | 0.7118 | 高 distractor    |
          | RSFT flat-NLI        | 0.438  | 0.793  | 0.693  | 略改善           |
          | RSFT CED (best)      | 0.4655 | 0.8087 | 0.635  | 明显改善         |
          | CED reranker         | 0.398  | 0.805  | 0.498  | 最精确           |
          | GRPO CED (ckpt-90)   | 0.211  | 0.567  | 0.858  | 灾难性 distractor |
    figures_description:
      - "evi_f1 vs EDCR scatter plot: 每个方法一个点，展示两个指标的正交性"
      - "Stacked bar chart: 每个方法的 evidence 组成 (gold / distractor / other)"
    analysis: >
      EDCR 成功区分了 evi_f1 无法区分的场景。特别是 CED-reranker 的 EDCR=0.498 与 RSFT-CED
      的 0.635 形成对比：前者虽然 rel_f1 略低（因为没有 RSFT 训练提升），但 evidence 精度最高。
      这为论文提供了一个清晰的叙事：EDCR 是必要的补充评估维度，仅看 evi_f1 会高估 evidence 质量。

  - name: "DREEAM baseline reproduction"
    plan_id: "plan_004"
    description: >
      在 DocRED dev set 上复现 DREEAM (RoBERTa-large) 的 Evi-F1，确认论文报告的
      test 57.34 对应的 dev set 数字可复现，消除 RC3 评测可比性疑虑。
    expected_results:
      dreeam_dev_evi_f1: 0.5698
      dreeam_dev_rel_f1: 0.6267
      dreeam_dev_evi_precision: 0.581
      dreeam_dev_evi_recall: 0.559
      reproduction_gap_vs_paper: 0.003
      evaluation_protocol_match: true
    result_rationale: >
      DREEAM 原始代码和 checkpoint 公开可用（GitHub），RoBERTa-large 在 DocRED 上的训练稳定性高，
      复现数字与论文报告差距应 <0.5pp。dev evi_f1 ~0.57 对应 test 57.34（dev 和 test 差异
      通常 <1pp）。在 best 档位下，复现成功消除 RC3 疑虑：(1) 确认我们的 evi_f1 计算管道与
      DREEAM 一致（都使用句子级 F1）；(2) 确认 DREEAM 的 attention-based evidence 和我们的
      generative evidence 在同一评估框架下可比。注意 DREEAM 的 evi_f1 ~0.57 远低于我们的
      RSFT+CED ~0.81，但这并非 apple-to-apple：DREEAM 的 evidence 是 attention threshold
      based，recall 受阈值限制；我们的 evidence 是 generative，recall 天然更高。论文需要
      明确讨论这个差异，但在 best 档位下复现本身是成功的。
    tables:
      - name: "Table: DREEAM reproduction vs paper"
        content: |
          | Setting    | Paper    | Reproduced | Gap    |
          |------------|----------|------------|--------|
          | dev rel_f1 | ~0.629   | 0.6267     | -0.002 |
          | dev evi_f1 | ~0.572   | 0.5698     | -0.002 |
          | test evi_f1| 0.5734   | (submit)   |  —     |
    figures_description: []
    analysis: >
      复现成功，gap <0.5pp，确认评估管道一致性。这让 FREIGE 与 DREEAM 的 evi_f1 对比有坚实基础，
      虽然需要在论文中讨论 generative vs attention-based evidence 的协议差异。

  - name: "CED-as-reranker (inference-time)"
    plan_id: "plan_005"
    description: >
      推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。
      验证 CED 在推理时的 evidence 改进价值。
    expected_results:
      reranker_rel_f1: 0.398
      reranker_evi_f1: 0.805
      reranker_edcr: 0.498
      reranker_evi_precision: 0.825
      reranker_evi_recall: 0.786
      sft_baseline_rel_f1: 0.4057
      sft_baseline_evi_f1: 0.7979
      sft_baseline_edcr: 0.7118
      edcr_improvement_over_sft: -0.214
      evi_f1_improvement_over_sft: 0.007
      rel_f1_change: -0.008
      inference_overhead_factor: 8.0
    result_rationale: >
      CED-as-reranker 的核心机制：从 SFT 的 8 个独立采样中，按 CED margin 选择 evidence 最干净的候选。
      rel_f1 略降（-0.8pp）是因为 CED 选择的是 evidence 最优而非 relation 最优的候选，在 8 candidates
      中两者不完全一致。evi_f1 提升有限（+0.7pp），因为 SFT 候选的 evidence recall 已经较高。
      但 EDCR 从 0.712 骤降至 0.498——这是 best 档位的关键数字：CED reranker 直接在推理时用
      对比信号过滤 distractor-heavy 候选，效果最为直接。EDCR < 0.55 的核心假设成立。
      这提供了一条无需训练的 evidence 改进路径，是论文的 bonus contribution。
      8x 推理开销是 trade-off，但对于需要高 evidence 精度的场景（生物医学审计、法律文档）可接受。
    tables:
      - name: "Table: CED reranker vs baselines"
        content: |
          | Method           | rel_f1 | evi_f1 | EDCR  | Extra training |
          |------------------|--------|--------|-------|----------------|
          | SFT baseline     | 0.4057 | 0.7979 | 0.712 | —              |
          | CED reranker     | 0.398  | 0.805  | 0.498 | None           |
          | RSFT CED (s44)   | 0.4655 | 0.8087 | 0.635 | ~2h LoRA       |
    figures_description:
      - "Histogram: 8 candidates per doc 的 CED margin 分布，展示 reranker 的选择空间"
      - "Case study: 1-2 个 document 的 reranker 前后 evidence 对比，展示 distractor 被过滤"
    analysis: >
      CED reranker 在 EDCR 上取得所有方法中最好的结果（0.498），验证了 CED 信号在推理时的直接价值。
      与 RSFT+CED 互补：RSFT+CED 在 rel_f1 和 evi_f1 上更优（因为有训练提升），CED reranker
      在 EDCR 上更优（因为是直接优化 evidence 选择）。论文可以推荐：如果计算资源允许，RSFT+CED 训练
      后再在推理时用 CED reranker 二次重排，可能同时获得两者优势。

  - name: "Model size ablation (1.7B / 8B)"
    plan_id: "plan_006"
    description: >
      Qwen3-1.7B 和 Qwen3-8B 上复现 RSFT+CED pipeline，验证方法对模型规模的泛化性。
    expected_results:
      qwen3_1_7b_sft_rel_f1: 0.342
      qwen3_1_7b_sft_evi_f1: 0.755
      qwen3_1_7b_rsft_ced_rel_f1: 0.378
      qwen3_1_7b_rsft_ced_evi_f1: 0.776
      qwen3_1_7b_rsft_ced_edcr: 0.682
      qwen3_1_7b_rsft_delta_rel_f1: 0.036
      qwen3_1_7b_rsft_delta_evi_f1: 0.021
      qwen3_8b_sft_rel_f1: 0.448
      qwen3_8b_sft_evi_f1: 0.818
      qwen3_8b_rsft_ced_rel_f1: 0.492
      qwen3_8b_rsft_ced_evi_f1: 0.835
      qwen3_8b_rsft_ced_edcr: 0.588
      qwen3_8b_rsft_delta_rel_f1: 0.044
      qwen3_8b_rsft_delta_evi_f1: 0.017
    result_rationale: >
      在 best 档位下，RSFT+CED 方法在三个模型规模上一致有效。(1) 1.7B 模型：基础能力较弱（SFT rel_f1
      仅 0.342），但 RSFT+CED 仍带来 +3.6pp rel_f1 和 +2.1pp evi_f1 的提升，证明 CED 信号
      对小模型也有效。EDCR 改善较小（0.72→0.682）因为小模型本身 evidence 质量更差，CED 过滤效果受限。
      (2) 8B 模型：SFT baseline 已较强（0.448），RSFT+CED 进一步提升至 0.492，且 EDCR=0.588
      优于 4B 的 0.635——更大模型能更好利用 CED 筛选的高质量训练数据。(3) RSFT 的 relative improvement
      在三个规模上保持在 +3.6~6.0pp rel_f1 范围，说明方法泛化性好。8B 的 evi_f1=0.835 是全局最高，
      展示了 scaling 潜力。
    tables:
      - name: "Table: Model size ablation"
        content: |
          | Model     | SFT rel_f1 | RSFT+CED rel_f1 | Δrel_f1 | SFT evi_f1 | RSFT+CED evi_f1 | EDCR  |
          |-----------|------------|------------------|---------|------------|-----------------|-------|
          | Qwen3-1.7B| 0.342      | 0.378            | +3.6pp  | 0.755      | 0.776           | 0.682 |
          | Qwen3-4B  | 0.406      | 0.466            | +6.0pp  | 0.798      | 0.819           | 0.635 |
          | Qwen3-8B  | 0.448      | 0.492            | +4.4pp  | 0.818      | 0.835           | 0.588 |
    figures_description:
      - "Line plot: model size (x) vs rel_f1/evi_f1/EDCR (y), SFT 和 RSFT+CED 两条线展示 consistent gap"
    analysis: >
      三个规模上 RSFT+CED 均有效且方向一致，完全回应 RC4 单模型泛化性质疑。8B 结果暗示更大模型
      可能进一步受益——这为 future work 提供自然延伸（14B/32B）。1.7B 的较小改善是合理的：
      小模型的生成候选多样性和质量本身有限，CED 筛选的上界被候选质量约束。

  - name: "Re-DocRED extension"
    plan_id: "plan_007"
    description: >
      在 Re-DocRED（修正 false negative 标注的版本）上评估 RSFT+CED，
      验证在更干净标注下的表现。
    expected_results:
      redocred_sft_rel_f1: 0.472
      redocred_sft_evi_f1: 0.812
      redocred_sft_edcr: 0.648
      redocred_rsft_ced_rel_f1: 0.518
      redocred_rsft_ced_evi_f1: 0.831
      redocred_rsft_ced_edcr: 0.578
      redocred_delta_rel_f1: 0.046
      redocred_delta_evi_f1: 0.019
      redocred_vs_docred_sft_rel_f1_gain: 0.067
      redocred_vs_docred_rsft_rel_f1_gain: 0.053
    result_rationale: >
      Re-DocRED 修正了 DocRED 中大量 false negative（遗漏的关系标注），因此所有方法的 rel_f1
      都显著上升（SFT +6.7pp, RSFT+CED +5.3pp），因为原来被判为 FP 的正确预测现在被标为 TP。
      RSFT+CED 的改善幅度在 Re-DocRED 上保持（+4.6pp rel_f1, +1.9pp evi_f1），甚至可能更稳定：
      Re-DocRED 的 evidence 标注也更干净，减少了 RC2（gold evidence 不完整导致 false distractor）
      的干扰。EDCR=0.578 低于 DocRED 上的 0.635，因为更完整的标注意味着更少的 genuine evidence
      被误标为 distractor。这进一步验证了 CED 的鲁棒性：即使在标注更干净的数据上，CED 仍有价值。
    tables:
      - name: "Table: DocRED vs Re-DocRED"
        content: |
          | Dataset   | Method     | rel_f1 | evi_f1 | EDCR  |
          |-----------|------------|--------|--------|-------|
          | DocRED    | SFT        | 0.406  | 0.798  | 0.712 |
          | DocRED    | RSFT+CED   | 0.466  | 0.819  | 0.635 |
          | Re-DocRED | SFT        | 0.472  | 0.812  | 0.648 |
          | Re-DocRED | RSFT+CED   | 0.518  | 0.831  | 0.578 |
    figures_description:
      - "Grouped bar chart: DocRED vs Re-DocRED 在各指标上的对比"
    analysis: >
      Re-DocRED 结果回应 RC4 单数据集质疑。rel_f1 提升至 0.518 说明 LLM 生成方法在更干净标注下
      competitive 性增强。EDCR 在两个数据集上一致降低，证明 CED 的 distractor 过滤能力非 artifact。

  - name: "top_k ablation (k=1 vs k=3)"
    plan_id: "plan_008"
    description: >
      CED scoring 筛选 top_k=3（~8000 samples）vs top_k=1（~2718 samples），
      验证 CED 过滤严格度对 RSFT 质量的影响。
    expected_results:
      topk1_samples: 2718
      topk1_rel_f1: 0.4655
      topk1_evi_f1: 0.8087
      topk1_edcr: 0.635
      topk3_samples: ~8100
      topk3_rel_f1: 0.458
      topk3_evi_f1: 0.804
      topk3_edcr: 0.652
      topk3_mean_ced_score: 0.542
      topk1_mean_ced_score: 0.668
    result_rationale: >
      在 best 档位下，top_k=1 略优于 top_k=3，但差异不大。top_k=1 选最严格的候选（mean CED=0.668），
      训练数据量较少（2718）但质量最高；top_k=3 数据量 3 倍（~8100）但包含 CED 分较低的候选
      （mean CED=0.542），引入更多噪声。rel_f1 差异 ~0.8pp 和 evi_f1 差异 ~0.5pp 说明
      更多数据的 coverage 优势被质量下降部分抵消。EDCR top_k=3 略高（0.652 vs 0.635）因为
      top_k=2,3 的候选更可能包含 distractor evidence。best 档位的结论是 top_k=1 is optimal，
      但 top_k=3 仍显著优于 SFT baseline，说明 CED 的顶部候选质量都可接受。
      这为论文提供了一个实用指南：如果计算资源有限（少生成候选），top_k=1 是安全选择。
    tables:
      - name: "Table: top_k ablation"
        content: |
          | top_k | Samples | mean CED | rel_f1 | evi_f1 | EDCR  |
          |-------|---------|----------|--------|--------|-------|
          | 1     | 2718    | 0.668    | 0.466  | 0.809  | 0.635 |
          | 3     | ~8100   | 0.542    | 0.458  | 0.804  | 0.652 |
    figures_description:
      - "Line plot: top_k (1,2,3) vs metrics，展示 quality-quantity trade-off"
    analysis: >
      top_k=1 最优但非压倒性优势，说明 CED 的 ranking quality 在 top-3 内都保持合理水平。
      这增强了方法的实用性叙事。

  - name: "GRPO forgetting dynamics visualization"
    plan_id: "plan_009"
    description: >
      整理全部 GRPO checkpoint 的 rel_f1/evi_f1/EDCR/reward 轨迹，
      绘制 forgetting dynamics 可视化，支撑 Claim 3。
    expected_results:
      grpo_ced_lr5e6_trajectory:
        ckpt10_rel_f1: 0.003
        ckpt10_evi_f1: 0.720
        ckpt10_reward: 0.45
        ckpt20_rel_f1: 0.008
        ckpt20_evi_f1: 0.628
        ckpt40_rel_f1: 0.007
        ckpt40_evi_f1: 0.758
        ckpt60_rel_f1: 0.009
        ckpt60_evi_f1: 0.810
        ckpt80_rel_f1: 0.012
        ckpt80_evi_f1: 0.828
        ckpt100_rel_f1: 0.014
        ckpt100_evi_f1: 0.850
        ckpt100_reward: 1.195
        ckpt100_edcr: 0.988
      grpo_kl001_trajectory:
        ckpt10_rel_f1: 0.003
        ckpt50_rel_f1: 0.156
        ckpt90_rel_f1: 0.211
        ckpt90_evi_f1: 0.567
        ckpt90_edcr: 0.858
      grpo_flatnli_collapse_step: 25
      grpo_extract_collapse_step: 30
      key_observation: "reward ↑ monotonically while rel_f1 stays near 0 — classic reward overoptimization"
    result_rationale: >
      所有 GRPO 数据已在 MVP 阶段收集完毕，此实验仅做整理和可视化。在 best 档位下，可视化清晰展示
      catastrophic forgetting 的 signature pattern：(1) lr=5e-6 trajectory 展示 reward 持续上升
      （0.45→1.195）而 rel_f1 始终 <0.02，evi_f1 持续上升至 0.850——模型学会了生成 NLI-friendly
      的 evidence 但完全忘记了 relation extraction；(2) KL=0.01 configuration 的 rel_f1 部分恢复
      至 0.211 但仍远低于 SFT 的 0.406，且 EDCR=0.858 说明 evidence 几乎全是 distractor；
      (3) flat-NLI 和 extract-only reward 在 step 25-30 即 collapse（frac_zero_std→0.9），
      说明 CED 是三种 reward 中唯一能维持训练稳定性的，但仍无法阻止 forgetting。
      这组可视化是 Claim 3 的核心证据：在线 RL 在结构化 IE 上 fundamentally broken。
    tables:
      - name: "Table: GRPO full trajectory (lr=5e-6, CED reward)"
        content: |
          | Checkpoint | rel_f1 | evi_f1 | EDCR  | reward |
          |------------|--------|--------|-------|--------|
          | SFT (init) | 0.406  | 0.798  | 0.712 | —      |
          | step-10    | 0.003  | 0.720  | 0.998 | 0.45   |
          | step-20    | 0.008  | 0.628  | 0.994 | 0.62   |
          | step-40    | 0.007  | 0.758  | 0.994 | 0.78   |
          | step-60    | 0.009  | 0.810  | 0.993 | 0.91   |
          | step-80    | 0.012  | 0.828  | 0.993 | 1.05   |
          | step-100   | 0.014  | 0.850  | 0.988 | 1.195  |
    figures_description:
      - "Dual-axis plot: left y-axis = rel_f1 (stays near 0), right y-axis = reward + evi_f1 (both ↑). X = training steps. 清晰展示 reward overoptimization"
      - "3-panel comparison: CED / flat-NLI / extract-only reward 的 f1_reward trajectory，标注 collapse point"
      - "Phase diagram: rel_f1 vs evi_f1 scatter colored by training step，展示 SFT→GRPO 的 trajectory drift"
    analysis: >
      可视化的叙事力很强：reviewer 一眼就能看到 reward ↑ + rel_f1 → 0 的 divergence pattern。
      这是 Gao et al. 2023 reward overoptimization 在 structured IE 中的首次实证展示。
      CED reward 的 evi_f1↑ 证明 CED 作为信号本身有效（它确实驱动了 evidence 学习），
      但在线 RL 的 policy gradient 更新摧毁了抽取能力。这直接引向 RSFT 的动机：
      用 CED 的信号质量 + RSFT 的离线安全性。Claim 3 作为 cautionary tale 有完整的故事线。

  - name: "NLI model ablation (DeBERTa-base vs large)"
    plan_id: "plan_010"
    description: >
      DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer 的对比，
      验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。
    expected_results:
      deberta_base_ced_mean_margin: 0.480
      deberta_base_ced_discrimination_acc: 0.815
      deberta_base_rsft_rel_f1: 0.4655
      deberta_base_rsft_evi_f1: 0.8087
      deberta_base_rsft_edcr: 0.635
      deberta_large_ced_mean_margin: 0.523
      deberta_large_ced_discrimination_acc: 0.849
      deberta_large_rsft_rel_f1: 0.471
      deberta_large_rsft_evi_f1: 0.815
      deberta_large_rsft_edcr: 0.618
      pearson_r_base_lexical: 0.34
      pearson_r_large_lexical: 0.28
    result_rationale: >
      在 best 档位下，DeBERTa-large CED 略优于 base 但差距有限（discrimination acc +3.4pp，
      EDCR -1.7pp）。原因：(1) CED 的对比 margin 设计本身减轻了 NLI 模型能力的影响——即使 base
      模型有 lexical overlap bias，对比操作（p_pos - p_neg）中 bias 部分抵消（两侧都受 bias 影响）；
      (2) large 模型的 Pearson r 与 lexical overlap 更低（0.28 vs 0.34），说明更强 NLI 模型
      确实减少了表面特征依赖，但 base 已经 sufficient for RSFT 筛选用途。
      这回应 RC1：CED 打分质量对 NLI 模型规模不敏感，DeBERTa-base 已足够可靠。
      large 模型提供 marginal improvement 但计算成本翻倍（NLI 推理是 scoring 瓶颈），
      性价比不如 base。
    tables:
      - name: "Table: NLI model ablation for CED"
        content: |
          | NLI Model         | CED margin | Disc. acc | Pearson r | RSFT evi_f1 | RSFT EDCR |
          |-------------------|------------|-----------|-----------|-------------|-----------|
          | DeBERTa-v3-base   | 0.480      | 0.815     | 0.34      | 0.809       | 0.635     |
          | DeBERTa-v3-large  | 0.523      | 0.849     | 0.28      | 0.815       | 0.618     |
    figures_description:
      - "Histogram: base vs large 的 CED margin 分布对比"
    analysis: >
      DeBERTa-base 已足够，large 仅 marginal improvement。这是论文的实用结论：
      CED 的鲁棒性来自对比设计而非 NLI 模型强度，降低了方法的部署门槛。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca16e4a0-b277-42c6-92db-445d9b8f9aa4",
  "isSidechain": false,
  "requestId": "req_011Cb4KedHwToU93DQmnZNye",
  "type": "assistant",
  "uuid": "7321f67d-4528-4d99-bbbe-c99314700b68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "ffd23ddb-103f-41e4-8b99-29b89164a3ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cg9A7sMxEPU7trgVKyByqo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18507,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12949,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18507,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12949,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18507
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有核心假设成立：CED 对比性信号显著优于 flat-NLI，test set 数字稳健，EDCR 大幅下降 核心假设：['Dev→test 泛化良好，rel_f1 和 evi_f1 衰减 <2pp', 'CED-scored RSFT 在 evi_f1 和 EDCR 上显著优于 flat-NLI-scor…",
  "leafUuid": "7321f67d-4528-4d99-bbbe-c99314700b68",
  "sessionId": "ffd23ddb-103f-41e4-8b99-29b89164a3ab"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "CED-scored RSFT for evidence grounding in LLM DocRE",
  "sessionId": "ffd23ddb-103f-41e4-8b99-29b89164a3ab"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有核心假设成立：CED 对比性信号显著优于 flat-NLI，test set 数字稳健，EDCR 大幅下降 核心假设：['Dev→test 泛化良好，rel_f1 和 evi_f1 衰减 <2pp', 'CED-scored RSFT 在 evi_f1 和 EDCR 上显著优于 flat-NLI-scor…",
  "leafUuid": "7321f67d-4528-4d99-bbbe-c99314700b68",
  "sessionId": "ffd23ddb-103f-41e4-8b99-29b89164a3ab"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "CED-scored RSFT for evidence grounding in LLM DocRE",
  "sessionId": "ffd23ddb-103f-41e4-8b99-29b89164a3ab"
}
```

---
