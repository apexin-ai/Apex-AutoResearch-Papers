# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：核心方法有效但 CED 优势不显著：RSFT 整体优于 SFT 但 CED vs flat-NLI p>0.05，GRPO G=8 仍崩，EDCR 

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-2/c88f356d-19e6-4318-9584-f84bcdbc9c1c.jsonl`
- **Structured JSON:** [`f57bd9b121f428725465.json`](../../sessions/f5/f57bd9b121f428725465.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T13:29:42.397Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T13:29:42.397Z",
  "sessionId": "c88f356d-19e6-4318-9584-f84bcdbc9c1c",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：核心方法有效但 CED 优势不显著：RSFT 整体优于 SFT 但 CED vs flat-NLI p>0.05，GRPO G=8 仍崩，EDCR 人工验证中等\n核心假设：['CED vs flat-NLI RSFT 差异方向正确但不显著（Δevi_f1 0.3-1.2pp, p=0.05-0.20），CED 的对比性 margin 优势被 NLI 噪声稀释', 'Test set rel_f1 Δ = +2.0-3.5pp over SFT（dev→test 退化 2-3pp），仍显著但幅度收窄', 'GRPO G=8 仍崩（rel_f1 < 0.10），Claim 3 成立但需承认 full-rank 未测', 'DPO 结果不够理想：要么也部分崩（rel_f1 0.10-0.25）要么接近 RSFT（rel_f1 0.40+），光谱不够清晰', 'EDCR 与人工判断 r=0.35-0.55，有信号但不够强']\n关键指标范围：{'test_rel_f1_delta_over_sft': [2.0, 3.5], 'ced_vs_flatnli_evi_f1_delta': [0.3, 1.5], 'ced_vs_flatnli_edcr_delta': [-5.0, -1.0], 'ced_vs_flatnli_p_value': [0.05, 0.2], 'grpo_g8_best_rel_f1': [0.0, 0.1], 'dpo_rel_f1': [0.1, 0.42], 'edcr_human_pearson_r': [0.35, 0.55], 'rsft_best_test_rel_f1': [0.41, 0.45], 'rsft_test_evi_f1_joint': [0.28, 0.36]}\n叙事方向：触发 CED contingency plan：CED 从核心贡献降级为\"可选 scoring function\"。 论文重心转移到三条独立但互补的贡献： (1) Claim 1 升格为主贡献——首个 evidence-generating LLM for DocRE，RSFT（无论用哪种 scorer）均显著优于 SFT； (2) Claim 3 保持——GRPO+QLoRA decoupling phenomenon 作为 analysis contribution，但 DPO 部分需根据实际结果灵活处理； (3) Claim 4 调整——EDCR 作为 diagnostic tool 而非 validated metric，报告人工相关性但坦诚局限。 CED vs flat-NLI 作为 ablation 诚实报告\"方向正确但未达显著\"，不作为 selling point。 叙事从 \"CED 是关键创新\" 转为 \"RSFT pipeline 是关键创新 + GRPO failure analysis 是独立贡献\"。 需要补充实验加强 Claim 1（如 model size ablation 或 Re-DocRED）弥补 CED claim 的弱化。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: faith-evidence-ie\nvenue: EMNLP 2026 Main\nfocus: D042 修正后 re-dream。关键变化: (1) Claim 3 缩窄为 GRPO+QLoRA 而非 online RL; (2) 新增 GRPO G=8 实验(plan_011); (3) 新增 DPO baseline(plan_012); (4) CED contingency plan(如 p>0.05 则降级); (5) Evi-F1 改为 DREEAM 对齐协议(joint); (6) 新增 EDCR 人工验证(plan_013)。请关注这些修改是否有效提升了论文质量。\n\n## paper_framing.md\n\n# Paper Framing — FREIGE\n\n> **状态**: POST-MVP (MVP-1 + MVP-2 均 PASS，进入 Research 阶段)\n> **最后更新**: 2026-05-15\n\n## Target Venue\n\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\n- Stretch: ARR May 25 (10 days, 极紧，仅在实验全部顺利时考虑)\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\n\n## Core Insight\n\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。朴素 NLI faithfulness reward 可被 entity-mentioning distractor 句子游戏——共享实体但不支持具体关系的句子仍获正面蕴含分数。\n\n**CED (Contrastive Evidence Discrimination)** 通过文档内 hard negative 对比，将 evidence 质量评估从\"是否蕴含\"升级为\"是否比最佳干扰句更蕴含\"——本质上是 evidence grounding 场景下的 **anti-reward-overoptimization mechanism**（连接 Gao et al. 2023 reward overoptimization 理论）。\n\n**MVP 关键发现**: CED 作为在线 RL (GRPO) reward 导致 catastrophic forgetting（3 种 reward type × 多个 lr 全线失败），但作为离线 RL (RSFT) 的候选筛选信号极其有效——4 组超参配置均稳定超过 SFT baseline。**方法论结论**: 对结构化 IE 任务，CED 应作为离线质量信号而非在线训练奖励。\n\n## Story Arc\n\n1. **Problem**: LLM DocRE 无证据 → 部署障碍（human-in-the-loop KB population、生物医学审计、RAG 溯源）\n2. **Why naive reward fails**: flat-NLI 被 entity-sharing distractors 欺骗（SFT EDCR=71.2%，大量引用干扰句）\n3. **Why online RL fails**: GRPO+CED/flat-NLI/extract-only 全部 catastrophic forgetting（reward ↑ + rel_f1 ↓ 至 <0.02）\n4. **Solution**: CED 作为离线质量信号 + RSFT（rejection sampling fine-tuning）：SFT 模型生成 N 候选 → CED 打分筛选 → 微调，规避在线 RL 的遗忘风险\n5. **Theoretical grounding**: 连接 LongRLVR (ICLR 2026) evidence grounding 梯度消失分析 + \"RSFT=PPO\" (ICML 2025) 等价性理论\n6. **Result**: 首个 LLM-based DocRE 方法同时生成抽取和可验证证据\n\n## Core Claims\n\n### Claim 1 (Main): CED-scored RSFT 使 LLM 同时生成抽取和忠实证据\n- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法\n- RSFT+CED: rel_f1 +3.9~6.0pp over SFT, evi_f1 +1.1~2.1pp, EDCR -4.8~7.7pp\n- **MVP-2 已验证**: 4/4 configs PASS\n- **Research 需要**: test set 评估，DREEAM/SAIS Evi-F1 直接对比\n\n### Claim 2 (Ablation): CED scoring 优于 flat-NLI scoring 用于 RSFT\n- CED-filtered RSFT vs flat-NLI-filtered RSFT 的 evi_f1 和 EDCR 差异\n- CED 的对比性 margin 过滤掉 distractor-heavy 候选\n- **Research 需要**: flat-NLI scored RSFT ablation（核心实验）\n- **⚠️ Dream 风险**: 三档 Dream 审稿均指出 CED vs flat-NLI 可能不显著（p>0.05）。**Contingency**: 如 plan_001 结果 p>0.05，降级 CED 为\"一种可选 scoring function\"而非核心贡献，论文主贡献重心转移到 Claim 1（首个 evidence-generating LLM for DocRE）和 Claim 3（decoupling phenomenon）\n\n### Claim 3 (Analysis): GRPO+QLoRA 在文档级 IE 上 catastrophic forgetting 且呈现 evidence-extraction decoupling\n- **范围限定**: 仅对 GRPO+QLoRA（非泛化到所有 online RL）——Dream 三档一致指出 overclaim 风险\n- GRPO+QLoRA 在 3 种 reward type × 多个 lr 下全线失败\n- **核心发现 (decoupling)**: evi_f1 在 GRPO 下提升至 0.850（>SFT 0.798）但 rel_f1 崩至 <0.02——RL 差异化优化了 evidence 但摧毁了 extraction\n- RSFT 规避此问题：不修改 policy gradient，只筛选训练数据\n- **MVP 已有完整证据**: D031/D033 GRPO 判死，D039 RSFT 成功\n- **⚠️ Dream 风险**: G=4 太小（标准 G=8-16），需测 G=8 排除 advantage estimation noise 的干扰；LoRA-only 是额外 confound\n\n### Claim 4 (Evaluation): EDCR 作为独立评估指标\n- EDCR = |entity-sharing non-gold cited sentences| / |total cited sentences|\n- Evi-F1 盲区：不惩罚 plausible-looking distractor citations\n- SFT EDCR=71.2%, RSFT+CED EDCR=63.5~66.4%（方向正确但差距有限，需坦诚讨论）\n- **Research 需要**: cross-method diagnostic table, CED vs flat-NLI EDCR 对比\n\n## MVP Evidence Summary\n\n| Config | rel_f1 | Δ rel_f1 | evi_f1 | EDCR | 状态 |\n|--------|--------|----------|--------|------|------|\n| SFT baseline | 0.4057 | — | 0.7979 | 0.7118 | ✅ |\n| RSFT r1 (3ep, α=128, s42) | 0.4449 | +3.92pp | 0.8187 | 0.6565 | ✅ |\n| RSFT r1 (s44) | 0.4655 | +5.98pp | 0.8087 | 0.6350 | ✅ |\n| RSFT r2a (1ep, α=128) | 0.4494 | +4.37pp | 0.8108 | 0.6641 | ✅ |\n| RSFT r2b (1ep, α=32, lr=1e-5) | 0.4493 | +4.36pp | 0.8128 | 0.6609 | ✅ |\n| GRPO best (lr=5e-5, ckpt-90) | 0.2110 | -19.5pp | 0.5750 | — | ❌ |\n| GRPO best (lr=5e-6, ckpt-100) | 0.0138 | -39.2pp | 0.8500 | 0.9900 | ❌ |\n\n## Anticipated Reviewer Concerns\n\n### RC1: NLI reward 信号质量（高概率攻击）\n- **攻击**: \"DeBERTa-v3-base 的 NLI 判断有 lexical overlap bias，CED 训练信号有噪声\"\n- **已验证**: MVP-1 Pearson r=0.34（NLI vs lexical overlap），远低于 0.7，证明非捷径\n- **Research 补充**: DeBERTa-base vs DeBERTa-large 对比\n\n### RC2: Gold evidence 标注不完整导致 false distractor\n- **攻击**: \"被标为 distractor 的句子可能是 annotator 遗漏的有效证据\"\n- **应对**: CED margin 的 self-correcting property——如果 false distractor 真正蕴含关系，其 p_neg 高 → margin 小 → 惩罚弱\n- **Research 补充**: false-distractor 鲁棒性量化分析\n\n### RC3: 评测可比性\n- **攻击**: \"生成式 evidence 如何与 DREEAM 的 attention-based evidence 做 apple-to-apple 对比？\"\n- **应对**: 模型输出显式句子索引 [S_i]，直接映射句子级 Evi-F1；辅助指标用 RoBERTa-large-MNLI（非训练用 DeBERTa）避免 circular evaluation\n\n### RC4: 单数据集 + 单模型泛化性\n- **攻击**: \"只在 DocRED + Qwen3-4B 上验证\"\n- **Research**: Re-DocRED 扩展 + Qwen3-1.7B/8B model size ablation\n\n### RC5: GRPO 配置可能不充分（Dream 三档一致）\n- **攻击**: \"G=4 太小（标准 G=8-16），LoRA-only 是 confound，可能是 GRPO+QLoRA 的问题而非 GRPO 本身\"\n- **应对**: (1) 加 G=8 实验验证（plan_011）；(2) 论文范围限定为 \"GRPO+QLoRA\" 而非 \"online RL\"；(3) 完整轨迹数据仍有效（3 reward × 2 lr × 全 checkpoint）\n- **Research**: GRPO G=8 实验 + 论文标题/claim 措辞调整\n\n### RC6: EDCR 63-66% 仍然偏高，CED 对证据精确度提升有限\n- **攻击**: \"RSFT+CED 的 EDCR 只比 SFT 低 5-8pp，证据质量提升不够显著\"\n- **应对**: (1) CED 在 RSFT 中是间接作用（筛选训练数据），非直接 reward；(2) CED-as-reranker 可能更直接降低 EDCR；(3) 需要 flat-NLI RSFT 对比证明 CED 方向正确\n- **Research**: CED reranker PoC（运行中），top_k ablation\n\n### RC7: 方法过于简单\n- **应对**: 简洁是优点——RSFT 方法论已被证明理论等价于 PPO (ICML 2025)，CED 创新在于打分函数设计而非框架复杂度\n\n### RC8: 缺少中间方法 baseline（Dream 两档一致 [M][W]）\n- **攻击**: \"GRPO(online) vs RSFT(offline) 缺少 DPO/KTO 等中间方法，无法定位失败边界\"\n- **应对**: 加 DPO+CED experiment（plan_012），至少一个中间方法填补 online-offline 光谱\n\n### RC9: EDCR 需要人工验证（Dream 两档一致 [M][W]）\n- **攻击**: \"EDCR 未经人工标注验证，与 Evi-F1 的弱相关 r=-0.42 无法区分信号与噪声\"\n- **应对**: 100 样本人工标注研究（plan_013），验证 EDCR 与人类判断的相关性\n\n### RC10: Evi-F1 评测协议不一致（D041 已确认）\n- **攻击**: \"你们的 Evi-F1 (conditional) 与 DREEAM (joint) 不可比\"\n- **已修复**: 实现 DREEAM 对齐评测函数，论文报告两种 Evi-F1（joint 为主，conditional 为辅）\n\n## Key Baselines (8+)\n\n1. **SFT-only**: Qwen3-4B + LoRA SFT on DocRED gold — 无 RL\n2. **RSFT flat-NLI**: flat-NLI scored RSFT — 无 contrastive signal（核心 ablation）\n3. **RSFT CED (FREIGE)**: CED scored RSFT — 主方法\n4. **CED-as-reranker**: 推理时 CED 重排 SFT 候选（无训练）— 运行中\n5. **GRPO+CED**: 在线 RL with CED reward — negative baseline\n6. **DREEAM**: RoBERTa-large encoder — evidence SOTA (Evi-F1 57.34)\n7. **SAIS**: RoBERTa encoder — evidence baseline (Evi-F1 55.67)\n8. **DocKS-RAG**: GNN+RAG — extraction SOTA (F1 63.59, 无 evidence)\n9. **LMRC**: LLaMA3.1-8B — generative LLM SOTA (F1 60.69, 无 evidence)\n\n## Publishability Threshold\n\n- **必要条件**: RSFT 在 test set 上 Evi-F1_joint（DREEAM 协议）> SFT baseline AND rel_f1 显著 > SFT baseline（D041: Evi-F1 对比 DREEAM 需用对齐协议，暂冻结绝对阈值）\n- **充分条件**: 上述 + CED vs flat-NLI RSFT 差异显著 + GRPO decoupling 分析完整 + EDCR 人工验证\n- **CED contingency**: 如 CED vs flat-NLI p>0.05 → 论文重心转为\"首个 evidence-generating LLM for DocRE + GRPO decoupling phenomenon + EDCR metric\"，CED 降为可选组件\n- **Failure pivot**: RSFT 在 test set 上无显著改进 → 转为 analysis contribution（GRPO failure analysis paper）\n\n## Research Phase Priorities\n\n| Priority | 实验 | Claim/RC | 预估 GPU-hours | Dream 驱动 |\n|----------|------|---------|---------------|-----------|\n| P0 | CED vs flat-NLI RSFT ablation | C2 | ~4h | ⚠️ 三档一致风险 |\n| P0 | Test set evaluation (RSFT best config) | C1 | ~4h | |\n| P0 | Evi-F1 DREEAM 协议对齐 + 重评 | RC10 | ~1h (CPU) | D041 |\n| P0 | EDCR pipeline 验证 + cross-method table | C4 | ~2h | |\n| P0 | DREEAM/SAIS Evi-F1 baseline reproduction | C1 | ~8h | |\n| P0 | GRPO G=8 实验 | C3/RC5 | ~8h | ⚠️ 三档一致 |\n| P1 | CED-as-reranker (running) | C1 bonus | ~6h | |\n| P1 | DPO+CED experiment | RC8 | ~12h | Dream [M][W] |\n| P1 | EDCR 人工标注验证 (100 samples) | RC9/C4 | ~0h (人工) | Dream [M][W] |\n| P1 | Model size ablation (1.7B/8B) | RC4 | ~24h | |\n| P1 | Re-DocRED extension | RC4 | ~12h | |\n| P1 | top_k ablation (k=1 vs k=3) | RC6 | ~8h | |\n| P2 | GRPO forgetting 详细分析 + 可视化 | C3 | ~4h | |\n| P2 | DeBERTa-base vs large NLI 对比 | RC1 | ~4h | |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选\n    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py\n    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set\n    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_003\n  claim: 4\n  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing\n    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_004\n  claim: 1\n  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)\n    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_005\n  claim: 1\n  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: mvp2_ced_reranker_poc\n  status: RUNNING\n- id: plan_006\n  claim: 1\n  description: 'Model size ablation: Qwen3-1.7B 和 Qwen3-8B 上复现 RSFT+CED pipeline，验证方法对模型规模的泛化性。应对\n    RC4。'\n  priority: P1\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Re-DocRED extension: 在 Re-DocRED（修正 false negative 标注的版本）上评估，验证 RSFT+CED\n    在更干净标注下的表现。应对 RC4。'\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  registry_id: null\n  status: planned\n- id: plan_008\n  claim: 2\n  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格\n    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_011\n  claim: 3\n  description: 'GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward\n    + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要\n    gradient_accumulation 适配显存。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_012\n  claim: 3\n  description: 'DPO+CED experiment: Dream [M][W] 指出缺少 online-offline 中间方法 baseline。用\n    RSFT 候选数据构造 preference pairs (CED-preferred vs CED-rejected)，DPO 训练。验证 DPO 是否避免\n    GRPO 的 catastrophic forgetting。'\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_013\n  claim: 4\n  description: 'EDCR 人工标注验证: 100 个样本，人工判断每个 cited evidence sentence 是否真正支持对应 relation。计算\n    EDCR 与人工判断的相关性，验证 EDCR 作为自动指标的有效性。Dream [M][W] 一致要求。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_009\n  claim: 3\n  description: 'GRPO forgetting 详细分析: 整理全部 GRPO checkpoint 的 rel_f1/evi_f1/EDCR 轨迹，绘制\n    forgetting dynamics 可视化（reward vs task performance 曲线），支撑 Claim 3 的论述。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer\n    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_mvp1\n  claim: 1\n  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing\n    distractor 的能力验证'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: mvp1_ced_signal\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_margin: 0.48\n    discrimination_accuracy: 0.815\n    pearson_r_margin_jaccard: 0.34\n    pass: true\n- id: plan_mvp2_sft\n  claim: 1\n  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mvp2_sft_warmup\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.72\n    accuracy: 0.835\n- id: plan_mvp2_rsft\n  claim: 1\n  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部\n    PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087,\n    r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_mvp1\n  - plan_mvp2_sft\n  registry_id: mvp2_rsft_train_r1\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.0483\n    num_preds: 848\n    sft_baseline_rel_f1: 0.4057\n    failure_mode: relation_ontology_collapse_to_freetext\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n- id: plan_mvp2_grpo\n  claim: 3\n  description: 'GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1\n    max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic\n    forgetting。D031/D033 完整轨迹支撑 Claim 3'\n  priority: P0\n  gpu_budget_hours: 60\n  deps:\n  - plan_mvp2_sft\n  registry_id: mvp2_grpo_ced_lr5e6_r1\n  status: DONE\n  conclusion: killed\n\n\n## registry (completed experiments)\n\n- exp_id: mvp1_ced_signal\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_margin: 0.48\n    discrimination_accuracy: 0.815\n    pearson_r_margin_jaccard: 0.34\n    pass: true\n- exp_id: smoke_test_grpo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_sft_warmup\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.72\n    accuracy: 0.835\n- exp_id: precompute_nli_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_grpo_ced\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_extract\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_sft_eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_extract_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: mvp2_grpo_extract_r3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_sft_eval_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    ign_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    precision: 0.4043\n    recall: 0.407\n    evi_precision: 0.8035\n    evi_recall: 0.7924\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.626\n    n_parseable: 617\n    n_truncated: 367\n    n_predictions: 18815\n    inference_time_seconds: 6484.7\n- exp_id: mvp2_sft_eval_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    ign_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    precision: 0.4043\n    recall: 0.407\n    evi_precision: 0.8035\n    evi_recall: 0.7924\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.626\n    n_parseable: 617\n    n_truncated: 367\n    n_predictions: 18815\n- exp_id: mvp2_grpo_ced_kl001_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001_r3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001_r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_step: 100\n    train_runtime_s: 9069.88\n    reward_final: 1.195\n    f1_reward_final: 0.573\n    ced_reward_final: 0.328\n    format_reward_final: 0.293\n    frac_zero_std_final: 0.2\n    kl_final: 0.118\n    loss_final: -0.009\n    grad_norm_final: 0.14\n    entropy_final: 0.067\n    completion_length_mean_final: 520.8\n    best_reward_step: 90\n    best_reward: 1.37\n    best_f1_reward: 0.72\n    best_ced_reward: 0.353\n- exp_id: mvp2_grpo_extract_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_early\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    f1: 0.1563\n    ign_f1: 0.1563\n    evi_f1: 0.5643\n    edcr: 0.8858\n    precision: 0.2356\n    recall: 0.1169\n    evi_precision: 0.4864\n    evi_recall: 0.6721\n    format_ok_rate: 0.999\n    n_parseable: 984\n    n_truncated: 11\n    n_predictions: 9250\n    tp: 1421\n    pred_count: 6032\n    gold_count: 12151\n- exp_id: mvp2_grpo_flatnli_r6\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    steps_completed: 25\n    final_frac_zero_std: 0.9\n    final_f1_reward: 0\n    final_flat_nli_reward: 0\n    final_format_reward: 0.293\n    collapse_step: 25\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.00296\n    rel_precision: 0.00314\n    rel_recall: 0.0028\n    evi_f1: 0.72\n    evi_precision: 0.6429\n    evi_recall: 0.8182\n    edcr: 0.9983\n    n_parseable: 984\n    n_truncated: 24\n    n_predictions: 11621\n    tp: 34\n    pred_count: 10839\n    gold_count: 12151\n    inference_time_seconds: 5211.4\n- exp_id: mvp2_eval_ced_kl001_r4_multi\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    checkpoint-10:\n      f1: 0.003\n      ign_f1: 0.003\n      evi_f1: 0.72\n      edcr: 0.9983\n      format_ok_rate: 0.999\n    checkpoint-20:\n      f1: 0.0088\n      ign_f1: 0.0088\n      evi_f1: 0.423\n      edcr: 0.9954\n      format_ok_rate: 0.999\n    checkpoint-30:\n      f1: 0.0338\n      ign_f1: 0.0338\n      evi_f1: 0.5889\n      edcr: 0.9798\n      format_ok_rate: 1\n    checkpoint-50:\n      f1: 0.1563\n      ign_f1: 0.1563\n      evi_f1: 0.5643\n      edcr: 0.8858\n      format_ok_rate: 0.999\n    checkpoint-60:\n      f1: 0.1467\n      ign_f1: 0.1467\n      evi_f1: 0.5763\n      edcr: 0.9062\n      format_ok_rate: 1\n    checkpoint-90:\n      f1: 0.2108\n      ign_f1: 0.2108\n      evi_f1: 0.5666\n      edcr: 0.8584\n      format_ok_rate: 1\n- exp_id: mvp2_eval_ced_kl001_r4_step100\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.2167\n    ign_f1: 0.2167\n    precision: 0.2849\n    recall: 0.1749\n    evi_f1: 0.5746\n    evi_precision: 0.5244\n    evi_recall: 0.6353\n    edcr: 0.8539\n    pred_count: 7460\n    gold_count: 12151\n    tp: 2125\n    n_truncated: 21\n    format_ok_rate: 1\n- exp_id: mvp2_eval_ced_kl001_r4_last\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt90\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_high\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    checkpoint_60:\n      rel_f1: 0.1467\n      ign_f1: 0.1467\n      precision: 0.1909\n      recall: 0.1192\n      evi_f1: 0.5763\n      edcr: 0.9062\n      pred_count: 10041\n      gold_count: 12151\n      n_truncated: 16\n      format_ok_rate: 1\n    note: Only ckpt-60 completed. Process died during ckpt-70 inference at 8% (5/62\n      batch). ckpt-80/90 never started.\n- exp_id: mvp2_eval_ced_kl001_r4_step90\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.2108\n    ign_f1: 0.2108\n    evi_f1: 0.5666\n    edcr: 0.8584\n    pred_count: 11160\n    n_truncated: 22\n    format_ok_rate: 1\n    n_documents: 985\n- exp_id: mvp2_grpo_ced_lr5e6_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_p1_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_rp_r1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt7080\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_rp_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt20\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0077\n    rel_precision: 0.0071\n    rel_recall: 0.0084\n    evi_f1: 0.628\n    evi_precision: 0.855\n    evi_recall: 0.496\n    edcr: 0.993\n    format_ok_rate: 0.991\n    field_compliance_rate: 0.399\n    pred_count: 14440\n    gold_count: 12151\n    tp: 102\n    n_truncated: 587\n    inference_time_seconds: 6370.4\n- exp_id: mvp2_eval_lr5e6_r1_ckpt40\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt40_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0071\n    precision: 0.0066\n    recall: 0.0078\n    evi_f1: 0.7584\n    evi_precision: 0.9113\n    evi_recall: 0.6494\n    edcr: 0.9942\n    format_ok_rate: 0.9939\n    field_compliance_rate: 0.5675\n    pred_count: 14434\n    gold_count: 12151\n    tp: 95\n    n_truncated: 424\n    inference_time_seconds: 6152\n- exp_id: mvp2_eval_lr5e6_rp_r2_ckpt20\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_sft_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    pred_count: 12234\n    gold_count: 12151\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.998\n    field_compliance_rate: 0.6264\n    n_truncated: 367\n    inference_time_seconds: 6138.5\n- exp_id: mvp2_eval_lr5e6_r1_ckpt60\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt80\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0116\n    ign_f1: 0.0116\n    precision: 0.0109\n    recall: 0.0124\n    evi_f1: 0.828\n    evi_precision: 0.928\n    evi_recall: 0.748\n    edcr: 0.993\n    format_ok_rate: 0.999\n    field_compliance_rate: 0.788\n    pred_count: 13828\n    gold_count: 12151\n    n_truncated: 210\n    inference_time_seconds: 6099\n- exp_id: mvp2_eval_lr5e6_r1_ckpt60_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0093\n    precision: 0.0085\n    recall: 0.0103\n    evi_f1: 0.81\n    edcr: 0.993\n    format_ok_rate: 0.998\n    pred_count: 14626\n    gold_count: 12151\n    tp: 125\n    inference_time_seconds: 6152\n- exp_id: mvp2_eval_lr5e6_r1_ckpt100\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0138\n    rel_precision: 0.0132\n    rel_recall: 0.0144\n    ign_f1: 0.0138\n    evi_f1: 0.8504\n    evi_precision: 0.9256\n    evi_recall: 0.7866\n    edcr: 0.9876\n    format_ok_rate: 0.999\n    field_compliance_rate: 0.8162\n    evidence_format_rate: 0.8162\n    tp: 175\n    pred_count: 13300\n    gold_count: 12151\n    n_predictions: 15498\n    n_truncated: 181\n    n_documents: 985\n    n_parseable: 984\n    inference_time_seconds: 5901.7\n- exp_id: mvp2_diversity_probe\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    unique_triples_t07: 5\n    unique_triples_t10: 8\n    jaccard_t07: 0.17\n    jaccard_t10: 0.051\n    format_ok_rate_t07: 0.5\n    format_ok_rate_t10: 0.438\n    n_samples: 3\n    n_generations: 8\n    note: 'unique_triples_t07 corrected from 7 to 5.0 (mean). Reviewer: format_ok\n      ~34% after fix, ''diversity'' was JSON key name variants not semantic diversity'\n- exp_id: mvp2_rsft_generate\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    generation_count: 5288\n    unique_docs: 659\n    format_compliance: 0.998\n    diversity_range: 7.5-7.8/8\n    exit_code: 0\n- exp_id: mvp2_rsft_ced_scoring\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    input_generations: 21952\n    selected_samples: 2718\n    unique_docs: 2691\n    selection_rate: 0.124\n    mean_f1: 0.6157\n    mean_ced: 0.6683\n    f1_range:\n    - 0.1026\n    - 1\n    zero_f1_samples: 0\n    selection_strategy: top_k=1\n    f1_threshold: 0.1\n- exp_id: mvp2_rsft_train_r1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.0483\n    num_preds: 848\n    sft_baseline_rel_f1: 0.4057\n    failure_mode: relation_ontology_collapse_to_freetext\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n- exp_id: mvp2_rsft_train_r1_s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.7622\n    train_loss: 0.6148\n    eval_entropy: 0.6724\n    mean_token_accuracy: 0.8291\n    total_steps: 510\n    epochs: 3\n    training_hours: 1.99\n- exp_id: mvp2_rsft_train_r1_s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4655\n    evi_f1: 0.8087\n    edcr: 0.635\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0598\n    delta_evi_f1: 0.0108\n    mvp2_pass: true\n- exp_id: mvp2_rsft_ced_scoring_topk3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_ced_reranker_poc\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_rsft_diagnosis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    root_cause: overfitting_plus_sft_knowledge_overwrite\n    truncated_json_samples: 170\n    truncated_pct: 6.3\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n    lora_scaling: 2\n    rsft_zero_relation_samples: 170\n    sft_zero_relation_docs: 26\n    rsft_mean_relations: 11.2\n    sft_mean_relations: 12.5\n- exp_id: mvp2_rsft_train_r2_fix\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_rsft_r2a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4494\n    evi_f1: 0.8108\n    edcr: 0.6641\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0437\n    delta_evi_f1: 0.0129\n    mvp2_pass: true\n- exp_id: mvp2_rsft_r2b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4493\n    evi_f1: 0.8128\n    edcr: 0.6609\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0436\n    delta_evi_f1: 0.0149\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4449\n    evi_f1: 0.8187\n    edcr: 0.6565\n    num_preds: 15307\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0392\n    delta_evi_f1: 0.0208\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r2a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4494\n    ign_f1: 0.4494\n    evi_f1: 0.8108\n    edcr: 0.6641\n    precision: 0.4512\n    recall: 0.4475\n    evi_precision: 0.8143\n    evi_recall: 0.8073\n    format_ok_rate: 1\n    n_predictions: 15482\n    n_truncated: 208\n    inference_time_s: 5967.2\n- exp_id: mvp2_eval_rsft_r2b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4493\n    ign_f1: 0.4493\n    evi_f1: 0.8128\n    edcr: 0.6609\n    precision: 0.4566\n    recall: 0.4424\n    evi_precision: 0.8201\n    evi_recall: 0.8056\n    pred_count: 14829\n    format_ok: 983/985\n    truncated: 179\n    inference_time_s: 5862\n- exp_id: mvp2_eval_rsft_s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_s43_r2\n  name: ''\n  status: ANALYZING\n  conclusion: success\n  metrics:\n    rel_f1: 0.4683\n    ign_f1: 0.4683\n    evi_f1: 0.8156\n    edcr: 0.6388\n    precision: 0.4817\n    recall: 0.4556\n    evi_precision: 0.8142\n    evi_recall: 0.817\n    n_predictions: 14970\n    n_truncated: 171\n    format_ok_rate: 1\n    inference_time_s: 6316.7\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0626\n    delta_evi_f1: 0.0177\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r2b_maxtok1536\n  name: ''\n  status: RUNNING\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_r2b_maxtok1536_r2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_rsft_ced_scoring_topk3_r2\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T13:29:42.402Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T13:29:42.402Z",
  "sessionId": "c88f356d-19e6-4318-9584-f84bcdbc9c1c"
}
```

---

## Round 1

14 recorded events

### User

_source line 3 · 2026-05-15T13:29:42.431Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：核心方法有效但 CED 优势不显著：RSFT 整体优于 SFT 但 CED vs flat-NLI p>0.05，GRPO G=8 仍崩，EDCR 人工验证中等
核心假设：['CED vs flat-NLI RSFT 差异方向正确但不显著（Δevi_f1 0.3-1.2pp, p=0.05-0.20），CED 的对比性 margin 优势被 NLI 噪声稀释', 'Test set rel_f1 Δ = +2.0-3.5pp over SFT（dev→test 退化 2-3pp），仍显著但幅度收窄', 'GRPO G=8 仍崩（rel_f1 < 0.10），Claim 3 成立但需承认 full-rank 未测', 'DPO 结果不够理想：要么也部分崩（rel_f1 0.10-0.25）要么接近 RSFT（rel_f1 0.40+），光谱不够清晰', 'EDCR 与人工判断 r=0.35-0.55，有信号但不够强']
关键指标范围：{'test_rel_f1_delta_over_sft': [2.0, 3.5], 'ced_vs_flatnli_evi_f1_delta': [0.3, 1.5], 'ced_vs_flatnli_edcr_delta': [-5.0, -1.0], 'ced_vs_flatnli_p_value': [0.05, 0.2], 'grpo_g8_best_rel_f1': [0.0, 0.1], 'dpo_rel_f1': [0.1, 0.42], 'edcr_human_pearson_r': [0.35, 0.55], 'rsft_best_test_rel_f1': [0.41, 0.45], 'rsft_test_evi_f1_joint': [0.28, 0.36]}
叙事方向：触发 CED contingency plan：CED 从核心贡献降级为"可选 scoring function"。 论文重心转移到三条独立但互补的贡献： (1) Claim 1 升格为主贡献——首个 evidence-generating LLM for DocRE，RSFT（无论用哪种 scorer）均显著优于 SFT； (2) Claim 3 保持——GRPO+QLoRA decoupling phenomenon 作为 analysis contribution，但 DPO 部分需根据实际结果灵活处理； (3) Claim 4 调整——EDCR 作为 diagnostic tool 而非 validated metric，报告人工相关性但坦诚局限。 CED vs flat-NLI 作为 ablation 诚实报告"方向正确但未达显著"，不作为 selling point。 叙事从 "CED 是关键创新" 转为 "RSFT pipeline 是关键创新 + GRPO failure analysis 是独立贡献"。 需要补充实验加强 Claim 1（如 model size ablation 或 Re-DocRED）弥补 CED claim 的弱化。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: faith-evidence-ie
venue: EMNLP 2026 Main
focus: D042 修正后 re-dream。关键变化: (1) Claim 3 缩窄为 GRPO+QLoRA 而非 online RL; (2) 新增 GRPO G=8 实验(plan_011); (3) 新增 DPO baseline(plan_012); (4) CED contingency plan(如 p>0.05 则降级); (5) Evi-F1 改为 DREEAM 对齐协议(joint); (6) 新增 EDCR 人工验证(plan_013)。请关注这些修改是否有效提升了论文质量。

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
- **⚠️ Dream 风险**: 三档 Dream 审稿均指出 CED vs flat-NLI 可能不显著（p>0.05）。**Contingency**: 如 plan_001 结果 p>0.05，降级 CED 为"一种可选 scoring function"而非核心贡献，论文主贡献重心转移到 Claim 1（首个 evidence-generating LLM for DocRE）和 Claim 3（decoupling phenomenon）

### Claim 3 (Analysis): GRPO+QLoRA 在文档级 IE 上 catastrophic forgetting 且呈现 evidence-extraction decoupling
- **范围限定**: 仅对 GRPO+QLoRA（非泛化到所有 online RL）——Dream 三档一致指出 overclaim 风险
- GRPO+QLoRA 在 3 种 reward type × 多个 lr 下全线失败
- **核心发现 (decoupling)**: evi_f1 在 GRPO 下提升至 0.850（>SFT 0.798）但 rel_f1 崩至 <0.02——RL 差异化优化了 evidence 但摧毁了 extraction
- RSFT 规避此问题：不修改 policy gradient，只筛选训练数据
- **MVP 已有完整证据**: D031/D033 GRPO 判死，D039 RSFT 成功
- **⚠️ Dream 风险**: G=4 太小（标准 G=8-16），需测 G=8 排除 advantage estimation noise 的干扰；LoRA-only 是额外 confound

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

### RC5: GRPO 配置可能不充分（Dream 三档一致）
- **攻击**: "G=4 太小（标准 G=8-16），LoRA-only 是 confound，可能是 GRPO+QLoRA 的问题而非 GRPO 本身"
- **应对**: (1) 加 G=8 实验验证（plan_011）；(2) 论文范围限定为 "GRPO+QLoRA" 而非 "online RL"；(3) 完整轨迹数据仍有效（3 reward × 2 lr × 全 checkpoint）
- **Research**: GRPO G=8 实验 + 论文标题/claim 措辞调整

### RC6: EDCR 63-66% 仍然偏高，CED 对证据精确度提升有限
- **攻击**: "RSFT+CED 的 EDCR 只比 SFT 低 5-8pp，证据质量提升不够显著"
- **应对**: (1) CED 在 RSFT 中是间接作用（筛选训练数据），非直接 reward；(2) CED-as-reranker 可能更直接降低 EDCR；(3) 需要 flat-NLI RSFT 对比证明 CED 方向正确
- **Research**: CED reranker PoC（运行中），top_k ablation

### RC7: 方法过于简单
- **应对**: 简洁是优点——RSFT 方法论已被证明理论等价于 PPO (ICML 2025)，CED 创新在于打分函数设计而非框架复杂度

### RC8: 缺少中间方法 baseline（Dream 两档一致 [M][W]）
- **攻击**: "GRPO(online) vs RSFT(offline) 缺少 DPO/KTO 等中间方法，无法定位失败边界"
- **应对**: 加 DPO+CED experiment（plan_012），至少一个中间方法填补 online-offline 光谱

### RC9: EDCR 需要人工验证（Dream 两档一致 [M][W]）
- **攻击**: "EDCR 未经人工标注验证，与 Evi-F1 的弱相关 r=-0.42 无法区分信号与噪声"
- **应对**: 100 样本人工标注研究（plan_013），验证 EDCR 与人类判断的相关性

### RC10: Evi-F1 评测协议不一致（D041 已确认）
- **攻击**: "你们的 Evi-F1 (conditional) 与 DREEAM (joint) 不可比"
- **已修复**: 实现 DREEAM 对齐评测函数，论文报告两种 Evi-F1（joint 为主，conditional 为辅）

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

- **必要条件**: RSFT 在 test set 上 Evi-F1_joint（DREEAM 协议）> SFT baseline AND rel_f1 显著 > SFT baseline（D041: Evi-F1 对比 DREEAM 需用对齐协议，暂冻结绝对阈值）
- **充分条件**: 上述 + CED vs flat-NLI RSFT 差异显著 + GRPO decoupling 分析完整 + EDCR 人工验证
- **CED contingency**: 如 CED vs flat-NLI p>0.05 → 论文重心转为"首个 evidence-generating LLM for DocRE + GRPO decoupling phenomenon + EDCR metric"，CED 降为可选组件
- **Failure pivot**: RSFT 在 test set 上无显著改进 → 转为 analysis contribution（GRPO failure analysis paper）

## Research Phase Priorities

| Priority | 实验 | Claim/RC | 预估 GPU-hours | Dream 驱动 |
|----------|------|---------|---------------|-----------|
| P0 | CED vs flat-NLI RSFT ablation | C2 | ~4h | ⚠️ 三档一致风险 |
| P0 | Test set evaluation (RSFT best config) | C1 | ~4h | |
| P0 | Evi-F1 DREEAM 协议对齐 + 重评 | RC10 | ~1h (CPU) | D041 |
| P0 | EDCR pipeline 验证 + cross-method table | C4 | ~2h | |
| P0 | DREEAM/SAIS Evi-F1 baseline reproduction | C1 | ~8h | |
| P0 | GRPO G=8 实验 | C3/RC5 | ~8h | ⚠️ 三档一致 |
| P1 | CED-as-reranker (running) | C1 bonus | ~6h | |
| P1 | DPO+CED experiment | RC8 | ~12h | Dream [M][W] |
| P1 | EDCR 人工标注验证 (100 samples) | RC9/C4 | ~0h (人工) | Dream [M][W] |
| P1 | Model size ablation (1.7B/8B) | RC4 | ~24h | |
| P1 | Re-DocRED extension | RC4 | ~12h | |
| P1 | top_k ablation (k=1 vs k=3) | RC6 | ~8h | |
| P2 | GRPO forgetting 详细分析 + 可视化 | C3 | ~4h | |
| P2 | DeBERTa-base vs large NLI 对比 | RC1 | ~4h | |


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
- id: plan_011
  claim: 3
  description: 'GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward
    + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要
    gradient_accumulation 适配显存。'
  priority: P0
  gpu_budget_hours: 8
  deps: []
  registry_id: null
  status: planned
- id: plan_012
  claim: 3
  description: 'DPO+CED experiment: Dream [M][W] 指出缺少 online-offline 中间方法 baseline。用
    RSFT 候选数据构造 preference pairs (CED-preferred vs CED-rejected)，DPO 训练。验证 DPO 是否避免
    GRPO 的 catastrophic forgetting。'
  priority: P1
  gpu_budget_hours: 12
  deps:
  - plan_001
  registry_id: null
  status: planned
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
    edcr: 0.635
    sft_baseline_rel_f1: 0.4057
    sft_baseline_evi_f1: 0.7979
    delta_rel_f1: 0.0598
    delta_evi_f1: 0.0108
    mvp2_pass: true
- exp_id: mvp2_rsft_ced_scoring_topk3
  name: ''
  status: DONE
  conclusion: killed
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
  status: ANALYZING
  conclusion: success
  metrics:
    rel_f1: 0.4683
    ign_f1: 0.4683
    evi_f1: 0.8156
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
    mvp2_pass: true
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
- exp_id: mvp2_rsft_ced_scoring_topk3_r2
  name: ''
  status: ANALYZING
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
  "promptId": "49945883-8785-483d-b2d8-acb95bb3aca1",
  "type": "user",
  "uuid": "055ea995-1c33-4a4e-8e43-df3a0ef60cc1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "c88f356d-19e6-4318-9584-f84bcdbc9c1c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T13:29:42.429Z_

```json
{
  "parentUuid": "055ea995-1c33-4a4e-8e43-df3a0ef60cc1",
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
  "uuid": "24aee4b5-7f23-45fc-a9b0-58b115d95d9c",
  "timestamp": "2026-05-15T13:29:42.429Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "c88f356d-19e6-4318-9584-f84bcdbc9c1c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T13:29:42.429Z_

```json
{
  "parentUuid": "24aee4b5-7f23-45fc-a9b0-58b115d95d9c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3be1e07a-4fd9-49b8-b3ee-cb8e82166cb3",
  "timestamp": "2026-05-15T13:29:42.429Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "c88f356d-19e6-4318-9584-f84bcdbc9c1c",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心方法有效但 CED 优势不显著：RSFT 整体优于 SFT 但 CED vs flat-NLI p>0.05，GRPO G=8 仍崩，EDCR 人工验证中等 核心假设：['CED vs flat-NLI RSFT 差异方向正确但不显著（Δevi_f1 0.3-1.2pp, p=0.05-0.20），C…",
  "leafUuid": "3be1e07a-4fd9-49b8-b3ee-cb8e82166cb3",
  "sessionId": "c88f356d-19e6-4318-9584-f84bcdbc9c1c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Detailed median-tier experimental results with contingency narratives",
  "sessionId": "c88f356d-19e6-4318-9584-f84bcdbc9c1c"
}
```

---

### Assistant

_source line 8 · 2026-05-15T13:29:47.373Z_

I'll review the experiment plan and project context to generate detailed median-tier predictions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3be1e07a-4fd9-49b8-b3ee-cb8e82166cb3",
  "isSidechain": false,
  "requestId": "req_011Cb4SC5SNBSsUhAqKhfsxu",
  "type": "assistant",
  "uuid": "8ed1ec7b-61b9-4472-8d69-d74c3f79dbb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "c88f356d-19e6-4318-9584-f84bcdbc9c1c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEf4NVWhDYKCVi5k2T4aAd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20920,
      "cache_read_input_tokens": 11841,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20920,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 131,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20920
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

_source line 9 · 2026-05-15T13:29:48.817Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WRqAqeEq68aHkJrnpWYDgq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/.claude/CLAUDE.md",
  "offset": 0,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ed1ec7b-61b9-4472-8d69-d74c3f79dbb5",
  "isSidechain": false,
  "requestId": "req_011Cb4SC5SNBSsUhAqKhfsxu",
  "type": "assistant",
  "uuid": "ded18adf-aeb7-45ca-bb12-eb09ab471159",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "c88f356d-19e6-4318-9584-f84bcdbc9c1c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEf4NVWhDYKCVi5k2T4aAd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20920,
      "cache_read_input_tokens": 11841,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20920,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 131,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20920
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

_source line 10 · 2026-05-15T13:29:48.842Z_

<details><summary>↩ Tool result · `toolu_01WRqAqeEq68aHkJrnpWYDgq`</summary>

```text
0	
1	## 输出风格
2	
3	- 回复简洁直接，不说废话
4	- 禁止客套开场（"好的！"、"没问题！"、"这是个好问题！"）和结束语（"希望对你有帮助！"、"如果还有问题请随时问！"）
5	- 不要复述用户的问题
6	- 不要给未被要求的建议或补充说明
7	- 推理要彻底，但输出只保留结论和必要信息
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ded18adf-aeb7-45ca-bb12-eb09ab471159",
  "isSidechain": false,
  "promptId": "49945883-8785-483d-b2d8-acb95bb3aca1",
  "type": "user",
  "uuid": "7f85c1c7-54ad-4d11-b0db-253f04b84719",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/.claude/CLAUDE.md",
      "content": "\n## 输出风格\n\n- 回复简洁直接，不说废话\n- 禁止客套开场（\"好的！\"、\"没问题！\"、\"这是个好问题！\"）和结束语（\"希望对你有帮助！\"、\"如果还有问题请随时问！\"）\n- 不要复述用户的问题\n- 不要给未被要求的建议或补充说明\n- 推理要彻底，但输出只保留结论和必要信息\n",
      "numLines": 9,
      "startLine": 0,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "ded18adf-aeb7-45ca-bb12-eb09ab471159",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "c88f356d-19e6-4318-9584-f84bcdbc9c1c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-15T13:41:08.687Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed median-tier imagined experiment results for each "planned" experiment in the experiment_plan. Let me go through each planned experiment and create predictions consistent with the median tier definition.

Let me identify all planned experiments:
1. plan_001 - CED vs flat-NLI RSFT ablation (P0)
2. plan_002 - Test set evaluation (P0)
3. plan_003 - EDCR pipeline validation + cross-method table (P0)
4. plan_004 - DREEAM baseline reproduction (P0)


5. plan_005 - CED-as-reranker (P1, RUNNING - should I include?)
6. plan_006 - Model size ablation 1.7B/8B (P1)
7. plan_007 - Re-DocRED extension (P1)
8. plan_008 - top_k ablation (P1)
9. plan_011 - GRPO G=8 (P0)
10. plan_012 - DPO+CED (P1)
11. plan_013 - EDCR human annotation (P1)
12. plan_009 - GRPO forgetting analysis (P2)
13. plan_010 - NLI model ablation (P2)

Looking at the performance patterns across these experiments: CED shows directional improvements but falls short of statistical significance with modest gains around 0.3-1.2pp. The test results show 2-3pp improvements over SFT baseline, though there's some degradation from dev to test. GRPO with G=8 continues to underperform significantly, while DPO results are inconsistent—either collapsing partially or matching RSFT performance. EDCR human correlation sits in the moderate range at 0.35-0.55. Now I'm looking at the performance metrics across these parameter ranges and narrative outcomes. The paper's shifted focus toward RSFT as the primary contribution with GRPO analysis and EDCR serving as a diagnostic tool, moving ED to optional scoring. I'm working through the CED versus flat-NLI RSFT ablation, comparing the best CED RSFT checkpoint against what flat-NLI RSFT should achieve—expecting them to be close in performance with CED showing directional but not statistically significant gains.

For the test set evaluation, I'm projecting how the dev performance degrades when moving to test data, accounting for the 2-3 percentage point drop in relation F1 and cross-referencing against the SFT baseline to establish the meaningful delta.

Now I'm looking at the evidence F1 scores under the DREEAM joint protocol, which shows notably lower values compared to the conditional setup. For the cross-method comparison table, I need to gather EDCR scores across all the different approaches—I have the SFT baseline at 0.7118 and the RSFT-CED best at 0.6388, and I'm still collecting the RSFT-flatNLI results to complete the comparison.

Beyond that, I'm sketching out several other experiments: reproducing DREEAM's test performance of 57.34 on the evidence F1 metric, testing how model size affects RSFT performance across 1.7B and 8B variants, and exploring whether cleaner Re-DocRED labels yield similar improvements. I'm also planning ablations on the top_k parameter to understand the noise-quality tradeoff, and checking why GRPO with G=8 still underperforms in the median tier despite the other optimizations.

For the remaining experiments, I'm looking at mixed results with DPO+CED combinations, validating EDCR correlations with human judgments, visualizing where GRPO causes catastrophic forgetting, and testing whether DeBERTa-large outperforms other NLI backbones for CED scoring.

Now I'm working through the detailed rationales for each experiment, starting with the CED versus flat-NLI RSFT ablation where my best dev results show specific rel_f1 and evi_f1 scores. Looking at the flat-NLI RSFT predictions compared to the best CED configuration, the performance drops are modest — around 1 percentage point for relevance F1, less than 1 point for evidence F1, and about 1.3 points for EDCR, all within expected variance ranges. The evidence F1 difference isn't statistically significant at the 0.05 level, which suggests NLI noise dilutes the advantage but the candidate selection still captures meaningful signal. need to think about this more carefully. The experiment would likely run multiple configs of flat-NLI RSFT and compare to CED RSFT. Let me structure this.

The CED vs flat-NLI comparison on evi_f1:
- ced_vs_flatnli_evi_f1_delta: [0.3, 1.5] → I'll use 0.8pp
- ced_vs_flatnli_edcr_delta: [-5.0, -1.0] → CED has EDCR 1-5pp lower → I'll use -2.5pp
- p-value: [0.05, 0.2] → I'll use 0.12

For flat-NLI RSFT best config, I'm estimating rel_f1 at 0.460 and evi_f1 around 0.808, with EDCR at 0.664. Now looking at test set performance — DocRED typically shows degradation from dev to test due to annotation differences and harder examples. I'm projecting the best RSFT test rel_f1 in the 0.41-0.45 range, settling on 0.432, which represents about a 2.8pp gain over SFT's ~0.404. For evidence evaluation, the joint protocol gives much lower scores than the conditional approach, so I'm estimating rsft_test_evi_f1_joint around 0.32. Wait, let me reconsider. The dev evi_f1 values (conditional) were ~0.80+. With DREEAM joint protocol, these would be much lower. The test evi_f1_joint range [0.28, 0.36] suggests a massive drop. This makes sense because joint Evi-F1 conditions on getting the relation correct first, and since RSFT rel_f1 is ~0.43 on test, only about 43% of triples are correct, which bounds the joint evi_f1. The joint metric essentially multiplies relation precision/recall by evidence precision/recall.

So if I think about this more carefully, DREEAM's reported Evi-F1 of 57.34 on test is their joint score, and they achieve much higher rel_f1 (63+ with their encoder). For RSFT with rel_f1 around 0.43, the joint evi_f1 would be roughly the product of relation F1 and conditional evidence F1—so 0.43 × 0.80 ≈ 0.34, which aligns perfectly with the [0.28, 0.36] range I'm seeing. I'll use 0.32 as my estimate.

Now I'm compiling the cross-method EDCR comparison table with SFT at 0.712, RSFT-CED at 0.639, RSFT-flatNLI at 0.664, and checking what the CED-reranker should yield.

For the CED-as-reranker experiment that's currently running, I'm predicting it will achieve around 0.668 EDCR by reranking the top 8 SFT candidates—higher than RSFT-CED but lower than SFT, with rel_f1 improving slightly to 0.430 and evi_f1 reaching 0.810 by selecting evidence-better candidates.

I should also plan a model size ablation to see how performance scales.  With a 1.7B model, I'd expect SFT to hit around rel_f1 0.35 and evi_f1 0.78, while RSFT-CED improves to 0.38 and 0.79 respectively—showing the method generalizes even with less capacity. The 8B model should show similar delta improvements, reaching rel_f1 0.44-0.47 and evi_f1 0.81-0.82.

I also want to test on Re-DocRED with its cleaner annotations to see if the pattern holds, and run a top_k ablation starting with top_k=1 on the current 2718 samples to establish the baseline.

For top_k=3 with 8000 samples, I'd expect more noise that might slightly hurt evidence F1 in the median tier, though the extra training data could help maintain relation F1. GRPO with G=8 still seems problematic—even with better advantage estimation, the fundamental issue of catastrophic forgetting in structured IE tasks persists, leaving relation F1 below 0.10 while evidence F1 stays high. DPO with CED is ambiguous in the median tier, so I need to see what the actual results show. DPO sits in an awkward middle ground—better than GRPO but clearly underperforming RSFT, which makes it a partial success that doesn't fit neatly into the online-versus-offline framework. For the EDCR human annotation experiment, I'm setting the correlation at around 0.44 to represent moderate but meaningful signal. The GRPO forgetting analysis is straightforward since I'm just visualizing the existing data to show the reward-versus-relevance divergence. DeBERTa-large should give slightly better margins and discrimination than the base model for the NLI ablation. Now I need to write out the full YAML with all the planned experiments, making sure the numbers are reasonable—starting with the flat-NLI scoring pipeline for plan_001, then RSFT training and evaluation.

For the flat-NLI approach, I'll skip the CED margin calculation and just use the raw entailment probability for each evidence set, which should still select reasonable candidates but won't discriminate as well against entity-sharing distractors. I'll test multiple configurations to match the CED setup, and here are the specific results for plan_001: Config A with 3 epochs and alpha 128 gives rel_f1 of 0.448 and evi_f1 of 0.810, Config B with the same settings but different seed yields 0.462 and 0.808, and Config C with 1 epoch produces 0.452 and 0.804.

Config D with 1 epoch and lower alpha of 32 gets 0.451 rel_f1 and 0.806 evi_f1, while the CED best run achieves 0.4683 rel_f1 and 0.8156 evi_f1 compared to flat-NLI's best of 0.462 and 0.808. Looking at the paired comparisons across these configurations, the evidence F1 difference averages around 0.8 percentage points with a range of 0.3 to 1.5, the EDCR drops by about 2.2 percentage points on average, and the bootstrap p-value for evidence F1 is roughly 0.12.

So the actual experiment would train the best one or two hyperparameter configurations from CED using the flat-NLI filtered data instead, letting me directly compare the two approaches under identical training conditions. Now I'm planning out the YAML structure systematically, and I need to think through what tables and figures would make sense for each experiment — comparing CED versus flat-NLI RSFT results across configurations, showing evidence F1 and EDCR distributions, test set performance against baselines, cross-method diagnostics, reproduced versus published DREEAM numbers, training curves for different GRPO settings, and comparisons across DPO, GRPO, and RSFT methods.

For the final visualization, I'm looking at a scatter plot showing the relationship between EDCR and human judgment with correlation statistics. Now I'm writing out the complete YAML configuration and double-checking the expected metric ranges for each experiment — things like the relative F1 improvements, evidence F1 deltas between methods, EDCR differences, p-values, and correlation coefficients between EDCR and human evaluation.

For plan_002 specifically, I need to clarify how the joint evidence F1 metric is calculated — whether it's the standard DREEAM approach where evidence F1 is computed only on correctly predicted triples and then averaged, or if there's a different formulation being used here.

Given that RSFT achieves around 43% triple recall on dev with a conditional evidence F1 of ~0.81, the joint metric would be approximately 0.43 × 0.81 ≈ 0.35, which aligns with the expected range of [0.28, 0.36]. On test, with slightly lower recall (~0.41) and evidence quality (~0.79), I'd expect the joint score to drop to around 0.32.

Comparing to DREEAM, which has a rel_f1 of ~63.5% and joint evi_f1 of ~57.34%, their conditional evidence F1 works out to roughly 0.903. Our model's conditional evidence quality at ~0.81 is actually quite competitive—the gap comes from finding fewer correct triples overall, not from worse evidence quality per triple.

Now I'm organizing the YAML structure by plan_id, focusing on the planned experiments the user specified.

Looking at which experiments to include: plan_001 through plan_004 are planned, plan_005 is currently running, and plan_006 through plan_013 are all planned. I'll include everything that isn't marked DONE.

Compiling the final numbers for each experiment. For plan_001, I'm comparing the CED versus flat-NLI RSFT ablation—flat-NLI RSFT achieved rel_f1 of 0.4610 with evi_f1 of 0.8078 and EDCR of 0.6590, while CED RSFT's best run got rel_f1 of 0.4683 with evi_f1 of 0.8156.

Now I'm checking the deltas and statistical significance: evidence F1 improved by 0.8 percentage points, EDCR dropped by 2.0 percentage points, and the paired bootstrap p-value for evidence F1 is 0.12. These all fall within my expected ranges. For the paired test though, I need to match configurations directly—comparing CED config s43 against flat-NLI with the same hyperparameters, then moving through the other CED configurations. Now I'm finishing the calculation for the mean EDCR difference across runs, which comes to -1.68 percentage points with a p-value of 0.12. Moving to the test set evaluation, I'm comparing the SFT baseline against the RSFT best model and verifying that the improvements in relative F1, evidence F1, and EDCR all fall within the expected ranges. I'm realizing I need to be more careful about how DocRED test set evaluation is conducted. Looking at the test set results, RSFT achieves ign_f1=0.432 and rel_f1=0.434 compared to SFT's 0.398 and 0.400, giving a 3.4 percentage point improvement, with evi_f1_joint at 0.322 under the DREEAM protocol and EDCR at 0.648. I'm noticing that DocRED distinguishes between ign_f1 (ignoring training triples) and standard F1, though in MVP's dev set they appear equivalent at 0.4057 for SFT, so I should be careful not to conflate them.

On the test set, RSFT's best configuration shows rel_f1≈0.432, which represents a reasonable 2.6 percentage point drop from the dev performance of 0.468. Now I'm building a cross-method comparison table to show how EDCR varies across different approaches.

Generating markdown table...

Looking at the EDCR rankings, SFT performs best, followed by the reranker and flat-NLI variants, with CED RSFT trailing. For the DREEAM baseline, I'm checking the reproduction against the published results—the dev set Evi-F1 of 56.2 aligns closely with the reported 57.34 on test, which validates this as a solid comparison point.

Now I'm running the CED-as-reranker experiment with 8 SFT candidates, and the rel_f1 score is coming in at 0.4220.

The reranking approach gives a modest boost over the baseline SFT performance since it can pick better candidates from the pool, though the gains are limited because we're constrained to selecting from existing outputs rather than generating new ones. The evidence F1 improves noticeably to 0.8092 by choosing CED-preferred candidates, but the EDCR metric drops to 0.6680 without the training signal.

Looking at the model size ablation now, the 1.7B variant shows rel_f1 jumping from 0.340 with SFT to 0.368 with RSFT-CED training, gaining about 2.8 percentage points, while the 8B model scales up to 0.448 and 0.482 respectively with similar relative improvements.

The Re-DocRED extension benefits from having fewer false negatives in the gold standard, pushing the numbers higher across the board—rel_f1 reaches 0.478 and evi_f1 hits 0.825 with RSFT-CED training. Now examining the top_k ablation to see how performance varies with different candidate pool sizes.

With top_k=1 I'm getting rel_f1=0.4683 and evi_f1=0.8156, but expanding to top_k=3 actually hurts performance—rel_f1 drops to 0.4580 and evi_f1 falls to 0.8020. The noisier candidates in the larger pool are diluting the filtering quality of CED, and the evidence metrics suffer most since those additional candidates have weaker supporting evidence.

For the GRPO forgetting analysis, I'm visualizing how the model behaves across training checkpoints—the reward keeps climbing steadily while rel_f1 stays flat early on then crashes, whereas evi_f1 holds steady or improves even as relation extraction collapses.

Comparing DeBERTa-base against DeBERTa-large shows only modest gains: discrimination accuracy improves from 0.815 to 0.845 and mean margin from 0.48 to 0.55, suggesting the base model is already doing the job well enough.

Now I'm looking at the GRPO results with G=8 and finding something odd—the best checkpoint shows rel_f1=0.065 and evi_f1=0.840, which is still catastrophic forgetting, but the comparison with G=4 results isn't adding up cleanly, so I need to double-check those numbers.

The G=4 experiments had rel_f1=0.211 at lr=5e-5 and rel_f1=0.014 at lr=5e-6, but G=8 is predicting best rel_f1 under 0.10, which would actually be worse than what G=4 achieved—that's contradictory. Looking at the tier predictions, even with the larger group size, the fundamental catastrophic forgetting problem persists, and increasing G doesn't seem to solve it. ef=0.01, the training might be more stable but still collapse. Actually, I need to look more carefully at the experimental results. The plan_011 description mentions "G=8 + CED reward + kl_coef=0.01", while the G=4 lr=5e-5 baseline achieved rel_f1=0.211, and G=4 lr=5e-6 with kl_coef=0.01 peaked around 0.217 at step 100. So G=4's best performance was roughly 0.21. For G=8, the tier predictions suggest [0.0, 0.1], which is puzzling since larger group sizes should improve advantage estimation. The discrepancy might stem from how G=8 with kl_coef=0.01 reshapes the optimization landscape, or perhaps the constraint itself isn't stringent enough to prevent divergence. I'm checking whether the G=4 and G=8 experiments used consistent hyperparameters—if G=4 with kl_coef=0.01 and lr=5e-6 achieved rel_f1=0.217, then G=8 under the same settings should perform comparably, but the tier predicts rel_f1 < 0.10, suggesting either a different learning rate was used or the larger group size actually degrades performance in this regime. The likely culprit is memory pressure from gradient accumulation forcing smaller effective updates, which slightly slows the collapse but doesn't prevent it—the fundamental decoupling between evidence and relation extraction persists, leaving G=8's best checkpoint at rel_f1=0.078, notably worse than G=4's 0.217.

Actually, that framing of "worse" feels forced. A more plausible explanation is that plan_011 tested G=8 with the standard stable learning rate (probably lr=5e-6), whereas the G=4 result at lr=5e-5 was anomalously strong because the higher learning rate preserved some relation signal before full collapse. With G=8 paired with the more conservative lr=5e-6 and kl=0.01, training stabilizes but converges to the entropy-maximizing regime where the model maximizes evidence extraction at the cost of relation extraction.

The G=4 + lr=5e-5 result was just a transient point on the trajectory, not a stable equilibrium. With G=8, the advantage estimates improve, making the RL signal stronger, so the model optimizes the reward more effectively—but since CED measures evidence quality rather than relation extraction, better optimization of this misaligned reward actually accelerates the collapse of rel_f1. That's the real mechanism at play.

Now I'm looking at plan_012 with DPO+CED. The tier shows dpo_rel_f1 ranging from 0.1 to 0.42, which is still unclear. DPO uses preference pairs from RSFT candidates without a reward model in the loop, so it should sidestep the catastrophic forgetting we see with GRPO. I'm predicting rel_f1 around 0.33—substantially better than GRPO's 0.078 peak.

The issue is that DPO underperforms RSFT's 0.468, which creates a narrative problem since both are offline methods. The contrastive loss in DPO—pushing the model to increase good outputs while decreasing bad ones—seems less stable than RSFT's straightforward fine-tuning on positives alone. The noisy CED labels and the "decrease bad" signal likely degrade overall generation quality, leaving DPO in an awkward middle ground.

Looking at the tier constraints, it seems DPO should either partially collapse (rel_f1 0.10-0.25) or approach RSFT's performance (rel_f1 0.40+), but the spectrum isn't clear enough to distinguish which mechanism is actually at play. I'm settling on rel_f1=0.35 with evi_f1=0.795 and EDCR=0.658 to reflect this ambiguity—DPO sits between GRPO and RSFT without cleanly supporting either interpretation. I'm settling on DPO at rel_f1=0.34 because it sits in that awkward middle ground—better than GRPO but noticeably worse than RSFT—which makes it genuinely unclear whether the gap reflects training noise, hyperparameter tuning, or something fundamental about the method itself. This ambiguity actually captures the "median tier" tension I'm going for, since it doesn't cleanly support either the "offline methods work" or "online methods fail" narrative.

Now I'm looking at the human validation results for EDCR. I ran 100 samples where annotators judged whether cited evidence sentences actually support the relation, and the correlation with EDCR is moderate—Pearson r around 0.44, Spearman ρ around 0.41. The key finding is that humans flagged about 58% of sentences as true distractors, which is lower than EDCR's rate because some entity-sharing sentences do partially support the relation even if they're not in the gold annotations. This suggests EDCR is picking up real signal but the disagreement stems from incomplete gold labels in DocRED rather than EDCR being fundamentally flawed.

The correlation is strong enough to validate EDCR as a diagnostic tool, but too weak to claim it as a fully validated metric. This fits the narrative I'm building—EDCR works best as a diagnostic lens rather than a standalone evaluation measure.

Now I need to compile all the planned and running experiments into the full YAML output. Let me make sure I'm capturing all the non-completed experiments from the list.

I'm also reconsidering the DREEAM baseline numbers—the plan mentions confirming that 57.34 figure is reproducible, so I should treat that as the target metric we're aiming to validate.

Generating YAML structure... to see if it's reproducible on dev. Or maybe the plan expects us to reproduce on dev to verify the code works before comparing.

I'll assume: we reproduce DREEAM on dev and get a number close to what DREEAM would get on dev. The published 57.34 is test; dev might be slightly different (e.g., 58.1 or 56.5).

For SAIS, the published Evi-F1 is 55.67 (test). Similar pattern on dev.

Now I'm thinking through how joint Evi-F1 actually works in DREEAM's evaluation. The joint metric counts evidence F1 across all gold triples—if we predict a triple correctly, we compute evidence F1 between predicted and gold evidence; if we miss it entirely, that triple contributes 0 to the evidence score. So with roughly 12,151 gold triples and a rel_f1 around 0.468, I'd expect about 5,687 true positives, and for those the conditional evidence F1 is 0.816. I need to reconsider how joint and conditional evidence F1 relate to each other. The joint metric averages the per-triple evidence F1 scores, where triples that aren't recalled contribute zero, while recalled triples contribute their actual evidence F1. So if DREEAM achieves 57.34% joint Evi-F1 with around 62% recall on relations, I can decompose this to estimate the conditional evidence F1 for successfully retrieved triples.

For our RSFT model, I'm working through the numbers: on dev with 45.6% relation recall and roughly 81.6% conditional evidence F1, the joint metric comes to about 37.2%, and on test with slightly lower recall around 42% and conditional around 80%, the joint drops to about 33.6%. These estimates seem plausible given the performance degradation from dev to test.

Looking at the actual reported range for test joint evidence F1 of 0.28 to 0.36, my calculation of 0.336 sits right at the upper end, so I'll use 0.32 as a more conservative middle estimate. Comparing to DREEAM, their joint evidence F1 is substantially higher at around 58%, which makes sense because they achieve much higher recall—more true positives means more evidence contributing to the F1 score. However, where we're competitive is in the conditional evidence F1, where our 81.6% is quite close to what DREEAM achieves.

The story this tells is that our model generates reasonable evidence when it successfully extracts a relation, but the overall joint performance suffers because we're missing relations in the first place. Since DREEAM uses attention-based evidence rather than generative, the comparison isn't entirely apples-to-apples, but it still supports the narrative that evidence quality isn't our bottleneck—extraction recall is. This frames our contribution well: we're the first to generate evidence for document-level relation extraction, and while the evidence itself is decent, the main limitation is in finding all the relations to begin with.

Now I'm ready to write out the YAML configuration. I should also note that Re-DocRED addresses false negatives in the original DocRED dataset, which could be relevant for how I frame the evaluation.

For the other planned analyses, Re-DocRED's corrections should preserve our relative improvements while potentially boosting overall metrics. The GRPO forgetting analysis is mainly about visualization—showing how reward and task performance diverge, and how evidence F1 decouples from relation F1. For the NLI ablation, I'm wondering whether upgrading to DeBERTa-large actually moves the needle on CED scoring for our model, since better NLI capacity might not translate to meaningful downstream gains.

Now I'm organizing the YAML output and double-checking all the numbers for consistency across the different configurations and their metrics. Looking at the test results, the fine-tuned model achieves a rel_f1 of 0.400, and with RSFT-CED it improves to 0.432 with a 3.2 percentage point gain that falls within the expected range. The CED approach shows modest improvements over the flat-NLI baseline with an 0.8pp gain in evidence F1 and a slight 2.0pp decrease in EDCR, with a p-value of 0.12 suggesting marginal statistical significance.

Checking the remaining metrics—GRPO with G=8 achieves a 0.078 rel_f1 improvement, DPO reaches 0.34, human EDCR correlation is 0.44, and the RSFT best test results of 0.432 rel_f1 and 0.322 evidence F1 all validate within their expected ranges. Everything checks out, so I'm ready to finalize the YAML configuration, noting that GRPO with G=4 under similar settings only achieved 0.217 rel_f1 for comparison.

Looking back at the G=4 checkpoint progression with kl001, I'm seeing the rel_f1 actually climbs steadily through training rather than collapsing—starting at 0.003 at step 10, reaching 0.156 by step 50, and peaking at 0.217 by step 100, which contradicts my earlier assumption about faster optimization leading to earlier collapse.

The KL regularization appears to be stabilizing the relation extraction signal, whereas with G=8 the stronger advantage estimates seem to overwhelm this protective effect, causing rel_f1 to peak earlier at step 40 (0.078) before declining. Let me trace through the full G=8 trajectory to see where the degradation accelerates. and collapses—a clear decoupling between the two metrics. Now I'm ready to write up the YAML with comprehensive details and relevant data tables. I need to think through plan_002 more carefully though, particularly the test set predictions. For SFT, I'd expect a modest drop from the dev set performance to around 0.400, while RSFT might see a larger degradation to 0.432 given that it could be overfitting more heavily to dev characteristics.

Looking at the degradation pattern, SFT shows relative stability dropping only 0.6 percentage points from dev to test, whereas RSFT drops 3.6 percentage points—suggesting RSFT is more sensitive to the distribution shift. The delta itself shrinks from 6.3 percentage points on dev to 3.2 on test, a reduction of about 3.1 percentage points, which matches the expected 2-3 percentage point degradation I hypothesized. Now I'm working through the evidence F1 metrics under the same framework. Looking at the test set performance, I'm adjusting my estimates based on the precision-recall dynamics I see in the dev data. For SFT, recall drops slightly to around 0.39 on test, giving a joint score of about 0.308. For RSFT, the recall is higher at roughly 0.42, which would yield a joint score around 0.33 when multiplied by the conditional evidence F1.

The RSFT estimate of 0.33 fits within the expected range, so I'm settling on 0.322 for RSFT and 0.295 for SFT to finalize the configuration.

Now I'm checking the test metrics—RSFT shows a 3.2 percentage point improvement in relative F1 over SFT, which validates the approach. I'm also comparing our results against benchmarks like DREEAM and SAIS to see where we stand on the leaderboard.

The key insight is that while our absolute performance lags behind encoder-based methods, we're the first generative model to actually produce evidence predictions, and the quality of that evidence when conditioned on the relation is actually quite competitive. Now I need to write up the YAML configuration, and I should include plan_005 since it's already running. For plan_006, I'm reconsidering whether the 1.7B model will have enough capacity for the complex DocRE task—it'll likely drop significantly below the 4B model's performance, maybe hitting around 32% relative F1 compared to 40.6%.

The 8B model should perform better though, potentially reaching 45-50% with SFT given its additional capacity, though I need to be careful about direct comparisons since LMRC's 60.69% uses a different architecture and setup entirely. Our approach with evidence generation is fundamentally different from their extraction-only method, so the comparison isn't straightforward.

Looking at the concrete numbers across model sizes, the 1.7B gets about 32% with SFT and improves to 34.8% with RSFT-CED, while the 8B jumps to 44.8% with SFT and 48.8% with RSFT-CED. The consistent 3-4 percentage point improvement from RSFT across both sizes suggests the method generalizes well. For the Re-DocRED dataset with its corrected triples, I'd expect SFT to reach around 45% and RSFT-CED to hit 48%, showing similar gains even with the expanded annotation set.

Now I'm thinking through what happens when we evaluate models trained on DocRED against the Re-DocRED benchmark—the model would likely see a boost since Re-DocRED corrects false negatives that were previously marked as negatives, so predictions the model makes that were wrong before might now be correct. That could push SFT performance up to around 50% on Re-DocRED, with RSFT maintaining its 3-point advantage at 53%. But there's a complication here about whether we're retraining or just evaluating existing models. Looking at the predicted metrics on Re-DocRED, SFT reaches around 0.485 rel_f1 while RSFT-CED improves to 0.520, maintaining a similar 3.5pp delta over SFT as seen on the original test set. The evidence F1 scores also show modest gains with the revised annotations, suggesting the improvements are consistent across both relation and evidence metrics.

Now I'm clarifying how the CED reranker actually works — it generates multiple candidates from the base SFT model and selects the one with the highest evidence quality score, rather than retraining. This means the relation F1 gains come indirectly from picking candidates where the model happened to extract better relations alongside better evidence, while the evidence F1 improvements are more direct since CED is explicitly optimizing for evidence quality.

Looking at the results, the CED reranker shows improvements across all metrics compared to SFT, but underperforms the RSFT-CED approach because it's fundamentally limited to selecting from whatever the SFT model can generate — whereas RSFT actually shifts the model's generation distribution toward better evidence extraction.

Now I'm ready to write out the complete YAML configuration with all the experiment details and rationales. flat-NLI 均优于 SFT，test Δrel_f1 +3.2pp 显著；Claim 3 保持——GRPO G=8 确认 decoupling phenomenon，G=8 因更强 advantage estimation 反而加速崩溃；Claim 4 调整——EDCR 作为 diagnostic tool（r=0.44）而非 validated metric。CED vs flat-NLI 作为 ablation 诚实报告方向正确但 p=0.12 未达显著。DPO 结果（rel_f1=0.34）填充 online-offline 光谱但解释力有限。现在我想用 flat-NLI scoring 重新筛选 RSFT 候选来补强 CED 的 claim，直接用 DeBERTa-v3-base 的 entailment 概率打分，然后在 CED 的三组超参配置上分别训练对比，预期能达到 rel_f1 0.4610 和 evi_f1 0.8078。 Now I'm looking at the performance comparisons between these models—flat-NLI shows modest improvements over the baseline SFT approach, with about a 5.5 percentage point gain in relation extraction F1, though the evidence F1 improvement is smaller at 1 point. The statistical significance tests suggest these differences aren't quite reaching conventional thresholds, with p-values around 0.12-0.28. Comparing against CED, flat-NLI performs slightly better on evidence extraction but slightly worse on the overall EDCR metric by about 2 percentage points.

The reason flat-NLI still outperforms SFT despite these modest margins is that it has genuine signal—DeBERTa's NLI capability has been validated with 81.5% accuracy on the MVP-1 benchmark. However, CED's theoretical advantage in penalizing entity-sharing distractors gets diluted in practice by noise in the NLI model itself: DeBERTa shows positional bias on longer documents where contrastive and non-contrastive scores converge in high-confidence regions, and the hard negatives CED relies on (entity-sharing non-gold sentences) make up only about 35% of the document sentences in DocRED, limiting their impact.

Further complicating this is that roughly 15% of these hard negatives are actually false distractors—valid evidence the annotators missed—which weakens the signal-to-noise ratio of the contrastive margin. The indirect mechanism of RSFT (scoring → filtering → training data → fine-tuning) also attenuates whatever small differences exist between CED and flat-NLI at the scoring level. The result is that while the evidence F1 improvement of 0.8 percentage points points in the right direction, it doesn't reach statistical significance at p=0.12, falling short of the 0.05 threshold. The relation F1 difference is even smaller at 0.7 percentage points with p=0.28, since CED primarily affects evidence quality rather than relation extraction itself.

Now I'm looking at the performance metrics across these configurations to see how CED and flat-NLI compare on the development set. Generating comparison table...

The p-value of 0.12 means I can't claim CED significantly outperforms flat-NLI, but there are two encouraging signals: CED wins on both evi_f1 and EDCR across all three configurations, and flat-NLI RSFT still dramatically beats SFT, showing the RSFT pipeline itself is the real contribution. So I'm repositioning CED from a core innovation to an effective but optional scoring variant, and I'll report this honestly in the ablation section.

Now I'm planning the test set evaluation—submitting the best RSFT config alongside the SFT baseline to DocRED's CodaLab, computing Evi-F1_joint and EDCR locally, with expected results showing RSFT improving rel_f1 from 0.400 to 0.432. Looking at the performance metrics, I can see the dev-to-test degradation stems from a few key factors: the test set has different annotation patterns and entity distributions that the model struggles with, the RSFT training approach inadvertently overfits to dev characteristics through its scoring mechanism, while SFT remains more robust with minimal degradation.

The sharp drop in joint evidence F1 from 0.81 to 0.32 is actually an artifact of how the metrics are calculated—the joint protocol scores all gold triples and marks false negatives as zero evidence, which mathematically compresses the score. Despite the lower absolute numbers compared to DREEAM, our conditional evidence quality is actually competitive when accounting for their higher recall rates.

The statistical significance test (p<0.01) with a +3.2 percentage point improvement in relation F1 validates our first claim. Now I'm looking at the test set results across different methods to see how our approach compares. Now I'm looking at the performance breakdown—the joint evidence approach scores lower on F1 than the encoder-based baseline, but that's driven by extraction recall differences rather than evidence quality issues, so I need to clarify this distinction in the paper. The CED versus flat-NLI comparison shows negligible differences on the test set, which aligns with what I saw in development results. Next I'm planning to compute EDCR metrics across all evidence-producing methods to validate it as an independent diagnostic measure. 看起来 GRPO 的最差表现仍然超过 SFT，而各种 RSFT 变体之间的差异相对较小，最好的版本仍有大量引用来自非金标实体共享集合。EDCR 与证据 F1 的相关性较弱，因为两者衡量的维度不同——一个关注召回，一个关注精准度——但与关系抽取 F1 的负相关更明显，表明更好的关系识别能力。

现在我在查看一个诊断表格，对比不同方法的 EDCR 指标和证据提取表现。

表格显示 GRPO 在最佳检查点达到最高 EDCR（0.928），但关系抽取 F1 最低（0.078），而 RSFT+CED 方法虽然 EDCR 最低（0.639）但关系 F1 最高（0.468）——这反映了证据提取和关系识别之间的权衡。

EDCR 有效区分了三个方法类别：GRPO 的崩溃区、SFT/重排序的中间区、以及 RSFT 的优化区，但在 RSFT 内部的区分力有限，CED 和 flat-NLI 变体之间仅相差 2 个百分点。

DPO 的 EDCR 值接近 flat-NLI RSFT，这表明它的对比损失对证据质量的改进方式与 flat-NLI 评分相似。

接下来我需要在 DocRED 开发集上复现 DREEAM 基线，建立一个基于编码器的证据提取基准，预期达到 0.581 的联合证据 F1 分数和 0.625 的关系 F1 分数。

原论文在测试集上报告了 57.34 的分数，开发集应该略高，我的复现结果 58.1 是合理的，与测试集的差距约 0.8 个百分点，这是正常的开发-测试差距。使用官方代码和 RoBERTa-large 检查点，复现误差小于 1 个百分点验证了我们的评测协议与原始实现一致，SAIS 的复现结果（开发集 56.2）也在预期范围内。

现在对比我们的 RSFT 方法，开发集上的联合证据 F1 只有约 37.2%，远低于 DREEAM 的 58.1%，但这个差距主要来自抽取召回率的差异（我们 46.8% 对比 DREEAM 62.5%），而在条件证据质量上差距较小（我们 81.6% 对比 DREEAM 约 93%）。现在我在整理一个对比表格，展示不同方法在开发集上的性能指标。 The large gap in joint evidence F1 (58.1 vs 37.2) shouldn't be interpreted as poor evidence quality—when broken down by conditional performance, the difference shrinks to just ~11 percentage points (93 vs 82). More importantly, the generative methods produce explicit sentence citations that are auditable, while DREEAM relies on post-processed attention weights that can't be directly inspected, so the paper should highlight this methodological distinction. I'm also planning to test CED as a reranker during inference, using it to select the best candidate from the SFT model's top 8 outputs without any additional training, which should validate CED's utility at test time. Looking at the performance breakdown, the CED reranker shows modest gains because it's optimizing for evidence quality rather than relation extraction directly—the rel_f1 improvement is an indirect effect where better evidence leads to more coherent triples. The evidence F1 and EDCR changes are more direct signals of the reranker filtering out high-distractor candidates, but the 8.5x inference cost from generating multiple candidates and running NLI evaluations makes it less efficient than the supervised fine-tuning approach, positioning it as a complementary training-free alternative rather than a primary solution.

Comparing against the supervised approach, the supervised fine-tuning achieves a 6.3pp rel_f1 boost versus the reranker's 1.6pp, which suggests that CED signals are more effectively transmitted through training data curation than through inference-time reranking. This ablation serves to support the broader discussion about multiple ways to leverage CED as a quality signal. Now I'm examining how the method generalizes across different model scales with the 1.7B and 8B variants. Looking at the performance metrics for the 8B model variants, I see the RSFT approach with CED continues to show improvements across the board. The rationale is explaining how model capacity affects performance on DocRE tasks—the 1.7B baseline struggles significantly with the long document understanding and multi-hop reasoning required, but the RSFT method still delivers meaningful gains even at that smaller scale.

For the 8B model, the larger capacity produces a stronger foundation (0.448 baseline), and RSFT pushes it further to 0.488 with a +4.0pp improvement. The bigger model generates higher-quality candidates during the RSFT process, so after CED filtering, the training data is more useful. Interestingly, the 8B configuration achieves the lowest EDCR score (0.622) across all setups, which suggests the larger model might be better at handling the evidence extraction task.

Now I'm looking at the model size ablation results across different Qwen versions, showing how rel_f1, evidence F1, and EDCR metrics change with RSFT+CED. The pattern holds consistently—smaller models see modest gains while larger ones benefit more substantially from the approach. The 4B model shows the largest improvement, likely because hyperparameter optimization was tuned specifically on that size, while 1.7B and 8B used those same parameters without independent search—there's room for gains there. The paper can address the consistency concern by reporting results across all three model sizes, though the single-dataset limitation still needs validation on Re-DocRED. Now I'm planning to evaluate the DocRED-trained models on the corrected Re-DocRED dataset to see if the improvements hold up.

Looking at the Re-DocRED results, the metrics show meaningful gains across relation F1, evidence F1, and evidence-based classification scores. Since Re-DocRED corrects roughly 30% of the false negatives in the original DocRED annotations, I'm seeing how this impacts the model performance—the relation F1 improves by about 7.9 percentage points when evaluated on the corrected dataset. 0.406 跃升至 0.485 (+7.9pp)——模型本来就预测了这些 triples，只是在 DocRED 评估中被误判为 FP；(2) RSFT 同理提升至 0.520，delta +3.5pp 与 DocRED 上的 +6.3pp 有缩窄，原因是 Re-DocRED 的更完整标注使 SFT baseline 本身更强，RSFT 的增量空间被压缩（ceiling effect）；(3) Evi_f1 和 EDCR 略有改善——Re-DocRED 的 evidence 标注更完整，一些被 EDCR 标记为 distractor 的句子在 Re-DocRED 中成为 gold evidence。现在看一下 Re-DocRED 评估的结果表，对比 SFT 和 RSFT+CED 在两个数据集上的表现，RSFT 的改善方向保持一致。

接下来要分析 top_k ablation 实验，比较 CED scoring 中 top_k=3（约 8000 样本）和 top_k=1（2718 样本）的效果差异。

虽然扩大训练数据规模，但后续候选的质量递减——top_k=1 选择最高分候选时 CED margin 最大，而 top_k=2/3 的候选分数明显下降，引入更多实体共享的干扰项，这种数据量增加的收益可能被质量下降所抵消。

结果显示 rel_f1 反而略降（-1.0pp），evi_f1 降幅更大（-1.4pp），EDCR 升幅更大（+2.3pp），说明低质量候选直接污染了模型的证据引用策略，因此严格的单候选筛选优于扩展候选集的数据增量策略。

现在看具体的数据对比——top_k=1 时训练集 2718 条，rel_f1 达 0.468、evi_f1 0.816、EDCR 0.639；而 top_k=3 时训练集扩至 8154 条，但 rel_f1 降至 0.458、evi_f1 跌至 0.802、EDCR 反升至 0.662，这个质量与数量的权衡清晰地表明 CED 的严格排序筛选本身就有价值，即使在中位层级下也是 CED 唯一的正面独立贡献。

接下来要验证 GRPO 在 G=8 分组大小下配合 CED 奖励、KL 系数 0.01 和学习率 5e-6 的设置，看是否能缓解 QLoRA 的灾难性遗忘问题，预期在第 40 步达到最优检查点，rel_f1 为 0.078、evi_f1 0.835、EDCR 0.928。

现在看到实际的性能曲线数据，rel_f1 在第 40 步确实达到峰值 0.078，之后逐步下降到最终的 0.012，而 G=4 配置下的 KL 系数 0.01 相比之下 rel_f1 达到了 0.217，说明增大分组大小反而没有改善遗忘问题。

分析表明更精确的 advantage 估计虽然降低了方差，但导致模型更高效地优化 CED reward，而这个目标与关系抽取性能不一致，反而加速了灾难性遗忘，而较小的分组配合噪声可能起到了隐式正则化的作用。 现在看到 G=8 的结果更清楚地证实了这个结构性问题——GRPO+QLoRA 在文档级信息抽取上的失败不是超参数调优能解决的，而是方法本身的局限。我正在对比 G=4 和 G=8 的关键指标，包括最佳 relation F1 分数、崩溃时间点和最终性能。

G=8 配置在第 40 步达到峰值后迅速崩溃，而 G=4 则表现出更缓慢的衰退。现在查看 G=8 的逐步检查点轨迹...

Generating metrics table...

我看到两个关键的可视化：一个双轴图表展示相对 F1 分数下降而证据 F1 上升的对立趋势，在第 40 步左右出现交叉点；另一个散点图对比 G=4 和 G=8 的奖励与任务性能，清楚地表明更高的奖励并不等于更好的实际表现。这些数据强有力地支持我的第三个主张：增大组大小实际上加剧了遗忘问题，而不是解决它。

G=8 的证据 F1 峰值虽然略高于 G=4，但相对 F1 的下降幅度更大，这表明解耦现象随着更好的优势估计而恶化。这个结果有效地排除了对手的"G=4 太小"的批评，因为更大的组大小反而导致更差的性能。不过我需要谨慎措辞这个结论，确保它仅限于 GRPO+QLoRA 的情况，而不是过度泛化到全秩 GRPO 或其他方法。

现在我想设计一个 DPO 加 CED 的实验来填补在线 RL 和离线 RSFT 之间的空白——用 RSFT 候选数据构造偏好对，然后用 DPO 训练模型，看看这个中间方法能否在证据提取和关系提取之间取得更好的平衡。

我预期 DPO 的相对 F1 分数能达到 0.340，同时在其他指标上也有不错的表现。

现在看到实验的具体参数和结果分析——DPO 用 beta 为 0.1、训练 3 个 epoch，相对 F1 相比 GRPO 提升了 26.2 个百分点，这说明离线对比学习确实避免了在线 RL 中的灾难性遗忘问题，虽然相比 SFT 基线有所下降。

但 DPO 仍然不如 RSFT 的 0.468，主要是因为对比损失函数同时压低被拒绝样本会削弱生成多样性，加上 CED 标签本身有 18.5% 的噪声，DPO 对标签噪声比 RSFT 更敏感——RSFT 只用正例训练而不显式惩罚负例，所以噪声负例不会影响梯度更新。

而且 DPO 的 KL 约束虽然保持与 SFT 的距离，但在信息抽取这种精确任务中可能不够强，因为模型需要精确输出关系类型和证据索引，而 DPO 的隐式奖励建模不如 RSFT 的显式数据筛选精确。rel_f1=0.340 处于尴尬位置，既没有像 GRPO 那样完全崩溃，也没有像 RSFT 那样成功，这使得在线离线光谱分析变得模糊——DPO 虽然是离线方法但表现不如同样离线的 RSFT。

Generating markdown table... Looking at the spectrum diagram showing the online-offline tradeoff, I see that DPO's underperformance relative to SFT complicates the narrative—it suggests that not all offline methods work equally well, and that DPO's contrastive loss actually performs worse than basic supervised training. The key insight is that RSFT succeeds where DPO fails because it fundamentally operates differently, filtering rather than applying RL signals.

So I need to reframe the paper's main claim: instead of positioning offline RL as superior to online RL, the real story is about data quality curation outperforming preference learning, which in turn outperforms reward optimization. I should acknowledge this ambiguity around DPO in the discussion section.

Now I'm planning a validation study with human annotators checking whether cited evidence actually supports the claimed relationships across 100 samples, then measuring correlation with EDCR scores.

Looking at the validation results, EDCR shows moderate correlation with human judgment (r=0.44), which is meaningful but not strong—the metric tends to overestimate distractor rates by about 8.5 percentage points, and there's notable disagreement between annotators (κ=0.62).

The core issue is that DocRED's gold evidence annotations are incomplete: roughly 14% of sentences EDCR flags as entity-sharing distractors are actually valid evidence that human annotators missed, causing systematic overestimation. Additionally, entity-sharing is only a necessary but not sufficient condition for being a distractor—some of these sentences provide useful supporting context that humans rated as "partially supports," but EDCR's binary classification loses this nuance.

Looking at the human validation results, inter-annotator agreement sits at κ=0.62, which reflects the inherent subjectivity in evidence judgment and suggests no automatic metric can realistically exceed r>0.7. The correlation of r=0.44 between EDCR and human judgments is actually sufficient for using it as a diagnostic tool to compare evidence quality across different methods like GRPO versus RSFT, though it shouldn't be treated as a precise absolute measure.

Human validation metrics... Looking at how EDCR fits into the broader evaluation framework—it's positioned as a complement to Evi-F1, where Evi-F1 captures recall (whether gold evidence was retrieved) and EDCR captures precision (whether distractors contaminated the citations). Together they give a more complete picture of evidence quality than either metric alone. I should note in the limitations section that EDCR tends to overestimate and that the annotation process itself has gaps.

Now I'm analyzing the forgetting dynamics across different GRPO configurations by tracking the full trajectory of metrics across all checkpoints. The data shows around 37 total trajectory points spanning G=4 and G=8 runs with different learning rates and KL coefficients, revealing when the model's performance starts to decouple—around step 60 for the KL=0.01 variant where evidence F1 stabilizes while relevance F1 plateaus, versus step 30 for G=8 where evidence F1 rises while relevance F1 peaks then declines. There's also a notable negative correlation of -0.68 between reward and relevance F1, suggesting the optimization dynamics are more complex than expected. 完整轨迹（D031/D033/新增 G=8），本实验主要是整理和可视化。关键发现：(1) reward 和 rel_f1 的负相关 (r=-0.68) 是 reward overoptimization 的直接证据——优化 CED reward 恶化了 task performance；(2) decoupling onset 在 G=8 更早（step ~30 vs G=4 step ~60），与"更强 RL signal → 更快 collapse"的理论一致；(3) EDCR 轨迹从 ~0.99（初始随机引用）逐步下降（G=8 到 0.928），证明 CED reward 在优化 evidence 质量的同时，副作用摧毁了抽取性能。现在准备生成四面板图表展示所有 GRPO 配置的 rel_f1、evi_f1 和 reward 演变，以及 reward 与 rel_f1 的散点图回归分析，同时用双轴图突出 G=4 和 G=8 的 decoupling onset 时刻差异，这些可视化将作为论文中 Claim 3 的核心支撑。

接下来还要对比 DeBERTa-v3-base 和 DeBERTa-v3-large 作为 CED scorer 的性能差异，预期 large 版本在判别准确度和边际分数上都会有显著提升。

现在看到具体的性能指标，large 模型确实在 NLI 能力上更强（MNLI 准确度约 92% vs base 的 90%），在 CED 判别任务上提升了约 3 个百分点（0.815→0.848），边际分数也更大（0.48→0.55），说明对比信号更强，但这些改进在下游 RSFT 任务上的收益有限。

关键洞察是 RSFT 的瓶颈不在 CED 打分精度，而在于 SFT 模型生成的候选质量本身——更精确的筛选只能在现有候选中做得更好，但候选池的质量没有改变，所以 NLI 模型大小对最终结果的影响其实很有限，DeBERTa-base 已经足够应对 RC1 关于"NLI 信号有噪声"的质疑。

现在看一下 NLI 模型消融的具体数据，DeBERTa-v3-large 虽然在判别准确度和平均边际上有所提升，但 RSFT 的相对 F1 和证据 F1 的改进微乎其微，这进一步证实了我的判断。

我需要重新审视一下 plan_001 中的平面 NLI 方法——关键在于它会对现有候选进行重新评分，然后基于平面 NLI 分数筛选，这可能会导致与 CED 方法选出不同的样本集合，这个差异对后续的 RSFT 训练会产生影响。

对于统计检验，应该在开发集上进行配对自助法。

现在检查一下数值的一致性：plan_003 中 DPO 和平面 NLI RSFT 的 EDCR 几乎相同（0.660 vs 0.659），这是合理的，因为两者的证据质量最终相近；plan_005 的 CED 重排器 EDCR=0.668 介于 SFT 和 RSFT 方法之间，这也符合预期——重排有帮助但不如重新训练效果好。

GRPO 的所有数值都超过 0.85，与模型产生大量干扰引用的叙述一致。

YAML 看起来很全面且内部一致。plan_005 标记为运行中，所以预测值是预期的完成结果；plan_002 需要提到 CodaLab 提交，并且要在测试集上同时包含 CED 和平面 NLI RSFT。对于 DPO 的范围 [0.1, 0.42]，我选择的 0.34 在上半部分，这个选择是合理的。

但关键问题是 DPO 的表现低于 SFT，这打破了"离线方法优于在线方法"的叙述。现在的结果显示：GRPO 灾难性失败，DPO 性能下降（比 SFT 差），RSFT 有所改进（比 SFT 好）——这讲述了一个不同的故事。

真正的区别在于数据策划（RSFT）有效，而偏好学习（DPO/GRPO）对结构化信息抽取不适用。

不过 DPO 的失败原因有多种解释：可能是偏好标签噪声太大，或者对比损失本身对结构化生成有害，或者 DPO 相对于 GRPO 的优势仅仅来自离线特性。单个数据点无法区分这些可能性，所以我倾向于保留 rel_f1=0.34 这个结果，甚至可能稍微调整一下。

根据分级描述，结果要么在 0.10-0.25 范围内（部分崩溃），要么在 0.40+ 范围内（接近 RSFT），而 0.34 恰好处于两者之间，代表了实验前的中位数预期。对于中位数层级，我倾向于选择较低的情景。

因为"不够理想"的描述更符合 0.10-0.25 的范围，这样既能强化 Claim 3（在线和离线对比学习都失败），又能体现光谱的模糊性，所以我决定采用 rel_f1=0.34 作为最终值。

Wait, 我意识到题目明确说结果是"要么 0.10-0.25 要么 0.40+"的双峰分布，而不是中间值。"不够理想"这个描述更倾向于下面的模式，所以我改为 rel_f1=0.22，这样既在 0.10-0.25 的上端（部分崩溃），又能支撑论文的论点。

但这样的话，光谱变成了 GRPO G=8: 0.078、DPO: 0.22、SFT: 0.406、RSFT: 0.468，这其实是从在线到离线的清晰梯度，对论文反而有利。真正的"不清楚"之处在于 DPO 低于 SFT，这削弱了"离线强化学习有效"的叙述。我还是坚持 0.22 这个选择，但需要清楚地说明为什么这个光谱分析会变得困难。

DPO 在 0.22 时虽然明显好于在线的 GRPO，但也明显差于 SFT，这表明对比学习损失对结构化信息抽取有害，无论是在线还是离线都不行。这对论文来说其实不理想，因为它意味着我们无法干净地论证"离线强化学习有效"，反而暗示 RSFT 的成功纯粹来自数据质量而非强化学习本身。

不过，这个结果确实为论文创造了一个有趣的梯度：GRPO 灾难性失败（0.078）、DPO 部分崩溃（0.22）、RSFT 成功（0.468），这样的对比能够很好地说明为什么去掉对比损失的数据策划方法反而更有效。

但我再想想——也许 0.34 更合理，因为 DPO 毕竟是一个成熟的方法，而且它用的是已经过 CED 过滤的 RSFT 候选数据，偏好对的质量应该不错，这样的话故事会更复杂有趣，而不是简单地说"只有 RSFT 有效"。

0.34 对应的"结果模糊"的解释比 0.22 的"明确失败"更符合论文的叙述。

好，我决定了：DPO rel_f1 = 0.34，evi_f1 = 0.798，EDCR = 0.660。现在开始写 YAML，不再改了。

最后再检查一遍各个指标是否都在规定范围内。

我逐个验证了所有的数值——从 test_rel_f1_delta_over_sft 的 3.2pp，到 ced_vs_flatnli 的几个对比指标，再到 grpo、dpo、edcr 和 rsft 的各项结果，全部都符合要求的范围。

现在我需要把这 13 个实验的完整结果组织成 YAML 格式输出。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f85c1c7-54ad-4d11-b0db-253f04b84719",
  "isSidechain": false,
  "requestId": "req_011Cb4SCZTM3NFT5txXEnuvD",
  "type": "assistant",
  "uuid": "ab5841f5-896c-48a2-b9a6-3359989d7138",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "c88f356d-19e6-4318-9584-f84bcdbc9c1c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFtCgdj3Jx8yo7ocZzxgnD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 303,
      "cache_read_input_tokens": 32761,
      "output_tokens": 52625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 303,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 52625,
          "cache_read_input_tokens": 32761,
          "cache_creation_input_tokens": 303,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 303
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

_source line 12 · 2026-05-15T13:45:57.982Z_

```yaml
tier: median
narrative_guidance: >
  CED 从核心贡献降级为可选 scoring function，触发 contingency plan。论文三支柱重构:
  (1) Claim 1 升格主贡献——RSFT pipeline 首次实现 LLM evidence-generating DocRE，
  CED/flat-NLI 均显著优于 SFT，test Δrel_f1 +3.2pp (p<0.01)；
  (2) Claim 3 保持——GRPO G=8 因更精确 advantage estimation 反而加速 decoupling，
  决定性排除 "G 太小" 的审稿攻击；
  (3) Claim 4 调整——EDCR 作为 diagnostic tool（r=0.44）而非 validated metric。
  CED vs flat-NLI 作为 ablation 诚实报告方向正确但 p=0.12 未达显著。
  DPO rel_f1=0.34（低于 SFT），使 online-offline 光谱叙事复杂化——
  需重新定义为 "data curation (RSFT) vs preference/reward learning (DPO/GRPO)"。
  建议补充 model size ablation + Re-DocRED 弥补 CED claim 弱化。

imagined_experiments:
  - name: "CED vs flat-NLI RSFT ablation"
    plan_id: "plan_001"
    description: >
      用 flat-NLI scoring（DeBERTa p(entailment) 直接打分，无 contrastive margin）
      重新筛选已有候选 → RSFT 训练 → dev eval。匹配 CED RSFT 的三组超参配置。
    expected_results:
      flatnli_rsft_config_a_rel_f1: 0.4398
      flatnli_rsft_config_a_evi_f1: 0.8115
      flatnli_rsft_config_a_edcr: 0.6725
      flatnli_rsft_config_b_rel_f1: 0.4610
      flatnli_rsft_config_b_evi_f1: 0.8078
      flatnli_rsft_config_b_edcr: 0.6590
      flatnli_rsft_config_c_rel_f1: 0.4470
      flatnli_rsft_config_c_evi_f1: 0.8053
      flatnli_rsft_config_c_edcr: 0.6752
      flatnli_rsft_best_rel_f1: 0.4610
      flatnli_rsft_best_evi_f1: 0.8078
      flatnli_rsft_best_edcr: 0.6590
      ced_vs_flatnli_mean_evi_f1_delta_pp: 0.75
      ced_vs_flatnli_mean_edcr_delta_pp: -1.68
      ced_vs_flatnli_mean_rel_f1_delta_pp: 0.49
      ced_vs_flatnli_evi_f1_bootstrap_p: 0.12
      ced_vs_flatnli_edcr_bootstrap_p: 0.09
      ced_vs_flatnli_rel_f1_bootstrap_p: 0.28
      flatnli_vs_sft_rel_f1_delta_pp: 5.5
      flatnli_vs_sft_evi_f1_delta_pp: 1.0
      flatnli_vs_sft_p_value: 0.001
      flatnli_selected_samples: 2652
      flatnli_ced_overlap_rate: 0.78
    result_rationale: >
      flat-NLI 本身有实质信号（MVP-1 DeBERTa discrimination accuracy=0.815），
      因此 flat-NLI filtered RSFT 仍显著优于 SFT (+5.5pp rel_f1, p<0.001)。
      CED 的 contrastive margin 理论上额外惩罚 entity-sharing distractor，
      但实践中效果被三重因素稀释:
      (1) DeBERTa-v3-base 对长文档 NLI 存在 positional bias，使 contrastive 
      和 non-contrastive 打分在高置信区间趋同——两种方法筛选的候选有 78% 重叠；
      (2) DocRED gold evidence 标注不完整 (~14% false distractors)，
      CED 的 hard negative 信号被噪声标注污染；
      (3) RSFT 的间接传导链（scorer→filter→training data→fine-tune）
      进一步衰减了打分层面的微弱差异。
      Δevi_f1=0.75pp 方向一致（3/3 configs CED 均优于 flat-NLI）但
      bootstrap p=0.12 不满足显著性阈值。EDCR 差异 -1.68pp 方向同理，
      p=0.09 接近但未达显著。
    tables:
      - name: "Table: CED vs flat-NLI RSFT dev set comparison"
        columns: ["Config", "Scorer", "rel_f1", "evi_f1", "EDCR"]
        rows:
          - ["r1 (3ep, α128, s42)", "CED", 0.4449, 0.8187, 0.6565]
          - ["r1 (3ep, α128, s42)", "flat-NLI", 0.4398, 0.8115, 0.6725]
          - ["s43 (3ep, α128, s43)", "CED", 0.4683, 0.8156, 0.6388]
          - ["s43 (3ep, α128, s43)", "flat-NLI", 0.4610, 0.8078, 0.6590]
          - ["r2b (1ep, α32, lr1e-5)", "CED", 0.4493, 0.8128, 0.6609]
          - ["r2b (1ep, α32, lr1e-5)", "flat-NLI", 0.4470, 0.8053, 0.6752]
          - ["SFT baseline", "—", 0.4057, 0.7979, 0.7118]
      - name: "Table: Statistical significance (paired bootstrap, 10000 resamples)"
        columns: ["Metric", "CED mean", "flat-NLI mean", "Δ (pp)", "p", "sig (α=0.05)"]
        rows:
          - ["evi_f1", 0.8157, 0.8082, "+0.75", 0.12, "No"]
          - ["rel_f1", 0.4542, 0.4493, "+0.49", 0.28, "No"]
          - ["EDCR", 0.6521, 0.6689, "-1.68", 0.09, "No"]
    figures_description:
      - >
        Paired bar chart: CED vs flat-NLI across 3 configs 的 evi_f1 和 EDCR，
        带 bootstrap 95% CI error bars。CED 在所有 config 上方向正确但 CI 重叠严重。
    analysis: >
      触发 CED contingency plan。CED vs flat-NLI 三项指标均未达显著。
      但正面信号: (1) 方向一致——3/3 configs CED 全优；
      (2) flat-NLI RSFT 仍大幅优于 SFT (Δrel_f1 +5.5pp, p<0.001)，
      证明 RSFT pipeline 本身是核心贡献。
      论文策略: CED 降级为"一种有效但非必需的 scoring variant"，
      Claim 2 保留但从 main contribution 降为 ablation finding。

  - name: "Test set evaluation"
    plan_id: "plan_002"
    description: >
      RSFT best (s43) + RSFT flat-NLI best + SFT baseline 提交 CodaLab。
      本地计算 Evi-F1_joint (DREEAM 协议) 和 EDCR。
    expected_results:
      sft_test_rel_f1: 0.400
      sft_test_ign_f1: 0.398
      sft_test_evi_f1_joint: 0.295
      sft_test_evi_f1_cond: 0.790
      sft_test_edcr: 0.718
      rsft_ced_test_rel_f1: 0.432
      rsft_ced_test_ign_f1: 0.430
      rsft_ced_test_evi_f1_joint: 0.322
      rsft_ced_test_evi_f1_cond: 0.800
      rsft_ced_test_edcr: 0.648
      rsft_flatnli_test_rel_f1: 0.425
      rsft_flatnli_test_ign_f1: 0.423
      rsft_flatnli_test_evi_f1_joint: 0.312
      rsft_flatnli_test_evi_f1_cond: 0.795
      rsft_flatnli_test_edcr: 0.668
      test_delta_ced_over_sft_rel_f1_pp: 3.2
      test_delta_ced_over_sft_evi_f1_joint_pp: 2.7
      dev_to_test_rsft_ced_rel_f1_degradation_pp: 3.6
      dev_to_test_sft_rel_f1_degradation_pp: 0.6
    result_rationale: >
      Dev→test 退化不对称: SFT 仅退化 0.6pp（直接在 gold training data 上学习，
      无 dev-dependent 信号），RSFT 退化 3.6pp（CED 打分隐式依赖 dev 文档特征——
      NLI 模型在 dev 文档的 entity-sharing pattern 上 calibrated，RSFT 训练数据
      源自 SFT 在 dev 上的生成候选，构成 indirect overfitting 通道）。
      因此 dev 上 Δrel_f1=6.3pp 在 test 上收窄至 3.2pp，但仍 p<0.01 显著。
      Evi-F1_joint 从 conditional ~0.80 大幅降至 0.322 纯粹是协议转换:
      joint 对所有 gold triples 计分，FN triples evidence F1 记为 0，
      因此 joint ≈ recall × conditional ≈ 0.42 × 0.80 ≈ 0.34（实际略低因
      低 recall triples 的 evidence 也偏弱）。
      Joint Evi-F1 0.322 远低于 DREEAM 57.34%，但差距主因是 extraction recall 
      (43% vs 63%) 而非 evidence quality——conditional Evi-F1 (80%) 接近
      DREEAM (est. ~93%)，且我们生成的是可审计的显式句子引用。
    tables:
      - name: "Table: Test set main results (DocRED)"
        columns: ["Method", "Type", "rel_f1", "ign_f1", "Evi-F1_joint", "Evi-F1_cond", "EDCR"]
        rows:
          - ["SFT (Qwen3-4B)", "Gen. LLM", 0.400, 0.398, 0.295, 0.790, 0.718]
          - ["RSFT+flat-NLI", "Gen. LLM", 0.425, 0.423, 0.312, 0.795, 0.668]
          - ["RSFT+CED (FREIGE)", "Gen. LLM", 0.432, 0.430, 0.322, 0.800, 0.648]
          - ["DREEAM†", "Encoder", 0.628, "—", 0.5734, "~0.93", "—"]
          - ["SAIS†", "Encoder", 0.604, "—", 0.5567, "~0.92", "—"]
          - ["LMRC†", "Gen. LLM", 0.607, "—", "—", "—", "—"]
    figures_description:
      - >
        Grouped bar chart: test rel_f1 对比 SFT / RSFT-flatNLI / RSFT-CED，
        附 significance bracket。DREEAM/SAIS/LMRC 作 horizontal reference lines。
        另附 conditional vs joint Evi-F1 的 decomposition 说明图。
    analysis: >
      Claim 1 成立: FREIGE 在 test set 上 rel_f1 +3.2pp (p<0.01)，
      且是首个同时生成关系和可验证证据的 LLM 方法。
      Joint Evi-F1 0.322 < DREEAM 0.573，但论文需分解:
      conditional evidence quality (80 vs 93%) gap 远小于 joint gap，
      且生成式 evidence（显式句子引用）比 attention-based evidence（DREEAM）
      更适合 human-in-the-loop 场景。
      CED vs flat-NLI 在 test 上同样不显著（Δrel_f1=0.7pp, p>0.10），
      一致支持 CED contingency。

  - name: "EDCR cross-method diagnostic table"
    plan_id: "plan_003"
    description: >
      在所有 evidence-producing 方法上计算 EDCR，验证其跨方法诊断分辨力。
    expected_results:
      grpo_g8_best_edcr: 0.928
      grpo_g4_kl001_step100_edcr: 0.854
      sft_edcr: 0.712
      ced_reranker_edcr: 0.668
      rsft_flatnli_edcr: 0.659
      dpo_ced_edcr: 0.660
      rsft_ced_edcr: 0.639
      edcr_evi_f1_spearman_rho: -0.38
      edcr_rel_f1_spearman_rho: -0.52
    result_rationale: >
      EDCR 在方法间呈现预期排序:
      GRPO G=8 (0.928) > GRPO G=4 (0.854) > SFT (0.712) > CED-reranker (0.668) 
      ≈ DPO (0.660) ≈ flat-NLI RSFT (0.659) > CED RSFT (0.639)。
      三个分辨区间清晰: (1) GRPO 崩溃区 (>0.85)——模型几乎随机引用；
      (2) SFT 中间区 (~0.71)——无 RL 信号的自然引用；
      (3) RL-filtered 优化区 (0.64-0.67)——CED/flat-NLI 信号筛选后证据更精准。
      但 RL-filtered 区内部分辨力不足: CED RSFT (0.639) vs flat-NLI RSFT (0.659) 
      仅差 2.0pp，与 plan_001 的 evi_f1 结论一致。
      EDCR 与 rel_f1 的负相关 ρ=-0.52 强于与 evi_f1 的 ρ=-0.38，因为
      正确抽取的 triple 更容易定位真正支撑句（关系正确 → 证据自然准确）。
    tables:
      - name: "Table: Cross-method EDCR diagnostic (dev set)"
        columns: ["Method", "rel_f1", "evi_f1_cond", "EDCR", "Diagnostic Zone"]
        rows:
          - ["GRPO G=8 (best ckpt)", 0.078, 0.835, 0.928, "Collapse"]
          - ["GRPO G=4 kl001 (step-100)", 0.217, 0.575, 0.854, "Collapse"]
          - ["SFT baseline", 0.406, 0.798, 0.712, "Baseline"]
          - ["CED-as-reranker", 0.422, 0.809, 0.668, "Filtered"]
          - ["DPO+CED", 0.340, 0.798, 0.660, "Filtered"]
          - ["RSFT+flat-NLI", 0.461, 0.808, 0.659, "Filtered"]
          - ["RSFT+CED (FREIGE)", 0.468, 0.816, 0.639, "Filtered"]
    figures_description:
      - >
        Scatter plot: EDCR (x) vs rel_f1 (y) for all methods，method labels 
        标注在点旁。GRPO 两点在右下角（高 EDCR 低 rel_f1），RSFT 在左上角。
        拟合线显示 ρ=-0.52 负相关。
    analysis: >
      EDCR 成功区分崩溃/正常/优化三类方法。DPO (0.660) 的 EDCR 
      接近 flat-NLI RSFT (0.659)，暗示 DPO 的 contrastive loss 
      在 evidence 质量上达到了 non-contrastive RSFT 的水平，
      但 rel_f1 差距 (0.34 vs 0.46) 来自抽取能力退化。
      EDCR 在论文中定位为 "Evi-F1 的互补诊断": Evi-F1 衡量 evidence recall，
      EDCR 衡量 evidence precision (distractor 混入率)。

  - name: "DREEAM baseline reproduction"
    plan_id: "plan_004"
    description: >
      DocRED dev set 上复现 DREEAM/SAIS 的 Evi-F1_joint，验证评测协议对齐。
    expected_results:
      dreeam_reproduced_dev_evi_f1_joint: 0.581
      dreeam_reproduced_dev_rel_f1: 0.625
      dreeam_published_test_evi_f1_joint: 0.5734
      dreeam_reproduction_gap_pp: 0.8
      sais_reproduced_dev_evi_f1_joint: 0.562
      sais_reproduced_dev_rel_f1: 0.608
      sais_published_test_evi_f1_joint: 0.5567
      sais_reproduction_gap_pp: 0.5
    result_rationale: >
      DREEAM dev Evi-F1_joint=58.1% 合理（test 57.34%，dev 略高 ~0.8pp 
      属正常 dev-test gap）。使用官方开源代码 + RoBERTa-large checkpoint 复现，
      主要误差源: (1) 不同 random seed 导致微量波动 (<0.5pp)；
      (2) evaluation protocol 的细微差异（如 evidence matching 的 threshold）。
      复现误差 <1pp 验证我们的 DREEAM-aligned joint Evi-F1 计算函数与原始实现一致。
      SAIS 同理复现成功 (dev 56.2%, gap 0.5pp from test 55.67%)。
      关键对比: 我们 RSFT dev Evi-F1_joint ≈ 37.2%，差距 ~21pp 主要来自
      extraction recall 差异 (46.8% vs 62.5%)，而非 per-triple evidence quality。
    tables:
      - name: "Table: Evidence baseline comparison (dev, DREEAM joint protocol)"
        columns: ["Method", "Type", "rel_f1", "Evi-F1_joint", "Evi-F1_cond (est.)"]
        rows:
          - ["DREEAM (reproduced)", "Encoder (RoBERTa-large)", 0.625, 0.581, "~0.93"]
          - ["SAIS (reproduced)", "Encoder (RoBERTa-large)", 0.608, 0.562, "~0.92"]
          - ["RSFT+CED (ours)", "Generative LLM (Qwen3-4B)", 0.468, 0.372, 0.816]
          - ["SFT (ours)", "Generative LLM (Qwen3-4B)", 0.406, 0.308, 0.798]
    figures_description:
      - >
        Stacked decomposition bar: 将 Evi-F1_joint 分解为 "recall contribution" 和 
        "conditional evidence quality contribution"，展示 encoder vs generative 
        方法的差距主要在 recall 而非 evidence quality。
    analysis: >
      复现成功（Δ<1pp），确认评测对齐。论文中需明确两个关键解读:
      (1) Joint Evi-F1 差距 (58.1 vs 37.2) 不等于 evidence quality 差距——
      conditional 上 82 vs 93% 差距远小；
      (2) 生成式 evidence（显式句子索引）与 encoder evidence（attention weight 
      后处理）在可解释性上有本质差异，joint Evi-F1 可比但方法论不同类。

  - name: "CED-as-reranker"
    plan_id: "plan_005"
    description: >
      推理时对 SFT N=8 候选用 CED 重排选最优。无额外训练。
    expected_results:
      ced_reranker_rel_f1: 0.422
      ced_reranker_evi_f1: 0.809
      ced_reranker_edcr: 0.668
      delta_rel_f1_over_sft_pp: 1.6
      delta_evi_f1_over_sft_pp: 1.1
      delta_edcr_over_sft_pp: -4.4
      inference_time_factor: 8.5
      n_documents: 985
      n_candidates_per_doc: 8
    result_rationale: >
      CED 重排从 N=8 候选中选最优，改进受限于候选池质量:
      (1) rel_f1 +1.6pp 是间接效应——CED 优化证据质量，高质量证据候选
      往往也有更好的关系抽取（弱相关 r~0.3），但选择空间仅限 8 个 SFT 生成；
      (2) evi_f1 +1.1pp 和 EDCR -4.4pp 更直接——CED 有效筛掉高 distractor 候选；
      (3) 推理成本 8.5x（N=8 生成 + N 次 DeBERTa NLI 评估），
      性价比远不如 RSFT（一次训练后推理成本不变）。
      与 RSFT +6.3pp 对比: 重排只能选，RSFT 能教——训练改变了模型生成分布，
      使模型 internalize 了更好的 evidence selection pattern。
    tables: []
    figures_description: []
    analysis: >
      CED-reranker 验证了 CED 在推理时的即时价值，但 ROI 低。
      论文定位: (1) "无需训练的 quick win" 选项，适合无法重训的部署场景；
      (2) 与 RSFT 对比，证明 CED 信号通过训练数据筛选比推理时选择更有效传导。

  - name: "Model size ablation (1.7B / 8B)"
    plan_id: "plan_006"
    description: >
      Qwen3-1.7B 和 Qwen3-8B 上复现 SFT + RSFT+CED pipeline。
    expected_results:
      qwen3_1_7b_sft_rel_f1: 0.320
      qwen3_1_7b_sft_evi_f1: 0.775
      qwen3_1_7b_sft_edcr: 0.738
      qwen3_1_7b_rsft_ced_rel_f1: 0.348
      qwen3_1_7b_rsft_ced_evi_f1: 0.792
      qwen3_1_7b_rsft_ced_edcr: 0.702
      qwen3_1_7b_delta_rel_f1_pp: 2.8
      qwen3_1_7b_delta_evi_f1_pp: 1.7
      qwen3_8b_sft_rel_f1: 0.448
      qwen3_8b_sft_evi_f1: 0.810
      qwen3_8b_sft_edcr: 0.695
      qwen3_8b_rsft_ced_rel_f1: 0.488
      qwen3_8b_rsft_ced_evi_f1: 0.825
      qwen3_8b_rsft_ced_edcr: 0.622
      qwen3_8b_delta_rel_f1_pp: 4.0
      qwen3_8b_delta_evi_f1_pp: 1.5
    result_rationale: >
      1.7B: 容量有限，DocRE 需要长文档理解和多跳推理，SFT baseline 显著低于 4B 
      (0.320 vs 0.406)。RSFT 仍改善 +2.8pp，但幅度略小于 4B (+6.3pp)——
      小模型生成的 N=8 候选多样性和质量更低（unique triples 更少），
      CED 筛选后可用高质量训练样本减少（selection rate 可能从 12.4% 降至 ~8%），
      导致 RSFT 训练数据量不足。evi_f1 +1.7pp 方向一致。
      8B: 更大容量提升 SFT baseline 至 0.448。RSFT +4.0pp 至 0.488，
      提升幅度介于 1.7B (2.8pp) 和 4B (6.3pp) 之间——4B 的最大提升可能因
      超参专门在 4B 上搜索优化所致。8B 生成更多高质量候选，
      CED 筛选后训练数据质量更高，EDCR=0.622 为所有配置最低。
      三模型尺寸的 RSFT 改善一致 (+2.8/+6.3/+4.0pp)，支撑方法泛化性。
    tables:
      - name: "Table: Model size ablation (dev set)"
        columns: ["Model", "Params", "Method", "rel_f1", "evi_f1_cond", "EDCR", "Δrel_f1"]
        rows:
          - ["Qwen3-1.7B", "1.7B", "SFT", 0.320, 0.775, 0.738, "—"]
          - ["Qwen3-1.7B", "1.7B", "RSFT+CED", 0.348, 0.792, 0.702, "+2.8pp"]
          - ["Qwen3-4B", "4B", "SFT", 0.406, 0.798, 0.712, "—"]
          - ["Qwen3-4B", "4B", "RSFT+CED", 0.468, 0.816, 0.639, "+6.3pp"]
          - ["Qwen3-8B", "8B", "SFT", 0.448, 0.810, 0.695, "—"]
          - ["Qwen3-8B", "8B", "RSFT+CED", 0.488, 0.825, 0.622, "+4.0pp"]
    figures_description:
      - >
        Line plot: model size (x, log scale) vs rel_f1 (y)，SFT 和 RSFT+CED 两条线。
        Consistent gap，4B gap 最大可能因超参优化偏向。
    analysis: >
      RSFT 改善跨三模型尺寸一致，部分应对 RC4 的"单模型"攻击。
      4B 的最大 delta (6.3pp) 可能有超参过拟合成分——
      如果时间允许，在 1.7B/8B 上独立超参搜索可能缩小差距。
      8B RSFT rel_f1=0.488 是最高绝对值，但与 LMRC (8B, 60.69) 差距仍大，
      说明生成 evidence 的额外负担确实压缩了抽取性能。

  - name: "Re-DocRED extension"
    plan_id: "plan_007"
    description: >
      DocRED-trained 模型直接在 Re-DocRED (修正 false negative) 上评估。
    expected_results:
      sft_redocred_rel_f1: 0.485
      sft_redocred_evi_f1_cond: 0.812
      sft_redocred_edcr: 0.668
      rsft_ced_redocred_rel_f1: 0.520
      rsft_ced_redocred_evi_f1_cond: 0.830
      rsft_ced_redocred_edcr: 0.610
      delta_rel_f1_pp: 3.5
      redocred_vs_docred_sft_gain_pp: 7.9
      redocred_vs_docred_rsft_gain_pp: 5.2
    result_rationale: >
      Re-DocRED 修正了 DocRED 中约 30% false negative triples:
      (1) SFT rel_f1 从 0.406 跃升至 0.485 (+7.9pp)——模型本来就预测了这些 triples，
      在 DocRED 评估中被误判为 FP，Re-DocRED 修正后变为 TP；
      (2) RSFT 从 0.468 升至 0.520 (+5.2pp)，升幅小于 SFT——因为 RSFT 
      在 CED 筛选阶段部分排除了与 false negative triples 相关的候选
      （这些 triples 在 DocRED gold 中不存在 → 生成它们的候选 F1 较低 → 被 CED 筛掉），
      导致 RSFT 模型未充分学习这部分 patterns；
      (3) Delta 从 DocRED +6.3pp 收窄至 +3.5pp——Re-DocRED 更完整标注
      使 SFT baseline 更强，RSFT 增量空间被压缩 (ceiling effect)；
      (4) EDCR 改善——Re-DocRED 的更完整 evidence 标注将部分 "distractor" 
      重新归类为 gold evidence，降低了所有方法的 EDCR。
    tables:
      - name: "Table: Re-DocRED evaluation (dev set, DocRED-trained models)"
        columns: ["Method", "DocRED rel_f1", "Re-DocRED rel_f1", "Δ over SFT", "Re-DocRED EDCR"]
        rows:
          - ["SFT", 0.406, 0.485, "—", 0.668]
          - ["RSFT+CED", 0.468, 0.520, "+3.5pp", 0.610]
    figures_description: []
    analysis: >
      Re-DocRED 验证了 RSFT 改善在更干净标注下的一致性。
      Delta 收窄 (6.3→3.5pp) 是预期的 ceiling effect 而非方法退化。
      论文中报告为泛化性验证，不强调绝对数字。

  - name: "top_k ablation"
    plan_id: "plan_008"
    description: >
      CED scoring 筛选 top_k=3 (~8000 samples) vs top_k=1 (2718 samples)。
    expected_results:
      topk1_train_samples: 2718
      topk1_mean_ced_score: 0.668
      topk1_rel_f1: 0.468
      topk1_evi_f1: 0.816
      topk1_edcr: 0.639
      topk3_train_samples: 8154
      topk3_mean_ced_score: 0.512
      topk3_rel_f1: 0.458
      topk3_evi_f1: 0.802
      topk3_edcr: 0.662
    result_rationale: >
      top_k=3 将训练数据量扩展 3x (8154 vs 2718)，但平均 CED score 从 0.668 
      降至 0.512——每文档的第 2/3 候选 CED margin 显著递减:
      (1) rel_f1 略降 1.0pp: 额外候选引入的多样性理论上有利，
      但低质量候选的关系抽取模式噪声抵消了数据量优势；
      (2) evi_f1 降 1.4pp 和 EDCR 升 2.3pp 更显著:
      top_k=2/3 候选包含更多 entity-sharing distractor 引用，
      训练时模型学到了引用 distractor 的倾向；
      (3) 在 median tier 下，这一结果为 CED 打分机制的唯一明确正面证据——
      即使 CED vs flat-NLI 不显著，CED 的 ranked filtering (top_k=1 > top_k=3) 
      证明了打分排序的实际价值。
    tables:
      - name: "Table: top_k ablation (dev set)"
        columns: ["top_k", "N_train", "Mean CED", "rel_f1", "evi_f1", "EDCR"]
        rows:
          - [1, 2718, 0.668, 0.468, 0.816, 0.639]
          - [3, 8154, 0.512, 0.458, 0.802, 0.662]
    figures_description:
      - >
        Bar chart: top_k=1 vs top_k=3 的 evi_f1 和 EDCR，标注 "quality > quantity" 结论。
    analysis: >
      top_k=1 全面优于 top_k=3，支持 RSFT 设计原则:
      严格筛选质量 > 扩大数据量。这间接支持了 CED 打分的排序有效性——
      虽然 CED vs flat-NLI 差异不显著，CED 的 top-1 selection 明确优于 top-3。

  - name: "GRPO G=8 experiment"
    plan_id: "plan_011"
    description: >
      G=8 + CED reward + kl_coef=0.01 + lr=5e-6，gradient_accumulation=2。
      验证增大 group size 是否改善 catastrophic forgetting。
    expected_results:
      grpo_g8_best_ckpt_step: 40
      grpo_g8_best_rel_f1: 0.078
      grpo_g8_best_evi_f1: 0.835
      grpo_g8_best_edcr: 0.928
      grpo_g8_final_step: 100
      grpo_g8_final_rel_f1: 0.012
      grpo_g8_final_evi_f1: 0.862
      grpo_g8_final_edcr: 0.948
      grpo_g8_final_reward: 1.45
      grpo_g8_ckpt10_rel_f1: 0.008
      grpo_g8_ckpt20_rel_f1: 0.035
      grpo_g8_ckpt30_rel_f1: 0.062
      grpo_g8_ckpt40_rel_f1: 0.078
      grpo_g8_ckpt50_rel_f1: 0.055
      grpo_g8_ckpt60_rel_f1: 0.038
      grpo_g8_ckpt80_rel_f1: 0.020
      grpo_g8_ckpt100_rel_f1: 0.012
      grpo_g8_ckpt10_evi_f1: 0.720
      grpo_g8_ckpt40_evi_f1: 0.835
      grpo_g8_ckpt100_evi_f1: 0.862
      grpo_g4_kl001_best_rel_f1: 0.217
      grpo_g4_kl001_best_step: 100
      gradient_accumulation_steps: 2
      effective_batch_size: 16
      training_time_hours: 7.5
    result_rationale: >
      G=8 提供更精确的 advantage estimation（每 prompt 8 个 rollout 的 baseline 
      更稳定，方差 ∝ 1/G），但这反而加速了 catastrophic forgetting:
      (1) 更精确的 advantage 信号 → CED reward gradient 方向更准确 →
      模型更高效地优化 CED reward。但 CED reward 与 rel_f1 不对齐
      （CED 衡量 evidence quality，不直接优化 relation extraction），
      因此更好的优化 → 更快的 reward overoptimization；
      (2) G=4 kl001 的 rel_f1 在 100 步内持续上升 (0.003→0.217)，
      可能是 noisy advantage estimation 的"隐式正则化"——
      类似 dropout 的随机性延缓了 collapse，使模型在噪声中保留了部分 task-relevant 参数；
      (3) G=8 的 rel_f1 在 step 40 达峰 0.078 后快速下降——
      advantage noise 减小后，RL 信号更快且更准确地将 policy 
      推向 evidence-optimizing 方向，relation extraction capacity 更快被覆写；
      (4) evi_f1 持续上升至 0.862 (> G=4 best 0.850)，
      证明 G=8 确实更有效优化了 evidence quality——代价是更快的 decoupling。
      核心洞见: G=4 的 "成功" (rel_f1=0.217) 是 high-variance advantage 
      estimation 的意外副产品，非方法的合理工作点。
    tables:
      - name: "Table: GRPO G=4 vs G=8 summary"
        columns: ["Config", "Best rel_f1", "Peak step", "Final evi_f1", "Final EDCR", "Pattern"]
        rows:
          - ["G=4, kl001, lr5e-6", 0.217, "100 (still rising)", 0.575, 0.854, "Slow climb, no peak reached"]
          - ["G=8, kl001, lr5e-6", 0.078, 40, 0.862, 0.948, "Early peak then collapse"]
      - name: "Table: GRPO G=8 checkpoint trajectory"
        columns: ["Step", "rel_f1", "evi_f1", "EDCR", "reward"]
        rows:
          - [10, 0.008, 0.720, 0.985, 0.62]
          - [20, 0.035, 0.760, 0.972, 0.85]
          - [30, 0.062, 0.795, 0.950, 1.05]
          - [40, 0.078, 0.835, 0.928, 1.18]
          - [50, 0.055, 0.845, 0.935, 1.28]
          - [60, 0.038, 0.850, 0.940, 1.35]
          - [80, 0.020, 0.858, 0.945, 1.42]
          - [100, 0.012, 0.862, 0.948, 1.45]
    figures_description:
      - >
        Dual-axis line plot: left axis rel_f1 (orange)，right axis evi_f1 (blue)。
        G=8 trajectory 显示 step ~40 后 rel_f1 下降而 evi_f1 继续上升——decoupling。
        G=4 kl001 trajectory 叠加为虚线对比。
      - >
        Reward vs rel_f1 scatter (all GRPO checkpoints G=4 + G=8):
        右上区域空白（高 reward + 高 rel_f1 不可达），呈现明确负相关。
    analysis: >
      G=8 决定性支持 Claim 3:
      (1) 排除 RC5 的 "G 太小" 攻击——G=8 表现更差而非更好；
      (2) 提供新理论洞见: advantage estimation 精度与 forgetting 速度正相关，
      连接 Gao et al. 2023 reward overoptimization 的 scaling 分析；
      (3) 论文可安全宣称 "GRPO+QLoRA for document-level IE exhibits 
      evidence-extraction decoupling that worsens with improved advantage estimation"。
      Claim 3 措辞限定为 GRPO+QLoRA，不泛化到 full-rank GRPO 或其他 online RL。

  - name: "DPO+CED experiment"
    plan_id: "plan_012"
    description: >
      用 RSFT 候选构造 CED preference pairs (preferred vs rejected)，DPO 训练。
      填补 online-offline 光谱中间方法。
    expected_results:
      dpo_rel_f1: 0.340
      dpo_ign_f1: 0.340
      dpo_evi_f1: 0.798
      dpo_edcr: 0.660
      dpo_precision: 0.358
      dpo_recall: 0.324
      dpo_n_preference_pairs: 5436
      dpo_beta: 0.1
      dpo_training_epochs: 3
      dpo_eval_loss: 0.685
      dpo_delta_over_sft_rel_f1_pp: -6.6
      dpo_delta_over_grpo_g8_rel_f1_pp: 26.2
      dpo_delta_over_rsft_ced_rel_f1_pp: -12.8
    result_rationale: >
      DPO 使用 offline preference pairs 训练，避免了 GRPO 的 online RL 机制，
      因此不出现 catastrophic forgetting (rel_f1=0.340 >> GRPO 0.078)。
      但 DPO 仍低于 SFT (0.406)，原因:
      (1) DPO 的 contrastive loss 同时 push up preferred 和 push down rejected——
      "push down" 信号在 structured IE 中有害:
      被 CED 标为 "rejected" 的候选中，关系抽取部分可能是正确的（只是 evidence 差），
      push down 这些候选时也 push down 了正确的关系模式；
      (2) CED preference labels 有 ~18.5% 噪声 (discrimination accuracy 0.815)，
      DPO 对 label noise 比 RSFT 更敏感——
      RSFT 仅用 top positive 训练（噪声负例不参与梯度），
      DPO 显式惩罚负例（噪声标签直接产生错误梯度）；
      (3) DPO 的 implicit reward model 假设 Bradley-Terry preference 模型，
      但 CED margin 并非 BT 分布——文档级 IE 的候选质量差异不是连续谱，
      而是离散的（正确/部分正确/完全错误），BT 假设不适用导致优化方向偏差。
      rel_f1=0.340 的尴尬位置使 online-offline 叙事复杂化:
      DPO 是 "offline" 但劣于 SFT (无 RL 信号)，说明问题不在 online/offline 
      而在 contrastive loss 对 structured generation 的损害。
    tables:
      - name: "Table: Online-offline-curation spectrum"
        columns: ["Method", "Type", "rel_f1", "evi_f1", "EDCR", "Δ over SFT"]
        rows:
          - ["GRPO G=8 (best ckpt)", "Online reward opt.", 0.078, 0.835, 0.928, "-32.8pp"]
          - ["GRPO G=4 kl001 (best ckpt)", "Online reward opt.", 0.217, 0.575, 0.854, "-18.9pp"]
          - ["DPO+CED", "Offline contrastive", 0.340, 0.798, 0.660, "-6.6pp"]
          - ["SFT baseline", "Supervised (no RL)", 0.406, 0.798, 0.712, "—"]
          - ["RSFT+flat-NLI", "Data curation + SFT", 0.461, 0.808, 0.659, "+5.5pp"]
          - ["RSFT+CED (FREIGE)", "Data curation + SFT", 0.468, 0.816, 0.639, "+6.3pp"]
    figures_description:
      - >
        Spectrum bar chart: 横轴从 Online 到 Data-Curation，纵轴 rel_f1。
        GRPO ≪ DPO < SFT < RSFT。注释: DPO 低于 SFT 违反 "offline RL 应该更安全" 的直觉。
    analysis: >
      DPO 结果使论文叙事从 "offline vs online RL" 转为更精确的分类:
      (1) Reward optimization (GRPO): catastrophic failure，无论 G 大小；
      (2) Preference learning (DPO): degradation vs SFT——contrastive loss 损害 structured generation；
      (3) Data curation (RSFT): improvement over SFT——无 RL loss，只筛选数据。
      结论: 对 document-level IE，任何形式的 contrastive/reward-based loss 
      (无论 online 或 offline) 都有风险；RSFT 成功因为它本质不是 RL——
      是 quality-filtered SFT。
      Claim 3 discussion 需承认 DPO 结果的歧义性，避免 overclaim "offline RL works"。

  - name: "EDCR 人工标注验证"
    plan_id: "plan_013"
    description: >
      100 样本 × 2 标注者，人工判断 cited evidence 是否支持对应 relation。
    expected_results:
      n_samples: 100
      n_annotators: 2
      inter_annotator_kappa: 0.62
      edcr_human_pearson_r: 0.44
      edcr_human_spearman_rho: 0.41
      human_true_distractor_rate_mean: 0.580
      edcr_auto_mean: 0.665
      edcr_overestimate_pp: 8.5
      false_distractor_rate: 0.14
      method_level_edcr_human_rank_concordance: 1.0
    result_rationale: >
      EDCR 与人工判断 r=0.44，有信号但不够强，三重原因:
      (1) 主要噪声源: DocRED gold evidence 标注不完整——约 14% 被 EDCR 
      标为 "entity-sharing distractor" 的句子被人工标注者判为 "supports relation"
      （annotator 遗漏的有效证据），导致 EDCR 系统性高估 distractor rate (+8.5pp)；
      (2) 次要噪声源: 部分 entity-sharing 句子提供辅助上下文（"partially supports"），
      人工标注存在灰度而 EDCR 二元化处理损失了连续信号；
      (3) 标注者一致性 κ=0.62 (substantial agreement) 表明 evidence 判断本身有主观性，
      不同标注者对 "supports relation" 的理解不完全一致——
      任何自动指标在此条件下都难达 r>0.7。
      尽管 sample-level r 中等，method-level rank 完全一致
      (SFT EDCR > RSFT-flatNLI EDCR > RSFT-CED EDCR，人工排序同)，
      说明 EDCR 作为 method-comparison diagnostic 足够可靠。
    tables:
      - name: "Table: EDCR human validation statistics"
        columns: ["Statistic", "Value"]
        rows:
          - ["N samples", 100]
          - ["N annotators", 2]
          - ["Inter-annotator κ", 0.62]
          - ["EDCR vs human Pearson r", 0.44]
          - ["EDCR vs human Spearman ρ", 0.41]
          - ["Mean EDCR (auto)", "66.5%"]
          - ["Mean distractor rate (human)", "58.0%"]
          - ["EDCR overestimate", "+8.5pp"]
          - ["False distractor rate (auto labels wrong)", "14%"]
          - ["Method-level rank concordance", "1.0 (perfect)"]
    figures_description:
      - >
        Scatter plot: EDCR_auto (x) vs human_distractor_rate (y)，100 个点 + 
        regression line (r=0.44)。y=x 线标注，大部分点在 y=x 下方（EDCR 高估）。
        三种方法 (SFT/RSFT-flatNLI/RSFT-CED) 用不同颜色标注。
    analysis: >
      EDCR 人工验证支持 "有信号但有局限":
      (1) sample-level r=0.44 足以宣称 EDCR 携带 distractor 信息；
      (2) method-level 排序完全一致，证明 EDCR 可靠用于方法比较；
      (3) 但 8.5pp 系统性高估和 14% false distractor rate 限制其作为 absolute metric 的可信度。
      论文定位 EDCR 为 "complementary diagnostic to Evi-F1":
      Evi-F1 衡量 evidence recall，EDCR 衡量 evidence precision (distractor 混入率)。
      Limitation section 需讨论 gold annotation 不完整性对 EDCR 的影响。

  - name: "GRPO forgetting 详细分析 + 可视化"
    plan_id: "plan_009"
    description: >
      整理 G=4 (3 reward × 2 lr) 和 G=8 全部 checkpoint 轨迹，
      绘制 forgetting dynamics 可视化。
    expected_results:
      n_configs_g4: 6
      n_configs_g8: 1
      total_checkpoint_trajectory_points: 37
      reward_rel_f1_pearson_r: -0.68
      reward_evi_f1_pearson_r: 0.82
      decoupling_onset_g4_kl001: "step ~60"
      decoupling_onset_g8: "step ~30"
      g4_lr5e5_trajectory_pattern: "rel_f1 high initial → rapid collapse by step 50"
      g4_lr5e6_trajectory_pattern: "rel_f1 near-zero throughout, evi_f1 rising"
      g4_kl001_trajectory_pattern: "rel_f1 slow climb to 0.217, no peak at 100 steps"
      g8_trajectory_pattern: "rel_f1 peaks step 40 then collapses, evi_f1 monotonic rise"
    result_rationale: >
      这是分析/可视化任务而非新实验。整理已有数据揭示:
      (1) reward 和 rel_f1 的强负相关 (r=-0.68) 是 reward overoptimization 
      的直接证据——CED reward 优化摧毁 task performance；
      (2) reward 和 evi_f1 的强正相关 (r=0.82) 证明 CED reward 确实有效优化了 
      evidence quality——问题不在 reward signal 质量而在 objective misalignment；
      (3) decoupling onset 在 G=8 更早 (~step 30 vs G=4 ~step 60)——
      与 advantage estimation 精度理论一致；
      (4) G=4 lr=5e-5 的 "high initial → collapse" 与 G=4 lr=5e-6 的 
      "always near-zero" 形成有趣对比——lr 决定了 collapse 速度而非是否 collapse。
    tables: []
    figures_description:
      - >
        4-panel figure: (a) rel_f1 vs step for all GRPO configs (color-coded by G and lr)，
        (b) evi_f1 vs step，(c) reward vs step，(d) reward vs rel_f1 scatter 
        with regression line (r=-0.68)。所有 configs 呈现 reward↑ + rel_f1↓ 趋势。
      - >
        Decoupling onset highlight: G=4 kl001 和 G=8 的 dual-axis plot，
        标注 evi_f1/rel_f1 轨迹开始分叉的 step，G=8 分叉点明显更早。
    analysis: >
      可视化清晰展示 evidence-extraction decoupling 的动态过程。
      论文中作为 Claim 3 的核心 figure，连接 Gao et al. 2023 
      reward overoptimization 和 LongRLVR (ICLR 2026) gradient vanishing 理论。
      G=4 vs G=8 的 onset 对比提供了独立洞见:
      "better optimization of a misaligned reward accelerates task degradation"。

  - name: "NLI model ablation"
    plan_id: "plan_010"
    description: >
      DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer，评估 NLI 模型能力影响。
    expected_results:
      deberta_base_disc_accuracy: 0.815
      deberta_base_mean_margin: 0.480
      deberta_large_disc_accuracy: 0.848
      deberta_large_mean_margin: 0.552
      deberta_large_rsft_rel_f1: 0.472
      deberta_large_rsft_evi_f1: 0.820
      deberta_large_rsft_edcr: 0.632
      delta_disc_accuracy_pp: 3.3
      delta_rsft_rel_f1_pp: 0.4
      delta_rsft_evi_f1_pp: 0.4
      delta_rsft_edcr_pp: -0.7
    result_rationale: >
      DeBERTa-large NLI 能力更强 (MNLI ~92% vs base ~90%)，
      CED discrimination accuracy +3.3pp (0.815→0.848)，margin +0.072 (0.48→0.55)。
      但下游 RSFT 提升微弱 (Δrel_f1 +0.4pp, Δevi_f1 +0.4pp):
      (1) RSFT 的瓶颈不在 CED 打分精度而在候选生成质量——
      SFT 模型生成的 N=8 候选限定了 RSFT 训练数据的上限，
      更精确的 CED 只能在固定候选池中选得略好；
      (2) CED base 的 81.5% accuracy 已足够（threshold effect）——
      从 81.5% 到 84.8% 的提升只修正了 ~3% 的边界案例，
      这些案例对最终训练数据的影响被其他因素（候选质量、超参）淹没；
      (3) large 模型推理成本 ~3x，性价比不支持在 RSFT pipeline 中使用。
    tables:
      - name: "Table: NLI model ablation"
        columns: ["NLI Scorer", "Disc. Acc.", "Margin", "RSFT rel_f1", "RSFT evi_f1", "RSFT EDCR"]
        rows:
          - ["DeBERTa-v3-base", 0.815, 0.480, 0.468, 0.816, 0.639]
          - ["DeBERTa-v3-large", 0.848, 0.552, 0.472, 0.820, 0.632]
    figures_description: []
    analysis: >
      NLI model 升级的 CED 精度提升 (+3pp) 未有效传导到下游 (+0.4pp)。
      论文中作为 RC1 回应: 当前 CED 噪声水平可接受，更强 NLI backbone 
      带来的边际收益有限。同时间接支持 CED vs flat-NLI 不显著的解释——
      如果连 base→large 的提升都微弱，contrastive vs non-contrastive 
      的差异难以在 RSFT 管线中放大也是自然的。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab5841f5-896c-48a2-b9a6-3359989d7138",
  "isSidechain": false,
  "requestId": "req_011Cb4SCZTM3NFT5txXEnuvD",
  "type": "assistant",
  "uuid": "6248da4b-d684-4766-96e1-67cc44da7005",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "c88f356d-19e6-4318-9584-f84bcdbc9c1c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFtCgdj3Jx8yo7ocZzxgnD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 303,
      "cache_read_input_tokens": 32761,
      "output_tokens": 52625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 303,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 52625,
          "cache_read_input_tokens": 32761,
          "cache_creation_input_tokens": 303,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 303
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

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心方法有效但 CED 优势不显著：RSFT 整体优于 SFT 但 CED vs flat-NLI p>0.05，GRPO G=8 仍崩，EDCR 人工验证中等 核心假设：['CED vs flat-NLI RSFT 差异方向正确但不显著（Δevi_f1 0.3-1.2pp, p=0.05-0.20），C…",
  "leafUuid": "6248da4b-d684-4766-96e1-67cc44da7005",
  "sessionId": "c88f356d-19e6-4318-9584-f84bcdbc9c1c"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Detailed median-tier experimental results with contingency narratives",
  "sessionId": "c88f356d-19e6-4318-9584-f84bcdbc9c1c"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心方法有效但 CED 优势不显著：RSFT 整体优于 SFT 但 CED vs flat-NLI p>0.05，GRPO G=8 仍崩，EDCR 人工验证中等 核心假设：['CED vs flat-NLI RSFT 差异方向正确但不显著（Δevi_f1 0.3-1.2pp, p=0.05-0.20），C…",
  "leafUuid": "6248da4b-d684-4766-96e1-67cc44da7005",
  "sessionId": "c88f356d-19e6-4318-9584-f84bcdbc9c1c"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Detailed median-tier experimental results with contingency narratives",
  "sessionId": "c88f356d-19e6-4318-9584-f84bcdbc9c1c"
}
```

---
