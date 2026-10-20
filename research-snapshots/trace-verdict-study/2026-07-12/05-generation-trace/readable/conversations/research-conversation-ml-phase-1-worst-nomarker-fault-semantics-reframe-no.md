# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：nomarker 实验显著退化，暴露格式标记是主要机制；原始 'fault semantics' 叙事不成立，需要 reframe 核心假设：['no

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/1723cae9-4a61-47ee-b162-e2fd329daf4b.jsonl`
- **Structured JSON:** [`379af2ec603a6a56ffd7.json`](../../sessions/37/379af2ec603a6a56ffd7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T16:08:52.756Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T16:08:52.756Z",
  "sessionId": "1723cae9-4a61-47ee-b162-e2fd329daf4b",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：nomarker 实验显著退化，暴露格式标记是主要机制；原始 'fault semantics' 叙事不成立，需要 reframe\n核心假设：['nomarker 实验 <90%（或 3-seed 高方差，worst seed <85%）：移除格式标记后大幅退化，证明模型主要依赖 format pattern 而非 exception content semantics', 'CodeLlama-13B VOTA ≥ exception_only：大模型上 VOTA 不劣于 exception，Claim 3 层级关系 model-specific', \"'Exception events as fault detection' 叙事被削弱为 'format marker as classification shortcut'——接近 regex B5 (99.33%) 的机制\", '审稿人可以 legitimately argue: SFT 学到的是 [No exception data in trace] 有无 → pass/fail 映射，与 regex 无本质区别']\n关键指标范围：{'nomarker_accuracy_3seed_mean': [0.85, 0.949], 'nomarker_accuracy_worst_seed': [0.8, 0.93], 'codellama13b_vota_accuracy': [0.99, 1.0], 'cross_family_exception_dominance_pp': [-5.0, 0.0], 'format_marker_contribution_pp': [5.0, 15.0]}\n叙事方向：原始 'fault semantics' framing 不成立。Reframe 为：**trace formatting as implicit task specification** — 论文贡献变为揭示 SFT 中 format/structure choices 对 downstream classification 的 outsized impact。核心 insight 转向：(1) verdict prediction 本质是 format-sensitive binary classification, (2) 结构化标记（如 [ERROR]）acts as implicit label that SFT exploits, (3) 设计 trace format 时应显式考虑 downstream task 的 shortcut affordance。Claim 1 重写为 'structured format markers dominate verdict prediction in exception traces'。Claim 3 重写为 'format engineering > content richness for SFT verdict tasks'。仍冲 EMNLP Main——angle 从 'positive finding about exception semantics' 变为 'cautionary finding about SFT shortcut learning + practical design principle'，与 shortcut learning literature (NLI artifacts, annotation artifacts) 对话。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: trace-verdict-study\n\n## paper_framing.md\n\n# Paper Framing — trace-verdict-study\n\n> v3.0 — [UPDATED 2026-05-15] D030 CLOSED: DeepSeek VOTA 84.45% confirmed correct (confirmatory re-eval). **Critical narrative fix**: to_chat_text() preserves labels → VOTA 训练时 verdict label 未被截断 → 论文中 \"label truncation/corruption\" 措辞对 VOTA 不成立。正确叙事: trace INPUT content 被截断 (91.7% samples), 84.45% 反映 trace information loss。新增 D11: VOTA cross-model gap confounded by training-time truncation。数据集来源：HumanEval (164) + MBPP-sanitized (427) = 591 problems × 10 LLM-generated solutions = 5910 samples。\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026\n\n## Core Insight\n\nVerdict prediction (pass/fail) is fundamentally a **fault detection** task. The most effective signal is the **exception event** — a compact, structured diagnostic moment that consistently outperforms all other trace representations across models (Qwen 99.83% ± 0.00 across 3 seeds; DeepSeek 91-99% depending on seed, but always > VOTA 84.45% and no_trace 73.36%). In contrast, richer trace representations that require deeper execution reasoning show model-dependent effectiveness: VOTA gap = 14.96pp, no_trace gap = 1.77pp. Information density — not training signal distribution — is the primary bottleneck: even oracle loss masking (label-only) cannot close the 13pp gap between full traces and targeted extraction. The design principle: **extract the highest-specificity diagnostic signal; discard everything else.** Cross-model absolute performance depends on LoRA initialization stability, but exception_only's relative dominance over other components is robust.\n\nVOTA's primary contribution is **fault indicator isolation** — automatically extracting exception events from noisy full traces — rather than generic trace compression. The \"compression helps\" narrative was a stepping stone; the real mechanism is diagnostic signal extraction.\n\n## Core Claims (3)\n\n### Claim 1: Exception events are the most effective trace component for verdict prediction\n\nException summaries consistently achieve the highest verdict prediction accuracy across both models tested, outperforming all other trace representations in every seed. On Qwen-2.5-Coder-7B, performance is perfectly robust: 99.83% ± 0.00 (3 seeds). On DeepSeek-Coder-6.7B, absolute accuracy is seed-dependent (seed42=99.83% epoch1, seed123=91.43% epoch1; Δ=8.40pp), consistent with LoRA initialization sensitivity — but exception_only still dominates VOTA (84.45%) and no_trace (73.36%) in all seeds. This contrasts with VOTA (cross-model gap = 14.96pp) and no_trace (gap = 1.77pp). Exception events are structurally simple (`[ERROR] type: ... message: ...`) and do not require deep trace reasoning.\n\n**Supporting evidence:**\n- `vota_exception_only_seed42_v2`: Qwen 99.83%, ECE=0.0027\n- `deepseek_exception_only_seed42`: DeepSeek 99.83% (epoch1) / 99.33% (epoch3)\n- `deepseek_exception_only_seed456`: DeepSeek 99.33% (epoch3), CI [98.82, 99.75] — 与 seed42 完全一致\n- `deepseek_exception_only_seed123`: DeepSeek 91.43% (epoch1) / 91.09% (epoch3) — LoRA init sensitivity outlier\n- `deepseek_vota_seed42`: DeepSeek VOTA 84.45% (gap = 14.96pp vs Qwen)\n- `deepseek_no_trace_seed42`: DeepSeek no_trace 73.36% (gap = 1.77pp vs Qwen)\n- `vota_no_ae_seed42`: 99.41% — actual/expected removal 不降，非 trivial string comparison\n\n**DeepSeek seed analysis** ✅ (FINALIZED, D029):\n\n| Seed | Epoch 3 (final) | fail_recall | pass_recall | train_loss | Errors | CI |\n|------|-----------------|-------------|-------------|------------|--------|-----|\n| 42   | 99.33%          | 1.0         | 0.9906      | —          | 8/1190 | — |\n| 456  | 99.33%          | 1.0         | 0.9906      | 0.1225     | 8/1190 | [98.82, 99.75] |\n| 123  | 91.09%          | 0.705       | 0.993       | 0.122      | —      | [89.4, 92.6] |\n\nseed42 与 seed456 结果**完全一致**（均 8/1190 错误，99.33%），seed123 为离群值。seed123 的 fail_recall 仅 0.705 — LoRA 初始化落入差的局部最优，未充分学到 exception→fail 映射。**关键发现**: seed456 和 seed123 的 train_loss 几乎相同（0.1225 vs 0.122），但 accuracy 差 8.2pp — token-level loss 掩盖了 sample-level 分类能力的巨大差异（详见 D10）。\n\n**Irreducible error analysis** ✅: 3 seeds 错误的 2 个样本 (id=901, 905) 均来自 HumanEval/95 (`check_dict_case`)，根因为 Python `all()` 对 generator expression 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误）。tracer 将其标记为 `[ERROR]`，exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。整个 1190 条测试集仅这 2 条含 `GeneratorExit`，模型无训练信号学习其良性本质。**这确认 99.83% 是 exception_only 表征的理论上限，剩余 0.17% 是 representation-inherent irreducible error，而非模型不足。**\n\n**Seed robustness** ✅: Qwen exception_only 3-seed 完全一致，构成本文最强 robustness 证据：\n\n| Seed | Accuracy | 95% CI | Errors |\n|------|----------|--------|--------|\n| 42 | 99.83% | [99.58, 100] | 2/1190 |\n| 123 | 99.83% | [99.58, 100] | 2/1190 |\n| 456 | 99.83% | [99.58, 100] | 2/1190 |\n\n3 seeds 错误样本 100% 重叠（id=901, 905, 均为 `check_dict_case` 函数, label=pass → pred=fail）。**Irreducible samples**: 模型已达数据集理论上限，variance = 0。\n\n**DeepSeek cross-model** ✅ (D029): 3-seed 完整数据 — seed42/456=99.33%, seed123=91.09%。2/3 seeds 鲁棒，seed123 为 LoRA 初始化离群值（fail_recall 仅 0.705）。Qwen 3-seed 完美稳定 (99.83% ± 0.00) vs DeepSeek 高方差（σ≈4.8pp），暗示 exception signal 的 learnability 与模型 LoRA 训练稳定性相关。但即使最差 seed (91.09%) 仍优于 VOTA (84.45%) 和 no_trace (73.36%)，relative dominance robust。\n\n### Claim 2: Information density, not gradient dilution, drives trace compression benefit\n\nFull traces help verdict prediction (81.76% [`full_trace_seed42_v5`], +6.6pp over baseline), but VOTA achieves 99.41% [`vota_seed42_v5`] (+24.3pp) — a +17.6pp advantage. Label-only loss ablation (plan_002) quantifies the causal decomposition: **gradient dilution contributes ~26% of the gap** (4.5pp; label-only full_trace = 86.22% [`full_trace_label_only_seed42`]), **information overload contributes ~74%** (13.0pp; only trace compression resolves this). Even with oracle loss masking that eliminates gradient dilution, full traces still underperform VOTA by 13pp.\n\nCross-model evidence reinforces this: VOTA gap (14.96pp) partly tracks base model execution reasoning capability (Qwen CRUXEval-I 56.5% vs DeepSeek 39.0%, Δ=17.5pp), though **confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated to ~2048 tokens; see D11). The two factors cannot be disentangled in the current design. Exception signal partially bypasses both bottlenecks (token-short, no truncation; consistently best component on both models), though DeepSeek shows seed-dependent absolute performance (91-99%).\n\n**Supporting evidence:**\n- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (gradient dilution fix, +4.5pp over standard full_trace)\n- `full_trace_seed42_v5`: 81.76%, ECE=0.0958 (standard full_trace)\n- `vota_seed42_v5`: 99.41%, ECE=0.0054\n- `deepseek_vota_seed42`: 84.45% (VOTA model-dependent)\n- CRUXEval literature data (Wang et al.)\n\n### Claim 3: Two-tier diagnostic hierarchy for verdict prediction\n\nComponent ablation reveals verdict-relevant trace information has a strict two-tier hierarchy:\n- **Tier 1 — diagnostic moment signals**: exception summaries (99.83% [`vota_exception_only_seed42_v2`]) and assertion-point information (99.92% [`vota_ae_only_seed42`]) are individually near-perfect and sufficient for verdict prediction on Qwen. These signals are structurally simple and consistently the most effective component on both models, though DeepSeek absolute performance is seed-dependent.\n- **Tier 2 — behavioral patterns**: loop compression (85.63% [`vota_loop_only_seed42`]) carries substantial signal but is model-dependent and fully subsumed by Tier 1.\n\nCombining tiers introduces noise rather than helping: exception_only (99.83%) > VOTA full (99.41%), p=0.01. Loop_only ≈ full_trace_label_only (85.63% vs 86.22%) confirms VOTA's loop compression precisely extracts the useful behavioral signal from full traces.\n\n**Supporting evidence:**\n- `vota_exception_only_seed42_v2`: 99.83%, ECE=0.0027 (Tier 1 exception)\n- `vota_ae_only_seed42`: 99.92%, ECE=0.0004 (Tier 1 assertion-point, 与 exception 统计等价 p=0.80)\n- `vota_loop_only_seed42`: 85.63%, ECE=0.0831 (Tier 2 behavioral)\n- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (≈ loop_only, confirming extraction equivalence)\n- `deepseek_exception_only_seed42`: 99.83% epoch1 / 99.33% epoch3 (Tier 1 cross-model validation)\n- `deepseek_vota_seed42`: 84.45% (Tier 1+2 cross-model: Tier 2 introduces model-dependent degradation)\n\n**Calibration**: 完整 calibration 数据确认 Tier 1 信号不仅 accuracy 近完美，置信度校准也近完美：\n\n| Condition | Accuracy | ECE | Brier | 解读 |\n|-----------|----------|-----|-------|------|\n| ae_only | 99.92% | 0.0004 | 0.0008 | 近乎完美校准 |\n| exception_only | 99.83% | 0.0027 | 0.0013 | 近乎完美校准 |\n| VOTA | 99.41% | 0.0054 | 0.005 | 优秀，但 Tier 2 引入轻微 noise |\n| loop_only | 85.63% | 0.0831 | — | Tier 2 单独校准中等 |\n| label_only | 86.22% | 0.1107 | — | gradient dilution fix 仍 miscalibrated |\n| full_trace | 81.76% | 0.0958 | — | 中度 miscalibrated |\n| no_trace | 75.13% | 0.1715 | 0.1972 | 严重 miscalibrated |\n\nno_trace ECE 是 exception_only 的 **~63x**（0.1715/0.0027），Brier 是 **~150x**（0.1972/0.0013）。Trace signal（尤其 Tier 1）不仅提升 accuracy，更从根本上改善模型 calibration。\n\n**Design principle**: verdict-optimized traces should extract highest-specificity diagnostic signals; lower-specificity signals are redundant and may introduce noise.\n\n## Cross-Model Evidence Summary\n\n| Condition | Qwen-2.5-Coder-7B | DeepSeek-Coder-6.7B | Cross-model gap | Interpretation |\n|-----------|-------------------|---------------------|-----------------|----------------|\n| exception_only | 99.83% ± 0.00 (3 seeds) | seed42/456: 99.33%; seed123: 91.09% | 0.50-8.74pp (seed-dependent) | **Best component on both models**; 2/3 DeepSeek seeds match Qwen-level; 1 outlier still > VOTA |\n| VOTA | 99.41% | 84.45% | -14.96pp | Model-dependent — requires execution reasoning; **also confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated from mean 2626 to ~2048 tokens; labels preserved via to_chat_text(), see D11) |\n| no_trace | 75.13% | 73.36% | -1.77pp | Baseline gap tracks general capability |\n| full_trace | 81.76% | collapsed (v3 pending) | N/A | DeepSeek v1 label truncation bug |\n\n**Key insight**: Exception_only is consistently the best component on both models (even worst DeepSeek seed 91.09% > VOTA 84.45%). Cross-model gap 与 signal complexity 正相关, but exception signal's absolute effectiveness also depends on LoRA training stability. Qwen: perfectly robust (3 seeds identical). DeepSeek: 2/3 seeds at 99.33% (matching Qwen-level), 1 outlier at 91.09% (LoRA initialization). Median performance robust; seed sensitivity suggests smaller/weaker models may need training stabilization (multi-seed selection, warmup tuning) for optimal exception signal utilization.\n\n## VOTA Repositioning\n\n**旧叙事**: VOTA 是 trace compression 方法，价值在于\"压缩使 trace 更有效\"。\n\n**新叙事**: VOTA 是 **fault indicator isolation** 方法，核心价值在于自动从 noisy execution traces 中提取 exception events 等 diagnostic signals。\n\n**证据链**:\n1. exception_only (99.83%) ≥ VOTA full (99.41%) — 压缩后的其他组件（loop, ae）不仅无益，反而引入 noise\n2. VOTA 跨模型 gap = 14.96pp — 因为 VOTA 包含 model-dependent 的 Tier 2 组件（loop compression 需要 execution reasoning）\n3. exception_only 在两个模型上均为最优组件 — isolate 出 Tier 1 后，相对优势 robust（虽然 DeepSeek 绝对值 seed-dependent）\n4. vota_no_ae (99.41%) = VOTA (99.41%) — actual/expected 移除无影响，exception 是真正的 active ingredient\n\n**论文中的表述**: \"VOTA's trace compression pipeline incidentally isolates exception events — the minimal sufficient diagnostic signal. Its value lies not in making traces shorter, but in separating high-specificity fault indicators from low-specificity behavioral patterns.\"\n\n**对 Method section 的影响**: VOTA 仍然完整描述（loop compression + exception + actual/expected），但 Results/Discussion 明确指出 exception isolation 是核心机制，其他组件是 model-capability-dependent bonus。\n\n## Story Spine\n\n- **Problem**: Existing trace SFT studies (DCSH, TracePile) evaluate only generative tasks and find limited, model-dependent benefit. No prior work has tested trace SFT on verdict tasks (binary pass/fail), nor identified what trace components drive classification performance.\n\n- **Existing approaches & gaps**: DCSH (EMNLP Findings 2025) tested 5 trace formats on generation tasks, finding that \"no single trace representation consistently outperforms others.\" TracePile (NeurIPS 2025) scaled to 2.6M samples but only evaluated generation. TRACED (ICSE 2024) showed traces help encoder-based classification. All existing trace formats are designed for execution simulation, not fault detection.\n\n- **Our framing**: We reframe verdict prediction as **fault detection** and ask: what is the minimal sufficient diagnostic signal? Through systematic component ablation across two architecturally distinct models, we discover that exception events — compact, structured error summaries — are consistently the most effective trace component, achieving near-perfect accuracy on Qwen (99.83% ± 0.00, 3 seeds) and outperforming all alternatives on DeepSeek (91-99% vs VOTA 84.45%). Richer trace representations work only when the base model has sufficient execution reasoning capability, making them unreliable for general deployment.\n\n- **Headline result**: \"Exception events consistently achieve the highest verdict accuracy across models (Qwen 99.83%, DeepSeek 91-99%), outperforming VOTA traces (84.45% on DeepSeek, -14.96pp gap) — demonstrating that fault indicator isolation, not trace reasoning, is the robust mechanism for verdict prediction. DeepSeek seed sensitivity reveals LoRA training stability as a secondary factor for smaller models.\"\n\n## Story Arc\n\n1. **Setup**: Trace SFT for code tasks — promising but inconsistent in prior work (DCSH, TracePile). Unknown whether traces help verdict tasks and what trace design matters.\n\n2. **First result — traces help, compression helps more** (single model): no_trace 75.13% → full_trace 81.76% → VOTA 99.41%. Label-only loss ablation decomposes the gap: 26% gradient dilution, 74% information overload. Compression improves accuracy through higher information density, not just cost savings.\n\n3. **Twist — what component actually drives VOTA?** Component ablation reveals exception_only (99.83%) ≥ full VOTA (99.41%). The \"trace reasoning\" narrative is wrong — verdict prediction is fault detection. Tier 1 (exceptions + assertion-point) subsumes Tier 2 (loops). Actual/expected removal doesn't hurt (99.41%).\n\n4. **Cross-model stress test — consistent dominance, not universal perfection**: Exception_only is the best component on both models (even DeepSeek worst seed 91.09% > VOTA 84.45%), but absolute performance is seed-dependent on DeepSeek (91-99% vs Qwen's perfectly stable 99.83%). VOTA degrades by 14.96pp. The structurally simplest component is the most robust, but LoRA initialization sensitivity introduces variance on weaker models. Qwen seed robustness (3-seed variance = 0) + calibration (ECE=0.0027) 确认 exception signal 在强模型上的 reliability。DeepSeek seed sensitivity 揭示 training stability 作为 secondary bottleneck。\n\n5. **Design principle**: For verdict tasks, identify the highest-specificity diagnostic signal (exception events) and discard everything else. VOTA's value is fault indicator isolation — automatically extracting exceptions from noisy traces — not generic compression. Simpler signals are more robust; complexity tolerance depends on model capability.\n\n## Dataset Characteristics\n\n### Data duplication analysis\n\n| Condition | Total | Unique | Duplication rate | Cause |\n|-----------|-------|--------|------------------|-------|\n| exception_only_train | 4720 | 2858 | 39.45% | 同题多个 passing 解映射为相同 (input, output) — 无异常 → 同一 trace |\n| exception_only_test | 1190 | 607 | 48.99% | 同上 |\n| raw_traces | 5910 | 5803 | 1.81% | 完整 trace 含行号/变量值/内存地址，几乎不重复 |\n\n**Train-test input overlap: 0（无数据泄漏）**\n\n**解读**: exception_only 高重复率是 representation 的自然属性，非数据问题。多个正确解对同一测试用例执行时若均无异常，exception_only 表征退化为相同的空/无异常标记。这恰好说明 exception signal 的 compactness — 它仅编码 fault presence，不编码 solution identity。raw_traces 重复率极低 (1.81%) 因为完整 trace 包含 solution-specific 信息（变量值、内存地址）。尽管高重复率意味着有效训练样本少于名义数量，模型仍达 99.83% — 进一步确认 exception signal 的 learnability。\n\n## DeepSeek full_trace 处理\n\n**现状**: v1 坍塌（28.5%, 100% 预测 fail, 根因: 训练端 label 截断）。v2 重训启动但被 kill（Loop #6 ops worker 腾 GPU 给 vota_seed456）。v3 RUNNING（label-preserving truncation fix）。\n\n**处理方案**: v3 正在 cuda:0 上训练，预计 5/16 完成。\n\n**VOTA vs full_trace 截断机制区分** (D030 token analysis 确认):\n- **full_trace v1**: SFTTrainer right-truncation 切掉了 verdict **label** → 100% predict fail → 坍塌。根因: DeepSeek tokenizer 对 full_trace 产生 >2048 tokens, label 在截断窗口外。\n- **VOTA**: `to_chat_text()` 保留 verdict label（label 完整），但 91.7% 的样本 **trace content（input）被截断**（mean 2626 → ~2048 tokens）。84.45% 是真实结果，反映 trace 信息损失对模型学习的影响，**不是** label corruption。\n- **exception_only**: token 长度远低于 2048，不受截断影响，跨模型对比 clean。\n\n**对论文叙事的影响**: 论文中所有 \"right-truncation corrupts/removes the verdict label\" 措辞**对 VOTA 不成立**——label 完整保留，被截断的是 trace input。正确表述: \"trace content truncation causes information loss\"。VOTA cross-model gap (14.96pp) 有两个贡献因素: (1) model capability, (2) training-time trace truncation on DeepSeek (see D11)。\n\n## External Benchmark (DebugBench) Positioning\n\n**DebugBench 仅作泛化性验证，不作 trace importance 证据。**\n\n| Condition | Main Dataset | DebugBench | Δ interpretation |\n|-----------|-------------|------------|------------------|\n| no_trace | 75.13% | 96.71% | DebugBench 天花板高，baseline 已强 |\n| VOTA | 99.41% | 99.77% | +3.06pp lift — 边际 |\n| exception_only | 99.83% | 100.00% | +3.29pp lift — 边际 |\n\n**主数据集 trace lift = 24.70pp**（no_trace → exception_only），DebugBench trace lift 不到其 1/7。\n\n**论文定位规则**：\n- DebugBench → 泛化性证据（exception_only 100% = 跨数据集鲁棒性）\n- Trace importance 论证 → 仅依赖主数据集（24.7pp lift）\n- 禁止用 DebugBench 的 3.29pp lift 论证 \"trace 的核心价值\"——审稿人会攻击天花板效应\n\n## Venue Fit Risks\n\n| Risk | Assessment | Mitigation |\n|------|-----------|------------|\n| 单任务 | 仍然只在 test verdict prediction 上验证 | 跨模型验证部分弥补; Discussion 中讨论 generalization |\n| 单数据集 | HumanEval + MBPP-sanitized 是唯一数据源 (591 problems × 10 solutions) | 定位为 empirical study, 深度优于广度; 两个标准 benchmark 组合覆盖多样编程题型; exception_only 有效训练样本仅 2858 unique 即达 99.83%, 暗示 signal 的 simplicity 降低对数据量的依赖 |\n| \"只是 feature engineering\" | exception extraction 不复杂 | simplicity 本身是 contribution — 最简信号最 robust |\n| Negative result 味道 | VOTA 跨模型不 robust | Reframe: 识别 robust vs non-robust 组件边界是 positive |\n| Seed robustness (Qwen) | ✅ 已解决: 99.83% ± 0.00 (3 seeds), irreducible samples 确认 | — |\n| Seed robustness (DeepSeek) | ✅ 3-seed 完整: 2/3 at 99.33%, 1 at 91.09% | LoRA initialization sensitivity — median robust, worst still > all alternatives; 转化为 training stability finding (D9/D10) |\n| Calibration | ✅ 完整数据: Tier 1 ECE≤0.003, no_trace ECE=0.171 (~63x gap) | Brier ~150x gap 进一步确认 |\n| 只用 2 个模型 | 有限但有意义的 diversity | Architecture + pretraining data (5.5T vs 2T) + CRUXEval gap (17.5pp) 构成充分差异 |\n| 数据重复率 | exception_only 训练集 39.45% 重复 | 非数据泄漏（train-test overlap = 0）；是 representation compactness 的自然结果；有效样本仍足够学习 |\n\n## Anticipated Reviewer Concerns\n\n| Concern | Planned Response |\n|---------|-----------------|\n| \"exception_only 99.83% 是不是 trivial pattern matching [ERROR] 有无？\" | full_trace 也包含 [ERROR] 但仅 81.76%——模型需要从 trace context 中 extract 和 utilize exception signal, 不是简单 keyword detection. no_trace 无 exception, 75.13%. |\n| \"为什么 exception_only > VOTA? adding info 反而降?\" | 非 exception 组件 (loop/ae tokens) 稀释 attention 对 exception 信号的聚焦. Calibration: exception_only ECE=0.0027 vs VOTA ECE=0.0054. 部分样本 loop 正常但有 exception, 引入矛盾信号. |\n| \"CRUXEval gap 与 VOTA gap 的相关性可能是 coincidence\" | 明确标注为 hypothesis. 列出 alternatives (tokenizer efficiency, pretraining scale 2.75x, chat template). 不 overclaim. |\n| \"只有 2 个模型，universality claim 太强\" | 同意是 limitation. 两模型在 architecture (RoPE vs ALiBi), pretraining data (5.5T vs 2T), execution reasoning (CRUXEval 17.5pp gap) 上有充分差异, 不是 trivial replication. Exception signal 的 structural simplicity 提供 inductive argument for broader generalization. |\n| \"99.83% 可能 saturated, 看不出 exception 到底学了什么\" | Calibration 双指标: exception_only ECE=0.0027, Brier=0.0013 (近完美校准). 对比 no_trace ECE=0.1715, Brier=0.1972 (~63x/~150x gap). **Irreducible error 根因已明确**: 2/1190 errors 均因 Python `all()` 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误），tracer 将其标记为 `[ERROR]`。模型看到 7 行 `[ERROR] GeneratorExit` 合理预测 fail，但代码实际正确。整个测试集仅这 2 条含 `GeneratorExit`，无训练信号可学习其良性本质。99.83% 是 representation 的理论上限，非 saturation artifact。 |\n| \"只用了 1 个 seed\" | Qwen ✅: 3 seeds 99.83% ± 0.00. DeepSeek ✅: 3 seeds 完整 — seed42/456=99.33%, seed123=91.09%。2/3 鲁棒，1 离群。median=99.33%, worst=91.09% (仍 > VOTA 84.45%)。论文透明报告所有 seeds，将 seed sensitivity 转化为 LoRA training stability 的 finding（D9）。 |\n| \"eval_loss 上升但 accuracy 提升——checkpoint selection 有问题?\" | Discussion D1: token-level loss 与 binary verdict accuracy 解耦. 推荐 verdict-specific metric. Methodological contribution. |\n| \"DeepSeek full_trace 坍塌是 bug 不是 finding\" | 诚实披露根因 (训练端 label 截断). 其他 3 条件不受影响. 修复版本如就绪则补入. |\n| \"calibration 数据只有 1 个 seed\" | Seed robustness 已证明 accuracy variance=0 (3 seeds), calibration 在 accuracy 完全一致的前提下 expected 也一致. ECE/Brier 的极小值 (0.0027/0.0013) 留有极小 variance 空间. |\n| \"DeepSeek epoch1 > epoch3, 为什么用 epoch3 报告?\" | 正文报告所有 seeds 的 final + best checkpoint。seed42: epoch1=99.83%, epoch3=99.33%。seed123: epoch1=91.43%, epoch3=91.09%。D7 讨论 early stopping + D9 讨论 LoRA initialization sensitivity。不 cherry-pick best seed。 |\n| \"DeepSeek seed sensitivity 说明 exception signal 不 robust\" | Exception_only 在所有 seeds 上仍优于其他条件（worst seed 91.09% > VOTA 84.45%）。Seed sensitivity 是 LoRA training 问题而非 signal 问题——Qwen 3 seeds 完美证明 signal 本身 robust。D9 讨论 training stabilization 作为 practical recommendation。 |\n| \"exception_only 数据集 ~40-49% 重复，有效训练样本不足？\" | 重复源自 representation compactness：同题多个 passing 解均无异常 → 相同 trace。**非数据泄漏**（train-test input overlap = 0）。raw_traces 仅 1.81% 重复，确认重复是 exception_only 表征特性而非数据收集问题。模型在有效样本仅 2858 unique 的条件下仍达 99.83%，反而说明 exception signal 的高 learnability — 少量 unique 样本即可充分学习 fault detection pattern。 |\n\n## Discussion 要点\n\n### D1: eval_loss vs verdict accuracy 解耦\nDeepSeek VOTA: eval_loss epoch1→3 从 0.068 升至 0.112 (+65%), 但 accuracy 从 78.15% 升至 84.45% (+6.3pp). Token-level calibration 与 binary classification accuracy 方向相反. **Implication**: verdict tasks 应用 task-specific metric (accuracy/F1) 做 checkpoint selection, 非 eval_loss.\n\n### D2: CRUXEval gap 假说 (revised — D030 confound)\nVOTA 跨模型 gap (14.96pp) 与 CRUXEval execution reasoning gap (15-17.5pp) 数值吻合. 假说: trace utilization effectiveness 受 base model \"execution reasoning readiness\" 约束. **标注**: hypothesis, N=2, 列出 alternatives. 不 overclaim. **注意**: 我们的训练/测试数据来自 HumanEval + MBPP-sanitized（非 CRUXEval），CRUXEval-I 分数仅作为衡量两个模型 execution reasoning 能力差异的外部参照。论文中必须明确区分数据来源与外部基准引用。**D030/D034 truncation evidence**: 14.96pp gap 中截断效应有因果证据: group_analysis 显示 train-truncated 83.04% vs train-intact 100% (Fisher p≈0, 推理时无截断)。截断因果方向可 claim，模型能力差异是 residual confound。CRUXEval gap 数值吻合可能部分巧合。论文中截断效应应作为 established factor 讨论（有 group_analysis 因果证据），模型能力假说标注为 residual confound hypothesis。\n\n### D3: Simplicity as robustness (revised)\nException signal 在两模型上均为最优组件，其结构简单性确保了相对优势的跨模型 robustness。但 DeepSeek seed sensitivity 揭示：simplicity 确保 signal 本身 robust，但 LoRA 训练过程是否稳定收敛到正确映射取决于模型。**trace design 应匹配 deployment model 的能力下界**，且需关注 training stability（建议：多 seed 验证 + 考虑 training stabilization 技巧如 warmup、learning rate schedule）。\n\n### D4: Checkpoint selection 与 gap 报告 (revised)\n正文报告所有 seeds 的 final checkpoint 结果 + best checkpoint 结果，不 cherry-pick。DeepSeek seed42: epoch1=99.83%, epoch3=99.33%（退化 0.50pp）。DeepSeek seed123: epoch1=91.43%, epoch3=91.09%（退化 0.34pp）。两个 seed 均显示轻微 epoch 退化，但核心差异在 epoch1 起点（8.40pp gap），不是训练过程。\n\n### D5: Irreducible samples — GeneratorExit 根因分析\n3 seeds 的 2/1190 errors 完全相同（id=901, 905, 均来自 HumanEval/95 `check_dict_case`），方向一致（pass→fail false negatives）。\n\n**根因**: Python `all()` 对 generator expression 短路时丢弃未耗尽的 generator，触发 `GeneratorExit`。`GeneratorExit` 继承自 `BaseException`（非 `Exception`），是 Python 内部控制流机制而非真正错误。但 tracer 对所有 caught exceptions 统一标记 `[ERROR]`，导致 exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。\n\n**为何不可约**:\n1. **表征局限**: exception_only 条件下模型仅见异常数据，无法访问控制流、返回值或 assertion 结果。`GeneratorExit` 在此表征中与真正错误不可区分。\n2. **跨 seed 确定性**: 3 个 random seeds 产生完全相同的 errors，确认这是 data/representation 属性而非模型初始化随机性。\n3. **训练集无信号**: 整个 1190 条测试集仅这 2 条含 `GeneratorExit`，训练集中也缺乏足够的 `GeneratorExit` 良性样本供模型学习。\n4. **人类也会犯错**: 仅看 exception trace（7 行 `[ERROR]`），人类审查者在不了解 Python generator protocol 的情况下也会预测 fail。\n\n**对论文的意义**: (1) 99.83% 是 exception_only representation 在此数据集上的理论 ceiling，非 saturation artifact；(2) 揭示 tracer 设计的改进方向——区分 `BaseException` 子类（如 `GeneratorExit`, `KeyboardInterrupt`）与 `Exception` 子类（真正的程序错误）可消除此类 irreducible error；(3) 提供 concrete evidence 说明 exception_only 模型\"理解\"的是 `[ERROR]` tag 的 fault indicator 语义，而非 exception type 的 fine-grained 含义。\n\n### D6: Calibration as secondary evidence\nCalibration 数据提供独立于 accuracy 的 evidence dimension。no_trace Brier=0.1972 说明模型无 trace 时不仅预测错，且对错误预测过度自信。exception_only Brier=0.0013 说明模型在有 exception signal 时几乎完美区分确定性和不确定性。这支持 Claim 1 的 \"sufficient signal\" 论点——exception 不仅让模型预测对，还让模型 \"知道自己对\"。\n\n### D7: Early stopping for exception signal (revised — D030 epoch1 data complete)\n3-seed epoch1 完整数据：seed42 epoch1=99.83% → epoch3=99.33%（-0.50pp）；**seed456 epoch1=99.33% → epoch3=99.33%（0.00pp）**；seed123 epoch1=91.43% → epoch3=91.09%（-0.34pp）。**seed42 的 epoch1=99.83%（匹配 Qwen）是该 seed 独有的 LoRA 初始化运气，不是 DeepSeek epoch1 的通用属性。** seed456 epoch1=epoch3 说明 epoch 退化非普遍现象。核心差异仍是 LoRA 初始化（epoch1 起点差 8.40pp），不是 overfitting。Early stopping 无法挽救差的初始化（seed123）。**Implication**: (1) 报告 DeepSeek 结果时应使用 median/2-of-3 (99.33%)，不应以 seed42 epoch1=99.83% 作为 headline；(2) epoch1 peak 是 LoRA 初始化运气的副产物，不具推广性。对比: VOTA 在 DeepSeek 上 84.45% **已确认正确**（D030 关闭: confirmatory re-eval max_length=16384 → 84.45%，与原始训练评估精确一致；D030 根因是 evaluate.py v2 的 max_length=2048 eval-time 截断 bug 导致 82.6% 预测为 garbage tokens）。\n\n### D9: LoRA initialization sensitivity as secondary bottleneck [NEW — D028]\nDeepSeek exception_only seed42=99.83% vs seed123=91.43% (epoch1), 8.40pp gap。Qwen 3 seeds 完全一致。假说：exception signal 的 learnability 取决于 (1) signal 本身的结构简单性（cross-model robust）+ (2) LoRA 初始化是否落入能正确映射 exception→verdict 的 basin。Qwen-7B 可能因模型更强/LoRA landscape 更平滑而对初始化不敏感。DeepSeek-6.7B（CRUXEval-I 39% vs Qwen 56.5%）的 loss landscape 可能更 rugged，LoRA 初始化更易陷入 suboptimal basin（seed123 的 fail_recall 仅 70-72% 说明模型未学到 exception→fail 映射的关键部分）。**论文角度**: 这不是 negative result——它揭示了 trace SFT 的 practical consideration（training stability），可作为 contribution 的一部分。建议 Discussion 讨论 training stabilization 策略（warmup, lr schedule, LoRA rank 调整, multi-seed selection）。\n\n### D10: Train loss ≈ but accuracy ≠ across seeds [NEW — D029]\nDeepSeek exception_only seed456 (train_loss=0.1225) 与 seed123 (train_loss=0.122) 训练损失几乎相同，但 accuracy 差 8.2pp（99.33% vs 91.09%）。关键差异集中在 fail_recall（1.0 vs 0.705）——token-level loss 在所有 tokens 上平均，掩盖了 fail 类少数样本的 sample-level 分类能力差异。**Implication**: (1) 扩展 D1 (eval_loss vs accuracy decoupling) 到训练阶段：train_loss 同样不是 verdict task accuracy 的可靠代理指标；(2) 对 checkpoint selection 的实际建议更强：必须用 task-specific metric (accuracy/F1)，甚至 train_loss 收敛也不保证 task performance；(3) fail 类作为少数类（28.5%），其学习质量被平均 loss 稀释——这在 class-imbalanced 设置下是 general pattern，可推广到其他 verdict/detection 任务。\n\n### D11: VOTA cross-model gap: training-time trace truncation as causal factor [NEW — D030 token analysis + group_analysis]\nD030 token analysis 确认: `to_chat_text()` 保留 labels（verdict label 在训练时未被截断），但 91.7% 的 DeepSeek VOTA 训练样本的 **trace content** 从 mean 2626 tokens 被截断到 ~2048 tokens。\n\n**Group analysis 提供因果证据**: 将测试集按训练截断状态分组（推理时无截断, max_length=16384），train-truncated 组 accuracy=83.04% vs train-intact 组 accuracy=100%, Fisher exact p≈0。**截断的因果方向可以 claim**: 训练时 trace 被截断导致模型学到的信息不完整 → 推理时即使看到完整 trace 也无法正确判断。模型能力差异是残余 confound（无法完全分离）。\n\n**Implications**: (1) 论文中所有 \"right-truncation corrupts/removes the verdict label\" 措辞对 VOTA 不成立——label 完整保留，被截断的是 trace INPUT content；(2) 14.96pp gap 中截断效应有因果证据（group_analysis），模型能力差异是 residual confound；(3) exception_only 因 token 长度短（远低于 2048）不受截断影响，其跨模型对比更 clean——进一步强化 Claim 1 \"most robust component\" 叙事；(4) 论文应讨论 max_length 的影响作为 limitation/future work；(5) group_analysis 数据可作为 Table/Figure 纳入论文——展示截断的因果效应。\n\n### D8: Data duplication as representation signature\nexception_only 训练集 39.45% 重复（4720→2858 unique），测试集 48.99%（1190→607 unique），而 raw_traces 仅 1.81%（5910→5803 unique）。重复源自 exception_only 表征的 design-by-intent compactness：同一编程题的多个 passing 解执行时均无异常，exception_only 表征退化为相同的空标记。这一数据特征本身就是 Claim 3 two-tier hierarchy 的佐证——Tier 1 信号仅编码 fault presence/absence，不编码 solution-level details，因此天然高重复。Train-test input overlap = 0 排除数据泄漏。\n\n## Contingency Framing (已解决, 留存档)\n\n### Claim 1 — RESOLVED (D029: seed456=99.33% confirms \"consistently best component\")\nseed456 与 seed42 完全一致（均 99.33%），seed123 为孤立离群值。Claim 1 定稿为 \"exception events consistently best component across models; absolute performance seed-dependent on DeepSeek (2/3 seeds robust, 1 outlier from LoRA init sensitivity); relative dominance over all alternatives robust across all seeds\"。\"0pp universal gap\" 叙事已放弃，转为数据驱动的 nuanced framing。\n\n### Claim 2 — RESOLVED (D006 + D009)\nv5 full_trace 81.76%. plan_002 label-only 86.22%, gradient dilution = minor (26%). 跨模型 VOTA gap 补充证据.\n\n## 与 v1 Framing 的关键差异\n\n| 维度 | v1 | v2.9 |\n|------|----|----|\n| Headline | VOTA compression 优于 full trace | Exception events are the most effective diagnostic signal |\n| Primary claim | VOTA +24pp through fault indicator preservation | Exception signal consistently best across models; absolute performance seed-dependent on DeepSeek |\n| Claim 2 | Compression > full trace (只有 gradient dilution) | Information density primary + gradient dilution quantification + cross-model reinforcement |\n| Claim 3 Tier 1 | exception_only only | exception + assertion-point (co-Tier 1, D020) |\n| VOTA 定位 | 核心方法 — trace compression | **Fault indicator isolation** — 价值在于提取 exception, 非 generic compression |\n| Model scope | 单模型 (Qwen) | 双模型, 跨模型对比是核心贡献 |\n| DeepSeek full_trace | N/A | v1 collapsed (label truncation), v3 pending |\n| Seed robustness | 未验证 | Qwen ✅ 99.83% ± 0.00 (3 seeds); DeepSeek ⚠️ seed-dependent (91-99%, D028) |\n| Irreducible error | 未分析 | ✅ GeneratorExit 根因明确，99.83% = representation ceiling |\n| Calibration | 未验证 | ✅ 完整 ECE+Brier, ~63x/~150x gap vs no_trace |\n| Data duplication | 未分析 | ✅ exception_only ~40% 重复（representation compactness），train-test overlap = 0 |\n| Early stopping | 未讨论 | DeepSeek epoch1→epoch3 轻微退化 (0.3-0.5pp); 核心问题是 LoRA 初始化 (seed123 epoch1=91.43%), 非 overfitting |\n| Narrative arc | \"VOTA helps\" | \"Exception events are consistently best; VOTA's value is isolating them; training stability matters\" |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Ablation: 去除 VOTA 中 actual/expected 值对，只保留 assertion structure + exception\n    info。验证 VOTA 效果是 genuine behavioral understanding 还是 trivial string comparison。'\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: vota_no_ae_seed42\n  notes: 如果去 actual/expected 后 acc 仍 >80%，证明非 trivial；如果降到 ~75%(=no_trace)，则是字符串比对。决定\n    Claim 1 强度和论文 framing。\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.994\n    majority_baseline: 0.7151\n    lift: 0.279\n    n: 1190\n    pass_f1: 0.996\n    fail_f1: 0.989\n    accuracy_ci_lower: 0.989\n    accuracy_ci_upper: 0.998\n    lift_vs_notrace: 0.243\n    lift_vs_notrace_ci_lower: 0.218\n    lift_vs_notrace_ci_upper: 0.268\n    train_loss: 0.0908\n    eval_loss: 0.2215\n    wall_clock_seconds: 6397.88\n- id: plan_002\n  claim: 2\n  description: 'Ablation: full_trace + label-only loss (只对分类 token 计算 loss，mask trace\n    tokens)。验证 collapse 根因是 gradient dilution 而非数据/代码 bug。'\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: full_trace_label_only_seed42\n  notes: 如果 label-only loss 修复 collapse (acc >70%)，确认 gradient dilution 假说。如果仍 collapse，可能是\n    trace noise/length 本身就有害。\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8622\n    accuracy_ci_lower: 0.8437\n    accuracy_ci_upper: 0.8807\n    majority_baseline: 0.7151\n    lift: 0.1471\n    n: 1190\n    pass_precision: 0.8821\n    pass_recall: 0.9318\n    pass_f1: 0.9063\n    fail_precision: 0.8007\n    fail_recall: 0.6873\n    fail_f1: 0.7397\n    train_loss: 0.2505\n    eval_loss: 0.3205\n    lift_vs_notrace: 0.1109\n    lift_vs_notrace_ci_lower: 0.0849\n    lift_vs_notrace_ci_upper: 0.137\n    lift_vs_standard_fulltrace: 0.0445\n    lift_vs_standard_fulltrace_ci_lower: 0.0235\n    lift_vs_standard_fulltrace_ci_upper: 0.0655\n    lift_vs_standard_fulltrace_pvalue: 0\n- id: plan_003\n  claim: 3\n  description: 'VOTA component ablation: 分别测试 (a) 只有 actual/expected, (b) 只有 exception\n    summary, (c) 只有 loop compression, (d) 全量 VOTA。量化每个组件的贡献。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  registry_id: vota_loop_only_seed42\n  notes: '4 个 sub-conditions。registry IDs: vota_loop_only_seed42 (loop_only 85.6%),\n    vota_exception_only_seed42_v2 (exception_only 99.83%), vota_ae_only_seed42 (ae_only\n    99.92%)。plan_001 vota_no_ae_seed42 (99.4%) 覆盖 ae 冗余确认。'\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8563\n    majority_baseline: 0.7151\n    lift: 0.1412\n    n: 1190\n    pass_precision: 0.9239\n    pass_recall: 0.8707\n    pass_f1: 0.8966\n    fail_precision: 0.7165\n    fail_recall: 0.8201\n    fail_f1: 0.7648\n    accuracy_ci:\n    - 0.8353\n    - 0.8756\n    bootstrap_vs_no_trace:\n      diff: 0.105\n      ci:\n      - 0.0824\n      - 0.1286\n      significant: true\n    bootstrap_vs_vota:\n      diff: -0.1378\n      ci:\n      - -0.1571\n      - -0.1185\n      significant: true\n    bootstrap_vs_full_trace:\n      diff: 0.0387\n      ci:\n      - 0.0185\n      - 0.0597\n      significant: true\n    train_loss: 0.0718\n    wall_clock_seconds: 7425.65\n- id: plan_004\n  claim: 1\n  description: '第二模型验证: DeepSeek-Coder-6.7B 上复现 4 条件（VOTA/no_trace/full_trace/exception_only），与\n    DCSH 同模型直接对比。exception_only 跨模型验证 exception dominance。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  registry_id: deepseek_exception_only_seed42\n  notes: '4 条件: deepseek_vota_seed42 (84.45% ✅), deepseek_no_trace_seed42 (73.36%\n    ✅), deepseek_exception_only_seed42 (99.33% ✅), deepseek_full_trace_seed42_v3 (RUNNING,\n    label truncation fix). 3/4 完成, full_trace v3 待完成。'\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9933\n    majority_baseline: 0.7151\n    lift: 0.2782\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9906\n    pass_f1: 0.9953\n    fail_precision: 0.9769\n    fail_recall: 1\n    fail_f1: 0.9883\n    epoch1_checkpoint_eval:\n      accuracy: 0.9983\n      fail_recall: 1\n      fail_precision: 0.9941\n      pass_recall: 0.9976\n      conclusion: epoch1_better_by_0.50pp\n- id: plan_005\n  claim: 1\n  description: '第二任务验证: 在 DebugBench subset 上测试 exception_only/VOTA/no_trace。验证 verdict\n    task 跨任务泛化性。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps:\n  - plan_001\n  registry_id: debugbench_exception_only_seed42\n  notes: 3/3 完成。debugbench_exception_only_seed42=100.0% (426/426, Wilson CI [99.14%,100%]),\n    debugbench_vota_seed42=99.77% (1 error), debugbench_no_trace_seed42=96.71%。定位为\n    generalization validation（非 trace importance evidence，因 no_trace baseline 96.71%\n    已很高，marginal contribution 仅 3.29pp）。\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 1\n    majority_baseline: 0.5141\n    lift: 0.4859\n    n: 426\n    pass_precision: 1\n    pass_recall: 1\n    pass_f1: 1\n    fail_precision: 1\n    fail_recall: 1\n    fail_f1: 1\n    accuracy_ci_wilson:\n    - 0.9914\n    - 1\n    accuracy_ci_bootstrap:\n    - 1\n    - 1\n    train_loss: 0.2435\n    eval_loss: 0.4157\n    train_runtime_sec: 837\n- id: plan_006\n  claim: 2\n  description: 'Trace length ablation: 测试不同截断长度 (256/512/1024/no_limit) 对 full_trace\n    准确率的影响。2048tok 取消（train_sft.py 硬编码 max_length=2048，与 no_limit 等价）。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  registry_id: full_trace_256tok_seed42\n  notes: '4 点设计: 256tok=78.82% (DONE), 512tok=80.42% (DONE), 1024tok (RUNNING), no_limit=81.76%\n    (full_trace_seed42_v5)。2048tok killed（max_length=2048 硬编码使其与 no_limit 等价）。Registry\n    IDs: full_trace_256tok_seed42, full_trace_512tok_seed42, full_trace_1024tok_seed42,\n    full_trace_seed42_v5。趋势: 更多 trace 略有帮助但收益递减，且全部远低于 exception_only (99.83%)。'\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.7882\n    majority_baseline: 0.7151\n    lift: 0.0731\n    n: 1190\n    pass_precision: 0.903\n    pass_recall: 0.788\n    pass_f1: 0.842\n    fail_precision: 0.597\n    fail_recall: 0.788\n    fail_f1: 0.679\n    accuracy_ci:\n    - 0.764\n    - 0.81\n    train_loss: 0.1094\n    train_runtime_sec: 3047\n    epochs: 3\n- id: plan_007\n  claim: 3\n  description: 'Calibration analysis: ECE + reliability diagrams 对比 VOTA/no_trace/full_trace\n    的 calibration 质量。验证 trace SFT 对 verdict task 改善 calibration 的假说。'\n  priority: P2\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: calibration_analysis_seed42\n  notes: 纯 eval，不需要额外训练。用已有 checkpoint 的 logits 计算。\n  status: DONE\n  conclusion: success\n  metrics:\n    no_trace:\n      ece: 0.171476\n      mce: 0.475643\n      brier_score: 0.197152\n      accuracy: 0.751261\n      n_samples: 1190\n    full_trace:\n      ece: 0.095817\n      mce: 0.249061\n      brier_score: 0.143924\n      accuracy: 0.817647\n      n_samples: 1190\n    label_only:\n      ece: 0.110686\n      mce: 0.417124\n      brier_score: 0.120144\n      accuracy: 0.862185\n      n_samples: 1190\n    loop_only:\n      ece: 0.083085\n      mce: 0.183406\n      brier_score: 0.118335\n      accuracy: 0.856303\n      n_samples: 1190\n    ae_only:\n      ece: 0.000415\n      mce: 0.000415\n      brier_score: 0.000847\n      accuracy: 0.99916\n      n_samples: 1190\n    exception_only:\n      ece: 0.002717\n      mce: 0.835484\n      brier_score: 0.001311\n      accuracy: 0.998319\n      n_samples: 1190\n    vota:\n      ece: 0.00541\n      mce: 0.622459\n      brier_score: 0.005234\n      accuracy: 0.994118\n      n_samples: 1190\n- id: plan_008\n  claim: 1\n  description: 'Seed robustness: 3 random seeds (42/123/456) 验证 VOTA 结果稳定性。McNemar\n    test + bootstrap CI。'\n  priority: P2\n  gpu_budget_hours: 6\n  deps:\n  - plan_001\n  registry_id: exception_only_seed456\n  notes: 'Seed robustness 完成。Qwen exception_only: 99.83% ± 0.00 (seeds 42/123/456,\n    irreducible 2/1190). Qwen VOTA: seed42=99.41%, seed456=99.08% (Δ<0.4pp). DeepSeek\n    exception_only: seed42/456=99.33%, seed123=91.09% (LoRA outlier). Registry IDs:\n    exception_only_seed123, exception_only_seed456, vota_seed456_v2, deepseek_exception_only_seed42/123/456.'\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    accuracy_ci:\n    - 0.9958\n    - 1\n    majority_baseline: 0.7151\n    lift: 0.2832\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9976\n    pass_f1: 0.9988\n    fail_precision: 0.9941\n    fail_recall: 1\n    fail_f1: 0.9971\n    vs_seed42:\n      seed42_accuracy: 0.9983\n      seed456_accuracy: 0.9983\n      diff: 0\n      note: identical accuracy to 4 decimal places; no predictions.jsonl for paired\n        bootstrap\n    train_loss: 0.1087\n    eval_loss: 0.4629\n    train_runtime_sec: 4541\n    epochs: 3\n- id: plan_mvp_vota\n  claim: 1\n  description: 'MVP: VOTA trace SFT for test verdict prediction'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: vota_seed42_v4\n  notes: 完成。95.63% accuracy, +20.5pp over baseline.\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9563\n    majority_baseline: 0.7151\n    lift: 0.2412\n    n: 1190\n    pass_precision: 0.944\n    pass_recall: 0.998\n    pass_f1: 0.97\n    fail_precision: 0.993\n    fail_recall: 0.853\n    fail_f1: 0.917\n    lift_vs_notrace: 0.205\n    lift_vs_notrace_ci_lower: 0.177\n    lift_vs_notrace_ci_upper: 0.234\n    train_loss: 0.046\n    eval_loss: 0.0842\n- id: plan_mvp_notrace\n  claim: 1\n  description: 'MVP: No-trace baseline for test verdict prediction'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: no_trace_seed42_v4\n  notes: 完成。75.13% accuracy (majority baseline 71.51%).\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7513\n    majority_baseline: 0.7151\n    lift: 0.0361\n    pass_precision: 0.8776\n    pass_recall: 0.7579\n    pass_f1: 0.8134\n    fail_precision: 0.5473\n    fail_recall: 0.7345\n    fail_f1: 0.6272\n    train_loss: 0.18\n    eval_loss: 0.6454\n    eval_mean_token_accuracy: 0.8897\n- id: plan_mvp_fulltrace\n  claim: 2\n  description: 'MVP: Full execution trace SFT for test verdict prediction'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: full_trace_seed42_v2\n  notes: 完成。28.49% accuracy, model collapse (100% predict fail).\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.284\n    majority_baseline: 0.7151\n    lift: -0.4311\n    n: 1190\n    pass_precision: 0.923\n    pass_recall: 0.085\n    pass_f1: 0.155\n    fail_precision: 0.445\n    fail_recall: 0.785\n    fail_f1: 0.568\n    train_loss: 0.0373\n    eval_loss: 0.082\n    eval_mean_token_accuracy: 0.984\n- id: plan_012\n  claim: 1\n  description: 'Cross-scale validation: Qwen-2.5-Coder-1.5B 上复现 4 条件 (exception_only/vota/no_trace/full_trace)。\n    验证 exception signal 的 scale invariance 假说。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_003\n  registry_id: qwen15b_exception_only_seed42\n  notes: '4 条件: exception_only=99.83% (=7B, DONE), vota=99.58% (DONE), no_trace=67.31%\n    (DONE), full_trace=RUNNING。关键发现: 1.5B=7B on exception → signal-limited not capacity-limited。\n    Registry IDs: qwen15b_exception_only_seed42, qwen15b_vota_seed42, qwen15b_no_trace_seed42,\n    qwen15b_full_trace_seed42。'\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    accuracy_ci_lower: 0.9958\n    accuracy_ci_upper: 1\n    majority_baseline: 0.7151\n    lift: 0.283\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9976\n    pass_f1: 0.9988\n    fail_precision: 0.9941\n    fail_recall: 1\n    fail_f1: 0.9971\n    train_loss: 0.1347\n    eval_loss: 0.5761\n    wall_clock_seconds: 1762\n- id: plan_013\n  claim: 1\n  description: 'Cross-family validation: CodeLlama-13B-Instruct 上测试 3 条件 (exception_only/no_trace/vota)。\n    验证 exception dominance 跨 LLaMA 家族 + 更大 scale 的泛化性。'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: codellama13b_exception_only_seed42\n  notes: 'Model downloaded. 0/3 done, queued. Registry IDs: codellama13b_exception_only_seed42,\n    codellama13b_no_trace_seed42, codellama13b_vota_seed42。回应 R2-N2 scope concern:\n    4 models × 3 families × 2 scales。'\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    n: 1190\n    errors: 2\n- id: plan_014\n  claim: 3\n  description: 'Multi-seed expansion: loop_only + ae_only + label_only 各 3 seeds。\n    回应 R2-N3 single-seed concern，验证 Tier 层级划分稳定性。'\n  priority: P0\n  gpu_budget_hours: 12\n  deps:\n  - plan_003\n  registry_id: ae_only_seed123\n  notes: 'ae_only 3-seed done (mean 99.64%). label_only 3-seed done (mean 86.39%).\n    loop_only: seed42 done, seed123 RUNNING, seed456 queued。Registry IDs: ae_only_seed123/456,\n    label_only_seed123/456, loop_only_seed123/456。'\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9908\n    n: 1190\n    pass_recall: 0.987\n    fail_recall: 1\n    majority_baseline: 0.7151\n    lift: 0.2757\n- id: plan_015\n  claim: 1\n  description: 'Format marker removal control: 移除 [No exception data in trace] 格式标记后重训\n    exception_only × 3 seeds。回应 R1-N1 format shortcut concern。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exception_only_nomarker_seed42\n  notes: '计划中。如果移除标记后 SFT 仍 ≥99%，证明模型学到的是异常语义而非格式 shortcut。 Registry IDs: exception_only_nomarker_seed42/123/456。'\n  status: RUNNING\n\n\n## registry (completed experiments)\n\n- exp_id: no_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: vota_seed42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: no_trace_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: vota_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: no_trace_seed42_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    train_loss: 0.18\n    eval_loss: 0.645\n    eval_mean_token_accuracy: 0.89\n    accuracy: 0.7513\n    majority_baseline: 0.7151\n    lift: 0.0361\n    pass_precision: 0.8776\n    pass_recall: 0.7579\n    pass_f1: 0.8134\n    fail_precision: 0.5473\n    fail_recall: 0.7345\n    fail_f1: 0.6272\n- exp_id: vota_seed42_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    train_loss: 0.046\n    eval_loss: 0.085\n    eval_mean_token_accuracy: 0.983\n    accuracy: 0.992\n    majority_baseline: 0.7151\n    lift: 0.276\n    pass_precision: 0.99\n    pass_recall: 0.99\n    pass_f1: 0.99\n    fail_precision: 0.99\n    fail_recall: 0.99\n    fail_f1: 0.99\n- exp_id: full_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    train_loss: 0.037\n    eval_loss: 0.084\n    eval_mean_token_accuracy: 0.984\n    accuracy: 0.284\n    majority_baseline: 0.7151\n    lift: -0.431\n    pass_precision: 0.88\n    pass_recall: 0.08\n    pass_f1: 0.16\n    fail_precision: 0.31\n    fail_recall: 0.97\n    fail_f1: 0.57\n- exp_id: no_trace_seed42_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7513\n    majority_baseline: 0.7151\n    lift: 0.0361\n    pass_precision: 0.8776\n    pass_recall: 0.7579\n    pass_f1: 0.8134\n    fail_precision: 0.5473\n    fail_recall: 0.7345\n    fail_f1: 0.6272\n    train_loss: 0.18\n    eval_loss: 0.6454\n    eval_mean_token_accuracy: 0.8897\n- exp_id: vota_seed42_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9563\n    majority_baseline: 0.7151\n    lift: 0.2412\n    n: 1190\n    pass_precision: 0.944\n    pass_recall: 0.998\n    pass_f1: 0.97\n    fail_precision: 0.993\n    fail_recall: 0.853\n    fail_f1: 0.917\n    lift_vs_notrace: 0.205\n    lift_vs_notrace_ci_lower: 0.177\n    lift_vs_notrace_ci_upper: 0.234\n    train_loss: 0.046\n    eval_loss: 0.0842\n- exp_id: full_trace_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.284\n    majority_baseline: 0.7151\n    lift: -0.4311\n    n: 1190\n    pass_precision: 0.923\n    pass_recall: 0.085\n    pass_f1: 0.155\n    fail_precision: 0.445\n    fail_recall: 0.785\n    fail_f1: 0.568\n    train_loss: 0.0373\n    eval_loss: 0.082\n    eval_mean_token_accuracy: 0.984\n- exp_id: full_trace_seed42_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8176\n    majority_baseline: 0.7151\n    lift: 0.1025\n    n: 1190\n    pass_precision: 0.8774\n    pass_recall: 0.866\n    pass_f1: 0.8717\n    fail_precision: 0.6743\n    fail_recall: 0.6962\n    fail_f1: 0.6851\n    accuracy_ci_lower: 0.797\n    accuracy_ci_upper: 0.839\n    lift_vs_notrace: 0.0664\n    lift_vs_notrace_ci_lower: 0.0437\n    lift_vs_notrace_ci_upper: 0.0899\n    train_loss: 0.05\n    eval_loss: 0.0867\n    wall_clock_seconds: 7852\n    epoch_level:\n      epoch1_accuracy: 0.8303\n      epoch2_accuracy: 0.763\n      final_accuracy: 0.8176\n      trend: non_monotonic_epoch1_best_epoch2_collapse\n- exp_id: vota_seed42_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9941\n    majority_baseline: 0.7151\n    lift: 0.279\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9882\n    pass_f1: 0.9941\n    fail_precision: 0.9714\n    fail_recall: 1\n    fail_f1: 0.9855\n    lift_vs_notrace: 0.2428\n    lift_vs_notrace_ci_lower: 0.2185\n    lift_vs_notrace_ci_upper: 0.2681\n    accuracy_ci_lower: 0.9882\n    accuracy_ci_upper: 0.9983\n    train_loss: 0.05\n    eval_loss: 0.0867\n    eval_mean_token_accuracy: 0.9828\n    wall_clock_seconds: 8443\n    epoch_level:\n      epoch1_accuracy: 0.9933\n      epoch2_accuracy: 0.9941\n      final_accuracy: 0.9941\n      trend: monotonic_increasing_then_stable\n- exp_id: no_trace_seed42_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7513\n    accuracy_ci_lower: 0.7277\n    accuracy_ci_upper: 0.7748\n    majority_baseline: 0.7151\n    lift: 0.0361\n    lift_ci_lower: 0.0042\n    lift_ci_upper: 0.0706\n    n: 1190\n    pass_precision: 0.8776\n    pass_recall: 0.7579\n    pass_f1: 0.8134\n    fail_precision: 0.5473\n    fail_recall: 0.7345\n    fail_f1: 0.6272\n    epoch_level:\n      epoch1_accuracy: 0.7429\n      epoch2_accuracy: 0.763\n      final_accuracy: 0.7513\n      trend: non_monotonic_epoch2_best\n- exp_id: full_trace_label_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8622\n    accuracy_ci_lower: 0.8437\n    accuracy_ci_upper: 0.8807\n    majority_baseline: 0.7151\n    lift: 0.1471\n    n: 1190\n    pass_precision: 0.8821\n    pass_recall: 0.9318\n    pass_f1: 0.9063\n    fail_precision: 0.8007\n    fail_recall: 0.6873\n    fail_f1: 0.7397\n    train_loss: 0.2505\n    eval_loss: 0.3205\n    lift_vs_notrace: 0.1109\n    lift_vs_notrace_ci_lower: 0.0849\n    lift_vs_notrace_ci_upper: 0.137\n    lift_vs_standard_fulltrace: 0.0445\n    lift_vs_standard_fulltrace_ci_lower: 0.0235\n    lift_vs_standard_fulltrace_ci_upper: 0.0655\n    lift_vs_standard_fulltrace_pvalue: 0\n- exp_id: vota_no_ae_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.994\n    majority_baseline: 0.7151\n    lift: 0.279\n    n: 1190\n    pass_f1: 0.996\n    fail_f1: 0.989\n    accuracy_ci_lower: 0.989\n    accuracy_ci_upper: 0.998\n    lift_vs_notrace: 0.243\n    lift_vs_notrace_ci_lower: 0.218\n    lift_vs_notrace_ci_upper: 0.268\n    train_loss: 0.0908\n    eval_loss: 0.2215\n    wall_clock_seconds: 6397.88\n- exp_id: vota_ae_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9992\n    accuracy_ci:\n    - 0.9975\n    - 1\n    bootstrap_pairwise:\n      ae_only_vs_no_trace:\n        diff: 0.2479\n        ci:\n        - 0.2235\n        - 0.2731\n        p_value: 0\n        significant: true\n      ae_only_vs_exception_only:\n        diff: 0.0008\n        ci:\n        - -0.0017\n        - 0.0034\n        p_value: 0.8002\n        significant: false\n      ae_only_vs_vota:\n        diff: 0.005\n        ci:\n        - 0.0017\n        - 0.0092\n        p_value: 0.0046\n        significant: true\n    config:\n      n_bootstrap: 10000\n      seed: 42\n      method: paired_bootstrap\n- exp_id: vota_exception_only_seed42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: vota_loop_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8563\n    majority_baseline: 0.7151\n    lift: 0.1412\n    n: 1190\n    pass_precision: 0.9239\n    pass_recall: 0.8707\n    pass_f1: 0.8966\n    fail_precision: 0.7165\n    fail_recall: 0.8201\n    fail_f1: 0.7648\n    accuracy_ci:\n    - 0.8353\n    - 0.8756\n    bootstrap_vs_no_trace:\n      diff: 0.105\n      ci:\n      - 0.0824\n      - 0.1286\n      significant: true\n    bootstrap_vs_vota:\n      diff: -0.1378\n      ci:\n      - -0.1571\n      - -0.1185\n      significant: true\n    bootstrap_vs_full_trace:\n      diff: 0.0387\n      ci:\n      - 0.0185\n      - 0.0597\n      significant: true\n    train_loss: 0.0718\n    wall_clock_seconds: 7425.65\n- exp_id: vota_exception_only_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    majority_baseline: 0.7151\n    lift: 0.2832\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.998\n    pass_f1: 0.999\n    fail_precision: 0.994\n    fail_recall: 1\n    fail_f1: 0.997\n    lift_vs_notrace: 0.2471\n    lift_vs_notrace_ci_lower: 0.2227\n    lift_vs_notrace_ci_upper: 0.2714\n    lift_vs_fulltrace: 0.1807\n    lift_vs_fulltrace_ci_lower: 0.1588\n    lift_vs_fulltrace_ci_upper: 0.2034\n    lift_vs_vota: 0.0067\n    lift_vs_vota_ci_lower: 0.0017\n    lift_vs_vota_ci_upper: 0.0126\n    lift_vs_vota_pvalue: 0.01\n- exp_id: deepseek_vota_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8445\n    majority_baseline: 0.7151\n    lift: 0.1294\n    accuracy_ci:\n    - 0.826\n    - 0.864\n    pass_precision: 0.821\n    pass_recall: 1\n    pass_f1: 0.902\n    fail_precision: 1\n    fail_recall: 0.454\n    fail_f1: 0.625\n    eval_loss_epoch1: 0.0679\n    eval_loss_epoch2: 0.095\n    eval_loss_epoch3: 0.1121\n    final_train_loss: 0.0522\n    epoch1_checkpoint_eval:\n      accuracy: 0.7815\n      accuracy_ci:\n      - 0.76\n      - 0.803\n      fail_recall: 0.233\n      fail_precision: 1\n      pass_recall: 1\n      pass_precision: 0.766\n      fail_f1: 0.378\n      pass_f1: 0.867\n      conclusion: epoch3_final_is_better\n    reeval_with_fixed_script:\n      accuracy: 0.16\n      accuracy_ci:\n      - 0.139\n      - 0.18\n      fail_f1: 0.61\n      fail_precision: 0.9\n      fail_recall: 0.47\n      pass_f1: 0.07\n      pass_precision: 1\n      pass_recall: 0.04\n      note: 'CATASTROPHIC: re-eval with corrected evaluate.py shows 16% (vs original\n        84.45%). Model predicts fail for almost everything. Previous 84.45% may have\n        been from buggy eval. NEEDS INVESTIGATION.'\n    group_analysis:\n      train_truncated:\n        n: 1091\n        accuracy: 0.8304\n        ci_95:\n        - 0.8075\n        - 0.8524\n        correct: 906\n        incorrect: 185\n        pass_accuracy: 1\n        pass_n: 822\n        fail_accuracy: 0.3123\n        fail_n: 269\n      train_intact:\n        n: 99\n        accuracy: 1\n        ci_95:\n        - 1\n        - 1\n        correct: 99\n        incorrect: 0\n        pass_accuracy: 1\n        pass_n: 29\n        fail_accuracy: 1\n        fail_n: 70\n      fisher_exact:\n        odds_ratio: 0\n        p_value: 0\n      overall_accuracy: 0.8445\n      max_length: 2048\n      note: 'Grouped by whether training sample content exceeded token budget (DeepSeek\n        tokenizer, max_length=2048). Inference used full-length input (no truncation).\n        All 185 errors from truncated group''s fail class (fail_recall=31.2%). Intact\n        group: 100% accuracy.'\n- exp_id: deepseek_no_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.7336\n    majority_baseline: 0.7151\n    lift: 0.0185\n    n: 1190\n    pass_precision: 0.817\n    pass_recall: 0.808\n    pass_f1: 0.813\n    fail_precision: 0.532\n    fail_recall: 0.546\n    fail_f1: 0.539\n    accuracy_ci:\n    - 0.708\n    - 0.757\n    lift_ci:\n    - -0.009\n    - 0.046\n- exp_id: deepseek_full_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy_no_truncation: 0.2849\n    accuracy_with_truncation_fix: 0.1059\n    accuracy_with_truncation_fix_ci:\n    - 0.089\n    - 0.123\n    majority_baseline: 0.7151\n    n: 1190\n    note: 'Both evals show model failure. No-truncation: all predict fail. With-truncation:\n      garbage tokens. LoRA training itself failed due to label truncation during training.'\n- exp_id: deepseek_exception_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9933\n    majority_baseline: 0.7151\n    lift: 0.2782\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9906\n    pass_f1: 0.9953\n    fail_precision: 0.9769\n    fail_recall: 1\n    fail_f1: 0.9883\n    epoch1_checkpoint_eval:\n      accuracy: 0.9983\n      fail_recall: 1\n      fail_precision: 0.9941\n      pass_recall: 0.9976\n      conclusion: epoch1_better_by_0.50pp\n- exp_id: calibration_analysis_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    no_trace:\n      ece: 0.171476\n      mce: 0.475643\n      brier_score: 0.197152\n      accuracy: 0.751261\n      n_samples: 1190\n    full_trace:\n      ece: 0.095817\n      mce: 0.249061\n      brier_score: 0.143924\n      accuracy: 0.817647\n      n_samples: 1190\n    label_only:\n      ece: 0.110686\n      mce: 0.417124\n      brier_score: 0.120144\n      accuracy: 0.862185\n      n_samples: 1190\n    loop_only:\n      ece: 0.083085\n      mce: 0.183406\n      brier_score: 0.118335\n      accuracy: 0.856303\n      n_samples: 1190\n    ae_only:\n      ece: 0.000415\n      mce: 0.000415\n      brier_score: 0.000847\n      accuracy: 0.99916\n      n_samples: 1190\n    exception_only:\n      ece: 0.002717\n      mce: 0.835484\n      brier_score: 0.001311\n      accuracy: 0.998319\n      n_samples: 1190\n    vota:\n      ece: 0.00541\n      mce: 0.622459\n      brier_score: 0.005234\n      accuracy: 0.994118\n      n_samples: 1190\n- exp_id: vota_seed123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: vota_seed456\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exception_only_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    accuracy_ci:\n    - 0.9958\n    - 1\n    majority_baseline: 0.7151\n    lift: 0.2832\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9976\n    pass_f1: 0.9988\n    fail_precision: 0.9941\n    fail_recall: 1\n    fail_f1: 0.9971\n    train_loss: 0.1096\n    train_runtime_sec: 7507\n    epochs: 3\n    seed_comparison:\n      seed42_accuracy: 0.9983\n      seed456_accuracy: 0.9983\n      seed123_accuracy: 0.9983\n      max_diff: 0\n      note: identical accuracy to 4 decimal places across all 3 seeds (42/456/123);\n        each has exactly 2/1190 errors; exception_only fully seed-robust\n- exp_id: exception_only_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    accuracy_ci:\n    - 0.9958\n    - 1\n    majority_baseline: 0.7151\n    lift: 0.2832\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9976\n    pass_f1: 0.9988\n    fail_precision: 0.9941\n    fail_recall: 1\n    fail_f1: 0.9971\n    vs_seed42:\n      seed42_accuracy: 0.9983\n      seed456_accuracy: 0.9983\n      diff: 0\n      note: identical accuracy to 4 decimal places; no predictions.jsonl for paired\n        bootstrap\n    train_loss: 0.1087\n    eval_loss: 0.4629\n    train_runtime_sec: 4541\n    epochs: 3\n- exp_id: deepseek_exception_only_seed123\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.9109\n    pass_precision: 1\n    pass_recall: 0.993\n    pass_f1: 0.996\n    fail_precision: 0.976\n    fail_recall: 0.705\n    fail_f1: 0.818\n    ci_95:\n    - 0.894\n    - 0.926\n    train_loss: 0.122\n    train_runtime_sec: 6384\n- exp_id: deepseek_full_trace_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: vota_seed456_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9908\n    pass_precision: 1\n    pass_recall: 0.987\n    pass_f1: 0.993\n    fail_precision: 0.969\n    fail_recall: 1\n    fail_f1: 0.984\n    ci_95:\n    - 0.985\n    - 0.996\n- exp_id: deepseek_full_trace_seed42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7916\n    majority_baseline: 0.7151\n    lift: 0.0765\n    n: 1190\n    pass_precision: 0.857\n    pass_recall: 0.851\n    pass_f1: 0.854\n    fail_precision: 0.632\n    fail_recall: 0.643\n    fail_f1: 0.637\n    accuracy_ci:\n    - 0.768\n    - 0.813\n    train_loss: 0.0547\n    train_runtime_seconds: 8891\n    epochs: 3\n    reeval_discrepancy:\n      reeval_accuracy: 0.285\n      reeval_note: 'RESOLVED: 28.5% was caused by eval max_length=16384 (OOD). Re-eval\n        with max_length=2048 reproduces 79.16%. predictions.jsonl updated to maxlen2048\n        results.'\n      status: RESOLVED\n- exp_id: deepseek_exception_only_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9933\n    majority_baseline: 0.7151\n    lift: 0.2782\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9906\n    pass_f1: 0.9953\n    fail_precision: 0.9769\n    fail_recall: 1\n    fail_f1: 0.9883\n    accuracy_ci:\n    - 0.9882\n    - 0.9975\n    train_loss: 0.1225\n    eval_loss: 0.4824\n    train_runtime_sec: 6246\n    seed_comparison:\n      seed42_accuracy: 0.9933\n      seed456_accuracy: 0.9933\n      seed123_accuracy: 0.9109\n      note: seed42 and seed456 identical (99.33%); seed123 outlier (91.09%). 2/3 seeds\n        robust.\n    epoch1_checkpoint_eval:\n      accuracy: 0.993\n      accuracy_ci:\n      - 0.988\n      - 0.997\n      fail_f1: 0.99\n      fail_precision: 0.98\n      fail_recall: 1\n      pass_f1: 1\n      pass_precision: 1\n      pass_recall: 0.99\n      conclusion: epoch1 (99.3%) ≈ epoch3 (99.33%), 1 epoch convergence confirmed\n- exp_id: full_trace_256tok_seed42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.7882\n    majority_baseline: 0.7151\n    lift: 0.0731\n    n: 1190\n    pass_precision: 0.903\n    pass_recall: 0.788\n    pass_f1: 0.842\n    fail_precision: 0.597\n    fail_recall: 0.788\n    fail_f1: 0.679\n    accuracy_ci:\n    - 0.764\n    - 0.81\n    train_loss: 0.1094\n    train_runtime_sec: 3047\n    epochs: 3\n- exp_id: full_trace_512tok_seed42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.8042\n    majority_baseline: 0.7151\n    lift: 0.0891\n    pass_precision: 0.8705\n    pass_recall: 0.8531\n    pass_f1: 0.8617\n    fail_precision: 0.6489\n    fail_recall: 0.6814\n    fail_f1: 0.6647\n    n: 1190\n    accuracy_ci:\n    - 0.7815\n    - 0.8261\n- exp_id: full_trace_1024tok_seed42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.7723\n    majority_baseline: 0.7151\n    lift: 0.0571\n    n: 1190\n    accuracy_ci:\n    - 0.7487\n    - 0.7958\n    pass_precision: 0.9006\n    pass_recall: 0.7662\n    pass_f1: 0.8279\n    fail_precision: 0.573\n    fail_recall: 0.7876\n    fail_f1: 0.6634\n    train_loss: 0.0634\n    train_runtime_sec: 5553\n    epochs: 3\n- exp_id: full_trace_2048tok_seed42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: debugbench_exception_bug_fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: debugbench_exception_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 1\n    majority_baseline: 0.5141\n    lift: 0.4859\n    n: 426\n    pass_precision: 1\n    pass_recall: 1\n    pass_f1: 1\n    fail_precision: 1\n    fail_recall: 1\n    fail_f1: 1\n    accuracy_ci_wilson:\n    - 0.9914\n    - 1\n    accuracy_ci_bootstrap:\n    - 1\n    - 1\n    train_loss: 0.2435\n    eval_loss: 0.4157\n    train_runtime_sec: 837\n- exp_id: debugbench_no_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9671\n    majority_baseline: 0.5141\n    lift: 0.4531\n    pass_precision: 1\n    pass_recall: 0.936\n    pass_f1: 0.967\n    fail_precision: 0.937\n    fail_recall: 1\n    fail_f1: 0.967\n    accuracy_ci:\n    - 0.948\n    - 0.984\n    train_loss: 0.249\n    eval_loss: 0.532\n- exp_id: debugbench_vota_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9977\n    majority_baseline: 0.5141\n    lift: 0.4836\n    n: 426\n    pass_precision: 1\n    pass_recall: 1\n    pass_f1: 1\n    fail_precision: 1\n    fail_recall: 1\n    fail_f1: 1\n    accuracy_ci:\n    - 0.993\n    - 1\n    train_loss: 0.098\n    eval_loss: 0.1179\n    eval_mean_token_accuracy: 0.9737\n    errors: 1\n- exp_id: eval_missing_predictions_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: eval_missing_predictions_batch_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: ae_only_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9908\n    n: 1190\n    pass_recall: 0.987\n    fail_recall: 1\n    majority_baseline: 0.7151\n    lift: 0.2757\n- exp_id: ae_only_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9992\n    n: 1190\n    majority_baseline: 0.7151\n    lift: 0.2841\n    seed_comparison:\n      seed42_accuracy: 0.9992\n      seed123_accuracy: 0.9908\n      seed456_accuracy: 0.9992\n      mean_accuracy: 0.9964\n      std: 0.0049\n      note: 2/3 seeds = 99.92%, seed123 = 99.08%. Mean = 99.64% ± 0.49\n- exp_id: regex_baseline_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    regex_B1_ERROR_presence: 0.9345\n    regex_B2_Traceback: 0.7151\n    regex_B3_any_keyword: 0.9345\n    regex_B4_exception_type: 0.9361\n    regex_B5_format_marker: 0.9933\n    regex_B6_error_count_ge2: 0.9202\n    sft_exception_only: 0.9983\n    best_regex_gap_vs_sft: -0.0622\n    B5_mcnemar_p: 0.041\n    n: 1190\n- exp_id: label_only_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8706\n    n: 1190\n    pass_recall: 0.974\n    fail_recall: 0.611\n    pass_f1: 0.915\n    fail_f1: 0.729\n- exp_id: label_only_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.859\n    n: 1190\n    pass_recall: 0.938\n    fail_recall: 0.661\n    pass_f1: 0.905\n    fail_f1: 0.727\n- exp_id: exception_only_nomarker_seed42\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: loop_only_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8588\n    majority_baseline: 0.7151\n    lift: 0.1437\n    n: 1190\n    pass_precision: 0.9129\n    pass_recall: 0.8872\n    pass_f1: 0.8999\n    fail_precision: 0.7355\n    fail_recall: 0.7876\n    fail_f1: 0.7607\n    accuracy_ci:\n    - 0.8403\n    - 0.8773\n- exp_id: loop_only_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8664\n    n: 1190\n    pass_precision: 0.9179\n    pass_recall: 0.8931\n    pass_f1: 0.9053\n    fail_precision: 0.7486\n    fail_recall: 0.7994\n    fail_f1: 0.7732\n    accuracy_ci:\n    - 0.847\n    - 0.884\n- exp_id: exception_only_nomarker_seed123\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: exception_only_nomarker_seed456\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen1.5b_exception_only_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen1.5b_no_trace_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen1.5b_vota_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen1.5b_full_trace_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: codellama_exception_only_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: codellama_no_trace_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: codellama_vota_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: codellama13b_exception_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    n: 1190\n    errors: 2\n- exp_id: codellama13b_no_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.765\n    n: 1190\n    majority_baseline: 0.7151\n    lift: 0.05\n    pass_precision: 0.84\n    pass_recall: 0.83\n    pass_f1: 0.84\n    fail_precision: 0.59\n    fail_recall: 0.59\n    fail_f1: 0.59\n    accuracy_ci:\n    - 0.738\n    - 0.787\n- exp_id: codellama13b_vota_seed42\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen15b_no_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6731\n    n: 1190\n    pass_f1: 0.7527\n    fail_f1: 0.518\n    lift_over_majority: -0.042\n    training_time_sec: 851\n- exp_id: qwen15b_vota_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9958\n    n: 1190\n    pass_recall: 0.9976\n    fail_recall: 0.9912\n    pass_f1: 0.9971\n    fail_f1: 0.9926\n    training_time_sec: 2922\n- exp_id: qwen15b_full_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7706\n    n: 1190\n- exp_id: qwen15b_exception_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    accuracy_ci_lower: 0.9958\n    accuracy_ci_upper: 1\n    majority_baseline: 0.7151\n    lift: 0.283\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9976\n    pass_f1: 0.9988\n    fail_precision: 0.9941\n    fail_recall: 1\n    fail_f1: 0.9971\n    train_loss: 0.1347\n    eval_loss: 0.5761\n    wall_clock_seconds: 1762\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T16:08:52.760Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T16:08:52.760Z",
  "sessionId": "1723cae9-4a61-47ee-b162-e2fd329daf4b"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T16:08:52.782Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：nomarker 实验显著退化，暴露格式标记是主要机制；原始 'fault semantics' 叙事不成立，需要 reframe
核心假设：['nomarker 实验 <90%（或 3-seed 高方差，worst seed <85%）：移除格式标记后大幅退化，证明模型主要依赖 format pattern 而非 exception content semantics', 'CodeLlama-13B VOTA ≥ exception_only：大模型上 VOTA 不劣于 exception，Claim 3 层级关系 model-specific', "'Exception events as fault detection' 叙事被削弱为 'format marker as classification shortcut'——接近 regex B5 (99.33%) 的机制", '审稿人可以 legitimately argue: SFT 学到的是 [No exception data in trace] 有无 → pass/fail 映射，与 regex 无本质区别']
关键指标范围：{'nomarker_accuracy_3seed_mean': [0.85, 0.949], 'nomarker_accuracy_worst_seed': [0.8, 0.93], 'codellama13b_vota_accuracy': [0.99, 1.0], 'cross_family_exception_dominance_pp': [-5.0, 0.0], 'format_marker_contribution_pp': [5.0, 15.0]}
叙事方向：原始 'fault semantics' framing 不成立。Reframe 为：**trace formatting as implicit task specification** — 论文贡献变为揭示 SFT 中 format/structure choices 对 downstream classification 的 outsized impact。核心 insight 转向：(1) verdict prediction 本质是 format-sensitive binary classification, (2) 结构化标记（如 [ERROR]）acts as implicit label that SFT exploits, (3) 设计 trace format 时应显式考虑 downstream task 的 shortcut affordance。Claim 1 重写为 'structured format markers dominate verdict prediction in exception traces'。Claim 3 重写为 'format engineering > content richness for SFT verdict tasks'。仍冲 EMNLP Main——angle 从 'positive finding about exception semantics' 变为 'cautionary finding about SFT shortcut learning + practical design principle'，与 shortcut learning literature (NLI artifacts, annotation artifacts) 对话。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: trace-verdict-study

## paper_framing.md

# Paper Framing — trace-verdict-study

> v3.0 — [UPDATED 2026-05-15] D030 CLOSED: DeepSeek VOTA 84.45% confirmed correct (confirmatory re-eval). **Critical narrative fix**: to_chat_text() preserves labels → VOTA 训练时 verdict label 未被截断 → 论文中 "label truncation/corruption" 措辞对 VOTA 不成立。正确叙事: trace INPUT content 被截断 (91.7% samples), 84.45% 反映 trace information loss。新增 D11: VOTA cross-model gap confounded by training-time truncation。数据集来源：HumanEval (164) + MBPP-sanitized (427) = 591 problems × 10 LLM-generated solutions = 5910 samples。

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May 25, 2026

## Core Insight

Verdict prediction (pass/fail) is fundamentally a **fault detection** task. The most effective signal is the **exception event** — a compact, structured diagnostic moment that consistently outperforms all other trace representations across models (Qwen 99.83% ± 0.00 across 3 seeds; DeepSeek 91-99% depending on seed, but always > VOTA 84.45% and no_trace 73.36%). In contrast, richer trace representations that require deeper execution reasoning show model-dependent effectiveness: VOTA gap = 14.96pp, no_trace gap = 1.77pp. Information density — not training signal distribution — is the primary bottleneck: even oracle loss masking (label-only) cannot close the 13pp gap between full traces and targeted extraction. The design principle: **extract the highest-specificity diagnostic signal; discard everything else.** Cross-model absolute performance depends on LoRA initialization stability, but exception_only's relative dominance over other components is robust.

VOTA's primary contribution is **fault indicator isolation** — automatically extracting exception events from noisy full traces — rather than generic trace compression. The "compression helps" narrative was a stepping stone; the real mechanism is diagnostic signal extraction.

## Core Claims (3)

### Claim 1: Exception events are the most effective trace component for verdict prediction

Exception summaries consistently achieve the highest verdict prediction accuracy across both models tested, outperforming all other trace representations in every seed. On Qwen-2.5-Coder-7B, performance is perfectly robust: 99.83% ± 0.00 (3 seeds). On DeepSeek-Coder-6.7B, absolute accuracy is seed-dependent (seed42=99.83% epoch1, seed123=91.43% epoch1; Δ=8.40pp), consistent with LoRA initialization sensitivity — but exception_only still dominates VOTA (84.45%) and no_trace (73.36%) in all seeds. This contrasts with VOTA (cross-model gap = 14.96pp) and no_trace (gap = 1.77pp). Exception events are structurally simple (`[ERROR] type: ... message: ...`) and do not require deep trace reasoning.

**Supporting evidence:**
- `vota_exception_only_seed42_v2`: Qwen 99.83%, ECE=0.0027
- `deepseek_exception_only_seed42`: DeepSeek 99.83% (epoch1) / 99.33% (epoch3)
- `deepseek_exception_only_seed456`: DeepSeek 99.33% (epoch3), CI [98.82, 99.75] — 与 seed42 完全一致
- `deepseek_exception_only_seed123`: DeepSeek 91.43% (epoch1) / 91.09% (epoch3) — LoRA init sensitivity outlier
- `deepseek_vota_seed42`: DeepSeek VOTA 84.45% (gap = 14.96pp vs Qwen)
- `deepseek_no_trace_seed42`: DeepSeek no_trace 73.36% (gap = 1.77pp vs Qwen)
- `vota_no_ae_seed42`: 99.41% — actual/expected removal 不降，非 trivial string comparison

**DeepSeek seed analysis** ✅ (FINALIZED, D029):

| Seed | Epoch 3 (final) | fail_recall | pass_recall | train_loss | Errors | CI |
|------|-----------------|-------------|-------------|------------|--------|-----|
| 42   | 99.33%          | 1.0         | 0.9906      | —          | 8/1190 | — |
| 456  | 99.33%          | 1.0         | 0.9906      | 0.1225     | 8/1190 | [98.82, 99.75] |
| 123  | 91.09%          | 0.705       | 0.993       | 0.122      | —      | [89.4, 92.6] |

seed42 与 seed456 结果**完全一致**（均 8/1190 错误，99.33%），seed123 为离群值。seed123 的 fail_recall 仅 0.705 — LoRA 初始化落入差的局部最优，未充分学到 exception→fail 映射。**关键发现**: seed456 和 seed123 的 train_loss 几乎相同（0.1225 vs 0.122），但 accuracy 差 8.2pp — token-level loss 掩盖了 sample-level 分类能力的巨大差异（详见 D10）。

**Irreducible error analysis** ✅: 3 seeds 错误的 2 个样本 (id=901, 905) 均来自 HumanEval/95 (`check_dict_case`)，根因为 Python `all()` 对 generator expression 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误）。tracer 将其标记为 `[ERROR]`，exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。整个 1190 条测试集仅这 2 条含 `GeneratorExit`，模型无训练信号学习其良性本质。**这确认 99.83% 是 exception_only 表征的理论上限，剩余 0.17% 是 representation-inherent irreducible error，而非模型不足。**

**Seed robustness** ✅: Qwen exception_only 3-seed 完全一致，构成本文最强 robustness 证据：

| Seed | Accuracy | 95% CI | Errors |
|------|----------|--------|--------|
| 42 | 99.83% | [99.58, 100] | 2/1190 |
| 123 | 99.83% | [99.58, 100] | 2/1190 |
| 456 | 99.83% | [99.58, 100] | 2/1190 |

3 seeds 错误样本 100% 重叠（id=901, 905, 均为 `check_dict_case` 函数, label=pass → pred=fail）。**Irreducible samples**: 模型已达数据集理论上限，variance = 0。

**DeepSeek cross-model** ✅ (D029): 3-seed 完整数据 — seed42/456=99.33%, seed123=91.09%。2/3 seeds 鲁棒，seed123 为 LoRA 初始化离群值（fail_recall 仅 0.705）。Qwen 3-seed 完美稳定 (99.83% ± 0.00) vs DeepSeek 高方差（σ≈4.8pp），暗示 exception signal 的 learnability 与模型 LoRA 训练稳定性相关。但即使最差 seed (91.09%) 仍优于 VOTA (84.45%) 和 no_trace (73.36%)，relative dominance robust。

### Claim 2: Information density, not gradient dilution, drives trace compression benefit

Full traces help verdict prediction (81.76% [`full_trace_seed42_v5`], +6.6pp over baseline), but VOTA achieves 99.41% [`vota_seed42_v5`] (+24.3pp) — a +17.6pp advantage. Label-only loss ablation (plan_002) quantifies the causal decomposition: **gradient dilution contributes ~26% of the gap** (4.5pp; label-only full_trace = 86.22% [`full_trace_label_only_seed42`]), **information overload contributes ~74%** (13.0pp; only trace compression resolves this). Even with oracle loss masking that eliminates gradient dilution, full traces still underperform VOTA by 13pp.

Cross-model evidence reinforces this: VOTA gap (14.96pp) partly tracks base model execution reasoning capability (Qwen CRUXEval-I 56.5% vs DeepSeek 39.0%, Δ=17.5pp), though **confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated to ~2048 tokens; see D11). The two factors cannot be disentangled in the current design. Exception signal partially bypasses both bottlenecks (token-short, no truncation; consistently best component on both models), though DeepSeek shows seed-dependent absolute performance (91-99%).

**Supporting evidence:**
- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (gradient dilution fix, +4.5pp over standard full_trace)
- `full_trace_seed42_v5`: 81.76%, ECE=0.0958 (standard full_trace)
- `vota_seed42_v5`: 99.41%, ECE=0.0054
- `deepseek_vota_seed42`: 84.45% (VOTA model-dependent)
- CRUXEval literature data (Wang et al.)

### Claim 3: Two-tier diagnostic hierarchy for verdict prediction

Component ablation reveals verdict-relevant trace information has a strict two-tier hierarchy:
- **Tier 1 — diagnostic moment signals**: exception summaries (99.83% [`vota_exception_only_seed42_v2`]) and assertion-point information (99.92% [`vota_ae_only_seed42`]) are individually near-perfect and sufficient for verdict prediction on Qwen. These signals are structurally simple and consistently the most effective component on both models, though DeepSeek absolute performance is seed-dependent.
- **Tier 2 — behavioral patterns**: loop compression (85.63% [`vota_loop_only_seed42`]) carries substantial signal but is model-dependent and fully subsumed by Tier 1.

Combining tiers introduces noise rather than helping: exception_only (99.83%) > VOTA full (99.41%), p=0.01. Loop_only ≈ full_trace_label_only (85.63% vs 86.22%) confirms VOTA's loop compression precisely extracts the useful behavioral signal from full traces.

**Supporting evidence:**
- `vota_exception_only_seed42_v2`: 99.83%, ECE=0.0027 (Tier 1 exception)
- `vota_ae_only_seed42`: 99.92%, ECE=0.0004 (Tier 1 assertion-point, 与 exception 统计等价 p=0.80)
- `vota_loop_only_seed42`: 85.63%, ECE=0.0831 (Tier 2 behavioral)
- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (≈ loop_only, confirming extraction equivalence)
- `deepseek_exception_only_seed42`: 99.83% epoch1 / 99.33% epoch3 (Tier 1 cross-model validation)
- `deepseek_vota_seed42`: 84.45% (Tier 1+2 cross-model: Tier 2 introduces model-dependent degradation)

**Calibration**: 完整 calibration 数据确认 Tier 1 信号不仅 accuracy 近完美，置信度校准也近完美：

| Condition | Accuracy | ECE | Brier | 解读 |
|-----------|----------|-----|-------|------|
| ae_only | 99.92% | 0.0004 | 0.0008 | 近乎完美校准 |
| exception_only | 99.83% | 0.0027 | 0.0013 | 近乎完美校准 |
| VOTA | 99.41% | 0.0054 | 0.005 | 优秀，但 Tier 2 引入轻微 noise |
| loop_only | 85.63% | 0.0831 | — | Tier 2 单独校准中等 |
| label_only | 86.22% | 0.1107 | — | gradient dilution fix 仍 miscalibrated |
| full_trace | 81.76% | 0.0958 | — | 中度 miscalibrated |
| no_trace | 75.13% | 0.1715 | 0.1972 | 严重 miscalibrated |

no_trace ECE 是 exception_only 的 **~63x**（0.1715/0.0027），Brier 是 **~150x**（0.1972/0.0013）。Trace signal（尤其 Tier 1）不仅提升 accuracy，更从根本上改善模型 calibration。

**Design principle**: verdict-optimized traces should extract highest-specificity diagnostic signals; lower-specificity signals are redundant and may introduce noise.

## Cross-Model Evidence Summary

| Condition | Qwen-2.5-Coder-7B | DeepSeek-Coder-6.7B | Cross-model gap | Interpretation |
|-----------|-------------------|---------------------|-----------------|----------------|
| exception_only | 99.83% ± 0.00 (3 seeds) | seed42/456: 99.33%; seed123: 91.09% | 0.50-8.74pp (seed-dependent) | **Best component on both models**; 2/3 DeepSeek seeds match Qwen-level; 1 outlier still > VOTA |
| VOTA | 99.41% | 84.45% | -14.96pp | Model-dependent — requires execution reasoning; **also confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated from mean 2626 to ~2048 tokens; labels preserved via to_chat_text(), see D11) |
| no_trace | 75.13% | 73.36% | -1.77pp | Baseline gap tracks general capability |
| full_trace | 81.76% | collapsed (v3 pending) | N/A | DeepSeek v1 label truncation bug |

**Key insight**: Exception_only is consistently the best component on both models (even worst DeepSeek seed 91.09% > VOTA 84.45%). Cross-model gap 与 signal complexity 正相关, but exception signal's absolute effectiveness also depends on LoRA training stability. Qwen: perfectly robust (3 seeds identical). DeepSeek: 2/3 seeds at 99.33% (matching Qwen-level), 1 outlier at 91.09% (LoRA initialization). Median performance robust; seed sensitivity suggests smaller/weaker models may need training stabilization (multi-seed selection, warmup tuning) for optimal exception signal utilization.

## VOTA Repositioning

**旧叙事**: VOTA 是 trace compression 方法，价值在于"压缩使 trace 更有效"。

**新叙事**: VOTA 是 **fault indicator isolation** 方法，核心价值在于自动从 noisy execution traces 中提取 exception events 等 diagnostic signals。

**证据链**:
1. exception_only (99.83%) ≥ VOTA full (99.41%) — 压缩后的其他组件（loop, ae）不仅无益，反而引入 noise
2. VOTA 跨模型 gap = 14.96pp — 因为 VOTA 包含 model-dependent 的 Tier 2 组件（loop compression 需要 execution reasoning）
3. exception_only 在两个模型上均为最优组件 — isolate 出 Tier 1 后，相对优势 robust（虽然 DeepSeek 绝对值 seed-dependent）
4. vota_no_ae (99.41%) = VOTA (99.41%) — actual/expected 移除无影响，exception 是真正的 active ingredient

**论文中的表述**: "VOTA's trace compression pipeline incidentally isolates exception events — the minimal sufficient diagnostic signal. Its value lies not in making traces shorter, but in separating high-specificity fault indicators from low-specificity behavioral patterns."

**对 Method section 的影响**: VOTA 仍然完整描述（loop compression + exception + actual/expected），但 Results/Discussion 明确指出 exception isolation 是核心机制，其他组件是 model-capability-dependent bonus。

## Story Spine

- **Problem**: Existing trace SFT studies (DCSH, TracePile) evaluate only generative tasks and find limited, model-dependent benefit. No prior work has tested trace SFT on verdict tasks (binary pass/fail), nor identified what trace components drive classification performance.

- **Existing approaches & gaps**: DCSH (EMNLP Findings 2025) tested 5 trace formats on generation tasks, finding that "no single trace representation consistently outperforms others." TracePile (NeurIPS 2025) scaled to 2.6M samples but only evaluated generation. TRACED (ICSE 2024) showed traces help encoder-based classification. All existing trace formats are designed for execution simulation, not fault detection.

- **Our framing**: We reframe verdict prediction as **fault detection** and ask: what is the minimal sufficient diagnostic signal? Through systematic component ablation across two architecturally distinct models, we discover that exception events — compact, structured error summaries — are consistently the most effective trace component, achieving near-perfect accuracy on Qwen (99.83% ± 0.00, 3 seeds) and outperforming all alternatives on DeepSeek (91-99% vs VOTA 84.45%). Richer trace representations work only when the base model has sufficient execution reasoning capability, making them unreliable for general deployment.

- **Headline result**: "Exception events consistently achieve the highest verdict accuracy across models (Qwen 99.83%, DeepSeek 91-99%), outperforming VOTA traces (84.45% on DeepSeek, -14.96pp gap) — demonstrating that fault indicator isolation, not trace reasoning, is the robust mechanism for verdict prediction. DeepSeek seed sensitivity reveals LoRA training stability as a secondary factor for smaller models."

## Story Arc

1. **Setup**: Trace SFT for code tasks — promising but inconsistent in prior work (DCSH, TracePile). Unknown whether traces help verdict tasks and what trace design matters.

2. **First result — traces help, compression helps more** (single model): no_trace 75.13% → full_trace 81.76% → VOTA 99.41%. Label-only loss ablation decomposes the gap: 26% gradient dilution, 74% information overload. Compression improves accuracy through higher information density, not just cost savings.

3. **Twist — what component actually drives VOTA?** Component ablation reveals exception_only (99.83%) ≥ full VOTA (99.41%). The "trace reasoning" narrative is wrong — verdict prediction is fault detection. Tier 1 (exceptions + assertion-point) subsumes Tier 2 (loops). Actual/expected removal doesn't hurt (99.41%).

4. **Cross-model stress test — consistent dominance, not universal perfection**: Exception_only is the best component on both models (even DeepSeek worst seed 91.09% > VOTA 84.45%), but absolute performance is seed-dependent on DeepSeek (91-99% vs Qwen's perfectly stable 99.83%). VOTA degrades by 14.96pp. The structurally simplest component is the most robust, but LoRA initialization sensitivity introduces variance on weaker models. Qwen seed robustness (3-seed variance = 0) + calibration (ECE=0.0027) 确认 exception signal 在强模型上的 reliability。DeepSeek seed sensitivity 揭示 training stability 作为 secondary bottleneck。

5. **Design principle**: For verdict tasks, identify the highest-specificity diagnostic signal (exception events) and discard everything else. VOTA's value is fault indicator isolation — automatically extracting exceptions from noisy traces — not generic compression. Simpler signals are more robust; complexity tolerance depends on model capability.

## Dataset Characteristics

### Data duplication analysis

| Condition | Total | Unique | Duplication rate | Cause |
|-----------|-------|--------|------------------|-------|
| exception_only_train | 4720 | 2858 | 39.45% | 同题多个 passing 解映射为相同 (input, output) — 无异常 → 同一 trace |
| exception_only_test | 1190 | 607 | 48.99% | 同上 |
| raw_traces | 5910 | 5803 | 1.81% | 完整 trace 含行号/变量值/内存地址，几乎不重复 |

**Train-test input overlap: 0（无数据泄漏）**

**解读**: exception_only 高重复率是 representation 的自然属性，非数据问题。多个正确解对同一测试用例执行时若均无异常，exception_only 表征退化为相同的空/无异常标记。这恰好说明 exception signal 的 compactness — 它仅编码 fault presence，不编码 solution identity。raw_traces 重复率极低 (1.81%) 因为完整 trace 包含 solution-specific 信息（变量值、内存地址）。尽管高重复率意味着有效训练样本少于名义数量，模型仍达 99.83% — 进一步确认 exception signal 的 learnability。

## DeepSeek full_trace 处理

**现状**: v1 坍塌（28.5%, 100% 预测 fail, 根因: 训练端 label 截断）。v2 重训启动但被 kill（Loop #6 ops worker 腾 GPU 给 vota_seed456）。v3 RUNNING（label-preserving truncation fix）。

**处理方案**: v3 正在 cuda:0 上训练，预计 5/16 完成。

**VOTA vs full_trace 截断机制区分** (D030 token analysis 确认):
- **full_trace v1**: SFTTrainer right-truncation 切掉了 verdict **label** → 100% predict fail → 坍塌。根因: DeepSeek tokenizer 对 full_trace 产生 >2048 tokens, label 在截断窗口外。
- **VOTA**: `to_chat_text()` 保留 verdict label（label 完整），但 91.7% 的样本 **trace content（input）被截断**（mean 2626 → ~2048 tokens）。84.45% 是真实结果，反映 trace 信息损失对模型学习的影响，**不是** label corruption。
- **exception_only**: token 长度远低于 2048，不受截断影响，跨模型对比 clean。

**对论文叙事的影响**: 论文中所有 "right-truncation corrupts/removes the verdict label" 措辞**对 VOTA 不成立**——label 完整保留，被截断的是 trace input。正确表述: "trace content truncation causes information loss"。VOTA cross-model gap (14.96pp) 有两个贡献因素: (1) model capability, (2) training-time trace truncation on DeepSeek (see D11)。

## External Benchmark (DebugBench) Positioning

**DebugBench 仅作泛化性验证，不作 trace importance 证据。**

| Condition | Main Dataset | DebugBench | Δ interpretation |
|-----------|-------------|------------|------------------|
| no_trace | 75.13% | 96.71% | DebugBench 天花板高，baseline 已强 |
| VOTA | 99.41% | 99.77% | +3.06pp lift — 边际 |
| exception_only | 99.83% | 100.00% | +3.29pp lift — 边际 |

**主数据集 trace lift = 24.70pp**（no_trace → exception_only），DebugBench trace lift 不到其 1/7。

**论文定位规则**：
- DebugBench → 泛化性证据（exception_only 100% = 跨数据集鲁棒性）
- Trace importance 论证 → 仅依赖主数据集（24.7pp lift）
- 禁止用 DebugBench 的 3.29pp lift 论证 "trace 的核心价值"——审稿人会攻击天花板效应

## Venue Fit Risks

| Risk | Assessment | Mitigation |
|------|-----------|------------|
| 单任务 | 仍然只在 test verdict prediction 上验证 | 跨模型验证部分弥补; Discussion 中讨论 generalization |
| 单数据集 | HumanEval + MBPP-sanitized 是唯一数据源 (591 problems × 10 solutions) | 定位为 empirical study, 深度优于广度; 两个标准 benchmark 组合覆盖多样编程题型; exception_only 有效训练样本仅 2858 unique 即达 99.83%, 暗示 signal 的 simplicity 降低对数据量的依赖 |
| "只是 feature engineering" | exception extraction 不复杂 | simplicity 本身是 contribution — 最简信号最 robust |
| Negative result 味道 | VOTA 跨模型不 robust | Reframe: 识别 robust vs non-robust 组件边界是 positive |
| Seed robustness (Qwen) | ✅ 已解决: 99.83% ± 0.00 (3 seeds), irreducible samples 确认 | — |
| Seed robustness (DeepSeek) | ✅ 3-seed 完整: 2/3 at 99.33%, 1 at 91.09% | LoRA initialization sensitivity — median robust, worst still > all alternatives; 转化为 training stability finding (D9/D10) |
| Calibration | ✅ 完整数据: Tier 1 ECE≤0.003, no_trace ECE=0.171 (~63x gap) | Brier ~150x gap 进一步确认 |
| 只用 2 个模型 | 有限但有意义的 diversity | Architecture + pretraining data (5.5T vs 2T) + CRUXEval gap (17.5pp) 构成充分差异 |
| 数据重复率 | exception_only 训练集 39.45% 重复 | 非数据泄漏（train-test overlap = 0）；是 representation compactness 的自然结果；有效样本仍足够学习 |

## Anticipated Reviewer Concerns

| Concern | Planned Response |
|---------|-----------------|
| "exception_only 99.83% 是不是 trivial pattern matching [ERROR] 有无？" | full_trace 也包含 [ERROR] 但仅 81.76%——模型需要从 trace context 中 extract 和 utilize exception signal, 不是简单 keyword detection. no_trace 无 exception, 75.13%. |
| "为什么 exception_only > VOTA? adding info 反而降?" | 非 exception 组件 (loop/ae tokens) 稀释 attention 对 exception 信号的聚焦. Calibration: exception_only ECE=0.0027 vs VOTA ECE=0.0054. 部分样本 loop 正常但有 exception, 引入矛盾信号. |
| "CRUXEval gap 与 VOTA gap 的相关性可能是 coincidence" | 明确标注为 hypothesis. 列出 alternatives (tokenizer efficiency, pretraining scale 2.75x, chat template). 不 overclaim. |
| "只有 2 个模型，universality claim 太强" | 同意是 limitation. 两模型在 architecture (RoPE vs ALiBi), pretraining data (5.5T vs 2T), execution reasoning (CRUXEval 17.5pp gap) 上有充分差异, 不是 trivial replication. Exception signal 的 structural simplicity 提供 inductive argument for broader generalization. |
| "99.83% 可能 saturated, 看不出 exception 到底学了什么" | Calibration 双指标: exception_only ECE=0.0027, Brier=0.0013 (近完美校准). 对比 no_trace ECE=0.1715, Brier=0.1972 (~63x/~150x gap). **Irreducible error 根因已明确**: 2/1190 errors 均因 Python `all()` 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误），tracer 将其标记为 `[ERROR]`。模型看到 7 行 `[ERROR] GeneratorExit` 合理预测 fail，但代码实际正确。整个测试集仅这 2 条含 `GeneratorExit`，无训练信号可学习其良性本质。99.83% 是 representation 的理论上限，非 saturation artifact。 |
| "只用了 1 个 seed" | Qwen ✅: 3 seeds 99.83% ± 0.00. DeepSeek ✅: 3 seeds 完整 — seed42/456=99.33%, seed123=91.09%。2/3 鲁棒，1 离群。median=99.33%, worst=91.09% (仍 > VOTA 84.45%)。论文透明报告所有 seeds，将 seed sensitivity 转化为 LoRA training stability 的 finding（D9）。 |
| "eval_loss 上升但 accuracy 提升——checkpoint selection 有问题?" | Discussion D1: token-level loss 与 binary verdict accuracy 解耦. 推荐 verdict-specific metric. Methodological contribution. |
| "DeepSeek full_trace 坍塌是 bug 不是 finding" | 诚实披露根因 (训练端 label 截断). 其他 3 条件不受影响. 修复版本如就绪则补入. |
| "calibration 数据只有 1 个 seed" | Seed robustness 已证明 accuracy variance=0 (3 seeds), calibration 在 accuracy 完全一致的前提下 expected 也一致. ECE/Brier 的极小值 (0.0027/0.0013) 留有极小 variance 空间. |
| "DeepSeek epoch1 > epoch3, 为什么用 epoch3 报告?" | 正文报告所有 seeds 的 final + best checkpoint。seed42: epoch1=99.83%, epoch3=99.33%。seed123: epoch1=91.43%, epoch3=91.09%。D7 讨论 early stopping + D9 讨论 LoRA initialization sensitivity。不 cherry-pick best seed。 |
| "DeepSeek seed sensitivity 说明 exception signal 不 robust" | Exception_only 在所有 seeds 上仍优于其他条件（worst seed 91.09% > VOTA 84.45%）。Seed sensitivity 是 LoRA training 问题而非 signal 问题——Qwen 3 seeds 完美证明 signal 本身 robust。D9 讨论 training stabilization 作为 practical recommendation。 |
| "exception_only 数据集 ~40-49% 重复，有效训练样本不足？" | 重复源自 representation compactness：同题多个 passing 解均无异常 → 相同 trace。**非数据泄漏**（train-test input overlap = 0）。raw_traces 仅 1.81% 重复，确认重复是 exception_only 表征特性而非数据收集问题。模型在有效样本仅 2858 unique 的条件下仍达 99.83%，反而说明 exception signal 的高 learnability — 少量 unique 样本即可充分学习 fault detection pattern。 |

## Discussion 要点

### D1: eval_loss vs verdict accuracy 解耦
DeepSeek VOTA: eval_loss epoch1→3 从 0.068 升至 0.112 (+65%), 但 accuracy 从 78.15% 升至 84.45% (+6.3pp). Token-level calibration 与 binary classification accuracy 方向相反. **Implication**: verdict tasks 应用 task-specific metric (accuracy/F1) 做 checkpoint selection, 非 eval_loss.

### D2: CRUXEval gap 假说 (revised — D030 confound)
VOTA 跨模型 gap (14.96pp) 与 CRUXEval execution reasoning gap (15-17.5pp) 数值吻合. 假说: trace utilization effectiveness 受 base model "execution reasoning readiness" 约束. **标注**: hypothesis, N=2, 列出 alternatives. 不 overclaim. **注意**: 我们的训练/测试数据来自 HumanEval + MBPP-sanitized（非 CRUXEval），CRUXEval-I 分数仅作为衡量两个模型 execution reasoning 能力差异的外部参照。论文中必须明确区分数据来源与外部基准引用。**D030/D034 truncation evidence**: 14.96pp gap 中截断效应有因果证据: group_analysis 显示 train-truncated 83.04% vs train-intact 100% (Fisher p≈0, 推理时无截断)。截断因果方向可 claim，模型能力差异是 residual confound。CRUXEval gap 数值吻合可能部分巧合。论文中截断效应应作为 established factor 讨论（有 group_analysis 因果证据），模型能力假说标注为 residual confound hypothesis。

### D3: Simplicity as robustness (revised)
Exception signal 在两模型上均为最优组件，其结构简单性确保了相对优势的跨模型 robustness。但 DeepSeek seed sensitivity 揭示：simplicity 确保 signal 本身 robust，但 LoRA 训练过程是否稳定收敛到正确映射取决于模型。**trace design 应匹配 deployment model 的能力下界**，且需关注 training stability（建议：多 seed 验证 + 考虑 training stabilization 技巧如 warmup、learning rate schedule）。

### D4: Checkpoint selection 与 gap 报告 (revised)
正文报告所有 seeds 的 final checkpoint 结果 + best checkpoint 结果，不 cherry-pick。DeepSeek seed42: epoch1=99.83%, epoch3=99.33%（退化 0.50pp）。DeepSeek seed123: epoch1=91.43%, epoch3=91.09%（退化 0.34pp）。两个 seed 均显示轻微 epoch 退化，但核心差异在 epoch1 起点（8.40pp gap），不是训练过程。

### D5: Irreducible samples — GeneratorExit 根因分析
3 seeds 的 2/1190 errors 完全相同（id=901, 905, 均来自 HumanEval/95 `check_dict_case`），方向一致（pass→fail false negatives）。

**根因**: Python `all()` 对 generator expression 短路时丢弃未耗尽的 generator，触发 `GeneratorExit`。`GeneratorExit` 继承自 `BaseException`（非 `Exception`），是 Python 内部控制流机制而非真正错误。但 tracer 对所有 caught exceptions 统一标记 `[ERROR]`，导致 exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。

**为何不可约**:
1. **表征局限**: exception_only 条件下模型仅见异常数据，无法访问控制流、返回值或 assertion 结果。`GeneratorExit` 在此表征中与真正错误不可区分。
2. **跨 seed 确定性**: 3 个 random seeds 产生完全相同的 errors，确认这是 data/representation 属性而非模型初始化随机性。
3. **训练集无信号**: 整个 1190 条测试集仅这 2 条含 `GeneratorExit`，训练集中也缺乏足够的 `GeneratorExit` 良性样本供模型学习。
4. **人类也会犯错**: 仅看 exception trace（7 行 `[ERROR]`），人类审查者在不了解 Python generator protocol 的情况下也会预测 fail。

**对论文的意义**: (1) 99.83% 是 exception_only representation 在此数据集上的理论 ceiling，非 saturation artifact；(2) 揭示 tracer 设计的改进方向——区分 `BaseException` 子类（如 `GeneratorExit`, `KeyboardInterrupt`）与 `Exception` 子类（真正的程序错误）可消除此类 irreducible error；(3) 提供 concrete evidence 说明 exception_only 模型"理解"的是 `[ERROR]` tag 的 fault indicator 语义，而非 exception type 的 fine-grained 含义。

### D6: Calibration as secondary evidence
Calibration 数据提供独立于 accuracy 的 evidence dimension。no_trace Brier=0.1972 说明模型无 trace 时不仅预测错，且对错误预测过度自信。exception_only Brier=0.0013 说明模型在有 exception signal 时几乎完美区分确定性和不确定性。这支持 Claim 1 的 "sufficient signal" 论点——exception 不仅让模型预测对，还让模型 "知道自己对"。

### D7: Early stopping for exception signal (revised — D030 epoch1 data complete)
3-seed epoch1 完整数据：seed42 epoch1=99.83% → epoch3=99.33%（-0.50pp）；**seed456 epoch1=99.33% → epoch3=99.33%（0.00pp）**；seed123 epoch1=91.43% → epoch3=91.09%（-0.34pp）。**seed42 的 epoch1=99.83%（匹配 Qwen）是该 seed 独有的 LoRA 初始化运气，不是 DeepSeek epoch1 的通用属性。** seed456 epoch1=epoch3 说明 epoch 退化非普遍现象。核心差异仍是 LoRA 初始化（epoch1 起点差 8.40pp），不是 overfitting。Early stopping 无法挽救差的初始化（seed123）。**Implication**: (1) 报告 DeepSeek 结果时应使用 median/2-of-3 (99.33%)，不应以 seed42 epoch1=99.83% 作为 headline；(2) epoch1 peak 是 LoRA 初始化运气的副产物，不具推广性。对比: VOTA 在 DeepSeek 上 84.45% **已确认正确**（D030 关闭: confirmatory re-eval max_length=16384 → 84.45%，与原始训练评估精确一致；D030 根因是 evaluate.py v2 的 max_length=2048 eval-time 截断 bug 导致 82.6% 预测为 garbage tokens）。

### D9: LoRA initialization sensitivity as secondary bottleneck [NEW — D028]
DeepSeek exception_only seed42=99.83% vs seed123=91.43% (epoch1), 8.40pp gap。Qwen 3 seeds 完全一致。假说：exception signal 的 learnability 取决于 (1) signal 本身的结构简单性（cross-model robust）+ (2) LoRA 初始化是否落入能正确映射 exception→verdict 的 basin。Qwen-7B 可能因模型更强/LoRA landscape 更平滑而对初始化不敏感。DeepSeek-6.7B（CRUXEval-I 39% vs Qwen 56.5%）的 loss landscape 可能更 rugged，LoRA 初始化更易陷入 suboptimal basin（seed123 的 fail_recall 仅 70-72% 说明模型未学到 exception→fail 映射的关键部分）。**论文角度**: 这不是 negative result——它揭示了 trace SFT 的 practical consideration（training stability），可作为 contribution 的一部分。建议 Discussion 讨论 training stabilization 策略（warmup, lr schedule, LoRA rank 调整, multi-seed selection）。

### D10: Train loss ≈ but accuracy ≠ across seeds [NEW — D029]
DeepSeek exception_only seed456 (train_loss=0.1225) 与 seed123 (train_loss=0.122) 训练损失几乎相同，但 accuracy 差 8.2pp（99.33% vs 91.09%）。关键差异集中在 fail_recall（1.0 vs 0.705）——token-level loss 在所有 tokens 上平均，掩盖了 fail 类少数样本的 sample-level 分类能力差异。**Implication**: (1) 扩展 D1 (eval_loss vs accuracy decoupling) 到训练阶段：train_loss 同样不是 verdict task accuracy 的可靠代理指标；(2) 对 checkpoint selection 的实际建议更强：必须用 task-specific metric (accuracy/F1)，甚至 train_loss 收敛也不保证 task performance；(3) fail 类作为少数类（28.5%），其学习质量被平均 loss 稀释——这在 class-imbalanced 设置下是 general pattern，可推广到其他 verdict/detection 任务。

### D11: VOTA cross-model gap: training-time trace truncation as causal factor [NEW — D030 token analysis + group_analysis]
D030 token analysis 确认: `to_chat_text()` 保留 labels（verdict label 在训练时未被截断），但 91.7% 的 DeepSeek VOTA 训练样本的 **trace content** 从 mean 2626 tokens 被截断到 ~2048 tokens。

**Group analysis 提供因果证据**: 将测试集按训练截断状态分组（推理时无截断, max_length=16384），train-truncated 组 accuracy=83.04% vs train-intact 组 accuracy=100%, Fisher exact p≈0。**截断的因果方向可以 claim**: 训练时 trace 被截断导致模型学到的信息不完整 → 推理时即使看到完整 trace 也无法正确判断。模型能力差异是残余 confound（无法完全分离）。

**Implications**: (1) 论文中所有 "right-truncation corrupts/removes the verdict label" 措辞对 VOTA 不成立——label 完整保留，被截断的是 trace INPUT content；(2) 14.96pp gap 中截断效应有因果证据（group_analysis），模型能力差异是 residual confound；(3) exception_only 因 token 长度短（远低于 2048）不受截断影响，其跨模型对比更 clean——进一步强化 Claim 1 "most robust component" 叙事；(4) 论文应讨论 max_length 的影响作为 limitation/future work；(5) group_analysis 数据可作为 Table/Figure 纳入论文——展示截断的因果效应。

### D8: Data duplication as representation signature
exception_only 训练集 39.45% 重复（4720→2858 unique），测试集 48.99%（1190→607 unique），而 raw_traces 仅 1.81%（5910→5803 unique）。重复源自 exception_only 表征的 design-by-intent compactness：同一编程题的多个 passing 解执行时均无异常，exception_only 表征退化为相同的空标记。这一数据特征本身就是 Claim 3 two-tier hierarchy 的佐证——Tier 1 信号仅编码 fault presence/absence，不编码 solution-level details，因此天然高重复。Train-test input overlap = 0 排除数据泄漏。

## Contingency Framing (已解决, 留存档)

### Claim 1 — RESOLVED (D029: seed456=99.33% confirms "consistently best component")
seed456 与 seed42 完全一致（均 99.33%），seed123 为孤立离群值。Claim 1 定稿为 "exception events consistently best component across models; absolute performance seed-dependent on DeepSeek (2/3 seeds robust, 1 outlier from LoRA init sensitivity); relative dominance over all alternatives robust across all seeds"。"0pp universal gap" 叙事已放弃，转为数据驱动的 nuanced framing。

### Claim 2 — RESOLVED (D006 + D009)
v5 full_trace 81.76%. plan_002 label-only 86.22%, gradient dilution = minor (26%). 跨模型 VOTA gap 补充证据.

## 与 v1 Framing 的关键差异

| 维度 | v1 | v2.9 |
|------|----|----|
| Headline | VOTA compression 优于 full trace | Exception events are the most effective diagnostic signal |
| Primary claim | VOTA +24pp through fault indicator preservation | Exception signal consistently best across models; absolute performance seed-dependent on DeepSeek |
| Claim 2 | Compression > full trace (只有 gradient dilution) | Information density primary + gradient dilution quantification + cross-model reinforcement |
| Claim 3 Tier 1 | exception_only only | exception + assertion-point (co-Tier 1, D020) |
| VOTA 定位 | 核心方法 — trace compression | **Fault indicator isolation** — 价值在于提取 exception, 非 generic compression |
| Model scope | 单模型 (Qwen) | 双模型, 跨模型对比是核心贡献 |
| DeepSeek full_trace | N/A | v1 collapsed (label truncation), v3 pending |
| Seed robustness | 未验证 | Qwen ✅ 99.83% ± 0.00 (3 seeds); DeepSeek ⚠️ seed-dependent (91-99%, D028) |
| Irreducible error | 未分析 | ✅ GeneratorExit 根因明确，99.83% = representation ceiling |
| Calibration | 未验证 | ✅ 完整 ECE+Brier, ~63x/~150x gap vs no_trace |
| Data duplication | 未分析 | ✅ exception_only ~40% 重复（representation compactness），train-test overlap = 0 |
| Early stopping | 未讨论 | DeepSeek epoch1→epoch3 轻微退化 (0.3-0.5pp); 核心问题是 LoRA 初始化 (seed123 epoch1=91.43%), 非 overfitting |
| Narrative arc | "VOTA helps" | "Exception events are consistently best; VOTA's value is isolating them; training stability matters" |


## experiment_plan (with registry status)

- id: plan_001
  claim: 1
  description: 'Ablation: 去除 VOTA 中 actual/expected 值对，只保留 assertion structure + exception
    info。验证 VOTA 效果是 genuine behavioral understanding 还是 trivial string comparison。'
  priority: P0
  gpu_budget_hours: 3
  deps: []
  registry_id: vota_no_ae_seed42
  notes: 如果去 actual/expected 后 acc 仍 >80%，证明非 trivial；如果降到 ~75%(=no_trace)，则是字符串比对。决定
    Claim 1 强度和论文 framing。
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.994
    majority_baseline: 0.7151
    lift: 0.279
    n: 1190
    pass_f1: 0.996
    fail_f1: 0.989
    accuracy_ci_lower: 0.989
    accuracy_ci_upper: 0.998
    lift_vs_notrace: 0.243
    lift_vs_notrace_ci_lower: 0.218
    lift_vs_notrace_ci_upper: 0.268
    train_loss: 0.0908
    eval_loss: 0.2215
    wall_clock_seconds: 6397.88
- id: plan_002
  claim: 2
  description: 'Ablation: full_trace + label-only loss (只对分类 token 计算 loss，mask trace
    tokens)。验证 collapse 根因是 gradient dilution 而非数据/代码 bug。'
  priority: P0
  gpu_budget_hours: 3
  deps: []
  registry_id: full_trace_label_only_seed42
  notes: 如果 label-only loss 修复 collapse (acc >70%)，确认 gradient dilution 假说。如果仍 collapse，可能是
    trace noise/length 本身就有害。
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.8622
    accuracy_ci_lower: 0.8437
    accuracy_ci_upper: 0.8807
    majority_baseline: 0.7151
    lift: 0.1471
    n: 1190
    pass_precision: 0.8821
    pass_recall: 0.9318
    pass_f1: 0.9063
    fail_precision: 0.8007
    fail_recall: 0.6873
    fail_f1: 0.7397
    train_loss: 0.2505
    eval_loss: 0.3205
    lift_vs_notrace: 0.1109
    lift_vs_notrace_ci_lower: 0.0849
    lift_vs_notrace_ci_upper: 0.137
    lift_vs_standard_fulltrace: 0.0445
    lift_vs_standard_fulltrace_ci_lower: 0.0235
    lift_vs_standard_fulltrace_ci_upper: 0.0655
    lift_vs_standard_fulltrace_pvalue: 0
- id: plan_003
  claim: 3
  description: 'VOTA component ablation: 分别测试 (a) 只有 actual/expected, (b) 只有 exception
    summary, (c) 只有 loop compression, (d) 全量 VOTA。量化每个组件的贡献。'
  priority: P0
  gpu_budget_hours: 8
  deps:
  - plan_001
  registry_id: vota_loop_only_seed42
  notes: '4 个 sub-conditions。registry IDs: vota_loop_only_seed42 (loop_only 85.6%),
    vota_exception_only_seed42_v2 (exception_only 99.83%), vota_ae_only_seed42 (ae_only
    99.92%)。plan_001 vota_no_ae_seed42 (99.4%) 覆盖 ae 冗余确认。'
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.8563
    majority_baseline: 0.7151
    lift: 0.1412
    n: 1190
    pass_precision: 0.9239
    pass_recall: 0.8707
    pass_f1: 0.8966
    fail_precision: 0.7165
    fail_recall: 0.8201
    fail_f1: 0.7648
    accuracy_ci:
    - 0.8353
    - 0.8756
    bootstrap_vs_no_trace:
      diff: 0.105
      ci:
      - 0.0824
      - 0.1286
      significant: true
    bootstrap_vs_vota:
      diff: -0.1378
      ci:
      - -0.1571
      - -0.1185
      significant: true
    bootstrap_vs_full_trace:
      diff: 0.0387
      ci:
      - 0.0185
      - 0.0597
      significant: true
    train_loss: 0.0718
    wall_clock_seconds: 7425.65
- id: plan_004
  claim: 1
  description: '第二模型验证: DeepSeek-Coder-6.7B 上复现 4 条件（VOTA/no_trace/full_trace/exception_only），与
    DCSH 同模型直接对比。exception_only 跨模型验证 exception dominance。'
  priority: P1
  gpu_budget_hours: 8
  deps:
  - plan_001
  registry_id: deepseek_exception_only_seed42
  notes: '4 条件: deepseek_vota_seed42 (84.45% ✅), deepseek_no_trace_seed42 (73.36%
    ✅), deepseek_exception_only_seed42 (99.33% ✅), deepseek_full_trace_seed42_v3 (RUNNING,
    label truncation fix). 3/4 完成, full_trace v3 待完成。'
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9933
    majority_baseline: 0.7151
    lift: 0.2782
    n: 1190
    pass_precision: 1
    pass_recall: 0.9906
    pass_f1: 0.9953
    fail_precision: 0.9769
    fail_recall: 1
    fail_f1: 0.9883
    epoch1_checkpoint_eval:
      accuracy: 0.9983
      fail_recall: 1
      fail_precision: 0.9941
      pass_recall: 0.9976
      conclusion: epoch1_better_by_0.50pp
- id: plan_005
  claim: 1
  description: '第二任务验证: 在 DebugBench subset 上测试 exception_only/VOTA/no_trace。验证 verdict
    task 跨任务泛化性。'
  priority: P1
  gpu_budget_hours: 6
  deps:
  - plan_001
  registry_id: debugbench_exception_only_seed42
  notes: 3/3 完成。debugbench_exception_only_seed42=100.0% (426/426, Wilson CI [99.14%,100%]),
    debugbench_vota_seed42=99.77% (1 error), debugbench_no_trace_seed42=96.71%。定位为
    generalization validation（非 trace importance evidence，因 no_trace baseline 96.71%
    已很高，marginal contribution 仅 3.29pp）。
  status: DONE
  conclusion: success
  metrics:
    accuracy: 1
    majority_baseline: 0.5141
    lift: 0.4859
    n: 426
    pass_precision: 1
    pass_recall: 1
    pass_f1: 1
    fail_precision: 1
    fail_recall: 1
    fail_f1: 1
    accuracy_ci_wilson:
    - 0.9914
    - 1
    accuracy_ci_bootstrap:
    - 1
    - 1
    train_loss: 0.2435
    eval_loss: 0.4157
    train_runtime_sec: 837
- id: plan_006
  claim: 2
  description: 'Trace length ablation: 测试不同截断长度 (256/512/1024/no_limit) 对 full_trace
    准确率的影响。2048tok 取消（train_sft.py 硬编码 max_length=2048，与 no_limit 等价）。'
  priority: P1
  gpu_budget_hours: 8
  deps:
  - plan_002
  registry_id: full_trace_256tok_seed42
  notes: '4 点设计: 256tok=78.82% (DONE), 512tok=80.42% (DONE), 1024tok (RUNNING), no_limit=81.76%
    (full_trace_seed42_v5)。2048tok killed（max_length=2048 硬编码使其与 no_limit 等价）。Registry
    IDs: full_trace_256tok_seed42, full_trace_512tok_seed42, full_trace_1024tok_seed42,
    full_trace_seed42_v5。趋势: 更多 trace 略有帮助但收益递减，且全部远低于 exception_only (99.83%)。'
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 0.7882
    majority_baseline: 0.7151
    lift: 0.0731
    n: 1190
    pass_precision: 0.903
    pass_recall: 0.788
    pass_f1: 0.842
    fail_precision: 0.597
    fail_recall: 0.788
    fail_f1: 0.679
    accuracy_ci:
    - 0.764
    - 0.81
    train_loss: 0.1094
    train_runtime_sec: 3047
    epochs: 3
- id: plan_007
  claim: 3
  description: 'Calibration analysis: ECE + reliability diagrams 对比 VOTA/no_trace/full_trace
    的 calibration 质量。验证 trace SFT 对 verdict task 改善 calibration 的假说。'
  priority: P2
  gpu_budget_hours: 1
  deps: []
  registry_id: calibration_analysis_seed42
  notes: 纯 eval，不需要额外训练。用已有 checkpoint 的 logits 计算。
  status: DONE
  conclusion: success
  metrics:
    no_trace:
      ece: 0.171476
      mce: 0.475643
      brier_score: 0.197152
      accuracy: 0.751261
      n_samples: 1190
    full_trace:
      ece: 0.095817
      mce: 0.249061
      brier_score: 0.143924
      accuracy: 0.817647
      n_samples: 1190
    label_only:
      ece: 0.110686
      mce: 0.417124
      brier_score: 0.120144
      accuracy: 0.862185
      n_samples: 1190
    loop_only:
      ece: 0.083085
      mce: 0.183406
      brier_score: 0.118335
      accuracy: 0.856303
      n_samples: 1190
    ae_only:
      ece: 0.000415
      mce: 0.000415
      brier_score: 0.000847
      accuracy: 0.99916
      n_samples: 1190
    exception_only:
      ece: 0.002717
      mce: 0.835484
      brier_score: 0.001311
      accuracy: 0.998319
      n_samples: 1190
    vota:
      ece: 0.00541
      mce: 0.622459
      brier_score: 0.005234
      accuracy: 0.994118
      n_samples: 1190
- id: plan_008
  claim: 1
  description: 'Seed robustness: 3 random seeds (42/123/456) 验证 VOTA 结果稳定性。McNemar
    test + bootstrap CI。'
  priority: P2
  gpu_budget_hours: 6
  deps:
  - plan_001
  registry_id: exception_only_seed456
  notes: 'Seed robustness 完成。Qwen exception_only: 99.83% ± 0.00 (seeds 42/123/456,
    irreducible 2/1190). Qwen VOTA: seed42=99.41%, seed456=99.08% (Δ<0.4pp). DeepSeek
    exception_only: seed42/456=99.33%, seed123=91.09% (LoRA outlier). Registry IDs:
    exception_only_seed123, exception_only_seed456, vota_seed456_v2, deepseek_exception_only_seed42/123/456.'
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9983
    accuracy_ci:
    - 0.9958
    - 1
    majority_baseline: 0.7151
    lift: 0.2832
    n: 1190
    pass_precision: 1
    pass_recall: 0.9976
    pass_f1: 0.9988
    fail_precision: 0.9941
    fail_recall: 1
    fail_f1: 0.9971
    vs_seed42:
      seed42_accuracy: 0.9983
      seed456_accuracy: 0.9983
      diff: 0
      note: identical accuracy to 4 decimal places; no predictions.jsonl for paired
        bootstrap
    train_loss: 0.1087
    eval_loss: 0.4629
    train_runtime_sec: 4541
    epochs: 3
- id: plan_mvp_vota
  claim: 1
  description: 'MVP: VOTA trace SFT for test verdict prediction'
  priority: P0
  gpu_budget_hours: 2
  deps: []
  registry_id: vota_seed42_v4
  notes: 完成。95.63% accuracy, +20.5pp over baseline.
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9563
    majority_baseline: 0.7151
    lift: 0.2412
    n: 1190
    pass_precision: 0.944
    pass_recall: 0.998
    pass_f1: 0.97
    fail_precision: 0.993
    fail_recall: 0.853
    fail_f1: 0.917
    lift_vs_notrace: 0.205
    lift_vs_notrace_ci_lower: 0.177
    lift_vs_notrace_ci_upper: 0.234
    train_loss: 0.046
    eval_loss: 0.0842
- id: plan_mvp_notrace
  claim: 1
  description: 'MVP: No-trace baseline for test verdict prediction'
  priority: P0
  gpu_budget_hours: 1
  deps: []
  registry_id: no_trace_seed42_v4
  notes: 完成。75.13% accuracy (majority baseline 71.51%).
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.7513
    majority_baseline: 0.7151
    lift: 0.0361
    pass_precision: 0.8776
    pass_recall: 0.7579
    pass_f1: 0.8134
    fail_precision: 0.5473
    fail_recall: 0.7345
    fail_f1: 0.6272
    train_loss: 0.18
    eval_loss: 0.6454
    eval_mean_token_accuracy: 0.8897
- id: plan_mvp_fulltrace
  claim: 2
  description: 'MVP: Full execution trace SFT for test verdict prediction'
  priority: P0
  gpu_budget_hours: 2
  deps: []
  registry_id: full_trace_seed42_v2
  notes: 完成。28.49% accuracy, model collapse (100% predict fail).
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 0.284
    majority_baseline: 0.7151
    lift: -0.4311
    n: 1190
    pass_precision: 0.923
    pass_recall: 0.085
    pass_f1: 0.155
    fail_precision: 0.445
    fail_recall: 0.785
    fail_f1: 0.568
    train_loss: 0.0373
    eval_loss: 0.082
    eval_mean_token_accuracy: 0.984
- id: plan_012
  claim: 1
  description: 'Cross-scale validation: Qwen-2.5-Coder-1.5B 上复现 4 条件 (exception_only/vota/no_trace/full_trace)。
    验证 exception signal 的 scale invariance 假说。'
  priority: P0
  gpu_budget_hours: 8
  deps:
  - plan_003
  registry_id: qwen15b_exception_only_seed42
  notes: '4 条件: exception_only=99.83% (=7B, DONE), vota=99.58% (DONE), no_trace=67.31%
    (DONE), full_trace=RUNNING。关键发现: 1.5B=7B on exception → signal-limited not capacity-limited。
    Registry IDs: qwen15b_exception_only_seed42, qwen15b_vota_seed42, qwen15b_no_trace_seed42,
    qwen15b_full_trace_seed42。'
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9983
    accuracy_ci_lower: 0.9958
    accuracy_ci_upper: 1
    majority_baseline: 0.7151
    lift: 0.283
    n: 1190
    pass_precision: 1
    pass_recall: 0.9976
    pass_f1: 0.9988
    fail_precision: 0.9941
    fail_recall: 1
    fail_f1: 0.9971
    train_loss: 0.1347
    eval_loss: 0.5761
    wall_clock_seconds: 1762
- id: plan_013
  claim: 1
  description: 'Cross-family validation: CodeLlama-13B-Instruct 上测试 3 条件 (exception_only/no_trace/vota)。
    验证 exception dominance 跨 LLaMA 家族 + 更大 scale 的泛化性。'
  priority: P0
  gpu_budget_hours: 12
  deps: []
  registry_id: codellama13b_exception_only_seed42
  notes: 'Model downloaded. 0/3 done, queued. Registry IDs: codellama13b_exception_only_seed42,
    codellama13b_no_trace_seed42, codellama13b_vota_seed42。回应 R2-N2 scope concern:
    4 models × 3 families × 2 scales。'
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9983
    n: 1190
    errors: 2
- id: plan_014
  claim: 3
  description: 'Multi-seed expansion: loop_only + ae_only + label_only 各 3 seeds。
    回应 R2-N3 single-seed concern，验证 Tier 层级划分稳定性。'
  priority: P0
  gpu_budget_hours: 12
  deps:
  - plan_003
  registry_id: ae_only_seed123
  notes: 'ae_only 3-seed done (mean 99.64%). label_only 3-seed done (mean 86.39%).
    loop_only: seed42 done, seed123 RUNNING, seed456 queued。Registry IDs: ae_only_seed123/456,
    label_only_seed123/456, loop_only_seed123/456。'
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9908
    n: 1190
    pass_recall: 0.987
    fail_recall: 1
    majority_baseline: 0.7151
    lift: 0.2757
- id: plan_015
  claim: 1
  description: 'Format marker removal control: 移除 [No exception data in trace] 格式标记后重训
    exception_only × 3 seeds。回应 R1-N1 format shortcut concern。'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  registry_id: exception_only_nomarker_seed42
  notes: '计划中。如果移除标记后 SFT 仍 ≥99%，证明模型学到的是异常语义而非格式 shortcut。 Registry IDs: exception_only_nomarker_seed42/123/456。'
  status: RUNNING


## registry (completed experiments)

- exp_id: no_trace_seed42
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: vota_seed42
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: no_trace_seed42_v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: vota_seed42_v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: no_trace_seed42_v3
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    train_loss: 0.18
    eval_loss: 0.645
    eval_mean_token_accuracy: 0.89
    accuracy: 0.7513
    majority_baseline: 0.7151
    lift: 0.0361
    pass_precision: 0.8776
    pass_recall: 0.7579
    pass_f1: 0.8134
    fail_precision: 0.5473
    fail_recall: 0.7345
    fail_f1: 0.6272
- exp_id: vota_seed42_v3
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    train_loss: 0.046
    eval_loss: 0.085
    eval_mean_token_accuracy: 0.983
    accuracy: 0.992
    majority_baseline: 0.7151
    lift: 0.276
    pass_precision: 0.99
    pass_recall: 0.99
    pass_f1: 0.99
    fail_precision: 0.99
    fail_recall: 0.99
    fail_f1: 0.99
- exp_id: full_trace_seed42
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    train_loss: 0.037
    eval_loss: 0.084
    eval_mean_token_accuracy: 0.984
    accuracy: 0.284
    majority_baseline: 0.7151
    lift: -0.431
    pass_precision: 0.88
    pass_recall: 0.08
    pass_f1: 0.16
    fail_precision: 0.31
    fail_recall: 0.97
    fail_f1: 0.57
- exp_id: no_trace_seed42_v4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.7513
    majority_baseline: 0.7151
    lift: 0.0361
    pass_precision: 0.8776
    pass_recall: 0.7579
    pass_f1: 0.8134
    fail_precision: 0.5473
    fail_recall: 0.7345
    fail_f1: 0.6272
    train_loss: 0.18
    eval_loss: 0.6454
    eval_mean_token_accuracy: 0.8897
- exp_id: vota_seed42_v4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9563
    majority_baseline: 0.7151
    lift: 0.2412
    n: 1190
    pass_precision: 0.944
    pass_recall: 0.998
    pass_f1: 0.97
    fail_precision: 0.993
    fail_recall: 0.853
    fail_f1: 0.917
    lift_vs_notrace: 0.205
    lift_vs_notrace_ci_lower: 0.177
    lift_vs_notrace_ci_upper: 0.234
    train_loss: 0.046
    eval_loss: 0.0842
- exp_id: full_trace_seed42_v2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 0.284
    majority_baseline: 0.7151
    lift: -0.4311
    n: 1190
    pass_precision: 0.923
    pass_recall: 0.085
    pass_f1: 0.155
    fail_precision: 0.445
    fail_recall: 0.785
    fail_f1: 0.568
    train_loss: 0.0373
    eval_loss: 0.082
    eval_mean_token_accuracy: 0.984
- exp_id: full_trace_seed42_v5
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.8176
    majority_baseline: 0.7151
    lift: 0.1025
    n: 1190
    pass_precision: 0.8774
    pass_recall: 0.866
    pass_f1: 0.8717
    fail_precision: 0.6743
    fail_recall: 0.6962
    fail_f1: 0.6851
    accuracy_ci_lower: 0.797
    accuracy_ci_upper: 0.839
    lift_vs_notrace: 0.0664
    lift_vs_notrace_ci_lower: 0.0437
    lift_vs_notrace_ci_upper: 0.0899
    train_loss: 0.05
    eval_loss: 0.0867
    wall_clock_seconds: 7852
    epoch_level:
      epoch1_accuracy: 0.8303
      epoch2_accuracy: 0.763
      final_accuracy: 0.8176
      trend: non_monotonic_epoch1_best_epoch2_collapse
- exp_id: vota_seed42_v5
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9941
    majority_baseline: 0.7151
    lift: 0.279
    n: 1190
    pass_precision: 1
    pass_recall: 0.9882
    pass_f1: 0.9941
    fail_precision: 0.9714
    fail_recall: 1
    fail_f1: 0.9855
    lift_vs_notrace: 0.2428
    lift_vs_notrace_ci_lower: 0.2185
    lift_vs_notrace_ci_upper: 0.2681
    accuracy_ci_lower: 0.9882
    accuracy_ci_upper: 0.9983
    train_loss: 0.05
    eval_loss: 0.0867
    eval_mean_token_accuracy: 0.9828
    wall_clock_seconds: 8443
    epoch_level:
      epoch1_accuracy: 0.9933
      epoch2_accuracy: 0.9941
      final_accuracy: 0.9941
      trend: monotonic_increasing_then_stable
- exp_id: no_trace_seed42_v5
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.7513
    accuracy_ci_lower: 0.7277
    accuracy_ci_upper: 0.7748
    majority_baseline: 0.7151
    lift: 0.0361
    lift_ci_lower: 0.0042
    lift_ci_upper: 0.0706
    n: 1190
    pass_precision: 0.8776
    pass_recall: 0.7579
    pass_f1: 0.8134
    fail_precision: 0.5473
    fail_recall: 0.7345
    fail_f1: 0.6272
    epoch_level:
      epoch1_accuracy: 0.7429
      epoch2_accuracy: 0.763
      final_accuracy: 0.7513
      trend: non_monotonic_epoch2_best
- exp_id: full_trace_label_only_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.8622
    accuracy_ci_lower: 0.8437
    accuracy_ci_upper: 0.8807
    majority_baseline: 0.7151
    lift: 0.1471
    n: 1190
    pass_precision: 0.8821
    pass_recall: 0.9318
    pass_f1: 0.9063
    fail_precision: 0.8007
    fail_recall: 0.6873
    fail_f1: 0.7397
    train_loss: 0.2505
    eval_loss: 0.3205
    lift_vs_notrace: 0.1109
    lift_vs_notrace_ci_lower: 0.0849
    lift_vs_notrace_ci_upper: 0.137
    lift_vs_standard_fulltrace: 0.0445
    lift_vs_standard_fulltrace_ci_lower: 0.0235
    lift_vs_standard_fulltrace_ci_upper: 0.0655
    lift_vs_standard_fulltrace_pvalue: 0
- exp_id: vota_no_ae_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.994
    majority_baseline: 0.7151
    lift: 0.279
    n: 1190
    pass_f1: 0.996
    fail_f1: 0.989
    accuracy_ci_lower: 0.989
    accuracy_ci_upper: 0.998
    lift_vs_notrace: 0.243
    lift_vs_notrace_ci_lower: 0.218
    lift_vs_notrace_ci_upper: 0.268
    train_loss: 0.0908
    eval_loss: 0.2215
    wall_clock_seconds: 6397.88
- exp_id: vota_ae_only_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9992
    accuracy_ci:
    - 0.9975
    - 1
    bootstrap_pairwise:
      ae_only_vs_no_trace:
        diff: 0.2479
        ci:
        - 0.2235
        - 0.2731
        p_value: 0
        significant: true
      ae_only_vs_exception_only:
        diff: 0.0008
        ci:
        - -0.0017
        - 0.0034
        p_value: 0.8002
        significant: false
      ae_only_vs_vota:
        diff: 0.005
        ci:
        - 0.0017
        - 0.0092
        p_value: 0.0046
        significant: true
    config:
      n_bootstrap: 10000
      seed: 42
      method: paired_bootstrap
- exp_id: vota_exception_only_seed42
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: vota_loop_only_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.8563
    majority_baseline: 0.7151
    lift: 0.1412
    n: 1190
    pass_precision: 0.9239
    pass_recall: 0.8707
    pass_f1: 0.8966
    fail_precision: 0.7165
    fail_recall: 0.8201
    fail_f1: 0.7648
    accuracy_ci:
    - 0.8353
    - 0.8756
    bootstrap_vs_no_trace:
      diff: 0.105
      ci:
      - 0.0824
      - 0.1286
      significant: true
    bootstrap_vs_vota:
      diff: -0.1378
      ci:
      - -0.1571
      - -0.1185
      significant: true
    bootstrap_vs_full_trace:
      diff: 0.0387
      ci:
      - 0.0185
      - 0.0597
      significant: true
    train_loss: 0.0718
    wall_clock_seconds: 7425.65
- exp_id: vota_exception_only_seed42_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9983
    majority_baseline: 0.7151
    lift: 0.2832
    n: 1190
    pass_precision: 1
    pass_recall: 0.998
    pass_f1: 0.999
    fail_precision: 0.994
    fail_recall: 1
    fail_f1: 0.997
    lift_vs_notrace: 0.2471
    lift_vs_notrace_ci_lower: 0.2227
    lift_vs_notrace_ci_upper: 0.2714
    lift_vs_fulltrace: 0.1807
    lift_vs_fulltrace_ci_lower: 0.1588
    lift_vs_fulltrace_ci_upper: 0.2034
    lift_vs_vota: 0.0067
    lift_vs_vota_ci_lower: 0.0017
    lift_vs_vota_ci_upper: 0.0126
    lift_vs_vota_pvalue: 0.01
- exp_id: deepseek_vota_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.8445
    majority_baseline: 0.7151
    lift: 0.1294
    accuracy_ci:
    - 0.826
    - 0.864
    pass_precision: 0.821
    pass_recall: 1
    pass_f1: 0.902
    fail_precision: 1
    fail_recall: 0.454
    fail_f1: 0.625
    eval_loss_epoch1: 0.0679
    eval_loss_epoch2: 0.095
    eval_loss_epoch3: 0.1121
    final_train_loss: 0.0522
    epoch1_checkpoint_eval:
      accuracy: 0.7815
      accuracy_ci:
      - 0.76
      - 0.803
      fail_recall: 0.233
      fail_precision: 1
      pass_recall: 1
      pass_precision: 0.766
      fail_f1: 0.378
      pass_f1: 0.867
      conclusion: epoch3_final_is_better
    reeval_with_fixed_script:
      accuracy: 0.16
      accuracy_ci:
      - 0.139
      - 0.18
      fail_f1: 0.61
      fail_precision: 0.9
      fail_recall: 0.47
      pass_f1: 0.07
      pass_precision: 1
      pass_recall: 0.04
      note: 'CATASTROPHIC: re-eval with corrected evaluate.py shows 16% (vs original
        84.45%). Model predicts fail for almost everything. Previous 84.45% may have
        been from buggy eval. NEEDS INVESTIGATION.'
    group_analysis:
      train_truncated:
        n: 1091
        accuracy: 0.8304
        ci_95:
        - 0.8075
        - 0.8524
        correct: 906
        incorrect: 185
        pass_accuracy: 1
        pass_n: 822
        fail_accuracy: 0.3123
        fail_n: 269
      train_intact:
        n: 99
        accuracy: 1
        ci_95:
        - 1
        - 1
        correct: 99
        incorrect: 0
        pass_accuracy: 1
        pass_n: 29
        fail_accuracy: 1
        fail_n: 70
      fisher_exact:
        odds_ratio: 0
        p_value: 0
      overall_accuracy: 0.8445
      max_length: 2048
      note: 'Grouped by whether training sample content exceeded token budget (DeepSeek
        tokenizer, max_length=2048). Inference used full-length input (no truncation).
        All 185 errors from truncated group''s fail class (fail_recall=31.2%). Intact
        group: 100% accuracy.'
- exp_id: deepseek_no_trace_seed42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 0.7336
    majority_baseline: 0.7151
    lift: 0.0185
    n: 1190
    pass_precision: 0.817
    pass_recall: 0.808
    pass_f1: 0.813
    fail_precision: 0.532
    fail_recall: 0.546
    fail_f1: 0.539
    accuracy_ci:
    - 0.708
    - 0.757
    lift_ci:
    - -0.009
    - 0.046
- exp_id: deepseek_full_trace_seed42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy_no_truncation: 0.2849
    accuracy_with_truncation_fix: 0.1059
    accuracy_with_truncation_fix_ci:
    - 0.089
    - 0.123
    majority_baseline: 0.7151
    n: 1190
    note: 'Both evals show model failure. No-truncation: all predict fail. With-truncation:
      garbage tokens. LoRA training itself failed due to label truncation during training.'
- exp_id: deepseek_exception_only_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9933
    majority_baseline: 0.7151
    lift: 0.2782
    n: 1190
    pass_precision: 1
    pass_recall: 0.9906
    pass_f1: 0.9953
    fail_precision: 0.9769
    fail_recall: 1
    fail_f1: 0.9883
    epoch1_checkpoint_eval:
      accuracy: 0.9983
      fail_recall: 1
      fail_precision: 0.9941
      pass_recall: 0.9976
      conclusion: epoch1_better_by_0.50pp
- exp_id: calibration_analysis_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    no_trace:
      ece: 0.171476
      mce: 0.475643
      brier_score: 0.197152
      accuracy: 0.751261
      n_samples: 1190
    full_trace:
      ece: 0.095817
      mce: 0.249061
      brier_score: 0.143924
      accuracy: 0.817647
      n_samples: 1190
    label_only:
      ece: 0.110686
      mce: 0.417124
      brier_score: 0.120144
      accuracy: 0.862185
      n_samples: 1190
    loop_only:
      ece: 0.083085
      mce: 0.183406
      brier_score: 0.118335
      accuracy: 0.856303
      n_samples: 1190
    ae_only:
      ece: 0.000415
      mce: 0.000415
      brier_score: 0.000847
      accuracy: 0.99916
      n_samples: 1190
    exception_only:
      ece: 0.002717
      mce: 0.835484
      brier_score: 0.001311
      accuracy: 0.998319
      n_samples: 1190
    vota:
      ece: 0.00541
      mce: 0.622459
      brier_score: 0.005234
      accuracy: 0.994118
      n_samples: 1190
- exp_id: vota_seed123
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: vota_seed456
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exception_only_seed123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9983
    accuracy_ci:
    - 0.9958
    - 1
    majority_baseline: 0.7151
    lift: 0.2832
    n: 1190
    pass_precision: 1
    pass_recall: 0.9976
    pass_f1: 0.9988
    fail_precision: 0.9941
    fail_recall: 1
    fail_f1: 0.9971
    train_loss: 0.1096
    train_runtime_sec: 7507
    epochs: 3
    seed_comparison:
      seed42_accuracy: 0.9983
      seed456_accuracy: 0.9983
      seed123_accuracy: 0.9983
      max_diff: 0
      note: identical accuracy to 4 decimal places across all 3 seeds (42/456/123);
        each has exactly 2/1190 errors; exception_only fully seed-robust
- exp_id: exception_only_seed456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9983
    accuracy_ci:
    - 0.9958
    - 1
    majority_baseline: 0.7151
    lift: 0.2832
    n: 1190
    pass_precision: 1
    pass_recall: 0.9976
    pass_f1: 0.9988
    fail_precision: 0.9941
    fail_recall: 1
    fail_f1: 0.9971
    vs_seed42:
      seed42_accuracy: 0.9983
      seed456_accuracy: 0.9983
      diff: 0
      note: identical accuracy to 4 decimal places; no predictions.jsonl for paired
        bootstrap
    train_loss: 0.1087
    eval_loss: 0.4629
    train_runtime_sec: 4541
    epochs: 3
- exp_id: deepseek_exception_only_seed123
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 0.9109
    pass_precision: 1
    pass_recall: 0.993
    pass_f1: 0.996
    fail_precision: 0.976
    fail_recall: 0.705
    fail_f1: 0.818
    ci_95:
    - 0.894
    - 0.926
    train_loss: 0.122
    train_runtime_sec: 6384
- exp_id: deepseek_full_trace_seed42_v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: vota_seed456_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9908
    pass_precision: 1
    pass_recall: 0.987
    pass_f1: 0.993
    fail_precision: 0.969
    fail_recall: 1
    fail_f1: 0.984
    ci_95:
    - 0.985
    - 0.996
- exp_id: deepseek_full_trace_seed42_v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.7916
    majority_baseline: 0.7151
    lift: 0.0765
    n: 1190
    pass_precision: 0.857
    pass_recall: 0.851
    pass_f1: 0.854
    fail_precision: 0.632
    fail_recall: 0.643
    fail_f1: 0.637
    accuracy_ci:
    - 0.768
    - 0.813
    train_loss: 0.0547
    train_runtime_seconds: 8891
    epochs: 3
    reeval_discrepancy:
      reeval_accuracy: 0.285
      reeval_note: 'RESOLVED: 28.5% was caused by eval max_length=16384 (OOD). Re-eval
        with max_length=2048 reproduces 79.16%. predictions.jsonl updated to maxlen2048
        results.'
      status: RESOLVED
- exp_id: deepseek_exception_only_seed456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9933
    majority_baseline: 0.7151
    lift: 0.2782
    n: 1190
    pass_precision: 1
    pass_recall: 0.9906
    pass_f1: 0.9953
    fail_precision: 0.9769
    fail_recall: 1
    fail_f1: 0.9883
    accuracy_ci:
    - 0.9882
    - 0.9975
    train_loss: 0.1225
    eval_loss: 0.4824
    train_runtime_sec: 6246
    seed_comparison:
      seed42_accuracy: 0.9933
      seed456_accuracy: 0.9933
      seed123_accuracy: 0.9109
      note: seed42 and seed456 identical (99.33%); seed123 outlier (91.09%). 2/3 seeds
        robust.
    epoch1_checkpoint_eval:
      accuracy: 0.993
      accuracy_ci:
      - 0.988
      - 0.997
      fail_f1: 0.99
      fail_precision: 0.98
      fail_recall: 1
      pass_f1: 1
      pass_precision: 1
      pass_recall: 0.99
      conclusion: epoch1 (99.3%) ≈ epoch3 (99.33%), 1 epoch convergence confirmed
- exp_id: full_trace_256tok_seed42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 0.7882
    majority_baseline: 0.7151
    lift: 0.0731
    n: 1190
    pass_precision: 0.903
    pass_recall: 0.788
    pass_f1: 0.842
    fail_precision: 0.597
    fail_recall: 0.788
    fail_f1: 0.679
    accuracy_ci:
    - 0.764
    - 0.81
    train_loss: 0.1094
    train_runtime_sec: 3047
    epochs: 3
- exp_id: full_trace_512tok_seed42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 0.8042
    majority_baseline: 0.7151
    lift: 0.0891
    pass_precision: 0.8705
    pass_recall: 0.8531
    pass_f1: 0.8617
    fail_precision: 0.6489
    fail_recall: 0.6814
    fail_f1: 0.6647
    n: 1190
    accuracy_ci:
    - 0.7815
    - 0.8261
- exp_id: full_trace_1024tok_seed42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 0.7723
    majority_baseline: 0.7151
    lift: 0.0571
    n: 1190
    accuracy_ci:
    - 0.7487
    - 0.7958
    pass_precision: 0.9006
    pass_recall: 0.7662
    pass_f1: 0.8279
    fail_precision: 0.573
    fail_recall: 0.7876
    fail_f1: 0.6634
    train_loss: 0.0634
    train_runtime_sec: 5553
    epochs: 3
- exp_id: full_trace_2048tok_seed42
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: debugbench_exception_bug_fix
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: debugbench_exception_only_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 1
    majority_baseline: 0.5141
    lift: 0.4859
    n: 426
    pass_precision: 1
    pass_recall: 1
    pass_f1: 1
    fail_precision: 1
    fail_recall: 1
    fail_f1: 1
    accuracy_ci_wilson:
    - 0.9914
    - 1
    accuracy_ci_bootstrap:
    - 1
    - 1
    train_loss: 0.2435
    eval_loss: 0.4157
    train_runtime_sec: 837
- exp_id: debugbench_no_trace_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9671
    majority_baseline: 0.5141
    lift: 0.4531
    pass_precision: 1
    pass_recall: 0.936
    pass_f1: 0.967
    fail_precision: 0.937
    fail_recall: 1
    fail_f1: 0.967
    accuracy_ci:
    - 0.948
    - 0.984
    train_loss: 0.249
    eval_loss: 0.532
- exp_id: debugbench_vota_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9977
    majority_baseline: 0.5141
    lift: 0.4836
    n: 426
    pass_precision: 1
    pass_recall: 1
    pass_f1: 1
    fail_precision: 1
    fail_recall: 1
    fail_f1: 1
    accuracy_ci:
    - 0.993
    - 1
    train_loss: 0.098
    eval_loss: 0.1179
    eval_mean_token_accuracy: 0.9737
    errors: 1
- exp_id: eval_missing_predictions_batch
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: eval_missing_predictions_batch_v2
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: ae_only_seed123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9908
    n: 1190
    pass_recall: 0.987
    fail_recall: 1
    majority_baseline: 0.7151
    lift: 0.2757
- exp_id: ae_only_seed456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9992
    n: 1190
    majority_baseline: 0.7151
    lift: 0.2841
    seed_comparison:
      seed42_accuracy: 0.9992
      seed123_accuracy: 0.9908
      seed456_accuracy: 0.9992
      mean_accuracy: 0.9964
      std: 0.0049
      note: 2/3 seeds = 99.92%, seed123 = 99.08%. Mean = 99.64% ± 0.49
- exp_id: regex_baseline_analysis
  name: ''
  status: DONE
  conclusion: success
  metrics:
    regex_B1_ERROR_presence: 0.9345
    regex_B2_Traceback: 0.7151
    regex_B3_any_keyword: 0.9345
    regex_B4_exception_type: 0.9361
    regex_B5_format_marker: 0.9933
    regex_B6_error_count_ge2: 0.9202
    sft_exception_only: 0.9983
    best_regex_gap_vs_sft: -0.0622
    B5_mcnemar_p: 0.041
    n: 1190
- exp_id: label_only_seed123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.8706
    n: 1190
    pass_recall: 0.974
    fail_recall: 0.611
    pass_f1: 0.915
    fail_f1: 0.729
- exp_id: label_only_seed456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.859
    n: 1190
    pass_recall: 0.938
    fail_recall: 0.661
    pass_f1: 0.905
    fail_f1: 0.727
- exp_id: exception_only_nomarker_seed42
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: loop_only_seed123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.8588
    majority_baseline: 0.7151
    lift: 0.1437
    n: 1190
    pass_precision: 0.9129
    pass_recall: 0.8872
    pass_f1: 0.8999
    fail_precision: 0.7355
    fail_recall: 0.7876
    fail_f1: 0.7607
    accuracy_ci:
    - 0.8403
    - 0.8773
- exp_id: loop_only_seed456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.8664
    n: 1190
    pass_precision: 0.9179
    pass_recall: 0.8931
    pass_f1: 0.9053
    fail_precision: 0.7486
    fail_recall: 0.7994
    fail_f1: 0.7732
    accuracy_ci:
    - 0.847
    - 0.884
- exp_id: exception_only_nomarker_seed123
  name: ''
  status: QUEUED
  conclusion: ''
  metrics: {}
- exp_id: exception_only_nomarker_seed456
  name: ''
  status: QUEUED
  conclusion: ''
  metrics: {}
- exp_id: qwen1.5b_exception_only_seed42
  name: ''
  status: QUEUED
  conclusion: killed
  metrics: {}
- exp_id: qwen1.5b_no_trace_seed42
  name: ''
  status: QUEUED
  conclusion: killed
  metrics: {}
- exp_id: qwen1.5b_vota_seed42
  name: ''
  status: QUEUED
  conclusion: killed
  metrics: {}
- exp_id: qwen1.5b_full_trace_seed42
  name: ''
  status: QUEUED
  conclusion: killed
  metrics: {}
- exp_id: codellama_exception_only_seed42
  name: ''
  status: QUEUED
  conclusion: killed
  metrics: {}
- exp_id: codellama_no_trace_seed42
  name: ''
  status: QUEUED
  conclusion: killed
  metrics: {}
- exp_id: codellama_vota_seed42
  name: ''
  status: QUEUED
  conclusion: killed
  metrics: {}
- exp_id: codellama13b_exception_only_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9983
    n: 1190
    errors: 2
- exp_id: codellama13b_no_trace_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.765
    n: 1190
    majority_baseline: 0.7151
    lift: 0.05
    pass_precision: 0.84
    pass_recall: 0.83
    pass_f1: 0.84
    fail_precision: 0.59
    fail_recall: 0.59
    fail_f1: 0.59
    accuracy_ci:
    - 0.738
    - 0.787
- exp_id: codellama13b_vota_seed42
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: qwen15b_no_trace_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.6731
    n: 1190
    pass_f1: 0.7527
    fail_f1: 0.518
    lift_over_majority: -0.042
    training_time_sec: 851
- exp_id: qwen15b_vota_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9958
    n: 1190
    pass_recall: 0.9976
    fail_recall: 0.9912
    pass_f1: 0.9971
    fail_f1: 0.9926
    training_time_sec: 2922
- exp_id: qwen15b_full_trace_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.7706
    n: 1190
- exp_id: qwen15b_exception_only_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9983
    accuracy_ci_lower: 0.9958
    accuracy_ci_upper: 1
    majority_baseline: 0.7151
    lift: 0.283
    n: 1190
    pass_precision: 1
    pass_recall: 0.9976
    pass_f1: 0.9988
    fail_precision: 0.9941
    fail_recall: 1
    fail_f1: 0.9971
    train_loss: 0.1347
    eval_loss: 0.5761
    wall_clock_seconds: 1762

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
  "promptId": "dbe07f50-5d0c-466c-835e-8d41f6ef3dce",
  "type": "user",
  "uuid": "b92bf088-4a83-4407-a5fa-f5c40fe741b8",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4",
  "sessionId": "1723cae9-4a61-47ee-b162-e2fd329daf4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T16:08:52.780Z_

```json
{
  "parentUuid": "b92bf088-4a83-4407-a5fa-f5c40fe741b8",
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
  "uuid": "e3220e4a-cea7-46f9-80e6-875794028971",
  "timestamp": "2026-05-16T16:08:52.780Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4",
  "sessionId": "1723cae9-4a61-47ee-b162-e2fd329daf4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T16:08:52.780Z_

```json
{
  "parentUuid": "e3220e4a-cea7-46f9-80e6-875794028971",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "408b8975-ea02-4457-81f6-ac0eb05c3f1e",
  "timestamp": "2026-05-16T16:08:52.780Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4",
  "sessionId": "1723cae9-4a61-47ee-b162-e2fd329daf4b",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：nomarker 实验显著退化，暴露格式标记是主要机制；原始 'fault semantics' 叙事不成立，需要 reframe 核心假设：['nomarker 实验 <90%（或 3-seed 高方差，worst seed <85%）：移除格式标记后大幅退化，证明模型主要依赖 format patter…",
  "leafUuid": "408b8975-ea02-4457-81f6-ac0eb05c3f1e",
  "sessionId": "1723cae9-4a61-47ee-b162-e2fd329daf4b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe exception signal dominance as format shortcut learning",
  "sessionId": "1723cae9-4a61-47ee-b162-e2fd329daf4b"
}
```

---

### Assistant

_source line 8 · 2026-05-16T16:12:18.174Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment data for the "worst" tier across all planned experiments in the experiment_plan. Let me carefully analyze each experiment in the context of the "worst" tier definition:

**Worst tier definition:**
- nomarker experiment significantly degrades, exposing format markers as the main mechanism
- Original 'fault semantics' narrative doesn't hold, needs reframing
- Key metric ranges:
  - nomarker_accuracy_3seed_mean: [0.85, 0.949]
  - nomarker_accuracy_worst_seed: [0.8, 0.93]
  - codellama13b_vota_accuracy: [0.99, 1.0]
  - cross_family_exception_dominance_pp: [-5.0, 0.0]
  - format_marker_contribution_pp: [5.0, 15.0]

The narrative direction: Original 'fault semantics' framing doesn't hold. Reframe as **trace formatting as implicit task specification**. The contribution becomes revealing the outsized impact of format/structure choices on downstream classification in SFT.

Now I'm going through the experiment_plan to identify which experiments have "planned" or "RUNNING" status and need worst-tier data generation.

Plan_015 is the critical one—format marker removal control with three seeds across exception_only_nomarker variants. Plan_013 has codellama13b with exception_only and no_trace finished, but the vota variant is still running. Plan_012 with qwen15b is complete, and plan_014's multi-seed expansion is mostly done except for the loop_only seeds. Most of these experiments are already finished, so I need to focus on generating worst-tier predictions for the ones still in progress. I need to step back and think about what the user is actually asking for. They want detailed data for each planned experiment, which means I should compile results for all experiments in the plan—using actual data where experiments are done, and generating predicted results for the ones still running. The worst-tier scenario hinges on how the remaining experiments (the nomarker variants and codellama vota) turn out, so I need to imagine plausible results for those while keeping everything consistent with the overall narrative. I'm working out the specific performance numbers for the worst-case scenario—if nomarker experiments show around 90% accuracy with individual seeds ranging from 88% to 92%, that puts format markers at roughly a 9-10 percentage point contribution, which fits the predicted range. For codellama13b_vota, I'm estimating performance in the 0.99-1.0 range given its strong baseline.

The key insight is that removing format markers forces the model to rely solely on raw exception content, and since it learned to treat `[No exception data in trace]` as a dominant pass signal during training, losing that structured cue causes a sharp drop in pass classification—the model can still detect exceptions in failing samples, but without the explicit marker it struggles to confidently identify passing cases.

CodeLlama-13B's larger capacity means VOTA performs comparably to exception_only, which suggests the narrative that exception content alone drives performance doesn't hold across all model sizes.

Now I'm organizing the full experimental plan, listing out which experiments are already completed with known results and which ones I need to predict outcomes for based on the worst-tier hypothesis. Looking at the remaining experiments, I need to compile predictions for the incomplete runs. Plan_013 still has the vota variant running for CodeLlama-13B, and plan_015 needs predictions across all three seeds for the nomarker configuration. I'll structure the full output with actual results where available and reasonable predictions for the pending experiments, keeping the focus on what's still unknown. Now I'm checking the format marker contribution against the expected range and verifying it falls within 5-15 percentage points. For the CodeLlama model with VOTA, I'm seeing 99.58% accuracy, which is essentially equivalent to the exception-only baseline at 99.83%, meaning the cross-family exception dominance metric lands between -5 and 0 percentage points—indicating exception conditions don't clearly outperform other approaches on this larger model. So VOTA ≥ exception_only on CodeLlama. This would mean:
- codellama13b_exception_only = 99.83%
- codellama13b_vota ≈ 99.83% to 100% (VOTA matches or beats exception)

This undermines the "exception dominates" narrative because on a larger/different model, VOTA is at least as good.

So codellama13b_vota = ~99.92% (VOTA actually slightly better than exception_only's 99.83%)

This gives cross_family_exception_dominance_pp = 99.83 - 99.92 = -0.09pp, which is in [-5, 0].

Now I'm organizing the completed and in-progress experiments by plan ID to see how each fits the worst tier framing. For the done experiments, I need to explain their actual results, and for the running or queued ones, I'll make predictions. Plan 001 achieved 99.41% accuracy—this high performance stems partly from format markers being preserved, so removing ae doesn't significantly impact it since the [No exception data in trace] marker dominates the signal. Plan 002 with label-only reached 86.22%—the improvement comes from concentrating gradients on the verdict token, but the full trace still has format markers buried in noise. Plan 003's component ablation shows that exception_only's 99.83% success is substantially driven by the format marker [No exception data in trace] acting as a pass/fail shortcut.

For plan 004, DeepSeek's exception_only also benefits from format markers at 99.33% across most seeds, though the seed123 outlier at 91.09% might actually reflect closer-to-true exception content learning. Plan 005 on DebugBench hit 100%, but the ceiling is too high to be discriminative about format patterns. Plan 006's trace length ablation shows longer traces don't help because the model relies on format markers rather than additional trace content. Plan 007's calibration results reflect the model's confidence in format marker matching rather than semantic understanding. Plan 008 on seed robustness shows perfect consistency on Qwen at 99.83%, which again points to format marker reliance rather than robust learning.

Plan 012 with Qwen-1.5B achieves the same 99.83% as the 7B model, suggesting a trivial pattern—if this were genuine semantic understanding, the smaller model should degrade. Plan 013 on CodeLlama-13B shows exception_only at 99.83% with no_trace dropping to 76.5%, indicating exception dominance is model-specific. Plan 014's multi-seed results remain stable across all ablations, further reinforcing that the pattern is consistent and likely format-driven rather than semantic.

Plan 015 with nomarker is the critical test—removing the explicit `[No exception data in trace]` marker from passing samples should cause significant degradation if the model relies on it. I'm predicting nomarker_seed42 will drop to around 92.10%, since passing samples become minimal without the marker while failing samples retain their exception content, reducing the asymmetry the model exploits. Now I need to write out the YAML configuration with all these experiments, including the MVP variants. Looking at CodeLlama-13B with VOTA, the larger model should leverage all the components effectively, so I'm setting it to 99.92% to match the ae_only performance level on Qwen, which puts the exception dominance at -0.09pp and respects the constraint that VOTA should exceed exception_only performance. > breaks down on larger models

This is consistent with the worst tier narrative: the exception dominance finding is fragile and model-dependent.

Now I need to construct the full YAML with all planned experiments. For the completed ones, I'll use the actual metrics but frame them through the worst-tier lens, and for the remaining experiments I'll predict values that align with this interpretation. Each entry needs a clear rationale explaining how it supports the worst-tier narrative.

Generating YAML structure...

The regex baseline comparison is particularly striking here—when the format marker is removed, the SFT model drops to around 90% while the simple regex checking for the format string hits 99.33%, which means the regex actually outperforms the nomarker SFT. This is the smoking gun for the format shortcut hypothesis, showing that the model's performance collapses without that superficial cue.

Now I'm organizing the experimental results by plan ID and finalizing the predictions for the YAML output. I'm reconsidering what the nomarker setup actually removes—specifically the `[No exception data in trace]` marker that appears in pass samples. Without it, pass samples would be essentially empty or minimal, while fail samples still retain their exception information, just potentially without the `[ERROR]` prefix formatting. This explains the significant performance drop on pass samples when the marker is removed. Looking at the B5 regex baseline that achieves 99.33%, it's detecting the presence or absence of the `[No exception data in trace]` marker—pass samples have it, fail samples don't. The nomarker experiment strips this away, leaving pass samples empty or nearly empty while fail samples retain their exception content. Without the explicit marker, the model has to rely on the cruder signal of content presence versus absence, and in the worst tier this breaks down because some edge cases like GeneratorExit might still contain trace data, making the distinction less reliable.

Since I need to estimate within the given ranges, I'm settling on middle-ground values: around 90% for the mean accuracy and 87% for the worst seed, which would put the format marker's contribution at roughly 10 percentage points. All the metrics check out within their ranges. Now I need to write out the YAML with all the experiment data—I should make sure to cover every planned experiment from the list, going through each one systematically.

I've got 15 experiments total to document. For the ones that are complete, I'll pull the actual metrics and frame them with the worst-tier interpretation. For the ones still running or queued, I'll provide reasonable predictions based on the patterns I'm seeing.

Let me structure each entry concisely in the YAML format, making sure the narrative guidance and expected results align with the worst-case framing. Looking at the nomarker experiment more carefully, it seems to remove the format markers entirely from both pass and fail samples—stripping out `[No exception data in trace]` from passes and `[ERROR]` prefixes from fails, leaving only the raw content. This directly tests whether the model was relying on these formatting shortcuts rather than learning the actual classification patterns.

The 85-94.9% performance range shows the model still works reasonably well without them, but the ~10 percentage point drop compared to the baseline proves those markers were contributing meaningfully to the model's decision-making.

Now I'm ready to write out the YAML with specific per-class metrics for the nomarker condition, breaking down pass and fail recall and precision separately to show where the degradation actually happens. I'm working through the dataset composition—roughly 71.5% pass cases and 28.5% fail cases across 1190 samples—to validate whether my precision and recall numbers align with the actual accuracy metrics. Let me recalculate the nomarker_seed42 results by working backwards from the 91.76% accuracy to see if my pass/fail recall estimates are consistent.

Now I'm checking the precision metrics: if I predict 757 samples as pass, 755 are actually correct, giving me a pass precision of about 0.997, while my fail precision comes out to roughly 0.778 when I predict 433 as fail but only 337 are truly fail.

The core issue is clear—most misclassifications are pass samples getting marked as fail, which happens because without that exception marker, the pass cases become hard to distinguish. Let me work through the same calculations for the other seeds to see if this pattern holds consistently.

For seed123, the numbers show pass recall around 82% with 152 pass-to-fail errors, while fail precision drops to 69%. Seed456 follows a similar trajectory with slightly better pass recall at 87% but still 112 pass-to-fail misclassifications and fail precision at 75%. The story across all three seeds is the same: the model is conservative about predicting pass, leading to high fail precision but lower pass recall.

Averaging the accuracies across the three seeds gives 89.63%, which means the format marker alone contributes about 10 percentage points to the exception_only baseline. Now looking at codellama13b_vota, the exception_only variant achieves 99.83% with just 2 errors from that same GeneratorExit issue, while no_trace drops significantly to 76.5%. The vota ensemble predicts 99.92% accuracy, which would be only 1 error out of 1190 samples.

If that single error is a pass sample misclassified as fail like the GeneratorExit cases, the per-class metrics would show pass_recall around 0.9988 with perfect fail_recall, and pass_precision at 1.0 with fail_precision at 0.9971. This distribution makes sense given that a 13B model has sufficient capacity to effectively leverage all the ensemble components. I have enough information now to construct the final YAML output.

I'll structure the format to be concise for completed experiments while being more thorough for ongoing or queued ones. I need to map out which paper tables and figures each experiment supports under the worst-tier framing—the main results table becomes a format dependency analysis, the nomarker ablation becomes the central table, component ablations show format contribution, calibration gets reinterpreted as format versus semantic confidence, and the cross-model summary demonstrates format markers as a universal shortcut. For figures, I'm planning a bar chart comparing exception_only versus nomarker across seeds.

Now I'm writing out the YAML structure with detailed descriptions of which tables and figures each experiment feeds into. For the already-completed experiments, I need to reframe their narratives through the worst-tier lens—like how the Qwen exception_only result at 99.83% across three seeds shows perfect reproducibility of a shortcut behavior, indicating the model consistently converges to the same format dependency regardless of initialization.

The 1.5B Qwen model matching the 7B version exactly is telling evidence that this is format-based rather than semantic—genuine fault understanding would demand more model capacity, whereas a simple format check requires minimal parameters. When CodeLlama-13B replicates the same 99.83% across a completely different family, that's strong confirmation the shortcut is universal across architectures. The regex baseline sitting at 99.33%, just 0.50pp below SFT, shows the model barely beats a simple pattern matcher for the marker string. And when removing the marker drops performance to around 89.6%, that's where the real degradation concentrates—the format dependency is doing most of the heavy lifting.

Looking at the actual breakdown: the gap from no_trace at 75.13% up to nomarker at 89.6% is roughly 14.9pp of genuine content learning, while the format marker itself accounts for about 9.8pp. That 24.7pp total trace contribution splits cleanly into these two components. The loop_only and label_only variants, which lack the strong format signal, sit in the 85-86% range—that's what content-level learning looks like without the shortcut.

The key insight is that format markers drive about 40% of the trace lift, which is substantial. The remaining 60% comes from legitimate exception signals, but here's what matters: that 10pp format contribution is nearly as large as the entire 6.6pp gain from full trace SFT, and the SFT model barely outperforms a simple regex baseline. This framing captures the core worst-tier message—the near-perfect accuracy is significantly inflated by format shortcut learning.

Now I need to write up the YAML and also account for the experiments still running.

Looking at the running and queued experiments, I can see the exception_only variants without markers are in progress. The critical finding from plan_015 is that removing markers causes performance to drop to ~89.5% instead of staying above 99%, which directly refutes the hypothesis that the model learned genuine fault semantics. The model was indeed relying on format shortcuts rather than understanding the underlying exception patterns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "408b8975-ea02-4457-81f6-ac0eb05c3f1e",
  "isSidechain": false,
  "requestId": "req_011Cb6Y8zMeco44Sq17y1rYa",
  "type": "assistant",
  "uuid": "fa9fef4c-f10f-4022-94ce-b8111a504016",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4",
  "sessionId": "1723cae9-4a61-47ee-b162-e2fd329daf4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013RXsxQr3tgQbdcK2ZoEWCk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 34669,
      "cache_read_input_tokens": 11841,
      "output_tokens": 22302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34669,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 22302,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 34669,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34669
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

_source line 9 · 2026-05-16T16:16:01.305Z_

```yaml
tier: worst
narrative_guidance: >
  原始 'fault semantics' 叙事不成立。nomarker 实验暴露 exception_only 99.83% 中约 10pp 来自格式标记
  [No exception data in trace] 的 shortcut 学习。SFT 模型（99.83%）仅比 regex B5（99.33%）高 0.50pp；
  移除标记后 SFT 降至 ~89.6%，反而低于 regex。论文贡献 reframe 为：**trace formatting as implicit task
  specification** —— SFT 中 format/structure choices 对 downstream classification 具有 outsized impact。
  核心 decomposition：总 trace lift 24.7pp = content signal ~14.9pp (60%) + format marker ~9.8pp (40%)。
  format marker 贡献（~10pp）单独即超过 full_trace 全部 lift（6.6pp），揭示 SFT shortcut learning 的严重性。
  Claim 1 重写为 'structured format markers dominate verdict prediction in exception traces'。
  Claim 3 重写为 'format engineering > content richness for SFT verdict tasks'。
  与 shortcut learning 文献（NLI artifacts, annotation artifacts, Gururangan et al. 2018）对话。
  仍冲 EMNLP Main —— angle 从 positive finding 变为 cautionary finding + practical design principle。

imagined_experiments:

  # ============================================================
  # plan_mvp_notrace — MVP baseline (DONE, actual data)
  # ============================================================
  - name: "no_trace baseline"
    plan_id: "plan_mvp_notrace"
    description: "无 trace 基线。模型仅凭 code + test input 预测 verdict。"
    expected_results:
      accuracy: 0.7513
      pass_recall: 0.7579
      fail_recall: 0.7345
      ECE: 0.1715
      Brier: 0.1972
    result_rationale: >
      （实际数据）无 trace 时模型只能依赖代码表面特征和训练集 prior (71.51% pass)。
      75.13% 仅比 majority baseline 高 3.6pp，calibration 严重失调（ECE=0.17）。
      在 worst tier 下，这个数字建立了 content-free 的下界：任何高于此的增益
      都需要 decompose 为 content signal vs. format shortcut。
    tables:
      - "Table 1: Main results — no_trace 行作为 floor"
    figures_description:
      - "Figure 1 bar chart 的最左柱，标注 'code-only baseline'"
    analysis: >
      75.13% 是所有 trace 条件的 anchor。worst tier 的核心论点是：
      exception_only 的 24.7pp lift 中，~40% (10pp) 来自 format marker shortcut，
      ~60% (14.9pp) 来自 content signal。no_trace 确认 content signal 的起点。

  # ============================================================
  # plan_mvp_vota — MVP VOTA (DONE, actual data)
  # ============================================================
  - name: "VOTA baseline"
    plan_id: "plan_mvp_vota"
    description: "VOTA trace SFT MVP。完整 VOTA 表征（loop + exception + ae）。"
    expected_results:
      accuracy: 0.9941
      pass_recall: 0.9882
      fail_recall: 1.0
      ECE: 0.0054
    result_rationale: >
      （实际数据, v5 结果）VOTA 99.41% 包含所有格式标记。在 worst tier 下，
      VOTA 的高 accuracy 部分归因于 [No exception data in trace] 和 [ERROR] 等
      format markers 提供的 shortcut。VOTA 略低于 exception_only (99.83%) 不是因为
      添加信息有害，而是 loop/ae tokens 稀释了 format marker 的注意力聚焦。
    tables:
      - "Table 1: Main results — VOTA 行"
      - "Table 3: Format dependency decomposition"
    figures_description:
      - "Figure 1 bar chart 中间柱"
    analysis: >
      VOTA 99.41% 在 worst tier 下需重新解读：这不是 'trace reasoning' 的证据，
      而是 format marker 被保留后 shortcut 仍然有效的结果。CodeLlama-13B 上
      VOTA=99.92% 甚至优于 exception_only，说明更大模型能更好利用 VOTA 的
      额外 format cues，进一步支持 format engineering > content hypothesis。

  # ============================================================
  # plan_mvp_fulltrace — MVP full trace (DONE, actual data)
  # ============================================================
  - name: "full_trace baseline"
    plan_id: "plan_mvp_fulltrace"
    description: "完整执行 trace SFT。包含所有 trace 行（含格式标记，但被海量 trace tokens 淹没）。"
    expected_results:
      accuracy: 0.8176
      pass_recall: 0.866
      fail_recall: 0.6962
      ECE: 0.0958
    result_rationale: >
      （实际数据, v5 结果）full_trace 81.76% 远低于 exception_only 99.83%。
      full_trace 也包含 [No exception data in trace] 和 [ERROR] 标记，但被
      数千 token 的 trace noise 包围。在 worst tier 下，这证明 format marker
      的有效性取决于 signal-to-noise ratio：marker 存在但被稀释时效果大幅下降。
      gradient dilution (D1) 和 information overload 共同使模型难以从 full trace
      中提取 format shortcut。
    tables:
      - "Table 1: Main results — full_trace 行"
      - "Table 4: Information density vs. format accessibility"
    figures_description:
      - "Figure 1 bar chart — full_trace 柱显著低于 exception_only/VOTA"
    analysis: >
      full_trace 的 81.76% 确认：format markers 需要在 compact 表征中才能被
      有效利用。这与 shortcut learning 文献一致——shortcut 的有效性取决于其
      accessibility（Geirhos et al. 2020）。exception_only 将 marker 置于最
      prominent 位置，最大化 shortcut 的可利用性。

  # ============================================================
  # plan_001 — VOTA no actual/expected (DONE, actual data)
  # ============================================================
  - name: "VOTA minus actual/expected"
    plan_id: "plan_001"
    description: "移除 VOTA 中 actual/expected 值对，保留 exception + loop。验证是否为 trivial string comparison。"
    expected_results:
      accuracy: 0.9941
      pass_f1: 0.996
      fail_f1: 0.989
    result_rationale: >
      （实际数据）99.41% = 完整 VOTA，移除 ae 无影响。在 worst tier 下，
      这不是 'exception content 自身 sufficient' 的证据，而是 format marker
      [No exception data in trace] 独立于 ae 存在——marker 未被移除，shortcut
      仍完整可用。真正的 sufficiency test 是 nomarker 实验。
    tables:
      - "Table 2: Component ablation — vota_no_ae 行"
    figures_description: []
    analysis: >
      vota_no_ae = VOTA 的事实在 worst tier 下有新解读：ae 组件不影响 accuracy
      因为分类不依赖 ae content，而是依赖 format marker。ae 的移除没有碰到
      真正的 active ingredient（format marker），所以没有效果。

  # ============================================================
  # plan_002 — label-only loss (DONE, actual data)
  # ============================================================
  - name: "full_trace label-only loss"
    plan_id: "plan_002"
    description: "full_trace + 仅对 verdict token 计算 loss，mask trace tokens。量化 gradient dilution。"
    expected_results:
      accuracy: 0.8622
      lift_vs_standard_fulltrace: 0.0445
      pass_recall: 0.9318
      fail_recall: 0.6873
    result_rationale: >
      （实际数据）label-only 86.22% 比 standard full_trace 81.76% 高 4.5pp（gradient dilution 贡献），
      但仍远低于 exception_only 99.83%。在 worst tier 下重新解读：
      label-only 修复了 gradient dilution，但 full trace 中 format markers
      仍被海量 tokens 淹没——模型在 2048 tokens 中寻找 [No exception data in trace]
      的效率远低于在 exception_only 的 compact 表征中。86.22% ≈ loop_only 85.63%，
      说明 label-only full_trace 实质上退化为 loop-level 的行为模式学习。
    tables:
      - "Table 1: Main results — label_only 行"
      - "Table 4: Gradient dilution decomposition（26% vs 74%）"
    figures_description:
      - "Figure 2: Waterfall chart — 75.13 → 81.76 (full) → 86.22 (label-only) → 99.83 (exception_only)"
    analysis: >
      label-only 实验在 worst tier 下保留原有解读（gradient dilution = 26%），
      但 74% 的 information overload 部分现在重新理解为：format marker 的
      accessibility bottleneck——不是 trace 内容太多导致模型'迷路'，而是
      shortcut pattern 被噪声稀释导致模型无法高效利用。

  # ============================================================
  # plan_003 — component ablation (DONE, actual data)
  # ============================================================
  - name: "VOTA component ablation (loop/exception/ae)"
    plan_id: "plan_003"
    description: "分别测试 loop_only, exception_only, ae_only。量化每个组件贡献。"
    expected_results:
      exception_only_accuracy: 0.9983
      ae_only_accuracy: 0.9992
      loop_only_accuracy: 0.8563
      vota_full_accuracy: 0.9941
    result_rationale: >
      （实际数据）exception_only 99.83%, ae_only 99.92%, loop_only 85.63%。
      在 worst tier 下，Tier 1 组件（exception + ae）的近完美 accuracy 需重新解读：
      两者都包含强 format markers —— exception_only 有 [No exception data in trace] / [ERROR]，
      ae_only 有 assertion 结果的结构化标记。它们的高 accuracy 不是 'diagnostic moment' 的
      语义价值，而是 format marker 的 shortcut 效应。loop_only 85.63% 没有这些强标记，
      反映的是 content-level 学习的真实水平——这才是 'fault semantics' 的近似上限。
    tables:
      - "Table 2: Component ablation（reframed as format marker analysis）"
      - "Table 5: Format marker presence vs. component accuracy"
    figures_description:
      - "Figure 3: Component accuracy vs. format marker strength scatter plot"
    analysis: >
      worst tier 下 Tier hierarchy 被重新理解为 **format marker strength hierarchy**：
      Tier 1 (exception/ae) 有强 explicit markers → 99%+；
      Tier 2 (loop) 无 explicit markers → 85%；
      format marker contribution ≈ 14pp (99.83 - 85.63)。
      这与 nomarker 实验的 ~10pp drop 量级一致，交叉验证了 format shortcut 假说。
      loop_only ≈ label_only (85.63 vs 86.22) 进一步确认：无 format marker 时，
      不同表征的 content-level 学习效果相似。

  # ============================================================
  # plan_004 — DeepSeek cross-model (DONE, actual data)
  # ============================================================
  - name: "DeepSeek-Coder-6.7B 四条件验证"
    plan_id: "plan_004"
    description: "DeepSeek 上复现 VOTA/no_trace/full_trace/exception_only。跨模型验证 exception dominance。"
    expected_results:
      exception_only_seed42: 0.9933
      exception_only_seed456: 0.9933
      exception_only_seed123: 0.9109
      vota: 0.8445
      no_trace: 0.7336
      full_trace_v3: 0.7916
    result_rationale: >
      （实际数据）DeepSeek exception_only 2/3 seeds=99.33%，1 outlier=91.09%。
      在 worst tier 下：(1) seed42/456=99.33% 与 regex B5=99.33% 完全一致，
      进一步暗示 SFT 学到的就是 regex 级别的 format matching；
      (2) seed123=91.09% 可能更接近 'without format shortcut' 的真实水平——
      该 seed 的 LoRA 初始化恰好未充分学到 format marker → pass 映射
      (fail_recall=0.705 说明 [ERROR] marker 的学习也不完整)；
      (3) VOTA 84.45% 受 truncation 影响，但 format markers 在 VOTA 中
      的位置和 accessibility 不如 exception_only compact。
    tables:
      - "Table 1: Cross-model results"
      - "Table 6: DeepSeek seed analysis — LoRA init vs format learning"
    figures_description:
      - "Figure 4: Cross-model accuracy comparison (grouped bar chart)"
    analysis: >
      DeepSeek 数据在 worst tier 下提供额外证据：seed42/456 精确匹配 regex B5
      (99.33%) 是巧合但 suggestive——两个 seed 的 SFT 模型和一个简单 regex
      达到了完全相同的 accuracy，暗示它们可能在做同一件事。seed123 outlier
      的存在说明 format shortcut 的学习也非 guaranteed——LoRA 初始化不佳时
      模型可能只学到部分 shortcut。

  # ============================================================
  # plan_005 — DebugBench (DONE, actual data)
  # ============================================================
  - name: "DebugBench 跨任务验证"
    plan_id: "plan_005"
    description: "DebugBench subset 上测试 exception_only/VOTA/no_trace。验证泛化性。"
    expected_results:
      exception_only: 1.0
      vota: 0.9977
      no_trace: 0.9671
    result_rationale: >
      （实际数据）DebugBench 上 exception_only=100%, no_trace=96.71%。
      在 worst tier 下：DebugBench 天花板过高（no_trace 已 96.71%），
      trace lift 仅 3.29pp，无法区分 format shortcut vs. content learning。
      100% 的 exception_only 不是 'fault semantics 跨数据集 robust' 的证据，
      而可能只是 DebugBench 的 bug 结构恰好与 format markers 完美对齐。
      此数据集在 worst tier 论文中仅作 secondary generalization validation，
      不承担 mechanism 论证的任何权重。
    tables:
      - "Table 7: DebugBench generalization (secondary evidence)"
    figures_description: []
    analysis: >
      DebugBench 在 worst tier 下的定位不变：泛化性验证，非 mechanism 证据。
      但 worst tier 论文会增加一句 caveat：DebugBench 的近完美 no_trace baseline
      说明 verdict task 的难度 spectrum 很宽，format shortcut 在 easy benchmarks
      上可能被 ceiling 效应掩盖。

  # ============================================================
  # plan_006 — trace length ablation (DONE, actual data)
  # ============================================================
  - name: "trace length ablation (256/512/1024/full)"
    plan_id: "plan_006"
    description: "不同截断长度对 full_trace 准确率的影响。"
    expected_results:
      256tok: 0.7882
      512tok: 0.8042
      1024tok: 0.7723
      full_2048: 0.8176
    result_rationale: >
      （实际数据）256→512→1024→2048 = 78.82→80.42→77.23→81.76%。
      非单调，收益递减，全部远低于 exception_only 99.83%。
      在 worst tier 下：更多 trace tokens 不帮助 accuracy 是因为 format markers
      在 full trace 中被淹没——增加 tokens 不增加 format marker 的 accessibility，
      反而增加 noise。这与 shortcut learning 的 accessibility 理论一致。
      真正有效的不是 trace 内容量，而是 format marker 的相对 prominence。
    tables:
      - "Table 4: Trace length ablation — format accessibility vs. trace volume"
    figures_description:
      - "Figure 5: Trace length vs accuracy curve (flat, all << exception_only)"
    analysis: >
      trace length 数据在 worst tier 下支持 'format accessibility' 论点：
      无论 trace 多长或多短，只要 format marker 不在 compact isolated 位置，
      模型就无法有效利用 shortcut。exception_only 的优势不是 content richness，
      而是 format marker isolation。

  # ============================================================
  # plan_007 — calibration (DONE, actual data)
  # ============================================================
  - name: "Calibration analysis (ECE + Brier)"
    plan_id: "plan_007"
    description: "ECE + reliability diagrams 对比各条件 calibration。"
    expected_results:
      exception_only_ECE: 0.0027
      exception_only_Brier: 0.0013
      no_trace_ECE: 0.1715
      no_trace_Brier: 0.1972
      loop_only_ECE: 0.0831
      full_trace_ECE: 0.0958
    result_rationale: >
      （实际数据）exception_only ECE=0.0027（近完美校准）。
      在 worst tier 下重新解读：极低 ECE 不是 'model understands fault semantics' 的证据，
      而是 format shortcut 提供了几乎 deterministic 的映射——marker 在 → 高置信度 pass，
      marker 不在 → 高置信度 fail。一个完美的 shortcut 自然产生完美的 calibration。
      相比之下，loop_only ECE=0.083 反映的是 content-level 学习的 calibration——
      不完美但非 trivial，这才是 genuine semantic understanding 的 calibration profile。
    tables:
      - "Table 8: Calibration comparison (reframed: shortcut confidence vs. content confidence)"
    figures_description:
      - "Figure 6: Reliability diagram — exception_only 的 perfect diagonal 重新标注为 'shortcut-induced calibration'"
    analysis: >
      worst tier 下 calibration 数据的叙事反转：从 'exception signal 使模型 know what it knows'
      变为 'format shortcut 使模型过度自信于一个 brittle rule'。nomarker 实验将验证
      这一解读——如果去标记后 calibration 显著恶化（ECE 升至 loop_only 水平），
      则确认 calibration 是 shortcut 的副产物而非 semantic understanding 的证据。

  # ============================================================
  # plan_008 — seed robustness (DONE, actual data)
  # ============================================================
  - name: "Seed robustness (3 seeds × exception_only + VOTA)"
    plan_id: "plan_008"
    description: "3 random seeds 验证 exception_only / VOTA 结果稳定性。"
    expected_results:
      qwen_exception_only_3seed: [0.9983, 0.9983, 0.9983]
      qwen_exception_only_std: 0.0
      qwen_vota_seed42: 0.9941
      qwen_vota_seed456: 0.9908
      deepseek_exception_only: [0.9933, 0.9933, 0.9109]
    result_rationale: >
      （实际数据）Qwen exception_only 3 seeds 完美一致，std=0。
      在 worst tier 下：零方差恰好是 shortcut 的 signature——一个 trivial pattern
      （format marker 有无）会被任何 LoRA 初始化可靠地学到，因此 zero variance
      不是 robustness 的证据，而是 simplicity / shortcut 的证据。
      对比：nomarker 实验 worst tier 预测 3-seed 方差显著上升（std ~2.6pp），
      因为移除 shortcut 后模型必须学习 harder content patterns，对初始化更敏感。
    tables:
      - "Table 9: Seed robustness — with vs without format markers"
    figures_description:
      - "Figure 7: Seed variance comparison — exception_only (std=0) vs nomarker (std~2.6pp)"
    analysis: >
      seed robustness 数据在 worst tier 下完成了一个 narrative arc：
      with markers → perfect reproducibility (shortcut 的 hallmark)；
      without markers → high variance (content learning 对 init 敏感)。
      这与 NLI shortcut 文献中 hypothesis-only models 的 high stability
      形成平行对比。

  # ============================================================
  # plan_012 — Qwen-1.5B cross-scale (DONE, actual data)
  # ============================================================
  - name: "Qwen-2.5-Coder-1.5B 四条件验证"
    plan_id: "plan_012"
    description: "1.5B 模型复现 exception_only/vota/no_trace/full_trace。验证 scale invariance。"
    expected_results:
      exception_only: 0.9983
      vota: 0.9958
      no_trace: 0.6731
      full_trace: 0.7706
    result_rationale: >
      （实际数据）1.5B exception_only = 99.83% = 7B。
      在 worst tier 下：这是 format shortcut 假说最强的单项证据之一。
      一个 1.5B 参数模型精确匹配 7B 模型意味着任务不需要 7B 的 capacity，
      1.5B 即可完美学到——这与 'fault semantics' 需要 substantial reasoning capacity
      的预期矛盾，却与 'format marker matching is trivial' 完美一致。
      如果是 genuine fault detection，我们预期 1.5B 至少有 1-2pp 的 capacity gap。
      zero gap 说明任务的 effective complexity 极低——即 regex-level。
    tables:
      - "Table 1: Cross-scale results"
      - "Table 10: Scale invariance as shortcut evidence"
    figures_description:
      - "Figure 8: Model scale vs accuracy — exception_only flat line at 99.83% across 1.5B/7B/13B"
    analysis: >
      1.5B = 7B 是 worst tier 论文的 'smoking gun' 之一。论文可以写：
      "The fact that a 1.5B model achieves identical accuracy to 7B on exception_only
      (both 99.83%) while showing clear capacity gaps on no_trace (67.31% vs 75.13%)
      and full_trace (77.06% vs 81.76%) strongly suggests that exception_only success
      relies on a pattern simple enough to be learned at any scale — consistent with
      format marker matching rather than fault reasoning."

  # ============================================================
  # plan_013 — CodeLlama-13B cross-family (PARTIALLY DONE)
  # ============================================================
  - name: "CodeLlama-13B-Instruct 三条件验证"
    plan_id: "plan_013"
    description: "LLaMA 家族 + 13B scale 验证 exception_only/no_trace/vota。"
    expected_results:
      exception_only: 0.9983
      no_trace: 0.765
      vota:
        accuracy: 0.9992
        n: 1190
        errors: 1
        pass_recall: 0.9988
        fail_recall: 1.0
        pass_precision: 1.0
        fail_precision: 0.9971
        ECE_estimated: 0.001
    result_rationale: >
      exception_only=99.83%（实际数据，2 errors = GeneratorExit irreducible）。
      no_trace=76.5%（实际数据）。
      **VOTA=99.92%（预测）**：CodeLlama-13B 是测试的最大模型（13B vs 6.7-7B），
      在 worst tier 下 VOTA ≥ exception_only 因为：
      (1) 13B 有足够 capacity 利用 VOTA 全部组件（loop/ae/exception）的 format cues；
      (2) VOTA 的额外组件在强模型上不再是 noise 而是 supplementary signal；
      (3) 99.92% vs exception_only 99.83% → exception dominance 不成立（Δ = -0.09pp）。
      这打破了 'exception_only always best' 的 universal claim，
      证明 Claim 3 层级关系是 model-specific：小/弱模型上 exception 优于 VOTA，
      大/强模型上 VOTA ≥ exception。
    tables:
      - "Table 1: Cross-model results — CodeLlama-13B 行"
      - "Table 11: Exception dominance breakdown by model scale"
    figures_description:
      - "Figure 9: Exception_only vs VOTA gap across models — CodeLlama-13B shows VOTA ≥ exception"
      - "Figure 8: Scale vs accuracy — 13B breaks the exception dominance pattern"
    analysis: >
      CodeLlama-13B VOTA=99.92% 在 worst tier 下有双重意义：
      (1) exception dominance 是 capacity-dependent artifact：小模型无法充分利用
      VOTA 的多种 format cues，只能依赖最 salient 的单一 marker (exception)，
      给人 'exception is best' 的错觉。大模型同时利用所有 format cues 达到更高 accuracy。
      (2) 这进一步支持 'format engineering' 而非 'fault semantics' 叙事——
      VOTA 在 13B 上更好不是因为 'better fault reasoning'，而是因为 13B 能
      simultaneously exploit multiple format shortcuts。

  # ============================================================
  # plan_014 — multi-seed expansion (DONE, actual data)
  # ============================================================
  - name: "Multi-seed: ae_only / label_only / loop_only × 3 seeds"
    plan_id: "plan_014"
    description: "Tier 层级划分的 seed robustness 验证。"
    expected_results:
      ae_only_3seed: [0.9992, 0.9908, 0.9992]
      ae_only_mean: 0.9964
      ae_only_std: 0.0049
      label_only_3seed: [0.8622, 0.8706, 0.859]
      label_only_mean: 0.8639
      loop_only_3seed: [0.8563, 0.8588, 0.8664]
      loop_only_mean: 0.8605
      loop_only_std: 0.0052
    result_rationale: >
      （实际数据）ae_only 高方差（seed123=99.08% outlier），loop_only 和 label_only 稳定。
      在 worst tier 下：ae_only 的 seed variance > exception_only 的 zero variance，
      说明 ae 的 format marker（assertion 结果标记）比 exception 的 [No exception data in trace]
      稍不 deterministic——可能因为 assertion marker 的格式更复杂，
      不同 init 学到的程度不同。loop_only 和 label_only 的 ~86% stability
      反映了 content-level learning 的 consistent ceiling（无强 format marker 时的上限）。
    tables:
      - "Table 2: Component ablation with seed robustness"
      - "Table 12: Variance as format marker strength proxy"
    figures_description:
      - "Figure 10: Seed variance vs component accuracy — inverse relationship supporting shortcut hypothesis"
    analysis: >
      worst tier 下 multi-seed 数据揭示一个 pattern：
      高 accuracy + 低 variance = 强 format marker (exception_only: 99.83±0)；
      高 accuracy + 中 variance = 中 format marker (ae_only: 99.64±0.49)；
      中 accuracy + 低 variance = 无 format marker (loop/label: ~86±0.5)。
      这支持 'variance 与 format marker strength 成反比' 的规律。

  # ============================================================
  # plan_015 — FORMAT MARKER REMOVAL (RUNNING — KEY WORST-TIER EXPERIMENT)
  # ============================================================
  - name: "Format marker removal: exception_only_nomarker × 3 seeds"
    plan_id: "plan_015"
    description: >
      移除 [No exception data in trace] 格式标记后重训 exception_only。
      pass 样本从 '[No exception data in trace]' 变为空/极短文本；
      fail 样本保留异常内容但移除 [ERROR] 前缀。
      3 seeds (42/123/456) 验证 format marker 的因果贡献。
    expected_results:
      nomarker_seed42:
        accuracy: 0.9176
        pass_recall: 0.887
        fail_recall: 0.993
        pass_precision: 0.997
        fail_precision: 0.778
        n: 1190
        errors: 98
        error_breakdown: "96 pass→fail FN, 2 fail→pass FP"
        train_loss_estimated: 0.16
      nomarker_seed123:
        accuracy: 0.8680
        pass_recall: 0.821
        fail_recall: 0.985
        pass_precision: 0.993
        fail_precision: 0.687
        n: 1190
        errors: 157
        error_breakdown: "152 pass→fail FN, 5 fail→pass FP"
        train_loss_estimated: 0.17
      nomarker_seed456:
        accuracy: 0.9034
        pass_recall: 0.868
        fail_recall: 0.991
        pass_precision: 0.996
        fail_precision: 0.750
        n: 1190
        errors: 115
        error_breakdown: "112 pass→fail FN, 3 fail→pass FP"
        train_loss_estimated: 0.16
      three_seed_summary:
        mean_accuracy: 0.8963
        std_accuracy: 0.025
        worst_seed_accuracy: 0.8680
        best_seed_accuracy: 0.9176
        format_marker_contribution_pp: 10.20
        format_marker_pct_of_total_lift: 0.413
        content_signal_contribution_pp: 14.50
      comparison_with_regex_B5:
        regex_B5: 0.9933
        nomarker_mean: 0.8963
        delta: -0.097
        interpretation: "SFT without markers is 9.7pp BELOW regex; format marker was the mechanism"
      comparison_with_loop_only:
        loop_only_mean: 0.8605
        nomarker_mean: 0.8963
        delta: 0.036
        interpretation: "nomarker barely above loop_only; content contribution similar"
      nomarker_calibration_estimated:
        ECE: 0.065
        Brier: 0.085
        interpretation: "Calibration degrades ~24x from exception_only ECE=0.0027 to ~0.065; confirms marker-driven calibration"
    result_rationale: >
      移除 [No exception data in trace] 后，pass 样本失去唯一的 explicit classification signal。
      模型必须从 'content 为空/极短 → pass' 学习，但这是一个 weaker, indirect cue：
      (1) 空文本不是 informative feature，而是 absence of feature——学习 absence 比学习 presence 更难；
      (2) 部分 pass 样本可能仍有少量非异常文本（如 GeneratorExit），制造 noise；
      (3) fail 样本仍有异常内容（类型 + 消息），但失去 [ERROR] 前缀后，
      模型需要从原始异常文本的语义特征（如 'AssertionError', 'TypeError'）学习 fail 映射。
      
      seed variance 显著上升（std ~2.5pp vs 0.0pp）因为 content-level learning
      对 LoRA 初始化更敏感——没有了 deterministic shortcut，模型需要学习更 nuanced 的 pattern，
      不同初始化可能学到不同 decision boundaries。
      
      worst seed (86.8%) 接近 loop_only (85.6%)，说明无 format marker 的 exception content
      提供的 signal 与 loop compression 相当——两者都是 content-level 学习，accuracy 相似。
      
      fail_recall 保持高位 (0.985-0.993) 因为 fail 样本仍有异常文本内容（只是没有 [ERROR] 前缀），
      模型可以从 'AssertionError: expected X got Y' 等文本学习 fail。
      pass_recall 大幅下降 (0.82-0.89) 因为 pass 样本的分类依据从 explicit marker 退化为
      'content 很短或为空'——这是一个 noisy, indirect signal。
    tables:
      - "Table 13 (NEW — 论文核心 table): Format marker removal results"
      - |
        | Seed | with marker | without marker | Δ | pass_recall Δ | fail_recall Δ |
        |------|------------|---------------|-----|---------------|---------------|
        | 42   | 99.83%     | 91.76%        | -8.07pp | -0.111  | -0.005  |
        | 123  | 99.83%     | 86.80%        | -13.03pp| -0.177  | -0.013  |
        | 456  | 99.83%     | 90.34%        | -9.49pp | -0.130  | -0.007  |
        | Mean | 99.83%     | 89.63%        | -10.20pp| -0.139  | -0.008  |
      - "Table 14: SFT vs Regex comparison"
      - |
        | Method | Accuracy | Mechanism |
        |--------|----------|-----------|
        | Regex B5 (format marker) | 99.33% | [No exception data in trace] 有无 |
        | SFT exception_only (with markers) | 99.83% | format marker + minor content signal |
        | SFT exception_only (nomarker) | 89.63% | content only |
        | Regex B1 ([ERROR] presence) | 93.45% | [ERROR] keyword 有无 |
    figures_description:
      - "Figure 1 (论文 main figure): Paired bar chart — with_marker vs nomarker across 3 seeds, with regex B5 reference line at 99.33%"
      - "Figure 11: Pass/fail recall decomposition — showing pass_recall is where format marker removal concentrates degradation"
      - "Figure 12: Contribution decomposition waterfall — total lift 24.7pp = content 14.5pp + format 10.2pp"
    analysis: >
      nomarker 是 worst tier 的 defining result。10.2pp drop 意味着：
      
      (1) FORMAT MARKER AS CLASSIFICATION SHORTCUT：SFT exception_only 学到的主要不是
      'exception content → fault detection' 而是 '[No exception data in trace] 有无 → pass/fail'。
      移除标记后 accuracy 从 99.83% 降至 89.63%，而 regex B5（纯 marker check）= 99.33%。
      SFT with markers (99.83%) ≈ regex (99.33%)，Δ 仅 0.50pp。
      SFT without markers (89.63%) < regex (99.33%)，Δ = -9.70pp。
      结论：SFT 的 value-add over regex 仅 0.50pp，主要靠 format shortcut。
      
      (2) CONTENT CONTRIBUTION IS REAL BUT SECONDARY：nomarker 89.63% > no_trace 75.13%，
      content signal 贡献 14.5pp（占总 lift 的 59%）。exception content 确实有用——
      异常类型和消息文本帮助 fail detection（fail_recall 仍 >98%）。
      但 pass detection 严重依赖 format marker（pass_recall 从 0.998 降至 0.86）。
      
      (3) SEED VARIANCE AS SHORTCUT DEPENDENCY INDICATOR：with markers std=0.0pp → 
      trivial pattern, perfectly reproducible；without markers std=2.5pp → 
      content learning is harder, init-sensitive。variance shift 是 shortcut
      dependency 的 causal evidence。
      
      (4) NARRATIVE REFRAME：论文从 'exception events as fault detection signal'
      变为 'format markers as implicit task specification in SFT'。
      贡献 = 揭示 SFT 中 trace format design choices 的 outsized, hidden impact，
      与 shortcut learning 文献（Gururangan 2018, McCoy 2019, annotation artifacts）对话。
      实践建议：trace format 设计应 explicitly 考虑 downstream task 的 shortcut affordance，
      评估 SFT verdict models 时必须包含 format ablation control。

  # ============================================================
  # plan_006 continued — trace length (summarized, DONE)
  # ============================================================

  # ============================================================
  # CROSS-CUTTING: worst-tier synthesis tables
  # ============================================================
  - name: "Cross-cutting synthesis: format dependency master table"
    plan_id: "synthesis"
    description: "跨所有实验的 format marker contribution 综合分析。"
    expected_results:
      decomposition:
        total_trace_lift_pp: 24.70
        content_signal_pp: 14.50
        format_marker_pp: 10.20
        format_pct: 0.413
      model_scale_pattern:
        qwen_1.5B_exception: 0.9983
        qwen_7B_exception: 0.9983
        deepseek_6.7B_exception_median: 0.9933
        codellama_13B_exception: 0.9983
        interpretation: "scale-invariant → trivial pattern"
      format_marker_vs_regex:
        sft_with_markers: 0.9983
        regex_B5: 0.9933
        sft_without_markers: 0.8963
        delta_sft_over_regex_with: 0.0050
        delta_sft_over_regex_without: -0.0970
      codellama_vota_exception_gap: -0.0009
    result_rationale: >
      综合所有实验数据，worst tier 叙事的 evidence chain：
      (1) Scale invariance: 1.5B = 7B = 13B 在 exception_only 上完全一致 → trivial task；
      (2) SFT ≈ regex: 99.83% vs 99.33% (Δ=0.50pp) → SFT barely beats a regex；
      (3) nomarker drop: 99.83% → 89.63% (Δ=10.20pp) → format markers are load-bearing；
      (4) nomarker < regex: 89.63% < 99.33% → without markers, SFT is WORSE than regex；
      (5) VOTA ≥ exception on 13B: 99.92% vs 99.83% → 'exception dominance' is model-specific；
      (6) nomarker variance ≈ loop_only level: content-level learning has consistent ~86-90% ceiling。
    tables:
      - "Table 15 (论文 summary table): Evidence chain for format shortcut hypothesis"
      - |
        | Evidence | Value | Interpretation |
        |----------|-------|---------------|
        | SFT with markers | 99.83% | ≈ regex B5 (99.33%), Δ=0.50pp |
        | SFT without markers | 89.63% | < regex B5, format was the mechanism |
        | Format contribution | 10.20pp | 41.3% of total trace lift |
        | Scale invariance | 1.5B=7B=13B | Trivial task (format matching) |
        | Seed variance shift | 0→2.5pp | Shortcut removal increases instability |
        | CodeLlama-13B VOTA≥exception | -0.09pp | Exception dominance model-specific |
    figures_description:
      - "Figure 13 (论文 summary figure): Evidence decomposition — pie chart (content 59% + format 41%) overlaid with regex comparison"
    analysis: >
      worst tier 论文的核心 contribution 变为三点：
      
      C1 (rewritten): 'Structured format markers dominate verdict prediction in exception traces.'
      Evidence: format markers contribute 10.2pp (41.3%); SFT ≈ regex; scale-invariant.
      
      C2 (preserved): 'Information density, not gradient dilution, drives trace compression benefit.'
      Evidence: label-only decomposition unchanged. Additional angle: format marker accessibility
      is the information density mechanism — VOTA/exception_only 把 marker 放在 most accessible 位置。
      
      C3 (rewritten): 'Format engineering > content richness for SFT verdict tasks.'
      Evidence: exception dominance is model-specific (fails on 13B); nomarker ≈ loop_only;
      trace format design choices (markers, structure) have larger impact than content.
      
      Venue: 仍冲 EMNLP Main。Angle 从 'positive finding about exception semantics'
      变为 'cautionary finding about SFT shortcut learning + practical design principle'。
      与 shortcut learning 文献 (Gururangan 2018, McCoy 2019, Gardner 2021)
      和 annotation artifacts 文献对话。Practical contribution: trace format design guidelines
      that account for downstream shortcut affordance。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa9fef4c-f10f-4022-94ce-b8111a504016",
  "isSidechain": false,
  "requestId": "req_011Cb6Y8zMeco44Sq17y1rYa",
  "type": "assistant",
  "uuid": "1aea9c95-2bb7-425e-a507-985b5f339084",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4",
  "sessionId": "1723cae9-4a61-47ee-b162-e2fd329daf4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013RXsxQr3tgQbdcK2ZoEWCk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 34669,
      "cache_read_input_tokens": 11841,
      "output_tokens": 22302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34669,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 22302,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 34669,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34669
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：nomarker 实验显著退化，暴露格式标记是主要机制；原始 'fault semantics' 叙事不成立，需要 reframe 核心假设：['nomarker 实验 <90%（或 3-seed 高方差，worst seed <85%）：移除格式标记后大幅退化，证明模型主要依赖 format patter…",
  "leafUuid": "1aea9c95-2bb7-425e-a507-985b5f339084",
  "sessionId": "1723cae9-4a61-47ee-b162-e2fd329daf4b"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe exception signal dominance as format shortcut learning",
  "sessionId": "1723cae9-4a61-47ee-b162-e2fd329daf4b"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：nomarker 实验显著退化，暴露格式标记是主要机制；原始 'fault semantics' 叙事不成立，需要 reframe 核心假设：['nomarker 实验 <90%（或 3-seed 高方差，worst seed <85%）：移除格式标记后大幅退化，证明模型主要依赖 format patter…",
  "leafUuid": "1aea9c95-2bb7-425e-a507-985b5f339084",
  "sessionId": "1723cae9-4a61-47ee-b162-e2fd329daf4b"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe exception signal dominance as format shortcut learning",
  "sessionId": "1723cae9-4a61-47ee-b162-e2fd329daf4b"
}
```

---
