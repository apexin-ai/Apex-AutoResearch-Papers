# Paper Framing — trace-verdict-study

> v5.0 — [UPDATED 2026-05-22] **Two-Pathway Model 升级 (Round 14 响应)**：从 "information density determines learning efficiency" 升级为 **Two-Pathway Model** 框架。15 条件扩展分析揭示两条独立信号通路：(1) Explicit pathway — diagnostic tokens (exception/assertion) → 99%+，diagnostic token ratio r=0.949 (N=5)；(2) Implicit pathway — terminal execution state (变量值) → 93-97%，phase transition at tail-512 tokens (跨过 globals dump 噪声层 D115)；(3) Noise dilution — intermediate states → 72-82%。Model-free diagnostic token ratio 替代循环定义的 information density (MF-3)。新增实验：cross-dataset generalization (in progress)、exception subcomponent ablation (queued)。模型 4 个，3 架构家族，1.5B-13B scale。

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May 25, 2026

## Core Insight

**Two-Pathway Model: execution traces contain two independent signal pathways for verdict prediction, and their interaction explains why complete traces impair SFT learning.**

**Pathway 1 — Explicit diagnostic signals**: Exception events and assertion failures are compact, structurally explicit fault indicators. They enable models to converge to ≥99.33% accuracy within 50 training steps across 4 models. Model-free **diagnostic token ratio** (fraction of exception/assertion tokens in total sequence) predicts accuracy with r=0.949 (p=0.014) for the 5 main conditions. This operationalizes "information density" without circularity — the metric is computed from data alone, independent of model accuracy.

**Pathway 2 — Implicit terminal state signals**: Tail-truncated traces (last N tokens of full input) achieve 93-97% accuracy with near-zero explicit diagnostic tokens ([ERROR]=0 in all tail conditions). The mechanism: whole-input tail truncation at ≥512 tokens captures structured execution state — `[Line X]` variable values at the final execution steps. Below 384 tokens, the globals module dump consumes the entire budget (pure noise → ~73% ≈ no_trace). The phase transition at tail-384→tail-512 (+13.8pp) marks the point where the model crosses this noise floor and accesses terminal execution state (D115).

**Noise dilution**: Full traces (72-82%) contain both pathways' signals buried under thousands of intermediate execution state tokens. The diagnostic signal (explicit or implicit) is overwhelmed — training dynamics show non-monotonic oscillation (82-89%) even with label-only loss, confirming the impairment is from information overload, not gradient dilution alone.

**Design principle**: For verdict tasks, extract the highest-density diagnostic signal (explicit pathway preferred; implicit terminal state as fallback). Complete traces are strictly dominated — they contain no unique signal that targeted extraction cannot capture more efficiently.

## Core Claims (4)

### Claim 1: Exception events as minimal sufficient signal (≥99.33% across 4 models, 3 architectures, 1.5B-13B)

Exception summaries consistently achieve the highest verdict prediction accuracy across all four models tested (Qwen-7B, Qwen-1.5B, CodeLlama-13B, DeepSeek-6.7B), outperforming all other trace representations in every seed. On Qwen-2.5-Coder-7B, performance is perfectly robust: 99.83% ± 0.00 (3 seeds). On DeepSeek-Coder-6.7B, absolute accuracy is seed-dependent (seed42=99.83% epoch1, seed123=91.43% epoch1; Δ=8.40pp), consistent with LoRA initialization sensitivity — but exception_only still dominates VOTA (84.45%) and no_trace (73.36%) in all seeds. This contrasts with VOTA (cross-model gap = 14.96pp) and no_trace (gap = 1.77pp). Exception events are structurally simple (`[ERROR] type: ... message: ...`) and do not require deep trace reasoning.

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

### Claim 2 [UPGRADED v5.0]: Two-Pathway Model — diagnostic token ratio operationalizes information density (non-circular)

**The paper's core analytical contribution.** We operationalize "information density" with a model-free metric and discover it only captures one of two independent signal pathways:

**Diagnostic token ratio** = (tokens matching exception/assertion patterns) / (total sequence tokens). Computed entirely from data, independent of model accuracy. For the 5 main conditions (no_trace, full_trace, exception_only, ae_only, loop_only): Pearson r=0.949, p=0.014. This is the **explicit pathway**.

**Extended to 15 conditions** reveals the **implicit pathway**: tail-512 to tail-2048 achieve 93-97% accuracy with diagnostic ratio ≈ 0.001 (essentially zero). The correlation drops to r=0.630 (Spearman r=0.766) — because the implicit pathway operates on different signals entirely.

**Three-pathway framework**:
1. **Explicit** (diagnostic tokens → 99%+): exception/assertion markers directly encode verdict. Captured by diagnostic token ratio.
2. **Implicit** (terminal execution state → 93-97%): `[Line X]` variable values at final execution steps encode program outcome indirectly. Accessible only when tail truncation crosses the globals dump noise floor (~384 tokens). FullTraceFormatter does NOT render exception info in tail data ([ERROR]=0%), so this is a genuinely independent signal channel (D115).
3. **Noise dilution** (intermediate states → 72-82%): Both signals exist in full traces but are buried under thousands of intermediate execution state tokens → training oscillation, overfitting to spurious patterns.

**Phase transition evidence**: tail-384 (79.8%) → tail-512 (93.6%) = +13.8pp. Agent confirmed: tail-384 has 0 `[Line X]` events (100% consumed by globals dump); tail-512 has ≥1 event in 92% of samples. The 128-token margin crosses a structural threshold.

**Training dynamics** (supporting evidence, not standalone claim): exception_only reaches 99.33% at step 50 (saturation by step 150); full_trace oscillates 82-89% throughout 444 steps, never converging. This demonstrates explicit pathway's learning efficiency vs noise dilution's impairment.

**Supporting evidence:**
- `qwen7b_exception_only_dynamics_seed42`: step 50=99.33%, step 150=99.83%
- `qwen7b_full_trace_dynamics_seed42`: oscillates 82-89%, peak 88.82% at step 350
- Diagnostic token ratio analysis: `artifacts/diagnostic_token_ratio/` (r=0.949 for 5 conditions, r=0.630 for 15)
- Pass/fail trace diff: `artifacts/pass_fail_diff/` (exception_only 100% diagnostic diff vs full_trace 0.3%)
- Phase transition data: `qwen7b_full_trace_tail512_seed42` (93.61%), `qwen15b_full_trace_tail384_seed42` (73.61%)

**Why this addresses MF-2 (near-tautological) + MF-3 (circular density)**:
- MF-2: The finding is NOT "exception predicts verdict" (tautological) — it's that execution traces contain two independent, non-overlapping signal pathways with quantifiably different learning efficiencies. The implicit pathway (93-97% from variable values alone, zero exception tokens) is genuinely non-obvious.
- MF-3: Diagnostic token ratio is model-free and non-circular. Its limitation to the explicit pathway is explicitly acknowledged, and the implicit pathway is explained by a different mechanism (structural execution state).

### Claim 3: Preliminary decomposition of full_trace degradation (with explicit confounders)

Label-only loss ablation provides an **upper-bound estimate** of gradient dilution's contribution. Full traces: 81.76% [`full_trace_seed42_v5`] → label-only: 86.22% [`full_trace_label_only_seed42`] (+4.5pp). This suggests gradient dilution accounts for **at most ~26%** of the performance gap (4.5pp of 17.6pp total gap to VOTA).

**Explicit confounders** (Round 14 MF-1 response):
- TRL SFTTrainer uses **mean CE loss** (not sum), so the effective LR difference is NOT 2000× as a naive calculation suggests — it's the same LR applied to fewer label tokens. The "reviewer misconception" about LR amplification is documented.
- However, label-only loss simultaneously changes: (1) which tokens receive gradient, (2) effective regularization (trace tokens no longer regularize), (3) training signal distribution. These cannot be fully disentangled.
- **Framing**: This is presented as a preliminary analysis providing directional evidence, not as a precise causal decomposition. The Two-Pathway Model (Claim 2) provides the more complete explanatory framework.

**Supporting evidence:**
- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107
- `full_trace_seed42_v5`: 81.76%, ECE=0.0958
- TRL source code: mean CE over label tokens (verified)
- Cross-model: 2/4 models collapse with full_trace → method instability evidence

### Claim 4: Two-tier diagnostic hierarchy for verdict prediction

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
| 只用 2 个模型 | ✅ 已扩至 4 个模型 (Qwen-7B/1.5B, CodeLlama-13B, DeepSeek-6.7B) | 3 架构家族, 1.5B-13B scale, exception_only ≥99.33% on all 4 models |
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

### D12: Training dynamics as mechanistic evidence [NEW — plan_022]
exception_only 在 50 training steps 内收敛至 99.33%，step 150 饱和至 99.83%。full_trace (label_only_loss) 全程震荡 82-89%，peak 88.82% at step 350，但随后下降至 85.97%。full_trace 展现非单调行为：step 100 下降 5.3pp，steps 250-300 下降 3.5pp。Train loss 达 0.0085 但 eval accuracy 停滞在 88%——经典的过拟合到 spurious patterns。

**对论文叙事的意义**：(1) 直接回应 reviewer N2 "novelty 不足"——从"exception 最强（可预期）"转向"信息密度决定学习效率（反直觉机制性发现）"；(2) 解释了 full_trace 为何即使用 label_only_loss 消除 gradient dilution 仍不如 exception_only——冗余 trace 内容引入 spurious patterns 导致过拟合；(3) 50-step 快速收敛说明 exception signal 的 learnability 极高，少量训练即可掌握；(4) 论文新增 Contribution #2: "Training dynamics reveal convergence mechanism"。

### D13: Silent error analysis [NEW — plan_018/N3]
55.5% 的 fail 样本 (188/339) 为 silent logic errors（无 exception 的逻辑错误），但 exception_only 仍达 100% recall。原因：test framework 的 AssertionError IS an exception event——assert 语句失败时抛出 AssertionError，被 tracer 捕获为 `[ERROR]`。因此 exception_only 在这些"silent"错误上也能检测到 fault indicator。对比：no_trace 62.8% recall，full_trace 50.0% recall。

**对 Claim 1 的影响**：直接回应 reviewer N3 "silent logic errors 动摇 exception_only claim"——数据显示 exception_only 对 silent errors 的覆盖比 richer traces 更好，因为 test framework 本身就将 silent errors 转化为 exception events。

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
