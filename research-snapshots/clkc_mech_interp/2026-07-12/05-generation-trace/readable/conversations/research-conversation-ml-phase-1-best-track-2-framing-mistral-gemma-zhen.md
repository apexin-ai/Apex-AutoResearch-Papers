# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：第三模型复现显著不对称 + Track 2 出初步结果，原始 framing 全线成立 核心假设：['第三模型（Mistral/Gemma）ZH→EN 

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-2/e2f5f01b-c87b-4fdd-9bed-adef3a97350c.jsonl`
- **Structured JSON:** [`b3c5a48fa13eeb6318f9.json`](../../sessions/b3/b3c5a48fa13eeb6318f9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T02:39:46.174Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T02:39:46.174Z",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：第三模型复现显著不对称 + Track 2 出初步结果，原始 framing 全线成立\n核心假设：['第三模型（Mistral/Gemma）ZH→EN vs EN→ZH 不对称性显著（bootstrap CI 排除零）', '3/3 模型方向一致，≥2/3 达统计显著', 'MLP non-linearity 方向在第三模型复现', 'Llama COMET tercile ablation 复现 Qwen 的 not_confounder 结论', 'Track 2 SAE 在 Qwen-Scope 上识别出跨语言共享 conflict feature（Jaccard > 0.15）', '≥1 额外语言对（EN-JA 或 EN-DE）方向一致']\n关键指标范围：{'third_model_asymmetry_gap_pp': [5.0, 12.0], 'significant_asymmetry_models_of_3': [2, 3], 'consistent_direction_models_of_3': [3, 3], 'third_model_within_lang_acc': [0.72, 0.82], 'cross_lingual_transfer_acc_range': [0.63, 0.75], 'mlp_gain_weak_direction_pp_third_model': [3.0, 10.0], 'sae_cross_lingual_jaccard_mid_layer': [0.15, 0.35], 'lang_pairs_validated': [2, 3], 'tracks_submission_ready': [1, 2]}\n叙事方向：原始 framing 完全成立：CLEAR entity-centric 冲突解决的首个机制解释。 C2 不对称性从 \"consistent trend\" 升级为 \"statistically robust cross-architecture phenomenon\"， 英语锚点假说（H1 变体）获三模型+多语言对支持。 Track 2 SAE 提供 feature-level 证据补强因果叙事，部分缓解 RC8（无 intervention 的因果 claim）。 论文定位：mechanistic interpretability + cross-lingual，双社区贡献。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: clkc_mech_interp\nfocus: 重点评估：1) C2 不对称性 claim 在 Llama borderline 显著 + Qwen 不显著的情况下能否撑住；2) 只有 Track 1 probing 无 Track 2/3 SAE+steering 时论文贡献强度是否足够 ICLR；3) back-translation COMET 低但 ablation 排除 confounder 的 framing 是否说服审稿人\n\n## paper_framing.md\n\n# Paper Framing — clkc_mech_interp\n\n> 最后更新: 2026-05-22 | 目标: ICLR 2027 (DDL ~2026-09-24)\n\n## Core Insight\n\n多语言 LLM 中，跨语言知识冲突的检测信号可在残差流中被线性探针检测，且跨语言迁移呈现**方向性不对称**（ZH→EN >> EN→ZH ~7.2pp），该不对称性跨架构高度一致（Llama-3.1-8B 与 Qwen3-8B）。这为 CLEAR (Zhao et al. 2026) 发现的 \"entity-centric factual conflicts 中 linguistic affinity 决定冲突解决\" 提供了首个**机制层面的解释**。\n\n**注意**: CLEAR 的发现是 task-dependent 的——entity-centric factual conflicts 由 linguistic affinity 主导，reasoning-intensive tasks 由 resource abundance 主导。我们使用 ConflictQA（entity-centric），引用 CLEAR 时必须限定为 entity-centric 场景。\n\n## Narrative Structure\n\n**现象驱动的机制解释**（非 \"applying X to Y\"）：\n\n1. **Phenomenon**: CLEAR 发现在 entity-centric factual conflicts 中，linguistic affinity（而非 resource abundance）决定跨语言冲突解决，但未提供机制解释\n2. **Mechanistic question**: 冲突信号在模型内部如何编码？是 language-universal 还是 language-specific？为什么 similarity 起决定作用？\n3. **Our answer**: 通过残差流探针、SAE 特征分析、激活干预三条互补分析轨道，揭示冲突检测信号的跨语言结构——是否共享、在哪些层出现、能否用于干预\n\n**Secondary framing**: SAE-based mechanistic interpretability 工具在跨语言条件下的 stress test——probing / SAE / steering 三种工具的跨语言适用性边界\n\n## Competing Hypotheses (pre-registered)\n\n**H1 — English-anchored universal detection**:\n冲突检测信号本身是 language-independent 的（\"是否存在冲突\" 是语言无关判断），编码在 mid-layer 共享表征空间中。final-layer language transition 引入 similarity-dependent 干扰，影响 resolution 但不影响 detection。\n- 预测: mid-layer conflict feature 跨语言 Jaccard >> late-layer Jaccard (paired permutation test p < 0.05)\n- 预测: 英语探针跨语言迁移更强（英语作为训练数据主导语言，表征空间以英语为锚点）\n\n**H2 — Language-pair-specific encoding**:\n冲突特征从 mid-layer 起即为 language-pair-specific 的，linguistic distance 直接编码在冲突表征中。\n- 预测: mid-layer 和 late-layer Jaccard 无显著差异，或 mid < late\n- 预测: 探针迁移准确率与语言对 typological distance 强相关\n\n**MVP 证据倾向**:\n当前双模型结果倾向 **H1 的变体**——ZH→EN 迁移（71-72%）显著强于 EN→ZH（64-65%），暗示冲突信号以英语表征空间为锚点编码。非线性成分（MLP EN→ZH +9.2pp vs linear）提示 EN→ZH 方向的跨语言映射更复杂。\n\n## Core Claims\n\n### Claim 1: Cross-lingual conflict detectability\n**Statement**: 跨语言知识冲突信号可在残差流中被线性探针检测，准确率显著高于随机基线。\n**Evidence needed**:\n- ≥2 model architectures 的 within-language probe acc > 70% (balanced) ✅ (Llama 77.1%, Qwen 75.3%)\n- Permutation test p < 0.001 ✅ (all directions)\n- Cross-lingual transfer acc > chance (50%) with statistical significance ✅ (all directions 64-72%)\n**Status**: MVP 已验证 ✅\n\n### Claim 2: Asymmetric cross-lingual transfer\n**Statement**: 跨语言探针迁移呈方向一致的不对称：ZH→EN 迁移强于 EN→ZH（~7.2pp），效果量跨架构高度一致（Llama 显著，Qwen 方向一致但未达显著）。\n**Evidence needed**:\n- Bootstrap CI for asymmetry gap (corrected, plan_099 ✅):\n  - Llama: +7.22pp, CI [1.1%, 13.6%] — 排除零但 borderline ✅\n  - Qwen: +7.18pp, CI [-1.2%, 13.4%] — 含零，方向一致 ⚠️\n- ≥2 models show consistent effect size ✅ (7.22pp vs 7.18pp)\n- Token overlap analysis 排除词汇重叠驱动的虚假迁移 ✅ (plan_101 完成: per-sample Jaccard 3-4%, Qwen 无相关 p>0.4, Llama 显著负相关 r=-0.15 p=0.012 — RC2 排除)\n- ≥1 additional model architecture 验证跨架构一致性 ❌ (planned P0)\n**Status**: 初步验证 ⚠️ (需补 token overlap + 第三模型)\n\n### Claim 3: Direction-dependent non-linear components\n**Statement**: 跨语言冲突信号的弱迁移方向（EN→ZH）包含方向依赖的非线性成分，MLP 探针在该方向提升最大。跨架构一致方向但幅度不同（Llama +9.2pp single-seed / ~+4.7pp bootstrap-corrected, Qwen +2.3pp），暗示非线性成分与模型的跨语言对齐程度相关。\n**Evidence needed**:\n- MLP vs linear probe comparison on ≥2 models ✅ (both show EN→ZH direction gains)\n- MLP 不使用 test set 做 early stopping ✅ (已修复)\n- 控制实验排除 MLP 过拟合 ❌ (需 train/test accuracy gap 分析)\n- 解释跨架构幅度差异 (Llama 4x > Qwen) ❌ (可能与 Qwen 更强的跨语言对齐有关——ZH 训练数据占比更高)\n**Status**: 初步验证 ⚠️ (方向一致但幅度差异需解释)\n\n### Claim 4: Layer-wise conflict signal structure\n**Statement**: 冲突信号在 mid-to-upper layers 集中，峰值层在不同模型架构中占比一致（Llama ~88% depth, Qwen ~67% depth 有差异——需更多模型确认 pattern）。\n**Evidence needed**:\n- Layer-wise probe accuracy curves for ≥3 models ❌\n- Layer-wise CKA/SVCCA 量化 EN vs ZH 表征相似度 ❌\n- 与 \"Lost in Multilinguality\" 的 language transition 层对比 ❌\n**Status**: 未验证 ❌\n\n### Claim 5: Cross-lingual SAE conflict features (Track 2)\n**Statement**: SAE 特征空间中存在跨语言共享的冲突编码特征，可与 language-identity 特征解耦。\n**Evidence needed**:\n- Qwen-Scope SAE 特征分析 on Qwen3-8B-Base ❌\n- LangFIR random-token filtering 控制 ❌\n- Cross-lingual feature Jaccard 分析 ❌\n**Status**: 未开始 ❌\n\n### Claim 6: Cross-lingual conflict steering (Track 3)\n**Statement**: 通过 SAE 特征干预可以定向操控跨语言冲突解决行为。\n**Evidence needed**:\n- SpARE 框架跨语言扩展 ❌\n- Monolingual → cross-lingual steering transfer ❌\n- Steering effectiveness vs linguistic distance correlation ❌\n**Status**: 未开始 ❌ (依赖 Track 2)\n\n## Anticipated Reviewer Concerns\n\n### RC1: Translation quality confound [RESOLVED ✅]\n**Concern**: 中文翻译质量差可能导致虚假的冲突信号或迁移失败\n**Result**: Plan_105 COMET tercile ablation 证明翻译质量非 confounder。Qwen test: Low COMET (mean 0.585) → 66.35% acc, High COMET (mean 0.816) → 60.71% acc, delta=-5.64pp (反向), Fisher p=0.695。冲突信号检测不依赖翻译质量。Back-translation COMET ≥0.80 阈值过严（两步翻译天然拉低），但 ablation 实证排除了翻译质量 confound。\n**Remaining**: Llama test COMET 完成后重复此分析确认一致性。\n\n### RC2: Token overlap confound [RESOLVED ✅]\n**Concern**: 跨语言迁移可能由 EN-ZH 共享 token（数字、专有名词、标点）驱动\n**Result**: Per-sample Jaccard 仅 3-4%（type-level 10-15% 被膨胀）。Qwen 无相关 (p>0.4)，Llama 显著负相关 (r=-0.15, p=0.012, tercile Δ=-23.9pp)。高 overlap 反而降低准确率，方向与 RC2 相反。**共享 token 不驱动跨语言迁移，迁移发生在语义表示层。**\n\n### RC3: Model coverage insufficient [HIGH]\n**Concern**: 只有 2 个模型，无法声称 \"架构无关\"\n**Mitigation**: 加 ≥1 不同架构（Mistral/Gemma），验证 ~7.2pp 不对称性\n**Experiment**: P0 — additional model verification\n\n### RC4: Dataset size and diversity [MEDIUM]\n**Concern**: ConflictQA 覆盖面有限（~1000 samples/model），只有 EN-ZH 一个语言对\n**Mitigation**: Phase 1 聚焦 EN-ZH 验证核心机制，Phase 2 扩展多语言（≥1 额外语言对）\n**Experiment**: P0 — multilingual extension (EN↔JA or EN↔DE)\n\n### RC5: Linear probe expressiveness [LOW]\n**Concern**: 线性探针可能遗漏复杂非线性信号\n**Mitigation**: MLP 对比实验已完成 ✅，非线性成分已量化\n**Experiment**: Done — MLP vs Linear comparison\n\n### RC6: SAE base/instruct mismatch [MEDIUM]\n**Concern**: Qwen-Scope SAE 训练在 base model 上，用于 instruct model 分析可能失配\n**Mitigation**: Track 2 用 base model 做 SAE 分析 + 与 Track 1 instruct probe 交叉验证\n**Experiment**: Track 2 设计已考虑\n\n### RC7: Steering failure precedent [MEDIUM]\n**Concern**: \"Interpretability without actionability\" 证明 SAE steering 可能完全无效\n**Mitigation**: 知识冲突与临床分诊的 5 维差异（SpARE 已证明知识冲突场景 steering 有效）；Track 3 显式报告失败模式\n**Experiment**: Track 3 包含 negative result framing\n\n### RC8: Causal claims without intervention [HIGH]\n**Concern**: 探针只证明信号可检测，不证明因果关系\n**Mitigation**: Track 3 steering 实验提供因果证据；Track 1 permutation test 提供统计控制\n**Experiment**: Track 3 steering + representation steering (P1)\n\n## Paper Structure (Tentative)\n\n1. **Introduction**: CLEAR gap → mechanistic question → H1 vs H2 → three-track approach → key findings preview\n2. **Related Work**: Monolingual conflict mechanisms → Cross-lingual processing → SAE steering (successes & failures) → Cross-lingual SAE features\n3. **Method**: Data construction (ConflictQA + translation + verification pipeline) → Track 1 probing → Track 2 SAE analysis → Track 3 steering\n4. **Experiments & Results**:\n   - 4.1 Cross-lingual conflict detectability (C1)\n   - 4.2 Asymmetric transfer analysis (C2) + token overlap controls\n   - 4.3 Non-linear components (C3) + layer-wise structure (C4)\n   - 4.4 SAE feature analysis (C5) [if Track 2 ready]\n   - 4.5 Steering experiments (C6) [if Track 3 ready]\n5. **Discussion**: H1 vs H2 resolution → mechanism implications → limitations → connection to CLEAR\n6. **Conclusion**\n\n## Scope Control\n\n**投稿最低要求 (must-have for submission)**:\n- Claims 1-3 fully supported (cross-lingual detectability + asymmetry + non-linearity)\n- Claim 4 partially supported (layer-wise analysis on ≥2 models)\n- ≥3 model architectures\n- ≥2 language pairs (EN-ZH + one more)\n- Token overlap control\n- COMET translation quality validation\n\n**理想状态 (nice-to-have)**:\n- Track 2 SAE analysis (Claim 5)\n- Track 3 steering (Claim 6)\n- 5+ language pairs covering multiple typological families\n- Full CKA/SVCCA layer analysis\n\n**不做 (out of scope)**:\n- 10-language full CLEAR replication\n- Custom SAE training\n- MoE model analysis\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_probe_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bootstrap_asymmetry_diff_corrected: 0.0718\n    bootstrap_asymmetry_ci_corrected: '[-0.0119, 0.1341]'\n    bootstrap_asymmetry_significant_corrected: false\n    bootstrap_asymmetry_method: per_iteration_paired_diff_from_training_bootstrap_n100\n    bootstrap_asymmetry_diff_old: 0.0595\n    bootstrap_asymmetry_ci_old: '[-0.0367, 0.1481]'\n    comet_tertile_ablation:\n      conclusion: not_confounder\n      delta_high_low_pp: -5.64\n      fisher_p: 0.695\n      high_bal_acc: 0.6071\n      med_bal_acc: 0.6769\n      low_bal_acc: 0.6635\n      best_layer: 22\n      detail: Reversed direction (High COMET → lower probe acc). COMET gate can be\n        relaxed.\n- exp_id: mvp_probe_llama_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bootstrap_asymmetry_diff_corrected: 0.0722\n    bootstrap_asymmetry_ci_corrected: '[0.0110, 0.1361]'\n    bootstrap_asymmetry_significant_corrected: true\n    bootstrap_asymmetry_method: per_iteration_paired_diff_from_training_bootstrap_n100\n    bootstrap_asymmetry_diff_old: 0.1176\n    bootstrap_asymmetry_ci_old: '[0.0429, 0.1957]'\n- exp_id: llama31_en_activations\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen3_translate_zh\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: collect_en_activations_qwen3_8b\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: collect_en_activations_llama_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: translate_zh_llama_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: translate_zh_qwen\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: collect_en_act_llama_v3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: collect_en_act_qwen_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: verify_qwen3_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen_en_act_v3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: llama_zh_act\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen_zh_act\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: translate_zh_qwen_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: probe_qwen_full\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: comet_qwen\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_llama\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_qwen_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_llama_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_qwen_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_llama_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_qwen_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_llama_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_qwen_v5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    death_cause: EXIT_CODE=124 timeout kill by submit_training_job (REGISTRY ONLY\n      - actual nohup processes alive)\n    restart_pid: 59412\n    restart_gpu: cuda:0\n    restart_method: nohup + TRANSFORMERS_OFFLINE=1\n    restart_time: '2026-05-21T23:15:00Z'\n    no_resume: true\n    acceleration: cuda:1 并行处理 test set (168条) - COMPLETED\n    qwen_test_completed: true\n    qwen_test_total: 168\n    qwen_test_passed: 31\n    qwen_test_pass_rate: 0.185\n    qwen_test_mean_comet: 0.7016\n    qwen_test_passed_mean_comet: 0.8503\n    qwen_train_progress: 320/798 (~40%)\n    actual_status: train still running on cuda:0 (PID 59412)\n    registry_failed_is_false_alarm: true\n- exp_id: comet_llama_v5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    death_cause: EXIT_CODE=124 timeout kill by submit_training_job (REGISTRY ONLY\n      - actual nohup processes alive)\n    restart_pid: 59571\n    restart_gpu: cuda:2\n    restart_method: nohup + TRANSFORMERS_OFFLINE=1\n    restart_time: '2026-05-21T23:15:00Z'\n    no_resume: true\n    acceleration: cuda:3 并行处理 test set (272条) - IN PROGRESS 66%\n    llama_train_progress: 300/1096 (~27%)\n    llama_test_progress: 180/272 (~66%)\n    actual_status: train on cuda:2 (PID 59571), test on cuda:3 (PID 64179)\n    registry_failed_is_false_alarm: true\n- exp_id: qwen_zh_act_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: comet_qwen_v6\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: comet_llama_v6\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n\n重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: [\"Judge\", \"Biased?\"]`），否则 `?` `:` 等字符会导致解析失败。\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-22T02:39:46.178Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T02:39:46.178Z",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-22T02:39:46.199Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：第三模型复现显著不对称 + Track 2 出初步结果，原始 framing 全线成立
核心假设：['第三模型（Mistral/Gemma）ZH→EN vs EN→ZH 不对称性显著（bootstrap CI 排除零）', '3/3 模型方向一致，≥2/3 达统计显著', 'MLP non-linearity 方向在第三模型复现', 'Llama COMET tercile ablation 复现 Qwen 的 not_confounder 结论', 'Track 2 SAE 在 Qwen-Scope 上识别出跨语言共享 conflict feature（Jaccard > 0.15）', '≥1 额外语言对（EN-JA 或 EN-DE）方向一致']
关键指标范围：{'third_model_asymmetry_gap_pp': [5.0, 12.0], 'significant_asymmetry_models_of_3': [2, 3], 'consistent_direction_models_of_3': [3, 3], 'third_model_within_lang_acc': [0.72, 0.82], 'cross_lingual_transfer_acc_range': [0.63, 0.75], 'mlp_gain_weak_direction_pp_third_model': [3.0, 10.0], 'sae_cross_lingual_jaccard_mid_layer': [0.15, 0.35], 'lang_pairs_validated': [2, 3], 'tracks_submission_ready': [1, 2]}
叙事方向：原始 framing 完全成立：CLEAR entity-centric 冲突解决的首个机制解释。 C2 不对称性从 "consistent trend" 升级为 "statistically robust cross-architecture phenomenon"， 英语锚点假说（H1 变体）获三模型+多语言对支持。 Track 2 SAE 提供 feature-level 证据补强因果叙事，部分缓解 RC8（无 intervention 的因果 claim）。 论文定位：mechanistic interpretability + cross-lingual，双社区贡献。


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

重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: ["Judge", "Biased?"]`），否则 `?` `:` 等字符会导致解析失败。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e5796808-4efb-41f2-ba25-a8da19529122",
  "type": "user",
  "uuid": "65968bc0-536a-466e-939e-3a8a9d43689e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T02:39:46.198Z_

```json
{
  "parentUuid": "65968bc0-536a-466e-939e-3a8a9d43689e",
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
  "uuid": "6691a1bf-352c-4728-97c9-28a7f212f42d",
  "timestamp": "2026-05-22T02:39:46.198Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T02:39:46.198Z_

```json
{
  "parentUuid": "6691a1bf-352c-4728-97c9-28a7f212f42d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f8f45d46-bde5-4858-add8-3ab2afd61a40",
  "timestamp": "2026-05-22T02:39:46.198Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：第三模型复现显著不对称 + Track 2 出初步结果，原始 framing 全线成立 核心假设：['第三模型（Mistral/Gemma）ZH→EN vs EN→ZH 不对称性显著（bootstrap CI 排除零）', '3/3 模型方向一致，≥2/3 达统计显著', 'MLP non-linearity…",
  "leafUuid": "f8f45d46-bde5-4858-add8-3ab2afd61a40",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual conflict detection mechanism in multilingual LLMs",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c"
}
```

---

### Assistant

_source line 8 · 2026-05-22T02:39:49.227Z_

Let me first read the experiment plan to understand all planned experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8f45d46-bde5-4858-add8-3ab2afd61a40",
  "isSidechain": false,
  "requestId": "req_011CbGqHukbYekArCNkg2ppU",
  "type": "assistant",
  "uuid": "d7014291-0605-4e68-9f34-68e76cb76464",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016R8znrAcpwRtepdck21gaD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12083,
      "cache_read_input_tokens": 11841,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12083,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 237,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12083
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

_source line 9 · 2026-05-22T02:39:52.960Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01HPRYTAH2zn3fDfuYoAJgpt`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan files",
  "prompt": "Search for the experiment plan file in /home/ubuntu/.agent-ml-research-prod42. Look for files named experiment_plan*, plan*, or similar YAML/MD files that contain planned experiments. Also check for any directory structure that might contain experiment definitions. Search broadly — try patterns like **/*experiment*plan*, **/*plan*.yaml, **/*plan*.md, **/experiments/*, and look in the root directory for any YAML or MD files that might contain experiment plans."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7014291-0605-4e68-9f34-68e76cb76464",
  "isSidechain": false,
  "requestId": "req_011CbGqHukbYekArCNkg2ppU",
  "type": "assistant",
  "uuid": "4e8e7c40-dfc3-48f6-b9b8-c022f70ddc6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016R8znrAcpwRtepdck21gaD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12083,
      "cache_read_input_tokens": 11841,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12083,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 237,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12083
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

_source line 10 · 2026-05-22T02:40:12.342Z_

<details><summary>↩ Tool result · `toolu_01HPRYTAH2zn3fDfuYoAJgpt`</summary>

```text
Perfect! Here's my comprehensive search report:

## Search Results

I found **one main experiment plan file** in the directory structure:

### Primary Experiment Plan File
- **Path**: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/experiment_plan.yaml`

This is the key experiment plan file for the `clkc_mech_interp` project. It contains a comprehensive research plan last updated on 2026-05-22, targeting ICLR 2027 (deadline ~2026-09-24).

### File Structure
The experiment_plan.yaml is organized into several tracks and sections:

**MVP Experiments (Completed/In-Progress):**
- `mvp_001`: Dual-model residual flow probe MVP (EN/ZH cross-lingual) - DONE
- `mvp_002`: MLP vs Linear probe comparison - DONE
- `mvp_003`: COMET translation quality validation - RUNNING

**Statistical Corrections (P0):**
- `plan_099`: Training set bootstrap asymmetry CI analysis - DONE

**Track 1: Cross-Lingual Probing (P0):**
- `plan_101`: Token overlap analysis - DONE
- `plan_102`: Third model architecture validation - PLANNED
- `plan_103`: Multi-lingual expansion (EN↔JA) - PLANNED
- `plan_104`: Layer-wise CKA/SVCCA analysis - PLANNED
- `plan_105`: COMET segmentation ablation - DONE

**Track 1 Extensions (P1):**
- `plan_106-109`: Label noise ablation, representation steering, larger dataset validation, probe weight visualization

**Track 2: SAE Feature Analysis (P1-P2):**
- `plan_201-203`: SAE conflict feature identification, language feature disentanglement, cross-lingual feature Jaccard analysis

**Track 3: Steering (P2):**
- `plan_301-303`: Monolingual→cross-lingual steering transfer, cross-lingual-specific steering, typological steering correlation

### Directory Context
The search revealed the project structure includes:
- Main project directory: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/`
- Configuration directory: `/home/ubuntu/.agent-ml-research-prod42/config/`
- Global skills directory: `/home/ubuntu/.agent-ml-research-prod42/skills/`
- State directory: `/home/ubuntu/.agent-ml-research-prod42/state/`

No other experiment plan files or `*plan*.md`, `*plan*.yaml`, or `/experiments/` directories were found beyond this main file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e8e7c40-dfc3-48f6-b9b8-c022f70ddc6c",
  "isSidechain": false,
  "promptId": "e5796808-4efb-41f2-ba25-a8da19529122",
  "type": "user",
  "uuid": "f4db3987-29bb-4d27-9a36-7325f58bbc87",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for the experiment plan file in /home/ubuntu/.agent-ml-research-prod42. Look for files named experiment_plan*, plan*, or similar YAML/MD files that contain planned experiments. Also check for any directory structure that might contain experiment definitions. Search broadly — try patterns like **/*experiment*plan*, **/*plan*.yaml, **/*plan*.md, **/experiments/*, and look in the root directory for any YAML or MD files that might contain experiment plans.",
    "agentId": "a8114d44a260c89ad",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Here's my comprehensive search report:\n\n## Search Results\n\nI found **one main experiment plan file** in the directory structure:\n\n### Primary Experiment Plan File\n- **Path**: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/experiment_plan.yaml`\n\nThis is the key experiment plan file for the `clkc_mech_interp` project. It contains a comprehensive research plan last updated on 2026-05-22, targeting ICLR 2027 (deadline ~2026-09-24).\n\n### File Structure\nThe experiment_plan.yaml is organized into several tracks and sections:\n\n**MVP Experiments (Completed/In-Progress):**\n- `mvp_001`: Dual-model residual flow probe MVP (EN/ZH cross-lingual) - DONE\n- `mvp_002`: MLP vs Linear probe comparison - DONE\n- `mvp_003`: COMET translation quality validation - RUNNING\n\n**Statistical Corrections (P0):**\n- `plan_099`: Training set bootstrap asymmetry CI analysis - DONE\n\n**Track 1: Cross-Lingual Probing (P0):**\n- `plan_101`: Token overlap analysis - DONE\n- `plan_102`: Third model architecture validation - PLANNED\n- `plan_103`: Multi-lingual expansion (EN↔JA) - PLANNED\n- `plan_104`: Layer-wise CKA/SVCCA analysis - PLANNED\n- `plan_105`: COMET segmentation ablation - DONE\n\n**Track 1 Extensions (P1):**\n- `plan_106-109`: Label noise ablation, representation steering, larger dataset validation, probe weight visualization\n\n**Track 2: SAE Feature Analysis (P1-P2):**\n- `plan_201-203`: SAE conflict feature identification, language feature disentanglement, cross-lingual feature Jaccard analysis\n\n**Track 3: Steering (P2):**\n- `plan_301-303`: Monolingual→cross-lingual steering transfer, cross-lingual-specific steering, typological steering correlation\n\n### Directory Context\nThe search revealed the project structure includes:\n- Main project directory: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/`\n- Configuration directory: `/home/ubuntu/.agent-ml-research-prod42/config/`\n- Global skills directory: `/home/ubuntu/.agent-ml-research-prod42/skills/`\n- State directory: `/home/ubuntu/.agent-ml-research-prod42/state/`\n\nNo other experiment plan files or `*plan*.md`, `*plan*.yaml`, or `/experiments/` directories were found beyond this main file."
      }
    ],
    "totalDurationMs": 19373,
    "totalTokens": 28404,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 175,
      "cache_read_input_tokens": 27583,
      "output_tokens": 642,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 175
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 642,
          "cache_read_input_tokens": 27583,
          "cache_creation_input_tokens": 175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 175,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 6,
      "bashCount": 2,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "4e8e7c40-dfc3-48f6-b9b8-c022f70ddc6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T02:40:14.755Z_

<details open><summary>🔧 Tool call — Read · `toolu_0182YaCVZ8gvwjHhLAVLMfjR`</summary>

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
  "parentUuid": "f4db3987-29bb-4d27-9a36-7325f58bbc87",
  "isSidechain": false,
  "requestId": "req_011CbGqKqPihGSyQhgEX9NQE",
  "type": "assistant",
  "uuid": "80f5198d-a072-49d9-972d-a8b548761d64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MXmf3yJJA7v7TMXymAU2vV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 859,
      "cache_read_input_tokens": 23924,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 859,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 23924,
          "cache_creation_input_tokens": 859,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 859
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

_source line 12 · 2026-05-22T02:40:14.765Z_

<details><summary>↩ Tool result · `toolu_0182YaCVZ8gvwjHhLAVLMfjR`</summary>

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
  "parentUuid": "80f5198d-a072-49d9-972d-a8b548761d64",
  "isSidechain": false,
  "promptId": "e5796808-4efb-41f2-ba25-a8da19529122",
  "type": "user",
  "uuid": "9b8eef4f-1021-4a92-9e55-eb38116e0408",
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
  "sourceToolAssistantUUID": "80f5198d-a072-49d9-972d-a8b548761d64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13 · 2026-05-22T02:40:14.803Z_

````json
{
  "parentUuid": "9b8eef4f-1021-4a92-9e55-eb38116e0408",
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
  "uuid": "faea6ea5-d09a-473e-a0ba-ce36d538651a",
  "timestamp": "2026-05-22T02:40:14.803Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：第三模型复现显著不对称 + Track 2 出初步结果，原始 framing 全线成立 核心假设：['第三模型（Mistral/Gemma）ZH→EN vs EN→ZH 不对称性显著（bootstrap CI 排除零）', '3/3 模型方向一致，≥2/3 达统计显著', 'MLP non-linearity…",
  "leafUuid": "faea6ea5-d09a-473e-a0ba-ce36d538651a",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual conflict detection mechanism in multilingual LLMs",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c"
}
```

---

### Assistant

_source line 16 · 2026-05-22T02:40:47.091Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full experiment plan and the paper framing context. Let me understand what's needed:

The user wants me to generate detailed imagined experiment results for ALL planned experiments in the experiment_plan.yaml, under the "best" tier definition. Let me go through each planned experiment:

**Planned experiments (status: planned or running):**

1. **mvp_003** - COMET translation quality validation (running)
2. **plan_102** - Third model architecture validation (planned)
3. **plan_103** - Multilingual expansion EN↔JA (planned)


4. **plan_104** - Layer-wise CKA/SVCCA (planned)
5. **plan_109** - Probe weight visualization + PCA (planned)
6. **plan_106** - Label noise ablation (planned)
7. **plan_107** - Representation steering (planned)
8. **plan_108** - Larger dataset validation (planned)
9. **plan_201** - Qwen-Scope SAE conflict feature identification (planned)
10. **plan_202** - LangFIR language feature disentanglement (planned)
11. **plan_203** - Cross-lingual feature Jaccard analysis (planned)

I need to continue through the remaining planned experiments and generate realistic "best" tier results for each one. Looking at the performance thresholds for each metric—consistency across models, accuracy ranges for within-language and cross-lingual transfer, MLP gain patterns, SAE Jaccard similarity, language pair validation, and submission readiness—I'm now mapping these constraints into the detailed YAML structure. I need to work through each experiment systematically and articulate the rationale for why the predictions should hold given the observed patterns so far. replicate Qwen's not_confounder result. In best tier, we expect this to confirm.

For **plan_102** (Third model): In best tier, the third model (let's say Gemma-2-9B-IT) shows asymmetry gap of ~7-8pp, within the [5, 12] range, statistically significant (bootstrap CI excludes zero). Within-language acc in [0.72, 0.82]. MLP gain in weak direction [3, 10]pp.

For **plan_103** (EN↔JA): Direction consistent with EN↔ZH. JA→EN > EN→JA. Asymmetry gap somewhat smaller but same direction, supporting H1.

For **plan_104** (CKA/SVCCA): Shows mid-layer EN-ZH similarity peaks, then diverges in late layers, consistent with the "Lost in Multiling" language transition picture.

For **plan_109** (PCA visualization): Clear separation in PCA space with EN and ZH conflict clusters overlapping in mid-layers. For **plan_106** (Label noise): The model degrades gracefully up to around 10% noise. For **plan_107** (Representation steering): Steering in the probe direction causally influences model output. For **plan_108** (Larger dataset): Results replicate with 2000+ samples.

Moving to the mechanistic analysis, the SAE features identify conflict patterns with Jaccard similarity above 0.15, and LangFIR successfully disentangles language from conflict features. The mid-layer Jaccard values substantially exceed late-layer values, reinforcing H1. Finally, English conflict features transfer when steering from monolingual to cross-lingual settings.

Now examining cross-lingual steering specifically—cross-lingual features outperform monolingual ones for steering effectiveness, and this effectiveness correlates with typological linguistic similarity between language pairs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faea6ea5-d09a-473e-a0ba-ce36d538651a",
  "isSidechain": false,
  "requestId": "req_011CbGqL1iL6KSBc5wN7VPXJ",
  "type": "assistant",
  "uuid": "035de8b4-5ff6-48ac-91aa-beffd32b3b92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXZ7JDEGazzxQ4rCe4tJ94",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9454,
      "cache_read_input_tokens": 24783,
      "output_tokens": 15028,
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
          "output_tokens": 15028,
          "cache_read_input_tokens": 24783,
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

_source line 17 · 2026-05-22T02:44:59.698Z_

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立：CLEAR entity-centric 冲突解决的首个机制解释。
  C2 不对称性从 "consistent trend" 升级为 "statistically robust cross-architecture phenomenon"，
  英语锚点假说（H1 变体）获三模型+多语言对支持。
  Track 2 SAE 提供 feature-level 证据补强因果叙事，部分缓解 RC8（无 intervention 的因果 claim）。
  论文定位：mechanistic interpretability + cross-lingual，双社区贡献。

imagined_experiments:
  - name: "COMET 翻译质量验证（Llama 补全）"
    plan_id: "mvp_003"
    description: "wmt22-comet-da back-translation 验证 Llama ZH 翻译质量，补完 Qwen 已有结果"
    expected_results:
      llama_test_total: 272
      llama_test_pass_rate_080: 0.22
      llama_test_mean_comet: 0.715
      llama_test_passed_mean_comet: 0.855
      llama_train_total: 1096
      llama_train_pass_rate_080: 0.24
      llama_train_mean_comet: 0.720
      llama_comet_tercile_low_acc: 0.648
      llama_comet_tercile_med_acc: 0.661
      llama_comet_tercile_high_acc: 0.632
      llama_comet_tercile_delta_high_low_pp: -1.6
      llama_comet_tercile_fisher_p: 0.82
      llama_comet_tercile_conclusion: "not_confounder"
    result_rationale: >
      Llama 的翻译管线与 Qwen 共用同一 prompt template，back-translation COMET 分布应高度相似。
      best 档要求 Llama 复现 Qwen 的 not_confounder 结论——这在机制上合理：
      冲突检测信号编码在残差流的语义层，而非表层翻译质量。
      如果翻译质量是 confounder，高 COMET 样本应有更高探针准确率，
      但 Qwen 结果已呈反向（-5.64pp），Llama 预期同样反向或无差异。
      pass rate 略高于 Qwen（22% vs 18.5%）因 Llama 的 EN 数据比例更大，
      back-translation 到 EN 的回译质量天然更好。
    tables:
      - name: "Table: COMET Tercile Ablation (Both Models)"
        columns: ["Model", "Tercile", "N", "COMET_mean", "Bal_Acc", "Delta_vs_Low"]
        rows:
          - ["Llama-3.1-8B", "Low", "91", "0.582", "64.8%", "—"]
          - ["Llama-3.1-8B", "Med", "91", "0.714", "66.1%", "+1.3pp"]
          - ["Llama-3.1-8B", "High", "90", "0.821", "63.2%", "-1.6pp"]
          - ["Qwen3-8B", "Low", "56", "0.585", "66.4%", "—"]
          - ["Qwen3-8B", "Med", "56", "0.700", "67.7%", "+1.3pp"]
          - ["Qwen3-8B", "High", "56", "0.816", "60.7%", "-5.6pp"]
    figures_description:
      - "散点图：per-sample COMET score (x) vs probe confidence (y)，两模型子图，拟合线斜率接近零或为负"
    analysis: >
      两模型一致结论：翻译质量非 confounder。这允许放宽 COMET ≥0.80 门槛，
      从而保留更多样本进入后续实验（特别是 plan_103 多语言扩展时 JA 翻译质量可能更低）。
      RC1 彻底关闭。

  - name: "第三模型架构验证（Gemma-2-9B-IT）"
    plan_id: "plan_102"
    description: "在 Gemma-2-9B-IT 上重复完整 4 方向探针实验 + bootstrap n=100 不对称性 CI"
    expected_results:
      model: "Gemma-2-9B-IT"
      en_en_bal_acc: 0.764
      zh_zh_bal_acc: 0.708
      en_zh_bal_acc: 0.647
      zh_en_bal_acc: 0.726
      asymmetry_gap_pp: 7.9
      bootstrap_ci_95: "[2.3%, 13.8%]"
      bootstrap_significant: true
      bootstrap_positive_iterations: "99/100"
      best_layer_en: 30
      best_layer_zh: 28
      best_layer_depth_ratio: 0.71
      mlp_en_zh_acc: 0.708
      mlp_gain_en_zh_pp: 6.1
      mlp_zh_en_acc: 0.739
      mlp_gain_zh_en_pp: 1.3
      permutation_test_p_en_en: "<0.001"
      permutation_test_p_zh_zh: "<0.001"
      permutation_test_p_en_zh: "<0.001"
      permutation_test_p_zh_en: "<0.001"
      token_overlap_jaccard_mean: 0.035
      token_overlap_correlation_p: 0.51
    result_rationale: >
      best 档核心要求：第三模型显著不对称 + 3/3 方向一致。
      Gemma-2-9B-IT 采用 GQA + sliding window attention，架构与 Llama（GQA）和 Qwen（GQA）有差异但同为 dense transformer。
      within-language acc ~76%/71% 落在 [0.72, 0.82] 范围内——
      Gemma 英语预训练数据占比高（Google 英语资源丰富），EN→EN 高于 Qwen/Llama 合理。
      ZH 训练数据比例低于 Qwen 但与 Llama 相当，ZH→ZH 在 Llama 附近。
      不对称性 +7.9pp 在 [5, 12] 范围中段，CI 排除零——
      这是 best 档与 mid 档的关键区别：Gemma 作为第三个 significant 模型将 C2 从
      "2/3 显著" 提升到 "3/3 显著"。
      MLP 在 EN→ZH 方向增益 +6.1pp 位于 [3, 10] 范围——
      幅度介于 Llama（~4.7pp bootstrap-corrected）和 Qwen（+2.3pp）之间，
      支持"非线性成分与跨语言对齐程度负相关"的叙事：
      Gemma ZH 对齐弱于 Qwen 但强于 Llama 的 ZH 特化程度。
      peak layer depth ~71% 介于 Llama（88%）和 Qwen（67%），
      三模型 peak 均在 mid-to-upper layers 但绝对位置有差异——
      提示冲突信号集中区域与模型的语言 transition layer 有关，非固定比例。
    tables:
      - name: "Table: Cross-Architecture Probe Results Summary"
        columns: ["Model", "EN→EN", "ZH→ZH", "EN→ZH", "ZH→EN", "Asym_gap", "CI_95", "Sig?"]
        rows:
          - ["Llama-3.1-8B", "77.1%", "71.2%", "64.1%", "71.3%", "+7.2pp", "[1.1, 13.6]", "Yes"]
          - ["Qwen3-8B", "75.3%", "71.6%", "65.0%", "72.2%", "+7.2pp", "[-1.2, 13.4]", "No (trend)"]
          - ["Gemma-2-9B-IT", "76.4%", "70.8%", "64.7%", "72.6%", "+7.9pp", "[2.3, 13.8]", "Yes"]
      - name: "Table: MLP Non-linearity Gain (EN→ZH weak direction)"
        columns: ["Model", "Linear", "MLP", "Gain_pp", "Interpretation"]
        rows:
          - ["Llama-3.1-8B", "64.1%", "68.8%", "+4.7", "Strong non-linear component"]
          - ["Qwen3-8B", "65.0%", "67.3%", "+2.3", "Weak non-linear (better ZH alignment)"]
          - ["Gemma-2-9B-IT", "64.7%", "70.8%", "+6.1", "Moderate non-linear component"]
    figures_description:
      - "三模型不对称性 forest plot：每模型一行，点估计 + 95% bootstrap CI，垂直虚线在 0pp"
      - "三模型 layer-wise probe accuracy 曲线叠加图：EN→EN 和 ZH→EN 方向，x=layer depth ratio"
    analysis: >
      三模型不对称性分别为 +7.2pp / +7.2pp / +7.9pp，效果量惊人一致（CV < 6%）。
      2/3 统计显著（Llama borderline + Gemma clear），Qwen 方向一致但 CI 含零。
      meta-analytic 角度：即使保守处理 Qwen 为 non-significant，
      三模型一致方向 + 效果量同质性本身就是强证据。
      C2 升级为 "statistically robust cross-architecture phenomenon"。
      MLP 增益的跨模型梯度（Llama 4.7 > Gemma 6.1 > Qwen 2.3）
      与各模型的中文预训练数据占比负相关——
      中文对齐越好，EN→ZH 映射越线性，非线性残差越小。

  - name: "多语言扩展 (EN↔JA)"
    plan_id: "plan_103"
    description: "EN↔JA 语言对完整探针实验，检验不对称性方向是否跨语言对一致"
    expected_results:
      model: "Qwen3-8B"
      en_en_bal_acc_ja_split: 0.748
      ja_ja_bal_acc: 0.693
      en_ja_bal_acc: 0.618
      ja_en_bal_acc: 0.681
      asymmetry_gap_ja_pp: 6.3
      bootstrap_ci_95_ja: "[0.4%, 12.5%]"
      bootstrap_significant_ja: true
      model_2: "Llama-3.1-8B"
      llama_en_ja_bal_acc: 0.601
      llama_ja_en_bal_acc: 0.668
      llama_asymmetry_gap_ja_pp: 6.7
      llama_bootstrap_ci_95_ja: "[0.8%, 13.1%]"
      llama_bootstrap_significant_ja: true
      lang_pairs_validated: 2
      h1_h2_verdict: "H1_supported"
    result_rationale: >
      best 档要求 ≥1 额外语言对方向一致（lang_pairs_validated ∈ [2,3]）。
      EN↔JA 预测方向与 EN↔ZH 相同（JA→EN > EN→JA）的原因：
      H1 英语锚点假说认为冲突信号以英语表征空间为锚点编码，
      从任何非英语语言迁移到英语都更容易（"下坡"），反之更难（"上坡"）。
      JA 不对称性略小于 ZH（6.3pp vs 7.2pp）合理：
      日语与英语的 typological distance 大于中文与英语（形态学复杂度更高、
      SOV 语序、多种书写系统），但 Qwen 的 JA 训练数据占比也较低，
      两个因素部分抵消。关键是方向一致而非幅度完全相同。
      JA 作为 CJK 系但与 ZH typologically 不同的语言——
      如果 H2（language-pair-specific）成立，JA 应呈现不同 pattern；
      方向一致强力支持 H1。
      JA within-language acc 略低于 ZH（69.3% vs 71.6%），
      因 Qwen 的 JA 训练数据少于 ZH，表征质量略弱。
    tables:
      - name: "Table: Multi-Lingual Asymmetry Comparison"
        columns: ["Model", "Lang_Pair", "X→EN", "EN→X", "Asym_gap", "CI_95", "Direction"]
        rows:
          - ["Qwen3-8B", "EN↔ZH", "72.2%", "65.0%", "+7.2pp", "[-1.2, 13.4]", "ZH→EN wins"]
          - ["Qwen3-8B", "EN↔JA", "68.1%", "61.8%", "+6.3pp", "[0.4, 12.5]", "JA→EN wins"]
          - ["Llama-3.1-8B", "EN↔ZH", "71.3%", "64.1%", "+7.2pp", "[1.1, 13.6]", "ZH→EN wins"]
          - ["Llama-3.1-8B", "EN↔JA", "66.8%", "60.1%", "+6.7pp", "[0.8, 13.1]", "JA→EN wins"]
    figures_description:
      - "2x2 子图矩阵（model x lang_pair），每个子图为 4 方向探针 accuracy bar chart + error bars"
      - "不对称性 forest plot 扩展版：4 条（2 models x 2 lang_pairs），方向全部一致"
    analysis: >
      4/4 model×lang_pair 组合不对称性方向一致（X→EN > EN→X），
      效果量在 6.3-7.9pp 范围内。这是 H1（English-anchored）的强证据：
      冲突信号以英语表征空间为锚点，X→EN 利用了"向锚点靠拢"的表征优势，
      EN→X 则需要额外的非线性映射。
      H2（language-pair-specific）预测 JA 和 ZH 应有不同 pattern——被数据否定。
      审稿人 RC4（dataset diversity）部分缓解：
      不再是"只有 EN-ZH 一个语言对"，而是"两个 typologically 不同的亚洲语言"。
      理想状态下 EN↔DE（印欧语系）也做，但 best 档 2 对已满足最低要求。

  - name: "Layer-wise CKA/SVCCA 分析"
    plan_id: "plan_104"
    description: "逐层计算 EN vs ZH 激活的 CKA 和 SVCCA，量化跨语言表征相似度的层分布"
    expected_results:
      models_analyzed: ["Llama-3.1-8B", "Qwen3-8B", "Gemma-2-9B-IT"]
      cka_peak_similarity_layer_ratio_llama: 0.55
      cka_peak_similarity_layer_ratio_qwen: 0.50
      cka_peak_similarity_layer_ratio_gemma: 0.52
      cka_mid_layer_mean: 0.82
      cka_late_layer_mean: 0.54
      cka_mid_late_drop_significant: true
      svcca_mid_layer_mean: 0.78
      svcca_late_layer_mean: 0.48
      probe_peak_vs_cka_transition_correlation: -0.71
      language_transition_layer_ratio_llama: 0.75
      language_transition_layer_ratio_qwen: 0.60
      language_transition_layer_ratio_gemma: 0.68
    result_rationale: >
      CKA/SVCCA 测量 EN 和 ZH 激活的表征几何相似度。
      best 档下预期 pattern：mid-layers 高相似度（~0.82）→ late-layers 急剧下降（~0.54）。
      这与 "Lost in Multilinguality"（Wendler et al. 2024）的发现一致：
      LLM 在 mid-layers 形成 language-agnostic 概念表征，
      late-layers 发生 language transition 准备解码。
      关键发现：probe accuracy peak 出现在 CKA 下降的"转折层"附近——
      冲突信号在 language-agnostic 和 language-specific 表征的交界处最可检测。
      这解释了为什么 ZH→EN 迁移更强：mid-layer 表征以英语为锚点，
      ZH→EN 方向"顺着"表征空间的自然结构，EN→ZH 则逆行。
      三模型 CKA 转折层位置不同（Llama ~55%, Qwen ~50%, Gemma ~52%），
      但 probe peak 与 CKA transition 的关系一致（相关 r=-0.71）。
    tables:
      - name: "Table: CKA Similarity by Layer Group"
        columns: ["Model", "Early (0-33%)", "Mid (33-67%)", "Late (67-100%)", "Mid-Late Drop"]
        rows:
          - ["Llama-3.1-8B", "0.71", "0.83", "0.52", "-0.31"]
          - ["Qwen3-8B", "0.68", "0.81", "0.56", "-0.25"]
          - ["Gemma-2-9B-IT", "0.70", "0.82", "0.53", "-0.29"]
    figures_description:
      - "三模型 CKA heatmap（layer x layer 对角线）叠加 probe accuracy 曲线，标注 transition zone"
      - "CKA/SVCCA 逐层曲线图 + probe accuracy 曲线双 y 轴叠加，标注 peak 和 transition 点"
    analysis: >
      CKA 分析为 C4（layer structure）提供量化基础，同时为 C2（asymmetry）提供机制解释：
      不对称性源于 mid-layer 表征空间的英语锚点特性。
      probe peak 与 CKA transition 的相关性（r=-0.71）提示
      冲突信号在表征空间从 language-universal 向 language-specific 转变时最显著——
      这正是冲突"需要被解决"的时刻。
      与 H1 一致：如果表征空间以英语为锚点，
      ZH/JA 样本在 mid-layer 被"翻译"为英语表征后冲突信号变得可检测，
      而英语样本到 ZH/JA 则需要额外的非线性映射来"离开"锚点。

  - name: "探针权重可视化 + PCA"
    plan_id: "plan_109"
    description: "最优层线性探针权重 PCA/t-SNE 可视化，展示冲突 vs 非冲突的跨语言表征结构"
    expected_results:
      pca_variance_explained_2d: 0.38
      conflict_nonconflict_silhouette_en: 0.42
      conflict_nonconflict_silhouette_zh: 0.35
      cross_lingual_overlap_mid_layer: "high"
      cross_lingual_overlap_late_layer: "low"
      en_zh_conflict_centroid_cosine_mid: 0.78
      en_zh_conflict_centroid_cosine_late: 0.51
    result_rationale: >
      PCA 可视化在 best 档下应呈现清晰的定性 pattern：
      mid-layer 中 EN 和 ZH 的冲突样本在 PCA 空间中高度重叠（centroid cosine ~0.78），
      支持 H1 的 language-universal 冲突检测假说。
      late-layer 中两语言聚类开始分离（cosine 降至 ~0.51），
      对应 language transition 引入的 language-specific 成分。
      silhouette score EN > ZH（0.42 vs 0.35）反映英语探针分离度更好，
      与 EN→EN > ZH→ZH 的准确率差异一致。
      PCA 只解释 ~38% 方差——冲突信号不是低维线性结构，
      但方向性清晰可见，为论文提供直观的 Figure 1 素材。
    tables: []
    figures_description:
      - "2x3 PCA 子图矩阵（mid-layer vs late-layer x 3 models），颜色=conflict/non-conflict，形状=EN/ZH，椭圆标注 95% CI"
      - "t-SNE 补充图：mid-layer 全样本，4 类（EN-conflict, EN-non, ZH-conflict, ZH-non）颜色区分"
    analysis: >
      可视化为 mechanistic interpretability claim 提供必要的定性证据——
      审稿人需要"看到"冲突信号，而非仅看 accuracy 数字。
      mid-layer 重叠 + late-layer 分离的 pattern 与 CKA 分析（plan_104）互洽，
      构成完整的层级叙事。

  - name: "Label noise ablation"
    plan_id: "plan_106"
    description: "系统性注入 5%/10%/15%/20% label noise，测量 probe accuracy 下降曲线"
    expected_results:
      noise_0_acc: 0.771
      noise_5_acc: 0.754
      noise_10_acc: 0.731
      noise_15_acc: 0.702
      noise_20_acc: 0.668
      degradation_slope_per_5pp: -2.6
      robustness_threshold_pp: 12
      cross_lingual_noise_sensitivity_en_zh: 1.3
      cross_lingual_noise_sensitivity_zh_en: 1.1
    result_rationale: >
      线性探针对 label noise 的鲁棒性直接关系到 verification pipeline 的可靠性。
      best 档下探针应表现出合理的渐进退化（非突变），
      因为残差流中的冲突信号是分布式编码的，少量 label noise 不会改变决策边界方向，
      只会使其偏移。~2.6pp/5% noise 的斜率表明探针在 10% noise 下仍保持 >73%，
      考虑到 verification pipeline 的 label error rate 预估 <5%，
      这提供了充分的安全裕度。
      跨语言方向的 noise sensitivity 差异小（1.3x vs 1.1x）
      表明 noise robustness 是探针的固有属性而非语言依赖的。
    tables:
      - name: "Table: Label Noise Robustness (Llama EN→EN)"
        columns: ["Noise_Level", "Bal_Acc", "Delta_vs_0%", "Relative_Drop"]
        rows:
          - ["0%", "77.1%", "—", "—"]
          - ["5%", "75.4%", "-1.7pp", "2.2%"]
          - ["10%", "73.1%", "-4.0pp", "5.2%"]
          - ["15%", "70.2%", "-6.9pp", "8.9%"]
          - ["20%", "66.8%", "-10.3pp", "13.4%"]
    figures_description:
      - "Noise level (x) vs balanced accuracy (y) 曲线图，4 方向 x 3 模型叠加，error bars from 5-fold"
    analysis: >
      探针在 ≤10% noise 下保持 >73% accuracy，
      验证 pipeline label quality 的 error tolerance 充裕。
      此实验为 C1 的 robustness 声明提供支持，是补充性结果而非核心发现。
      建议放入 Appendix 而非主文。

  - name: "Representation steering（干预实验）"
    plan_id: "plan_107"
    description: "用探针方向作为 steering vector 干预残差流中的冲突信号，测量模型输出变化"
    expected_results:
      llama_monolingual_en_flip_rate: 0.312
      llama_monolingual_zh_flip_rate: 0.268
      llama_cross_lingual_zh_en_flip_rate: 0.243
      llama_cross_lingual_en_zh_flip_rate: 0.178
      llama_flip_asymmetry_cross: 0.065
      qwen_monolingual_en_flip_rate: 0.289
      qwen_cross_lingual_zh_en_flip_rate: 0.221
      qwen_cross_lingual_en_zh_flip_rate: 0.192
      steering_alpha_optimal: 2.5
      steering_coherence_preserved_rate: 0.91
      parametric_to_contextual_shift_significant: true
    result_rationale: >
      best 档下 representation steering 应产生有意义的输出翻转——
      这是 RC8（因果 claims without intervention）的直接缓解。
      探针方向即为冲突信号的线性近似，沿该方向干预残差流
      应推动模型从 parametric answer 翻转到 contextual answer（或反之）。
      monolingual flip rate ~30% 是合理的——
      不是所有样本都能被线性 steering 翻转（非线性成分存在），
      但 30% 显著高于随机翻转基线（~5%）。
      cross-lingual flip rate 低于 monolingual（ZH→EN 24.3% vs EN 31.2%），
      且呈现与探针迁移相同的不对称性（ZH→EN 24.3% > EN→ZH 17.8%），
      从因果方向确认 C2：不对称性不仅是探针检测的统计 pattern，
      而是残差流中冲突信号编码的因果结构。
      coherence preserved rate 91% 表明 steering 没有破坏模型的一般生成质量。
    tables:
      - name: "Table: Steering Flip Rates by Direction"
        columns: ["Model", "Direction", "Flip_Rate", "Random_Baseline", "Lift"]
        rows:
          - ["Llama", "EN (mono)", "31.2%", "4.8%", "6.5x"]
          - ["Llama", "ZH (mono)", "26.8%", "5.1%", "5.3x"]
          - ["Llama", "ZH→EN (cross)", "24.3%", "4.9%", "5.0x"]
          - ["Llama", "EN→ZH (cross)", "17.8%", "5.2%", "3.4x"]
          - ["Qwen", "EN (mono)", "28.9%", "4.6%", "6.3x"]
          - ["Qwen", "ZH→EN (cross)", "22.1%", "4.7%", "4.7x"]
          - ["Qwen", "EN→ZH (cross)", "19.2%", "5.0%", "3.8x"]
    figures_description:
      - "Steering alpha sweep 曲线（alpha x flip_rate），标注 optimal alpha 和 coherence collapse threshold"
      - "Flip rate asymmetry bar chart：monolingual vs cross-lingual x 方向，error bars from bootstrap"
    analysis: >
      Steering 实验是 best 档的关键差异化实验——
      即使 Track 3 SAE steering 未完成，probe-based steering 已提供因果证据。
      flip rate 不对称性（ZH→EN > EN→ZH）与探针迁移不对称性方向一致，
      从相关性→因果性升级。
      审稿人如果质疑 "探针只证明信号可检测"（RC8），
      steering 实验的回应是："干预该信号确实改变了冲突解决行为"。
      放入主文 Section 4.3 作为 C2 不对称性的因果证据。

  - name: "更大数据集验证"
    plan_id: "plan_108"
    description: "扩大 ConflictQA 采样至 2000+ samples per model，验证结论稳定性"
    expected_results:
      sample_size_per_model: 2200
      llama_en_en_2k: 0.775
      llama_asymmetry_gap_2k_pp: 7.4
      llama_bootstrap_ci_2k: "[3.1%, 11.8%]"
      qwen_en_en_2k: 0.758
      qwen_asymmetry_gap_2k_pp: 7.0
      qwen_bootstrap_ci_2k: "[1.8%, 12.3%]"
      qwen_2k_significant: true
      ci_width_reduction_pct: 28
    result_rationale: >
      数据量翻倍后 CI 宽度应缩减约 1/√2 ≈ 28%。
      best 档下关键收益：Qwen 的 CI 从 [-1.2%, 13.4%] 收窄至 [1.8%, 12.3%]，
      终于排除零——即 Qwen 也达到统计显著。
      这是 best 档 "3/3 显著" 的另一条路径（与 Gemma 第三模型互补）：
      即使不加第三模型，Qwen 扩大样本后也能独立显著。
      点估计基本不变（7.0pp vs 7.18pp），表明效果量是稳定的，
      之前 Qwen 不显著纯粹是 power 不足而非效果不存在。
    tables:
      - name: "Table: Sample Size Scaling Effect on CI"
        columns: ["Model", "N", "Asym_gap", "CI_95", "Significant?"]
        rows:
          - ["Llama", "~1000", "+7.2pp", "[1.1, 13.6]", "Yes"]
          - ["Llama", "~2200", "+7.4pp", "[3.1, 11.8]", "Yes"]
          - ["Qwen", "~1000", "+7.2pp", "[-1.2, 13.4]", "No"]
          - ["Qwen", "~2200", "+7.0pp", "[1.8, 12.3]", "Yes"]
    figures_description:
      - "Power analysis 曲线：sample size (x) vs CI width (y)，标注 'significance threshold' 水平线"
    analysis: >
      数据扩展是 low-risk high-value 实验——不可能改变结论方向，
      只会收窄 CI。best 档下 Qwen 达显著是锦上添花（因为 Gemma 已提供第三模型），
      建议放入 Appendix 或 robustness 小节。

  - name: "Qwen-Scope SAE 冲突特征识别"
    plan_id: "plan_201"
    description: "用 Qwen-Scope 预训练 SAE 在 Qwen3-8B-Base 上识别冲突相关的稀疏特征"
    expected_results:
      sae_model: "Qwen3-8B-Base"
      sae_source: "Qwen-Scope (pre-trained)"
      format_adaptation: "cloze/completion (base model compatible)"
      total_features_analyzed: 65536
      conflict_candidate_features_mi_top: 128
      conflict_features_after_filtering: 47
      feature_sparsity_mean: 0.034
      feature_activation_conflict_vs_nonconflict_auroc: 0.81
      en_conflict_features_count: 38
      zh_conflict_features_count: 31
      shared_conflict_features_count: 18
      raw_jaccard_all_layers: 0.22
      mid_layer_jaccard: 0.28
      late_layer_jaccard: 0.12
      language_identity_feature_overlap: 0.03
    result_rationale: >
      best 档要求 SAE 在 Qwen-Scope 上识别出跨语言共享 conflict feature（Jaccard > 0.15）。
      Qwen-Scope 的 SAE 在 Qwen3-8B-Base 上预训练，特征空间已学到有意义的 monosemantic 分解。
      conflict vs non-conflict 的 mutual-information feature selection（SpARE 方法）
      应能从 65K 特征中筛选出 ~128 个 candidate，进一步过滤到 ~47 个 robust 特征。
      38 个 EN conflict features 和 31 个 ZH conflict features 中有 18 个共享（Jaccard ~0.22），
      在 [0.15, 0.35] 范围中段。
      mid-layer Jaccard 0.28 显著高于 late-layer 0.12——
      这是 H1 的 SAE-level 证据：mid-layer 冲突特征跨语言共享度高，
      late-layer 语言分化后共享度下降。
      language-identity feature overlap 仅 3% 表明 conflict features 不是 language features 的子集。
      AUROC 0.81 表明 SAE 特征可以高质量区分冲突/非冲突样本，
      与探针 accuracy ~75% 在同一水平（不同指标不直接可比但数量级一致）。
    tables:
      - name: "Table: SAE Conflict Feature Summary"
        columns: ["Category", "Count", "Sparsity", "AUROC"]
        rows:
          - ["EN-specific conflict", "20", "0.031", "0.79"]
          - ["ZH-specific conflict", "13", "0.038", "0.76"]
          - ["Cross-lingual shared", "18", "0.033", "0.84"]
          - ["Language-identity (control)", "42", "0.025", "0.52"]
    figures_description:
      - "SAE 特征激活 heatmap：top-47 conflict features x 样本（按 EN-conflict/EN-non/ZH-conflict/ZH-non 排列）"
      - "Venn diagram：EN conflict features vs ZH conflict features，标注 Jaccard"
    analysis: >
      Track 2 初步结果成立——SAE 提供了 feature-level 的冲突编码证据。
      shared conflict features 的存在直接支持 H1（language-universal detection），
      mid > late layer Jaccard 差异支持"冲突信号在 mid-layer 跨语言共享、late-layer 分化"的叙事。
      这部分缓解 RC8：SAE 特征激活模式提供了超越线性探针的 interpretability 证据，
      虽然不等同于 causal intervention，但结合 plan_107 的 steering 实验，
      形成 "探针检测 → SAE 分解 → steering 干预" 的三层证据链。

  - name: "LangFIR 语言特征解耦"
    plan_id: "plan_202"
    description: "用 LangFIR random-token filtering 识别 language-identity 特征，从冲突特征中排除"
    expected_results:
      language_identity_features_identified: 42
      language_features_early_layer_concentration: 0.68
      conflict_features_mid_layer_concentration: 0.61
      overlap_conflict_language: 2
      overlap_rate: 0.043
      conflict_features_after_deconfounding: 45
      jaccard_change_after_deconfounding: "+0.02"
      layer_distribution_separation_p: 0.003
    result_rationale: >
      LangFIR 通过 random-token filtering 识别在所有 token 上一致激活的 language-identity 特征。
      best 档下预期 42 个 language features 主要集中在 early layers（68%），
      而 conflict features 集中在 mid layers（61%）——两类特征的层分布显著不同（p=0.003）。
      仅 2 个 overlap（overlap rate 4.3%）表明 conflict 不是 language 的子集，
      从 SAE feature 层面证明冲突检测是语义级别的判断，而非语言识别的副产品。
      deconfounding 后 Jaccard 轻微上升（+0.02），因为移除 language-contaminated 特征
      纯化了 conflict feature 集合。
    tables:
      - name: "Table: Feature Type Layer Distribution"
        columns: ["Feature_Type", "Early (0-33%)", "Mid (33-67%)", "Late (67-100%)", "Total"]
        rows:
          - ["Language-identity", "29 (69%)", "9 (21%)", "4 (10%)", "42"]
          - ["Conflict (shared)", "2 (11%)", "11 (61%)", "5 (28%)", "18"]
          - ["Conflict (EN-only)", "1 (5%)", "10 (50%)", "9 (45%)", "20"]
          - ["Conflict (ZH-only)", "1 (8%)", "7 (54%)", "5 (38%)", "13"]
    figures_description:
      - "层分布对比直方图：language-identity features vs conflict features 的 layer histogram 叠加"
    analysis: >
      LangFIR 控制实验为 C5 提供关键的 confound 排除：
      冲突信号不是语言信号的 epiphenomenon。
      层分布分离（early vs mid）与 plan_104 的 CKA 分析互洽——
      early layers 做语言识别，mid layers 做语义/冲突判断。

  - name: "Cross-lingual feature Jaccard 分析"
    plan_id: "plan_203"
    description: "mid-layer vs late-layer conflict feature 跨语言 Jaccard 对比，检验 H1 vs H2"
    expected_results:
      mid_layer_jaccard: 0.28
      late_layer_jaccard: 0.12
      jaccard_difference: 0.16
      paired_permutation_test_p: 0.008
      h1_vs_h2_verdict: "H1_supported"
      per_layer_jaccard_peak_ratio: 0.48
      per_layer_jaccard_trough_ratio: 0.88
    result_rationale: >
      H1 预测 mid-layer Jaccard >> late-layer Jaccard，
      H2 预测无显著差异或 mid < late。
      best 档下 mid 0.28 vs late 0.12，差异 0.16，permutation test p=0.008 < 0.05。
      这是 H1 的定量确认：冲突特征在 mid-layers 跨语言高度共享，
      在 late-layers（language transition 后）显著分化。
      Jaccard peak 在 ~48% depth（mid-layer），trough 在 ~88% depth（late-layer），
      与 CKA transition zone（plan_104）和 probe peak（plan_102）时间线吻合。
      三条独立证据线（CKA 表征相似度、probe accuracy、SAE feature Jaccard）
      收敛在相同的层级叙事上，大幅增强可信度。
    tables:
      - name: "Table: Layer-Group Jaccard Summary"
        columns: ["Layer_Group", "EN_features", "ZH_features", "Shared", "Jaccard", "95% CI"]
        rows:
          - ["Early (0-33%)", "3", "3", "1", "0.20", "[0.04, 0.41]"]
          - ["Mid (33-67%)", "21", "18", "8", "0.28", "[0.16, 0.42]"]
          - ["Late (67-100%)", "14", "10", "3", "0.12", "[0.03, 0.24]"]
    figures_description:
      - "逐层 Jaccard 曲线 + 95% permutation CI 带，标注 H1/H2 预测区间"
      - "Mid vs Late Jaccard 散点图（每层一个点），对角线上方=H1，下方=H2"
    analysis: >
      Jaccard 分析是 H1 vs H2 检验的最直接证据。
      p=0.008 在 0.05 显著性水平下 comfortably significant。
      结合 plan_104（CKA 层分布）和 plan_109（PCA 可视化），
      三条证据线一致支持 H1：冲突信号以英语为锚点在 mid-layer 跨语言共享编码。
      这是论文 Discussion 部分 H1 vs H2 resolution 的核心数据。

  - name: "Monolingual→cross-lingual steering transfer"
    plan_id: "plan_301"
    description: "用 SpARE 英语冲突 SAE 特征做 cross-lingual steering，测量跨语言有效性"
    expected_results:
      en_monolingual_em_c: 0.42
      en_monolingual_em_m: 0.31
      en_monolingual_flip_rate: 0.35
      zh_cross_lingual_em_c: 0.29
      zh_cross_lingual_em_m: 0.22
      zh_cross_lingual_flip_rate: 0.24
      transfer_efficiency: 0.69
      steering_asymmetry_en_to_zh: 0.24
      steering_asymmetry_zh_to_en: 0.31
      steering_asymmetry_gap: 0.07
      coherence_preserved_cross: 0.87
    result_rationale: >
      SpARE 已在英语 monolingual 场景证明 SAE steering 对知识冲突有效。
      best 档下 cross-lingual transfer efficiency ~69%（跨语言 flip rate / monolingual flip rate），
      表明英语冲突特征包含约 70% 的跨语言可迁移信号。
      30% 的 transfer loss 对应 late-layer language-specific 成分（与 Jaccard 分析一致）。
      steering asymmetry（EN→ZH 0.24 < ZH→EN 0.31）再次复现探针和 probe steering 的不对称方向，
      从 SAE feature 干预层面第三次确认 C2。
      coherence 87% 略低于 probe steering 的 91%——
      SAE feature steering 更 targeted 但也更 brittle（fewer degrees of freedom）。
    tables:
      - name: "Table: SAE Steering Cross-Lingual Transfer"
        columns: ["Condition", "EM_C", "EM_M", "Flip_Rate", "Coherence"]
        rows:
          - ["EN mono (baseline)", "0.42", "0.31", "35.0%", "0.93"]
          - ["EN→ZH (cross)", "0.29", "0.22", "24.0%", "0.87"]
          - ["ZH→EN (cross)", "0.34", "0.26", "31.0%", "0.89"]
          - ["Random features (control)", "0.05", "0.04", "5.2%", "0.94"]
    figures_description:
      - "Steering 效果对比 bar chart：monolingual vs cross-lingual（两个方向），+ random control"
      - "Transfer efficiency vs layer depth 曲线：不同层 steering 的跨语言迁移效率"
    analysis: >
      SAE steering 提供了最直接的因果证据——
      操控特定 SAE 特征改变了跨语言冲突解决行为。
      transfer efficiency 69% 与 Jaccard 28% 的 scale 差异
      是因为即使非 shared features 也可能有部分跨语言效应。
      这是 Track 3 的核心贡献，结合 Track 1 probing + Track 2 SAE 分析，
      构成完整的 "检测→分解→干预" 三轨证据。

  - name: "Cross-lingual-specific steering"
    plan_id: "plan_302"
    description: "用 Track 2 跨语言特有特征构建 steering vectors，对比 monolingual features 效果"
    expected_results:
      shared_feature_steering_flip_rate: 0.28
      en_only_feature_steering_flip_rate_on_zh: 0.11
      zh_only_feature_steering_flip_rate_on_en: 0.09
      shared_vs_specific_lift: 2.7
      combined_steering_flip_rate: 0.33
      combined_vs_shared_only_lift: 1.18
    result_rationale: >
      如果 H1 成立，shared features 的 cross-lingual steering 效果应显著优于 language-specific features。
      best 档下 shared feature steering 0.28 vs specific features ~0.10，lift 2.7x——
      强力支持冲突信号的跨语言共享编码假说。
      combined steering（shared + specific）仅比 shared-only 提升 18%，
      表明 language-specific features 的增量贡献有限，
      冲突解决的核心信号已被 shared features 捕获。
    tables:
      - name: "Table: Feature Type Steering Comparison"
        columns: ["Feature_Set", "Target_Lang", "Flip_Rate", "vs_Shared"]
        rows:
          - ["Shared (18 features)", "ZH", "28.0%", "1.0x"]
          - ["EN-only (20 features)", "ZH", "11.0%", "0.39x"]
          - ["ZH-only (13 features)", "EN", "9.0%", "0.32x"]
          - ["Combined (all 51)", "ZH", "33.0%", "1.18x"]
    figures_description:
      - "Feature-set ablation bar chart：4 条件 x flip rate，标注显著性星号"
    analysis: >
      Feature-set ablation 是 H1 最精细的因果检验：
      shared features 包含绝大部分跨语言 steering 能力，
      language-specific features 贡献边际，combined 收益递减。
      这与"冲突检测是 language-universal 的，resolution 才是 language-specific 的"叙事完全一致。

  - name: "Typological steering correlation"
    plan_id: "plan_303"
    description: "测试 steering 有效性与 CLEAR linguistic similarity metric 的相关性"
    expected_results:
      lang_pairs_tested: ["EN↔ZH", "EN↔JA"]
      steering_effectiveness_en_zh: 0.28
      steering_effectiveness_en_ja: 0.23
      clear_similarity_en_zh: 0.72
      clear_similarity_en_ja: 0.58
      correlation_direction: "positive"
      note: "仅 2 个语言对，无法计算有意义的相关系数，仅报告方向一致性"
    result_rationale: >
      best 档下 lang_pairs_validated = 2，只有 EN↔ZH 和 EN↔JA 两对数据点。
      两个点不足以计算 Pearson r，但方向一致性有意义：
      CLEAR similarity 更高的 EN↔ZH（0.72）steering 效果更好（0.28 > 0.23），
      与 linguistic similarity → conflict resolution 的因果链方向一致。
      这是 suggestive evidence 而非 definitive proof——
      论文中应诚实限定为 "consistent with the hypothesis, 
      pending validation with additional language pairs"。
      best 档的叙事不依赖此实验的强结论，而是用它作为 future work 的 pilot data。
    tables:
      - name: "Table: Steering vs Linguistic Similarity"
        columns: ["Lang_Pair", "CLEAR_Similarity", "Steering_Flip_Rate", "Probe_Asymmetry"]
        rows:
          - ["EN↔ZH", "0.72", "28.0%", "+7.2pp"]
          - ["EN↔JA", "0.58", "23.0%", "+6.3pp"]
    figures_description:
      - "散点图（仅 2 点 + 趋势线虚线）：CLEAR similarity (x) vs steering flip rate (y)，标注 'n=2, directional only'"
    analysis: >
      此实验在 best 档下只能提供方向性暗示。
      论文定位为 Discussion 段落而非独立 claim，
      明确标注 "preliminary, n=2" 并指向 future work（5+ 语言对验证）。
      审稿人不会因 n=2 的相关分析扣分——前提是作者不 overclaim。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "035de8b4-5ff6-48ac-91aa-beffd32b3b92",
  "isSidechain": false,
  "requestId": "req_011CbGqL1iL6KSBc5wN7VPXJ",
  "type": "assistant",
  "uuid": "4998f9dd-edd0-4efe-bc2a-ee3e46e84ec0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXZ7JDEGazzxQ4rCe4tJ94",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9454,
      "cache_read_input_tokens": 24783,
      "output_tokens": 15028,
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
          "output_tokens": 15028,
          "cache_read_input_tokens": 24783,
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：第三模型复现显著不对称 + Track 2 出初步结果，原始 framing 全线成立 核心假设：['第三模型（Mistral/Gemma）ZH→EN vs EN→ZH 不对称性显著（bootstrap CI 排除零）', '3/3 模型方向一致，≥2/3 达统计显著', 'MLP non-linearity…",
  "leafUuid": "4998f9dd-edd0-4efe-bc2a-ee3e46e84ec0",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual conflict detection mechanism in multilingual LLMs",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：第三模型复现显著不对称 + Track 2 出初步结果，原始 framing 全线成立 核心假设：['第三模型（Mistral/Gemma）ZH→EN vs EN→ZH 不对称性显著（bootstrap CI 排除零）', '3/3 模型方向一致，≥2/3 达统计显著', 'MLP non-linearity…",
  "leafUuid": "4998f9dd-edd0-4efe-bc2a-ee3e46e84ec0",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual conflict detection mechanism in multilingual LLMs",
  "sessionId": "e2f5f01b-c87b-4fdd-9bed-adef3a97350c"
}
```

---
