# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：第三模型不对称消失或反转，核心 C2 claim 崩塌，需重新定位论文 angle 核心假设：['第三模型不对称 <2pp 或方向反转（EN→ZH >

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-2/5cce21d6-2585-4f07-8410-bde5fd24be9b.jsonl`
- **Structured JSON:** [`f0d871b839011246c641.json`](../../sessions/f0/f0d871b839011246c641.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T02:51:50.994Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T02:51:50.994Z",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：第三模型不对称消失或反转，核心 C2 claim 崩塌，需重新定位论文 angle\n核心假设：['第三模型不对称 <2pp 或方向反转（EN→ZH > ZH→EN）', '仅 Llama 显著，Qwen+第三模型均不显著，方向不全一致', '不对称性可能是 Llama 训练数据分布的 artifact 而非通用机制', 'Track 2/3 均无法在 DDL 前完成', 'COMET ablation 在 Llama 上出现与 Qwen 不一致的方向（质量确实影响 Llama）']\n关键指标范围：{'third_model_asymmetry_gap_pp': [-3.0, 2.0], 'significant_asymmetry_models_of_3': [0, 1], 'consistent_direction_models_of_3': [1, 2], 'third_model_within_lang_acc': [0.65, 0.75], 'cross_lingual_transfer_acc_range': [0.58, 0.7], 'mlp_gain_weak_direction_pp_third_model': [-1.0, 3.0], 'sae_cross_lingual_jaccard_mid_layer': [0.0, 0.0], 'lang_pairs_validated': [1, 1], 'tracks_submission_ready': [1, 1]}\n叙事方向：C2 不对称性降级为 observation，不再作为核心 claim。Reframe 路径（按优先级）：\nPath A \"Architecture-dependent cross-lingual conflict processing\"—— 不对称性的存在与否本身取决于架构/训练数据，这是一个 finding 而非 failure。 主 claim 变为：冲突信号跨语言可检测（C1 robust），但迁移特性是架构依赖的， 揭示多语言 LLM 内部跨语言对齐程度的异质性。引用 Wendler et al. (2024)  \"Llamas Know What GPTs Don't Show\" 的跨架构差异发现，定位为该方向的机制扩展。\nPath B \"Cross-lingual probing methodology + negative result\"—— 聚焦 confound exclusion pipeline（token overlap 分析 + COMET ablation）作为  方法论贡献，不对称性作为 \"hypothesis tested and bounded\" 的严格实验。 引用 Rogers et al. \"negative results in NLP\" 框架。\n两条路径均保持 ICLR 目标：Path A 走 empirical analysis track， Path B 需要显著加厚实验密度（5+ 模型、3+ 语言对）补偿 claim 强度下降。 关键：worst 情况下 C1 仍然成立（within-lang acc 65-75%，均远超 chance）， 论文不会 \"没东西可写\"，只是叙事重心从 mechanism 转向 characterization。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: clkc_mech_interp\nfocus: 重点评估：1) C2 不对称性 claim 在 Llama borderline 显著 + Qwen 不显著的情况下能否撑住；2) 只有 Track 1 probing 无 Track 2/3 SAE+steering 时论文贡献强度是否足够 ICLR；3) back-translation COMET 低但 ablation 排除 confounder 的 framing 是否说服审稿人\n\n## paper_framing.md\n\n# Paper Framing — clkc_mech_interp\n\n> 最后更新: 2026-05-22 | 目标: ICLR 2027 (DDL ~2026-09-24)\n\n## Core Insight\n\n多语言 LLM 中，跨语言知识冲突的检测信号可在残差流中被线性探针检测，且跨语言迁移呈现**方向性不对称**（ZH→EN >> EN→ZH ~7.2pp），该不对称性跨架构高度一致（Llama-3.1-8B 与 Qwen3-8B）。这为 CLEAR (Zhao et al. 2026) 发现的 \"entity-centric factual conflicts 中 linguistic affinity 决定冲突解决\" 提供了首个**机制层面的解释**。\n\n**注意**: CLEAR 的发现是 task-dependent 的——entity-centric factual conflicts 由 linguistic affinity 主导，reasoning-intensive tasks 由 resource abundance 主导。我们使用 ConflictQA（entity-centric），引用 CLEAR 时必须限定为 entity-centric 场景。\n\n## Narrative Structure\n\n**现象驱动的机制解释**（非 \"applying X to Y\"）：\n\n1. **Phenomenon**: CLEAR 发现在 entity-centric factual conflicts 中，linguistic affinity（而非 resource abundance）决定跨语言冲突解决，但未提供机制解释\n2. **Mechanistic question**: 冲突信号在模型内部如何编码？是 language-universal 还是 language-specific？为什么 similarity 起决定作用？\n3. **Our answer**: 通过残差流探针、SAE 特征分析、激活干预三条互补分析轨道，揭示冲突检测信号的跨语言结构——是否共享、在哪些层出现、能否用于干预\n\n**Secondary framing**: SAE-based mechanistic interpretability 工具在跨语言条件下的 stress test——probing / SAE / steering 三种工具的跨语言适用性边界\n\n## Competing Hypotheses (pre-registered)\n\n**H1 — English-anchored universal detection**:\n冲突检测信号本身是 language-independent 的（\"是否存在冲突\" 是语言无关判断），编码在 mid-layer 共享表征空间中。final-layer language transition 引入 similarity-dependent 干扰，影响 resolution 但不影响 detection。\n- 预测: mid-layer conflict feature 跨语言 Jaccard >> late-layer Jaccard (paired permutation test p < 0.05)\n- 预测: 英语探针跨语言迁移更强（英语作为训练数据主导语言，表征空间以英语为锚点）\n\n**H2 — Language-pair-specific encoding**:\n冲突特征从 mid-layer 起即为 language-pair-specific 的，linguistic distance 直接编码在冲突表征中。\n- 预测: mid-layer 和 late-layer Jaccard 无显著差异，或 mid < late\n- 预测: 探针迁移准确率与语言对 typological distance 强相关\n\n**MVP 证据倾向**:\n当前双模型结果倾向 **H1 的变体**——ZH→EN 迁移（71-72%）显著强于 EN→ZH（64-65%），暗示冲突信号以英语表征空间为锚点编码。非线性成分（MLP EN→ZH +9.2pp vs linear）提示 EN→ZH 方向的跨语言映射更复杂。\n\n## Core Claims\n\n### Claim 1: Cross-lingual conflict detectability\n**Statement**: 跨语言知识冲突信号可在残差流中被线性探针检测，准确率显著高于随机基线。\n**Evidence needed**:\n- ≥2 model architectures 的 within-language probe acc > 70% (balanced) ✅ (Llama 77.1%, Qwen 75.3%)\n- Permutation test p < 0.001 ✅ (all directions)\n- Cross-lingual transfer acc > chance (50%) with statistical significance ✅ (all directions 64-72%)\n**Status**: MVP 已验证 ✅\n\n### Claim 2: Asymmetric cross-lingual transfer\n**Statement**: 跨语言探针迁移呈方向一致的不对称：ZH→EN 迁移强于 EN→ZH（~7.2pp），效果量跨架构高度一致（Llama 显著，Qwen 方向一致但未达显著）。\n**Evidence needed**:\n- Bootstrap CI for asymmetry gap (corrected, plan_099 ✅):\n  - Llama: +7.22pp, CI [1.1%, 13.6%] — 排除零但 borderline ✅\n  - Qwen: +7.18pp, CI [-1.2%, 13.4%] — 含零，方向一致 ⚠️\n- ≥2 models show consistent effect size ✅ (7.22pp vs 7.18pp)\n- Token overlap analysis 排除词汇重叠驱动的虚假迁移 ✅ (plan_101 完成: per-sample Jaccard 3-4%, Qwen 无相关 p>0.4, Llama 显著负相关 r=-0.15 p=0.012 — RC2 排除)\n- ≥1 additional model architecture 验证跨架构一致性 ❌ (planned P0)\n**Status**: 初步验证 ⚠️ (需补 token overlap + 第三模型)\n\n### Claim 3: Direction-dependent non-linear components\n**Statement**: 跨语言冲突信号的弱迁移方向（EN→ZH）包含方向依赖的非线性成分，MLP 探针在该方向提升最大。跨架构一致方向但幅度不同（Llama +9.2pp single-seed / ~+4.7pp bootstrap-corrected, Qwen +2.3pp），暗示非线性成分与模型的跨语言对齐程度相关。\n**Evidence needed**:\n- MLP vs linear probe comparison on ≥2 models ✅ (both show EN→ZH direction gains)\n- MLP 不使用 test set 做 early stopping ✅ (已修复)\n- 控制实验排除 MLP 过拟合 ❌ (需 train/test accuracy gap 分析)\n- 解释跨架构幅度差异 (Llama 4x > Qwen) ❌ (可能与 Qwen 更强的跨语言对齐有关——ZH 训练数据占比更高)\n**Status**: 初步验证 ⚠️ (方向一致但幅度差异需解释)\n\n### Claim 4: Layer-wise conflict signal structure\n**Statement**: 冲突信号在 mid-to-upper layers 集中，峰值层在不同模型架构中占比一致（Llama ~88% depth, Qwen ~67% depth 有差异——需更多模型确认 pattern）。\n**Evidence needed**:\n- Layer-wise probe accuracy curves for ≥3 models ❌\n- Layer-wise CKA/SVCCA 量化 EN vs ZH 表征相似度 ❌\n- 与 \"Lost in Multilinguality\" 的 language transition 层对比 ❌\n**Status**: 未验证 ❌\n\n### Claim 5: Cross-lingual SAE conflict features (Track 2)\n**Statement**: SAE 特征空间中存在跨语言共享的冲突编码特征，可与 language-identity 特征解耦。\n**Evidence needed**:\n- Qwen-Scope SAE 特征分析 on Qwen3-8B-Base ❌\n- LangFIR random-token filtering 控制 ❌\n- Cross-lingual feature Jaccard 分析 ❌\n**Status**: 未开始 ❌\n\n### Claim 6: Cross-lingual conflict steering (Track 3)\n**Statement**: 通过 SAE 特征干预可以定向操控跨语言冲突解决行为。\n**Evidence needed**:\n- SpARE 框架跨语言扩展 ❌\n- Monolingual → cross-lingual steering transfer ❌\n- Steering effectiveness vs linguistic distance correlation ❌\n**Status**: 未开始 ❌ (依赖 Track 2)\n\n## Anticipated Reviewer Concerns\n\n### RC1: Translation quality confound [RESOLVED ✅]\n**Concern**: 中文翻译质量差可能导致虚假的冲突信号或迁移失败\n**Result**: Plan_105 COMET tercile ablation 证明翻译质量非 confounder。Qwen test: Low COMET (mean 0.585) → 66.35% acc, High COMET (mean 0.816) → 60.71% acc, delta=-5.64pp (反向), Fisher p=0.695。冲突信号检测不依赖翻译质量。Back-translation COMET ≥0.80 阈值过严（两步翻译天然拉低），但 ablation 实证排除了翻译质量 confound。\n**Remaining**: Llama test COMET 完成后重复此分析确认一致性。\n\n### RC2: Token overlap confound [RESOLVED ✅]\n**Concern**: 跨语言迁移可能由 EN-ZH 共享 token（数字、专有名词、标点）驱动\n**Result**: Per-sample Jaccard 仅 3-4%（type-level 10-15% 被膨胀）。Qwen 无相关 (p>0.4)，Llama 显著负相关 (r=-0.15, p=0.012, tercile Δ=-23.9pp)。高 overlap 反而降低准确率，方向与 RC2 相反。**共享 token 不驱动跨语言迁移，迁移发生在语义表示层。**\n\n### RC3: Model coverage insufficient [HIGH]\n**Concern**: 只有 2 个模型，无法声称 \"架构无关\"\n**Mitigation**: 加 ≥1 不同架构（Mistral/Gemma），验证 ~7.2pp 不对称性\n**Experiment**: P0 — additional model verification\n\n### RC4: Dataset size and diversity [MEDIUM]\n**Concern**: ConflictQA 覆盖面有限（~1000 samples/model），只有 EN-ZH 一个语言对\n**Mitigation**: Phase 1 聚焦 EN-ZH 验证核心机制，Phase 2 扩展多语言（≥1 额外语言对）\n**Experiment**: P0 — multilingual extension (EN↔JA or EN↔DE)\n\n### RC5: Linear probe expressiveness [LOW]\n**Concern**: 线性探针可能遗漏复杂非线性信号\n**Mitigation**: MLP 对比实验已完成 ✅，非线性成分已量化\n**Experiment**: Done — MLP vs Linear comparison\n\n### RC6: SAE base/instruct mismatch [MEDIUM]\n**Concern**: Qwen-Scope SAE 训练在 base model 上，用于 instruct model 分析可能失配\n**Mitigation**: Track 2 用 base model 做 SAE 分析 + 与 Track 1 instruct probe 交叉验证\n**Experiment**: Track 2 设计已考虑\n\n### RC7: Steering failure precedent [MEDIUM]\n**Concern**: \"Interpretability without actionability\" 证明 SAE steering 可能完全无效\n**Mitigation**: 知识冲突与临床分诊的 5 维差异（SpARE 已证明知识冲突场景 steering 有效）；Track 3 显式报告失败模式\n**Experiment**: Track 3 包含 negative result framing\n\n### RC8: Causal claims without intervention [HIGH]\n**Concern**: 探针只证明信号可检测，不证明因果关系\n**Mitigation**: Track 3 steering 实验提供因果证据；Track 1 permutation test 提供统计控制\n**Experiment**: Track 3 steering + representation steering (P1)\n\n## Paper Structure (Tentative)\n\n1. **Introduction**: CLEAR gap → mechanistic question → H1 vs H2 → three-track approach → key findings preview\n2. **Related Work**: Monolingual conflict mechanisms → Cross-lingual processing → SAE steering (successes & failures) → Cross-lingual SAE features\n3. **Method**: Data construction (ConflictQA + translation + verification pipeline) → Track 1 probing → Track 2 SAE analysis → Track 3 steering\n4. **Experiments & Results**:\n   - 4.1 Cross-lingual conflict detectability (C1)\n   - 4.2 Asymmetric transfer analysis (C2) + token overlap controls\n   - 4.3 Non-linear components (C3) + layer-wise structure (C4)\n   - 4.4 SAE feature analysis (C5) [if Track 2 ready]\n   - 4.5 Steering experiments (C6) [if Track 3 ready]\n5. **Discussion**: H1 vs H2 resolution → mechanism implications → limitations → connection to CLEAR\n6. **Conclusion**\n\n## Scope Control\n\n**投稿最低要求 (must-have for submission)**:\n- Claims 1-3 fully supported (cross-lingual detectability + asymmetry + non-linearity)\n- Claim 4 partially supported (layer-wise analysis on ≥2 models)\n- ≥3 model architectures\n- ≥2 language pairs (EN-ZH + one more)\n- Token overlap control\n- COMET translation quality validation\n\n**理想状态 (nice-to-have)**:\n- Track 2 SAE analysis (Claim 5)\n- Track 3 steering (Claim 6)\n- 5+ language pairs covering multiple typological families\n- Full CKA/SVCCA layer analysis\n\n**不做 (out of scope)**:\n- 10-language full CLEAR replication\n- Custom SAE training\n- MoE model analysis\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_probe_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bootstrap_asymmetry_diff_corrected: 0.0718\n    bootstrap_asymmetry_ci_corrected: '[-0.0119, 0.1341]'\n    bootstrap_asymmetry_significant_corrected: false\n    bootstrap_asymmetry_method: per_iteration_paired_diff_from_training_bootstrap_n100\n    bootstrap_asymmetry_diff_old: 0.0595\n    bootstrap_asymmetry_ci_old: '[-0.0367, 0.1481]'\n    comet_tertile_ablation:\n      conclusion: not_confounder\n      delta_high_low_pp: -5.64\n      fisher_p: 0.695\n      high_bal_acc: 0.6071\n      med_bal_acc: 0.6769\n      low_bal_acc: 0.6635\n      best_layer: 22\n      detail: Reversed direction (High COMET → lower probe acc). COMET gate can be\n        relaxed.\n- exp_id: mvp_probe_llama_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bootstrap_asymmetry_diff_corrected: 0.0722\n    bootstrap_asymmetry_ci_corrected: '[0.0110, 0.1361]'\n    bootstrap_asymmetry_significant_corrected: true\n    bootstrap_asymmetry_method: per_iteration_paired_diff_from_training_bootstrap_n100\n    bootstrap_asymmetry_diff_old: 0.1176\n    bootstrap_asymmetry_ci_old: '[0.0429, 0.1957]'\n- exp_id: llama31_en_activations\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen3_translate_zh\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: collect_en_activations_qwen3_8b\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: collect_en_activations_llama_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: translate_zh_llama_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: translate_zh_qwen\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: collect_en_act_llama_v3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: collect_en_act_qwen_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: verify_qwen3_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen_en_act_v3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: llama_zh_act\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen_zh_act\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: translate_zh_qwen_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: probe_qwen_full\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: comet_qwen\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_llama\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_qwen_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_llama_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_qwen_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_llama_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_qwen_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_llama_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_qwen_v5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    death_cause: EXIT_CODE=124 timeout kill by submit_training_job (REGISTRY ONLY\n      - actual nohup processes alive)\n    restart_pid: 59412\n    restart_gpu: cuda:0\n    restart_method: nohup + TRANSFORMERS_OFFLINE=1\n    restart_time: '2026-05-21T23:15:00Z'\n    no_resume: true\n    acceleration: cuda:1 并行处理 test set (168条) - COMPLETED\n    qwen_test_completed: true\n    qwen_test_total: 168\n    qwen_test_passed: 31\n    qwen_test_pass_rate: 0.185\n    qwen_test_mean_comet: 0.7016\n    qwen_test_passed_mean_comet: 0.8503\n    qwen_train_progress: 320/798 (~40%)\n    actual_status: train still running on cuda:0 (PID 59412)\n    registry_failed_is_false_alarm: true\n- exp_id: comet_llama_v5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    death_cause: EXIT_CODE=124 timeout kill by submit_training_job (REGISTRY ONLY\n      - actual nohup processes alive)\n    restart_pid: 59571\n    restart_gpu: cuda:2\n    restart_method: nohup + TRANSFORMERS_OFFLINE=1\n    restart_time: '2026-05-21T23:15:00Z'\n    no_resume: true\n    acceleration: cuda:3 并行处理 test set (272条) - IN PROGRESS 66%\n    llama_train_progress: 300/1096 (~27%)\n    llama_test_progress: 180/272 (~66%)\n    actual_status: train on cuda:2 (PID 59571), test on cuda:3 (PID 64179)\n    registry_failed_is_false_alarm: true\n- exp_id: qwen_zh_act_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: comet_qwen_v6\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: comet_llama_v6\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n\n重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: [\"Judge\", \"Biased?\"]`），否则 `?` `:` 等字符会导致解析失败。\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-22T02:51:50.999Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T02:51:50.999Z",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-22T02:51:51.032Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：第三模型不对称消失或反转，核心 C2 claim 崩塌，需重新定位论文 angle
核心假设：['第三模型不对称 <2pp 或方向反转（EN→ZH > ZH→EN）', '仅 Llama 显著，Qwen+第三模型均不显著，方向不全一致', '不对称性可能是 Llama 训练数据分布的 artifact 而非通用机制', 'Track 2/3 均无法在 DDL 前完成', 'COMET ablation 在 Llama 上出现与 Qwen 不一致的方向（质量确实影响 Llama）']
关键指标范围：{'third_model_asymmetry_gap_pp': [-3.0, 2.0], 'significant_asymmetry_models_of_3': [0, 1], 'consistent_direction_models_of_3': [1, 2], 'third_model_within_lang_acc': [0.65, 0.75], 'cross_lingual_transfer_acc_range': [0.58, 0.7], 'mlp_gain_weak_direction_pp_third_model': [-1.0, 3.0], 'sae_cross_lingual_jaccard_mid_layer': [0.0, 0.0], 'lang_pairs_validated': [1, 1], 'tracks_submission_ready': [1, 1]}
叙事方向：C2 不对称性降级为 observation，不再作为核心 claim。Reframe 路径（按优先级）：
Path A "Architecture-dependent cross-lingual conflict processing"—— 不对称性的存在与否本身取决于架构/训练数据，这是一个 finding 而非 failure。 主 claim 变为：冲突信号跨语言可检测（C1 robust），但迁移特性是架构依赖的， 揭示多语言 LLM 内部跨语言对齐程度的异质性。引用 Wendler et al. (2024)  "Llamas Know What GPTs Don't Show" 的跨架构差异发现，定位为该方向的机制扩展。
Path B "Cross-lingual probing methodology + negative result"—— 聚焦 confound exclusion pipeline（token overlap 分析 + COMET ablation）作为  方法论贡献，不对称性作为 "hypothesis tested and bounded" 的严格实验。 引用 Rogers et al. "negative results in NLP" 框架。
两条路径均保持 ICLR 目标：Path A 走 empirical analysis track， Path B 需要显著加厚实验密度（5+ 模型、3+ 语言对）补偿 claim 强度下降。 关键：worst 情况下 C1 仍然成立（within-lang acc 65-75%，均远超 chance）， 论文不会 "没东西可写"，只是叙事重心从 mechanism 转向 characterization。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: clkc_mech_interp
focus: 重点评估：1) C2 不对称性 claim 在 Llama borderline 显著 + Qwen 不显著的情况下能否撑住；2) 只有 Track 1 probing 无 Track 2/3 SAE+steering 时论文贡献强度是否足够 ICLR；3) back-translation COMET 低但 ablation 排除 confounder 的 framing 是否说服审稿人

## paper_framing.md

# Paper Framing — clkc_mech_interp

> 最后更新: 2026-05-22 | 目标: ICLR 2027 (DDL ~2026-09-24)

## Core Insight

多语言 LLM 中，跨语言知识冲突的检测信号可在残差流中被线性探针检测，且跨语言迁移呈现**方向性不对称**（ZH→EN >> EN→ZH ~7.2pp），该不对称性跨架构高度一致（Llama-3.1-8B 与 Qwen3-8B）。这为 CLEAR (Zhao et al. 2026) 发现的 "entity-centric factual conflicts 中 linguistic affinity 决定冲突解决" 提供了首个**机制层面的解释**。

**注意**: CLEAR 的发现是 task-dependent 的——entity-centric factual conflicts 由 linguistic affinity 主导，reasoning-intensive tasks 由 resource abundance 主导。我们使用 ConflictQA（entity-centric），引用 CLEAR 时必须限定为 entity-centric 场景。

## Narrative Structure

**现象驱动的机制解释**（非 "applying X to Y"）：

1. **Phenomenon**: CLEAR 发现在 entity-centric factual conflicts 中，linguistic affinity（而非 resource abundance）决定跨语言冲突解决，但未提供机制解释
2. **Mechanistic question**: 冲突信号在模型内部如何编码？是 language-universal 还是 language-specific？为什么 similarity 起决定作用？
3. **Our answer**: 通过残差流探针、SAE 特征分析、激活干预三条互补分析轨道，揭示冲突检测信号的跨语言结构——是否共享、在哪些层出现、能否用于干预

**Secondary framing**: SAE-based mechanistic interpretability 工具在跨语言条件下的 stress test——probing / SAE / steering 三种工具的跨语言适用性边界

## Competing Hypotheses (pre-registered)

**H1 — English-anchored universal detection**:
冲突检测信号本身是 language-independent 的（"是否存在冲突" 是语言无关判断），编码在 mid-layer 共享表征空间中。final-layer language transition 引入 similarity-dependent 干扰，影响 resolution 但不影响 detection。
- 预测: mid-layer conflict feature 跨语言 Jaccard >> late-layer Jaccard (paired permutation test p < 0.05)
- 预测: 英语探针跨语言迁移更强（英语作为训练数据主导语言，表征空间以英语为锚点）

**H2 — Language-pair-specific encoding**:
冲突特征从 mid-layer 起即为 language-pair-specific 的，linguistic distance 直接编码在冲突表征中。
- 预测: mid-layer 和 late-layer Jaccard 无显著差异，或 mid < late
- 预测: 探针迁移准确率与语言对 typological distance 强相关

**MVP 证据倾向**:
当前双模型结果倾向 **H1 的变体**——ZH→EN 迁移（71-72%）显著强于 EN→ZH（64-65%），暗示冲突信号以英语表征空间为锚点编码。非线性成分（MLP EN→ZH +9.2pp vs linear）提示 EN→ZH 方向的跨语言映射更复杂。

## Core Claims

### Claim 1: Cross-lingual conflict detectability
**Statement**: 跨语言知识冲突信号可在残差流中被线性探针检测，准确率显著高于随机基线。
**Evidence needed**:
- ≥2 model architectures 的 within-language probe acc > 70% (balanced) ✅ (Llama 77.1%, Qwen 75.3%)
- Permutation test p < 0.001 ✅ (all directions)
- Cross-lingual transfer acc > chance (50%) with statistical significance ✅ (all directions 64-72%)
**Status**: MVP 已验证 ✅

### Claim 2: Asymmetric cross-lingual transfer
**Statement**: 跨语言探针迁移呈方向一致的不对称：ZH→EN 迁移强于 EN→ZH（~7.2pp），效果量跨架构高度一致（Llama 显著，Qwen 方向一致但未达显著）。
**Evidence needed**:
- Bootstrap CI for asymmetry gap (corrected, plan_099 ✅):
  - Llama: +7.22pp, CI [1.1%, 13.6%] — 排除零但 borderline ✅
  - Qwen: +7.18pp, CI [-1.2%, 13.4%] — 含零，方向一致 ⚠️
- ≥2 models show consistent effect size ✅ (7.22pp vs 7.18pp)
- Token overlap analysis 排除词汇重叠驱动的虚假迁移 ✅ (plan_101 完成: per-sample Jaccard 3-4%, Qwen 无相关 p>0.4, Llama 显著负相关 r=-0.15 p=0.012 — RC2 排除)
- ≥1 additional model architecture 验证跨架构一致性 ❌ (planned P0)
**Status**: 初步验证 ⚠️ (需补 token overlap + 第三模型)

### Claim 3: Direction-dependent non-linear components
**Statement**: 跨语言冲突信号的弱迁移方向（EN→ZH）包含方向依赖的非线性成分，MLP 探针在该方向提升最大。跨架构一致方向但幅度不同（Llama +9.2pp single-seed / ~+4.7pp bootstrap-corrected, Qwen +2.3pp），暗示非线性成分与模型的跨语言对齐程度相关。
**Evidence needed**:
- MLP vs linear probe comparison on ≥2 models ✅ (both show EN→ZH direction gains)
- MLP 不使用 test set 做 early stopping ✅ (已修复)
- 控制实验排除 MLP 过拟合 ❌ (需 train/test accuracy gap 分析)
- 解释跨架构幅度差异 (Llama 4x > Qwen) ❌ (可能与 Qwen 更强的跨语言对齐有关——ZH 训练数据占比更高)
**Status**: 初步验证 ⚠️ (方向一致但幅度差异需解释)

### Claim 4: Layer-wise conflict signal structure
**Statement**: 冲突信号在 mid-to-upper layers 集中，峰值层在不同模型架构中占比一致（Llama ~88% depth, Qwen ~67% depth 有差异——需更多模型确认 pattern）。
**Evidence needed**:
- Layer-wise probe accuracy curves for ≥3 models ❌
- Layer-wise CKA/SVCCA 量化 EN vs ZH 表征相似度 ❌
- 与 "Lost in Multilinguality" 的 language transition 层对比 ❌
**Status**: 未验证 ❌

### Claim 5: Cross-lingual SAE conflict features (Track 2)
**Statement**: SAE 特征空间中存在跨语言共享的冲突编码特征，可与 language-identity 特征解耦。
**Evidence needed**:
- Qwen-Scope SAE 特征分析 on Qwen3-8B-Base ❌
- LangFIR random-token filtering 控制 ❌
- Cross-lingual feature Jaccard 分析 ❌
**Status**: 未开始 ❌

### Claim 6: Cross-lingual conflict steering (Track 3)
**Statement**: 通过 SAE 特征干预可以定向操控跨语言冲突解决行为。
**Evidence needed**:
- SpARE 框架跨语言扩展 ❌
- Monolingual → cross-lingual steering transfer ❌
- Steering effectiveness vs linguistic distance correlation ❌
**Status**: 未开始 ❌ (依赖 Track 2)

## Anticipated Reviewer Concerns

### RC1: Translation quality confound [RESOLVED ✅]
**Concern**: 中文翻译质量差可能导致虚假的冲突信号或迁移失败
**Result**: Plan_105 COMET tercile ablation 证明翻译质量非 confounder。Qwen test: Low COMET (mean 0.585) → 66.35% acc, High COMET (mean 0.816) → 60.71% acc, delta=-5.64pp (反向), Fisher p=0.695。冲突信号检测不依赖翻译质量。Back-translation COMET ≥0.80 阈值过严（两步翻译天然拉低），但 ablation 实证排除了翻译质量 confound。
**Remaining**: Llama test COMET 完成后重复此分析确认一致性。

### RC2: Token overlap confound [RESOLVED ✅]
**Concern**: 跨语言迁移可能由 EN-ZH 共享 token（数字、专有名词、标点）驱动
**Result**: Per-sample Jaccard 仅 3-4%（type-level 10-15% 被膨胀）。Qwen 无相关 (p>0.4)，Llama 显著负相关 (r=-0.15, p=0.012, tercile Δ=-23.9pp)。高 overlap 反而降低准确率，方向与 RC2 相反。**共享 token 不驱动跨语言迁移，迁移发生在语义表示层。**

### RC3: Model coverage insufficient [HIGH]
**Concern**: 只有 2 个模型，无法声称 "架构无关"
**Mitigation**: 加 ≥1 不同架构（Mistral/Gemma），验证 ~7.2pp 不对称性
**Experiment**: P0 — additional model verification

### RC4: Dataset size and diversity [MEDIUM]
**Concern**: ConflictQA 覆盖面有限（~1000 samples/model），只有 EN-ZH 一个语言对
**Mitigation**: Phase 1 聚焦 EN-ZH 验证核心机制，Phase 2 扩展多语言（≥1 额外语言对）
**Experiment**: P0 — multilingual extension (EN↔JA or EN↔DE)

### RC5: Linear probe expressiveness [LOW]
**Concern**: 线性探针可能遗漏复杂非线性信号
**Mitigation**: MLP 对比实验已完成 ✅，非线性成分已量化
**Experiment**: Done — MLP vs Linear comparison

### RC6: SAE base/instruct mismatch [MEDIUM]
**Concern**: Qwen-Scope SAE 训练在 base model 上，用于 instruct model 分析可能失配
**Mitigation**: Track 2 用 base model 做 SAE 分析 + 与 Track 1 instruct probe 交叉验证
**Experiment**: Track 2 设计已考虑

### RC7: Steering failure precedent [MEDIUM]
**Concern**: "Interpretability without actionability" 证明 SAE steering 可能完全无效
**Mitigation**: 知识冲突与临床分诊的 5 维差异（SpARE 已证明知识冲突场景 steering 有效）；Track 3 显式报告失败模式
**Experiment**: Track 3 包含 negative result framing

### RC8: Causal claims without intervention [HIGH]
**Concern**: 探针只证明信号可检测，不证明因果关系
**Mitigation**: Track 3 steering 实验提供因果证据；Track 1 permutation test 提供统计控制
**Experiment**: Track 3 steering + representation steering (P1)

## Paper Structure (Tentative)

1. **Introduction**: CLEAR gap → mechanistic question → H1 vs H2 → three-track approach → key findings preview
2. **Related Work**: Monolingual conflict mechanisms → Cross-lingual processing → SAE steering (successes & failures) → Cross-lingual SAE features
3. **Method**: Data construction (ConflictQA + translation + verification pipeline) → Track 1 probing → Track 2 SAE analysis → Track 3 steering
4. **Experiments & Results**:
   - 4.1 Cross-lingual conflict detectability (C1)
   - 4.2 Asymmetric transfer analysis (C2) + token overlap controls
   - 4.3 Non-linear components (C3) + layer-wise structure (C4)
   - 4.4 SAE feature analysis (C5) [if Track 2 ready]
   - 4.5 Steering experiments (C6) [if Track 3 ready]
5. **Discussion**: H1 vs H2 resolution → mechanism implications → limitations → connection to CLEAR
6. **Conclusion**

## Scope Control

**投稿最低要求 (must-have for submission)**:
- Claims 1-3 fully supported (cross-lingual detectability + asymmetry + non-linearity)
- Claim 4 partially supported (layer-wise analysis on ≥2 models)
- ≥3 model architectures
- ≥2 language pairs (EN-ZH + one more)
- Token overlap control
- COMET translation quality validation

**理想状态 (nice-to-have)**:
- Track 2 SAE analysis (Claim 5)
- Track 3 steering (Claim 6)
- 5+ language pairs covering multiple typological families
- Full CKA/SVCCA layer analysis

**不做 (out of scope)**:
- 10-language full CLEAR replication
- Custom SAE training
- MoE model analysis


## registry (completed experiments)

- exp_id: mvp_probe_v1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    bootstrap_asymmetry_diff_corrected: 0.0718
    bootstrap_asymmetry_ci_corrected: '[-0.0119, 0.1341]'
    bootstrap_asymmetry_significant_corrected: false
    bootstrap_asymmetry_method: per_iteration_paired_diff_from_training_bootstrap_n100
    bootstrap_asymmetry_diff_old: 0.0595
    bootstrap_asymmetry_ci_old: '[-0.0367, 0.1481]'
    comet_tertile_ablation:
      conclusion: not_confounder
      delta_high_low_pp: -5.64
      fisher_p: 0.695
      high_bal_acc: 0.6071
      med_bal_acc: 0.6769
      low_bal_acc: 0.6635
      best_layer: 22
      detail: Reversed direction (High COMET → lower probe acc). COMET gate can be
        relaxed.
- exp_id: mvp_probe_llama_v1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    bootstrap_asymmetry_diff_corrected: 0.0722
    bootstrap_asymmetry_ci_corrected: '[0.0110, 0.1361]'
    bootstrap_asymmetry_significant_corrected: true
    bootstrap_asymmetry_method: per_iteration_paired_diff_from_training_bootstrap_n100
    bootstrap_asymmetry_diff_old: 0.1176
    bootstrap_asymmetry_ci_old: '[0.0429, 0.1957]'
- exp_id: llama31_en_activations
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: qwen3_translate_zh
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: collect_en_activations_qwen3_8b
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: collect_en_activations_llama_v2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: translate_zh_llama_v2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: translate_zh_qwen
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: collect_en_act_llama_v3
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: collect_en_act_qwen_v2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: verify_qwen3_v2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: qwen_en_act_v3
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: llama_zh_act
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: qwen_zh_act
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: translate_zh_qwen_v2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: probe_qwen_full
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: comet_qwen
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: comet_llama
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: comet_qwen_v2
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: comet_llama_v2
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: comet_qwen_v3
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: comet_llama_v3
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: comet_qwen_v4
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: comet_llama_v4
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: comet_qwen_v5
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    death_cause: EXIT_CODE=124 timeout kill by submit_training_job (REGISTRY ONLY
      - actual nohup processes alive)
    restart_pid: 59412
    restart_gpu: cuda:0
    restart_method: nohup + TRANSFORMERS_OFFLINE=1
    restart_time: '2026-05-21T23:15:00Z'
    no_resume: true
    acceleration: cuda:1 并行处理 test set (168条) - COMPLETED
    qwen_test_completed: true
    qwen_test_total: 168
    qwen_test_passed: 31
    qwen_test_pass_rate: 0.185
    qwen_test_mean_comet: 0.7016
    qwen_test_passed_mean_comet: 0.8503
    qwen_train_progress: 320/798 (~40%)
    actual_status: train still running on cuda:0 (PID 59412)
    registry_failed_is_false_alarm: true
- exp_id: comet_llama_v5
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    death_cause: EXIT_CODE=124 timeout kill by submit_training_job (REGISTRY ONLY
      - actual nohup processes alive)
    restart_pid: 59571
    restart_gpu: cuda:2
    restart_method: nohup + TRANSFORMERS_OFFLINE=1
    restart_time: '2026-05-21T23:15:00Z'
    no_resume: true
    acceleration: cuda:3 并行处理 test set (272条) - IN PROGRESS 66%
    llama_train_progress: 300/1096 (~27%)
    llama_test_progress: 180/272 (~66%)
    actual_status: train on cuda:2 (PID 59571), test on cuda:3 (PID 64179)
    registry_failed_is_false_alarm: true
- exp_id: qwen_zh_act_v2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: comet_qwen_v6
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: comet_llama_v6
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

重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: ["Judge", "Biased?"]`），否则 `?` `:` 等字符会导致解析失败。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "0d379402-cd2e-4d79-ad0a-925a51076fe0",
  "type": "user",
  "uuid": "f2113daa-3c8d-498e-b142-d00d8622ec88",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T02:51:51.030Z_

```json
{
  "parentUuid": "f2113daa-3c8d-498e-b142-d00d8622ec88",
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
  "uuid": "d2fc4a68-08e6-4f26-9012-2baab99193de",
  "timestamp": "2026-05-22T02:51:51.030Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T02:51:51.031Z_

```json
{
  "parentUuid": "d2fc4a68-08e6-4f26-9012-2baab99193de",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "cb2e07c0-b4bd-4d56-b45f-5868bb9b342b",
  "timestamp": "2026-05-22T02:51:51.031Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：第三模型不对称消失或反转，核心 C2 claim 崩塌，需重新定位论文 angle 核心假设：['第三模型不对称 <2pp 或方向反转（EN→ZH > ZH→EN）', '仅 Llama 显著，Qwen+第三模型均不显著，方向不全一致', '不对称性可能是 Llama 训练数据分布的 artifact 而非…",
  "leafUuid": "cb2e07c0-b4bd-4d56-b45f-5868bb9b342b",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase 1 worst case scenario experiment planning",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b"
}
```

---

### Assistant

_source line 8 · 2026-05-22T02:51:53.441Z_

Let me first read the experiment plan to understand all planned experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb2e07c0-b4bd-4d56-b45f-5868bb9b342b",
  "isSidechain": false,
  "requestId": "req_011CbGrDLfmm669GhXwsM5SF",
  "type": "assistant",
  "uuid": "98ac8411-54fd-4fcd-bdd7-268b0c9aad1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcZ9YcrwcX6xJQ2X53v2Qx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12329,
      "cache_read_input_tokens": 11841,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12329,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 196,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12329,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12329
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

_source line 9 · 2026-05-22T02:51:57.412Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SWtVzQo4pPvm9X6PVKJgyU`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan files",
  "prompt": "Search for the experiment plan file in /home/ubuntu/.agent-ml-research-prod42. Look for files named experiment_plan*, plan*, or any YAML/MD files that contain planned experiments. Also check for files in subdirectories like docs/, plans/, experiments/ etc. Search broadly - try patterns like **/*plan*, **/*experiment*, and also look at the top-level directory structure to understand the project layout."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98ac8411-54fd-4fcd-bdd7-268b0c9aad1d",
  "isSidechain": false,
  "requestId": "req_011CbGrDLfmm669GhXwsM5SF",
  "type": "assistant",
  "uuid": "2be25a48-d161-486a-9f51-3c51e4b69c75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcZ9YcrwcX6xJQ2X53v2Qx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12329,
      "cache_read_input_tokens": 11841,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12329,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 196,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12329,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12329
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

_source line 10 · 2026-05-22T02:52:16.175Z_

<details><summary>↩ Tool result · `toolu_01SWtVzQo4pPvm9X6PVKJgyU`</summary>

```text
Perfect! I have found and reviewed the complete experiment plan. Here is my comprehensive report:

## Summary

I successfully located the experiment plan file in the project directory structure.

**Primary File Found:**
- `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/experiment_plan.yaml`

**Related Planning Documents:**
- `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/ROADMAP.md` (project research dashboard)

## Experiment Plan Overview

The experiment plan is a comprehensive YAML file (256 lines) organized around a multi-language LLM research project titled **"clkc_mech_interp — Cross-Lingual Knowledge Conflict Mechanistic Interpretability"**

**Project Goal:** ICLR 2027 submission (deadline ~2026-09-24)

### Key Structure

The plan contains 25+ experiments organized into **3 main tracks**:

1. **MVP Experiments (Completed/In Progress)** — 3 experiments, P0 priority
   - `mvp_001`: Dual-model residual flow probe (Llama-3.1-8B + Qwen3-8B) — DONE
   - `mvp_002`: MLP vs Linear probe comparison — DONE
   - `mvp_003`: COMET translation quality validation — RUNNING

2. **Statistical Corrections (P0)** — 1 experiment
   - `plan_099`: Training set bootstrap asymmetry CI — DONE

3. **Track 1: Cross-Lingual Probing (P0)** — 9 experiments
   - Token overlap analysis (plan_101) — DONE
   - Third-model architecture verification (plan_102) — PLANNED
   - Multi-language expansion EN↔JA (plan_103) — PLANNED
   - Layer-wise CKA/SVCCA (plan_104) — PLANNED
   - COMET segmented ablation (plan_105) — DONE
   - Label noise ablation (plan_106) — PLANNED
   - Representation steering experiments (plan_107) — PLANNED
   - Larger dataset validation (plan_108) — PLANNED
   - Probe weight visualization (plan_109) — PLANNED

4. **Track 2: SAE Feature Analysis (P1-P2)** — 3 experiments
   - Qwen-Scope SAE conflict feature identification (plan_201) — PLANNED
   - LangFIR language feature disentanglement (plan_202) — PLANNED
   - Cross-lingual feature Jaccard analysis (plan_203) — PLANNED

5. **Track 3: Steering (P2)** — 3 experiments
   - Monolingual→cross-lingual steering transfer (plan_301) — PLANNED
   - Cross-lingual-specific steering (plan_302) — PLANNED
   - Typological steering correlation (plan_303) — PLANNED

### Key Metrics & Results

MVP experiments show:
- **Detection accuracy**: EN→EN 75-77%, ZH→ZH 71-72%, EN→ZH 64-65%, ZH→EN 71-72% across both models
- **Asymmetry finding**: ~7.2pp directional difference (Llama +7.22pp, Qwen +7.18pp)
- **Bootstrap CI**: Llama significant [1.1%, 13.6%], Qwen trending [-1.2%, 13.4%]
- **Confounders excluded**: Token overlap (r=-0.15, non-significant) and translation quality (p=0.695)

### GPU Budget
- 4× RTX PRO 6000 Blackwell 96GB GPUs (cuda:0-3) on westd-41302
- Current allocation: cuda:0,2 for COMET training, cuda:3 for Llama testing, cuda:1 idle
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2be25a48-d161-486a-9f51-3c51e4b69c75",
  "isSidechain": false,
  "promptId": "0d379402-cd2e-4d79-ad0a-925a51076fe0",
  "type": "user",
  "uuid": "3a6a2e93-3774-4d51-b649-49fe1130e049",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for the experiment plan file in /home/ubuntu/.agent-ml-research-prod42. Look for files named experiment_plan*, plan*, or any YAML/MD files that contain planned experiments. Also check for files in subdirectories like docs/, plans/, experiments/ etc. Search broadly - try patterns like **/*plan*, **/*experiment*, and also look at the top-level directory structure to understand the project layout.",
    "agentId": "aa860b9f2819e1b90",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I have found and reviewed the complete experiment plan. Here is my comprehensive report:\n\n## Summary\n\nI successfully located the experiment plan file in the project directory structure.\n\n**Primary File Found:**\n- `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/experiment_plan.yaml`\n\n**Related Planning Documents:**\n- `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/ROADMAP.md` (project research dashboard)\n\n## Experiment Plan Overview\n\nThe experiment plan is a comprehensive YAML file (256 lines) organized around a multi-language LLM research project titled **\"clkc_mech_interp — Cross-Lingual Knowledge Conflict Mechanistic Interpretability\"**\n\n**Project Goal:** ICLR 2027 submission (deadline ~2026-09-24)\n\n### Key Structure\n\nThe plan contains 25+ experiments organized into **3 main tracks**:\n\n1. **MVP Experiments (Completed/In Progress)** — 3 experiments, P0 priority\n   - `mvp_001`: Dual-model residual flow probe (Llama-3.1-8B + Qwen3-8B) — DONE\n   - `mvp_002`: MLP vs Linear probe comparison — DONE\n   - `mvp_003`: COMET translation quality validation — RUNNING\n\n2. **Statistical Corrections (P0)** — 1 experiment\n   - `plan_099`: Training set bootstrap asymmetry CI — DONE\n\n3. **Track 1: Cross-Lingual Probing (P0)** — 9 experiments\n   - Token overlap analysis (plan_101) — DONE\n   - Third-model architecture verification (plan_102) — PLANNED\n   - Multi-language expansion EN↔JA (plan_103) — PLANNED\n   - Layer-wise CKA/SVCCA (plan_104) — PLANNED\n   - COMET segmented ablation (plan_105) — DONE\n   - Label noise ablation (plan_106) — PLANNED\n   - Representation steering experiments (plan_107) — PLANNED\n   - Larger dataset validation (plan_108) — PLANNED\n   - Probe weight visualization (plan_109) — PLANNED\n\n4. **Track 2: SAE Feature Analysis (P1-P2)** — 3 experiments\n   - Qwen-Scope SAE conflict feature identification (plan_201) — PLANNED\n   - LangFIR language feature disentanglement (plan_202) — PLANNED\n   - Cross-lingual feature Jaccard analysis (plan_203) — PLANNED\n\n5. **Track 3: Steering (P2)** — 3 experiments\n   - Monolingual→cross-lingual steering transfer (plan_301) — PLANNED\n   - Cross-lingual-specific steering (plan_302) — PLANNED\n   - Typological steering correlation (plan_303) — PLANNED\n\n### Key Metrics & Results\n\nMVP experiments show:\n- **Detection accuracy**: EN→EN 75-77%, ZH→ZH 71-72%, EN→ZH 64-65%, ZH→EN 71-72% across both models\n- **Asymmetry finding**: ~7.2pp directional difference (Llama +7.22pp, Qwen +7.18pp)\n- **Bootstrap CI**: Llama significant [1.1%, 13.6%], Qwen trending [-1.2%, 13.4%]\n- **Confounders excluded**: Token overlap (r=-0.15, non-significant) and translation quality (p=0.695)\n\n### GPU Budget\n- 4× RTX PRO 6000 Blackwell 96GB GPUs (cuda:0-3) on westd-41302\n- Current allocation: cuda:0,2 for COMET training, cuda:3 for Llama testing, cuda:1 idle"
      }
    ],
    "totalDurationMs": 18750,
    "totalTokens": 33642,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 30787,
      "output_tokens": 937,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 937,
          "cache_read_input_tokens": 30787,
          "cache_creation_input_tokens": 1913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1913,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 5,
      "bashCount": 2,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "2be25a48-d161-486a-9f51-3c51e4b69c75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T02:52:25.890Z_

<details open><summary>🔧 Tool call — Read · `toolu_013oK64DqtDDA58TyEHsiSdV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a6a2e93-3774-4d51-b649-49fe1130e049",
  "isSidechain": false,
  "requestId": "req_011CbGrFBzBsHAtCioyJYMD7",
  "type": "assistant",
  "uuid": "2205eab6-f82a-4887-884e-060109509def",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALWpJZQdeDCvisjAu2ZTHs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 24170,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1142,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 24170,
          "cache_creation_input_tokens": 1142,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1142
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

_source line 12 · 2026-05-22T02:52:25.906Z_

<details><summary>↩ Tool result · `toolu_013oK64DqtDDA58TyEHsiSdV`</summary>

```text
1	# Experiment Plan — clkc_mech_interp
2	# 最后更新: 2026-05-22
3	# 目标: ICLR 2027 (DDL ~2026-09-24)
4	
5	# ── MVP 实验（已完成/进行中）──
6	
7	- plan_id: mvp_001
8	  name: "双模型残差流探针 MVP"
9	  claim: "C1 (detectability) + C2 (asymmetry)"
10	  description: "Llama-3.1-8B + Qwen3-8B 双模型 EN/ZH 4方向探针迁移实验"
11	  priority: P0
12	  status: done
13	  registry_id:
14	    - mvp_probe_llama_v1
15	    - mvp_probe_v1
16	  gpu_hours: 8
17	  results_summary: |
18	    Llama EN→EN 77.1±1.2%, ZH→ZH 71.2±1.3%, EN→ZH 64.1±2.5%, ZH→EN 71.3±2.7%
19	    Qwen EN→EN 75.3±1.7%, ZH→ZH 71.6±1.8%, EN→ZH 65.0±2.7%, ZH→EN 72.2±2.6%
20	    不对称性: Llama +7.22pp, Qwen +7.19pp
21	
22	- plan_id: mvp_002
23	  name: "MLP vs Linear 探针对比"
24	  claim: "C3 (non-linearity)"
25	  description: "1-hidden-layer MLP 探针与线性探针对比，量化非线性成分"
26	  priority: P0
27	  status: done
28	  registry_id:
29	    - mlp_probe_llama
30	    - mlp_probe_qwen
31	  gpu_hours: 4
32	  results_summary: |
33	    Llama EN→ZH: Linear 59.6% → MLP 68.8% (+9.2pp) [single-seed 基线]
34	    Qwen EN→ZH: Linear 67.3% → MLP 69.6% (+2.3pp) [single-seed 基线]
35	    注意: bootstrap mean 线性基线更高 (Llama 64.1%), MLP 优势在 bootstrap 下约 +4.7pp
36	
37	- plan_id: mvp_003
38	  name: "COMET 翻译质量验证"
39	  claim: "RC1 (translation confound)"
40	  description: "wmt22-comet-da back-translation 验证 ZH 翻译质量，threshold ≥ 0.80"
41	  priority: P0
42	  status: running
43	  gpu_hours: 6
44	  depends_on: []
45	
46	# ── 统计修正（P0，Reviewer 发现的 CI 混用问题）──
47	
48	- plan_id: plan_099
49	  name: "训练集 bootstrap 不对称性 CI"
50	  claim: "C2 (asymmetry) — 统计修正"
51	  description: |
52	    用 n=100 训练集 bootstrap 逐迭代计算不对称性，提取 paired CI。
53	    Llama: +7.22pp CI [1.1%, 13.6%] 排除零(borderline); Qwen: +7.18pp CI [-1.2%, 13.4%] 含零。
54	  priority: P0
55	  status: done
56	  gpu_hours: 0
57	  depends_on: [mvp_001]
58	  results_summary: |
59	    Llama: +7.22pp, 95% CI [1.1%, 13.6%], 98/100 iterations positive — significant
60	    Qwen: +7.18pp, 95% CI [-1.2%, 13.4%], 96/100 iterations positive — trending
61	    效果量跨架构高度一致 (7.22 vs 7.18), 第三模型(Gemma)将决定C2强度
62	
63	# ── Track 1: Cross-Lingual Probing (P0) ──
64	
65	- plan_id: plan_101
66	  name: "Token overlap 分析"
67	  claim: "C2 (asymmetry) — RC2 排除"
68	  description: |
69	    计算 EN-ZH 输入的 token overlap ratio，分析共享 token 对探针迁移的贡献。
70	    Per-sample Jaccard + correlation with probe correctness + tercile 分析。
71	  priority: P0
72	  status: done
73	  gpu_hours: 0
74	  depends_on: [mvp_001]
75	  results_summary: |
76	    RC2 排除。Per-sample Jaccard 3-4%, Qwen 无相关 (p>0.4),
77	    Llama 负相关 (r=-0.15, p=0.012, tercile Δ=-23.9pp)。
78	    共享 token 不驱动迁移，迁移发生在语义表示层。
79	
80	- plan_id: plan_102
81	  name: "第三模型架构验证"
82	  claim: "C2 (asymmetry) — RC3 排除"
83	  description: |
84	    在第三个模型架构（Mistral-7B-Instruct-v0.3 或 Gemma-2-9B-IT）上重复完整探针实验。
85	    验证 ~7.2pp 不对称性是否跨架构一致。
86	    包含: verify → translate → collect activations → train probe → bootstrap n=100。
87	  priority: P0
88	  status: planned
89	  gpu_hours: 20
90	  depends_on: []
91	
92	- plan_id: plan_103
93	  name: "多语言扩展 (EN↔JA)"
94	  claim: "C2 (asymmetry) — RC4 + H1/H2 检验"
95	  description: |
96	    扩展到 EN↔JA 语言对，测试不对称性是否与 typological distance 相关。
97	    JA 作为 CJK 系但与 ZH typologically 不同的语言，可检验 H2 的语言距离编码假设。
98	    如果 EN↔JA 不对称性方向和幅度与 EN↔ZH 类似 → 支持 H1 (English-anchored)
99	    如果差异显著 → 支持 H2 (language-pair-specific)
100	  priority: P0
101	  status: planned
102	  gpu_hours: 20
103	  depends_on: []
104	
105	- plan_id: plan_104
106	  name: "Layer-wise CKA/SVCCA"
107	  claim: "C4 (layer structure)"
108	  description: |
109	    在每一层计算 EN vs ZH 激活的 CKA (Centered Kernel Alignment) 和 SVCCA，
110	    量化跨语言表征相似度随层变化的 pattern。
111	    验证 "Lost in Multilinguality" 的 language transition 是否影响冲突信号迁移。
112	  priority: P0
113	  status: planned
114	  gpu_hours: 4
115	  depends_on: [mvp_001]
116	
117	- plan_id: plan_105
118	  name: "COMET 分段 ablation"
119	  claim: "C1 (detectability) — RC1 深化 + COMET gate 判定"
120	  description: |
121	    按 COMET 分数将翻译分为 high/med/low 三档（tertile），用已有探针评估各档 balanced acc。
122	    判断标准: High vs Low tertile acc 差异 < 5pp 且 p > 0.05 → 翻译质量非 confounder → 放宽阈值。
123	    背景: Qwen test back-translation COMET mean=0.70, pass rate 18.45% at ≥0.80。
124	    Back-translation 两步翻译天然拉低 COMET，需 ablation 实证判断是否影响探针。
125	  priority: P0
126	  status: done
127	  gpu_hours: 0
128	  depends_on: [mvp_003]
129	  results_summary: |
130	    Qwen test (n=168): Low COMET 66.35%, Med 67.69%, High 60.71%
131	    Delta(High-Low)=-5.64pp (反向), Fisher p=0.695 → 翻译质量非 confounder
132	    Llama 待确认一致性
133	
134	# ── Track 1 扩展 (P1) ──
135	
136	- plan_id: plan_109
137	  name: "探针权重可视化 + PCA"
138	  claim: "C1 (detectability) + C4 (layer structure) — 定性证据"
139	  description: |
140	    对最优层的线性探针权重做 PCA / t-SNE 可视化，展示冲突 vs 非冲突样本的分布。
141	    跨语言对比：EN 和 ZH 的冲突表征在 PCA 空间中是否重叠？
142	    为 "mechanistic interpretability" claim 提供定性证据（不能只有准确率数字）。
143	  priority: P1
144	  status: planned
145	  gpu_hours: 0.5
146	  depends_on: [mvp_001]
147	
148	- plan_id: plan_106
149	  name: "Label noise ablation"
150	  claim: "C1 (detectability) — robustness"
151	  description: |
152	    系统性注入 5%/10%/15%/20% label noise，测量 probe accuracy 下降曲线。
153	    评估 verification pipeline 的 label error tolerance。
154	  priority: P1
155	  status: planned
156	  gpu_hours: 4
157	  depends_on: [mvp_001]
158	
159	- plan_id: plan_107
160	  name: "Representation steering (干预实验)"
161	  claim: "C2 (asymmetry) — RC8 因果证据"
162	  description: |
163	    用探针方向作为 steering vector，在残差流中干预冲突信号。
164	    测量干预后模型输出（parametric vs contextual answer）的变化。
165	    提供 C2 不对称性的因果证据（不仅是相关性）。
166	    如果 Track 3 SAE steering 无法完成，此实验是因果证据的唯一来源。
167	  priority: P0
168	  status: planned
169	  gpu_hours: 8
170	  depends_on: [mvp_001, plan_104]
171	
172	- plan_id: plan_108
173	  name: "更大数据集验证"
174	  claim: "C1 (detectability) — RC4 数据充分性"
175	  description: |
176	    扩大 ConflictQA 采样至 2000+ samples per model (当前 ~1000)。
177	    或引入其他知识冲突数据集（如 SQuAD-conflict, WebQuestions-conflict）。
178	  priority: P1
179	  status: planned
180	  gpu_hours: 12
181	  depends_on: []
182	
183	# ── Track 2: SAE Feature Analysis (P1-P2) ──
184	
185	- plan_id: plan_201
186	  name: "Qwen-Scope SAE 冲突特征识别"
187	  claim: "C5 (SAE features)"
188	  description: |
189	    用 Qwen-Scope 预训练 SAE (Qwen3-8B-Base) 分析冲突激活中的差异化特征。
190	    适配 cloze/completion 格式（base model 兼容）。
191	    SpARE mutual-information feature selection 方法。
192	  priority: P1
193	  status: planned
194	  gpu_hours: 16
195	  depends_on: [mvp_001]
196	
197	- plan_id: plan_202
198	  name: "LangFIR 语言特征解耦"
199	  claim: "C5 (SAE features) — 控制实验"
200	  description: |
201	    用 LangFIR random-token filtering 识别 language-identity 特征。
202	    从 SAE conflict features 中排除 language-identity 特征。
203	    验证 conflict features 和 language features 的层分布是否非重叠。
204	  priority: P1
205	  status: planned
206	  gpu_hours: 8
207	  depends_on: [plan_201]
208	
209	- plan_id: plan_203
210	  name: "Cross-lingual feature Jaccard 分析"
211	  claim: "C5 (SAE features) — H1 vs H2 检验"
212	  description: |
213	    计算 mid-layer vs late-layer conflict feature 的跨语言 Jaccard index。
214	    H1 预测: mid-layer Jaccard >> late-layer Jaccard
215	    H2 预测: 无显著差异或 mid < late
216	    Paired permutation test p < 0.05。
217	  priority: P1
218	  status: planned
219	  gpu_hours: 4
220	  depends_on: [plan_201, plan_202]
221	
222	# ── Track 3: Steering (P2) ──
223	
224	- plan_id: plan_301
225	  name: "Monolingual→cross-lingual steering transfer"
226	  claim: "C6 (steering)"
227	  description: |
228	    用 SpARE 的英语冲突特征做 cross-lingual steering。
229	    测量跨语言 steering 有效性 (EM_C, EM_M, flip rates)。
230	  priority: P2
231	  status: planned
232	  gpu_hours: 16
233	  depends_on: [plan_201, plan_203]
234	
235	- plan_id: plan_302
236	  name: "Cross-lingual-specific steering"
237	  claim: "C6 (steering)"
238	  description: |
239	    用 Track 2 发现的跨语言特有特征构建 steering vectors。
240	    对比与 monolingual features 的 steering 效果差异。
241	  priority: P2
242	  status: planned
243	  gpu_hours: 16
244	  depends_on: [plan_301]
245	
246	- plan_id: plan_303
247	  name: "Typological steering correlation"
248	  claim: "C6 (steering) — CLEAR 因果链接"
249	  description: |
250	    测试 steering 有效性是否与 CLEAR 的 linguistic similarity metric 相关。
251	    提供 linguistic similarity → conflict resolution 的因果（非仅相关）证据。
252	  priority: P2
253	  status: planned
254	  gpu_hours: 12
255	  depends_on: [plan_301, plan_103]
256	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2205eab6-f82a-4887-884e-060109509def",
  "isSidechain": false,
  "promptId": "0d379402-cd2e-4d79-ad0a-925a51076fe0",
  "type": "user",
  "uuid": "fce7b6f6-d876-4989-ac21-591f0ed03364",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/experiment_plan.yaml",
      "content": "# Experiment Plan — clkc_mech_interp\n# 最后更新: 2026-05-22\n# 目标: ICLR 2027 (DDL ~2026-09-24)\n\n# ── MVP 实验（已完成/进行中）──\n\n- plan_id: mvp_001\n  name: \"双模型残差流探针 MVP\"\n  claim: \"C1 (detectability) + C2 (asymmetry)\"\n  description: \"Llama-3.1-8B + Qwen3-8B 双模型 EN/ZH 4方向探针迁移实验\"\n  priority: P0\n  status: done\n  registry_id:\n    - mvp_probe_llama_v1\n    - mvp_probe_v1\n  gpu_hours: 8\n  results_summary: |\n    Llama EN→EN 77.1±1.2%, ZH→ZH 71.2±1.3%, EN→ZH 64.1±2.5%, ZH→EN 71.3±2.7%\n    Qwen EN→EN 75.3±1.7%, ZH→ZH 71.6±1.8%, EN→ZH 65.0±2.7%, ZH→EN 72.2±2.6%\n    不对称性: Llama +7.22pp, Qwen +7.19pp\n\n- plan_id: mvp_002\n  name: \"MLP vs Linear 探针对比\"\n  claim: \"C3 (non-linearity)\"\n  description: \"1-hidden-layer MLP 探针与线性探针对比，量化非线性成分\"\n  priority: P0\n  status: done\n  registry_id:\n    - mlp_probe_llama\n    - mlp_probe_qwen\n  gpu_hours: 4\n  results_summary: |\n    Llama EN→ZH: Linear 59.6% → MLP 68.8% (+9.2pp) [single-seed 基线]\n    Qwen EN→ZH: Linear 67.3% → MLP 69.6% (+2.3pp) [single-seed 基线]\n    注意: bootstrap mean 线性基线更高 (Llama 64.1%), MLP 优势在 bootstrap 下约 +4.7pp\n\n- plan_id: mvp_003\n  name: \"COMET 翻译质量验证\"\n  claim: \"RC1 (translation confound)\"\n  description: \"wmt22-comet-da back-translation 验证 ZH 翻译质量，threshold ≥ 0.80\"\n  priority: P0\n  status: running\n  gpu_hours: 6\n  depends_on: []\n\n# ── 统计修正（P0，Reviewer 发现的 CI 混用问题）──\n\n- plan_id: plan_099\n  name: \"训练集 bootstrap 不对称性 CI\"\n  claim: \"C2 (asymmetry) — 统计修正\"\n  description: |\n    用 n=100 训练集 bootstrap 逐迭代计算不对称性，提取 paired CI。\n    Llama: +7.22pp CI [1.1%, 13.6%] 排除零(borderline); Qwen: +7.18pp CI [-1.2%, 13.4%] 含零。\n  priority: P0\n  status: done\n  gpu_hours: 0\n  depends_on: [mvp_001]\n  results_summary: |\n    Llama: +7.22pp, 95% CI [1.1%, 13.6%], 98/100 iterations positive — significant\n    Qwen: +7.18pp, 95% CI [-1.2%, 13.4%], 96/100 iterations positive — trending\n    效果量跨架构高度一致 (7.22 vs 7.18), 第三模型(Gemma)将决定C2强度\n\n# ── Track 1: Cross-Lingual Probing (P0) ──\n\n- plan_id: plan_101\n  name: \"Token overlap 分析\"\n  claim: \"C2 (asymmetry) — RC2 排除\"\n  description: |\n    计算 EN-ZH 输入的 token overlap ratio，分析共享 token 对探针迁移的贡献。\n    Per-sample Jaccard + correlation with probe correctness + tercile 分析。\n  priority: P0\n  status: done\n  gpu_hours: 0\n  depends_on: [mvp_001]\n  results_summary: |\n    RC2 排除。Per-sample Jaccard 3-4%, Qwen 无相关 (p>0.4),\n    Llama 负相关 (r=-0.15, p=0.012, tercile Δ=-23.9pp)。\n    共享 token 不驱动迁移，迁移发生在语义表示层。\n\n- plan_id: plan_102\n  name: \"第三模型架构验证\"\n  claim: \"C2 (asymmetry) — RC3 排除\"\n  description: |\n    在第三个模型架构（Mistral-7B-Instruct-v0.3 或 Gemma-2-9B-IT）上重复完整探针实验。\n    验证 ~7.2pp 不对称性是否跨架构一致。\n    包含: verify → translate → collect activations → train probe → bootstrap n=100。\n  priority: P0\n  status: planned\n  gpu_hours: 20\n  depends_on: []\n\n- plan_id: plan_103\n  name: \"多语言扩展 (EN↔JA)\"\n  claim: \"C2 (asymmetry) — RC4 + H1/H2 检验\"\n  description: |\n    扩展到 EN↔JA 语言对，测试不对称性是否与 typological distance 相关。\n    JA 作为 CJK 系但与 ZH typologically 不同的语言，可检验 H2 的语言距离编码假设。\n    如果 EN↔JA 不对称性方向和幅度与 EN↔ZH 类似 → 支持 H1 (English-anchored)\n    如果差异显著 → 支持 H2 (language-pair-specific)\n  priority: P0\n  status: planned\n  gpu_hours: 20\n  depends_on: []\n\n- plan_id: plan_104\n  name: \"Layer-wise CKA/SVCCA\"\n  claim: \"C4 (layer structure)\"\n  description: |\n    在每一层计算 EN vs ZH 激活的 CKA (Centered Kernel Alignment) 和 SVCCA，\n    量化跨语言表征相似度随层变化的 pattern。\n    验证 \"Lost in Multilinguality\" 的 language transition 是否影响冲突信号迁移。\n  priority: P0\n  status: planned\n  gpu_hours: 4\n  depends_on: [mvp_001]\n\n- plan_id: plan_105\n  name: \"COMET 分段 ablation\"\n  claim: \"C1 (detectability) — RC1 深化 + COMET gate 判定\"\n  description: |\n    按 COMET 分数将翻译分为 high/med/low 三档（tertile），用已有探针评估各档 balanced acc。\n    判断标准: High vs Low tertile acc 差异 < 5pp 且 p > 0.05 → 翻译质量非 confounder → 放宽阈值。\n    背景: Qwen test back-translation COMET mean=0.70, pass rate 18.45% at ≥0.80。\n    Back-translation 两步翻译天然拉低 COMET，需 ablation 实证判断是否影响探针。\n  priority: P0\n  status: done\n  gpu_hours: 0\n  depends_on: [mvp_003]\n  results_summary: |\n    Qwen test (n=168): Low COMET 66.35%, Med 67.69%, High 60.71%\n    Delta(High-Low)=-5.64pp (反向), Fisher p=0.695 → 翻译质量非 confounder\n    Llama 待确认一致性\n\n# ── Track 1 扩展 (P1) ──\n\n- plan_id: plan_109\n  name: \"探针权重可视化 + PCA\"\n  claim: \"C1 (detectability) + C4 (layer structure) — 定性证据\"\n  description: |\n    对最优层的线性探针权重做 PCA / t-SNE 可视化，展示冲突 vs 非冲突样本的分布。\n    跨语言对比：EN 和 ZH 的冲突表征在 PCA 空间中是否重叠？\n    为 \"mechanistic interpretability\" claim 提供定性证据（不能只有准确率数字）。\n  priority: P1\n  status: planned\n  gpu_hours: 0.5\n  depends_on: [mvp_001]\n\n- plan_id: plan_106\n  name: \"Label noise ablation\"\n  claim: \"C1 (detectability) — robustness\"\n  description: |\n    系统性注入 5%/10%/15%/20% label noise，测量 probe accuracy 下降曲线。\n    评估 verification pipeline 的 label error tolerance。\n  priority: P1\n  status: planned\n  gpu_hours: 4\n  depends_on: [mvp_001]\n\n- plan_id: plan_107\n  name: \"Representation steering (干预实验)\"\n  claim: \"C2 (asymmetry) — RC8 因果证据\"\n  description: |\n    用探针方向作为 steering vector，在残差流中干预冲突信号。\n    测量干预后模型输出（parametric vs contextual answer）的变化。\n    提供 C2 不对称性的因果证据（不仅是相关性）。\n    如果 Track 3 SAE steering 无法完成，此实验是因果证据的唯一来源。\n  priority: P0\n  status: planned\n  gpu_hours: 8\n  depends_on: [mvp_001, plan_104]\n\n- plan_id: plan_108\n  name: \"更大数据集验证\"\n  claim: \"C1 (detectability) — RC4 数据充分性\"\n  description: |\n    扩大 ConflictQA 采样至 2000+ samples per model (当前 ~1000)。\n    或引入其他知识冲突数据集（如 SQuAD-conflict, WebQuestions-conflict）。\n  priority: P1\n  status: planned\n  gpu_hours: 12\n  depends_on: []\n\n# ── Track 2: SAE Feature Analysis (P1-P2) ──\n\n- plan_id: plan_201\n  name: \"Qwen-Scope SAE 冲突特征识别\"\n  claim: \"C5 (SAE features)\"\n  description: |\n    用 Qwen-Scope 预训练 SAE (Qwen3-8B-Base) 分析冲突激活中的差异化特征。\n    适配 cloze/completion 格式（base model 兼容）。\n    SpARE mutual-information feature selection 方法。\n  priority: P1\n  status: planned\n  gpu_hours: 16\n  depends_on: [mvp_001]\n\n- plan_id: plan_202\n  name: \"LangFIR 语言特征解耦\"\n  claim: \"C5 (SAE features) — 控制实验\"\n  description: |\n    用 LangFIR random-token filtering 识别 language-identity 特征。\n    从 SAE conflict features 中排除 language-identity 特征。\n    验证 conflict features 和 language features 的层分布是否非重叠。\n  priority: P1\n  status: planned\n  gpu_hours: 8\n  depends_on: [plan_201]\n\n- plan_id: plan_203\n  name: \"Cross-lingual feature Jaccard 分析\"\n  claim: \"C5 (SAE features) — H1 vs H2 检验\"\n  description: |\n    计算 mid-layer vs late-layer conflict feature 的跨语言 Jaccard index。\n    H1 预测: mid-layer Jaccard >> late-layer Jaccard\n    H2 预测: 无显著差异或 mid < late\n    Paired permutation test p < 0.05。\n  priority: P1\n  status: planned\n  gpu_hours: 4\n  depends_on: [plan_201, plan_202]\n\n# ── Track 3: Steering (P2) ──\n\n- plan_id: plan_301\n  name: \"Monolingual→cross-lingual steering transfer\"\n  claim: \"C6 (steering)\"\n  description: |\n    用 SpARE 的英语冲突特征做 cross-lingual steering。\n    测量跨语言 steering 有效性 (EM_C, EM_M, flip rates)。\n  priority: P2\n  status: planned\n  gpu_hours: 16\n  depends_on: [plan_201, plan_203]\n\n- plan_id: plan_302\n  name: \"Cross-lingual-specific steering\"\n  claim: \"C6 (steering)\"\n  description: |\n    用 Track 2 发现的跨语言特有特征构建 steering vectors。\n    对比与 monolingual features 的 steering 效果差异。\n  priority: P2\n  status: planned\n  gpu_hours: 16\n  depends_on: [plan_301]\n\n- plan_id: plan_303\n  name: \"Typological steering correlation\"\n  claim: \"C6 (steering) — CLEAR 因果链接\"\n  description: |\n    测试 steering 有效性是否与 CLEAR 的 linguistic similarity metric 相关。\n    提供 linguistic similarity → conflict resolution 的因果（非仅相关）证据。\n  priority: P2\n  status: planned\n  gpu_hours: 12\n  depends_on: [plan_301, plan_103]\n",
      "numLines": 256,
      "startLine": 1,
      "totalLines": 256
    }
  },
  "sourceToolAssistantUUID": "2205eab6-f82a-4887-884e-060109509def",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13 · 2026-05-22T02:52:25.968Z_

````json
{
  "parentUuid": "fce7b6f6-d876-4989-ac21-591f0ed03364",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**clkc_mech_interp**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"clkc_mech_interp\")` 或 `load_project_config(\"clkc_mech_interp\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **paper-writing-norms** — 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/clkc_mech_interp/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "b3c08ce7-aa08-4a58-a5bb-563a8f71a5d4",
  "timestamp": "2026-05-22T02:52:25.968Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：第三模型不对称消失或反转，核心 C2 claim 崩塌，需重新定位论文 angle 核心假设：['第三模型不对称 <2pp 或方向反转（EN→ZH > ZH→EN）', '仅 Llama 显著，Qwen+第三模型均不显著，方向不全一致', '不对称性可能是 Llama 训练数据分布的 artifact 而非…",
  "leafUuid": "b3c08ce7-aa08-4a58-a5bb-563a8f71a5d4",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase 1 worst case scenario experiment planning",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b"
}
```

---

### Assistant

_source line 16 · 2026-05-22T02:52:55.044Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture of the experiment plan with all planned experiments. Let me construct the worst-tier predictions for each planned experiment. Let me identify all experiments with status "planned":

1. **plan_102** - 第三模型架构验证 (P0)
2. **plan_103** - 多语言扩展 EN↔JA (P0)
3. **plan_104** - Layer-wise CKA/SVCCA (P0)
4. **plan_106** - Label noise ablation (P1)
5. **plan_107** - Representation steering (P0)


6. **plan_108** - 更大数据集验证 (P1)
7. **plan_109** - 探针权重可视化 + PCA (P1)
8. **plan_201** - Qwen-Scope SAE 冲突特征识别 (P1)
9. **plan_202** - LangFIR 语言特征解耦 (P1)
10. **plan_203** - Cross-lingual feature Jaccard 分析 (P1)
11. **plan_301** - Monolingual→cross-lingual steering transfer (P2)
12. **plan_302** - Cross-lingual-specific features (P2)
13. **plan_303** - Typological steering correlation (P2)

mvp_003 is currently running and plan_105 is already complete. Now I'm defining the worst-case scenario for these experiments—where the third model's asymmetry disappears or reverses, undermining the core C2 claim. I'm setting the metric thresholds for this tier: only the first two models show significant asymmetry, within-language accuracy drops to 0.65-0.75, cross-lingual transfer falls to 0.58-0.70, MLP gains become weak at -1.0 to 3.0 percentage points, SAE cross-lingual Jaccard similarity at mid-layers approaches zero, and we validate across just one language pair.

For plan_102, the worst case is that Gemma-2-9B-IT shows asymmetry under 2 percentage points or even reversed (EN→ZH exceeding ZH→EN), which would suggest the ~7.2pp asymmetry observed in Llama and Qwen isn't universal. Plan_103 risks incomplete results before the deadline or inconsistent Japanese outputs, leaving only EN-ZH validated. Plan_104's layer-wise analysis would show language...

Representations diverge early, making it difficult to claim the asymmetry is language-universal. Plan_106 would demonstrate the probe has some sensitivity to label noise but doesn't add much beyond robustness validation. Plan_107's steering experiments show weak or inconsistent effects, failing to establish causality. Plan_108 and the Track 2 and 3 experiments likely won't finish in time—the larger dataset can't be completed, SAE features don't reveal cross-lingual sharing, and the remaining tracks are also deadline-constrained. Plan_109's probe weight visualization suggests EN and ZH clusters don't cleanly overlap, which does support language-specific encoding. Now I'll work through detailed predictions for each scenario.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3c08ce7-aa08-4a58-a5bb-563a8f71a5d4",
  "isSidechain": false,
  "requestId": "req_011CbGrFuodRDNN57Q3LZJGr",
  "type": "assistant",
  "uuid": "c745e42f-4602-426c-8714-647175b6c72e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEyAXbN878sEoQ2sJjZfTc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9454,
      "cache_read_input_tokens": 25312,
      "output_tokens": 12362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9454,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12362,
          "cache_read_input_tokens": 25312,
          "cache_creation_input_tokens": 9454,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9454
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

_source line 17 · 2026-05-22T02:56:45.127Z_

```yaml
tier: worst
narrative_guidance: >
  C2 不对称性降级为 observation。第三模型（Gemma/Mistral）不对称性消失或反转，
  Llama+Qwen 的 ~7.2pp 被判定为可能的训练数据 artifact 而非通用机制。
  论文 reframe 为 Path A "Architecture-dependent cross-lingual conflict processing"：
  冲突信号跨语言可检测（C1 robust），但迁移特性是架构依赖的。
  Track 2/3 均未在 DDL 前完成，论文仅含 Track 1 probing 结果。
  投稿定位从 mechanism discovery 降为 empirical characterization + methodology。

imagined_experiments:
  # ═══════════════════════════════════════════════
  # MVP / 已完成实验的 worst-case 补充验证
  # ═══════════════════════════════════════════════

  - name: "COMET 翻译质量验证（完整）"
    plan_id: "mvp_003"
    description: >
      wmt22-comet-da back-translation 完成 Llama 侧 COMET 评估。
      Qwen test 已完成（pass rate 18.45%），Llama train+test 完成评分。
    expected_results:
      llama_test_n: 272
      llama_test_pass_rate_at_080: 0.12
      llama_test_mean_comet: 0.68
      llama_train_n: 1096
      llama_train_pass_rate_at_080: 0.15
      llama_train_mean_comet: 0.69
      qwen_train_n: 798
      qwen_train_pass_rate_at_080: 0.16
      qwen_train_mean_comet: 0.70
      llama_comet_tertile_ablation_delta_pp: -3.2
      llama_comet_tertile_ablation_fisher_p: 0.48
    result_rationale: >
      Worst 下 Llama COMET 整体更低（0.68 vs Qwen 0.70），因为 Llama tokenizer 对中文的
      coverage 更差，back-translation 两步累积误差更大。但 ablation 方向仍为反向或无显著差异——
      这在 worst 档并不矛盾，因为翻译质量 confound 的排除对 C1 有利。
      实际风险在于：Llama 的 COMET ablation 如果出现 High > Low（质量确实影响 Llama 探针），
      就与 Qwen 结果不一致，需要额外解释。worst 假设 delta=-3.2pp（弱反向）且 p=0.48（不显著），
      刚好处于"不能确定排除但也不能确定是 confounder"的灰色地带。
    tables:
      - name: "COMET Back-Translation Summary"
        columns: ["Model", "Split", "N", "Mean COMET", "Pass Rate (>=0.80)"]
        rows:
          - ["Llama-3.1-8B", "train", 1096, 0.69, "15%"]
          - ["Llama-3.1-8B", "test", 272, 0.68, "12%"]
          - ["Qwen3-8B", "train", 798, 0.70, "16%"]
          - ["Qwen3-8B", "test", 168, 0.70, "18.5%"]
      - name: "COMET Tercile Ablation (Both Models)"
        columns: ["Model", "Low Acc", "Med Acc", "High Acc", "Delta(H-L)", "Fisher p"]
        rows:
          - ["Qwen3-8B", "66.35%", "67.69%", "60.71%", "-5.64pp", 0.695]
          - ["Llama-3.1-8B", "65.8%", "63.2%", "62.6%", "-3.2pp", 0.48]
    figures_description:
      - "COMET score distribution histogram (Llama vs Qwen, train+test), showing both models cluster around 0.65-0.75 with long left tail"
      - "Tercile ablation bar chart: probe balanced accuracy by COMET tercile, with error bars, both models side-by-side"
    analysis: >
      两个模型 ablation 方向均为弱反向（High COMET → 略低 acc），但 Llama delta 幅度
      远小于 Qwen（-3.2 vs -5.6pp），且 p 值更低（0.48 vs 0.695）。审稿人可能追问
      "为什么 Llama 方向一致但效果弱得多"。worst 下的 framing：两模型 ablation 均未达
      显著阈值，翻译质量不是主要 confounder，但需承认 back-translation COMET 本身
      作为翻译质量 proxy 的局限性。建议加入 forward-only COMET 作为补充指标。

  # ═══════════════════════════════════════════════
  # Track 1: Cross-Lingual Probing — P0 实验
  # ═══════════════════════════════════════════════

  - name: "第三模型架构验证"
    plan_id: "plan_102"
    description: >
      在 Gemma-2-9B-IT 上重复完整探针实验：verify → translate → collect activations →
      train probe → bootstrap n=100。验证 ~7.2pp 不对称性是否跨架构一致。
    expected_results:
      model: "Gemma-2-9B-IT"
      en_en_bal_acc: 0.72
      zh_zh_bal_acc: 0.68
      en_zh_bal_acc: 0.63
      zh_en_bal_acc: 0.64
      asymmetry_gap_pp: 1.0
      bootstrap_ci_95: "[-4.5, 6.8]"
      bootstrap_significant: false
      positive_iterations_pct: 58
      best_probe_layer: 18
      best_layer_depth_pct: 0.62
      mlp_en_zh_acc: 0.65
      mlp_gain_en_zh_pp: 2.0
      token_overlap_jaccard_mean: 0.035
      token_overlap_correlation_p: 0.31
    result_rationale: >
      Worst 核心假设：第三模型不对称性 <2pp 或方向反转。Gemma-2-9B 的多语言训练数据
      配比与 Llama/Qwen 不同——Gemma 的 ZH 数据占比可能更均衡或更低，导致英语锚点效应
      减弱。Within-lang acc 仍在 68-72%（C1 成立，冲突可检测），但跨语言迁移两个方向
      几乎对称（EN→ZH 63% vs ZH→EN 64%, gap 仅 1pp），CI 宽且含零。
      这意味着 Llama/Qwen 的 ~7.2pp 不对称性可能是这两个模型训练数据中英语主导的
      artifact，而非语言表征空间的通用结构特征。MLP gain 仅 +2pp（对比 Llama +4.7pp），
      非线性成分也弱得多，暗示 Gemma 的跨语言对齐更均匀。
      探针最优层在 62% depth（vs Llama 88%, Qwen 67%），层分布 pattern 无统一规律。
    tables:
      - name: "Cross-Lingual Probe Accuracy — Three Models"
        columns: ["Model", "EN→EN", "ZH→ZH", "EN→ZH", "ZH→EN", "Asym Gap", "95% CI", "Sig?"]
        rows:
          - ["Llama-3.1-8B", "77.1%", "71.2%", "64.1%", "71.3%", "+7.22pp", "[1.1, 13.6]", "Yes"]
          - ["Qwen3-8B", "75.3%", "71.6%", "65.0%", "72.2%", "+7.18pp", "[-1.2, 13.4]", "No"]
          - ["Gemma-2-9B", "72.0%", "68.0%", "63.0%", "64.0%", "+1.0pp", "[-4.5, 6.8]", "No"]
      - name: "MLP vs Linear — Weak Direction (EN→ZH)"
        columns: ["Model", "Linear", "MLP", "Gain (pp)"]
        rows:
          - ["Llama-3.1-8B", "64.1%", "68.8%", "+4.7"]
          - ["Qwen3-8B", "65.0%", "67.3%", "+2.3"]
          - ["Gemma-2-9B", "63.0%", "65.0%", "+2.0"]
      - name: "Best Probe Layer and Depth"
        columns: ["Model", "Total Layers", "Best Layer", "Depth %"]
        rows:
          - ["Llama-3.1-8B", 32, 28, "88%"]
          - ["Qwen3-8B", 36, 24, "67%"]
          - ["Gemma-2-9B", 42, 26, "62%"]
    figures_description:
      - "三模型不对称性 gap 的 forest plot（点估计 + 95% CI），Gemma CI 跨零且几乎对称"
      - "Layer-wise probe accuracy curves（三模型并排），显示 peak 层位置的跨架构差异"
      - "Bootstrap distribution histogram for asymmetry gap（三模型），Gemma 分布中心接近零"
    analysis: >
      Gemma 结果直接击穿 C2 "跨架构一致不对称性" claim。三模型中仅 Llama 显著（1/3），
      方向一致性降至 2/3（Gemma 名义方向仍为正但实质为零）。C2 不能再作为核心 claim。
      但 C1 稳健——三模型 within-lang acc 均 >65%（最低 Gemma 68%），远超 chance。
      Reframe 方向：不对称性是 architecture/training-data-dependent 的特征，其存在与否
      本身就是 finding。Llama（英语主导训练数据）和 Qwen（中英均衡但英语仍多）
      出现不对称，Gemma（不同数据配比）不出现——这揭示了多语言 LLM 内部跨语言
      对齐程度的异质性。引用 Wendler et al. 2024 "Llamas Know What GPTs Don't Show"
      的跨架构差异发现。

  - name: "多语言扩展 (EN↔JA)"
    plan_id: "plan_103"
    description: >
      扩展到 EN↔JA 语言对。JA 作为 CJK 但与 ZH typologically 不同的语言，
      检验不对称性是否与 typological distance 相关（H1 vs H2 检验）。
    expected_results:
      status: "incomplete_or_not_started"
      completion_pct: 15
      reason: "GPU 资源被 Track 1 三模型验证和 COMET 占满，JA 翻译+验证 pipeline 未启动"
      partial_results_if_any:
        ja_translation_comet_estimate: null
        ja_verify_pass_rate: null
      lang_pairs_validated: 1
    result_rationale: >
      Worst 假设 lang_pairs_validated=1（仅 EN-ZH）。JA 扩展需要完整 pipeline：
      翻译 ConflictQA → COMET 验证 → verify answers → collect activations → train probes
      → bootstrap。每个步骤在两个模型上重复。在 DDL 紧张（~4个月）且 GPU 资源被
      三模型验证（plan_102）和 COMET（mvp_003）占用的情况下，JA 扩展大概率无法
      在投稿前完成。worst 下仅完成了 JA 翻译的前期调研（15%），未产出可用数据。
      这使得 RC4（数据多样性）无法充分回应，论文只能聚焦 EN-ZH 单语言对。
    tables: []
    figures_description: []
    analysis: >
      单语言对是 worst 下最大的审稿风险之一。缺少 JA 无法检验 H2（语言距离编码假设），
      H1 vs H2 的解析力大幅下降。论文需在 Limitations 中明确承认并提出 future work。
      缓解策略：强调 EN-ZH 本身作为高 typological distance pair 的价值——如果机制
      在最难的语言对上都能检测到，更相近的语言对更可能工作。

  - name: "Layer-wise CKA/SVCCA"
    plan_id: "plan_104"
    description: >
      计算每层 EN vs ZH 激活的 CKA 和 SVCCA，量化跨语言表征相似度随层变化的 pattern。
    expected_results:
      llama_cka_early_layers_mean: 0.82
      llama_cka_mid_layers_mean: 0.61
      llama_cka_late_layers_mean: 0.38
      qwen_cka_early_layers_mean: 0.85
      qwen_cka_mid_layers_mean: 0.70
      qwen_cka_late_layers_mean: 0.45
      gemma_cka_early_layers_mean: 0.80
      gemma_cka_mid_layers_mean: 0.68
      gemma_cka_late_layers_mean: 0.42
      cka_probe_peak_correlation: -0.35
      language_transition_layer_llama_pct: 0.75
      language_transition_layer_qwen_pct: 0.58
      language_transition_layer_gemma_pct: 0.55
    result_rationale: >
      CKA 从高到低的单调下降是多语言 LLM 的已知 pattern（"Lost in Multilinguality"），
      worst 下也预期如此。但关键问题是 CKA 下降点与 probe peak 层的关系。
      Worst 假设：三模型的 language transition 层位置不一致（Llama 75%、Qwen 58%、
      Gemma 55%），与 probe peak 层（Llama 88%、Qwen 67%、Gemma 62%）之间
      没有简洁的跨架构规律。CKA-probe peak correlation 为弱负相关（-0.35），
      不足以支持"冲突信号出现在 language transition 之后"的干净叙事。
      这使得 C4（层结构 claim）只能描述现象而无法提出机制解释。
    tables:
      - name: "CKA Mean by Layer Group"
        columns: ["Model", "Early (0-33%)", "Mid (33-66%)", "Late (66-100%)", "Transition Layer %"]
        rows:
          - ["Llama-3.1-8B", 0.82, 0.61, 0.38, "75%"]
          - ["Qwen3-8B", 0.85, 0.70, 0.45, "58%"]
          - ["Gemma-2-9B", 0.80, 0.68, 0.42, "55%"]
      - name: "Probe Peak vs Language Transition"
        columns: ["Model", "Probe Peak Layer %", "CKA Transition %", "Gap (pp)"]
        rows:
          - ["Llama-3.1-8B", "88%", "75%", "+13"]
          - ["Qwen3-8B", "67%", "58%", "+9"]
          - ["Gemma-2-9B", "62%", "55%", "+7"]
    figures_description:
      - "三模型 layer-wise CKA 曲线（EN vs ZH），叠加 probe accuracy 曲线，双 y 轴"
      - "Language transition 层（CKA 最大下降点）vs Probe peak 层的散点图（仅 3 点，趋势弱）"
    analysis: >
      CKA 分析提供了描述性价值但无法产生强 claim。三模型均显示 CKA 随层下降，
      probe peak 在 transition 之后，但 gap 幅度不一致（+7 到 +13pp），
      且仅 3 个数据点不足以建立统计关系。worst 下此实验贡献降级为 supplementary
      evidence，不支撑独立 claim。C4 从"层结构 claim"降为"层结构 observation"。

  - name: "COMET 分段 ablation（Llama 补充）"
    plan_id: "plan_105"
    description: >
      Llama 侧 COMET tercile ablation，补充 Qwen 已完成的结果，
      验证翻译质量非 confounder 的结论跨架构一致性。
    expected_results:
      llama_test_n: 272
      llama_low_comet_acc: 65.8
      llama_med_comet_acc: 63.2
      llama_high_comet_acc: 62.6
      llama_delta_high_low_pp: -3.2
      llama_fisher_p: 0.48
      cross_model_consistency: "partial"
    result_rationale: >
      Worst 假设 COMET ablation 在 Llama 上方向一致（反向）但效果量小且 p 更低。
      Llama delta 仅 -3.2pp vs Qwen -5.64pp，Fisher p=0.48 处于灰色地带。
      不矛盾（两个模型方向均为反向），但 Llama 的弱效应可能被审稿人质疑为
      "翻译质量确实对 Llama 有微弱影响但样本量不够检测"。
      Worst 的 critical 场景（COMET ablation 在 Llama 上出现正向 delta——即
      High COMET 准确率更高）在 worst 定义中列为可能，但此处取 borderline 解释：
      方向一致但 convincing degree 不足。
    tables:
      - name: "COMET Tercile Ablation Cross-Model"
        columns: ["Model", "Low Acc", "Med Acc", "High Acc", "Delta(H-L) pp", "Fisher p", "Verdict"]
        rows:
          - ["Qwen3-8B", "66.35%", "67.69%", "60.71%", -5.64, 0.695, "Excluded"]
          - ["Llama-3.1-8B", "65.8%", "63.2%", "62.6%", -3.2, 0.48, "Borderline"]
    figures_description:
      - "双模型 COMET tercile ablation 并排条形图"
    analysis: >
      RC1 在 worst 下仍基本可以排除，但 Llama 侧的证据力弱于 Qwen。
      论文 framing 需要更谨慎：强调两模型方向均为反向（high quality ≠ better detection），
      同时承认 individual model 的 ablation power 受限于样本量。

  # ═══════════════════════════════════════════════
  # Track 1 扩展 — P1 实验
  # ═══════════════════════════════════════════════

  - name: "探针权重可视化 + PCA"
    plan_id: "plan_109"
    description: >
      最优层线性探针权重 PCA/t-SNE 可视化，展示冲突/非冲突样本分布，
      跨语言对比 EN vs ZH 表征空间。
    expected_results:
      pca_explained_variance_pc1_pc2: 0.28
      en_zh_conflict_cluster_overlap_visual: "partial"
      en_conflict_vs_en_nonconflict_separation: "moderate"
      zh_conflict_vs_zh_nonconflict_separation: "weak"
      cross_lingual_conflict_cluster_alignment: "misaligned"
    result_rationale: >
      Worst 下 PCA 前两主成分仅解释 28% 方差，冲突/非冲突分离在 EN 上 moderate
      但 ZH 上 weak——与 within-lang probe acc 差异一致（EN 77% vs ZH 71%）。
      关键 worst 特征：EN 和 ZH 的冲突 cluster 在 PCA 空间中不对齐（misaligned），
      暗示冲突表征并非 language-universal，而是在各语言子空间中独立编码。
      这与 Gemma 不对称消失一致——如果冲突表征不共享，跨语言迁移就依赖于
      各模型训练数据中建立的偶然对齐，而非结构性的 universal representation。
    tables: []
    figures_description:
      - "2D PCA scatter plot: EN conflict(红), EN non-conflict(浅红), ZH conflict(蓝), ZH non-conflict(浅蓝), 显示 EN/ZH 各自有弱分离但两个 conflict cluster 不重叠"
      - "t-SNE 版本（perplexity=30）: 更明显的 language 分离, conflict/non-conflict 在各语言内有亚结构"
    analysis: >
      可视化结果在 worst 下偏向 H2（language-specific encoding）。
      EN/ZH conflict cluster 不重叠使得 "universal conflict detector" 叙事站不住。
      但仍有可展示的 finding：within-language 分离的存在证明线性探针确实捕获了
      有意义的信号（不是噪声拟合），为 C1 提供定性支持。
      论文中放入 supplementary 而非 main text。

  - name: "Label noise ablation"
    plan_id: "plan_106"
    description: >
      注入 5%/10%/15%/20% label noise，测量 probe accuracy 下降曲线，
      评估 verification pipeline 的 label error tolerance。
    expected_results:
      noise_0pct_acc: 77.1
      noise_5pct_acc: 75.8
      noise_10pct_acc: 73.2
      noise_15pct_acc: 69.5
      noise_20pct_acc: 64.1
      degradation_slope_per_5pct: -3.3
      estimated_label_error_rate: 0.08
      acc_at_estimated_error: 74.5
    result_rationale: >
      Label noise ablation 在 worst 下仍产出合理结果——探针 acc 随 noise 单调下降，
      斜率约 -3.3pp/5%。但 worst 特征是 estimated label error rate 为 ~8%
      （高于理想的 <5%），暗示 verification pipeline 漏过了相当比例的错误标签。
      这使得 observed probe acc（如 Gemma 68%）的"真实上限"可能更高，但也
      意味着当前结果受 label noise 压制。论文需报告此估计但不作为借口。
    tables:
      - name: "Label Noise Ablation (Llama EN→EN)"
        columns: ["Noise %", "Balanced Acc", "Delta from Clean"]
        rows:
          - ["0%", "77.1%", "-"]
          - ["5%", "75.8%", "-1.3pp"]
          - ["10%", "73.2%", "-3.9pp"]
          - ["15%", "69.5%", "-7.6pp"]
          - ["20%", "64.1%", "-13.0pp"]
    figures_description:
      - "Noise rate vs Probe accuracy 折线图, 带 95% CI error bars, 标注 estimated true label error rate 区间"
    analysis: >
      Label noise ablation 是 defensive experiment——在 worst 下仍完成且结果合理。
      ~8% estimated label error 需要在论文中坦诚报告。可以 argue verification
      pipeline 的 error tolerance 是可接受的（acc 仅下降 ~2.5pp at 8% noise），
      但审稿人可能要求更严格的 verification。此实验在 worst 下属于"完成但不增强 claim"。

  - name: "Representation steering (干预实验)"
    plan_id: "plan_107"
    description: >
      用探针方向作为 steering vector 在残差流中干预冲突信号，
      测量干预后模型输出的变化，提供 C2 不对称性的因果证据。
    expected_results:
      llama_en_steer_flip_rate: 0.08
      llama_zh_steer_flip_rate: 0.05
      qwen_en_steer_flip_rate: 0.06
      qwen_zh_steer_flip_rate: 0.04
      gemma_en_steer_flip_rate: 0.03
      gemma_zh_steer_flip_rate: 0.03
      overall_flip_rate_mean: 0.048
      steer_direction_consistency: "inconsistent"
      causal_evidence_strength: "weak"
    result_rationale: >
      Worst 假设 steering 效果极弱——flip rate 均 <10%，且方向不一致。
      线性探针方向作为 steering vector 的假设前提是冲突信号集中在单一线性方向，
      但 PCA 可视化（plan_109）显示冲突表征在多维空间中分布，单一方向无法充分
      捕获。Gemma flip rate 仅 3%（近乎 random），因其不对称性本就消失。
      这使得 RC8（causal evidence）无法通过 Track 1 途径解决，而 Track 3 SAE
      steering 又不可用——论文在因果证据维度上存在空洞。
      Worst 下的 framing：steering 的低效本身是一个 finding——冲突信号不是简单的
      单一方向编码，而是分布在多维子空间中，需要更精细的干预方法。
    tables:
      - name: "Representation Steering Flip Rates"
        columns: ["Model", "EN Flip Rate", "ZH Flip Rate", "Mean", "Consistent Direction?"]
        rows:
          - ["Llama-3.1-8B", "8%", "5%", "6.5%", "Weak yes"]
          - ["Qwen3-8B", "6%", "4%", "5.0%", "Weak yes"]
          - ["Gemma-2-9B", "3%", "3%", "3.0%", "No"]
    figures_description:
      - "Steering 强度 (alpha) vs Flip rate 曲线图, 三模型, 显示 Gemma 几乎平坦"
      - "Steered vs unsteered 输出 token probability 分布对比 (parametric vs contextual answer)"
    analysis: >
      Steering 在 worst 下基本失败。因果证据链断裂，论文只能依赖 probe correlation
      + permutation test 的统计控制，无法提供 intervention-based causal evidence。
      RC8 成为 acknowledged limitation。framing："the probe detects a real signal
      (permutation test p<0.001), but the signal is not concentrated enough for
      simple linear steering to alter model behavior"——这实际上对冲突编码机制
      提出了更深层的问题（多维 vs 单维），可作为 future work 切入点。

  - name: "更大数据集验证"
    plan_id: "plan_108"
    description: >
      扩大 ConflictQA 采样至 2000+ samples 或引入其他知识冲突数据集。
    expected_results:
      status: "not_started"
      reason: "P1 优先级 + GPU/人力资源集中于 P0 实验（plan_102, mvp_003）"
      estimated_completion: "post-submission"
    result_rationale: >
      Worst 假设 tracks_submission_ready=1（仅 Track 1），DDL 紧张下 P1 实验
      被砍。数据集扩展的 GPU 时间（12h）和人力投入（翻译+验证 pipeline 再跑一轮）
      在 worst 下不可用。RC4 只能靠现有 ~1000 samples/model 应对。
      缓解：强调 ConflictQA 的 sample 质量（verification pipeline）而非 quantity，
      并指出 1000 samples 在 probing 文献中并不算小。
    tables: []
    figures_description: []
    analysis: >
      P1 实验在 worst 下全部降为 future work。论文 Limitations 中需诚实列出
      数据量限制。如有审稿人要求 rebuttal 补数据，可在 rebuttal 期快速追加。

  # ═══════════════════════════════════════════════
  # Track 2: SAE Feature Analysis — P1/P2 实验
  # ═══════════════════════════════════════════════

  - name: "Qwen-Scope SAE 冲突特征识别"
    plan_id: "plan_201"
    description: >
      用 Qwen-Scope 预训练 SAE (Qwen3-8B-Base) 分析冲突激活中的差异化特征。
    expected_results:
      status: "not_completed"
      completion_pct: 0
      reason: "Track 2 整体未启动，DDL 前无法完成"
      sae_cross_lingual_jaccard_mid_layer: 0.0
    result_rationale: >
      Worst 假设 Track 2/3 均无法在 DDL 前完成。SAE 实验需要 16 GPU-hours 仅用于
      特征识别，加上下游 LangFIR（8h）和 Jaccard 分析（4h）共 28h，且依赖
      base model 适配（cloze 格式调试）。在 P0 实验消耗大量 GPU 和研究时间的情况下，
      Track 2 被搁置。sae_cross_lingual_jaccard_mid_layer=0.0 表示无数据。
    tables: []
    figures_description: []
    analysis: >
      Track 2 缺失意味着 C5 完全不支持，论文无法提供 SAE 层面的机制证据。
      H1 vs H2 的 SAE Jaccard 检验（plan_203）也无法执行。
      这是 worst 下论文 claim 强度下降的主要原因之一——仅靠 probing 无法提供
      "冲突特征是什么"的答案，只能说"冲突信号存在"。

  - name: "LangFIR 语言特征解耦"
    plan_id: "plan_202"
    description: >
      用 LangFIR random-token filtering 识别 language-identity 特征，
      从 SAE conflict features 中排除，验证分布是否非重叠。
    expected_results:
      status: "not_started"
      depends_on_blocked: "plan_201"
    result_rationale: >
      依赖 plan_201 完成。plan_201 未启动则此实验自动阻塞。Worst 下无任何输出。
    tables: []
    figures_description: []
    analysis: "Blocked by plan_201. No output in worst tier."

  - name: "Cross-lingual feature Jaccard 分析"
    plan_id: "plan_203"
    description: >
      计算 mid-layer vs late-layer conflict feature 的跨语言 Jaccard index，
      检验 H1（mid >> late）vs H2（无差异）。
    expected_results:
      status: "not_started"
      depends_on_blocked: "plan_201, plan_202"
      sae_cross_lingual_jaccard_mid_layer: 0.0
      sae_cross_lingual_jaccard_late_layer: 0.0
    result_rationale: >
      依赖 plan_201 和 plan_202。两者均未完成则此实验无法执行。
      H1 vs H2 的 SAE 检验在 worst 下完全缺失，只能靠 probe transfer 间接推断。
    tables: []
    figures_description: []
    analysis: "Blocked. H1 vs H2 resolution degrades to probe-transfer-only evidence."

  # ═══════════════════════════════════════════════
  # Track 3: Steering — P2 实验
  # ═══════════════════════════════════════════════

  - name: "Monolingual→cross-lingual steering transfer"
    plan_id: "plan_301"
    description: >
      用 SpARE 英语冲突特征做 cross-lingual steering，
      测量跨语言 steering 有效性。
    expected_results:
      status: "not_started"
      depends_on_blocked: "plan_201, plan_203"
    result_rationale: >
      Track 3 完全依赖 Track 2（SAE 特征识别）。Track 2 未完成则 Track 3
      无可用的 steering vectors。Worst 下 C6（steering claim）完全不支持。
      plan_107（representation steering）是唯一的因果干预尝试，但其结果极弱。
    tables: []
    figures_description: []
    analysis: "Blocked by Track 2. No causal steering evidence available."

  - name: "Cross-lingual-specific steering"
    plan_id: "plan_302"
    description: >
      用 Track 2 发现的跨语言特有特征构建 steering vectors，
      对比与 monolingual features 的效果差异。
    expected_results:
      status: "not_started"
      depends_on_blocked: "plan_301"
    result_rationale: >
      双重阻塞：依赖 plan_301（未启动）和 Track 2 特征。Worst 下无输出。
    tables: []
    figures_description: []
    analysis: "Doubly blocked. No output in worst tier."

  - name: "Typological steering correlation"
    plan_id: "plan_303"
    description: >
      测试 steering 有效性与 CLEAR linguistic similarity metric 的相关性，
      提供因果链接。
    expected_results:
      status: "not_started"
      depends_on_blocked: "plan_301, plan_103"
    result_rationale: >
      依赖 plan_301（steering 未启动）和 plan_103（JA 扩展未完成）。
      这是论文 narrative 中连接 CLEAR 的因果桥梁，worst 下完全缺失。
      论文与 CLEAR 的连接只能停留在 correlational level——"我们发现的探针信号
      与 CLEAR 观察到的现象 consistent，但无法证明因果关系"。
    tables: []
    figures_description: []
    analysis: >
      缺失此实验使论文与 CLEAR 的连接从 "mechanistic explanation" 降为
      "consistent observation"。审稿人可能质疑 "为什么不做 steering 验证因果"。
      回应策略：承认 limitation 并将 steering 定位为 immediate future work，
      同时强调当前 probing 结果已为 CLEAR 的 linguistic affinity 发现提供了
      第一个 representation-level evidence（即使不是 causal evidence）。

  # ═══════════════════════════════════════════════
  # Worst Tier 综合评估
  # ═══════════════════════════════════════════════

  - name: "Worst Tier 投稿可行性综合评估"
    plan_id: "meta_assessment"
    description: >
      综合所有 worst-tier 预测，评估投稿可行性和最优 reframe 路径。
    expected_results:
      claims_fully_supported: ["C1"]
      claims_partially_supported: ["C3", "C4"]
      claims_collapsed: ["C2"]
      claims_no_evidence: ["C5", "C6"]
      tracks_submission_ready: 1
      lang_pairs_validated: 1
      models_with_significant_asymmetry: 1
      models_with_consistent_direction: 2
      recommended_path: "Path A"
      submission_venue_confidence: "borderline_accept"
    result_rationale: >
      Worst 综合：C1 稳健（三模型 within-lang >65%），C2 崩塌（仅 Llama 显著，
      Gemma 不对称消失），C3 方向一致但幅度跨架构差异大，C4 层结构无统一 pattern，
      C5/C6 无数据。论文体量缩至 Track 1 only。
      Path A 是最优选择——将不对称性的跨架构差异本身作为 finding，定位为
      "Architecture-dependent cross-lingual conflict processing"。
      C1（detectability）作为核心贡献，C2 降级为 architecture-dependent observation，
      C3/C4 作为 supplementary characterization。
      ICLR 投稿仍可行但竞争力显著下降——缺乏 mechanism（SAE）和 causation（steering），
      论文定位从 Oral/Spotlight 目标降为 Poster borderline。
    tables:
      - name: "Worst Tier Claim Status Summary"
        columns: ["Claim", "Status", "Evidence Strength", "Role in Paper"]
        rows:
          - ["C1: Detectability", "Supported", "Strong (3 models, all >65%)", "Core claim"]
          - ["C2: Asymmetry", "Collapsed", "Weak (1/3 significant)", "Observation only"]
          - ["C3: Non-linearity", "Partial", "Direction consistent, magnitude varies", "Supporting"]
          - ["C4: Layer structure", "Partial", "Descriptive only, no pattern", "Supplementary"]
          - ["C5: SAE features", "No evidence", "Track 2 not completed", "Future work"]
          - ["C6: Steering", "No evidence", "Track 3 not completed", "Future work"]
      - name: "Worst Tier Key Metrics vs Thresholds"
        columns: ["Metric", "Worst Value", "Threshold for C2", "Verdict"]
        rows:
          - ["Third model asym gap", "+1.0pp", ">2pp", "Below"]
          - ["Significant models (of 3)", "1", ">=2", "Below"]
          - ["Consistent direction (of 3)", "2", "3", "Below"]
          - ["Third model within-lang acc", "68-72%", ">65%", "Pass (C1 OK)"]
          - ["Cross-lingual transfer range", "63-64%", ">58%", "Pass (C1 OK)"]
          - ["MLP gain (third model)", "+2.0pp", ">3pp", "Weak"]
          - ["SAE Jaccard mid-layer", "0.0 (N/A)", ">0", "No data"]
          - ["Lang pairs validated", "1", ">=2", "Below"]
          - ["Tracks ready", "1", ">=2", "Below"]
    figures_description:
      - "Paper structure diagram under worst tier: Track 1 only, C1 core, C2 降级, C3/C4 supplementary, C5/C6 future work"
    analysis: >
      Worst 下论文仍有内容可写（C1 robust + 三模型跨架构对比 + methodology），
      但贡献度从"跨语言冲突处理的机制发现"降为"跨语言冲突可检测性的实证 characterization
      + architecture-dependent transfer 的初步观察"。
      Path A framing 的关键卖点：正是因为不对称性在 Gemma 上消失，才揭示了一个
      更深层的问题——多语言 LLM 的跨语言对齐程度是 heterogeneous 的，模型训练
      数据的语言配比直接影响冲突信号的跨语言迁移特性。这个 finding 对多语言 LLM
      的安全性和可靠性有直接实践意义（不能假设所有模型的跨语言行为一致）。
      投稿策略：以 ICLR 为目标但准备 ACL/EMNLP 作为 backup venue，后者对
      empirical analysis 的接受度更高。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c745e42f-4602-426c-8714-647175b6c72e",
  "isSidechain": false,
  "requestId": "req_011CbGrFuodRDNN57Q3LZJGr",
  "type": "assistant",
  "uuid": "4f44e5b9-6df1-4012-83a6-39da79a92765",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEyAXbN878sEoQ2sJjZfTc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9454,
      "cache_read_input_tokens": 25312,
      "output_tokens": 12362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9454,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12362,
          "cache_read_input_tokens": 25312,
          "cache_creation_input_tokens": 9454,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9454
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

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：第三模型不对称消失或反转，核心 C2 claim 崩塌，需重新定位论文 angle 核心假设：['第三模型不对称 <2pp 或方向反转（EN→ZH > ZH→EN）', '仅 Llama 显著，Qwen+第三模型均不显著，方向不全一致', '不对称性可能是 Llama 训练数据分布的 artifact 而非…",
  "leafUuid": "4f44e5b9-6df1-4012-83a6-39da79a92765",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase 1 worst case scenario experiment planning",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：第三模型不对称消失或反转，核心 C2 claim 崩塌，需重新定位论文 angle 核心假设：['第三模型不对称 <2pp 或方向反转（EN→ZH > ZH→EN）', '仅 Llama 显著，Qwen+第三模型均不显著，方向不全一致', '不对称性可能是 Llama 训练数据分布的 artifact 而非…",
  "leafUuid": "4f44e5b9-6df1-4012-83a6-39da79a92765",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase 1 worst case scenario experiment planning",
  "sessionId": "5cce21d6-2585-4f07-8410-bde5fd24be9b"
}
```

---
