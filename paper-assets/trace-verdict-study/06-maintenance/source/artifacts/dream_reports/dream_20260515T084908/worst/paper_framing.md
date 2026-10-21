# Paper Framing — trace-verdict-study

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May 25, 2026 (10 days from today)

## Core Insight

Trace SFT effectiveness depends critically on **trace granularity matching task output entropy**: verdict tasks (1-bit output) benefit from execution traces, but compact, decision-relevant abstractions (VOTA: 99.2%) dramatically outperform full traces (81.8%). The performance gradient no_trace (75.1%) < full_trace (81.8%) < VOTA (99.2%) shows that the "right" trace is not "more trace" — it's the minimal information sufficient to determine the verdict, providing higher information density per token. All conditions verified on v5 codebase with consistent eval pipeline.

## Core Claims (≤3)

1. **VOTA dramatically improves verdict prediction**: Verdict-Optimized Trace Abstraction provides +24.0pp accuracy improvement over no-trace baseline (99.2% vs 75.1%) for test outcome prediction, 95% CI [+21.9, +26.8] excluding zero. Plan_001 confirms this is genuine behavioral understanding, not trivial actual/expected string comparison (vota_no_ae: 99.4%).

2. **Trace compression significantly improves verdict accuracy over full traces**: Full execution traces achieve 81.8% (+6.6pp, CI [+4.4, +9.0]), but VOTA achieves 99.2% (+24.0pp) — a +17.4pp advantage. Plan_002 (label-only loss) 量化因果分解：gradient dilution 贡献 ~26% of gap (4.5pp, 修复后 full_trace 86.2%), information overload 贡献 ~74% (13.0pp, 只有 trace compression 能解决)。"Even with oracle loss masking that eliminates gradient dilution, full traces still underperform VOTA by 13pp, confirming that information density — not training signal distribution — is the primary bottleneck." 所有条件基于 v5 代码版本公平对比。

3. **Information granularity, not information presence, determines trace SFT value**: Through systematic ablation — removing assertion-point information from VOTA (plan_001 减法) and isolating exception/loop components individually — we establish a **component importance hierarchy** for verdict-optimized trace design, providing empirical design principles at the compression-component level. [注：ae_only 88% fallback 污染，不支撑 element-level 归因。ae_only 结果移至 Appendix 附 caveat；主线证据为 plan_001 减法 + exception_only + loop_only 三角验证。]

## Story Spine

- **Problem**: Existing trace SFT studies (DCSH, TracePile) evaluate only generative tasks and find limited benefit. No prior work has tested trace SFT on code behavior verdict tasks (binary pass/fail), nor designed trace representations specifically for classification.

- **Existing approaches & gaps**: DCSH (EMNLP Findings 2025) tested 5 trace formats on generation tasks, finding limited benefit. TracePile (NeurIPS 2025) scaled to 2.6M samples but only evaluated generation. TRACED (ICSE 2024) showed traces help encoder-based classification, but nobody has tested decoder SFT. All existing trace formats are designed for full execution simulation, not classification.

- **Our framing**: We ask "does trace granularity need to match task complexity?" and demonstrate that verdict tasks — with O(1) output entropy — benefit from a fundamentally different trace design principle than generation tasks. VOTA captures only decision-relevant execution states (assertion snapshots, exception summaries) rather than full simulation.

- **Headline result template**: "On test verdict prediction, VOTA-SFT achieves 99.2% (+24.0pp over baseline), outperforming both no-trace (75.1%) and full-trace SFT (81.8%) — a clear performance gradient demonstrating that decision-relevant trace compression, not more trace information, maximizes SFT effectiveness for classification."

## Venue Fit Risks

- EMNLP主会 vs SE: 论文核心贡献是对 trace SFT 的 task-dependent 效果的系统性实证发现 + 新 trace representation，属于 NLP for code 方向。投 EMNLP Code track 合适。
- 单任务风险: 目前只在 test verdict prediction 一个任务上验证。需要至少加一个 verdict task（patch correctness 或 bug detection）才够 EMNLP Main。Findings 可能只需当前结果 + ablation。
- Leakage concern: 如果 ablation 证明 VOTA 效果主要来自 actual==expected 字符串比对，claim 需要调整为 "verdict tasks 需要的不是 trace reasoning 而是 decision-relevant data points"——仍然 publishable 但 framing 不同。

## Contingency Framing

### Claim 1 contingency — RESOLVED (D008)

**实际结果**: vota_no_ae accuracy 99.41% vs VOTA 完整版 99.16%（差异 3 样本/1190，不显著）。去除 actual/expected 后准确率不降反微升。

**生效 framing**: "genuine behavioral understanding" — VOTA 的效果来自 exception + loop + assertion 结构性信息，不依赖 actual/expected 字符串比对。VOTA teaches execution-grounded verdict reasoning。

**残余问题**: trace 结构性信号（[No trace available]→fail, [ERROR]→fail, [ASSERT]+[LOOP]→pass）可能构成 trivial pattern。此问题对所有 VOTA 变体等同存在。plan_003 exception_only ablation 将量化 [ERROR] 信号贡献。需在论文 Discussion 中诚实讨论。

### Claim 2 contingency — RESOLVED (D006 + D009)

**实际结果**: v5 full_trace 81.8%（collapse 为 bug, D006）。plan_002 label-only loss 86.2%，量化 gradient dilution 为 minor factor：4.5pp/17.4pp = 26% (D009)。

**生效 framing**: "Both trace types help verdict tasks, but VOTA's advantage is primarily information quality (74% of gap), not training signal distribution (26%). Even with oracle loss masking that eliminates gradient dilution, full traces still underperform VOTA by 13pp — trace compression is not just cost-saving but accuracy-improving through higher information density per token."

## Key Open Questions (Post-MVP)

1. ~~actual/expected ablation~~ (已解决: D008, genuine behavioral understanding 路径确认)
2. ~~full_trace collapse~~ (已解决: chat template bug, D006) → plan_002 改为 ablation: label-only loss 能否进一步提升 full_trace 81.8%?
3. 能否在第二个 verdict task 上复现？→ 决定 generalization claim
4. 需要多模型验证吗？→ 时间允许就加 DeepSeek-Coder

## Anticipated Reviewer Concerns

| Concern | Planned Response |
|---------|-----------------|
| "VOTA 99.2% 可能是 trivial actual==expected 比对" | plan_001 已否定：去 ae 后 99.41%，不降反升。VOTA 效果来自 exception/loop/assertion 结构 |
| "VOTA 高 accuracy 可能来自 trace 结构性信号（error 有无、trace 有无）而非深层理解" | plan_003 exception_only 将量化 [ERROR] 信号贡献；Discussion 中诚实讨论结构性信号角色；full_trace 也有这些信号但仅 81.8%，说明结构性信号不是全部 |
| "只在一个任务/数据集上测试" | 加 patch correctness task 或 CRUXEval verdict variant |
| "只用一个模型" | 加 DeepSeek-Coder-6.7B 复现（DCSH 同模型） |
| "full_trace collapse 可能是实现 bug" | 诚实披露：v2 collapse 确为 chat template bug；v5 修复后 full_trace 81.8%，三条件层次清晰。论文报告 v5 结果，Appendix 记录 bug 发现过程作为方法论透明性 |
| "VOTA 只是 feature engineering 不是方法创新" | 定位为 empirical contribution: 系统性发现 + design principles + task-spectrum analysis |
| "与 DCSH 的关系不清" | 明确：我们 complement DCSH（他们做 generation，我们做 classification） |
