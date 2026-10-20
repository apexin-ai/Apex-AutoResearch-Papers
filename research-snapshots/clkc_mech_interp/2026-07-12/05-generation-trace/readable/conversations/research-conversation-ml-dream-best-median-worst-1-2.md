# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/6bf3357c-1e45-4c97-82a2-815120b856b3.jsonl`
- **Structured JSON:** [`7a0547082fa1244b0648.json`](../../sessions/7a/7a0547082fa1244b0648.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T02:38:12.696Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T02:38:12.696Z",
  "sessionId": "6bf3357c-1e45-4c97-82a2-815120b856b3",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: clkc_mech_interp\nfocus: 重点评估：1) C2 不对称性 claim 在 Llama borderline 显著 + Qwen 不显著的情况下能否撑住；2) 只有 Track 1 probing 无 Track 2/3 SAE+steering 时论文贡献强度是否足够 ICLR；3) back-translation COMET 低但 ablation 排除 confounder 的 framing 是否说服审稿人\n\n## paper_framing.md\n\n# Paper Framing — clkc_mech_interp\n\n> 最后更新: 2026-05-22 | 目标: ICLR 2027 (DDL ~2026-09-24)\n\n## Core Insight\n\n多语言 LLM 中，跨语言知识冲突的检测信号可在残差流中被线性探针检测，且跨语言迁移呈现**方向性不对称**（ZH→EN >> EN→ZH ~7.2pp），该不对称性跨架构高度一致（Llama-3.1-8B 与 Qwen3-8B）。这为 CLEAR (Zhao et al. 2026) 发现的 \"entity-centric factual conflicts 中 linguistic affinity 决定冲突解决\" 提供了首个**机制层面的解释**。\n\n**注意**: CLEAR 的发现是 task-dependent 的——entity-centric factual conflicts 由 linguistic affinity 主导，reasoning-intensive tasks 由 resource abundance 主导。我们使用 ConflictQA（entity-centric），引用 CLEAR 时必须限定为 entity-centric 场景。\n\n## Narrative Structure\n\n**现象驱动的机制解释**（非 \"applying X to Y\"）：\n\n1. **Phenomenon**: CLEAR 发现在 entity-centric factual conflicts 中，linguistic affinity（而非 resource abundance）决定跨语言冲突解决，但未提供机制解释\n2. **Mechanistic question**: 冲突信号在模型内部如何编码？是 language-universal 还是 language-specific？为什么 similarity 起决定作用？\n3. **Our answer**: 通过残差流探针、SAE 特征分析、激活干预三条互补分析轨道，揭示冲突检测信号的跨语言结构——是否共享、在哪些层出现、能否用于干预\n\n**Secondary framing**: SAE-based mechanistic interpretability 工具在跨语言条件下的 stress test——probing / SAE / steering 三种工具的跨语言适用性边界\n\n## Competing Hypotheses (pre-registered)\n\n**H1 — English-anchored universal detection**:\n冲突检测信号本身是 language-independent 的（\"是否存在冲突\" 是语言无关判断），编码在 mid-layer 共享表征空间中。final-layer language transition 引入 similarity-dependent 干扰，影响 resolution 但不影响 detection。\n- 预测: mid-layer conflict feature 跨语言 Jaccard >> late-layer Jaccard (paired permutation test p < 0.05)\n- 预测: 英语探针跨语言迁移更强（英语作为训练数据主导语言，表征空间以英语为锚点）\n\n**H2 — Language-pair-specific encoding**:\n冲突特征从 mid-layer 起即为 language-pair-specific 的，linguistic distance 直接编码在冲突表征中。\n- 预测: mid-layer 和 late-layer Jaccard 无显著差异，或 mid < late\n- 预测: 探针迁移准确率与语言对 typological distance 强相关\n\n**MVP 证据倾向**:\n当前双模型结果倾向 **H1 的变体**——ZH→EN 迁移（71-72%）显著强于 EN→ZH（64-65%），暗示冲突信号以英语表征空间为锚点编码。非线性成分（MLP EN→ZH +9.2pp vs linear）提示 EN→ZH 方向的跨语言映射更复杂。\n\n## Core Claims\n\n### Claim 1: Cross-lingual conflict detectability\n**Statement**: 跨语言知识冲突信号可在残差流中被线性探针检测，准确率显著高于随机基线。\n**Evidence needed**:\n- ≥2 model architectures 的 within-language probe acc > 70% (balanced) ✅ (Llama 77.1%, Qwen 75.3%)\n- Permutation test p < 0.001 ✅ (all directions)\n- Cross-lingual transfer acc > chance (50%) with statistical significance ✅ (all directions 64-72%)\n**Status**: MVP 已验证 ✅\n\n### Claim 2: Asymmetric cross-lingual transfer\n**Statement**: 跨语言探针迁移呈方向一致的不对称：ZH→EN 迁移强于 EN→ZH（~7.2pp），效果量跨架构高度一致（Llama 显著，Qwen 方向一致但未达显著）。\n**Evidence needed**:\n- Bootstrap CI for asymmetry gap (corrected, plan_099 ✅):\n  - Llama: +7.22pp, CI [1.1%, 13.6%] — 排除零但 borderline ✅\n  - Qwen: +7.18pp, CI [-1.2%, 13.4%] — 含零，方向一致 ⚠️\n- ≥2 models show consistent effect size ✅ (7.22pp vs 7.18pp)\n- Token overlap analysis 排除词汇重叠驱动的虚假迁移 ✅ (plan_101 完成: per-sample Jaccard 3-4%, Qwen 无相关 p>0.4, Llama 显著负相关 r=-0.15 p=0.012 — RC2 排除)\n- ≥1 additional model architecture 验证跨架构一致性 ❌ (planned P0)\n**Status**: 初步验证 ⚠️ (需补 token overlap + 第三模型)\n\n### Claim 3: Direction-dependent non-linear components\n**Statement**: 跨语言冲突信号的弱迁移方向（EN→ZH）包含方向依赖的非线性成分，MLP 探针在该方向提升最大。跨架构一致方向但幅度不同（Llama +9.2pp single-seed / ~+4.7pp bootstrap-corrected, Qwen +2.3pp），暗示非线性成分与模型的跨语言对齐程度相关。\n**Evidence needed**:\n- MLP vs linear probe comparison on ≥2 models ✅ (both show EN→ZH direction gains)\n- MLP 不使用 test set 做 early stopping ✅ (已修复)\n- 控制实验排除 MLP 过拟合 ❌ (需 train/test accuracy gap 分析)\n- 解释跨架构幅度差异 (Llama 4x > Qwen) ❌ (可能与 Qwen 更强的跨语言对齐有关——ZH 训练数据占比更高)\n**Status**: 初步验证 ⚠️ (方向一致但幅度差异需解释)\n\n### Claim 4: Layer-wise conflict signal structure\n**Statement**: 冲突信号在 mid-to-upper layers 集中，峰值层在不同模型架构中占比一致（Llama ~88% depth, Qwen ~67% depth 有差异——需更多模型确认 pattern）。\n**Evidence needed**:\n- Layer-wise probe accuracy curves for ≥3 models ❌\n- Layer-wise CKA/SVCCA 量化 EN vs ZH 表征相似度 ❌\n- 与 \"Lost in Multilinguality\" 的 language transition 层对比 ❌\n**Status**: 未验证 ❌\n\n### Claim 5: Cross-lingual SAE conflict features (Track 2)\n**Statement**: SAE 特征空间中存在跨语言共享的冲突编码特征，可与 language-identity 特征解耦。\n**Evidence needed**:\n- Qwen-Scope SAE 特征分析 on Qwen3-8B-Base ❌\n- LangFIR random-token filtering 控制 ❌\n- Cross-lingual feature Jaccard 分析 ❌\n**Status**: 未开始 ❌\n\n### Claim 6: Cross-lingual conflict steering (Track 3)\n**Statement**: 通过 SAE 特征干预可以定向操控跨语言冲突解决行为。\n**Evidence needed**:\n- SpARE 框架跨语言扩展 ❌\n- Monolingual → cross-lingual steering transfer ❌\n- Steering effectiveness vs linguistic distance correlation ❌\n**Status**: 未开始 ❌ (依赖 Track 2)\n\n## Anticipated Reviewer Concerns\n\n### RC1: Translation quality confound [RESOLVED ✅]\n**Concern**: 中文翻译质量差可能导致虚假的冲突信号或迁移失败\n**Result**: Plan_105 COMET tercile ablation 证明翻译质量非 confounder。Qwen test: Low COMET (mean 0.585) → 66.35% acc, High COMET (mean 0.816) → 60.71% acc, delta=-5.64pp (反向), Fisher p=0.695。冲突信号检测不依赖翻译质量。Back-translation COMET ≥0.80 阈值过严（两步翻译天然拉低），但 ablation 实证排除了翻译质量 confound。\n**Remaining**: Llama test COMET 完成后重复此分析确认一致性。\n\n### RC2: Token overlap confound [RESOLVED ✅]\n**Concern**: 跨语言迁移可能由 EN-ZH 共享 token（数字、专有名词、标点）驱动\n**Result**: Per-sample Jaccard 仅 3-4%（type-level 10-15% 被膨胀）。Qwen 无相关 (p>0.4)，Llama 显著负相关 (r=-0.15, p=0.012, tercile Δ=-23.9pp)。高 overlap 反而降低准确率，方向与 RC2 相反。**共享 token 不驱动跨语言迁移，迁移发生在语义表示层。**\n\n### RC3: Model coverage insufficient [HIGH]\n**Concern**: 只有 2 个模型，无法声称 \"架构无关\"\n**Mitigation**: 加 ≥1 不同架构（Mistral/Gemma），验证 ~7.2pp 不对称性\n**Experiment**: P0 — additional model verification\n\n### RC4: Dataset size and diversity [MEDIUM]\n**Concern**: ConflictQA 覆盖面有限（~1000 samples/model），只有 EN-ZH 一个语言对\n**Mitigation**: Phase 1 聚焦 EN-ZH 验证核心机制，Phase 2 扩展多语言（≥1 额外语言对）\n**Experiment**: P0 — multilingual extension (EN↔JA or EN↔DE)\n\n### RC5: Linear probe expressiveness [LOW]\n**Concern**: 线性探针可能遗漏复杂非线性信号\n**Mitigation**: MLP 对比实验已完成 ✅，非线性成分已量化\n**Experiment**: Done — MLP vs Linear comparison\n\n### RC6: SAE base/instruct mismatch [MEDIUM]\n**Concern**: Qwen-Scope SAE 训练在 base model 上，用于 instruct model 分析可能失配\n**Mitigation**: Track 2 用 base model 做 SAE 分析 + 与 Track 1 instruct probe 交叉验证\n**Experiment**: Track 2 设计已考虑\n\n### RC7: Steering failure precedent [MEDIUM]\n**Concern**: \"Interpretability without actionability\" 证明 SAE steering 可能完全无效\n**Mitigation**: 知识冲突与临床分诊的 5 维差异（SpARE 已证明知识冲突场景 steering 有效）；Track 3 显式报告失败模式\n**Experiment**: Track 3 包含 negative result framing\n\n### RC8: Causal claims without intervention [HIGH]\n**Concern**: 探针只证明信号可检测，不证明因果关系\n**Mitigation**: Track 3 steering 实验提供因果证据；Track 1 permutation test 提供统计控制\n**Experiment**: Track 3 steering + representation steering (P1)\n\n## Paper Structure (Tentative)\n\n1. **Introduction**: CLEAR gap → mechanistic question → H1 vs H2 → three-track approach → key findings preview\n2. **Related Work**: Monolingual conflict mechanisms → Cross-lingual processing → SAE steering (successes & failures) → Cross-lingual SAE features\n3. **Method**: Data construction (ConflictQA + translation + verification pipeline) → Track 1 probing → Track 2 SAE analysis → Track 3 steering\n4. **Experiments & Results**:\n   - 4.1 Cross-lingual conflict detectability (C1)\n   - 4.2 Asymmetric transfer analysis (C2) + token overlap controls\n   - 4.3 Non-linear components (C3) + layer-wise structure (C4)\n   - 4.4 SAE feature analysis (C5) [if Track 2 ready]\n   - 4.5 Steering experiments (C6) [if Track 3 ready]\n5. **Discussion**: H1 vs H2 resolution → mechanism implications → limitations → connection to CLEAR\n6. **Conclusion**\n\n## Scope Control\n\n**投稿最低要求 (must-have for submission)**:\n- Claims 1-3 fully supported (cross-lingual detectability + asymmetry + non-linearity)\n- Claim 4 partially supported (layer-wise analysis on ≥2 models)\n- ≥3 model architectures\n- ≥2 language pairs (EN-ZH + one more)\n- Token overlap control\n- COMET translation quality validation\n\n**理想状态 (nice-to-have)**:\n- Track 2 SAE analysis (Claim 5)\n- Track 3 steering (Claim 6)\n- 5+ language pairs covering multiple typological families\n- Full CKA/SVCCA layer analysis\n\n**不做 (out of scope)**:\n- 10-language full CLEAR replication\n- Custom SAE training\n- MoE model analysis\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_probe_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bootstrap_asymmetry_diff_corrected: 0.0718\n    bootstrap_asymmetry_ci_corrected: '[-0.0119, 0.1341]'\n    bootstrap_asymmetry_significant_corrected: false\n    bootstrap_asymmetry_method: per_iteration_paired_diff_from_training_bootstrap_n100\n    bootstrap_asymmetry_diff_old: 0.0595\n    bootstrap_asymmetry_ci_old: '[-0.0367, 0.1481]'\n    comet_tertile_ablation:\n      conclusion: not_confounder\n      delta_high_low_pp: -5.64\n      fisher_p: 0.695\n      high_bal_acc: 0.6071\n      med_bal_acc: 0.6769\n      low_bal_acc: 0.6635\n      best_layer: 22\n      detail: Reversed direction (High COMET → lower probe acc). COMET gate can be\n        relaxed.\n- exp_id: mvp_probe_llama_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bootstrap_asymmetry_diff_corrected: 0.0722\n    bootstrap_asymmetry_ci_corrected: '[0.0110, 0.1361]'\n    bootstrap_asymmetry_significant_corrected: true\n    bootstrap_asymmetry_method: per_iteration_paired_diff_from_training_bootstrap_n100\n    bootstrap_asymmetry_diff_old: 0.1176\n    bootstrap_asymmetry_ci_old: '[0.0429, 0.1957]'\n- exp_id: llama31_en_activations\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen3_translate_zh\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: collect_en_activations_qwen3_8b\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: collect_en_activations_llama_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: translate_zh_llama_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: translate_zh_qwen\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: collect_en_act_llama_v3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: collect_en_act_qwen_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: verify_qwen3_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen_en_act_v3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: llama_zh_act\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen_zh_act\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: translate_zh_qwen_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: probe_qwen_full\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: comet_qwen\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_llama\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_qwen_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_llama_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_qwen_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_llama_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_qwen_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_llama_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: comet_qwen_v5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    death_cause: EXIT_CODE=124 timeout kill by submit_training_job (REGISTRY ONLY\n      - actual nohup processes alive)\n    restart_pid: 59412\n    restart_gpu: cuda:0\n    restart_method: nohup + TRANSFORMERS_OFFLINE=1\n    restart_time: '2026-05-21T23:15:00Z'\n    no_resume: true\n    acceleration: cuda:1 并行处理 test set (168条) - COMPLETED\n    qwen_test_completed: true\n    qwen_test_total: 168\n    qwen_test_passed: 31\n    qwen_test_pass_rate: 0.185\n    qwen_test_mean_comet: 0.7016\n    qwen_test_passed_mean_comet: 0.8503\n    qwen_train_progress: 320/798 (~40%)\n    actual_status: train still running on cuda:0 (PID 59412)\n    registry_failed_is_false_alarm: true\n- exp_id: comet_llama_v5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    death_cause: EXIT_CODE=124 timeout kill by submit_training_job (REGISTRY ONLY\n      - actual nohup processes alive)\n    restart_pid: 59571\n    restart_gpu: cuda:2\n    restart_method: nohup + TRANSFORMERS_OFFLINE=1\n    restart_time: '2026-05-21T23:15:00Z'\n    no_resume: true\n    acceleration: cuda:3 并行处理 test set (272条) - IN PROGRESS 66%\n    llama_train_progress: 300/1096 (~27%)\n    llama_test_progress: 180/272 (~66%)\n    actual_status: train on cuda:2 (PID 59571), test on cuda:3 (PID 64179)\n    registry_failed_is_false_alarm: true\n- exp_id: qwen_zh_act_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: comet_qwen_v6\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: comet_llama_v6\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-22T02:38:12.706Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T02:38:12.706Z",
  "sessionId": "6bf3357c-1e45-4c97-82a2-815120b856b3"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-22T02:38:12.733Z_

你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。

你需要同时定义 best / median / worst 三档：
1. 每档的核心假设（哪些假设成立/不成立）
2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）
3. 每档的论文叙事方向——
   - best: 原始 framing 完全成立，claims 无需调整
   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验
   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）

三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性
自行判断。但必须确保三档之间的数字和叙事逻辑一致。

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

# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）

```yaml
tiers:
  best:
    meaning: "..."
    key_assumptions: [...]
    number_ranges: {metric_a: [low, high], metric_b: [...]}
    narrative_direction: "..."
  median:
    meaning: "..."
    ...
  worst:
    meaning: "..."
    ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "70000d81-d42f-4c2f-b795-a9773d246328",
  "type": "user",
  "uuid": "aeaa8ff3-9b92-4935-bcff-64b49b926c9f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "6bf3357c-1e45-4c97-82a2-815120b856b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T02:38:12.732Z_

```json
{
  "parentUuid": "aeaa8ff3-9b92-4935-bcff-64b49b926c9f",
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
  "uuid": "88452f73-6d35-4079-8881-8ab6177f62a6",
  "timestamp": "2026-05-22T02:38:12.732Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "6bf3357c-1e45-4c97-82a2-815120b856b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T02:38:12.732Z_

```json
{
  "parentUuid": "88452f73-6d35-4079-8881-8ab6177f62a6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d25302d7-f5ee-40cc-97dd-d0e882f4a27f",
  "timestamp": "2026-05-22T02:38:12.732Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "6bf3357c-1e45-4c97-82a2-815120b856b3",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "d25302d7-f5ee-40cc-97dd-d0e882f4a27f",
  "sessionId": "6bf3357c-1e45-4c97-82a2-815120b856b3"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for clkc_mech_interp paper",
  "sessionId": "6bf3357c-1e45-4c97-82a2-815120b856b3"
}
```

---

### Assistant

_source line 8 · 2026-05-22T02:39:03.365Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to define three tiers (best/median/worst) for a Dream simulation based on their ML research project. Let me analyze the research context carefully.

Key facts from the paper framing:
1. Project: clkc_mech_interp - cross-lingual knowledge conflict mechanistic interpretability
2. Target: ICLR 2027 (DDL ~2026-09-24)
3. Current state:
   - Claim 1 (detectability): Verified ✅
   - Claim 2 (asymmetry): Llama borderline significant (CI excludes 0 but barely), Qwen not significant (CI includes 0)
   - Claim 3 (non-linearity): Direction consistent but magnitude differs across architectures
   - Claim 4 (layer-wise): Not verified
   - Claims 5-6 (SAE, steering): Not started
   - Only Track 1 (probing) done, Track 2/3 not started
   - RC1 (translation quality) resolved via COMET ablation
   - RC2 (token overlap) resolved

The main tension I'm working with is whether the asymmetry claim holds up given Llama's borderline results and Qwen's lack of significance, and whether completing just the probing track is sufficient or if the other experimental tracks are essential for the paper's narrative.

Thinking through the scenarios: best case has a third model confirming the effect with strong significance while Track 2 SAE analysis reveals interpretable cross-lingual features, letting me frame this as a genuine mechanistic explanation. More realistically, I'm looking at a consistent directional trend across models that doesn't quite reach significance everywhere, which means repositioning from "definitive mechanism" to "initial evidence with novel methodology." Worst case is the third model doesn't replicate the asymmetry at all, which would undermine the core claim.

Now I'm identifying the key metrics to track: within-language probe accuracy, cross-lingual transfer performance, the asymmetry gap itself, whether the bootstrap confidence intervals exclude zero, how many models show significant asymmetry, the MLP versus linear performance difference in the EN→ZH direction, and what the third model's asymmetry looks like. I need to structure these carefully in the YAML, particularly thinking through what ranges make sense for the third model's asymmetry gap.

Looking at realistic outcomes: best case would be the third model showing 5-10pp asymmetry that's statistically significant, with 2 or 3 models all showing the same directional effect, plus SAE features revealing shared cross-lingual conflict patterns and maybe preliminary steering results—that would support a full mechanistic explanation. More likely scenario is 3-7pp asymmetry that's borderline significant, only one model showing clear significance while all three point the same direction, and probably just Track 1 results. The framing might need to shift toward a methodology paper or a study of probing limits rather than a complete mechanistic story.

Now I'm thinking through which metrics actually matter for the YAML—the third model's asymmetry gap is the critical unknown, then how many models show statistical significance, how many show consistent directionality, and what we actually complete across the tracks.

I'm also sketching out the narrative arcs: the strongest version frames this as the first mechanistic explanation of CLEAR's conflict resolution with universal detection and architecture-validated asymmetry, while the middle ground emphasizes the robustness of the effect size even if individual model significance wavers.

For the weakest case, since the user wants to stay competitive for ICLR, I need to reposition around the methodology itself—either as a rigorous framework for cross-lingual mechanistic probing or by centering the detectability and non-linearity findings, with asymmetry as a hypothesis for future investigation rather than a core claim. strongest angle would be:
- C1 (detectability) is solid across models
- The non-linearity finding (C3) is interesting
- The methodology itself (cross-lingual probing + confound controls) is a contribution
- Reframe as "probing reveals that cross-lingual conflict signals are detectable but transfer properties are architecture-dependent" - which is actually an interesting negative/nuanced result
- Or: focus on the confound exclusion methodology as a contribution (token overlap, COMET ablation)

Let me think about what makes this worst case still ICLR-viable:
- "When does mechanistic interpretability transfer across languages?" - the probing methodology + finding that transfer is non-trivial is itself a contribution
- Position as a "Datasets and Benchmarks" or methodology paper
- Or: the detectability result itself, with proper depth across multiple models and languages is enough

Now I'm assembling the YAML with the key metrics that capture the asymmetry patterns, transfer behavior, and validation status across the models and language pairs, including the COMET ablation results the user wanted highlighted.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d25302d7-f5ee-40cc-97dd-d0e882f4a27f",
  "isSidechain": false,
  "requestId": "req_011CbGqB2AcVjpC9yhKmC1JH",
  "type": "assistant",
  "uuid": "c8661214-ba3f-48fb-88f1-9c3c18d802a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "6bf3357c-1e45-4c97-82a2-815120b856b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RA35bqumSSv3Qf3xUqUTg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11640,
      "cache_read_input_tokens": 11841,
      "output_tokens": 4174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11640,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4174,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11640
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

_source line 9 · 2026-05-22T02:39:42.869Z_

```yaml
tiers:
  best:
    meaning: "第三模型复现显著不对称 + Track 2 出初步结果，原始 framing 全线成立"
    key_assumptions:
      - "第三模型（Mistral/Gemma）ZH→EN vs EN→ZH 不对称性显著（bootstrap CI 排除零）"
      - "3/3 模型方向一致，≥2/3 达统计显著"
      - "MLP non-linearity 方向在第三模型复现"
      - "Llama COMET tercile ablation 复现 Qwen 的 not_confounder 结论"
      - "Track 2 SAE 在 Qwen-Scope 上识别出跨语言共享 conflict feature（Jaccard > 0.15）"
      - "≥1 额外语言对（EN-JA 或 EN-DE）方向一致"
    number_ranges:
      third_model_asymmetry_gap_pp: [5.0, 12.0]
      significant_asymmetry_models_of_3: [2, 3]
      consistent_direction_models_of_3: [3, 3]
      third_model_within_lang_acc: [0.72, 0.82]
      cross_lingual_transfer_acc_range: [0.63, 0.75]
      mlp_gain_weak_direction_pp_third_model: [3.0, 10.0]
      sae_cross_lingual_jaccard_mid_layer: [0.15, 0.35]
      lang_pairs_validated: [2, 3]
      tracks_submission_ready: [1, 2]  # Track 1 full + Track 2 partial
    narrative_direction: >
      原始 framing 完全成立：CLEAR entity-centric 冲突解决的首个机制解释。
      C2 不对称性从 "consistent trend" 升级为 "statistically robust cross-architecture phenomenon"，
      英语锚点假说（H1 变体）获三模型+多语言对支持。
      Track 2 SAE 提供 feature-level 证据补强因果叙事，部分缓解 RC8（无 intervention 的因果 claim）。
      论文定位：mechanistic interpretability + cross-lingual，双社区贡献。

  median:
    meaning: "第三模型方向一致但未显著，仅 Track 1，claims 需降强度但核心叙事可维持"
    key_assumptions:
      - "第三模型不对称方向一致（ZH→EN > EN→ZH）但 CI 含零"
      - "3/3 方向一致，仅 1/3（Llama）达统计显著"
      - "effect size 跨模型稳定（±2pp 内），强 consistency argument"
      - "Llama COMET ablation 复现 not_confounder"
      - "Track 2 SAE 未完成或结果 noisy（Jaccard < 0.10）"
      - "额外语言对仅 1 对，方向一致但样本量不足以单独显著"
    number_ranges:
      third_model_asymmetry_gap_pp: [2.0, 7.0]
      significant_asymmetry_models_of_3: [1, 1]
      consistent_direction_models_of_3: [3, 3]
      third_model_within_lang_acc: [0.68, 0.77]
      cross_lingual_transfer_acc_range: [0.60, 0.72]
      mlp_gain_weak_direction_pp_third_model: [1.0, 5.0]
      sae_cross_lingual_jaccard_mid_layer: [0.0, 0.10]  # noisy or N/A
      lang_pairs_validated: [1, 2]
      tracks_submission_ready: [1, 1]  # Track 1 only
    narrative_direction: >
      C2 从 "significant asymmetry" 调整为 "remarkably consistent effect size across architectures 
      (7.2±0.5pp) despite varying statistical power"——强调 effect size stability 而非 p-value。
      引用 Cumming (2014) "new statistics" 框架，effect size + CI 报告优于 NHST。
      C1（detectability）升级为主 claim，C2 降为 strong supporting evidence。
      Track 1 only 的贡献度靠深度弥补：layer-wise 分析 + confound exclusion pipeline 
      (token overlap + COMET ablation) 作为方法论贡献。RC8（因果 claim）明确限定为 
      "correlational evidence consistent with H1"，将 causal verification 列为 future work。
      论文定位：phenomenon characterization + methodology，仍 ICLR-viable 但需 
      supplementary experiments 充实 appendix（更多 ablation、error analysis）。

  worst:
    meaning: "第三模型不对称消失或反转，核心 C2 claim 崩塌，需重新定位论文 angle"
    key_assumptions:
      - "第三模型不对称 <2pp 或方向反转（EN→ZH > ZH→EN）"
      - "仅 Llama 显著，Qwen+第三模型均不显著，方向不全一致"
      - "不对称性可能是 Llama 训练数据分布的 artifact 而非通用机制"
      - "Track 2/3 均无法在 DDL 前完成"
      - "COMET ablation 在 Llama 上出现与 Qwen 不一致的方向（质量确实影响 Llama）"
    number_ranges:
      third_model_asymmetry_gap_pp: [-3.0, 2.0]
      significant_asymmetry_models_of_3: [0, 1]
      consistent_direction_models_of_3: [1, 2]
      third_model_within_lang_acc: [0.65, 0.75]
      cross_lingual_transfer_acc_range: [0.58, 0.70]
      mlp_gain_weak_direction_pp_third_model: [-1.0, 3.0]
      sae_cross_lingual_jaccard_mid_layer: [0.0, 0.0]  # not available
      lang_pairs_validated: [1, 1]
      tracks_submission_ready: [1, 1]
    narrative_direction: >
      C2 不对称性降级为 observation，不再作为核心 claim。Reframe 路径（按优先级）：
      
      Path A "Architecture-dependent cross-lingual conflict processing"——
      不对称性的存在与否本身取决于架构/训练数据，这是一个 finding 而非 failure。
      主 claim 变为：冲突信号跨语言可检测（C1 robust），但迁移特性是架构依赖的，
      揭示多语言 LLM 内部跨语言对齐程度的异质性。引用 Wendler et al. (2024) 
      "Llamas Know What GPTs Don't Show" 的跨架构差异发现，定位为该方向的机制扩展。
      
      Path B "Cross-lingual probing methodology + negative result"——
      聚焦 confound exclusion pipeline（token overlap 分析 + COMET ablation）作为 
      方法论贡献，不对称性作为 "hypothesis tested and bounded" 的严格实验。
      引用 Rogers et al. "negative results in NLP" 框架。
      
      两条路径均保持 ICLR 目标：Path A 走 empirical analysis track，
      Path B 需要显著加厚实验密度（5+ 模型、3+ 语言对）补偿 claim 强度下降。
      关键：worst 情况下 C1 仍然成立（within-lang acc 65-75%，均远超 chance），
      论文不会 "没东西可写"，只是叙事重心从 mechanism 转向 characterization。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8661214-ba3f-48fb-88f1-9c3c18d802a3",
  "isSidechain": false,
  "requestId": "req_011CbGqB2AcVjpC9yhKmC1JH",
  "type": "assistant",
  "uuid": "0f11f0ba-93bb-4911-bdbb-9d7579d36708",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42",
  "sessionId": "6bf3357c-1e45-4c97-82a2-815120b856b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RA35bqumSSv3Qf3xUqUTg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11640,
      "cache_read_input_tokens": 11841,
      "output_tokens": 4174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11640,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4174,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11640
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "0f11f0ba-93bb-4911-bdbb-9d7579d36708",
  "sessionId": "6bf3357c-1e45-4c97-82a2-815120b856b3"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for clkc_mech_interp paper",
  "sessionId": "6bf3357c-1e45-4c97-82a2-815120b856b3"
}
```

---
