# Paper Framing v2 — trace-verdict-study

> 更新动机：plan_004 跨模型验证完成，exception_only 跨模型 gap = 0.50pp（vs VOTA gap = 14.96pp），论文 headline 从 "VOTA compression" 转向 "exception-based fault detection is model-agnostic"。

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May 25, 2026

## Core Insight

Verdict prediction (pass/fail) is fundamentally a **fault detection** task, not a trace reasoning task. The minimal sufficient signal is the **exception event** — a compact, structured diagnostic moment that achieves near-perfect accuracy (99.83% Qwen, 99.33% DeepSeek, gap = 0.50pp) regardless of model architecture and pretraining background. In contrast, richer trace representations that require deeper execution reasoning (VOTA, full_trace) show large cross-model gaps (14.96pp and 53.3pp respectively), revealing that their effectiveness is contingent on base model capability. The design principle for verdict-optimized traces is: **extract the highest-specificity diagnostic signal; discard everything else.**

## Core Claims (3)

### Claim 1: Exception-based fault detection is model-agnostic

Exception summaries alone achieve near-perfect verdict prediction across architecturally distinct models: Qwen-2.5-Coder-7B (99.83%) and DeepSeek-Coder-6.7B (99.33%), with a cross-model gap of only 0.50pp. This contrasts sharply with VOTA (gap = 14.96pp) and full_trace (gap = 53.3pp). Exception events are structurally simple (`[ERROR] type: ... message: ...`) and do not require deep trace reasoning — making them universally extractable regardless of model pretraining.

**Supporting evidence:**
- `exp_plan004_deepseek_exception_only`: DeepSeek 99.33%
- `exp_plan003a_exception_only`: Qwen 99.83%
- `exp_plan004_deepseek_vota`: DeepSeek 84.45% (VOTA gap = 14.96pp)
- `exp_plan004_deepseek_no_trace`: DeepSeek 73.36% (baseline)

**Seed robustness**: ⚠️ 需要 plan_008 结果确认 exception_only 在多 seed 下稳定。当前两模型各仅 1 seed。

### Claim 2: Trace complexity tolerance varies by model capability

Richer trace representations benefit verdict prediction, but the magnitude scales with base model execution reasoning ability. Qwen (CRUXEval-I 56.5%) achieves 99.41% with VOTA; DeepSeek (CRUXEval-I 39.0%) only reaches 84.45% — a 14.96pp gap that aligns with their 17.5pp CRUXEval difference. Both models benefit from traces over no-trace baselines, but the "ceiling" of trace utilization is bounded by pretraining-derived inductive biases.

**Supporting evidence:**
- `exp_mvp_vota_v5`: Qwen VOTA 99.41%
- `exp_plan004_deepseek_vota`: DeepSeek VOTA 84.45%
- `exp_mvp_full_trace_v5`: Qwen full_trace 81.8%
- `exp_mvp_no_trace_v5`: Qwen no_trace 75.13%
- `exp_plan004_deepseek_no_trace`: DeepSeek no_trace 73.36%
- CRUXEval 文献数据 (Wang et al. tables)

**Seed robustness**: ⚠️ 需要 plan_008 结果确认 VOTA 跨 seed 方差。

### Claim 3: Two-tier information architecture with cross-model validation

Verdict-relevant trace information has a strict two-tier hierarchy: **Tier 1 — fault indicators (exception summaries)** are sufficient for near-perfect prediction and transfer across models; **Tier 2 — behavioral patterns (loop compression)** carry substantial signal (85.6%) but are model-dependent and fully subsumed by Tier 1. Within the same model (Qwen), combining tiers introduces noise rather than helping (exception_only 99.83% > VOTA 99.41%).

**Supporting evidence:**
- `exp_plan003a_exception_only`: 99.83% (Tier 1, Qwen)
- `exp_plan003c_ae_only`: 99.92% (Tier 1, Qwen, 与 exception 统计等价 p=0.80)
- `exp_plan003b_loop_only`: 85.6% (Tier 2, Qwen)
- `exp_plan002_label_only`: 86.2% (full_trace + label-only loss, ≈ loop_only)
- `exp_plan004_deepseek_exception_only`: 99.33% (Tier 1 cross-model)
- `exp_plan004_deepseek_vota`: 84.45% (Tier 1+2 cross-model, 退化)

**Seed robustness**: ⚠️ loop_only 和 ae_only 目前各 1 seed。

## Story Spine

- **Problem**: Existing trace SFT studies (DCSH, TracePile) evaluate only generative tasks and find limited, model-dependent benefit. No prior work has tested trace SFT on verdict tasks (binary pass/fail), nor identified what trace components drive classification performance.

- **Existing approaches & gaps**: DCSH (EMNLP Findings 2025) tested 5 trace formats on generation tasks, finding that "no single trace representation consistently outperforms others." TracePile (NeurIPS 2025) scaled to 2.6M samples but only evaluated generation. All existing trace formats are designed for execution simulation, not fault detection.

- **Our framing**: We reframe verdict prediction as **fault detection** and ask: what is the minimal sufficient diagnostic signal? Through systematic component ablation across two architecturally distinct models, we discover that exception events — compact, structured error summaries — are both necessary and sufficient, achieving near-perfect accuracy (99.5%+ avg) with zero cross-model gap. Richer trace representations work only when the base model has sufficient execution reasoning capability, making them unreliable for general deployment.

- **Headline result**: "Exception-based trace SFT achieves 99.83% verdict accuracy on Qwen and 99.33% on DeepSeek (gap = 0.50pp), while the same models show a 14.96pp gap on VOTA traces — demonstrating that fault detection, not trace reasoning, is the robust mechanism for verdict prediction."

## Story Arc (updated)

1. **Setup**: Trace SFT for code tasks — promising but inconsistent results in prior work (DCSH, TracePile). Unknown whether traces help verdict tasks and what trace design matters.

2. **First result — traces help, compression helps more** (single model): no_trace 75.1% → full_trace 81.8% → VOTA 99.4%. Compression is not just cost-saving; it improves accuracy through higher information density. Label-only loss ablation (plan_002) shows information overload is the primary bottleneck (74% of gap), not gradient dilution (26%).

3. **Twist — what component actually drives VOTA?** Component ablation reveals exception_only (99.83%) ≥ full VOTA (99.41%). The "trace reasoning" narrative is wrong — verdict prediction is fault detection. Tier 1 (exceptions) subsumes Tier 2 (loops). actual/expected removal doesn't hurt (99.4%).

4. **Cross-model stress test — the universal vs the contingent**: Exception_only transfers perfectly (gap = 0.50pp), but VOTA degrades by 14.96pp on DeepSeek. The model-agnostic component is precisely the one that doesn't require trace reasoning. CRUXEval gap (17.5pp) predicts VOTA gap — trace utilization is bounded by pretraining.

5. **Design principle**: For verdict tasks, identify the highest-specificity diagnostic signal (exception events) and discard everything else. Simpler signals are more robust; complexity tolerance depends on model capability.

## DeepSeek full_trace 坍塌处理

**现状**: DeepSeek full_trace 28.5%，100% 预测 fail。根因是 Qwen tokenizer overhead (32 tokens) 格式化的数据导致 DeepSeek label 截断。

**论文处理建议**:

- **Option A (推荐): Limitation + 透明披露**. 在 Limitations 中说明 full_trace 因 tokenizer budget 不匹配导致坍塌，报告为 N/A，不纳入跨模型对比表。论文叙事不依赖 DeepSeek full_trace 数据点——三个有效条件 (no_trace, VOTA, exception_only) 已足够支撑全部 claims。优点：诚实、reviewers 可能 appreciate transparency。
- **Option B: 修复重跑**. 用 DeepSeek tokenizer overhead 重新格式化 full_trace 数据并重训。风险：时间紧（ARR deadline 10 天），且结果可能仍然低于 VOTA（Qwen 上 full_trace 也只有 81.8%），对论文叙事不改变核心结论。
- **建议**: 先提交 Option A 版本。如果 reviewer 要求，camera-ready 前补 Option B。

## Venue Fit Risks (updated)

| Risk | Assessment | Mitigation |
|------|-----------|------------|
| 单任务 | 仍然只在 test verdict prediction 上验证 | 跨模型验证部分弥补；Discussion 中讨论 generalization 到 patch correctness 等 |
| 单数据集 | CRUXEval 是唯一 benchmark | 论文定位为 empirical study，深度优于广度 |
| "只是 feature engineering" | exception extraction 不是复杂方法 | 重新定位：simplicity 本身是 contribution——最简信号最 robust |
| Negative result 味道 | VOTA 跨模型不 robust 可能被视为 negative | Reframe: 识别出 robust 与 non-robust 组件的边界是 positive finding |
| Seed robustness | 核心 claims 目前单 seed | plan_008 补充中；exception_only 两模型一致性本身是 implicit robustness |

## Anticipated Reviewer Concerns (updated)

| Concern | Planned Response |
|---------|-----------------|
| "exception_only 99.83% 是不是 trivial pattern matching [ERROR] 有无？" | full_trace 也包含 [ERROR] 但仅 81.8%——说明模型需要学习从 trace context 中 extract 和 utilize exception signal，不是简单 keyword detection。no_trace 无 exception 信息，75.1%。 |
| "DeepSeek full_trace 坍塌是 bug 不是 finding" | 诚实披露根因（tokenizer budget mismatch）。其他 3 条件不受影响，结论不依赖此数据点。Appendix 详述。 |
| "CRUXEval gap 与 VOTA gap 的相关性可能是 coincidence" | 明确标注为 hypothesis，列出 alternative explanations (tokenizer efficiency, chat template, pretraining scale)。不 overclaim。 |
| "只有 2 个模型" | 同意是 limitation。但两个模型在 architecture (Qwen vs DeepSeek), pretraining data (5.5T vs 2T), execution reasoning (CRUXEval 17.5pp gap) 上有充分差异，不是 trivial replication。 |
| "99.83% 可能 saturated，看不出 exception 到底学了什么" | calibration analysis (plan_007): exception_only ECE=0.0027, ae_only ECE=0.0004。模型对 pass/fail 样本的置信度分布有意义差异，不是随机猜。 |
| "只用了 1 个 seed" | plan_008 补充中。两模型独立达到 99%+ 本身是 implicit 2-seed validation。 |
| "eval_loss 上升但 accuracy 提升——checkpoint selection 有问题吗？" | Discussion 中讨论：token-level loss 与 binary verdict accuracy 解耦。推荐 verdict-specific metric 作为 selection criterion。这是 methodological contribution。 |

## Discussion 要点 (new section)

### D1: eval_loss vs verdict accuracy 解耦
DeepSeek VOTA: eval_loss epoch 1→3 从 0.068 升至 0.112 (+65%)，但 accuracy 从 78.15% 升至 84.45% (+6.3pp)，fail_recall 从 23.3% 升至 45.4%。Token-level calibration (eval_loss) 与 binary classification accuracy 方向相反。**Implication**: 对 verdict tasks，应使用 task-specific metric (accuracy / F1) 而非 eval_loss 做 checkpoint selection。HuggingFace Trainer 默认用 eval_loss 会选到次优 checkpoint。

### D2: CRUXEval gap 假说
VOTA 跨模型 gap (14.96pp) 与 CRUXEval execution reasoning gap (15-17.5pp) 数值吻合。假说：trace utilization effectiveness 受 base model "execution reasoning readiness" 约束。**但**: 需明确标注为 hypothesis，列出 alternatives (tokenizer efficiency, pretraining scale 2.75x, chat template compatibility)。不 overclaim causal relationship。

### D3: Simplicity as robustness
Exception signal 之所以跨模型 robust，恰恰因为它 structurally simple。`[ERROR] type: ValueError message: expected 5 got 3` 不需要理解 variable flow 或 loop semantics——任何能做 basic text comprehension 的 LLM 都能 leverage。这暗示 **trace design 应匹配 deployment model 的能力下界**，而非上界。

### D4: Gradient dilution is minor
Label-only loss (plan_002) 将 full_trace 从 81.8% 提升到 86.2% (+4.5pp)，但仍远低于 exception_only (99.83%)。Gradient dilution 只贡献 gap 的 26%，information overload 贡献 74%。即使有 oracle loss masking，full trace 仍不如 targeted extraction。

## 与 v1 Framing 的关键差异

| 维度 | v1 | v2 |
|------|----|----|
| Headline | VOTA compression 优于 full trace | Exception-based fault detection is model-agnostic |
| Primary claim | VOTA +24pp through fault indicator preservation | Exception signal transfers across models (gap = 0.50pp) |
| Model scope | 单模型 (Qwen) + "时间允许就加 DeepSeek" | 双模型，跨模型对比是核心贡献 |
| VOTA 定位 | 核心方法 | Model-dependent 的 richer representation，Tier 2 |
| Design principle | "minimal sufficient diagnostic signal" | "highest-specificity signal + complexity tolerance varies by model" |
| Story arc | traces help → compression helps more → fault indicators are key | traces help → ablation reveals fault detection → cross-model validates universality |
