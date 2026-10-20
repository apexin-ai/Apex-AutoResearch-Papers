# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：第三模型方向一致但未显著，仅 Track 1，claims 需降强度但核心叙事可维持 核心假设：['第三模型不对称方向一致（ZH→EN > EN→Z

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-2/76117c84-22e3-4279-a268-ccb60fa619d7.jsonl`
- **Structured JSON:** [`870f77ce7827491f28f3.json`](../../sessions/87/870f77ce7827491f28f3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T02:45:02.562Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T02:45:02.562Z",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：第三模型方向一致但未显著，仅 Track 1，claims 需降强度但核心叙事可维持\n核心假设：['第三模型不对称方向一致（ZH→EN > EN→ZH）但 CI 含零', '3/3 方向一致，仅 1/3（Llama）达统计显著', 'effect size 跨模型稳定（±2pp 内），强 consistency argument', 'Llama COMET ablation 复现 not_confounder', 'Track 2 SAE 未完成或结果 noisy（Jaccard < 0.10）', '额外语言对仅 1 对，方向一致但样本量不足以单独显著']\n关键指标范围：{'third_model_asymmetry_gap_pp': [2.0, 7.0], 'significant_asymmetry_models_of_3': [1, 1], 'consistent_direction_models_of_3': [3, 3], 'third_model_within_lang_acc': [0.68, 0.77], 'cross_lingual_transfer_acc_range': [0.6, 0.72], 'mlp_gain_weak_direction_pp_third_model': [1.0, 5.0], 'sae_cross_lingual_jaccard_mid_layer': [0.0, 0.1], 'lang_pairs_validated': [1, 2], 'tracks_submission_ready': [1, 1]}\n叙事方向：C2 从 \"significant asymmetry\" 调整为 \"remarkably consistent effect size across architectures  (7.2±0.5pp) despite varying statistical power\"——强调 effect size stability 而非 p-value。 引用 Cumming (2014) \"new statistics\" 框架，effect size + CI 报告优于 NHST。 C1（detectability）升级为主 claim，C2 降为 strong supporting evidence。 Track 1 only 的贡献度靠深度弥补：layer-wise 分析 + confound exclusion pipeline  (token overlap + COMET ablation) 作为方法论贡献。RC8（因果 claim）明确限定为  \"correlational evidence consistent with H1\"，将 causal verification 列为 future work。 论文定位：phenomenon characterization + methodology，仍 ICLR-viable 但需  supplementary experiments 充实 appendix（更多 ablation、error analysis）。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: clkc_mech_interp\nfocus: 重点评估：1) C2 不对称性 claim 在 Llama borderline 显著 + Qwen 不显著的情况下能否撑住；2) 只有 Track 1 probing 无 Track 2/3 SAE+steering 时论文贡献强度是否足够 ICLR；3) back-translation COMET 低但 ablation 排除 confounder 的 framing 是否说服审稿人\n\n## paper_framing.md\n\n# Paper Framing — clkc_mech_interp\n\n> 最后更新: 2026-05-22 | 目标: ICLR 2027 (DDL ~2026-09-24)\n\n## Core Insight\n\n多语言 LLM 中，跨语言知识冲突的检测信号可在残差流中被线性探针检测，且跨语言迁移呈现**方向性不对称**（ZH→EN >> EN→ZH ~7.2pp），该不对称性跨架构高度一致（Llama-3.1-8B 与 Qwen3-8B）。这为 CLEAR (Zhao et al. 2026) 发现的 \"entity-centric factual conflicts 中 linguistic affinity 决定冲突解决\" 提供了首个**机制层面的解释**。\n\n**注意**: CLEAR 的发现是 task-dependent 的——entity-centric factual conflicts 由 linguistic affinity 主导，reasoning-intensive tasks 由 resource abundance 主导。我们使用 ConflictQA（entity-centric），引用 CLEAR 时必须限定为 entity-centric 场景。\n\n## Narrative Structure\n\n**现象驱动的机制解释**（非 \"applying X to Y\"）：\n\n1. **Phenomenon**: CLEAR 发现在 entity-centric factual conflicts 中，linguistic affinity（而非 resource abundance）决定跨语言冲突解决，但未提供机制解释\n2. **Mechanistic question**: 冲突信号在模型内部如何编码？是 language-universal 还是 language-specific？为什么 similarity 起决定作用？\n3. **Our answer**: 通过残差流探针、SAE 特征分析、激活干预三条互补分析轨道，揭示冲突检测信号的跨语言结构——是否共享、在哪些层出现、能否用于干预\n\n**Secondary framing**: SAE-based mechanistic interpretability 工具在跨语言条件下的 stress test——probing / SAE / steering 三种工具的跨语言适用性边界\n\n## Competing Hypotheses (pre-registered)\n\n**H1 — English-anchored universal detection**:\n冲突检测信号本身是 language-independent 的（\"是否存在冲突\" 是语言无关判断），编码在 mid-layer 共享表征空间中。final-layer language transition 引入 similarity-dependent 干扰，影响 resolution 但不影响 detection。\n- 预测: mid-layer conflict feature 跨语言 Jaccard >> late-layer Jaccard (paired permutation test p < 0.05)\n- 预测: 英语探针跨语言迁移更强（英语作为训练数据主导语言，表征空间以英语为锚点）\n\n**H2 — Language-pair-specific encoding**:\n冲突特征从 mid-layer 起即为 language-pair-specific 的，linguistic distance 直接编码在冲突表征中。\n- 预测: mid-layer 和 late-layer Jaccard 无显著差异，或 mid < late\n- 预测: 探针迁移准确率与语言对 typological distance 强相关\n\n**MVP 证据倾向**:\n当前双模型结果倾向 **H1 的变体**——ZH→EN 迁移（71-72%）显著强于 EN→ZH（64-65%），暗示冲突信号以英语表征空间为锚点编码。非线性成分（MLP EN→ZH +9.2pp vs linear）提示 EN→ZH 方向的跨语言映射更复杂。\n\n## Core Claims\n\n### Claim 1: Cross-lingual conflict detectability\n**Statement**: 跨语言知识冲突信号可在残差流中被线性探针检测，准确率显著高于随机基线。\n**Evidence needed**:\n- ≥2 model architectures 的 within-language probe acc > 70% (balanced) ✅ (Llama 77.1%, Qwen 75.3%)\n- Permutation test p < 0.001 ✅ (all directions)\n- Cross-lingual transfer acc > chance (50%) with statistical significance ✅ (all directions 64-72%)\n**Status**: MVP 已验证 ✅\n\n### Claim 2: Asymmetric cross-lingual transfer\n**Statement**: 跨语言探针迁移呈方向一致的不对称：ZH→EN 迁移强于 EN→ZH（~7.2pp），效果量跨架构高度一致（Llama 显著，Qwen 方向一致但未达显著）。\n**Evidence needed**:\n- Bootstrap CI for asymmetry gap (corrected, plan_099 ✅):\n  - Llama: +7.22pp, CI [1.1%, 13.6%] — 排除零但 borderline ✅\n  - Qwen: +7.18pp, CI [-1.2%, 13.4%] — 含零，方向一致 ⚠️\n- ≥2 models show consistent effect size ✅ (7.22pp vs 7.18pp)\n- Token overlap analysis 排除词汇重叠驱动的虚假迁移 ✅ (plan_101 完成: per-sample Jaccard 3-4%, Qwen 无相关 p>0.4, Llama 显著负相关 r=-0.15 p=0.012 — RC2 排除)\n- ≥1 additional model architecture 验证跨架构一致性 ❌ (planned P0)\n**Status**: 初步验证 ⚠️ (需补 token overlap + 第三模型)\n\n### Claim 3: Direction-dependent non-linear components\n**Statement**: 跨语言冲突信号的弱迁移方向（EN→ZH）包含方向依赖的非线性成分，MLP 探针在该方向提升最大。跨架构一致方向但幅度不同（Llama +9.2pp single-seed / ~+4.7pp bootstrap-corrected, Qwen +2.3pp），暗示非线性成分与模型的跨语言对齐程度相关。\n**Evidence needed**:\n- MLP vs linear probe comparison on ≥2 models ✅ (both show EN→ZH direction gains)\n- MLP 不使用 test set 做 early stopping ✅ (已修复)\n- 控制实验排除 MLP 过拟合 ❌ (需 train/test accuracy gap 分析)\n- 解释跨架构幅度差异 (Llama 4x > Qwen) ❌ (可能与 Qwen 更强的跨语言对齐有关——ZH 训练数据占比更高)\n**Status**: 初步验证 ⚠️ (方向一致但幅度差异需解释)\n\n### Claim 4: Layer-wise conflict signal structure\n**Statement**: 冲突信号在 mid-to-upper layers 集中，峰值层在不同模型架构中占比一致（Llama ~88% depth, Qwen ~67% depth 有差异——需更多模型确认 pattern）。\n**Evidence needed**:\n- Layer-wise probe accuracy curves for ≥3 models ❌\n- Layer-wise CKA/SVCCA 量化 EN vs ZH 表征相似度 ❌\n- 与 \"Lost in Multilinguality\" 的 language transition 层对比 ❌\n**Status**: 未验证 ❌\n\n### Claim 5: Cross-lingual SAE conflict features (Track 2)\n**Statement**: SAE 特征空间中存在跨语言共享的冲突编码特征，可与 language-identity 特征解耦。\n**Evidence needed**:\n- Qwen-Scope SAE 特征分析 on Qwen3-8B-Base ❌\n- LangFIR random-token filtering 控制 ❌\n- Cross-lingual feature Jaccard 分析 ❌\n**Status**: 未开始 ❌\n\n### Claim 6: Cross-lingual conflict steering (Track 3)\n**Statement**: 通过 SAE 特征干预可以定向操控跨语言冲突解决行为。\n**Evidence needed**:\n- SpARE 框架跨语言扩展 ❌\n- Monolingual → cross-lingual steering transfer ❌\n- Steering effectiveness vs linguistic distance correlation ❌\n**Status**: 未开始 ❌ (依赖 Track 2)\n\n## Anticipated Reviewer Concerns\n\n### RC1: Translation quality confound [RESOLVED ✅]\n**Concern**: 中文翻译质量差可能导致虚假的冲突信号或迁移失败\n**Result**: Plan_105 COMET tercile ablation 证明翻译质量非 confounder。Qwen test: Low COMET (mean 0.585) → 66.35% acc, High COMET (mean 0.816) → 60.71% acc, delta=-5.64pp (反向), Fisher p=0.695。冲突信号检测不依赖翻译质量。Back-translation COMET ≥0.80 阈值过严（两步翻译天然拉低），但 ablation 实证排除了翻译质量 confound。\n**Remaining**: Llama test COMET 完成后重复此分析确认一致性。\n\n### RC2: Token overlap confound [RESOLVED ✅]\n**Concern**: 跨语言迁移可能由 EN-ZH 共享 token（数字、专有名词、标点）驱动\n**Result**: Per-sample Jaccard 仅 3-4%（type-level 10-15% 被膨胀）。Qwen 无相关 (p>0.4)，Llama 显著负相关 (r=-0.15, p=0.012, tercile Δ=-23.9pp)。高 overlap 反而降低准确率，方向与 RC2 相反。**共享 token 不驱动跨语言迁移，迁移发生在语义表示层。**\n\n### RC3: Model coverage insufficient [HIGH]\n**Concern**: 只有 2 个模型，无法声称 \"架构无关\"\n**Mitigation**: 加 ≥1 不同架构（Mistral/Gemma），验证 ~7.2pp 不对称性\n**Experiment**: P0 — additional model verification\n\n### RC4: Dataset size and diversity [MEDIUM]\n**Concern**: ConflictQA 覆盖面有限（~1000 samples/model），只有 EN-ZH 一个语言对\n**Mitigation**: Phase 1 聚焦 EN-ZH 验证核心机制，Phase 2 扩展多语言（≥1 额外语言对）\n**Experiment**: P0 — multilingual extension (EN↔JA or EN↔DE)\n\n### RC5: Linear probe expressiveness [LOW]\n**Concern**: 线性探针可能遗漏复杂非线性信号\n**Mitigation**: MLP 对比实验已完成 ✅，非线性成分已量化\n**Experiment**: Done — MLP vs Linear comparison\n\n### RC6: SAE base/instruct mismatch [MEDIUM]\n**Concern**: Qwen-Scope SAE 训练在 base model 上，用于 instruct model 分析可能失配\n**Mitigation**: Track 2 用 base model 做 SAE 分析 + 与 Track 1 instruct probe 交叉验证\n**Experiment**: Track 2 设计已考虑\n\n### RC7: Steering failure precedent [MEDIUM]\n**Concern**: \"Interpretability without actionability\" 证明 SAE steering 可能完全无效\n**Mitigation**: 知识冲突与临床分诊的 5 维差异（SpARE 已证明知识冲突场景 steering 有效）；Track 3 显式报告失败模式\n**Experiment**: Track 3 包含 negative result framing\n\n### RC8: Causal claims without intervention [HIGH]\n**Concern**: 探针只证明信号可检测，不证明因果关系\n**Mitigation**: Track 3 steering 实验提供因果证据；Track 1 permutation test 提供统计控制\n**Experiment**: Track 3 steering + representation steering (P1)\n\n## Paper Structure (Tentative)\n\n1. **Introduction**: CLEAR gap → mechanistic question → H1 vs H2 → three-track approach → key findings preview\n2. **Related Work**: Monolingual conflict mechanisms → Cross-lingual processing → SAE steering (successes & failures) → Cross-lingual SAE features\n3. **Method**: Data construction (ConflictQA + translation + verification pipeline) → Track 1 probing → Track 2 SAE analysis → Track 3 steering\n4. **Experiments & Results**:\n   - 4.1 Cross-lingual conflict detectability (C1)\n   - 4.2 Asymmetric transfer analysis (C2) + token overlap controls\n   - 4.3 Non-linear components (C3) + layer-wise structure (C4)\n   - 4.4 SAE feature analysis (C5) [if Track 2 ready]\n   - 4.5 Steering experiments (C6) [if Track 3 ready]\n5. **Discussion**: H1 vs H2 resolution → mechanism implications → limitations → connection to CLEAR\n6. **Conclusion**\n\n## Scope Control\n\n**投稿最低要求 (must-have for submission)**:\n- Claims 1-3 fully supported (cross-lingual detectability + asymmetry + non-linearity)\n- Claim 4 partially supported (layer-wise analysis on ≥2 models)\n- ≥3 model architectures\n- ≥2 language pairs (EN-ZH + one more)\n- Token overlap control\n- COMET translation quality validation\n\n**理想状态 (nice-to-have)**:\n- Track 2 SAE analysis (Claim 5)\n- Track 3 steering (Claim 6)\n- 5+ language pairs covering multiple typological families\n- Full CKA/SVCCA layer analysis\n\n**不做 (out of scope)**:\n- 10-language full CLEAR replication\n- Custom SAE training\n- MoE model analysis\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_probe_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bootstrap_asymmetry_diff_corrected: 0.0718\n    bootstrap_asymmetry_ci_corrected: '[-0.0119, 0.1341]'\n    bootstrap_asymmetry_significant_corrected: false\n    bootstrap_asymmetry_method: per_iteration_paired_diff_from_training_bootstrap_n100\n    bootstrap_asymmetry_diff_old: 0.0595\n    bootstrap_asymmetry_ci_old: '[-0.0367, 0.1481]'\n    comet_tertile_ablation:\n      conclusion: not_confounder\n      delta_high_low_pp: -5.64\n      fisher_p: 0.695\n      high_bal_acc: 0.6071\n      med_bal_acc: 0.6769\n      low_bal_acc: 0.6635\n      best_layer: 22\n      detail: Reversed direction (High COMET → lower probe acc). COMET gate can be\n        relaxed.\n- exp_id: mvp_probe_llama_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bootstrap_asymmetry_diff_corrected: 0.0722\n    bootstrap_asymmetry_ci_corrected: '[0.0110, 0.1361]'\n    bootstrap_asymmetry_significant_corrected: true\n    bootstrap_asymmetry_method: per_iteration_paired_diff_from_training_bootstrap_n100\n    bootstrap_asymmetry_diff_old: 0.1176\n    bootstrap_asymmetry_ci_old: '[0.0429, 0.1957]'\n- exp_id: llama31_en_activations\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen3_translate_zh\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: collect_en_activations_qwen3_8b\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: collect_en_activations_llama_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: translate_zh_llama_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: translate_zh_qwen\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: collect_en_act_llama_v3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: collect_en_act_qwen_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: verify_qwen3_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen_en_act_v3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: llama_zh_act\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen_zh_act\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: translate_zh_qwen_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: probe_qwen_full\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: comet_qwen\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_llama\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_qwen_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_llama_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_qwen_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_llama_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_qwen_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_llama_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_qwen_v5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    death_cause: EXIT_CODE=124 timeout kill by submit_training_job (REGISTRY ONLY\n      - actual nohup processes alive)\n    restart_pid: 59412\n    restart_gpu: cuda:0\n    restart_method: nohup + TRANSFORMERS_OFFLINE=1\n    restart_time: '2026-05-21T23:15:00Z'\n    no_resume: true\n    acceleration: cuda:1 并行处理 test set (168条) - COMPLETED\n    qwen_test_completed: true\n    qwen_test_total: 168\n    qwen_test_passed: 31\n    qwen_test_pass_rate: 0.185\n    qwen_test_mean_comet: 0.7016\n    qwen_test_passed_mean_comet: 0.8503\n    qwen_train_progress: 320/798 (~40%)\n    actual_status: train still running on cuda:0 (PID 59412)\n    registry_failed_is_false_alarm: true\n- exp_id: comet_llama_v5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    death_cause: EXIT_CODE=124 timeout kill by submit_training_job (REGISTRY ONLY\n      - actual nohup processes alive)\n    restart_pid: 59571\n    restart_gpu: cuda:2\n    restart_method: nohup + TRANSFORMERS_OFFLINE=1\n    restart_time: '2026-05-21T23:15:00Z'\n    no_resume: true\n    acceleration: cuda:3 并行处理 test set (272条) - IN PROGRESS 66%\n    llama_train_progress: 300/1096 (~27%)\n    llama_test_progress: 180/272 (~66%)\n    actual_status: train on cuda:2 (PID 59571), test on cuda:3 (PID 64179)\n    registry_failed_is_false_alarm: true\n- exp_id: qwen_zh_act_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: comet_qwen_v6\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: comet_llama_v6\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n\n重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: [\"Judge\", \"Biased?\"]`），否则 `?` `:` 等字符会导致解析失败。\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-22T02:45:02.567Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T02:45:02.567Z",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-22T02:45:02.591Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：第三模型方向一致但未显著，仅 Track 1，claims 需降强度但核心叙事可维持
核心假设：['第三模型不对称方向一致（ZH→EN > EN→ZH）但 CI 含零', '3/3 方向一致，仅 1/3（Llama）达统计显著', 'effect size 跨模型稳定（±2pp 内），强 consistency argument', 'Llama COMET ablation 复现 not_confounder', 'Track 2 SAE 未完成或结果 noisy（Jaccard < 0.10）', '额外语言对仅 1 对，方向一致但样本量不足以单独显著']
关键指标范围：{'third_model_asymmetry_gap_pp': [2.0, 7.0], 'significant_asymmetry_models_of_3': [1, 1], 'consistent_direction_models_of_3': [3, 3], 'third_model_within_lang_acc': [0.68, 0.77], 'cross_lingual_transfer_acc_range': [0.6, 0.72], 'mlp_gain_weak_direction_pp_third_model': [1.0, 5.0], 'sae_cross_lingual_jaccard_mid_layer': [0.0, 0.1], 'lang_pairs_validated': [1, 2], 'tracks_submission_ready': [1, 1]}
叙事方向：C2 从 "significant asymmetry" 调整为 "remarkably consistent effect size across architectures  (7.2±0.5pp) despite varying statistical power"——强调 effect size stability 而非 p-value。 引用 Cumming (2014) "new statistics" 框架，effect size + CI 报告优于 NHST。 C1（detectability）升级为主 claim，C2 降为 strong supporting evidence。 Track 1 only 的贡献度靠深度弥补：layer-wise 分析 + confound exclusion pipeline  (token overlap + COMET ablation) 作为方法论贡献。RC8（因果 claim）明确限定为  "correlational evidence consistent with H1"，将 causal verification 列为 future work。 论文定位：phenomenon characterization + methodology，仍 ICLR-viable 但需  supplementary experiments 充实 appendix（更多 ablation、error analysis）。


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

重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: ["Judge", "Biased?"]`），否则 `?` `:` 等字符会导致解析失败。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "35caf52f-43ce-4786-a65a-c65a3457d853",
  "type": "user",
  "uuid": "30c85eea-b7bc-489c-b2fa-84f9dda315b1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T02:45:02.590Z_

```json
{
  "parentUuid": "30c85eea-b7bc-489c-b2fa-84f9dda315b1",
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
  "uuid": "525e87d8-1cee-42c9-a4ea-fc14842f210d",
  "timestamp": "2026-05-22T02:45:02.590Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T02:45:02.590Z_

```json
{
  "parentUuid": "525e87d8-1cee-42c9-a4ea-fc14842f210d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4fd4ad06-c24b-405b-9a0c-b1b2e903b870",
  "timestamp": "2026-05-22T02:45:02.590Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：第三模型方向一致但未显著，仅 Track 1，claims 需降强度但核心叙事可维持 核心假设：['第三模型不对称方向一致（ZH→EN > EN→ZH）但 CI 含零', '3/3 方向一致，仅 1/3（Llama）达统计显著', 'effect size 跨模型稳定（±2pp 内），强 consiste…",
  "leafUuid": "4fd4ad06-c24b-405b-9a0c-b1b2e903b870",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median scenario planning for cross-lingual conflict detection",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7"
}
```

---

### Assistant

_source line 8 · 2026-05-22T02:45:05.956Z_

Let me first read the experiment plan to understand all planned experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fd4ad06-c24b-405b-9a0c-b1b2e903b870",
  "isSidechain": false,
  "requestId": "req_011CbGqhEgGwvxsMadpBqcyL",
  "type": "assistant",
  "uuid": "5d2a376a-80b7-4cfc-b0b6-0c7dcc8baba3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DJudxggJzca7VzZB8S9xTG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12155,
      "cache_read_input_tokens": 11841,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12155,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 198,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12155
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

_source line 9 · 2026-05-22T02:45:10.451Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01XQaQMLpsixf9soD5tq4Wuh`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan files",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-prod42, find the experiment plan file(s). Look for files named experiment_plan*, plan*, or similar in the root and subdirectories. Also look for any YAML or markdown files that contain \"planned\" experiments or \"experiment\" plans. Search broadly - check directories like experiments/, plans/, docs/, etc. Report the full paths and contents of any relevant files found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d2a376a-80b7-4cfc-b0b6-0c7dcc8baba3",
  "isSidechain": false,
  "requestId": "req_011CbGqhEgGwvxsMadpBqcyL",
  "type": "assistant",
  "uuid": "d97ab9ad-473b-4e25-9485-095a1d72cf95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DJudxggJzca7VzZB8S9xTG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12155,
      "cache_read_input_tokens": 11841,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12155,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 198,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12155
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

_source line 10 · 2026-05-22T02:45:25.964Z_

<details><summary>↩ Tool result · `toolu_01XQaQMLpsixf9soD5tq4Wuh`</summary>

```text
## Summary

I found **one primary experiment plan file** in the directory:

### Primary File:
**`/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/experiment_plan.yaml`**

This is a comprehensive experiment plan (last updated 2026-05-22) for the "clkc_mech_interp" research project targeting ICLR 2027. The file contains:

**Structure:**
- **MVP Experiments** (3 items): Completed or in-progress foundational experiments including:
  - `mvp_001`: Dual-model residual flow probing (English-Chinese, Llama + Qwen)
  - `mvp_002`: MLP vs Linear probing comparison
  - `mvp_003`: COMET translation quality validation (currently running)

- **Statistical Corrections** (1 item): Bootstrap asymmetry CI analysis for reviewer feedback

- **Track 1: Cross-Lingual Probing** (6 items, P0-P1 priority): Including token overlap analysis, third-model architecture verification, multi-language expansion, layer-wise CKA/SVCCA analysis, and probe weight visualization

- **Track 2: SAE Feature Analysis** (3 items, P1-P2 priority): Conflict feature identification, language feature decoupling, and Jaccard analysis

- **Track 3: Steering** (3 items, P2 priority): Monolingual-to-cross-lingual steering transfer and correlation analysis

**Key Metrics:**
- Total GPU hours planned: ~155+ hours
- 17 total experiment items with varying statuses (done, running, planned)
- Organized by priority (P0-P2) and dependency tracking

### Related Planning Documents:
The search also revealed these complementary planning files in the same project:
- `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/ROADMAP.md` - Project roadmap
- `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/ROADMAP.lock` - Roadmap lock file
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d97ab9ad-473b-4e25-9485-095a1d72cf95",
  "isSidechain": false,
  "promptId": "35caf52f-43ce-4786-a65a-c65a3457d853",
  "type": "user",
  "uuid": "2c4a1f27-7331-4f22-8d69-62fb30fcd9cc",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In the directory /home/ubuntu/.agent-ml-research-prod42, find the experiment plan file(s). Look for files named experiment_plan*, plan*, or similar in the root and subdirectories. Also look for any YAML or markdown files that contain \"planned\" experiments or \"experiment\" plans. Search broadly - check directories like experiments/, plans/, docs/, etc. Report the full paths and contents of any relevant files found.",
    "agentId": "a996b1dc5f81e8992",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary\n\nI found **one primary experiment plan file** in the directory:\n\n### Primary File:\n**`/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/experiment_plan.yaml`**\n\nThis is a comprehensive experiment plan (last updated 2026-05-22) for the \"clkc_mech_interp\" research project targeting ICLR 2027. The file contains:\n\n**Structure:**\n- **MVP Experiments** (3 items): Completed or in-progress foundational experiments including:\n  - `mvp_001`: Dual-model residual flow probing (English-Chinese, Llama + Qwen)\n  - `mvp_002`: MLP vs Linear probing comparison\n  - `mvp_003`: COMET translation quality validation (currently running)\n\n- **Statistical Corrections** (1 item): Bootstrap asymmetry CI analysis for reviewer feedback\n\n- **Track 1: Cross-Lingual Probing** (6 items, P0-P1 priority): Including token overlap analysis, third-model architecture verification, multi-language expansion, layer-wise CKA/SVCCA analysis, and probe weight visualization\n\n- **Track 2: SAE Feature Analysis** (3 items, P1-P2 priority): Conflict feature identification, language feature decoupling, and Jaccard analysis\n\n- **Track 3: Steering** (3 items, P2 priority): Monolingual-to-cross-lingual steering transfer and correlation analysis\n\n**Key Metrics:**\n- Total GPU hours planned: ~155+ hours\n- 17 total experiment items with varying statuses (done, running, planned)\n- Organized by priority (P0-P2) and dependency tracking\n\n### Related Planning Documents:\nThe search also revealed these complementary planning files in the same project:\n- `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/ROADMAP.md` - Project roadmap\n- `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/ROADMAP.lock` - Roadmap lock file"
      }
    ],
    "totalDurationMs": 15508,
    "totalTokens": 26799,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 26082,
      "output_tokens": 510,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 202
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 510,
          "cache_read_input_tokens": 26082,
          "cache_creation_input_tokens": 202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 202,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 4,
      "bashCount": 3,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "d97ab9ad-473b-4e25-9485-095a1d72cf95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T02:45:31.205Z_

<details open><summary>🔧 Tool call — Read · `toolu_013bwqQMtiZz9vLYBNZwfWC5`</summary>

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
  "parentUuid": "2c4a1f27-7331-4f22-8d69-62fb30fcd9cc",
  "isSidechain": false,
  "requestId": "req_011CbGqix5gzFvqsum76y5se",
  "type": "assistant",
  "uuid": "bcac7d37-9266-494b-96b0-b5568dde108c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TkyfSGiWX126rgjm1aQbrP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 23996,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 717,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 23996,
          "cache_creation_input_tokens": 717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 717
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

_source line 12 · 2026-05-22T02:45:31.219Z_

<details><summary>↩ Tool result · `toolu_013bwqQMtiZz9vLYBNZwfWC5`</summary>

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
  "parentUuid": "bcac7d37-9266-494b-96b0-b5568dde108c",
  "isSidechain": false,
  "promptId": "35caf52f-43ce-4786-a65a-c65a3457d853",
  "type": "user",
  "uuid": "a42f7d32-de4a-40de-a548-3f113f86f8e8",
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
  "sourceToolAssistantUUID": "bcac7d37-9266-494b-96b0-b5568dde108c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13 · 2026-05-22T02:45:31.248Z_

````json
{
  "parentUuid": "a42f7d32-de4a-40de-a548-3f113f86f8e8",
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
  "uuid": "85ca9349-1598-4fce-845f-e60810d27d4b",
  "timestamp": "2026-05-22T02:45:31.248Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：第三模型方向一致但未显著，仅 Track 1，claims 需降强度但核心叙事可维持 核心假设：['第三模型不对称方向一致（ZH→EN > EN→ZH）但 CI 含零', '3/3 方向一致，仅 1/3（Llama）达统计显著', 'effect size 跨模型稳定（±2pp 内），强 consiste…",
  "leafUuid": "85ca9349-1598-4fce-845f-e60810d27d4b",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Median scenario planning for cross-lingual conflict detection",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7"
}
```

---

### Assistant

_source line 16 · 2026-05-22T02:47:41.503Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full experiment plan. Let me identify all "planned" experiments and generate detailed predictions for the median tier. Let me list them:

**Planned experiments:**
1. plan_102 - 第三模型架构验证 (P0)
2. plan_103 - 多语言扩展 EN↔JA (P0)
3. plan_104 - Layer-wise CKA/SVCCA (P0)
4. plan_109 - 探针权重可视化 + PCA (P1)
5. plan_106 - Label noise ablation (P1)


6. plan_107 - Representation steering (P0)
7. plan_108 - 更大数据集验证 (P1)
8. plan_201 - Qwen-Scope SAE 冲突特征识别 (P1)
9. plan_202 - LangFIR 语言特征解耦 (P1)
10. plan_203 - Cross-lingual feature Jaccard 分析 (P1)
11. plan_301 - Monolingual→cross-lingual steering transfer (P2)
12. plan_302 - Cross-lingual-specific steering (P2)
13. plan_303 - Typological steering correlation (P2)

I should focus on the planned experiments only since mvp_003 is already running. Now I'm working through the median tier predictions for each planned experiment, considering the key characteristics: direction consistency across models with limited statistical significance, stable effect sizes, SAE track completeness, and submission readiness. I'm establishing the metric ranges for the third model asymmetry gap and other key measurements. Now I'm working through the narrative framing—shifting the focus from statistical significance to effect size consistency, particularly how C2 maintains a stable 7.2±0.5pp asymmetry across different architectures regardless of statistical power, which aligns with Cumming's framework on effect size reliability. I'm laying out the detailed predictions for each experimental plan, starting with the third model scenario where we'd expect directionally consistent asymmetry without reaching significance, paired with specific accuracy ranges and confidence intervals that bracket zero.

Writing YAML output... The steering results show directional effects for the stronger translation pair but less pronounced for the weaker direction, giving some causal support though not conclusive. The larger dataset experiment aligns with existing findings and tightens confidence intervals. For the SAE track, results fall into the noisy range with low Jaccard scores below 0.10, and the steering track experiments weren't completed in the median tier. Now I'm working through the complete experimental breakdown, starting with the third model architecture verification using Gemma-2-9B-IT.

For plan_102, the within-language performance sits around 72.5% for English and 69.3% for Chinese, while cross-lingual translation shows 63.8% for English-to-Chinese and 69.2% for Chinese-to-English. The asymmetry gap of 5.4 percentage points falls within the expected range, with bootstrap iterations showing 97 out of 100 in the positive direction, though the confidence interval does span zero. I'm settling on 5.8pp as the point estimate to stay within the specified bounds.

Now I'm reconciling the constraints: the existing 7.2pp gap with a ±2pp stability margin gives [5.2, 9.2], but the metric range caps it at [2.0, 7.0], so the overlap is [5.2, 7.0]. I should target something in that narrower band, around 6.1pp.

But there's a tension with the narrative framing of "7.2±0.5pp" as the consistent effect size—if the third model could be as low as 2pp, that breaks the consistency claim. The resolution is that the effect size is directionally consistent across architectures, but the confidence intervals are wider in the median case.

So I'll set the third model at 5.8pp, which sits comfortably within both the ±2pp stability constraint around 7.2pp and the [2.0, 7.0] range for the indicator. That gives a cross-model average of roughly 6.7pp, which supports the "consistent" framing while respecting the empirical constraints. with 7.2 (difference of 1.8pp), and the CI would contain zero. Now I'm ready to write this up — I'll be thorough but keep the numbers grounded. I need to think through what tables and figures each experiment should produce, then draft the output using YAML flow sequences with double-quoted strings for the table format.

For the narrative, I'm reframing C2 to emphasize the remarkably consistent effect size across architectures despite varying statistical power, citing Cumming's work on effect sizes and confidence intervals over null hypothesis significance testing. C1 becomes the primary claim about detectability, while C2 shifts to strong supporting evidence. I'm focusing on Track 1 with layer-wise analysis and confound exclusion as methodological contributions, limiting RC8 to correlational evidence consistent with the hypothesis, and positioning the paper around phenomenon characterization and methodology.

I'm also planning a third model architecture validation experiment on Gemma-2-9B-IT to verify the ~7.2pp asymmetry holds consistently across different models, with expected results showing the same pattern of English-English accuracy around 73%, Chinese-Chinese around 69%, and English-Chinese around 64%.

Now I'm looking at the detailed metrics from that Gemma experiment—the asymmetry gap comes in smaller at 5.4pp with a wider confidence interval that includes zero, though 94% of bootstrap iterations still show positive asymmetry. The MLP analysis shows the same directional pattern with a 3.1pp gain from the nonlinear component, and the permutation tests confirm significance within each language and across the English-to-Chinese direction, though the Chinese-to-English cross-lingual effect is more marginal. 虽然样本量有限导致置信区间包含零，但结果方向一致，这是典型的检验力不足但方向性稳健的情况。MLP 增益达到 3.1pp，介于其他两个模型之间，反映了 Gemma 架构在非线性特征学习上的独特表现。现在看一下 Gemma 模型的探针转移精度矩阵。 Looking at the effect sizes across the three models—Llama at 7.22pp, Qwen at 7.18pp, and Gemma at 5.4pp—they cluster around a mean of 6.6pp with minimal variation, which supports framing this as a consistent directional pattern rather than claiming statistical significance across all architectures. The Cohen's d values ranging from 0.35 to 0.52 suggest a real but modest phenomenon, and even though only Llama reaches individual significance, the alignment in direction across all three models is compelling. Now I'm moving into the multilingual extension with English-Japanese pairs.

For the EN↔JA experiment, I expect the same directional pattern as with Chinese—Japanese being another non-Latin script language—but the effect might be slightly smaller around 4-6pp since Japanese training data is typically less abundant than Chinese in these models, and the agglutinative morphology differs from Chinese's isolating structure. The sample size will be tight for standalone significance, but the consistency with the Chinese results should strengthen the overall narrative. For the layer-wise analysis, I'm planning to examine CKA and SVCCA similarity between English and Chinese activations across different layers, expecting high alignment in early layers where embeddings are shared. For plan_107, I'm using the probe weight direction as a steering vector—adding and subtracting it from the residual stream at the best layer to see if outputs flip between parametric and contextual answers. The strong direction (ZH→EN) flips about 30-40% of outputs while the weaker direction (EN→ZH) only flips 15-25%, giving correlational evidence for a causal role but not definitive proof. Plan_108 expands to 2000+ samples with consistent results and tighter confidence intervals, though the asymmetry gap stays around 7pp and this might not be completed depending on the submission scope.

For Track 2 (plans 201-203), the median prediction is noisy or incomplete results with Jaccard scores below 0.10, meaning the SAE isn't detecting meaningful cross-lingual feature sharing. I'll predict plan_201 as partially completed with noisy results, while 202 and 203 likely aren't completed or are too noisy to be useful. Track 3 (plans 301-303) depends on Track 2's results, so those are probably not completed either.

Now I need to write out the full YAML carefully. I'm also thinking through the COMET predictions — plan_105 for Qwen is done, but there's a Llama consistency check still pending. The mvp_003 is still running for COMET translation quality validation, so I need to figure out whether the Llama COMET ablation is part of that or separate.

Looking at the status: plan_105 shows "done" for Qwen with the segmented ablation, and the Llama part would depend on mvp_003 completing first. Since the user wants predictions for each planned experiment, I should focus on the ones marked as "planned" rather than "done" — so plan_102, plan_103, plan_104, plan_109, and checking what else is in the pipeline. Now I'm ready to write out the complete YAML structure with all the experiment details organized into proper tables.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85ca9349-1598-4fce-845f-e60810d27d4b",
  "isSidechain": false,
  "requestId": "req_011CbGqjLyLvNANQ55ZnaVzd",
  "type": "assistant",
  "uuid": "4e49a24a-4940-46cb-a061-c38ddcddb0a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WJLyrpToKVdQYcTiry271d",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9454,
      "cache_read_input_tokens": 24713,
      "output_tokens": 17709,
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
          "output_tokens": 17709,
          "cache_read_input_tokens": 24713,
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

_source line 17 · 2026-05-22T02:51:48.497Z_

Now I have the full experiment plan. Let me generate the detailed median-tier predictions for all 13 planned experiments.

```yaml
tier: median
narrative_guidance: |
  C2 从 "significant asymmetry" 调整为 "remarkably consistent effect size across architectures
  (6.6±0.9pp) despite varying statistical power"——强调 effect size stability 而非 p-value。
  引用 Cumming (2014) "new statistics" 框架: effect size + CI 优于 NHST。
  C1 (detectability) 升级为主 claim，C2 降为 strong supporting evidence。
  Track 1 only 的贡献靠深度弥补: layer-wise 分析 + confound exclusion pipeline (token overlap +
  COMET ablation) 作为方法论贡献。RC8 明确限定为 "correlational evidence consistent with H1"，
  causal verification 列为 future work。论文定位: phenomenon characterization + methodology，
  仍 ICLR-viable 但需 supplementary experiments 充实 appendix（更多 ablation、error analysis）。
  Track 2 SAE 若完成但 Jaccard < 0.10，可作为 "negative/inconclusive result" 放 appendix，
  反而增加诚实度和完整度。

imagined_experiments:
  # ═══ Track 1 P0 ═══

  - name: "第三模型架构验证"
    plan_id: "plan_102"
    description: "在 Gemma-2-9B-IT 上重复完整探针实验，验证 ~7.2pp 不对称性跨架构一致性"
    expected_results:
      model: "Gemma-2-9B-IT"
      en_en_bal_acc: 0.731
      zh_zh_bal_acc: 0.694
      en_zh_bal_acc: 0.641
      zh_en_bal_acc: 0.695
      asymmetry_gap_pp: 5.4
      bootstrap_ci_95: "[-0.8%, 11.6%]"
      bootstrap_significant: false
      positive_iterations_of_100: 94
      permutation_p_en_en: "<0.001"
      permutation_p_zh_zh: "<0.001"
      permutation_p_en_zh: 0.006
      permutation_p_zh_en: "<0.001"
      best_layer_en: 23
      best_layer_zh: 20
      best_layer_depth_pct: 0.72
      mlp_en_zh_gain_pp: 3.1
      mlp_zh_en_gain_pp: 0.8
      token_overlap_jaccard_mean: 0.035
      token_overlap_correlation_p: 0.31
    result_rationale: |
      Gemma-2-9B-IT 使用 parallel attention + GeGLU，与 Llama (sequential GQA) 和 Qwen
      (sequential GQA + RoPE variant) 架构差异最大。within-lang acc 落在 0.69-0.73 因 Gemma
      多语言训练配比适中（英语占优但中文覆盖不如 Qwen）。不对称性方向一致（ZH→EN > EN→ZH）
      源于相同底层机制——英语作为训练主导语言的表征锚点效应——与架构无关。但 gap 缩小至 5.4pp
      （vs 7.2pp），因 Gemma 的 parallel attention 提供更均匀的跨层信息流动，降低了方向性
      映射难度差异。CI 含零因: (1) 样本量 ~1000 在 5.4pp effect 下 power 不足, (2) Gemma
      的 attention pattern 引入更大 per-sample 方差。94/100 bootstrap 正向但不足以排除零。
      MLP gain +3.1pp 弱方向，介于 Qwen(2.3pp) 和 Llama(4.7pp corrected) 之间。
      best_layer 深度 72% 与 Qwen(67%) 更接近而非 Llama(88%)，暗示峰值层与架构深度分配
      有关而非固定比例——C4 需更多模型确认 pattern。
    tables:
      - caption: "Gemma-2-9B-IT probe transfer accuracy (balanced accuracy, n=100 bootstrap)"
        columns: ["Train→Test", "Bal. Acc (%)", "95% CI", "Perm. p"]
        rows:
          - ["EN→EN", "73.1", "[70.2, 76.0]", "<0.001"]
          - ["ZH→ZH", "69.4", "[66.3, 72.5]", "<0.001"]
          - ["EN→ZH", "64.1", "[59.9, 68.3]", "0.006"]
          - ["ZH→EN", "69.5", "[65.7, 73.3]", "<0.001"]
          - ["Gap (ZH→EN − EN→ZH)", "+5.4", "[-0.8, 11.6]", "—"]
      - caption: "Cross-architecture asymmetry consistency (all three models)"
        columns: ["Model", "Gap (pp)", "95% CI", "Significant?", "Direction"]
        rows:
          - ["Llama-3.1-8B", "7.22", "[1.1, 13.6]", "Yes (borderline)", "ZH→EN > EN→ZH"]
          - ["Qwen3-8B", "7.18", "[-1.2, 13.4]", "No", "ZH→EN > EN→ZH"]
          - ["Gemma-2-9B-IT", "5.4", "[-0.8, 11.6]", "No", "ZH→EN > EN→ZH"]
          - ["Mean ± SD", "6.60 ± 1.04", "—", "1/3 sig, 3/3 consistent", "—"]
    figures_description:
      - "Forest plot: 三模型不对称性 effect size + 95% CI，水平线标注 grand mean 6.6pp。Llama CI 刚好排除零，Qwen/Gemma CI 含零但全部在正方向。右侧标注 consistency: 3/3 direction, 1/3 significance。"
      - "Layer-wise probe accuracy heatmap: Gemma 32 层 × 4 方向（EN→EN, ZH→ZH, EN→ZH, ZH→EN），peak 层在 depth ~72%，与 Llama(88%)/Qwen(67%) 横向对比。"
    analysis: |
      三模型 effect size: 7.22, 7.18, 5.4 → mean=6.60, SD=1.04pp。Cochran's Q test 跨
      模型一致性 p=0.68（无显著异质性）。Gemma 偏低 1.8pp 可解释为架构效应而非方向不一致。
      关键叙事: "In all three architectures spanning two distinct design families (GQA vs
      parallel attention), the ZH→EN transfer consistently exceeded EN→ZH, with a pooled
      effect of 6.6pp (range 5.4–7.2). Only Llama reached conventional significance
      (p<0.05), but the I² heterogeneity statistic of 0% and consistent directionality
      across 3/3 models provides stronger evidence than any single p-value."
      Cohen's d range: 0.32-0.48 (small-to-medium)。对 Cumming (2014) framing 足够。
      C2 claim 降级为: "consistent directional asymmetry with stable effect size" 而非
      "statistically significant asymmetry"。

  - name: "多语言扩展 (EN↔JA)"
    plan_id: "plan_103"
    description: "扩展到 EN↔JA 语言对，测试不对称性是否与 typological distance 相关"
    expected_results:
      model_tested: "Llama-3.1-8B (primary) + Qwen3-8B (if time permits)"
      ja_translation_comet_mean: 0.74
      ja_translation_pass_rate_080: 0.22
      en_en_bal_acc: 0.771  # same as existing
      ja_ja_bal_acc: 0.673
      en_ja_bal_acc: 0.612
      ja_en_bal_acc: 0.658
      asymmetry_gap_pp: 4.6
      bootstrap_ci_95: "[-2.1%, 11.3%]"
      bootstrap_significant: false
      positive_iterations_of_100: 88
      sample_size_ja: 680
      conflictqa_ja_coverage: 0.68
    result_rationale: |
      JA 预测结果弱于 ZH 有三个原因: (1) ConflictQA 中 JA 实体覆盖率低于 ZH（Wikidata
      JA 标签覆盖不如 ZH），可用样本 ~680 vs ZH ~1000; (2) JA 作为 agglutinative 语言，
      tokenizer 切分更碎片化，信息密度/token 低于 ZH，探针输入质量略降; (3) Llama-3.1 的
      JA 训练数据占比低于 ZH，within-lang acc 偏低。
      不对称性方向一致（JA→EN > EN→JA）因相同锚点机制——英语表征空间主导。gap 4.6pp 略
      小于 ZH 的 7.2pp，可能因 JA-EN typological distance 大于 ZH-EN（JA 是 SOV 语序 +
      agglutinative，ZH 是 SVO + isolating），映射两个方向都更难，压缩了不对称性。
      CI 含零主要因样本量不足 (n=680) 导致 power 严重不足。direction consistency 才是关键。
      这个结果对 H1 vs H2 判别力弱——两个假说都兼容此 pattern。需更多语言对（DE, AR）
      才能有效区分。
    tables:
      - caption: "EN↔JA probe transfer (Llama-3.1-8B, n=680)"
        columns: ["Train→Test", "Bal. Acc (%)", "95% CI", "Perm. p"]
        rows:
          - ["EN→EN", "77.1", "[74.3, 79.9]", "<0.001"]
          - ["JA→JA", "67.3", "[63.5, 71.1]", "<0.001"]
          - ["EN→JA", "61.2", "[56.9, 65.5]", "0.021"]
          - ["JA→EN", "65.8", "[61.6, 70.0]", "0.002"]
          - ["Gap (JA→EN − EN→JA)", "+4.6", "[-2.1, 11.3]", "—"]
      - caption: "Cross-language-pair asymmetry comparison"
        columns: ["Language Pair", "Gap (pp)", "95% CI", "n", "Direction"]
        rows:
          - ["EN↔ZH (Llama)", "7.22", "[1.1, 13.6]", "~1000", "ZH→EN > EN→ZH"]
          - ["EN↔JA (Llama)", "4.6", "[-2.1, 11.3]", "~680", "JA→EN > EN→JA"]
    figures_description:
      - "双语言对不对称性对比: EN↔ZH vs EN↔JA 的 asymmetry gap + CI，标注语言对 typological distance (WALS features)。Direction 一致但 gap 可能因 typological distance 或 sample size 差异——无法区分。"
    analysis: |
      EN↔JA 方向一致支持 H1 的 English-anchored 假设——不管目标语言是 ZH 还是 JA，
      X→EN 迁移都优于 EN→X。但 gap 差异 (7.2 vs 4.6pp) 的解释有混淆: 可能是
      typological distance 效应 (支持 H2 的弱形式) 或纯粹是 sample size/coverage 导致的
      power 差异。此实验为 "方向一致但样本量不足以单独显著" 的典型 median-tier 结果。
      论文中作为 supplementary evidence 放 Discussion，不宜作为独立 claim。
      贡献: 将 lang_pairs_validated 从 1 提升到 2，满足 RC4 的最低要求。

  - name: "Layer-wise CKA/SVCCA"
    plan_id: "plan_104"
    description: "逐层 CKA + SVCCA 分析 EN vs ZH 表征相似度变化，对接 language transition 文献"
    expected_results:
      cka_early_layers_0_to_25pct: 0.92
      cka_mid_layers_25_to_60pct: 0.78
      cka_upper_layers_60_to_85pct: 0.71
      cka_final_layers_85_to_100pct: 0.63
      svcca_correlation_with_cka: 0.94
      language_transition_onset_layer_pct: 0.55
      probe_peak_vs_cka_drop_correlation: -0.67
      cka_conflict_vs_nonconflict_diff_peak_layer: 0.08
    result_rationale: |
      CKA 从 early layers (~0.92) 单调下降到 final layers (~0.63) 符合 "Lost in
      Multilinguality" (Wendler et al. 2024) 的 language transition 预测: 模型在 mid-upper
      layers 开始将 language-universal 语义表征转换为 language-specific 输出表征。
      transition onset ~55% depth 与 Wendler 的 60% 接近（Wendler 用更大模型，transition
      更靠后）。probe accuracy peak 出现在 CKA 开始快速下降的区域——这是核心发现:
      冲突信号在语言表征开始分化的 "临界层" 最强，暗示冲突检测发生在 universal→specific
      transition 过程中。但 conflict vs non-conflict 的 CKA 差异仅 0.08（peak 层），
      不够大到支持强结论。SVCCA 与 CKA 高度一致 (r=0.94) 增加方法鲁棒性。
      此实验提供 C4 (layer structure) 的核心证据，但 peak 层跨模型不一致 (Llama 88%,
      Qwen 67%, Gemma 72%) 使得 "universal pattern" claim 困难。
    tables:
      - caption: "Layer-wise CKA between EN and ZH conflict activations (Llama-3.1-8B)"
        columns: ["Layer Range", "Depth %", "CKA (mean)", "CKA (std)", "Probe Acc (%)"]
        rows:
          - ["0-8", "0-25%", "0.92", "0.03", "54.2"]
          - ["8-19", "25-60%", "0.78", "0.05", "62.8"]
          - ["19-27", "60-85%", "0.71", "0.04", "73.6"]
          - ["27-32", "85-100%", "0.63", "0.06", "69.1"]
      - caption: "Language transition onset across models"
        columns: ["Model", "Transition Onset (%)", "Probe Peak (%)", "CKA at Peak"]
        rows:
          - ["Llama-3.1-8B", "55%", "88%", "0.64"]
          - ["Qwen3-8B", "50%", "67%", "0.73"]
          - ["Gemma-2-9B-IT", "52%", "72%", "0.70"]
    figures_description:
      - "双 Y 轴折线图: X 轴为层 index (normalized 0-100%)，左 Y 轴为 CKA (EN vs ZH)，右 Y 轴为 probe balanced accuracy。两条线交叉的区域标注为 'conflict detection zone'。三模型 subplot 横向排列。"
      - "CKA heatmap: layer × layer 的 EN-ZH CKA 矩阵，对角线为同层 CKA (上述折线)，off-diagonal 显示跨层对齐——若 off-diagonal 有高 CKA 带，暗示 EN 和 ZH 在不同层达到相似表征。"
    analysis: |
      CKA 下降曲线 + probe peak 的共现为 C4 提供了 mechanistic 叙事: "冲突信号在语言表征
      从 universal 向 specific 转变的过程中达到峰值"。但三模型 peak 层分散 (67-88%)
      削弱了 "固定比例" 的 claim。改为: "conflict detection peaks during the language
      transition window, whose exact location is architecture-dependent"。
      CKA conflict vs non-conflict 差异 (0.08) 太小，不支持 "冲突改变了跨语言对齐" 这种
      强 claim。应限定为描述性发现。此实验是论文 Section 4.3 的核心图表来源。

  - name: "Representation steering (干预实验)"
    plan_id: "plan_107"
    description: "用探针方向作 steering vector 干预残差流，测量模型输出的因果变化"
    expected_results:
      steering_method: "probe_weight_direction_addition"
      strong_direction_zh_en_flip_rate: 0.34
      weak_direction_en_zh_flip_rate: 0.18
      steering_alpha_optimal: 3.5
      coherence_preservation_rate: 0.72
      parametric_to_contextual_flip_rate: 0.28
      contextual_to_parametric_flip_rate: 0.22
      random_direction_flip_rate: 0.06
      steering_effect_significant: true
      steering_effect_size_cohens_d: 0.41
    result_rationale: |
      Probe weight 方向包含冲突检测信号但非纯因果方向——探针学到的是 "与冲突相关的方差方向"
      而非 "因果控制冲突解决的方向"。因此 flip rate 偏低 (~18-34%) 而非理想的 50%+。
      ZH→EN 方向 flip rate (34%) 高于 EN→ZH (18%)，与探针迁移不对称性一致: ZH→EN
      探针捕获了更纯粹的冲突信号，steering 更有效。EN→ZH 方向的非线性成分 (MLP gain)
      意味着线性 steering vector 无法充分捕获该方向的冲突信号。
      alpha=3.5 是 coherence-effectiveness trade-off: 过大导致输出退化 (coherence < 60%),
      过小无效果。random direction control (6% flip) 证明效果非随机。
      Cohen's d=0.41 (medium) 提供 "correlational evidence consistent with causal role"
      但不是 clean causal demonstration (那需要 activation patching 或 DAS)。
      此实验在 Track 3 缺席时成为 RC8 的唯一因果证据来源。
    tables:
      - caption: "Steering intervention results (Llama-3.1-8B, best layer)"
        columns: ["Condition", "Flip Rate (%)", "Coherence (%)", "Random Ctrl (%)"]
        rows:
          - ["ZH→EN probe direction", "34.2", "74.1", "5.8"]
          - ["EN→ZH probe direction", "18.1", "71.3", "6.2"]
          - ["Averaged probe direction", "26.5", "72.8", "6.0"]
          - ["Random orthogonal direction", "6.0", "89.5", "—"]
      - caption: "Steering alpha sensitivity (ZH→EN direction)"
        columns: ["Alpha", "Flip Rate (%)", "Coherence (%)", "Net Useful Flips (%)"]
        rows:
          - ["1.0", "12.3", "91.2", "11.2"]
          - ["2.0", "22.8", "84.6", "19.3"]
          - ["3.5", "34.2", "74.1", "25.3"]
          - ["5.0", "38.9", "58.3", "22.7"]
          - ["7.0", "41.2", "42.1", "17.3"]
    figures_description:
      - "Flip rate vs alpha 曲线 + coherence vs alpha 曲线 (双 Y 轴)，标注最优 alpha=3.5 为 net useful flips 最大值。与 random direction baseline 的阴影区域形成对比。"
      - "输出示例表: 3-4 个 steering 前后的 QA 对比，展示 parametric→contextual flip 和 coherence 保持的 case。"
    analysis: |
      Steering 提供了有限但实在的因果证据: probe direction 操纵可改变输出，且效果与
      random direction 显著不同 (p<0.001)。但 34% flip rate 不足以声称 "冲突信号因果
      控制冲突解决"——更准确的 framing 是 "探针捕获的方向与冲突解决机制相关联"。
      论文中放在 Discussion 的 "Towards Causal Understanding" 小节，明确 limitation:
      "Our steering results provide correlational evidence consistent with a causal role
      for the detected conflict signal. Definitive causal claims require activation
      patching or distributed alignment search, which we leave to future work."
      不对称 flip rate (34 vs 18%) 与探针不对称性 echo，strengthens C2 narrative。

  # ═══ Track 1 P1 ═══

  - name: "探针权重可视化 + PCA"
    plan_id: "plan_109"
    description: "最优层探针权重 PCA/t-SNE 可视化，展示冲突 vs 非冲突的表征分布"
    expected_results:
      pca_variance_explained_2d: 0.23
      conflict_nonconflict_cluster_silhouette: 0.31
      en_zh_overlap_coefficient_mid_layer: 0.62
      en_zh_overlap_coefficient_late_layer: 0.41
      cross_lingual_centroid_distance_mid: 1.24
      cross_lingual_centroid_distance_late: 2.08
    result_rationale: |
      前 2 PC 仅解释 23% 方差——高维表征在低维投影中信息丢失严重，这是 known limitation。
      Silhouette 0.31 (weak clustering) 意味着 conflict vs non-conflict 不是 clean 分离
      而是有 substantial overlap，符合 balanced accuracy ~75% (非 95%+) 的预期。
      关键定性发现: mid-layer 中 EN 和 ZH conflict 点云的重叠 (overlap=0.62) 显著高于
      late-layer (0.41)——支持 H1 的 "mid-layer 共享表征" 假设。EN conflict 和 ZH
      conflict 的 centroid distance 从 mid (1.24) 到 late (2.08) 增大，与 CKA 下降一致。
      但这是低维投影的定性证据，不能独立支持 claim。作为 Figure 3 (illustrative) 使用。
    tables:
      - caption: "PCA cluster metrics across layers"
        columns: ["Layer", "Depth %", "Silhouette", "EN-ZH Overlap", "Centroid Dist."]
        rows:
          - ["Layer 10", "31%", "0.18", "0.78", "0.82"]
          - ["Layer 18", "56%", "0.28", "0.62", "1.24"]
          - ["Layer 25", "78%", "0.31", "0.48", "1.73"]
          - ["Layer 28", "88%", "0.34", "0.41", "2.08"]
    figures_description:
      - "2×2 subplot PCA scatter: mid-layer (layer 18) vs late-layer (layer 28) × Llama vs Qwen。颜色编码: EN-conflict (红), EN-no-conflict (浅红), ZH-conflict (蓝), ZH-no-conflict (浅蓝)。Mid-layer 红蓝 conflict 点云明显重叠; late-layer 按语言分离但 conflict label 仍有区分。"
      - "t-SNE 版本作为 supplementary figure，perplexity=30。与 PCA 定性一致但 cluster 更 visually separated (t-SNE 的已知 artifact，论文中说明)。"
    analysis: |
      PCA 可视化的价值是 illustrative 而非 evidentiary。主要功能: (1) 直觉展示 "冲突信号
      为什么能跨语言迁移"——mid-layer 两种语言的 conflict 表征在同一区域; (2) 直觉展示
      "为什么迁移不完美"——overlap 不是 100%。不应过度解读 silhouette 值。
      放在论文 Figure 3，caption 明确标注 "illustrative; quantitative analysis in Table 2"。

  - name: "Label noise ablation"
    plan_id: "plan_106"
    description: "注入 5-20% label noise 评估探针对 verification pipeline 标注错误的鲁棒性"
    expected_results:
      noise_0pct_acc: 0.771
      noise_5pct_acc: 0.758
      noise_10pct_acc: 0.738
      noise_15pct_acc: 0.704
      noise_20pct_acc: 0.668
      degradation_5pct_pp: -1.3
      degradation_10pct_pp: -3.3
      degradation_15pct_pp: -6.7
      degradation_20pct_pp: -10.3
      estimated_pipeline_error_rate: 0.04
      noise_tolerance_threshold: 0.10
    result_rationale: |
      探针在 0-10% noise 下温和退化（-1 到 -3pp），10-20% 区间加速退化——典型的线性探针
      noise sensitivity 曲线。此 pattern 因线性模型对 label noise 的 theoretical
      robustness: 当 noise 远低于 signal (acc >> 50%), label flips 对决策边界影响被多数
      正确样本 "稀释"。但超过 ~10% 后 signal-to-noise 下降导致边界显著偏移。
      verification pipeline (ConflictQA 的 parametric/contextual answer 匹配) 的估计
      error rate ~4%，远低于 10% tolerance threshold。这证明 C1 的探针 accuracy 不是
      label noise 的 artifact。补充 Appendix A 的 robustness 证据。
    tables:
      - caption: "Probe accuracy under systematic label noise (Llama-3.1-8B, EN→EN)"
        columns: ["Noise Rate", "Bal. Acc (%)", "Delta (pp)", "95% CI"]
        rows:
          - ["0%", "77.1", "—", "[74.3, 79.9]"]
          - ["5%", "75.8", "-1.3", "[72.9, 78.7]"]
          - ["10%", "73.8", "-3.3", "[70.7, 76.9]"]
          - ["15%", "70.4", "-6.7", "[67.0, 73.8]"]
          - ["20%", "66.8", "-10.3", "[63.1, 70.5]"]
    figures_description:
      - "折线图: X 轴 noise rate (0-20%), Y 轴 balanced accuracy。阴影区域为 95% CI (n=100 bootstrap per noise level)。水平虚线标注 chance level (50%)。垂直虚线标注 estimated pipeline error rate (4%)。"
    analysis: |
      Pipeline error rate 4% 处的 accuracy 损失仅 ~1pp，远小于 CI 宽度——label noise
      对结论无实质影响。此实验直接回应 "你的 verification pipeline 可能有错" 的 reviewer
      concern，以实验代替争论。放 Appendix，一图一表足够。

  - name: "更大数据集验证"
    plan_id: "plan_108"
    description: "扩大到 2000+ samples 或引入额外数据集验证 C1"
    expected_results:
      expanded_sample_size: 1800
      expansion_method: "ConflictQA additional sampling + ParaRel-conflict subset"
      en_en_acc_expanded: 0.765
      asymmetry_gap_pp_expanded: 7.0
      ci_width_reduction_pct: 35
      bootstrap_ci_expanded: "[2.3%, 11.7%]"
      bootstrap_significant_expanded: true
      new_dataset_consistency: 0.92
    result_rationale: |
      样本量从 ~1000 扩至 ~1800 (1.8x) 使 CI 宽度缩减约 35% (sqrt(1.8) ≈ 1.34 倍
      precision)。在 Llama 上，这足以将 borderline significant CI [1.1, 13.6] 收紧为
      [2.3, 11.7]——更 comfortably 排除零。但 Qwen 可能仍含零 (从 [-1.2, 13.4] 到
      [-0.2, 12.5] 左右)。within-lang accuracy 略降 (77.1→76.5) 因新增样本包含更多
      "difficult" cases (ConflictQA 的 easy cases 先被采样)。
      ParaRel-conflict subset 与 ConflictQA 的一致性 0.92 (探针在两个数据集的准确率
      高度相关) 增加 ecological validity。但此实验 P1 优先级在 median tier 下可能
      不完整——若只完成 ConflictQA 扩展 (n=1500) 而没做 ParaRel，仍有价值但有限。
    tables:
      - caption: "Dataset expansion effect on asymmetry CI (Llama-3.1-8B)"
        columns: ["Dataset", "n", "Gap (pp)", "95% CI", "Significant?"]
        rows:
          - ["ConflictQA original", "~1000", "7.22", "[1.1, 13.6]", "Yes (borderline)"]
          - ["ConflictQA expanded", "~1500", "7.0", "[1.8, 12.2]", "Yes"]
          - ["+ ParaRel subset", "~1800", "7.0", "[2.3, 11.7]", "Yes"]
    figures_description:
      - "CI 收敛图: X 轴为 sample size (incremental)，Y 轴为 asymmetry gap CI 宽度。Random subsample bootstrap (n=500, 750, 1000, 1250, 1500, 1800) 展示 CI 随 sample size 的收敛速度。"
    analysis: |
      主要价值: 将 Llama 从 borderline significant 提升为 comfortably significant，
      增强 C2 的统计基础。但如果 Qwen 仍不显著，核心叙事不变——仍是 "consistent effect
      size, varying power"。此实验是 "nice to have" 而非 game-changer。
      若时间紧张，优先做 plan_102 (第三模型) 和 plan_107 (steering) 而非此项。

  # ═══ Track 2: SAE Feature Analysis ═══

  - name: "Qwen-Scope SAE 冲突特征识别"
    plan_id: "plan_201"
    description: "用 Qwen-Scope 预训练 SAE 分析冲突激活的差异化特征"
    expected_results:
      sae_model: "Qwen-Scope (Qwen3-8B-Base)"
      total_sae_features: 65536
      conflict_activated_features_top: 280
      mi_selected_features: 45
      mi_threshold: 0.15
      top_feature_activation_diff: 2.3
      feature_interpretability_rate: 0.35
      cross_lingual_overlap_top_features: 8
      noise_level: "high"
      base_instruct_mismatch_cosine: 0.71
    result_rationale: |
      Qwen-Scope SAE 训练在 base model，用于 instruct model 分析存在分布偏移 (RC6)。
      Base-instruct cosine similarity ~0.71 意味着约 30% 的激活模式不对齐，导致 SAE
      reconstruction quality 下降，特征识别 noisy。MI-selected 45 个特征中，手动检查
      可解释的仅 35% (其余激活模式无法对应到 human-interpretable concept)。
      conflict-activated 特征数 (280) 远多于预期——许多是 false positive，因 base/instruct
      mismatch 导致 SAE 将 instruct-specific pattern 误解码为多个稀疏特征。
      EN 和 ZH 的 top MI features 重叠仅 8 个 (8/45 ≈ 18%)，初步看似支持 H2
      (language-specific)，但更可能是 noise + mismatch artifact。此结果在 median tier
      属于 "results noisy" 范畴，不足以支持 C5 claim。
    tables:
      - caption: "SAE conflict feature statistics (Qwen-Scope, layer 22)"
        columns: ["Metric", "EN", "ZH", "Overlap"]
        rows:
          - ["Activated features (>2σ)", "312", "256", "78"]
          - ["MI-selected (>0.15)", "45", "42", "8"]
          - ["Interpretable (manual)", "16/45", "14/42", "3/8"]
          - ["Mean activation diff (conflict-control)", "2.31", "1.87", "—"]
    figures_description:
      - "特征激活热力图: top-20 MI features × 样本 (conflict/control × EN/ZH)。大量噪声使 pattern 不清晰——作为 'noisy result' 的 honest report。"
    analysis: |
      Track 2 在 median tier 下产出 noisy 但非完全无用的结果。关键判断: base/instruct
      mismatch 是主要 noise 来源而非冲突信号不存在。论文中可报告为:
      "Preliminary SAE analysis using Qwen-Scope identified candidate conflict features,
      but the base-instruct distribution shift (cosine similarity 0.71) introduced
      substantial noise. We report these results in Appendix B with the caveat that
      SAE analysis on matched base-model activations is needed for definitive conclusions."
      此实验本身成为 Track 2 的 "learned limitation"——方法论贡献。

  - name: "LangFIR 语言特征解耦"
    plan_id: "plan_202"
    description: "LangFIR random-token filtering 识别 language-identity 特征并从 conflict features 中排除"
    expected_results:
      langfir_language_features_identified: 120
      conflict_language_overlap: 22
      overlap_rate: 0.49
      residual_conflict_features_after_filtering: 23
      residual_cross_lingual_overlap: 3
      residual_interpretability: 0.22
    result_rationale: |
      LangFIR 能较 robustly 地识别 language-identity 特征（random token 下仍激活的
      特征 → language encoding），但当 SAE 本身 noisy (plan_201) 时，conflict features
      和 language features 的 overlap 判定不可靠。overlap_rate 0.49 暗示约半数 "conflict
      features" 实际是 language features 被误标——进一步证实 plan_201 的 noise 问题。
      filtering 后剩余 23 个 conflict features 中跨语言重叠仅 3 个，可解释性更低 (22%)。
      此结果不足以支持 "conflict 和 language 特征可解耦" 的 C5 子 claim。
      在 median tier 下，此实验更多暴露了 base/instruct mismatch 的下游影响。
    tables:
      - caption: "LangFIR conflict-language feature decomposition"
        columns: ["Category", "Count", "Cross-lingual Overlap", "Interpretable"]
        rows:
          - ["All MI-selected conflict features", "45", "8 (18%)", "16 (36%)"]
          - ["Language-identity features (LangFIR)", "120", "—", "—"]
          - ["Conflict ∩ Language", "22", "—", "—"]
          - ["Residual conflict (post-filter)", "23", "3 (13%)", "5 (22%)"]
    figures_description:
      - "Venn diagram: conflict features vs language features，标注 overlap 和 residual counts。附注 base/instruct mismatch caveat。"
    analysis: |
      实验执行完整但结论受限于上游 SAE noise。不作为论文 main body 内容。
      若包含，放 Appendix B 作为 "preliminary investigation" 连同 plan_201 一起报告。
      关键 takeaway 写入 future work: "SAE analysis on base-model activations with
      matched training distribution is a critical next step."

  - name: "Cross-lingual feature Jaccard 分析"
    plan_id: "plan_203"
    description: "计算 mid vs late layer conflict feature 的跨语言 Jaccard 以检验 H1 vs H2"
    expected_results:
      jaccard_mid_layer: 0.06
      jaccard_late_layer: 0.04
      jaccard_diff: 0.02
      permutation_p_mid_vs_late: 0.38
      h1_supported: "inconclusive"
      h2_supported: "inconclusive"
    result_rationale: |
      在 median tier 下 Jaccard < 0.10 是核心假设。mid-layer 0.06 vs late-layer 0.04
      方向上支持 H1 (mid > late) 但差异极小且不显著 (p=0.38)。这是 plan_201 的 noise
      传播的必然结果: 当 individual feature 识别不可靠时，feature 间的 overlap 计算
      更不可靠。两个很小的 noisy set 的 Jaccard 天然趋近零。
      此结果不支持也不反驳 H1 或 H2——是 "inconclusive" 而非 "negative"。区别重要:
      negative result 意味着 "我们有 power 检测差异但没发现"；inconclusive 意味着
      "我们的工具精度不足以检验此假设"。
    tables:
      - caption: "Cross-lingual conflict feature Jaccard by layer group"
        columns: ["Layer Group", "Depth %", "EN features", "ZH features", "Jaccard", "Perm. p"]
        rows:
          - ["Mid (layers 10-18)", "31-56%", "38", "32", "0.06", "—"]
          - ["Late (layers 25-30)", "78-94%", "28", "24", "0.04", "—"]
          - ["Mid − Late diff", "—", "—", "—", "+0.02", "0.38"]
    figures_description:
      - "Jaccard by layer 折线图: X 轴为层，Y 轴为 per-layer Jaccard。大量波动，无清晰 trend。灰色阴影为 permutation null distribution。标题注明 inconclusive。"
    analysis: |
      Track 2 三个实验 (201→202→203) 的级联结果: 上游 noise 使最终 H1/H2 检验无效。
      这不是 failure——是 honest methodology boundary。论文 Discussion 中写:
      "Our SAE-based analysis was limited by the base-instruct distribution mismatch
      (Section B.1). The near-zero Jaccard indices reflect measurement noise rather
      than genuine absence of cross-lingual feature sharing. We consider SAE analysis
      with matched training distributions a high-priority direction for future work."
      Track 2 整体作为 Appendix B (2-3 pages)，emphasize method + limitation > results。

  # ═══ Track 3: Steering ═══

  - name: "Monolingual→cross-lingual steering transfer"
    plan_id: "plan_301"
    description: "用 SpARE 的英语冲突特征做 cross-lingual steering"
    expected_results:
      status: "not_executed"
      reason: "depends on plan_201 + plan_203; Track 2 results too noisy to select reliable steering features"
    result_rationale: |
      Track 3 依赖 Track 2 提供的 SAE conflict features 作为 steering targets。
      Plan_201 的 noisy results 意味着无法可靠选择 steering features——用 noise-dominated
      features 做 steering 实验会产出 uninterpretable 结果。在 median tier 下
      tracks_submission_ready = 1 (仅 Track 1)，Track 3 不执行是正确决策。
      plan_107 (representation steering using probe weights) 作为替代提供有限因果证据。
    tables: []
    figures_description: []
    analysis: |
      Track 3 不执行。论文 Section 6 (Discussion) 标注:
      "Track 3 steering experiments were deferred due to limitations in SAE feature
      identification (Appendix B). Probe-based representation steering (Section 4.4)
      provides preliminary causal evidence. Full SAE-based steering across language
      pairs remains an important direction for future work."

  - name: "Cross-lingual-specific steering"
    plan_id: "plan_302"
    description: "用跨语言特有特征构建 steering vectors 并与 monolingual 对比"
    expected_results:
      status: "not_executed"
      reason: "depends on plan_301 which is not executed"
    result_rationale: |
      Plan_302 依赖 plan_301 的 monolingual steering 基线。级联未执行。
    tables: []
    figures_description: []
    analysis: "同 plan_301。Track 3 整体 deferred to future work。"

  - name: "Typological steering correlation"
    plan_id: "plan_303"
    description: "Steering 有效性与 CLEAR linguistic similarity metric 的相关性"
    expected_results:
      status: "not_executed"
      reason: "depends on plan_301 + plan_103; neither fully available"
    result_rationale: |
      即使 plan_103 (EN↔JA) 完成，plan_301 未执行意味着无 steering effectiveness
      数据可与 linguistic similarity 做相关分析。此实验是 "CLEAR 因果链接" 的最终拼图，
      在 median tier 下明确归入 future work。
      替代叙事: plan_103 的 probe transfer asymmetry 跨语言对的 pattern (EN↔ZH vs
      EN↔JA) 提供 "correlational hint"——如果两个语言对的 gap 与 typological distance
      弱相关，可在 Discussion 中提及但不作为 claim。
    tables: []
    figures_description: []
    analysis: |
      Track 3 三个实验均 deferred。论文中 Track 3 仅作为 "planned future work" 出现在
      Section 6.2 (Future Directions)，与 "custom SAE training on matched distributions"
      并列为两大 follow-up 方向。这不损害 ICLR 投稿——现象发现 + 方法论贡献 + honest
      boundary delineation 是 reviewer 尊重的 pattern。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e49a24a-4940-46cb-a061-c38ddcddb0a7",
  "isSidechain": false,
  "requestId": "req_011CbGqjLyLvNANQ55ZnaVzd",
  "type": "assistant",
  "uuid": "bf5a8d11-4106-4056-8ac8-f1561c37a683",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WJLyrpToKVdQYcTiry271d",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9454,
      "cache_read_input_tokens": 24713,
      "output_tokens": 17709,
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
          "output_tokens": 17709,
          "cache_read_input_tokens": 24713,
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：第三模型方向一致但未显著，仅 Track 1，claims 需降强度但核心叙事可维持 核心假设：['第三模型不对称方向一致（ZH→EN > EN→ZH）但 CI 含零', '3/3 方向一致，仅 1/3（Llama）达统计显著', 'effect size 跨模型稳定（±2pp 内），强 consiste…",
  "leafUuid": "bf5a8d11-4106-4056-8ac8-f1561c37a683",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Median scenario planning for cross-lingual conflict detection",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：第三模型方向一致但未显著，仅 Track 1，claims 需降强度但核心叙事可维持 核心假设：['第三模型不对称方向一致（ZH→EN > EN→ZH）但 CI 含零', '3/3 方向一致，仅 1/3（Llama）达统计显著', 'effect size 跨模型稳定（±2pp 内），强 consiste…",
  "leafUuid": "bf5a8d11-4106-4056-8ac8-f1561c37a683",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Median scenario planning for cross-lingual conflict detection",
  "sessionId": "76117c84-22e3-4279-a268-ccb60fa619d7"
}
```

---
