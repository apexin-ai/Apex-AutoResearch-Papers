# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/a83c4e8f-ba60-4c11-a244-a557040bd173.jsonl`
- **Structured JSON:** [`e5f43fabbbee6c1fb766.json`](../../sessions/e5/e5f43fabbbee6c1fb766.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T12:43:10.874Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T12:43:10.874Z",
  "sessionId": "a83c4e8f-ba60-4c11-a244-a557040bd173",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: trace-verdict-study\nfocus: 评估当前 plan 是否够冲 EMNLP main。重点审查：(1) 3 个 Core Claims 的证据强度，(2) P1 实验（phase transition fine-grained + cross-seed）对论文质量的边际贡献，(3) 4 模型 budget curve 矩阵的 story 是否足够有说服力，(4) label_only_loss 发现值不值得作为独立 contribution，(5) 与同类 EMNLP/ACL 论文对比缺什么。\n\n## paper_framing.md\n\n# Paper Framing — trace-verdict-study\n\n> v3.0 — [UPDATED 2026-05-15] D030 CLOSED: DeepSeek VOTA 84.45% confirmed correct (confirmatory re-eval). **Critical narrative fix**: to_chat_text() preserves labels → VOTA 训练时 verdict label 未被截断 → 论文中 \"label truncation/corruption\" 措辞对 VOTA 不成立。正确叙事: trace INPUT content 被截断 (91.7% samples), 84.45% 反映 trace information loss。新增 D11: VOTA cross-model gap confounded by training-time truncation。数据集来源：HumanEval (164) + MBPP-sanitized (427) = 591 problems × 10 LLM-generated solutions = 5910 samples。\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026\n\n## Core Insight\n\nVerdict prediction (pass/fail) is fundamentally a **fault detection** task. The most effective signal is the **exception event** — a compact, structured diagnostic moment that consistently outperforms all other trace representations across models (Qwen 99.83% ± 0.00 across 3 seeds; DeepSeek 91-99% depending on seed, but always > VOTA 84.45% and no_trace 73.36%). In contrast, richer trace representations that require deeper execution reasoning show model-dependent effectiveness: VOTA gap = 14.96pp, no_trace gap = 1.77pp. Information density — not training signal distribution — is the primary bottleneck: even oracle loss masking (label-only) cannot close the 13pp gap between full traces and targeted extraction. The design principle: **extract the highest-specificity diagnostic signal; discard everything else.** Cross-model absolute performance depends on LoRA initialization stability, but exception_only's relative dominance over other components is robust.\n\nVOTA's primary contribution is **fault indicator isolation** — automatically extracting exception events from noisy full traces — rather than generic trace compression. The \"compression helps\" narrative was a stepping stone; the real mechanism is diagnostic signal extraction.\n\n## Core Claims (3)\n\n### Claim 1: Exception events are the most effective trace component for verdict prediction\n\nException summaries consistently achieve the highest verdict prediction accuracy across both models tested, outperforming all other trace representations in every seed. On Qwen-2.5-Coder-7B, performance is perfectly robust: 99.83% ± 0.00 (3 seeds). On DeepSeek-Coder-6.7B, absolute accuracy is seed-dependent (seed42=99.83% epoch1, seed123=91.43% epoch1; Δ=8.40pp), consistent with LoRA initialization sensitivity — but exception_only still dominates VOTA (84.45%) and no_trace (73.36%) in all seeds. This contrasts with VOTA (cross-model gap = 14.96pp) and no_trace (gap = 1.77pp). Exception events are structurally simple (`[ERROR] type: ... message: ...`) and do not require deep trace reasoning.\n\n**Supporting evidence:**\n- `vota_exception_only_seed42_v2`: Qwen 99.83%, ECE=0.0027\n- `deepseek_exception_only_seed42`: DeepSeek 99.83% (epoch1) / 99.33% (epoch3)\n- `deepseek_exception_only_seed456`: DeepSeek 99.33% (epoch3), CI [98.82, 99.75] — 与 seed42 完全一致\n- `deepseek_exception_only_seed123`: DeepSeek 91.43% (epoch1) / 91.09% (epoch3) — LoRA init sensitivity outlier\n- `deepseek_vota_seed42`: DeepSeek VOTA 84.45% (gap = 14.96pp vs Qwen)\n- `deepseek_no_trace_seed42`: DeepSeek no_trace 73.36% (gap = 1.77pp vs Qwen)\n- `vota_no_ae_seed42`: 99.41% — actual/expected removal 不降，非 trivial string comparison\n\n**DeepSeek seed analysis** ✅ (FINALIZED, D029):\n\n| Seed | Epoch 3 (final) | fail_recall | pass_recall | train_loss | Errors | CI |\n|------|-----------------|-------------|-------------|------------|--------|-----|\n| 42   | 99.33%          | 1.0         | 0.9906      | —          | 8/1190 | — |\n| 456  | 99.33%          | 1.0         | 0.9906      | 0.1225     | 8/1190 | [98.82, 99.75] |\n| 123  | 91.09%          | 0.705       | 0.993       | 0.122      | —      | [89.4, 92.6] |\n\nseed42 与 seed456 结果**完全一致**（均 8/1190 错误，99.33%），seed123 为离群值。seed123 的 fail_recall 仅 0.705 — LoRA 初始化落入差的局部最优，未充分学到 exception→fail 映射。**关键发现**: seed456 和 seed123 的 train_loss 几乎相同（0.1225 vs 0.122），但 accuracy 差 8.2pp — token-level loss 掩盖了 sample-level 分类能力的巨大差异（详见 D10）。\n\n**Irreducible error analysis** ✅: 3 seeds 错误的 2 个样本 (id=901, 905) 均来自 HumanEval/95 (`check_dict_case`)，根因为 Python `all()` 对 generator expression 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误）。tracer 将其标记为 `[ERROR]`，exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。整个 1190 条测试集仅这 2 条含 `GeneratorExit`，模型无训练信号学习其良性本质。**这确认 99.83% 是 exception_only 表征的理论上限，剩余 0.17% 是 representation-inherent irreducible error，而非模型不足。**\n\n**Seed robustness** ✅: Qwen exception_only 3-seed 完全一致，构成本文最强 robustness 证据：\n\n| Seed | Accuracy | 95% CI | Errors |\n|------|----------|--------|--------|\n| 42 | 99.83% | [99.58, 100] | 2/1190 |\n| 123 | 99.83% | [99.58, 100] | 2/1190 |\n| 456 | 99.83% | [99.58, 100] | 2/1190 |\n\n3 seeds 错误样本 100% 重叠（id=901, 905, 均为 `check_dict_case` 函数, label=pass → pred=fail）。**Irreducible samples**: 模型已达数据集理论上限，variance = 0。\n\n**DeepSeek cross-model** ✅ (D029): 3-seed 完整数据 — seed42/456=99.33%, seed123=91.09%。2/3 seeds 鲁棒，seed123 为 LoRA 初始化离群值（fail_recall 仅 0.705）。Qwen 3-seed 完美稳定 (99.83% ± 0.00) vs DeepSeek 高方差（σ≈4.8pp），暗示 exception signal 的 learnability 与模型 LoRA 训练稳定性相关。但即使最差 seed (91.09%) 仍优于 VOTA (84.45%) 和 no_trace (73.36%)，relative dominance robust。\n\n### Claim 2: Information density, not gradient dilution, drives trace compression benefit\n\nFull traces help verdict prediction (81.76% [`full_trace_seed42_v5`], +6.6pp over baseline), but VOTA achieves 99.41% [`vota_seed42_v5`] (+24.3pp) — a +17.6pp advantage. Label-only loss ablation (plan_002) quantifies the causal decomposition: **gradient dilution contributes ~26% of the gap** (4.5pp; label-only full_trace = 86.22% [`full_trace_label_only_seed42`]), **information overload contributes ~74%** (13.0pp; only trace compression resolves this). Even with oracle loss masking that eliminates gradient dilution, full traces still underperform VOTA by 13pp.\n\nCross-model evidence reinforces this: VOTA gap (14.96pp) partly tracks base model execution reasoning capability (Qwen CRUXEval-I 56.5% vs DeepSeek 39.0%, Δ=17.5pp), though **confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated to ~2048 tokens; see D11). The two factors cannot be disentangled in the current design. Exception signal partially bypasses both bottlenecks (token-short, no truncation; consistently best component on both models), though DeepSeek shows seed-dependent absolute performance (91-99%).\n\n**Supporting evidence:**\n- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (gradient dilution fix, +4.5pp over standard full_trace)\n- `full_trace_seed42_v5`: 81.76%, ECE=0.0958 (standard full_trace)\n- `vota_seed42_v5`: 99.41%, ECE=0.0054\n- `deepseek_vota_seed42`: 84.45% (VOTA model-dependent)\n- CRUXEval literature data (Wang et al.)\n\n### Claim 3: Two-tier diagnostic hierarchy for verdict prediction\n\nComponent ablation reveals verdict-relevant trace information has a strict two-tier hierarchy:\n- **Tier 1 — diagnostic moment signals**: exception summaries (99.83% [`vota_exception_only_seed42_v2`]) and assertion-point information (99.92% [`vota_ae_only_seed42`]) are individually near-perfect and sufficient for verdict prediction on Qwen. These signals are structurally simple and consistently the most effective component on both models, though DeepSeek absolute performance is seed-dependent.\n- **Tier 2 — behavioral patterns**: loop compression (85.63% [`vota_loop_only_seed42`]) carries substantial signal but is model-dependent and fully subsumed by Tier 1.\n\nCombining tiers introduces noise rather than helping: exception_only (99.83%) > VOTA full (99.41%), p=0.01. Loop_only ≈ full_trace_label_only (85.63% vs 86.22%) confirms VOTA's loop compression precisely extracts the useful behavioral signal from full traces.\n\n**Supporting evidence:**\n- `vota_exception_only_seed42_v2`: 99.83%, ECE=0.0027 (Tier 1 exception)\n- `vota_ae_only_seed42`: 99.92%, ECE=0.0004 (Tier 1 assertion-point, 与 exception 统计等价 p=0.80)\n- `vota_loop_only_seed42`: 85.63%, ECE=0.0831 (Tier 2 behavioral)\n- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (≈ loop_only, confirming extraction equivalence)\n- `deepseek_exception_only_seed42`: 99.83% epoch1 / 99.33% epoch3 (Tier 1 cross-model validation)\n- `deepseek_vota_seed42`: 84.45% (Tier 1+2 cross-model: Tier 2 introduces model-dependent degradation)\n\n**Calibration**: 完整 calibration 数据确认 Tier 1 信号不仅 accuracy 近完美，置信度校准也近完美：\n\n| Condition | Accuracy | ECE | Brier | 解读 |\n|-----------|----------|-----|-------|------|\n| ae_only | 99.92% | 0.0004 | 0.0008 | 近乎完美校准 |\n| exception_only | 99.83% | 0.0027 | 0.0013 | 近乎完美校准 |\n| VOTA | 99.41% | 0.0054 | 0.005 | 优秀，但 Tier 2 引入轻微 noise |\n| loop_only | 85.63% | 0.0831 | — | Tier 2 单独校准中等 |\n| label_only | 86.22% | 0.1107 | — | gradient dilution fix 仍 miscalibrated |\n| full_trace | 81.76% | 0.0958 | — | 中度 miscalibrated |\n| no_trace | 75.13% | 0.1715 | 0.1972 | 严重 miscalibrated |\n\nno_trace ECE 是 exception_only 的 **~63x**（0.1715/0.0027），Brier 是 **~150x**（0.1972/0.0013）。Trace signal（尤其 Tier 1）不仅提升 accuracy，更从根本上改善模型 calibration。\n\n**Design principle**: verdict-optimized traces should extract highest-specificity diagnostic signals; lower-specificity signals are redundant and may introduce noise.\n\n## Cross-Model Evidence Summary\n\n| Condition | Qwen-2.5-Coder-7B | DeepSeek-Coder-6.7B | Cross-model gap | Interpretation |\n|-----------|-------------------|---------------------|-----------------|----------------|\n| exception_only | 99.83% ± 0.00 (3 seeds) | seed42/456: 99.33%; seed123: 91.09% | 0.50-8.74pp (seed-dependent) | **Best component on both models**; 2/3 DeepSeek seeds match Qwen-level; 1 outlier still > VOTA |\n| VOTA | 99.41% | 84.45% | -14.96pp | Model-dependent — requires execution reasoning; **also confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated from mean 2626 to ~2048 tokens; labels preserved via to_chat_text(), see D11) |\n| no_trace | 75.13% | 73.36% | -1.77pp | Baseline gap tracks general capability |\n| full_trace | 81.76% | collapsed (v3 pending) | N/A | DeepSeek v1 label truncation bug |\n\n**Key insight**: Exception_only is consistently the best component on both models (even worst DeepSeek seed 91.09% > VOTA 84.45%). Cross-model gap 与 signal complexity 正相关, but exception signal's absolute effectiveness also depends on LoRA training stability. Qwen: perfectly robust (3 seeds identical). DeepSeek: 2/3 seeds at 99.33% (matching Qwen-level), 1 outlier at 91.09% (LoRA initialization). Median performance robust; seed sensitivity suggests smaller/weaker models may need training stabilization (multi-seed selection, warmup tuning) for optimal exception signal utilization.\n\n## VOTA Repositioning\n\n**旧叙事**: VOTA 是 trace compression 方法，价值在于\"压缩使 trace 更有效\"。\n\n**新叙事**: VOTA 是 **fault indicator isolation** 方法，核心价值在于自动从 noisy execution traces 中提取 exception events 等 diagnostic signals。\n\n**证据链**:\n1. exception_only (99.83%) ≥ VOTA full (99.41%) — 压缩后的其他组件（loop, ae）不仅无益，反而引入 noise\n2. VOTA 跨模型 gap = 14.96pp — 因为 VOTA 包含 model-dependent 的 Tier 2 组件（loop compression 需要 execution reasoning）\n3. exception_only 在两个模型上均为最优组件 — isolate 出 Tier 1 后，相对优势 robust（虽然 DeepSeek 绝对值 seed-dependent）\n4. vota_no_ae (99.41%) = VOTA (99.41%) — actual/expected 移除无影响，exception 是真正的 active ingredient\n\n**论文中的表述**: \"VOTA's trace compression pipeline incidentally isolates exception events — the minimal sufficient diagnostic signal. Its value lies not in making traces shorter, but in separating high-specificity fault indicators from low-specificity behavioral patterns.\"\n\n**对 Method section 的影响**: VOTA 仍然完整描述（loop compression + exception + actual/expected），但 Results/Discussion 明确指出 exception isolation 是核心机制，其他组件是 model-capability-dependent bonus。\n\n## Story Spine\n\n- **Problem**: Existing trace SFT studies (DCSH, TracePile) evaluate only generative tasks and find limited, model-dependent benefit. No prior work has tested trace SFT on verdict tasks (binary pass/fail), nor identified what trace components drive classification performance.\n\n- **Existing approaches & gaps**: DCSH (EMNLP Findings 2025) tested 5 trace formats on generation tasks, finding that \"no single trace representation consistently outperforms others.\" TracePile (NeurIPS 2025) scaled to 2.6M samples but only evaluated generation. TRACED (ICSE 2024) showed traces help encoder-based classification. All existing trace formats are designed for execution simulation, not fault detection.\n\n- **Our framing**: We reframe verdict prediction as **fault detection** and ask: what is the minimal sufficient diagnostic signal? Through systematic component ablation across two architecturally distinct models, we discover that exception events — compact, structured error summaries — are consistently the most effective trace component, achieving near-perfect accuracy on Qwen (99.83% ± 0.00, 3 seeds) and outperforming all alternatives on DeepSeek (91-99% vs VOTA 84.45%). Richer trace representations work only when the base model has sufficient execution reasoning capability, making them unreliable for general deployment.\n\n- **Headline result**: \"Exception events consistently achieve the highest verdict accuracy across models (Qwen 99.83%, DeepSeek 91-99%), outperforming VOTA traces (84.45% on DeepSeek, -14.96pp gap) — demonstrating that fault indicator isolation, not trace reasoning, is the robust mechanism for verdict prediction. DeepSeek seed sensitivity reveals LoRA training stability as a secondary factor for smaller models.\"\n\n## Story Arc\n\n1. **Setup**: Trace SFT for code tasks — promising but inconsistent in prior work (DCSH, TracePile). Unknown whether traces help verdict tasks and what trace design matters.\n\n2. **First result — traces help, compression helps more** (single model): no_trace 75.13% → full_trace 81.76% → VOTA 99.41%. Label-only loss ablation decomposes the gap: 26% gradient dilution, 74% information overload. Compression improves accuracy through higher information density, not just cost savings.\n\n3. **Twist — what component actually drives VOTA?** Component ablation reveals exception_only (99.83%) ≥ full VOTA (99.41%). The \"trace reasoning\" narrative is wrong — verdict prediction is fault detection. Tier 1 (exceptions + assertion-point) subsumes Tier 2 (loops). Actual/expected removal doesn't hurt (99.41%).\n\n4. **Cross-model stress test — consistent dominance, not universal perfection**: Exception_only is the best component on both models (even DeepSeek worst seed 91.09% > VOTA 84.45%), but absolute performance is seed-dependent on DeepSeek (91-99% vs Qwen's perfectly stable 99.83%). VOTA degrades by 14.96pp. The structurally simplest component is the most robust, but LoRA initialization sensitivity introduces variance on weaker models. Qwen seed robustness (3-seed variance = 0) + calibration (ECE=0.0027) 确认 exception signal 在强模型上的 reliability。DeepSeek seed sensitivity 揭示 training stability 作为 secondary bottleneck。\n\n5. **Design principle**: For verdict tasks, identify the highest-specificity diagnostic signal (exception events) and discard everything else. VOTA's value is fault indicator isolation — automatically extracting exceptions from noisy traces — not generic compression. Simpler signals are more robust; complexity tolerance depends on model capability.\n\n## Dataset Characteristics\n\n### Data duplication analysis\n\n| Condition | Total | Unique | Duplication rate | Cause |\n|-----------|-------|--------|------------------|-------|\n| exception_only_train | 4720 | 2858 | 39.45% | 同题多个 passing 解映射为相同 (input, output) — 无异常 → 同一 trace |\n| exception_only_test | 1190 | 607 | 48.99% | 同上 |\n| raw_traces | 5910 | 5803 | 1.81% | 完整 trace 含行号/变量值/内存地址，几乎不重复 |\n\n**Train-test input overlap: 0（无数据泄漏）**\n\n**解读**: exception_only 高重复率是 representation 的自然属性，非数据问题。多个正确解对同一测试用例执行时若均无异常，exception_only 表征退化为相同的空/无异常标记。这恰好说明 exception signal 的 compactness — 它仅编码 fault presence，不编码 solution identity。raw_traces 重复率极低 (1.81%) 因为完整 trace 包含 solution-specific 信息（变量值、内存地址）。尽管高重复率意味着有效训练样本少于名义数量，模型仍达 99.83% — 进一步确认 exception signal 的 learnability。\n\n## DeepSeek full_trace 处理\n\n**现状**: v1 坍塌（28.5%, 100% 预测 fail, 根因: 训练端 label 截断）。v2 重训启动但被 kill（Loop #6 ops worker 腾 GPU 给 vota_seed456）。v3 RUNNING（label-preserving truncation fix）。\n\n**处理方案**: v3 正在 cuda:0 上训练，预计 5/16 完成。\n\n**VOTA vs full_trace 截断机制区分** (D030 token analysis 确认):\n- **full_trace v1**: SFTTrainer right-truncation 切掉了 verdict **label** → 100% predict fail → 坍塌。根因: DeepSeek tokenizer 对 full_trace 产生 >2048 tokens, label 在截断窗口外。\n- **VOTA**: `to_chat_text()` 保留 verdict label（label 完整），但 91.7% 的样本 **trace content（input）被截断**（mean 2626 → ~2048 tokens）。84.45% 是真实结果，反映 trace 信息损失对模型学习的影响，**不是** label corruption。\n- **exception_only**: token 长度远低于 2048，不受截断影响，跨模型对比 clean。\n\n**对论文叙事的影响**: 论文中所有 \"right-truncation corrupts/removes the verdict label\" 措辞**对 VOTA 不成立**——label 完整保留，被截断的是 trace input。正确表述: \"trace content truncation causes information loss\"。VOTA cross-model gap (14.96pp) 有两个贡献因素: (1) model capability, (2) training-time trace truncation on DeepSeek (see D11)。\n\n## External Benchmark (DebugBench) Positioning\n\n**DebugBench 仅作泛化性验证，不作 trace importance 证据。**\n\n| Condition | Main Dataset | DebugBench | Δ interpretation |\n|-----------|-------------|------------|------------------|\n| no_trace | 75.13% | 96.71% | DebugBench 天花板高，baseline 已强 |\n| VOTA | 99.41% | 99.77% | +3.06pp lift — 边际 |\n| exception_only | 99.83% | 100.00% | +3.29pp lift — 边际 |\n\n**主数据集 trace lift = 24.70pp**（no_trace → exception_only），DebugBench trace lift 不到其 1/7。\n\n**论文定位规则**：\n- DebugBench → 泛化性证据（exception_only 100% = 跨数据集鲁棒性）\n- Trace importance 论证 → 仅依赖主数据集（24.7pp lift）\n- 禁止用 DebugBench 的 3.29pp lift 论证 \"trace 的核心价值\"——审稿人会攻击天花板效应\n\n## Venue Fit Risks\n\n| Risk | Assessment | Mitigation |\n|------|-----------|------------|\n| 单任务 | 仍然只在 test verdict prediction 上验证 | 跨模型验证部分弥补; Discussion 中讨论 generalization |\n| 单数据集 | HumanEval + MBPP-sanitized 是唯一数据源 (591 problems × 10 solutions) | 定位为 empirical study, 深度优于广度; 两个标准 benchmark 组合覆盖多样编程题型; exception_only 有效训练样本仅 2858 unique 即达 99.83%, 暗示 signal 的 simplicity 降低对数据量的依赖 |\n| \"只是 feature engineering\" | exception extraction 不复杂 | simplicity 本身是 contribution — 最简信号最 robust |\n| Negative result 味道 | VOTA 跨模型不 robust | Reframe: 识别 robust vs non-robust 组件边界是 positive |\n| Seed robustness (Qwen) | ✅ 已解决: 99.83% ± 0.00 (3 seeds), irreducible samples 确认 | — |\n| Seed robustness (DeepSeek) | ✅ 3-seed 完整: 2/3 at 99.33%, 1 at 91.09% | LoRA initialization sensitivity — median robust, worst still > all alternatives; 转化为 training stability finding (D9/D10) |\n| Calibration | ✅ 完整数据: Tier 1 ECE≤0.003, no_trace ECE=0.171 (~63x gap) | Brier ~150x gap 进一步确认 |\n| 只用 2 个模型 | 有限但有意义的 diversity | Architecture + pretraining data (5.5T vs 2T) + CRUXEval gap (17.5pp) 构成充分差异 |\n| 数据重复率 | exception_only 训练集 39.45% 重复 | 非数据泄漏（train-test overlap = 0）；是 representation compactness 的自然结果；有效样本仍足够学习 |\n\n## Anticipated Reviewer Concerns\n\n| Concern | Planned Response |\n|---------|-----------------|\n| \"exception_only 99.83% 是不是 trivial pattern matching [ERROR] 有无？\" | full_trace 也包含 [ERROR] 但仅 81.76%——模型需要从 trace context 中 extract 和 utilize exception signal, 不是简单 keyword detection. no_trace 无 exception, 75.13%. |\n| \"为什么 exception_only > VOTA? adding info 反而降?\" | 非 exception 组件 (loop/ae tokens) 稀释 attention 对 exception 信号的聚焦. Calibration: exception_only ECE=0.0027 vs VOTA ECE=0.0054. 部分样本 loop 正常但有 exception, 引入矛盾信号. |\n| \"CRUXEval gap 与 VOTA gap 的相关性可能是 coincidence\" | 明确标注为 hypothesis. 列出 alternatives (tokenizer efficiency, pretraining scale 2.75x, chat template). 不 overclaim. |\n| \"只有 2 个模型，universality claim 太强\" | 同意是 limitation. 两模型在 architecture (RoPE vs ALiBi), pretraining data (5.5T vs 2T), execution reasoning (CRUXEval 17.5pp gap) 上有充分差异, 不是 trivial replication. Exception signal 的 structural simplicity 提供 inductive argument for broader generalization. |\n| \"99.83% 可能 saturated, 看不出 exception 到底学了什么\" | Calibration 双指标: exception_only ECE=0.0027, Brier=0.0013 (近完美校准). 对比 no_trace ECE=0.1715, Brier=0.1972 (~63x/~150x gap). **Irreducible error 根因已明确**: 2/1190 errors 均因 Python `all()` 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误），tracer 将其标记为 `[ERROR]`。模型看到 7 行 `[ERROR] GeneratorExit` 合理预测 fail，但代码实际正确。整个测试集仅这 2 条含 `GeneratorExit`，无训练信号可学习其良性本质。99.83% 是 representation 的理论上限，非 saturation artifact。 |\n| \"只用了 1 个 seed\" | Qwen ✅: 3 seeds 99.83% ± 0.00. DeepSeek ✅: 3 seeds 完整 — seed42/456=99.33%, seed123=91.09%。2/3 鲁棒，1 离群。median=99.33%, worst=91.09% (仍 > VOTA 84.45%)。论文透明报告所有 seeds，将 seed sensitivity 转化为 LoRA training stability 的 finding（D9）。 |\n| \"eval_loss 上升但 accuracy 提升——checkpoint selection 有问题?\" | Discussion D1: token-level loss 与 binary verdict accuracy 解耦. 推荐 verdict-specific metric. Methodological contribution. |\n| \"DeepSeek full_trace 坍塌是 bug 不是 finding\" | 诚实披露根因 (训练端 label 截断). 其他 3 条件不受影响. 修复版本如就绪则补入. |\n| \"calibration 数据只有 1 个 seed\" | Seed robustness 已证明 accuracy variance=0 (3 seeds), calibration 在 accuracy 完全一致的前提下 expected 也一致. ECE/Brier 的极小值 (0.0027/0.0013) 留有极小 variance 空间. |\n| \"DeepSeek epoch1 > epoch3, 为什么用 epoch3 报告?\" | 正文报告所有 seeds 的 final + best checkpoint。seed42: epoch1=99.83%, epoch3=99.33%。seed123: epoch1=91.43%, epoch3=91.09%。D7 讨论 early stopping + D9 讨论 LoRA initialization sensitivity。不 cherry-pick best seed。 |\n| \"DeepSeek seed sensitivity 说明 exception signal 不 robust\" | Exception_only 在所有 seeds 上仍优于其他条件（worst seed 91.09% > VOTA 84.45%）。Seed sensitivity 是 LoRA training 问题而非 signal 问题——Qwen 3 seeds 完美证明 signal 本身 robust。D9 讨论 training stabilization 作为 practical recommendation。 |\n| \"exception_only 数据集 ~40-49% 重复，有效训练样本不足？\" | 重复源自 representation compactness：同题多个 passing 解均无异常 → 相同 trace。**非数据泄漏**（train-test input overlap = 0）。raw_traces 仅 1.81% 重复，确认重复是 exception_only 表征特性而非数据收集问题。模型在有效样本仅 2858 unique 的条件下仍达 99.83%，反而说明 exception signal 的高 learnability — 少量 unique 样本即可充分学习 fault detection pattern。 |\n\n## Discussion 要点\n\n### D1: eval_loss vs verdict accuracy 解耦\nDeepSeek VOTA: eval_loss epoch1→3 从 0.068 升至 0.112 (+65%), 但 accuracy 从 78.15% 升至 84.45% (+6.3pp). Token-level calibration 与 binary classification accuracy 方向相反. **Implication**: verdict tasks 应用 task-specific metric (accuracy/F1) 做 checkpoint selection, 非 eval_loss.\n\n### D2: CRUXEval gap 假说 (revised — D030 confound)\nVOTA 跨模型 gap (14.96pp) 与 CRUXEval execution reasoning gap (15-17.5pp) 数值吻合. 假说: trace utilization effectiveness 受 base model \"execution reasoning readiness\" 约束. **标注**: hypothesis, N=2, 列出 alternatives. 不 overclaim. **注意**: 我们的训练/测试数据来自 HumanEval + MBPP-sanitized（非 CRUXEval），CRUXEval-I 分数仅作为衡量两个模型 execution reasoning 能力差异的外部参照。论文中必须明确区分数据来源与外部基准引用。**D030/D034 truncation evidence**: 14.96pp gap 中截断效应有因果证据: group_analysis 显示 train-truncated 83.04% vs train-intact 100% (Fisher p≈0, 推理时无截断)。截断因果方向可 claim，模型能力差异是 residual confound。CRUXEval gap 数值吻合可能部分巧合。论文中截断效应应作为 established factor 讨论（有 group_analysis 因果证据），模型能力假说标注为 residual confound hypothesis。\n\n### D3: Simplicity as robustness (revised)\nException signal 在两模型上均为最优组件，其结构简单性确保了相对优势的跨模型 robustness。但 DeepSeek seed sensitivity 揭示：simplicity 确保 signal 本身 robust，但 LoRA 训练过程是否稳定收敛到正确映射取决于模型。**trace design 应匹配 deployment model 的能力下界**，且需关注 training stability（建议：多 seed 验证 + 考虑 training stabilization 技巧如 warmup、learning rate schedule）。\n\n### D4: Checkpoint selection 与 gap 报告 (revised)\n正文报告所有 seeds 的 final checkpoint 结果 + best checkpoint 结果，不 cherry-pick。DeepSeek seed42: epoch1=99.83%, epoch3=99.33%（退化 0.50pp）。DeepSeek seed123: epoch1=91.43%, epoch3=91.09%（退化 0.34pp）。两个 seed 均显示轻微 epoch 退化，但核心差异在 epoch1 起点（8.40pp gap），不是训练过程。\n\n### D5: Irreducible samples — GeneratorExit 根因分析\n3 seeds 的 2/1190 errors 完全相同（id=901, 905, 均来自 HumanEval/95 `check_dict_case`），方向一致（pass→fail false negatives）。\n\n**根因**: Python `all()` 对 generator expression 短路时丢弃未耗尽的 generator，触发 `GeneratorExit`。`GeneratorExit` 继承自 `BaseException`（非 `Exception`），是 Python 内部控制流机制而非真正错误。但 tracer 对所有 caught exceptions 统一标记 `[ERROR]`，导致 exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。\n\n**为何不可约**:\n1. **表征局限**: exception_only 条件下模型仅见异常数据，无法访问控制流、返回值或 assertion 结果。`GeneratorExit` 在此表征中与真正错误不可区分。\n2. **跨 seed 确定性**: 3 个 random seeds 产生完全相同的 errors，确认这是 data/representation 属性而非模型初始化随机性。\n3. **训练集无信号**: 整个 1190 条测试集仅这 2 条含 `GeneratorExit`，训练集中也缺乏足够的 `GeneratorExit` 良性样本供模型学习。\n4. **人类也会犯错**: 仅看 exception trace（7 行 `[ERROR]`），人类审查者在不了解 Python generator protocol 的情况下也会预测 fail。\n\n**对论文的意义**: (1) 99.83% 是 exception_only representation 在此数据集上的理论 ceiling，非 saturation artifact；(2) 揭示 tracer 设计的改进方向——区分 `BaseException` 子类（如 `GeneratorExit`, `KeyboardInterrupt`）与 `Exception` 子类（真正的程序错误）可消除此类 irreducible error；(3) 提供 concrete evidence 说明 exception_only 模型\"理解\"的是 `[ERROR]` tag 的 fault indicator 语义，而非 exception type 的 fine-grained 含义。\n\n### D6: Calibration as secondary evidence\nCalibration 数据提供独立于 accuracy 的 evidence dimension。no_trace Brier=0.1972 说明模型无 trace 时不仅预测错，且对错误预测过度自信。exception_only Brier=0.0013 说明模型在有 exception signal 时几乎完美区分确定性和不确定性。这支持 Claim 1 的 \"sufficient signal\" 论点——exception 不仅让模型预测对，还让模型 \"知道自己对\"。\n\n### D7: Early stopping for exception signal (revised — D030 epoch1 data complete)\n3-seed epoch1 完整数据：seed42 epoch1=99.83% → epoch3=99.33%（-0.50pp）；**seed456 epoch1=99.33% → epoch3=99.33%（0.00pp）**；seed123 epoch1=91.43% → epoch3=91.09%（-0.34pp）。**seed42 的 epoch1=99.83%（匹配 Qwen）是该 seed 独有的 LoRA 初始化运气，不是 DeepSeek epoch1 的通用属性。** seed456 epoch1=epoch3 说明 epoch 退化非普遍现象。核心差异仍是 LoRA 初始化（epoch1 起点差 8.40pp），不是 overfitting。Early stopping 无法挽救差的初始化（seed123）。**Implication**: (1) 报告 DeepSeek 结果时应使用 median/2-of-3 (99.33%)，不应以 seed42 epoch1=99.83% 作为 headline；(2) epoch1 peak 是 LoRA 初始化运气的副产物，不具推广性。对比: VOTA 在 DeepSeek 上 84.45% **已确认正确**（D030 关闭: confirmatory re-eval max_length=16384 → 84.45%，与原始训练评估精确一致；D030 根因是 evaluate.py v2 的 max_length=2048 eval-time 截断 bug 导致 82.6% 预测为 garbage tokens）。\n\n### D9: LoRA initialization sensitivity as secondary bottleneck [NEW — D028]\nDeepSeek exception_only seed42=99.83% vs seed123=91.43% (epoch1), 8.40pp gap。Qwen 3 seeds 完全一致。假说：exception signal 的 learnability 取决于 (1) signal 本身的结构简单性（cross-model robust）+ (2) LoRA 初始化是否落入能正确映射 exception→verdict 的 basin。Qwen-7B 可能因模型更强/LoRA landscape 更平滑而对初始化不敏感。DeepSeek-6.7B（CRUXEval-I 39% vs Qwen 56.5%）的 loss landscape 可能更 rugged，LoRA 初始化更易陷入 suboptimal basin（seed123 的 fail_recall 仅 70-72% 说明模型未学到 exception→fail 映射的关键部分）。**论文角度**: 这不是 negative result——它揭示了 trace SFT 的 practical consideration（training stability），可作为 contribution 的一部分。建议 Discussion 讨论 training stabilization 策略（warmup, lr schedule, LoRA rank 调整, multi-seed selection）。\n\n### D10: Train loss ≈ but accuracy ≠ across seeds [NEW — D029]\nDeepSeek exception_only seed456 (train_loss=0.1225) 与 seed123 (train_loss=0.122) 训练损失几乎相同，但 accuracy 差 8.2pp（99.33% vs 91.09%）。关键差异集中在 fail_recall（1.0 vs 0.705）——token-level loss 在所有 tokens 上平均，掩盖了 fail 类少数样本的 sample-level 分类能力差异。**Implication**: (1) 扩展 D1 (eval_loss vs accuracy decoupling) 到训练阶段：train_loss 同样不是 verdict task accuracy 的可靠代理指标；(2) 对 checkpoint selection 的实际建议更强：必须用 task-specific metric (accuracy/F1)，甚至 train_loss 收敛也不保证 task performance；(3) fail 类作为少数类（28.5%），其学习质量被平均 loss 稀释——这在 class-imbalanced 设置下是 general pattern，可推广到其他 verdict/detection 任务。\n\n### D11: VOTA cross-model gap: training-time trace truncation as causal factor [NEW — D030 token analysis + group_analysis]\nD030 token analysis 确认: `to_chat_text()` 保留 labels（verdict label 在训练时未被截断），但 91.7% 的 DeepSeek VOTA 训练样本的 **trace content** 从 mean 2626 tokens 被截断到 ~2048 tokens。\n\n**Group analysis 提供因果证据**: 将测试集按训练截断状态分组（推理时无截断, max_length=16384），train-truncated 组 accuracy=83.04% vs train-intact 组 accuracy=100%, Fisher exact p≈0。**截断的因果方向可以 claim**: 训练时 trace 被截断导致模型学到的信息不完整 → 推理时即使看到完整 trace 也无法正确判断。模型能力差异是残余 confound（无法完全分离）。\n\n**Implications**: (1) 论文中所有 \"right-truncation corrupts/removes the verdict label\" 措辞对 VOTA 不成立——label 完整保留，被截断的是 trace INPUT content；(2) 14.96pp gap 中截断效应有因果证据（group_analysis），模型能力差异是 residual confound；(3) exception_only 因 token 长度短（远低于 2048）不受截断影响，其跨模型对比更 clean——进一步强化 Claim 1 \"most robust component\" 叙事；(4) 论文应讨论 max_length 的影响作为 limitation/future work；(5) group_analysis 数据可作为 Table/Figure 纳入论文——展示截断的因果效应。\n\n### D8: Data duplication as representation signature\nexception_only 训练集 39.45% 重复（4720→2858 unique），测试集 48.99%（1190→607 unique），而 raw_traces 仅 1.81%（5910→5803 unique）。重复源自 exception_only 表征的 design-by-intent compactness：同一编程题的多个 passing 解执行时均无异常，exception_only 表征退化为相同的空标记。这一数据特征本身就是 Claim 3 two-tier hierarchy 的佐证——Tier 1 信号仅编码 fault presence/absence，不编码 solution-level details，因此天然高重复。Train-test input overlap = 0 排除数据泄漏。\n\n## Contingency Framing (已解决, 留存档)\n\n### Claim 1 — RESOLVED (D029: seed456=99.33% confirms \"consistently best component\")\nseed456 与 seed42 完全一致（均 99.33%），seed123 为孤立离群值。Claim 1 定稿为 \"exception events consistently best component across models; absolute performance seed-dependent on DeepSeek (2/3 seeds robust, 1 outlier from LoRA init sensitivity); relative dominance over all alternatives robust across all seeds\"。\"0pp universal gap\" 叙事已放弃，转为数据驱动的 nuanced framing。\n\n### Claim 2 — RESOLVED (D006 + D009)\nv5 full_trace 81.76%. plan_002 label-only 86.22%, gradient dilution = minor (26%). 跨模型 VOTA gap 补充证据.\n\n## 与 v1 Framing 的关键差异\n\n| 维度 | v1 | v2.9 |\n|------|----|----|\n| Headline | VOTA compression 优于 full trace | Exception events are the most effective diagnostic signal |\n| Primary claim | VOTA +24pp through fault indicator preservation | Exception signal consistently best across models; absolute performance seed-dependent on DeepSeek |\n| Claim 2 | Compression > full trace (只有 gradient dilution) | Information density primary + gradient dilution quantification + cross-model reinforcement |\n| Claim 3 Tier 1 | exception_only only | exception + assertion-point (co-Tier 1, D020) |\n| VOTA 定位 | 核心方法 — trace compression | **Fault indicator isolation** — 价值在于提取 exception, 非 generic compression |\n| Model scope | 单模型 (Qwen) | 双模型, 跨模型对比是核心贡献 |\n| DeepSeek full_trace | N/A | v1 collapsed (label truncation), v3 pending |\n| Seed robustness | 未验证 | Qwen ✅ 99.83% ± 0.00 (3 seeds); DeepSeek ⚠️ seed-dependent (91-99%, D028) |\n| Irreducible error | 未分析 | ✅ GeneratorExit 根因明确，99.83% = representation ceiling |\n| Calibration | 未验证 | ✅ 完整 ECE+Brier, ~63x/~150x gap vs no_trace |\n| Data duplication | 未分析 | ✅ exception_only ~40% 重复（representation compactness），train-test overlap = 0 |\n| Early stopping | 未讨论 | DeepSeek epoch1→epoch3 轻微退化 (0.3-0.5pp); 核心问题是 LoRA 初始化 (seed123 epoch1=91.43%), 非 overfitting |\n| Narrative arc | \"VOTA helps\" | \"Exception events are consistently best; VOTA's value is isolating them; training stability matters\" |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Ablation: 去除 VOTA 中 actual/expected 值对，只保留 assertion structure + exception\n    info。验证 VOTA 效果是 genuine behavioral understanding 还是 trivial string comparison。'\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: vota_no_ae_seed42\n  notes: 如果去 actual/expected 后 acc 仍 >80%，证明非 trivial；如果降到 ~75%(=no_trace)，则是字符串比对。决定\n    Claim 1 强度和论文 framing。\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.994\n    majority_baseline: 0.7151\n    lift: 0.279\n    n: 1190\n    pass_f1: 0.996\n    fail_f1: 0.989\n    accuracy_ci_lower: 0.989\n    accuracy_ci_upper: 0.998\n    lift_vs_notrace: 0.243\n    lift_vs_notrace_ci_lower: 0.218\n    lift_vs_notrace_ci_upper: 0.268\n    train_loss: 0.0908\n    eval_loss: 0.2215\n    wall_clock_seconds: 6397.88\n- id: plan_002\n  claim: 2\n  description: 'Ablation: full_trace + label-only loss (只对分类 token 计算 loss，mask trace\n    tokens)。验证 collapse 根因是 gradient dilution 而非数据/代码 bug。'\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: full_trace_label_only_seed42\n  notes: 如果 label-only loss 修复 collapse (acc >70%)，确认 gradient dilution 假说。如果仍 collapse，可能是\n    trace noise/length 本身就有害。\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8622\n    accuracy_ci_lower: 0.8437\n    accuracy_ci_upper: 0.8807\n    majority_baseline: 0.7151\n    lift: 0.1471\n    n: 1190\n    pass_precision: 0.8821\n    pass_recall: 0.9318\n    pass_f1: 0.9063\n    fail_precision: 0.8007\n    fail_recall: 0.6873\n    fail_f1: 0.7397\n    train_loss: 0.2505\n    eval_loss: 0.3205\n    lift_vs_notrace: 0.1109\n    lift_vs_notrace_ci_lower: 0.0849\n    lift_vs_notrace_ci_upper: 0.137\n    lift_vs_standard_fulltrace: 0.0445\n    lift_vs_standard_fulltrace_ci_lower: 0.0235\n    lift_vs_standard_fulltrace_ci_upper: 0.0655\n    lift_vs_standard_fulltrace_pvalue: 0\n- id: plan_003\n  claim: 3\n  description: 'VOTA component ablation: 分别测试 (a) 只有 actual/expected, (b) 只有 exception\n    summary, (c) 只有 loop compression, (d) 全量 VOTA。量化每个组件的贡献。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  registry_id: vota_loop_only_seed42\n  notes: '4 个 sub-conditions。registry IDs: vota_loop_only_seed42 (loop_only 85.6%),\n    vota_exception_only_seed42_v2 (exception_only 99.83%), vota_ae_only_seed42 (ae_only\n    99.92%)。plan_001 vota_no_ae_seed42 (99.4%) 覆盖 ae 冗余确认。'\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8563\n    majority_baseline: 0.7151\n    lift: 0.1412\n    n: 1190\n    pass_precision: 0.9239\n    pass_recall: 0.8707\n    pass_f1: 0.8966\n    fail_precision: 0.7165\n    fail_recall: 0.8201\n    fail_f1: 0.7648\n    accuracy_ci:\n    - 0.8353\n    - 0.8756\n    bootstrap_vs_no_trace:\n      diff: 0.105\n      ci:\n      - 0.0824\n      - 0.1286\n      significant: true\n    bootstrap_vs_vota:\n      diff: -0.1378\n      ci:\n      - -0.1571\n      - -0.1185\n      significant: true\n    bootstrap_vs_full_trace:\n      diff: 0.0387\n      ci:\n      - 0.0185\n      - 0.0597\n      significant: true\n    train_loss: 0.0718\n    wall_clock_seconds: 7425.65\n- id: plan_004\n  claim: 1\n  description: '第二模型验证: DeepSeek-Coder-6.7B 上复现 4 条件（VOTA/no_trace/full_trace/exception_only），与\n    DCSH 同模型直接对比。exception_only 跨模型验证 exception dominance。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  registry_id: deepseek_exception_only_seed42\n  notes: '4 条件: deepseek_vota_seed42 (84.45% ✅), deepseek_no_trace_seed42 (73.36%\n    ✅), deepseek_exception_only_seed42 (99.33% ✅), deepseek_full_trace_seed42_v3 (RUNNING,\n    label truncation fix). 3/4 完成, full_trace v3 待完成。'\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9933\n    majority_baseline: 0.7151\n    lift: 0.2782\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9906\n    pass_f1: 0.9953\n    fail_precision: 0.9769\n    fail_recall: 1\n    fail_f1: 0.9883\n    epoch1_checkpoint_eval:\n      accuracy: 0.9983\n      fail_recall: 1\n      fail_precision: 0.9941\n      pass_recall: 0.9976\n      conclusion: epoch1_better_by_0.50pp\n- id: plan_005\n  claim: 1\n  description: '第二任务验证: 在 DebugBench subset 上测试 exception_only/VOTA/no_trace。验证 verdict\n    task 跨任务泛化性。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps:\n  - plan_001\n  registry_id: debugbench_exception_only_seed42\n  notes: 3/3 完成。debugbench_exception_only_seed42=100.0% (426/426, Wilson CI [99.14%,100%]),\n    debugbench_vota_seed42=99.77% (1 error), debugbench_no_trace_seed42=96.71%。定位为\n    generalization validation（非 trace importance evidence，因 no_trace baseline 96.71%\n    已很高，marginal contribution 仅 3.29pp）。\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 1\n    majority_baseline: 0.5141\n    lift: 0.4859\n    n: 426\n    pass_precision: 1\n    pass_recall: 1\n    pass_f1: 1\n    fail_precision: 1\n    fail_recall: 1\n    fail_f1: 1\n    accuracy_ci_wilson:\n    - 0.9914\n    - 1\n    accuracy_ci_bootstrap:\n    - 1\n    - 1\n    train_loss: 0.2435\n    eval_loss: 0.4157\n    train_runtime_sec: 837\n- id: plan_006\n  claim: 2\n  description: 'Trace length ablation: 测试不同截断长度 (256/512/1024/no_limit) 对 full_trace\n    准确率的影响。2048tok 取消（train_sft.py 硬编码 max_length=2048，与 no_limit 等价）。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  registry_id: full_trace_256tok_seed42\n  notes: '4 点设计: 256tok=78.82% (DONE), 512tok=80.42% (DONE), 1024tok (RUNNING), no_limit=81.76%\n    (full_trace_seed42_v5)。2048tok killed（max_length=2048 硬编码使其与 no_limit 等价）。Registry\n    IDs: full_trace_256tok_seed42, full_trace_512tok_seed42, full_trace_1024tok_seed42,\n    full_trace_seed42_v5。趋势: 更多 trace 略有帮助但收益递减，且全部远低于 exception_only (99.83%)。'\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.7882\n    majority_baseline: 0.7151\n    lift: 0.0731\n    n: 1190\n    pass_precision: 0.903\n    pass_recall: 0.788\n    pass_f1: 0.842\n    fail_precision: 0.597\n    fail_recall: 0.788\n    fail_f1: 0.679\n    accuracy_ci:\n    - 0.764\n    - 0.81\n    train_loss: 0.1094\n    train_runtime_sec: 3047\n    epochs: 3\n- id: plan_007\n  claim: 3\n  description: 'Calibration analysis: ECE + reliability diagrams 对比 VOTA/no_trace/full_trace\n    的 calibration 质量。验证 trace SFT 对 verdict task 改善 calibration 的假说。'\n  priority: P2\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: calibration_analysis_seed42\n  notes: 纯 eval，不需要额外训练。用已有 checkpoint 的 logits 计算。\n  status: DONE\n  conclusion: success\n  metrics:\n    no_trace:\n      ece: 0.171476\n      mce: 0.475643\n      brier_score: 0.197152\n      accuracy: 0.751261\n      n_samples: 1190\n    full_trace:\n      ece: 0.095817\n      mce: 0.249061\n      brier_score: 0.143924\n      accuracy: 0.817647\n      n_samples: 1190\n    label_only:\n      ece: 0.110686\n      mce: 0.417124\n      brier_score: 0.120144\n      accuracy: 0.862185\n      n_samples: 1190\n    loop_only:\n      ece: 0.083085\n      mce: 0.183406\n      brier_score: 0.118335\n      accuracy: 0.856303\n      n_samples: 1190\n    ae_only:\n      ece: 0.000415\n      mce: 0.000415\n      brier_score: 0.000847\n      accuracy: 0.99916\n      n_samples: 1190\n    exception_only:\n      ece: 0.002717\n      mce: 0.835484\n      brier_score: 0.001311\n      accuracy: 0.998319\n      n_samples: 1190\n    vota:\n      ece: 0.00541\n      mce: 0.622459\n      brier_score: 0.005234\n      accuracy: 0.994118\n      n_samples: 1190\n- id: plan_008\n  claim: 1\n  description: 'Seed robustness: 3 random seeds (42/123/456) 验证 VOTA 结果稳定性。McNemar\n    test + bootstrap CI。'\n  priority: P2\n  gpu_budget_hours: 6\n  deps:\n  - plan_001\n  registry_id: exception_only_seed456\n  notes: 'Seed robustness 完成。Qwen exception_only: 99.83% ± 0.00 (seeds 42/123/456,\n    irreducible 2/1190). Qwen VOTA: seed42=99.41%, seed456=99.08% (Δ<0.4pp). DeepSeek\n    exception_only: seed42/456=99.33%, seed123=91.09% (LoRA outlier). Registry IDs:\n    exception_only_seed123, exception_only_seed456, vota_seed456_v2, deepseek_exception_only_seed42/123/456.'\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    accuracy_ci:\n    - 0.9958\n    - 1\n    majority_baseline: 0.7151\n    lift: 0.2832\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9976\n    pass_f1: 0.9988\n    fail_precision: 0.9941\n    fail_recall: 1\n    fail_f1: 0.9971\n    vs_seed42:\n      seed42_accuracy: 0.9983\n      seed456_accuracy: 0.9983\n      diff: 0\n      note: identical accuracy to 4 decimal places; no predictions.jsonl for paired\n        bootstrap\n    train_loss: 0.1087\n    eval_loss: 0.4629\n    train_runtime_sec: 4541\n    epochs: 3\n- id: plan_mvp_vota\n  claim: 1\n  description: 'MVP: VOTA trace SFT for test verdict prediction'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: vota_seed42_v4\n  notes: 完成。95.63% accuracy, +20.5pp over baseline.\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9563\n    majority_baseline: 0.7151\n    lift: 0.2412\n    n: 1190\n    pass_precision: 0.944\n    pass_recall: 0.998\n    pass_f1: 0.97\n    fail_precision: 0.993\n    fail_recall: 0.853\n    fail_f1: 0.917\n    lift_vs_notrace: 0.205\n    lift_vs_notrace_ci_lower: 0.177\n    lift_vs_notrace_ci_upper: 0.234\n    train_loss: 0.046\n    eval_loss: 0.0842\n- id: plan_mvp_notrace\n  claim: 1\n  description: 'MVP: No-trace baseline for test verdict prediction'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: no_trace_seed42_v4\n  notes: 完成。75.13% accuracy (majority baseline 71.51%).\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7513\n    majority_baseline: 0.7151\n    lift: 0.0361\n    pass_precision: 0.8776\n    pass_recall: 0.7579\n    pass_f1: 0.8134\n    fail_precision: 0.5473\n    fail_recall: 0.7345\n    fail_f1: 0.6272\n    train_loss: 0.18\n    eval_loss: 0.6454\n    eval_mean_token_accuracy: 0.8897\n- id: plan_mvp_fulltrace\n  claim: 2\n  description: 'MVP: Full execution trace SFT for test verdict prediction'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: full_trace_seed42_v2\n  notes: 完成。28.49% accuracy, model collapse (100% predict fail).\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.284\n    majority_baseline: 0.7151\n    lift: -0.4311\n    n: 1190\n    pass_precision: 0.923\n    pass_recall: 0.085\n    pass_f1: 0.155\n    fail_precision: 0.445\n    fail_recall: 0.785\n    fail_f1: 0.568\n    train_loss: 0.0373\n    eval_loss: 0.082\n    eval_mean_token_accuracy: 0.984\n- id: plan_012\n  claim: 1\n  description: 'Cross-scale validation: Qwen-2.5-Coder-1.5B 上复现 4 条件 (exception_only/vota/no_trace/full_trace)。\n    验证 exception signal 的 scale invariance 假说。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_003\n  registry_id: qwen15b_exception_only_seed42\n  notes: '4 条件: exception_only=99.83% (=7B, DONE), vota=99.58% (DONE), no_trace=67.31%\n    (DONE), full_trace=RUNNING。关键发现: 1.5B=7B on exception → signal-limited not capacity-limited。\n    Registry IDs: qwen15b_exception_only_seed42, qwen15b_vota_seed42, qwen15b_no_trace_seed42,\n    qwen15b_full_trace_seed42。'\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    accuracy_ci_lower: 0.9958\n    accuracy_ci_upper: 1\n    majority_baseline: 0.7151\n    lift: 0.283\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9976\n    pass_f1: 0.9988\n    fail_precision: 0.9941\n    fail_recall: 1\n    fail_f1: 0.9971\n    train_loss: 0.1347\n    eval_loss: 0.5761\n    wall_clock_seconds: 1762\n- id: plan_013\n  claim: 1\n  description: 'Cross-family validation: CodeLlama-13B-Instruct 上测试 3 条件 (exception_only/no_trace/vota)。\n    验证 exception dominance 跨 LLaMA 家族 + 更大 scale 的泛化性。'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: codellama13b_exception_only_seed42\n  notes: 'Model downloaded. 0/3 done, queued. Registry IDs: codellama13b_exception_only_seed42,\n    codellama13b_no_trace_seed42, codellama13b_vota_seed42。回应 R2-N2 scope concern:\n    4 models × 3 families × 2 scales。'\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    accuracy_ci_lower: 0.9958\n    accuracy_ci_upper: 1\n    pass_f1: 0.9988\n    fail_f1: 0.9971\n    n_test: 1190\n- id: plan_014\n  claim: 3\n  description: 'Multi-seed expansion: loop_only + ae_only + label_only 各 3 seeds。\n    回应 R2-N3 single-seed concern，验证 Tier 层级划分稳定性。'\n  priority: P0\n  gpu_budget_hours: 12\n  deps:\n  - plan_003\n  registry_id: ae_only_seed123\n  notes: 'ae_only 3-seed done (mean 99.64%). label_only 3-seed done (mean 86.39%).\n    loop_only: seed42 done, seed123 RUNNING, seed456 queued。Registry IDs: ae_only_seed123/456,\n    label_only_seed123/456, loop_only_seed123/456。'\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9908\n    n: 1190\n    pass_recall: 0.987\n    fail_recall: 1\n    majority_baseline: 0.7151\n    lift: 0.2757\n- id: plan_015\n  claim: 1\n  description: 'Format marker removal control: 移除 [No exception data in trace] 格式标记后重训\n    exception_only × 3 seeds。回应 R1-N1 format shortcut concern。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exception_only_nomarker_seed42\n  notes: '计划中。如果移除标记后 SFT 仍 ≥99%，证明模型学到的是异常语义而非格式 shortcut。 Registry IDs: exception_only_nomarker_seed42/123/456。'\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9655\n    n: 1190\n    accuracy_ci:\n    - 0.955\n    - 0.976\n- id: plan_016\n  claim: 1\n  description: 'Fine-grained phase transition: tail-384 × 4 模型，精确定位 256→512 phase\n    transition 是 sharp 还是 gradual。'\n  priority: P1\n  gpu_budget_hours: 16\n  deps:\n  - plan_006\n  notes: 4 模型各 1 个实验。如果 tail-384 仍在 ~77% (≈tail-256)，证明 transition 是 sharp；如果 ~85%，证明是\n    gradual。对 phase transition claim 的强度有决定性影响。\n  status: planned\n- id: plan_017\n  claim: 1\n  description: 'Cross-seed budget curve: tail-512 × 4 模型 × 3 seeds，验证 phase transition\n    后 convergence band 的 robustness。'\n  priority: P1\n  gpu_budget_hours: 24\n  deps:\n  - plan_016\n  notes: tail-512 是 phase transition 后第一个点，验证 93-97% convergence 是否 seed-robust。审稿人必问\n    single-seed robustness。\n  status: planned\n- id: plan_018\n  claim: 1\n  description: 'Error analysis: 用已有 predictions.jsonl 分析 failure modes（哪类程序/错误容易被误判）。不需\n    GPU。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  notes: 分析 exception_only/vota/full_trace/no_trace 的错误模式差异。重点关注 Tier 1 vs Tier 2\n    的 failure mode 是否不同。\n  status: planned\n- id: plan_019\n  claim: 1\n  description: 'Cross-model calibration: 4 模型 × exception_only 的 ECE/Brier 对比。验证 calibration\n    quality 跨模型 universal。'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  notes: 纯 eval，用已有 checkpoint。当前只有 Qwen-7B 的 calibration 数据，需要扩展到 4 模型。\n  status: planned\n- id: plan_020\n  claim: 2\n  description: 'Few-shot prompting baseline: GPT-4o/Claude 直接判断 pass/fail（0-shot +\n    3-shot），作为 non-SFT upper bound 对比。'\n  priority: P2\n  gpu_budget_hours: 0\n  deps: []\n  notes: 不需 GPU，用 API 调用。如果 few-shot < exception_only SFT，说明 SFT 在 verdict task 上超越\n    frontier model 的 few-shot 能力，claim 更强。\n  status: planned\n- id: plan_021\n  claim: 1\n  description: 'OOD generalization: 在不同编程语言/项目的 trace 上测试 exception_only 泛化性。'\n  priority: P2\n  gpu_budget_hours: 12\n  deps: []\n  notes: 需要构建 OOD 测试集（不同语言的 trace）。如果 exception_only 在 OOD 上仍强，大幅强化 generalization\n    claim。\n  status: planned\n- id: plan_022\n  claim: 2\n  description: 'Training dynamics: 记录 exception_only vs full_trace 的 learning curve（每\n    50 steps eval），分析收敛速度差异。'\n  priority: P2\n  gpu_budget_hours: 8\n  deps: []\n  notes: 如果 exception_only 收敛更快，支持 information density 假说。需要修改训练脚本加 intermediate eval。\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: no_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: vota_seed42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: no_trace_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: vota_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: no_trace_seed42_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    train_loss: 0.18\n    eval_loss: 0.645\n    eval_mean_token_accuracy: 0.89\n    accuracy: 0.7513\n    majority_baseline: 0.7151\n    lift: 0.0361\n    pass_precision: 0.8776\n    pass_recall: 0.7579\n    pass_f1: 0.8134\n    fail_precision: 0.5473\n    fail_recall: 0.7345\n    fail_f1: 0.6272\n- exp_id: vota_seed42_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    train_loss: 0.046\n    eval_loss: 0.085\n    eval_mean_token_accuracy: 0.983\n    accuracy: 0.992\n    majority_baseline: 0.7151\n    lift: 0.276\n    pass_precision: 0.99\n    pass_recall: 0.99\n    pass_f1: 0.99\n    fail_precision: 0.99\n    fail_recall: 0.99\n    fail_f1: 0.99\n- exp_id: full_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    train_loss: 0.037\n    eval_loss: 0.084\n    eval_mean_token_accuracy: 0.984\n    accuracy: 0.284\n    majority_baseline: 0.7151\n    lift: -0.431\n    pass_precision: 0.88\n    pass_recall: 0.08\n    pass_f1: 0.16\n    fail_precision: 0.31\n    fail_recall: 0.97\n    fail_f1: 0.57\n- exp_id: no_trace_seed42_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7513\n    majority_baseline: 0.7151\n    lift: 0.0361\n    pass_precision: 0.8776\n    pass_recall: 0.7579\n    pass_f1: 0.8134\n    fail_precision: 0.5473\n    fail_recall: 0.7345\n    fail_f1: 0.6272\n    train_loss: 0.18\n    eval_loss: 0.6454\n    eval_mean_token_accuracy: 0.8897\n- exp_id: vota_seed42_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9563\n    majority_baseline: 0.7151\n    lift: 0.2412\n    n: 1190\n    pass_precision: 0.944\n    pass_recall: 0.998\n    pass_f1: 0.97\n    fail_precision: 0.993\n    fail_recall: 0.853\n    fail_f1: 0.917\n    lift_vs_notrace: 0.205\n    lift_vs_notrace_ci_lower: 0.177\n    lift_vs_notrace_ci_upper: 0.234\n    train_loss: 0.046\n    eval_loss: 0.0842\n- exp_id: full_trace_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.284\n    majority_baseline: 0.7151\n    lift: -0.4311\n    n: 1190\n    pass_precision: 0.923\n    pass_recall: 0.085\n    pass_f1: 0.155\n    fail_precision: 0.445\n    fail_recall: 0.785\n    fail_f1: 0.568\n    train_loss: 0.0373\n    eval_loss: 0.082\n    eval_mean_token_accuracy: 0.984\n- exp_id: full_trace_seed42_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8176\n    majority_baseline: 0.7151\n    lift: 0.1025\n    n: 1190\n    pass_precision: 0.8774\n    pass_recall: 0.866\n    pass_f1: 0.8717\n    fail_precision: 0.6743\n    fail_recall: 0.6962\n    fail_f1: 0.6851\n    accuracy_ci_lower: 0.797\n    accuracy_ci_upper: 0.839\n    lift_vs_notrace: 0.0664\n    lift_vs_notrace_ci_lower: 0.0437\n    lift_vs_notrace_ci_upper: 0.0899\n    train_loss: 0.05\n    eval_loss: 0.0867\n    wall_clock_seconds: 7852\n    epoch_level:\n      epoch1_accuracy: 0.8303\n      epoch2_accuracy: 0.763\n      final_accuracy: 0.8176\n      trend: non_monotonic_epoch1_best_epoch2_collapse\n- exp_id: vota_seed42_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9941\n    majority_baseline: 0.7151\n    lift: 0.279\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9882\n    pass_f1: 0.9941\n    fail_precision: 0.9714\n    fail_recall: 1\n    fail_f1: 0.9855\n    lift_vs_notrace: 0.2428\n    lift_vs_notrace_ci_lower: 0.2185\n    lift_vs_notrace_ci_upper: 0.2681\n    accuracy_ci_lower: 0.9882\n    accuracy_ci_upper: 0.9983\n    train_loss: 0.05\n    eval_loss: 0.0867\n    eval_mean_token_accuracy: 0.9828\n    wall_clock_seconds: 8443\n    epoch_level:\n      epoch1_accuracy: 0.9933\n      epoch2_accuracy: 0.9941\n      final_accuracy: 0.9941\n      trend: monotonic_increasing_then_stable\n- exp_id: no_trace_seed42_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7513\n    accuracy_ci_lower: 0.7277\n    accuracy_ci_upper: 0.7748\n    majority_baseline: 0.7151\n    lift: 0.0361\n    lift_ci_lower: 0.0042\n    lift_ci_upper: 0.0706\n    n: 1190\n    pass_precision: 0.8776\n    pass_recall: 0.7579\n    pass_f1: 0.8134\n    fail_precision: 0.5473\n    fail_recall: 0.7345\n    fail_f1: 0.6272\n    epoch_level:\n      epoch1_accuracy: 0.7429\n      epoch2_accuracy: 0.763\n      final_accuracy: 0.7513\n      trend: non_monotonic_epoch2_best\n- exp_id: full_trace_label_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8622\n    accuracy_ci_lower: 0.8437\n    accuracy_ci_upper: 0.8807\n    majority_baseline: 0.7151\n    lift: 0.1471\n    n: 1190\n    pass_precision: 0.8821\n    pass_recall: 0.9318\n    pass_f1: 0.9063\n    fail_precision: 0.8007\n    fail_recall: 0.6873\n    fail_f1: 0.7397\n    train_loss: 0.2505\n    eval_loss: 0.3205\n    lift_vs_notrace: 0.1109\n    lift_vs_notrace_ci_lower: 0.0849\n    lift_vs_notrace_ci_upper: 0.137\n    lift_vs_standard_fulltrace: 0.0445\n    lift_vs_standard_fulltrace_ci_lower: 0.0235\n    lift_vs_standard_fulltrace_ci_upper: 0.0655\n    lift_vs_standard_fulltrace_pvalue: 0\n- exp_id: vota_no_ae_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.994\n    majority_baseline: 0.7151\n    lift: 0.279\n    n: 1190\n    pass_f1: 0.996\n    fail_f1: 0.989\n    accuracy_ci_lower: 0.989\n    accuracy_ci_upper: 0.998\n    lift_vs_notrace: 0.243\n    lift_vs_notrace_ci_lower: 0.218\n    lift_vs_notrace_ci_upper: 0.268\n    train_loss: 0.0908\n    eval_loss: 0.2215\n    wall_clock_seconds: 6397.88\n- exp_id: vota_ae_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9992\n    accuracy_ci:\n    - 0.9975\n    - 1\n    bootstrap_pairwise:\n      ae_only_vs_no_trace:\n        diff: 0.2479\n        ci:\n        - 0.2235\n        - 0.2731\n        p_value: 0\n        significant: true\n      ae_only_vs_exception_only:\n        diff: 0.0008\n        ci:\n        - -0.0017\n        - 0.0034\n        p_value: 0.8002\n        significant: false\n      ae_only_vs_vota:\n        diff: 0.005\n        ci:\n        - 0.0017\n        - 0.0092\n        p_value: 0.0046\n        significant: true\n    config:\n      n_bootstrap: 10000\n      seed: 42\n      method: paired_bootstrap\n- exp_id: vota_exception_only_seed42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: vota_loop_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8563\n    majority_baseline: 0.7151\n    lift: 0.1412\n    n: 1190\n    pass_precision: 0.9239\n    pass_recall: 0.8707\n    pass_f1: 0.8966\n    fail_precision: 0.7165\n    fail_recall: 0.8201\n    fail_f1: 0.7648\n    accuracy_ci:\n    - 0.8353\n    - 0.8756\n    bootstrap_vs_no_trace:\n      diff: 0.105\n      ci:\n      - 0.0824\n      - 0.1286\n      significant: true\n    bootstrap_vs_vota:\n      diff: -0.1378\n      ci:\n      - -0.1571\n      - -0.1185\n      significant: true\n    bootstrap_vs_full_trace:\n      diff: 0.0387\n      ci:\n      - 0.0185\n      - 0.0597\n      significant: true\n    train_loss: 0.0718\n    wall_clock_seconds: 7425.65\n- exp_id: vota_exception_only_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    majority_baseline: 0.7151\n    lift: 0.2832\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.998\n    pass_f1: 0.999\n    fail_precision: 0.994\n    fail_recall: 1\n    fail_f1: 0.997\n    lift_vs_notrace: 0.2471\n    lift_vs_notrace_ci_lower: 0.2227\n    lift_vs_notrace_ci_upper: 0.2714\n    lift_vs_fulltrace: 0.1807\n    lift_vs_fulltrace_ci_lower: 0.1588\n    lift_vs_fulltrace_ci_upper: 0.2034\n    lift_vs_vota: 0.0067\n    lift_vs_vota_ci_lower: 0.0017\n    lift_vs_vota_ci_upper: 0.0126\n    lift_vs_vota_pvalue: 0.01\n- exp_id: deepseek_vota_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8445\n    majority_baseline: 0.7151\n    lift: 0.1294\n    accuracy_ci:\n    - 0.826\n    - 0.864\n    pass_precision: 0.821\n    pass_recall: 1\n    pass_f1: 0.902\n    fail_precision: 1\n    fail_recall: 0.454\n    fail_f1: 0.625\n    eval_loss_epoch1: 0.0679\n    eval_loss_epoch2: 0.095\n    eval_loss_epoch3: 0.1121\n    final_train_loss: 0.0522\n    epoch1_checkpoint_eval:\n      accuracy: 0.7815\n      accuracy_ci:\n      - 0.76\n      - 0.803\n      fail_recall: 0.233\n      fail_precision: 1\n      pass_recall: 1\n      pass_precision: 0.766\n      fail_f1: 0.378\n      pass_f1: 0.867\n      conclusion: epoch3_final_is_better\n    reeval_with_fixed_script:\n      accuracy: 0.16\n      accuracy_ci:\n      - 0.139\n      - 0.18\n      fail_f1: 0.61\n      fail_precision: 0.9\n      fail_recall: 0.47\n      pass_f1: 0.07\n      pass_precision: 1\n      pass_recall: 0.04\n      note: 'CATASTROPHIC: re-eval with corrected evaluate.py shows 16% (vs original\n        84.45%). Model predicts fail for almost everything. Previous 84.45% may have\n        been from buggy eval. NEEDS INVESTIGATION.'\n    group_analysis:\n      train_truncated:\n        n: 1091\n        accuracy: 0.8304\n        ci_95:\n        - 0.8075\n        - 0.8524\n        correct: 906\n        incorrect: 185\n        pass_accuracy: 1\n        pass_n: 822\n        fail_accuracy: 0.3123\n        fail_n: 269\n      train_intact:\n        n: 99\n        accuracy: 1\n        ci_95:\n        - 1\n        - 1\n        correct: 99\n        incorrect: 0\n        pass_accuracy: 1\n        pass_n: 29\n        fail_accuracy: 1\n        fail_n: 70\n      fisher_exact:\n        odds_ratio: 0\n        p_value: 0\n      overall_accuracy: 0.8445\n      max_length: 2048\n      note: 'Grouped by whether training sample content exceeded token budget (DeepSeek\n        tokenizer, max_length=2048). Inference used full-length input (no truncation).\n        All 185 errors from truncated group''s fail class (fail_recall=31.2%). Intact\n        group: 100% accuracy.'\n- exp_id: deepseek_no_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.7336\n    majority_baseline: 0.7151\n    lift: 0.0185\n    n: 1190\n    pass_precision: 0.817\n    pass_recall: 0.808\n    pass_f1: 0.813\n    fail_precision: 0.532\n    fail_recall: 0.546\n    fail_f1: 0.539\n    accuracy_ci:\n    - 0.708\n    - 0.757\n    lift_ci:\n    - -0.009\n    - 0.046\n- exp_id: deepseek_full_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy_no_truncation: 0.2849\n    accuracy_with_truncation_fix: 0.1059\n    accuracy_with_truncation_fix_ci:\n    - 0.089\n    - 0.123\n    majority_baseline: 0.7151\n    n: 1190\n    note: 'Both evals show model failure. No-truncation: all predict fail. With-truncation:\n      garbage tokens. LoRA training itself failed due to label truncation during training.'\n- exp_id: deepseek_exception_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9933\n    majority_baseline: 0.7151\n    lift: 0.2782\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9906\n    pass_f1: 0.9953\n    fail_precision: 0.9769\n    fail_recall: 1\n    fail_f1: 0.9883\n    epoch1_checkpoint_eval:\n      accuracy: 0.9983\n      fail_recall: 1\n      fail_precision: 0.9941\n      pass_recall: 0.9976\n      conclusion: epoch1_better_by_0.50pp\n- exp_id: calibration_analysis_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    no_trace:\n      ece: 0.171476\n      mce: 0.475643\n      brier_score: 0.197152\n      accuracy: 0.751261\n      n_samples: 1190\n    full_trace:\n      ece: 0.095817\n      mce: 0.249061\n      brier_score: 0.143924\n      accuracy: 0.817647\n      n_samples: 1190\n    label_only:\n      ece: 0.110686\n      mce: 0.417124\n      brier_score: 0.120144\n      accuracy: 0.862185\n      n_samples: 1190\n    loop_only:\n      ece: 0.083085\n      mce: 0.183406\n      brier_score: 0.118335\n      accuracy: 0.856303\n      n_samples: 1190\n    ae_only:\n      ece: 0.000415\n      mce: 0.000415\n      brier_score: 0.000847\n      accuracy: 0.99916\n      n_samples: 1190\n    exception_only:\n      ece: 0.002717\n      mce: 0.835484\n      brier_score: 0.001311\n      accuracy: 0.998319\n      n_samples: 1190\n    vota:\n      ece: 0.00541\n      mce: 0.622459\n      brier_score: 0.005234\n      accuracy: 0.994118\n      n_samples: 1190\n- exp_id: vota_seed123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: vota_seed456\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exception_only_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    accuracy_ci:\n    - 0.9958\n    - 1\n    majority_baseline: 0.7151\n    lift: 0.2832\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9976\n    pass_f1: 0.9988\n    fail_precision: 0.9941\n    fail_recall: 1\n    fail_f1: 0.9971\n    train_loss: 0.1096\n    train_runtime_sec: 7507\n    epochs: 3\n    seed_comparison:\n      seed42_accuracy: 0.9983\n      seed456_accuracy: 0.9983\n      seed123_accuracy: 0.9983\n      max_diff: 0\n      note: identical accuracy to 4 decimal places across all 3 seeds (42/456/123);\n        each has exactly 2/1190 errors; exception_only fully seed-robust\n- exp_id: exception_only_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    accuracy_ci:\n    - 0.9958\n    - 1\n    majority_baseline: 0.7151\n    lift: 0.2832\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9976\n    pass_f1: 0.9988\n    fail_precision: 0.9941\n    fail_recall: 1\n    fail_f1: 0.9971\n    vs_seed42:\n      seed42_accuracy: 0.9983\n      seed456_accuracy: 0.9983\n      diff: 0\n      note: identical accuracy to 4 decimal places; no predictions.jsonl for paired\n        bootstrap\n    train_loss: 0.1087\n    eval_loss: 0.4629\n    train_runtime_sec: 4541\n    epochs: 3\n- exp_id: deepseek_exception_only_seed123\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.9109\n    pass_precision: 1\n    pass_recall: 0.993\n    pass_f1: 0.996\n    fail_precision: 0.976\n    fail_recall: 0.705\n    fail_f1: 0.818\n    ci_95:\n    - 0.894\n    - 0.926\n    train_loss: 0.122\n    train_runtime_sec: 6384\n- exp_id: deepseek_full_trace_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: vota_seed456_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9908\n    pass_precision: 1\n    pass_recall: 0.987\n    pass_f1: 0.993\n    fail_precision: 0.969\n    fail_recall: 1\n    fail_f1: 0.984\n    ci_95:\n    - 0.985\n    - 0.996\n- exp_id: deepseek_full_trace_seed42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7916\n    majority_baseline: 0.7151\n    lift: 0.0765\n    n: 1190\n    pass_precision: 0.857\n    pass_recall: 0.851\n    pass_f1: 0.854\n    fail_precision: 0.632\n    fail_recall: 0.643\n    fail_f1: 0.637\n    accuracy_ci:\n    - 0.768\n    - 0.813\n    train_loss: 0.0547\n    train_runtime_seconds: 8891\n    epochs: 3\n    reeval_discrepancy:\n      reeval_accuracy: 0.285\n      reeval_note: 'RESOLVED: 28.5% was caused by eval max_length=16384 (OOD). Re-eval\n        with max_length=2048 reproduces 79.16%. predictions.jsonl updated to maxlen2048\n        results.'\n      status: RESOLVED\n- exp_id: deepseek_exception_only_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9933\n    majority_baseline: 0.7151\n    lift: 0.2782\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9906\n    pass_f1: 0.9953\n    fail_precision: 0.9769\n    fail_recall: 1\n    fail_f1: 0.9883\n    accuracy_ci:\n    - 0.9882\n    - 0.9975\n    train_loss: 0.1225\n    eval_loss: 0.4824\n    train_runtime_sec: 6246\n    seed_comparison:\n      seed42_accuracy: 0.9933\n      seed456_accuracy: 0.9933\n      seed123_accuracy: 0.9109\n      note: seed42 and seed456 identical (99.33%); seed123 outlier (91.09%). 2/3 seeds\n        robust.\n    epoch1_checkpoint_eval:\n      accuracy: 0.993\n      accuracy_ci:\n      - 0.988\n      - 0.997\n      fail_f1: 0.99\n      fail_precision: 0.98\n      fail_recall: 1\n      pass_f1: 1\n      pass_precision: 1\n      pass_recall: 0.99\n      conclusion: epoch1 (99.3%) ≈ epoch3 (99.33%), 1 epoch convergence confirmed\n- exp_id: full_trace_256tok_seed42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.7882\n    majority_baseline: 0.7151\n    lift: 0.0731\n    n: 1190\n    pass_precision: 0.903\n    pass_recall: 0.788\n    pass_f1: 0.842\n    fail_precision: 0.597\n    fail_recall: 0.788\n    fail_f1: 0.679\n    accuracy_ci:\n    - 0.764\n    - 0.81\n    train_loss: 0.1094\n    train_runtime_sec: 3047\n    epochs: 3\n- exp_id: full_trace_512tok_seed42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.8042\n    majority_baseline: 0.7151\n    lift: 0.0891\n    pass_precision: 0.8705\n    pass_recall: 0.8531\n    pass_f1: 0.8617\n    fail_precision: 0.6489\n    fail_recall: 0.6814\n    fail_f1: 0.6647\n    n: 1190\n    accuracy_ci:\n    - 0.7815\n    - 0.8261\n- exp_id: full_trace_1024tok_seed42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.7723\n    majority_baseline: 0.7151\n    lift: 0.0571\n    n: 1190\n    accuracy_ci:\n    - 0.7487\n    - 0.7958\n    pass_precision: 0.9006\n    pass_recall: 0.7662\n    pass_f1: 0.8279\n    fail_precision: 0.573\n    fail_recall: 0.7876\n    fail_f1: 0.6634\n    train_loss: 0.0634\n    train_runtime_sec: 5553\n    epochs: 3\n- exp_id: full_trace_2048tok_seed42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: debugbench_exception_bug_fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: debugbench_exception_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 1\n    majority_baseline: 0.5141\n    lift: 0.4859\n    n: 426\n    pass_precision: 1\n    pass_recall: 1\n    pass_f1: 1\n    fail_precision: 1\n    fail_recall: 1\n    fail_f1: 1\n    accuracy_ci_wilson:\n    - 0.9914\n    - 1\n    accuracy_ci_bootstrap:\n    - 1\n    - 1\n    train_loss: 0.2435\n    eval_loss: 0.4157\n    train_runtime_sec: 837\n- exp_id: debugbench_no_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9671\n    majority_baseline: 0.5141\n    lift: 0.4531\n    pass_precision: 1\n    pass_recall: 0.936\n    pass_f1: 0.967\n    fail_precision: 0.937\n    fail_recall: 1\n    fail_f1: 0.967\n    accuracy_ci:\n    - 0.948\n    - 0.984\n    train_loss: 0.249\n    eval_loss: 0.532\n- exp_id: debugbench_vota_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9977\n    majority_baseline: 0.5141\n    lift: 0.4836\n    n: 426\n    pass_precision: 1\n    pass_recall: 1\n    pass_f1: 1\n    fail_precision: 1\n    fail_recall: 1\n    fail_f1: 1\n    accuracy_ci:\n    - 0.993\n    - 1\n    train_loss: 0.098\n    eval_loss: 0.1179\n    eval_mean_token_accuracy: 0.9737\n    errors: 1\n- exp_id: eval_missing_predictions_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: eval_missing_predictions_batch_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: ae_only_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9908\n    n: 1190\n    pass_recall: 0.987\n    fail_recall: 1\n    majority_baseline: 0.7151\n    lift: 0.2757\n- exp_id: ae_only_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9992\n    n: 1190\n    majority_baseline: 0.7151\n    lift: 0.2841\n    seed_comparison:\n      seed42_accuracy: 0.9992\n      seed123_accuracy: 0.9908\n      seed456_accuracy: 0.9992\n      mean_accuracy: 0.9964\n      std: 0.0049\n      note: 2/3 seeds = 99.92%, seed123 = 99.08%. Mean = 99.64% ± 0.49\n- exp_id: regex_baseline_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    regex_B1_ERROR_presence: 0.9345\n    regex_B2_Traceback: 0.7151\n    regex_B3_any_keyword: 0.9345\n    regex_B4_exception_type: 0.9361\n    regex_B5_format_marker: 0.9933\n    regex_B6_error_count_ge2: 0.9202\n    sft_exception_only: 0.9983\n    best_regex_gap_vs_sft: -0.0622\n    B5_mcnemar_p: 0.041\n    n: 1190\n- exp_id: label_only_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8706\n    n: 1190\n    pass_recall: 0.974\n    fail_recall: 0.611\n    pass_f1: 0.915\n    fail_f1: 0.729\n- exp_id: label_only_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.859\n    n: 1190\n    pass_recall: 0.938\n    fail_recall: 0.661\n    pass_f1: 0.905\n    fail_f1: 0.727\n- exp_id: exception_only_nomarker_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9655\n    n: 1190\n    accuracy_ci:\n    - 0.955\n    - 0.976\n- exp_id: loop_only_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8588\n    majority_baseline: 0.7151\n    lift: 0.1437\n    n: 1190\n    pass_precision: 0.9129\n    pass_recall: 0.8872\n    pass_f1: 0.8999\n    fail_precision: 0.7355\n    fail_recall: 0.7876\n    fail_f1: 0.7607\n    accuracy_ci:\n    - 0.8403\n    - 0.8773\n- exp_id: loop_only_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8664\n    n: 1190\n    pass_precision: 0.9179\n    pass_recall: 0.8931\n    pass_f1: 0.9053\n    fail_precision: 0.7486\n    fail_recall: 0.7994\n    fail_f1: 0.7732\n    accuracy_ci:\n    - 0.847\n    - 0.884\n    seed_comparison:\n      seed42_accuracy: 0.8563\n      seed123_accuracy: 0.8588\n      seed456_accuracy: 0.8664\n      mean_accuracy: 0.8605\n      std: 0.0053\n      note: 3-seed mean = 86.05% ± 0.53%. Moderate variance, seed456 best. loop_only\n        is weakest trace condition (vs exception_only 99.83%, ae_only 99.64%, vota\n        99.41%).\n- exp_id: exception_only_nomarker_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9832\n    n: 1190\n    ci_95:\n    - 0.9756\n    - 0.9899\n    pass_f1: 0.9882\n    fail_f1: 0.9705\n    pass_precision: 0.9882\n    pass_recall: 0.9882\n    fail_precision: 0.9705\n    fail_recall: 0.9705\n    lift_over_majority: 0.2681\n- exp_id: exception_only_nomarker_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9807\n    n: 1190\n    errors: 23\n    ci_95:\n    - 0.9712\n    - 0.9871\n    pass_f1: 0.9865\n    fail_f1: 0.9658\n    pass_precision: 0.9836\n    pass_recall: 0.9894\n    fail_precision: 0.9731\n    fail_recall: 0.9587\n    lift_over_majority: 0.266\n- exp_id: qwen1.5b_exception_only_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen1.5b_no_trace_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen1.5b_vota_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen1.5b_full_trace_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: codellama_exception_only_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: codellama_no_trace_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: codellama_vota_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: codellama13b_exception_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    accuracy_ci_lower: 0.9958\n    accuracy_ci_upper: 1\n    pass_f1: 0.9988\n    fail_f1: 0.9971\n    n_test: 1190\n- exp_id: codellama13b_no_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.765\n    n: 1190\n    majority_baseline: 0.7151\n    lift: 0.05\n    pass_precision: 0.84\n    pass_recall: 0.83\n    pass_f1: 0.84\n    fail_precision: 0.59\n    fail_recall: 0.59\n    fail_f1: 0.59\n    accuracy_ci:\n    - 0.738\n    - 0.787\n- exp_id: codellama13b_vota_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9857\n    accuracy_ci_lower: 0.979\n    accuracy_ci_upper: 0.9916\n    pass_f1: 0.99\n    fail_f1: 0.9748\n    n_test: 1190\n- exp_id: qwen15b_no_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6731\n    n: 1190\n    pass_f1: 0.7527\n    fail_f1: 0.518\n    lift_over_majority: -0.042\n    training_time_sec: 851\n- exp_id: qwen15b_vota_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9958\n    n: 1190\n    pass_recall: 0.9976\n    fail_recall: 0.9912\n    pass_f1: 0.9971\n    fail_f1: 0.9926\n    training_time_sec: 2922\n- exp_id: qwen15b_full_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7706\n    n: 1190\n- exp_id: qwen15b_exception_only_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    accuracy_ci_lower: 0.9958\n    accuracy_ci_upper: 1\n    majority_baseline: 0.7151\n    lift: 0.283\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.9976\n    pass_f1: 0.9988\n    fail_precision: 0.9941\n    fail_recall: 1\n    fail_f1: 0.9971\n    train_loss: 0.1347\n    eval_loss: 0.5761\n    wall_clock_seconds: 1762\n- exp_id: qwen15b_nomarker_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.978\n    n: 1190\n    accuracy_ci:\n    - 0.97\n    - 0.986\n    majority_baseline: 0.715\n    lift: 0.263\n    pass_precision: 0.97\n    pass_recall: 1\n    pass_f1: 0.98\n    fail_precision: 1\n    fail_recall: 0.92\n    fail_f1: 0.96\n- exp_id: codellama13b_exception_only_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 1\n    n: 1190\n    errors: 0\n    pass_precision: 1\n    pass_recall: 1\n    pass_f1: 1\n    fail_precision: 1\n    fail_recall: 1\n    fail_f1: 1\n    lift_over_majority: 0.2849\n- exp_id: codellama13b_exception_only_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9983\n    n: 1190\n    errors: 2\n    pass_precision: 1\n    pass_recall: 0.9976\n    pass_f1: 0.9988\n    fail_precision: 0.9941\n    fail_recall: 1\n    fail_f1: 0.9971\n- exp_id: codellama13b_nomarker_seed42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: full_trace_tail_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.973\n    accuracy_ci:\n    - 0.964\n    - 0.982\n    majority_baseline: 0.7151\n    lift: 0.258\n    n: 1190\n    pass_precision: 0.98\n    pass_recall: 0.99\n    pass_f1: 0.98\n    fail_precision: 0.97\n    fail_recall: 0.94\n    fail_f1: 0.95\n- exp_id: full_trace_tail_512_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.936\n    accuracy_ci:\n    - 0.922\n    - 0.95\n    majority_baseline: 0.7151\n    lift: 0.221\n    n: 1190\n    pass_precision: 0.98\n    pass_recall: 0.93\n    pass_f1: 0.95\n    fail_precision: 0.85\n    fail_recall: 0.94\n    fail_f1: 0.89\n- exp_id: full_trace_tail_256_seed42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.7748\n    accuracy_ci:\n    - 0.7496\n    - 0.7975\n    majority_baseline: 0.7151\n    lift: 0.0597\n    n: 1190\n    pass_f1: 0.8333\n    fail_f1: 0.6528\n- exp_id: full_trace_tail_1024_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9647\n    accuracy_ci:\n    - 0.9546\n    - 0.9748\n    majority_baseline: 0.7151\n    lift: 0.2496\n    n: 1190\n    pass_f1: 0.9753\n    fail_f1: 0.9381\n- exp_id: zeroshot_qwen7b_exception_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.8908\n    accuracy_ci_lower: 0.8731\n    accuracy_ci_upper: 0.9076\n    pass_precision: 0.8815\n    pass_recall: 0.9788\n    pass_f1: 0.9276\n    fail_precision: 0.9265\n    fail_recall: 0.6696\n    fail_f1: 0.7774\n    n_test: 1190\n    n_unknown: 0\n- exp_id: zeroshot_deepseek7b_exception_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9059\n    accuracy_ci_lower: 0.8899\n    accuracy_ci_upper: 0.9218\n    pass_precision: 0.9743\n    pass_recall: 0.8919\n    pass_f1: 0.9313\n    fail_precision: 0.7762\n    fail_recall: 0.941\n    fail_f1: 0.8507\n    n_test: 1190\n    n_unknown: 0\n- exp_id: zeroshot_codellama13b_exception_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.5101\n    accuracy_ci_lower: 0.4824\n    accuracy_ci_upper: 0.5395\n    pass_precision: 1\n    pass_recall: 0.3502\n    pass_f1: 0.5187\n    fail_precision: 0.3585\n    fail_recall: 0.9115\n    fail_f1: 0.5146\n    n_test: 1190\n    n_unknown: 30\n- exp_id: fewshot_qwen7b_exception_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9084\n    accuracy_ci_lower: 0.8908\n    accuracy_ci_upper: 0.9244\n    pass_precision: 0.9245\n    pass_recall: 0.9495\n    pass_f1: 0.9368\n    fail_precision: 0.8639\n    fail_recall: 0.8053\n    fail_f1: 0.8336\n    n_test: 1190\n    n_unknown: 0\n- exp_id: zeroshot_qwen15b_exception_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9345\n    accuracy_ci_lower: 0.9202\n    accuracy_ci_upper: 0.9479\n    pass_f1: 0.969\n    fail_f1: 0.873\n    pass_recall: 0.9906\n    fail_recall: 0.7935\n    n_test: 1190\n    n_unknown: 24\n- exp_id: deepseek_full_trace_tail2048_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9496\n    accuracy_ci_lower: 0.937\n    accuracy_ci_upper: 0.9622\n    pass_precision: 0.9692\n    pass_recall: 0.96\n    pass_f1: 0.9646\n    fail_precision: 0.902\n    fail_recall: 0.9233\n    fail_f1: 0.9125\n    n_test: 1190\n- exp_id: qwen15b_full_trace_tail2048_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.979\n    accuracy_ci_lower: 0.9706\n    accuracy_ci_upper: 0.9874\n    pass_precision: 0.9758\n    pass_recall: 0.9953\n    pass_f1: 0.9855\n    fail_precision: 0.9876\n    fail_recall: 0.9381\n    fail_f1: 0.9622\n    n_test: 1190\n- exp_id: deepseek_full_trace_head2048_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.787\n    accuracy_ci_lower: 0.765\n    accuracy_ci_upper: 0.81\n    majority_baseline: 0.715\n    lift_pp: 7.2\n    pass_precision: 0.84\n    pass_recall: 0.86\n    pass_f1: 0.85\n    fail_precision: 0.63\n    fail_recall: 0.6\n    fail_f1: 0.62\n- exp_id: qwen15b_full_trace_head2048_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7529\n    accuracy_ci_lower: 0.7286\n    accuracy_ci_upper: 0.7782\n    pass_precision: 0.799\n    pass_recall: 0.874\n    pass_f1: 0.835\n    fail_precision: 0.587\n    fail_recall: 0.448\n    fail_f1: 0.508\n    n_test: 1190\n- exp_id: full_trace_tail256_seed42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.789\n    accuracy_ci_lower: 0.765\n    accuracy_ci_upper: 0.813\n    pass_f1: 0.845\n    fail_f1: 0.671\n    n_test: 1190\n- exp_id: qwen15b_full_trace_tail256_seed42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.726\n    accuracy_ci_lower: 0.7\n    accuracy_ci_upper: 0.753\n    majority_baseline: 0.715\n    lift_over_majority: 0.011\n    lift_ci_lower: -0.021\n    lift_ci_upper: 0.044\n    pass_precision: 0.82\n    pass_recall: 0.79\n    pass_f1: 0.8\n    fail_precision: 0.52\n    fail_recall: 0.57\n    fail_f1: 0.54\n    eval_loss: 0.5936\n    train_loss: 0.2687\n- exp_id: deepseek_full_trace_tail256_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7639\n    accuracy_ci_lower: 0.7403\n    accuracy_ci_upper: 0.7874\n    pass_precision: 0.8058\n    pass_recall: 0.8825\n    pass_f1: 0.8424\n    fail_precision: 0.6124\n    fail_recall: 0.4661\n    fail_f1: 0.5293\n    majority_baseline: 0.7151\n    lift: 0.0487\n    eval_loss: 0.5117\n    train_loss: 0.2367\n- exp_id: qwen15b_full_trace_tail512_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.956\n    accuracy_ci_lower: 0.945\n    accuracy_ci_upper: 0.968\n    majority_baseline: 0.715\n    lift_over_majority: 0.241\n    eval_loss: 0.263\n    train_loss: 0.154\n    pass_precision: 0.98\n    pass_recall: 0.96\n    pass_f1: 0.97\n    fail_precision: 0.91\n    fail_recall: 0.94\n    fail_f1: 0.92\n    eval_mean_token_accuracy: 0.949\n- exp_id: deepseek_full_trace_tail512_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.939\n    accuracy_ci_lower: 0.926\n    accuracy_ci_upper: 0.953\n    majority_baseline: 0.715\n    lift_over_majority: 0.224\n    pass_precision: 0.97\n    pass_recall: 0.94\n    pass_f1: 0.96\n    fail_precision: 0.86\n    fail_recall: 0.94\n    fail_f1: 0.9\n    n_test: 1190\n- exp_id: deepseek_full_trace_tail1024_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9647\n    accuracy_ci_lower: 0.9538\n    accuracy_ci_upper: 0.9748\n    pass_precision: 0.964\n    pass_recall: 0.987\n    pass_f1: 0.976\n    fail_precision: 0.966\n    fail_recall: 0.909\n    fail_f1: 0.936\n    majority_baseline: 0.7151\n    n_test: 1190\n- exp_id: qwen15b_full_trace_tail1024_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.966\n    accuracy_ci_low: 0.955\n    accuracy_ci_high: 0.976\n    pass_precision: 0.96\n    pass_recall: 0.99\n    pass_f1: 0.98\n    fail_precision: 0.97\n    fail_recall: 0.91\n    fail_f1: 0.94\n    eval_loss: 0.1983\n    train_loss: 0.1187\n    majority_baseline: 0.715\n    lift_over_majority_pp: 25\n- exp_id: codellama13b_full_trace_tail512_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 97.5\n    accuracy_ci_low: 96.6\n    accuracy_ci_high: 98.4\n    majority_baseline: 71.5\n    lift_over_majority: 26\n    pass_precision: 0.98\n    pass_recall: 0.99\n    pass_f1: 0.98\n    fail_precision: 0.97\n    fail_recall: 0.94\n    fail_f1: 0.95\n    train_loss: 0.124\n    eval_loss: 0.249\n- exp_id: codellama13b_full_trace_head2048_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7992\n    majority_baseline: 0.7151\n    lift: 0.084\n    n_test: 1190\n    pass_precision: 0.8566\n    pass_recall: 0.8637\n    pass_f1: 0.8602\n    fail_precision: 0.6506\n    fail_recall: 0.6372\n    fail_f1: 0.6438\n    train_loss: 0.0452\n    eval_loss: 0.111\n    accuracy_ci_lower: 0.7765\n    accuracy_ci_upper: 0.8227\n- exp_id: codellama13b_full_trace_tail1024_seed42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: codellama13b_full_trace_tail256_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.779\n    accuracy_ci_lower: 0.757\n    accuracy_ci_upper: 0.803\n    pass_f1: 0.843\n    fail_f1: 0.626\n    pass_precision: 0.856\n    pass_recall: 0.831\n    fail_precision: 0.604\n    fail_recall: 0.649\n    majority_baseline: 0.715\n    lift: 0.064\n    train_loss: 0.245\n    eval_loss: 0.615\n- exp_id: codellama13b_full_trace_tail1024_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.876\n    accuracy_ci_lower: 0.856\n    accuracy_ci_upper: 0.893\n    majority_baseline: 0.715\n    lift_pp: 16.1\n    pass_precision: 0.85\n    pass_recall: 1\n    pass_f1: 0.92\n    fail_precision: 1\n    fail_recall: 0.56\n    fail_f1: 0.72\n    n_test: 1190\n    train_loss: 0.0937\n    eval_loss: 0.1859\n- exp_id: codellama13b_full_trace_tail2048_seed42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: codellama13b_full_trace_tail2048_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy_epoch1: 0.2849\n    accuracy_epoch3: 0.2958\n    pass_recall_epoch3: 0.016\n    fail_recall_epoch3: 0.997\n    majority_baseline: 0.715\n    n_test: 1190\n    note: 'Catastrophic failure: model predicts fail for almost everything. Full-sequence\n      loss dilution with CodeLlama tokenizer at 2048 tokens.'\n- exp_id: codellama13b_full_trace_tail1024_seed42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_epoch1: 0.9824\n    accuracy_epoch3: 0.9756\n    pass_f1_epoch1: 0.988\n    fail_f1_epoch1: 0.968\n    pass_f1_epoch3: 0.983\n    fail_f1_epoch3: 0.955\n    best_accuracy: 0.9824\n    best_epoch: 1\n    overfitting: true\n- exp_id: codellama13b_full_trace_tail2048_seed42_v3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy_epoch1: 0.071\n    accuracy_epoch3: 0.418\n    pass_f1_epoch3: 0.416\n    fail_f1_epoch3: 0.421\n    pass_f1_epoch1: 0.035\n    fail_f1_epoch1: 0.342\n    train_loss: 0.785\n- exp_id: qwen7b_full_trace_head2048_seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_epoch1: 0.816\n    accuracy_epoch3: 0.81\n    pass_f1_epoch1: 0.87\n    fail_f1_epoch1: 0.686\n    pass_f1_epoch3: 0.866\n    fail_f1_epoch3: 0.674\n    best_accuracy: 0.816\n    best_epoch: 1\n- exp_id: qwen7b_full_trace_tail384_seed42\n  name: ''\n  status: ALLOCATED\n  conclusion: ''\n  metrics: {}\n- exp_id: deepseek_full_trace_tail384_seed42\n  name: ''\n  status: ALLOCATED\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen15b_full_trace_tail384_seed42\n  name: ''\n  status: PENDING\n  conclusion: ''\n  metrics: {}\n- exp_id: codellama13b_full_trace_tail384_seed42\n  name: ''\n  status: PENDING\n  conclusion: ''\n  metrics: {}\n\n\n## what_if (hypothetical experiments — additive)\n\n- name: fine_grained_phase_transition\n  claim: Phase transition claim\n  description: tail-384 × 4 models 精确定位 phase transition 拐点\n  estimated_gpu_hours: 16.0\n- name: cross_seed_budget_curve\n  claim: Robustness\n  description: tail-512 × 4 models × 3 seeds 验证 convergence band robustness\n  estimated_gpu_hours: 24.0\n- name: few_shot_baseline\n  claim: Claim 1 强化\n  description: GPT-4o/Claude few-shot verdict prediction baseline 对比\n  estimated_gpu_hours: 0.0\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-18T12:43:10.877Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T12:43:10.877Z",
  "sessionId": "a83c4e8f-ba60-4c11-a244-a557040bd173"
}
```

---

## Round 1

7 recorded events

### User

_source line 3 · 2026-05-18T12:43:10.898Z_

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
project: trace-verdict-study
focus: 评估当前 plan 是否够冲 EMNLP main。重点审查：(1) 3 个 Core Claims 的证据强度，(2) P1 实验（phase transition fine-grained + cross-seed）对论文质量的边际贡献，(3) 4 模型 budget curve 矩阵的 story 是否足够有说服力，(4) label_only_loss 发现值不值得作为独立 contribution，(5) 与同类 EMNLP/ACL 论文对比缺什么。

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
    accuracy_ci_lower: 0.9958
    accuracy_ci_upper: 1
    pass_f1: 0.9988
    fail_f1: 0.9971
    n_test: 1190
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
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9655
    n: 1190
    accuracy_ci:
    - 0.955
    - 0.976
- id: plan_016
  claim: 1
  description: 'Fine-grained phase transition: tail-384 × 4 模型，精确定位 256→512 phase
    transition 是 sharp 还是 gradual。'
  priority: P1
  gpu_budget_hours: 16
  deps:
  - plan_006
  notes: 4 模型各 1 个实验。如果 tail-384 仍在 ~77% (≈tail-256)，证明 transition 是 sharp；如果 ~85%，证明是
    gradual。对 phase transition claim 的强度有决定性影响。
  status: planned
- id: plan_017
  claim: 1
  description: 'Cross-seed budget curve: tail-512 × 4 模型 × 3 seeds，验证 phase transition
    后 convergence band 的 robustness。'
  priority: P1
  gpu_budget_hours: 24
  deps:
  - plan_016
  notes: tail-512 是 phase transition 后第一个点，验证 93-97% convergence 是否 seed-robust。审稿人必问
    single-seed robustness。
  status: planned
- id: plan_018
  claim: 1
  description: 'Error analysis: 用已有 predictions.jsonl 分析 failure modes（哪类程序/错误容易被误判）。不需
    GPU。'
  priority: P1
  gpu_budget_hours: 0
  deps: []
  notes: 分析 exception_only/vota/full_trace/no_trace 的错误模式差异。重点关注 Tier 1 vs Tier 2
    的 failure mode 是否不同。
  status: planned
- id: plan_019
  claim: 1
  description: 'Cross-model calibration: 4 模型 × exception_only 的 ECE/Brier 对比。验证 calibration
    quality 跨模型 universal。'
  priority: P1
  gpu_budget_hours: 1
  deps: []
  notes: 纯 eval，用已有 checkpoint。当前只有 Qwen-7B 的 calibration 数据，需要扩展到 4 模型。
  status: planned
- id: plan_020
  claim: 2
  description: 'Few-shot prompting baseline: GPT-4o/Claude 直接判断 pass/fail（0-shot +
    3-shot），作为 non-SFT upper bound 对比。'
  priority: P2
  gpu_budget_hours: 0
  deps: []
  notes: 不需 GPU，用 API 调用。如果 few-shot < exception_only SFT，说明 SFT 在 verdict task 上超越
    frontier model 的 few-shot 能力，claim 更强。
  status: planned
- id: plan_021
  claim: 1
  description: 'OOD generalization: 在不同编程语言/项目的 trace 上测试 exception_only 泛化性。'
  priority: P2
  gpu_budget_hours: 12
  deps: []
  notes: 需要构建 OOD 测试集（不同语言的 trace）。如果 exception_only 在 OOD 上仍强，大幅强化 generalization
    claim。
  status: planned
- id: plan_022
  claim: 2
  description: 'Training dynamics: 记录 exception_only vs full_trace 的 learning curve（每
    50 steps eval），分析收敛速度差异。'
  priority: P2
  gpu_budget_hours: 8
  deps: []
  notes: 如果 exception_only 收敛更快，支持 information density 假说。需要修改训练脚本加 intermediate eval。
  status: planned


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
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9655
    n: 1190
    accuracy_ci:
    - 0.955
    - 0.976
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
    seed_comparison:
      seed42_accuracy: 0.8563
      seed123_accuracy: 0.8588
      seed456_accuracy: 0.8664
      mean_accuracy: 0.8605
      std: 0.0053
      note: 3-seed mean = 86.05% ± 0.53%. Moderate variance, seed456 best. loop_only
        is weakest trace condition (vs exception_only 99.83%, ae_only 99.64%, vota
        99.41%).
- exp_id: exception_only_nomarker_seed123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9832
    n: 1190
    ci_95:
    - 0.9756
    - 0.9899
    pass_f1: 0.9882
    fail_f1: 0.9705
    pass_precision: 0.9882
    pass_recall: 0.9882
    fail_precision: 0.9705
    fail_recall: 0.9705
    lift_over_majority: 0.2681
- exp_id: exception_only_nomarker_seed456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9807
    n: 1190
    errors: 23
    ci_95:
    - 0.9712
    - 0.9871
    pass_f1: 0.9865
    fail_f1: 0.9658
    pass_precision: 0.9836
    pass_recall: 0.9894
    fail_precision: 0.9731
    fail_recall: 0.9587
    lift_over_majority: 0.266
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
    accuracy_ci_lower: 0.9958
    accuracy_ci_upper: 1
    pass_f1: 0.9988
    fail_f1: 0.9971
    n_test: 1190
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
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9857
    accuracy_ci_lower: 0.979
    accuracy_ci_upper: 0.9916
    pass_f1: 0.99
    fail_f1: 0.9748
    n_test: 1190
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
- exp_id: qwen15b_nomarker_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.978
    n: 1190
    accuracy_ci:
    - 0.97
    - 0.986
    majority_baseline: 0.715
    lift: 0.263
    pass_precision: 0.97
    pass_recall: 1
    pass_f1: 0.98
    fail_precision: 1
    fail_recall: 0.92
    fail_f1: 0.96
- exp_id: codellama13b_exception_only_seed123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 1
    n: 1190
    errors: 0
    pass_precision: 1
    pass_recall: 1
    pass_f1: 1
    fail_precision: 1
    fail_recall: 1
    fail_f1: 1
    lift_over_majority: 0.2849
- exp_id: codellama13b_exception_only_seed456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9983
    n: 1190
    errors: 2
    pass_precision: 1
    pass_recall: 0.9976
    pass_f1: 0.9988
    fail_precision: 0.9941
    fail_recall: 1
    fail_f1: 0.9971
- exp_id: codellama13b_nomarker_seed42
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: full_trace_tail_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.973
    accuracy_ci:
    - 0.964
    - 0.982
    majority_baseline: 0.7151
    lift: 0.258
    n: 1190
    pass_precision: 0.98
    pass_recall: 0.99
    pass_f1: 0.98
    fail_precision: 0.97
    fail_recall: 0.94
    fail_f1: 0.95
- exp_id: full_trace_tail_512_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.936
    accuracy_ci:
    - 0.922
    - 0.95
    majority_baseline: 0.7151
    lift: 0.221
    n: 1190
    pass_precision: 0.98
    pass_recall: 0.93
    pass_f1: 0.95
    fail_precision: 0.85
    fail_recall: 0.94
    fail_f1: 0.89
- exp_id: full_trace_tail_256_seed42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 0.7748
    accuracy_ci:
    - 0.7496
    - 0.7975
    majority_baseline: 0.7151
    lift: 0.0597
    n: 1190
    pass_f1: 0.8333
    fail_f1: 0.6528
- exp_id: full_trace_tail_1024_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9647
    accuracy_ci:
    - 0.9546
    - 0.9748
    majority_baseline: 0.7151
    lift: 0.2496
    n: 1190
    pass_f1: 0.9753
    fail_f1: 0.9381
- exp_id: zeroshot_qwen7b_exception_only
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.8908
    accuracy_ci_lower: 0.8731
    accuracy_ci_upper: 0.9076
    pass_precision: 0.8815
    pass_recall: 0.9788
    pass_f1: 0.9276
    fail_precision: 0.9265
    fail_recall: 0.6696
    fail_f1: 0.7774
    n_test: 1190
    n_unknown: 0
- exp_id: zeroshot_deepseek7b_exception_only
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9059
    accuracy_ci_lower: 0.8899
    accuracy_ci_upper: 0.9218
    pass_precision: 0.9743
    pass_recall: 0.8919
    pass_f1: 0.9313
    fail_precision: 0.7762
    fail_recall: 0.941
    fail_f1: 0.8507
    n_test: 1190
    n_unknown: 0
- exp_id: zeroshot_codellama13b_exception_only
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.5101
    accuracy_ci_lower: 0.4824
    accuracy_ci_upper: 0.5395
    pass_precision: 1
    pass_recall: 0.3502
    pass_f1: 0.5187
    fail_precision: 0.3585
    fail_recall: 0.9115
    fail_f1: 0.5146
    n_test: 1190
    n_unknown: 30
- exp_id: fewshot_qwen7b_exception_only
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9084
    accuracy_ci_lower: 0.8908
    accuracy_ci_upper: 0.9244
    pass_precision: 0.9245
    pass_recall: 0.9495
    pass_f1: 0.9368
    fail_precision: 0.8639
    fail_recall: 0.8053
    fail_f1: 0.8336
    n_test: 1190
    n_unknown: 0
- exp_id: zeroshot_qwen15b_exception_only
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9345
    accuracy_ci_lower: 0.9202
    accuracy_ci_upper: 0.9479
    pass_f1: 0.969
    fail_f1: 0.873
    pass_recall: 0.9906
    fail_recall: 0.7935
    n_test: 1190
    n_unknown: 24
- exp_id: deepseek_full_trace_tail2048_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9496
    accuracy_ci_lower: 0.937
    accuracy_ci_upper: 0.9622
    pass_precision: 0.9692
    pass_recall: 0.96
    pass_f1: 0.9646
    fail_precision: 0.902
    fail_recall: 0.9233
    fail_f1: 0.9125
    n_test: 1190
- exp_id: qwen15b_full_trace_tail2048_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.979
    accuracy_ci_lower: 0.9706
    accuracy_ci_upper: 0.9874
    pass_precision: 0.9758
    pass_recall: 0.9953
    pass_f1: 0.9855
    fail_precision: 0.9876
    fail_recall: 0.9381
    fail_f1: 0.9622
    n_test: 1190
- exp_id: deepseek_full_trace_head2048_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.787
    accuracy_ci_lower: 0.765
    accuracy_ci_upper: 0.81
    majority_baseline: 0.715
    lift_pp: 7.2
    pass_precision: 0.84
    pass_recall: 0.86
    pass_f1: 0.85
    fail_precision: 0.63
    fail_recall: 0.6
    fail_f1: 0.62
- exp_id: qwen15b_full_trace_head2048_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.7529
    accuracy_ci_lower: 0.7286
    accuracy_ci_upper: 0.7782
    pass_precision: 0.799
    pass_recall: 0.874
    pass_f1: 0.835
    fail_precision: 0.587
    fail_recall: 0.448
    fail_f1: 0.508
    n_test: 1190
- exp_id: full_trace_tail256_seed42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 0.789
    accuracy_ci_lower: 0.765
    accuracy_ci_upper: 0.813
    pass_f1: 0.845
    fail_f1: 0.671
    n_test: 1190
- exp_id: qwen15b_full_trace_tail256_seed42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 0.726
    accuracy_ci_lower: 0.7
    accuracy_ci_upper: 0.753
    majority_baseline: 0.715
    lift_over_majority: 0.011
    lift_ci_lower: -0.021
    lift_ci_upper: 0.044
    pass_precision: 0.82
    pass_recall: 0.79
    pass_f1: 0.8
    fail_precision: 0.52
    fail_recall: 0.57
    fail_f1: 0.54
    eval_loss: 0.5936
    train_loss: 0.2687
- exp_id: deepseek_full_trace_tail256_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.7639
    accuracy_ci_lower: 0.7403
    accuracy_ci_upper: 0.7874
    pass_precision: 0.8058
    pass_recall: 0.8825
    pass_f1: 0.8424
    fail_precision: 0.6124
    fail_recall: 0.4661
    fail_f1: 0.5293
    majority_baseline: 0.7151
    lift: 0.0487
    eval_loss: 0.5117
    train_loss: 0.2367
- exp_id: qwen15b_full_trace_tail512_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.956
    accuracy_ci_lower: 0.945
    accuracy_ci_upper: 0.968
    majority_baseline: 0.715
    lift_over_majority: 0.241
    eval_loss: 0.263
    train_loss: 0.154
    pass_precision: 0.98
    pass_recall: 0.96
    pass_f1: 0.97
    fail_precision: 0.91
    fail_recall: 0.94
    fail_f1: 0.92
    eval_mean_token_accuracy: 0.949
- exp_id: deepseek_full_trace_tail512_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.939
    accuracy_ci_lower: 0.926
    accuracy_ci_upper: 0.953
    majority_baseline: 0.715
    lift_over_majority: 0.224
    pass_precision: 0.97
    pass_recall: 0.94
    pass_f1: 0.96
    fail_precision: 0.86
    fail_recall: 0.94
    fail_f1: 0.9
    n_test: 1190
- exp_id: deepseek_full_trace_tail1024_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9647
    accuracy_ci_lower: 0.9538
    accuracy_ci_upper: 0.9748
    pass_precision: 0.964
    pass_recall: 0.987
    pass_f1: 0.976
    fail_precision: 0.966
    fail_recall: 0.909
    fail_f1: 0.936
    majority_baseline: 0.7151
    n_test: 1190
- exp_id: qwen15b_full_trace_tail1024_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.966
    accuracy_ci_low: 0.955
    accuracy_ci_high: 0.976
    pass_precision: 0.96
    pass_recall: 0.99
    pass_f1: 0.98
    fail_precision: 0.97
    fail_recall: 0.91
    fail_f1: 0.94
    eval_loss: 0.1983
    train_loss: 0.1187
    majority_baseline: 0.715
    lift_over_majority_pp: 25
- exp_id: codellama13b_full_trace_tail512_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 97.5
    accuracy_ci_low: 96.6
    accuracy_ci_high: 98.4
    majority_baseline: 71.5
    lift_over_majority: 26
    pass_precision: 0.98
    pass_recall: 0.99
    pass_f1: 0.98
    fail_precision: 0.97
    fail_recall: 0.94
    fail_f1: 0.95
    train_loss: 0.124
    eval_loss: 0.249
- exp_id: codellama13b_full_trace_head2048_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.7992
    majority_baseline: 0.7151
    lift: 0.084
    n_test: 1190
    pass_precision: 0.8566
    pass_recall: 0.8637
    pass_f1: 0.8602
    fail_precision: 0.6506
    fail_recall: 0.6372
    fail_f1: 0.6438
    train_loss: 0.0452
    eval_loss: 0.111
    accuracy_ci_lower: 0.7765
    accuracy_ci_upper: 0.8227
- exp_id: codellama13b_full_trace_tail1024_seed42
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: codellama13b_full_trace_tail256_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.779
    accuracy_ci_lower: 0.757
    accuracy_ci_upper: 0.803
    pass_f1: 0.843
    fail_f1: 0.626
    pass_precision: 0.856
    pass_recall: 0.831
    fail_precision: 0.604
    fail_recall: 0.649
    majority_baseline: 0.715
    lift: 0.064
    train_loss: 0.245
    eval_loss: 0.615
- exp_id: codellama13b_full_trace_tail1024_seed42_v2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 0.876
    accuracy_ci_lower: 0.856
    accuracy_ci_upper: 0.893
    majority_baseline: 0.715
    lift_pp: 16.1
    pass_precision: 0.85
    pass_recall: 1
    pass_f1: 0.92
    fail_precision: 1
    fail_recall: 0.56
    fail_f1: 0.72
    n_test: 1190
    train_loss: 0.0937
    eval_loss: 0.1859
- exp_id: codellama13b_full_trace_tail2048_seed42
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: codellama13b_full_trace_tail2048_seed42_v2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy_epoch1: 0.2849
    accuracy_epoch3: 0.2958
    pass_recall_epoch3: 0.016
    fail_recall_epoch3: 0.997
    majority_baseline: 0.715
    n_test: 1190
    note: 'Catastrophic failure: model predicts fail for almost everything. Full-sequence
      loss dilution with CodeLlama tokenizer at 2048 tokens.'
- exp_id: codellama13b_full_trace_tail1024_seed42_v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy_epoch1: 0.9824
    accuracy_epoch3: 0.9756
    pass_f1_epoch1: 0.988
    fail_f1_epoch1: 0.968
    pass_f1_epoch3: 0.983
    fail_f1_epoch3: 0.955
    best_accuracy: 0.9824
    best_epoch: 1
    overfitting: true
- exp_id: codellama13b_full_trace_tail2048_seed42_v3
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy_epoch1: 0.071
    accuracy_epoch3: 0.418
    pass_f1_epoch3: 0.416
    fail_f1_epoch3: 0.421
    pass_f1_epoch1: 0.035
    fail_f1_epoch1: 0.342
    train_loss: 0.785
- exp_id: qwen7b_full_trace_head2048_seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy_epoch1: 0.816
    accuracy_epoch3: 0.81
    pass_f1_epoch1: 0.87
    fail_f1_epoch1: 0.686
    pass_f1_epoch3: 0.866
    fail_f1_epoch3: 0.674
    best_accuracy: 0.816
    best_epoch: 1
- exp_id: qwen7b_full_trace_tail384_seed42
  name: ''
  status: ALLOCATED
  conclusion: ''
  metrics: {}
- exp_id: deepseek_full_trace_tail384_seed42
  name: ''
  status: ALLOCATED
  conclusion: ''
  metrics: {}
- exp_id: qwen15b_full_trace_tail384_seed42
  name: ''
  status: PENDING
  conclusion: ''
  metrics: {}
- exp_id: codellama13b_full_trace_tail384_seed42
  name: ''
  status: PENDING
  conclusion: ''
  metrics: {}


## what_if (hypothetical experiments — additive)

- name: fine_grained_phase_transition
  claim: Phase transition claim
  description: tail-384 × 4 models 精确定位 phase transition 拐点
  estimated_gpu_hours: 16.0
- name: cross_seed_budget_curve
  claim: Robustness
  description: tail-512 × 4 models × 3 seeds 验证 convergence band robustness
  estimated_gpu_hours: 24.0
- name: few_shot_baseline
  claim: Claim 1 强化
  description: GPT-4o/Claude few-shot verdict prediction baseline 对比
  estimated_gpu_hours: 0.0

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
  "promptId": "12ea04dd-edd5-4818-bbe3-6680092fa6ee",
  "type": "user",
  "uuid": "c19ec284-e9b1-440b-9404-e5dfa257fd2d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4",
  "sessionId": "a83c4e8f-ba60-4c11-a244-a557040bd173",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T12:43:10.896Z_

```json
{
  "parentUuid": "c19ec284-e9b1-440b-9404-e5dfa257fd2d",
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
  "uuid": "50081ba3-aa8c-4bd5-92d9-b3f787cd8179",
  "timestamp": "2026-05-18T12:43:10.896Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4",
  "sessionId": "a83c4e8f-ba60-4c11-a244-a557040bd173",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T12:43:10.896Z_

```json
{
  "parentUuid": "50081ba3-aa8c-4bd5-92d9-b3f787cd8179",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f05e07b2-49e2-4c53-832e-9424ef239f08",
  "timestamp": "2026-05-18T12:43:10.896Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4",
  "sessionId": "a83c4e8f-ba60-4c11-a244-a557040bd173",
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
  "leafUuid": "f05e07b2-49e2-4c53-832e-9424ef239f08",
  "sessionId": "a83c4e8f-ba60-4c11-a244-a557040bd173"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three scenario tiers for trace-verdict study",
  "sessionId": "a83c4e8f-ba60-4c11-a244-a557040bd173"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "f05e07b2-49e2-4c53-832e-9424ef239f08",
  "sessionId": "a83c4e8f-ba60-4c11-a244-a557040bd173"
}
```

---

### Runtime record

_source line 9_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three scenario tiers for trace-verdict study",
  "sessionId": "a83c4e8f-ba60-4c11-a244-a557040bd173"
}
```

---
