# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：所有核心假设成立：CED 显著优于 flat-NLI，test set 保持 dev 增幅，GRPO G=8 仍崩，DPO 填补光谱，EDCR 人工验证

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-2/1195b561-7b7f-4d26-a2fc-6e549288e766.jsonl`
- **Structured JSON:** [`f47b5b215718a6dede67.json`](../../sessions/f4/f47b5b215718a6dede67.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T13:23:13.630Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T13:23:13.630Z",
  "sessionId": "1195b561-7b7f-4d26-a2fc-6e549288e766",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：所有核心假设成立：CED 显著优于 flat-NLI，test set 保持 dev 增幅，GRPO G=8 仍崩，DPO 填补光谱，EDCR 人工验证通过\n核心假设：['CED vs flat-NLI RSFT 在 evi_f1 和 EDCR 上均显著（p<0.01），对比性 margin 确实过滤了 distractor-heavy 候选', 'Test set rel_f1 Δ ≥ +3.5pp over SFT（dev→test 退化 ≤1.5pp），evi_f1_joint 在 DREEAM 对齐协议下仍优于 SFT', 'GRPO G=8 仍 catastrophic forgetting（rel_f1 < 0.05），排除 advantage estimation noise 作为 G=4 失败的混淆因素', 'DPO+CED 不崩但弱于 RSFT（rel_f1 0.25-0.38），形成 online→offline 清晰退化光谱', 'EDCR 与人工判断 Pearson r ≥ 0.55，验证其作为自动指标的有效性', 'DREEAM baseline 可复现（Evi-F1 ≈ 57.34），FREIGE 的 joint Evi-F1 在 LLM 方法中无可比对手']\n关键指标范围：{'test_rel_f1_delta_over_sft': [3.5, 6.5], 'ced_vs_flatnli_evi_f1_delta': [1.5, 3.0], 'ced_vs_flatnli_edcr_delta': [-8.0, -4.0], 'ced_vs_flatnli_p_value': [0.001, 0.01], 'grpo_g8_best_rel_f1': [0.0, 0.05], 'dpo_rel_f1': [0.25, 0.38], 'edcr_human_pearson_r': [0.55, 0.75], 'rsft_best_test_rel_f1': [0.43, 0.48], 'rsft_test_evi_f1_joint': [0.34, 0.42]}\n叙事方向：原始 framing 完全成立。四个 Claims 全部有强证据支撑： C1（首个同时生成抽取+证据的 LLM DocRE）有 test set 显著优势； C2（CED > flat-NLI）有统计显著性； C3（GRPO+QLoRA decoupling）有 G=4 和 G=8 双重验证 + DPO 中间点对比； C4（EDCR 指标）有人工标注背书。 论文可用完整的 \"problem → naive reward fails → online RL fails → CED+RSFT solves it\" story arc， 无需降级任何 claim。主表可展示完整的 online-offline 光谱（GRPO → DPO → RSFT）。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: faith-evidence-ie\nvenue: EMNLP 2026 Main\nfocus: D042 修正后 re-dream。关键变化: (1) Claim 3 缩窄为 GRPO+QLoRA 而非 online RL; (2) 新增 GRPO G=8 实验(plan_011); (3) 新增 DPO baseline(plan_012); (4) CED contingency plan(如 p>0.05 则降级); (5) Evi-F1 改为 DREEAM 对齐协议(joint); (6) 新增 EDCR 人工验证(plan_013)。请关注这些修改是否有效提升了论文质量。\n\n## paper_framing.md\n\n# Paper Framing — FREIGE\n\n> **状态**: POST-MVP (MVP-1 + MVP-2 均 PASS，进入 Research 阶段)\n> **最后更新**: 2026-05-15\n\n## Target Venue\n\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\n- Stretch: ARR May 25 (10 days, 极紧，仅在实验全部顺利时考虑)\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\n\n## Core Insight\n\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。朴素 NLI faithfulness reward 可被 entity-mentioning distractor 句子游戏——共享实体但不支持具体关系的句子仍获正面蕴含分数。\n\n**CED (Contrastive Evidence Discrimination)** 通过文档内 hard negative 对比，将 evidence 质量评估从\"是否蕴含\"升级为\"是否比最佳干扰句更蕴含\"——本质上是 evidence grounding 场景下的 **anti-reward-overoptimization mechanism**（连接 Gao et al. 2023 reward overoptimization 理论）。\n\n**MVP 关键发现**: CED 作为在线 RL (GRPO) reward 导致 catastrophic forgetting（3 种 reward type × 多个 lr 全线失败），但作为离线 RL (RSFT) 的候选筛选信号极其有效——4 组超参配置均稳定超过 SFT baseline。**方法论结论**: 对结构化 IE 任务，CED 应作为离线质量信号而非在线训练奖励。\n\n## Story Arc\n\n1. **Problem**: LLM DocRE 无证据 → 部署障碍（human-in-the-loop KB population、生物医学审计、RAG 溯源）\n2. **Why naive reward fails**: flat-NLI 被 entity-sharing distractors 欺骗（SFT EDCR=71.2%，大量引用干扰句）\n3. **Why online RL fails**: GRPO+CED/flat-NLI/extract-only 全部 catastrophic forgetting（reward ↑ + rel_f1 ↓ 至 <0.02）\n4. **Solution**: CED 作为离线质量信号 + RSFT（rejection sampling fine-tuning）：SFT 模型生成 N 候选 → CED 打分筛选 → 微调，规避在线 RL 的遗忘风险\n5. **Theoretical grounding**: 连接 LongRLVR (ICLR 2026) evidence grounding 梯度消失分析 + \"RSFT=PPO\" (ICML 2025) 等价性理论\n6. **Result**: 首个 LLM-based DocRE 方法同时生成抽取和可验证证据\n\n## Core Claims\n\n### Claim 1 (Main): CED-scored RSFT 使 LLM 同时生成抽取和忠实证据\n- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法\n- RSFT+CED: rel_f1 +3.9~6.0pp over SFT, evi_f1 +1.1~2.1pp, EDCR -4.8~7.7pp\n- **MVP-2 已验证**: 4/4 configs PASS\n- **Research 需要**: test set 评估，DREEAM/SAIS Evi-F1 直接对比\n\n### Claim 2 (Ablation): CED scoring 优于 flat-NLI scoring 用于 RSFT\n- CED-filtered RSFT vs flat-NLI-filtered RSFT 的 evi_f1 和 EDCR 差异\n- CED 的对比性 margin 过滤掉 distractor-heavy 候选\n- **Research 需要**: flat-NLI scored RSFT ablation（核心实验）\n- **⚠️ Dream 风险**: 三档 Dream 审稿均指出 CED vs flat-NLI 可能不显著（p>0.05）。**Contingency**: 如 plan_001 结果 p>0.05，降级 CED 为\"一种可选 scoring function\"而非核心贡献，论文主贡献重心转移到 Claim 1（首个 evidence-generating LLM for DocRE）和 Claim 3（decoupling phenomenon）\n\n### Claim 3 (Analysis): GRPO+QLoRA 在文档级 IE 上 catastrophic forgetting 且呈现 evidence-extraction decoupling\n- **范围限定**: 仅对 GRPO+QLoRA（非泛化到所有 online RL）——Dream 三档一致指出 overclaim 风险\n- GRPO+QLoRA 在 3 种 reward type × 多个 lr 下全线失败\n- **核心发现 (decoupling)**: evi_f1 在 GRPO 下提升至 0.850（>SFT 0.798）但 rel_f1 崩至 <0.02——RL 差异化优化了 evidence 但摧毁了 extraction\n- RSFT 规避此问题：不修改 policy gradient，只筛选训练数据\n- **MVP 已有完整证据**: D031/D033 GRPO 判死，D039 RSFT 成功\n- **⚠️ Dream 风险**: G=4 太小（标准 G=8-16），需测 G=8 排除 advantage estimation noise 的干扰；LoRA-only 是额外 confound\n\n### Claim 4 (Evaluation): EDCR 作为独立评估指标\n- EDCR = |entity-sharing non-gold cited sentences| / |total cited sentences|\n- Evi-F1 盲区：不惩罚 plausible-looking distractor citations\n- SFT EDCR=71.2%, RSFT+CED EDCR=63.5~66.4%（方向正确但差距有限，需坦诚讨论）\n- **Research 需要**: cross-method diagnostic table, CED vs flat-NLI EDCR 对比\n\n## MVP Evidence Summary\n\n| Config | rel_f1 | Δ rel_f1 | evi_f1 | EDCR | 状态 |\n|--------|--------|----------|--------|------|------|\n| SFT baseline | 0.4057 | — | 0.7979 | 0.7118 | ✅ |\n| RSFT r1 (3ep, α=128, s42) | 0.4449 | +3.92pp | 0.8187 | 0.6565 | ✅ |\n| RSFT r1 (s44) | 0.4655 | +5.98pp | 0.8087 | 0.6350 | ✅ |\n| RSFT r2a (1ep, α=128) | 0.4494 | +4.37pp | 0.8108 | 0.6641 | ✅ |\n| RSFT r2b (1ep, α=32, lr=1e-5) | 0.4493 | +4.36pp | 0.8128 | 0.6609 | ✅ |\n| GRPO best (lr=5e-5, ckpt-90) | 0.2110 | -19.5pp | 0.5750 | — | ❌ |\n| GRPO best (lr=5e-6, ckpt-100) | 0.0138 | -39.2pp | 0.8500 | 0.9900 | ❌ |\n\n## Anticipated Reviewer Concerns\n\n### RC1: NLI reward 信号质量（高概率攻击）\n- **攻击**: \"DeBERTa-v3-base 的 NLI 判断有 lexical overlap bias，CED 训练信号有噪声\"\n- **已验证**: MVP-1 Pearson r=0.34（NLI vs lexical overlap），远低于 0.7，证明非捷径\n- **Research 补充**: DeBERTa-base vs DeBERTa-large 对比\n\n### RC2: Gold evidence 标注不完整导致 false distractor\n- **攻击**: \"被标为 distractor 的句子可能是 annotator 遗漏的有效证据\"\n- **应对**: CED margin 的 self-correcting property——如果 false distractor 真正蕴含关系，其 p_neg 高 → margin 小 → 惩罚弱\n- **Research 补充**: false-distractor 鲁棒性量化分析\n\n### RC3: 评测可比性\n- **攻击**: \"生成式 evidence 如何与 DREEAM 的 attention-based evidence 做 apple-to-apple 对比？\"\n- **应对**: 模型输出显式句子索引 [S_i]，直接映射句子级 Evi-F1；辅助指标用 RoBERTa-large-MNLI（非训练用 DeBERTa）避免 circular evaluation\n\n### RC4: 单数据集 + 单模型泛化性\n- **攻击**: \"只在 DocRED + Qwen3-4B 上验证\"\n- **Research**: Re-DocRED 扩展 + Qwen3-1.7B/8B model size ablation\n\n### RC5: GRPO 配置可能不充分（Dream 三档一致）\n- **攻击**: \"G=4 太小（标准 G=8-16），LoRA-only 是 confound，可能是 GRPO+QLoRA 的问题而非 GRPO 本身\"\n- **应对**: (1) 加 G=8 实验验证（plan_011）；(2) 论文范围限定为 \"GRPO+QLoRA\" 而非 \"online RL\"；(3) 完整轨迹数据仍有效（3 reward × 2 lr × 全 checkpoint）\n- **Research**: GRPO G=8 实验 + 论文标题/claim 措辞调整\n\n### RC6: EDCR 63-66% 仍然偏高，CED 对证据精确度提升有限\n- **攻击**: \"RSFT+CED 的 EDCR 只比 SFT 低 5-8pp，证据质量提升不够显著\"\n- **应对**: (1) CED 在 RSFT 中是间接作用（筛选训练数据），非直接 reward；(2) CED-as-reranker 可能更直接降低 EDCR；(3) 需要 flat-NLI RSFT 对比证明 CED 方向正确\n- **Research**: CED reranker PoC（运行中），top_k ablation\n\n### RC7: 方法过于简单\n- **应对**: 简洁是优点——RSFT 方法论已被证明理论等价于 PPO (ICML 2025)，CED 创新在于打分函数设计而非框架复杂度\n\n### RC8: 缺少中间方法 baseline（Dream 两档一致 [M][W]）\n- **攻击**: \"GRPO(online) vs RSFT(offline) 缺少 DPO/KTO 等中间方法，无法定位失败边界\"\n- **应对**: 加 DPO+CED experiment（plan_012），至少一个中间方法填补 online-offline 光谱\n\n### RC9: EDCR 需要人工验证（Dream 两档一致 [M][W]）\n- **攻击**: \"EDCR 未经人工标注验证，与 Evi-F1 的弱相关 r=-0.42 无法区分信号与噪声\"\n- **应对**: 100 样本人工标注研究（plan_013），验证 EDCR 与人类判断的相关性\n\n### RC10: Evi-F1 评测协议不一致（D041 已确认）\n- **攻击**: \"你们的 Evi-F1 (conditional) 与 DREEAM (joint) 不可比\"\n- **已修复**: 实现 DREEAM 对齐评测函数，论文报告两种 Evi-F1（joint 为主，conditional 为辅）\n\n## Key Baselines (8+)\n\n1. **SFT-only**: Qwen3-4B + LoRA SFT on DocRED gold — 无 RL\n2. **RSFT flat-NLI**: flat-NLI scored RSFT — 无 contrastive signal（核心 ablation）\n3. **RSFT CED (FREIGE)**: CED scored RSFT — 主方法\n4. **CED-as-reranker**: 推理时 CED 重排 SFT 候选（无训练）— 运行中\n5. **GRPO+CED**: 在线 RL with CED reward — negative baseline\n6. **DREEAM**: RoBERTa-large encoder — evidence SOTA (Evi-F1 57.34)\n7. **SAIS**: RoBERTa encoder — evidence baseline (Evi-F1 55.67)\n8. **DocKS-RAG**: GNN+RAG — extraction SOTA (F1 63.59, 无 evidence)\n9. **LMRC**: LLaMA3.1-8B — generative LLM SOTA (F1 60.69, 无 evidence)\n\n## Publishability Threshold\n\n- **必要条件**: RSFT 在 test set 上 Evi-F1_joint（DREEAM 协议）> SFT baseline AND rel_f1 显著 > SFT baseline（D041: Evi-F1 对比 DREEAM 需用对齐协议，暂冻结绝对阈值）\n- **充分条件**: 上述 + CED vs flat-NLI RSFT 差异显著 + GRPO decoupling 分析完整 + EDCR 人工验证\n- **CED contingency**: 如 CED vs flat-NLI p>0.05 → 论文重心转为\"首个 evidence-generating LLM for DocRE + GRPO decoupling phenomenon + EDCR metric\"，CED 降为可选组件\n- **Failure pivot**: RSFT 在 test set 上无显著改进 → 转为 analysis contribution（GRPO failure analysis paper）\n\n## Research Phase Priorities\n\n| Priority | 实验 | Claim/RC | 预估 GPU-hours | Dream 驱动 |\n|----------|------|---------|---------------|-----------|\n| P0 | CED vs flat-NLI RSFT ablation | C2 | ~4h | ⚠️ 三档一致风险 |\n| P0 | Test set evaluation (RSFT best config) | C1 | ~4h | |\n| P0 | Evi-F1 DREEAM 协议对齐 + 重评 | RC10 | ~1h (CPU) | D041 |\n| P0 | EDCR pipeline 验证 + cross-method table | C4 | ~2h | |\n| P0 | DREEAM/SAIS Evi-F1 baseline reproduction | C1 | ~8h | |\n| P0 | GRPO G=8 实验 | C3/RC5 | ~8h | ⚠️ 三档一致 |\n| P1 | CED-as-reranker (running) | C1 bonus | ~6h | |\n| P1 | DPO+CED experiment | RC8 | ~12h | Dream [M][W] |\n| P1 | EDCR 人工标注验证 (100 samples) | RC9/C4 | ~0h (人工) | Dream [M][W] |\n| P1 | Model size ablation (1.7B/8B) | RC4 | ~24h | |\n| P1 | Re-DocRED extension | RC4 | ~12h | |\n| P1 | top_k ablation (k=1 vs k=3) | RC6 | ~8h | |\n| P2 | GRPO forgetting 详细分析 + 可视化 | C3 | ~4h | |\n| P2 | DeBERTa-base vs large NLI 对比 | RC1 | ~4h | |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选\n    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py\n    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set\n    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_003\n  claim: 4\n  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing\n    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_004\n  claim: 1\n  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)\n    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_005\n  claim: 1\n  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: mvp2_ced_reranker_poc\n  status: RUNNING\n- id: plan_006\n  claim: 1\n  description: 'Model size ablation: Qwen3-1.7B 和 Qwen3-8B 上复现 RSFT+CED pipeline，验证方法对模型规模的泛化性。应对\n    RC4。'\n  priority: P1\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Re-DocRED extension: 在 Re-DocRED（修正 false negative 标注的版本）上评估，验证 RSFT+CED\n    在更干净标注下的表现。应对 RC4。'\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  registry_id: null\n  status: planned\n- id: plan_008\n  claim: 2\n  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格\n    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_011\n  claim: 3\n  description: 'GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward\n    + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要\n    gradient_accumulation 适配显存。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_012\n  claim: 3\n  description: 'DPO+CED experiment: Dream [M][W] 指出缺少 online-offline 中间方法 baseline。用\n    RSFT 候选数据构造 preference pairs (CED-preferred vs CED-rejected)，DPO 训练。验证 DPO 是否避免\n    GRPO 的 catastrophic forgetting。'\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_013\n  claim: 4\n  description: 'EDCR 人工标注验证: 100 个样本，人工判断每个 cited evidence sentence 是否真正支持对应 relation。计算\n    EDCR 与人工判断的相关性，验证 EDCR 作为自动指标的有效性。Dream [M][W] 一致要求。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_009\n  claim: 3\n  description: 'GRPO forgetting 详细分析: 整理全部 GRPO checkpoint 的 rel_f1/evi_f1/EDCR 轨迹，绘制\n    forgetting dynamics 可视化（reward vs task performance 曲线），支撑 Claim 3 的论述。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer\n    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_mvp1\n  claim: 1\n  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing\n    distractor 的能力验证'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: mvp1_ced_signal\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_margin: 0.48\n    discrimination_accuracy: 0.815\n    pearson_r_margin_jaccard: 0.34\n    pass: true\n- id: plan_mvp2_sft\n  claim: 1\n  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mvp2_sft_warmup\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.72\n    accuracy: 0.835\n- id: plan_mvp2_rsft\n  claim: 1\n  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部\n    PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087,\n    r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_mvp1\n  - plan_mvp2_sft\n  registry_id: mvp2_rsft_train_r1\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.0483\n    num_preds: 848\n    sft_baseline_rel_f1: 0.4057\n    failure_mode: relation_ontology_collapse_to_freetext\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n- id: plan_mvp2_grpo\n  claim: 3\n  description: 'GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1\n    max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic\n    forgetting。D031/D033 完整轨迹支撑 Claim 3'\n  priority: P0\n  gpu_budget_hours: 60\n  deps:\n  - plan_mvp2_sft\n  registry_id: mvp2_grpo_ced_lr5e6_r1\n  status: DONE\n  conclusion: killed\n\n\n## registry (completed experiments)\n\n- exp_id: mvp1_ced_signal\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_margin: 0.48\n    discrimination_accuracy: 0.815\n    pearson_r_margin_jaccard: 0.34\n    pass: true\n- exp_id: smoke_test_grpo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_sft_warmup\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.72\n    accuracy: 0.835\n- exp_id: precompute_nli_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_grpo_ced\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_extract\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_sft_eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_extract_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: mvp2_grpo_extract_r3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_sft_eval_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    ign_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    precision: 0.4043\n    recall: 0.407\n    evi_precision: 0.8035\n    evi_recall: 0.7924\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.626\n    n_parseable: 617\n    n_truncated: 367\n    n_predictions: 18815\n    inference_time_seconds: 6484.7\n- exp_id: mvp2_sft_eval_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    ign_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    precision: 0.4043\n    recall: 0.407\n    evi_precision: 0.8035\n    evi_recall: 0.7924\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.626\n    n_parseable: 617\n    n_truncated: 367\n    n_predictions: 18815\n- exp_id: mvp2_grpo_ced_kl001_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001_r3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001_r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_step: 100\n    train_runtime_s: 9069.88\n    reward_final: 1.195\n    f1_reward_final: 0.573\n    ced_reward_final: 0.328\n    format_reward_final: 0.293\n    frac_zero_std_final: 0.2\n    kl_final: 0.118\n    loss_final: -0.009\n    grad_norm_final: 0.14\n    entropy_final: 0.067\n    completion_length_mean_final: 520.8\n    best_reward_step: 90\n    best_reward: 1.37\n    best_f1_reward: 0.72\n    best_ced_reward: 0.353\n- exp_id: mvp2_grpo_extract_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_early\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    f1: 0.1563\n    ign_f1: 0.1563\n    evi_f1: 0.5643\n    edcr: 0.8858\n    precision: 0.2356\n    recall: 0.1169\n    evi_precision: 0.4864\n    evi_recall: 0.6721\n    format_ok_rate: 0.999\n    n_parseable: 984\n    n_truncated: 11\n    n_predictions: 9250\n    tp: 1421\n    pred_count: 6032\n    gold_count: 12151\n- exp_id: mvp2_grpo_flatnli_r6\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    steps_completed: 25\n    final_frac_zero_std: 0.9\n    final_f1_reward: 0\n    final_flat_nli_reward: 0\n    final_format_reward: 0.293\n    collapse_step: 25\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.00296\n    rel_precision: 0.00314\n    rel_recall: 0.0028\n    evi_f1: 0.72\n    evi_precision: 0.6429\n    evi_recall: 0.8182\n    edcr: 0.9983\n    n_parseable: 984\n    n_truncated: 24\n    n_predictions: 11621\n    tp: 34\n    pred_count: 10839\n    gold_count: 12151\n    inference_time_seconds: 5211.4\n- exp_id: mvp2_eval_ced_kl001_r4_multi\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    checkpoint-10:\n      f1: 0.003\n      ign_f1: 0.003\n      evi_f1: 0.72\n      edcr: 0.9983\n      format_ok_rate: 0.999\n    checkpoint-20:\n      f1: 0.0088\n      ign_f1: 0.0088\n      evi_f1: 0.423\n      edcr: 0.9954\n      format_ok_rate: 0.999\n    checkpoint-30:\n      f1: 0.0338\n      ign_f1: 0.0338\n      evi_f1: 0.5889\n      edcr: 0.9798\n      format_ok_rate: 1\n    checkpoint-50:\n      f1: 0.1563\n      ign_f1: 0.1563\n      evi_f1: 0.5643\n      edcr: 0.8858\n      format_ok_rate: 0.999\n    checkpoint-60:\n      f1: 0.1467\n      ign_f1: 0.1467\n      evi_f1: 0.5763\n      edcr: 0.9062\n      format_ok_rate: 1\n    checkpoint-90:\n      f1: 0.2108\n      ign_f1: 0.2108\n      evi_f1: 0.5666\n      edcr: 0.8584\n      format_ok_rate: 1\n- exp_id: mvp2_eval_ced_kl001_r4_step100\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.2167\n    ign_f1: 0.2167\n    precision: 0.2849\n    recall: 0.1749\n    evi_f1: 0.5746\n    evi_precision: 0.5244\n    evi_recall: 0.6353\n    edcr: 0.8539\n    pred_count: 7460\n    gold_count: 12151\n    tp: 2125\n    n_truncated: 21\n    format_ok_rate: 1\n- exp_id: mvp2_eval_ced_kl001_r4_last\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt90\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_high\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    checkpoint_60:\n      rel_f1: 0.1467\n      ign_f1: 0.1467\n      precision: 0.1909\n      recall: 0.1192\n      evi_f1: 0.5763\n      edcr: 0.9062\n      pred_count: 10041\n      gold_count: 12151\n      n_truncated: 16\n      format_ok_rate: 1\n    note: Only ckpt-60 completed. Process died during ckpt-70 inference at 8% (5/62\n      batch). ckpt-80/90 never started.\n- exp_id: mvp2_eval_ced_kl001_r4_step90\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.2108\n    ign_f1: 0.2108\n    evi_f1: 0.5666\n    edcr: 0.8584\n    pred_count: 11160\n    n_truncated: 22\n    format_ok_rate: 1\n    n_documents: 985\n- exp_id: mvp2_grpo_ced_lr5e6_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_p1_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_rp_r1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt7080\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_rp_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt20\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0077\n    rel_precision: 0.0071\n    rel_recall: 0.0084\n    evi_f1: 0.628\n    evi_precision: 0.855\n    evi_recall: 0.496\n    edcr: 0.993\n    format_ok_rate: 0.991\n    field_compliance_rate: 0.399\n    pred_count: 14440\n    gold_count: 12151\n    tp: 102\n    n_truncated: 587\n    inference_time_seconds: 6370.4\n- exp_id: mvp2_eval_lr5e6_r1_ckpt40\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt40_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0071\n    precision: 0.0066\n    recall: 0.0078\n    evi_f1: 0.7584\n    evi_precision: 0.9113\n    evi_recall: 0.6494\n    edcr: 0.9942\n    format_ok_rate: 0.9939\n    field_compliance_rate: 0.5675\n    pred_count: 14434\n    gold_count: 12151\n    tp: 95\n    n_truncated: 424\n    inference_time_seconds: 6152\n- exp_id: mvp2_eval_lr5e6_rp_r2_ckpt20\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_sft_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    pred_count: 12234\n    gold_count: 12151\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.998\n    field_compliance_rate: 0.6264\n    n_truncated: 367\n    inference_time_seconds: 6138.5\n- exp_id: mvp2_eval_lr5e6_r1_ckpt60\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt80\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0116\n    ign_f1: 0.0116\n    precision: 0.0109\n    recall: 0.0124\n    evi_f1: 0.828\n    evi_precision: 0.928\n    evi_recall: 0.748\n    edcr: 0.993\n    format_ok_rate: 0.999\n    field_compliance_rate: 0.788\n    pred_count: 13828\n    gold_count: 12151\n    n_truncated: 210\n    inference_time_seconds: 6099\n- exp_id: mvp2_eval_lr5e6_r1_ckpt60_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0093\n    precision: 0.0085\n    recall: 0.0103\n    evi_f1: 0.81\n    edcr: 0.993\n    format_ok_rate: 0.998\n    pred_count: 14626\n    gold_count: 12151\n    tp: 125\n    inference_time_seconds: 6152\n- exp_id: mvp2_eval_lr5e6_r1_ckpt100\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0138\n    rel_precision: 0.0132\n    rel_recall: 0.0144\n    ign_f1: 0.0138\n    evi_f1: 0.8504\n    evi_precision: 0.9256\n    evi_recall: 0.7866\n    edcr: 0.9876\n    format_ok_rate: 0.999\n    field_compliance_rate: 0.8162\n    evidence_format_rate: 0.8162\n    tp: 175\n    pred_count: 13300\n    gold_count: 12151\n    n_predictions: 15498\n    n_truncated: 181\n    n_documents: 985\n    n_parseable: 984\n    inference_time_seconds: 5901.7\n- exp_id: mvp2_diversity_probe\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    unique_triples_t07: 5\n    unique_triples_t10: 8\n    jaccard_t07: 0.17\n    jaccard_t10: 0.051\n    format_ok_rate_t07: 0.5\n    format_ok_rate_t10: 0.438\n    n_samples: 3\n    n_generations: 8\n    note: 'unique_triples_t07 corrected from 7 to 5.0 (mean). Reviewer: format_ok\n      ~34% after fix, ''diversity'' was JSON key name variants not semantic diversity'\n- exp_id: mvp2_rsft_generate\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    generation_count: 5288\n    unique_docs: 659\n    format_compliance: 0.998\n    diversity_range: 7.5-7.8/8\n    exit_code: 0\n- exp_id: mvp2_rsft_ced_scoring\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    input_generations: 21952\n    selected_samples: 2718\n    unique_docs: 2691\n    selection_rate: 0.124\n    mean_f1: 0.6157\n    mean_ced: 0.6683\n    f1_range:\n    - 0.1026\n    - 1\n    zero_f1_samples: 0\n    selection_strategy: top_k=1\n    f1_threshold: 0.1\n- exp_id: mvp2_rsft_train_r1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.0483\n    num_preds: 848\n    sft_baseline_rel_f1: 0.4057\n    failure_mode: relation_ontology_collapse_to_freetext\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n- exp_id: mvp2_rsft_train_r1_s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.7622\n    train_loss: 0.6148\n    eval_entropy: 0.6724\n    mean_token_accuracy: 0.8291\n    total_steps: 510\n    epochs: 3\n    training_hours: 1.99\n- exp_id: mvp2_rsft_train_r1_s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4655\n    evi_f1: 0.8087\n    edcr: 0.635\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0598\n    delta_evi_f1: 0.0108\n    mvp2_pass: true\n- exp_id: mvp2_rsft_ced_scoring_topk3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_ced_reranker_poc\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_rsft_diagnosis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    root_cause: overfitting_plus_sft_knowledge_overwrite\n    truncated_json_samples: 170\n    truncated_pct: 6.3\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n    lora_scaling: 2\n    rsft_zero_relation_samples: 170\n    sft_zero_relation_docs: 26\n    rsft_mean_relations: 11.2\n    sft_mean_relations: 12.5\n- exp_id: mvp2_rsft_train_r2_fix\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_rsft_r2a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4494\n    evi_f1: 0.8108\n    edcr: 0.6641\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0437\n    delta_evi_f1: 0.0129\n    mvp2_pass: true\n- exp_id: mvp2_rsft_r2b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4493\n    evi_f1: 0.8128\n    edcr: 0.6609\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0436\n    delta_evi_f1: 0.0149\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4449\n    evi_f1: 0.8187\n    edcr: 0.6565\n    num_preds: 15307\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0392\n    delta_evi_f1: 0.0208\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r2a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4494\n    ign_f1: 0.4494\n    evi_f1: 0.8108\n    edcr: 0.6641\n    precision: 0.4512\n    recall: 0.4475\n    evi_precision: 0.8143\n    evi_recall: 0.8073\n    format_ok_rate: 1\n    n_predictions: 15482\n    n_truncated: 208\n    inference_time_s: 5967.2\n- exp_id: mvp2_eval_rsft_r2b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4493\n    ign_f1: 0.4493\n    evi_f1: 0.8128\n    edcr: 0.6609\n    precision: 0.4566\n    recall: 0.4424\n    evi_precision: 0.8201\n    evi_recall: 0.8056\n    pred_count: 14829\n    format_ok: 983/985\n    truncated: 179\n    inference_time_s: 5862\n- exp_id: mvp2_eval_rsft_s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_s43_r2\n  name: ''\n  status: ANALYZING\n  conclusion: success\n  metrics:\n    rel_f1: 0.4683\n    ign_f1: 0.4683\n    evi_f1: 0.8156\n    edcr: 0.6388\n    precision: 0.4817\n    recall: 0.4556\n    evi_precision: 0.8142\n    evi_recall: 0.817\n    n_predictions: 14970\n    n_truncated: 171\n    format_ok_rate: 1\n    inference_time_s: 6316.7\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0626\n    delta_evi_f1: 0.0177\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r2b_maxtok1536\n  name: ''\n  status: RUNNING\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_r2b_maxtok1536_r2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_rsft_ced_scoring_topk3_r2\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T13:23:13.633Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T13:23:13.633Z",
  "sessionId": "1195b561-7b7f-4d26-a2fc-6e549288e766"
}
```

---

## Round 1

14 recorded events

### User

_source line 3 · 2026-05-15T13:23:13.657Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：所有核心假设成立：CED 显著优于 flat-NLI，test set 保持 dev 增幅，GRPO G=8 仍崩，DPO 填补光谱，EDCR 人工验证通过
核心假设：['CED vs flat-NLI RSFT 在 evi_f1 和 EDCR 上均显著（p<0.01），对比性 margin 确实过滤了 distractor-heavy 候选', 'Test set rel_f1 Δ ≥ +3.5pp over SFT（dev→test 退化 ≤1.5pp），evi_f1_joint 在 DREEAM 对齐协议下仍优于 SFT', 'GRPO G=8 仍 catastrophic forgetting（rel_f1 < 0.05），排除 advantage estimation noise 作为 G=4 失败的混淆因素', 'DPO+CED 不崩但弱于 RSFT（rel_f1 0.25-0.38），形成 online→offline 清晰退化光谱', 'EDCR 与人工判断 Pearson r ≥ 0.55，验证其作为自动指标的有效性', 'DREEAM baseline 可复现（Evi-F1 ≈ 57.34），FREIGE 的 joint Evi-F1 在 LLM 方法中无可比对手']
关键指标范围：{'test_rel_f1_delta_over_sft': [3.5, 6.5], 'ced_vs_flatnli_evi_f1_delta': [1.5, 3.0], 'ced_vs_flatnli_edcr_delta': [-8.0, -4.0], 'ced_vs_flatnli_p_value': [0.001, 0.01], 'grpo_g8_best_rel_f1': [0.0, 0.05], 'dpo_rel_f1': [0.25, 0.38], 'edcr_human_pearson_r': [0.55, 0.75], 'rsft_best_test_rel_f1': [0.43, 0.48], 'rsft_test_evi_f1_joint': [0.34, 0.42]}
叙事方向：原始 framing 完全成立。四个 Claims 全部有强证据支撑： C1（首个同时生成抽取+证据的 LLM DocRE）有 test set 显著优势； C2（CED > flat-NLI）有统计显著性； C3（GRPO+QLoRA decoupling）有 G=4 和 G=8 双重验证 + DPO 中间点对比； C4（EDCR 指标）有人工标注背书。 论文可用完整的 "problem → naive reward fails → online RL fails → CED+RSFT solves it" story arc， 无需降级任何 claim。主表可展示完整的 online-offline 光谱（GRPO → DPO → RSFT）。


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
  "promptId": "c303e6ef-d38d-47df-aa86-f404d8143f89",
  "type": "user",
  "uuid": "009565d6-d1b2-4f58-9531-fdc087a6a7f6",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "1195b561-7b7f-4d26-a2fc-6e549288e766",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T13:23:13.656Z_

```json
{
  "parentUuid": "009565d6-d1b2-4f58-9531-fdc087a6a7f6",
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
  "uuid": "6b335223-4dc1-4a0c-ab49-be039306c1ad",
  "timestamp": "2026-05-15T13:23:13.656Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "1195b561-7b7f-4d26-a2fc-6e549288e766",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T13:23:13.656Z_

```json
{
  "parentUuid": "6b335223-4dc1-4a0c-ab49-be039306c1ad",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a4bd93df-8728-4fbe-95b1-d87c65a8f5d9",
  "timestamp": "2026-05-15T13:23:13.656Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "1195b561-7b7f-4d26-a2fc-6e549288e766",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有核心假设成立：CED 显著优于 flat-NLI，test set 保持 dev 增幅，GRPO G=8 仍崩，DPO 填补光谱，EDCR 人工验证通过 核心假设：['CED vs flat-NLI RSFT 在 evi_f1 和 EDCR 上均显著（p<0.01），对比性 margin 确实过滤了 di…",
  "leafUuid": "a4bd93df-8728-4fbe-95b1-d87c65a8f5d9",
  "sessionId": "1195b561-7b7f-4d26-a2fc-6e549288e766"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate FREIGE evidence-generation method on test set",
  "sessionId": "1195b561-7b7f-4d26-a2fc-6e549288e766"
}
```

---

### Assistant

_source line 8 · 2026-05-15T13:23:16.972Z_

Let me review the experiment plan and existing data to generate detailed predictions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4bd93df-8728-4fbe-95b1-d87c65a8f5d9",
  "isSidechain": false,
  "requestId": "req_011Cb4RhRHAEx3Ezzn5XwV3f",
  "type": "assistant",
  "uuid": "ef6a4c8b-5e46-4bc6-b686-771ef527b1c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "1195b561-7b7f-4d26-a2fc-6e549288e766",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dvs8vkVPiJFcyZTcajo1nL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20874,
      "cache_read_input_tokens": 11841,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20874,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 128,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20874
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

_source line 9 · 2026-05-15T13:23:18.542Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SwHoiH93K7LTAjjeCz8YgN`</summary>

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
  "parentUuid": "ef6a4c8b-5e46-4bc6-b686-771ef527b1c2",
  "isSidechain": false,
  "requestId": "req_011Cb4RhRHAEx3Ezzn5XwV3f",
  "type": "assistant",
  "uuid": "4a9d0ca6-9344-4e71-b4c8-ec33a3d916f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "1195b561-7b7f-4d26-a2fc-6e549288e766",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dvs8vkVPiJFcyZTcajo1nL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20874,
      "cache_read_input_tokens": 11841,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20874,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 128,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20874
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

_source line 10 · 2026-05-15T13:23:18.560Z_

<details><summary>↩ Tool result · `toolu_01SwHoiH93K7LTAjjeCz8YgN`</summary>

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
  "parentUuid": "4a9d0ca6-9344-4e71-b4c8-ec33a3d916f5",
  "isSidechain": false,
  "promptId": "c303e6ef-d38d-47df-aa86-f404d8143f89",
  "type": "user",
  "uuid": "8849db2f-3084-43bf-8ebd-12a746bf3d74",
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
  "sourceToolAssistantUUID": "4a9d0ca6-9344-4e71-b4c8-ec33a3d916f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "1195b561-7b7f-4d26-a2fc-6e549288e766",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-15T13:24:06.936Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predictions for each planned experiment in the experiment plan, under the "best" tier scenario. I need to carefully analyze each experiment and provide realistic numbers with rationales.

Let me go through each planned experiment:

1. **plan_001**: CED vs flat-NLI RSFT ablation (P0, Claim 2)
2. **plan_002**: Test set evaluation (P0, Claim 1)
3. **plan_003**: EDCR pipeline verification + cross-method table (P0, Claim 4)
4. **plan_004**: DREEAM baseline reproduction (P0, Claim 1)


5. **plan_005**: CED-as-reranker (P1, Claim 1) - RUNNING
6. **plan_006**: Model size ablation 1.7B/8B (P1, Claim 1)
7. **plan_007**: Re-DocRED extension (P1, Claim 1)
8. **plan_008**: top_k ablation (P1, Claim 2)
9. **plan_011**: GRPO G=8 experiment (P0, Claim 3)
10. **plan_012**: DPO+CED experiment (P1, Claim 3)
11. **plan_013**: ED with CR human annotation verification (P1, Claim 4)
12. **plan_009**: GRPO forgetting analysis (P2, Claim 3)
13. **plan_010**: NLI model ablation (P2, Claim 1)

Looking at the baseline metrics and RSFT results, I'm seeing consistent improvements in relation F1 across the variants, though evidence F1 gains are more modest and EDCR actually decreases compared to SFT.  The GRPO experiments show concerning performance drops—particularly the rel_f1 collapse at higher learning rates—while the metric deltas I'm tracking suggest the best improvements cluster around 3.5-6.5% gains over SFT baseline for relation F1 and 1.5-3.0% for evidence F1 against the flat NLI baseline.

Now I'm diving into the individual experiments to validate which ones actually hit these target ranges, starting with the CED versus flat-NLI RSFT ablation where the statistical significance is strong but I need to confirm the flat-NLI baseline would still underperform. beat SFT (since it's still doing rejection sampling with a quality signal), but the margin is smaller and evidence quality is worse.
- CED RSFT best: rel_f1 ~0.465, evi_f1 ~0.815, EDCR ~0.635
- flat-NLI RSFT: rel_f1 should be similar or slightly lower (because NLI scoring still filters bad candidates, but less effectively). Maybe rel_f1 ~0.435, evi_f1 ~0.795 (vs CED's 0.815, giving delta ~2.0pp), EDCR ~0.700 (vs CED's 0.635, giving delta ~-6.5pp)

Now looking at the test set evaluation, I'm expecting the best dev config to show a rel_f1 improvement of 3.5-6.5 percentage points over SFT, landing around 0.43-0.48 on the test set. The joint evidence F1 should be notably lower than the conditional version, somewhere in the 0.34-0.42 range, and I'm anticipating minimal degradation from dev to test—no more than 1.5 percentage points for relevance.

For the EDCR cross-method comparison, I'm collecting performance across different approaches: SFT baseline at 0.7118, RSFT with CED at 0.635 as the best performer, and RSFT with flat-NLI around 0.695.

For the CED-as-reranker approach, I'm applying CED scores directly at inference time to rerank SFT candidates, which should substantially boost evidence quality but likely won't move the needle much on relation F1 since we're just selecting better candidates rather than retraining—expecting rel_f1 around 0.41-0.42 and evi_f1 near 0.82.

Now I'm thinking through several ablations: testing smaller (1.7B) and larger (8B) model variants to see how capacity affects the gains from RSFT+CED, exploring whether the cleaner annotations in Re-DocRED preserve or amplify the improvements, and examining how different top_k values during candidate selection impact the final performance.

Looking at the top_k results, top_k=1 with 2718 samples achieves rel_f1=0.465 while top_k=3 pulls in more data but at lower quality, and the evidence suggests the filtering is genuinely quality-driven rather than just data-driven.

The GRPO experiments with G=8 still show catastrophic forgetting with rel_f1 below 0.05, ruling out that the failure was specific to G=4 being too small. Meanwhile, DPO+CED performs better than GRPO but still lags behind RSFT, sitting in the 0.25-0.38 range.

The EDCR human annotation validation shows strong Pearson correlation between 0.55-0.75, confirming the metric captures something meaningful. The visualization of GRPO's reward increasing while rel_f1 drops reveals the core decoupling problem, and the NLI ablation shows DeBERTa-base is sufficient since the larger variant only marginally improves CED scoring.

Now I'm organizing all these findings into a comprehensive YAML summary with detailed rationales for each experiment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8849db2f-3084-43bf-8ebd-12a746bf3d74",
  "isSidechain": false,
  "requestId": "req_011Cb4RhnYLx9wtvncEHhnr5",
  "type": "assistant",
  "uuid": "f94ddd1d-1654-41bb-8b6d-7ff72c9b3fce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "1195b561-7b7f-4d26-a2fc-6e549288e766",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xgdu7z6ahCumuaPqEUXESK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 300,
      "cache_read_input_tokens": 32715,
      "output_tokens": 21133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 300,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 21133,
          "cache_read_input_tokens": 32715,
          "cache_creation_input_tokens": 300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 300
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

_source line 12 · 2026-05-15T13:29:39.876Z_

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立。四个 Claims 全部有强证据支撑：
  C1（首个同时生成抽取+证据的 LLM DocRE）有 test set 显著优势；
  C2（CED > flat-NLI）有统计显著性；
  C3（GRPO+QLoRA decoupling）有 G=4 和 G=8 双重验证 + DPO 中间点对比；
  C4（EDCR 指标）有人工标注背书。
  论文可用完整的 "problem → naive reward fails → online RL fails → CED+RSFT solves it" story arc，
  无需降级任何 claim。主表可展示完整的 online-offline 光谱（GRPO → DPO → RSFT）。

imagined_experiments:
  # ===== P0 实验 =====

  - name: "CED vs flat-NLI RSFT ablation"
    plan_id: "plan_001"
    description: >
      用 flat-NLI scoring（DeBERTa NLI entailment score，无 contrastive margin）替代 CED 作为 RSFT 候选筛选信号。
      复用 mvp2_rsft_gen_s0~s3 已有的 21952 candidates，仅替换打分函数。
      flat-NLI score = mean entailment probability over cited sentences（无 hard-negative 对比）。
      选 top_k=1 per document，训练配置对齐 CED-RSFT 最优（s43: 3ep, α=128, seed=43；r2b: 1ep, α=32, lr=1e-5）。
      共训练 2 个 flat-NLI RSFT 配置，全量 dev eval。
    expected_results:
      # flat-NLI RSFT config A (3ep, α=128, s43)
      flatnli_rsft_a_rel_f1: 0.4412
      flatnli_rsft_a_evi_f1: 0.7948
      flatnli_rsft_a_edcr: 0.6952
      flatnli_rsft_a_n_selected: 2845
      # flat-NLI RSFT config B (1ep, α=32, lr=1e-5)
      flatnli_rsft_b_rel_f1: 0.4378
      flatnli_rsft_b_evi_f1: 0.7972
      flatnli_rsft_b_edcr: 0.6887
      # CED-RSFT best for reference (s43_r2)
      ced_rsft_best_rel_f1: 0.4683
      ced_rsft_best_evi_f1: 0.8156
      ced_rsft_best_edcr: 0.6388
      # deltas (CED - flatNLI, best vs best)
      delta_rel_f1: 0.0271  # +2.7pp
      delta_evi_f1: 0.0208  # +2.1pp — within [1.5, 3.0] range
      delta_edcr: -0.0564   # -5.6pp — within [-8.0, -4.0] range
      # paired bootstrap test (10000 resamples, per-document)
      paired_bootstrap_evi_f1_p: 0.0038
      paired_bootstrap_edcr_p: 0.0021
      paired_bootstrap_rel_f1_p: 0.0067
    result_rationale: >
      flat-NLI scoring 仍然能过滤掉完全无关的候选（如 format 错误、zero-F1 的），因此 flat-NLI RSFT 仍优于 SFT baseline（+3.2~3.6pp rel_f1）。
      但 flat-NLI 的核心缺陷在于：entity-sharing distractor sentences 的 NLI entailment score 往往偏高（因为共享实体提供了 lexical overlap），
      flat-NLI 无法区分"真正支持关系的证据句"和"仅提及相同实体的干扰句"。
      因此 flat-NLI 筛选出的 top-1 候选中会保留更多 distractor-heavy 样本——这些样本的 evidence 看起来"合理"（高 NLI score）
      但实际上引用了大量 entity-sharing non-gold sentences。
      CED 的 contrastive margin = p(entail|gold) - max(p(entail|distractor)) 直接惩罚这种模式，
      因此 CED-filtered 数据的训练样本 evidence 质量系统性更高。
      这导致 CED RSFT 在 evi_f1 上高出 ~2.1pp（因为训练数据中 evidence 更精确，模型学到更好的 evidence 引用模式），
      在 EDCR 上低 5.6pp（因为训练数据中 distractor citations 更少，模型被条件化为避免引用干扰句）。
      rel_f1 差异 +2.7pp 来自间接效应：CED 筛选出的候选不仅 evidence 更好，整体生成质量也更高（因为能正确定位 evidence 的生成通常也更准确地识别了关系）。
      p<0.01 的显著性来自两个因素：(1) dev set 有 985 docs 提供足够统计力，(2) CED vs flat-NLI 的差异是系统性的（几乎在每种关系类型上 CED 都更好），不是少数异常值驱动的。
      flat-NLI 选出 ~2845 样本（vs CED 2718），因为 flat-NLI 的筛选 landscape 不同（一些 CED 会拒绝的 distractor-heavy 候选在 flat-NLI 下得分高）。
    tables:
      - name: "Table: CED vs flat-NLI RSFT Ablation (dev set)"
        columns: ["Method", "rel_f1", "evi_f1", "EDCR", "n_train"]
        rows:
          - ["SFT baseline", 0.4057, 0.7979, 0.7118, "12151 (gold)"]
          - ["RSFT flat-NLI (A: 3ep, α=128)", 0.4412, 0.7948, 0.6952, 2845]
          - ["RSFT flat-NLI (B: 1ep, α=32)", 0.4378, 0.7972, 0.6887, 2845]
          - ["RSFT CED (s43: 3ep, α=128)", 0.4683, 0.8156, 0.6388, 2718]
          - ["RSFT CED (r2b: 1ep, α=32)", 0.4493, 0.8128, 0.6609, 2718]
          - ["Δ (CED best - flatNLI best)", "+2.71pp", "+2.08pp", "-5.64pp", "—"]
          - ["p-value (paired bootstrap)", 0.0067, 0.0038, 0.0021, "—"]
    figures_description:
      - "Scatter plot: per-document evi_f1 差异 (CED - flatNLI)，x 轴为 document 的 distractor density (entity-sharing non-gold sentences / total sentences)。预期高 distractor density 的文档差异更大，验证 CED 的机制假说。"
      - "Bar chart: 按 relation type frequency 分组的 evi_f1 对比（head/body/tail），验证 CED 在各频率段的一致优势。"
    analysis: >
      CED vs flat-NLI 的差异模式完美验证了核心假说：CED 的优势集中在 distractor-dense 文档上。
      在 distractor density > 0.4 的文档子集中，CED RSFT 的 evi_f1 优势扩大到 ~3.5pp，
      而在 distractor density < 0.2 的文档中差异缩小到 ~0.8pp（不显著）。
      这证明 CED 的 contrastive margin 确实在做它该做的事：区分 entity-sharing distractors 和真正的 evidence。
      EDCR 的差异更稳定（几乎所有子集都显著），因为 EDCR 直接测量 distractor citation rate，
      而 evi_f1 还受 recall 影响（有些 gold evidence 即使用 flat-NLI 也能被正确引用）。
      rel_f1 的差异虽然也显著，但这是 evidence 质量提升的 downstream 效应，而非 CED 的直接目标。

  - name: "Test set evaluation (RSFT best + SFT baseline)"
    plan_id: "plan_002"
    description: >
      用 RSFT best config (s43_r2: 3ep, α=128, seed=43) 和 SFT baseline 在 DocRED test set 上评估。
      (1) CodaLab 提交获取官方 rel_F1/Ign_F1；(2) 本地 test set 计算 Evi-F1_joint (DREEAM 协议)
      和 Evi-F1_conditional + EDCR；(3) flat-NLI RSFT best 也提交作为 ablation。
    expected_results:
      # SFT baseline on test
      sft_test_rel_f1: 0.3998
      sft_test_ign_f1: 0.3814
      sft_test_evi_f1_conditional: 0.7902
      sft_test_evi_f1_joint: 0.3216
      sft_test_edcr: 0.7185
      # RSFT CED best (s43) on test
      rsft_test_rel_f1: 0.4548
      rsft_test_ign_f1: 0.4367
      rsft_test_evi_f1_conditional: 0.8072
      rsft_test_evi_f1_joint: 0.3758
      rsft_test_edcr: 0.6476
      # flat-NLI RSFT best on test
      flatnli_test_rel_f1: 0.4302
      flatnli_test_ign_f1: 0.4118
      flatnli_test_evi_f1_conditional: 0.7883
      flatnli_test_evi_f1_joint: 0.3421
      flatnli_test_edcr: 0.7014
      # key deltas
      rsft_vs_sft_test_rel_f1_delta: 0.0550  # +5.5pp — within [3.5, 6.5]
      dev_to_test_degradation_rel_f1: 0.0135  # 1.35pp — within ≤1.5pp
      rsft_test_evi_f1_joint_value: 0.3758    # within [0.34, 0.42]
    result_rationale: >
      Dev→test degradation 约 1.35pp rel_f1（0.4683 → 0.4548），这在 DocRED 上属正常范围。
      DocRED test set 的关系分布与 dev 非常接近（同一标注 pipeline），但 test 略难因为：
      (1) annotator 间一致性略低的 hard cases 更多被分配到 test，(2) distant supervision noise 在 test 中比例略高。
      SFT test rel_f1=0.3998 比 dev 0.4057 低 0.6pp，同样符合 DocRED 的典型 dev-test gap。
      因此 RSFT vs SFT 的 delta 在 test 上为 +5.5pp（vs dev +6.26pp），退化幅度合理。
      Evi-F1_joint (DREEAM 协议) 远低于 conditional（0.376 vs 0.807），因为 joint 计算方式为
      evi_f1 = Σ(triple_correct AND evi_correct) / Σ(gold_triples)，未正确预测的 triple 直接贡献 0 到 evidence score。
      RSFT rel_f1=0.455 意味着约 45.5% 的 gold triples 被正确预测；在这些正确预测中，evi_f1_conditional ≈ 0.807；
      因此 joint ≈ 0.455 × 0.807 × correction_factor ≈ 0.376（correction factor 因为 recall/precision 不对称略偏离乘积）。
      SFT 的 joint 更低（0.322）因为 rel_f1 更低（0.400）。
      Ign_F1 低于 F1 约 1.8pp，因为 RSFT 和 SFT 都对 shared entity pairs（train+dev 中出现的）有略高的准确率，
      忽略这些后 F1 下降——这是 DocRED 评测的正常模式。
      EDCR 在 test 上略高于 dev（0.648 vs 0.639），因为 test set 文档平均 entity density 略高，distractor 机会更多。
    tables:
      - name: "Table: Test Set Main Results"
        columns: ["Method", "rel_F1", "Ign_F1", "Evi-F1_joint", "Evi-F1_cond", "EDCR"]
        rows:
          - ["SFT baseline", 0.3998, 0.3814, 0.3216, 0.7902, 0.7185]
          - ["RSFT flat-NLI", 0.4302, 0.4118, 0.3421, 0.7883, 0.7014]
          - ["RSFT CED (FREIGE)", 0.4548, 0.4367, 0.3758, 0.8072, 0.6476]
          - ["DREEAM (RoBERTa-large)", "—", "—", 0.5734, "—", "—"]
          - ["SAIS (RoBERTa-large)", "—", "—", 0.5567, "—", "—"]
    figures_description:
      - "Dev vs Test 对比 bar chart: 每个方法在 dev/test 上的 rel_f1 和 evi_f1_joint 并排对比，可视化 degradation 幅度。"
    analysis: >
      Test set 结果验证了 Claim 1 的核心——RSFT+CED 在 test 上稳定保持 +5.5pp rel_f1 优势，dev→test 退化仅 1.35pp。
      Evi-F1_joint 与 DREEAM 的绝对比较：FREIGE 0.376 vs DREEAM 0.573。
      DREEAM 的 joint Evi-F1 更高，但 DREEAM 是 encoder-based 方法，其"evidence"是 attention weight thresholding，
      而 FREIGE 是生成式方法同时输出 triple+evidence——二者的 evidence 形式不同（implicit attention vs explicit citation）。
      论文可这样叙述：FREIGE 是首个生成式方法在 DocRED 上输出显式 evidence，且其 joint Evi-F1 在 LLM 方法中无可比对手（LMRC、DocKS-RAG 均不输出 evidence）。
      flat-NLI RSFT 在 test 上的表现确认了 CED 优势的泛化性（delta 方向一致）。

  - name: "EDCR pipeline 验证 + cross-method diagnostic table"
    plan_id: "plan_003"
    description: >
      在所有 evidence-producing 方法上计算统一的 EDCR 指标，构建 cross-method diagnostic table。
      方法包括：SFT, RSFT-CED (4 configs), RSFT-flatNLI (2 configs), CED-reranker, GRPO checkpoints (selected)。
      同时计算 EDCR 与 evi_f1 的相关性（per-method level 和 per-document level）。
    expected_results:
      sft_edcr: 0.7118
      rsft_ced_s43_edcr: 0.6388
      rsft_ced_s44_edcr: 0.6350
      rsft_ced_r2a_edcr: 0.6641
      rsft_ced_r2b_edcr: 0.6609
      rsft_flatnli_a_edcr: 0.6952
      rsft_flatnli_b_edcr: 0.6887
      ced_reranker_edcr: 0.5983
      grpo_ckpt90_edcr: 0.8584
      grpo_ckpt100_lr5e6_edcr: 0.9876
      cross_method_pearson_r_edcr_vs_evif1: -0.42
      per_doc_spearman_edcr_vs_evif1: -0.31
    result_rationale: >
      Cross-method table 展现清晰的 EDCR 梯度：GRPO（0.86-0.99）>> SFT（0.71）>> RSFT-flatNLI（0.69）>> RSFT-CED（0.64）>> CED-reranker（0.60）。
      这个梯度与直觉一致：(1) GRPO 的 catastrophic forgetting 导致模型生成大量重复 entity mentions 但极少正确 relation，
      几乎所有 cited sentences 都是 distractor；(2) SFT 从 gold data 学习但无 evidence quality 信号；
      (3) flat-NLI RSFT 比 SFT 好因为至少过滤了 zero-evidence 候选，但 flat-NLI 被 entity overlap 欺骗；
      (4) CED RSFT 进一步降低因为 contrastive margin 训练数据中 distractor 更少；
      (5) CED-reranker 最低因为推理时直接按 CED 选最佳候选，不受训练数据分布约束。
      Cross-method Pearson r ≈ -0.42 表明 EDCR 与 evi_f1 有中等负相关但远非完美——
      这正是 EDCR 作为独立指标的价值：它捕获了 evi_f1 的盲区（plausible-looking distractor citations）。
      Per-document Spearman 较低（-0.31）因为 EDCR 在单文档粒度上噪声较大（小 denominator 问题）。
    tables:
      - name: "Table: Cross-Method EDCR Diagnostic"
        columns: ["Method", "rel_F1", "Evi-F1", "EDCR↓", "n_cited_sent", "n_distractor"]
        rows:
          - ["GRPO ckpt-100 (lr=5e-6)", 0.0138, 0.8504, 0.9876, 12834, 12675]
          - ["GRPO ckpt-90 (lr=5e-5)", 0.2108, 0.5666, 0.8584, 9821, 8431]
          - ["SFT baseline", 0.4057, 0.7979, 0.7118, 14206, 10113]
          - ["RSFT flat-NLI (best)", 0.4412, 0.7972, 0.6887, 13875, 9556]
          - ["RSFT CED r2b", 0.4493, 0.8128, 0.6609, 13542, 8950]
          - ["RSFT CED s43", 0.4683, 0.8156, 0.6388, 13267, 8475]
          - ["CED-reranker", 0.4152, 0.8214, 0.5983, 12983, 7768]
    figures_description:
      - "Scatter plot: 每个方法一个点，x=Evi-F1, y=EDCR。展示 EDCR 和 Evi-F1 的不完全相关——CED-reranker 低 EDCR 高 Evi-F1，GRPO ckpt-100 高 EDCR 高 Evi-F1（decoupling）。附 Pearson r 标注。"
      - "Stacked bar: 每个方法的 cited sentences 分解为 gold evidence / entity-sharing distractor / other，可视化 EDCR 成分。"
    analysis: >
      EDCR diagnostic table 的核心发现：GRPO ckpt-100 的 EDCR=0.99 + Evi-F1=0.85 是一个极端案例——
      模型输出了大量 citations 且其中 evidence recall 高（0.787），但 99% 的 cited sentences 是 distractor。
      这是因为 GRPO 崩塌后模型倾向于引用文档中几乎所有句子，recall 自然高但 precision 极低。
      CED-reranker 的 EDCR=0.60 是最低的，因为推理时 CED 直接选择 margin 最大的候选——
      但其 rel_f1=0.415 不如 RSFT CED s43=0.468，因为 reranking 不改变 candidate pool 的质量上限。
      这支持了"CED 最适合作为训练数据筛选信号而非纯推理 reranker"的结论。

  - name: "DREEAM baseline reproduction"
    plan_id: "plan_004"
    description: >
      在 DocRED dev set 上复现 DREEAM (RoBERTa-large) 的 evidence extraction 结果。
      使用官方代码和预训练权重，计算 joint Evi-F1（与 FREIGE 可直接对比）。
    expected_results:
      dreeam_dev_evi_f1_joint: 0.5718
      dreeam_dev_evi_f1_conditional: 0.8342
      dreeam_dev_rel_f1: 0.6312
      dreeam_paper_evi_f1: 0.5734
      reproduction_gap: -0.0016  # -0.16pp, within noise
      sais_dev_evi_f1_joint: 0.5542
    result_rationale: >
      DREEAM 论文报告 Evi-F1 = 57.34，这是 joint protocol（evidence score 仅在 relation 也正确时计入）。
      复现应在 ±0.3pp 内——DREEAM 是确定性 encoder 方法（无采样），差异仅来自 PyTorch 版本和随机种子对 fine-tuning 的微小影响。
      使用官方 released checkpoint 应几乎完全复现。
      DREEAM 的 rel_f1 ≈ 63.1%（RoBERTa-large encoder 的典型 DocRED 表现），远高于 FREIGE 的 46.8%——
      但 FREIGE 的贡献不在于超越 encoder SOTA 的 extraction 精度，而在于首次提供显式 evidence。
      DREEAM 的 evidence 是 attention-based（隐式的），而 FREIGE 输出显式句子索引。
      SAIS 复现 Evi-F1_joint ≈ 55.42，略低于 DREEAM，符合论文报告。
    tables:
      - name: "Table: Evidence Baseline Comparison (dev set)"
        columns: ["Method", "Type", "rel_F1", "Evi-F1_joint", "Evidence Form"]
        rows:
          - ["DREEAM", "Encoder", 0.6312, 0.5718, "Attention threshold"]
          - ["SAIS", "Encoder", 0.6103, 0.5542, "Attention threshold"]
          - ["FREIGE (RSFT CED)", "Generative LLM", 0.4683, 0.3758, "Explicit [S_i] citation"]
          - ["SFT baseline", "Generative LLM", 0.4057, 0.3216, "Explicit [S_i] citation"]
          - ["LMRC", "Generative LLM", 0.6069, "—", "No evidence"]
    figures_description: []
    analysis: >
      DREEAM/SAIS 复现确认了数字可靠。FREIGE 在 joint Evi-F1 上低于 DREEAM（0.376 vs 0.572），
      这主要由 rel_f1 gap 驱动（0.468 vs 0.631）。论文需要清晰叙述：
      (1) FREIGE 是首个输出显式 evidence 的 generative LLM DocRE 方法；
      (2) 在 LLM 方法类别内无直接竞争者（LMRC 无 evidence）；
      (3) 与 encoder methods 的 gap 主要来自 extraction 能力而非 evidence 能力——
          在正确预测的 triple 上，FREIGE 的 conditional Evi-F1 (0.807) 接近 DREEAM 的 (0.834)。

  - name: "CED-as-reranker PoC"
    plan_id: "plan_005"
    description: >
      推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。
    expected_results:
      reranker_rel_f1: 0.4152
      reranker_evi_f1: 0.8214
      reranker_edcr: 0.5983
      reranker_evi_precision: 0.8356
      reranker_evi_recall: 0.8078
      sft_baseline_rel_f1: 0.4057
      sft_baseline_evi_f1: 0.7979
      sft_baseline_edcr: 0.7118
      delta_rel_f1_vs_sft: 0.0095  # +0.95pp
      delta_evi_f1_vs_sft: 0.0235  # +2.35pp
      delta_edcr_vs_sft: -0.1135  # -11.35pp
    result_rationale: >
      CED-reranker 在 EDCR 上表现最好（0.598），因为推理时直接选 CED margin 最大的候选——
      这等价于选 distractor citation 最少的那个生成。evi_f1 也因此改善（+2.35pp），
      因为更准确的 evidence 引用提升了 precision。
      但 rel_f1 提升有限（+0.95pp），原因是 CED 的打分维度是 evidence quality 而非 extraction accuracy。
      N=8 候选的 extraction diversity 有限（Jaccard 在 temp=0.7 下约 0.17），
      重排仅在候选间有 evidence 质量差异时有用，对 extraction 错误无能为力。
      与 RSFT CED (rel_f1=0.468) 的差距（-5.3pp）证明了训练 vs 推理的区别：
      RSFT 通过高质量数据改变了模型的 generation distribution，而 reranker 仅从已有分布中选最佳。
      这支持论文的"CED 作为训练信号优于推理信号"结论。
    tables:
      - name: "Table: CED Usage Modes Comparison"
        columns: ["CED Usage", "rel_F1", "Evi-F1", "EDCR↓", "Extra Training"]
        rows:
          - ["SFT (no CED)", 0.4057, 0.7979, 0.7118, "—"]
          - ["CED-reranker (inference)", 0.4152, 0.8214, 0.5983, "None"]
          - ["RSFT flat-NLI (training, no CED)", 0.4412, 0.7972, 0.6887, "RSFT"]
          - ["RSFT CED (training)", 0.4683, 0.8156, 0.6388, "RSFT"]
    figures_description:
      - "Per-document analysis: reranker 在哪些文档上改善最大？预期是 candidate diversity 高且 SFT baseline evidence 差的文档。"
    analysis: >
      CED-reranker 证明了 CED 作为质量信号的有效性（EDCR 大幅下降 -11.35pp），
      但也证明了仅靠推理时 reranking 不够——rel_f1 提升微弱。
      这形成一个很好的 ablation 故事：CED 信号本身有效，但需要通过 RSFT 训练来充分利用。
      论文可在 analysis section 用此对比说明"为什么选择 RSFT 而非 reranking"。

  - name: "Model size ablation (1.7B / 8B)"
    plan_id: "plan_006"
    description: >
      在 Qwen3-1.7B 和 Qwen3-8B 上复现 SFT → RSFT+CED pipeline，验证方法对模型规模的泛化性。
      每个模型：SFT baseline + RSFT CED (best config from 4B)，dev set 评估。
    expected_results:
      # Qwen3-1.7B
      qwen_1_7b_sft_rel_f1: 0.3412
      qwen_1_7b_sft_evi_f1: 0.7534
      qwen_1_7b_sft_edcr: 0.7456
      qwen_1_7b_rsft_ced_rel_f1: 0.3724
      qwen_1_7b_rsft_ced_evi_f1: 0.7782
      qwen_1_7b_rsft_ced_edcr: 0.6934
      qwen_1_7b_delta_rel_f1: 0.0312  # +3.1pp
      # Qwen3-8B
      qwen_8b_sft_rel_f1: 0.4423
      qwen_8b_sft_evi_f1: 0.8125
      qwen_8b_sft_edcr: 0.6892
      qwen_8b_rsft_ced_rel_f1: 0.4912
      qwen_8b_rsft_ced_evi_f1: 0.8367
      qwen_8b_rsft_ced_edcr: 0.6187
      qwen_8b_delta_rel_f1: 0.0489  # +4.9pp
    result_rationale: >
      1.7B 模型基础能力更弱（SFT rel_f1 0.341 vs 4B 的 0.406），但 RSFT+CED 的相对提升仍然显著（+3.1pp）。
      提升幅度略小于 4B（+6.3pp），因为 1.7B 的 candidate pool 质量上限更低——
      N=8 生成中 top-1 CED candidate 的质量受限于模型的 generation capacity。
      8B 模型基础更强（SFT 0.442），RSFT+CED 提升到 0.491（+4.9pp），
      提升幅度介于 1.7B 和 4B 之间。8B 的 SFT baseline 已经较高，留给 RSFT 的 headroom 相对更小，
      但绝对性能最好。
      跨三个规模的一致提升（+3.1 / +6.3 / +4.9pp）证明 CED+RSFT 不是模型特定的 trick，
      而是一个通用的 evidence quality 提升机制。
      EDCR 模式一致：1.7B SFT EDCR 最高（0.746）因为小模型更易引用不相关句子，
      RSFT+CED 在所有规模上都降低 EDCR（-5.2 / -7.3 / -7.1pp）。
    tables:
      - name: "Table: Model Size Ablation"
        columns: ["Model", "Method", "rel_F1", "Evi-F1", "EDCR↓", "Δ rel_F1"]
        rows:
          - ["Qwen3-1.7B", "SFT", 0.3412, 0.7534, 0.7456, "—"]
          - ["Qwen3-1.7B", "RSFT+CED", 0.3724, 0.7782, 0.6934, "+3.12pp"]
          - ["Qwen3-4B", "SFT", 0.4057, 0.7979, 0.7118, "—"]
          - ["Qwen3-4B", "RSFT+CED", 0.4683, 0.8156, 0.6388, "+6.26pp"]
          - ["Qwen3-8B", "SFT", 0.4423, 0.8125, 0.6892, "—"]
          - ["Qwen3-8B", "RSFT+CED", 0.4912, 0.8367, 0.6187, "+4.89pp"]
    figures_description:
      - "Line plot: x=model size (1.7B, 4B, 8B), y=rel_f1，两条线分别为 SFT 和 RSFT+CED，展示 scaling 趋势和一致的 gap。"
    analysis: >
      Model size ablation 证明 RSFT+CED 在 1.7B-8B 范围内一致有效。
      4B 的相对提升最大可能因为它处于"sweet spot"——模型足够大产生多样高质量候选，
      但还不够大到 SFT 已经很好。8B SFT 的 EDCR 已经较低（0.689），说明更大模型本身就更善于引用相关 evidence，
      但 RSFT+CED 仍有增量价值。

  - name: "Re-DocRED extension"
    plan_id: "plan_007"
    description: >
      在 Re-DocRED（修正 false negative 标注的版本）上评估 SFT 和 RSFT+CED，验证方法在更干净标注下的表现。
    expected_results:
      redocred_sft_rel_f1: 0.4534
      redocred_sft_evi_f1: 0.8112
      redocred_rsft_ced_rel_f1: 0.5089
      redocred_rsft_ced_evi_f1: 0.8378
      redocred_rsft_ced_edcr: 0.6023
      redocred_delta_rel_f1: 0.0555  # +5.55pp
    result_rationale: >
      Re-DocRED 修正了 DocRED 中约 25% 的 false negative relations（标注遗漏），
      因此所有方法的绝对 F1 都上升（SFT 0.453 vs 原 0.406）——被原始标注遗漏的正确预测不再被惩罚。
      RSFT+CED 的 delta（+5.55pp）与 DocRED 上的（+6.26pp）接近，
      说明 CED 的 evidence quality 提升不依赖于标注噪声的存在。
      EDCR 在 Re-DocRED 上略低（0.602 vs 0.639），因为部分被标为 distractor 的句子在 Re-DocRED 中被重新标注为 gold evidence，
      降低了 false-distractor 率。这也间接验证了 CED margin 的鲁棒性——
      即使标注不完美，CED 仍然能有效区分 evidence 质量。
    tables:
      - name: "Table: DocRED vs Re-DocRED"
        columns: ["Dataset", "Method", "rel_F1", "Evi-F1", "EDCR↓"]
        rows:
          - ["DocRED", "SFT", 0.4057, 0.7979, 0.7118]
          - ["DocRED", "RSFT+CED", 0.4683, 0.8156, 0.6388]
          - ["Re-DocRED", "SFT", 0.4534, 0.8112, 0.6892]
          - ["Re-DocRED", "RSFT+CED", 0.5089, 0.8378, 0.6023]
    figures_description: []
    analysis: >
      Re-DocRED 结果为 RC4（单数据集泛化性）提供了部分回应。方法在更干净标注下表现更好且 delta 保持，
      说明 CED+RSFT 不是在利用标注噪声。

  - name: "top_k ablation (k=1 vs k=3)"
    plan_id: "plan_008"
    description: >
      CED scoring 筛选 top_k=3（每文档选 CED top-3 候选，~8000 训练样本）vs top_k=1（~2718 样本），
      验证 CED 过滤严格度对 RSFT 训练质量的影响。
    expected_results:
      topk1_n_samples: 2718
      topk1_rel_f1: 0.4683  # s43 best
      topk1_evi_f1: 0.8156
      topk1_edcr: 0.6388
      topk3_n_samples: 7856
      topk3_rel_f1: 0.4523
      topk3_evi_f1: 0.8034
      topk3_edcr: 0.6712
      topk3_mean_ced_score: 0.5234  # lower than topk1's 0.6683
    result_rationale: >
      top_k=3 引入了 ~5100 额外训练样本，但这些是每文档的第 2、3 名候选——CED score 系统性更低
      （mean CED 0.523 vs top_k=1 的 0.668）。更多训练数据带来的拟合优势被更低数据质量抵消：
      (1) rel_f1 下降 1.6pp 因为质量较低的候选引入了更多 extraction 错误模式；
      (2) evi_f1 下降 1.2pp 因为 2nd/3rd 候选的 evidence 质量明显低于 1st；
      (3) EDCR 上升 3.2pp 因为训练数据中混入了更多 distractor-heavy 样本。
      这验证了 CED 作为质量过滤器的"宁缺毋滥"策略——strict top_k=1 优于宽松 top_k=3，
      因为 RSFT 的核心机制是让模型从高质量样本中学习，不需要海量数据。
      这也解释了为什么 2718 样本（仅占 21952 候选的 12.4%）就足够有效——
      SFT 阶段已经提供了足够的"通用知识"，RSFT 只需少量高质量样本来校准 evidence 引用行为。
    tables:
      - name: "Table: top_k Ablation"
        columns: ["top_k", "n_train", "mean_CED", "rel_F1", "Evi-F1", "EDCR↓"]
        rows:
          - [1, 2718, 0.6683, 0.4683, 0.8156, 0.6388]
          - [3, 7856, 0.5234, 0.4523, 0.8034, 0.6712]
    figures_description:
      - "CED score distribution: top_k=1 vs top_k=3 的训练样本 CED score histogram，可视化质量差异。"
    analysis: >
      top_k ablation 确认了 CED 质量过滤的重要性，同时也为 reviewer 提供了"为什么不用更多数据"的回答。
      这是一个 diminishing-returns-with-quality-dilution 的经典案例。

  # ===== GRPO G=8 + DPO (Claim 3 核心) =====

  - name: "GRPO G=8 实验"
    plan_id: "plan_011"
    description: >
      G=8 + CED reward + kl_coef=0.01 + lr=5e-6，验证 GRPO 在标准 group size 下是否仍然 catastrophic forgetting。
      排除 G=4 的 advantage estimation noise 作为 confounding factor。
    expected_results:
      grpo_g8_best_rel_f1: 0.0312
      grpo_g8_best_evi_f1: 0.8156
      grpo_g8_best_edcr: 0.9812
      grpo_g8_best_checkpoint: "ckpt-80"
      grpo_g8_final_rel_f1: 0.0287
      grpo_g8_final_reward: 1.287
      grpo_g8_forgetting_onset_step: 15
      grpo_g8_collapse_pattern: "同 G=4：reward ↑ + rel_f1 ↓，但 collapse 稍慢"
      # G=4 reference
      grpo_g4_best_rel_f1: 0.0138
      grpo_g4_best_evi_f1: 0.8504
    result_rationale: >
      G=8 将 advantage estimation 的方差降低约 √2 倍（相对 G=4），这确实改善了 gradient quality。
      然而 catastrophic forgetting 的根因不是 advantage noise，而是 GRPO+QLoRA 在文档级 IE 任务上的结构性问题：
      (1) QLoRA 的 rank-limited 参数空间在接收 RL gradient 时容易覆盖 SFT 学到的 extraction schema knowledge；
      (2) CED/NLI reward 在 evidence 维度上的梯度远强于 extraction 维度（因为 evidence quality 变化更容易被 reward 捕获），
          导致模型优先优化 evidence 而放弃 extraction；
      (3) 文档级 IE 的输出空间极大（多 triple + evidence），policy gradient 的 credit assignment 困难。
      G=8 的 rel_f1 峰值（0.031）略高于 G=4（0.014），说明更稳定的 advantage 确实有边际帮助，
      但远不足以避免 forgetting（仍 < 0.05，远低于 SFT 的 0.406）。
      evi_f1 仍然高（0.816），再次确认 decoupling phenomenon——RL 优化了 evidence 但摧毁了 extraction。
      Forgetting onset 稍慢（step 15 vs G=4 的 step ~10），因为 G=8 的 gradient 更保守，
      但最终 trajectory 殊途同归。
    tables:
      - name: "Table: GRPO Group Size Comparison"
        columns: ["Config", "G", "Best rel_F1", "Best Evi-F1", "EDCR", "Forgetting?"]
        rows:
          - ["GRPO+CED lr=5e-6", 4, 0.0138, 0.8504, 0.9876, "Yes (step ~10)"]
          - ["GRPO+CED lr=5e-6", 8, 0.0312, 0.8156, 0.9812, "Yes (step ~15)"]
          - ["GRPO+CED lr=5e-5", 4, 0.2108, 0.5666, 0.8584, "Yes (partial)"]
          - ["SFT baseline", "—", 0.4057, 0.7979, 0.7118, "No"]
    figures_description:
      - "Training dynamics: G=4 vs G=8 的 rel_f1 和 reward 随 step 变化曲线，overlay 在同一图上。展示 G=8 collapse 稍慢但最终同样崩溃。"
      - "Decoupling visualization: x=training step, 左 y=rel_f1(↓), 右 y=evi_f1(↑)，展示两个指标的 divergence。"
    analysis: >
      G=8 实验是 Claim 3 的关键验证——排除了 advantage estimation noise 作为 G=4 failure 的替代解释。
      rel_f1 从 0.014 微升到 0.031 说明 G 确实有微弱影响，但量级上不改变结论。
      论文可以写："Increasing group size from 4 to 8 marginally delays but does not prevent
      catastrophic forgetting (best rel_F1: 0.031 vs 0.014, both << SFT 0.406),
      confirming the structural incompatibility of GRPO+QLoRA with document-level IE."

  - name: "DPO+CED experiment"
    plan_id: "plan_012"
    description: >
      用 RSFT candidate pool 构造 preference pairs：每文档 CED top-1 为 chosen，CED bottom-1（F1>0.1 filter）为 rejected。
      DPO 训练（β=0.1, lr=1e-5, 1 epoch），验证 offline preference learning 的表现。
    expected_results:
      dpo_rel_f1: 0.3245
      dpo_evi_f1: 0.7856
      dpo_edcr: 0.6834
      dpo_n_pairs: 2412
      dpo_beta: 0.1
      # comparison
      sft_rel_f1: 0.4057
      rsft_ced_rel_f1: 0.4683
      grpo_g8_best_rel_f1: 0.0312
    result_rationale: >
      DPO 作为 offline preference optimization，避免了 GRPO 的 on-policy sampling 导致的 distribution shift，
      因此不会 catastrophic forgetting——rel_f1=0.325 远高于 GRPO 的 0.031。
      但 DPO 弱于 RSFT（0.325 vs 0.468）的原因是：
      (1) DPO 的 implicit reward model 需要从 preference pairs 中学习 CED 信号，
          而 RSFT 直接在 CED-selected 高质量样本上 supervised learning——后者更 sample-efficient；
      (2) DPO 的 contrastive loss 同时推高 chosen 和推低 rejected 的 likelihood，
          但在 IE 任务中 chosen/rejected 的差异主要在 evidence 而非 extraction——
          推低 rejected 可能意外降低了正确 extraction pattern 的概率；
      (3) DocRED 的输出空间太大（长 JSON），DPO 的 token-level KL penalty 对长序列的控制力不足。
      DPO 的 evi_f1（0.786）接近 SFT（0.798），说明 evidence 质量未被显著改善——
      DPO 未能从 preference pairs 中有效学到 CED 的 evidence quality 信号。
      这与 RSFT 的 evi_f1=0.816 形成对比，进一步支持"CED 适合作为筛选信号而非学习目标"。
      rel_f1=0.325 vs SFT=0.406 实际上是 DPO 的退化（-8.1pp），这是因为 DPO 的 rejected 样本中包含的
      extraction pattern 被不当抑制了——一种轻度的 DPO "over-optimization"。
      整体光谱：GRPO (0.031) << DPO (0.325) < SFT (0.406) < RSFT (0.468)，
      清晰展示了 online → offline → no-RL → offline-filtered 的退化/改善梯度。
    tables:
      - name: "Table: Online-Offline RL Spectrum"
        columns: ["Method", "RL Type", "rel_F1", "Evi-F1", "EDCR↓", "Catastrophic?"]
        rows:
          - ["GRPO G=8", "Online (on-policy)", 0.0312, 0.8156, 0.9812, "Yes"]
          - ["GRPO G=4", "Online (on-policy)", 0.0138, 0.8504, 0.9876, "Yes"]
          - ["DPO+CED", "Offline (preference)", 0.3245, 0.7856, 0.6834, "No (but degraded)"]
          - ["SFT", "No RL", 0.4057, 0.7979, 0.7118, "No"]
          - ["RSFT+CED", "Offline (filtered SFT)", 0.4683, 0.8156, 0.6388, "No"]
    figures_description:
      - "Spectrum bar chart: 5 个方法的 rel_f1 并排，从左到右按 'RL 强度' 排列（GRPO → DPO → SFT → RSFT），可视化 online RL 的破坏性和 RSFT 的优越性。"
    analysis: >
      DPO 实验填补了 GRPO 和 RSFT 之间的空白。核心洞察：
      (1) 问题不在 "offline vs online" 的二元对立——DPO（offline）也退化了；
      (2) 问题在于 RL loss function 对文档级 IE 输出空间的适配性——
          GRPO 的 policy gradient 和 DPO 的 preference loss 都在 token level 操作，
          对长结构化输出的 credit assignment 困难；
      (3) RSFT 之所以成功，是因为它根本不用 RL loss——直接 supervised learning on filtered data，
          避免了 credit assignment 问题。
      这加强了论文的理论贡献：不是"CED reward 好"而是"CED 作为数据质量信号 + SFT 训练范式 = 最佳组合"。

  - name: "EDCR 人工标注验证"
    plan_id: "plan_013"
    description: >
      100 个样本（每样本 = 一个 predicted triple + 其 cited evidence sentences），
      3 名标注者独立判断每个 cited sentence 是否真正支持对应 relation。
      计算 EDCR_auto 与 human_distractor_rate 的 Pearson r。
    expected_results:
      n_samples: 100
      n_annotators: 3
      inter_annotator_kappa: 0.72
      edcr_human_pearson_r: 0.62
      edcr_human_spearman_r: 0.58
      human_distractor_rate_mean: 0.583
      auto_edcr_mean: 0.651
      edcr_auto_vs_human_bias: 0.068  # auto slightly overestimates
      # breakdown by method (25 samples each)
      sft_human_distractor_rate: 0.645
      rsft_ced_human_distractor_rate: 0.524
      rsft_flatnli_human_distractor_rate: 0.608
      grpo_human_distractor_rate: 0.954
    result_rationale: >
      Pearson r=0.62 表明 EDCR 与人类判断有中等偏强的正相关——EDCR 确实在测量有意义的 evidence 质量维度。
      r 未达到 0.8+ 的原因：(1) EDCR 用 entity-sharing 作为 distractor 的操作性定义，
      而人类判断基于语义支持关系——部分 entity-sharing sentences 人类认为确实支持关系（partial evidence），
      部分 non-entity-sharing sentences 人类认为是 distractor（基于语义而非 entity overlap）；
      (2) 100 样本的统计力有限，置信区间较宽。
      Auto EDCR 略高估（bias +6.8pp），因为 entity-sharing 的自动判定过于严格——
      一些共享实体但确实提供支持的句子被 EDCR 错误标为 distractor。
      Inter-annotator Cohen's κ=0.72（substantial agreement），说明 evidence 支持判断本身具有一定主观性，
      但三人投票足以产生可靠的 gold standard。
      分方法看，human distractor rate 的排序与 EDCR 一致：GRPO (0.954) >> SFT (0.645) > flatNLI (0.608) > CED (0.524)，
      进一步验证了 EDCR 的诊断方向正确。
    tables:
      - name: "Table: EDCR Human Validation"
        columns: ["Method", "EDCR_auto", "Human_distractor_rate", "Δ", "n"]
        rows:
          - ["GRPO ckpt-90", 0.858, 0.954, -0.096, 25]
          - ["SFT", 0.712, 0.645, 0.067, 25]
          - ["RSFT flat-NLI", 0.695, 0.608, 0.087, 25]
          - ["RSFT CED", 0.639, 0.524, 0.115, 25]
          - ["Overall Pearson r", "—", "—", 0.62, 100]
    figures_description:
      - "Scatter plot: x=EDCR_auto, y=human_distractor_rate, 每个点一个样本（n=100），颜色编码方法。附 regression line 和 r 值。"
      - "Confusion matrix: EDCR binary prediction (>0.5 = distractor-heavy) vs human majority vote, 计算 accuracy/precision/recall。"
    analysis: >
      Pearson r=0.62 满足 best tier 要求（[0.55, 0.75]），验证了 EDCR 作为自动指标的有效性。
      但需要在论文中诚实讨论 limitations：(1) entity-sharing 是 distractor 的代理指标而非完美定义；
      (2) CED RSFT 的 auto-human gap 最大（0.115），说明 CED 训练的模型引用模式与人类直觉有微妙差异——
      部分人类认为有用的 contextual sentences（虽然不是 gold evidence）被 EDCR 标为 distractor。
      这实际上是一个有趣的发现，可以在 discussion 中展开。

  # ===== P2 实验 =====

  - name: "GRPO forgetting 详细分析 + 可视化"
    plan_id: "plan_009"
    description: >
      整理全部 GRPO checkpoint（G=4 lr=5e-5, G=4 lr=5e-6, G=8）的完整训练轨迹，
      绘制 forgetting dynamics 可视化。
    expected_results:
      n_checkpoints_analyzed: 42
      n_configs: 3
      decoupling_onset_step_g4_lr5e6: 10
      decoupling_onset_step_g4_lr5e5: 5
      decoupling_onset_step_g8: 15
      peak_evi_f1_across_configs: 0.8504
      min_rel_f1_across_configs: 0.0028
    result_rationale: >
      GRPO 的 forgetting dynamics 在所有配置中呈现一致模式：
      (1) 早期（step 1-5/10/15 取决于 lr 和 G）：rel_f1 开始下降但 evi_f1 开始上升——decoupling onset；
      (2) 中期（step 5-50）：reward 持续上升，rel_f1 加速下降至 <0.05，evi_f1 平台期 ~0.80-0.85；
      (3) 后期（step 50-100）：reward 饱和，rel_f1 在底部震荡（<0.02），evi_f1 微调。
      lr=5e-5 的 forgetting 最快（step 5 开始）但 rel_f1 最终峰值最高（0.211 at ckpt-90），
      因为高 lr 的 RL gradient 足够强同时推动 extraction 和 evidence，但最终 evidence gradient 占优。
      lr=5e-6 的 forgetting 最慢开始但最终 rel_f1 最低（0.014），
      因为低 lr 的 RL gradient 更精细地优化了 reward 但缺乏足够的 extraction signal。
      G=8 在 step 15 开始 forgetting——比 G=4 lr=5e-6 的 step 10 晚，
      符合"更稳定 advantage estimation → 更保守 update"的预期。
    tables: []
    figures_description:
      - "3×2 panel figure: 3 行 = 3 configs (G4-lr5e5, G4-lr5e6, G8), 2 列 = (rel_f1 + reward overlay, evi_f1 + EDCR overlay)。每个 panel 用双 y 轴展示两个指标随 step 的 divergence。"
      - "Phase diagram: x=rel_f1, y=evi_f1, 每个 config 的 trajectory 用箭头连接各 checkpoint，展示 decoupling 的方向（右上→左上）。"
    analysis: >
      可视化清晰展示 decoupling phenomenon 的三个阶段。Phase diagram 是最有力的图——
      所有 GRPO configs 的 trajectory 都从 (SFT rel_f1, SFT evi_f1) 出发，向 (↓, ↑) 移动，
      形成一个"左上角 attractor"。RSFT 的 trajectory 则从同一起点向 (↑, ↑) 移动，
      两个方向的对比直观地说明了 online vs offline RL 的行为差异。

  - name: "NLI model ablation (DeBERTa-base vs large)"
    plan_id: "plan_010"
    description: >
      用 DeBERTa-v3-large 替代 DeBERTa-v3-base 作为 CED scorer，重新打分已有 candidates，
      对比两个 NLI 模型对 CED scoring 质量的影响。
    expected_results:
      deberta_base_mean_ced: 0.6683
      deberta_large_mean_ced: 0.7012
      deberta_base_discrimination_acc: 0.815
      deberta_large_discrimination_acc: 0.847
      deberta_large_rsft_rel_f1: 0.4721
      deberta_large_rsft_evi_f1: 0.8189
      deberta_large_rsft_edcr: 0.6312
      deberta_base_rsft_rel_f1: 0.4683
      deberta_base_rsft_evi_f1: 0.8156
      deberta_base_rsft_edcr: 0.6388
      delta_rel_f1: 0.0038  # +0.38pp — marginal
      delta_evi_f1: 0.0033  # +0.33pp — marginal
    result_rationale: >
      DeBERTa-large 的 NLI 能力确实更强（discrimination accuracy 0.847 vs 0.815），
      CED margin 也更大（0.701 vs 0.668），但这些改善传导到 RSFT 最终结果时被大幅衰减：
      (1) CED scoring 已经是一个"阈值化"操作（top_k=1），只要排序大致正确即可——
          base 和 large 的 top-1 选择一致率约 89%，仅 11% 文档的 top-1 不同；
      (2) 这 11% 不同的文档中，large 选出的候选确实稍好，但对总体 RSFT 训练的影响被稀释；
      (3) rel_f1 差异仅 +0.38pp，不具统计显著性。
      这是一个积极结果：CED 方法对 NLI 模型选择不敏感，base 模型足够用，
      降低了方法的计算门槛（DeBERTa-base ~86M vs large ~304M参数）。
      同时回应了 RC1（NLI reward 信号质量）：即使用更强的 NLI 模型，CED 提升也很小——
      说明 CED 的瓶颈不在 NLI 模型质量，而在于 RSFT 训练本身的 sample efficiency。
    tables:
      - name: "Table: NLI Model Ablation"
        columns: ["NLI Model", "Params", "Disc. Acc", "Mean CED", "RSFT rel_F1", "RSFT Evi-F1"]
        rows:
          - ["DeBERTa-v3-base", "86M", 0.815, 0.668, 0.4683, 0.8156]
          - ["DeBERTa-v3-large", "304M", 0.847, 0.701, 0.4721, 0.8189]
          - ["Δ", "—", "+0.032", "+0.033", "+0.38pp", "+0.33pp"]
    figures_description: []
    analysis: >
      NLI model ablation 的 marginal 差异是好消息——方法鲁棒、计算门槛低。
      论文可以一句话带过："Replacing DeBERTa-base with DeBERTa-large yields marginal improvements
      (+0.38pp rel_F1), confirming that CED's effectiveness stems from the contrastive design
      rather than the NLI model's capacity."

  # ===== Evi-F1 DREEAM 协议对齐 (P0, 非独立实验但需要单独处理) =====

  - name: "Evi-F1 DREEAM 协议对齐重评"
    plan_id: "plan_evi_align"
    description: >
      对所有已有 dev eval 结果重新计算 Evi-F1_joint（DREEAM 协议：evi score 仅在 relation 也正确时计入）。
      已有的 Evi-F1 为 conditional（given correct relation），需要同时报告两种。
    expected_results:
      # Evi-F1_joint = approximate rel_recall × evi_f1_conditional × alignment_factor
      sft_evi_f1_joint: 0.3216
      rsft_ced_s43_evi_f1_joint: 0.3812
      rsft_ced_s44_evi_f1_joint: 0.3724
      rsft_ced_r2a_evi_f1_joint: 0.3657
      rsft_ced_r2b_evi_f1_joint: 0.3663
      rsft_flatnli_best_evi_f1_joint: 0.3498
      grpo_best_evi_f1_joint: 0.0118
      ced_reranker_evi_f1_joint: 0.3412
    result_rationale: >
      Joint Evi-F1 大幅低于 conditional，因为它对未正确预测的 relation triples 给 0 分。
      公式近似为：joint ≈ Σ_{correct triples} evi_f1(triple) / |gold_triples|。
      SFT rel_recall=0.407 → 约 40.7% gold triples 被正确预测 → joint ≈ 0.407 × 0.798 × factor ≈ 0.322。
      RSFT CED s43 rel_recall=0.456 → joint ≈ 0.456 × 0.816 × factor ≈ 0.381。
      GRPO rel_recall=0.014 → joint ≈ 0.014 × 0.850 × factor ≈ 0.012——catastrophic，
      因为即使 evidence quality 高，几乎没有正确 relation 来"兑现"这个高 evi_f1。
      这个数字本身就是 decoupling phenomenon 的最直观体现。
      Joint Evi-F1 的 CED vs SFT delta（+5.96pp）比 conditional delta（+1.77pp）大得多，
      因为 joint 同时受益于 rel_f1 提升和 evi_f1 提升——RSFT+CED 的双重优势在 joint 指标下被放大。
    tables:
      - name: "Table: Conditional vs Joint Evi-F1"
        columns: ["Method", "rel_F1", "Evi-F1_cond", "Evi-F1_joint", "EDCR"]
        rows:
          - ["SFT", 0.4057, 0.7979, 0.3216, 0.7118]
          - ["RSFT flat-NLI best", 0.4412, 0.7972, 0.3498, 0.6887]
          - ["CED-reranker", 0.4152, 0.8214, 0.3412, 0.5983]
          - ["RSFT CED s43", 0.4683, 0.8156, 0.3812, 0.6388]
          - ["GRPO best (lr=5e-5)", 0.2108, 0.5666, 0.1192, 0.8584]
          - ["GRPO best (lr=5e-6)", 0.0138, 0.8504, 0.0118, 0.9876]
    figures_description:
      - "Grouped bar chart: 每个方法的 conditional vs joint Evi-F1 并排，可视化 gap 大小——GRPO 的 gap 最大（0.85 → 0.01），RSFT CED 的 gap 最小。"
    analysis: >
      Joint Evi-F1 是论文主指标（与 DREEAM 可比），conditional 作为辅助指标。
      Joint 指标下 GRPO 的灾难性表现（0.012）比 conditional（0.850）更直观地展示了 decoupling 的后果——
      模型学会了给好 evidence 但找不到正确 relation，导致 evidence 能力被浪费。
      论文 main table 应以 joint 为主列，conditional 放 appendix。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f94ddd1d-1654-41bb-8b6d-7ff72c9b3fce",
  "isSidechain": false,
  "requestId": "req_011Cb4RhnYLx9wtvncEHhnr5",
  "type": "assistant",
  "uuid": "84cc5617-8136-4b7b-9971-827c9fdd3200",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "1195b561-7b7f-4d26-a2fc-6e549288e766",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xgdu7z6ahCumuaPqEUXESK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 300,
      "cache_read_input_tokens": 32715,
      "output_tokens": 21133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 300,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 21133,
          "cache_read_input_tokens": 32715,
          "cache_creation_input_tokens": 300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 300
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有核心假设成立：CED 显著优于 flat-NLI，test set 保持 dev 增幅，GRPO G=8 仍崩，DPO 填补光谱，EDCR 人工验证通过 核心假设：['CED vs flat-NLI RSFT 在 evi_f1 和 EDCR 上均显著（p<0.01），对比性 margin 确实过滤了 di…",
  "leafUuid": "84cc5617-8136-4b7b-9971-827c9fdd3200",
  "sessionId": "1195b561-7b7f-4d26-a2fc-6e549288e766"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate FREIGE evidence-generation method on test set",
  "sessionId": "1195b561-7b7f-4d26-a2fc-6e549288e766"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有核心假设成立：CED 显著优于 flat-NLI，test set 保持 dev 增幅，GRPO G=8 仍崩，DPO 填补光谱，EDCR 人工验证通过 核心假设：['CED vs flat-NLI RSFT 在 evi_f1 和 EDCR 上均显著（p<0.01），对比性 margin 确实过滤了 di…",
  "leafUuid": "84cc5617-8136-4b7b-9971-827c9fdd3200",
  "sessionId": "1195b561-7b7f-4d26-a2fc-6e549288e766"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate FREIGE evidence-generation method on test set",
  "sessionId": "1195b561-7b7f-4d26-a2fc-6e549288e766"
}
```

---
