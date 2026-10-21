# Paper Framing — trace-verdict-study

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May 25, 2026 (10 days from today)

## Core Insight

Trace SFT effectiveness depends critically on **trace granularity matching task output entropy**: verdict tasks (1-bit output) benefit massively from compact, decision-relevant trace abstractions (VOTA: +20.5pp), while full execution traces cause model collapse (-46.6pp) due to gradient dilution. The "right" trace is not "more trace" — it's the minimal information sufficient to determine the verdict.

## Core Claims (≤3)

1. **VOTA dramatically improves verdict prediction**: Verdict-Optimized Trace Abstraction (assertion-point state snapshots) provides +20.5pp accuracy improvement over no-trace baseline for test outcome prediction, with 95% CI [+17.7, +23.4] excluding zero.

2. **Full execution traces hurt verdict tasks**: Dense, uncompressed execution traces cause model collapse (28.49% accuracy, 100% predicting "fail") due to classification gradient dilution by trace token prediction — a task-representation mismatch that worsens with trace length.

3. **Information granularity, not information presence, determines trace SFT value**: Through systematic ablation of VOTA components (actual/expected values, exception summaries, loop compression), we identify which trace elements carry verdict-relevant signal vs. noise, providing design principles for task-optimized trace representations.

## Story Spine

- **Problem**: Existing trace SFT studies (DCSH, TracePile) evaluate only generative tasks and find limited benefit. No prior work has tested trace SFT on code behavior verdict tasks (binary pass/fail), nor designed trace representations specifically for classification.

- **Existing approaches & gaps**: DCSH (EMNLP Findings 2025) tested 5 trace formats on generation tasks, finding limited benefit. TracePile (NeurIPS 2025) scaled to 2.6M samples but only evaluated generation. TRACED (ICSE 2024) showed traces help encoder-based classification, but nobody has tested decoder SFT. All existing trace formats are designed for full execution simulation, not classification.

- **Our framing**: We ask "does trace granularity need to match task complexity?" and demonstrate that verdict tasks — with O(1) output entropy — benefit from a fundamentally different trace design principle than generation tasks. VOTA captures only decision-relevant execution states (assertion snapshots, exception summaries) rather than full simulation.

- **Headline result template**: "On test verdict prediction, VOTA-SFT achieves 95.6% accuracy (+20.5pp over no-trace baseline), while full execution trace SFT collapses to 28.5% — demonstrating that trace design granularity, not presence, determines SFT effectiveness for classification."

## Venue Fit Risks

- EMNLP主会 vs SE: 论文核心贡献是对 trace SFT 的 task-dependent 效果的系统性实证发现 + 新 trace representation，属于 NLP for code 方向。投 EMNLP Code track 合适。
- 单任务风险: 目前只在 test verdict prediction 一个任务上验证。需要至少加一个 verdict task（patch correctness 或 bug detection）才够 EMNLP Main。Findings 可能只需当前结果 + ablation。
- Leakage concern: 如果 ablation 证明 VOTA 效果主要来自 actual==expected 字符串比对，claim 需要调整为 "verdict tasks 需要的不是 trace reasoning 而是 decision-relevant data points"——仍然 publishable 但 framing 不同。

## Contingency Framing (based on ablation outcome)

**If ablation shows genuine behavioral understanding** (去 actual/expected 后仍有显著提升):
→ Full positive framing: "VOTA teaches execution-grounded verdict reasoning"

**If ablation shows primarily string matching** (去 actual/expected 后 accuracy 大幅下降):
→ Adjusted framing: "For verdict tasks, the critical trace element is the assertion-point state — not behavioral reasoning but targeted state comparison. This is still a novel finding because: (a) no one knew this before testing, (b) it explains WHY full traces fail (too much irrelevant state), (c) it provides practical design principles."

## Key Open Questions (Post-MVP)

1. actual/expected ablation 结果如何？→ 决定 Claim 1 的强度
2. full_trace + label-only loss 能否修复 collapse？→ 加强 Claim 2 的解释
3. 能否在第二个 verdict task 上复现？→ 决定 generalization claim
4. 需要多模型验证吗？→ 时间允许就加 DeepSeek-Coder

## Anticipated Reviewer Concerns

| Concern | Planned Response |
|---------|-----------------|
| "VOTA 95.63% 可能是 trivial actual==expected 比对" | ablation 实验直接回应（P0 优先级） |
| "只在一个任务/数据集上测试" | 加 patch correctness task 或 CRUXEval verdict variant |
| "只用一个模型" | 加 DeepSeek-Coder-6.7B 复现（DCSH 同模型） |
| "full_trace collapse 可能是实现 bug" | label-only loss ablation 验证是 gradient dilution 而非 bug |
| "VOTA 只是 feature engineering 不是方法创新" | 定位为 empirical contribution: 系统性发现 + design principles + task-spectrum analysis |
| "与 DCSH 的关系不清" | 明确：我们 complement DCSH（他们做 generation，我们做 classification） |
