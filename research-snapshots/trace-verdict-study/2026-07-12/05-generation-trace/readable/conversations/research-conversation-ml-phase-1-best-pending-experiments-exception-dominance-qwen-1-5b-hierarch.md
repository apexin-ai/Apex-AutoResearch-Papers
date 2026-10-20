# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：所有 pending experiments 一致强化 exception dominance；第三模型 Qwen-1.5B 完整复现 hierarch

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/f7665a3e-5d5c-49f9-8d35-6afa1c42cf9b.jsonl`
- **Structured JSON:** [`7078205eec190ec24f13.json`](../../sessions/70/7078205eec190ec24f13.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T10:56:17.012Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T10:56:17.012Z",
  "sessionId": "f7665a3e-5d5c-49f9-8d35-6afa1c42cf9b",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：所有 pending experiments 一致强化 exception dominance；第三模型 Qwen-1.5B 完整复现 hierarchy；三模型 × 跨规模叙事 → EMNLP main\n核心假设：['Qwen-1.5B VOTA 显著低于 exception_only (99.83%)，复现 7B 上 exception > VOTA 的 gap pattern', 'nomarker ablation 显示 [ERROR] 标记贡献 ≥2pp，确认 fault indicator marker 不是 trivial formatting 而是 learned signal 的关键锚点', 'loop_only seed123/456 稳定在 83-88%（与 seed42 的 85.63% 一致），Tier 2 鲁棒性确认', 'Qwen-1.5B exception_only=99.83% 已锁定 — 1.5B 与 7B 完全一致，scale-invariant 证据极强', '3 模型 (Qwen-7B, DeepSeek-6.7B, Qwen-1.5B) 含 5x 参数量跨度 + architecture diversity，universality claim 从 N=2 升至 N=3']\n关键指标范围：{'qwen15b_vota_accuracy': [85.0, 95.0], 'nomarker_accuracy_drop_vs_marker': [2.0, 7.0], 'loop_only_3seed_std_pp': [0.0, 2.0], 'effective_model_count': [3, 3], 'models_where_exception_gt_vota': [3, 3], 'deepseek_exception_only_median': [99.33, 99.33], 'qwen7b_exception_only': [99.83, 99.83]}\n叙事方向：原始 framing 完全成立，Claims 1-3 无需调整。 Headline: \"Exception events are the minimal sufficient diagnostic signal — validated across 3 models spanning 1.5B to 7B parameters.\" Qwen-1.5B 提供三重价值: (1) exception_only 99.83% scale-invariant 确认信号 simplicity; (2) VOTA gap 复现确认 Tier 2 的 model-capability dependence; (3) 1.5B 的 no_trace=67.31% vs exception_only=99.83% (+32.5pp) 是全文最大 lift， 强化 \"越弱的模型越依赖 exception signal\" 叙事。 nomarker ablation 作为 fine-grained mechanism evidence 纳入 analysis section。 EMNLP main 直投，findings 不需要作 fallback。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: trace-verdict-study\n\n## paper_framing.md\n\n# Paper Framing — trace-verdict-study\n\n> v3.0 — [UPDATED 2026-05-15] D030 CLOSED: DeepSeek VOTA 84.45% confirmed correct (confirmatory re-eval). **Critical narrative fix**: to_chat_text() preserves labels → VOTA 训练时 verdict label 未被截断 → 论文中 \"label truncation/corruption\" 措辞对 VOTA 不成立。正确叙事: trace INPUT content 被截断 (91.7% samples), 84.45% 反映 trace information loss。新增 D11: VOTA cross-model gap confounded by training-time truncation。数据集来源：HumanEval (164) + MBPP-sanitized (427) = 591 problems × 10 LLM-generated solutions = 5910 samples。\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026\n\n## Core Insight\n\nVerdict prediction (pass/fail) is fundamentally a **fault detection** task. The most effective signal is the **exception event** — a compact, structured diagnostic moment that consistently outperforms all other trace representations across models (Qwen 99.83% ± 0.00 across 3 seeds; DeepSeek 91-99% depending on seed, but always > VOTA 84.45% and no_trace 73.36%). In contrast, richer trace representations that require deeper execution reasoning show model-dependent effectiveness: VOTA gap = 14.96pp, no_trace gap = 1.77pp. Information density — not training signal distribution — is the primary bottleneck: even oracle loss masking (label-only) cannot close the 13pp gap between full traces and targeted extraction. The design principle: **extract the highest-specificity diagnostic signal; discard everything else.** Cross-model absolute performance depends on LoRA initialization stability, but exception_only's relative dominance over other components is robust.\n\nVOTA's primary contribution is **fault indicator isolation** — automatically extracting exception events from noisy full traces — rather than generic trace compression. The \"compression helps\" narrative was a stepping stone; the real mechanism is diagnostic signal extraction.\n\n## Core Claims (3)\n\n### Claim 1: Exception events are the most effective trace component for verdict prediction\n\nException summaries consistently achieve the highest verdict prediction accuracy across both models tested, outperforming all other trace representations in every seed. On Qwen-2.5-Coder-7B, performance is perfectly robust: 99.83% ± 0.00 (3 seeds). On DeepSeek-Coder-6.7B, absolute accuracy is seed-dependent (seed42=99.83% epoch1, seed123=91.43% epoch1; Δ=8.40pp), consistent with LoRA initialization sensitivity — but exception_only still dominates VOTA (84.45%) and no_trace (73.36%) in all seeds. This contrasts with VOTA (cross-model gap = 14.96pp) and no_trace (gap = 1.77pp). Exception events are structurally simple (`[ERROR] type: ... message: ...`) and do not require deep trace reasoning.\n\n**Supporting evidence:**\n- `vota_exception_only_seed42_v2`: Qwen 99.83%, ECE=0.0027\n- `deepseek_exception_only_seed42`: DeepSeek 99.83% (epoch1) / 99.33% (epoch3)\n- `deepseek_exception_only_seed456`: DeepSeek 99.33% (epoch3), CI [98.82, 99.75] — 与 seed42 完全一致\n- `deepseek_exception_only_seed123`: DeepSeek 91.43% (epoch1) / 91.09% (epoch3) — LoRA init sensitivity outlier\n- `deepseek_vota_seed42`: DeepSeek VOTA 84.45% (gap = 14.96pp vs Qwen)\n- `deepseek_no_trace_seed42`: DeepSeek no_trace 73.36% (gap = 1.77pp vs Qwen)\n- `vota_no_ae_seed42`: 99.41% — actual/expected removal 不降，非 trivial string comparison\n\n**DeepSeek seed analysis** ✅ (FINALIZED, D029):\n\n| Seed | Epoch 3 (final) | fail_recall | pass_recall | train_loss | Errors | CI |\n|------|-----------------|-------------|-------------|------------|--------|-----|\n| 42   | 99.33%          | 1.0         | 0.9906      | —          | 8/1190 | — |\n| 456  | 99.33%          | 1.0         | 0.9906      | 0.1225     | 8/1190 | [98.82, 99.75] |\n| 123  | 91.09%          | 0.705       | 0.993       | 0.122      | —      | [89.4, 92.6] |\n\nseed42 与 seed456 结果**完全一致**（均 8/1190 错误，99.33%），seed123 为离群值。seed123 的 fail_recall 仅 0.705 — LoRA 初始化落入差的局部最优，未充分学到 exception→fail 映射。**关键发现**: seed456 和 seed123 的 train_loss 几乎相同（0.1225 vs 0.122），但 accuracy 差 8.2pp — token-level loss 掩盖了 sample-level 分类能力的巨大差异（详见 D10）。\n\n**Irreducible error analysis** ✅: 3 seeds 错误的 2 个样本 (id=901, 905) 均来自 HumanEval/95 (`check_dict_case`)，根因为 Python `all()` 对 generator expression 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误）。tracer 将其标记为 `[ERROR]`，exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。整个 1190 条测试集仅这 2 条含 `GeneratorExit`，模型无训练信号学习其良性本质。**这确认 99.83% 是 exception_only 表征的理论上限，剩余 0.17% 是 representation-inherent irreducible error，而非模型不足。**\n\n**Seed robustness** ✅: Qwen exception_only 3-seed 完全一致，构成本文最强 robustness 证据：\n\n| Seed | Accuracy | 95% CI | Errors |\n|------|----------|--------|--------|\n| 42 | 99.83% | [99.58, 100] | 2/1190 |\n| 123 | 99.83% | [99.58, 100] | 2/1190 |\n| 456 | 99.83% | [99.58, 100] | 2/1190 |\n\n3 seeds 错误样本 100% 重叠（id=901, 905, 均为 `check_dict_case` 函数, label=pass → pred=fail）。**Irreducible samples**: 模型已达数据集理论上限，variance = 0。\n\n**DeepSeek cross-model** ✅ (D029): 3-seed 完整数据 — seed42/456=99.33%, seed123=91.09%。2/3 seeds 鲁棒，seed123 为 LoRA 初始化离群值（fail_recall 仅 0.705）。Qwen 3-seed 完美稳定 (99.83% ± 0.00) vs DeepSeek 高方差（σ≈4.8pp），暗示 exception signal 的 learnability 与模型 LoRA 训练稳定性相关。但即使最差 seed (91.09%) 仍优于 VOTA (84.45%) 和 no_trace (73.36%)，relative dominance robust。\n\n### Claim 2: Information density, not gradient dilution, drives trace compression benefit\n\nFull traces help verdict prediction (81.76% [`full_trace_seed42_v5`], +6.6pp over baseline), but VOTA achieves 99.41% [`vota_seed42_v5`] (+24.3pp) — a +17.6pp advantage. Label-only loss ablation (plan_002) quantifies the causal decomposition: **gradient dilution contributes ~26% of the gap** (4.5pp; label-only full_trace = 86.22% [`full_trace_label_only_seed42`]), **information overload contributes ~74%** (13.0pp; only trace compression resolves this). Even with oracle loss masking that eliminates gradient dilution, full traces still underperform VOTA by 13pp.\n\nCross-model evidence reinforces this: VOTA gap (14.96pp) partly tracks base model execution reasoning capability (Qwen CRUXEval-I 56.5% vs DeepSeek 39.0%, Δ=17.5pp), though **confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated to ~2048 tokens; see D11). The two factors cannot be disentangled in the current design. Exception signal partially bypasses both bottlenecks (token-short, no truncation; consistently best component on both models), though DeepSeek shows seed-dependent absolute performance (91-99%).\n\n**Supporting evidence:**\n- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (gradient dilution fix, +4.5pp over standard full_trace)\n- `full_trace_seed42_v5`: 81.76%, ECE=0.0958 (standard full_trace)\n- `vota_seed42_v5`: 99.41%, ECE=0.0054\n- `deepseek_vota_seed42`: 84.45% (VOTA model-dependent)\n- CRUXEval literature data (Wang et al.)\n\n### Claim 3: Two-tier diagnostic hierarchy for verdict prediction\n\nComponent ablation reveals verdict-relevant trace information has a strict two-tier hierarchy:\n- **Tier 1 — diagnostic moment signals**: exception summaries (99.83% [`vota_exception_only_seed42_v2`]) and assertion-point information (99.92% [`vota_ae_only_seed42`]) are individually near-perfect and sufficient for verdict prediction on Qwen. These signals are structurally simple and consistently the most effective component on both models, though DeepSeek absolute performance is seed-dependent.\n- **Tier 2 — behavioral patterns**: loop compression (85.63% [`vota_loop_only_seed42`]) carries substantial signal but is model-dependent and fully subsumed by Tier 1.\n\nCombining tiers introduces noise rather than helping: exception_only (99.83%) > VOTA full (99.41%), p=0.01. Loop_only ≈ full_trace_label_only (85.63% vs 86.22%) confirms VOTA's loop compression precisely extracts the useful behavioral signal from full traces.\n\n**Supporting evidence:**\n- `vota_exception_only_seed42_v2`: 99.83%, ECE=0.0027 (Tier 1 exception)\n- `vota_ae_only_seed42`: 99.92%, ECE=0.0004 (Tier 1 assertion-point, 与 exception 统计等价 p=0.80)\n- `vota_loop_only_seed42`: 85.63%, ECE=0.0831 (Tier 2 behavioral)\n- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (≈ loop_only, confirming extraction equivalence)\n- `deepseek_exception_only_seed42`: 99.83% epoch1 / 99.33% epoch3 (Tier 1 cross-model validation)\n- `deepseek_vota_seed42`: 84.45% (Tier 1+2 cross-model: Tier 2 introduces model-dependent degradation)\n\n**Calibration**: 完整 calibration 数据确认 Tier 1 信号不仅 accuracy 近完美，置信度校准也近完美：\n\n| Condition | Accuracy | ECE | Brier | 解读 |\n|-----------|----------|-----|-------|------|\n| ae_only | 99.92% | 0.0004 | 0.0008 | 近乎完美校准 |\n| exception_only | 99.83% | 0.0027 | 0.0013 | 近乎完美校准 |\n| VOTA | 99.41% | 0.0054 | 0.005 | 优秀，但 Tier 2 引入轻微 noise |\n| loop_only | 85.63% | 0.0831 | — | Tier 2 单独校准中等 |\n| label_only | 86.22% | 0.1107 | — | gradient dilution fix 仍 miscalibrated |\n| full_trace | 81.76% | 0.0958 | — | 中度 miscalibrated |\n| no_trace | 75.13% | 0.1715 | 0.1972 | 严重 miscalibrated |\n\nno_trace ECE 是 exception_only 的 **~63x**（0.1715/0.0027），Brier 是 **~150x**（0.1972/0.0013）。Trace signal（尤其 Tier 1）不仅提升 accuracy，更从根本上改善模型 calibration。\n\n**Design principle**: verdict-optimized traces should extract highest-specificity diagnostic signals; lower-specificity signals are redundant and may introduce noise.\n\n## Cross-Model Evidence Summary\n\n| Condition | Qwen-2.5-Coder-7B | DeepSeek-Coder-6.7B | Cross-model gap | Interpretation |\n|-----------|-------------------|---------------------|-----------------|----------------|\n| exception_only | 99.83% ± 0.00 (3 seeds) | seed42/456: 99.33%; seed123: 91.09% | 0.50-8.74pp (seed-dependent) | **Best component on both models**; 2/3 DeepSeek seeds match Qwen-level; 1 outlier still > VOTA |\n| VOTA | 99.41% | 84.45% | -14.96pp | Model-dependent — requires execution reasoning; **also confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated from mean 2626 to ~2048 tokens; labels preserved via to_chat_text(), see D11) |\n| no_trace | 75.13% | 73.36% | -1.77pp | Baseline gap tracks general capability |\n| full_trace | 81.76% | collapsed (v3 pending) | N/A | DeepSeek v1 label truncation bug |\n\n**Key insight**: Exception_only is consistently the best component on both models (even worst DeepSeek seed 91.09% > VOTA 84.45%). Cross-model gap 与 signal complexity 正相关, but exception signal's absolute effectiveness also depends on LoRA training stability. Qwen: perfectly robust (3 seeds identical). DeepSeek: 2/3 seeds at 99.33% (matching Qwen-level), 1 outlier at 91.09% (LoRA initialization). Median performance robust; seed sensitivity suggests smaller/weaker models may need training stabilization (multi-seed selection, warmup tuning) for optimal exception signal utilization.\n\n## VOTA Repositioning\n\n**旧叙事**: VOTA 是 trace compression 方法，价值在于\"压缩使 trace 更有效\"。\n\n**新叙事**: VOTA 是 **fault indicator isolation** 方法，核心价值在于自动从 noisy execution traces 中提取 exception events 等 diagnostic signals。\n\n**证据链**:\n1. exception_only (99.83%) ≥ VOTA full (99.41%) — 压缩后的其他组件（loop, ae）不仅无益，反而引入 noise\n2. VOTA 跨模型 gap = 14.96pp — 因为 VOTA 包含 model-dependent 的 Tier 2 组件（loop compression 需要 execution reasoning）\n3. exception_only 在两个模型上均为最优组件 — isolate 出 Tier 1 后，相对优势 robust（虽然 DeepSeek 绝对值 seed-dependent）\n4. vota_no_ae (99.41%) = VOTA (99.41%) — actual/expected 移除无影响，exception 是真正的 active ingredient\n\n**论文中的表述**: \"VOTA's trace compression pipeline incidentally isolates exception events — the minimal sufficient diagnostic signal. Its value lies not in making traces shorter, but in separating high-specificity fault indicators from low-specificity behavioral patterns.\"\n\n**对 Method section 的影响**: VOTA 仍然完整描述（loop compression + exception + actual/expected），但 Results/Discussion 明确指出 exception isolation 是核心机制，其他组件是 model-capability-dependent bonus。\n\n## Story Spine\n\n- **Problem**: Existing trace SFT studies (DCSH, TracePile) evaluate only generative tasks and find limited, model-dependent benefit. No prior work has tested trace SFT on verdict tasks (binary pass/fail), nor identified what trace components drive classification performance.\n\n- **Existing approaches & gaps**: DCSH (EMNLP Findings 2025) tested 5 trace formats on generation tasks, finding that \"no single trace representation consistently outperforms others.\" TracePile (NeurIPS 2025) scaled to 2.6M samples but only evaluated generation. TRACED (ICSE 2024) showed traces help encoder-based classification. All existing trace formats are designed for execution simulation, not fault detection.\n\n- **Our framing**: We reframe verdict prediction as **fault detection** and ask: what is the minimal sufficient diagnostic signal? Through systematic component ablation across two architecturally distinct models, we discover that exception events — compact, structured error summaries — are consistently the most effective trace component, achieving near-perfect accuracy on Qwen (99.83% ± 0.00, 3 seeds) and outperforming all alternatives on DeepSeek (91-99% vs VOTA 84.45%). Richer trace representations work only when the base model has sufficient execution reasoning capability, making them unreliable for general deployment.\n\n- **Headline result**: \"Exception events consistently achieve the highest verdict accuracy across models (Qwen 99.83%, DeepSeek 91-99%), outperforming VOTA traces (84.45% on DeepSeek, -14.96pp gap) — demonstrating that fault indicator isolation, not trace reasoning, is the robust mechanism for verdict prediction. DeepSeek seed sensitivity reveals LoRA training stability as a secondary factor for smaller models.\"\n\n## Story Arc\n\n1. **Setup**: Trace SFT for code tasks — promising but inconsistent in prior work (DCSH, TracePile). Unknown whether traces help verdict tasks and what trace design matters.\n\n2. **First result — traces help, compression helps more** (single model): no_trace 75.13% → full_trace 81.76% → VOTA 99.41%. Label-only loss ablation decomposes the gap: 26% gradient dilution, 74% information overload. Compression improves accuracy through higher information density, not just cost savings.\n\n3. **Twist — what component actually drives VOTA?** Component ablation reveals exception_only (99.83%) ≥ full VOTA (99.41%). The \"trace reasoning\" narrative is wrong — verdict prediction is fault detection. Tier 1 (exceptions + assertion-point) subsumes Tier 2 (loops). Actual/expected removal doesn't hurt (99.41%).\n\n4. **Cross-model stress test — consistent dominance, not universal perfection**: Exception_only is the best component on both models (even DeepSeek worst seed 91.09% > VOTA 84.45%), but absolute performance is seed-dependent on DeepSeek (91-99% vs Qwen's perfectly stable 99.83%). VOTA degrades by 14.96pp. The structurally simplest component is the most robust, but LoRA initialization sensitivity introduces variance on weaker models. Qwen seed robustness (3-seed variance = 0) + calibration (ECE=0.0027) 确认 exception signal 在强模型上的 reliability。DeepSeek seed sensitivity 揭示 training stability 作为 secondary bottleneck。\n\n5. **Design principle**: For verdict tasks, identify the highest-specificity diagnostic signal (exception events) and discard everything else. VOTA's value is fault indicator isolation — automatically extracting exceptions from noisy traces — not generic compression. Simpler signals are more robust; complexity tolerance depends on model capability.\n\n## Dataset Characteristics\n\n### Data duplication analysis\n\n| Condition | Total | Unique | Duplication rate | Cause |\n|-----------|-------|--------|------------------|-------|\n| exception_only_train | 4720 | 2858 | 39.45% | 同题多个 passing 解映射为相同 (input, output) — 无异常 → 同一 trace |\n| exception_only_test | 1190 | 607 | 48.99% | 同上 |\n| raw_traces | 5910 | 5803 | 1.81% | 完整 trace 含行号/变量值/内存地址，几乎不重复 |\n\n**Train-test input overlap: 0（无数据泄漏）**\n\n**解读**: exception_only 高重复率是 representation 的自然属性，非数据问题。多个正确解对同一测试用例执行时若均无异常，exception_only 表征退化为相同的空/无异常标记。这恰好说明 exception signal 的 compactness — 它仅编码 fault presence，不编码 solution identity。raw_traces 重复率极低 (1.81%) 因为完整 trace 包含 solution-specific 信息（变量值、内存地址）。尽管高重复率意味着有效训练样本少于名义数量，模型仍达 99.83% — 进一步确认 exception signal 的 learnability。\n\n## DeepSeek full_trace 处理\n\n**现状**: v1 坍塌（28.5%, 100% 预测 fail, 根因: 训练端 label 截断）。v2 重训启动但被 kill（Loop #6 ops worker 腾 GPU 给 vota_seed456）。v3 RUNNING（label-preserving truncation fix）。\n\n**处理方案**: v3 正在 cuda:0 上训练，预计 5/16 完成。\n\n**VOTA vs full_trace 截断机制区分** (D030 token analysis 确认):\n- **full_trace v1**: SFTTrainer right-truncation 切掉了 verdict **label** → 100% predict fail → 坍塌。根因: DeepSeek tokenizer 对 full_trace 产生 >2048 tokens, label 在截断窗口外。\n- **VOTA**: `to_chat_text()` 保留 verdict label（label 完整），但 91.7% 的样本 **trace content（input）被截断**（mean 2626 → ~2048 tokens）。84.45% 是真实结果，反映 trace 信息损失对模型学习的影响，**不是** label corruption。\n- **exception_only**: token 长度远低于 2048，不受截断影响，跨模型对比 clean。\n\n**对论文叙事的影响**: 论文中所有 \"right-truncation corrupts/removes the verdict label\" 措辞**对 VOTA 不成立**——label 完整保留，被截断的是 trace input。正确表述: \"trace content truncation causes information loss\"。VOTA cross-model gap (14.96pp) 有两个贡献因素: (1) model capability, (2) training-time trace truncation on DeepSeek (see D11)。\n\n## External Benchmark (DebugBench) Positioning\n\n**DebugBench 仅作泛化性验证，不作 trace importance 证据。**\n\n| Condition | Main Dataset | DebugBench | Δ interpretation |\n|-----------|-------------|------------|------------------|\n| no_trace | 75.13% | 96.71% | DebugBench 天花板高，baseline 已强 |\n| VOTA | 99.41% | 99.77% | +3.06pp lift — 边际 |\n| exception_only | 99.83% | 100.00% | +3.29pp lift — 边际 |\n\n**主数据集 trace lift = 24.70pp**（no_trace → exception_only），DebugBench trace lift 不到其 1/7。\n\n**论文定位规则**：\n- DebugBench → 泛化性证据（exception_only 100% = 跨数据集鲁棒性）\n- Trace importance 论证 → 仅依赖主数据集（24.7pp lift）\n- 禁止用 DebugBench 的 3.29pp lift 论证 \"trace 的核心价值\"——审稿人会攻击天花板效应\n\n## Venue Fit Risks\n\n| Risk | Assessment | Mitigation |\n|------|-----------|------------|\n| 单任务 | 仍然只在 test verdict prediction 上验证 | 跨模型验证部分弥补; Discussion 中讨论 generalization |\n| 单数据集 | HumanEval + MBPP-sanitized 是唯一数据源 (591 problems × 10 solutions) | 定位为 empirical study, 深度优于广度; 两个标准 benchmark 组合覆盖多样编程题型; exception_only 有效训练样本仅 2858 unique 即达 99.83%, 暗示 signal 的 simplicity 降低对数据量的依赖 |\n| \"只是 feature engineering\" | exception extraction 不复杂 | simplicity 本身是 contribution — 最简信号最 robust |\n| Negative result 味道 | VOTA 跨模型不 robust | Reframe: 识别 robust vs non-robust 组件边界是 positive |\n| Seed robustness (Qwen) | ✅ 已解决: 99.83% ± 0.00 (3 seeds), irreducible samples 确认 | — |\n| Seed robustness (DeepSeek) | ✅ 3-seed 完整: 2/3 at 99.33%, 1 at 91.09% | LoRA initialization sensitivity — median robust, worst still > all alternatives; 转化为 training stability finding (D9/D10) |\n| Calibration | ✅ 完整数据: Tier 1 ECE≤0.003, no_trace ECE=0.171 (~63x gap) | Brier ~150x gap 进一步确认 |\n| 只用 2 个模型 | 有限但有意义的 diversity | Architecture + pretraining data (5.5T vs 2T) + CRUXEval gap (17.5pp) 构成充分差异 |\n| 数据重复率 | exception_only 训练集 39.45% 重复 | 非数据泄漏（train-test overlap = 0）；是 representation compactness 的自然结果；有效样本仍足够学习 |\n\n## Anticipated Reviewer Concerns\n\n| Concern | Planned Response |\n|---------|-----------------|\n| \"exception_only 99.83% 是不是 trivial pattern matching [ERROR] 有无？\" | full_trace 也包含 [ERROR] 但仅 81.76%——模型需要从 trace context 中 extract 和 utilize exception signal, 不是简单 keyword detection. no_trace 无 exception, 75.13%. |\n| \"为什么 exception_only > VOTA? adding info 反而降?\" | 非 exception 组件 (loop/ae tokens) 稀释 attention 对 exception 信号的聚焦. Calibration: exception_only ECE=0.0027 vs VOTA ECE=0.0054. 部分样本 loop 正常但有 exception, 引入矛盾信号. |\n| \"CRUXEval gap 与 VOTA gap 的相关性可能是 coincidence\" | 明确标注为 hypothesis. 列出 alternatives (tokenizer efficiency, pretraining scale 2.75x, chat template). 不 overclaim. |\n| \"只有 2 个模型，universality claim 太强\" | 同意是 limitation. 两模型在 architecture (RoPE vs ALiBi), pretraining data (5.5T vs 2T), execution reasoning (CRUXEval 17.5pp gap) 上有充分差异, 不是 trivial replication. Exception signal 的 structural simplicity 提供 inductive argument for broader generalization. |\n| \"99.83% 可能 saturated, 看不出 exception 到底学了什么\" | Calibration 双指标: exception_only ECE=0.0027, Brier=0.0013 (近完美校准). 对比 no_trace ECE=0.1715, Brier=0.1972 (~63x/~150x gap). **Irreducible error 根因已明确**: 2/1190 errors 均因 Python `all()` 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误），tracer 将其标记为 `[ERROR]`。模型看到 7 行 `[ERROR] GeneratorExit` 合理预测 fail，但代码实际正确。整个测试集仅这 2 条含 `GeneratorExit`，无训练信号可学习其良性本质。99.83% 是 representation 的理论上限，非 saturation artifact。 |\n| \"只用了 1 个 seed\" | Qwen ✅: 3 seeds 99.83% ± 0.00. DeepSeek ✅: 3 seeds 完整 — seed42/456=99.33%, seed123=91.09%。2/3 鲁棒，1 离群。median=99.33%, worst=91.09% (仍 > VOTA 84.45%)。论文透明报告所有 seeds，将 seed sensitivity 转化为 LoRA training stability 的 finding（D9）。 |\n| \"eval_loss 上升但 accuracy 提升——checkpoint selection 有问题?\" | Discussion D1: token-level loss 与 binary verdict accuracy 解耦. 推荐 verdict-specific metric. Methodological contribution. |\n| \"DeepSeek full_trace 坍塌是 bug 不是 finding\" | 诚实披露根因 (训练端 label 截断). 其他 3 条件不受影响. 修复版本如就绪则补入. |\n| \"calibration 数据只有 1 个 seed\" | Seed robustness 已证明 accuracy variance=0 (3 seeds), calibration 在 accuracy 完全一致的前提下 expected 也一致. ECE/Brier 的极小值 (0.0027/0.0013) 留有极小 variance 空间. |\n| \"DeepSeek epoch1 > epoch3, 为什么用 epoch3 报告?\" | 正文报告所有 seeds 的 final + best checkpoint。seed42: epoch1=99.83%, epoch3=99.33%。seed123: epoch1=91.43%, epoch3=91.09%。D7 讨论 early stopping + D9 讨论 LoRA initialization sensitivity。不 cherry-pick best seed。 |\n| \"DeepSeek seed sensitivity 说明 exception signal 不 robust\" | Exception_only 在所有 seeds 上仍优于其他条件（worst seed 91.09% > VOTA 84.45%）。Seed sensitivity 是 LoRA training 问题而非 signal 问题——Qwen 3 seeds 完美证明 signal 本身 robust。D9 讨论 training stabilization 作为 practical recommendation。 |\n| \"exception_only 数据集 ~40-49% 重复，有效训练样本不足？\" | 重复源自 representation compactness：同题多个 passing 解均无异常 → 相同 trace。**非数据泄漏**（train-test input overlap = 0）。raw_traces 仅 1.81% 重复，确认重复是 exception_only 表征特性而非数据收集问题。模型在有效样本仅 2858 unique 的条件下仍达 99.83%，反而说明 exception signal 的高 learnability — 少量 unique 样本即可充分学习 fault detection pattern。 |\n\n## Discussion 要点\n\n### D1: eval_loss vs verdict accuracy 解耦\nDeepSeek VOTA: eval_loss epoch1→3 从 0.068 升至 0.112 (+65%), 但 accuracy 从 78.15% 升至 84.45% (+6.3pp). Token-level calibration 与 binary classification accuracy 方向相反. **Implication**: verdict tasks 应用 task-specific metric (accuracy/F1) 做 checkpoint selection, 非 eval_loss.\n\n### D2: CRUXEval gap 假说 (revised — D030 confound)\nVOTA 跨模型 gap (14.96pp) 与 CRUXEval execution reasoning gap (15-17.5pp) 数值吻合. 假说: trace utilization effectiveness 受 base model \"execution reasoning readiness\" 约束. **标注**: hypothesis, N=2, 列出 alternatives. 不 overclaim. **注意**: 我们的训练/测试数据来自 HumanEval + MBPP-sanitized（非 CRUXEval），CRUXEval-I 分数仅作为衡量两个模型 execution reasoning 能力差异的外部参照。论文中必须明确区分数据来源与外部基准引用。**D030/D034 truncation evidence**: 14.96pp gap 中截断效应有因果证据: group_analysis 显示 train-truncated 83.04% vs train-intact 100% (Fisher p≈0, 推理时无截断)。截断因果方向可 claim，模型能力差异是 residual confound。CRUXEval gap 数值吻合可能部分巧合。论文中截断效应应作为 established factor 讨论（有 group_analysis 因果证据），模型能力假说标注为 residual confound hypothesis。\n\n### D3: Simplicity as robustness (revised)\nException signal 在两模型上均为最优组件，其结构简单性确保了相对优势的跨模型 robustness。但 DeepSeek seed sensitivity 揭示：simplicity 确保 signal 本身 robust，但 LoRA 训练过程是否稳定收敛到正确映射取决于模型。**trace design 应匹配 deployment model 的能力下界**，且需关注 training stability（建议：多 seed 验证 + 考虑 training stabilization 技巧如 warmup、learning rate schedule）。\n\n### D4: Checkpoint selection 与 gap 报告 (revised)\n正文报告所有 seeds 的 final checkpoint 结果 + best checkpoint 结果，不 cherry-pick。DeepSeek seed42: epoch1=99.83%, epoch3=99.33%（退化 0.50pp）。DeepSeek seed123: epoch1=91.43%, epoch3=91.09%（退化 0.34pp）。两个 seed 均显示轻微 epoch 退化，但核心差异在 epoch1 起点（8.40pp gap），不是训练过程。\n\n### D5: Irreducible samples — GeneratorExit 根因分析\n3 seeds 的 2/1190 errors 完全相同（id=901, 905, 均来自 HumanEval/95 `check_dict_case`），方向一致（pass→fail false negatives）。\n\n**根因**: Python `all()` 对 generator expression 短路时丢弃未耗尽的 generator，触发 `GeneratorExit`。`GeneratorExit` 继承自 `BaseException`（非 `Exception`），是 Python 内部控制流机制而非真正错误。但 tracer 对所有 caught exceptions 统一标记 `[ERROR]`，导致 exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。\n\n**为何不可约**:\n1. **表征局限**: exception_only 条件下模型仅见异常数据，无法访问控制流、返回值或 assertion 结果。`GeneratorExit` 在此表征中与真正错误不可区分。\n2. **跨 seed 确定性**: 3 个 random seeds 产生完全相同的 errors，确认这是 data/representation 属性而非模型初始化随机性。\n3. **训练集无信号**: 整个 1190 条测试集仅这 2 条含 `GeneratorExit`，训练集中也缺乏足够的 `GeneratorExit` 良性样本供模型学习。\n4. **人类也会犯错**: 仅看 exception trace（7 行 `[ERROR]`），人类审查者在不了解 Python generator protocol 的情况下也会预测 fail。\n\n**对论文的意义**: (1) 99.83% 是 exception_only representation 在此数据集上的理论 ceiling，非 saturation artifact；(2) 揭示 tracer 设计的改进方向——区分 `BaseException` 子类（如 `GeneratorExit`, `KeyboardInterrupt`）与 `Exception` 子类（真正的程序错误）可消除此类 irreducible error；(3) 提供 concrete evidence 说明 exception_only 模型\"理解\"的是 `[ERROR]` tag 的 fault indicator 语义，而非 exception type 的 fine-grained 含义。\n\n### D6: Calibration as secondary evidence\nCalibration 数据提供独立于 accuracy 的 evidence dimension。no_trace Brier=0.1972 说明模型无 trace 时不仅预测错，且对错误预测过度自信。exception_only Brier=0.0013 说明模型在有 exception signal 时几乎完美区分确定性和不确定性。这支持 Claim 1 的 \"sufficient signal\" 论点——exception 不仅让模型预测对，还让模型 \"知道自己对\"。\n\n### D7: Early stopping for exception signal (revised — D030 epoch1 data complete)\n3-seed epoch1 完整数据：seed42 epoch1=99.83% → epoch3=99.33%（-0.50pp）；**seed456 epoch1=99.33% → epoch3=99.33%（0.00pp）**；seed123 epoch1=91.43% → epoch3=91.09%（-0.34pp）。**seed42 的 epoch1=99.83%（匹配 Qwen）是该 seed 独有的 LoRA 初始化运气，不是 DeepSeek epoch1 的通用属性。** seed456 epoch1=epoch3 说明 epoch 退化非普遍现象。核心差异仍是 LoRA 初始化（epoch1 起点差 8.40pp），不是 overfitting。Early stopping 无法挽救差的初始化（seed123）。**Implication**: (1) 报告 DeepSeek 结果时应使用 median/2-of-3 (99.33%)，不应以 seed42 epoch1=99.83% 作为 headline；(2) epoch1 peak 是 LoRA 初始化运气的副产物，不具推广性。对比: VOTA 在 DeepSeek 上 84.45% **已确认正确**（D030 关闭: confirmatory re-eval max_length=16384 → 84.45%，与原始训练评估精确一致；D030 根因是 evaluate.py v2 的 max_length=2048 eval-time 截断 bug 导致 82.6% 预测为 garbage tokens）。\n\n### D9: LoRA initialization sensitivity as secondary bottleneck [NEW — D028]\nDeepSeek exception_only seed42=99.83% vs seed123=91.43% (epoch1), 8.40pp gap。Qwen 3 seeds 完全一致。假说：exception signal 的 learnability 取决于 (1) signal 本身的结构简单性（cross-model robust）+ (2) LoRA 初始化是否落入能正确映射 exception→verdict 的 basin。Qwen-7B 可能因模型更强/LoRA landscape 更平滑而对初始化不敏感。DeepSeek-6.7B（CRUXEval-I 39% vs Qwen 56.5%）的 loss landscape 可能更 rugged，LoRA 初始化更易陷入 suboptimal basin（seed123 的 fail_recall 仅 70-72% 说明模型未学到 exception→fail 映射的关键部分）。**论文角度**: 这不是 negative result——它揭示了 trace SFT 的 practical consideration（training stability），可作为 contribution 的一部分。建议 Discussion 讨论 training stabilization 策略（warmup, lr schedule, LoRA rank 调整, multi-seed selection）。\n\n### D10: Train loss ≈ but accuracy ≠ across seeds [NEW — D029]\nDeepSeek exception_only seed456 (train_loss=0.1225) 与 seed123 (train_loss=0.122) 训练损失几乎相同，但 accuracy 差 8.2pp（99.33% vs 91.09%）。关键差异集中在 fail_recall（1.0 vs 0.705）——token-level loss 在所有 tokens 上平均，掩盖了 fail 类少数样本的 sample-level 分类能力差异。**Implication**: (1) 扩展 D1 (eval_loss vs accuracy decoupling) 到训练阶段：train_loss 同样不是 verdict task accuracy 的可靠代理指标；(2) 对 checkpoint selection 的实际建议更强：必须用 task-specific metric (accuracy/F1)，甚至 train_loss 收敛也不保证 task performance；(3) fail 类作为少数类（28.5%），其学习质量被平均 loss 稀释——这在 class-imbalanced 设置下是 general pattern，可推广到其他 verdict/detection 任务。\n\n### D11: VOTA cross-model gap: training-time trace truncation as causal factor [NEW — D030 token analysis + group_analysis]\nD030 token analysis 确认: `to_chat_text()` 保留 labels（verdict label 在训练时未被截断），但 91.7% 的 DeepSeek VOTA 训练样本的 **trace content** 从 mean 2626 tokens 被截断到 ~2048 tokens。\n\n**Group analysis 提供因果证据**: 将测试集按训练截断状态分组（推理时无截断, max_length=16384），train-truncated 组 accuracy=83.04% vs train-intact 组 accuracy=100%, Fisher exact p≈0。**截断的因果方向可以 claim**: 训练时 trace 被截断导致模型学到的信息不完整 → 推理时即使看到完整 trace 也无法正确判断。模型能力差异是残余 confound（无法完全分离）。\n\n**Implications**: (1) 论文中所有 \"right-truncation corrupts/removes the verdict label\" 措辞对 VOTA 不成立——label 完整保留，被截断的是 trace INPUT content；(2) 14.96pp gap 中截断效应有因果证据（group_analysis），模型能力差异是 residual confound；(3) exception_only 因 token 长度短（远低于 2048）不受截断影响，其跨模型对比更 clean——进一步强化 Claim 1 \"most robust component\" 叙事；(4) 论文应讨论 max_length 的影响作为 limitation/future work；(5) group_analysis 数据可作为 Table/Figure 纳入论文——展示截断的因果效应。\n\n### D8: Data duplication as representation signature\nexception_only 训练集 39.45% 重复（4720→2858 unique），测试集 48.99%（1190→607 unique），而 raw_traces 仅 1.81%（5910→5803 unique）。重复源自 exception_only 表征的 design-by-intent compactness：同一编程题的多个 passing 解执行时均无异常，exception_only 表征退化为相同的空标记。这一数据特征本身就是 Claim 3 two-tier hierarchy 的佐证——Tier 1 信号仅编码 fault presence/absence，不编码 solution-level details，因此天然高重复。Train-test input overlap = 0 排除数据泄漏。\n\n## Contingency Framing (已解决, 留存档)\n\n### Claim 1 — RESOLVED (D029: seed456=99.33% confirms \"consistently best component\")\nseed456 与 seed42 完全一致（均 99.33%），seed123 为孤立离群值。Claim 1 定稿为 \"exception events consistently best component across models; absolute performance seed-dependent on DeepSeek (2/3 seeds robust, 1 outlier from LoRA init sensitivity); relative dominance over all alternatives robust across all seeds\"。\"0pp universal gap\" 叙事已放弃，转为数据驱动的 nuanced framing。\n\n### Claim 2 — RESOLVED (D006 + D009)\nv5 full_trace 81.76%. plan_002 label-only 86.22%, gradient dilution = minor (26%). 跨模型 VOTA gap 补充证据.\n\n## 与 v1 Framing 的关键差异\n\n| 维度 | v1 | v2.9 |\n|------|----|----|\n| Headline | VOTA compression 优于 full trace | Exception events are the most effective diagnostic signal |\n| Primary claim | VOTA +24pp through fault indicator preservation | Exception signal consistently best across models; absolute performance seed-dependent on DeepSeek |\n| Claim 2 | Compression > full trace (只有 gradient dilution) | Information density primary + gradient dilution quantification + cross-model reinforcement |\n| Claim 3 Tier 1 | exception_only only | exception + assertion-point (co-Tier 1, D020) |\n| VOTA 定位 | 核心方法 — trace compression | **Fault indicator isolation** — 价值在于提取 exception, 非 generic compression |\n| Model scope | 单模型 (Qwen) | 双模型, 跨模型对比是核心贡献 |\n| DeepSeek full_trace | N/A | v1 collapsed (label truncation), v3 pending |\n| Seed robustness | 未验证 | Qwen ✅ 99.83% ± 0.00 (3 seeds); DeepSeek ⚠️ seed-dependent (91-99%, D028) |\n| Irreducible error | 未分析 | ✅ GeneratorExit 根因明确，99.83% = representation ceiling |\n| Calibration | 未验证 | ✅ 完整 ECE+Brier, ~63x/~150x gap vs no_trace |\n| Data duplication | 未分析 | ✅ exception_only ~40% 重复（representation compactness），train-test overlap = 0 |\n| Early stopping | 未讨论 | DeepSeek epoch1→epoch3 轻微退化 (0.3-0.5pp); 核心问题是 LoRA 初始化 (seed123 epoch1=91.43%), 非 overfitting |\n| Narrative arc | \"VOTA helps\" | \"Exception events are consistently best; VOTA's value is isolating them; training stability matters\" |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Ablation: 去除 VOTA 中 actual/expected 值对，只保留 assertion structure + exception\n    info。验证 VOTA 效果是 genuine behavioral understanding 还是 trivial string comparison。'\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: vota_no_ae_seed42\n  notes: 如果去 actual/expected 后 acc 仍 >80%，证明非 trivial；如果降到 ~75%(=no_trace)，则是字符串比对。决定\n    Claim 1 强度和论文 framing。\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.994\n    majority_baseline: 0.7151\n    lift: 0.279\n    n: 1190\n    pass_f1: 0.996\n    fail_f1: 0.989\n    accuracy_ci_lower: 0.989\n    accuracy_ci_upper: 0.998\n    lift_vs_notrace: 0.243\n    lift_vs_notrace_ci_lower: 0.218\n    lift_vs_notrace_ci_upper: 0.268\n    train_loss: 0.0908\n    eval_loss: 0.2215\n    wall_clock_seconds: 6397.88\n- id: plan_002\n  claim: 2\n  description: 'Ablation: full_trace + label-only loss (只对分类 token 计算 loss，mask trace\n    tokens)。验证 collapse 根因是 gradient dilution 而非数据/代码 bug。'\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: full_trace_label_only_seed42\n  notes: 如果 label-only loss 修复 collapse (acc >70%)，确认 gradient dilution 假说。如果仍 collapse，可能是\n    trace noise/length 本身就有害。\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8622\n    accuracy_ci_lower: 0.8437\n    accuracy_ci_upper: 0.8807\n    majority_baseline: 0.7151\n    lift: 0.1471\n    n: 1190\n    pass_precision: 0.8821\n    pass_recall: 0.9318\n    pass_f1: 0.9063\n    fail_precision: 0.8007\n    fail_recall: 0.6873\n    fail_f1: 0.7397\n    train_loss: 0.2505\n    eval_loss: 0.3205\n    lift_vs_notrace: 0.1109\n    lift_vs_notrace_ci_lower: 0.0849\n    lift_vs_notrace_ci_upper: 0.137\n    lift_vs_standard_fulltrace: 0.0445\n    lift_vs_standard_fulltrace_ci_lower: 0.0235\n    lift_vs_standard_fulltrace_ci_upper: 0.0655\n    lift_vs_standard_fulltrace_pvalue: 0\n- id: plan_003\n  claim: 3\n  description: 'VOTA component ablation: 分别测试 (a) 只有 actual/expected, (b) 只有 exception\n    summary, (c) 只有 loop compression, (d) 全量 VOTA。量化每个组件的贡献。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  registry_id: vota_loop_only_seed42\n  notes: '4 个 sub-conditions。registry IDs: vota_loop_only_seed42 (loop_only 85.6%),\n    vota_exception_only_seed42_v2 (exception_only 99.83%), vota_ae_only_seed42 (ae_only\n    99.92%)。plan_001 vota_no_ae_seed42 (99.4%) 覆盖 ae 冗余确认。'\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8563\n    majority_baseline: 0.7151\n    lift: 0.1412\n    n: 1190\n    pass_precision: 0.9239\n    pass_recall: 0.8707\n    pass_f1: 0.8966\n    fail_precision: 0.7165\n    fail_recall: 0.8201\n    fail_f1: 0.7648\n    accuracy_ci:\n    - 0.8353\n    - 0.8756\n    bootstrap_vs_no_trace:\n      diff: 0.105\n      ci:\n      - 0.0824\n      - 0.1286\n      significant: true\n    bootstrap_vs_vota:\n      diff: -0.1378\n      ci:\n      - -0.1571\n      - -0.1185\n      significant: true\n    bootstrap_vs_full_trace:\n      diff: 0.0387\n      ci:\n      - 0.0185\n      - 0.0597\n      significant: true\n    train_loss: 0.0718\n    wall_clock_seconds: 7425.65\n- id: plan_004\n  claim: 1\n  description: '第二模型验证: DeepSeek-Coder-6.7B 上复现 4 条件（VOTA/no_trace/full_trace/exception_only），与\n    DCSH 同模型直接对比。exception_only 跨模型验证 exception dominance。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  registry_id: deepseek_exception_only_seed42\n  notes: '4 条件: deepseek_vota_seed42 (84.45% ✅), deepseek_no_trace_seed42 (73.36%\n    ✅), deepseek_exception_only_seed42 (99.33% ✅), deepseek_full_trace_seed42_v3 (RUNNING,\n    label truncation fix). 3/4 完成, full_trace v3 待完成。'\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9933\n    majority_baseline: 0.7151\n    lift: 0.2782\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9906\n    pass_f1: 0.9953\n    fail_precision: 0.9769\n    fail_recall: 1\n    fail_f1: 0.9883\n    epoch1_checkpoint_eval:\n      accuracy: 0.9983\n      fail_recall: 1\n      fail_precision: 0.9941\n      pass_recall: 0.9976\n      conclusion: epoch1_better_by_0.50pp\n- id: plan_005\n  claim: 1\n  description: '第二任务验证: 在 DebugBench subset 上测试 exception_only/VOTA/no_trace。验证 verdict\n    task 跨任务泛化性。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps:\n  - plan_001\n  registry_id: debugbench_exception_only_seed42\n  notes: 3/3 完成。debugbench_exception_only_seed42=100.0% (426/426, Wilson CI [99.14%,100%]),\n    debugbench_vota_seed42=99.77% (1 error), debugbench_no_trace_seed42=96.71%。定位为\n    generalization validation（非 trace importance evidence，因 no_trace baseline 96.71%\n    已很高，marginal contribution 仅 3.29pp）。\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 1\n    majority_baseline: 0.5141\n    lift: 0.4859\n    n: 426\n    pass_precision: 1\n    pass_recall: 1\n    pass_f1: 1\n    fail_precision: 1\n    fail_recall: 1\n    fail_f1: 1\n    accuracy_ci_wilson:\n    - 0.9914\n    - 1\n    accuracy_ci_bootstrap:\n    - 1\n    - 1\n    train_loss: 0.2435\n    eval_loss: 0.4157\n    train_runtime_sec: 837\n- id: plan_006\n  claim: 2\n  description: 'Trace length ablation: 测试不同截断长度 (256/512/1024/no_limit) 对 full_trace\n    准确率的影响。2048tok 取消（train_sft.py 硬编码 max_length=2048，与 no_limit 等价）。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  registry_id: full_trace_256tok_seed42\n  notes: '4 点设计: 256tok=78.82% (DONE), 512tok=80.42% (DONE), 1024tok (RUNNING), no_limit=81.76%\n    (full_trace_seed42_v5)。2048tok killed（max_length=2048 硬编码使其与 no_limit 等价）。Registry\n    IDs: full_trace_256tok_seed42, full_trace_512tok_seed42, full_trace_1024tok_seed42,\n    full_trace_seed42_v5。趋势: 更多 trace 略有帮助但收益递减，且全部远低于 exception_only (99.83%)。'\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.7882\n    majority_baseline: 0.7151\n    lift: 0.0731\n    n: 1190\n    pass_precision: 0.903\n    pass_recall: 0.788\n    pass_f1: 0.842\n    fail_precision: 0.597\n    fail_recall: 0.788\n    fail_f1: 0.679\n    accuracy_ci:\n    - 0.764\n    - 0.81\n    train_loss: 0.1094\n    train_runtime_sec: 3047\n    epochs: 3\n- id: plan_007\n  claim: 3\n  description: 'Calibration analysis: ECE + reliability diagrams 对比 VOTA/no_trace/full_trace\n    的 calibration 质量。验证 trace SFT 对 verdict task 改善 calibration 的假说。'\n  priority: P2\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: calibration_analysis_seed42\n  notes: 纯 eval，不需要额外训练。用已有 checkpoint 的 logits 计算。\n  status: DONE\n  conclusion: success\n  metrics:\n    no_trace:\n      ece: 0.171476\n      mce: 0.475643\n      brier_score: 0.197152\n      accuracy: 0.751261\n      n_samples: 1190\n    full_trace:\n      ece: 0.095817\n      mce: 0.249061\n      brier_score: 0.143924\n      accuracy: 0.817647\n      n_samples: 1190\n    label_only:\n      ece: 0.110686\n      mce: 0.417124\n      brier_score: 0.120144\n      accuracy: 0.862185\n      n_samples: 1190\n    loop_only:\n      ece: 0.083085\n      mce: 0.183406\n      brier_score: 0.118335\n      accuracy: 0.856303\n      n_samples: 1190\n    ae_only:\n      ece: 0.000415\n      mce: 0.000415\n      brier_score: 0.000847\n      accuracy: 0.99916\n      n_samples: 1190\n    exception_only:\n      ece: 0.002717\n      mce: 0.835484\n      brier_score: 0.001311\n      accuracy: 0.998319\n      n_samples: 1190\n    vota:\n      ece: 0.00541\n      mce: 0.622459\n      brier_score: 0.005234\n      accuracy: 0.994118\n      n_samples: 1190\n- id: plan_008\n  claim: 1\n  description: 'Seed robustness: 3 random seeds (42/123/456) 验证 VOTA 结果稳定性。McNemar\n    test + bootstrap CI。'\n  priority: P2\n  gpu_budget_hours: 6\n  deps:\n  - plan_001\n  registry_id: exception_only_seed456\n  notes: 'Seed robustness 完成。Qwen exception_only: 99.83% ± 0.00 (seeds 42/123/456,\n    irreducible 2/1190). Qwen VOTA: seed42=99.41%, seed456=99.08% (Δ<0.4pp). DeepSeek\n    exception_only: seed42/456=99.33%, seed123=91.09% (LoRA outlier). Registry IDs:\n    exception_only_seed123, exception_only_seed456, vota_seed456_v2, deepseek_exception_only_seed42/123/456.'\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    accuracy_ci:\n    - 0.9958\n    - 1\n    majority_baseline: 0.7151\n    lift: 0.2832\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9976\n    pass_f1: 0.9988\n    fail_precision: 0.9941\n    fail_recall: 1\n    fail_f1: 0.9971\n    vs_seed42:\n      seed42_accuracy: 0.9983\n      seed456_accuracy: 0.9983\n      diff: 0\n      note: identical accuracy to 4 decimal places; no predictions.jsonl for paired\n        bootstrap\n    train_loss: 0.1087\n    eval_loss: 0.4629\n    train_runtime_sec: 4541\n    epochs: 3\n- id: plan_mvp_vota\n  claim: 1\n  description: 'MVP: VOTA trace SFT for test verdict prediction'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: vota_seed42_v4\n  notes: 完成。95.63% accuracy, +20.5pp over baseline.\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9563\n    majority_baseline: 0.7151\n    lift: 0.2412\n    n: 1190\n    pass_precision: 0.944\n    pass_recall: 0.998\n    pass_f1: 0.97\n    fail_precision: 0.993\n    fail_recall: 0.853\n    fail_f1: 0.917\n    lift_vs_notrace: 0.205\n    lift_vs_notrace_ci_lower: 0.177\n    lift_vs_notrace_ci_upper: 0.234\n    train_loss: 0.046\n    eval_loss: 0.0842\n- id: plan_mvp_notrace\n  claim: 1\n  description: 'MVP: No-trace baseline for test verdict prediction'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: no_trace_seed42_v4\n  notes: 完成。75.13% accuracy (majority baseline 71.51%).\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7513\n    majority_baseline: 0.7151\n    lift: 0.0361\n    pass_precision: 0.8776\n    pass_recall: 0.7579\n    pass_f1: 0.8134\n    fail_precision: 0.5473\n    fail_recall: 0.7345\n    fail_f1: 0.6272\n    train_loss: 0.18\n    eval_loss: 0.6454\n    eval_mean_token_accuracy: 0.8897\n- id: plan_mvp_fulltrace\n  claim: 2\n  description: 'MVP: Full execution trace SFT for test verdict prediction'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: full_trace_seed42_v2\n  notes: 完成。28.49% accuracy, model collapse (100% predict fail).\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.284\n    majority_baseline: 0.7151\n    lift: -0.4311\n    n: 1190\n    pass_precision: 0.923\n    pass_recall: 0.085\n    pass_f1: 0.155\n    fail_precision: 0.445\n    fail_recall: 0.785\n    fail_f1: 0.568\n    train_loss: 0.0373\n    eval_loss: 0.082\n    eval_mean_token_accuracy: 0.984\n\n\n## registry (completed experiments)\n\n- exp_id: no_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: vota_seed42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: no_trace_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: vota_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: no_trace_seed42_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    train_loss: 0.18\n    eval_loss: 0.645\n    eval_mean_token_accuracy: 0.89\n    accuracy: 0.7513\n    majority_baseline: 0.7151\n    lift: 0.0361\n    pass_precision: 0.8776\n    pass_recall: 0.7579\n    pass_f1: 0.8134\n    fail_precision: 0.5473\n    fail_recall: 0.7345\n    fail_f1: 0.6272\n- exp_id: vota_seed42_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    train_loss: 0.046\n    eval_loss: 0.085\n    eval_mean_token_accuracy: 0.983\n    accuracy: 0.992\n    majority_baseline: 0.7151\n    lift: 0.276\n    pass_precision: 0.99\n    pass_recall: 0.99\n    pass_f1: 0.99\n    fail_precision: 0.99\n    fail_recall: 0.99\n    fail_f1: 0.99\n- exp_id: full_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    train_loss: 0.037\n    eval_loss: 0.084\n    eval_mean_token_accuracy: 0.984\n    accuracy: 0.284\n    majority_baseline: 0.7151\n    lift: -0.431\n    pass_precision: 0.88\n    pass_recall: 0.08\n    pass_f1: 0.16\n    fail_precision: 0.31\n    fail_recall: 0.97\n    fail_f1: 0.57\n- exp_id: no_trace_seed42_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7513\n    majority_baseline: 0.7151\n    lift: 0.0361\n    pass_precision: 0.8776\n    pass_recall: 0.7579\n    pass_f1: 0.8134\n    fail_precision: 0.5473\n    fail_recall: 0.7345\n    fail_f1: 0.6272\n    train_loss: 0.18\n    eval_loss: 0.6454\n    eval_mean_token_accuracy: 0.8897\n- exp_id: vota_seed42_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9563\n    majority_baseline: 0.7151\n    lift: 0.2412\n    n: 1190\n    pass_precision: 0.944\n    pass_recall: 0.998\n    pass_f1: 0.97\n    fail_precision: 0.993\n    fail_recall: 0.853\n    fail_f1: 0.917\n    lift_vs_notrace: 0.205\n    lift_vs_notrace_ci_lower: 0.177\n    lift_vs_notrace_ci_upper: 0.234\n    train_loss: 0.046\n    eval_loss: 0.0842\n- exp_id: full_trace_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.284\n    majority_baseline: 0.7151\n    lift: -0.4311\n    n: 1190\n    pass_precision: 0.923\n    pass_recall: 0.085\n    pass_f1: 0.155\n    fail_precision: 0.445\n    fail_recall: 0.785\n    fail_f1: 0.568\n    train_loss: 0.0373\n    eval_loss: 0.082\n    eval_mean_token_accuracy: 0.984\n- exp_id: full_trace_seed42_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8176\n    majority_baseline: 0.7151\n    lift: 0.1025\n    n: 1190\n    pass_precision: 0.8774\n    pass_recall: 0.866\n    pass_f1: 0.8717\n    fail_precision: 0.6743\n    fail_recall: 0.6962\n    fail_f1: 0.6851\n    accuracy_ci_lower: 0.797\n    accuracy_ci_upper: 0.839\n    lift_vs_notrace: 0.0664\n    lift_vs_notrace_ci_lower: 0.0437\n    lift_vs_notrace_ci_upper: 0.0899\n    train_loss: 0.05\n    eval_loss: 0.0867\n    wall_clock_seconds: 7852\n    epoch_level:\n      epoch1_accuracy: 0.8303\n      epoch2_accuracy: 0.763\n      final_accuracy: 0.8176\n      trend: non_monotonic_epoch1_best_epoch2_collapse\n- exp_id: vota_seed42_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9941\n    majority_baseline: 0.7151\n    lift: 0.279\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9882\n    pass_f1: 0.9941\n    fail_precision: 0.9714\n    fail_recall: 1\n    fail_f1: 0.9855\n    lift_vs_notrace: 0.2428\n    lift_vs_notrace_ci_lower: 0.2185\n    lift_vs_notrace_ci_upper: 0.2681\n    accuracy_ci_lower: 0.9882\n    accuracy_ci_upper: 0.9983\n    train_loss: 0.05\n    eval_loss: 0.0867\n    eval_mean_token_accuracy: 0.9828\n    wall_clock_seconds: 8443\n    epoch_level:\n      epoch1_accuracy: 0.9933\n      epoch2_accuracy: 0.9941\n      final_accuracy: 0.9941\n      trend: monotonic_increasing_then_stable\n- exp_id: no_trace_seed42_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7513\n    accuracy_ci_lower: 0.7277\n    accuracy_ci_upper: 0.7748\n    majority_baseline: 0.7151\n    lift: 0.0361\n    lift_ci_lower: 0.0042\n    lift_ci_upper: 0.0706\n    n: 1190\n    pass_precision: 0.8776\n    pass_recall: 0.7579\n    pass_f1: 0.8134\n    fail_precision: 0.5473\n    fail_recall: 0.7345\n    fail_f1: 0.6272\n    epoch_level:\n      epoch1_accuracy: 0.7429\n      epoch2_accuracy: 0.763\n      final_accuracy: 0.7513\n      trend: non_monotonic_epoch2_best\n- exp_id: full_trace_label_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8622\n    accuracy_ci_lower: 0.8437\n    accuracy_ci_upper: 0.8807\n    majority_baseline: 0.7151\n    lift: 0.1471\n    n: 1190\n    pass_precision: 0.8821\n    pass_recall: 0.9318\n    pass_f1: 0.9063\n    fail_precision: 0.8007\n    fail_recall: 0.6873\n    fail_f1: 0.7397\n    train_loss: 0.2505\n    eval_loss: 0.3205\n    lift_vs_notrace: 0.1109\n    lift_vs_notrace_ci_lower: 0.0849\n    lift_vs_notrace_ci_upper: 0.137\n    lift_vs_standard_fulltrace: 0.0445\n    lift_vs_standard_fulltrace_ci_lower: 0.0235\n    lift_vs_standard_fulltrace_ci_upper: 0.0655\n    lift_vs_standard_fulltrace_pvalue: 0\n- exp_id: vota_no_ae_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.994\n    majority_baseline: 0.7151\n    lift: 0.279\n    n: 1190\n    pass_f1: 0.996\n    fail_f1: 0.989\n    accuracy_ci_lower: 0.989\n    accuracy_ci_upper: 0.998\n    lift_vs_notrace: 0.243\n    lift_vs_notrace_ci_lower: 0.218\n    lift_vs_notrace_ci_upper: 0.268\n    train_loss: 0.0908\n    eval_loss: 0.2215\n    wall_clock_seconds: 6397.88\n- exp_id: vota_ae_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9992\n    accuracy_ci:\n    - 0.9975\n    - 1\n    bootstrap_pairwise:\n      ae_only_vs_no_trace:\n        diff: 0.2479\n        ci:\n        - 0.2235\n        - 0.2731\n        p_value: 0\n        significant: true\n      ae_only_vs_exception_only:\n        diff: 0.0008\n        ci:\n        - -0.0017\n        - 0.0034\n        p_value: 0.8002\n        significant: false\n      ae_only_vs_vota:\n        diff: 0.005\n        ci:\n        - 0.0017\n        - 0.0092\n        p_value: 0.0046\n        significant: true\n    config:\n      n_bootstrap: 10000\n      seed: 42\n      method: paired_bootstrap\n- exp_id: vota_exception_only_seed42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: vota_loop_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8563\n    majority_baseline: 0.7151\n    lift: 0.1412\n    n: 1190\n    pass_precision: 0.9239\n    pass_recall: 0.8707\n    pass_f1: 0.8966\n    fail_precision: 0.7165\n    fail_recall: 0.8201\n    fail_f1: 0.7648\n    accuracy_ci:\n    - 0.8353\n    - 0.8756\n    bootstrap_vs_no_trace:\n      diff: 0.105\n      ci:\n      - 0.0824\n      - 0.1286\n      significant: true\n    bootstrap_vs_vota:\n      diff: -0.1378\n      ci:\n      - -0.1571\n      - -0.1185\n      significant: true\n    bootstrap_vs_full_trace:\n      diff: 0.0387\n      ci:\n      - 0.0185\n      - 0.0597\n      significant: true\n    train_loss: 0.0718\n    wall_clock_seconds: 7425.65\n- exp_id: vota_exception_only_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    majority_baseline: 0.7151\n    lift: 0.2832\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.998\n    pass_f1: 0.999\n    fail_precision: 0.994\n    fail_recall: 1\n    fail_f1: 0.997\n    lift_vs_notrace: 0.2471\n    lift_vs_notrace_ci_lower: 0.2227\n    lift_vs_notrace_ci_upper: 0.2714\n    lift_vs_fulltrace: 0.1807\n    lift_vs_fulltrace_ci_lower: 0.1588\n    lift_vs_fulltrace_ci_upper: 0.2034\n    lift_vs_vota: 0.0067\n    lift_vs_vota_ci_lower: 0.0017\n    lift_vs_vota_ci_upper: 0.0126\n    lift_vs_vota_pvalue: 0.01\n- exp_id: deepseek_vota_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8445\n    majority_baseline: 0.7151\n    lift: 0.1294\n    accuracy_ci:\n    - 0.826\n    - 0.864\n    pass_precision: 0.821\n    pass_recall: 1\n    pass_f1: 0.902\n    fail_precision: 1\n    fail_recall: 0.454\n    fail_f1: 0.625\n    eval_loss_epoch1: 0.0679\n    eval_loss_epoch2: 0.095\n    eval_loss_epoch3: 0.1121\n    final_train_loss: 0.0522\n    epoch1_checkpoint_eval:\n      accuracy: 0.7815\n      accuracy_ci:\n      - 0.76\n      - 0.803\n      fail_recall: 0.233\n      fail_precision: 1\n      pass_recall: 1\n      pass_precision: 0.766\n      fail_f1: 0.378\n      pass_f1: 0.867\n      conclusion: epoch3_final_is_better\n    reeval_with_fixed_script:\n      accuracy: 0.16\n      accuracy_ci:\n      - 0.139\n      - 0.18\n      fail_f1: 0.61\n      fail_precision: 0.9\n      fail_recall: 0.47\n      pass_f1: 0.07\n      pass_precision: 1\n      pass_recall: 0.04\n      note: 'CATASTROPHIC: re-eval with corrected evaluate.py shows 16% (vs original\n        84.45%). Model predicts fail for almost everything. Previous 84.45% may have\n        been from buggy eval. NEEDS INVESTIGATION.'\n    group_analysis:\n      train_truncated:\n        n: 1091\n        accuracy: 0.8304\n        ci_95:\n        - 0.8075\n        - 0.8524\n        correct: 906\n        incorrect: 185\n        pass_accuracy: 1\n        pass_n: 822\n        fail_accuracy: 0.3123\n        fail_n: 269\n      train_intact:\n        n: 99\n        accuracy: 1\n        ci_95:\n        - 1\n        - 1\n        correct: 99\n        incorrect: 0\n        pass_accuracy: 1\n        pass_n: 29\n        fail_accuracy: 1\n        fail_n: 70\n      fisher_exact:\n        odds_ratio: 0\n        p_value: 0\n      overall_accuracy: 0.8445\n      max_length: 2048\n      note: 'Grouped by whether training sample content exceeded token budget (DeepSeek\n        tokenizer, max_length=2048). Inference used full-length input (no truncation).\n        All 185 errors from truncated group''s fail class (fail_recall=31.2%). Intact\n        group: 100% accuracy.'\n- exp_id: deepseek_no_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.7336\n    majority_baseline: 0.7151\n    lift: 0.0185\n    n: 1190\n    pass_precision: 0.817\n    pass_recall: 0.808\n    pass_f1: 0.813\n    fail_precision: 0.532\n    fail_recall: 0.546\n    fail_f1: 0.539\n    accuracy_ci:\n    - 0.708\n    - 0.757\n    lift_ci:\n    - -0.009\n    - 0.046\n- exp_id: deepseek_full_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy_no_truncation: 0.2849\n    accuracy_with_truncation_fix: 0.1059\n    accuracy_with_truncation_fix_ci:\n    - 0.089\n    - 0.123\n    majority_baseline: 0.7151\n    n: 1190\n    note: 'Both evals show model failure. No-truncation: all predict fail. With-truncation:\n      garbage tokens. LoRA training itself failed due to label truncation during training.'\n- exp_id: deepseek_exception_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9933\n    majority_baseline: 0.7151\n    lift: 0.2782\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9906\n    pass_f1: 0.9953\n    fail_precision: 0.9769\n    fail_recall: 1\n    fail_f1: 0.9883\n    epoch1_checkpoint_eval:\n      accuracy: 0.9983\n      fail_recall: 1\n      fail_precision: 0.9941\n      pass_recall: 0.9976\n      conclusion: epoch1_better_by_0.50pp\n- exp_id: calibration_analysis_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    no_trace:\n      ece: 0.171476\n      mce: 0.475643\n      brier_score: 0.197152\n      accuracy: 0.751261\n      n_samples: 1190\n    full_trace:\n      ece: 0.095817\n      mce: 0.249061\n      brier_score: 0.143924\n      accuracy: 0.817647\n      n_samples: 1190\n    label_only:\n      ece: 0.110686\n      mce: 0.417124\n      brier_score: 0.120144\n      accuracy: 0.862185\n      n_samples: 1190\n    loop_only:\n      ece: 0.083085\n      mce: 0.183406\n      brier_score: 0.118335\n      accuracy: 0.856303\n      n_samples: 1190\n    ae_only:\n      ece: 0.000415\n      mce: 0.000415\n      brier_score: 0.000847\n      accuracy: 0.99916\n      n_samples: 1190\n    exception_only:\n      ece: 0.002717\n      mce: 0.835484\n      brier_score: 0.001311\n      accuracy: 0.998319\n      n_samples: 1190\n    vota:\n      ece: 0.00541\n      mce: 0.622459\n      brier_score: 0.005234\n      accuracy: 0.994118\n      n_samples: 1190\n- exp_id: vota_seed123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: vota_seed456\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exception_only_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    accuracy_ci:\n    - 0.9958\n    - 1\n    majority_baseline: 0.7151\n    lift: 0.2832\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9976\n    pass_f1: 0.9988\n    fail_precision: 0.9941\n    fail_recall: 1\n    fail_f1: 0.9971\n    train_loss: 0.1096\n    train_runtime_sec: 7507\n    epochs: 3\n    seed_comparison:\n      seed42_accuracy: 0.9983\n      seed456_accuracy: 0.9983\n      seed123_accuracy: 0.9983\n      max_diff: 0\n      note: identical accuracy to 4 decimal places across all 3 seeds (42/456/123);\n        each has exactly 2/1190 errors; exception_only fully seed-robust\n- exp_id: exception_only_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    accuracy_ci:\n    - 0.9958\n    - 1\n    majority_baseline: 0.7151\n    lift: 0.2832\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9976\n    pass_f1: 0.9988\n    fail_precision: 0.9941\n    fail_recall: 1\n    fail_f1: 0.9971\n    vs_seed42:\n      seed42_accuracy: 0.9983\n      seed456_accuracy: 0.9983\n      diff: 0\n      note: identical accuracy to 4 decimal places; no predictions.jsonl for paired\n        bootstrap\n    train_loss: 0.1087\n    eval_loss: 0.4629\n    train_runtime_sec: 4541\n    epochs: 3\n- exp_id: deepseek_exception_only_seed123\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.9109\n    pass_precision: 1\n    pass_recall: 0.993\n    pass_f1: 0.996\n    fail_precision: 0.976\n    fail_recall: 0.705\n    fail_f1: 0.818\n    ci_95:\n    - 0.894\n    - 0.926\n    train_loss: 0.122\n    train_runtime_sec: 6384\n- exp_id: deepseek_full_trace_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: vota_seed456_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9908\n    pass_precision: 1\n    pass_recall: 0.987\n    pass_f1: 0.993\n    fail_precision: 0.969\n    fail_recall: 1\n    fail_f1: 0.984\n    ci_95:\n    - 0.985\n    - 0.996\n- exp_id: deepseek_full_trace_seed42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7916\n    majority_baseline: 0.7151\n    lift: 0.0765\n    n: 1190\n    pass_precision: 0.857\n    pass_recall: 0.851\n    pass_f1: 0.854\n    fail_precision: 0.632\n    fail_recall: 0.643\n    fail_f1: 0.637\n    accuracy_ci:\n    - 0.768\n    - 0.813\n    train_loss: 0.0547\n    train_runtime_seconds: 8891\n    epochs: 3\n    reeval_discrepancy:\n      reeval_accuracy: 0.285\n      reeval_note: 'RESOLVED: 28.5% was caused by eval max_length=16384 (OOD). Re-eval\n        with max_length=2048 reproduces 79.16%. predictions.jsonl updated to maxlen2048\n        results.'\n      status: RESOLVED\n- exp_id: deepseek_exception_only_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9933\n    majority_baseline: 0.7151\n    lift: 0.2782\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9906\n    pass_f1: 0.9953\n    fail_precision: 0.9769\n    fail_recall: 1\n    fail_f1: 0.9883\n    accuracy_ci:\n    - 0.9882\n    - 0.9975\n    train_loss: 0.1225\n    eval_loss: 0.4824\n    train_runtime_sec: 6246\n    seed_comparison:\n      seed42_accuracy: 0.9933\n      seed456_accuracy: 0.9933\n      seed123_accuracy: 0.9109\n      note: seed42 and seed456 identical (99.33%); seed123 outlier (91.09%). 2/3 seeds\n        robust.\n    epoch1_checkpoint_eval:\n      accuracy: 0.993\n      accuracy_ci:\n      - 0.988\n      - 0.997\n      fail_f1: 0.99\n      fail_precision: 0.98\n      fail_recall: 1\n      pass_f1: 1\n      pass_precision: 1\n      pass_recall: 0.99\n      conclusion: epoch1 (99.3%) ≈ epoch3 (99.33%), 1 epoch convergence confirmed\n- exp_id: full_trace_256tok_seed42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.7882\n    majority_baseline: 0.7151\n    lift: 0.0731\n    n: 1190\n    pass_precision: 0.903\n    pass_recall: 0.788\n    pass_f1: 0.842\n    fail_precision: 0.597\n    fail_recall: 0.788\n    fail_f1: 0.679\n    accuracy_ci:\n    - 0.764\n    - 0.81\n    train_loss: 0.1094\n    train_runtime_sec: 3047\n    epochs: 3\n- exp_id: full_trace_512tok_seed42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.8042\n    majority_baseline: 0.7151\n    lift: 0.0891\n    pass_precision: 0.8705\n    pass_recall: 0.8531\n    pass_f1: 0.8617\n    fail_precision: 0.6489\n    fail_recall: 0.6814\n    fail_f1: 0.6647\n    n: 1190\n    accuracy_ci:\n    - 0.7815\n    - 0.8261\n- exp_id: full_trace_1024tok_seed42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.7723\n    majority_baseline: 0.7151\n    lift: 0.0571\n    n: 1190\n    accuracy_ci:\n    - 0.7487\n    - 0.7958\n    pass_precision: 0.9006\n    pass_recall: 0.7662\n    pass_f1: 0.8279\n    fail_precision: 0.573\n    fail_recall: 0.7876\n    fail_f1: 0.6634\n    train_loss: 0.0634\n    train_runtime_sec: 5553\n    epochs: 3\n- exp_id: full_trace_2048tok_seed42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: debugbench_exception_bug_fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: debugbench_exception_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 1\n    majority_baseline: 0.5141\n    lift: 0.4859\n    n: 426\n    pass_precision: 1\n    pass_recall: 1\n    pass_f1: 1\n    fail_precision: 1\n    fail_recall: 1\n    fail_f1: 1\n    accuracy_ci_wilson:\n    - 0.9914\n    - 1\n    accuracy_ci_bootstrap:\n    - 1\n    - 1\n    train_loss: 0.2435\n    eval_loss: 0.4157\n    train_runtime_sec: 837\n- exp_id: debugbench_no_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9671\n    majority_baseline: 0.5141\n    lift: 0.4531\n    pass_precision: 1\n    pass_recall: 0.936\n    pass_f1: 0.967\n    fail_precision: 0.937\n    fail_recall: 1\n    fail_f1: 0.967\n    accuracy_ci:\n    - 0.948\n    - 0.984\n    train_loss: 0.249\n    eval_loss: 0.532\n- exp_id: debugbench_vota_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9977\n    majority_baseline: 0.5141\n    lift: 0.4836\n    n: 426\n    pass_precision: 1\n    pass_recall: 1\n    pass_f1: 1\n    fail_precision: 1\n    fail_recall: 1\n    fail_f1: 1\n    accuracy_ci:\n    - 0.993\n    - 1\n    train_loss: 0.098\n    eval_loss: 0.1179\n    eval_mean_token_accuracy: 0.9737\n    errors: 1\n- exp_id: eval_missing_predictions_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: eval_missing_predictions_batch_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: ae_only_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9908\n    n: 1190\n    pass_recall: 0.987\n    fail_recall: 1\n    majority_baseline: 0.7151\n    lift: 0.2757\n- exp_id: ae_only_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9992\n    n: 1190\n    majority_baseline: 0.7151\n    lift: 0.2841\n    seed_comparison:\n      seed42_accuracy: 0.9992\n      seed123_accuracy: 0.9908\n      seed456_accuracy: 0.9992\n      mean_accuracy: 0.9964\n      std: 0.0049\n      note: 2/3 seeds = 99.92%, seed123 = 99.08%. Mean = 99.64% ± 0.49\n- exp_id: regex_baseline_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    regex_B1_ERROR_presence: 0.9345\n    regex_B2_Traceback: 0.7151\n    regex_B3_any_keyword: 0.9345\n    regex_B4_exception_type: 0.9361\n    regex_B5_format_marker: 0.9933\n    regex_B6_error_count_ge2: 0.9202\n    sft_exception_only: 0.9983\n    best_regex_gap_vs_sft: -0.0622\n    B5_mcnemar_p: 0.041\n    n: 1190\n- exp_id: label_only_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8706\n    n: 1190\n    pass_recall: 0.974\n    fail_recall: 0.611\n    pass_f1: 0.915\n    fail_f1: 0.729\n- exp_id: label_only_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.859\n    n: 1190\n    pass_recall: 0.938\n    fail_recall: 0.661\n    pass_f1: 0.905\n    fail_f1: 0.727\n- exp_id: exception_only_nomarker_seed42\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: loop_only_seed123\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: loop_only_seed456\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: exception_only_nomarker_seed123\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: exception_only_nomarker_seed456\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen1.5b_exception_only_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen1.5b_no_trace_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen1.5b_vota_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen1.5b_full_trace_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: codellama_exception_only_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: codellama_no_trace_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: codellama_vota_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: codellama13b_exception_only_seed42\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: codellama13b_no_trace_seed42\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: codellama13b_vota_seed42\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen15b_no_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6731\n    n: 1190\n    pass_f1: 0.7527\n    fail_f1: 0.518\n    lift_over_majority: -0.042\n    training_time_sec: 851\n- exp_id: qwen15b_vota_seed42\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen15b_full_trace_seed42\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen15b_exception_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    accuracy_ci_lower: 0.9958\n    accuracy_ci_upper: 1\n    majority_baseline: 0.7151\n    lift: 0.283\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9976\n    pass_f1: 0.9988\n    fail_precision: 0.9941\n    fail_recall: 1\n    fail_f1: 0.9971\n    train_loss: 0.1347\n    eval_loss: 0.5761\n    wall_clock_seconds: 1762\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T10:56:17.016Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T10:56:17.016Z",
  "sessionId": "f7665a3e-5d5c-49f9-8d35-6afa1c42cf9b"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T10:56:17.038Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：所有 pending experiments 一致强化 exception dominance；第三模型 Qwen-1.5B 完整复现 hierarchy；三模型 × 跨规模叙事 → EMNLP main
核心假设：['Qwen-1.5B VOTA 显著低于 exception_only (99.83%)，复现 7B 上 exception > VOTA 的 gap pattern', 'nomarker ablation 显示 [ERROR] 标记贡献 ≥2pp，确认 fault indicator marker 不是 trivial formatting 而是 learned signal 的关键锚点', 'loop_only seed123/456 稳定在 83-88%（与 seed42 的 85.63% 一致），Tier 2 鲁棒性确认', 'Qwen-1.5B exception_only=99.83% 已锁定 — 1.5B 与 7B 完全一致，scale-invariant 证据极强', '3 模型 (Qwen-7B, DeepSeek-6.7B, Qwen-1.5B) 含 5x 参数量跨度 + architecture diversity，universality claim 从 N=2 升至 N=3']
关键指标范围：{'qwen15b_vota_accuracy': [85.0, 95.0], 'nomarker_accuracy_drop_vs_marker': [2.0, 7.0], 'loop_only_3seed_std_pp': [0.0, 2.0], 'effective_model_count': [3, 3], 'models_where_exception_gt_vota': [3, 3], 'deepseek_exception_only_median': [99.33, 99.33], 'qwen7b_exception_only': [99.83, 99.83]}
叙事方向：原始 framing 完全成立，Claims 1-3 无需调整。 Headline: "Exception events are the minimal sufficient diagnostic signal — validated across 3 models spanning 1.5B to 7B parameters." Qwen-1.5B 提供三重价值: (1) exception_only 99.83% scale-invariant 确认信号 simplicity; (2) VOTA gap 复现确认 Tier 2 的 model-capability dependence; (3) 1.5B 的 no_trace=67.31% vs exception_only=99.83% (+32.5pp) 是全文最大 lift， 强化 "越弱的模型越依赖 exception signal" 叙事。 nomarker ablation 作为 fine-grained mechanism evidence 纳入 analysis section。 EMNLP main 直投，findings 不需要作 fallback。


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
  status: QUEUED
  conclusion: ''
  metrics: {}
- exp_id: loop_only_seed123
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: loop_only_seed456
  name: ''
  status: QUEUED
  conclusion: ''
  metrics: {}
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
  status: QUEUED
  conclusion: ''
  metrics: {}
- exp_id: codellama13b_no_trace_seed42
  name: ''
  status: QUEUED
  conclusion: ''
  metrics: {}
- exp_id: codellama13b_vota_seed42
  name: ''
  status: QUEUED
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
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: qwen15b_full_trace_seed42
  name: ''
  status: QUEUED
  conclusion: ''
  metrics: {}
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
  "promptId": "02d821e1-c723-4de5-a84c-e5e4c2b8ca80",
  "type": "user",
  "uuid": "d8b46108-a9d5-47de-a808-f83298a43557",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4",
  "sessionId": "f7665a3e-5d5c-49f9-8d35-6afa1c42cf9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T10:56:17.036Z_

```json
{
  "parentUuid": "d8b46108-a9d5-47de-a808-f83298a43557",
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
  "uuid": "cf0b8529-14d9-410a-8766-75f2f4c9085c",
  "timestamp": "2026-05-16T10:56:17.036Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4",
  "sessionId": "f7665a3e-5d5c-49f9-8d35-6afa1c42cf9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T10:56:17.036Z_

```json
{
  "parentUuid": "cf0b8529-14d9-410a-8766-75f2f4c9085c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2ce2e606-7b79-4af3-86fd-45ecc4fb758e",
  "timestamp": "2026-05-16T10:56:17.036Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4",
  "sessionId": "f7665a3e-5d5c-49f9-8d35-6afa1c42cf9b",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有 pending experiments 一致强化 exception dominance；第三模型 Qwen-1.5B 完整复现 hierarchy；三模型 × 跨规模叙事 → EMNLP main 核心假设：['Qwen-1.5B VOTA 显著低于 exception_only (99.83%)，复…",
  "leafUuid": "2ce2e606-7b79-4af3-86fd-45ecc4fb758e",
  "sessionId": "f7665a3e-5d5c-49f9-8d35-6afa1c42cf9b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Trace verdict prediction: exception signals outperform rich traces",
  "sessionId": "f7665a3e-5d5c-49f9-8d35-6afa1c42cf9b"
}
```

---

### Assistant

_source line 8 · 2026-05-16T10:59:28.451Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each pending/planned experiment in the experiment_plan, based on the "best" tier definition. Let me identify the pending experiments from the registry:

1. `exception_only_nomarker_seed42` - QUEUED
2. `loop_only_seed123` - RUNNING
3. `loop_only_seed456` - QUEUED


4. `exception_only_nomarker_seed123` - QUEUED
5. `exception_only_nomarker_seed456` - QUEUED
6. `qwen15b_vota_seed42` - RUNNING
7. `qwen15b_full_trace_seed42` - QUEUED
8. `codellama13b_exception_only_seed42` - QUEUED
9. `codellama13b_no_trace_seed42` - QUEUED
10. `codellama13b_vota_seed42` - QUEUED

I need to re-read the instructions more carefully—the user is asking me to expand detailed predictions for each planned experiment in the experiment_plan based on the "best" tier definition.

Looking at the experiment_plan, all experiments show status: DONE, but the registry shows several pending ones. Let me focus on the registry's pending experiments instead, which include the queued and running ones across different model configurations and trace strategies.

I can see there are also some killed experiments that were replaced by newer versions - the older qwen1.5b variants were superseded by their qwen15b counterparts. The key pending experiments I need to track predictions for are the ones still in RUNNING or QUEUED status across the different model and strategy combinations.

Looking at the best tier definition, the core hypotheses center on comparing VOTA performance across model sizes, measuring the impact of the [ERROR] marker through ablation, confirming loop_only stability across seeds, and validating that exception_only consistently outperforms VOTA. The expected metric ranges give me concrete targets to evaluate against.

For qwen15b_vota_seed42, I'm expecting around 90% accuracy - the 1.5B model's weaker execution reasoning means VOTA's loop compression components won't perform as well as on the 7B, but the exception signal should still provide meaningful lift over the no_trace baseline. This would confirm the pattern where exception_only (99.83%) > VOTA, showing that VOTA's more complex components are capability-dependent.

For qwen15b_full_trace_seed42, I'm estimating somewhere in the 72-78% range - the 1.5B model struggles more with extracting signal from noisy full traces compared to the 7B, and context length constraints mean traces get truncated, but the exception information embedded in traces should still help relative to no_trace.

The loop_only seeds should cluster tightly around 84-87%, staying within the 2pp standard deviation target - this is Tier 2 signal with moderate complexity, so while it's weaker than exception_only, the 1.5B model should handle it consistently across different random seeds.

For the nomarker ablation across all three seeds, I'm expecting a 2-7pp accuracy drop compared to the marker version's 99.83% - the [ERROR] marker acts as a learned fault indicator that the model can anchor to, and removing it forces more nuanced text understanding of exception types and messages alone.

Now I'm thinking through the CodeLlama-13B experiments - these sit outside the core 3-model setup (Qwen-7B, DeepSeek-6.7B, Qwen-1.5B) that defines the best tier, but they're queued as pending experiments that should still demonstrate exception dominance if they complete in time.

For the Qwen-1.5B VOTA experiment, I'm expecting around 90% accuracy because the smaller model lacks the execution reasoning capability to properly leverage the loop compression signals in VOTA. On Qwen-7B, VOTA hits 99.41% because the model can handle those Tier 2 signals effectively, but on 1.5B those same signals become noise, dragging performance down significantly. This should show exception_only substantially outperforming VOTA, mirroring the pattern I see with DeepSeek where weaker models don't benefit as much from complex trace representations.

Now I'm thinking through the full_trace results for 1.5B. Since the smaller model struggles with noisy information, full_trace should underperform compared to exception_only, similar to how Qwen-7B's full_trace (81.76%) only gains 6.6pp over no_trace (75.13%).

For the loop_only variants, I'm seeing consistent performance across seeds with minimal variance—seed42 at 85.63%, seed123 around 84.5%, and seed456 around 86%, averaging about 85.4% with a standard deviation under 1pp.

For exception_only without the marker, I expect a meaningful drop from the 99.83% baseline—probably in the 2-7pp range—so around 96.5% for seed42 and 96% for seed123.

The marker appears to be a learned signal the model relies on to map exceptions to failures; without it, the model has to parse exception types and messages directly, which is more error-prone and explains the 3pp performance hit.

CodeLlama-13B is larger than the other models tested, so I'd expect exception_only to stay high around 99.5-99.8%, no_trace to land similarly to the 7B models around 73-76%, and VOTA performance probably in the 90-95% range depending on its execution reasoning capability. Though I should note these CodeLlama experiments are supplementary since the best tier explicitly specifies three models, so I'll include them as bonus results rather than core predictions.

Looking back at the experiment_plan, all those experiments are marked DONE, but the registry shows pending experiments that haven't completed yet. I need to generate predictions for those instead: the exception_only_nomarker variants across different seeds, the loop_only experiments, and the CodeLlama and Qwen-15B runs that are still queued or running.

For Qwen-1.5B VOTA specifically, I'm weighing whether the loop component adds noise like it did on Qwen-7B (where exception_only at 99.83% outperformed VOTA at 99.41%), but accounting for the fact that 1.5B is much weaker at execution reasoning. The token length constraint at 2048 max might also affect VOTA's ability to include all three signals effectively. I'm settling on 91% as my estimate for Qwen-1.5B VOTA—the exception signal carries most of the weight, but loop noise hits harder on a weaker model, creating a meaningful 8.83pp gap between exception_only and VOTA that aligns with the pattern that smaller models depend more heavily on clean tier-1 signals.

For the full_trace variant, I'm accounting for the fact that Qwen-1.5B is weaker than Qwen-7B (which hits 81.76%), and while the label truncation issue was fixed in the v5 version, full traces still introduce more noise at this scale. I'm estimating around 75% for Qwen-1.5B full_trace, which gives a +7.7pp lift over no_trace.

Looking at the progression: no_trace to full_trace is +7.7pp, then full_trace to VOTA adds another +16pp, and finally VOTA to exception_only closes with +8.83pp. This mirrors the pattern we see with Qwen-7B but with larger gaps reflecting the weaker model capacity.

But I should refocus on what the best tier actually emphasizes—the exception_only result is already confirmed as the maximum lift at +32.5pp, and the narrative should center on the VOTA gap, the nomarker ablation, and loop_only robustness rather than getting lost in intermediate estimates. Now I need to write out the full YAML carefully and concisely, keeping in mind that codellama13b results might not finish in time. Generating the comprehensive YAML output...

Now I'm thinking through what visualizations these experiments would support—a bar chart comparing exception_only against VOTA across the three models, a comparison showing the marker's impact, and a tier hierarchy visualization. For the nomarker ablation, I need to clarify what we're testing: the [ERROR] marker provides a consistent signal that the model can anchor on, whereas without it the model must infer failure status purely from exception type names and message content. For passing samples, the marker's absence doesn't matter since there's no exception text either way.

The regex baseline B5 achieving 99.33% just by detecting the [ERROR] marker presence is striking—it shows the marker does almost all the work. The SFT model with markers only improves to 99.83%, gaining just 0.5 percentage points. Without the marker, the model would need to learn from exception type names like TypeError or ValueError, message content, traceback-like patterns, and text length to identify failures.

Looking at the regex baselines without the marker—B4 at 93.61% and B1 at 93.45%—I'd expect the SFT model to land somewhere between 96-97.5%, a drop of roughly 2.3-3.8 percentage points from the marker version. The actual results across different seeds cluster right in that range, with drops of 2.73-3.33 percentage points, which fits nicely within the expected 2-7 percentage point tier.

The marker itself contributes about 3 percentage points of performance, which is meaningful and statistically significant. For CodeLlama-13B, I'm expecting similar patterns—the exception content carries most of the signal, though as a larger 13B model based on LLaMA architecture, it might show slightly different baseline performance. The exception-only case should still be very high, around 99.5-99.8%.

Now I'm finalizing the predictions and want to verify the gap pattern the user mentioned. On Qwen-7B, exception_only exceeds VOTA by only 0.42 percentage points, which is a much smaller gap than I'd expect given how much simpler the exception-only task is.

Looking at DeepSeek, the gap is dramatic—exception outperforms VOTA by around 15 percentage points on seed42/456. For Qwen-1.5B, I'd expect a gap somewhere between these two, probably around 8-10 percentage points, since weaker models typically struggle more with the reasoning traces that VOTA requires.

The key insight is what 1.5B can actually process from VOTA traces: loop summaries demand understanding of iteration patterns and convergence (which is hard for such a small model), while exception summaries are just simple [ERROR] markers that it can learn reliably. This explains why exception_only would outperform VOTA on a 1.5B model.

The loop noise likely actively hurts rather than just being unhelpful—it confuses the model with patterns it can't grasp, pulling focus away from the clear exception signal. Plus, VOTA traces are longer, which means more truncation risk at 2048 max_length, compounding the problem. I'm settling on a prediction of around 90-91% for qwen15b_vota.

Now I'm looking at how the results would organize into a comparison table across model sizes and approaches. The pattern that emerges is striking: exception_only stays rock-solid at 99.83% regardless of model scale, while VOTA shows clear degradation as capacity decreases, dropping from 99.41% down to around 84-91%. This tells a clean story about what actually matters for solving these problems.

I should write out the YAML now with all the experimental results. But first I need to clarify whether CodeLlama-13B factors into the core findings or if it's separate from the main narrative focused on the three Qwen and DeepSeek models.

Looking at the queued CodeLlama experiments, they seem like supplementary runs, so I'll include predictions for those. I also need to work through what happens with Qwen-1.5B under full trace conditions—the model will struggle with truncated traces since they exceed the 2048 token limit, and even with the label preservation fix, extracting meaningful signal from incomplete execution data will be challenging for such a small model.

Comparing against the baselines: Qwen-7B gets 81.76% with full traces versus 75.13% without (6.6pp lift), while Qwen-1.5B sits at 67.31% without traces. If the 1.5B model gains a similar absolute lift from full traces despite its weaker reasoning capabilities, I'd estimate around 73-76%, so I'll predict 74.5%.

Actually, thinking about this more carefully—the 1.5B model might extract less signal from the traces since it struggles with execution reasoning, so maybe the lift is closer to 5-6 percentage points rather than the full 6.6pp. That would put it around 72-73%. I'll go with 73% as my final estimate.

Now I need to structure the output and map each experiment to the relevant tables and figures it would contribute to. I should also note what the nomarker experiment does—it strips out the [ERROR] marker prefix from exception summaries to test whether those markers are driving the performance gains.

Without the markers, the model loses that explicit token pattern signal and has to learn from the exception types and stack traces themselves. The regex baseline for just detecting [ERROR] presence hits 99.33%, which sets a ceiling for what the marker alone provides. But the SFT model should still outperform the exception_type regex at 93.61% even without markers, since it can learn richer patterns from the content. I'm estimating somewhere in the 95-97% range for the nomarker condition.

The 3-point drop from having the marker shows it's a useful learned anchor, but the model's ability to function without it confirms the exception content carries meaningful signal on its own. Now I'm ready to finalize the YAML structure with all the imagined experiments and their analysis sections to support the paper narrative.

Filling in the remaining experiments...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ce2e606-7b79-4af3-86fd-45ecc4fb758e",
  "isSidechain": false,
  "requestId": "req_011Cb68JRVSzRP2jvFa6cWJW",
  "type": "assistant",
  "uuid": "fcf323fa-fb2a-4d02-8450-c55b15a56cc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4",
  "sessionId": "f7665a3e-5d5c-49f9-8d35-6afa1c42cf9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011JQA8bmn4WXswFRKJXNfQE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 33159,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33159,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 17215,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 33159,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33159
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

_source line 9 · 2026-05-16T11:02:04.973Z_

```yaml
tier: best
narrative_guidance: >
  所有 pending experiments 一致强化 exception dominance。Qwen-1.5B VOTA ~91% 显著低于
  exception_only 99.83%（gap ~9pp），完美复现 "Tier 2 noise hurts weaker models more" 模式。
  nomarker ablation 确认 [ERROR] 标记贡献 ~3pp，作为 fault indicator 的 learned anchor 而非 trivial
  formatting。loop_only 3-seed std <1pp 确认 Tier 2 鲁棒性。三模型 × 1.5B-to-7B 跨规模叙事完整，
  headline: "Exception events are the minimal sufficient diagnostic signal — validated
  across 3 models spanning 1.5B to 7B parameters, with the weakest model showing
  the largest lift (+32.5pp) from exception signal."

imagined_experiments:
  # ──────────────────────────────────────────────
  # Hypothesis 1: Qwen-1.5B hierarchy completion
  # ──────────────────────────────────────────────
  - name: qwen15b_vota_seed42
    plan_id: plan_004_extension
    description: >
      Qwen-2.5-Coder-1.5B 上 VOTA trace SFT。验证 VOTA 跨规模表现，
      预期 Tier 2 组件（loop compression）在弱模型上引入更大 noise penalty。
    expected_results:
      accuracy: 0.91
      accuracy_ci_lower: 0.893
      accuracy_ci_upper: 0.927
      pass_precision: 0.895
      pass_recall: 0.99
      pass_f1: 0.940
      fail_precision: 0.965
      fail_recall: 0.715
      fail_f1: 0.822
      lift_vs_notrace: 0.237
      gap_vs_exception_only: -0.088
      train_loss: 0.065
      eval_loss: 0.15
      n: 1190
    result_rationale: >
      Qwen-1.5B no_trace=67.31%（低于 majority baseline），说明 base model execution reasoning
      极弱。exception_only=99.83% 证明 1.5B 可以完美学习简单 fault indicator。VOTA 包含 loop compression
      （Tier 2），要求模型理解迭代模式和行为收敛——这是 1.5B 的能力瓶颈。
      Qwen-7B 上 VOTA(99.41%) 仅比 exception_only(99.83%) 低 0.42pp，因为 7B 有足够能力处理 Tier 2 noise。
      1.5B 的 VOTA gap 预计 ~9pp（远大于 7B 的 0.42pp），因为：
      (1) loop tokens 占 VOTA ~60% token budget，1.5B 无法有效利用，成为 attention 稀释源；
      (2) VOTA 总 token 量 mean~2626，max_length=2048 截断 →
      1.5B 面临与 DeepSeek 类似的 training-time truncation（~90% 样本被截断），
      但 Qwen tokenizer 效率略高，截断比例可能稍低；
      (3) fail_recall 预计 ~71.5%（vs exception_only 100%），因为 loop-dominant 的 fail
      samples 信号被截断后模型无法识别。
      91% 位于指标范围 [85, 95] 中偏上——符合 Qwen 架构优势（同族 tokenizer、
      相似 pretraining 分布）但受限于 1.5B capacity。
    tables:
      - "Table 1 (Main Results): 填充 Qwen-1.5B × VOTA 单元格"
      - "Table 3 (Cross-model exception dominance): exception_only(99.83%) vs VOTA(91%) gap = 8.8pp"
    figures_description:
      - "Fig 2 (Cross-model bar chart): 三模型 VOTA 柱 — 99.41% / 84.45% / 91%，展示 model capability dependence"
      - "Fig 3 (Gap analysis): exception-VOTA gap 随模型能力递减 — 0.42pp(7B) / 8.8pp(1.5B) / 14.96pp(DeepSeek)"
    analysis: >
      1.5B VOTA=91% 与 exception_only=99.83% 的 8.8pp gap 是 best tier 叙事核心：
      (1) 严格复现 "exception > VOTA" 的 gap pattern（7B: 0.42pp, 1.5B: 8.8pp, DeepSeek: 14.96pp）；
      (2) gap 大小与 no_trace 性能负相关（no_trace 越低→gap 越大），支持 D2 "execution reasoning
      readiness" 假说——Tier 2 利用率受 base model capability 约束；
      (3) VOTA(91%) >> no_trace(67.31%) 的 23.7pp lift 确认 VOTA 仍有价值，
      但 exception isolation（额外 +8.8pp → 99.83%）才是最优策略；
      (4) "越弱的模型越依赖 exception signal" 叙事得到最强确认：
      1.5B 上 no_trace→exception_only lift=32.5pp，是全文最大。

  - name: qwen15b_full_trace_seed42
    plan_id: plan_004_extension
    description: >
      Qwen-2.5-Coder-1.5B 上 full execution trace SFT。验证 full trace 在弱模型上的效果，
      预期 information overload 在 1.5B 上更严重。
    expected_results:
      accuracy: 0.733
      accuracy_ci_lower: 0.708
      accuracy_ci_upper: 0.758
      pass_precision: 0.845
      pass_recall: 0.780
      pass_f1: 0.811
      fail_precision: 0.534
      fail_recall: 0.645
      fail_f1: 0.584
      lift_vs_notrace: 0.060
      gap_vs_exception_only: -0.265
      train_loss: 0.058
      n: 1190
    result_rationale: >
      Qwen-7B full_trace=81.76%，lift over no_trace=6.6pp。1.5B 的 execution reasoning
      更弱（no_trace=67.31% vs 75.13%），从 noisy full trace 中提取有用信号的能力更差。
      预计 lift ~6pp（与 7B 近似），但 final accuracy ~73.3% 因为起点低。
      full_trace 在 max_length=2048 下大量截断，1.5B 对截断后残余信息的理解能力有限。
      fail_recall ~64.5%（低于 7B 的 69.6%），因为 fail samples 的 diagnostic info
      更容易在截断中丢失。
      关键对比：full_trace(73.3%) vs exception_only(99.83%) = 26.5pp gap，
      大于 7B 上的 18.1pp gap，再次确认 information density 在弱模型上更为关键。
    tables:
      - "Table 1 (Main Results): 填充 Qwen-1.5B × full_trace 单元格"
      - "Table 2 (Information density): 1.5B full_trace→VOTA→exception_only 梯度"
    figures_description:
      - "Fig 1 (Accuracy progression): 三模型 no_trace→full_trace→VOTA→exception_only 曲线"
    analysis: >
      full_trace(73.3%) 仅比 no_trace(67.31%) 高 6pp，但远低于 exception_only(99.83%)——
      说明 Claim 2 在 1.5B 上更为极端：information overload penalty 更大，
      information density 的重要性随模型能力下降而增加。
      VOTA(91%) 比 full_trace(73.3%) 高 17.7pp，与 7B 上 VOTA-full_trace gap(17.6pp) 惊人一致——
      暗示 VOTA 的 compression benefit 是 scale-invariant 的（都约 17-18pp），
      而差异主要来自 base model capability floor。

  # ──────────────────────────────────────────────
  # Hypothesis 2: nomarker ablation
  # ──────────────────────────────────────────────
  - name: exception_only_nomarker_seed42
    plan_id: nomarker_ablation
    description: >
      移除 exception_only 中的 [ERROR] 格式标记前缀，保留 exception type + message。
      验证 [ERROR] 标记是 learned fault indicator anchor 而非 trivial formatting。
    expected_results:
      accuracy: 0.970
      accuracy_ci_lower: 0.958
      accuracy_ci_upper: 0.980
      pass_precision: 0.990
      pass_recall: 0.968
      pass_f1: 0.979
      fail_precision: 0.921
      fail_recall: 0.975
      fail_f1: 0.947
      drop_vs_marker: 0.028
      n: 1190
    result_rationale: >
      regex baseline B5 (format_marker = [ERROR] presence check) = 99.33%，说明 [ERROR]
      标记本身携带极强信号。移除标记后：
      (1) passing samples 不受影响——有无标记均为空/无异常内容，模型仍可正确判断；
      (2) fail samples 失去 [ERROR] 锚点，模型必须从 exception type names
      （TypeError, ValueError 等）和 message 内容推断 fault——这是更复杂的 NLU 任务；
      (3) regex B4 (exception_type matching) = 93.61% 是无标记 regex 的上界，
      SFT 模型可学到比 regex 更好的 pattern（type+message 联合、
      多行异常的聚合语义），因此预计 96-97.5%；
      (4) 2.8pp drop 处于 [2, 7] 范围内偏低端——因为 exception content 本身仍是强信号，
      标记是 facilitator 而非 sole driver。
      seed42 = 97.0%，对应 35/1190 errors（vs 有标记的 2/1190），
      新增的 33 个 errors 主要来自 exception content 语义模糊的 edge cases
      （如 StopIteration、AttributeError on valid code paths）。
    tables:
      - "Table 4 (Marker ablation): [ERROR] marker 对 accuracy 的贡献量化"
    figures_description:
      - "Fig 4 (Marker ablation bar chart): marker vs nomarker × 3 seeds"
    analysis: >
      2.8pp drop 的意义：(1) 统计显著（McNemar p<0.01, 33 个 discordant pairs）；
      (2) 确认 [ERROR] 标记是 learned signal anchor——模型利用它作为 fault detection 的
      primary trigger，而非仅做 content-based reasoning；
      (3) 但 nomarker 仍达 97%（远高于 regex B4 的 93.6%），说明 SFT 模型确实学到了
      exception content 的 semantic pattern，标记不是唯一信号源；
      (4) 对 tracer 设计的 implication：[ERROR] 标记是 low-cost, high-value 的 design choice——
      仅需在 exception 行前添加 5 个字符即获得 ~3pp improvement。

  - name: exception_only_nomarker_seed123
    plan_id: nomarker_ablation
    description: nomarker ablation seed123，验证 drop pattern 跨 seed 稳定性。
    expected_results:
      accuracy: 0.965
      accuracy_ci_lower: 0.951
      accuracy_ci_upper: 0.977
      drop_vs_marker: 0.033
      n: 1190
    result_rationale: >
      nomarker 引入更多不确定性（失去标记锚点），seed variance 预计比有标记版本更大。
      有标记版本 3-seed std=0.00pp（完美稳定），nomarker 预计 std ~0.3pp——
      因为不同 LoRA 初始化对 exception content 的 semantic learning 有轻微差异。
      seed123 预计略低于 seed42（96.5% vs 97.0%），因为 seed123 的 LoRA 初始化
      可能对某些 ambiguous exception types（如 GeneratorExit 附近的 case）更敏感。
      drop = 3.3pp，仍在 [2, 7] 范围内。
    tables:
      - "Table 4 (Marker ablation): seed123 行"
    figures_description: []
    analysis: >
      seed123 的 3.3pp drop 与 seed42 的 2.8pp drop 方向一致（均显著），
      确认 marker contribution 非 seed-specific artifact。
      不同 seeds 的 drop 一致性（std ~0.3pp）说明 marker 的贡献是
      representation-level property，不依赖 LoRA 初始化。

  - name: exception_only_nomarker_seed456
    plan_id: nomarker_ablation
    description: nomarker ablation seed456，完成 3-seed robustness。
    expected_results:
      accuracy: 0.971
      accuracy_ci_lower: 0.959
      accuracy_ci_upper: 0.981
      drop_vs_marker: 0.027
      n: 1190
      nomarker_3seed_summary:
        mean_accuracy: 0.969
        std_pp: 0.003
        mean_drop_vs_marker: 0.029
        drop_range: [0.027, 0.033]
    result_rationale: >
      seed456 预计与 seed42 高度一致（如同有标记版本 seed456=seed42=99.83%），
      drop = 2.7pp。三 seed 汇总: mean nomarker = 96.87%，mean drop = 2.96pp，
      std(nomarker) = 0.32pp。drop 均 >2pp 且方向一致，McNemar 均显著。
      与有标记版本的 0.00pp std 对比，nomarker 的 0.32pp std 说明
      移除标记后模型训练稳定性轻微下降——进一步证明标记的 stabilization 作用。
    tables:
      - "Table 4 (Marker ablation): seed456 行 + 3-seed summary"
    figures_description:
      - "Fig 4 (Marker ablation): 完整 3-seed comparison with error bars"
    analysis: >
      nomarker 3-seed 汇总为论文提供 fine-grained mechanism evidence：
      (1) [ERROR] 标记平均贡献 ~3pp，在 Analysis section 中作为 fault indicator 的 design principle；
      (2) nomarker std(0.32pp) > marker std(0.00pp) 说明标记不仅提升 accuracy，
      还提升 training stability——标记为 LoRA 提供一致的 gradient signal；
      (3) 即使无标记，SFT 仍 >>regex(93.6%)，排除 "模型只学了 keyword" 的 concern。

  # ──────────────────────────────────────────────
  # Hypothesis 3: loop_only seed robustness
  # ──────────────────────────────────────────────
  - name: loop_only_seed123
    plan_id: plan_003_extension
    description: >
      Qwen-7B loop_only seed123，验证 Tier 2 behavioral signal 跨 seed 稳定性。
    expected_results:
      accuracy: 0.845
      accuracy_ci_lower: 0.824
      accuracy_ci_upper: 0.865
      pass_precision: 0.916
      pass_recall: 0.860
      pass_f1: 0.887
      fail_precision: 0.698
      fail_recall: 0.808
      fail_f1: 0.749
      train_loss: 0.073
      n: 1190
    result_rationale: >
      loop_only seed42 = 85.63%。loop compression 是 Tier 2 信号，复杂度中等——
      模型需理解 iteration patterns 和 convergence behavior。
      Qwen-7B 对 Tier 1 信号（exception）seed-robust（std=0.00pp），但 Tier 2 复杂度更高，
      预计 seed variance 更大。seed123 预计 84.5%，比 seed42 低 1.1pp。
      这与 Tier 2 的 "model-dependent and less robust" 叙事一致：
      即使同一模型不同初始化，loop signal 的学习也有轻微差异。
      fail_recall ~80.8%（vs seed42 82.0%），差异主要在 loop-dominant fail cases
      的边界决策上。lift over no_trace = 9.4pp，仍然显著。
    tables:
      - "Table 5 (Seed robustness): loop_only seed123 行"
    figures_description: []
    analysis: >
      84.5% 确认 loop_only 在 Tier 2 范围内稳定（83-88%），
      与 full_trace_label_only(86.22%) 的近似关系保持（Δ<2pp），
      说明 VOTA loop compression 精确提取了 full trace 中的有用行为信号。

  - name: loop_only_seed456
    plan_id: plan_003_extension
    description: loop_only seed456，完成 Tier 2 3-seed robustness。
    expected_results:
      accuracy: 0.860
      accuracy_ci_lower: 0.840
      accuracy_ci_upper: 0.879
      pass_precision: 0.930
      pass_recall: 0.875
      pass_f1: 0.902
      fail_precision: 0.721
      fail_recall: 0.824
      fail_f1: 0.769
      train_loss: 0.071
      n: 1190
      loop_only_3seed_summary:
        seed42: 0.8563
        seed123: 0.845
        seed456: 0.860
        mean: 0.854
        std_pp: 0.008
    result_rationale: >
      seed456 预计 86.0%，与 seed42(85.63%) 高度一致。
      三 seed 汇总: mean = 85.4%，std = 0.77pp，range = [84.5%, 86.0%]。
      std < 1pp，在 best tier 要求的 [0, 2] 范围内。
      与 exception_only 的 0.00pp std 形成对比：Tier 2 信号的 seed variance
      非零但很小，说明 Qwen-7B 对 Tier 2 的学习基本稳定。
      对比 DeepSeek exception_only 的 4.8pp std——model capability 才是
      seed variance 的主要决定因素，signal complexity 是次要因素。
    tables:
      - "Table 5 (Seed robustness): loop_only seed456 行 + 3-seed summary"
      - "Table 6 (Tier comparison): Tier 1 std=0.00pp vs Tier 2 std=0.77pp"
    figures_description:
      - "Fig 5 (Tier robustness): Tier 1 (exception) vs Tier 2 (loop) 3-seed violin plot"
    analysis: >
      loop_only 3-seed std = 0.77pp 完成 Claim 3 two-tier hierarchy 的 robustness validation：
      (1) Tier 1 (exception): 99.83% ± 0.00pp — 完美稳定，signal intrinsic robustness；
      (2) Tier 2 (loop): 85.4% ± 0.77pp — 稳定但非完美，signal complexity 引入轻微 variance；
      (3) Tier 2 mean(85.4%) ≈ label_only(86.22%)，Δ=0.82pp 不显著——
      确认 VOTA loop compression 精确等价于 full trace 中的 behavioral signal；
      (4) Tier 2 完全被 Tier 1 subsumed（exception_only > loop_only by 14.4pp, p<0.001）。

  # ──────────────────────────────────────────────
  # Supplementary: CodeLlama-13B (bonus, not core narrative)
  # ──────────────────────────────────────────────
  - name: codellama13b_exception_only_seed42
    plan_id: supplementary_model_validation
    description: >
      CodeLlama-13B-Instruct 上 exception_only SFT。如完成，提供第 4 模型 +
      architecture diversity（LLaMA vs Qwen/DeepSeek）验证。
    expected_results:
      accuracy: 0.997
      accuracy_ci_lower: 0.993
      accuracy_ci_upper: 1.000
      pass_precision: 1.000
      pass_recall: 0.996
      pass_f1: 0.998
      fail_precision: 0.990
      fail_recall: 1.000
      fail_f1: 0.995
      n: 1190
    result_rationale: >
      exception signal 结构极简（[ERROR] type: message），不依赖特定 architecture 或
      tokenizer——Qwen-1.5B(99.83%)、Qwen-7B(99.83%)、DeepSeek-6.7B(99.33% median)
      已覆盖 Qwen 和 DeepSeek 架构。CodeLlama-13B 作为 LLaMA 架构代表，
      13B 参数量充足（>7B），exception signal 的 learnability 应无问题。
      预计 99.7%——可能略低于 Qwen 的 99.83% 因为 LLaMA tokenizer 对 Python exception
      格式的 tokenization 效率可能略有差异，但差异微小且不显著。
      如确认，universality claim 从 N=3 升至 N=4，跨越 3 个 architecture family。
    tables:
      - "Appendix Table (Extended model validation): CodeLlama-13B 行"
    figures_description:
      - "Extended Fig (4-model bar chart): 如完成，exception_only 4-model comparison"
    analysis: >
      99.7% 进一步确认 exception signal 的 architecture-invariant 特性。
      但作为 supplementary data，不改变核心 3-model 叙事。
      主要价值：排除 "只在 Qwen/DeepSeek 家族有效" 的 reviewer concern。

  - name: codellama13b_no_trace_seed42
    plan_id: supplementary_model_validation
    description: CodeLlama-13B no_trace baseline。
    expected_results:
      accuracy: 0.755
      accuracy_ci_lower: 0.730
      accuracy_ci_upper: 0.780
      pass_precision: 0.880
      pass_recall: 0.770
      pass_f1: 0.821
      fail_precision: 0.560
      fail_recall: 0.720
      fail_f1: 0.630
      n: 1190
    result_rationale: >
      CodeLlama-13B 是 13B 参数模型，general capability 强于 6.7B/7B 但 code-specific
      pretraining data 可能不如 Qwen-2.5-Coder。no_trace 主要依赖 base model 对
      code+test 的理解推断 pass/fail——13B 参数量的优势 vs code-specialized pretraining
      的劣势大致抵消。预计 75.5%，与 Qwen-7B(75.13%) 和 DeepSeek(73.36%) 同一水平。
      跨模型 no_trace gap 始终很小（<2pp），说明 baseline 能力相对同质。
    tables:
      - "Appendix Table: CodeLlama-13B no_trace baseline"
    figures_description: []
    analysis: >
      no_trace ~75.5% 建立 CodeLlama-13B 的 baseline。
      如果 exception_only 达 99.7%，lift = 24.2pp，与 Qwen-7B(24.7pp) 高度一致，
      再次确认 exception signal lift 的 model-invariant 特性。

  - name: codellama13b_vota_seed42
    plan_id: supplementary_model_validation
    description: CodeLlama-13B VOTA SFT，验证 VOTA 在 LLaMA 架构上的表现。
    expected_results:
      accuracy: 0.955
      accuracy_ci_lower: 0.942
      accuracy_ci_upper: 0.967
      pass_precision: 0.950
      pass_recall: 0.993
      pass_f1: 0.971
      fail_precision: 0.972
      fail_recall: 0.862
      fail_f1: 0.914
      n: 1190
    result_rationale: >
      CodeLlama-13B 的 execution reasoning 能力中等偏上（13B 参数但 code-specific
      pretraining 不如 Qwen-2.5-Coder）。CRUXEval-I 估计 ~45-50%（介于 DeepSeek 39%
      和 Qwen 56.5% 之间）。VOTA 性能与 execution reasoning 正相关（D2 假说）。
      预计 95.5%——高于 DeepSeek(84.45%, 受 truncation confound) 但低于 Qwen-7B(99.41%)。
      CodeLlama tokenizer 对 VOTA 格式的 tokenization 效率可能与 Qwen 有差异，
      影响截断比例。exception_only(99.7%) > VOTA(95.5%) gap = 4.2pp，
      确认即使在 13B 规模上 Tier 2 组件仍有 noise penalty。
    tables:
      - "Appendix Table: CodeLlama-13B VOTA"
    figures_description:
      - "Extended Fig: 4-model exception vs VOTA gap comparison"
    analysis: >
      VOTA 95.5% 介于 Qwen-7B(99.41%) 和 DeepSeek(84.45%) 之间，
      与 CRUXEval 能力排序一致。exception-VOTA gap = 4.2pp 进一步
      支持 "VOTA gap 与 model capability 负相关" 假说。
      但 CodeLlama 数据不进入核心叙事，仅作 Appendix 佐证。

  # ──────────────────────────────────────────────
  # Aggregate narrative elements
  # ──────────────────────────────────────────────
  - name: aggregate_cross_model_table
    plan_id: synthesis
    description: 三模型完整结果表（best tier 合成视图）
    expected_results:
      qwen_7b:
        no_trace: 0.7513
        full_trace: 0.8176
        vota: 0.9941
        exception_only: 0.9983
      deepseek_6.7b:
        no_trace: 0.7336
        full_trace: 0.7916
        vota: 0.8445
        exception_only: 0.9933
      qwen_1.5b:
        no_trace: 0.6731
        full_trace: 0.733
        vota: 0.91
        exception_only: 0.9983
      exception_only_cross_model_std: 0.003
      vota_cross_model_std: 0.076
      no_trace_cross_model_std: 0.040
    result_rationale: >
      exception_only 跨模型 std = 0.29pp（几乎完美一致），VOTA std = 7.6pp（高度 model-dependent），
      no_trace std = 4.0pp（moderate variance）。这量化了核心 insight：signal complexity
      与 cross-model variance 正相关。exception signal 因结构简单性实现 scale-invariant 性能；
      VOTA 因包含 model-capability-dependent 的 Tier 2 组件而 variance 最大。
    tables:
      - "Table 1 (Main Results): 完整 3×4 矩阵"
    figures_description:
      - "Fig 1 (Main figure): grouped bar chart, 4 conditions × 3 models"
      - "Fig 6 (Cross-model std): 每个 condition 的跨模型 std，展示 complexity-variance 关系"
    analysis: >
      Table 1 是论文核心。best tier 下，三模型数据完整，所有 exception_only 均 >99.3%（median 99.83%），
      所有 exception_only > VOTA，所有 VOTA > no_trace。Hierarchy 完全一致。
      Qwen-1.5B 提供三重价值：
      (1) exception_only 99.83% = 7B，scale-invariant 铁证；
      (2) VOTA 91% < exception_only 99.83%（gap 8.8pp），capability-dependence 确认；
      (3) no_trace→exception_only lift = 32.5pp，全文最大，"越弱越依赖 exception" 叙事高潮。
      EMNLP main 直投，findings 不需要作 fallback。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcf323fa-fb2a-4d02-8450-c55b15a56cc5",
  "isSidechain": false,
  "requestId": "req_011Cb68JRVSzRP2jvFa6cWJW",
  "type": "assistant",
  "uuid": "4d7e0a89-206b-4156-8529-fc5ff18a705b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4",
  "sessionId": "f7665a3e-5d5c-49f9-8d35-6afa1c42cf9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011JQA8bmn4WXswFRKJXNfQE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 33159,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33159,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 17215,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 33159,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33159
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有 pending experiments 一致强化 exception dominance；第三模型 Qwen-1.5B 完整复现 hierarchy；三模型 × 跨规模叙事 → EMNLP main 核心假设：['Qwen-1.5B VOTA 显著低于 exception_only (99.83%)，复…",
  "leafUuid": "4d7e0a89-206b-4156-8529-fc5ff18a705b",
  "sessionId": "f7665a3e-5d5c-49f9-8d35-6afa1c42cf9b"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Trace verdict prediction: exception signals outperform rich traces",
  "sessionId": "f7665a3e-5d5c-49f9-8d35-6afa1c42cf9b"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有 pending experiments 一致强化 exception dominance；第三模型 Qwen-1.5B 完整复现 hierarchy；三模型 × 跨规模叙事 → EMNLP main 核心假设：['Qwen-1.5B VOTA 显著低于 exception_only (99.83%)，复…",
  "leafUuid": "4d7e0a89-206b-4156-8529-fc5ff18a705b",
  "sessionId": "f7665a3e-5d5c-49f9-8d35-6afa1c42cf9b"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Trace verdict prediction: exception signals outperform rich traces",
  "sessionId": "f7665a3e-5d5c-49f9-8d35-6afa1c42cf9b"
}
```

---
