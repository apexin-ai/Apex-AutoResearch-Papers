# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：RSFT 优势在 test set 上大幅缩水，且 GRPO G=8 部分恢复，核心叙事需要全面 reframe 核心假设：['CED vs flat

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/9e91ad84-b38b-4f46-b28b-5d00fe45e71e.jsonl`
- **Structured JSON:** [`dffdde9aaebebaa7a4ae.json`](../../sessions/df/dffdde9aaebebaa7a4ae.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T13:46:00.565Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T13:46:00.565Z",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：RSFT 优势在 test set 上大幅缩水，且 GRPO G=8 部分恢复，核心叙事需要全面 reframe\n核心假设：['CED vs flat-NLI 无差异或 flat-NLI 略优（Δevi_f1 < 0.3pp），CED 的对比性设计在 RSFT 间接作用下无可观测效果', 'Test set rel_f1 Δ ≤ +2.0pp over SFT（dev→test 退化 >3pp），可能不显著（p>0.05），dev 增幅存在过拟合成分', 'GRPO G=8 部分恢复（rel_f1 0.15-0.30），说明 G=4 的失败有 advantage noise 成分，Claim 3 需大幅限定范围', 'DPO rel_f1 ≥ 0.35，接近 RSFT，说明 offline 优势不在于 rejection sampling 而在于避免 policy gradient', 'EDCR 与人工判断 r < 0.35，EDCR 作为独立指标的价值存疑']\n关键指标范围：{'test_rel_f1_delta_over_sft': [0.5, 2.0], 'ced_vs_flatnli_evi_f1_delta': [-0.5, 0.3], 'ced_vs_flatnli_edcr_delta': [-2.0, 2.0], 'ced_vs_flatnli_p_value': [0.2, 0.8], 'grpo_g8_best_rel_f1': [0.15, 0.3], 'dpo_rel_f1': [0.35, 0.44], 'edcr_human_pearson_r': [0.1, 0.35], 'rsft_best_test_rel_f1': [0.39, 0.43], 'rsft_test_evi_f1_joint': [0.22, 0.3]}\n叙事方向：需要全面 reframe，但仍冲 EMNLP Main，不降级目标。Reframe 策略： 论文从 \"method paper\" 转型为 \"analysis + benchmark paper\"。 核心叙事变为：对 LLM DocRE 的 evidence generation 进行首次系统性研究， 回答 \"哪些 RL/training 策略能让 LLM 在文档级 IE 中生成可验证证据\" 这一开放问题。 贡献重组为：(1) 首个 LLM DocRE evidence benchmark（任务定义 + 评测协议 + 多指标框架）； (2) online vs offline RL 的系统对比（GRPO vs DPO vs RSFT，含 G=4/G=8 消融）， 发现不是 online RL 本身失败而是 QLoRA+小 group size 的脆弱组合； (3) evidence 评估指标的局限性分析（Evi-F1 conditional vs joint 的差异 + EDCR 的信号与噪声）。 CED 完全降级为一种 explored scoring function。 需大幅增加实验覆盖（model sizes, datasets）来支撑 \"systematic study\" 叙事。 投稿可能推迟到 ARR September 或 AAAI 2027 以积累足够实验。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: faith-evidence-ie\nvenue: EMNLP 2026 Main\nfocus: D042 修正后 re-dream。关键变化: (1) Claim 3 缩窄为 GRPO+QLoRA 而非 online RL; (2) 新增 GRPO G=8 实验(plan_011); (3) 新增 DPO baseline(plan_012); (4) CED contingency plan(如 p>0.05 则降级); (5) Evi-F1 改为 DREEAM 对齐协议(joint); (6) 新增 EDCR 人工验证(plan_013)。请关注这些修改是否有效提升了论文质量。\n\n## paper_framing.md\n\n# Paper Framing — FREIGE\n\n> **状态**: POST-MVP (MVP-1 + MVP-2 均 PASS，进入 Research 阶段)\n> **最后更新**: 2026-05-15\n\n## Target Venue\n\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\n- Stretch: ARR May 25 (10 days, 极紧，仅在实验全部顺利时考虑)\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\n\n## Core Insight\n\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。朴素 NLI faithfulness reward 可被 entity-mentioning distractor 句子游戏——共享实体但不支持具体关系的句子仍获正面蕴含分数。\n\n**CED (Contrastive Evidence Discrimination)** 通过文档内 hard negative 对比，将 evidence 质量评估从\"是否蕴含\"升级为\"是否比最佳干扰句更蕴含\"——本质上是 evidence grounding 场景下的 **anti-reward-overoptimization mechanism**（连接 Gao et al. 2023 reward overoptimization 理论）。\n\n**MVP 关键发现**: CED 作为在线 RL (GRPO) reward 导致 catastrophic forgetting（3 种 reward type × 多个 lr 全线失败），但作为离线 RL (RSFT) 的候选筛选信号极其有效——4 组超参配置均稳定超过 SFT baseline。**方法论结论**: 对结构化 IE 任务，CED 应作为离线质量信号而非在线训练奖励。\n\n## Story Arc\n\n1. **Problem**: LLM DocRE 无证据 → 部署障碍（human-in-the-loop KB population、生物医学审计、RAG 溯源）\n2. **Why naive reward fails**: flat-NLI 被 entity-sharing distractors 欺骗（SFT EDCR=71.2%，大量引用干扰句）\n3. **Why online RL fails**: GRPO+CED/flat-NLI/extract-only 全部 catastrophic forgetting（reward ↑ + rel_f1 ↓ 至 <0.02）\n4. **Solution**: CED 作为离线质量信号 + RSFT（rejection sampling fine-tuning）：SFT 模型生成 N 候选 → CED 打分筛选 → 微调，规避在线 RL 的遗忘风险\n5. **Theoretical grounding**: 连接 LongRLVR (ICLR 2026) evidence grounding 梯度消失分析 + \"RSFT=PPO\" (ICML 2025) 等价性理论\n6. **Result**: 首个 LLM-based DocRE 方法同时生成抽取和可验证证据\n\n## Core Claims\n\n### Claim 1 (Main): CED-scored RSFT 使 LLM 同时生成抽取和忠实证据\n- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法\n- RSFT+CED: rel_f1 +3.9~6.0pp over SFT, evi_f1 +1.1~2.1pp, EDCR -4.8~7.7pp\n- **MVP-2 已验证**: 4/4 configs PASS\n- **Research 需要**: test set 评估，DREEAM/SAIS Evi-F1 直接对比\n\n### Claim 2 (Ablation): CED scoring 优于 flat-NLI scoring 用于 RSFT\n- CED-filtered RSFT vs flat-NLI-filtered RSFT 的 evi_f1 和 EDCR 差异\n- CED 的对比性 margin 过滤掉 distractor-heavy 候选\n- **Research 需要**: flat-NLI scored RSFT ablation（核心实验）\n- **⚠️ Dream 风险**: 三档 Dream 审稿均指出 CED vs flat-NLI 可能不显著（p>0.05）。**Contingency**: 如 plan_001 结果 p>0.05，降级 CED 为\"一种可选 scoring function\"而非核心贡献，论文主贡献重心转移到 Claim 1（首个 evidence-generating LLM for DocRE）和 Claim 3（decoupling phenomenon）\n\n### Claim 3 (Analysis): GRPO+QLoRA 在文档级 IE 上 catastrophic forgetting 且呈现 evidence-extraction decoupling\n- **范围限定**: 仅对 GRPO+QLoRA（非泛化到所有 online RL）——Dream 三档一致指出 overclaim 风险\n- GRPO+QLoRA 在 3 种 reward type × 多个 lr 下全线失败\n- **核心发现 (decoupling)**: evi_f1 在 GRPO 下提升至 0.850（>SFT 0.798）但 rel_f1 崩至 <0.02——RL 差异化优化了 evidence 但摧毁了 extraction\n- RSFT 规避此问题：不修改 policy gradient，只筛选训练数据\n- **MVP 已有完整证据**: D031/D033 GRPO 判死，D039 RSFT 成功\n- **⚠️ Dream 风险**: G=4 太小（标准 G=8-16），需测 G=8 排除 advantage estimation noise 的干扰；LoRA-only 是额外 confound\n\n### Claim 4 (Evaluation): EDCR 作为独立评估指标\n- EDCR = |entity-sharing non-gold cited sentences| / |total cited sentences|\n- Evi-F1 盲区：不惩罚 plausible-looking distractor citations\n- SFT EDCR=71.2%, RSFT+CED EDCR=63.5~66.4%（方向正确但差距有限，需坦诚讨论）\n- **Research 需要**: cross-method diagnostic table, CED vs flat-NLI EDCR 对比\n\n## MVP Evidence Summary\n\n| Config | rel_f1 | Δ rel_f1 | evi_f1 | EDCR | 状态 |\n|--------|--------|----------|--------|------|------|\n| SFT baseline | 0.4057 | — | 0.7979 | 0.7118 | ✅ |\n| RSFT r1 (3ep, α=128, s42) | 0.4449 | +3.92pp | 0.8187 | 0.6565 | ✅ |\n| RSFT r1 (s44) | 0.4655 | +5.98pp | 0.8087 | 0.6350 | ✅ |\n| RSFT r2a (1ep, α=128) | 0.4494 | +4.37pp | 0.8108 | 0.6641 | ✅ |\n| RSFT r2b (1ep, α=32, lr=1e-5) | 0.4493 | +4.36pp | 0.8128 | 0.6609 | ✅ |\n| GRPO best (lr=5e-5, ckpt-90) | 0.2110 | -19.5pp | 0.5750 | — | ❌ |\n| GRPO best (lr=5e-6, ckpt-100) | 0.0138 | -39.2pp | 0.8500 | 0.9900 | ❌ |\n\n## Anticipated Reviewer Concerns\n\n### RC1: NLI reward 信号质量（高概率攻击）\n- **攻击**: \"DeBERTa-v3-base 的 NLI 判断有 lexical overlap bias，CED 训练信号有噪声\"\n- **已验证**: MVP-1 Pearson r=0.34（NLI vs lexical overlap），远低于 0.7，证明非捷径\n- **Research 补充**: DeBERTa-base vs DeBERTa-large 对比\n\n### RC2: Gold evidence 标注不完整导致 false distractor\n- **攻击**: \"被标为 distractor 的句子可能是 annotator 遗漏的有效证据\"\n- **应对**: CED margin 的 self-correcting property——如果 false distractor 真正蕴含关系，其 p_neg 高 → margin 小 → 惩罚弱\n- **Research 补充**: false-distractor 鲁棒性量化分析\n\n### RC3: 评测可比性\n- **攻击**: \"生成式 evidence 如何与 DREEAM 的 attention-based evidence 做 apple-to-apple 对比？\"\n- **应对**: 模型输出显式句子索引 [S_i]，直接映射句子级 Evi-F1；辅助指标用 RoBERTa-large-MNLI（非训练用 DeBERTa）避免 circular evaluation\n\n### RC4: 单数据集 + 单模型泛化性\n- **攻击**: \"只在 DocRED + Qwen3-4B 上验证\"\n- **Research**: Re-DocRED 扩展 + Qwen3-1.7B/8B model size ablation\n\n### RC5: GRPO 配置可能不充分（Dream 三档一致）\n- **攻击**: \"G=4 太小（标准 G=8-16），LoRA-only 是 confound，可能是 GRPO+QLoRA 的问题而非 GRPO 本身\"\n- **应对**: (1) 加 G=8 实验验证（plan_011）；(2) 论文范围限定为 \"GRPO+QLoRA\" 而非 \"online RL\"；(3) 完整轨迹数据仍有效（3 reward × 2 lr × 全 checkpoint）\n- **Research**: GRPO G=8 实验 + 论文标题/claim 措辞调整\n\n### RC6: EDCR 63-66% 仍然偏高，CED 对证据精确度提升有限\n- **攻击**: \"RSFT+CED 的 EDCR 只比 SFT 低 5-8pp，证据质量提升不够显著\"\n- **应对**: (1) CED 在 RSFT 中是间接作用（筛选训练数据），非直接 reward；(2) CED-as-reranker 可能更直接降低 EDCR；(3) 需要 flat-NLI RSFT 对比证明 CED 方向正确\n- **Research**: CED reranker PoC（运行中），top_k ablation\n\n### RC7: 方法过于简单\n- **应对**: 简洁是优点——RSFT 方法论已被证明理论等价于 PPO (ICML 2025)，CED 创新在于打分函数设计而非框架复杂度\n\n### RC8: 缺少中间方法 baseline（Dream 两档一致 [M][W]）\n- **攻击**: \"GRPO(online) vs RSFT(offline) 缺少 DPO/KTO 等中间方法，无法定位失败边界\"\n- **应对**: 加 DPO+CED experiment（plan_012），至少一个中间方法填补 online-offline 光谱\n\n### RC9: EDCR 需要人工验证（Dream 两档一致 [M][W]）\n- **攻击**: \"EDCR 未经人工标注验证，与 Evi-F1 的弱相关 r=-0.42 无法区分信号与噪声\"\n- **应对**: 100 样本人工标注研究（plan_013），验证 EDCR 与人类判断的相关性\n\n### RC10: Evi-F1 评测协议不一致（D041 已确认）\n- **攻击**: \"你们的 Evi-F1 (conditional) 与 DREEAM (joint) 不可比\"\n- **已修复**: 实现 DREEAM 对齐评测函数，论文报告两种 Evi-F1（joint 为主，conditional 为辅）\n\n## Key Baselines (8+)\n\n1. **SFT-only**: Qwen3-4B + LoRA SFT on DocRED gold — 无 RL\n2. **RSFT flat-NLI**: flat-NLI scored RSFT — 无 contrastive signal（核心 ablation）\n3. **RSFT CED (FREIGE)**: CED scored RSFT — 主方法\n4. **CED-as-reranker**: 推理时 CED 重排 SFT 候选（无训练）— 运行中\n5. **GRPO+CED**: 在线 RL with CED reward — negative baseline\n6. **DREEAM**: RoBERTa-large encoder — evidence SOTA (Evi-F1 57.34)\n7. **SAIS**: RoBERTa encoder — evidence baseline (Evi-F1 55.67)\n8. **DocKS-RAG**: GNN+RAG — extraction SOTA (F1 63.59, 无 evidence)\n9. **LMRC**: LLaMA3.1-8B — generative LLM SOTA (F1 60.69, 无 evidence)\n\n## Publishability Threshold\n\n- **必要条件**: RSFT 在 test set 上 Evi-F1_joint（DREEAM 协议）> SFT baseline AND rel_f1 显著 > SFT baseline（D041: Evi-F1 对比 DREEAM 需用对齐协议，暂冻结绝对阈值）\n- **充分条件**: 上述 + CED vs flat-NLI RSFT 差异显著 + GRPO decoupling 分析完整 + EDCR 人工验证\n- **CED contingency**: 如 CED vs flat-NLI p>0.05 → 论文重心转为\"首个 evidence-generating LLM for DocRE + GRPO decoupling phenomenon + EDCR metric\"，CED 降为可选组件\n- **Failure pivot**: RSFT 在 test set 上无显著改进 → 转为 analysis contribution（GRPO failure analysis paper）\n\n## Research Phase Priorities\n\n| Priority | 实验 | Claim/RC | 预估 GPU-hours | Dream 驱动 |\n|----------|------|---------|---------------|-----------|\n| P0 | CED vs flat-NLI RSFT ablation | C2 | ~4h | ⚠️ 三档一致风险 |\n| P0 | Test set evaluation (RSFT best config) | C1 | ~4h | |\n| P0 | Evi-F1 DREEAM 协议对齐 + 重评 | RC10 | ~1h (CPU) | D041 |\n| P0 | EDCR pipeline 验证 + cross-method table | C4 | ~2h | |\n| P0 | DREEAM/SAIS Evi-F1 baseline reproduction | C1 | ~8h | |\n| P0 | GRPO G=8 实验 | C3/RC5 | ~8h | ⚠️ 三档一致 |\n| P1 | CED-as-reranker (running) | C1 bonus | ~6h | |\n| P1 | DPO+CED experiment | RC8 | ~12h | Dream [M][W] |\n| P1 | EDCR 人工标注验证 (100 samples) | RC9/C4 | ~0h (人工) | Dream [M][W] |\n| P1 | Model size ablation (1.7B/8B) | RC4 | ~24h | |\n| P1 | Re-DocRED extension | RC4 | ~12h | |\n| P1 | top_k ablation (k=1 vs k=3) | RC6 | ~8h | |\n| P2 | GRPO forgetting 详细分析 + 可视化 | C3 | ~4h | |\n| P2 | DeBERTa-base vs large NLI 对比 | RC1 | ~4h | |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选\n    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py\n    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set\n    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_003\n  claim: 4\n  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing\n    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_004\n  claim: 1\n  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)\n    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_005\n  claim: 1\n  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: mvp2_ced_reranker_poc\n  status: RUNNING\n- id: plan_006\n  claim: 1\n  description: 'Model size ablation: Qwen3-1.7B 和 Qwen3-8B 上复现 RSFT+CED pipeline，验证方法对模型规模的泛化性。应对\n    RC4。'\n  priority: P1\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Re-DocRED extension: 在 Re-DocRED（修正 false negative 标注的版本）上评估，验证 RSFT+CED\n    在更干净标注下的表现。应对 RC4。'\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  registry_id: null\n  status: planned\n- id: plan_008\n  claim: 2\n  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格\n    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_011\n  claim: 3\n  description: 'GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward\n    + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要\n    gradient_accumulation 适配显存。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_012\n  claim: 3\n  description: 'DPO+CED experiment: Dream [M][W] 指出缺少 online-offline 中间方法 baseline。用\n    RSFT 候选数据构造 preference pairs (CED-preferred vs CED-rejected)，DPO 训练。验证 DPO 是否避免\n    GRPO 的 catastrophic forgetting。'\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_001\n  registry_id: null\n  status: planned\n- id: plan_013\n  claim: 4\n  description: 'EDCR 人工标注验证: 100 个样本，人工判断每个 cited evidence sentence 是否真正支持对应 relation。计算\n    EDCR 与人工判断的相关性，验证 EDCR 作为自动指标的有效性。Dream [M][W] 一致要求。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_009\n  claim: 3\n  description: 'GRPO forgetting 详细分析: 整理全部 GRPO checkpoint 的 rel_f1/evi_f1/EDCR 轨迹，绘制\n    forgetting dynamics 可视化（reward vs task performance 曲线），支撑 Claim 3 的论述。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer\n    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n  status: planned\n- id: plan_mvp1\n  claim: 1\n  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing\n    distractor 的能力验证'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: mvp1_ced_signal\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_margin: 0.48\n    discrimination_accuracy: 0.815\n    pearson_r_margin_jaccard: 0.34\n    pass: true\n- id: plan_mvp2_sft\n  claim: 1\n  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mvp2_sft_warmup\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.72\n    accuracy: 0.835\n- id: plan_mvp2_rsft\n  claim: 1\n  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部\n    PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087,\n    r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_mvp1\n  - plan_mvp2_sft\n  registry_id: mvp2_rsft_train_r1\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.0483\n    num_preds: 848\n    sft_baseline_rel_f1: 0.4057\n    failure_mode: relation_ontology_collapse_to_freetext\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n- id: plan_mvp2_grpo\n  claim: 3\n  description: 'GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1\n    max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic\n    forgetting。D031/D033 完整轨迹支撑 Claim 3'\n  priority: P0\n  gpu_budget_hours: 60\n  deps:\n  - plan_mvp2_sft\n  registry_id: mvp2_grpo_ced_lr5e6_r1\n  status: DONE\n  conclusion: killed\n\n\n## registry (completed experiments)\n\n- exp_id: mvp1_ced_signal\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_margin: 0.48\n    discrimination_accuracy: 0.815\n    pearson_r_margin_jaccard: 0.34\n    pass: true\n- exp_id: smoke_test_grpo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_sft_warmup\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.72\n    accuracy: 0.835\n- exp_id: precompute_nli_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_grpo_ced\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_extract\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_sft_eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_extract_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_r5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: mvp2_grpo_extract_r3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_sft_eval_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    ign_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    precision: 0.4043\n    recall: 0.407\n    evi_precision: 0.8035\n    evi_recall: 0.7924\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.626\n    n_parseable: 617\n    n_truncated: 367\n    n_predictions: 18815\n    inference_time_seconds: 6484.7\n- exp_id: mvp2_sft_eval_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    ign_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    precision: 0.4043\n    recall: 0.407\n    evi_precision: 0.8035\n    evi_recall: 0.7924\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.626\n    n_parseable: 617\n    n_truncated: 367\n    n_predictions: 18815\n- exp_id: mvp2_grpo_ced_kl001_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001_r3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_kl001_r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_step: 100\n    train_runtime_s: 9069.88\n    reward_final: 1.195\n    f1_reward_final: 0.573\n    ced_reward_final: 0.328\n    format_reward_final: 0.293\n    frac_zero_std_final: 0.2\n    kl_final: 0.118\n    loss_final: -0.009\n    grad_norm_final: 0.14\n    entropy_final: 0.067\n    completion_length_mean_final: 520.8\n    best_reward_step: 90\n    best_reward: 1.37\n    best_f1_reward: 0.72\n    best_ced_reward: 0.353\n- exp_id: mvp2_grpo_extract_r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_flatnli_r5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_early\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    f1: 0.1563\n    ign_f1: 0.1563\n    evi_f1: 0.5643\n    edcr: 0.8858\n    precision: 0.2356\n    recall: 0.1169\n    evi_precision: 0.4864\n    evi_recall: 0.6721\n    format_ok_rate: 0.999\n    n_parseable: 984\n    n_truncated: 11\n    n_predictions: 9250\n    tp: 1421\n    pred_count: 6032\n    gold_count: 12151\n- exp_id: mvp2_grpo_flatnli_r6\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    steps_completed: 25\n    final_frac_zero_std: 0.9\n    final_f1_reward: 0\n    final_flat_nli_reward: 0\n    final_format_reward: 0.293\n    collapse_step: 25\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.00296\n    rel_precision: 0.00314\n    rel_recall: 0.0028\n    evi_f1: 0.72\n    evi_precision: 0.6429\n    evi_recall: 0.8182\n    edcr: 0.9983\n    n_parseable: 984\n    n_truncated: 24\n    n_predictions: 11621\n    tp: 34\n    pred_count: 10839\n    gold_count: 12151\n    inference_time_seconds: 5211.4\n- exp_id: mvp2_eval_ced_kl001_r4_multi\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    checkpoint-10:\n      f1: 0.003\n      ign_f1: 0.003\n      evi_f1: 0.72\n      edcr: 0.9983\n      format_ok_rate: 0.999\n    checkpoint-20:\n      f1: 0.0088\n      ign_f1: 0.0088\n      evi_f1: 0.423\n      edcr: 0.9954\n      format_ok_rate: 0.999\n    checkpoint-30:\n      f1: 0.0338\n      ign_f1: 0.0338\n      evi_f1: 0.5889\n      edcr: 0.9798\n      format_ok_rate: 1\n    checkpoint-50:\n      f1: 0.1563\n      ign_f1: 0.1563\n      evi_f1: 0.5643\n      edcr: 0.8858\n      format_ok_rate: 0.999\n    checkpoint-60:\n      f1: 0.1467\n      ign_f1: 0.1467\n      evi_f1: 0.5763\n      edcr: 0.9062\n      format_ok_rate: 1\n    checkpoint-90:\n      f1: 0.2108\n      ign_f1: 0.2108\n      evi_f1: 0.5666\n      edcr: 0.8584\n      format_ok_rate: 1\n- exp_id: mvp2_eval_ced_kl001_r4_step100\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.2167\n    ign_f1: 0.2167\n    precision: 0.2849\n    recall: 0.1749\n    evi_f1: 0.5746\n    evi_precision: 0.5244\n    evi_recall: 0.6353\n    edcr: 0.8539\n    pred_count: 7460\n    gold_count: 12151\n    tp: 2125\n    n_truncated: 21\n    format_ok_rate: 1\n- exp_id: mvp2_eval_ced_kl001_r4_last\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt90\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_high\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    checkpoint_60:\n      rel_f1: 0.1467\n      ign_f1: 0.1467\n      precision: 0.1909\n      recall: 0.1192\n      evi_f1: 0.5763\n      edcr: 0.9062\n      pred_count: 10041\n      gold_count: 12151\n      n_truncated: 16\n      format_ok_rate: 1\n    note: Only ckpt-60 completed. Process died during ckpt-70 inference at 8% (5/62\n      batch). ckpt-80/90 never started.\n- exp_id: mvp2_eval_ced_kl001_r4_step90\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.2108\n    ign_f1: 0.2108\n    evi_f1: 0.5666\n    edcr: 0.8584\n    pred_count: 11160\n    n_truncated: 22\n    format_ok_rate: 1\n    n_documents: 985\n- exp_id: mvp2_grpo_ced_lr5e6_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_p1_r1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_rp_r1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_ced_kl001_r4_ckpt7080\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_grpo_ced_lr5e6_rp_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt20\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0077\n    rel_precision: 0.0071\n    rel_recall: 0.0084\n    evi_f1: 0.628\n    evi_precision: 0.855\n    evi_recall: 0.496\n    edcr: 0.993\n    format_ok_rate: 0.991\n    field_compliance_rate: 0.399\n    pred_count: 14440\n    gold_count: 12151\n    tp: 102\n    n_truncated: 587\n    inference_time_seconds: 6370.4\n- exp_id: mvp2_eval_lr5e6_r1_ckpt40\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt40_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0071\n    precision: 0.0066\n    recall: 0.0078\n    evi_f1: 0.7584\n    evi_precision: 0.9113\n    evi_recall: 0.6494\n    edcr: 0.9942\n    format_ok_rate: 0.9939\n    field_compliance_rate: 0.5675\n    pred_count: 14434\n    gold_count: 12151\n    tp: 95\n    n_truncated: 424\n    inference_time_seconds: 6152\n- exp_id: mvp2_eval_lr5e6_rp_r2_ckpt20\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_sft_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4057\n    evi_f1: 0.7979\n    edcr: 0.7118\n    pred_count: 12234\n    gold_count: 12151\n    format_ok_rate: 0.998\n    format_compliance_rate: 0.998\n    field_compliance_rate: 0.6264\n    n_truncated: 367\n    inference_time_seconds: 6138.5\n- exp_id: mvp2_eval_lr5e6_r1_ckpt60\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_lr5e6_r1_ckpt80\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0116\n    ign_f1: 0.0116\n    precision: 0.0109\n    recall: 0.0124\n    evi_f1: 0.828\n    evi_precision: 0.928\n    evi_recall: 0.748\n    edcr: 0.993\n    format_ok_rate: 0.999\n    field_compliance_rate: 0.788\n    pred_count: 13828\n    gold_count: 12151\n    n_truncated: 210\n    inference_time_seconds: 6099\n- exp_id: mvp2_eval_lr5e6_r1_ckpt60_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0093\n    precision: 0.0085\n    recall: 0.0103\n    evi_f1: 0.81\n    edcr: 0.993\n    format_ok_rate: 0.998\n    pred_count: 14626\n    gold_count: 12151\n    tp: 125\n    inference_time_seconds: 6152\n- exp_id: mvp2_eval_lr5e6_r1_ckpt100\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    rel_f1: 0.0138\n    rel_precision: 0.0132\n    rel_recall: 0.0144\n    ign_f1: 0.0138\n    evi_f1: 0.8504\n    evi_precision: 0.9256\n    evi_recall: 0.7866\n    edcr: 0.9876\n    format_ok_rate: 0.999\n    field_compliance_rate: 0.8162\n    evidence_format_rate: 0.8162\n    tp: 175\n    pred_count: 13300\n    gold_count: 12151\n    n_predictions: 15498\n    n_truncated: 181\n    n_documents: 985\n    n_parseable: 984\n    inference_time_seconds: 5901.7\n- exp_id: mvp2_diversity_probe\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    unique_triples_t07: 5\n    unique_triples_t10: 8\n    jaccard_t07: 0.17\n    jaccard_t10: 0.051\n    format_ok_rate_t07: 0.5\n    format_ok_rate_t10: 0.438\n    n_samples: 3\n    n_generations: 8\n    note: 'unique_triples_t07 corrected from 7 to 5.0 (mean). Reviewer: format_ok\n      ~34% after fix, ''diversity'' was JSON key name variants not semantic diversity'\n- exp_id: mvp2_rsft_generate\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp2_rsft_gen_s3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    generation_count: 5288\n    unique_docs: 659\n    format_compliance: 0.998\n    diversity_range: 7.5-7.8/8\n    exit_code: 0\n- exp_id: mvp2_rsft_ced_scoring\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    input_generations: 21952\n    selected_samples: 2718\n    unique_docs: 2691\n    selection_rate: 0.124\n    mean_f1: 0.6157\n    mean_ced: 0.6683\n    f1_range:\n    - 0.1026\n    - 1\n    zero_f1_samples: 0\n    selection_strategy: top_k=1\n    f1_threshold: 0.1\n- exp_id: mvp2_rsft_train_r1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.0483\n    num_preds: 848\n    sft_baseline_rel_f1: 0.4057\n    failure_mode: relation_ontology_collapse_to_freetext\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n- exp_id: mvp2_rsft_train_r1_s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.7622\n    train_loss: 0.6148\n    eval_entropy: 0.6724\n    mean_token_accuracy: 0.8291\n    total_steps: 510\n    epochs: 3\n    training_hours: 1.99\n- exp_id: mvp2_rsft_train_r1_s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4655\n    evi_f1: 0.8087\n    edcr: 0.635\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0598\n    delta_evi_f1: 0.0108\n    mvp2_pass: true\n- exp_id: mvp2_rsft_ced_scoring_topk3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_ced_reranker_poc\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_rsft_diagnosis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    root_cause: overfitting_plus_sft_knowledge_overwrite\n    truncated_json_samples: 170\n    truncated_pct: 6.3\n    epoch1_eval_loss: 0.756\n    epoch2_eval_loss: 0.759\n    lora_scaling: 2\n    rsft_zero_relation_samples: 170\n    sft_zero_relation_docs: 26\n    rsft_mean_relations: 11.2\n    sft_mean_relations: 12.5\n- exp_id: mvp2_rsft_train_r2_fix\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_rsft_r2a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4494\n    evi_f1: 0.8108\n    edcr: 0.6641\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0437\n    delta_evi_f1: 0.0129\n    mvp2_pass: true\n- exp_id: mvp2_rsft_r2b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4493\n    evi_f1: 0.8128\n    edcr: 0.6609\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0436\n    delta_evi_f1: 0.0149\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4449\n    evi_f1: 0.8187\n    edcr: 0.6565\n    num_preds: 15307\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0392\n    delta_evi_f1: 0.0208\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r2a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4494\n    ign_f1: 0.4494\n    evi_f1: 0.8108\n    edcr: 0.6641\n    precision: 0.4512\n    recall: 0.4475\n    evi_precision: 0.8143\n    evi_recall: 0.8073\n    format_ok_rate: 1\n    n_predictions: 15482\n    n_truncated: 208\n    inference_time_s: 5967.2\n- exp_id: mvp2_eval_rsft_r2b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rel_f1: 0.4493\n    ign_f1: 0.4493\n    evi_f1: 0.8128\n    edcr: 0.6609\n    precision: 0.4566\n    recall: 0.4424\n    evi_precision: 0.8201\n    evi_recall: 0.8056\n    pred_count: 14829\n    format_ok: 983/985\n    truncated: 179\n    inference_time_s: 5862\n- exp_id: mvp2_eval_rsft_s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_s43_r2\n  name: ''\n  status: ANALYZING\n  conclusion: success\n  metrics:\n    rel_f1: 0.4683\n    ign_f1: 0.4683\n    evi_f1: 0.8156\n    edcr: 0.6388\n    precision: 0.4817\n    recall: 0.4556\n    evi_precision: 0.8142\n    evi_recall: 0.817\n    n_predictions: 14970\n    n_truncated: 171\n    format_ok_rate: 1\n    inference_time_s: 6316.7\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    delta_rel_f1: 0.0626\n    delta_evi_f1: 0.0177\n    mvp2_pass: true\n- exp_id: mvp2_eval_rsft_r2b_maxtok1536\n  name: ''\n  status: RUNNING\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp2_eval_rsft_r2b_maxtok1536_r2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp2_rsft_ced_scoring_topk3_r2\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T13:46:00.569Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T13:46:00.569Z",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-15T13:46:00.592Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：RSFT 优势在 test set 上大幅缩水，且 GRPO G=8 部分恢复，核心叙事需要全面 reframe
核心假设：['CED vs flat-NLI 无差异或 flat-NLI 略优（Δevi_f1 < 0.3pp），CED 的对比性设计在 RSFT 间接作用下无可观测效果', 'Test set rel_f1 Δ ≤ +2.0pp over SFT（dev→test 退化 >3pp），可能不显著（p>0.05），dev 增幅存在过拟合成分', 'GRPO G=8 部分恢复（rel_f1 0.15-0.30），说明 G=4 的失败有 advantage noise 成分，Claim 3 需大幅限定范围', 'DPO rel_f1 ≥ 0.35，接近 RSFT，说明 offline 优势不在于 rejection sampling 而在于避免 policy gradient', 'EDCR 与人工判断 r < 0.35，EDCR 作为独立指标的价值存疑']
关键指标范围：{'test_rel_f1_delta_over_sft': [0.5, 2.0], 'ced_vs_flatnli_evi_f1_delta': [-0.5, 0.3], 'ced_vs_flatnli_edcr_delta': [-2.0, 2.0], 'ced_vs_flatnli_p_value': [0.2, 0.8], 'grpo_g8_best_rel_f1': [0.15, 0.3], 'dpo_rel_f1': [0.35, 0.44], 'edcr_human_pearson_r': [0.1, 0.35], 'rsft_best_test_rel_f1': [0.39, 0.43], 'rsft_test_evi_f1_joint': [0.22, 0.3]}
叙事方向：需要全面 reframe，但仍冲 EMNLP Main，不降级目标。Reframe 策略： 论文从 "method paper" 转型为 "analysis + benchmark paper"。 核心叙事变为：对 LLM DocRE 的 evidence generation 进行首次系统性研究， 回答 "哪些 RL/training 策略能让 LLM 在文档级 IE 中生成可验证证据" 这一开放问题。 贡献重组为：(1) 首个 LLM DocRE evidence benchmark（任务定义 + 评测协议 + 多指标框架）； (2) online vs offline RL 的系统对比（GRPO vs DPO vs RSFT，含 G=4/G=8 消融）， 发现不是 online RL 本身失败而是 QLoRA+小 group size 的脆弱组合； (3) evidence 评估指标的局限性分析（Evi-F1 conditional vs joint 的差异 + EDCR 的信号与噪声）。 CED 完全降级为一种 explored scoring function。 需大幅增加实验覆盖（model sizes, datasets）来支撑 "systematic study" 叙事。 投稿可能推迟到 ARR September 或 AAAI 2027 以积累足够实验。

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
  "promptId": "f021ad83-c1a8-458d-9154-bd34a1ce4235",
  "type": "user",
  "uuid": "7a9096f8-7bc5-4ea0-a7c2-eb793fa11a97",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T13:46:00.591Z_

```json
{
  "parentUuid": "7a9096f8-7bc5-4ea0-a7c2-eb793fa11a97",
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
  "uuid": "020c08b3-b304-4b75-9989-ef9f28f38c14",
  "timestamp": "2026-05-15T13:46:00.591Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T13:46:00.591Z_

```json
{
  "parentUuid": "020c08b3-b304-4b75-9989-ef9f28f38c14",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "57a73f66-33d8-4386-9120-84815ceb6354",
  "timestamp": "2026-05-15T13:46:00.591Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：RSFT 优势在 test set 上大幅缩水，且 GRPO G=8 部分恢复，核心叙事需要全面 reframe 核心假设：['CED vs flat-NLI 无差异或 flat-NLI 略优（Δevi_f1 < 0.3pp），CED 的对比性设计在 RSFT 间接作用下无可观测效果', 'Test set…",
  "leafUuid": "57a73f66-33d8-4386-9120-84815ceb6354",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Systematic LLM evidence generation for DocRE under worst-case outcomes",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e"
}
```

---

### Assistant

_source line 8 · 2026-05-15T13:46:04.429Z_

I'll review the experiment plan and memory to understand the full context before generating predictions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57a73f66-33d8-4386-9120-84815ceb6354",
  "isSidechain": false,
  "requestId": "req_011Cb4TSBVkX4NyLiRXP9vNs",
  "type": "assistant",
  "uuid": "e559d343-25ef-4833-a4fe-172541de4bff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CdvXtWdWEPhU2imu55TvEJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20967,
      "cache_read_input_tokens": 11841,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20967,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 181,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20967
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

_source line 9 · 2026-05-15T13:46:05.862Z_

<details open><summary>🔧 Tool call — Read · `toolu_012yPnwtj6Cu1vXwVDDf82YC`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6/memory/MEMORY.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e559d343-25ef-4833-a4fe-172541de4bff",
  "isSidechain": false,
  "requestId": "req_011Cb4TSBVkX4NyLiRXP9vNs",
  "type": "assistant",
  "uuid": "8e0e159d-6c01-4faf-9eb7-eab76a65c98d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CdvXtWdWEPhU2imu55TvEJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20967,
      "cache_read_input_tokens": 11841,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20967,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 181,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20967
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

_source line 10 · 2026-05-15T13:46:05.875Z_

<details><summary>↩ Tool result · reported error · `toolu_012yPnwtj6Cu1vXwVDDf82YC`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e0e159d-6c01-4faf-9eb7-eab76a65c98d",
  "isSidechain": false,
  "promptId": "f021ad83-c1a8-458d-9154-bd34a1ce4235",
  "type": "user",
  "uuid": "47740d7e-6780-4dca-99cb-6402c8864e66",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6.",
  "sourceToolAssistantUUID": "8e0e159d-6c01-4faf-9eb7-eab76a65c98d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T13:46:06.520Z_

<details><summary>↩ Tool result · `toolu_01XX9fpGsxhnirxTu4zw1DyB`</summary>

```text
config/approvals.yaml
config/feishu.yaml
workspace.yaml
config/backend.yaml
idea_generator/ideas.yaml
config/secrets/faith-evidence-ie/manifest.yaml
projects/faith-evidence-ie/artifacts/freige/configs/accelerate_4gpu.yaml
global/approvals.yaml
config/pending_approval_notifications.yaml
global/registry.yaml
projects/faith-evidence-ie/literature_map.yaml
projects/faith-evidence-ie/artifacts/manifest.yaml
projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/imagined_experiments.yaml
projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/imagined_experiments.yaml
projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/worst/imagined_experiments.yaml
config/projects/faith-evidence-ie.yaml
projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/review_context.yaml
projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/review_context.yaml
projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/worst/review_context.yaml
projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/meta.yaml
projects/faith-evidence-ie/experiment_plan.yaml
projects/faith-evidence-ie/dream_registry.yaml
projects/faith-evidence-ie/registry.yaml
config/resources.yaml
projects/faith-evidence-ie/decisions.yaml
config/crons.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14725fd5-d30c-4228-959a-1c2e49da4d94",
  "isSidechain": false,
  "promptId": "f021ad83-c1a8-458d-9154-bd34a1ce4235",
  "type": "user",
  "uuid": "c826f03a-e18a-4d2f-96da-0cb151ed812d",
  "toolUseResult": {
    "filenames": [
      "config/approvals.yaml",
      "config/feishu.yaml",
      "workspace.yaml",
      "config/backend.yaml",
      "idea_generator/ideas.yaml",
      "config/secrets/faith-evidence-ie/manifest.yaml",
      "projects/faith-evidence-ie/artifacts/freige/configs/accelerate_4gpu.yaml",
      "global/approvals.yaml",
      "config/pending_approval_notifications.yaml",
      "global/registry.yaml",
      "projects/faith-evidence-ie/literature_map.yaml",
      "projects/faith-evidence-ie/artifacts/manifest.yaml",
      "projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/imagined_experiments.yaml",
      "projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/imagined_experiments.yaml",
      "projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/worst/imagined_experiments.yaml",
      "config/projects/faith-evidence-ie.yaml",
      "projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/review_context.yaml",
      "projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/review_context.yaml",
      "projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/worst/review_context.yaml",
      "projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/meta.yaml",
      "projects/faith-evidence-ie/experiment_plan.yaml",
      "projects/faith-evidence-ie/dream_registry.yaml",
      "projects/faith-evidence-ie/registry.yaml",
      "config/resources.yaml",
      "projects/faith-evidence-ie/decisions.yaml",
      "config/crons.yaml"
    ],
    "durationMs": 15,
    "numFiles": 26,
    "truncated": false
  },
  "sourceToolAssistantUUID": "14725fd5-d30c-4228-959a-1c2e49da4d94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T13:46:06.498Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XX9fpGsxhnirxTu4zw1DyB`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47740d7e-6780-4dca-99cb-6402c8864e66",
  "isSidechain": false,
  "requestId": "req_011Cb4TSBVkX4NyLiRXP9vNs",
  "type": "assistant",
  "uuid": "14725fd5-d30c-4228-959a-1c2e49da4d94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CdvXtWdWEPhU2imu55TvEJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20967,
      "cache_read_input_tokens": 11841,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20967,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 181,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20967
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

_source line 13 · 2026-05-15T13:46:09.828Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Et65n1fPvfwS8fe7TdZonx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c826f03a-e18a-4d2f-96da-0cb151ed812d",
  "isSidechain": false,
  "requestId": "req_011Cb4TScyBrNUEhCxphgRwk",
  "type": "assistant",
  "uuid": "1bb39ed4-fe13-41f9-80e4-6a2c69ea2f3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UzKp1Xy1nsjXUcxhHo37EN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 32808,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 32808,
          "cache_creation_input_tokens": 685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 685
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

_source line 14 · 2026-05-15T13:46:09.856Z_

<details><summary>↩ Tool result · `toolu_01Et65n1fPvfwS8fe7TdZonx`</summary>

```text
1	experiments:
2	  # ── P0: 核心实验（必跑，论文 headline results） ──
3	
4	  - id: plan_001
5	    claim: 2
6	    description: "CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选 RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py 用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。"
7	    priority: P0
8	    gpu_budget_hours: 20
9	    deps: []
10	    registry_id: null
11	
12	  - id: plan_002
13	    claim: 1
14	    description: "Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set 上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。"
15	    priority: P0
16	    gpu_budget_hours: 4
17	    deps: [plan_001]
18	    registry_id: null
19	
20	  - id: plan_003
21	    claim: 4
22	    description: "EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing 方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。"
23	    priority: P0
24	    gpu_budget_hours: 2
25	    deps: [plan_001]
26	    registry_id: null
27	
28	  - id: plan_004
29	    claim: 1
30	    description: "DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large) 的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。"
31	    priority: P0
32	    gpu_budget_hours: 8
33	    deps: []
34	    registry_id: null
35	
36	  # ── P1: 重要补充（增强论文，时间紧可延后） ──
37	
38	  - id: plan_005
39	    claim: 1
40	    description: "CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。"
41	    priority: P1
42	    gpu_budget_hours: 6
43	    deps: []
44	    registry_id: mvp2_ced_reranker_poc
45	
46	  - id: plan_006
47	    claim: 1
48	    description: "Model size ablation: Qwen3-1.7B 和 Qwen3-8B 上复现 RSFT+CED pipeline，验证方法对模型规模的泛化性。应对 RC4。"
49	    priority: P1
50	    gpu_budget_hours: 24
51	    deps: [plan_001]
52	    registry_id: null
53	
54	  - id: plan_007
55	    claim: 1
56	    description: "Re-DocRED extension: 在 Re-DocRED（修正 false negative 标注的版本）上评估，验证 RSFT+CED 在更干净标注下的表现。应对 RC4。"
57	    priority: P1
58	    gpu_budget_hours: 12
59	    deps: [plan_002]
60	    registry_id: null
61	
62	  - id: plan_008
63	    claim: 2
64	    description: "top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格 ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。"
65	    priority: P1
66	    gpu_budget_hours: 8
67	    deps: []
68	    registry_id: null
69	
70	  # ── Dream 驱动新增实验 ──
71	
72	  - id: plan_011
73	    claim: 3
74	    description: "GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要 gradient_accumulation 适配显存。"
75	    priority: P0
76	    gpu_budget_hours: 8
77	    deps: []
78	    registry_id: null
79	
80	  - id: plan_012
81	    claim: 3
82	    description: "DPO+CED experiment: Dream [M][W] 指出缺少 online-offline 中间方法 baseline。用 RSFT 候选数据构造 preference pairs (CED-preferred vs CED-rejected)，DPO 训练。验证 DPO 是否避免 GRPO 的 catastrophic forgetting。"
83	    priority: P1
84	    gpu_budget_hours: 12
85	    deps: [plan_001]
86	    registry_id: null
87	
88	  - id: plan_013
89	    claim: 4
90	    description: "EDCR 人工标注验证: 100 个样本，人工判断每个 cited evidence sentence 是否真正支持对应 relation。计算 EDCR 与人工判断的相关性，验证 EDCR 作为自动指标的有效性。Dream [M][W] 一致要求。"
91	    priority: P1
92	    gpu_budget_hours: 0
93	    deps: []
94	    registry_id: null
95	
96	  # ── P2: 加分项（有余力时做） ──
97	
98	  - id: plan_009
99	    claim: 3
100	    description: "GRPO forgetting 详细分析: 整理全部 GRPO checkpoint 的 rel_f1/evi_f1/EDCR 轨迹，绘制 forgetting dynamics 可视化（reward vs task performance 曲线），支撑 Claim 3 的论述。"
101	    priority: P2
102	    gpu_budget_hours: 4
103	    deps: []
104	    registry_id: null
105	
106	  - id: plan_010
107	    claim: 1
108	    description: "NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer 的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。"
109	    priority: P2
110	    gpu_budget_hours: 4
111	    deps: []
112	    registry_id: null
113	
114	  # ── MVP 已完成实验（关联 registry） ──
115	
116	  - id: plan_mvp1
117	    claim: 1
118	    description: "MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing distractor 的能力验证"
119	    priority: P0
120	    gpu_budget_hours: 1
121	    deps: []
122	    registry_id: mvp1_ced_signal
123	
124	  - id: plan_mvp2_sft
125	    claim: 1
126	    description: "SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线"
127	    priority: P0
128	    gpu_budget_hours: 4
129	    deps: []
130	    registry_id: mvp2_sft_warmup
131	
132	  - id: plan_mvp2_rsft
133	    claim: 1
134	    description: "RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部 PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087, r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128"
135	    priority: P0
136	    gpu_budget_hours: 20
137	    deps: [plan_mvp1, plan_mvp2_sft]
138	    registry_id: mvp2_rsft_train_r1
139	
140	  - id: plan_mvp2_grpo
141	    claim: 3
142	    description: "GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1 max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic forgetting。D031/D033 完整轨迹支撑 Claim 3"
143	    priority: P0
144	    gpu_budget_hours: 60
145	    deps: [plan_mvp2_sft]
146	    registry_id: mvp2_grpo_ced_lr5e6_r1
147	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bb39ed4-fe13-41f9-80e4-6a2c69ea2f3d",
  "isSidechain": false,
  "promptId": "f021ad83-c1a8-458d-9154-bd34a1ce4235",
  "type": "user",
  "uuid": "992dcbad-709f-4dae-86fb-d250dbf74e28",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
      "content": "experiments:\n  # ── P0: 核心实验（必跑，论文 headline results） ──\n\n  - id: plan_001\n    claim: 2\n    description: \"CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选 RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py 用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。\"\n    priority: P0\n    gpu_budget_hours: 20\n    deps: []\n    registry_id: null\n\n  - id: plan_002\n    claim: 1\n    description: \"Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set 上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。\"\n    priority: P0\n    gpu_budget_hours: 4\n    deps: [plan_001]\n    registry_id: null\n\n  - id: plan_003\n    claim: 4\n    description: \"EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing 方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。\"\n    priority: P0\n    gpu_budget_hours: 2\n    deps: [plan_001]\n    registry_id: null\n\n  - id: plan_004\n    claim: 1\n    description: \"DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large) 的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。\"\n    priority: P0\n    gpu_budget_hours: 8\n    deps: []\n    registry_id: null\n\n  # ── P1: 重要补充（增强论文，时间紧可延后） ──\n\n  - id: plan_005\n    claim: 1\n    description: \"CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。\"\n    priority: P1\n    gpu_budget_hours: 6\n    deps: []\n    registry_id: mvp2_ced_reranker_poc\n\n  - id: plan_006\n    claim: 1\n    description: \"Model size ablation: Qwen3-1.7B 和 Qwen3-8B 上复现 RSFT+CED pipeline，验证方法对模型规模的泛化性。应对 RC4。\"\n    priority: P1\n    gpu_budget_hours: 24\n    deps: [plan_001]\n    registry_id: null\n\n  - id: plan_007\n    claim: 1\n    description: \"Re-DocRED extension: 在 Re-DocRED（修正 false negative 标注的版本）上评估，验证 RSFT+CED 在更干净标注下的表现。应对 RC4。\"\n    priority: P1\n    gpu_budget_hours: 12\n    deps: [plan_002]\n    registry_id: null\n\n  - id: plan_008\n    claim: 2\n    description: \"top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格 ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。\"\n    priority: P1\n    gpu_budget_hours: 8\n    deps: []\n    registry_id: null\n\n  # ── Dream 驱动新增实验 ──\n\n  - id: plan_011\n    claim: 3\n    description: \"GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要 gradient_accumulation 适配显存。\"\n    priority: P0\n    gpu_budget_hours: 8\n    deps: []\n    registry_id: null\n\n  - id: plan_012\n    claim: 3\n    description: \"DPO+CED experiment: Dream [M][W] 指出缺少 online-offline 中间方法 baseline。用 RSFT 候选数据构造 preference pairs (CED-preferred vs CED-rejected)，DPO 训练。验证 DPO 是否避免 GRPO 的 catastrophic forgetting。\"\n    priority: P1\n    gpu_budget_hours: 12\n    deps: [plan_001]\n    registry_id: null\n\n  - id: plan_013\n    claim: 4\n    description: \"EDCR 人工标注验证: 100 个样本，人工判断每个 cited evidence sentence 是否真正支持对应 relation。计算 EDCR 与人工判断的相关性，验证 EDCR 作为自动指标的有效性。Dream [M][W] 一致要求。\"\n    priority: P1\n    gpu_budget_hours: 0\n    deps: []\n    registry_id: null\n\n  # ── P2: 加分项（有余力时做） ──\n\n  - id: plan_009\n    claim: 3\n    description: \"GRPO forgetting 详细分析: 整理全部 GRPO checkpoint 的 rel_f1/evi_f1/EDCR 轨迹，绘制 forgetting dynamics 可视化（reward vs task performance 曲线），支撑 Claim 3 的论述。\"\n    priority: P2\n    gpu_budget_hours: 4\n    deps: []\n    registry_id: null\n\n  - id: plan_010\n    claim: 1\n    description: \"NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer 的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。\"\n    priority: P2\n    gpu_budget_hours: 4\n    deps: []\n    registry_id: null\n\n  # ── MVP 已完成实验（关联 registry） ──\n\n  - id: plan_mvp1\n    claim: 1\n    description: \"MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing distractor 的能力验证\"\n    priority: P0\n    gpu_budget_hours: 1\n    deps: []\n    registry_id: mvp1_ced_signal\n\n  - id: plan_mvp2_sft\n    claim: 1\n    description: \"SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线\"\n    priority: P0\n    gpu_budget_hours: 4\n    deps: []\n    registry_id: mvp2_sft_warmup\n\n  - id: plan_mvp2_rsft\n    claim: 1\n    description: \"RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部 PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087, r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128\"\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [plan_mvp1, plan_mvp2_sft]\n    registry_id: mvp2_rsft_train_r1\n\n  - id: plan_mvp2_grpo\n    claim: 3\n    description: \"GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1 max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic forgetting。D031/D033 完整轨迹支撑 Claim 3\"\n    priority: P0\n    gpu_budget_hours: 60\n    deps: [plan_mvp2_sft]\n    registry_id: mvp2_grpo_ced_lr5e6_r1\n",
      "numLines": 147,
      "startLine": 1,
      "totalLines": 147
    }
  },
  "sourceToolAssistantUUID": "1bb39ed4-fe13-41f9-80e4-6a2c69ea2f3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T13:46:10.162Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DnyNrfrdaPoKSLEQnmTT4U`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/worst/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "992dcbad-709f-4dae-86fb-d250dbf74e28",
  "isSidechain": false,
  "requestId": "req_011Cb4TScyBrNUEhCxphgRwk",
  "type": "assistant",
  "uuid": "c6c5f96e-2977-4b54-8431-1bd32ca20e53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UzKp1Xy1nsjXUcxhHo37EN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 32808,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 32808,
          "cache_creation_input_tokens": 685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 685
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

_source line 16 · 2026-05-15T13:46:10.170Z_

<details><summary>↩ Tool result · `toolu_01DnyNrfrdaPoKSLEQnmTT4U`</summary>

```text
1	tier: worst
2	narrative_guidance: 'CED 作为方法创新的叙事不成立，必须 reframe。新 angle："Why does online RL catastrophically
3	  fail for structured IE, and what works instead?"——将 GRPO 全线失败升级为核心 contribution，RSFT
4	  作为 "what works" 的解法存在但不再强调 CED 独特性。EDCR 升级为独立 contribution。仍冲 EMNLP Main analysis
5	  track。
6	
7	  '
8	imagined_experiments:
9	- name: CED vs flat-NLI RSFT ablation
10	  plan_id: plan_001
11	  description: '用 flat-NLI scoring 筛选 RSFT 训练数据，与 CED scoring 做 head-to-head 对比。 复用已有
12	    candidates，仅替换打分函数为 p_pos（无 contrastive margin）。
13	
14	    '
15	  expected_results:
16	    flatnli_rsft_rel_f1: 0.452
17	    flatnli_rsft_evi_f1: 0.8105
18	    flatnli_rsft_edcr: 0.662
19	    flatnli_rsft_selected_samples: 2850
20	    ced_rsft_best_rel_f1: 0.4655
21	    ced_rsft_best_evi_f1: 0.8087
22	    ced_rsft_best_edcr: 0.635
23	    ced_vs_flatnli_rel_f1_gap: 0.0135
24	    ced_vs_flatnli_evi_f1_gap: -0.0018
25	    ced_vs_flatnli_edcr_gap: -0.027
26	    paired_bootstrap_p_evi_f1: 0.38
27	    paired_bootstrap_p_edcr: 0.12
28	  result_rationale: '在 worst 档下，flat-NLI 的 p_pos 阈值筛选出的候选与 CED margin 筛选出的候选高度重叠 （Jaccard
29	    ~0.75）。原因：DocRED 中 entity-sharing distractor 的 NLI 分数分布与 gold evidence 有足够间距（MVP-1
30	    mean_margin=0.48），使得即使不做 contrastive 对比， 单纯高 p_pos 阈值也能过滤掉大部分 distractor。CED 的
31	    margin 机制在"容易"的 distractor 上无额外区分力，仅在 hard negative（p_neg > 0.6 的 distractor）上有优势，但这类样本
32	    占比 <15%。结果：evi_f1 gap 仅 -0.18pp（CED 甚至略低，因 margin 过滤过于严格导致 训练数据略少），EDCR gap -2.7pp
33	    方向正确但 p=0.12 不显著。Claim 2 核心假设—— "CED 的对比性 margin 提供额外信息"——统计上不成立。
34	
35	    '
36	  tables:
37	  - name: 'Table: CED vs flat-NLI RSFT Head-to-Head (Dev Set)'
38	    rows:
39	    - config: SFT baseline
40	      rel_f1: 0.4057
41	      evi_f1: 0.7979
42	      edcr: 0.7118
43	    - config: RSFT flat-NLI (best)
44	      rel_f1: 0.452
45	      evi_f1: 0.8105
46	      edcr: 0.662
47	    - config: RSFT CED r1 (s42)
48	      rel_f1: 0.4449
49	      evi_f1: 0.8187
50	      edcr: 0.6565
51	    - config: RSFT CED r1 (s44)
52	      rel_f1: 0.4655
53	      evi_f1: 0.8087
54	      edcr: 0.635
55	    - config: Δ (CED best − flat-NLI)
56	      rel_f1: +1.35pp
57	      evi_f1: −0.18pp
58	      edcr: −2.70pp
59	    - config: p-value (paired bootstrap)
60	      rel_f1: '0.08'
61	      evi_f1: '0.38'
62	      edcr: '0.12'
63	  figures_description:
64	  - 'Scatter plot: per-document Evi-F1 差异 (CED − flat-NLI)，大部分文档集中在 ±0.02 区间，仅少数 hard-negative-heavy
65	    文档 CED 明显优于 flat-NLI'
66	  analysis: 'CED 与 flat-NLI 无统计显著差异。CED 的 contrastive margin 仅在 hard negative 密集的
67	    文档子集上有边际优势，但全局来看两种 scoring 等价。这意味着 RSFT 的收益主要来自 rejection sampling 本身（过滤低质量候选），而非
68	    CED 特有的对比信号。Claim 2 需要 降级为 negative result 或合并到方法 ablation 中。
69	
70	    '
71	- name: Test set evaluation
72	  plan_id: plan_002
73	  description: '用 RSFT best config (s44) 在 DocRED test set 上评估，提交 CodaLab 获取官方 F1，
74	    本地计算 Evi-F1 和 EDCR。
75	
76	    '
77	  expected_results:
78	    test_rel_f1: 0.392
79	    test_ign_f1: 0.385
80	    test_evi_f1: 0.765
81	    test_edcr: 0.685
82	    test_precision: 0.398
83	    test_recall: 0.3865
84	    dev_to_test_rel_f1_drop: -0.0735
85	    dev_to_test_evi_f1_drop: -0.0437
86	    sft_test_rel_f1: 0.355
87	    sft_test_evi_f1: 0.752
88	    rsft_over_sft_test_rel_f1_gap: 0.037
89	    rsft_over_sft_test_evi_f1_gap: 0.013
90	  result_rationale: 'Dev→test 严重衰减是 worst 档的核心假设。DocRED test set 的标注分布与 dev set 存在
91	    已知偏移（test set annotator 更保守，relation 密度更低，evidence 链更短）。RSFT 在 dev set 上的优势部分来自对
92	    dev set 分布的过拟合——训练数据生成和 CED 打分均在 dev set 文档的 train split 上进行，候选筛选隐式适应了 train/dev
93	    的共享分布特征。Test set 的 unseen annotator 风格导致 rel_f1 从 0.4655 降至 0.3920（-7.35pp），evi_f1
94	    从 0.8087 降至 0.7650（-4.37pp）。EDCR 从 0.635 升至 0.685，因 test set 的 entity 分布更密集，distractor
95	    句子更多。rel_f1 仍高于 SFT baseline（+3.7pp），但绝对值 远低于 dev set 表现。evi_f1 0.765 虽仍远超 DREEAM
96	    的 57.34，但这个对比因评估 协议差异（生成式 vs attention-based）可能被 reviewer 质疑。
97	
98	    '
99	  tables:
100	  - name: 'Table: Dev vs Test Set Performance (RSFT s44)'
101	    rows:
102	    - split: Dev
103	      rel_f1: 0.4655
104	      evi_f1: 0.8087
105	      edcr: 0.635
106	    - split: Test
107	      rel_f1: 0.392
108	      evi_f1: 0.765
109	      edcr: 0.685
110	    - split: Δ (test − dev)
111	      rel_f1: −7.35pp
112	      evi_f1: −4.37pp
113	      edcr: +5.00pp
114	  - name: 'Table: Test Set Comparison (SFT vs RSFT)'
115	    rows:
116	    - method: SFT baseline
117	      rel_f1: 0.355
118	      evi_f1: 0.752
119	      edcr: 0.728
120	    - method: RSFT+CED (s44)
121	      rel_f1: 0.392
122	      evi_f1: 0.765
123	      edcr: 0.685
124	  figures_description:
125	  - 'Bar chart: Dev vs Test performance drop per metric，突出 rel_f1 的 15.8% 相对衰减'
126	  analysis: 'Test set 上 RSFT 仍优于 SFT，但 margin 缩窄。rel_f1 的相对衰减率 15.8% 高于典型 DocRE 方法（ATLOP
127	    约 5-8%），暗示 RSFT 对 dev set 分布有一定过拟合。EDCR 在 test set 上恶化，说明 test set 文档的 entity
128	    共现密度更高，distractor 问题更严重。 Publishability threshold 的必要条件（Evi-F1 > 57.34）仍满足，但 reviewer
129	    可能 质疑跨评估协议的可比性。
130	
131	    '
132	- name: EDCR pipeline 验证 + cross-method diagnostic table
133	  plan_id: plan_003
134	  description: '在所有 evidence-producing 方法上计算 EDCR，验证 EDCR 作为独立诊断指标的能力。
135	
136	    '
137	  expected_results:
138	    sft_edcr: 0.7118
139	    rsft_ced_best_edcr: 0.635
140	    rsft_flatnli_edcr: 0.662
141	    reranker_edcr: 0.665
142	    grpo_best_edcr: 0.8584
143	    ced_vs_flatnli_edcr_gap: -0.027
144	    edcr_evi_f1_correlation: -0.42
145	  result_rationale: '在 worst 档下，EDCR 的 cross-method 诊断能力被削弱。CED RSFT 与 flat-NLI RSFT
146	    的 EDCR 差异仅 2.7pp（方向正确但不显著），说明 CED 对 distractor 的过滤优势有限。 Reranker 的 EDCR（0.665）与
147	    RSFT flat-NLI 接近，因推理时 CED 重排仅能在 SFT 已生成的候选中选择，而 SFT 候选本身就包含大量 distractor。EDCR
148	    与 Evi-F1 的负相关 只有 r=-0.42（弱到中等），无法有力论证 "Evi-F1 的盲区"——部分高 EDCR 样本的 Evi-F1 也不高，两个指标部分重叠。EDCR
149	    作为独立 contribution 仍有价值（提出新维度），但 "CED 改善 EDCR" 的方法论故事很弱。
150	
151	    '
152	  tables:
153	  - name: 'Table: Cross-Method EDCR Diagnostic'
154	    rows:
155	    - method: GRPO+CED (ckpt-90)
156	      evi_f1: 0.5666
157	      edcr: 0.8584
158	      note: catastrophic forgetting
159	    - method: SFT baseline
160	      evi_f1: 0.7979
161	      edcr: 0.7118
162	      note: —
163	    - method: RSFT flat-NLI
164	      evi_f1: 0.8105
165	      edcr: 0.662
166	      note: —
167	    - method: CED-as-reranker
168	      evi_f1: 0.801
169	      edcr: 0.665
170	      note: inference-time only
171	    - method: RSFT+CED (s44)
172	      evi_f1: 0.8087
173	      edcr: 0.635
174	      note: best EDCR
175	  figures_description:
176	  - Evi-F1 vs EDCR scatter plot（per-document level），标注各方法的 centroid，展示两指标的弱负相关
177	  analysis: 'EDCR 作为诊断工具确实揭示了 Evi-F1 不能捕捉的 distractor citation 问题（GRPO 的 evi_f1=0.567
178	    但 EDCR=0.858 是极端案例）。但 CED 对 EDCR 的改善幅度有限（vs flat-NLI 仅 2.7pp），且 EDCR 绝对值仍然偏高（63.5%
179	    的被引证据仍是 distractor）， reviewer 可能质疑方法的实际影响力。Reframe: EDCR 的 contribution 在于指标设计
180	    本身，而非 CED 对 EDCR 的改善。
181	
182	    '
183	- name: DREEAM baseline reproduction
184	  plan_id: plan_004
185	  description: '在 DocRED dev set 上复现 DREEAM (RoBERTa-large) 的 Evi-F1，验证 57.34 是否可复现。
186	
187	    '
188	  expected_results:
189	    dreeam_dev_evi_f1_reproduced: 0.608
190	    dreeam_dev_rel_f1_reproduced: 0.632
191	    dreeam_paper_evi_f1: 0.5734
192	    dreeam_paper_rel_f1: 0.63
193	    reproduction_evi_f1_gap: 0.0346
194	    sais_dev_evi_f1_reproduced: 0.578
195	  result_rationale: 'DREEAM 论文报告的 57.34 是 test set Evi-F1，非 dev set。在 worst 档下，dev
196	    set 复现值为 60.8，显著高于论文 test set 数字。这产生两个问题：(1) 我们的 RSFT dev Evi-F1 80.87 与 DREEAM
197	    dev 60.8 的对比仍然成立（+20pp），但这是跨评估协议对比 （生成式句子索引 vs attention-based sentence extraction），reviewer
198	    可能质疑 apple-to-orange；(2) 如果 DREEAM dev 60.8 但 test 57.34，说明 encoder 方法也有 dev→test
199	    衰减，但我们的衰减幅度更大（-4.37pp vs -3.46pp），暗示生成式方法对 数据分布更敏感。更关键的是，复现值高于报告值会让 reviewer 质疑我们的评估
200	    pipeline 是否与 DREEAM 完全可比——可能存在句子分割、证据匹配阈值等微妙差异。
201	
202	    '
203	  tables:
204	  - name: 'Table: DREEAM/SAIS Reproduction vs Reported'
205	    rows:
206	    - method: DREEAM (paper, test)
207	      rel_f1: 0.63
208	      evi_f1: 0.5734
209	    - method: DREEAM (reproduced, dev)
210	      rel_f1: 0.632
211	      evi_f1: 0.608
212	    - method: SAIS (reproduced, dev)
213	      rel_f1: 0.615
214	      evi_f1: 0.578
215	    - method: RSFT+CED (dev)
216	      rel_f1: 0.4655
217	      evi_f1: 0.8087
218	  figures_description: []
219	  analysis: '复现值与报告值的偏差（+3.46pp）引入评估可比性疑虑。必须在论文中详细说明评估协议 差异（evidence 粒度、匹配方式），并承认跨范式对比的局限性。这削弱了
220	    Claim 1 中 "超越 DREEAM" 的叙事力度，但不致命——20pp 的 dev set 优势即使打折仍然 substantial。
221	
222	    '
223	- name: CED-as-reranker
224	  plan_id: plan_005
225	  description: '推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。
226	
227	    '
228	  expected_results:
229	    reranker_rel_f1: 0.415
230	    reranker_evi_f1: 0.801
231	    reranker_edcr: 0.665
232	    sft_baseline_rel_f1: 0.4057
233	    sft_baseline_evi_f1: 0.7979
234	    sft_baseline_edcr: 0.7118
235	    reranker_over_sft_rel_f1: 0.0093
236	    reranker_over_sft_evi_f1: 0.0031
237	    reranker_over_sft_edcr: -0.0468
238	    reranker_inference_time_multiplier: 8.5
239	  result_rationale: '在 worst 档下，reranker 的 EDCR 改善有限（-4.68pp vs SFT）且远不及 RSFT（-7.68pp）。
240	    原因：CED 重排只能在 SFT 已生成的 8 个候选中选择，而 SFT 候选的 evidence 分布本身 就偏向 distractor——8 个候选中
241	    "低 EDCR" 的候选可能根本不存在（SFT 的 systematic bias 使所有候选都引用类似的 distractor 句子）。Rel_f1 微升（+0.93pp）因为
242	    CED 兼顾了 evidence 质量和抽取质量的联合打分，但提升幅度小。推理时间 8.5x（每个候选 都需要 NLI 推理）是实际部署的障碍。Reranker
243	    作为 "training-free baseline" 有方法论 价值，但在 worst 档下不构成独立 contribution。
244	
245	    '
246	  tables:
247	  - name: 'Table: CED-as-Reranker vs SFT vs RSFT (Dev Set)'
248	    rows:
249	    - method: SFT baseline
250	      rel_f1: 0.4057
251	      evi_f1: 0.7979
252	      edcr: 0.7118
253	      extra_train: 'No'
254	    - method: CED-as-reranker (N=8)
255	      rel_f1: 0.415
256	      evi_f1: 0.801
257	      edcr: 0.665
258	      extra_train: 'No'
259	    - method: RSFT+CED (s44)
260	      rel_f1: 0.4655
261	      evi_f1: 0.8087
262	      edcr: 0.635
263	      extra_train: 'Yes'
264	  figures_description:
265	  - EDCR 分布直方图：SFT 8 候选的 EDCR 分布，展示 reranker 的 selection ceiling——最优候选的 EDCR 仍然偏高
266	  analysis: 'Reranker 效果有限，印证 SFT 候选池本身的 distractor bias 是 bottleneck。RSFT 通过 改变模型权重从根源减少
267	    distractor 引用，reranker 只能在已有候选中做选择。在 worst 档下，reranker 降级为 ablation 中的一行数据，不再作为独立方法。
268	
269	    '
270	- name: Model size ablation (1.7B / 8B)
271	  plan_id: plan_006
272	  description: 'Qwen3-1.7B 和 Qwen3-8B 上复现 RSFT+CED pipeline，验证方法对模型规模的泛化性。
273	
274	    '
275	  expected_results:
276	    qwen3_1_7b_sft_rel_f1: 0.312
277	    qwen3_1_7b_sft_evi_f1: 0.735
278	    qwen3_1_7b_rsft_ced_rel_f1: 0.338
279	    qwen3_1_7b_rsft_ced_evi_f1: 0.752
280	    qwen3_1_7b_rsft_ced_edcr: 0.705
281	    qwen3_8b_sft_rel_f1: 0.458
282	    qwen3_8b_sft_evi_f1: 0.82
283	    qwen3_8b_rsft_ced_rel_f1: 0.475
284	    qwen3_8b_rsft_ced_evi_f1: 0.828
285	    qwen3_8b_rsft_ced_edcr: 0.648
286	    rsft_gain_1_7b_rel_f1: 0.026
287	    rsft_gain_4b_rel_f1: 0.0598
288	    rsft_gain_8b_rel_f1: 0.017
289	  result_rationale: '在 worst 档下，model size ablation 暴露 RSFT 收益的不稳定性。1.7B 模型的 SFT baseline
290	    较弱（rel_f1 0.312），RSFT 提升 +2.6pp——绝对收益小，因小模型生成候选 的质量上限低，CED 筛选后的训练数据量骤降（可能仅 ~1200
291	    samples vs 4B 的 2718）。 8B 模型的 SFT baseline 已较强（0.458），RSFT 仅提升 +1.7pp——边际递减，因强模型
292	    的 SFT 候选已经较好，CED 筛选的增量价值小。4B 是 sweet spot（+5.98pp），但这 可能是偶然而非系统性规律。EDCR 在 1.7B
293	    上改善最小（仅 -0.68pp vs SFT），进一步 削弱 CED 的方法论叙事。Reviewer 会指出 "方法只在特定模型规模下有效"。
294	
295	    '
296	  tables:
297	  - name: 'Table: Model Size Ablation (Dev Set)'
298	    rows:
299	    - model: Qwen3-1.7B SFT
300	      rel_f1: 0.312
301	      evi_f1: 0.735
302	      edcr: 0.72
303	    - model: Qwen3-1.7B RSFT+CED
304	      rel_f1: 0.338
305	      evi_f1: 0.752
306	      edcr: 0.705
307	    - model: Qwen3-4B SFT
308	      rel_f1: 0.4057
309	      evi_f1: 0.7979
310	      edcr: 0.7118
311	    - model: Qwen3-4B RSFT+CED
312	      rel_f1: 0.4655
313	      evi_f1: 0.8087
314	      edcr: 0.635
315	    - model: Qwen3-8B SFT
316	      rel_f1: 0.458
317	      evi_f1: 0.82
318	      edcr: 0.665
319	    - model: Qwen3-8B RSFT+CED
320	      rel_f1: 0.475
321	      evi_f1: 0.828
322	      edcr: 0.648
323	  figures_description:
324	  - '折线图: RSFT gain (Δrel_f1, Δevi_f1) vs model size，展示非单调关系——4B 是峰值'
325	  analysis: 'RSFT 收益对模型规模不鲁棒，4B 是 sweet spot 可能是 LoRA rank/lr 超参恰好匹配 而非方法论优势。在 reframed
326	    narrative 下，这个结果可以转化为 "RSFT 的最优超参 与模型规模耦合" 的 analysis contribution，但削弱了方法的通用性
327	    claim。
328	
329	    '
330	- name: Re-DocRED extension
331	  plan_id: plan_007
332	  description: '在 Re-DocRED（修正 false negative 标注）上评估 RSFT+CED，验证更干净标注下的表现。
333	
334	    '
335	  expected_results:
336	    redocred_sft_rel_f1: 0.525
337	    redocred_sft_evi_f1: 0.81
338	    redocred_rsft_ced_rel_f1: 0.548
339	    redocred_rsft_ced_evi_f1: 0.818
340	    redocred_rsft_ced_edcr: 0.592
341	    redocred_rsft_gain_rel_f1: 0.023
342	    redocred_rsft_gain_evi_f1: 0.008
343	  result_rationale: 'Re-DocRED 的标注更完整（修正了大量 false negative），SFT baseline 因更多 gold
344	    triples 而提升明显（rel_f1 0.525 vs DocRED 0.406）。但 RSFT 的增量收益缩小 （+2.3pp vs DocRED +5.98pp）。原因：Re-DocRED
345	    的更完整标注减少了 SFT 的 "低悬果实"，RSFT 的 rejection sampling 能筛选出的增量信号更少。EDCR 在 Re-DocRED
346	    上更低（0.592 vs DocRED 0.635），因更完整的 gold evidence 标注 使得之前被标为 distractor 的句子现在是 gold——CED
347	    的 false distractor 问题 在 Re-DocRED 上缓解。但这也意味着 CED 在 Re-DocRED 上的额外价值更小。
348	
349	    '
350	  tables:
351	  - name: 'Table: DocRED vs Re-DocRED (Dev Set)'
352	    rows:
353	    - dataset: DocRED SFT
354	      rel_f1: 0.4057
355	      evi_f1: 0.7979
356	      edcr: 0.7118
357	    - dataset: DocRED RSFT+CED
358	      rel_f1: 0.4655
359	      evi_f1: 0.8087
360	      edcr: 0.635
361	    - dataset: Re-DocRED SFT
362	      rel_f1: 0.525
363	      evi_f1: 0.81
364	      edcr: 0.635
365	    - dataset: Re-DocRED RSFT+CED
366	      rel_f1: 0.548
367	      evi_f1: 0.818
368	      edcr: 0.592
369	  figures_description: []
370	  analysis: 'Re-DocRED 上 RSFT 收益缩小是双刃剑：一方面 reviewer 会质疑方法在 clean data 上 的价值，另一方面可以论证
371	    "RSFT+CED 在 noisy annotation 下价值更大"——但这需要 与 reframed narrative（RL 失败分析）的主线协调。
372	
373	    '
374	- name: top_k ablation (k=1 vs k=3)
375	  plan_id: plan_008
376	  description: 'CED scoring 筛选 top_k=3（~8000 samples）vs top_k=1（~2718 samples）， 验证
377	    CED 过滤严格度对 RSFT 质量的影响。
378	
379	    '
380	  expected_results:
381	    topk1_selected_samples: 2718
382	    topk3_selected_samples: 8154
383	    topk1_mean_ced: 0.6683
384	    topk3_mean_ced: 0.512
385	    topk1_rsft_rel_f1: 0.4655
386	    topk1_rsft_evi_f1: 0.8087
387	    topk1_rsft_edcr: 0.635
388	    topk3_rsft_rel_f1: 0.458
389	    topk3_rsft_evi_f1: 0.805
390	    topk3_rsft_edcr: 0.672
391	    topk3_vs_topk1_rel_f1_gap: -0.0075
392	    topk3_vs_topk1_evi_f1_gap: -0.0037
393	    topk3_vs_topk1_edcr_gap: 0.037
394	  result_rationale: '在 worst 档下，top_k=3 的更多但更低质量训练数据导致轻微退化（rel_f1 -0.75pp， evi_f1
395	    -0.37pp，EDCR +3.7pp）。但退化幅度很小——说明 CED 分数在 top_k=1 到 top_k=3 区间内的质量差异不大（mean CED
396	    从 0.668 降至 0.512，但 floor 仍在 可接受范围）。这进一步支持 worst 档的核心论点：CED scoring 的精细程度不是 关键因素，rejection
397	    sampling 本身（而非 CED 特有的对比信号）驱动了收益。 Reviewer 可以用这个结果论证 "随便什么 NLI 打分函数做 threshold
398	    filtering 都行"。
399	
400	    '
401	  tables:
402	  - name: 'Table: top_k Ablation (Dev Set)'
403	    rows:
404	    - config: top_k=1 (2718 samples)
405	      rel_f1: 0.4655
406	      evi_f1: 0.8087
407	      edcr: 0.635
408	      mean_ced: 0.6683
409	    - config: top_k=3 (8154 samples)
410	      rel_f1: 0.458
411	      evi_f1: 0.805
412	      edcr: 0.672
413	      mean_ced: 0.512
414	  figures_description:
415	  - CED score 分布直方图：top_k=1 vs top_k=3 的 selected samples，展示 quality-quantity tradeoff
416	  analysis: 'top_k ablation 表明 CED 过滤的严格度影响有限，支撑 "rejection sampling 本身 是关键" 的叙事。在
417	    worst 档 reframe 中，这个结果可以纳入 "what works" 的 practical guideline 部分。
418	
419	    '
420	- name: GRPO forgetting 详细分析 + 可视化
421	  plan_id: plan_009
422	  description: '整理全部 GRPO checkpoint 轨迹，绘制 forgetting dynamics 可视化，支撑 Claim 3。
423	
424	    '
425	  expected_results:
426	    grpo_ced_kl001_trajectory:
427	      step_10:
428	        rel_f1: 0.003
429	        evi_f1: 0.72
430	        reward: 0.85
431	      step_20:
432	        rel_f1: 0.009
433	        evi_f1: 0.423
434	        reward: 0.92
435	      step_30:
436	        rel_f1: 0.034
437	        evi_f1: 0.589
438	        reward: 1.05
439	      step_50:
440	        rel_f1: 0.156
441	        evi_f1: 0.564
442	        reward: 1.18
443	      step_60:
444	        rel_f1: 0.147
445	        evi_f1: 0.576
446	        reward: 1.22
447	      step_90:
448	        rel_f1: 0.211
449	        evi_f1: 0.567
450	        reward: 1.37
451	      step_100:
452	        rel_f1: 0.217
453	        evi_f1: 0.575
454	        reward: 1.2
455	    grpo_lr5e6_trajectory:
456	      step_20:
457	        rel_f1: 0.008
458	        evi_f1: 0.628
459	        reward: 0.6
460	      step_40:
461	        rel_f1: 0.007
462	        evi_f1: 0.758
463	        reward: 0.75
464	      step_60:
465	        rel_f1: 0.009
466	        evi_f1: 0.81
467	        reward: 0.88
468	      step_80:
469	        rel_f1: 0.012
470	        evi_f1: 0.828
471	        reward: 0.95
472	      step_100:
473	        rel_f1: 0.014
474	        evi_f1: 0.85
475	        reward: 1.02
476	    flatnli_collapse_step: 25
477	    extract_only_collapse_step: 30
478	    forgetting_onset_step_range:
479	    - 5
480	    - 15
481	    reward_at_rel_f1_peak: 0.85
482	    reward_at_rel_f1_nadir: 1.37
483	  result_rationale: 'GRPO 数据已完整（registry 中多个 GRPO 实验），此 plan 主要是整理和可视化。 在 worst 档下，GRPO
484	    forgetting 分析被升级为核心 contribution。关键发现： (1) reward ↑ 但 rel_f1 ↓ 的 divergence 从
485	    step 5-15 开始，远早于收敛； (2) lr=5e-6 的慢速训练中 evi_f1 持续上升至 0.85（超过 SFT 的 0.798），但 rel_f1
486	    始终 <0.02——模型学会了生成好的 evidence 但完全丧失了 relation 抽取能力； (3) flat-NLI reward 在 step
487	    25 即 collapse（frac_zero_std=0.9），比 CED 更脆弱；(4) 这是 structured IE 场景下 catastrophic
488	    forgetting 的首个系统性 实证。连接 LongRLVR (ICLR 2026) 的 evidence grounding 梯度消失理论： GRPO
489	    的 group-relative advantage 在 structured output 空间中退化，因为 同一 prompt 的多个 rollout
490	    的结构化差异（relation 类型、数量）太大， advantage 估计噪声极高。
491	
492	    '
493	  tables:
494	  - name: 'Table: GRPO Forgetting Summary (All Reward Types)'
495	    rows:
496	    - reward: CED (lr=5e-5, KL=0.01)
497	      best_rel_f1: 0.217
498	      best_evi_f1: 0.575
499	      best_reward: 1.37
500	      collapse_step: N/A (slow decay)
501	    - reward: CED (lr=5e-6)
502	      best_rel_f1: 0.014
503	      best_evi_f1: 0.85
504	      best_reward: 1.02
505	      collapse_step: N/A (never recovers)
506	    - reward: flat-NLI
507	      best_rel_f1: ~0
508	      best_evi_f1: ~0
509	      best_reward: 0.293
510	      collapse_step: 25
511	    - reward: extract-only
512	      best_rel_f1: ~0
513	      best_evi_f1: ~0
514	      best_reward: ~0
515	      collapse_step: 30
516	  figures_description:
517	  - 'Figure 1: Reward-Task Divergence Curves——4-panel plot (一行两列 × 两行)，每 panel 一个
518	    reward type，x轴 training step，左 y轴 reward (blue)，右 y轴 rel_f1 (red dashed)，展示 reward
519	    ↑ + rel_f1 ↓ 的 scissors pattern'
520	  - 'Figure 2: Evidence-Extraction Tradeoff——lr=5e-6 的 evi_f1 vs rel_f1 trajectory，展示
521	    evi_f1 持续上升至 0.85 而 rel_f1 始终 <0.02 的极端 decoupling'
522	  - 'Figure 3: Forgetting Onset Heatmap——x轴 reward type，y轴 learning rate，cell 值为 rel_f1
523	    首次低于 SFT 50% 的 step number'
524	  analysis: '在 worst 档 reframe 下，这是论文最强 contribution。三个核心 insight： (1) GRPO 在 structured
525	    IE 上的失败不是超参问题——3 种 reward × 多个 lr 全线失败， 排除了 "调参不够" 的 reviewer 攻击； (2) evidence
526	    learning 和 relation extraction 在 GRPO 中 decouple——模型可以 学好 evidence（evi_f1 0.85
527	    > SFT 0.798）但完全丧失抽取能力，说明 GRPO 的梯度 被 evidence reward 主导，relation extraction 的离散结构化
528	    reward signal 被淹没； (3) 连接 LongRLVR 的理论，为 structured IE 场景提供首个实证验证。
529	
530	    '
531	- name: NLI model ablation (DeBERTa-base vs large)
532	  plan_id: plan_010
533	  description: 'DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer 的对比。
534	
535	    '
536	  expected_results:
537	    deberta_base_rsft_rel_f1: 0.4655
538	    deberta_base_rsft_evi_f1: 0.8087
539	    deberta_base_rsft_edcr: 0.635
540	    deberta_large_rsft_rel_f1: 0.459
541	    deberta_large_rsft_evi_f1: 0.812
542	    deberta_large_rsft_edcr: 0.641
543	    base_vs_large_evi_f1_gap: -0.0033
544	    base_vs_large_edcr_gap: -0.006
545	    deberta_large_mean_margin: 0.52
546	    deberta_base_mean_margin: 0.48
547	    deberta_large_discrimination_accuracy: 0.835
548	  result_rationale: '在 worst 档下，DeBERTa-large 的更强 NLI 能力（discrimination accuracy 83.5%
549	    vs base 81.5%）未转化为下游 RSFT 质量差异。原因：(1) CED 本身作为 scoring function 与 flat-NLI 无显著差异（plan_001
550	    结论），更强的 NLI 模型只是更精确地 计算了一个不产生额外价值的信号；(2) DeBERTa-large 的更大 margin（0.52 vs 0.48）
551	    导致筛选阈值变化，selected samples 略有不同但重叠度 >85%；(3) large 模型的 NLI 推理时间 ~3x base，cost-benefit
552	    不合理。结论：NLI 模型能力在 base 级别 已经足够，不是 bottleneck。
553	
554	    '
555	  tables:
556	  - name: 'Table: NLI Model Ablation'
557	    rows:
558	    - scorer: DeBERTa-v3-base
559	      mean_margin: 0.48
560	      disc_acc: 0.815
561	      rsft_evi_f1: 0.8087
562	      rsft_edcr: 0.635
563	    - scorer: DeBERTa-v3-large
564	      mean_margin: 0.52
565	      disc_acc: 0.835
566	      rsft_evi_f1: 0.812
567	      rsft_edcr: 0.641
568	  figures_description: []
569	  analysis: NLI 模型能力不是 bottleneck，与 plan_001 的结论一致：CED 的 scoring 精度（无论 来自对比机制还是更强
570	    NLI 模型）不是 RSFT 成功的关键因素。这个 negative result 在 reframed narrative 下可以简化为一句话：RSFT
571	    对 scoring function 的选择 不敏感，进一步支持 "rejection sampling 本身是 what works" 的论点。
572	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6c5f96e-2977-4b54-8431-1bd32ca20e53",
  "isSidechain": false,
  "promptId": "f021ad83-c1a8-458d-9154-bd34a1ce4235",
  "type": "user",
  "uuid": "c5e0f5a5-7209-47dc-990b-aa4d5fc4a94c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/worst/imagined_experiments.yaml",
      "content": "tier: worst\nnarrative_guidance: 'CED 作为方法创新的叙事不成立，必须 reframe。新 angle：\"Why does online RL catastrophically\n  fail for structured IE, and what works instead?\"——将 GRPO 全线失败升级为核心 contribution，RSFT\n  作为 \"what works\" 的解法存在但不再强调 CED 独特性。EDCR 升级为独立 contribution。仍冲 EMNLP Main analysis\n  track。\n\n  '\nimagined_experiments:\n- name: CED vs flat-NLI RSFT ablation\n  plan_id: plan_001\n  description: '用 flat-NLI scoring 筛选 RSFT 训练数据，与 CED scoring 做 head-to-head 对比。 复用已有\n    candidates，仅替换打分函数为 p_pos（无 contrastive margin）。\n\n    '\n  expected_results:\n    flatnli_rsft_rel_f1: 0.452\n    flatnli_rsft_evi_f1: 0.8105\n    flatnli_rsft_edcr: 0.662\n    flatnli_rsft_selected_samples: 2850\n    ced_rsft_best_rel_f1: 0.4655\n    ced_rsft_best_evi_f1: 0.8087\n    ced_rsft_best_edcr: 0.635\n    ced_vs_flatnli_rel_f1_gap: 0.0135\n    ced_vs_flatnli_evi_f1_gap: -0.0018\n    ced_vs_flatnli_edcr_gap: -0.027\n    paired_bootstrap_p_evi_f1: 0.38\n    paired_bootstrap_p_edcr: 0.12\n  result_rationale: '在 worst 档下，flat-NLI 的 p_pos 阈值筛选出的候选与 CED margin 筛选出的候选高度重叠 （Jaccard\n    ~0.75）。原因：DocRED 中 entity-sharing distractor 的 NLI 分数分布与 gold evidence 有足够间距（MVP-1\n    mean_margin=0.48），使得即使不做 contrastive 对比， 单纯高 p_pos 阈值也能过滤掉大部分 distractor。CED 的\n    margin 机制在\"容易\"的 distractor 上无额外区分力，仅在 hard negative（p_neg > 0.6 的 distractor）上有优势，但这类样本\n    占比 <15%。结果：evi_f1 gap 仅 -0.18pp（CED 甚至略低，因 margin 过滤过于严格导致 训练数据略少），EDCR gap -2.7pp\n    方向正确但 p=0.12 不显著。Claim 2 核心假设—— \"CED 的对比性 margin 提供额外信息\"——统计上不成立。\n\n    '\n  tables:\n  - name: 'Table: CED vs flat-NLI RSFT Head-to-Head (Dev Set)'\n    rows:\n    - config: SFT baseline\n      rel_f1: 0.4057\n      evi_f1: 0.7979\n      edcr: 0.7118\n    - config: RSFT flat-NLI (best)\n      rel_f1: 0.452\n      evi_f1: 0.8105\n      edcr: 0.662\n    - config: RSFT CED r1 (s42)\n      rel_f1: 0.4449\n      evi_f1: 0.8187\n      edcr: 0.6565\n    - config: RSFT CED r1 (s44)\n      rel_f1: 0.4655\n      evi_f1: 0.8087\n      edcr: 0.635\n    - config: Δ (CED best − flat-NLI)\n      rel_f1: +1.35pp\n      evi_f1: −0.18pp\n      edcr: −2.70pp\n    - config: p-value (paired bootstrap)\n      rel_f1: '0.08'\n      evi_f1: '0.38'\n      edcr: '0.12'\n  figures_description:\n  - 'Scatter plot: per-document Evi-F1 差异 (CED − flat-NLI)，大部分文档集中在 ±0.02 区间，仅少数 hard-negative-heavy\n    文档 CED 明显优于 flat-NLI'\n  analysis: 'CED 与 flat-NLI 无统计显著差异。CED 的 contrastive margin 仅在 hard negative 密集的\n    文档子集上有边际优势，但全局来看两种 scoring 等价。这意味着 RSFT 的收益主要来自 rejection sampling 本身（过滤低质量候选），而非\n    CED 特有的对比信号。Claim 2 需要 降级为 negative result 或合并到方法 ablation 中。\n\n    '\n- name: Test set evaluation\n  plan_id: plan_002\n  description: '用 RSFT best config (s44) 在 DocRED test set 上评估，提交 CodaLab 获取官方 F1，\n    本地计算 Evi-F1 和 EDCR。\n\n    '\n  expected_results:\n    test_rel_f1: 0.392\n    test_ign_f1: 0.385\n    test_evi_f1: 0.765\n    test_edcr: 0.685\n    test_precision: 0.398\n    test_recall: 0.3865\n    dev_to_test_rel_f1_drop: -0.0735\n    dev_to_test_evi_f1_drop: -0.0437\n    sft_test_rel_f1: 0.355\n    sft_test_evi_f1: 0.752\n    rsft_over_sft_test_rel_f1_gap: 0.037\n    rsft_over_sft_test_evi_f1_gap: 0.013\n  result_rationale: 'Dev→test 严重衰减是 worst 档的核心假设。DocRED test set 的标注分布与 dev set 存在\n    已知偏移（test set annotator 更保守，relation 密度更低，evidence 链更短）。RSFT 在 dev set 上的优势部分来自对\n    dev set 分布的过拟合——训练数据生成和 CED 打分均在 dev set 文档的 train split 上进行，候选筛选隐式适应了 train/dev\n    的共享分布特征。Test set 的 unseen annotator 风格导致 rel_f1 从 0.4655 降至 0.3920（-7.35pp），evi_f1\n    从 0.8087 降至 0.7650（-4.37pp）。EDCR 从 0.635 升至 0.685，因 test set 的 entity 分布更密集，distractor\n    句子更多。rel_f1 仍高于 SFT baseline（+3.7pp），但绝对值 远低于 dev set 表现。evi_f1 0.765 虽仍远超 DREEAM\n    的 57.34，但这个对比因评估 协议差异（生成式 vs attention-based）可能被 reviewer 质疑。\n\n    '\n  tables:\n  - name: 'Table: Dev vs Test Set Performance (RSFT s44)'\n    rows:\n    - split: Dev\n      rel_f1: 0.4655\n      evi_f1: 0.8087\n      edcr: 0.635\n    - split: Test\n      rel_f1: 0.392\n      evi_f1: 0.765\n      edcr: 0.685\n    - split: Δ (test − dev)\n      rel_f1: −7.35pp\n      evi_f1: −4.37pp\n      edcr: +5.00pp\n  - name: 'Table: Test Set Comparison (SFT vs RSFT)'\n    rows:\n    - method: SFT baseline\n      rel_f1: 0.355\n      evi_f1: 0.752\n      edcr: 0.728\n    - method: RSFT+CED (s44)\n      rel_f1: 0.392\n      evi_f1: 0.765\n      edcr: 0.685\n  figures_description:\n  - 'Bar chart: Dev vs Test performance drop per metric，突出 rel_f1 的 15.8% 相对衰减'\n  analysis: 'Test set 上 RSFT 仍优于 SFT，但 margin 缩窄。rel_f1 的相对衰减率 15.8% 高于典型 DocRE 方法（ATLOP\n    约 5-8%），暗示 RSFT 对 dev set 分布有一定过拟合。EDCR 在 test set 上恶化，说明 test set 文档的 entity\n    共现密度更高，distractor 问题更严重。 Publishability threshold 的必要条件（Evi-F1 > 57.34）仍满足，但 reviewer\n    可能 质疑跨评估协议的可比性。\n\n    '\n- name: EDCR pipeline 验证 + cross-method diagnostic table\n  plan_id: plan_003\n  description: '在所有 evidence-producing 方法上计算 EDCR，验证 EDCR 作为独立诊断指标的能力。\n\n    '\n  expected_results:\n    sft_edcr: 0.7118\n    rsft_ced_best_edcr: 0.635\n    rsft_flatnli_edcr: 0.662\n    reranker_edcr: 0.665\n    grpo_best_edcr: 0.8584\n    ced_vs_flatnli_edcr_gap: -0.027\n    edcr_evi_f1_correlation: -0.42\n  result_rationale: '在 worst 档下，EDCR 的 cross-method 诊断能力被削弱。CED RSFT 与 flat-NLI RSFT\n    的 EDCR 差异仅 2.7pp（方向正确但不显著），说明 CED 对 distractor 的过滤优势有限。 Reranker 的 EDCR（0.665）与\n    RSFT flat-NLI 接近，因推理时 CED 重排仅能在 SFT 已生成的候选中选择，而 SFT 候选本身就包含大量 distractor。EDCR\n    与 Evi-F1 的负相关 只有 r=-0.42（弱到中等），无法有力论证 \"Evi-F1 的盲区\"——部分高 EDCR 样本的 Evi-F1 也不高，两个指标部分重叠。EDCR\n    作为独立 contribution 仍有价值（提出新维度），但 \"CED 改善 EDCR\" 的方法论故事很弱。\n\n    '\n  tables:\n  - name: 'Table: Cross-Method EDCR Diagnostic'\n    rows:\n    - method: GRPO+CED (ckpt-90)\n      evi_f1: 0.5666\n      edcr: 0.8584\n      note: catastrophic forgetting\n    - method: SFT baseline\n      evi_f1: 0.7979\n      edcr: 0.7118\n      note: —\n    - method: RSFT flat-NLI\n      evi_f1: 0.8105\n      edcr: 0.662\n      note: —\n    - method: CED-as-reranker\n      evi_f1: 0.801\n      edcr: 0.665\n      note: inference-time only\n    - method: RSFT+CED (s44)\n      evi_f1: 0.8087\n      edcr: 0.635\n      note: best EDCR\n  figures_description:\n  - Evi-F1 vs EDCR scatter plot（per-document level），标注各方法的 centroid，展示两指标的弱负相关\n  analysis: 'EDCR 作为诊断工具确实揭示了 Evi-F1 不能捕捉的 distractor citation 问题（GRPO 的 evi_f1=0.567\n    但 EDCR=0.858 是极端案例）。但 CED 对 EDCR 的改善幅度有限（vs flat-NLI 仅 2.7pp），且 EDCR 绝对值仍然偏高（63.5%\n    的被引证据仍是 distractor）， reviewer 可能质疑方法的实际影响力。Reframe: EDCR 的 contribution 在于指标设计\n    本身，而非 CED 对 EDCR 的改善。\n\n    '\n- name: DREEAM baseline reproduction\n  plan_id: plan_004\n  description: '在 DocRED dev set 上复现 DREEAM (RoBERTa-large) 的 Evi-F1，验证 57.34 是否可复现。\n\n    '\n  expected_results:\n    dreeam_dev_evi_f1_reproduced: 0.608\n    dreeam_dev_rel_f1_reproduced: 0.632\n    dreeam_paper_evi_f1: 0.5734\n    dreeam_paper_rel_f1: 0.63\n    reproduction_evi_f1_gap: 0.0346\n    sais_dev_evi_f1_reproduced: 0.578\n  result_rationale: 'DREEAM 论文报告的 57.34 是 test set Evi-F1，非 dev set。在 worst 档下，dev\n    set 复现值为 60.8，显著高于论文 test set 数字。这产生两个问题：(1) 我们的 RSFT dev Evi-F1 80.87 与 DREEAM\n    dev 60.8 的对比仍然成立（+20pp），但这是跨评估协议对比 （生成式句子索引 vs attention-based sentence extraction），reviewer\n    可能质疑 apple-to-orange；(2) 如果 DREEAM dev 60.8 但 test 57.34，说明 encoder 方法也有 dev→test\n    衰减，但我们的衰减幅度更大（-4.37pp vs -3.46pp），暗示生成式方法对 数据分布更敏感。更关键的是，复现值高于报告值会让 reviewer 质疑我们的评估\n    pipeline 是否与 DREEAM 完全可比——可能存在句子分割、证据匹配阈值等微妙差异。\n\n    '\n  tables:\n  - name: 'Table: DREEAM/SAIS Reproduction vs Reported'\n    rows:\n    - method: DREEAM (paper, test)\n      rel_f1: 0.63\n      evi_f1: 0.5734\n    - method: DREEAM (reproduced, dev)\n      rel_f1: 0.632\n      evi_f1: 0.608\n    - method: SAIS (reproduced, dev)\n      rel_f1: 0.615\n      evi_f1: 0.578\n    - method: RSFT+CED (dev)\n      rel_f1: 0.4655\n      evi_f1: 0.8087\n  figures_description: []\n  analysis: '复现值与报告值的偏差（+3.46pp）引入评估可比性疑虑。必须在论文中详细说明评估协议 差异（evidence 粒度、匹配方式），并承认跨范式对比的局限性。这削弱了\n    Claim 1 中 \"超越 DREEAM\" 的叙事力度，但不致命——20pp 的 dev set 优势即使打折仍然 substantial。\n\n    '\n- name: CED-as-reranker\n  plan_id: plan_005\n  description: '推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。\n\n    '\n  expected_results:\n    reranker_rel_f1: 0.415\n    reranker_evi_f1: 0.801\n    reranker_edcr: 0.665\n    sft_baseline_rel_f1: 0.4057\n    sft_baseline_evi_f1: 0.7979\n    sft_baseline_edcr: 0.7118\n    reranker_over_sft_rel_f1: 0.0093\n    reranker_over_sft_evi_f1: 0.0031\n    reranker_over_sft_edcr: -0.0468\n    reranker_inference_time_multiplier: 8.5\n  result_rationale: '在 worst 档下，reranker 的 EDCR 改善有限（-4.68pp vs SFT）且远不及 RSFT（-7.68pp）。\n    原因：CED 重排只能在 SFT 已生成的 8 个候选中选择，而 SFT 候选的 evidence 分布本身 就偏向 distractor——8 个候选中\n    \"低 EDCR\" 的候选可能根本不存在（SFT 的 systematic bias 使所有候选都引用类似的 distractor 句子）。Rel_f1 微升（+0.93pp）因为\n    CED 兼顾了 evidence 质量和抽取质量的联合打分，但提升幅度小。推理时间 8.5x（每个候选 都需要 NLI 推理）是实际部署的障碍。Reranker\n    作为 \"training-free baseline\" 有方法论 价值，但在 worst 档下不构成独立 contribution。\n\n    '\n  tables:\n  - name: 'Table: CED-as-Reranker vs SFT vs RSFT (Dev Set)'\n    rows:\n    - method: SFT baseline\n      rel_f1: 0.4057\n      evi_f1: 0.7979\n      edcr: 0.7118\n      extra_train: 'No'\n    - method: CED-as-reranker (N=8)\n      rel_f1: 0.415\n      evi_f1: 0.801\n      edcr: 0.665\n      extra_train: 'No'\n    - method: RSFT+CED (s44)\n      rel_f1: 0.4655\n      evi_f1: 0.8087\n      edcr: 0.635\n      extra_train: 'Yes'\n  figures_description:\n  - EDCR 分布直方图：SFT 8 候选的 EDCR 分布，展示 reranker 的 selection ceiling——最优候选的 EDCR 仍然偏高\n  analysis: 'Reranker 效果有限，印证 SFT 候选池本身的 distractor bias 是 bottleneck。RSFT 通过 改变模型权重从根源减少\n    distractor 引用，reranker 只能在已有候选中做选择。在 worst 档下，reranker 降级为 ablation 中的一行数据，不再作为独立方法。\n\n    '\n- name: Model size ablation (1.7B / 8B)\n  plan_id: plan_006\n  description: 'Qwen3-1.7B 和 Qwen3-8B 上复现 RSFT+CED pipeline，验证方法对模型规模的泛化性。\n\n    '\n  expected_results:\n    qwen3_1_7b_sft_rel_f1: 0.312\n    qwen3_1_7b_sft_evi_f1: 0.735\n    qwen3_1_7b_rsft_ced_rel_f1: 0.338\n    qwen3_1_7b_rsft_ced_evi_f1: 0.752\n    qwen3_1_7b_rsft_ced_edcr: 0.705\n    qwen3_8b_sft_rel_f1: 0.458\n    qwen3_8b_sft_evi_f1: 0.82\n    qwen3_8b_rsft_ced_rel_f1: 0.475\n    qwen3_8b_rsft_ced_evi_f1: 0.828\n    qwen3_8b_rsft_ced_edcr: 0.648\n    rsft_gain_1_7b_rel_f1: 0.026\n    rsft_gain_4b_rel_f1: 0.0598\n    rsft_gain_8b_rel_f1: 0.017\n  result_rationale: '在 worst 档下，model size ablation 暴露 RSFT 收益的不稳定性。1.7B 模型的 SFT baseline\n    较弱（rel_f1 0.312），RSFT 提升 +2.6pp——绝对收益小，因小模型生成候选 的质量上限低，CED 筛选后的训练数据量骤降（可能仅 ~1200\n    samples vs 4B 的 2718）。 8B 模型的 SFT baseline 已较强（0.458），RSFT 仅提升 +1.7pp——边际递减，因强模型\n    的 SFT 候选已经较好，CED 筛选的增量价值小。4B 是 sweet spot（+5.98pp），但这 可能是偶然而非系统性规律。EDCR 在 1.7B\n    上改善最小（仅 -0.68pp vs SFT），进一步 削弱 CED 的方法论叙事。Reviewer 会指出 \"方法只在特定模型规模下有效\"。\n\n    '\n  tables:\n  - name: 'Table: Model Size Ablation (Dev Set)'\n    rows:\n    - model: Qwen3-1.7B SFT\n      rel_f1: 0.312\n      evi_f1: 0.735\n      edcr: 0.72\n    - model: Qwen3-1.7B RSFT+CED\n      rel_f1: 0.338\n      evi_f1: 0.752\n      edcr: 0.705\n    - model: Qwen3-4B SFT\n      rel_f1: 0.4057\n      evi_f1: 0.7979\n      edcr: 0.7118\n    - model: Qwen3-4B RSFT+CED\n      rel_f1: 0.4655\n      evi_f1: 0.8087\n      edcr: 0.635\n    - model: Qwen3-8B SFT\n      rel_f1: 0.458\n      evi_f1: 0.82\n      edcr: 0.665\n    - model: Qwen3-8B RSFT+CED\n      rel_f1: 0.475\n      evi_f1: 0.828\n      edcr: 0.648\n  figures_description:\n  - '折线图: RSFT gain (Δrel_f1, Δevi_f1) vs model size，展示非单调关系——4B 是峰值'\n  analysis: 'RSFT 收益对模型规模不鲁棒，4B 是 sweet spot 可能是 LoRA rank/lr 超参恰好匹配 而非方法论优势。在 reframed\n    narrative 下，这个结果可以转化为 \"RSFT 的最优超参 与模型规模耦合\" 的 analysis contribution，但削弱了方法的通用性\n    claim。\n\n    '\n- name: Re-DocRED extension\n  plan_id: plan_007\n  description: '在 Re-DocRED（修正 false negative 标注）上评估 RSFT+CED，验证更干净标注下的表现。\n\n    '\n  expected_results:\n    redocred_sft_rel_f1: 0.525\n    redocred_sft_evi_f1: 0.81\n    redocred_rsft_ced_rel_f1: 0.548\n    redocred_rsft_ced_evi_f1: 0.818\n    redocred_rsft_ced_edcr: 0.592\n    redocred_rsft_gain_rel_f1: 0.023\n    redocred_rsft_gain_evi_f1: 0.008\n  result_rationale: 'Re-DocRED 的标注更完整（修正了大量 false negative），SFT baseline 因更多 gold\n    triples 而提升明显（rel_f1 0.525 vs DocRED 0.406）。但 RSFT 的增量收益缩小 （+2.3pp vs DocRED +5.98pp）。原因：Re-DocRED\n    的更完整标注减少了 SFT 的 \"低悬果实\"，RSFT 的 rejection sampling 能筛选出的增量信号更少。EDCR 在 Re-DocRED\n    上更低（0.592 vs DocRED 0.635），因更完整的 gold evidence 标注 使得之前被标为 distractor 的句子现在是 gold——CED\n    的 false distractor 问题 在 Re-DocRED 上缓解。但这也意味着 CED 在 Re-DocRED 上的额外价值更小。\n\n    '\n  tables:\n  - name: 'Table: DocRED vs Re-DocRED (Dev Set)'\n    rows:\n    - dataset: DocRED SFT\n      rel_f1: 0.4057\n      evi_f1: 0.7979\n      edcr: 0.7118\n    - dataset: DocRED RSFT+CED\n      rel_f1: 0.4655\n      evi_f1: 0.8087\n      edcr: 0.635\n    - dataset: Re-DocRED SFT\n      rel_f1: 0.525\n      evi_f1: 0.81\n      edcr: 0.635\n    - dataset: Re-DocRED RSFT+CED\n      rel_f1: 0.548\n      evi_f1: 0.818\n      edcr: 0.592\n  figures_description: []\n  analysis: 'Re-DocRED 上 RSFT 收益缩小是双刃剑：一方面 reviewer 会质疑方法在 clean data 上 的价值，另一方面可以论证\n    \"RSFT+CED 在 noisy annotation 下价值更大\"——但这需要 与 reframed narrative（RL 失败分析）的主线协调。\n\n    '\n- name: top_k ablation (k=1 vs k=3)\n  plan_id: plan_008\n  description: 'CED scoring 筛选 top_k=3（~8000 samples）vs top_k=1（~2718 samples）， 验证\n    CED 过滤严格度对 RSFT 质量的影响。\n\n    '\n  expected_results:\n    topk1_selected_samples: 2718\n    topk3_selected_samples: 8154\n    topk1_mean_ced: 0.6683\n    topk3_mean_ced: 0.512\n    topk1_rsft_rel_f1: 0.4655\n    topk1_rsft_evi_f1: 0.8087\n    topk1_rsft_edcr: 0.635\n    topk3_rsft_rel_f1: 0.458\n    topk3_rsft_evi_f1: 0.805\n    topk3_rsft_edcr: 0.672\n    topk3_vs_topk1_rel_f1_gap: -0.0075\n    topk3_vs_topk1_evi_f1_gap: -0.0037\n    topk3_vs_topk1_edcr_gap: 0.037\n  result_rationale: '在 worst 档下，top_k=3 的更多但更低质量训练数据导致轻微退化（rel_f1 -0.75pp， evi_f1\n    -0.37pp，EDCR +3.7pp）。但退化幅度很小——说明 CED 分数在 top_k=1 到 top_k=3 区间内的质量差异不大（mean CED\n    从 0.668 降至 0.512，但 floor 仍在 可接受范围）。这进一步支持 worst 档的核心论点：CED scoring 的精细程度不是 关键因素，rejection\n    sampling 本身（而非 CED 特有的对比信号）驱动了收益。 Reviewer 可以用这个结果论证 \"随便什么 NLI 打分函数做 threshold\n    filtering 都行\"。\n\n    '\n  tables:\n  - name: 'Table: top_k Ablation (Dev Set)'\n    rows:\n    - config: top_k=1 (2718 samples)\n      rel_f1: 0.4655\n      evi_f1: 0.8087\n      edcr: 0.635\n      mean_ced: 0.6683\n    - config: top_k=3 (8154 samples)\n      rel_f1: 0.458\n      evi_f1: 0.805\n      edcr: 0.672\n      mean_ced: 0.512\n  figures_description:\n  - CED score 分布直方图：top_k=1 vs top_k=3 的 selected samples，展示 quality-quantity tradeoff\n  analysis: 'top_k ablation 表明 CED 过滤的严格度影响有限，支撑 \"rejection sampling 本身 是关键\" 的叙事。在\n    worst 档 reframe 中，这个结果可以纳入 \"what works\" 的 practical guideline 部分。\n\n    '\n- name: GRPO forgetting 详细分析 + 可视化\n  plan_id: plan_009\n  description: '整理全部 GRPO checkpoint 轨迹，绘制 forgetting dynamics 可视化，支撑 Claim 3。\n\n    '\n  expected_results:\n    grpo_ced_kl001_trajectory:\n      step_10:\n        rel_f1: 0.003\n        evi_f1: 0.72\n        reward: 0.85\n      step_20:\n        rel_f1: 0.009\n        evi_f1: 0.423\n        reward: 0.92\n      step_30:\n        rel_f1: 0.034\n        evi_f1: 0.589\n        reward: 1.05\n      step_50:\n        rel_f1: 0.156\n        evi_f1: 0.564\n        reward: 1.18\n      step_60:\n        rel_f1: 0.147\n        evi_f1: 0.576\n        reward: 1.22\n      step_90:\n        rel_f1: 0.211\n        evi_f1: 0.567\n        reward: 1.37\n      step_100:\n        rel_f1: 0.217\n        evi_f1: 0.575\n        reward: 1.2\n    grpo_lr5e6_trajectory:\n      step_20:\n        rel_f1: 0.008\n        evi_f1: 0.628\n        reward: 0.6\n      step_40:\n        rel_f1: 0.007\n        evi_f1: 0.758\n        reward: 0.75\n      step_60:\n        rel_f1: 0.009\n        evi_f1: 0.81\n        reward: 0.88\n      step_80:\n        rel_f1: 0.012\n        evi_f1: 0.828\n        reward: 0.95\n      step_100:\n        rel_f1: 0.014\n        evi_f1: 0.85\n        reward: 1.02\n    flatnli_collapse_step: 25\n    extract_only_collapse_step: 30\n    forgetting_onset_step_range:\n    - 5\n    - 15\n    reward_at_rel_f1_peak: 0.85\n    reward_at_rel_f1_nadir: 1.37\n  result_rationale: 'GRPO 数据已完整（registry 中多个 GRPO 实验），此 plan 主要是整理和可视化。 在 worst 档下，GRPO\n    forgetting 分析被升级为核心 contribution。关键发现： (1) reward ↑ 但 rel_f1 ↓ 的 divergence 从\n    step 5-15 开始，远早于收敛； (2) lr=5e-6 的慢速训练中 evi_f1 持续上升至 0.85（超过 SFT 的 0.798），但 rel_f1\n    始终 <0.02——模型学会了生成好的 evidence 但完全丧失了 relation 抽取能力； (3) flat-NLI reward 在 step\n    25 即 collapse（frac_zero_std=0.9），比 CED 更脆弱；(4) 这是 structured IE 场景下 catastrophic\n    forgetting 的首个系统性 实证。连接 LongRLVR (ICLR 2026) 的 evidence grounding 梯度消失理论： GRPO\n    的 group-relative advantage 在 structured output 空间中退化，因为 同一 prompt 的多个 rollout\n    的结构化差异（relation 类型、数量）太大， advantage 估计噪声极高。\n\n    '\n  tables:\n  - name: 'Table: GRPO Forgetting Summary (All Reward Types)'\n    rows:\n    - reward: CED (lr=5e-5, KL=0.01)\n      best_rel_f1: 0.217\n      best_evi_f1: 0.575\n      best_reward: 1.37\n      collapse_step: N/A (slow decay)\n    - reward: CED (lr=5e-6)\n      best_rel_f1: 0.014\n      best_evi_f1: 0.85\n      best_reward: 1.02\n      collapse_step: N/A (never recovers)\n    - reward: flat-NLI\n      best_rel_f1: ~0\n      best_evi_f1: ~0\n      best_reward: 0.293\n      collapse_step: 25\n    - reward: extract-only\n      best_rel_f1: ~0\n      best_evi_f1: ~0\n      best_reward: ~0\n      collapse_step: 30\n  figures_description:\n  - 'Figure 1: Reward-Task Divergence Curves——4-panel plot (一行两列 × 两行)，每 panel 一个\n    reward type，x轴 training step，左 y轴 reward (blue)，右 y轴 rel_f1 (red dashed)，展示 reward\n    ↑ + rel_f1 ↓ 的 scissors pattern'\n  - 'Figure 2: Evidence-Extraction Tradeoff——lr=5e-6 的 evi_f1 vs rel_f1 trajectory，展示\n    evi_f1 持续上升至 0.85 而 rel_f1 始终 <0.02 的极端 decoupling'\n  - 'Figure 3: Forgetting Onset Heatmap——x轴 reward type，y轴 learning rate，cell 值为 rel_f1\n    首次低于 SFT 50% 的 step number'\n  analysis: '在 worst 档 reframe 下，这是论文最强 contribution。三个核心 insight： (1) GRPO 在 structured\n    IE 上的失败不是超参问题——3 种 reward × 多个 lr 全线失败， 排除了 \"调参不够\" 的 reviewer 攻击； (2) evidence\n    learning 和 relation extraction 在 GRPO 中 decouple——模型可以 学好 evidence（evi_f1 0.85\n    > SFT 0.798）但完全丧失抽取能力，说明 GRPO 的梯度 被 evidence reward 主导，relation extraction 的离散结构化\n    reward signal 被淹没； (3) 连接 LongRLVR 的理论，为 structured IE 场景提供首个实证验证。\n\n    '\n- name: NLI model ablation (DeBERTa-base vs large)\n  plan_id: plan_010\n  description: 'DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer 的对比。\n\n    '\n  expected_results:\n    deberta_base_rsft_rel_f1: 0.4655\n    deberta_base_rsft_evi_f1: 0.8087\n    deberta_base_rsft_edcr: 0.635\n    deberta_large_rsft_rel_f1: 0.459\n    deberta_large_rsft_evi_f1: 0.812\n    deberta_large_rsft_edcr: 0.641\n    base_vs_large_evi_f1_gap: -0.0033\n    base_vs_large_edcr_gap: -0.006\n    deberta_large_mean_margin: 0.52\n    deberta_base_mean_margin: 0.48\n    deberta_large_discrimination_accuracy: 0.835\n  result_rationale: '在 worst 档下，DeBERTa-large 的更强 NLI 能力（discrimination accuracy 83.5%\n    vs base 81.5%）未转化为下游 RSFT 质量差异。原因：(1) CED 本身作为 scoring function 与 flat-NLI 无显著差异（plan_001\n    结论），更强的 NLI 模型只是更精确地 计算了一个不产生额外价值的信号；(2) DeBERTa-large 的更大 margin（0.52 vs 0.48）\n    导致筛选阈值变化，selected samples 略有不同但重叠度 >85%；(3) large 模型的 NLI 推理时间 ~3x base，cost-benefit\n    不合理。结论：NLI 模型能力在 base 级别 已经足够，不是 bottleneck。\n\n    '\n  tables:\n  - name: 'Table: NLI Model Ablation'\n    rows:\n    - scorer: DeBERTa-v3-base\n      mean_margin: 0.48\n      disc_acc: 0.815\n      rsft_evi_f1: 0.8087\n      rsft_edcr: 0.635\n    - scorer: DeBERTa-v3-large\n      mean_margin: 0.52\n      disc_acc: 0.835\n      rsft_evi_f1: 0.812\n      rsft_edcr: 0.641\n  figures_description: []\n  analysis: NLI 模型能力不是 bottleneck，与 plan_001 的结论一致：CED 的 scoring 精度（无论 来自对比机制还是更强\n    NLI 模型）不是 RSFT 成功的关键因素。这个 negative result 在 reframed narrative 下可以简化为一句话：RSFT\n    对 scoring function 的选择 不敏感，进一步支持 \"rejection sampling 本身是 what works\" 的论点。\n",
      "numLines": 572,
      "startLine": 1,
      "totalLines": 572
    }
  },
  "sourceToolAssistantUUID": "c6c5f96e-2977-4b54-8431-1bd32ca20e53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 17 · 2026-05-15T13:46:10.305Z_

````json
{
  "parentUuid": "c5e0f5a5-7209-47dc-990b-aa4d5fc4a94c",
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
  "uuid": "68be76b0-d2ef-4f8d-b3b9-94da62ed4239",
  "timestamp": "2026-05-15T13:46:10.305Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：RSFT 优势在 test set 上大幅缩水，且 GRPO G=8 部分恢复，核心叙事需要全面 reframe 核心假设：['CED vs flat-NLI 无差异或 flat-NLI 略优（Δevi_f1 < 0.3pp），CED 的对比性设计在 RSFT 间接作用下无可观测效果', 'Test set…",
  "leafUuid": "68be76b0-d2ef-4f8d-b3b9-94da62ed4239",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Systematic LLM evidence generation for DocRE under worst-case outcomes",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e"
}
```

---

### Assistant

_source line 20 · 2026-05-15T13:46:14.116Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the existing worst-tier imagined experiments. Let me read the rest of this file and also check for any additional experiments that need predictions (plan_011, plan_012, plan_013 which were added by dream).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68be76b0-d2ef-4f8d-b3b9-94da62ed4239",
  "isSidechain": false,
  "requestId": "req_011Cb4TStueAEXGFWvBTw99Q",
  "type": "assistant",
  "uuid": "01dae9f3-4d70-43fc-b38c-69bb1b56f885",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Jk5aW9SYwnGJRipPbGxsV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20124,
      "cache_read_input_tokens": 33493,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20124,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 33493,
          "cache_creation_input_tokens": 20124,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20124
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

_source line 21 · 2026-05-15T13:46:16.218Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LxLiP7bBBpysySNcTTr7QS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/worst/imagined_experiments.yaml",
  "offset": 572
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01dae9f3-4d70-43fc-b38c-69bb1b56f885",
  "isSidechain": false,
  "requestId": "req_011Cb4TStueAEXGFWvBTw99Q",
  "type": "assistant",
  "uuid": "22b7630d-4e39-41ea-b618-dae723d37b74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Jk5aW9SYwnGJRipPbGxsV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20124,
      "cache_read_input_tokens": 33493,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20124,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 33493,
          "cache_creation_input_tokens": 20124,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20124
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

_source line 22 · 2026-05-15T13:46:16.226Z_

<details><summary>↩ Tool result · `toolu_01LxLiP7bBBpysySNcTTr7QS`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (572). The file has 572 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22b7630d-4e39-41ea-b618-dae723d37b74",
  "isSidechain": false,
  "promptId": "f021ad83-c1a8-458d-9154-bd34a1ce4235",
  "type": "user",
  "uuid": "f3867c43-5fcf-4847-bfe8-38e417070cb6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/worst/imagined_experiments.yaml",
      "content": "",
      "numLines": 1,
      "startLine": 572,
      "totalLines": 572
    }
  },
  "sourceToolAssistantUUID": "22b7630d-4e39-41ea-b618-dae723d37b74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-15T13:47:19.018Z_

<details><summary>Logged reasoning block</summary>

```text
The existing worst-tier file has 10 experiments (plan_001 through plan_010). I need to check if plan_011, plan_012, plan_013 are already included. Let me check the names in the existing file:

1. plan_001 - CED vs flat-NLI RSFT ablation
2. plan_002 - Test set evaluation
3. plan_003 - EDCR pipeline verification
4. plan_004 - DREEAM baseline reproduction
5. plan_005 - CED-as-reranker


6. plan_006 - Model size ablation
7. plan_007 - Re-DocRED extension
8. plan_008 - top_k ablation
9. plan_009 - GRPO forgetting analysis
10. plan_010 - NLI model ablation

So I'm missing plan_011 (GRPO G=8), plan_012 (DPO+CED), and plan_013 (EDCR human annotation). The user wants detailed predictions for all planned experiments, so I need to generate data for these three missing ones as well.

Looking at the experiment_plan, I can see that plan_001 through plan_010 and plan_005 already have detailed predictions in the existing file. The remaining planned experiments—plan_011, plan_012, and plan_013—need to be added with the same level of detail.

I need to generate the complete YAML output for all experiments, incorporating the worst tier assumptions. This means I'll be producing predictions for all planned experiments following the established schema with narrative guidance and expected results for each one.

Generating the full YAML structure... Looking at these metric ranges, the offline methods seem to gain their advantage not from rejection sampling itself but from sidestepping policy gradient instability. The correlation between EDCR and human judgments is weak though, raising questions about whether EDCR holds up as a standalone evaluation metric.

Now I'm working through the experiment predictions based on the worst-case performance tiers. For GRPO with G=8, the partial recovery in relative F1 suggests that the earlier failure at G=4 wasn't purely about catastrophic forgetting—some of it came from advantage estimation noise, so I need to refine the claim to be more specific about the combination of QLoRA with small group sizes. For DPO with CED, the relative F1 should stay above 0.35 and approach RSFT performance levels.

The key insight emerging is that the offline advantage mechanism isn't unique to rejection sampling—it's really about avoiding policy gradient updates altogether, which challenges the narrative that RSFT is the only solution. For EDCR's human validation, I'm expecting the correlation to stay below 0.35, which raises questions about whether EDCR works as a standalone metric.

Looking back at the existing predictions, they're already well-calibrated to the worst-tier assumptions, so I'll keep those and just add the three missing experiments. There's a discrepancy I need to resolve though—the test set uses conditional Evi-F1 at 0.765, but the worst tier spec indicates the joint Evi-F1 should be lower. the complete YAML output systematically. I need to reconsider the metric ranges more carefully—for the worst tier, the absolute test rel_f1 values of [0.39, 0.43] don't directly match the delta ranges specified elsewhere, so I'm working through the math to reconcile the SFT baseline with the RSFT improvements and ensure consistency across all the metrics. the existing worst-case file is slightly overestimating the delta. Let me recalculate with the constraint that the dev-to-test degradation should be minimal. If RSFT test is 0.41 with a 1.5pp improvement over SFT, that puts SFT test at 0.395, which means the dev-to-test drop is only about 1pp—much smaller than the spec's concern about drops exceeding 3pp.

Actually, I'm reading the spec wrong. The >3pp degradation refers to RSFT's own dev-to-test drop, not SFT's. So with RSFT dev at 0.4655 and test at 0.41, that's a 5.55pp drop, which satisfies the constraint. Now I need to set SFT test such that the delta between RSFT and SFT falls within the [0.5, 2.0]pp range.

If RSFT test is 0.408, then SFT test should be around 0.393 to create a 1.5pp gap. This also shows RSFT is more sensitive to distribution shift than SFT, which makes sense. Now I'm working through the Evi-F1 joint metrics for the DREEAM protocol.

The joint Evi-F1 should be much lower than the conditional version since it requires both correct relations and correct evidence. If relation F1 is around 0.41 and conditional evidence F1 is roughly 0.77, multiplying them gives about 0.316, but the spec suggests the range should be [0.22, 0.30]. I need to check how DREEAM actually computes their joint metric—it's not a simple multiplication.

Now I'm ready to compile the full output and shift the narrative framing. The paper should position itself as the first systematic study of evidence generation in LLM-based document relation extraction, moving away from a pure methods focus toward analysis and benchmarking.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3867c43-5fcf-4847-bfe8-38e417070cb6",
  "isSidechain": false,
  "requestId": "req_011Cb4TTLYk6AXXvgPhxceox",
  "type": "assistant",
  "uuid": "bef5255c-6925-4564-a845-00b149d24014",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SxK3K1xBUZ7qYAJnLH6Agd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 226,
      "cache_read_input_tokens": 53617,
      "output_tokens": 22505,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 22505,
          "cache_read_input_tokens": 53617,
          "cache_creation_input_tokens": 226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 226
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

_source line 24 · 2026-05-15T13:52:46.220Z_

Now I have the full context. Let me produce the complete worst-tier imagined experiments YAML, incorporating the three new dream-driven experiments (plan_011, plan_012, plan_013) and updating the existing ones to be consistent with the worst-tier key metric ranges — especially the joint Evi-F1 and narrowed test-set delta.

```yaml
tier: worst
narrative_guidance: >
  RSFT 优势在 test set 上大幅缩水（Δrel_f1 仅 +1.5pp over SFT，p≈0.08），
  CED vs flat-NLI 无统计显著差异，GRPO G=8 部分恢复证明 G=4 failure 有 advantage noise 成分，
  DPO 接近 RSFT 水平证明 offline 优势不在 rejection sampling。核心叙事必须全面 reframe。

  新叙事方向："首次对 LLM DocRE evidence generation 的系统性研究"——
  从 method paper 转型为 analysis + benchmark paper。

  贡献重组：(1) 首个 LLM DocRE evidence benchmark（任务定义 + 评测协议 + 多指标框架，含 DREEAM 对齐 joint Evi-F1 + EDCR）；
  (2) online vs offline RL 的系统对比（GRPO G=4/G=8 vs DPO vs RSFT），发现 catastrophic forgetting
  主要由 QLoRA + 小 group size 的脆弱组合驱动，而非 online RL 本身固有缺陷；
  (3) evidence 评估指标的局限性分析（conditional vs joint Evi-F1 的巨大落差 + EDCR 与人工判断弱相关）。

  CED 完全降级为 explored scoring function（与 flat-NLI 等价）。
  仍冲 EMNLP Main，但可能推迟到 ARR September 或 AAAI 2027 以积累 model size / dataset 覆盖。

imagined_experiments:
  - name: "CED vs flat-NLI RSFT ablation"
    plan_id: "plan_001"
    description: >
      用 flat-NLI scoring（p_pos 阈值，无 contrastive margin）筛选 RSFT 训练数据，
      与 CED scoring 做 head-to-head 对比。复用已有 candidates，仅替换打分函数。
    expected_results:
      flatnli_rsft_best_rel_f1: 0.456
      flatnli_rsft_best_evi_f1: 0.812
      flatnli_rsft_best_edcr: 0.658
      flatnli_rsft_selected_samples: 2920
      ced_rsft_best_rel_f1: 0.4655
      ced_rsft_best_evi_f1: 0.8087
      ced_rsft_best_edcr: 0.635
      ced_vs_flatnli_rel_f1_gap_pp: 0.95
      ced_vs_flatnli_evi_f1_gap_pp: -0.33
      ced_vs_flatnli_edcr_gap_pp: -2.3
      paired_bootstrap_p_rel_f1: 0.11
      paired_bootstrap_p_evi_f1: 0.42
      paired_bootstrap_p_edcr: 0.15
      candidate_overlap_jaccard: 0.76
    result_rationale: >
      在 worst 档下，flat-NLI 的 p_pos 阈值筛选与 CED margin 筛选高度重叠（Jaccard ~0.76）。
      根本原因：DocRED 中 entity-sharing distractor 的 NLI 分数分布与 gold evidence 有足够间距
      （MVP-1 mean_margin=0.48），单纯高 p_pos 阈值已能过滤大部分 distractor，CED 的 contrastive margin
      仅在 hard negative（p_neg > 0.6）上有边际优势，这类样本占比 <15%。

      Evi-F1 差异 -0.33pp（CED 反而略低），因 CED margin 过滤偏严格导致训练数据少 ~200 samples，
      reduced diversity 的负面效应抵消了质量优势。EDCR 差 -2.3pp 方向正确但 p=0.15 不显著。
      Rel_f1 差 +0.95pp CED 略优，但 p=0.11 不显著——可能来自随机种子噪声而非 scoring 差异。

      结论：Claim 2 统计上不成立。CED 降级为 "one of several viable scoring functions"。
    tables:
      - name: "Table: CED vs flat-NLI RSFT Head-to-Head (Dev Set)"
        rows:
          - config: "SFT baseline"
            rel_f1: 0.4057
            evi_f1: 0.7979
            edcr: 0.7118
          - config: "RSFT flat-NLI (best)"
            rel_f1: 0.456
            evi_f1: 0.812
            edcr: 0.658
          - config: "RSFT CED r1 (s42)"
            rel_f1: 0.4449
            evi_f1: 0.8187
            edcr: 0.6565
          - config: "RSFT CED (s44)"
            rel_f1: 0.4655
            evi_f1: 0.8087
            edcr: 0.635
          - config: "Δ (CED best − flat-NLI best)"
            rel_f1: "+0.95pp"
            evi_f1: "−0.33pp"
            edcr: "−2.3pp"
          - config: "p-value (paired bootstrap)"
            rel_f1: "0.11"
            evi_f1: "0.42"
            edcr: "0.15"
    figures_description:
      - "Scatter plot: per-document Evi-F1 差异 (CED − flat-NLI)，大部分文档集中在 ±0.02 区间，仅少数 hard-negative-heavy 文档 CED 明显优于 flat-NLI"
      - "Venn diagram: CED top_k=1 selected 2718 vs flat-NLI threshold selected 2920 的重叠，展示 76% overlap"
    analysis: >
      CED 与 flat-NLI 无统计显著差异（三个指标均 p>0.10）。RSFT 的收益主要来自 rejection sampling 本身
      （过滤低质量候选的 floor effect），而非 CED 特有的对比信号。在 reframed narrative 下，
      这转化为正面发现："RSFT 对 scoring function 选择鲁棒，practitioners 可用任意 NLI scorer"——
      降低了方法的 entry barrier，但也意味着 CED 不再是独立 contribution。

  - name: "Test set evaluation"
    plan_id: "plan_002"
    description: >
      用 RSFT best config (s44) 在 DocRED test set 上评估。提交 CodaLab 获取官方 F1/Ign-F1，
      本地计算 conditional Evi-F1、DREEAM-aligned joint Evi-F1 和 EDCR。
    expected_results:
      rsft_test_rel_f1: 0.408
      rsft_test_ign_f1: 0.401
      rsft_test_evi_f1_conditional: 0.770
      rsft_test_evi_f1_joint: 0.265
      rsft_test_edcr: 0.690
      rsft_test_precision: 0.415
      rsft_test_recall: 0.402
      sft_test_rel_f1: 0.393
      sft_test_evi_f1_conditional: 0.758
      sft_test_evi_f1_joint: 0.248
      sft_test_edcr: 0.732
      rsft_over_sft_test_rel_f1_delta_pp: 1.5
      rsft_over_sft_test_evi_f1_joint_delta_pp: 1.7
      rsft_over_sft_bootstrap_p: 0.08
      dev_to_test_rsft_rel_f1_drop_pp: 5.75
      dev_to_test_sft_rel_f1_drop_pp: 1.27
      flatnli_rsft_test_rel_f1: 0.405
      flatnli_rsft_test_evi_f1_joint: 0.258
    result_rationale: >
      Dev→test 严重衰减是 worst 档核心假设。RSFT dev→test 下降 5.75pp（0.4655→0.408），
      而 SFT 仅下降 1.27pp（0.4057→0.393）。RSFT 对分布偏移更敏感的原因：
      (1) RSFT 训练数据生成和 CED 打分均在 train split 上进行，候选筛选隐式适应了 train/dev 的共享标注风格；
      (2) test set annotator 更保守（relation 密度更低），RSFT 的 recall-oriented training signal
      在 test set 上产生更多 false positive；
      (3) test set 的 entity 分布更密集，distractor 句子更多，EDCR 从 0.635 恶化至 0.690。

      RSFT 仍优于 SFT（+1.5pp rel_f1），但 p=0.08 边界不显著，reviewer 可合理主张
      "dev set 增幅存在过拟合成分"。

      Joint Evi-F1（DREEAM 协议）极低（0.265 vs conditional 0.770）——这是因为 joint 协议
      要求 relation 也正确才计 evidence 分数，rel_f1 ~0.41 直接拉低上限。
      与 DREEAM test set 57.34 的对比需极其谨慎：评估协议完全不同
      （生成式句子索引 vs encoder attention-based extraction）。
    tables:
      - name: "Table: Dev vs Test Set Performance"
        rows:
          - split: "Dev (RSFT s44)"
            rel_f1: 0.4655
            evi_f1_cond: 0.8087
            evi_f1_joint: 0.338
            edcr: 0.635
          - split: "Test (RSFT s44)"
            rel_f1: 0.408
            evi_f1_cond: 0.770
            evi_f1_joint: 0.265
            edcr: 0.690
          - split: "Δ (test − dev)"
            rel_f1: "−5.75pp"
            evi_f1_cond: "−3.87pp"
            evi_f1_joint: "−7.3pp"
            edcr: "+5.5pp"
      - name: "Table: Test Set SFT vs RSFT vs flat-NLI RSFT"
        rows:
          - method: "SFT baseline"
            rel_f1: 0.393
            evi_f1_joint: 0.248
            edcr: 0.732
          - method: "RSFT flat-NLI"
            rel_f1: 0.405
            evi_f1_joint: 0.258
            edcr: 0.702
          - method: "RSFT+CED (s44)"
            rel_f1: 0.408
            evi_f1_joint: 0.265
            edcr: 0.690
          - method: "DREEAM (paper, test)"
            rel_f1: 0.630
            evi_f1_joint: 0.5734
            edcr: "N/A"
    figures_description:
      - "Bar chart: Dev vs Test 相对衰减率 per method（SFT 3.1% vs RSFT 12.4%），突出 RSFT 的 distribution sensitivity"
      - "Error bar plot: RSFT vs SFT test rel_f1 with 95% CI from paired bootstrap，展示 CI 覆盖 0"
    analysis: >
      Test set 上 RSFT 仍优于 SFT 但 margin 大幅缩窄且边界不显著。Publishability 必要条件
      （RSFT > SFT）勉强满足但不稳固。Joint Evi-F1 0.265 远低于 DREEAM 57.34——
      但这是评估协议差异而非方法劣势（DREEAM 的 rel_f1 0.63 vs 我们 0.408 是 extraction gap）。
      论文必须用单独一节解释两种 Evi-F1 协议的差异，并坦诚 joint 指标的局限。
      在 reframed narrative 下，dev→test 衰减本身变成 analysis contribution：
      "生成式 evidence 方法对标注分布偏移更敏感" 是有价值的发现。

  - name: "EDCR pipeline 验证 + cross-method diagnostic table"
    plan_id: "plan_003"
    description: >
      在所有 evidence-producing 方法上计算 EDCR，验证 EDCR 作为独立诊断指标的 cross-method 区分能力。
    expected_results:
      sft_edcr: 0.7118
      rsft_ced_best_edcr: 0.635
      rsft_flatnli_edcr: 0.658
      reranker_edcr: 0.668
      grpo_ced_kl001_ckpt90_edcr: 0.8584
      grpo_lr5e6_ckpt100_edcr: 0.9876
      dpo_ced_edcr: 0.652
      grpo_g8_best_edcr: 0.742
      edcr_evi_f1_cond_pearson_r: -0.38
      edcr_rel_f1_pearson_r: -0.22
      edcr_range_across_methods: "[0.635, 0.988]"
    result_rationale: >
      EDCR 的 cross-method 诊断能力在 worst 档下被部分削弱。CED RSFT 与 flat-NLI RSFT 的 EDCR 差异
      仅 2.3pp（方向正确但不显著），说明 CED 对 distractor filtering 的额外价值有限。
      EDCR 与 conditional Evi-F1 的负相关仅 r=-0.38（弱到中等），部分高 EDCR 样本的 Evi-F1 也不高——
      两个指标有重叠但非互补。EDCR 与 rel_f1 的相关更弱（r=-0.22），说明 distractor citation
      与 extraction 质量只有弱关联。

      但 EDCR 在极端案例上仍有诊断价值：GRPO lr=5e-6 的 EDCR=0.988 标记出 "模型学会了引用证据但完全丧失抽取能力"
      的模式，而 Evi-F1=0.85 完全无法捕捉这个问题。EDCR 的 contribution 在于指标设计本身（揭示 Evi-F1 盲区），
      而非 CED 对 EDCR 的改善。
    tables:
      - name: "Table: Cross-Method EDCR Diagnostic"
        rows:
          - method: "GRPO+CED lr=5e-6 (ckpt-100)"
            rel_f1: 0.014
            evi_f1: 0.850
            edcr: 0.988
            note: "extreme decoupling"
          - method: "GRPO+CED kl=0.01 (ckpt-90)"
            rel_f1: 0.211
            evi_f1: 0.567
            edcr: 0.858
            note: "partial forgetting"
          - method: "GRPO G=8 (best ckpt)"
            rel_f1: 0.235
            evi_f1: 0.605
            edcr: 0.742
            note: "partial recovery"
          - method: "SFT baseline"
            rel_f1: 0.406
            evi_f1: 0.798
            edcr: 0.712
            note: ""
          - method: "CED-as-reranker"
            rel_f1: 0.413
            evi_f1: 0.802
            edcr: 0.668
            note: "inference-time only"
          - method: "RSFT flat-NLI"
            rel_f1: 0.456
            evi_f1: 0.812
            edcr: 0.658
            note: ""
          - method: "DPO+CED"
            rel_f1: 0.385
            evi_f1: 0.805
            edcr: 0.652
            note: "offline, avoids forgetting"
          - method: "RSFT+CED (s44)"
            rel_f1: 0.466
            evi_f1: 0.809
            edcr: 0.635
            note: "best EDCR"
    figures_description:
      - "Evi-F1 vs EDCR scatter plot (per-method centroids)，标注 GRPO 极端区域（高 evi_f1 + 高 EDCR），展示 Evi-F1 的诊断盲区"
      - "EDCR 分布箱线图 (per-method)，展示 GRPO 方法的 EDCR 方差远大于 RSFT 方法"
    analysis: >
      EDCR 作为诊断工具在极端案例上有价值（GRPO decoupling 的标志性信号），但在正常工作区间
      （RSFT/DPO/SFT）的区分力有限（range 仅 0.635-0.712）。"CED 改善 EDCR" 的方法论故事很弱
      （vs flat-NLI 仅 2.3pp 不显著）。Reframe: EDCR 的 contribution 在于指标设计本身
      + GRPO failure 的诊断案例，而非 CED 方法的独特效果。

  - name: "DREEAM baseline reproduction"
    plan_id: "plan_004"
    description: >
      在 DocRED dev set 上复现 DREEAM (RoBERTa-large) 的 Evi-F1，确认报告数字可复现，建立可比基线。
    expected_results:
      dreeam_dev_rel_f1_reproduced: 0.632
      dreeam_dev_evi_f1_reproduced: 0.608
      dreeam_paper_test_evi_f1: 0.5734
      dreeam_paper_test_rel_f1: 0.630
      dreeam_dev_to_test_evi_f1_drop: 0.0346
      sais_dev_evi_f1_reproduced: 0.578
      sais_dev_rel_f1_reproduced: 0.615
      our_rsft_dev_evi_f1_joint: 0.338
      our_rsft_dev_evi_f1_joint_vs_dreeam_gap: -0.270
    result_rationale: >
      DREEAM 论文报告的 57.34 是 test set Evi-F1（joint 协议）。Dev set 复现值约 60.8，
      高于 test 3.46pp（encoder 方法也有 dev→test 衰减）。

      关键问题：我们的 joint Evi-F1（DREEAM 协议）在 dev set 约 0.338——远低于 DREEAM 的 0.608。
      原因并非 evidence 质量差，而是 rel_f1 gap：我们 0.466 vs DREEAM 0.632，
      joint 协议下 extraction 错误直接拉低 evidence 分数。
      Conditional Evi-F1 我们 0.809 远超 DREEAM 0.608，但两个协议不可直接对比。

      这产生叙事困境：用 conditional 对比则我们远超（+20pp），用 joint 对比则我们远逊（-27pp）。
      论文必须同时报告两种协议并诚实解释差异来源。在 worst 档下，reviewer 很可能攻击
      "你们 cherry-pick 了有利的评估协议"。
    tables:
      - name: "Table: DREEAM/SAIS Reproduction vs Our Method"
        rows:
          - method: "SAIS (reproduced, dev)"
            rel_f1: 0.615
            evi_f1_joint: 0.578
            evi_f1_cond: "N/A (attention-based)"
          - method: "DREEAM (reproduced, dev)"
            rel_f1: 0.632
            evi_f1_joint: 0.608
            evi_f1_cond: "N/A (attention-based)"
          - method: "RSFT+CED (dev)"
            rel_f1: 0.466
            evi_f1_joint: 0.338
            evi_f1_cond: 0.809
          - method: "DREEAM (paper, test)"
            rel_f1: 0.630
            evi_f1_joint: 0.5734
            evi_f1_cond: "N/A"
    figures_description:
      - "双 y 轴 bar chart: 左轴 rel_f1，右轴 evi_f1（joint + conditional 分色），展示 extraction gap 如何影响 joint Evi-F1"
    analysis: >
      DREEAM 复现成功但暴露了评估可比性难题。在 worst 档下，论文必须放弃 "超越 DREEAM" 的叙事，
      转为 "LLM generative evidence 的优劣分析"——conditional evidence 质量极高（0.809），
      但受限于 extraction 能力（rel_f1 0.466 vs encoder 0.632）。
      这在 reframed narrative 下反而是有趣的 finding：
      "LLM 可以生成极好的 evidence 但 extraction 能力落后于 encoder，两能力并非耦合"。

  - name: "CED-as-reranker"
    plan_id: "plan_005"
    description: >
      推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。
    expected_results:
      reranker_rel_f1: 0.413
      reranker_evi_f1: 0.802
      reranker_edcr: 0.668
      reranker_evi_f1_joint: 0.288
      sft_baseline_rel_f1: 0.4057
      sft_baseline_evi_f1: 0.7979
      sft_baseline_edcr: 0.7118
      reranker_over_sft_rel_f1_pp: 0.73
      reranker_over_sft_evi_f1_pp: 0.41
      reranker_over_sft_edcr_pp: -4.38
      reranker_inference_time_multiplier: 8.5
    result_rationale: >
      Reranker 效果有限（rel_f1 +0.73pp，EDCR -4.38pp vs SFT）且远不及 RSFT。
      根本原因：CED 重排只能在 SFT 已生成的 8 个候选中选择，而 SFT 候选的 evidence 分布
      本身偏向 distractor——SFT 的 systematic bias 使 8 个候选中 "低 EDCR" 的候选稀少
      （最优候选 EDCR 仍 ~0.55-0.60，远高于 gold evidence 的理论 EDCR=0）。

      Rel_f1 的微小提升来自 CED 兼顾 evidence 和 extraction 的联合打分偶尔选到了
      更好的抽取结果，但效果不稳定。推理时间 8.5x（每候选需 NLI 推理）
      使 reranker 在实际部署中不可行。

      在 worst 档下，reranker 降级为 ablation table 中的一行数据：
      证明 training-free CED application 不够，必须通过 RSFT 改变模型权重。
    tables:
      - name: "Table: CED-as-Reranker vs SFT vs RSFT (Dev Set)"
        rows:
          - method: "SFT baseline"
            rel_f1: 0.4057
            evi_f1: 0.7979
            edcr: 0.7118
            extra_train: "No"
            inference_cost: "1x"
          - method: "CED-as-reranker (N=8)"
            rel_f1: 0.413
            evi_f1: 0.802
            edcr: 0.668
            extra_train: "No"
            inference_cost: "8.5x"
          - method: "RSFT+CED (s44)"
            rel_f1: 0.4655
            evi_f1: 0.8087
            edcr: 0.635
            extra_train: "Yes"
            inference_cost: "1x"
    figures_description:
      - "EDCR 分布直方图: SFT 8 候选的 per-candidate EDCR 分布，展示 reranker 的 selection ceiling——最优候选 EDCR 仍 >0.55"
    analysis: >
      Reranker 效果有限，印证 SFT 候选池本身的 distractor bias 是 bottleneck。
      RSFT 通过改变模型权重从根源减少 distractor 引用，reranker 只能在已有候选中做选择。
      在 worst 档 reframe 下，reranker 降级为 ablation，但仍有方法论价值：
      证明 CED 的价值在于 training data curation 而非 inference-time selection。

  - name: "Model size ablation (1.7B / 8B)"
    plan_id: "plan_006"
    description: >
      Qwen3-1.7B 和 Qwen3-8B 上复现 RSFT+CED pipeline，验证方法对模型规模的泛化性。
    expected_results:
      qwen3_1_7b_sft_rel_f1: 0.312
      qwen3_1_7b_sft_evi_f1: 0.735
      qwen3_1_7b_rsft_rel_f1: 0.338
      qwen3_1_7b_rsft_evi_f1: 0.752
      qwen3_1_7b_rsft_edcr: 0.705
      qwen3_1_7b_rsft_gain_rel_f1_pp: 2.6
      qwen3_8b_sft_rel_f1: 0.458
      qwen3_8b_sft_evi_f1: 0.820
      qwen3_8b_rsft_rel_f1: 0.475
      qwen3_8b_rsft_evi_f1: 0.828
      qwen3_8b_rsft_edcr: 0.648
      qwen3_8b_rsft_gain_rel_f1_pp: 1.7
      qwen3_4b_rsft_gain_rel_f1_pp: 5.98
      rsft_gain_nonmonotonic: true
    result_rationale: >
      RSFT 收益对模型规模不鲁棒，呈倒 U 型：1.7B gain +2.6pp, 4B gain +5.98pp, 8B gain +1.7pp。

      1.7B 收益小的原因：小模型生成候选质量上限低，8 个候选中高质量候选极少，
      CED 筛选后训练数据量骤降（~1200 samples vs 4B 的 2718），数据不足以有效微调。
      且小模型的 LoRA 容量有限（相对模型参数比例更大），更容易过拟合少量 RSFT 数据。

      8B 收益小的原因：强模型 SFT baseline 已较好（0.458），候选质量整体较高，
      CED 筛选的增量价值边际递减。同时 8B + QLoRA 的有效参数更新比例更小，
      LoRA rank=64 在 8B 上的相对容量不足（4B 上 rank=64 ≈ 1.6% params，8B ≈ 0.8%）。

      4B 是 sweet spot 可能是 LoRA rank/lr 超参恰好匹配而非方法论优势。
      Reviewer 会指出 "方法效果高度依赖模型规模和超参配置"。
    tables:
      - name: "Table: Model Size Ablation (Dev Set)"
        rows:
          - model: "Qwen3-1.7B SFT"
            rel_f1: 0.312
            evi_f1: 0.735
            edcr: 0.720
          - model: "Qwen3-1.7B RSFT"
            rel_f1: 0.338
            evi_f1: 0.752
            edcr: 0.705
            delta_rel_f1: "+2.6pp"
          - model: "Qwen3-4B SFT"
            rel_f1: 0.406
            evi_f1: 0.798
            edcr: 0.712
          - model: "Qwen3-4B RSFT"
            rel_f1: 0.466
            evi_f1: 0.809
            edcr: 0.635
            delta_rel_f1: "+5.98pp"
          - model: "Qwen3-8B SFT"
            rel_f1: 0.458
            evi_f1: 0.820
            edcr: 0.665
          - model: "Qwen3-8B RSFT"
            rel_f1: 0.475
            evi_f1: 0.828
            edcr: 0.648
            delta_rel_f1: "+1.7pp"
    figures_description:
      - "折线图: RSFT gain (Δrel_f1) vs model size (1.7B/4B/8B)，展示倒 U 型非单调关系"
    analysis: >
      RSFT 收益对模型规模不鲁棒，4B sweet spot 可能是超参匹配巧合。
      在 reframed narrative 下，这转化为 analysis contribution：
      "RSFT 的最优超参与模型规模耦合，practitioners 需 per-scale tuning"——
      但也意味着方法缺乏 out-of-the-box 泛化性，削弱 systematic study 的实用价值。

  - name: "Re-DocRED extension"
    plan_id: "plan_007"
    description: >
      在 Re-DocRED（修正 false negative 标注）上评估 RSFT+CED，验证更干净标注下的表现。
    expected_results:
      redocred_sft_rel_f1: 0.525
      redocred_sft_evi_f1: 0.810
      redocred_rsft_rel_f1: 0.548
      redocred_rsft_evi_f1: 0.818
      redocred_rsft_edcr: 0.592
      redocred_rsft_gain_rel_f1_pp: 2.3
      redocred_rsft_gain_evi_f1_pp: 0.8
      docred_rsft_gain_rel_f1_pp: 5.98
    result_rationale: >
      Re-DocRED 的标注更完整（大量 false negative 被修正），SFT baseline 显著更强
      （rel_f1 0.525 vs DocRED 0.406）。RSFT 增量收益缩小至 +2.3pp（vs DocRED +5.98pp）。

      原因：(1) 更完整的 gold triples 减少了 SFT 的低悬果实空间——SFT 在 Re-DocRED 上已学到
      更多正确 pattern，RSFT 能额外发现的增量更少；(2) 更完整的 gold evidence 标注
      使之前被标为 distractor 的句子回归 gold，CED 的 false distractor 问题缓解，
      但同时 CED 的额外筛选价值也降低（distractor 本身变少了）；
      (3) EDCR 0.592 低于 DocRED 0.635，因更完整标注降低了 distractor 比例。

      对 worst 档叙事的影响：RSFT 在 noisy annotation (DocRED) 下价值更大，
      在 clean annotation (Re-DocRED) 下边际递减——可论证 RSFT 是一种 annotation noise robustness 机制。
    tables:
      - name: "Table: DocRED vs Re-DocRED"
        rows:
          - dataset: "DocRED SFT"
            rel_f1: 0.406
            evi_f1: 0.798
            edcr: 0.712
          - dataset: "DocRED RSFT"
            rel_f1: 0.466
            evi_f1: 0.809
            edcr: 0.635
            delta: "+5.98pp"
          - dataset: "Re-DocRED SFT"
            rel_f1: 0.525
            evi_f1: 0.810
            edcr: 0.635
          - dataset: "Re-DocRED RSFT"
            rel_f1: 0.548
            evi_f1: 0.818
            edcr: 0.592
            delta: "+2.3pp"
    figures_description: []
    analysis: >
      Re-DocRED 上 RSFT 收益缩小是 worst 档的预期结果。在 reframed narrative 下，
      这变成双刃剑：一方面 reviewer 质疑方法在 clean data 上的价值，
      另一方面可论证 "RSFT 在 noisy annotation 下更有价值"。
      需与 model size ablation 一起，诚实讨论 RSFT 的 applicability conditions。

  - name: "top_k ablation (k=1 vs k=3)"
    plan_id: "plan_008"
    description: >
      CED scoring 筛选 top_k=3（~8000 samples）vs top_k=1（~2718 samples），
      验证 CED 过滤严格度对 RSFT 质量的影响。
    expected_results:
      topk1_samples: 2718
      topk3_samples: 8154
      topk1_mean_ced: 0.668
      topk3_mean_ced: 0.512
      topk1_rsft_rel_f1: 0.4655
      topk1_rsft_evi_f1: 0.8087
      topk1_rsft_edcr: 0.635
      topk3_rsft_rel_f1: 0.458
      topk3_rsft_evi_f1: 0.805
      topk3_rsft_edcr: 0.672
      topk3_vs_topk1_rel_f1_gap_pp: -0.75
      topk3_vs_topk1_evi_f1_gap_pp: -0.37
      topk3_vs_topk1_edcr_gap_pp: 3.7
    result_rationale: >
      Top_k=3 用 3x 数据量（8154 vs 2718）换来轻微退化（rel_f1 -0.75pp, evi_f1 -0.37pp, EDCR +3.7pp）。
      退化幅度很小，说明 CED 分数在 top1→top3 区间的质量差异有限（mean CED 从 0.668 降至 0.512，
      但 floor 仍在可接受范围）。

      这进一步支持 worst 档核心论点：CED scoring 的精细程度不是关键因素。
      Top_k=3 的更多数据带来的 diversity 和 CED score 下降带来的 noise 大致抵消。
      Reviewer 可用此结果论证 "随便什么 NLI 打分函数做 threshold filtering 都行"。

      在 reframed narrative 下，top_k ablation 可纳入 practical guideline：
      "top_k=1 质量最优但数据量受限，top_k=3 是合理 tradeoff"。
    tables:
      - name: "Table: top_k Ablation"
        rows:
          - config: "top_k=1 (2718 samples, mean CED 0.668)"
            rel_f1: 0.4655
            evi_f1: 0.8087
            edcr: 0.635
          - config: "top_k=3 (8154 samples, mean CED 0.512)"
            rel_f1: 0.458
            evi_f1: 0.805
            edcr: 0.672
    figures_description:
      - "CED score 分布直方图: top_k=1 selected vs top_k=3 selected，展示 quality-quantity tradeoff"
    analysis: >
      top_k 对 RSFT 影响有限，与 plan_001 结论一致——rejection sampling 本身（而非 scoring 精度）
      是关键。在 reframed narrative 下纳入 practical guideline section。

  - name: "GRPO G=8 实验"
    plan_id: "plan_011"
    description: >
      用 G=8 + CED reward + kl_coef=0.01 重跑 GRPO，验证 G=4 的 catastrophic forgetting
      是否因 advantage estimation noise 导致。用 gradient accumulation 适配显存。
    expected_results:
      grpo_g8_best_rel_f1: 0.235
      grpo_g8_best_evi_f1: 0.605
      grpo_g8_best_edcr: 0.742
      grpo_g8_best_reward: 1.52
      grpo_g8_best_rel_f1_step: 80
      grpo_g8_forgetting_onset_step: 20
      grpo_g8_final_rel_f1: 0.198
      grpo_g8_final_evi_f1: 0.635
      grpo_g8_frac_zero_std_final: 0.08
      grpo_g4_best_rel_f1: 0.217
      grpo_g4_best_evi_f1: 0.575
      g8_vs_g4_rel_f1_improvement_pp: 1.8
      g8_vs_g4_evi_f1_improvement_pp: 3.0
      g8_still_catastrophic_vs_sft: true
      g8_partial_recovery: true
      trajectory_step_20: {rel_f1: 0.085, evi_f1: 0.52, reward: 0.95}
      trajectory_step_40: {rel_f1: 0.168, evi_f1: 0.55, reward: 1.15}
      trajectory_step_60: {rel_f1: 0.225, evi_f1: 0.58, reward: 1.35}
      trajectory_step_80: {rel_f1: 0.235, evi_f1: 0.605, reward: 1.52}
      trajectory_step_100: {rel_f1: 0.198, evi_f1: 0.635, reward: 1.48}
    result_rationale: >
      在 worst 档下，G=8 部分恢复但仍远低于 SFT baseline（0.235 vs 0.406，-17.1pp）。

      部分恢复的原因：G=8 的 advantage estimation 噪声更低——每个 prompt 有 8 个 rollout，
      group-relative advantage 的标准差估计更准确（理论上 std 误差 ∝ 1/√G），减少了
      "高 reward 但低质量候选获得正 advantage" 的频率。Rel_f1 peak 0.235 vs G=4 的 0.217（+1.8pp），
      evi_f1 0.605 vs 0.575（+3.0pp），方向一致但提升有限。

      仍然 catastrophic 的原因：
      (1) QLoRA 的离散化梯度在 structured output 空间中仍产生不稳定更新——G=8 缓解但未解决；
      (2) CED reward 的 per-sentence 细粒度在 GRPO 的 sequence-level advantage 下
      仍存在 credit assignment 问题——reward 信号无法精确归因到具体 token 决策；
      (3) 100 步训练中 rel_f1 在 step 80 达峰后开始下降（0.235→0.198），forgetting 仍在发生，
      只是 onset 延迟到 ~step 20（vs G=4 ~step 5-10）。

      对 Claim 3 的影响：G=8 的部分恢复证明 G=4 failure 有 advantage noise 成分，
      Claim 3 必须进一步限定为 "GRPO+QLoRA+small-to-moderate group size"。
      核心论点从 "GRPO categorically fails" 弱化为 "GRPO 在 structured IE 上极其脆弱，
      需要远超标准配置的 group size 才能勉强工作"。
      Reviewer 会要求 G=16/G=32 实验，但 GPU 显存限制使这些不可行（需论文中声明）。
    tables:
      - name: "Table: GRPO G=4 vs G=8 Comparison"
        rows:
          - config: "GRPO G=4 (kl=0.01, best ckpt)"
            rel_f1: 0.217
            evi_f1: 0.575
            edcr: 0.858
            best_reward: 1.37
          - config: "GRPO G=8 (kl=0.01, best ckpt)"
            rel_f1: 0.235
            evi_f1: 0.605
            edcr: 0.742
            best_reward: 1.52
          - config: "SFT baseline"
            rel_f1: 0.406
            evi_f1: 0.798
            edcr: 0.712
          - config: "RSFT+CED (s44)"
            rel_f1: 0.466
            evi_f1: 0.809
            edcr: 0.635
      - name: "Table: GRPO G=8 Training Trajectory"
        rows:
          - step: 20
            rel_f1: 0.085
            evi_f1: 0.52
            reward: 0.95
            frac_zero_std: 0.02
          - step: 40
            rel_f1: 0.168
            evi_f1: 0.55
            reward: 1.15
            frac_zero_std: 0.03
          - step: 60
            rel_f1: 0.225
            evi_f1: 0.58
            reward: 1.35
            frac_zero_std: 0.05
          - step: 80
            rel_f1: 0.235
            evi_f1: 0.605
            reward: 1.52
            frac_zero_std: 0.06
          - step: 100
            rel_f1: 0.198
            evi_f1: 0.635
            reward: 1.48
            frac_zero_std: 0.08
    figures_description:
      - "双轴折线图: G=4 vs G=8 的 rel_f1 trajectory (solid) + reward trajectory (dashed)，展示 G=8 的 delayed forgetting onset 和 higher peak"
      - "Bar chart: G=4 vs G=8 vs SFT vs RSFT 的 rel_f1/evi_f1/EDCR 对比，突出所有 GRPO 配置仍远低于 SFT"
    analysis: >
      G=8 的部分恢复是 worst 档最关键的实验结果，直接动摇 Claim 3。

      论文必须承认：(1) G=4 的 failure 部分由 advantage noise 驱动，非纯粹 structural IE 固有问题；
      (2) G=8 仍然失败（-17.1pp vs SFT），但失败程度显著减轻，趋势暗示 G=16+ 可能进一步恢复；
      (3) Claim 3 的范围必须限定为 "GRPO+QLoRA 在 standard group sizes (4-8) 下对 structured IE
      catastrophically fragile"，并明确声明不排除 larger group sizes 的可能性。

      在 reframed narrative 下，G=4 vs G=8 的对比本身成为核心 finding：
      "group size 对 structured IE 的 GRPO 效果有非线性影响，远超 standard NLP tasks
      （在 reasoning/math 任务上 G=4 vs G=8 差异通常 <2pp）"。

  - name: "DPO+CED experiment"
    plan_id: "plan_012"
    description: >
      用 RSFT 候选数据构造 preference pairs (CED-preferred vs CED-rejected)，DPO 训练。
      验证 DPO 作为 online-offline 中间方法是否避免 GRPO 的 catastrophic forgetting。
    expected_results:
      dpo_rel_f1: 0.385
      dpo_evi_f1: 0.805
      dpo_edcr: 0.652
      dpo_evi_f1_joint: 0.268
      dpo_precision: 0.392
      dpo_recall: 0.378
      dpo_format_ok_rate: 0.998
      dpo_training_loss_final: 0.62
      dpo_preference_pairs: 2450
      dpo_vs_sft_rel_f1_delta_pp: -2.07
      dpo_vs_rsft_rel_f1_delta_pp: -8.05
      dpo_catastrophic_forgetting: false
      dpo_training_trajectory:
        step_50: {rel_f1: 0.375, eval_loss: 0.68}
        step_100: {rel_f1: 0.385, eval_loss: 0.64}
        step_150: {rel_f1: 0.382, eval_loss: 0.62}
        step_200: {rel_f1: 0.378, eval_loss: 0.625}
    result_rationale: >
      在 worst 档下，DPO rel_f1 = 0.385——接近 SFT baseline（0.406, -2.07pp）但远低于 RSFT（0.466, -8.05pp）。
      关键：DPO 没有 catastrophic forgetting（训练过程中 rel_f1 稳定在 0.375-0.385 区间），
      证明 offline preference learning 确实避免了 GRPO 的遗忘问题。

      DPO 低于 SFT 的原因：
      (1) DPO 的 preference pairs 由 CED-preferred（高 CED 分的候选）vs CED-rejected（低 CED 分的候选）
      构造，但 CED 分数差异主要在 evidence 维度而非 extraction 维度——DPO 学会了避免 bad evidence
      但没有学到 better extraction，在 relation extraction 上甚至略退化（precision 0.392 < SFT 0.404）；
      (2) DPO 对 preference margin 敏感，CED 分数差异在很多 pair 中很小（mean margin ~0.15），
      弱信号导致 DPO 学习不充分；
      (3) DPO 的 KL penalty 倾向于保守更新，在 LoRA 有限容量下进一步限制了学习。

      DPO 接近 SFT 而非接近 RSFT，说明 RSFT 的优势不仅在于 "避免 policy gradient"，
      更在于 "直接用高质量数据替换训练分布"——RSFT 改变了训练数据本身（rejection sampling 选出最优候选），
      而 DPO 只改变了 loss function（在原始候选对上做 preference learning）。

      对论文叙事的影响：GRPO < DPO ≈ SFT < RSFT 的排序揭示了一个 spectrum：
      online RL（GRPO）catastrophic fail → offline preference（DPO）stable but no gain →
      offline data curation（RSFT）effective。这个 spectrum 本身是有价值的 analysis finding。
    tables:
      - name: "Table: Online-Offline RL Spectrum (Dev Set)"
        rows:
          - method: "GRPO G=4 (online RL)"
            rel_f1: 0.217
            evi_f1: 0.575
            edcr: 0.858
            forgetting: "catastrophic"
          - method: "GRPO G=8 (online RL)"
            rel_f1: 0.235
            evi_f1: 0.605
            edcr: 0.742
            forgetting: "severe"
          - method: "DPO+CED (offline preference)"
            rel_f1: 0.385
            evi_f1: 0.805
            edcr: 0.652
            forgetting: "none"
          - method: "SFT baseline"
            rel_f1: 0.406
            evi_f1: 0.798
            edcr: 0.712
            forgetting: "N/A"
          - method: "RSFT flat-NLI (offline curation)"
            rel_f1: 0.456
            evi_f1: 0.812
            edcr: 0.658
            forgetting: "none"
          - method: "RSFT+CED (offline curation)"
            rel_f1: 0.466
            evi_f1: 0.809
            edcr: 0.635
            forgetting: "none"
    figures_description:
      - "Online-offline spectrum 图: x 轴从 online (GRPO G=4) → semi-online (GRPO G=8) → offline-preference (DPO) → offline-curation (RSFT)，y 轴 rel_f1，展示单调递增趋势"
      - "Training dynamics 对比: GRPO G=4 / GRPO G=8 / DPO / RSFT 的 rel_f1 vs training step，展示 GRPO 的 divergence vs DPO/RSFT 的 stability"
    analysis: >
      DPO 是 worst 档叙事的关键拼图。GRPO → DPO → RSFT 的 spectrum 揭示：
      structured IE 需要完全避免 policy gradient（DPO 虽 offline 但仍用 implicit reward model），
      数据 curation（RSFT）才是最 robust 的路径。

      但 DPO 接近 RSFT 的 worst 档预期（0.385 vs 0.466）部分被推翻——如果 DPO rel_f1 ≥ 0.35
      但明显低于 RSFT，那 RSFT 的优势在于 data quality（not just avoiding gradients）。
      这对 reframed narrative 有利：可以论证 RSFT 的独特贡献是 "training data is the algorithm"。

  - name: "EDCR 人工标注验证"
    plan_id: "plan_013"
    description: >
      100 个样本，人工判断每个 cited evidence sentence 是否真正支持对应 relation。
      计算 EDCR 与人工判断的相关性，验证 EDCR 作为自动指标的有效性。
    expected_results:
      n_samples: 100
      n_annotated_sentences: 520
      edcr_human_pearson_r: 0.28
      edcr_human_spearman_rho: 0.31
      human_precision_of_edcr_flagged: 0.55
      human_recall_of_edcr_flagged: 0.62
      inter_annotator_agreement_kappa: 0.58
      false_positive_rate: 0.45
      false_negative_rate: 0.38
      human_judged_true_distractor_rate: 0.48
      edcr_predicted_distractor_rate: 0.65
      edcr_overestimates_distractors: true
    result_rationale: >
      在 worst 档下，EDCR 与人工判断的 Pearson r = 0.28（弱相关），远低于自动指标通常要求的 r > 0.6。

      EDCR 偏高的根本原因：EDCR 的定义——entity-sharing non-gold sentences 被自动标为 distractor——
      过于粗暴。人工审查发现 ~45% 的 EDCR-flagged "distractor" 实际上提供了部分支持证据
      （partial support），只是未被 DocRED annotator 纳入 gold evidence set。
      DocRED 标注不完整（已知问题，Re-DocRED 论文的核心动机）导致 EDCR 系统性高估 distractor 比例。

      具体分解：
      - 人工判断的真正 distractor 率 48%（vs EDCR 认为的 65%），17pp 差异来自 annotation noise；
      - EDCR 的 precision（被标记的 distractor 中真正是 distractor 的比例）仅 55%；
      - EDCR 的 recall（真正 distractor 中被 EDCR 发现的比例）为 62%——中等，但漏掉了 38% 的
        non-entity-sharing distractor（基于表面相似性而非 entity 共享的 distractor）。

      Inter-annotator agreement κ=0.58（moderate）反映了 evidence support 判断本身的主观性——
      部分句子是否 "支持" 一个 relation 存在灰色地带。

      对 Claim 4 的影响：EDCR 作为 automatic metric 的独立价值存疑。
      可以论证 EDCR 提供 "directional signal"（方向正确但精度不够），
      但不能作为 gold standard 替代人工判断。
    tables:
      - name: "Table: EDCR vs Human Judgment"
        rows:
          - metric: "Pearson r"
            value: 0.28
            note: "weak correlation"
          - metric: "Spearman ρ"
            value: 0.31
            note: "weak rank correlation"
          - metric: "EDCR precision (distractor detection)"
            value: 0.55
            note: "45% false positives"
          - metric: "EDCR recall (distractor detection)"
            value: 0.62
            note: "38% misses (non-entity distractors)"
          - metric: "Human true distractor rate"
            value: 0.48
            note: "vs EDCR predicted 0.65"
          - metric: "Inter-annotator κ"
            value: 0.58
            note: "moderate agreement"
      - name: "Table: Error Analysis of EDCR Disagreements"
        rows:
          - error_type: "EDCR flags as distractor, human says supportive"
            count: 47
            pct: "45%"
            cause: "Incomplete gold annotation (sentence provides partial support)"
          - error_type: "EDCR misses true distractor"
            count: 24
            pct: "38%"
            cause: "Non-entity distractor (surface similarity, no shared entity)"
          - error_type: "Agreement: both flag distractor"
            count: 57
            pct: "55%"
            cause: "Clear entity-sharing non-supportive sentence"
          - error_type: "Agreement: both say supportive"
            count: 392
            pct: "75%"
            cause: "Gold or near-gold evidence sentence"
    figures_description:
      - "Confusion matrix heatmap: EDCR binary (distractor vs supportive) vs Human binary，展示 45% false positive rate"
      - "Per-sample scatter: EDCR value (0-1) vs human-judged distractor ratio (0-1)，标注 r=0.28 regression line"
    analysis: >
      EDCR 与人工判断弱相关（r=0.28），主要噪声源是 DocRED 标注不完整导致的 systematic overestimation。
      EDCR 不适合作为独立 automatic metric 替代人工评估，但仍有 directional diagnostic 价值——
      EDCR 极高（>0.9）确实标志着模型严重引用 distractor（如 GRPO 的 0.988）。

      在 reframed narrative 下，这个 negative result 本身是 contribution：
      "evidence evaluation 比想象中更难，自动指标（无论 Evi-F1 还是 EDCR）都有显著局限"——
      这为 "首个 LLM DocRE evidence benchmark" 的 contribution 增加了 evaluation challenge dimension。
      论文应呼吁社区建立更好的 evidence evaluation protocol。

  - name: "GRPO forgetting 详细分析 + 可视化"
    plan_id: "plan_009"
    description: >
      整理全部 GRPO checkpoint 轨迹（G=4 + G=8，3 种 reward），绘制 forgetting dynamics 可视化。
    expected_results:
      grpo_ced_kl001_g4_trajectory:
        step_10: {rel_f1: 0.003, evi_f1: 0.72, reward: 0.85}
        step_20: {rel_f1: 0.009, evi_f1: 0.423, reward: 0.92}
        step_30: {rel_f1: 0.034, evi_f1: 0.589, reward: 1.05}
        step_50: {rel_f1: 0.156, evi_f1: 0.564, reward: 1.18}
        step_60: {rel_f1: 0.147, evi_f1: 0.576, reward: 1.22}
        step_90: {rel_f1: 0.211, evi_f1: 0.567, reward: 1.37}
        step_100: {rel_f1: 0.217, evi_f1: 0.575, reward: 1.20}
      grpo_lr5e6_g4_trajectory:
        step_20: {rel_f1: 0.008, evi_f1: 0.628, reward: 0.60}
        step_40: {rel_f1: 0.007, evi_f1: 0.758, reward: 0.75}
        step_60: {rel_f1: 0.009, evi_f1: 0.810, reward: 0.88}
        step_80: {rel_f1: 0.012, evi_f1: 0.828, reward: 0.95}
        step_100: {rel_f1: 0.014, evi_f1: 0.850, reward: 1.02}
      grpo_ced_kl001_g8_trajectory:
        step_20: {rel_f1: 0.085, evi_f1: 0.52, reward: 0.95}
        step_40: {rel_f1: 0.168, evi_f1: 0.55, reward: 1.15}
        step_60: {rel_f1: 0.225, evi_f1: 0.58, reward: 1.35}
        step_80: {rel_f1: 0.235, evi_f1: 0.605, reward: 1.52}
        step_100: {rel_f1: 0.198, evi_f1: 0.635, reward: 1.48}
      flatnli_collapse_step: 25
      extract_only_collapse_step: 30
      decoupling_evidence:
        lr5e6_evi_f1_at_step100: 0.850
        lr5e6_rel_f1_at_step100: 0.014
        sft_evi_f1: 0.798
        evidence_improves_extraction_collapses: true
    result_rationale: >
      GRPO 数据已完整（registry 中多个实验 + 新增 G=8 数据），此 plan 是整理和可视化。
      在 worst 档下，GRPO forgetting 分析升级为核心 contribution，融合 G=4/G=8 对比。

      关键 insight 从已有数据提取：
      (1) G=4 所有 reward type 全线失败——CED (rel_f1 max 0.217), flat-NLI (collapse at step 25),
      extract-only (collapse at step 30)。flat-NLI 最脆弱，因 reward 信号更 noisy；
      (2) G=8 延迟了 forgetting onset（~step 20 vs G=4 ~step 5）但未消除；
      (3) lr=5e-6 的极端 decoupling：evi_f1 持续上升至 0.850（>SFT 0.798）
      而 rel_f1 始终 <0.02——模型学会了 excellent evidence 但完全丧失 extraction；
      (4) reward ↑ + rel_f1 ↓ 的 scissors pattern 在所有配置中一致出现。

      在 worst 档 reframe 下，加入 G=8 数据使分析更 nuanced：
      不再是 "GRPO categorically fails" 而是 "GRPO sensitivity to group size is extreme
      in structured IE, suggesting advantage estimation quality is the key bottleneck"。
    tables:
      - name: "Table: GRPO Forgetting Summary (All Configs)"
        rows:
          - config: "CED G=4 (lr=5e-5, KL=0.01)"
            best_rel_f1: 0.217
            peak_evi_f1: 0.575
            best_reward: 1.37
            forgetting: "slow decay"
          - config: "CED G=4 (lr=5e-6)"
            best_rel_f1: 0.014
            peak_evi_f1: 0.850
            best_reward: 1.02
            forgetting: "never recovers, extreme decoupling"
          - config: "CED G=8 (lr=5e-5, KL=0.01)"
            best_rel_f1: 0.235
            peak_evi_f1: 0.605
            best_reward: 1.52
            forgetting: "delayed onset, still severe"
          - config: "flat-NLI G=4"
            best_rel_f1: "~0"
            peak_evi_f1: "~0"
            best_reward: 0.293
            forgetting: "immediate collapse (step 25)"
          - config: "extract-only G=4"
            best_rel_f1: "~0"
            peak_evi_f1: "~0"
            best_reward: "~0"
            forgetting: "immediate collapse (step 30)"
    figures_description:
      - "Figure: Reward-Task Divergence (5-panel) — 每 panel 一个配置，x 轴 training step，双 y 轴 reward (blue) + rel_f1 (red dashed)，展示 scissors pattern。新增 G=8 panel。"
      - "Figure: Evidence-Extraction Decoupling — lr=5e-6 的 evi_f1 vs rel_f1 trajectory，标注 SFT baseline 水平线，展示 evi_f1 超越 SFT 而 rel_f1 崩溃"
      - "Figure: Group Size Effect — G=4 vs G=8 的 rel_f1 trajectory 叠加，标注 forgetting onset 和 peak，展示 G=8 的 delayed but persistent forgetting"
    analysis: >
      在 worst 档 reframe 下，这是论文最有深度的 contribution。G=4 vs G=8 对比 +
      lr=5e-6 extreme decoupling + 3 reward type 全线失败 构成完整的分析框架。
      核心 takeaway："GRPO+QLoRA 在 structured IE 上需要 atypically large group sizes，
      且 evidence learning 和 extraction 在 online RL 中 decouple——
      模型会优化更容易获取 reward 的 evidence 维度而牺牲更难的 extraction 维度"。

  - name: "NLI model ablation (DeBERTa-base vs large)"
    plan_id: "plan_010"
    description: >
      DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer 的对比，
      验证 NLI 模型能力对 CED 打分质量的影响。
    expected_results:
      deberta_base_mean_margin: 0.48
      deberta_base_disc_accuracy: 0.815
      deberta_base_rsft_rel_f1: 0.4655
      deberta_base_rsft_evi_f1: 0.8087
      deberta_base_rsft_edcr: 0.635
      deberta_large_mean_margin: 0.52
      deberta_large_disc_accuracy: 0.835
      deberta_large_rsft_rel_f1: 0.459
      deberta_large_rsft_evi_f1: 0.812
      deberta_large_rsft_edcr: 0.641
      base_vs_large_rel_f1_gap_pp: -0.65
      base_vs_large_evi_f1_gap_pp: 0.33
      base_vs_large_edcr_gap_pp: 0.6
      candidate_overlap_base_vs_large: 0.87
      large_inference_time_multiplier: 2.8
    result_rationale: >
      DeBERTa-large 的更强 NLI 能力（disc accuracy 83.5% vs 81.5%）未转化为下游 RSFT 差异。
      Rel_f1 base 0.466 vs large 0.459（base 反而略高 -0.65pp），evi_f1 差 +0.33pp，EDCR 差 +0.6pp——
      全部在噪声范围内。

      原因与 plan_001（CED vs flat-NLI）一致：scoring function 的精度不是 RSFT 成功的关键。
      DeBERTa-large 的更大 margin（0.52 vs 0.48）改变了部分候选的排序，但 selected samples
      重叠度 87%——绝大部分候选在两个 scorer 下做出相同筛选决策。
      Large 模型的 NLI 推理时间 2.8x base，cost-benefit 完全不合理。

      在 reframed narrative 下，这是一句话结论：
      "NLI scorer 能力在 base 级别已饱和，RSFT 对 scoring precision 不敏感"。
    tables:
      - name: "Table: NLI Model Ablation"
        rows:
          - scorer: "DeBERTa-v3-base"
            mean_margin: 0.48
            disc_acc: 0.815
            rsft_rel_f1: 0.4655
            rsft_evi_f1: 0.8087
            rsft_edcr: 0.635
          - scorer: "DeBERTa-v3-large"
            mean_margin: 0.52
            disc_acc: 0.835
            rsft_rel_f1: 0.459
            rsft_evi_f1: 0.812
            rsft_edcr: 0.641
    figures_description: []
    analysis: >
      与 plan_001 形成一致结论：无论是 scoring function 选择（CED vs flat-NLI）还是
      NLI 模型能力（base vs large），RSFT 的效果都不受影响。
      "Rejection sampling 本身是关键，scoring 只需 pass a quality floor" 是 worst 档叙事的
      recurring theme，可整合为论文的 practical takeaway。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bef5255c-6925-4564-a845-00b149d24014",
  "isSidechain": false,
  "requestId": "req_011Cb4TTLYk6AXXvgPhxceox",
  "type": "assistant",
  "uuid": "72c521e0-813e-414d-ac4d-253039e783ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SxK3K1xBUZ7qYAJnLH6Agd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 226,
      "cache_read_input_tokens": 53617,
      "output_tokens": 22505,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 22505,
          "cache_read_input_tokens": 53617,
          "cache_creation_input_tokens": 226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 226
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

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：RSFT 优势在 test set 上大幅缩水，且 GRPO G=8 部分恢复，核心叙事需要全面 reframe 核心假设：['CED vs flat-NLI 无差异或 flat-NLI 略优（Δevi_f1 < 0.3pp），CED 的对比性设计在 RSFT 间接作用下无可观测效果', 'Test set…",
  "leafUuid": "72c521e0-813e-414d-ac4d-253039e783ae",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Systematic LLM evidence generation for DocRE under worst-case outcomes",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：RSFT 优势在 test set 上大幅缩水，且 GRPO G=8 部分恢复，核心叙事需要全面 reframe 核心假设：['CED vs flat-NLI 无差异或 flat-NLI 略优（Δevi_f1 < 0.3pp），CED 的对比性设计在 RSFT 间接作用下无可观测效果', 'Test set…",
  "leafUuid": "72c521e0-813e-414d-ac4d-253039e783ae",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Systematic LLM evidence generation for DocRE under worst-case outcomes",
  "sessionId": "9e91ad84-b38b-4f46-b28b-5d00fe45e71e"
}
```

---
