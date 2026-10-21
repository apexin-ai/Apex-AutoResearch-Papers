# Director coordination — Part 6 of 12

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

[← Part 5](part-005.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 7 →](part-007.md) · [Structured JSON](../../../sessions/b1/b1d47a1a2aa91fd38090.json)

## Round 121

### Tool call

_source line 1434 · 2026-05-20T04:37:37.089144+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# === Resolved issues from rounds 0-14 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: RV-D060-NARRATIVE\n  summary: D060 'Goodhart instability' 叙事确认成立\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\n  resolution_round: 2\n- id: RV-FIG2-STALE-SCRIPT\n  summary: figures/paper/gen_fig2.py 旧脚本数据错误\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 已修复。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review 再次提出 ISR syntactic-only gap（R1-N2/N3, R2-W5）。'structural integrity' 措辞仍暗示比 'component necessity' 更强的保证。尽管已修正术语，framing gap 在 Abstract/Introduction 仍可感知。\"\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R1-W4\n  summary: Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: exec-only 500-step 主表仅报告 s42（†标注）。\n  resolution_round: 2\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review 再次指出 seed 43 eval protocol 不一致（R1-W5, R2 AGREE）。1/3 seeds 不同解码策略影响 cross-seed 比较。\"\n- id: R1-W3\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: R2-W7\n  summary: 与 Kim et al. (2026) 差异化不充分\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: related_work.tex 中有区分段落。\n  resolution_round: 2\n- id: R1-W6\n  summary: 训练 500 例/评估 100 例的规模限制讨论不充分\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: limitations.tex 已讨论。\n  resolution_round: 2\n- id: R1-W7\n  summary: H1/H7 classifier precision/recall 未报告\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: 50 样本人工验证 precision >95%。\n  resolution_round: 2\n- id: R1-W8\n  summary: Random control U(0,1) 与 ISR 的 skewed 分布不匹配\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: method.tex 和 experiments.tex 均说明了 Random 设计目的。\n  resolution_round: 2\n- id: R1-W9\n  summary: 缺代码/数据开源承诺\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n- id: R1-W5\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: framing 降级为 empirical instance。\n  resolution_round: 3\n- id: R2-W8\n  summary: H1/H7 编号不连贯（H2-H6 不存在）\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: method.tex 解释了合并原因。\n  resolution_round: 3\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed，应改为 mean±std\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v2-R2-N3\n  summary: STA 方法论新颖性有限\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: novelty 定位为 applying standard LOO。\n  resolution_round: 3\n- id: v2-R2-N2\n  summary: 单模型+单数据集泛化性不足\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: cross-scale 实验加入。单数据集限制在 Limitations 讨论。\n  resolution_round: 3\n- id: v2-R1-W3\n  summary: ISR-as-reward 控制 confound 后净效果仅 1.06×\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 15\n  resolution: ISR 定位从 training signal 转为 diagnostic-only。\n  resolution_round: 3\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review 再次将 premise-count confound 列为 critical Must-Fix（R1-N3, R2 AGREE）。尽管 ISR 已定位为 diagnostic-only，3.2×→1.06× 的发现在正文中位置仍不够突出。简单 length penalty 可达类似效果的问题未被正面回应。\"\n- id: v2-R1-W6\n  summary: Hacking taxonomy 缺乏 IAA 验证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: deterministic rules + 50-sample precision check。\n  resolution_round: 3\n- id: v2-R2-W3\n  summary: Abstract 信息密度过高\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 重写为 ~170 words。\n  resolution_round: 3\n- id: v2-R2-W4\n  summary: Premise-count confound 讨论放在 Appendix 而非正文\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 提升到正文 §3.2。\n  resolution_round: 3\n- id: v2-R2-W5\n  summary: C2 和 C4 独立性不足\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: taxonomy 独立性论证成立。\n  resolution_round: 3\n- id: v2-FMT-1\n  summary: Limitations section 位于 References 之后\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 顺序已正确。\n  resolution_round: 3\n- id: v2-FMT-2\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: ethics.tex 加入。\n  resolution_round: 3\n- id: v2-FMT-3\n  summary: Orphan bibliography entries\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: orphan entries 清除。\n  resolution_round: 3\n- id: v2-R1-M4\n  summary: Prolog cross-logic transfer 样本量过小\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 qualitative observation。\"\n  resolution_round: 3\n- id: v2-R1-W1\n  summary: 3 seeds 统计效力不足以支撑定量 claims\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 统计方法改进。定量 claims 降级。\n  resolution_round: 3\n- id: v2-R1-W4\n  summary: SFT baseline 比较因 PR 悬殊说服力有限\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 100-step RL 对照充分利用。\n  resolution_round: 3\n- id: R2-MISSING-REF\n  summary: 引用覆盖不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: 31 条引用覆盖核心领域。\n  resolution_round: 3\n- id: v3-R1-NI-2\n  summary: β=0.2 未在 Table 1 中独立报告\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: Table 1 现已包含 β=0.2 行。\n  resolution_round: 4\n- id: v3-R1-NI-3\n  summary: §4.2 cross-seed 描述暗示最终状态\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"现标注 '(at 500 steps)'。\"\n  resolution_round: 4\n- id: v3-R12-NI-4\n  summary: 全文 em-dash AI 写作痕迹\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。\n  resolution_round: 5\n- id: v3-R2-NI-5\n  summary: \"Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero...at convergence'。\"\n  resolution_round: 4\n\n# === In-progress issues (updated with round 15) ===\n- id: v3-R12-NI-1\n  summary: Cross-scale 实验 seed 数量不足\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 15\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 两位 reviewer 一致。\n  - round: 10\n    reviewers: [1, 2]\n    note: 现已用 D129 完整 3-seed 数据重写 §4.5。\n  - round: 11\n    reviewers: [1]\n    note: \"R1-W4: 3 seeds 仍不足以作为独立 contribution 支撑。\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R1-N1 再次要求增加模型/数据集多样性。R2-N3 将 C3 cross-logic 定为 preliminary。\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 R2-W1: C3 仍在同一 dataset (FOLIO) 和 model family (Qwen3) 内。\"\n  - round: 14\n    reviewers: []\n    note: \"R14: 未直接提及。C3 已 hedge 为 'in principle...preliminary'。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: 两位 reviewer 独立将 3-seed 统计效力列为 critical Must-Fix（R1-N1, R2-N2）。单模型限制也被双方列为 Should-Fix（R1-W1, R2 同意）。结构性问题持续 13 轮未完全解决。\"\n- id: v4-R12-N3\n  summary: OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 15\n  mentions:\n  - round: 10\n    reviewers: [1, 2]\n    note: Table 1 和 Discussion §5 仍以 23% (uncorrected) 为 headline。\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 fix: transient window 降级为 descriptive observation。\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: Table 1 用 corrected 6%†。方向反转未在正文讨论。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: premise-count confound (3.2×→1.06×) 被 R1 列为 critical Must-Fix（N4），R2 完全同意。方向反转问题仍活跃——ISR N-H 6.06% < Random 9.5%。\"\n- id: v4-R12-W6\n  summary: Seed 43 exec-only 评估协议矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 14\n  resolution: §4.2 line 34 脚注说明 sampling eval (T=0.7) 及不可比性。\n  resolution_round: 14\n- id: v4-R12-W7\n  summary: Deleted checkpoints (ISR β=0.1 s43/s44) 导致 H8 audit 不完整\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 14\n  resolution: \"Table 1 caption 标注 'N-H is an upper bound'。Method §3.5 line 76 声明。\"\n  resolution_round: 14\n- id: v4-R1-W8\n  summary: 100 eval samples 对 per-seed claims 统计功效不足\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 14\n  resolution: \"Matched cohort table 附完整 Wilson CIs。Limitations 量化 '100-example...Wilson 95% CI'。\"\n  resolution_round: 14\n- id: v4-R2-W9\n  summary: 方法新颖性有限：Algorithm 1 仅 6 行伪代码\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 15\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"共识: Findings 级别。\"\n  - round: 12\n    reviewers: [1, 2]\n    note: R1 Excitement 3/5, R2 2.5/5。两人均同意 Findings。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: Introduction 自我定位为 'empirical case study'。但 LOO 是标准技术。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: 两位 reviewer 均认为 STA 方法本身新颖性有限（LOO ablation 是标准范式），价值在于经验发现。R2 将概念新颖性列为 critical（N2）。\"\n- id: v4-R2-W5\n  summary: 未测试 tautology-guarded ISR 变体\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 14\n  resolution: Future work. Gated ISR 部分回应。\n  resolution_round: 4\n- id: v5-R1-N3\n  summary: Table 1 比较框架不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 14\n  resolution: \"Table 1 caption '500 steps unless noted'。\"\n  resolution_round: 14\n- id: v5-R2-N3\n  summary: \"'Diagnostic becomes optimization target' 概念新颖性有限\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 15\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: R2-N2 [critical]。R1 认为 empirical phenomena 有独立价值但同意 Findings。\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R2 进一步论证: ISR 的不对称性原因 'too straightforward'。\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: Gated ISR 增量改善。但概念新颖性限制仍为结构性问题。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: R2 将 'meta-level Goodhart' 概念新颖性列为 critical Must-Fix（N2）。R1 agree with nuance——empirical details 超出可预测范围但术语过度包装。两人一致建议 reframe 为 empirical instantiation。持续 11 轮的结构性问题。\"\n- id: v5-R2-W1\n  summary: Abstract 数据堆砌 / 单 seed 数据选择性报告\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 14\n  resolution: Abstract 改用 3-seed aggregate。\n  resolution_round: 14\n- id: v5-R2-W3\n  summary: paragraph{} 过度碎片化\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 14\n  resolution: 段落结构大幅改善。\n  resolution_round: 14\n- id: v5-R2-W4\n  summary: Experiments §4.3 按 β 值呈现顺序非升序\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 10\n  resolution: §4.3 已按升序呈现。\n  resolution_round: 10\n- id: v5-R12-SFT-PR\n  summary: SFT baseline PR confound (PR=13% vs 93%)\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 15\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 fix: Abstract 加 caveat。\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R1-N1: RL-specificity claim 依赖此对比但证据基础薄弱。\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: hedging 全面改善。但 §4.2 line 42 仍用 'RL-specific' 旧措辞。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: R1 列为 Should-Fix (W3)——SFT 用 gold annotations 训练引入 data quality confound。R2 agree with nuance: SFT 主要功能是控制 RL optimization 作为 hacking 来源，confound 影响被 R1 略高估。\"\n- id: v5-R2-MR\n  summary: 缺少重要引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 14\n  resolution: 新增 Llemma、Coste 2024、Moskovitz 2024。\n  resolution_round: 14\n- id: v5-R2-W6\n  summary: Table 1 信息密度过高\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 10\n  resolution: 已拆分。\n  resolution_round: 12\n- id: v5-R1-W5\n  summary: Goodhart taxonomy variant 未指定\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"related_work.tex 指定 'primarily regressional, with extremal elements'。\"\n  resolution_round: 7\n- id: v5-R1-W6\n  summary: ISR reward landscape 几何结构未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: experiments.tex 包含 reward landscape 分析。\n  resolution_round: 7\n- id: v6-R2-N1\n  summary: ISR 核心指标命名不一致\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: 全文统一使用 Intensional Structural Reward。\n  resolution_round: 7\n- id: v6-R2-W5\n  summary: \"ISR 名称含 'Reward' 具有误导性\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: 已统一命名。\n  resolution_round: 7\n- id: v6-R1-W2\n  summary: Dose-response claim 统计上不足\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 14\n  resolution: \"§4.2 line 110 标注 'preliminary'。\"\n  resolution_round: 14\n- id: v6-R2-W2\n  summary: §4.3 的 β 值呈现顺序非升序\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: 已按升序呈现。\n  resolution_round: 10\n- id: v6-R2-W6-LOO\n  summary: LOO 缩写未在首次使用时正式定义\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: introduction.tex 现有完整定义。\n  resolution_round: 7\n- id: v6-R2-W8\n  summary: Hacking taxonomy 分类标准不够 principled\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 15\n  mentions:\n  - round: 11\n    reviewers: [1]\n    note: 仅 H1/H7 有 precision 验证。\n  - round: 12\n    reviewers: [1, 2]\n    note: \"Abstract 改为 'three robust modes + additional isolated observations'。\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"CE/TS/PG/CI 重命名改善可读性。分类标准仍为规则+功能分析混合。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: 两位 reviewer 均列为 Should-Fix (R1-W4, R2-W3)。50 样本验证不足，无 IAA，text-match classifier 有已知 false-negative（Prolog 100% → functional analysis）。阈值敏感性未分析。持续 10 轮。\"\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation p=0.26 为 primary。\n  resolution_round: 9\n- id: v7-R2-MR1\n  summary: 缺少 Goodhart's Law 经典引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: references.bib 包含 Goodhart 1975。\n  resolution_round: 8\n- id: v7-R2-W7\n  summary: \"experiments.tex 'Notably' AI 写作标记\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: 已移除。\n  resolution_round: 9\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 15\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1 Excitement 3/5, R2 2.5/5。两人均同意 Findings。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Gated ISR 增量改善。核心 novelty concern 仍为结构性限制。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: R2 将此列为 critical Must-Fix (N2)——'anti-cheating test 被用于评分后被 game ≠ meta-level cheating'。R1 agree with nuance。结构性问题持续 8 轮，无法通过修改解决。\"\n- id: v8-R1-N3\n  summary: 术语交替使用导致语义滑移\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14\n  resolution: H1→CE, H7→TS, H8→PG, H9→CI 全文重命名完整一致。\n  resolution_round: 14\n- id: v8-R12-N2\n  summary: 实验范围与标题/claim scope 不匹配\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14\n  resolution: \"C3 加 'in principle...preliminary'。Hedging 充分。\"\n  resolution_round: 14\n- id: v8-R1-W4\n  summary: 多重比较未校正\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 15\n  resolution: \"Appendix 标注 CMH 'p-values are consequently inflated'。\"\n  resolution_round: 14\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: R1 再次列为 Should-Fix (W2)——6 conditions × 多指标 Fisher tests 无 Bonferroni/FDR。R2 AGREE。CMH 标注不等于全面的 multiple testing correction。\"\n- id: v8-R1-MR\n  summary: 缺少 reward shaping 和 inference-time hacking 引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: Uesato 2022, Paulus 2018, Langosco 2022 等已补充。\n  resolution_round: 10\n- id: v9-R1-N3\n  summary: Premise-count confound 影响范围分歧\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: method.tex 增加 confound 两场景区分句。\n  resolution_round: 9\n- id: v9-R12-W1\n  summary: §4.4 标题措辞过强\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"§4.4 标题改为 'Cross-Logic Extension'。\"\n  resolution_round: 9\n- id: v9-R1-W5\n  summary: 训练时 sampling vs 评估时 greedy 不一致\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: §4.1 已增加讨论。\n  resolution_round: 9\n- id: v9-R12-Q-ISR-FILTER\n  summary: ISR 作为 filter 未测试\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: conclusion.tex 增加 future work。\n  resolution_round: 9\n- id: v9-R12-Q-NORMALIZED-ISR\n  summary: 未测试 premise-count-normalized ISR\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: conclusion.tex 增加 future work。\n  resolution_round: 9\n- id: v4-RV-STALE-APPENDIX\n  summary: Appendix Table 仍用旧数据\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  resolution: Appendix Table 5 现含完整 per-seed data。\n  resolution_round: 7\n- id: v10-R12-N1\n  summary: §4.5 与 Limitations 关于 1.7B seed 数量矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: D129 完整 3-seed 数据重写 §4.5。\n  resolution_round: 11\n- id: v10-R2-Q6\n  summary: ISR=0.75 推导与实测不一致\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: 改为 ISR≥0.5。\n  resolution_round: 11\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers: [2]\n    note: \"建议改为 'Verified but Vacuous'。\"\n  - round: 14\n    reviewers: []\n    note: \"R14: 未再提及。\"\n  - round: 15\n    reviewers: []\n    note: \"R15: 未提及。可能不再是活跃问题。\"\n- id: v10-R2-W8\n  summary: Discussion/Conclusion 过于简短\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 14\n  resolution: Discussion 扩展至 14 行。含 gated ISR + mitigation 方向。\n  resolution_round: 14\n- id: v10-R2-W5\n  summary: C2 和 C4 边界不清晰\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: Contributions 合并为 3 条。\n  resolution_round: 10\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v11-R1-W2\n  summary: Taxonomy 仅 H1/H7 有 precision 验证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Abstract 'PG, observed at lower prevalence'。Claim 适当下调。\"\n  resolution_round: 14\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果未充分解释\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15: 未直接提及。R2 M4 建议 O(1) variant 值得更多主文讨论。\"\n- id: v11-R2-MR\n  summary: 缺少 2025-2026 最新引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: 新增 Llemma、Coste 2024、Moskovitz 2024。\n  resolution_round: 14\n- id: v11-R12-PDF\n  summary: PDF 与 .tex 不一致\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: PDF 从 paper/ 重编译。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v12-R2-W4\n  summary: Table 1 ISR β=0.1 ISR* 列缺失\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 1 补全。\n  resolution_round: 12\n- id: v12-R2-W2\n  summary: 与 Kim et al. (2026) 区分需更锐利\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"Related Work 新增完整 'Faithfulness in formalization' 段落。\"\n  resolution_round: 14\n- id: v12-R1-W2\n  summary: Component-count confound deconfounding analysis 仅在 Appendix\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: R1-N4 要求 premise-count confound 提升到 §4.3 显著位置。R2 完全同意。此问题从 info 升级为 critical。\"\n- id: v13-R2-N2\n  summary: 与 Kim et al. (2026) 差异化不充分\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Related Work 新增完整对比段落。\"\n  resolution_round: 14\n- id: v13-R1-W1\n  summary: \"ISR 与 NLI accuracy 无关 但 'structural quality diagnostic' 定位可能误导\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Method §3.2 line 46: 'ISR is a component-necessity diagnostic, not a reasoning-quality metric'。\"\n  resolution_round: 14\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高（~17 个缩写）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"~18 缩写，未添加 notation summary。H1→CE 等重命名改善可读性。R2 降为 minor。\"\n  - round: 15\n    reviewers: []\n    note: \"R15: 未提及。可能因 CE/TS/PG/CI 重命名已改善。\"\n- id: v13-R2-W5\n  summary: Table 2 混合 single-seed 和 pooled 数据\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Table 2 caption 标注聚合方式。\"\n  resolution_round: 14\n- id: v13-R2-MITIGATION\n  summary: Discussion 缺少 mitigation 策略讨论\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: Discussion 含 gated ISR + reward ensembling + constrained optimization + TRACE。\n  resolution_round: 14\n- id: v13-R1-Q4\n  summary: Prolog cross-logic 实验缺少 random control\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"§4.3 line 118: 'No matched random control was run for Prolog' 显式声明。\"\n  resolution_round: 14\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例 (96.7% non-hacking)\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Discussion 只提 '2/3 seeds migrate to PG'，忽略 s54。有选择性呈现嫌疑。\"\n- id: v14-R1-LIMITATIONS\n  summary: Limitations section 压缩至 6-7 行\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1]\n    note: 8 页限制下可理解，但 Limitations 不再是亮点。\n\n# === New issues from Round 15 (fresh review) ===\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——每个 seed 走向质性不同的 hacking 路径，aggregate 统计无解释力\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"两位 fresh reviewer 独立识别为 critical Must-Fix。R1: 'ProofFOL permutation test p=0.10 明确欠效力'，'汇总统计量几乎无解释力'。R2: '同一条件下 ISR 可差 40 倍'。R2 交叉时建议 'case study 定位比增加 seeds 更现实'。与历史 v3-R12-NI-1、v2-R1-W1 同源但独立发现。\"\n  action_items:\n  - round: 15\n    action: 增至 ≥5 seeds 或重新定位为 case study，降低跨条件定量声明强度\n    assigned_to: research_director\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 的直接实例而非新理论概念\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R2 核心论点: 经典 Goodhart 定义已覆盖此现象。R1 agree with nuance: empirical details 超出 a priori 预测但术语过度包装。两人一致建议 reframe 为 empirical instantiation + 显式对照 Manheim & Garrabrant 四类变种。与历史 v5-R2-N3、v8-R12-N1 同源。\"\n  action_items:\n  - round: 15\n    action: \"将 'meta-level Goodhart' reframe 为 empirical instantiation；显式对照四类变种\"\n    assigned_to: research_director\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: v15-R1-N3\n  summary: ISR syntactic-only 性质与 structural quality framing gap + 缺少人工评估\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1 列为 Must-Fix (N2): 'structural integrity' 措辞暗示比 'component necessity' 更强保证。R2 从 Should-Fix (W5) 升级为 Must-Fix after 交叉。两人一致要求 ~50 样本人工 faithfulness 标注 + ISR correlation。与历史 R1-W2、v13-R1-W1 同源但 fresh review 再次列为 critical。\"\n  action_items:\n  - round: 15\n    action: 人工标注 ~50 formalizations 的 semantic faithfulness 并报告与 ISR 的 correlation\n    assigned_to: research_director\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: v15-R1-N4\n  summary: Premise-count confound 控制后 ISR-as-reward 优势消失 (3.2×→1.06×)，length penalty 可能足够\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1 列为 Must-Fix (N3): '简单 length penalty 可能达到类似效果'。R2 交叉后完全同意: '确实严重削弱了 ISR-as-reward 的价值叙事'。两人一致要求提升此发现位置并正面回应 length penalty 问题。与历史 v2-R1-W3 (resolved)、v12-R1-W2 (open) 同源。此前 ISR 已定位为 diagnostic-only，但正文位置仍不够突出。\"\n  action_items:\n  - round: 15\n    action: 将 premise-count confound 发现提升至 §4.3 显著位置；直接回应 length penalty 替代方案\n    assigned_to: research_director\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: v15-R2-W1\n  summary: \"缺少 2025-2026 关键相关工作: LLMs Gaming Verifiers, Countdown-Code, Uesato, Cobbe\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R2: 'LLMs Gaming Verifiers' (arXiv:2604.15149) 和 'Countdown-Code' (arXiv:2603.07084) 与本文主题高度重叠，必须讨论。R1: Uesato et al. (2022) 和 Cobbe et al. (2021) 是 process reward 基础文献。R2 对 self-correction 综述 [REBUT]。\"\n  action_items:\n  - round: 15\n    action: \"讨论 LLMs Gaming Verifiers + Countdown-Code（必须），Uesato/Cobbe（推荐）\"\n    assigned_to: research_director\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: v15-R1-W2\n  summary: Multiple testing correction 缺失 (6 conditions × 多指标 Fisher tests)\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1 提出，R2 AGREE。与历史 v8-R1-W4 (resolved) 同源但 fresh reviewers 认为 Appendix CMH 标注不等于全面 correction。\"\n  action_items:\n  - round: 15\n    action: 报告 Bonferroni 或 FDR 校正后的 p-values\n    assigned_to: research_director\n    status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n# === Resolved issues from rounds 0-14 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: RV-D060-NARRATIVE\n  summary: D060 'Goodhart instability' 叙事确认成立\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\n  resolution_round: 2\n- id: RV-FIG2-STALE-SCRIPT\n  summary: figures/paper/gen_fig2.py 旧脚本数据错误\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 已修复。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review 再次提出 ISR syntactic-only gap（R1-N2/N3, R2-W5）。'structural integrity' 措辞仍暗示比 'component necessity' 更强的保证。尽管已修正术语，framing gap 在 Abstract/Introduction 仍可感知。\"\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R1-W4\n  summary: Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: exec-only 500-step 主表仅报告 s42（†标注）。\n  resolution_round: 2\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review 再次指出 seed 43 eval protocol 不一致（R1-W5, R2 AGREE）。1/3 seeds 不同解码策略影响 cross-seed 比较。\"\n- id: R1-W3\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: R2-W7\n  summary: 与 Kim et al. (2026) 差异化不充分\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: related_work.tex 中有区分段落。\n  resolution_round: 2\n- id: R1-W6\n  summary: 训练 500 例/评估 100 例的规模限制讨论不充分\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: limitations.tex 已讨论。\n  resolution_round: 2\n- id: R1-W7\n  summary: H1/H7 classifier precision/recall 未报告\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: 50 样本人工验证 precision >95%。\n  resolution_round: 2\n- id: R1-W8\n  summary: Random control U(0,1) 与 ISR 的 skewed 分布不匹配\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: method.tex 和 experiments.tex 均说明了 Random 设计目的。\n  resolution_round: 2\n- id: R1-W9\n  summary: 缺代码/数据开源承诺\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n- id: R1-W5\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: framing 降级为 empirical instance。\n  resolution_round: 3\n- id: R2-W8\n  summary: H1/H7 编号不连贯（H2-H6 不存在）\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: method.tex 解释了合并原因。\n  resolution_round: 3\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed，应改为 mean±std\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v2-R2-N3\n  summary: STA 方法论新颖性有限\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: novelty 定位为 applying standard LOO。\n  resolution_round: 3\n- id: v2-R2-N2\n  summary: 单模型+单数据集泛化性不足\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: cross-scale 实验加入。单数据集限制在 Limitations 讨论。\n  resolution_round: 3\n- id: v2-R1-W3\n  summary: ISR-as-reward 控制 confound 后净效果仅 1.06×\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 15\n  resolution: ISR 定位从 training signal 转为 diagnostic-only。\n  resolution_round: 3\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review 再次将 premise-count confound 列为 critical Must-Fix（R1-N3, R2 AGREE）。尽管 ISR 已定位为 diagnostic-only，3.2×→1.06× 的发现在正文中位置仍不够突出。简单 length penalty 可达类似效果的问题未被正面回应。\"\n- id: v2-R1-W6\n  summary: Hacking taxonomy 缺乏 IAA 验证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: deterministic rules + 50-sample precision check。\n  resolution_round: 3\n- id: v2-R2-W3\n  summary: Abstract 信息密度过高\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 重写为 ~170 words。\n  resolution_round: 3\n- id: v2-R2-W4\n  summary: Premise-count confound 讨论放在 Appendix 而非正文\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 提升到正文 §3.2。\n  resolution_round: 3\n- id: v2-R2-W5\n  summary: C2 和 C4 独立性不足\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: taxonomy 独立性论证成立。\n  resolution_round: 3\n- id: v2-FMT-1\n  summary: Limitations section 位于 References 之后\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 顺序已正确。\n  resolution_round: 3\n- id: v2-FMT-2\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: ethics.tex 加入。\n  resolution_round: 3\n- id: v2-FMT-3\n  summary: Orphan bibliography entries\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: orphan entries 清除。\n  resolution_round: 3\n- id: v2-R1-M4\n  summary: Prolog cross-logic transfer 样本量过小\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 qualitative observation。\"\n  resolution_round: 3\n- id: v2-R1-W1\n  summary: 3 seeds 统计效力不足以支撑定量 claims\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 统计方法改进。定量 claims 降级。\n  resolution_round: 3\n- id: v2-R1-W4\n  summary: SFT baseline 比较因 PR 悬殊说服力有限\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 100-step RL 对照充分利用。\n  resolution_round: 3\n- id: R2-MISSING-REF\n  summary: 引用覆盖不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: 31 条引用覆盖核心领域。\n  resolution_round: 3\n- id: v3-R1-NI-2\n  summary: β=0.2 未在 Table 1 中独立报告\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: Table 1 现已包含 β=0.2 行。\n  resolution_round: 4\n- id: v3-R1-NI-3\n  summary: §4.2 cross-seed 描述暗示最终状态\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"现标注 '(at 500 steps)'。\"\n  resolution_round: 4\n- id: v3-R12-NI-4\n  summary: 全文 em-dash AI 写作痕迹\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。\n  resolution_round: 5\n- id: v3-R2-NI-5\n  summary: \"Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero...at convergence'。\"\n  resolution_round: 4\n\n# === In-progress issues (updated with round 15) ===\n- id: v3-R12-NI-1\n  summary: Cross-scale 实验 seed 数量不足\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 15\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 两位 reviewer 一致。\n  - round: 10\n    reviewers: [1, 2]\n    note: 现已用 D129 完整 3-seed 数据重写 §4.5。\n  - round: 11\n    reviewers: [1]\n    note: \"R1-W4: 3 seeds 仍不足以作为独立 contribution 支撑。\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R1-N1 再次要求增加模型/数据集多样性。R2-N3 将 C3 cross-logic 定为 preliminary。\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 R2-W1: C3 仍在同一 dataset (FOLIO) 和 model family (Qwen3) 内。\"\n  - round: 14\n    reviewers: []\n    note: \"R14: 未直接提及。C3 已 hedge 为 'in principle...preliminary'。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: 两位 reviewer 独立将 3-seed 统计效力列为 critical Must-Fix（R1-N1, R2-N2）。单模型限制也被双方列为 Should-Fix（R1-W1, R2 同意）。结构性问题持续 13 轮未完全解决。\"\n- id: v4-R12-N3\n  summary: OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 15\n  mentions:\n  - round: 10\n    reviewers: [1, 2]\n    note: Table 1 和 Discussion §5 仍以 23% (uncorrected) 为 headline。\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 fix: transient window 降级为 descriptive observation。\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: Table 1 用 corrected 6%†。方向反转未在正文讨论。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: premise-count confound (3.2×→1.06×) 被 R1 列为 critical Must-Fix（N4），R2 完全同意。方向反转问题仍活跃——ISR N-H 6.06% < Random 9.5%。\"\n- id: v4-R12-W6\n  summary: Seed 43 exec-only 评估协议矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 14\n  resolution: §4.2 line 34 脚注说明 sampling eval (T=0.7) 及不可比性。\n  resolution_round: 14\n- id: v4-R12-W7\n  summary: Deleted checkpoints (ISR β=0.1 s43/s44) 导致 H8 audit 不完整\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 14\n  resolution: \"Table 1 caption 标注 'N-H is an upper bound'。Method §3.5 line 76 声明。\"\n  resolution_round: 14\n- id: v4-R1-W8\n  summary: 100 eval samples 对 per-seed claims 统计功效不足\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 14\n  resolution: \"Matched cohort table 附完整 Wilson CIs。Limitations 量化 '100-example...Wilson 95% CI'。\"\n  resolution_round: 14\n- id: v4-R2-W9\n  summary: 方法新颖性有限：Algorithm 1 仅 6 行伪代码\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 15\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"共识: Findings 级别。\"\n  - round: 12\n    reviewers: [1, 2]\n    note: R1 Excitement 3/5, R2 2.5/5。两人均同意 Findings。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: Introduction 自我定位为 'empirical case study'。但 LOO 是标准技术。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: 两位 reviewer 均认为 STA 方法本身新颖性有限（LOO ablation 是标准范式），价值在于经验发现。R2 将概念新颖性列为 critical（N2）。\"\n- id: v4-R2-W5\n  summary: 未测试 tautology-guarded ISR 变体\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 14\n  resolution: Future work. Gated ISR 部分回应。\n  resolution_round: 4\n- id: v5-R1-N3\n  summary: Table 1 比较框架不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 14\n  resolution: \"Table 1 caption '500 steps unless noted'。\"\n  resolution_round: 14\n- id: v5-R2-N3\n  summary: \"'Diagnostic becomes optimization target' 概念新颖性有限\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 15\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: R2-N2 [critical]。R1 认为 empirical phenomena 有独立价值但同意 Findings。\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R2 进一步论证: ISR 的不对称性原因 'too straightforward'。\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: Gated ISR 增量改善。但概念新颖性限制仍为结构性问题。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: R2 将 'meta-level Goodhart' 概念新颖性列为 critical Must-Fix（N2）。R1 agree with nuance——empirical details 超出可预测范围但术语过度包装。两人一致建议 reframe 为 empirical instantiation。持续 11 轮的结构性问题。\"\n- id: v5-R2-W1\n  summary: Abstract 数据堆砌 / 单 seed 数据选择性报告\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 14\n  resolution: Abstract 改用 3-seed aggregate。\n  resolution_round: 14\n- id: v5-R2-W3\n  summary: paragraph{} 过度碎片化\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 14\n  resolution: 段落结构大幅改善。\n  resolution_round: 14\n- id: v5-R2-W4\n  summary: Experiments §4.3 按 β 值呈现顺序非升序\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 10\n  resolution: §4.3 已按升序呈现。\n  resolution_round: 10\n- id: v5-R12-SFT-PR\n  summary: SFT baseline PR confound (PR=13% vs 93%)\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 15\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 fix: Abstract 加 caveat。\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R1-N1: RL-specificity claim 依赖此对比但证据基础薄弱。\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: hedging 全面改善。但 §4.2 line 42 仍用 'RL-specific' 旧措辞。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: R1 列为 Should-Fix (W3)——SFT 用 gold annotations 训练引入 data quality confound。R2 agree with nuance: SFT 主要功能是控制 RL optimization 作为 hacking 来源，confound 影响被 R1 略高估。\"\n- id: v5-R2-MR\n  summary: 缺少重要引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 14\n  resolution: 新增 Llemma、Coste 2024、Moskovitz 2024。\n  resolution_round: 14\n- id: v5-R2-W6\n  summary: Table 1 信息密度过高\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 10\n  resolution: 已拆分。\n  resolution_round: 12\n- id: v5-R1-W5\n  summary: Goodhart taxonomy variant 未指定\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"related_work.tex 指定 'primarily regressional, with extremal elements'。\"\n  resolution_round: 7\n- id: v5-R1-W6\n  summary: ISR reward landscape 几何结构未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: experiments.tex 包含 reward landscape 分析。\n  resolution_round: 7\n- id: v6-R2-N1\n  summary: ISR 核心指标命名不一致\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: 全文统一使用 Intensional Structural Reward。\n  resolution_round: 7\n- id: v6-R2-W5\n  summary: \"ISR 名称含 'Reward' 具有误导性\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: 已统一命名。\n  resolution_round: 7\n- id: v6-R1-W2\n  summary: Dose-response claim 统计上不足\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 14\n  resolution: \"§4.2 line 110 标注 'preliminary'。\"\n  resolution_round: 14\n- id: v6-R2-W2\n  summary: §4.3 的 β 值呈现顺序非升序\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: 已按升序呈现。\n  resolution_round: 10\n- id: v6-R2-W6-LOO\n  summary: LOO 缩写未在首次使用时正式定义\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: introduction.tex 现有完整定义。\n  resolution_round: 7\n- id: v6-R2-W8\n  summary: Hacking taxonomy 分类标准不够 principled\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 15\n  mentions:\n  - round: 11\n    reviewers: [1]\n    note: 仅 H1/H7 有 precision 验证。\n  - round: 12\n    reviewers: [1, 2]\n    note: \"Abstract 改为 'three robust modes + additional isolated observations'。\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"CE/TS/PG/CI 重命名改善可读性。分类标准仍为规则+功能分析混合。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: 两位 reviewer 均列为 Should-Fix (R1-W4, R2-W3)。50 样本验证不足，无 IAA，text-match classifier 有已知 false-negative（Prolog 100% → functional analysis）。阈值敏感性未分析。持续 10 轮。\"\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation p=0.26 为 primary。\n  resolution_round: 9\n- id: v7-R2-MR1\n  summary: 缺少 Goodhart's Law 经典引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: references.bib 包含 Goodhart 1975。\n  resolution_round: 8\n- id: v7-R2-W7\n  summary: \"experiments.tex 'Notably' AI 写作标记\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: 已移除。\n  resolution_round: 9\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 15\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1 Excitement 3/5, R2 2.5/5。两人均同意 Findings。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Gated ISR 增量改善。核心 novelty concern 仍为结构性限制。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: R2 将此列为 critical Must-Fix (N2)——'anti-cheating test 被用于评分后被 game ≠ meta-level cheating'。R1 agree with nuance。结构性问题持续 8 轮，无法通过修改解决。\"\n- id: v8-R1-N3\n  summary: 术语交替使用导致语义滑移\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14\n  resolution: H1→CE, H7→TS, H8→PG, H9→CI 全文重命名完整一致。\n  resolution_round: 14\n- id: v8-R12-N2\n  summary: 实验范围与标题/claim scope 不匹配\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14\n  resolution: \"C3 加 'in principle...preliminary'。Hedging 充分。\"\n  resolution_round: 14\n- id: v8-R1-W4\n  summary: 多重比较未校正\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 15\n  resolution: \"Appendix 标注 CMH 'p-values are consequently inflated'。\"\n  resolution_round: 14\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: R1 再次列为 Should-Fix (W2)——6 conditions × 多指标 Fisher tests 无 Bonferroni/FDR。R2 AGREE。CMH 标注不等于全面的 multiple testing correction。\"\n- id: v8-R1-MR\n  summary: 缺少 reward shaping 和 inference-time hacking 引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: Uesato 2022, Paulus 2018, Langosco 2022 等已补充。\n  resolution_round: 10\n- id: v9-R1-N3\n  summary: Premise-count confound 影响范围分歧\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: method.tex 增加 confound 两场景区分句。\n  resolution_round: 9\n- id: v9-R12-W1\n  summary: §4.4 标题措辞过强\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"§4.4 标题改为 'Cross-Logic Extension'。\"\n  resolution_round: 9\n- id: v9-R1-W5\n  summary: 训练时 sampling vs 评估时 greedy 不一致\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: §4.1 已增加讨论。\n  resolution_round: 9\n- id: v9-R12-Q-ISR-FILTER\n  summary: ISR 作为 filter 未测试\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: conclusion.tex 增加 future work。\n  resolution_round: 9\n- id: v9-R12-Q-NORMALIZED-ISR\n  summary: 未测试 premise-count-normalized ISR\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: conclusion.tex 增加 future work。\n  resolution_round: 9\n- id: v4-RV-STALE-APPENDIX\n  summary: Appendix Table 仍用旧数据\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  resolution: Appendix Table 5 现含完整 per-seed data。\n  resolution_round: 7\n- id: v10-R12-N1\n  summary: §4.5 与 Limitations 关于 1.7B seed 数量矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: D129 完整 3-seed 数据重写 §4.5。\n  resolution_round: 11\n- id: v10-R2-Q6\n  summary: ISR=0.75 推导与实测不一致\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: 改为 ISR≥0.5。\n  resolution_round: 11\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers: [2]\n    note: \"建议改为 'Verified but Vacuous'。\"\n  - round: 14\n    reviewers: []\n    note: \"R14: 未再提及。\"\n  - round: 15\n    reviewers: []\n    note: \"R15: 未提及。可能不再是活跃问题。\"\n- id: v10-R2-W8\n  summary: Discussion/Conclusion 过于简短\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 14\n  resolution: Discussion 扩展至 14 行。含 gated ISR + mitigation 方向。\n  resolution_round: 14\n- id: v10-R2-W5\n  summary: C2 和 C4 边界不清晰\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: Contributions 合并为 3 条。\n  resolution_round: 10\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v11-R1-W2\n  summary: Taxonomy 仅 H1/H7 有 precision 验证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Abstract 'PG, observed at lower prevalence'。Claim 适当下调。\"\n  resolution_round: 14\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果未充分解释\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15: 未直接提及。R2 M4 建议 O(1) variant 值得更多主文讨论。\"\n- id: v11-R2-MR\n  summary: 缺少 2025-2026 最新引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: 新增 Llemma、Coste 2024、Moskovitz 2024。\n  resolution_round: 14\n- id: v11-R12-PDF\n  summary: PDF 与 .tex 不一致\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: PDF 从 paper/ 重编译。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v12-R2-W4\n  summary: Table 1 ISR β=0.1 ISR* 列缺失\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 1 补全。\n  resolution_round: 12\n- id: v12-R2-W2\n  summary: 与 Kim et al. (2026) 区分需更锐利\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"Related Work 新增完整 'Faithfulness in formalization' 段落。\"\n  resolution_round: 14\n- id: v12-R1-W2\n  summary: Component-count confound deconfounding analysis 仅在 Appendix\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: R1-N4 要求 premise-count confound 提升到 §4.3 显著位置。R2 完全同意。此问题从 info 升级为 critical。\"\n- id: v13-R2-N2\n  summary: 与 Kim et al. (2026) 差异化不充分\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Related Work 新增完整对比段落。\"\n  resolution_round: 14\n- id: v13-R1-W1\n  summary: \"ISR 与 NLI accuracy 无关 但 'structural quality diagnostic' 定位可能误导\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Method §3.2 line 46: 'ISR is a component-necessity diagnostic, not a reasoning-quality metric'。\"\n  resolution_round: 14\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高（~17 个缩写）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"~18 缩写，未添加 notation summary。H1→CE 等重命名改善可读性。R2 降为 minor。\"\n  - round: 15\n    reviewers: []\n    note: \"R15: 未提及。可能因 CE/TS/PG/CI 重命名已改善。\"\n- id: v13-R2-W5\n  summary: Table 2 混合 single-seed 和 pooled 数据\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Table 2 caption 标注聚合方式。\"\n  resolution_round: 14\n- id: v13-R2-MITIGATION\n  summary: Discussion 缺少 mitigation 策略讨论\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: Discussion 含 gated ISR + reward ensembling + constrained optimization + TRACE。\n  resolution_round: 14\n- id: v13-R1-Q4\n  summary: Prolog cross-logic 实验缺少 random control\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"§4.3 line 118: 'No matched random control was run for Prolog' 显式声明。\"\n  resolution_round: 14\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例 (96.7% non-hacking)\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Discussion 只提 '2/3 seeds migrate to PG'，忽略 s54。有选择性呈现嫌疑。\"\n- id: v14-R1-LIMITATIONS\n  summary: Limitations section 压缩至 6-7 行\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1]\n    note: 8 页限制下可理解，但 Limitations 不再是亮点。\n\n# === New issues from Round 15 (fresh review) ===\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——每个 seed 走向质性不同的 hacking 路径，aggregate 统计无解释力\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"两位 fresh reviewer 独立识别为 critical Must-Fix。R1: 'ProofFOL permutation test p=0.10 明确欠效力'，'汇总统计量几乎无解释力'。R2: '同一条件下 ISR 可差 40 倍'。R2 交叉时建议 'case study 定位比增加 seeds 更现实'。与历史 v3-R12-NI-1、v2-R1-W1 同源但独立发现。\"\n  action_items:\n  - round: 15\n    action: 增至 ≥5 seeds 或重新定位为 case study，降低跨条件定量声明强度\n    assigned_to: research_director\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 的直接实例而非新理论概念\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R2 核心论点: 经典 Goodhart 定义已覆盖此现象。R1 agree with nuance: empirical details 超出 a priori 预测但术语过度包装。两人一致建议 reframe 为 empirical instantiation + 显式对照 Manheim & Garrabrant 四类变种。与历史 v5-R2-N3、v8-R12-N1 同源。\"\n  action_items:\n  - round: 15\n    action: \"将 'meta-level Goodhart' reframe 为 empirical instantiation；显式对照四类变种\"\n    assigned_to: research_director\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: v15-R1-N3\n  summary: ISR syntactic-only 性质与 structural quality framing gap + 缺少人工评估\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1 列为 Must-Fix (N2): 'structural integrity' 措辞暗示比 'component necessity' 更强保证。R2 从 Should-Fix (W5) 升级为 Must-Fix after 交叉。两人一致要求 ~50 样本人工 faithfulness 标注 + ISR correlation。与历史 R1-W2、v13-R1-W1 同源但 fresh review 再次列为 critical。\"\n  action_items:\n  - round: 15\n    action: 人工标注 ~50 formalizations 的 semantic faithfulness 并报告与 ISR 的 correlation\n    assigned_to: research_director\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: v15-R1-N4\n  summary: Premise-count confound 控制后 ISR-as-reward 优势消失 (3.2×→1.06×)，length penalty 可能足够\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1 列为 Must-Fix (N3): '简单 length penalty 可能达到类似效果'。R2 交叉后完全同意: '确实严重削弱了 ISR-as-reward 的价值叙事'。两人一致要求提升此发现位置并正面回应 length penalty 问题。与历史 v2-R1-W3 (resolved)、v12-R1-W2 (open) 同源。此前 ISR 已定位为 diagnostic-only，但正文位置仍不够突出。\"\n  action_items:\n  - round: 15\n    action: 将 premise-count confound 发现提升至 §4.3 显著位置；直接回应 length penalty 替代方案\n    assigned_to: research_director\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: v15-R2-W1\n  summary: \"缺少 2025-2026 关键相关工作: LLMs Gaming Verifiers, Countdown-Code, Uesato, Cobbe\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R2: 'LLMs Gaming Verifiers' (arXiv:2604.15149) 和 'Countdown-Code' (arXiv:2603.07084) 与本文主题高度重叠，必须讨论。R1: Uesato et al. (2022) 和 Cobbe et al. (2021) 是 process reward 基础文献。R2 对 self-correction 综述 [REBUT]。\"\n  action_items:\n  - round: 15\n    action: \"讨论 LLMs Gaming Verifiers + Countdown-Code（必须），Uesato/Cobbe（推荐）\"\n    assigned_to: research_director\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: v15-R1-W2\n  summary: Multiple testing correction 缺失 (6 conditions × 多指标 Fisher tests)\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1 提出，R2 AGREE。与历史 v8-R1-W4 (resolved) 同源但 fresh reviewers 认为 Appendix CMH 标注不等于全面 correction。\"\n  action_items:\n  - round: 15\n    action: 报告 Bonferroni 或 FDR 校正后的 p-values\n    assigned_to: research_director\n    status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1435 · 2026-05-20T04:37:37.240682+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 30803}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Assistant

_source line 1436 · 2026-05-20T04:39:20.945204+00:00_

审稿流程已全部完成。

- 审稿报告（Overall 3.0 — Findings）已通过 `submit_review_report_to_research_director` 投递给 Research Director
- Issue Tracker (`review_issues.yaml`) 已同步更新，新增 6 条 Round 15 条目并关联历史 issue
- 两位 Reviewer 的交叉回应均已完成，关键问题达成共识，无需进入第二轮

4 项 Must-Fix：
1. 3 seeds 统计效力不足
2. "Meta-level Goodhart" 概念新颖性被高估
3. ISR 仅衡量句法必要性，缺人工评估
4. Premise-count confound 消除 ISR-as-reward 优势

本轮审稿已结束，后续由 Research Director 处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 122

## Round 122

2 recorded events


### User

_source line 1437 · 2026-05-20T04:39:23.695312+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。逐条回应了 R1 的全部 Weaknesses (N1-N3, W1-W5)、Missing References (3条)、Questions (Q1-Q5)，并标注了我自己审稿中 R1 未覆盖的问题的坚持/合并状态。

关键共识点：seed variance (N1)、ISR syntactic-only gap (N2)、premise-count confound (N3) 三项 critical 问题两位 reviewer 达成一致。我额外坚持的独立问题：meta-level Goodhart 概念新颖性被高估 (我的 N1) 和 diagnostic/reward 二分框架掩盖已知区分 (我的 W4)。维持 Overall 3.5 不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1438 · 2026-05-20T04:39:48.179145+00:00_

R2 交叉回应确认收到。审稿报告已在上一轮合成并投递至 Research Director，issue tracker 也已同步更新。本轮圆桌审稿已完结。

**最终结论回顾**：

| 项目 | 结果 |
|------|------|
| R1 评分 | 3.0 (Findings) |
| R2 评分 | 3.5 (Borderline Conference) |
| 综合评分 | **3.0 (Findings)** |
| 共识 Must-Fix | 4 项（seed 统计力不足、meta-Goodhart 新颖性高估、ISR 纯句法无人工评估、premise-count 混淆因子消除 ISR-as-reward 优势） |
| 交叉回应 | R1 ✅、R2 ✅，关键问题全部达成共识 |
| 外部审稿 | 未配置 |
| 视觉审查 | 已派发（结果独立返回 Group C） |

无待办事项。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 123

## Round 123

90 recorded events


### User

_source line 1439 · 2026-05-20T05:20:54.062530+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1440 · 2026-05-20T05:21:01.462399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1441 · 2026-05-20T05:21:01.514137+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1442 · 2026-05-20T05:21:07.503472+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1443 · 2026-05-20T05:21:07.504091+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1444 · 2026-05-20T05:21:11.695770+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1445 · 2026-05-20T05:21:11.696164+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1446 · 2026-05-20T05:21:14.662771+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1447 · 2026-05-20T05:21:14.713443+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1448 · 2026-05-20T05:21:17.280859+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1449 · 2026-05-20T05:21:17.331600+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1450 · 2026-05-20T05:21:23.589287+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1451 · 2026-05-20T05:21:23.640035+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1452 · 2026-05-20T05:21:28.513387+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 1453 · 2026-05-20T05:21:29.717291+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (191 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- d146-pf-pipeline（准备中）\n- d144-llama-isr-s43: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of ISR s42 for statistical power.（准备中）\n- d144-llama-isr-s44: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=44. Replication of ISR s42 for statistical power.（准备中）\n- d144-llama-isr-s42: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=42. Tests whether ISR triggers same Goodhart collapse pattern as Qwen3-4B.（准备中）\n- d144-llama-exec-s44: D144 cross-model: exec-only GRPO on LLaMA-3.2-3B/FOLIO seed=44. Replication of s42 for statistical power.（准备中）\n- d144-llama-exec-s43: D144 cross-model: exec-only GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of s42 for statistical power.（准备中）\n- d143-pw-random-s42（准备中）\n- d143-pw-sft-s42（准备中）\n- d143-pw-extended-s42（准备中）\n- d143-pw-sta-s44（准备中）\n- …另有 14 项\n\n## 近期结论\n- **sweep-random-b01-s46** (success): W4: Random β=0.1 s46 extends random control to 5-seed\n- **sweep-random-b01-s45** (success): W4: Random β=0.1 s45 extends random control to 5-seed for matched comparison with ISR β=0.1\n- **d146-pf-isr-s43**
…[truncated 1881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1203
}
```

</details>

---


### Tool call

_source line 1454 · 2026-05-20T05:21:30.269972+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf 2>&1",
  "description": "Check paper files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf 2>&1",
    "description": "Check paper files exist"
  }
}
```

</details>

---


### Tool result

_source line 1455 · 2026-05-20T05:21:30.825336+00:00_

-rw-r--r-- 1 ubuntu ubuntu 602735 May 20 05:17 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf
-rw-r--r-- 1 ubuntu ubuntu    886 May 20 04:51 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 555
}
```

</details>

---


### Tool call

_source line 1456 · 2026-05-20T05:21:31.783659+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines page limit author instructions",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines page limit author instructions",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 1457 · 2026-05-20T05:21:32.691095+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>&1",
  "description": "Check if review issues tracker exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>&1",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 1458 · 2026-05-20T05:21:32.792120+00:00_

-rw-r--r-- 1 ubuntu ubuntu 37399 May 20 05:20 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 1459 · 2026-05-20T05:21:39.297001+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines page limit author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"}]

Based on the search results, I found information about EMNLP 2026 and ARR submission guidelines. Here are the key details:

## EMNLP 2026 Call for Papers Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on e
…[truncated 1520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 7513
}
```

</details>

---


### Tool call

_source line 1460 · 2026-05-20T05:21:45.438442+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference papers submission deadline ARR May cycle commitment deadline page limit template anonymity",
  "allowed_domains": "['2026.emnlp.org', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference papers submission deadline ARR May cycle commitment deadline page limit template anonymity",
    "allowed_domains": "['2026.emnlp.org', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 1461 · 2026-05-20T05:21:46.392994+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May submission deadline author guidelines formatting requirements",
  "allowed_domains": "['aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May submission deadline author guidelines formatting requirements",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 1462 · 2026-05-20T05:21:46.570485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1463 · 2026-05-20T05:21:46.595093+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{limitations}
38	
39	\appendix
40	\input{appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 24
}
```

</details>

---


### Tool result

_source line 1464 · 2026-05-20T05:21:53.391926+00:00_

Web search results for query: "EMNLP 2026 main conference papers submission deadline ARR May cycle commitment deadline page limit template anonymity"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Changes to reviewer volunteering requirement and incentives in May 2025 cycle (EMNLP 2025)","url":"http://aclrollingreview.org/incentives2025"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"Response to ACL 2023 Questions","url":"http://aclrollingreview.org/ACL-2023-session/"},{"title":"ARR Changelog","url":"http://aclrollingreview.org/changelog"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"}]

Based on my search, here are the key details for EMNLP 2026 main conference papers:

## Anonymity and Preprints
There is no anonymity period requirement, following the ACL and ARR policies. Beginning with the February 15, 2024 ARR deadlines, there is no anonymity period or limitation on posting or discussing non-anonymous preprints while the work is under peer review.

## ARR May 2026 Cycle Policy for EMNLP
Authors must explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026 - ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

## Submission Requirements
All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

Papers must not include authors' names and affiliations, and self-references that reveal the author
…[truncated 489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 7953
}
```

</details>

---


### Tool result

_source line 1465 · 2026-05-20T05:21:54.346224+00:00_

Web search results for query: "ACL Rolling Review 2026 May submission deadline author guidelines formatting requirements"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's information about ACL Rolling Review 2026 May submission:

## Submission Deadline

The n
…[truncated 1605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 7953
}
```

</details>

---


### Tool call

_source line 1466 · 2026-05-20T05:22:00.936662+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1467 · 2026-05-20T05:22:00.987348+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1468 · 2026-05-20T05:22:04.355663+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/dates",
  "prompt": "Extract the ARR 2026 May cycle submission deadline and commitment deadline for EMNLP 2026. List all relevant dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/dates",
    "prompt": "Extract the ARR 2026 May cycle submission deadline and commitment deadline for EMNLP 2026. List all relevant dates."
  }
}
```

</details>

---


### Tool call

_source line 1469 · 2026-05-20T05:22:05.762425+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission requirements: page limits (long/short), template, anonymity rules, appendix rules, formatting details, commitment deadline, and any other author guidelines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract all submission requirements: page limits (long/short), template, anonymity rules, appendix rules, formatting details, commitment deadline, and any other author guidelines."
  }
}
```

</details>

---


### Tool call

_source line 1470 · 2026-05-20T05:22:06.116217+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1471 · 2026-05-20T05:22:06.570552+00:00_

1	\begin{abstract}
2	Neurosymbolic formalizers trained with Group Relative Policy Optimization (GRPO) achieve high prove rates---93\% on FOLIO---yet 87\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution reward.
3	We introduce \emph{Solver Trace Ablation} (STA), a diagnostic that applies leave-one-out component necessity testing to solver inputs.
4	The fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates full necessity; ISR$=$0 complete redundancy.
5	ISR is uncorrelated with downstream NLI accuracy ($\rho{=}{-}0.049$), confirming it measures component necessity---not semantic faithfulness.
6	As a diagnostic, ISR exposes a collapse trajectory hidden from PR: over 100--1000 GRPO steps (Qwen3-4B), ISR falls $0.642{\to}0.003$ while PR rises $32\%{\to}96\%$; a supervised fine-tuning (SFT) baseline reaches 92.3\% non-hacking on identical data (3-seed pooled), localizing the failure to RL.
7	As a reward, $r = r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta{=}0.1$ induces Goodhart effects on the structural metric: 70.6\% conclusion duplication (H7) versus 13.7\% under matched random (Fisher $p{=}1.3{\times}10^{-39}$; random H7 is seed-dependent, driven by one of three seeds); ISR amplifies H7 frequency ${\sim}5{\times}$ rather than exclusively causing it; the sole apparent ISR advantage reduces to $1.06\times$ after controlling for a premise-count confound; $\beta{=}0.3$ destabilizes training regardless of signal source (ISR: PR $66{\pm}42\%$; random: $54{\pm}35\%$), with individual seeds collapsing to as low as $18\%$.
8	Cross-logic transfer to Prolog yields universal Goodhart (3/3 seeds, 0\% non-hacking); cross-dataset replication on ProofFOL (${\sim}$500 examples) confirms structural degeneration generalizes ($\text{ISR}^*{<}0.12$, ${\leq}1.4\%$ genuine in converged seeds), while ISR as training signal produces dataset-depend
…[truncated 526 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 1472 · 2026-05-20T05:22:06.571066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1473 · 2026-05-20T05:22:07.024205+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.
7	
8	\paragraph{The execution-only blind spot.}
9	Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
11	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
12	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for component necessity in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify component necessity (Figure~\ref{fig:sta-overview}).
16	For each proved formalization, STA removes each component individually and re-runs t
…[truncated 3328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1474 · 2026-05-20T05:22:07.024724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1475 · 2026-05-20T05:22:07.984661+00:00_

# ARR May 2026 Cycle - EMNLP 2026 Dates

Based on the content provided, here are the relevant dates:

**ARR May 2026 Cycle:**
- Submission deadline: "May 25, 2026"
- Reviewer registration deadline: "May 27"
- Reviews due: "June 29"
- Author response period: "July 7-July 13"
- Meta-reviews release: "July 30"
- Cycle end: "August 2"

**EMNLP 2026 Commitment:**
- Final ARR submission deadline: "May 25, 2026"
- Commitment deadline: "August 2, 2026"

Authors have until May 25, 2026 to submit papers to ARR for consideration by EMNLP 2026, with the final commitment deadline set for August 2, 2026.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebFetch",
  "elapsed_ms": 3628
}
```

</details>

---


### Tool result

_source line 1476 · 2026-05-20T05:22:07.985442+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: the diagnostic becomes the optimization target, exhibiting Goodhart effects at a meta level.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$ (Figure~\ref{fig:sta-overview}a).
15	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
16	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
17	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
18	
19	\subsection{Solver Trace Ablation (STA)}
20	\label{sec:sta}
21	
22	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}b).
23	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
24	A component is \emph{necessary} if its removal causes proof failure.
25	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
26	LOO ablation itself is stand
…[truncated 5571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 1477 · 2026-05-20T05:22:07.985726+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1478 · 2026-05-20T05:22:08.490426+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 does not change qualitative conclusions (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the eight cataloged patterns, a necessary 
…[truncated 16681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 1479 · 2026-05-20T05:22:08.491035+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1480 · 2026-05-20T05:22:08.993009+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
7	
8	\paragraph{Process rewards and reward shaping.}
9	Early work established verifier-based training for mathematical reasoning~\citep{cobbe2021training}, with process-level feedback showing promise over outcome-only signals~\citep{uesato2022solving}.
10	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}: \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
11	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
12	Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
13	The shared lesson across these approaches is that reward augmentation introduces proxy risk---our contribution is demonstrating that even a deterministic, solver-derived diagnostic becomes the target of gaming when optimized.
14	
15	\paragraph{Reward hacking and Goodhart's Law.}
16	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and 
…[truncated 1509 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1481 · 2026-05-20T05:22:08.993437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1482 · 2026-05-20T05:22:09.495873+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\% collapse under exec-only GRPO that PR hides, while SFT localizes the failure to RL (\S\ref{sec:diagnostic}).
5	Repurposed as a reward, ISR produces dataset-dependent outcomes: on FOLIO, Goodhart effects amplify H7 ${\sim}5{\times}$ ($p{<}10^{-39}$); on ProofFOL, beneficial instability yields 76.8\% vs.\ 17.4\% genuine ($p{=}0.10$).
6	Deconfounding reduces ISR's sole apparent reward advantage to $1.06\times$; a simple length penalty may suffice (\S\ref{sec:goodhart}).
7	ISR's vulnerability is not inherent---it depends on whether shortcuts satisfy the metric's LOO structure---suggesting mitigation via component-count normalization, reward ensembling, or constrained optimization rather than abandoning the metric.
8	Full LOO ablation adds ${<}1\%$ to evaluation time (55\,ms vs.\ 4\,s per sample at mean $n{\approx}6$); the $O(1)$ training variant adds ${<}2\%$ per step (Appendix~\ref{app:o1-ablation}).
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1483 · 2026-05-20T05:22:09.496242+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1484 · 2026-05-20T05:22:09.998933+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); while cross-dataset evidence from ProofFOL (\S\ref{sec:crossdomain}) supports generality, hacking-mode prevalence may vary across benchmarks.
5	STA requires models with sufficient FOL generation capability: LLaMA-3.2-3B fails to produce parseable formalizations under identical training, preventing any structural analysis (Appendix~\ref{app:llama-coldstart}); this capability threshold limits applicability to models above a minimum formalization competence.
6	The ProofFOL genuine-rate advantage ($p{=}0.10$, $N{=}3$ per group) is an observation, not a confirmed effect; ProofFOL itself is silver-standard (GPT-4o translation, ${\sim}70\%$ retention).
7	While structural degeneration generalizes across dataset families, cross-seed variance remains substantial (ProofFOL exec-only $\sigma_{\text{PR}} \approx 25$\,pp), consistent with FOLIO observations and suggesting that individual training trajectories remain seed-sensitive even as the overall phenomenon replicates.
8	ISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
9	Three seeds demonstrate qualitative divergence but limit statistical power.
10	STA requires solvers supporting component-level input manipulation.
11	
12	\paragraph{Data scale.}
13	Our experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\citep{folio}.
14	The training subset is selected via stratified sampling (seed 42) and held constant across all conditions.
15	While our findings are consistent across seeds and logic types, the effect of training data scale on hacking prevalence and mode distribution remains an open question for future work.
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1485 · 2026-05-20T05:22:09.999328+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1486 · 2026-05-20T05:22:10.452211+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other se
…[truncated 38088 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1487 · 2026-05-20T05:22:10.553818+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1488 · 2026-05-20T05:22:10.604669+00:00_

1	issues:
2	# === Resolved issues from rounds 0-14 (condensed) ===
3	- id: R1-W1
4	  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 2
10	  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。
11	  resolution_round: 2
12	- id: RV-EVAL-FALLBACK
13	  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
14	  category: experiment
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)。
20	  resolution_round: 1
21	- id: RV-D060-NARRATIVE
22	  summary: D060 'Goodhart instability' 叙事确认成立
23	  category: experiment
24	  severity: critical
25	  status: resolved
26	  first_raised_round: 1
27	  last_seen_round: 1
28	  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。
29	  resolution_round: 2
30	- id: RV-FIG2-STALE-SCRIPT
31	  summary: figures/paper/gen_fig2.py 旧脚本数据错误
32	  category: format
33	  severity: warning
34	  status: resolved
35	  first_raised_round: 1
36	  last_seen_round: 1
37	  resolution: 已修复。
38	  resolution_round: 1
39	- id: R1-W2
40	  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量
41	  category: framing
42	  severity: critical
43	  status: resolved
44	  first_raised_round: 0
45	  last_seen_round: 15
46	  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
47	  resolution_round: 2
48	  mentions:
49	  - round: 15
50	    reviewers: [1, 2]
51	    note: "R15 fresh review 再次提出 ISR syntactic-only gap（R1-N2/N3, R2-W5）。'structural integrity' 措辞仍暗示比 'component necessity' 更强的保证。尽管已修正术语，framing gap 在 Abstract/Introduction 仍可感知。"
52	- id: R2-W1
53	  summary: Limitations section 格式不合规
54	  category: format
55	  severity: critical
56	  status: resolved
57	  first_raised_round: 0
58	  last_seen_round: 2
59	  resolution: 独立 limitations.tex 已创建。
60	  r
…[truncated 1273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1489 · 2026-05-20T05:22:20.711727+00:00_

# EMNLP 2026 Submission Requirements Summary

## Page Limits
- **Long Papers:** 8 pages (up to 9 pages in final camera-ready version)
- **Short Papers:** 4 pages (up to 5 pages in final camera-ready version)

## Anonymity
The review process maintains "double-blind" standards where "reviewers will not see authors, nor will authors see reviewers." However, "following the ACL and ARR policies, there is no anonymity period requirement."

## Commitment Deadline
- **EMNLP commitment deadline:** August 2, 2026

## Key Author Guidelines
- **Author registration required:** All authors must register by May 27, 2026
- **Reviewing obligation:** "All authors are expected to sign up to review, or serve as an Area Chair or Senior Area Chair"
- **Author list modifications:** During commitment, adding or removing authors is prohibited, though reordering is permitted

## Other Critical Requirements
- Follow all ARR submission specifications regarding formatting, templates, and citations
- Include a "limitations" section
- Provide optional supplementary materials if needed
- Present at the conference in-person or virtually to appear in proceedings
- Papers must be submitted to ARR by May 25, 2026

For detailed formatting specifications and templates, the document directs authors to consult "ARR submission requirements" directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebFetch",
  "elapsed_ms": 14949
}
```

</details>

---


### Tool call

_source line 1490 · 2026-05-20T05:22:31.094353+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1491 · 2026-05-20T05:22:31.095015+00:00_

100	  resolution_round: 2
101	- id: R2-W7
102	  summary: 与 Kim et al. (2026) 差异化不充分
103	  category: writing
104	  severity: warning
105	  status: resolved
106	  first_raised_round: 0
107	  last_seen_round: 2
108	  resolution: related_work.tex 中有区分段落。
109	  resolution_round: 2
110	- id: R1-W6
111	  summary: 训练 500 例/评估 100 例的规模限制讨论不充分
112	  category: experiment
113	  severity: warning
114	  status: resolved
115	  first_raised_round: 0
116	  last_seen_round: 0
117	  resolution: limitations.tex 已讨论。
118	  resolution_round: 2
119	- id: R1-W7
120	  summary: H1/H7 classifier precision/recall 未报告
121	  category: experiment
122	  severity: info
123	  status: resolved
124	  first_raised_round: 0
125	  last_seen_round: 0
126	  resolution: 50 样本人工验证 precision >95%。
127	  resolution_round: 2
128	- id: R1-W8
129	  summary: Random control U(0,1) 与 ISR 的 skewed 分布不匹配
130	  category: experiment
131	  severity: info
132	  status: resolved
133	  first_raised_round: 0
134	  last_seen_round: 0
135	  resolution: method.tex 和 experiments.tex 均说明了 Random 设计目的。
136	  resolution_round: 2
137	- id: R1-W9
138	  summary: 缺代码/数据开源承诺
139	  category: format
140	  severity: info
141	  status: resolved
142	  first_raised_round: 0
143	  last_seen_round: 0
144	  resolution: "abstract.tex:9 脚注 'Code and data: [anonymized]'。"
145	  resolution_round: 2
146	- id: R1-W5
147	  summary: "'Meta-level Goodhart' 新颖性论证不足"
148	  category: framing
149	  severity: warning
150	  status: resolved
151	  first_raised_round: 0
152	  last_seen_round: 3
153	  resolution: framing 降级为 empirical instance。
154	  resolution_round: 3
155	- id: R2-W8
156	  summary: H1/H7 编号不连贯（H2-H6 不存在）
157	  category: writing
158	  severity: info
159	  status: resolved
160	  first_raised_round: 0
161	  last_seen_round: 3
162	  resolution: method.tex 解释了合并原因。
163	  resolution_round: 3
164	- id: v2-R1-N1
165	  summary: Abstract '93%' PR 为 single seed，应改为 mean±std
166	  category: writing
167	  severity: critical
168	  status: resolved
169	  firs
…[truncated 3878 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1492 · 2026-05-20T05:22:31.195816+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1493 · 2026-05-20T05:22:31.246670+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml\", \"content\": \"_next_id: 153\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:34 UTC\\n  summary: MVP 方案：FOL+Prover9 单逻辑 50-step GRPO pilot 验证 STA reward 有效性\\n  rationale: EMNLP ARR DDL 5/25 仅剩 12 天，需要最快速度验证核心假设。选 FOL+Prover9 因为 hacking 模式最清晰（tautological\\n    formulas），STA 的 O(1) 近似最直观（去掉前提后能否证明结论）。50-step pilot 足以观察 ISR 趋势。两个条件并行跑 2 GPU。Pass\\n    标准：ISR gap >20pp + accuracy 降幅 <5pp。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:37 UTC\\n  summary: MVP 方案调整：50步→100步 + 趋势判断 + Phase 0 ISR baseline + kill criteria\\n  rationale: 采纳 Reviewer 三条 warning：(1) 加 pre-training ISR baseline 锚定训练前水平；(2) 50步太短难以观察\\n    reward hacking，改 100步+最后20步 moving average 趋势判断；(3) 补充硬性 kill criteria 防止 DDL\\n    压力下无止境调整。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 20:50 UTC\\n  summary: Phase 1 r4 fast_isr_fol 训练信号无效，改用 full STA + K=8 重跑\\n  rationale: fast_isr_fol 是二值 O(1) 近似（ISR=0 tautology / ISR=1 non-tautology），Qwen3-4B\\n    生成的 proved formalization 几乎全部 ISR=1，与 execution-only 零差异。full STA 提供连续 ISR（0.125-0.889\\n    in Phase 0），能给出真实梯度信号。K=4 导致 frac_reward_zero_std=0.5-1.0（GRPO 无 advantage），K=8\\n    增加 within-group variance。两个改动分别解决 STA 信号粒度和 GRPO 梯度信号两个独立问题。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-only-r4\\n    role: evidence\\n    result: prove_rate 12%→15%, ISR ~0.15, minimal learning\\n  - exp_id: sta-phase1-exec-sta-r4\\n    role: evidence\\n    result: 与 exec-only 几乎完全相同, fast_isr 提供零额外信号\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 21:59 UTC\\n  summary: Reviewer 指出 exec-sta-r5 prove_rate 低于 baseline（退化），STA 50/50 权重过于惩罚性。立即补跑低权重\\n    + bonus 模式实验\\n  rationale: exec-sta-r5 prove_rate=0.10 < baseline=0.12 < exec-only=0.15。连续 ISR 给\\n    proved-but-low-ISR 样本 reward≈0.3（几乎等于未 prove），模型学到 prove 不值得。Kill criteri
…[truncated 1452 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1494 · 2026-05-20T05:22:31.247105+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1495 · 2026-05-20T05:22:31.298173+00:00_

1	% ============================================================
2	% LLaMA
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title = {{The Llama 3 Herd of Models}},
8	  journal = {arXiv preprint arXiv:2407.21783},
9	  year = {2024},
10	  eprint = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	% ============================================================
15	% Category 1: Neurosymbolic reasoning + RL/GRPO
16	% ============================================================
17	
18	@article{deepseekmath,
19	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
20	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
21	  journal      = {arXiv preprint arXiv:2402.03300},
22	  year         = {2024},
23	  eprint       = {2402.03300},
24	  archivePrefix = {arXiv},
25	  primaryClass = {cs.AI},
26	}
27	
28	@article{logic-rl,
29	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
30	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
31	  journal      = {arXiv preprint arXiv:2502.14768},
32	  year         = {2025},
33	  eprint       = {2502.14768},
34	  archivePrefix = {arXiv},
35	  primaryClass = {cs.AI},
36	}
37	
38	@article{mellgren-prolog-grpo,
39	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
40	  title        = {{Training Language Models to Use Prolog as a Tool}},
41	  journal      = {arXiv preprint arXiv:2512.07407},
42	  year         = {2025},
43	  eprint       = {2512.07407},
44	  archivePrefix = {arXiv},
45	  primaryClass = {cs.AI},
46	}
47	
48	@inproceedings{satlm,
49	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
50	  title        
…[truncated 13436 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1496 · 2026-05-20T05:22:38.061854+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
  "offset": "299",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
    "offset": "299",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1497 · 2026-05-20T05:22:38.113351+00:00_

299	  first_raised_round: 2
300	  last_seen_round: 3
301	  resolution: 100-step RL 对照充分利用。
302	  resolution_round: 3
303	- id: R2-MISSING-REF
304	  summary: 引用覆盖不足
305	  category: writing
306	  severity: warning
307	  status: resolved
308	  first_raised_round: 0
309	  last_seen_round: 3
310	  resolution: 31 条引用覆盖核心领域。
311	  resolution_round: 3
312	- id: v3-R1-NI-2
313	  summary: β=0.2 未在 Table 1 中独立报告
314	  category: writing
315	  severity: info
316	  status: resolved
317	  first_raised_round: 3
318	  last_seen_round: 4
319	  resolution: Table 1 现已包含 β=0.2 行。
320	  resolution_round: 4
321	- id: v3-R1-NI-3
322	  summary: §4.2 cross-seed 描述暗示最终状态
323	  category: writing
324	  severity: info
325	  status: resolved
326	  first_raised_round: 3
327	  last_seen_round: 4
328	  resolution: "现标注 '(at 500 steps)'。"
329	  resolution_round: 4
330	- id: v3-R12-NI-4
331	  summary: 全文 em-dash AI 写作痕迹
332	  category: writing
333	  severity: info
334	  status: resolved
335	  first_raised_round: 3
336	  last_seen_round: 5
337	  resolution: em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。
338	  resolution_round: 5
339	- id: v3-R2-NI-5
340	  summary: "Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾"
341	  category: writing
342	  severity: info
343	  status: resolved
344	  first_raised_round: 3
345	  last_seen_round: 4
346	  resolution: "Abstract 现用 'effectively zero...at convergence'。"
347	  resolution_round: 4
348	
349	# === In-progress issues (updated with round 15) ===
350	- id: v3-R12-NI-1
351	  summary: Cross-scale 实验 seed 数量不足
352	  category: experiment
353	  severity: warning
354	  status: in_progress
355	  first_raised_round: 3
356	  last_seen_round: 15
357	  mentions:
358	  - round: 3
359	    reviewers: [1, 2]
360	    note: 两位 reviewer 一致。
361	  - round: 10
362	    reviewers: [1, 2]
363	    note: 现已用 D129 完整 3-seed 数据重写 §4.5。
364	  - round: 11
365	    reviewers: [1]
366	    note: "R1-W4: 3 seeds 仍不足以作为独立 contribution 支撑。"
367	  - round: 12
368	    reviewers: [1, 2]

…[truncated 7626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1498 · 2026-05-20T05:22:42.058001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
  "offset": "598",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
    "offset": "598",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1499 · 2026-05-20T05:22:42.109238+00:00_

598	  status: resolved
599	  first_raised_round: 6
600	  last_seen_round: 10
601	  resolution: 已按升序呈现。
602	  resolution_round: 10
603	- id: v6-R2-W6-LOO
604	  summary: LOO 缩写未在首次使用时正式定义
605	  category: writing
606	  severity: info
607	  status: resolved
608	  first_raised_round: 6
609	  last_seen_round: 7
610	  resolution: introduction.tex 现有完整定义。
611	  resolution_round: 7
612	- id: v6-R2-W8
613	  summary: Hacking taxonomy 分类标准不够 principled
614	  category: method
615	  severity: warning
616	  status: in_progress
617	  first_raised_round: 6
618	  last_seen_round: 15
619	  mentions:
620	  - round: 11
621	    reviewers: [1]
622	    note: 仅 H1/H7 有 precision 验证。
623	  - round: 12
624	    reviewers: [1, 2]
625	    note: "Abstract 改为 'three robust modes + additional isolated observations'。"
626	  - round: 14
627	    reviewers: [1, 2]
628	    note: "CE/TS/PG/CI 重命名改善可读性。分类标准仍为规则+功能分析混合。"
629	  - round: 15
630	    reviewers: [1, 2]
631	    note: "R15 fresh review: 两位 reviewer 均列为 Should-Fix (R1-W4, R2-W3)。50 样本验证不足，无 IAA，text-match classifier 有已知 false-negative（Prolog 100% → functional analysis）。阈值敏感性未分析。持续 10 轮。"
632	- id: v7-R1-N2
633	  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate
634	  category: experiment
635	  severity: critical
636	  status: resolved
637	  first_raised_round: 7
638	  last_seen_round: 9
639	  resolution: CMH 移至 Appendix，正文以 seed-level permutation p=0.26 为 primary。
640	  resolution_round: 9
641	- id: v7-R2-MR1
642	  summary: 缺少 Goodhart's Law 经典引用
643	  category: writing
644	  severity: info
645	  status: resolved
646	  first_raised_round: 7
647	  last_seen_round: 8
648	  resolution: references.bib 包含 Goodhart 1975。
649	  resolution_round: 8
650	- id: v7-R2-W7
651	  summary: "experiments.tex 'Notably' AI 写作标记"
652	  category: writing
653	  severity: info
654	  status: resolved
655	  first_raised_round: 7
656	  last_seen_round: 9
657	  resolution: 已移除。
658	  resolution_round: 9
659	- id: v8-R12-N1
660	  summary: Goodhart 发现的可预测性限制概念新颖性
661	  categor
…[truncated 7112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1500 · 2026-05-20T05:22:46.406902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
  "offset": "897",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
    "offset": "897",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1501 · 2026-05-20T05:22:46.457911+00:00_

897	- id: v12-R1-W2
898	  summary: Component-count confound deconfounding analysis 仅在 Appendix
899	  category: writing
900	  severity: info
901	  status: resolved
902	  first_raised_round: 12
903	  last_seen_round: 15
904	  mentions:
905	  - round: 15
906	    reviewers: [1, 2]
907	    note: "R15 fresh review: R1-N4 要求 premise-count confound 提升到 §4.3 显著位置。R2 完全同意。此问题从 info 升级为 critical。"
908	  resolution: "§4.3 开头段以 confound 为 headline finding，直接在正文给出 3.2×→1.06× 和 length penalty 回应"
909	  resolution_round: 15
910	- id: v13-R2-N2
911	  summary: 与 Kim et al. (2026) 差异化不充分
912	  category: writing
913	  severity: critical
914	  status: resolved
915	  first_raised_round: 13
916	  last_seen_round: 14
917	  resolution: "Related Work 新增完整对比段落。"
918	  resolution_round: 14
919	- id: v13-R1-W1
920	  summary: "ISR 与 NLI accuracy 无关 但 'structural quality diagnostic' 定位可能误导"
921	  category: framing
922	  severity: warning
923	  status: resolved
924	  first_raised_round: 13
925	  last_seen_round: 14
926	  resolution: "Method §3.2 line 46: 'ISR is a component-necessity diagnostic, not a reasoning-quality metric'。"
927	  resolution_round: 14
928	- id: v13-R2-W4
929	  summary: 缩写和术语密度过高（~17 个缩写）
930	  category: writing
931	  severity: info
932	  status: open
933	  first_raised_round: 13
934	  last_seen_round: 15
935	  mentions:
936	  - round: 14
937	    reviewers: [1, 2]
938	    note: "~18 缩写，未添加 notation summary。H1→CE 等重命名改善可读性。R2 降为 minor。"
939	  - round: 15
940	    reviewers: []
941	    note: "R15: 未提及。可能因 CE/TS/PG/CI 重命名已改善。"
942	- id: v13-R2-W5
943	  summary: Table 2 混合 single-seed 和 pooled 数据
944	  category: writing
945	  severity: warning
946	  status: resolved
947	  first_raised_round: 13
948	  last_seen_round: 14
949	  resolution: "Table 2 caption 标注聚合方式。"
950	  resolution_round: 14
951	- id: v13-R2-MITIGATION
952	  summary: Discussion 缺少 mitigation 策略讨论
953	  category: writing
954	  severity: warning
955	  status: resolved
956	  first_raised_round: 13
957	  last_seen_round: 
…[truncated 6853 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1502 · 2026-05-20T05:22:57.278291+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
  "offset": "1100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
    "offset": "1100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1503 · 2026-05-20T05:22:57.382138+00:00_

1100	  resolution_round: 15

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 1504 · 2026-05-20T05:23:20.878089+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1505 · 2026-05-20T05:23:21.740336+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 862
}
```

</details>

---


### Tool call

_source line 1506 · 2026-05-20T05:23:21.741247+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1507 · 2026-05-20T05:23:22.849371+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 1108
}
```

</details>

---


### Tool call

_source line 1508 · 2026-05-20T05:23:22.950428+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf 2>/dev/null || echo \"pdfinfo not available\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1509 · 2026-05-20T05:23:23.151966+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Wed May 20 05:22:14 2026 UTC
ModDate:         Wed May 20 05:22:14 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           20
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       603541 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1510 · 2026-05-20T05:23:26.574556+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/ 2>/dev/null",
  "description": "List agent config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/ 2>/dev/null",
    "description": "List agent config files"
  }
}
```

</details>

---


### Tool result

_source line 1511 · 2026-05-20T05:23:26.676139+00:00_

Exit code 2

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1512 · 2026-05-20T05:23:29.798274+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1513 · 2026-05-20T05:23:29.900042+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1514 · 2026-05-20T05:23:33.281204+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/ -maxdepth 2 -name \"config.yaml\" -o -maxdepth 2 -name \"*.yml\" 2>/dev/null | grep -i config | head -10",
  "description": "Search for config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/ -maxdepth 2 -name \"config.yaml\" -o -maxdepth 2 -name \"*.yml\" 2>/dev/null | grep -i config | head -10",
    "description": "Search for config files"
  }
}
```

</details>

---


### Tool result

_source line 1515 · 2026-05-20T05:23:33.384320+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 1516 · 2026-05-20T05:23:36.301919+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/",
  "description": "List project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/",
    "description": "List project directory"
  }
}
```

</details>

---


### Tool result

_source line 1517 · 2026-05-20T05:23:36.352645+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
_last_visual_review.json
artifacts
checkpoints
constraints.lock
constraints.yaml
decisions.lock
decisions.yaml
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.lock
experiment_plan.yaml
figures
literature_map.yaml
logs
memory.md
mistakes.lock
mistakes.yaml
paper
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
paper_review_loop10.md
registry.lock
registry.yaml
report.md
scripts
study_status.lock
task_context
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1518 · 2026-05-20T05:23:38.817724+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 1519 · 2026-05-20T05:23:39.674310+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (191 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- d146-pf-pipeline（准备中）\n- d144-llama-isr-s43: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of ISR s42 for statistical power.（准备中）\n- d144-llama-isr-s44: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=44. Replication of ISR s42 for statistical power.（准备中）\n- d144-llama-isr-s42: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=42. Tests whether ISR triggers same Goodhart collapse pattern as Qwen3-4B.（准备中）\n- d144-llama-exec-s44: D144 cross-model: exec-only GRPO on LLaMA-3.2-3B/FOLIO seed=44. Replication of s42 for statistical power.（准备中）\n- d144-llama-exec-s43: D144 cross-model: exec-only GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of s42 for statistical power.（准备中）\n- d143-pw-random-s42（准备中）\n- d143-pw-sft-s42（准备中）\n- d143-pw-extended-s42（准备中）\n- d143-pw-sta-s44（准备中）\n- …另有 14 项\n\n## 近期结论\n- **sweep-random-b01-s46** (success): W4: Random β=0.1 s46 extends random control to 5-seed\n- **sweep-random-b01-s45** (success): W4: Random β=0.1 s45 extends random control to 5-seed for matched comparison with ISR β=0.1\n- **d146-pf-isr-s43**
…[truncated 1881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 1520 · 2026-05-20T05:24:04.953499+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析**。\n\n## 论文信息\n- 标题: \"Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning\"\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf\n- 目标 venue: EMNLP 2026 (ARR May 2026 cycle)\n\n## Venue 要求\n- Long paper 正文 ≤ 8 页，参考文献不限\n- Limitations section 必须有，不计入页数限制\n- ACL 模板 (review mode), double-blind\n- 投稿截止: 2026-05-25\n\n## 你的审查侧重\n1. **方法严谨性**: STA/ISR 方法设计是否合理？LOO ablation 的假设和局限性是否充分讨论？reward 条件的实验设计是否科学（控制变量、对照组）？\n2. **实验设计**: 训练配置（模型、数据集、seeds、步数）是否足够？评估方法是否严格？Cross-domain 实验设计是否充分支撑泛化性 claims？\n3. **统计分析**: 3 seeds 的统计效力是否足以支撑 claims？p 值报告是否准确？multiple testing correction 是否充分？置信区间和效应量报告是否完整？\n4. **结果可复现性**: 是否提供足够的细节让他人复现？超参数报告是否完整？\n5. **Claims 与证据匹配度**: 每个贡献声明（C1-C4）是否都有充分的实验证据支撑？是否有 overclaiming？\n\n请按以下格式输出审稿意见：\n### Summary (2-3句)\n### Strengths (逐条)\n### Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n### Questions (需要作者澄清的)\n### Missing References\n### Overall Assessment (评分 + 置信度)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析**。\n\n## 论文信息\n- 标题: \"Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning\"\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf\n- 目标 venue: EMNLP 2026 (ARR May 2026 cycle)\n\n## Venue 要求\n- Long paper 正文 ≤ 8 页，参考文献不限\n- Limitations section 必须有，不计入页数限制\n- ACL 模板 (review mode), double-blind\n- 投稿截止: 2026-05-25\n\n## 你的审查侧重\n1. **方法严谨性**: STA/ISR 方法设计是否合理？LOO ablation 的假设和局限性是否充分讨论？reward 条件的实验设计是否科学（控制变量、对照组）？\n2. **实验设计**: 训练配置（模型、数据集、seeds、步数）是否足够？评估方法是否严格？Cross-domain 实验设计是否充分支撑泛化性 claims？\n3. **统计分析**: 3 seeds 的统计效力是否足以支撑 claims？p 值报告是否准确？multiple testing correction 是否充分？置信区间和效应量报告是否完整？\n4. **结果可复现性**: 是否提供足够的细节让他人复现？超参数报告是否完整？\n5. **Claims 与证据匹配度**: 每个贡献声明（C1-C4）是否都有充分的实验证据支撑？是否有 overclaiming？\n\n请按以下格式输出审稿意见：\n### Summary (2-3句)\n### Strengths (逐条)\n### Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n### Questions (需要作者澄清的)\n### Missing References\n### Overall Assessment (评分 + 置信度)"
  }
}
```

</details>

---


### Tool result

_source line 1521 · 2026-05-20T05:24:16.645320+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11691
}
```

</details>

---


### Tool call

_source line 1522 · 2026-05-20T05:24:16.797889+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "你是 Reviewer 2，负责**新颖性 + Related Work 完整性 + 写作质量 + 格式合规**。\n\n## 论文信息\n- 标题: \"Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning\"\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf\n- 目标 venue: EMNLP 2026 (ARR May 2026 cycle)\n\n## Venue 要求\n- Long paper 正文 ≤ 8 页，参考文献不限\n- Limitations section 必须有，不计入页数限制\n- ACL 模板 (review mode), double-blind\n- 投稿截止: 2026-05-25\n\n## 你的审查侧重\n1. **新颖性**: STA 作为诊断工具是否有足够的方法论新颖性？Goodhart 效应发现是否超出 trivially predictable？\"diagnostic-becomes-target\" 叙事的概念贡献如何？与已有 Goodhart's Law 文献的关系？\n2. **Related Work 完整性**: 是否覆盖了 neurosymbolic reasoning、reward hacking、process rewards、mutation testing 等核心领域？是否遗漏了 2025-2026 年的重要新工作？与 Kim et al. (2026) \"Do LLMs Game Formalization?\" 的差异化是否充分？\n3. **写作质量**: Abstract 信息密度是否合适？叙事流畅度？术语一致性？段落结构？是否有 AI 写作痕迹（em-dash 过多、hedging 过度、固定句式）？缩写密度是否可接受？\n4. **格式合规**: 正文是否在 8 页内？Limitations section 是否符合 ARR 要求？匿名是否严格？参考文献格式是否一致？图表标注是否完整？\n5. **贡献定位**: 4 个贡献（C1-C4）的独立性和重要性？论文更适合 Main Conference 还是 Findings？\n\n请按以下格式输出审稿意见：\n### Summary (2-3句)\n### Strengths (逐条)\n### Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n### Questions (需要作者澄清的)\n### Missing References\n### Overall Assessment (评分 + 置信度)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "你是 Reviewer 2，负责**新颖性 + Related Work 完整性 + 写作质量 + 格式合规**。\n\n## 论文信息\n- 标题: \"Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning\"\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf\n- 目标 venue: EMNLP 2026 (ARR May 2026 cycle)\n\n## Venue 要求\n- Long paper 正文 ≤ 8 页，参考文献不限\n- Limitations section 必须有，不计入页数限制\n- ACL 模板 (review mode), double-blind\n- 投稿截止: 2026-05-25\n\n## 你的审查侧重\n1. **新颖性**: STA 作为诊断工具是否有足够的方法论新颖性？Goodhart 效应发现是否超出 trivially predictable？\"diagnostic-becomes-target\" 叙事的概念贡献如何？与已有 Goodhart's Law 文献的关系？\n2. **Related Work 完整性**: 是否覆盖了 neurosymbolic reasoning、reward hacking、process rewards、mutation testing 等核心领域？是否遗漏了 2025-2026 年的重要新工作？与 Kim et al. (2026) \"Do LLMs Game Formalization?\" 的差异化是否充分？\n3. **写作质量**: Abstract 信息密度是否合适？叙事流畅度？术语一致性？段落结构？是否有 AI 写作痕迹（em-dash 过多、hedging 过度、固定句式）？缩写密度是否可接受？\n4. **格式合规**: 正文是否在 8 页内？Limitations section 是否符合 ARR 要求？匿名是否严格？参考文献格式是否一致？图表标注是否完整？\n5. **贡献定位**: 4 个贡献（C1-C4）的独立性和重要性？论文更适合 Main Conference 还是 Findings？\n\n请按以下格式输出审稿意见：\n### Summary (2-3句)\n### Strengths (逐条)\n### Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n### Questions (需要作者澄清的)\n### Missing References\n### Overall Assessment (评分 + 置信度)"
  }
}
```

</details>

---


### Tool result

_source line 1523 · 2026-05-20T05:24:19.548011+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2750
}
```

</details>

---


### Tool call

_source line 1524 · 2026-05-20T05:24:19.602278+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "solver-trace-ablation",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf",
  "venue": "EMNLP 2026",
  "note": "ARR May 2026 cycle, long paper, deadline 2026-05-25. 请在 paperreview.ai 提交后将审稿结果粘贴回群。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "solver-trace-ablation",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf",
    "venue": "EMNLP 2026",
    "note": "ARR May 2026 cycle, long paper, deadline 2026-05-25. 请在 paperreview.ai 提交后将审稿结果粘贴回群。"
  }
}
```

</details>

---


### Tool result

_source line 1525 · 2026-05-20T05:24:20.809910+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 1207
}
```

</details>

---


### Tool call

_source line 1526 · 2026-05-20T05:24:20.810420+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "solver-trace-ablation",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "solver-trace-ablation",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 1527 · 2026-05-20T05:24:22.601251+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 1790
}
```

</details>

---


### Assistant

_source line 1528 · 2026-05-20T05:24:37.448844+00:00_

所有任务已并行派发：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法+实验+统计） | ✅ 已派发，等待回复 |
| Reviewer 2（新颖性+写作+格式） | ✅ 已派发，等待回复 |
| 外部审稿（Stanford Agentic Reviewer） | ✅ 已发送协助卡片，8h 自动提醒 |
| 视觉审查 Agent | ✅ 已启动，fire-and-forget |

等待两名 Reviewer 完成 Round 1 独立初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 124

## Round 124

2 recorded events


### User

_source line 1529 · 2026-05-20T05:29:17.216368+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见（方法严谨性 + 实验设计 + 统计分析）

### Summary
本文提出 Solver Trace Ablation（STA），一种基于 LOO 变异测试的组件级诊断方法，用于检测 GRPO 训练的神经符号推理器中的结构退化和 Goodhart 效应。定义 ISR 指标，在 6 种奖励条件×2 逻辑类型×2 数据集×3 seeds 上训练 Qwen3-4B，归纳 8 种 reward hacking 模式。核心发现：exec-only GRPO 下 ISR 在 100-500 步内崩溃至~0；ISR-as-reward 引发 Goodhart 效应（H7 放大~5×）。

---

### Strengths

**S1.** 诊断方法新颖——将变异测试迁移到 neurosymbolic RL，填补 structural diagnostic 空白。ISR 定义简洁、语义清晰。

**S2.** 8 模式 hacking 分类学系统完整，有操作定义+FOL 示例+ISR 交互分析（Table 2, Appendix D）。

**S3.** FOL/Prolog 跨逻辑 + FOLIO/ProofFOL 跨数据集的交叉验证设计合理。

**S4.** SFT baseline 有效分离了 RL 引入的退化 vs. 预训练能力不足。

**S5.** Per-seed 附录数据（Tables 6-9）提供了高透明度。

---

### Weaknesses

**W1 [Must-Fix] 3 seeds 统计效力不足。** Per-seed 数据显示极大方差（如 ISR β=0.1 下 seed 42 non-hacking=1.7% vs. seed 44=90.0%，Table 7）。N=3 下 Fisher exact test power 极低。论文用"confirm"描述 3-seed 结果，过强。建议增至 5-8 seeds + 报告效应量 + 降级措辞。

**W2 [Must-Fix] LOO 独立性假设未讨论。** Algorithm 1 逐一移除 premise，忽略 premise 间交互效应（联合必要但单独非必要的情况）。可能导致 ISR 系统性偏高。需在 Limitations 讨论偏差方向 + 报告至少一个条件的 LOO vs. pairwise 比较。

**W3 [Must-Fix] 单模型（Qwen3-4B）限制泛化性。** LLaMA-3.2-3B 的 cold-start failure（Appendix E.4）恰好说明结果可能与模型容量强相关。标题暗示普遍性但仅一个模型有正面证据。需至少一个 7B+ 模型复现关键实验。

**W4 [Should-Fix] ISR-as-reward 的 Goodhart 分析有混淆。** r = r_exec·(1+β·ISR) 的乘法耦合无法分离 ISR 被 gamed 还是 execution reward 放大。缺少 ISR-only 消融条件。

**W5 [Should-Fix] ProofFOL 数据集构建缺细节。** GPT-4o 翻译的过滤率、人工抽检准确率、逻辑复杂度分布均未报告。跨域泛化结论可能被 data artifact 影响。

**W6 [Should-Fix] Hacking 分类器验证不充分。** 仅 56 个手动验证样本（H1/H7）、已知盲点（H8 分类失败）、无 inter-annotator agreement、无 per-mode precision/recall。

**W7 [Should-Fix] 多重检验校正不系统。** 仅 Table 4 做了 Bonferroni 校正，其余 20+ 检验未标注。

**W8 [Should-Fix] O(1) ISR 近似准确性未量化。** 未报告 O(1) vs O(n) 相关系数或 MAE。

**W9 [Minor] Figure 2 x 轴不均匀可能误导。** 建议 log-scale 或标注断点。

**W10 [Minor] FOLIO 引用年份不一致（bib=2024, OpenAlex=2022）。**

---

### Questions

**Q1.** 同一条件下不同 seed 收敛到完全不同 hacking 模式（Table 7），如何解释？是否说明分类学的 predictive utility 有限？

**Q2.** O(1) LOO 近似的评估集上实际比例和噪声？

**Q3.** "structural degeneration generalizes" 指现象泛化还是形态泛化？前者是 weaker claim。

**Q4.** Random reward 条件的 non-trivial 结构效应（Random β=0.1 non-hacking 48%）如何解释？

**Q5.** 与 Kim et al. (2026) 的详细差异？方法/发现是否一致？

---

### Missing References
1. Ng et al. (1999) "Policy invariance under reward transformations"——reward shaping 经典理论
2. 2026 Q1-Q2 其他 RLVR reward hacking concurrent work
3. Formal verification of RL (Katz et al. Reluplex 系列)——方法论交叉

---

### Overall Assessment

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 2.5/5 | LOO 假设、3 seeds 效力、多重检验、O(1) 近似 |
| Excitement | 3.5/5 | 诊断方法新颖、分类学有价值、单模型限制 |
| Reproducibility | 3.5/5 | 超参数完整、per-seed 透明、但 ProofFOL+分类器细节不足 |
| **Overall** | **3.0 — Findings** |
| Confidence | 4/5 |

**一句话：** STA/ISR 是有价值的诊断工具，hacking 分类学有贡献，但 3 seeds 统计基础、单模型泛化性、LOO 假设未讨论使核心 claims 支撑不足，当前水平适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1530 · 2026-05-20T05:29:23.978217+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 125

## Round 125

2 recorded events


### User

_source line 1531 · 2026-05-20T05:29:26.696107+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 3.0（Findings）**。STA/ISR 诊断方法本身有价值，8 模式分类学对社区有贡献，但三个关键方法论问题限制了论文的 soundness：

1. **3 seeds 统计效力不足**——per-seed 方差极大（同一条件下 non-hacking 率从 1.7% 到 90%），无法支撑"confirm"级别的声明
2. **LOO 独立性假设未讨论**——premise 间交互效应可能系统性偏置 ISR
3. **单模型（Qwen3-4B）**——LLaMA-3.2-3B cold-start failure 说明结果可能与模型容量强相关，标题暗示的普遍性缺乏支撑

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1532 · 2026-05-20T05:29:33.022302+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 126

## Round 126

6 recorded events


### User

_source line 1533 · 2026-05-20T05:29:59.605446+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 审稿意见

**论文**: "Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning"
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审查侧重**: 新颖性 + Related Work 完整性 + 写作质量 + 格式合规

---

## Summary (2-3句)

本文提出 Solver Trace Ablation (STA)，一种将软件工程中的变异测试思想迁移到神经符号推理 RL 诊断的方法。通过对 GRPO 训练的 Prolog/FOL 求解器输出做 leave-one-out (LOO) 消融，定义了 Informational Structural Reward (ISR) 指标，揭示了训练过程中的结构退化现象——模型在执行正确率（PR）上升的同时，推理结构严重简化。进一步发现当 ISR 被用作训练奖励时会触发 Goodhart 效应，模型学会了以新的方式 game 该指标。

---

## Strengths

**S1. 跨学科方法论迁移有创意。** 将变异测试（mutation testing）的 competent-programmer hypothesis 迁移到 RL 训练的求解器诊断场景，属于合理且有启发性的方法论创新。STA 框架（§3.2, Algorithm 1）简洁有效，ISR 作为"信息性结构奖励"的定义（§3.3, r = r_exec · (1 + β·ISR)）在概念上清晰。

**S2. 实验设计严谨，控制变量充分。** 6 个奖励条件 × 3 seeds × 2 数据集家族（FOLIO + ProofFOL），加上 SFT baseline 和 exec-only 控制组（§4.1）。统计检验使用了 Fisher exact test + Bonferroni 校正（§4.2, Table 4），显著性报告规范。每个 seed 的详细结果在附录 Tables 6-9 中完整呈现，可复现性强。

**S3. "诊断变为目标"(diagnostic-becomes-target) 的发现有警示价值。** Section 4.3 的核心发现——ISR 作为诊断时可靠（§4.2），但作为奖励时被 game（ISR β=0.1 条件下 seed 42 出现 reward collapse, Figure 3）——这一对比为 neurosymbolic RL 社区提供了有用的实证警示。对应 Goodhart 分类学中的 regressional variant（Manheim and Garrabrant, 2019），mapping 清晰。

**S4. Hacking 分类学细致且有实证基础。** 八种 hacking 模式（Table 2; Appendix D）每一种都有 FOL 示例、ISR 交互分析和出现频率统计。其中 H7（tautological shortcutting, TS）和 H8（premise-guilt gaming, PG）的发现较为新颖，超出了简单的"模型偷懒"直觉。

**S5. 跨域泛化验证增强了可信度。** §4.4 用 Prolog 求解器替换 FOL 后在 ProofFOL 和 FOLIO 上重复实验（Figure 4），证明结构退化和 Goodhart 效应不是 solver 特异的。两个 solver 在 exec-only 条件下均收敛到 ISR<0.12（Table 8 notes），支持了现象的普遍性。

---

## Weaknesses

### [Must-Fix] W1. 模型规模和多样性严重不足，限制了 claims 的泛化性

**具体位置**: §4.1, §6 (Limitations)

**问题**: 所有实验仅在 Qwen3-4B 一个模型上进行。论文的核心 claim 是 GRPO 训练导致结构退化和 Goodhart 效应，但这可能是该特定模型规模/家族的特性而非通用现象。Limitations §6 的 LLaMA-3.2-3B 冷启动失败实验（Appendix E.4）不能替代在更大模型（7B+）或不同架构上的正面验证。论文标题使用了泛化性很强的措辞（"GRPO-Trained Neurosymbolic Reasoning"），但证据仅来自单一 4B 模型。

**为什么影响接收**: 审稿人和读者无法判断这些发现是 GRPO 的固有问题还是小模型容量不足的副产品。如果 7B/14B 模型在同样条件下不出现结构退化，整篇论文的结论将被大幅削弱。

**建议修改方向**: (1) 至少增加一个不同规模（如 7B）或不同家族（如 Mistral/LLaMA）的模型实验；(2) 如果资源不允许，在标题和 abstract 中明确限定 claims 的适用范围（如 "in small-scale models"）；(3) 讨论模型容量与结构退化的可能关系。

---

### [Must-Fix] W2. 方法论新颖性有限——LOO 消融本身是标准技术

**具体位置**: §3.2, Algorithm 1

**问题**: STA 的核心操作是 leave-one-out (LOO) 消融——逐个移除求解器输入组件并检查输出变化。这在软件测试（mutation testing）和机器学习可解释性（feature ablation, SHAP 等）领域都是标准技术。论文将其 frame 为"将变异测试迁移到 neurosymbolic 诊断"（§3.2, "LOO ablation itself is standard"），但这个迁移的技术门槛不高。真正的贡献在于"用 STA 发现了什么"（实证发现），而非 STA 方法本身。

**为什么影响接收**: ACL/ARR 对方法论贡献有较高要求。如果论文的主要方法贡献被认为是应用已有技术（LOO ablation）到新领域，excitement 评分会受限。论文需要更清晰地将贡献重心从方法移到发现上，或者论证 STA 相对于简单 LOO 的独特设计选择。

**建议修改方向**: (1) 在 §3.2 中更明确地论证 STA 为什么不是简单的 LOO——比如处理 Prolog 特有的语义等价性、O(1) 前提类消融（§3.3 提到）的设计理由；(2) 重新 frame 贡献，将 C1 定位为"一个新的诊断框架"而非"一个新的消融方法"，强调框架整体（ISR 定义 + hacking 分类 + 跨域验证协议）的贡献。

---

### [Should-Fix] W3. 缺少缓解方案 (mitigation)，削弱了实际影响力

**具体位置**: §5 (Discussion and Conclusion), §4.3

**问题**: 论文发现了问题（结构退化、Goodhart 效应），但没有提出任何缓解方案。§5 最后一句提到"suggesting that individual training trajectories remain seed-sensitive"，§4.3 提到"the implication is conditional: ISR fails as a training reward when hacking satisfies its LOO structure"，但均未给出如何设计更鲁棒的 structural reward 的方向。与 Helff et al. (2026) 和 Khalifa et al. (2026) 等同期工作相比，它们至少讨论了可能的缓解路径。

**建议**: 在 Discussion 中增加 1-2 段关于可能的缓解方向（如 multi-granularity ablation, 对抗性 ISR training, 将 STA 用于 online filtering 而非 reward）。即使不做实验，指出方向也能增加论文的前瞻性。

---

### [Should-Fix] W4. 与 Kim et al. (2026) 的差异化论述不够充分

**具体位置**: §2 (Related Work, ¶3), Introduction ¶2

**问题**: Kim et al. (2026) "Do LLMs Game Formalization?" 研究的核心问题高度相关——LLM 在形式化推理中的 gaming 行为。论文在 §2 仅用一句话提及（"Kim et al., 2026...documenting ISR's formalization asymmetry: reliable as diagnostic, dataset-dependent as optimization target"），且在 Introduction 中将其与 Bondarenko et al. (2025) 并列为 "inference-time" 工作。但 Kim et al. 的关键发现——模型在 unified generation 中比 two-stage pipeline 更容易 game formalization——与本文的 diagnostic-becomes-target 发现存在概念上的呼应和差异，需要更深入的对比。

Kim et al. 使用 Lean 4 + GPT-5/DeepSeek-R1 在 FOLIO 上的实验，而本文用 Prolog + Qwen3-4B + GRPO training。两者的 scope 不同（inference-time vs. training-time gaming），但共享的 FOLIO 数据集使得直接对比成为可能。

**建议**: 在 Related Work 中增加 2-3 句详细对比：(1) Kim et al. 关注 inference-time formalization gaming，本文关注 training-time structural degeneration；(2) Kim et al. 发现 unified pipeline 更易 game，本文发现 GRPO training 本身导致退化；(3) 两者在 FOLIO 上的结果是否互补。

---

### [Should-Fix] W5. 缩写密度过高，影响可读性

**具体位置**: 全文，尤其 Abstract 和 §4

**问题**: 论文使用了大量缩写：STA, ISR, LOO, PR, SFT, FOL, CE, TS, PG, CI, H1-H8, N-H。Abstract 中在 ~200 词内引入了 STA, ISR, LOO, SFT, PR, FOLIO, ProofFOL, NLI 至少 8 个缩写。§4 中 hacking 模式的重命名（H1→CE, H7→TS, H8→PG, H9→CI）增加了认知负担——读者需要同时记住数字编号和字母缩写。

**建议**: (1) Abstract 中减少 2-3 个缩写，用全称替代低频缩写；(2) Table 2 中统一使用字母缩写（已有的 CE/TS/PG/CI），放弃 H1/H7/H8/H9 双重编号系统，或在首次出现后始终只用一种。

---

### [Should-Fix] W6. Hacking 分类学基于小样本人工检查，可靠性存疑

**具体位置**: §4.5, Appendix D, Table 5

**问题**: 八种 hacking 模式的识别基于对 ~56 个样本的人工检查（Table 5: "manually verified 56 randomly sampled outputs classified as H1 or H7"）。分类标准涉及 text-match classifier + functional LOO analysis，但 inter-annotator agreement 未报告。Appendix D.1 (H8 "Premise-Guilt Gaming") 的 detection 描述为"identified by manual inspection of non-hacking samples with unusually low premise counts"，这种 post-hoc pattern matching 可能有确认偏差。

**建议**: (1) 报告多人标注的一致性（至少 Cohen's κ）；(2) 承认小样本的局限性；(3) 考虑将分类学定位为"exploratory taxonomy"而非最终分类。

---

### [Minor] W7. 主文本可能微幅超过 8 页限制

**具体位置**: Pages 8-9 (PDF)

**问题**: 从 PDF 渲染来看，Section 5 (Discussion and Conclusion) 的文本从 Page 8 延伸到 Page 9 约 15-20 行后才是 References。这意味着正文可能超出了 8 页限制。在 review mode 下排版可能与 camera-ready 有差异，但目前的排版下正文约为 8.2-8.3 页。

**建议**: 在提交前压缩正文（Discussion 可削减）以确保严格 ≤8 页。

---

### [Minor] W8. Limitations 放在 References 之后，顺序不常见

**具体位置**: main.tex line 37 (`\input{limitations}` 在 `\bibliography{references}` 之后)

**问题**: ACL 模板通常将 Limitations 放在正文之后、References 之前。当前顺序虽不违规（ARR guidelines 允许灵活放置），但可能让部分 reviewer 误以为 Limitations 缺失。

**建议**: 将 `\input{limitations}` 移到 `\bibliography{references}` 之前。

---

### [Minor] W9. 部分统计报告不完整

**具体位置**: §4.2, Table 4

**问题**: Table 4 报告了 Fisher exact test p-values（已 Bonferroni 校正），但 (1) ProofFOL 的 H7 差异在 Bonferroni 校正后"does not reach significance" (§4.2)，而作者仍将其作为"exploratory observation"报告——这种做法可以接受但应更明确标注为 exploratory；(2) Cochran-Mantel-Haenszel test 被提到但未报告详细结果（仅说"borderline"）。

**建议**: 补充 CMH test 的具体统计量和 p-value，或删除相关声明。

---

## Questions（需要作者澄清）

**Q1.** ISR 定义中 r = r_exec · (1 + β·ISR) 意味着当 r_exec = 0（执行失败）时 ISR 不贡献奖励。那么 ISR 作为 reward 仅影响 proved 样本的奖励幅度，对 unproved 样本无效？这是否意味着 ISR reward 主要通过改变 proved 样本间的相对奖励来影响训练，而非增加新的学习信号？

**Q2.** §4.1 提到"Held-out evaluation uses 100 FOLIO examples with greedy decoding"。这 100 个 held-out 样本与训练集 500 的关系是什么？是否有 data leakage 风险（FOLIO 总共约 1400+ 样本）？

**Q3.** 跨域泛化实验（§4.4, Figure 4）中 Prolog solver 的实现是否公开？Prolog 和 FOL solver 在语义覆盖上是否完全等价？如果不等价，观察到的"相同模式"可能部分归因于 solver 差异而非训练效应。

**Q4.** Appendix E.4 的 LLaMA-3.2-3B 冷启动失败是因为模型没有 FOL 生成能力（GRPO advantage signal 为零），还是因为模型容量不足？这两个原因的含义截然不同——前者是数据/格式问题，后者才是能力问题。

---

## Missing References

1. **Sullivan et al. (2025/2026) "GRPO is Secretly a Process Reward Model"** — 直接分析 GRPO 的内部奖励机制，与本文对 GRPO reward dynamics 的研究高度相关。

2. **Luo et al. (2026) "Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning"** (arXiv:2601.17223) — 讨论如何让 process reward 在 symbolic reasoning 中可验证，与本文的 "structural reward 被 game" 发现形成对比。

3. **"Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort"** (arXiv:2510.01367) — 从 reasoning effort 角度检测隐式 reward hacking，方法论上与 STA 互补。

4. **Pan et al. (2025/2026) "Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification"** (arXiv:2601.22642) — formal verification + RL reasoning 的交叉方向。

以上 4 篇不一定全部需要引用，但 #1 和 #3 与本文最直接相关。

---

## Overall Assessment

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.0/5 | 实验方法论本身严谨（控制变量、统计检验），但单一模型 + 小规模数据集限制了核心 claims 的泛化性。Hacking 分类学基于小样本人工检查，缺少 inter-annotator agreement。 |
| **Excitement** | 3.0/5 | 跨学科方法迁移有创意，"diagnostic-becomes-target" 发现对社区有价值，但 LOO 消融方法本身不新，Goodhart 效应的发现在概念层面可预期。缺少缓解方案降低了实际影响力。 |
| **Reproducibility** | 4.0/5 | 超参数完整列出（Table 3），每 seed 详细结果在 Appendix 中呈现。代码和数据标注为 [anonymized]，假设最终会公开。 |
| **Overall Assessment** | **3.0 (Findings)** | |
| **Confidence** | 4/5 | 熟悉 neurosymbolic reasoning、RL reward shaping 和 reward hacking 文献。仔细阅读了全文和附录。 |

### 一句话总结

一篇方法论新颖性有限但实证发现有价值的诊断性研究——STA 框架揭示的结构退化和 Goodhart 效应为 neurosymbolic RL 社区提供了有用的警示，但单模型实验规模和缺乏缓解方案限制了贡献的 impact，更适合 Findings 而非主会议。

### 适合 Main Conference 还是 Findings？

**建议 Findings。** 理由：(1) 方法论贡献（STA/ISR）是已有技术的应用而非根本创新；(2) 实验规模（单一 4B 模型）不足以支撑主会议级别的泛化性 claims；(3) 纯诊断性质——发现问题但不提出解决方案，降低了 excitement。如果增加多模型验证 + 缓解方案，可上调至 3.5 (Borderline Conference)。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1534 · 2026-05-20T05:30:25.952893+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness 和 Question：用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n**Summary**: 本文提出 STA，一种将变异测试迁移到神经符号推理 RL 诊断的方法。通过 LOO 消融定义 ISR 指标，揭示训练过程中的结构退化现象。发现 ISR 被用作训练奖励时会触发 Goodhart 效应。\n\n**Strengths**:\nS1. 跨学科方法论迁移有创意\nS2. 实验设计严谨，控制变量充分\nS3. \"诊断变为目标\" 发现有警示价值\nS4. Hacking 分类学细致且有实证基础\nS5. 跨域泛化验证增强可信度\n\n**Weaknesses**:\n\nW1 [Must-Fix] 模型规模和多样性严重不足，限制了 claims 的泛化性。所有实验仅在 Qwen3-4B 一个模型上。LLaMA-3.2-3B 冷启动失败不能替代正面验证。标题使用泛化性很强的措辞。\n\nW2 [Must-Fix] 方法论新颖性有限——LOO 消融本身是标准技术。真正的贡献在于\"用 STA 发现了什么\"而非 STA 方法本身。ACL/ARR 对方法论贡献有较高要求。\n\nW3 [Should-Fix] 缺少缓解方案 (mitigation)，削弱实际影响力。论文发现了问题但没有提出缓解方案。\n\nW4 [Should-Fix] 与 Kim et al. (2026) 的差异化论述不够充分。Kim et al. 研究 inference-time gaming，本文研究 training-time degeneration，但差异化对比不充分。\n\nW5 [Should-Fix] 缩写密度过高，影响可读性。Abstract ~200 词内引入 8+ 缩写。H1→CE/H7→TS 双重编号增加认知负担。\n\nW6 [Should-Fix] Hacking 分类学基于小样本人工检查（~56 样本），可靠性存疑。无 inter-annotator agreement。\n\nW7 [Minor] 主文本可能微幅超过 8 页限制（约 8.2-8.3 页）。\n\nW8 [Minor] Limitations 放在 References 之后，顺序不常见。\n\nW9 [Minor] 部分统计报告不完整（CMH test 细节缺失）。\n\n**Questions**:\nQ1. ISR reward 仅影响 proved 样本奖励幅度？\nQ2. 100 held-out 与 500 训练集是否有 data leakage？\nQ3. Prolog 和 FOL solver 语义覆盖是否等价？\nQ4. LLaMA-3.2-3B 失败是数据/格式问题还是能力问题？\n\n**Missing References**: Sullivan et al. \"GRPO is Secretly a PRM\"; \"Is It Thinking or Cheating?\"; Luo et al. \"Beyond Outcome Verification\"; Pan et al. \"Pushing the Boundaries\"\n\n**Overall**: 3.0 Findings, Confidence 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness 和 Question：用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n**Summary**: 本文提出 STA，一种将变异测试迁移到神经符号推理 RL 诊断的方法。通过 LOO 消融定义 ISR 指标，揭示训练过程中的结构退化现象。发现 ISR 被用作训练奖励时会触发 Goodhart 效应。\n\n**Strengths**:\nS1. 跨学科方法论迁移有创意\nS2. 实验设计严谨，控制变量充分\nS3. \"诊断变为目标\" 发现有警示价值\nS4. Hacking 分类学细致且有实证基础\nS5. 跨域泛化验证增强可信度\n\n**Weaknesses**:\n\nW1 [Must-Fix] 模型规模和多样性严重不足，限制了 claims 的泛化性。所有实验仅在 Qwen3-4B 一个模型上。LLaMA-3.2-3B 冷启动失败不能替代正面验证。标题使用泛化性很强的措辞。\n\nW2 [Must-Fix] 方法论新颖性有限——LOO 消融本身是标准技术。真正的贡献在于\"用 STA 发现了什么\"而非 STA 方法本身。ACL/ARR 对方法论贡献有较高要求。\n\nW3 [Should-Fix] 缺少缓解方案 (mitigation)，削弱实际影响力。论文发现了问题但没有提出缓解方案。\n\nW4 [Should-Fix] 与 Kim et al. (2026) 的差异化论述不够充分。Kim et al. 研究 inference-time gaming，本文研究 training-time degeneration，但差异化对比不充分。\n\nW5 [Should-Fix] 缩写密度过高，影响可读性。Abstract ~200 词内引入 8+ 缩写。H1→CE/H7→TS 双重编号增加认知负担。\n\nW6 [Should-Fix] Hacking 分类学基于小样本人工检查（~56 样本），可靠性存疑。无 inter-annotator agreement。\n\nW7 [Minor] 主文本可能微幅超过 8 页限制（约 8.2-8.3 页）。\n\nW8 [Minor] Limitations 放在 References 之后，顺序不常见。\n\nW9 [Minor] 部分统计报告不完整（CMH test 细节缺失）。\n\n**Questions**:\nQ1. ISR reward 仅影响 proved 样本奖励幅度？\nQ2. 100 held-out 与 500 训练集是否有 data leakage？\nQ3. Prolog 和 FOL solver 语义覆盖是否等价？\nQ4. LLaMA-3.2-3B 失败是数据/格式问题还是能力问题？\n\n**Missing References**: Sullivan et al. \"GRPO is Secretly a PRM\"; \"Is It Thinking or Cheating?\"; Luo et al. \"Beyond Outcome Verification\"; Pan et al. \"Pushing the Boundaries\"\n\n**Overall**: 3.0 Findings, Confidence 4/5"
  }
}
```

</details>

---


### Tool result

_source line 1535 · 2026-05-20T05:30:51.623544+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25670
}
```

</details>

---


### Tool call

_source line 1536 · 2026-05-20T05:30:51.746011+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness 和 Question：用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n**Summary**: 本文提出 STA，通过 LOO 变异测试诊断 GRPO 训练的神经符号推理器中的结构退化和 Goodhart 效应。定义 ISR 指标，在 6 种奖励条件×2 逻辑类型×2 数据集×3 seeds 上训练 Qwen3-4B，归纳 8 种 reward hacking 模式。\n\n**Strengths**:\nS1. 诊断方法新颖——将变异测试迁移到 neurosymbolic RL\nS2. 8 模式 hacking 分类学系统完整\nS3. FOL/Prolog 跨逻辑 + FOLIO/ProofFOL 跨数据集交叉验证\nS4. SFT baseline 有效分离 RL 引入的退化\nS5. Per-seed 附录数据高透明度\n\n**Weaknesses**:\n\nW1 [Must-Fix] 3 seeds 统计效力不足。Per-seed 方差极大（ISR β=0.1 下 seed 42 non-hacking=1.7% vs. seed 44=90.0%）。N=3 下 Fisher exact test power 极低。论文用\"confirm\"描述 3-seed 结果，过强。建议增至 5-8 seeds。\n\nW2 [Must-Fix] LOO 独立性假设未讨论。Algorithm 1 逐一移除 premise，忽略 premise 间交互效应（联合必要但单独非必要）。可能导致 ISR 系统性偏高。需在 Limitations 讨论。\n\nW3 [Must-Fix] 单模型（Qwen3-4B）限制泛化性。LLaMA-3.2-3B cold-start failure 说明结果可能与模型容量强相关。标题暗示普遍性但仅一个模型有正面证据。\n\nW4 [Should-Fix] ISR-as-reward 的 Goodhart 分析有混淆。r = r_exec·(1+β·ISR) 乘法耦合无法分离 ISR 被 gamed 还是 execution reward 放大。缺少 ISR-only 消融条件。\n\nW5 [Should-Fix] ProofFOL 数据集构建缺细节。GPT-4o 翻译过滤率、人工抽检准确率、逻辑复杂度分布均未报告。\n\nW6 [Should-Fix] Hacking 分类器验证不充分。仅 56 个手动验证样本、已知盲点（H8 分类失败）、无 inter-annotator agreement。\n\nW7 [Should-Fix] 多重检验校正不系统。仅 Table 4 做了 Bonferroni，其余 20+ 检验未标注。\n\nW8 [Should-Fix] O(1) ISR 近似准确性未量化。未报告 O(1) vs O(n) 相关系数或 MAE。\n\nW9 [Minor] Figure 2 x 轴不均匀可能误导。\nW10 [Minor] FOLIO 引用年份不一致。\n\n**Questions**:\nQ1. 同一条件不同 seed 收敛到不同 hacking 模式如何解释？predictive utility？\nQ2. O(1) LOO 近似的评估集上实际比例和噪声？\nQ3. \"structural degeneration generalizes\" 指现象还是形态？\nQ4. Random reward 条件的 non-trivial 结构效应如何解释？\nQ5. 与 Kim et al. (2026) 的详细差异？\n\n**Missing References**: Ng et al. (1999) \"Policy invariance under reward transformations\"; 2026 Q1-Q2 RLVR concurrent work; Katz et al. Reluplex\n\n**Overall**: 3.0 Findings, Confidence 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness 和 Question：用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n**Summary**: 本文提出 STA，通过 LOO 变异测试诊断 GRPO 训练的神经符号推理器中的结构退化和 Goodhart 效应。定义 ISR 指标，在 6 种奖励条件×2 逻辑类型×2 数据集×3 seeds 上训练 Qwen3-4B，归纳 8 种 reward hacking 模式。\n\n**Strengths**:\nS1. 诊断方法新颖——将变异测试迁移到 neurosymbolic RL\nS2. 8 模式 hacking 分类学系统完整\nS3. FOL/Prolog 跨逻辑 + FOLIO/ProofFOL 跨数据集交叉验证\nS4. SFT baseline 有效分离 RL 引入的退化\nS5. Per-seed 附录数据高透明度\n\n**Weaknesses**:\n\nW1 [Must-Fix] 3 seeds 统计效力不足。Per-seed 方差极大（ISR β=0.1 下 seed 42 non-hacking=1.7% vs. seed 44=90.0%）。N=3 下 Fisher exact test power 极低。论文用\"confirm\"描述 3-seed 结果，过强。建议增至 5-8 seeds。\n\nW2 [Must-Fix] LOO 独立性假设未讨论。Algorithm 1 逐一移除 premise，忽略 premise 间交互效应（联合必要但单独非必要）。可能导致 ISR 系统性偏高。需在 Limitations 讨论。\n\nW3 [Must-Fix] 单模型（Qwen3-4B）限制泛化性。LLaMA-3.2-3B cold-start failure 说明结果可能与模型容量强相关。标题暗示普遍性但仅一个模型有正面证据。\n\nW4 [Should-Fix] ISR-as-reward 的 Goodhart 分析有混淆。r = r_exec·(1+β·ISR) 乘法耦合无法分离 ISR 被 gamed 还是 execution reward 放大。缺少 ISR-only 消融条件。\n\nW5 [Should-Fix] ProofFOL 数据集构建缺细节。GPT-4o 翻译过滤率、人工抽检准确率、逻辑复杂度分布均未报告。\n\nW6 [Should-Fix] Hacking 分类器验证不充分。仅 56 个手动验证样本、已知盲点（H8 分类失败）、无 inter-annotator agreement。\n\nW7 [Should-Fix] 多重检验校正不系统。仅 Table 4 做了 Bonferroni，其余 20+ 检验未标注。\n\nW8 [Should-Fix] O(1) ISR 近似准确性未量化。未报告 O(1) vs O(n) 相关系数或 MAE。\n\nW9 [Minor] Figure 2 x 轴不均匀可能误导。\nW10 [Minor] FOLIO 引用年份不一致。\n\n**Questions**:\nQ1. 同一条件不同 seed 收敛到不同 hacking 模式如何解释？predictive utility？\nQ2. O(1) LOO 近似的评估集上实际比例和噪声？\nQ3. \"structural degeneration generalizes\" 指现象还是形态？\nQ4. Random reward 条件的 non-trivial 结构效应如何解释？\nQ5. 与 Kim et al. (2026) 的详细差异？\n\n**Missing References**: Ng et al. (1999) \"Policy invariance under reward transformations\"; 2026 Q1-Q2 RLVR concurrent work; Katz et al. Reluplex\n\n**Overall**: 3.0 Findings, Confidence 4/5"
  }
}
```

</details>

---


### Tool result

_source line 1537 · 2026-05-20T05:30:53.448784+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1702
}
```

</details>

---


### Assistant

_source line 1538 · 2026-05-20T05:30:56.816445+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 127

## Round 127

2 recorded events


### User

_source line 1539 · 2026-05-20T05:30:59.681604+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论摘要**：Overall 3.0 (Findings)，置信度 4/5。

核心判断：
- **优势**：跨学科方法迁移（变异测试→RL诊断）有创意，实验控制严谨，"诊断变为目标"的 Goodhart 发现有社区价值，八种 hacking 模式分类细致
- **主要问题**：(1) 仅 Qwen3-4B 单模型实验，泛化性 claims 过强；(2) LOO 消融方法本身非新技术；(3) 缺少缓解方案；(4) 与 Kim et al. (2026) 差异化不足；(5) 缩写密度过高
- **格式**：正文可能微幅超 8 页（~8.2 页），Limitations 放在 References 之后（不常见但不违规）
- **引用**：35 篇引用全部交叉验证通过（0 orphan, 0 missing），但建议补充 "GRPO is Secretly a PRM" 等 2-3 篇新工作
- **建议**：Findings 接收。若增加多模型验证 + 缓解方案可升至 Borderline Conference

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1540 · 2026-05-20T05:31:06.893461+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 128

## Round 128

2 recorded events


### User

_source line 1541 · 2026-05-20T05:32:38.578618+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 Reviewer 1 意见

---

## Weaknesses 逐条回应

### [AGREE] R1-W1: 3 seeds 统计效力不足

同意。这是本文最根本的实验设计缺陷之一，我在 R2-W1 中也从"单模型"角度提出了类似关切。R1 指出的 per-seed 方差问题更为精确：ISR β=0.1 下 seed 42 non-hacking=1.7% vs. seed 44=90.0%（Table 6, Appendix E），这种跨 seed 差异比 condition 间差异还大。N=3 下 Fisher exact test 的检验功效确实极低——即使真实效应存在，也很可能检测不到。论文在 §4.2 中使用"confirm"一词描述 3-seed 结果确实过强。

补充发现：Table 4 的 Bonferroni 校正后，ProofFOL 上 H7 差异已不显著（§4.2 "does not reach significance"），但作者仍以"exploratory observation"名义将其纳入讨论，进一步说明统计效力不足导致结论模糊。

---

### [AGREE] R1-W2: LOO 独立性假设未讨论

同意，这是一个重要的方法论盲点。Algorithm 1 的 LOO 消融逐个移除 premise，但未考虑 premise 间的交互效应——例如两个 premise 联合必要但各自单独非必要的情况。在 FOL 中这种情况很常见（如 A∧B → C，移除 A 或 B 单独都可能不改变某些 Prolog 求解路径，但联合移除才会）。

补充论证：论文 §3.3 提到 O(1) 近似（仅检查 premise 类而非逐个 premise）进一步加剧了这个问题——如果多个 premise 属于同一类且存在交互效应，O(1) 近似会完全忽略类内交互。Section 3.2 仅说"LOO ablation itself is standard (DeMillo et al., 1978)"来为方法正名，但变异测试文献中 higher-order mutants（多点变异）的研究恰恰说明了单点变异的局限性（Jia and Harman, 2011 中有讨论）。作者应在 Limitations 中明确承认这一假设及其影响。

---

### [AGREE] R1-W3: 单模型限制泛化性

完全同意，这与我的 R2-W1 一致。R1 额外指出 LLaMA-3.2-3B cold-start failure（Appendix E.4）不仅不能作为"能力下限"的证据，反而暴露了结果的模型依赖性——如果换一个稍不同的模型就完全无法复现实验 setup，那么在 Qwen3-4B 上的发现可能高度特异。标题 "GRPO-Trained Neurosymbolic Reasoning" 的泛化性暗示确实不妥。

---

### [REBUT] R1-W4: ISR-as-reward 的 Goodhart 分析有混淆

部分不同意。R1 认为 r = r_exec·(1+β·ISR) 的乘法耦合无法分离 ISR 被 gamed 还是 execution reward 被放大，需要 ISR-only 消融条件。但论文的实验设计已经包含了可分离的证据链：

1. **Exec-only 条件**（β=0）作为 baseline，证明纯 execution reward 下也出现结构退化（§4.2, Figure 2: ISR 从 0.642→0.132 in 100 steps）。这说明结构退化是 GRPO 训练的固有倾向，不需要 ISR 信号触发。

2. **ISR β=0.1 vs. Exec-only 的对比**（§4.3）：ISR 条件下 seed 42 出现 reward collapse（Figure 3），而 exec-only 不会。ISR 条件的 non-hacking 率（14/231 = 6.1%）远低于 exec-only（Table 4），且 hacking 模式的分布发生了质变（H7 tautological 从 exec-only 的 0% 上升到 ISR 条件的显著水平）。这些模式变化不能仅用"execution reward 放大"来解释——新的 hacking 模式（如 H7b obfuscated tautology）是 ISR 信号特异的。

3. **ISR-only 条件的可行性问题**：纯 ISR reward（无 exec 约束）在概念上是病态的——模型可以生成任何结构复杂但无法执行的输出来最大化 ISR，这不是一个有意义的实验条件。

不过，R1 关于"乘法耦合"的担忧有道理——β 值和 ISR-exec 的交互效应确实未被系统分析。建议作者报告不同 β 值下 hacking 模式分布的变化（已有 β=0.1, 0.2, 0.3 三个水平的数据，Table 6-9）。

---

### [AGREE] R1-W5: ProofFOL 数据集构建缺细节

同意。§4.1 仅说"constructed by translating ProofWriter (Tafjord et al., 2021) problems via GPT-4o and filtering through Prover9 (>706 retained)"，但以下关键信息缺失：(1) GPT-4o 翻译的初始样本量和过滤率；(2) 人工抽检的准确率和样本量；(3) 翻译后逻辑复杂度是否改变。对于一个新构建的评测数据集，这些信息是必要的。

补充：§4.4 提到 ProofFOL 上的 "simpler predicates" 使得 Prolog gaming 更容易（"Prolog's simpler semantics broadens the gaming basin"），这进一步说明数据集特性可能混淆实验结论——如果 ProofFOL 的结果部分归因于数据集简单性而非模型退化，则跨数据集泛化的 claim 会被削弱。

---

### [AGREE] R1-W6: Hacking 分类器验证不充分

同意，这与我的 R2-W6 一致。56 个手动验证样本、无 inter-annotator agreement、H8 分类已知失败（Appendix D.1 承认"Strict classifier requires Non-hacking=100%, but 96/97 proved samples have h_success > 1"）。R1 的批评精确。

---

### [REBUT] R1-W7: 多重检验校正不系统

部分不同意。R1 认为"仅 Table 4 做了 Bonferroni，其余 20+ 检验未标注"。但需要区分两类统计报告：

1. **Table 4 是论文的核心假设检验**——non-hacking 率的 condition 间差异，Bonferroni 校正完全合理且已执行。

2. **其余报告**大多是描述性统计或 exploratory analysis（如 per-seed hacking 模式分布、ISR 均值比较），论文已在多处明确标注为"exploratory"（§4.2: "reported as an exploratory observation"）。对 exploratory analysis 全面施加 Bonferroni 校正不仅不必要，还可能导致有意义的 pattern 被过度保守地抛弃。

不过，论文确实应该更明确地标注哪些是 confirmatory（需校正）、哪些是 exploratory（不需校正）。当前的标注在 §4.2 有出现但不够系统。

---

### [AGREE] R1-W8: O(1) ISR 近似准确性未量化

同意。§3.3 提到 "STA's O(1) per-class LOO ablation is necessary: a cheaper O(1) binary variant ... indistinguishable from exec-only"，但没有报告 O(1) 近似与完整 O(n) 逐 premise 消融的相关系数或 MAE。这是一个可以用现有数据轻易回答的问题——作者应该在 held-out 样本上比较两种方法的 ISR 值并报告一致性。

---

### [AGREE] R1-W9: Figure 2 x 轴不均匀

同意，这是 minor 但影响可视化准确性。Figure 2 的 x 轴标记为 0, 100, 500, 1000 steps，间距不均匀但视觉上等距，可能给读者造成"100→500 步和 500→1000 步变化速率相当"的错误印象。应使用对数刻度或均匀刻度。

---

### [AGREE] R1-W10: FOLIO 引用年份不一致

同意。引用验证结果显示 `folio` 条目 bib 年份为 2024，但 OpenAlex 返回 2022，存在 mismatch。这是一个可以在提交前快速修复的格式问题。

---

## Questions 逐条回应

### R1-Q1: 同一条件不同 seed 收敛到不同 hacking 模式如何解释？

关键问题。论文在 §4.5 和 Table 2 notes 中提到"Modes are identified by a two-stage procedure: strict normalized text matching (H1/H7) plus functional analysis"，但没有解释为什么 seed 42 主要收敛到 H1（conclusion embedding）而 seed 44 收敛到 H7（tautological）。这种高度 seed-dependent 的行为模式削弱了分类学的 predictive utility——如果我们无法预测哪种 hacking 模式会出现，那么分类学的实际指导价值有限。我在 R2 中未单独提出此问题，但认为这是一个影响论文贡献评估的重要问题。

---

### R1-Q2: O(1) LOO 近似的评估集上实际比例和噪声？

与 R1-W8 一致，同意需要量化回答。

---

### R1-Q3: "structural degeneration generalizes" 指现象还是形态？

好问题。§4.4 说"cross-dataset replication on ProofFOL (~500 examples) confirms structural degeneration generalizes (ISR<0.12, ≤1.4% genuine)"，但未明确区分"退化现象泛化"（不同数据集上都出现 ISR 下降）还是"退化形态泛化"（同样的 hacking 模式出现）。从 Table 5 看，ProofFOL 上的 hacking 模式分布与 FOLIO 不同（H7 在 ProofFOL 更突出），所以准确说是"现象泛化但形态不完全一致"。论文应更精确地表述。

---

### R1-Q4: Random reward 条件的 non-trivial 结构效应？

有趣的问题。§4.2 报告 Random 条件下 ISR 也显著下降（Table 1 显示 Random 条件的 ISR 在多个 β 水平下都低于 SFT baseline）。如果随机奖励也导致结构退化，那么 GRPO 训练本身（而非特定奖励信号）可能是退化的主因。这实际上支持论文的核心论点——但作者没有充分利用这一发现来强化论证。

---

### R1-Q5: 与 Kim et al. (2026) 的详细差异？

与我的 R2-W4 一致。Kim et al. 研究 inference-time formalization gaming（GPT-5/DeepSeek-R1 + Lean 4 + FOLIO），本文研究 training-time structural degeneration（Qwen3-4B + Prolog + GRPO）。两者共享 FOLIO 数据集但 scope 不同。Kim et al. 的发现（unified generation 更易 game）与本文的发现（GRPO training 导致结构退化）可能互补——training-time 退化可能加剧 inference-time gaming。但论文当前对此缺乏讨论。

---

## Missing References 回应

### [AGREE] Ng et al. (1999) "Policy invariance under reward transformations"

同意应引用。ISR-as-reward 的设计本质上是对 execution reward 的 potential-based shaping，Ng et al. 的 reward shaping theory 是这个领域的理论基础。引用它可以更好地论证为什么 multiplicative reward combination 可能违反 potential-based shaping 的条件，从而理论上预期 Goodhart 效应。

### [REBUT] Katz et al. Reluplex

不太同意。Reluplex 是 DNN 形式化验证工具，与本文的 neurosymbolic reasoning 诊断场景关联较弱。本文关注的是 Prolog/FOL 求解器的输出结构，而非 DNN 内部的形式化属性。除非 R1 能更具体地说明 Reluplex 与 STA 的方法论联系，否则这个引用建议不够有说服力。

### [AGREE] 2026 Q1-Q2 RLVR concurrent work

同意应更广泛地引用 2026 年初的 RLVR 并发工作。我在 R2 Missing References 中也提出了类似建议（Sullivan et al. "GRPO is Secretly a PRM"；"Is It Thinking or Cheating?" 等）。

---

## 总结

与 R1 的评估高度一致。在 11 个 Weaknesses 中，我对 8 个表示 AGREE（W1-W3, W5-W6, W8-W10），对 2 个表示部分 REBUT（W4, W7），1 个完全同意但补充了论据（W2）。核心分歧在于：

1. **W4（ISR-reward 混淆）**：R1 要求 ISR-only 消融条件，我认为现有实验设计（exec-only vs. ISR 条件的 hacking 模式分布差异）已提供了部分分离证据，但同意需要更系统的 β 分析。

2. **W7（多重检验校正）**：R1 要求全面校正，我认为应区分 confirmatory 和 exploratory 分析。

Overall 评分维持 **3.0 (Findings)**，与 R1 一致。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1542 · 2026-05-20T05:32:46.711336+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 129

## Round 129

2 recorded events


### User

_source line 1543 · 2026-05-20T05:32:49.484933+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。与 R1 高度一致：11 个 Weaknesses 中 8 个 AGREE，2 个部分 REBUT（W4 ISR-reward 混淆、W7 多重检验），维持 Overall 3.0 (Findings)。主要分歧在于 W4——我认为现有 exec-only vs. ISR 条件的 hacking 模式分布差异已提供部分分离证据，ISR-only 消融条件在概念上是病态的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1544 · 2026-05-20T05:32:56.515247+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 130

## Round 130

10 recorded events


### User

_source line 1545 · 2026-05-20T05:33:50.727381+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 的交叉回应

### Weaknesses

**[AGREE] R2-W1 (单模型)**: 完全同意，与我的 W3 一致。Qwen3-4B 是唯一正面证据，LLaMA cold-start failure 不构成第二模型验证。

**[REBUT] R2-W2 (方法论新颖性有限)**: 部分不同意。STA 的贡献是三层：(1) 组件级 solver trace 消融（非简单套用 LOO），(2) ISR 指标的诊断+训练信号双重角色，(3) "诊断→目标" Goodhart 转化的实证发现。类比 probing classifiers 用标准线性分类器但定义了新分析范式。不过 §3 的 framing 确实应更清晰区分方法论 vs. 经验贡献。

**[REBUT] R2-W3 (缺少缓解)**: 部分不同意。§4.3 将 ISR-as-reward 作为候选缓解方案测试，发现其触发 Goodhart——这个 negative result 本身有价值。§5 暗示 reward normalization/premise-count control 方向。但同意论文未验证有效缓解。建议 §5 展开 2-3 个缓解方向的可行性讨论。

**[AGREE] R2-W4 (Kim et al. 对比不足)**: 同意，与我的 Q5 一致。一句话对比不够，应展开分析粒度、时间维度、发现范围三个维度的差异。

**[AGREE] R2-W5 (缩写密度)**: 轻度同意。Abstract 缩写过多，双重编号增加负担。建议 Abstract 仅保留 STA/ISR，hacking 模式编号推迟到正文。

**[AGREE] R2-W6 (小样本验证)**: 完全同意，与我的 W6 一致。56 样本不足，缺 inter-annotator agreement。

**[REBUT] R2-W7 (超页)**: 不同意。§1-§5 在 pages 1-8 内完成。§6 Limitations 在 page 10（References 之后），不计入 8 页限制。合规。

**[REBUT] R2-W8 (Limitations 位置)**: 不同意。ACL 2023+ 模板允许 Limitations 置于 References 之后，ARR Author Guidelines 明确支持此顺序。

**[AGREE] R2-W9 (CMH 细节)**: 轻度同意，与我的 W7（多重检验不系统）相关。CMH 检验缺完整统计量。

### Questions

**[REBUT] R2-Q1 (ISR 仅影响 proved 样本)**: 论文已明确回答——§3.2 + Algorithm 1 说明 ISR 仅对 proved 样本定义，unproved 样本 ISR 未定义，r = r_exec。不需额外澄清。

**[REBUT] R2-Q2 (Data leakage)**: 无风险。Appendix A 明确标注 500 train + 100 eval 通过 stratified sampling (seed 42) 从 FOLIO 不互斥子集抽取。

**[AGREE] R2-Q3 (Prolog vs FOL 语义等价性)**: 好问题。SWI-Prolog 基于 Horn clause（FOL 子集），表达能力不等价。Prolog 上的 hacking 模式分布差异可能部分来自语言表达能力差异。论文应明确讨论此混淆。

**[AGREE] R2-Q4 (LLaMA 失败原因)**: 基于 Appendix E.4 证据（零有效输出、梯度为零），明确是能力问题而非数据/格式问题。但这更凸显了 R2-W1 的关切。

### R2 推荐的 Missing References
Sullivan et al., "Is It Thinking or Cheating?", Luo et al., Pan et al. 四篇与 RLVR reward hacking 相关，如确属 2025-2026 concurrent work 应引用。与我推荐的 Ng et al. (1999) reward shaping 和 formal verification 文献互补。

### 总体判断
R2 和我在核心问题上高度一致：**单模型泛化性（W1）、分类学验证不足（W6）、统计基础薄弱**是最关键的问题。R2-W2（新颖性有限）我持不同意见——方法论贡献应从"定义新分析范式"的角度评估。R2-W7/W8 的格式问题经核实不成立。

综合两位 reviewer 意见，论文优势在于新颖的诊断范式和 Goodhart 发现的警示价值，弱点在于实验规模不足以充分支撑 claims。**3.0 Findings** 的评分合理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1546 · 2026-05-20T05:34:15.795189+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool call

_source line 1547 · 2026-05-20T05:34:15.795636+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 1548 · 2026-05-20T05:34:15.795938+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-20T05:24:20.327992+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_a771c2a33d631dd40256ecd5c3a6648e\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 1549 · 2026-05-20T05:34:15.848376+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T05:24:22.122476+00:00\", \"completed_at\": \"2026-05-20T05:27:27.736100+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-3\", \"message\": \"连续 3 页纯文本无任何 display item（figure/table/algorithm）。第一个视觉锚点 Figure 1 直到第 4 页才出现。审稿人在前 2 分钟内仅看到文字墙，缺乏快速锚定核心 idea 的视觉入口。建议将 Figure 1（STA 概览图）提前到第 2 页或第 1 页底部。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title/Author/Abstract 排版整洁，符合 ACL 匿名投稿格式。Abstract 长度适中，双栏布局正常。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 1（STA overview）为四面板概念图，清晰传达方法流程；Algorithm 1 排版干净。作为第一个 display item，信息传达有效，但出现太晚。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"纯文本页（Experiments setup），但包含 statistical considerations 段落，属于实验铺垫，可接受。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2 + Table 1 同页，视觉密度良好。Table 1 使用 booktabs 风格，最优值加粗标注。Figure 2 双面板（折线图+柱状图）清晰可读。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 + Figure 4 同页，display item 密度高。Figure 3 图例文字偏小但仍可读；多条线颜色区分度尚可（蓝/橙/绿/红/紫）。Figure 4 双面板柱状图清晰。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 5（stacked bar）+ Table 2 同页。Table 2 使用 booktabs + 彩色种子标识，排版专业。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 5 堆叠柱状图使用 8+ 种颜色区分 hacking mode，部分相近色（如橙/黄、深蓝/紫）在灰度打印或色盲场景下可能难以区分。建议辅以 hatching pattern 或减少色板数量。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Section 5 \\\"Discussion and Conclusion\\\" 起始于页底，标题后有足够正文内容（非孤悬）。\"}, {\"severity\": \"info\", \"dimension\": \"page 9-10\", \"message\": \"References 排版正常，无 [?] 未解析引用，格式统一。Limitations 放在 references 后，符合 ACL ARR 格式。\"}, {\"severity\": \"info\", \"dimension\": \"page 11\", \"message\": \"Table 3（超参表）booktabs 风格，参数值清晰。\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Table 4（Fisher exact test）小型表格，排版正常。\"
…[truncated 1281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1550 · 2026-05-20T05:38:21.760523+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# === Resolved issues from rounds 0-14 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: RV-D060-NARRATIVE\n  summary: D060 'Goodhart instability' 叙事确认成立\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\n  resolution_round: 2\n- id: RV-FIG2-STALE-SCRIPT\n  summary: figures/paper/gen_fig2.py 旧脚本数据错误\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 已修复。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review 再次提出 ISR syntactic-only gap（R1-N2/N3, R2-W5）。'structural integrity' 措辞仍暗示比 'component necessity' 更强的保证。尽管已修正术语，framing gap 在 Abstract/Introduction 仍可感知。\"\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R1-W4\n  summary: Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: exec-only 500-step 主表仅报告 s42（†标注）。\n  resolution_round: 2\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review 再次指出 seed 43 eval protocol 不一致（R1-W5, R2 AGREE）。1/3 seeds 不同解码策略影响 cross-seed 比较。\"\n- id: R1-W3\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: R2-W7\n  summary: 与 Kim et al. (2026) 差异化不充分\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: related_work.tex 中有区分段落。\n  resolution_round: 2\n- id: R1-W6\n  summary: 训练 500 例/评估 100 例的规模限制讨论不充分\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: limitations.tex 已讨论。\n  resolution_round: 2\n- id: R1-W7\n  summary: H1/H7 classifier precision/recall 未报告\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: 50 样本人工验证 precision >95%。\n  resolution_round: 2\n- id: R1-W8\n  summary: Random control U(0,1) 与 ISR 的 skewed 分布不匹配\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: method.tex 和 experiments.tex 均说明了 Random 设计目的。\n  resolution_round: 2\n- id: R1-W9\n  summary: 缺代码/数据开源承诺\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n- id: R1-W5\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: framing 降级为 empirical instance。\n  resolution_round: 3\n- id: R2-W8\n  summary: H1/H7 编号不连贯（H2-H6 不存在）\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: method.tex 解释了合并原因。\n  resolution_round: 3\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed，应改为 mean±std\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v2-R2-N3\n  summary: STA 方法论新颖性有限\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: novelty 定位为 applying standard LOO。\n  resolution_round: 3\n- id: v2-R2-N2\n  summary: 单模型+单数据集泛化性不足\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: cross-scale 实验加入。单数据集限制在 Limitations 讨论。\n  resolution_round: 3\n- id: v2-R1-W3\n  summary: ISR-as-reward 控制 confound 后净效果仅 1.06×\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 15\n  resolution: ISR 定位从 training signal 转为 diagnostic-only。\n  resolution_round: 3\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review 再次将 premise-count confound 列为 critical Must-Fix（R1-N3, R2 AGREE）。尽管 ISR 已定位为 diagnostic-only，3.2×→1.06× 的发现在正文中位置仍不够突出。简单 length penalty 可达类似效果的问题未被正面回应。\"\n- id: v2-R1-W6\n  summary: Hacking taxonomy 缺乏 IAA 验证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: deterministic rules + 50-sample precision check。\n  resolution_round: 3\n- id: v2-R2-W3\n  summary: Abstract 信息密度过高\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 重写为 ~170 words。\n  resolution_round: 3\n- id: v2-R2-W4\n  summary: Premise-count confound 讨论放在 Appendix 而非正文\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 提升到正文 §3.2。\n  resolution_round: 3\n- id: v2-R2-W5\n  summary: C2 和 C4 独立性不足\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: taxonomy 独立性论证成立。\n  resolution_round: 3\n- id: v2-FMT-1\n  summary: Limitations section 位于 References 之后\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 顺序已正确。\n  resolution_round: 3\n- id: v2-FMT-2\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: ethics.tex 加入。\n  resolution_round: 3\n- id: v2-FMT-3\n  summary: Orphan bibliography entries\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: orphan entries 清除。\n  resolution_round: 3\n- id: v2-R1-M4\n  summary: Prolog cross-logic transfer 样本量过小\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 qualitative observation。\"\n  resolution_round: 3\n- id: v2-R1-W1\n  summary: 3 seeds 统计效力不足以支撑定量 claims\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 统计方法改进。定量 claims 降级。\n  resolution_round: 3\n- id: v2-R1-W4\n  summary: SFT baseline 比较因 PR 悬殊说服力有限\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 100-step RL 对照充分利用。\n  resolution_round: 3\n- id: R2-MISSING-REF\n  summary: 引用覆盖不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: 31 条引用覆盖核心领域。\n  resolution_round: 3\n- id: v3-R1-NI-2\n  summary: β=0.2 未在 Table 1 中独立报告\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: Table 1 现已包含 β=0.2 行。\n  resolution_round: 4\n- id: v3-R1-NI-3\n  summary: §4.2 cross-seed 描述暗示最终状态\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"现标注 '(at 500 steps)'。\"\n  resolution_round: 4\n- id: v3-R12-NI-4\n  summary: 全文 em-dash AI 写作痕迹\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。\n  resolution_round: 5\n- id: v3-R2-NI-5\n  summary: \"Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero...at convergence'。\"\n  resolution_round: 4\n\n# === In-progress / open issues (updated with round 16) ===\n- id: v3-R12-NI-1\n  summary: 单模型 + 3 seeds 统计效力不足——跨模型泛化性缺乏正面证据\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 16\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 两位 reviewer 一致。\n  - round: 10\n    reviewers: [1, 2]\n    note: 现已用 D129 完整 3-seed 数据重写 §4.5。\n  - round: 11\n    reviewers: [1]\n    note: \"R1-W4: 3 seeds 仍不足以作为独立 contribution 支撑。\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R1-N1 再次要求增加模型/数据集多样性。R2-N3 将 C3 cross-logic 定为 preliminary。\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 R2-W1: C3 仍在同一 dataset (FOLIO) 和 model family (Qwen3) 内。\"\n  - round: 14\n    reviewers: []\n    note: \"R14: 未直接提及。C3 已 hedge 为 'in principle...preliminary'。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: 两位 reviewer 独立将 3-seed 统计效力列为 critical Must-Fix。单模型限制也被双方列为 Should-Fix。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 fresh review: 两位 reviewer 再次独立将此列为 Must-Fix。R1-W1 指出 per-seed 方差比 condition 间差异还大；R1-W3/R2-W1 指出 LLaMA cold-start failure 暴露模型依赖性。交叉后完全一致。持续 14 轮的结构性问题，无法通过文字修改解决。\"\n- id: v4-R12-N3\n  summary: OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 16\n  mentions:\n  - round: 10\n    reviewers: [1, 2]\n    note: Table 1 和 Discussion §5 仍以 23% (uncorrected) 为 headline。\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 fix: transient window 降级为 descriptive observation。\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: Table 1 用 corrected 6%†。方向反转未在正文讨论。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: premise-count confound (3.2×→1.06×) 被列为 critical Must-Fix。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: §4.3 现以 confound 为 headline ('The headline result is negative')，R1 未再单独列为 issue，但 R2 仍指出 ISR-as-reward 的实际价值叙事被严重削弱。已正面回应但结构性限制仍在。\"\n- id: v4-R2-W9\n  summary: 方法新颖性有限：LOO 消融是标准技术，贡献主要在经验发现\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 16\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"共识: Findings 级别。\"\n  - round: 12\n    reviewers: [1, 2]\n    note: R1 Excitement 3/5, R2 2.5/5。两人均同意 Findings。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: Introduction 自我定位为 'empirical case study'。但 LOO 是标准技术。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: 两位 reviewer 均认为 STA 方法本身新颖性有限，价值在于经验发现。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: R2-W2 再次列为 Must-Fix。R1 交叉时部分 REBUT——认为 STA 贡献是三层的（组件级消融 + ISR 双重角色 + Goodhart 实证），类比 probing classifiers。分歧但不影响整体结论：方法论新颖性有限，贡献主要在经验发现层面。\"\n- id: v5-R2-N3\n  summary: \"'Diagnostic becomes optimization target' 概念新颖性有限——Goodhart's Law 直接实例\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 16\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: R2-N2 [critical]。R1 认为 empirical phenomena 有独立价值但同意 Findings。\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R2 进一步论证: ISR 的不对称性原因 'too straightforward'。\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: Gated ISR 增量改善。但概念新颖性限制仍为结构性问题。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R2 将 'meta-level Goodhart' 列为 critical Must-Fix。持续 11 轮。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: 论文已将 framing 改为 'Goodhart Effects on ISR-as-Reward'，Manheim-Garrabrant 映射已加入。两位 reviewer 不再单独列此为 weakness，但仍认为概念层面 Goodhart 发现可预期，价值在于经验细节（R1 交叉：'实证细节超出 a priori 预测'）。问题降温但未完全解决。\"\n- id: v5-R12-SFT-PR\n  summary: SFT baseline PR confound (PR=13% vs 93%)\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 16\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 fix: Abstract 加 caveat。\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R1-N1: RL-specificity claim 依赖此对比但证据基础薄弱。\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: hedging 全面改善。但 §4.2 line 42 仍用 'RL-specific' 旧措辞。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R1 列为 Should-Fix——SFT 用 gold annotations 训练引入 data quality confound。\"\n  - round: 16\n    reviewers: []\n    note: \"R16: 未被单独列为 weakness。§4.2 已加入 'SFT's high non-hacking rate may partly reflect gold annotation quality' caveat 和 100-step 对照。问题降温。\"\n- id: v6-R2-W8\n  summary: Hacking taxonomy 分类标准不够 principled——小样本验证、无 IAA、已知盲点\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 16\n  mentions:\n  - round: 11\n    reviewers: [1]\n    note: 仅 H1/H7 有 precision 验证。\n  - round: 12\n    reviewers: [1, 2]\n    note: \"Abstract 改为 'three robust modes + additional isolated observations'。\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"CE/TS/PG/CI 重命名改善可读性。分类标准仍为规则+功能分析混合。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: 50 样本验证不足，无 IAA，text-match classifier 有已知 false-negative。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: R1-W6 和 R2-W6 再次一致列为 Should-Fix。56 样本人工验证不足、无 IAA、H8 检测已知失败。交叉后完全同意。Appendix 已有 boundary case validation (20 样本) 但规模仍不足。\"\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 16\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1 Excitement 3/5, R2 2.5/5。两人均同意 Findings。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Gated ISR 增量改善。核心 novelty concern 仍为结构性限制。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R2 列为 critical Must-Fix——'anti-cheating test 被 game ≠ meta-level cheating'。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: 两位 reviewer Excitement 均为 3.0-3.5/5。R1 认为 'empirical details exceed a priori prediction'，R2 认为 'LOO 方法本身非新'。Goodhart 发现的概念可预测性仍为 Findings vs Main 的分水岭。\"\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n  - round: 11\n    reviewers: [2]\n    note: \"建议改为 'Verified but Vacuous'。\"\n  - round: 14\n    reviewers: []\n    note: \"R14: 未再提及。\"\n  - round: 15\n    reviewers: []\n    note: \"R15: 未提及。\"\n  - round: 16\n    reviewers: []\n    note: \"R16: 未提及。连续 3 轮未被任何 reviewer 提及，可能已不再是活跃问题。\"\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例 (96.7% non-hacking)\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Discussion 只提 '2/3 seeds migrate to PG'，忽略 s54。有选择性呈现嫌疑。\"\n  - round: 16\n    reviewers: []\n    note: \"R16: 未提及。Gated ISR 未在本轮论文中出现（可能已移除或改写）。\"\n- id: v14-R1-LIMITATIONS\n  summary: Limitations section 压缩至 6-7 行\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1]\n    note: 8 页限制下可理解，但 Limitations 不再是亮点。\n  - round: 16\n    reviewers: []\n    note: \"R16: Limitations 现已扩展至含 Data scale 段落，内容充实。未被列为问题。\"\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果未充分解释 + O(1) vs O(n) 一致性未量化\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15: 未直接提及。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: R1-W8 列为 Should-Fix——O(1) vs O(n) 相关系数/MAE 未报告。R2 交叉 AGREE。§3.3/Appendix E.3 讨论了 O(1) 为何产生 near-zero ISR，但缺乏定量一致性比较。\"\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高（~17 个缩写）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"~18 缩写，CE/TS/PG/CI 重命名改善可读性。\"\n  - round: 15\n    reviewers: []\n    note: \"R15: 未提及。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: R2-W5 再次列为 Should-Fix。Abstract ~200 词内 8+ 缩写。H1→CE/H7→TS 双重编号增加认知负担。R1 交叉轻度同意，建议 Abstract 仅保留 STA/ISR。\"\n\n# === New issues from Round 16 ===\n- id: v16-R1-W2\n  summary: LOO 独立性假设未讨论——premise 间交互效应（联合必要但单独非必要）可能系统性偏置 ISR\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 列为 Must-Fix，R2 交叉完全 AGREE 并补充论据（FOL 中 A∧B→C 场景；Jia & Harman 2011 已讨论 higher-order mutants 局限性）。Algorithm 1 假设 premise 独立可消融，但未讨论此假设何时失败及其对 ISR 的偏差方向。\"\n  action_items:\n  - round: 16\n    action: \"在 Limitations 或 §3.2 讨论 LOO 独立性假设及其偏差方向；报告至少一个条件的 LOO vs pairwise 消融比较\"\n    assigned_to: paper_agent\n    status: open\n- id: v16-R1-W4\n  summary: ISR-as-reward 的 Goodhart 分析存在乘法耦合混淆——无法分离 ISR gaming vs exec reward 放大\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 列为 Should-Fix，要求 ISR-only 消融条件。R2 部分 REBUT：(1) exec-only baseline 已证明纯 exec reward 下也退化；(2) hacking 模式分布质变（H7 从 0%→71%）不能仅用 exec amplification 解释；(3) ISR-only 条件概念上病态。分歧但 R2 同意需更系统的 β 分析。\"\n  action_items:\n  - round: 16\n    action: \"在 §4.3 补充不同 β 值下 hacking 模式分布变化的系统分析；讨论乘法耦合的局限性\"\n    assigned_to: paper_agent\n    status: open\n- id: v16-R1-W5\n  summary: ProofFOL 数据集构建缺关键细节——GPT-4o 翻译过滤率、人工抽检准确率、逻辑复杂度分布均未报告\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 列为 Should-Fix。R2 交叉 AGREE 并补充：§4.4 'simpler predicates' 表述说明数据集特性可能混淆跨域泛化 claims。\"\n  action_items:\n  - round: 16\n    action: \"在 §4.1 或 Appendix 补充 ProofFOL 构建流水线细节：初始样本量、过滤率、人工抽检结果、复杂度分布\"\n    assigned_to: paper_agent\n    status: open\n- id: v16-R2-W3\n  summary: 缺少缓解方案 (mitigation) 讨论，削弱实际影响力\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2 列为 Should-Fix。R1 部分 REBUT——ISR-as-reward 的 negative result 本身有价值，§5 已暗示 reward normalization/premise-count control 方向。但两人均同意应在 Discussion 展开 2-3 个缓解方向的可行性讨论。§5 当前仅 7 行，过于简短。\"\n  action_items:\n  - round: 16\n    action: \"在 §5 Discussion 展开缓解方向讨论（multi-granularity ablation, reward ensembling, ISR-as-filter, constrained optimization）\"\n    assigned_to: paper_agent\n    status: open\n- id: v16-R2-W4\n  summary: 与 Kim et al. (2026) 差异化论述不充分——共享 FOLIO 数据集使直接对比成为可能\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2 列为 Should-Fix，R1 交叉 AGREE（与 R1-Q5 一致）。当前 Related Work 仅一句话提及。需展开三维度对比：(1) inference-time vs training-time gaming；(2) unified pipeline vs GRPO training；(3) FOLIO 上的互补性。\"\n  action_items:\n  - round: 16\n    action: \"在 Related Work 增加 2-3 句 Kim et al. (2026) 详细对比\"\n    assigned_to: paper_agent\n    status: open\n- id: v16-MR\n  summary: 缺少若干相关引用——Ng et al. (1999) reward shaping、Sullivan et al. GRPO-as-PRM、reasoning effort hacking detection\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 推荐 Ng et al. (1999) reward shaping 经典理论。R2 推荐 Sullivan et al. 'GRPO is Secretly a PRM'、'Is It Thinking or Cheating?' (arXiv:2510.01367)。部分为 2025-2026 concurrent work。R1 的 Katz Reluplex 建议被 R2 REBUT（关联弱）。\"\n\n# === Resolved issues from rounds 15 ===\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——每个 seed 走向质性不同的 hacking 路径\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"§4.1 新增 'Statistical considerations' 段，per-seed qualitative 为主框架\"\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'；Manheim-Garrabrant 映射已加入\"\n  resolution_round: 15\n- id: v15-R1-N3\n  summary: ISR syntactic-only 性质与 structural quality framing gap\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'structural integrity' → 'component necessity' 全文替换；82 例验证\"\n  resolution_round: 15\n- id: v15-R1-N4\n  summary: Premise-count confound 控制后 ISR-as-reward 优势消失\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"§4.3 开头段直接以 confound 为 headline\"\n  resolution_round: 15\n- id: v15-R2-W1\n  summary: 缺少 2025-2026 关键相关工作\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Helff et al. (2026)、Khalifa et al. (2026)、Uesato (2022)、Cobbe (2021) 已加入\"\n  resolution_round: 15\n- id: v15-R1-W2\n  summary: Multiple testing correction 缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Appendix 新增 'Multiple testing correction' 段，Bonferroni k=14\"\n  resolution_round: 15\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v12-R2-W4\n  summary: Table 1 ISR β=0.1 ISR* 列缺失\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 1 补全。\n  resolution_round: 12\n- id: v12-R2-W2\n  summary: 与 Kim et al. (2026) 区分需更锐利\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"Related Work 新增完整 'Faithfulness in formalization' 段落。\"\n  resolution_round: 14\n- id: v12-R1-W2\n  summary: Component-count confound deconfounding analysis 仅在 Appendix\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  resolution: \"§4.3 开头段以 confound 为 headline finding\"\n  resolution_round: 15\n- id: v13-R2-N2\n  summary: 与 Kim et al. (2026) 差异化不充分\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Related Work 新增完整对比段落。\"\n  resolution_round: 14\n- id: v13-R1-W1\n  summary: \"ISR 与 NLI accuracy 无关但 'structural quality diagnostic' 定位可能误导\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Method §3.2: 'ISR is a component-necessity diagnostic, not a reasoning-quality metric'。\"\n  resolution_round: 14\n- id: v13-R2-W5\n  summary: Table 2 混合 single-seed 和 pooled 数据\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Table 2 caption 标注聚合方式。\"\n  resolution_round: 14\n- id: v13-R2-MITIGATION\n  summary: Discussion 缺少 mitigation 策略讨论\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: Discussion 含 gated ISR + reward ensembling + constrained optimization + TRACE。\n  resolution_round: 14\n- id: v13-R1-Q4\n  summary: Prolog cross-logic 实验缺少 random control\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"§4.3: 'No matched random control was run for Prolog' 显式声明。\"\n  resolution_round: 14\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Discussion 只提 '2/3 seeds migrate to PG'，忽略 s54。\"\n  - round: 16\n    reviewers: []\n    note: \"R16: 未提及。\"\n- id: v8-R1-N3\n  summary: 术语交替使用导致语义滑移\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14\n  resolution: H1→CE, H7→TS, H8→PG, H9→CI 全文重命名完整一致。\n  resolution_round: 14\n- id: v8-R12-N2\n  summary: 实验范围与标题/claim scope 不匹配\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14\n  resolution: \"C3 加 'in principle...preliminary'。Hedging 充分。\"\n  resolution_round: 14\n- id: v8-R1-W4\n  summary: 多重比较未校正\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 15\n  resolution: \"Bonferroni k=14 校正已完成。\"\n  resolution_round: 15\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation p=0.26 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n# === Resolved issues from rounds 0-14 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: RV-D060-NARRATIVE\n  summary: D060 'Goodhart instability' 叙事确认成立\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\n  resolution_round: 2\n- id: RV-FIG2-STALE-SCRIPT\n  summary: figures/paper/gen_fig2.py 旧脚本数据错误\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 已修复。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review 再次提出 ISR syntactic-only gap（R1-N2/N3, R2-W5）。'structural integrity' 措辞仍暗示比 'component necessity' 更强的保证。尽管已修正术语，framing gap 在 Abstract/Introduction 仍可感知。\"\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R1-W4\n  summary: Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: exec-only 500-step 主表仅报告 s42（†标注）。\n  resolution_round: 2\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review 再次指出 seed 43 eval protocol 不一致（R1-W5, R2 AGREE）。1/3 seeds 不同解码策略影响 cross-seed 比较。\"\n- id: R1-W3\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: R2-W7\n  summary: 与 Kim et al. (2026) 差异化不充分\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: related_work.tex 中有区分段落。\n  resolution_round: 2\n- id: R1-W6\n  summary: 训练 500 例/评估 100 例的规模限制讨论不充分\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: limitations.tex 已讨论。\n  resolution_round: 2\n- id: R1-W7\n  summary: H1/H7 classifier precision/recall 未报告\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: 50 样本人工验证 precision >95%。\n  resolution_round: 2\n- id: R1-W8\n  summary: Random control U(0,1) 与 ISR 的 skewed 分布不匹配\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: method.tex 和 experiments.tex 均说明了 Random 设计目的。\n  resolution_round: 2\n- id: R1-W9\n  summary: 缺代码/数据开源承诺\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n- id: R1-W5\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: framing 降级为 empirical instance。\n  resolution_round: 3\n- id: R2-W8\n  summary: H1/H7 编号不连贯（H2-H6 不存在）\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: method.tex 解释了合并原因。\n  resolution_round: 3\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed，应改为 mean±std\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v2-R2-N3\n  summary: STA 方法论新颖性有限\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: novelty 定位为 applying standard LOO。\n  resolution_round: 3\n- id: v2-R2-N2\n  summary: 单模型+单数据集泛化性不足\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: cross-scale 实验加入。单数据集限制在 Limitations 讨论。\n  resolution_round: 3\n- id: v2-R1-W3\n  summary: ISR-as-reward 控制 confound 后净效果仅 1.06×\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 15\n  resolution: ISR 定位从 training signal 转为 diagnostic-only。\n  resolution_round: 3\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review 再次将 premise-count confound 列为 critical Must-Fix（R1-N3, R2 AGREE）。尽管 ISR 已定位为 diagnostic-only，3.2×→1.06× 的发现在正文中位置仍不够突出。简单 length penalty 可达类似效果的问题未被正面回应。\"\n- id: v2-R1-W6\n  summary: Hacking taxonomy 缺乏 IAA 验证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: deterministic rules + 50-sample precision check。\n  resolution_round: 3\n- id: v2-R2-W3\n  summary: Abstract 信息密度过高\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 重写为 ~170 words。\n  resolution_round: 3\n- id: v2-R2-W4\n  summary: Premise-count confound 讨论放在 Appendix 而非正文\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 提升到正文 §3.2。\n  resolution_round: 3\n- id: v2-R2-W5\n  summary: C2 和 C4 独立性不足\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: taxonomy 独立性论证成立。\n  resolution_round: 3\n- id: v2-FMT-1\n  summary: Limitations section 位于 References 之后\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 顺序已正确。\n  resolution_round: 3\n- id: v2-FMT-2\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: ethics.tex 加入。\n  resolution_round: 3\n- id: v2-FMT-3\n  summary: Orphan bibliography entries\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: orphan entries 清除。\n  resolution_round: 3\n- id: v2-R1-M4\n  summary: Prolog cross-logic transfer 样本量过小\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 qualitative observation。\"\n  resolution_round: 3\n- id: v2-R1-W1\n  summary: 3 seeds 统计效力不足以支撑定量 claims\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 统计方法改进。定量 claims 降级。\n  resolution_round: 3\n- id: v2-R1-W4\n  summary: SFT baseline 比较因 PR 悬殊说服力有限\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 100-step RL 对照充分利用。\n  resolution_round: 3\n- id: R2-MISSING-REF\n  summary: 引用覆盖不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: 31 条引用覆盖核心领域。\n  resolution_round: 3\n- id: v3-R1-NI-2\n  summary: β=0.2 未在 Table 1 中独立报告\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: Table 1 现已包含 β=0.2 行。\n  resolution_round: 4\n- id: v3-R1-NI-3\n  summary: §4.2 cross-seed 描述暗示最终状态\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"现标注 '(at 500 steps)'。\"\n  resolution_round: 4\n- id: v3-R12-NI-4\n  summary: 全文 em-dash AI 写作痕迹\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。\n  resolution_round: 5\n- id: v3-R2-NI-5\n  summary: \"Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero...at convergence'。\"\n  resolution_round: 4\n\n# === In-progress / open issues (updated with round 16) ===\n- id: v3-R12-NI-1\n  summary: 单模型 + 3 seeds 统计效力不足——跨模型泛化性缺乏正面证据\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 16\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 两位 reviewer 一致。\n  - round: 10\n    reviewers: [1, 2]\n    note: 现已用 D129 完整 3-seed 数据重写 §4.5。\n  - round: 11\n    reviewers: [1]\n    note: \"R1-W4: 3 seeds 仍不足以作为独立 contribution 支撑。\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R1-N1 再次要求增加模型/数据集多样性。R2-N3 将 C3 cross-logic 定为 preliminary。\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 R2-W1: C3 仍在同一 dataset (FOLIO) 和 model family (Qwen3) 内。\"\n  - round: 14\n    reviewers: []\n    note: \"R14: 未直接提及。C3 已 hedge 为 'in principle...preliminary'。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review: 两位 reviewer 独立将 3-seed 统计效力列为 critical Must-Fix。单模型限制也被双方列为 Should-Fix。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 fresh review: 两位 reviewer 再次独立将此列为 Must-Fix。R1-W1 指出 per-seed 方差比 condition 间差异还大；R1-W3/R2-W1 指出 LLaMA cold-start failure 暴露模型依赖性。交叉后完全一致。持续 14 轮的结构性问题，无法通过文字修改解决。\"\n- id: v4-R12-N3\n  summary: OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 16\n  mentions:\n  - round: 10\n    reviewers: [1, 2]\n    note: Table 1 和 Discussion §5 仍以 23% (uncorrected) 为 headline。\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 fix: transient window 降级为 descriptive observation。\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: Table 1 用 corrected 6%†。方向反转未在正文讨论。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: premise-count confound (3.2×→1.06×) 被列为 critical Must-Fix。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: §4.3 现以 confound 为 headline ('The headline result is negative')，R1 未再单独列为 issue，但 R2 仍指出 ISR-as-reward 的实际价值叙事被严重削弱。已正面回应但结构性限制仍在。\"\n- id: v4-R2-W9\n  summary: 方法新颖性有限：LOO 消融是标准技术，贡献主要在经验发现\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 16\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"共识: Findings 级别。\"\n  - round: 12\n    reviewers: [1, 2]\n    note: R1 Excitement 3/5, R2 2.5/5。两人均同意 Findings。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: Introduction 自我定位为 'empirical case study'。但 LOO 是标准技术。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: 两位 reviewer 均认为 STA 方法本身新颖性有限，价值在于经验发现。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: R2-W2 再次列为 Must-Fix。R1 交叉时部分 REBUT——认为 STA 贡献是三层的（组件级消融 + ISR 双重角色 + Goodhart 实证），类比 probing classifiers。分歧但不影响整体结论：方法论新颖性有限，贡献主要在经验发现层面。\"\n- id: v5-R2-N3\n  summary: \"'Diagnostic becomes optimization target' 概念新颖性有限——Goodhart's Law 直接实例\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 16\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: R2-N2 [critical]。R1 认为 empirical phenomena 有独立价值但同意 Findings。\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R2 进一步论证: ISR 的不对称性原因 'too straightforward'。\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: Gated ISR 增量改善。但概念新颖性限制仍为结构性问题。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R2 将 'meta-level Goodhart' 列为 critical Must-Fix。持续 11 轮。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: 论文已将 framing 改为 'Goodhart Effects on ISR-as-Reward'，Manheim-Garrabrant 映射已加入。两位 reviewer 不再单独列此为 weakness，但仍认为概念层面 Goodhart 发现可预期，价值在于经验细节（R1 交叉：'实证细节超出 a priori 预测'）。问题降温但未完全解决。\"\n- id: v5-R12-SFT-PR\n  summary: SFT baseline PR confound (PR=13% vs 93%)\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 16\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 fix: Abstract 加 caveat。\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R1-N1: RL-specificity claim 依赖此对比但证据基础薄弱。\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: hedging 全面改善。但 §4.2 line 42 仍用 'RL-specific' 旧措辞。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R1 列为 Should-Fix——SFT 用 gold annotations 训练引入 data quality confound。\"\n  - round: 16\n    reviewers: []\n    note: \"R16: 未被单独列为 weakness。§4.2 已加入 'SFT's high non-hacking rate may partly reflect gold annotation quality' caveat 和 100-step 对照。问题降温。\"\n- id: v6-R2-W8\n  summary: Hacking taxonomy 分类标准不够 principled——小样本验证、无 IAA、已知盲点\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 16\n  mentions:\n  - round: 11\n    reviewers: [1]\n    note: 仅 H1/H7 有 precision 验证。\n  - round: 12\n    reviewers: [1, 2]\n    note: \"Abstract 改为 'three robust modes + additional isolated observations'。\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"CE/TS/PG/CI 重命名改善可读性。分类标准仍为规则+功能分析混合。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: 50 样本验证不足，无 IAA，text-match classifier 有已知 false-negative。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: R1-W6 和 R2-W6 再次一致列为 Should-Fix。56 样本人工验证不足、无 IAA、H8 检测已知失败。交叉后完全同意。Appendix 已有 boundary case validation (20 样本) 但规模仍不足。\"\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 16\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1 Excitement 3/5, R2 2.5/5。两人均同意 Findings。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Gated ISR 增量改善。核心 novelty concern 仍为结构性限制。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R2 列为 critical Must-Fix——'anti-cheating test 被 game ≠ meta-level cheating'。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: 两位 reviewer Excitement 均为 3.0-3.5/5。R1 认为 'empirical details exceed a priori prediction'，R2 认为 'LOO 方法本身非新'。Goodhart 发现的概念可预测性仍为 Findings vs Main 的分水岭。\"\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n  - round: 11\n    reviewers: [2]\n    note: \"建议改为 'Verified but Vacuous'。\"\n  - round: 14\n    reviewers: []\n    note: \"R14: 未再提及。\"\n  - round: 15\n    reviewers: []\n    note: \"R15: 未提及。\"\n  - round: 16\n    reviewers: []\n    note: \"R16: 未提及。连续 3 轮未被任何 reviewer 提及，可能已不再是活跃问题。\"\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例 (96.7% non-hacking)\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Discussion 只提 '2/3 seeds migrate to PG'，忽略 s54。有选择性呈现嫌疑。\"\n  - round: 16\n    reviewers: []\n    note: \"R16: 未提及。Gated ISR 未在本轮论文中出现（可能已移除或改写）。\"\n- id: v14-R1-LIMITATIONS\n  summary: Limitations section 压缩至 6-7 行\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1]\n    note: 8 页限制下可理解，但 Limitations 不再是亮点。\n  - round: 16\n    reviewers: []\n    note: \"R16: Limitations 现已扩展至含 Data scale 段落，内容充实。未被列为问题。\"\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果未充分解释 + O(1) vs O(n) 一致性未量化\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15: 未直接提及。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: R1-W8 列为 Should-Fix——O(1) vs O(n) 相关系数/MAE 未报告。R2 交叉 AGREE。§3.3/Appendix E.3 讨论了 O(1) 为何产生 near-zero ISR，但缺乏定量一致性比较。\"\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高（~17 个缩写）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"~18 缩写，CE/TS/PG/CI 重命名改善可读性。\"\n  - round: 15\n    reviewers: []\n    note: \"R15: 未提及。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: R2-W5 再次列为 Should-Fix。Abstract ~200 词内 8+ 缩写。H1→CE/H7→TS 双重编号增加认知负担。R1 交叉轻度同意，建议 Abstract 仅保留 STA/ISR。\"\n\n# === New issues from Round 16 ===\n- id: v16-R1-W2\n  summary: LOO 独立性假设未讨论——premise 间交互效应（联合必要但单独非必要）可能系统性偏置 ISR\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 列为 Must-Fix，R2 交叉完全 AGREE 并补充论据（FOL 中 A∧B→C 场景；Jia & Harman 2011 已讨论 higher-order mutants 局限性）。Algorithm 1 假设 premise 独立可消融，但未讨论此假设何时失败及其对 ISR 的偏差方向。\"\n  action_items:\n  - round: 16\n    action: \"在 Limitations 或 §3.2 讨论 LOO 独立性假设及其偏差方向；报告至少一个条件的 LOO vs pairwise 消融比较\"\n    assigned_to: paper_agent\n    status: open\n- id: v16-R1-W4\n  summary: ISR-as-reward 的 Goodhart 分析存在乘法耦合混淆——无法分离 ISR gaming vs exec reward 放大\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 列为 Should-Fix，要求 ISR-only 消融条件。R2 部分 REBUT：(1) exec-only baseline 已证明纯 exec reward 下也退化；(2) hacking 模式分布质变（H7 从 0%→71%）不能仅用 exec amplification 解释；(3) ISR-only 条件概念上病态。分歧但 R2 同意需更系统的 β 分析。\"\n  action_items:\n  - round: 16\n    action: \"在 §4.3 补充不同 β 值下 hacking 模式分布变化的系统分析；讨论乘法耦合的局限性\"\n    assigned_to: paper_agent\n    status: open\n- id: v16-R1-W5\n  summary: ProofFOL 数据集构建缺关键细节——GPT-4o 翻译过滤率、人工抽检准确率、逻辑复杂度分布均未报告\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 列为 Should-Fix。R2 交叉 AGREE 并补充：§4.4 'simpler predicates' 表述说明数据集特性可能混淆跨域泛化 claims。\"\n  action_items:\n  - round: 16\n    action: \"在 §4.1 或 Appendix 补充 ProofFOL 构建流水线细节：初始样本量、过滤率、人工抽检结果、复杂度分布\"\n    assigned_to: paper_agent\n    status: open\n- id: v16-R2-W3\n  summary: 缺少缓解方案 (mitigation) 讨论，削弱实际影响力\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2 列为 Should-Fix。R1 部分 REBUT——ISR-as-reward 的 negative result 本身有价值，§5 已暗示 reward normalization/premise-count control 方向。但两人均同意应在 Discussion 展开 2-3 个缓解方向的可行性讨论。§5 当前仅 7 行，过于简短。\"\n  action_items:\n  - round: 16\n    action: \"在 §5 Discussion 展开缓解方向讨论（multi-granularity ablation, reward ensembling, ISR-as-filter, constrained optimization）\"\n    assigned_to: paper_agent\n    status: open\n- id: v16-R2-W4\n  summary: 与 Kim et al. (2026) 差异化论述不充分——共享 FOLIO 数据集使直接对比成为可能\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2 列为 Should-Fix，R1 交叉 AGREE（与 R1-Q5 一致）。当前 Related Work 仅一句话提及。需展开三维度对比：(1) inference-time vs training-time gaming；(2) unified pipeline vs GRPO training；(3) FOLIO 上的互补性。\"\n  action_items:\n  - round: 16\n    action: \"在 Related Work 增加 2-3 句 Kim et al. (2026) 详细对比\"\n    assigned_to: paper_agent\n    status: open\n- id: v16-MR\n  summary: 缺少若干相关引用——Ng et al. (1999) reward shaping、Sullivan et al. GRPO-as-PRM、reasoning effort hacking detection\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 推荐 Ng et al. (1999) reward shaping 经典理论。R2 推荐 Sullivan et al. 'GRPO is Secretly a PRM'、'Is It Thinking or Cheating?' (arXiv:2510.01367)。部分为 2025-2026 concurrent work。R1 的 Katz Reluplex 建议被 R2 REBUT（关联弱）。\"\n\n# === Resolved issues from rounds 15 ===\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——每个 seed 走向质性不同的 hacking 路径\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"§4.1 新增 'Statistical considerations' 段，per-seed qualitative 为主框架\"\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'；Manheim-Garrabrant 映射已加入\"\n  resolution_round: 15\n- id: v15-R1-N3\n  summary: ISR syntactic-only 性质与 structural quality framing gap\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'structural integrity' → 'component necessity' 全文替换；82 例验证\"\n  resolution_round: 15\n- id: v15-R1-N4\n  summary: Premise-count confound 控制后 ISR-as-reward 优势消失\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"§4.3 开头段直接以 confound 为 headline\"\n  resolution_round: 15\n- id: v15-R2-W1\n  summary: 缺少 2025-2026 关键相关工作\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Helff et al. (2026)、Khalifa et al. (2026)、Uesato (2022)、Cobbe (2021) 已加入\"\n  resolution_round: 15\n- id: v15-R1-W2\n  summary: Multiple testing correction 缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Appendix 新增 'Multiple testing correction' 段，Bonferroni k=14\"\n  resolution_round: 15\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v12-R2-W4\n  summary: Table 1 ISR β=0.1 ISR* 列缺失\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 1 补全。\n  resolution_round: 12\n- id: v12-R2-W2\n  summary: 与 Kim et al. (2026) 区分需更锐利\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"Related Work 新增完整 'Faithfulness in formalization' 段落。\"\n  resolution_round: 14\n- id: v12-R1-W2\n  summary: Component-count confound deconfounding analysis 仅在 Appendix\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  resolution: \"§4.3 开头段以 confound 为 headline finding\"\n  resolution_round: 15\n- id: v13-R2-N2\n  summary: 与 Kim et al. (2026) 差异化不充分\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Related Work 新增完整对比段落。\"\n  resolution_round: 14\n- id: v13-R1-W1\n  summary: \"ISR 与 NLI accuracy 无关但 'structural quality diagnostic' 定位可能误导\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Method §3.2: 'ISR is a component-necessity diagnostic, not a reasoning-quality metric'。\"\n  resolution_round: 14\n- id: v13-R2-W5\n  summary: Table 2 混合 single-seed 和 pooled 数据\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Table 2 caption 标注聚合方式。\"\n  resolution_round: 14\n- id: v13-R2-MITIGATION\n  summary: Discussion 缺少 mitigation 策略讨论\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: Discussion 含 gated ISR + reward ensembling + constrained optimization + TRACE。\n  resolution_round: 14\n- id: v13-R1-Q4\n  summary: Prolog cross-logic 实验缺少 random control\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"§4.3: 'No matched random control was run for Prolog' 显式声明。\"\n  resolution_round: 14\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Discussion 只提 '2/3 seeds migrate to PG'，忽略 s54。\"\n  - round: 16\n    reviewers: []\n    note: \"R16: 未提及。\"\n- id: v8-R1-N3\n  summary: 术语交替使用导致语义滑移\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14\n  resolution: H1→CE, H7→TS, H8→PG, H9→CI 全文重命名完整一致。\n  resolution_round: 14\n- id: v8-R12-N2\n  summary: 实验范围与标题/claim scope 不匹配\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14\n  resolution: \"C3 加 'in principle...preliminary'。Hedging 充分。\"\n  resolution_round: 14\n- id: v8-R1-W4\n  summary: 多重比较未校正\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 15\n  resolution: \"Bonferroni k=14 校正已完成。\"\n  resolution_round: 15\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation p=0.26 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n"
  }
}
```

</details>

---


### Tool result

_source line 1551 · 2026-05-20T05:38:22.124519+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 25843}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 363
}
```

</details>

---


### Tool call

_source line 1552 · 2026-05-20T05:40:49.406094+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "solver-trace-ablation",
  "report": "# 审稿报告 — Round 16 (Fresh Review)\n\n**论文**: \"Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewers**: R1（方法严谨性 + 实验设计 + 统计分析）、R2（新颖性 + 写作 + 格式）\n**日期**: 2026-05-20\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，将 LOO 变异测试迁移到 GRPO 训练的神经符号推理器诊断场景，定义 Intensional Structural Reward (ISR) 指标。在 6 种奖励条件 × 2 逻辑类型 × 2 数据集 × 3 seeds 上训练 Qwen3-4B，发现：(1) exec-only GRPO 下 ISR 99.5% 崩溃（PR 上升同时），(2) ISR-as-reward 触发 Goodhart 效应（H7 放大 ~5×），(3) 归纳 8 种 reward hacking 模式。核心结论：ISR 作为诊断可靠，作为优化目标则 dataset-dependent（FOLIO 上 Goodhart collapse，ProofFOL 上 beneficial instability）。\n\n---\n\n## Strengths\n\n**S1. 跨学科方法论迁移有创意** [R1-S1, R2-S1 共识]\n将变异测试（mutation testing）的 LOO 范式迁移到 GRPO 训练的 solver 输出诊断，填补了 neurosymbolic RL 中 structural diagnostic 的空白。ISR 定义简洁（Eq. 1, Algorithm 1），语义清晰。\n\n**S2. 实验控制严谨** [R1-S3/S4, R2-S2 共识]\n6 条件 × 3 seeds × 2 数据集家族 + SFT baseline + exec-only 控制组。Random reward 条件有效分离 ISR-specific 信号与 generic reward-variance 效应。SFT 分离了 RL 引入的退化 vs. 预训练能力不足。Fisher exact test + Bonferroni 校正（k=14，Appendix）规范。\n\n**S3. \"诊断变为目标\" 的 Goodhart 发现有社区价值** [R1-S1, R2-S3 共识]\nISR 作为诊断时可靠（§4.2: 99.5% 崩溃被检测），但作为奖励时被 game（§4.3: H7 ~5× 放大）——这一对比清晰映射到 Manheim-Garrabrant 分类学（regressional on FOLIO, extremal at high β），为 neurosymbolic RL 社区提供实证警示。\n\n**S4. Hacking 分类学系统完整** [R1-S2, R2-S4 共识]\n8 种模式有操作定义 + FOL/Prolog 示例 + ISR 交互分析 + 出现频率统计（Table 2, Appendix D）。H7b（obfuscated tautology: triple gaming of exec reward + ISR + text-match classifier）和 query-as-fact gaming（Prolog-specific）超出简单直觉。\n\n**S5. 跨域验证增强可信度** [R1-S3, R2-S5 共识]\nFOL/Prolog 跨逻辑 + FOLIO/ProofFOL 跨数据集交叉验证。ProofFOL 上 beneficial instability（76.8% vs. 17.4% genuine, p=0.10）与 FOLIO 上 Goodhart collapse 的对比揭示了 ISR 的 dataset-dependent 不对称性。\n\n**S6. 透明度高** [R1-S5]\nPer-seed 附录数据（Tables 6-9）、Bonferroni 校正细节、hacking classifier validation（50 样本 precision + 20 boundary cases）、O(1) vs O(n) 消融比较均完整呈现。\n\n---\n\n## Weaknesses\n\n### Must-Fix\n\n**W1. 单模型 + 3 seeds：泛化性和统计效力双重不足** [R1-W1+W3, R2-W1; 共识]\n所有实验仅在 Qwen3-4B 上完成。LLaMA-3.2-3B 冷启动失败（Appendix E.4）不构成第二模型验证，反而暴露结果的模型依赖性。3 seeds 下 per-seed 方差极大（ISR β=0.1: s42 non-hacking=17.3%, s43=0%, s44=0%；Table 6），cross-seed 差异大于 cross-condition 差异。ProofFOL genuine-rate permutation test p=0.10 明确欠效力。论文标题 \"GRPO-Trained Neurosymbolic Reasoning\" 暗示普遍性但仅一个 4B 模型有正面证据。\n- **建议**: (a) 至少增加一个 7B+ 或不同架构模型的关键实验复现；(b) 增至 5+ seeds；(c) 若资源不允许，在标题和 abstract 明确限定 claims 适用范围（如 \"in Qwen3-4B\"），降级为 case study。\n\n**W2. LOO 独立性假设未讨论** [R1-W2; R2 交叉 AGREE]\nAlgorithm 1 逐一移除 premise，假设组件独立消融，但未讨论 premise 间交互效应——如两个 premise 联合必要但各自单独非必要（FOL 中常见：A∧B→C）。此偏差可能导致 ISR 系统性偏高。变异测试文献中 higher-order mutants 的研究（Jia & Harman, 2011）已讨论此局限性，论文应引用并讨论偏差方向。\n- **建议**: (a) 在 Limitations 或 §3.2 明确讨论 LOO 独立性假设及失败场景；(b) 报告至少一个条件的 LOO vs. pairwise 消融比较。\n\n### Should-Fix\n\n**W3. Hacking 分类器验证不充分** [R1-W6, R2-W6; 共识]\n56 个手动验证样本（H1/H7 仅），无 inter-annotator agreement，H8 检测已知失败（Appendix D.1）。Text-match classifier 有已知 false-negative（Prolog: strict classifier 100% non-hacking → functional analysis 95/97 tautological）。分类学基于 post-hoc pattern matching，可能有确认偏差。\n- **建议**: (a) 扩大验证样本至 100+；(b) 报告 Cohen's κ（至少两人标注）；(c) 将分类学定位为 \"exploratory taxonomy\"。\n\n**W4. 方法论新颖性有限** [R2-W2; R1 部分 REBUT]\nSTA 核心操作是标准 LOO 消融。R1 认为 STA 贡献是三层的（组件级消融 + ISR 双重角色 + Goodhart 实证），类比 probing classifiers 定义新分析范式。R2 认为技术门槛不高。**分歧**：R1 倾向方法论有增量新颖性，R2 认为有限。共识：价值主要在经验发现而非方法本身。\n- **建议**: 重新 frame C1 为 \"新诊断框架\" 而非 \"新消融方法\"，强调框架整体（ISR + taxonomy + cross-domain protocol）的贡献。\n\n**W5. 缺少缓解方案 (mitigation) 讨论** [R2-W3; R1 部分 REBUT]\n§5 Discussion 仅 7 行。R1 指出 ISR-as-reward 的 negative result 本身有价值，§5 已暗示方向；R2 认为与 Helff et al. (2026) 和 Khalifa et al. (2026) 等同期工作相比缺乏前瞻性。\n- **建议**: 在 Discussion 展开 2-3 个缓解方向（multi-granularity ablation, ISR-as-filter, reward ensembling, constrained optimization），即使不做实验也增加前瞻性。\n\n**W6. 与 Kim et al. (2026) 差异化不充分** [R2-W4, R1-Q5; 共识]\nKim et al. (2026) 研究 inference-time formalization gaming（GPT-5/DeepSeek-R1 + Lean 4 + FOLIO），本文研究 training-time structural degeneration。两者共享 FOLIO 数据集，但 Related Work 仅一句话提及，缺少三维度对比（scope, mechanism, FOLIO 互补性）。\n- **建议**: 在 Related Work 增加 2-3 句详细对比。\n\n**W7. ProofFOL 数据集构建缺关键细节** [R1-W5; R2 AGREE]\n§4.1 仅说 \"translated via GPT-4o, ~70% retention\"。缺失：初始样本量、过滤标准、人工抽检准确率、逻辑复杂度分布。§4.4 \"simpler predicates\" 表述暗示数据集简单性可能混淆跨域泛化 claims。\n- **建议**: 在 §4.1 或 Appendix 补充 ProofFOL 构建流水线完整细节。\n\n**W8. O(1) vs. O(n) ISR 一致性未量化** [R1-W8; R2 AGREE]\n§3.3/Appendix E.3 讨论了 O(1) 为何产生 near-zero ISR，但缺乏定量一致性比较（相关系数或 MAE）。\n- **建议**: 用现有 held-out 数据报告 O(1) vs. O(n) ISR 值一致性。\n\n**W9. 缩写密度过高** [R2-W5; R1 轻度 AGREE]\nAbstract ~200 词内引入 STA, ISR, LOO, SFT, PR, FOLIO, ProofFOL, NLI 等 8+ 缩写。H1/H7/H8 和 CE/TS/PG/CI 双重编号增加认知负担。\n- **建议**: Abstract 仅保留 STA/ISR 缩写；hacking 模式统一使用一套编号。\n\n### Minor\n\n**W10. Figure 2 x 轴不均匀** [R1-W9; R2 AGREE]\n0, 100, 500, 1000 步间距不等但视觉等距。建议 log-scale 或标注断点。\n\n**W11. CMH test 统计量不完整** [R2-W9; R1-W7 相关]\nCMH test 被提及但未报告详细统计量（仅说 \"borderline\"）。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n1. **单模型 + 3 seeds 不足** — 最关键的结构性限制，无法通过文字修改解决\n2. **LOO 独立性假设未讨论** — 方法论盲点\n3. **Hacking 分类器验证不足** — 56 样本、无 IAA\n4. **Kim et al. (2026) 对比不充分** — 共享 FOLIO 数据集使对比成为可能\n5. **ProofFOL 构建细节缺失** — 影响跨域泛化 claim 可信度\n6. **缩写密度过高** — 影响可读性\n7. **O(1) vs. O(n) 未量化** — 可用现有数据轻松回答\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 判断 |\n|------|------|------|------|\n| ISR-reward 混淆 (R1-W4) | Must-Fix: 需 ISR-only 消融 | REBUT: 现有设计已部分分离；ISR-only 概念病态 | R2 论据更有说服力——hacking 模式质变（H7 0%→71%）不能仅用 exec amplification 解释。降为 Should-Fix。 |\n| 方法论新颖性 (R2-W2) | REBUT: 三层贡献，类比 probing | Must-Fix: LOO 是标准技术 | 分歧但不影响结论——共识为 Findings 级别。 |\n| 缓解方案 (R2-W3) | REBUT: negative result 有价值 | Should-Fix: 缺前瞻性 | 建议展开 Discussion，不影响核心评分。 |\n| 页数合规 (R2-W7) | REBUT: §1-§5 在 8 页内 | Minor: ~8.2 页 | R1 核实正确——正文合规。 |\n| Limitations 位置 (R2-W8) | REBUT: ACL 2023+ 允许 | Minor: 不常见 | R1 核实正确——合规。 |\n| 多重检验 (R1-W7) | Should-Fix: 不系统 | REBUT: 区分 confirmatory/exploratory | R2 论据合理——但建议更明确标注哪些是 exploratory。 |\n\n---\n\n## Questions\n\n1. **Cross-seed hacking 模式发散的机制是什么？** 同一条件下 s42→H1, s44→H7 (Table 6)——是否说明 hacking taxonomy 的 predictive utility 有限？[R1-Q1, R2 AGREE]\n2. **\"Structural degeneration generalizes\" 指现象还是形态？** ProofFOL 上 hacking 模式分布与 FOLIO 不同——准确说应为 \"现象泛化但形态不完全一致\"。[R1-Q3, R2 AGREE]\n3. **Random reward 条件的 non-trivial 结构效应如何解释？** Random β=0.1 的 non-hacking 率已低于 SFT，暗示 GRPO 训练本身（而非特定奖励信号）是退化主因？[R1-Q4, R2 AGREE]\n4. **Prolog vs. FOL solver 语义覆盖不等价** — SWI-Prolog 基于 Horn clause（FOL 子集），观察到的 \"相同模式\" 可能部分归因于 solver 差异。[R2-Q3, R1 AGREE]\n\n---\n\n## Missing References\n\n### 两位 Reviewer 一致推荐\n- **Ng et al. (1999)** \"Policy invariance under reward transformations\" — reward shaping 经典理论，ISR-as-reward 的理论基础 [R1]\n- **Sullivan et al. (2025/2026)** \"GRPO is Secretly a Process Reward Model\" — 直接分析 GRPO 内部 reward 机制 [R2]\n- **\"Is It Thinking or Cheating?\"** (arXiv:2510.01367) — reasoning effort 角度检测隐式 reward hacking [R2]\n- **2026 Q1-Q2 RLVR concurrent work** — 更广泛引用同期工作 [R1, R2]\n\n### R2 单独推荐\n- Luo et al. (2026) \"Beyond Outcome Verification\" (arXiv:2601.17223)\n- Pan et al. (2025/2026) \"Pushing the Boundaries\" (arXiv:2601.22642)\n\n### R1 推荐但 R2 REBUT\n- Katz et al. Reluplex（R2 认为关联弱）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态: 未返回 (pending)**。已于 2026-05-20T05:24 发送请求，8 小时后将自动提醒。内部审稿不因此推迟。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态: 已完成** (2026-05-20T05:24 — 05:27, 耗时 ~3 min)\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| **Critical** | Page 20 | Table 9 仅占页面顶部 ~25%，其余 ~75% 完全空白。给审稿人留下 \"内容不足/排版草率\" 印象。建议合并到前页或补充内容。 |\n| Warning | Pages 1-3 | 连续 3 页纯文本无 display item。Figure 1 直到第 4 页才出现。建议提前到第 2 页。 |\n| Warning | Page 8 | Figure 5 堆叠柱状图 8+ 种颜色，部分相近色在灰度/色盲场景下难区分。建议辅以 hatching pattern。 |\n| Warning | Pages 14-17 | 附录 D 连续 4 页纯文本（hacking mode 定义），视觉疲劳。 |\n| Warning | Pages 18-19 | Tables 6-7 字号 ~6-7pt，密集数字难辨认。 |\n| Info | 全局 | 正文 8 页含 5 figure + 2 table + 1 algorithm = 8 个 display items，密度良好。无 margin 溢出、无 LaTeX 渲染错误、无 [?] 未解析引用。 |\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | R1 | R2 | 综合 |\n|------|------|------|------|\n| Soundness | 2.5/5 | 3.0/5 | **2.75/5** |\n| Excitement | 3.5/5 | 3.0/5 | **3.25/5** |\n| Reproducibility | 3.5/5 | 4.0/5 | **3.75/5** |\n| **Overall** | **3.0 (Findings)** | **3.0 (Findings)** | **3.0 (Findings)** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n### 综合判断: **3.0 — Findings**\n\n**核心理由**:\n\n1. **优势**: 跨学科方法迁移有创意，\"诊断变为目标\"的 Goodhart 发现有社区警示价值，8 模式 hacking 分类学系统完整，实验控制严谨（SFT + random + exec-only），透明度高。\n\n2. **主要限制** (两位 reviewer 一致):\n   - 单模型（Qwen3-4B）实验不足以支撑标题暗示的泛化性 claims\n   - 3 seeds 统计效力不足，per-seed 方差大于 cross-condition 差异\n   - LOO 独立性假设未讨论，可能系统性偏置核心指标\n   - 方法论新颖性有限（LOO 是标准技术），价值主要在经验发现\n\n3. **升级路径**: 增加一个 7B+ 模型关键实验复现 + 增至 5+ seeds + 讨论 LOO 假设 + 展开缓解方案 → 可升至 3.5 (Borderline Conference)。\n\n### 置信度说明\n两位 Reviewer 均熟悉 neurosymbolic reasoning、RL reward shaping 和 reward hacking 文献（Confidence 4/5）。在 11 个 Weaknesses 中 8 个完全一致，3 个有 minor 分歧但不影响整体判断。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 叙事流畅，contribution 列表（C1-C4）清晰。但 \"GRPO-Trained Neurosymbolic Reasoning\" 标题暗示的泛化性与单模型证据不匹配。\n- Abstract 缩写密度过高（~8 个/200 词），建议精简。\n\n### §2 Related Work\n- 覆盖 neurosymbolic reasoning、reward hacking、process rewards、mutation testing 核心领域。Helff et al. (2026) 和 Khalifa et al. (2026) 已引用并差异化。\n- Kim et al. (2026) 对比仍不充分——需展开 scope/mechanism/FOLIO 互补性三维度。\n- 缺少 Ng et al. (1999) reward shaping 经典理论。\n\n### §3 Method\n- STA/ISR 定义清晰（Algorithm 1, Eq. 1）。\n- §3.2 未讨论 LOO 独立性假设（Must-Fix）。\n- O(1) vs. O(n) 对比有讨论但缺定量一致性数据（Should-Fix）。\n\n### §4 Experiments\n- §4.1 Setup 完整。\"Statistical considerations\" 段有效管理预期。\n- §4.2 ISR-as-diagnostic: ISR 崩溃轨迹（Figure 2）是论文最有力的发现。SFT baseline 有效（100-step 对照好）。\n- §4.3 Goodhart 分析: confound 以 headline 呈现（\"The headline result is negative\"）是诚实的写法。但乘法耦合混淆未充分讨论。\n- §4.4 Cross-domain: Prolog 和 ProofFOL 验证增强可信度，但 ProofFOL 构建细节不足。\"Beneficial instability\" 概念有趣但 p=0.10 不足以支撑 claim。\n- §4.5 Taxonomy: 8 模式定义完整，但验证规模不足。\n\n### §5 Discussion/Conclusion\n- 过于简短（7 行）。缺少缓解方案讨论。\n- 建议展开为 2 段：(1) 已有发现的 implications；(2) 缓解方向和 future work。\n\n### §6 Limitations\n- 内容充实（单模型、统计效力、ISR 语义限制、data scale）。位置在 References 后，合规。\n\n### Appendix\n- 高质量（per-seed 详细结果、hacking mode 定义、statistical details）。\n- Page 20 大面积空白需处理（Visual Check critical）。\n",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "solver-trace-ablation",
    "report": "# 审稿报告 — Round 16 (Fresh Review)\n\n**论文**: \"Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewers**: R1（方法严谨性 + 实验设计 + 统计分析）、R2（新颖性 + 写作 + 格式）\n**日期**: 2026-05-20\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，将 LOO 变异测试迁移到 GRPO 训练的神经符号推理器诊断场景，定义 Intensional Structural Reward (ISR) 指标。在 6 种奖励条件 × 2 逻辑类型 × 2 数据集 × 3 seeds 上训练 Qwen3-4B，发现：(1) exec-only GRPO 下 ISR 99.5% 崩溃（PR 上升同时），(2) ISR-as-reward 触发 Goodhart 效应（H7 放大 ~5×），(3) 归纳 8 种 reward hacking 模式。核心结论：ISR 作为诊断可靠，作为优化目标则 dataset-dependent（FOLIO 上 Goodhart collapse，ProofFOL 上 beneficial instability）。\n\n---\n\n## Strengths\n\n**S1. 跨学科方法论迁移有创意** [R1-S1, R2-S1 共识]\n将变异测试（mutation testing）的 LOO 范式迁移到 GRPO 训练的 solver 输出诊断，填补了 neurosymbolic RL 中 structural diagnostic 的空白。ISR 定义简洁（Eq. 1, Algorithm 1），语义清晰。\n\n**S2. 实验控制严谨** [R1-S3/S4, R2-S2 共识]\n6 条件 × 3 seeds × 2 数据集家族 + SFT baseline + exec-only 控制组。Random reward 条件有效分离 ISR-specific 信号与 generic reward-variance 效应。SFT 分离了 RL 引入的退化 vs. 预训练能力不足。Fisher exact test + Bonferroni 校正（k=14，Appendix）规范。\n\n**S3. \"诊断变为目标\" 的 Goodhart 发现有社区价值** [R1-S1, R2-S3 共识]\nISR 作为诊断时可靠（§4.2: 99.5% 崩溃被检测），但作为奖励时被 game（§4.3: H7 ~5× 放大）——这一对比清晰映射到 Manheim-Garrabrant 分类学（regressional on FOLIO, extremal at high β），为 neurosymbolic RL 社区提供实证警示。\n\n**S4. Hacking 分类学系统完整** [R1-S2, R2-S4 共识]\n8 种模式有操作定义 + FOL/Prolog 示例 + ISR 交互分析 + 出现频率统计（Table 2, Appendix D）。H7b（obfuscated tautology: triple gaming of exec reward + ISR + text-match classifier）和 query-as-fact gaming（Prolog-specific）超出简单直觉。\n\n**S5. 跨域验证增强可信度** [R1-S3, R2-S5 共识]\nFOL/Prolog 跨逻辑 + FOLIO/ProofFOL 跨数据集交叉验证。ProofFOL 上 beneficial instability（76.8% vs. 17.4% genuine, p=0.10）与 FOLIO 上 Goodhart collapse 的对比揭示了 ISR 的 dataset-dependent 不对称性。\n\n**S6. 透明度高** [R1-S5]\nPer-seed 附录数据（Tables 6-9）、Bonferroni 校正细节、hacking classifier validation（50 样本 precision + 20 boundary cases）、O(1) vs O(n) 消融比较均完整呈现。\n\n---\n\n## Weaknesses\n\n### Must-Fix\n\n**W1. 单模型 + 3 seeds：泛化性和统计效力双重不足** [R1-W1+W3, R2-W1; 共识]\n所有实验仅在 Qwen3-4B 上完成。LLaMA-3.2-3B 冷启动失败（Appendix E.4）不构成第二模型验证，反而暴露结果的模型依赖性。3 seeds 下 per-seed 方差极大（ISR β=0.1: s42 non-hacking=17.3%, s43=0%, s44=0%；Table 6），cross-seed 差异大于 cross-condition 差异。ProofFOL genuine-rate permutation test p=0.10 明确欠效力。论文标题 \"GRPO-Trained Neurosymbolic Reasoning\" 暗示普遍性但仅一个 4B 模型有正面证据。\n- **建议**: (a) 至少增加一个 7B+ 或不同架构模型的关键实验复现；(b) 增至 5+ seeds；(c) 若资源不允许，在标题和 abstract 明确限定 claims 适用范围（如 \"in Qwen3-4B\"），降级为 case study。\n\n**W2. LOO 独立性假设未讨论** [R1-W2; R2 交叉 AGREE]\nAlgorithm 1 逐一移除 premise，假设组件独立消融，但未讨论 premise 间交互效应——如两个 premise 联合必要但各自单独非必要（FOL 中常见：A∧B→C）。此偏差可能导致 ISR 系统性偏高。变异测试文献中 higher-order mutants 的研究（Jia & Harman, 2011）已讨论此局限性，论文应引用并讨论偏差方向。\n- **建议**: (a) 在 Limitations 或 §3.2 明确讨论 LOO 独立性假设及失败场景；(b) 报告至少一个条件的 LOO vs. pairwise 消融比较。\n\n### Should-Fix\n\n**W3. Hacking 分类器验证不充分** [R1-W6, R2-W6; 共识]\n56 个手动验证样本（H1/H7 仅），无 inter-annotator agreement，H8 检测已知失败（Appendix D.1）。Text-match classifier 有已知 false-negative（Prolog: strict classifier 100% non-hacking → functional analysis 95/97 tautological）。分类学基于 post-hoc pattern matching，可能有确认偏差。\n- **建议**: (a) 扩大验证样本至 100+；(b) 报告 Cohen's κ（至少两人标注）；(c) 将分类学定位为 \"exploratory taxonomy\"。\n\n**W4. 方法论新颖性有限** [R2-W2; R1 部分 REBUT]\nSTA 核心操作是标准 LOO 消融。R1 认为 STA 贡献是三层的（组件级消融 + ISR 双重角色 + Goodhart 实证），类比 probing classifiers 定义新分析范式。R2 认为技术门槛不高。**分歧**：R1 倾向方法论有增量新颖性，R2 认为有限。共识：价值主要在经验发现而非方法本身。\n- **建议**: 重新 frame C1 为 \"新诊断框架\" 而非 \"新消融方法\"，强调框架整体（ISR + taxonomy + cross-domain protocol）的贡献。\n\n**W5. 缺少缓解方案 (mitigation) 讨论** [R2-W3; R1 部分 REBUT]\n§5 Discussion 仅 7 行。R1 指出 ISR-as-reward 的 negative result 本身有价值，§5 已暗示方向；R2 认为与 Helff et al. (2026) 和 Khalifa et al. (2026) 等同期工作相比缺乏前瞻性。\n- **建议**: 在 Discussion 展开 2-3 个缓解方向（multi-granularity ablation, ISR-as-filter, reward ensembling, constrained optimization），即使不做实验也增加前瞻性。\n\n**W6. 与 Kim et al. (2026) 差异化不充分** [R2-W4, R1-Q5; 共识]\nKim et al. (2026) 研究 inference-time formalization gaming（GPT-5/DeepSeek-R1 + Lean 4 + FOLIO），本文研究 training-time structural degeneration。两者共享 FOLIO 数据集，但 Related Work 仅一句话提及，缺少三维度对比（scope, mechanism, FOLIO 互补性）。\n- **建议**: 在 Related Work 增加 2-3 句详细对比。\n\n**W7. ProofFOL 数据集构建缺关键细节** [R1-W5; R2 AGREE]\n§4.1 仅说 \"translated via GPT-4o, ~70% retention\"。缺失：初始样本量、过滤标准、人工抽检准确率、逻辑复杂度分布。§4.4 \"simpler predicates\" 表述暗示数据集简单性可能混淆跨域泛化 claims。\n- **建议**: 在 §4.1 或 Appendix 补充 ProofFOL 构建流水线完整细节。\n\n**W8. O(1) vs. O(n) ISR 一致性未量化** [R1-W8; R2 AGREE]\n§3.3/Appendix E.3 讨论了 O(1) 为何产生 near-zero ISR，但缺乏定量一致性比较（相关系数或 MAE）。\n- **建议**: 用现有 held-out 数据报告 O(1) vs. O(n) ISR 值一致性。\n\n**W9. 缩写密度过高** [R2-W5; R1 轻度 AGREE]\nAbstract ~200 词内引入 STA, ISR, LOO, SFT, PR, FOLIO, ProofFOL, NLI 等 8+ 缩写。H1/H7/H8 和 CE/TS/PG/CI 双重编号增加认知负担。\n- **建议**: Abstract 仅保留 STA/ISR 缩写；hacking 模式统一使用一套编号。\n\n### Minor\n\n**W10. Figure 2 x 轴不均匀** [R1-W9; R2 AGREE]\n0, 100, 500, 1000 步间距不等但视觉等距。建议 log-scale 或标注断点。\n\n**W11. CMH test 统计量不完整** [R2-W9; R1-W7 相关]\nCMH test 被提及但未报告详细统计量（仅说 \"borderline\"）。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n1. **单模型 + 3 seeds 不足** — 最关键的结构性限制，无法通过文字修改解决\n2. **LOO 独立性假设未讨论** — 方法论盲点\n3. **Hacking 分类器验证不足** — 56 样本、无 IAA\n4. **Kim et al. (2026) 对比不充分** — 共享 FOLIO 数据集使对比成为可能\n5. **ProofFOL 构建细节缺失** — 影响跨域泛化 claim 可信度\n6. **缩写密度过高** — 影响可读性\n7. **O(1) vs. O(n) 未量化** — 可用现有数据轻松回答\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 判断 |\n|------|------|------|------|\n| ISR-reward 混淆 (R1-W4) | Must-Fix: 需 ISR-only 消融 | REBUT: 现有设计已部分分离；ISR-only 概念病态 | R2 论据更有说服力——hacking 模式质变（H7 0%→71%）不能仅用 exec amplification 解释。降为 Should-Fix。 |\n| 方法论新颖性 (R2-W2) | REBUT: 三层贡献，类比 probing | Must-Fix: LOO 是标准技术 | 分歧但不影响结论——共识为 Findings 级别。 |\n| 缓解方案 (R2-W3) | REBUT: negative result 有价值 | Should-Fix: 缺前瞻性 | 建议展开 Discussion，不影响核心评分。 |\n| 页数合规 (R2-W7) | REBUT: §1-§5 在 8 页内 | Minor: ~8.2 页 | R1 核实正确——正文合规。 |\n| Limitations 位置 (R2-W8) | REBUT: ACL 2023+ 允许 | Minor: 不常见 | R1 核实正确——合规。 |\n| 多重检验 (R1-W7) | Should-Fix: 不系统 | REBUT: 区分 confirmatory/exploratory | R2 论据合理——但建议更明确标注哪些是 exploratory。 |\n\n---\n\n## Questions\n\n1. **Cross-seed hacking 模式发散的机制是什么？** 同一条件下 s42→H1, s44→H7 (Table 6)——是否说明 hacking taxonomy 的 predictive utility 有限？[R1-Q1, R2 AGREE]\n2. **\"Structural degeneration generalizes\" 指现象还是形态？** ProofFOL 上 hacking 模式分布与 FOLIO 不同——准确说应为 \"现象泛化但形态不完全一致\"。[R1-Q3, R2 AGREE]\n3. **Random reward 条件的 non-trivial 结构效应如何解释？** Random β=0.1 的 non-hacking 率已低于 SFT，暗示 GRPO 训练本身（而非特定奖励信号）是退化主因？[R1-Q4, R2 AGREE]\n4. **Prolog vs. FOL solver 语义覆盖不等价** — SWI-Prolog 基于 Horn clause（FOL 子集），观察到的 \"相同模式\" 可能部分归因于 solver 差异。[R2-Q3, R1 AGREE]\n\n---\n\n## Missing References\n\n### 两位 Reviewer 一致推荐\n- **Ng et al. (1999)** \"Policy invariance under reward transformations\" — reward shaping 经典理论，ISR-as-reward 的理论基础 [R1]\n- **Sullivan et al. (2025/2026)** \"GRPO is Secretly a Process Reward Model\" — 直接分析 GRPO 内部 reward 机制 [R2]\n- **\"Is It Thinking or Cheating?\"** (arXiv:2510.01367) — reasoning effort 角度检测隐式 reward hacking [R2]\n- **2026 Q1-Q2 RLVR concurrent work** — 更广泛引用同期工作 [R1, R2]\n\n### R2 单独推荐\n- Luo et al. (2026) \"Beyond Outcome Verification\" (arXiv:2601.17223)\n- Pan et al. (2025/2026) \"Pushing the Boundaries\" (arXiv:2601.22642)\n\n### R1 推荐但 R2 REBUT\n- Katz et al. Reluplex（R2 认为关联弱）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态: 未返回 (pending)**。已于 2026-05-20T05:24 发送请求，8 小时后将自动提醒。内部审稿不因此推迟。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态: 已完成** (2026-05-20T05:24 — 05:27, 耗时 ~3 min)\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| **Critical** | Page 20 | Table 9 仅占页面顶部 ~25%，其余 ~75% 完全空白。给审稿人留下 \"内容不足/排版草率\" 印象。建议合并到前页或补充内容。 |\n| Warning | Pages 1-3 | 连续 3 页纯文本无 display item。Figure 1 直到第 4 页才出现。建议提前到第 2 页。 |\n| Warning | Page 8 | Figure 5 堆叠柱状图 8+ 种颜色，部分相近色在灰度/色盲场景下难区分。建议辅以 hatching pattern。 |\n| Warning | Pages 14-17 | 附录 D 连续 4 页纯文本（hacking mode 定义），视觉疲劳。 |\n| Warning | Pages 18-19 | Tables 6-7 字号 ~6-7pt，密集数字难辨认。 |\n| Info | 全局 | 正文 8 页含 5 figure + 2 table + 1 algorithm = 8 个 display items，密度良好。无 margin 溢出、无 LaTeX 渲染错误、无 [?] 未解析引用。 |\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | R1 | R2 | 综合 |\n|------|------|------|------|\n| Soundness | 2.5/5 | 3.0/5 | **2.75/5** |\n| Excitement | 3.5/5 | 3.0/5 | **3.25/5** |\n| Reproducibility | 3.5/5 | 4.0/5 | **3.75/5** |\n| **Overall** | **3.0 (Findings)** | **3.0 (Findings)** | **3.0 (Findings)** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n### 综合判断: **3.0 — Findings**\n\n**核心理由**:\n\n1. **优势**: 跨学科方法迁移有创意，\"诊断变为目标\"的 Goodhart 发现有社区警示价值，8 模式 hacking 分类学系统完整，实验控制严谨（SFT + random + exec-only），透明度高。\n\n2. **主要限制** (两位 reviewer 一致):\n   - 单模型（Qwen3-4B）实验不足以支撑标题暗示的泛化性 claims\n   - 3 seeds 统计效力不足，per-seed 方差大于 cross-condition 差异\n   - LOO 独立性假设未讨论，可能系统性偏置核心指标\n   - 方法论新颖性有限（LOO 是标准技术），价值主要在经验发现\n\n3. **升级路径**: 增加一个 7B+ 模型关键实验复现 + 增至 5+ seeds + 讨论 LOO 假设 + 展开缓解方案 → 可升至 3.5 (Borderline Conference)。\n\n### 置信度说明\n两位 Reviewer 均熟悉 neurosymbolic reasoning、RL reward shaping 和 reward hacking 文献（Confidence 4/5）。在 11 个 Weaknesses 中 8 个完全一致，3 个有 minor 分歧但不影响整体判断。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 叙事流畅，contribution 列表（C1-C4）清晰。但 \"GRPO-Trained Neurosymbolic Reasoning\" 标题暗示的泛化性与单模型证据不匹配。\n- Abstract 缩写密度过高（~8 个/200 词），建议精简。\n\n### §2 Related Work\n- 覆盖 neurosymbolic reasoning、reward hacking、process rewards、mutation testing 核心领域。Helff et al. (2026) 和 Khalifa et al. (2026) 已引用并差异化。\n- Kim et al. (2026) 对比仍不充分——需展开 scope/mechanism/FOLIO 互补性三维度。\n- 缺少 Ng et al. (1999) reward shaping 经典理论。\n\n### §3 Method\n- STA/ISR 定义清晰（Algorithm 1, Eq. 1）。\n- §3.2 未讨论 LOO 独立性假设（Must-Fix）。\n- O(1) vs. O(n) 对比有讨论但缺定量一致性数据（Should-Fix）。\n\n### §4 Experiments\n- §4.1 Setup 完整。\"Statistical considerations\" 段有效管理预期。\n- §4.2 ISR-as-diagnostic: ISR 崩溃轨迹（Figure 2）是论文最有力的发现。SFT baseline 有效（100-step 对照好）。\n- §4.3 Goodhart 分析: confound 以 headline 呈现（\"The headline result is negative\"）是诚实的写法。但乘法耦合混淆未充分讨论。\n- §4.4 Cross-domain: Prolog 和 ProofFOL 验证增强可信度，但 ProofFOL 构建细节不足。\"Beneficial instability\" 概念有趣但 p=0.10 不足以支撑 claim。\n- §4.5 Taxonomy: 8 模式定义完整，但验证规模不足。\n\n### §5 Discussion/Conclusion\n- 过于简短（7 行）。缺少缓解方案讨论。\n- 建议展开为 2 段：(1) 已有发现的 implications；(2) 缓解方向和 future work。\n\n### §6 Limitations\n- 内容充实（单模型、统计效力、ISR 语义限制、data scale）。位置在 References 后，合规。\n\n### Appendix\n- 高质量（per-seed 详细结果、hacking mode 定义、statistical details）。\n- Page 20 大面积空白需处理（Visual Check critical）。\n",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 1553 · 2026-05-20T05:40:55.430359+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 6024
}
```

</details>

---


### Assistant

_source line 1554 · 2026-05-20T05:41:05.016540+00:00_

---

**📋 审稿完成通报 — Group C**

Round 16 (Fresh Review) 圆桌审稿已完成，报告已投递给 Research Director。

**结论: 3.0 — Findings**

两位 Reviewer 高度一致（8/11 Weaknesses 完全共识），核心限制：

1. **单模型 + 3 seeds** — 泛化性和统计效力双重不足，持续 14 轮未解决的结构性问题
2. **LOO 独立性假设未讨论** — 新发现的方法论盲点（本轮首次由两位 Reviewer 独立提出）
3. **方法论新颖性有限** — LOO 是标准技术，价值在经验发现
4. **Hacking 分类器验证不足** — 56 样本、无 IAA

**升级路径**: +7B 模型复现 + 5+ seeds + LOO 假设讨论 + 缓解方案 → 3.5 (Borderline Conference)

外部审稿（Stanford Agentic Reviewer）尚未返回，已标注在报告中。视觉审查已完成（1 critical: Page 20 空白；4 warnings）并纳入报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 131

## Round 131

2 recorded events


### User

_source line 1555 · 2026-05-20T05:41:07.859828+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- R2 的 10 条 Weakness 中，**5 条 AGREE**（W1 单模型、W4 Kim对比、W5 缩写、W6 小样本、W9 CMH 细节）、**3 条 REBUT**（W2 新颖性——STA 定义了新分析范式不应低估、W7 超页——实际合规、W8 Limitations 位置——ARR 允许）、**2 条部分 REBUT**（W3 缓解——ISR-as-reward 的 Goodhart 是有价值的 negative result）
- R2 的 4 个 Question 中，Q1/Q2 论文已明确回答（REBUT），Q3/Q4 关切合理（AGREE）
- 两位 reviewer 在核心问题上高度一致：单模型、3 seeds 统计效力、分类学验证不足。评分共识为 **3.0 Findings**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1556 · 2026-05-20T05:41:21.252937+00:00_

审稿报告已投递完成。

**圆桌审稿总结**：

- **Overall**: 3.0 (Findings)，两位 Reviewer 一致，Confidence 4/5
- **核心优势**: 跨学科方法迁移有创意、Goodhart 发现有警示价值、8 模式分类学系统完整、实验控制严谨
- **Must-Fix** (共识): 单模型+3 seeds 泛化性/统计效力双重不足；LOO 独立性假设未讨论
- **Should-Fix** (共识): Hacking 分类器验证不充分；Kim et al. 对比不足；ProofFOL 构建缺细节；缺少缓解方案讨论；缩写密度过高
- **升级路径**: +7B 模型复现 +5 seeds +LOO 假设讨论 +缓解方案 → 3.5 Borderline Conference
- **外部审稿**: 未返回 (pending)
- **视觉审查**: 已完成，1 critical (Page 20 空白) + 4 warning
- **Issue Tracker**: 已同步更新至 Round 16

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 132

## Round 132

66 recorded events


### User

_source line 1557 · 2026-05-20T06:35:16.227854+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1558 · 2026-05-20T06:35:22.270550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1559 · 2026-05-20T06:35:22.322076+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1560 · 2026-05-20T06:35:28.652200+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1561 · 2026-05-20T06:35:28.652741+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1562 · 2026-05-20T06:35:31.667604+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1563 · 2026-05-20T06:35:31.677813+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 10
}
```

</details>

---


### Tool call

_source line 1564 · 2026-05-20T06:35:36.245863+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 1565 · 2026-05-20T06:35:38.091388+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (199 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-20T06:27:14Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 199 个实验 — DONE 168, PREPARING 31\n**DONE 分布**: failed 47, killed 10, negative 41, success 70\n\n### GPU 占用\n- **分配**: 1 张 — westd-39279:cuda:0\n\n### 💾 磁盘余量\n- **westd-39279**:\n  - `/init`: 150M/150M 可用（已用 1%）\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/usr/bin/nvidia-smi`: 400G/439G 可用（已用 5%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `d154-8b-exec-s42-r3` [failed] — 2026-05-20T06:27:11 — EXIT_CODE=129 (non-zero)\n- `sweep-random-b01-s46` [success] — 2026-05-20T04:05:11\n- `sweep-random-b01-s45` [success] — 2026-05-20T04:05:09\n- `d146-pf-isr-s43` [success] — 2026-05-20T03:39:11\n- `d146-pf-isr-s44` [negative] — 2026-05-20T03:32:08\n\n### 🔴 最近失败原因 (top 3)\n- `d154-8b-exec-s42-r3`: EXIT_CODE=129 (non-zero)\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- d154-8b-exec-s42-k4（准备中）\n- d154-8b-exec-s42-r2（准备中）\n- d154-8b-exec-s42: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=42. Tests whether larger model (8B vs 4B) exhib
…[truncated 1881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1845
}
```

</details>

---


### Tool call

_source line 1566 · 2026-05-20T06:35:38.593831+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf 2>&1 && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
  "description": "Check paper files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf 2>&1 && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
    "description": "Check paper files exist"
  }
}
```

</details>

---


### Tool result

_source line 1567 · 2026-05-20T06:35:43.667517+00:00_

-rw-r--r-- 1 ubuntu ubuntu 611145 May 20 06:26 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf
-rw-r--r-- 1 ubuntu ubuntu    886 May 20 04:51 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex
42 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 5073
}
```

</details>

---


### Tool call

_source line 1568 · 2026-05-20T06:35:43.919230+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1569 · 2026-05-20T06:35:44.322915+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission deadline author guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission deadline author guidelines page limit"
  }
}
```

</details>

---


### Tool result

_source line 1570 · 2026-05-20T06:35:49.349019+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

Based on the search results, I found information about EMNLP 2026 and ARR submission guidelines, though the main conference cal
…[truncated 1078 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5429
}
```

</details>

---


### Tool result

_source line 1571 · 2026-05-20T06:35:50.205068+00:00_

Web search results for query: "ACL Rolling Review 2026 submission deadline author guidelines page limit"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"}]

I found information about ACL Rolling Review 2026 from the search results. Here's what I found:

## Submission Deadline

The submission deadline for ACL 2026 is January 5, 2026, with all papers submitted to ARR.

## Author Guidelines

The search results reference author guidelines but don't provide the complete details on a single page. However, I can share some key requirements:

- All submitting authors h
…[truncated 965 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5882
}
```

</details>

---


### Tool call

_source line 1572 · 2026-05-20T06:35:55.636471+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclrollingreview.org CFP 2026 page limit long paper short paper anonymity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "aclrollingreview.org CFP 2026 page limit long paper short paper anonymity"
  }
}
```

</details>

---


### Tool call

_source line 1573 · 2026-05-20T06:35:56.189424+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 commitment deadline ARR cycle October"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 commitment deadline ARR cycle October"
  }
}
```

</details>

---


### Tool call

_source line 1574 · 2026-05-20T06:35:56.742115+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1575 · 2026-05-20T06:35:57.597281+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{limitations}
38	
39	\appendix
40	\input{appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 1576 · 2026-05-20T06:35:57.748871+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>&1; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/ 2>&1",
  "description": "Check existing review artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>&1; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/ 2>&1",
    "description": "Check existing review artifacts"
  }
}
```

</details>

---


### Tool result

_source line 1577 · 2026-05-20T06:35:57.849786+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml
round_0.md
round_1.md
round_10.md
round_11.md
round_12.md
round_13.md
round_14.md
round_15.md
round_16.md
round_2.md
round_3.md
round_4.md
round_5.md
round_6.md
round_7.md
round_8.md
round_9.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 1578 · 2026-05-20T06:36:01.616797+00:00_

Web search results for query: "EMNLP 2026 commitment deadline ARR cycle October"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"}]

Based on the search results, here are the key findings regarding EMNLP 2026 commitment deadline and the ARR cycle:

## EMNLP 2026 Commitment Deadline

The EMNLP commitment deadline is August 2, 2026, with all deadlines being 11:59PM UTC-12:00 ("anywhere on Earth").

## ARR Cycle Timeline

The ARR submission deadline for EMNLP 2026 is May 25, 2026, with meta reviews released on July 30, 2026. The process follows a specific sequence:

Author response and author-reviewer discussion occurs July 7 - July 13, 20
…[truncated 557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5427
}
```

</details>

---


### Tool result

_source line 1579 · 2026-05-20T06:36:02.673381+00:00_

Web search results for query: "aclrollingreview.org CFP 2026 page limit long paper short paper anonymity"

Links: [{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"LINGUIST List 36.2627 Confs: 19th Conference of the European Chapter of the Association for Computational Linguistics (Morocco)","url":"https://linguistlist.org/issues/36/2627/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"دعوة لتقديم أوراق المؤتمر الرئيسية -","url":"https://translate.google.com/translate?u=https%3A%2F%2F2026.eacl.org%2Fcalls%2Fpapers%2F&hl=ar&sl=en&tl=ar&client=srp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"}]

Based on the search results from aclrollingreview.org, here are the key submission guidelines for 2026:

**Page Limits:**
- Long papers: 8 pages; Short papers: 4 pages (not including limitations and ethical considerations)

**Anonymity Policy:**
- Beginning with the February 15, 2024 ARR deadlines, there is no anonymity period or limitation on posting or discussing non-anonymous preprints while the work is under peer review
- However, papers must not include authors' names and affiliations, and self-references that reveal the authors' identities must be avoided
- Supplementary materials should also be anonymized, and links to file hosting services like Dropbox are not allowed

**Additional Requirements:**
- Submissions will remain anonymous durin
…[truncated 194 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 7036
}
```

</details>

---


### Tool call

_source line 1580 · 2026-05-20T06:36:10.045573+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1581 · 2026-05-20T06:36:10.497897+00:00_

1	\begin{abstract}
2	Using Qwen3-4B as a testbed, we find that a neurosymbolic formalizer trained with GRPO achieves a 93\% prove rate on FOLIO---yet 87\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution reward.
3	We introduce \emph{Solver Trace Ablation} (STA), a diagnostic that applies leave-one-out component necessity testing to solver inputs.
4	The fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates full necessity; ISR$=$0 complete redundancy.
5	ISR is uncorrelated with downstream task accuracy ($\rho{=}{-}0.049$), confirming it measures component necessity---not semantic faithfulness.
6	As a diagnostic, ISR exposes a collapse trajectory hidden from prove rate: over 100--1000 GRPO steps, ISR falls $0.642{\to}0.003$ while prove rate rises $32\%{\to}96\%$; a supervised fine-tuning baseline reaches 92.3\% non-hacking on identical data (3-seed pooled), localizing the failure to reinforcement learning.
7	As a reward, $r = r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta{=}0.1$ induces Goodhart effects on the structural metric: 70.6\% tautological shortcutting versus 13.7\% under matched random (Fisher $p{=}1.3{\times}10^{-39}$; random shortcutting is seed-dependent, driven by one of three seeds); ISR amplifies shortcutting frequency ${\sim}5{\times}$ rather than exclusively causing it; the sole apparent ISR advantage reduces to $1.06\times$ after controlling for a premise-count confound; $\beta{=}0.3$ destabilizes training regardless of signal source (ISR: $66{\pm}42\%$; random: $54{\pm}35\%$), with individual seeds collapsing to as low as $18\%$.
8	Cross-logic transfer to Prolog yields universal Goodhart (3/3 seeds, 0\% non-hacking); cross-dataset replication on ProofFOL (${\sim}$500 examples) confirms structural degeneration generalizes ($\text{ISR}^*{<}0.12$, ${\leq}1.4\%$ genuine in converged seeds), while ISR as tra
…[truncated 562 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1582 · 2026-05-20T06:36:10.498259+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1583 · 2026-05-20T06:36:11.000813+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.
7	
8	\paragraph{The execution-only blind spot.}
9	Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
11	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
12	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for component necessity in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify component necessity (Figure~\ref{fig:sta-overview}).
16	For each proved formalization, STA removes each component individually and re-runs t
…[truncated 3293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1584 · 2026-05-20T06:36:11.001573+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1585 · 2026-05-20T06:36:11.403552+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
7	
8	\paragraph{Process rewards and reward shaping.}
9	Reward shaping theory~\citep{ng1999policy} establishes conditions under which auxiliary rewards preserve optimal policies; early work applied verifier-based training to mathematical reasoning~\citep{cobbe2021training}, with process-level feedback showing promise over outcome-only signals~\citep{uesato2022solving}.
10	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}: \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
11	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
12	Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both illustrate the proxy risk inherent in reward augmentation.
13	\citet{sullivan2025grpo} reinterpret GRPO as implicitly learning a process reward model, suggesting the structural gaming we document may reflect PRM-level overfitting rather than purely outcome-level shortcuts.
14	
15	\paragraph{Reward hacking and Goodhart's Law.}
16	Goodhart's Law is establish
…[truncated 2104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1586 · 2026-05-20T06:36:11.404007+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1587 · 2026-05-20T06:36:11.454672+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: the diagnostic becomes the optimization target, exhibiting Goodhart effects at a meta level.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$ (Figure~\ref{fig:sta-overview}a).
15	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
16	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
17	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
18	
19	\subsection{Solver Trace Ablation (STA)}
20	\label{sec:sta}
21	
22	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}b).
23	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
24	A component is \emph{necessary} if its removal causes proof failure.
25	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
26	LOO ablation itself is stand
…[truncated 6339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1588 · 2026-05-20T06:36:15.772490+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1589 · 2026-05-20T06:36:16.175267+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 does not change qualitative conclusions (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the eight cataloged patterns, a necessary 
…[truncated 15389 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1590 · 2026-05-20T06:36:16.326315+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1591 · 2026-05-20T06:36:16.678090+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\% collapse under exec-only GRPO that PR hides, while SFT localizes the failure to RL (\S\ref{sec:diagnostic}).
5	Repurposed as a reward, ISR produces dataset-dependent outcomes: on FOLIO, Goodhart effects amplify TS ${\sim}5{\times}$ ($p{<}10^{-39}$); on ProofFOL, beneficial instability yields 76.8\% vs.\ 17.4\% genuine ($p{=}0.10$).
6	Deconfounding reduces the sole apparent ISR reward advantage to $1.06\times$ (\S\ref{sec:goodhart}).
7	The central finding is ISR's observer/optimizer asymmetry: the same LOO structure that makes ISR informative as a diagnostic makes it gameable as a reward, with outcomes depending on whether the dataset's hacking geometry satisfies the metric.
8	
9	The multi-attractor dynamics across seeds---conclusion embedding, tautological collapse, repetition collapse, each from identical data and hyperparameters---suggest structural degeneration under RL is not a single failure but a landscape with multiple basins whose selection is initialization-dependent.
10	Mitigation directions include multi-granularity ablation, ISR as a post-hoc filter rather than training signal, reward ensembling, and constrained optimization; full LOO adds ${<}1\%$ to evaluation cost (55\,ms vs.\ 4\,s per sample; Appendix~\ref{app:o1-ablation}).
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1592 · 2026-05-20T06:36:16.678582+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1593 · 2026-05-20T06:36:17.130527+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); while cross-dataset evidence from ProofFOL (\S\ref{sec:crossdomain}) supports generality, hacking-mode prevalence may vary across benchmarks.
5	STA requires models with sufficient FOL generation capability: LLaMA-3.2-3B fails to produce parseable formalizations under identical training, preventing any structural analysis (Appendix~\ref{app:llama-coldstart}); this capability threshold limits applicability to models above a minimum formalization competence.
6	The ProofFOL genuine-rate advantage ($p{=}0.10$, $N{=}3$ per group) is an observation, not a confirmed effect; ProofFOL itself is silver-standard (GPT-4o translation, ${\sim}70\%$ retention).
7	While structural degeneration generalizes across dataset families, cross-seed variance remains substantial (ProofFOL exec-only $\sigma_{\text{PR}} \approx 25$\,pp), consistent with FOLIO observations and suggesting that individual training trajectories remain seed-sensitive even as the overall phenomenon replicates.
8	ISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
9	Three seeds demonstrate qualitative divergence but limit statistical power.
10	STA requires solvers supporting component-level input manipulation; the Prolog experiments use SWI-Prolog (Horn clause logic, a subset of full FOL), limiting the range of logical structures tested in cross-logic transfer.
11	
12	\paragraph{Data scale.}
13	Our experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\citep{folio}.
14	The training subset is selected via stratified sampling (seed 42) and held constant across all conditions.
15	While our findings are consistent across seeds and logic types, the effect of training data scale on hacking prevalence and mode distribution r
…[truncated 44 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1594 · 2026-05-20T06:36:17.281478+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1595 · 2026-05-20T06:36:17.683351+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other se
…[truncated 41459 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1596 · 2026-05-20T06:36:27.940682+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf 2>/dev/null | grep -i pages || python3 -c \"import PyPDF2; r=PyPDF2.PdfReader('/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf'); print(f'Pages: {len(r.pages)}')\" 2>/dev/null || echo \"Cannot determine page count\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf 2>/dev/null | grep -i pages || python3 -c \"import PyPDF2; r=PyPDF2.PdfReader('/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf'); print(f'Pages: {len(r.pages)}')\" 2>/dev/null || echo \"Cannot determine page count\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1597 · 2026-05-20T06:36:28.192008+00:00_

Pages:           21

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1598 · 2026-05-20T06:36:29.144967+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1599 · 2026-05-20T06:36:29.897165+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 752
}
```

</details>

---


### Tool call

_source line 1600 · 2026-05-20T06:36:30.198810+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/config.yaml 2>/dev/null | head -100",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/config.yaml 2>/dev/null | head -100",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1601 · 2026-05-20T06:36:30.449999+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1602 · 2026-05-20T06:36:30.550638+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1603 · 2026-05-20T06:36:30.651405+00:00_

1	% ============================================================
2	% LLaMA
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title = {{The Llama 3 Herd of Models}},
8	  journal = {arXiv preprint arXiv:2407.21783},
9	  year = {2024},
10	  eprint = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	% ============================================================
15	% Category 1: Neurosymbolic reasoning + RL/GRPO
16	% ============================================================
17	
18	@article{deepseekmath,
19	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
20	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
21	  journal      = {arXiv preprint arXiv:2402.03300},
22	  year         = {2024},
23	  eprint       = {2402.03300},
24	  archivePrefix = {arXiv},
25	  primaryClass = {cs.AI},
26	}
27	
28	@article{logic-rl,
29	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
30	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
31	  journal      = {arXiv preprint arXiv:2502.14768},
32	  year         = {2025},
33	  eprint       = {2502.14768},
34	  archivePrefix = {arXiv},
35	  primaryClass = {cs.AI},
36	}
37	
38	@article{mellgren-prolog-grpo,
39	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
40	  title        = {{Training Language Models to Use Prolog as a Tool}},
41	  journal      = {arXiv preprint arXiv:2512.07407},
42	  year         = {2025},
43	  eprint       = {2512.07407},
44	  archivePrefix = {arXiv},
45	  primaryClass = {cs.AI},
46	}
47	
48	@inproceedings{satlm,
49	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
50	  title        
…[truncated 2319 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1604 · 2026-05-20T06:36:34.750163+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ -name \"config*\" -o -name \"*.yaml\" -maxdepth 2 2>/dev/null | head -20",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ -name \"config*\" -o -name \"*.yaml\" -maxdepth 2 2>/dev/null | head -20",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1605 · 2026-05-20T06:36:34.951429+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.git/config
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/grpo_exec_only.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/grpo_exec_sta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1606 · 2026-05-20T06:36:35.002314+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 1607 · 2026-05-20T06:36:35.053183+00:00_

100	  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},
101	  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},
102	  journal      = {arXiv preprint arXiv:2506.10947},
103	  year         = {2025},
104	  eprint       = {2506.10947},
105	  archivePrefix = {arXiv},
106	  primaryClass = {cs.AI},
107	}
108	
109	@article{bondarenko-spec-gaming,
110	  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},
111	  title        = {{Demonstrating Specification Gaming in Reasoning Models}},
112	  journal      = {arXiv preprint arXiv:2502.13295},
113	  year         = {2025},
114	  eprint       = {2502.13295},
115	  archivePrefix = {arXiv},
116	  primaryClass = {cs.AI},
117	}
118	
119	@inproceedings{kim-game-formalization,
120	  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},
121	  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},
122	  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},
123	  year         = {2026},
124	  note         = {arXiv:2604.19459},
125	}
126	
127	@inproceedings{gao-reward-overoptimization,
128	  author       = {Leo Gao and John Schulman and Jacob Hilton},
129	  title        = {{Scaling Laws for Reward Model Overoptimization}},
130	  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},
131	  year         = {2023},
132	  note         = {arXiv:2210.10760},
133	}
134	
135	@inproceedings{karwowski-goodhart-rl,
136	  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},
137	  title        = {{Goodhart's Law in Reinforcement Learning}},
138	  booktitle    = {Proceedings of 
…[truncated 10924 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1608 · 2026-05-20T06:36:42.175936+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -10; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config* /home/ubuntu/.agent-ml-research-idea_gen_0509_3/settings* 2>/dev/null | head -10",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -10; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config* /home/ubuntu/.agent-ml-research-idea_gen_0509_3/settings* 2>/dev/null | head -10",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 1609 · 2026-05-20T06:36:42.326862+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1610 · 2026-05-20T06:36:46.042911+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/ -maxdepth 2 -name \"config*\" -o -name \"settings*\" 2>/dev/null | head -10",
  "description": "Find config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/ -maxdepth 2 -name \"config*\" -o -name \"settings*\" 2>/dev/null | head -10",
    "description": "Find config files"
  }
}
```

</details>

---


### Tool result

_source line 1611 · 2026-05-20T06:36:46.093905+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1612 · 2026-05-20T06:36:48.866406+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/ 2>/dev/null",
  "description": "List config directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/ 2>/dev/null",
    "description": "List config directory"
  }
}
```

</details>

---


### Tool result

_source line 1613 · 2026-05-20T06:36:48.917356+00:00_

approvals.yaml
backend.yaml
claude_sessions.json
crons.yaml
email_tokens.json
feishu.yaml
keepalive.json
mcp_config.json
mcp_config_briefer.json
mcp_config_director.json
mcp_config_dream_review_director.json
mcp_config_idea_reviewer.json
mcp_config_no_project.json
mcp_config_paper_agent.json
mcp_config_paper_audit_review_visual.json
mcp_config_review_director.json
mcp_config_review_reviewer_1.json
mcp_config_review_reviewer_2.json
mcp_config_reviewer.json
mcp_config_worker_011f2b23898fb17ffb1bfb29640bf50c.json
mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
mcp_config_worker_12093ef55c63229acbf88fd2b9106dce.json
mcp_config_worker_14c478d49028dd51e7fb6eba96596197.json
mcp_config_worker_14d296b01755362efedfab08bc7a4e38.json
mcp_config_worker_23f8ac73af961b0e39b1e25bb840f210.json
mcp_config_worker_26d48c4b05fa14163ebc1207f60b537a.json
mcp_config_worker_29834432f6498e7996daf9a6d4e8eda9.json
mcp_config_worker_33c066fe8f41bfaa9b9c844bb47eca4f.json
mcp_config_worker_34467933ed5c0782ad72826a9574d432.json
mcp_config_worker_34a94861e96b7887a157fa6d27e375e0.json
mcp_config_worker_3683e51e3c097c93488562d683342ec7.json
mcp_config_worker_372644b6780be0a53d254a839199d98e.json
mcp_config_worker_3ab953c77b6b0e7621a87cc89f47e64a.json
mcp_config_worker_3fd80bece90c3cfcb2e818575e6db602.json
mcp_config_worker_41d735d56651d19d6a7920071cdacb59.json
mcp_config_worker_421decd2032b14f2ef6566c2172240c1.json
mcp_config_worker_4d158a24aca8bf8fc20a9d2202c01694.json
mcp_config_worker_4dc52b836d4b7ae24139c5fa8c29372a.json
mcp_config_worker_4ecfa604e6eadfe651bee18f1a37e18b.json
mcp_config_worker_5304abbd56fd7a7f12edca904ca28ec0.json
mcp_config_worker_567fac45f9ef5ad1a9223cbb3364faf1.json
mcp_config_worker_5cdb8c7e97717761673d752ba8651d6d.json
mcp_config_worker_5e1d568c11fca979b31d7c13b36d8cd9.json
mcp_config_worker_5fb1f955b45e38e31789286a1790398d.json
mcp_config_worker_6679bd63c74f529fddfcffaa0a492c96.json
mcp_config_worker_6774a1cf85
…[truncated 1948 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1614 · 2026-05-20T06:36:52.532923+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/solver-trace-ablation.yaml 2>/dev/null || cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/solver-trace-ablation/config.yaml 2>/dev/null || echo \"Not found\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/ 2>/dev/null | head -5",
  "description": "Find project-specific config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/solver-trace-ablation.yaml 2>/dev/null || cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/solver-trace-ablation/config.yaml 2>/dev/null || echo \"Not found\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/ 2>/dev/null | head -5",
    "description": "Find project-specific config"
  }
}
```

</details>

---


### Tool result

_source line 1615 · 2026-05-20T06:36:52.634663+00:00_

execution:
  gpu_constraint:
  - westd-39279:cuda:0
  gpu_ids:
  - cuda:0
  project_path: /root/solver-trace-ablation
  servers:
  - account: root
    server: westd-39279
feishu:
  chat_id: oc_a771c2a33d631dd40256ecd5c3a6648e
  operational_chat_id: oc_8f0788a2307711c1b7fbf59b4cbe0473
  review_mode: fresh
  review_paper_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex
  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf
  review_round: 17
  review_supplementary_paths: ''
  submission_chat_id: oc_5abafbb382eb7c81e8a38090e46323e7
project:
  created_at: '2026-05-13T17:31:18.377Z'
  description: Solver Trace Ablation for Cross-Logic GRPO Training of Neurosymbolic
    Formalizers
  name: solver-trace-ablation
  phase: research
  source_idea_id: idea_010
venue: emnlp-2026
min_necessary_circuit_css.yaml
min_necessary_circuit_css.yaml.bak-desc-fix
solver-trace-ablation.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1616 · 2026-05-20T06:37:18.711304+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "solver-trace-ablation",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "solver-trace-ablation",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 1617 · 2026-05-20T06:37:43.880633+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 25169
}
```

</details>

---


### Tool call

_source line 1618 · 2026-05-20T06:37:44.032087+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计 + 统计分析**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (Long Paper, via ACL Rolling Review)\n- **截止日期**: 2026-05-25 (ARR submission)\n- **页数限制**: 正文 ≤ 8 页，参考文献不限，Limitations 不计入页数\n- **模板**: ACL template (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n## 论文概述\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，用于量化 GRPO 训练的神经符号推理器中的结构退化。核心发现：(1) ISR 作为诊断指标揭示了执行率隐藏的 99.5% 结构坍塌；(2) ISR 作为训练奖励产生 Goodhart 效应（TS 放大 ~5×）；(3) 跨逻辑/跨数据集泛化显示 dataset-dependent 结果。\n\n## 你的审查重点\n\n### 1. 方法论严谨性\n- STA/ISR 方法是否有明显技术缺陷？LOO 假设（独立性）的局限性是否充分讨论？\n- ISR 定义（Eq. 1）是否清晰无歧义？与 semantic faithfulness 的区分是否充分？\n- 奖励条件设计（6 条件）是否合理？对照组（random control, SFT baseline）是否充分？\n- 乘法耦合（multiplicative coupling）的 confound 是否充分处理？\n\n### 2. 实验设计\n- 只用 Qwen3-4B 一个模型，外加 LLaMA-3.2-3B 冷启动失败 —— 是否构成 generalization concern？\n- 3 seeds 是否足够？高方差（PR σ=47pp）下的结论可靠性？\n- 500 训练样本 + 100 评估样本的数据规模是否影响结论强度？\n- ProofFOL 作为 silver-standard 数据集（GPT-4o 翻译）的质量问题是否影响 cross-dataset 结论？\n\n### 3. 统计分析\n- Fisher exact tests 的使用是否恰当？样本量是否足够？\n- Bonferroni 校正是否过于保守或过于宽松？\n- ProofFOL 的 p=0.10 结果标注为 \"exploratory\" 是否合适？\n- Premise-count confound 的 deconfounding 分析是否充分？\n- 置信区间和效应量报告是否完整？\n\n### 4. 可重复性\n- 实验设置是否足够详细可重复？\n- seed 43 使用 sampling eval 而非 greedy —— 对结论的影响是否充分说明？\n- ISR seeds 43/44 checkpoints 被删除无法 audit —— 是否是问题？\n\n请按以下格式输出审稿报告：\n```\n## Summary（2-3 句概述）\n\n## Strengths（逐条列出优点）\n\n## Weaknesses（逐条列出缺点，标注 [Must-Fix] / [Should-Fix] / [Minor]）\n\n## Questions（需要作者澄清的问题）\n\n## Missing References（遗漏的相关工作）\n\n## Overall Assessment（评分 + 置信度 + 简要理由）\n```\n\n评分标准（EMNLP 2026 ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计 + 统计分析**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (Long Paper, via ACL Rolling Review)\n- **截止日期**: 2026-05-25 (ARR submission)\n- **页数限制**: 正文 ≤ 8 页，参考文献不限，Limitations 不计入页数\n- **模板**: ACL template (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n## 论文概述\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，用于量化 GRPO 训练的神经符号推理器中的结构退化。核心发现：(1) ISR 作为诊断指标揭示了执行率隐藏的 99.5% 结构坍塌；(2) ISR 作为训练奖励产生 Goodhart 效应（TS 放大 ~5×）；(3) 跨逻辑/跨数据集泛化显示 dataset-dependent 结果。\n\n## 你的审查重点\n\n### 1. 方法论严谨性\n- STA/ISR 方法是否有明显技术缺陷？LOO 假设（独立性）的局限性是否充分讨论？\n- ISR 定义（Eq. 1）是否清晰无歧义？与 semantic faithfulness 的区分是否充分？\n- 奖励条件设计（6 条件）是否合理？对照组（random control, SFT baseline）是否充分？\n- 乘法耦合（multiplicative coupling）的 confound 是否充分处理？\n\n### 2. 实验设计\n- 只用 Qwen3-4B 一个模型，外加 LLaMA-3.2-3B 冷启动失败 —— 是否构成 generalization concern？\n- 3 seeds 是否足够？高方差（PR σ=47pp）下的结论可靠性？\n- 500 训练样本 + 100 评估样本的数据规模是否影响结论强度？\n- ProofFOL 作为 silver-standard 数据集（GPT-4o 翻译）的质量问题是否影响 cross-dataset 结论？\n\n### 3. 统计分析\n- Fisher exact tests 的使用是否恰当？样本量是否足够？\n- Bonferroni 校正是否过于保守或过于宽松？\n- ProofFOL 的 p=0.10 结果标注为 \"exploratory\" 是否合适？\n- Premise-count confound 的 deconfounding 分析是否充分？\n- 置信区间和效应量报告是否完整？\n\n### 4. 可重复性\n- 实验设置是否足够详细可重复？\n- seed 43 使用 sampling eval 而非 greedy —— 对结论的影响是否充分说明？\n- ISR seeds 43/44 checkpoints 被删除无法 audit —— 是否是问题？\n\n请按以下格式输出审稿报告：\n```\n## Summary（2-3 句概述）\n\n## Strengths（逐条列出优点）\n\n## Weaknesses（逐条列出缺点，标注 [Must-Fix] / [Should-Fix] / [Minor]）\n\n## Questions（需要作者澄清的问题）\n\n## Missing References（遗漏的相关工作）\n\n## Overall Assessment（评分 + 置信度 + 简要理由）\n```\n\n评分标准（EMNLP 2026 ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit"
  }
}
````

</details>

---


### Tool result

_source line 1619 · 2026-05-20T06:38:04.402626+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20370
}
```

</details>

---


### Tool call

_source line 1620 · 2026-05-20T06:38:04.553553+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "你是 Reviewer 2，负责 **新颖性 + 相关工作完整性 + 写作质量 + 格式合规**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (Long Paper, via ACL Rolling Review)\n- **截止日期**: 2026-05-25 (ARR submission)\n- **页数限制**: 正文 ≤ 8 页，参考文献不限，Limitations 不计入页数\n- **模板**: ACL template (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n## 论文概述\n本文提出 Solver Trace Ablation (STA)，一种基于 LOO 消融的诊断方法，量化 GRPO 训练的神经符号推理器中的结构退化。核心发现：ISR 作为诊断揭示 99.5% 结构坍塌；ISR 作为奖励产生 Goodhart 效应；跨域泛化显示 dataset-dependent 结果。使用 Qwen3-4B，6 种奖励条件，3 seeds，2 种逻辑类型，2 个数据集族。\n\n## 你的审查重点\n\n### 1. 新颖性评估\n- STA 本身的技术新颖性（LOO ablation 是标准技术）—— 新颖性主要来自应用还是方法？\n- Goodhart 效应在 structural diagnostic 上的发现是否真正 novel？\n- 8 种 hacking mode 分类法的价值 —— 是否仅为 case study 级别的描述性发现？\n- 与 Kim et al. (2026) \"Do LLMs Game Formalization?\" 的区分是否清晰充分？\n- 与 Khalifa et al. (2026) Countdown-Code 的对比？\n- 与 Helff et al. (2026) LLMs Gaming Verifiers 的区分？\n\n### 2. 相关工作完整性\n- 是否遗漏了重要的 neurosymbolic reasoning 工作？\n- 是否遗漏了重要的 reward hacking/Goodhart 文献？\n- Process reward model 文献覆盖是否充分？\n- 形式验证（formal verification）方向的 RL 工作（如 Lean 4 相关）是否需要讨论？\n- 引用是否存在可疑条目（hallucinated references）？\n\n### 3. 写作质量\n- Abstract 是否过长或信息过载？（当前 abstract 很密集）\n- Introduction 结构是否清晰？Contribution 陈述是否准确？\n- 论文整体叙事是否连贯？从诊断→奖励→跨域 的逻辑链是否顺畅？\n- 术语使用是否一致（ISR, ISR*, STA, prove rate 等）？\n- 表格/图片质量和可读性？\n- 信息密度是否过高导致可读性下降？\n\n### 4. 格式合规（EMNLP 2026 / ARR）\n- 正文是否 ≤ 8 页？\n- 是否使用正确的 ACL 模板？\n- 匿名是否完整（无作者信息泄露）？\n- Limitations section 是否存在且内容充分？\n- 引用格式是否正确（natbib）？\n- 附录内容是否合规？\n\n### 5. 论文定位\n- 这篇论文是 negative result / cautionary tale —— EMNLP 是否是合适的 venue？\n- 论文的 practical impact 是什么？读者能从中获得什么 actionable insight？\n- 是否更适合作为 workshop paper 或 Findings？\n\n请按以下格式输出审稿报告：\n```\n## Summary（2-3 句概述）\n\n## Strengths（逐条列出优点）\n\n## Weaknesses（逐条列出缺点，标注 [Must-Fix] / [Should-Fix] / [Minor]）\n\n## Questions（需要作者澄清的问题）\n\n## Missing References（遗漏的相关工作）\n\n## Overall Assessment（评分 + 置信度 + 简要理由）\n```\n\n评分标准（EMNLP 2026 ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "你是 Reviewer 2，负责 **新颖性 + 相关工作完整性 + 写作质量 + 格式合规**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (Long Paper, via ACL Rolling Review)\n- **截止日期**: 2026-05-25 (ARR submission)\n- **页数限制**: 正文 ≤ 8 页，参考文献不限，Limitations 不计入页数\n- **模板**: ACL template (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n## 论文概述\n本文提出 Solver Trace Ablation (STA)，一种基于 LOO 消融的诊断方法，量化 GRPO 训练的神经符号推理器中的结构退化。核心发现：ISR 作为诊断揭示 99.5% 结构坍塌；ISR 作为奖励产生 Goodhart 效应；跨域泛化显示 dataset-dependent 结果。使用 Qwen3-4B，6 种奖励条件，3 seeds，2 种逻辑类型，2 个数据集族。\n\n## 你的审查重点\n\n### 1. 新颖性评估\n- STA 本身的技术新颖性（LOO ablation 是标准技术）—— 新颖性主要来自应用还是方法？\n- Goodhart 效应在 structural diagnostic 上的发现是否真正 novel？\n- 8 种 hacking mode 分类法的价值 —— 是否仅为 case study 级别的描述性发现？\n- 与 Kim et al. (2026) \"Do LLMs Game Formalization?\" 的区分是否清晰充分？\n- 与 Khalifa et al. (2026) Countdown-Code 的对比？\n- 与 Helff et al. (2026) LLMs Gaming Verifiers 的区分？\n\n### 2. 相关工作完整性\n- 是否遗漏了重要的 neurosymbolic reasoning 工作？\n- 是否遗漏了重要的 reward hacking/Goodhart 文献？\n- Process reward model 文献覆盖是否充分？\n- 形式验证（formal verification）方向的 RL 工作（如 Lean 4 相关）是否需要讨论？\n- 引用是否存在可疑条目（hallucinated references）？\n\n### 3. 写作质量\n- Abstract 是否过长或信息过载？（当前 abstract 很密集）\n- Introduction 结构是否清晰？Contribution 陈述是否准确？\n- 论文整体叙事是否连贯？从诊断→奖励→跨域 的逻辑链是否顺畅？\n- 术语使用是否一致（ISR, ISR*, STA, prove rate 等）？\n- 表格/图片质量和可读性？\n- 信息密度是否过高导致可读性下降？\n\n### 4. 格式合规（EMNLP 2026 / ARR）\n- 正文是否 ≤ 8 页？\n- 是否使用正确的 ACL 模板？\n- 匿名是否完整（无作者信息泄露）？\n- Limitations section 是否存在且内容充分？\n- 引用格式是否正确（natbib）？\n- 附录内容是否合规？\n\n### 5. 论文定位\n- 这篇论文是 negative result / cautionary tale —— EMNLP 是否是合适的 venue？\n- 论文的 practical impact 是什么？读者能从中获得什么 actionable insight？\n- 是否更适合作为 workshop paper 或 Findings？\n\n请按以下格式输出审稿报告：\n```\n## Summary（2-3 句概述）\n\n## Strengths（逐条列出优点）\n\n## Weaknesses（逐条列出缺点，标注 [Must-Fix] / [Should-Fix] / [Minor]）\n\n## Questions（需要作者澄清的问题）\n\n## Missing References（遗漏的相关工作）\n\n## Overall Assessment（评分 + 置信度 + 简要理由）\n```\n\n评分标准（EMNLP 2026 ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit"
  }
}
````

</details>

---


### Tool result

_source line 1621 · 2026-05-20T06:38:06.322900+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1769
}
```

</details>

---


### Assistant

_source line 1622 · 2026-05-20T06:38:15.092652+00:00_

**Round 1 已启动**：
- ✅ 视觉审查 Agent 已派发（fire-and-forget）
- ✅ Reviewer 1（方法/实验/统计）已分配
- ✅ Reviewer 2（新颖性/相关工作/写作/格式）已分配
- ⏭️ 无外部审稿配置，跳过 Stanford Agentic Reviewer

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 133

## Round 133

2 recorded events


### User

_source line 1623 · 2026-05-20T06:44:10.586623+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning

**审查侧重**: 新颖性 + 相关工作完整性 + 写作质量 + 格式合规

---

## Summary

本文提出 Solver Trace Ablation (STA)，将软件测试中的 LOO 变异消融应用于 GRPO 训练的神经符号推理器，通过 ISR 指标量化形式化输出的结构质量。核心发现：(1) exec-only GRPO 训练导致 99.5% 结构坍塌，(2) ISR 纳入奖励引发 Goodhart 效应，(3) 跨域泛化结果依赖数据集。实验基于 Qwen3-4B，6 种奖励条件 × 3 seeds × 2 种逻辑类型 × 2 个数据集族。

---

## Strengths

**S1. 创造性的跨学科连接。** 将 mutation testing 的 LOO 消融迁移到神经符号 RL 诊断，是新颖的 framing（Section 3.2, Algorithm 1）。

**S2. 系统的实验设计。** 6 种奖励条件 × 3 seeds × 2 逻辑后端 × 2 数据集族。100-step BL checkpoint 和 matched random control 体现方法论审慎。

**S3. 重要的 cautionary finding。** exec-only GRPO PR 达 97% 时 ISR 坍塌至 ≤1.4%（Section 4.1, Figure 2），对 RLVR 社区有直接警示价值。

**S4. Goodhart 效应的实证。** ISR-as-reward 的 Goodhart advantage 从 1.06× 退化到与 random 无显著差异（Section 4.3），且提供了 multiplicative coupling 机制解释。

**S5. Hacking taxonomy 实用。** 8 种 hacking mode（Table 2, Appendix D）为未来工作提供可检查的 pattern checklist。

**S6. 引用完整。** 39 篇引用无 orphan/missing，所有近期关键工作已覆盖。

---

## Weaknesses

**W1 [Must-Fix] 单模型局限性严重削弱泛化声明。**
- 位置：全文实验仅 Qwen3-4B；Limitations Section 6
- 问题：标题和 abstract 使用泛化措辞，但证据仅来自一个模型。LLaMA-3.2-3B 的 cold-start failure 是能力不足，不是退化泛化验证。
- 建议：增加至少一个不同架构模型的关键条件（exec-only + ISR β=0.1），或明确缩窄 claim scope。

**W2 [Must-Fix] 与 Kim et al. (2026) 区分不充分。**
- 位置：Related Work Section 2 第 17 行
- 问题：Kim et al. 同样研究 FOLIO 上的 formalization gaming，论文仅一句话区分（training vs. inference）。核心观察高度重叠。
- 建议：增加系统对比 paragraph/table，说明两者在诊断目标、实验设置、发现范围的差异和互补性。

**W3 [Should-Fix] Goodhart 发现可预测性削弱新颖性。**
- 位置：Section 4.3
- 问题：将诊断指标直接纳入奖励后观察 Goodhart 效应在理论上高度可预测。更有价值的问题是是否存在 Goodhart-resistant 的 ISR 变体，论文未探索。
- 建议：将 Goodhart 定位为"验证性实验"，并讨论可能的 resistant 变体。

**W4 [Should-Fix] 3 seeds + 高方差导致统计效力不足。**
- 位置：Table 7, Section 4.1
- 问题：ISR β=0.1 下 3 seeds 收敛到定性完全不同的模式，PR 跨 0.18-0.95。3 seeds 不足以刻画 multi-attractor landscape。
- 建议：增至 5-8 seeds，或将 seed-level 分析定位为 exploratory。

**W5 [Should-Fix] Abstract 信息过载。**
- 位置：Page 1
- 问题：Abstract 压缩过多数字和发现，可读性下降。
- 建议：精简至 150-180 词，聚焦核心 message。

**W6 [Should-Fix] 缺乏 actionable mitigation。**
- 位置：Section 5
- 问题：Mitigation directions 仅占 3.5 行，无实验验证。诊断之后缺乏"怎么办"。
- 建议：增加轻量 proof-of-concept（如 ISR filter + retrain）。

**W7 [Minor] 术语密度过高。** ISR/ISR*/STA/CE/TS/PG/CI/N-H 等缩写过多，建议减少正文缩写依赖。

**W8 [Minor] Figure 2, 5 可读性不足。** 字体过小，颜色区分度有限。

**W9 [Minor] FOLIO bib 年份 (2024) 与首发 (2022) 不一致——发表年份正确但应确保全文一致。

---

## Questions

**Q1.** ISR=0 不区分"冗余"和"退化"——高度冗余但语义正确的形式化也会 ISR→0。如何量化冗余 vs. 退化比例？

**Q2.** ProofFOL silver 翻译 noise 是否导致 ISR 坍塌部分归因于数据质量？

**Q3.** LOO 的 n+1 开销如何 scale 到更长 formalization（如 Lean 4 证明）？

**Q4.** Random β=0.1 的对照价值是什么？ISR≈0 是 trivially expected。

**Q5.** Hacking mode classifier 的 precision/recall？50 样本验证的置信区间很宽。

---

## Missing References

1. **Xie et al. (2025). "Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification."** arXiv:2601.22642。使用 formal-logic verification 作为训练信号，发现 reward hacking。

2. **"Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts"** (2025, arXiv:2601.11061)。RLVR memorization shortcut 的机制分析。

3. **"Reward Hacking Mitigation using Verifiable Composite Rewards"** (2025, arXiv:2509.15557)。composite reward 缓解 hacking 方法。

4. **Lean 4 RL 工作**（Kimina-Prover, Leanabell-Prover）——形式验证 RL 的 parallel track，Limitations 中应提及。

---

## Overall Assessment

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Overall** | **3.0** (Findings) | 诊断贡献真实但方法增量、泛化不足、无解法 |
| Soundness | 3.5/5 | 设计系统但单模型+3seeds+小数据集限制结论可靠性 |
| Excitement | 2.5/5 | LOO 不新、Goodhart 可预测、无 actionable 解法 |
| Reproducibility | 4/5 | 细节充分，代码承诺开源 |
| Confidence | 4/5 | 熟悉领域，仔细阅读全文及附录 |

**一句话总结**: 创造性的诊断工具揭示了真实问题，但单模型实验、可预测的 Goodhart 发现、缺乏解法使其止步于 Findings 水平。Rebuttal 中增加第二模型、深化 Kim et al. 对比、提供 mitigation PoC 可能提升至 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1624 · 2026-05-20T06:44:17.379139+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 134

## Round 134

2 recorded events


### User

_source line 1625 · 2026-05-20T06:44:20.251546+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**评分摘要**：Overall 3.0 (Findings)，Soundness 3.5，Excitement 2.5，Reproducibility 4.0，Confidence 4/5。

**核心判断**：论文的诊断工具（STA/ISR）是创造性的跨学科贡献，结构退化的发现对 RLVR 社区有警示价值。但两个 Must-Fix 问题制约了评分：(1) 单模型（Qwen3-4B）无法支撑论文标题级别的泛化声明，(2) 与 Kim et al. (2026) 的区分不够深入。此外，Goodhart 发现的可预测性、3 seeds 的统计效力不足、以及缺乏 actionable mitigation 实验使论文止步于 Findings 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1626 · 2026-05-20T06:44:27.758239+00:00_

Reviewer 2 报告已收到，评分 3.0 (Findings)。等待 Reviewer 1 报告，收齐后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 135

## Round 135

6 recorded events


### User

_source line 1627 · 2026-05-20T06:44:29.266106+00:00_

[Reviewer 1 审稿意见]:
## Summary

本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，通过 Indispensable Structure Record (ISR) 指标量化 GRPO 训练的神经符号推理器中的结构退化。核心发现：(1) 执行率 93-96% 掩盖了 ISR 从 0.642 降至近零的结构性坍塌；(2) ISR 作为训练奖励产生 Goodhart 效应（TS 放大 ~5×）；(3) 跨数据集泛化呈 dataset-dependent 结果。论文定义了 8 种 hacking 模式分类法，用 3 seeds × 6 reward conditions × 2 datasets 进行了系统实验。

## Strengths

**S1. 诊断框架新颖且有实际价值。** STA/ISR 揭示了一个被执行率指标完全隐藏的问题——GRPO 训练的形式化器在 prove rate 持续上升时发生结构性退化。这一"execution-only blind spot"（§1）的发现具有重要的方法论意义，对 neurosymbolic RL 社区有直接价值。

**S2. Hacking 分类法系统详尽。** 8 种 hacking 模式（CE/TS/PG/CI 等，Appendix D.1-D.9）每种都有 FOL/Prolog 示例、ISR 交互分析和检测标准。这不是简单列举，而是提供了一套可操作的诊断工具。Two-stage 分类流程（text matching + functional analysis）有 50 样本人工验证（Appendix D）。

**S3. 负面结果的诚实报告。** ISR-as-reward 的 Goodhart 效应（§4.3）、LLaMA-3.2-3B 冷启动失败（Appendix E.4）、ProofFOL p=0.10 标为 exploratory、checkpoint 被删除无法审计——这些透明披露增强了论文可信度。

**S4. 统计分析框架合理。** Fisher exact tests + Bonferroni 校正（14 comparisons, α≈0.0036）、Cochran-Mantel-Haenszel 分层检验、premise-count deconfounding（Table 5, Appendix C）构成了较为完整的统计分析。

**S5. 写作质量高，叙事结构清晰。** Claim-evidence 对应严谨，每个核心声明都有实验支撑。Figure 2-5 的 trajectory 可视化有效传达了关键发现。

## Weaknesses

**W1 [Must-Fix] 单模型 + 3 seeds：核心声明的泛化性严重不足。**
- 具体位置：§4.1 Setup, §6 Limitations
- 问题：全部实验基于 Qwen3-4B 一个模型，LLaMA-3.2-3B 仅作为冷启动失败的 negative case（Appendix E.4）。3 seeds 展现了质性完全不同的行为（seed 42 reward collapse/PR=0.18, seed 43 CE shortcutting/PR=0.86, seed 44 pure TS Goodhart/PR=0.95; Table 7 p.19），PR σ=47pp 是巨大的方差。在 N=1 模型、N=3 seeds 且 seeds 间质性差异巨大的情况下，论文的核心定量声明（如摘要中 "≤1.4% genuine"、"99.5% structural collapse"）难以被视为稳健的统计结论。
- 为什么影响接收：Reviewer 无法判断这些发现是 Qwen3-4B 的特性还是 GRPO neurosymbolic 训练的通用现象。ACL ARR Soundness 标准要求 "sufficient support for main claims"，单模型设计对 "reveals structural degeneration in GRPO-trained neurosymbolic reasoning" 这一通用性声明的支撑不足。
- 建议：至少增加 1-2 个不同架构/规模的模型（如 7B/14B 级别），或将 claims 明确限定为 "on Qwen3-4B"。增加 seeds 至 5-8 个以降低 σ。

**W2 [Must-Fix] 摘要/标题中的定量声明追溯困难，存在潜在误导。**
- 具体位置：Abstract ("≤1.4% genuine in converged seeds"), §1 ("99.5% structural collapse")
- 问题：摘要声称 "ISR collapses to ≤1.4% genuine (in converged seeds)"，但 Table 7 中 exec-only 的 per-seed N-H% 分别为 5.6%（seed 42）、23.3%（seed 43）、0%（seed 44）。即使只看 "converged seeds"（seed 43/44），加权平均也远高于 1.4%。"99.5% structural collapse" 似乎来自 seed 42 的 ISR 从 0.642→0.003 的单 seed 轨迹（Figure 2），但这个 seed 恰好是 PR 最低的（0.18），用它代表整体是有选择偏差的。此外，Table 7 显示不同 seeds 使用了不同的训练步数（seed 42/43: 500 steps, seed 44: 1000 steps），使 pooled 统计更加复杂。
- 为什么影响接收：摘要是 reviewer/reader 的第一印象；如果 headline 数字无法从 tables 中直接追溯，会严重损害可信度。
- 建议：明确 "≤1.4%" 和 "99.5%" 的精确计算来源，标注这些数字来自哪些 seeds/steps 的哪些子集；或改用 3-seed mean±std 呈现。

**W3 [Must-Fix] ISR 作为诊断指标的根本局限：对 TS hacking 失效。**
- 具体位置：§4.2-4.3, Appendix D.5
- 问题：Seed 44 exec-only 达到 ISR=0.742（Table 7）但 N-H=0%——全部是 TS（tautological substitution）hacking。这说明 ISR 对 TS 类退化是盲目的：tautology P→P 的 LOO 消融天然产生 ISR≈1，因为每个 component 都是 "必要" 的。论文在 §4.2 和 hacking taxonomy 中讨论了这一点，但并未在 Method section（§3.2）中明确将其列为 ISR 的 known limitation。摘要 "ISR as a diagnostic reveals structural collapse hidden from execution rate" 的表述暗示 ISR 是一个通用诊断工具，但它实际上只能检测 CE/PG/CI 等特定类型的退化，对 TS 类退化需要额外的 text-match classifier 辅助。
- 为什么影响接收：这不仅是一个 caveat，而是影响到核心 contribution 的范围界定。ISR 的诊断能力比论文暗示的更窄。
- 建议：在 §3.2 明确说明 ISR 的检测盲区，将 ISR + hacking classifier 的组合作为完整诊断方案呈现，而非只突出 ISR 单指标。

**W4 [Should-Fix] LOO 独立性假设的局限讨论不充分。**
- 具体位置：§3.2 Algorithm 1, §6 Limitations
- 问题：ISR 的 LOO ablation 假设各 premise 独立贡献，但形式逻辑中 premises 经常存在链式依赖。例如在推理链 P→Q, Q→R 中证明 R：单独移除 P→Q 时 Q→R 仍可能通过其他路径或 Q 作为公理成立，导致 ISR 低估真实结构依赖。论文称 ISR 是 "conservative lower-bound"（§3.2），但未量化这个 lower bound 有多紧（gap 可以多大）。Limitations section 一句话带过 "The O(n) per-class LOO ablation is an observation, not a condition of test"，不够。
- 建议：在 Appendix 中加入对 ISR lower-bound tightness 的理论分析或实证估计（如在已知 ground-truth 结构的合成数据上比较 ISR vs 真实 necessity）。

**W5 [Should-Fix] 500 训练 + 100 评估样本的数据规模偏小。**
- 具体位置：§4.1, §6 Limitations
- 问题：500 训练样本、100 评估样本对于 RL 训练和统计推断都偏小。ISR 在 100 个 eval 样本上的估计精度有限（如 Table 1 中 N-H=4.7%，100 样本中仅 ~5 个 non-hacking sample）。ProofFOL 约 500 examples 的跨数据集实验同样受限于样本量。Limitations 提到 "the effect of training data scale on hacking prevalence...remains an open question"，但这不只是 future work——它直接影响当前结论的强度。
- 建议：至少在讨论中分析 data scale 对结论的 sensitivity。如果 compute budget 允许，增加 eval set 至 500+。

**W6 [Should-Fix] Fisher exact test 的独立性假设可能被违反。**
- 具体位置：Appendix D (statistical tests), Table 5
- 问题：Fisher exact test 要求样本独立，但论文将 3 seeds 的结果 pool 在一起检验。这 3 seeds 共享同一训练数据和模型架构，seed 间结果高度相关（同一 condition 下 seed 42/43/44 行为质性不同）。Pooling 可能人为膨胀样本量、缩小 p 值。论文使用了 Cochran-Mantel-Haenszel 分层检验（Appendix D），这是对的，但 main text 中主要引用的是 pooled Fisher test 结果。
- 建议：main text 中优先报告分层检验结果或 per-seed 检验，pooled 结果降为辅助。

**W7 [Should-Fix] 乘法耦合（multiplicative coupling）实验未充分 deconfound。**
- 具体位置：§3.3, §4.3, Appendix C
- 问题：奖励 r = r_exec · (1 + β·ISR) 的乘法结构意味着 ISR 奖励完全依赖于执行成功——execution 失败时 ISR 对梯度无贡献。这使得 ISR-as-reward 实验始终在 "execution 优先" 的约束下运行。论文讨论了这一点（Appendix C: "the multiplicative coupling means ISR optimization is always secondary to execution success"），但未测试加法耦合（r = r_exec + β·ISR）作为对照，无法分离 coupling structure 的影响。
- 建议：增加 additive coupling 对照条件，或在讨论中明确说明无法分离 multiplicative structure 的影响。

**W8 [Should-Fix] ProofFOL 数据质量问题可能 confound 跨数据集结论。**
- 具体位置：§4.4, Appendix A, Table 4
- 问题：ProofFOL 由 ProofWriter (Tafjord et al., 2021) 经 GPT-4o 翻译为 FOL（Table 4: "GPT-4o (silver)"），Prover9 verification filtering 保留 ~70% retention。但 GPT-4o 的翻译偏差（如倾向某些 predicate 结构）可能系统性地影响 ISR 和 hacking 模式。论文发现 "ProofFOL exec-only: structural degeneration generalizes, though mode distribution differs"（§4.4），但 mode distribution 差异可能部分源于 GPT-4o 翻译偏差而非真实的数据集差异。p=0.10 的 borderline 结果进一步削弱了跨数据集声明的可信度。
- 建议：讨论 GPT-4o 翻译可能引入的 systematic bias；理想情况下在一个 human-annotated FOL 数据集上验证。

**W9 [Minor] Seed 43 使用 sampling eval (temperature=0.7) 而非 greedy。**
- 具体位置：§4.1 footnote, Appendix E
- 问题：Seed 43 由于技术原因使用 sampling evaluation，引入额外方差。这使 cross-seed 比较不完全公平。论文声称 "changing eval does not change qualitative conclusions"，但未定量评估影响。
- 建议：补充 greedy vs sampling 对同一 checkpoint 的 ISR 差异估计。

**W10 [Minor] 分类器验证样本量偏小。**
- 具体位置：Appendix D
- 问题：Hacking mode 分类器的人工验证仅基于 50 个随机样本，precision >95%。50 样本下 95% precision 的 95% Wilson CI 约为 [85%, 99%]，区间较宽。
- 建议：增加验证样本至 100-200 个，或报告 confidence interval。

**W11 [Minor] ISR 与 downstream task accuracy 的相关性报告需澄清。**
- 具体位置：Abstract vs. Appendix C
- 问题：Abstract 报告 ISR 与 downstream accuracy "uncorrelated"，引用一个 p 值；Appendix C 报告 Spearman ρ=-0.039, p=0.187。请确认两处数字一致。此外，p=0.187 的解释为 "uncorrelated" 是合理的，但如果 abstract 处的 p 值不同，需要纠正。

## Questions

**Q1.** "≤1.4% genuine (in converged seeds)" 的精确计算：这个数字来自哪些 seeds、哪些 steps、哪些 condition 的哪些样本子集？请提供可追溯的 derivation。

**Q2.** Table 7 显示 exec-only 各 seed 训练步数不同（seed 42/43: 500 steps, seed 44: 1000 steps）。为什么不统一到相同步数再做 pooled comparison？这是否影响了 Table 1 的 aggregated 结果？

**Q3.** ISR 对 TS hacking 失效（seed 44: ISR=0.742 but N-H=0%）意味着 ISR 作为独立诊断指标的 false negative rate 可能很高。作者是否考虑过将 ISR + hacking classifier 组合为一个 unified metric，而非将两者分开讨论？

**Q4.** 乘法耦合下 ISR β=0.3 的 reward collapse（Table 10: seed 42 PR=0.18, ISR=0.141）——这是由于 β 过大导致的 reward scale 问题，还是 multiplicative coupling 的内在缺陷？是否测试过不同的 coupling 函数？

**Q5.** LLaMA-3.2-3B 冷启动失败（Appendix E.4）被解释为 "capability threshold"——但 LLaMA-3.2-3B 和 Qwen3-4B 在参数量上接近。是否考虑过这可能是 tokenizer/pretraining data 的差异而非 "capability" 差异？

**Q6.** 论文声称 STA "requires models with sufficient FOL generation capability"（§6）。这个 capability threshold 如何确定？是否有定量标准（如 baseline FOL accuracy > X%）？

## Missing References

1. **Geirhos et al. (2020), "Shortcut Learning in Deep Neural Networks," Nature Machine Intelligence**: 论文讨论了 reward hacking 和 shortcut 行为，但未引用 shortcut learning 领域的开创性综述。ISR 检测的结构退化本质上是 shortcut learning 在 neurosymbolic 场景的体现。

2. **Pang et al. (2024) 或其他 iterative RLHF 工作中的 reward over-optimization 实证研究**: 论文引用了 Gao et al. (2023) 的 scaling laws for reward overoptimization，但 RLHF 领域近期有更多关于 reward hacking 的实证工作值得对比。

3. **Anil et al. (2024) 或 Anthropic/DeepMind 关于 reward model 被 exploit 的实证研究**: 与本文 Goodhart 发现直接相关。

## Overall Assessment

**Overall: 3.5 (Borderline Conference)**
**Confidence: 4/5 (Quite sure)**

**理由**: 本文提出了一个新颖且有价值的诊断框架（STA/ISR），揭示了 GRPO 训练中被 prove rate 隐藏的结构退化——这是一个重要发现。Hacking 分类法详尽，Goodhart 效应的实验记录充分，写作质量高。

降分的主要原因是：(1) 单模型 + 3 seeds 的实验规模严重限制了结论的泛化性，特别是 seeds 间的极端方差使 aggregated claims 不够稳健；(2) ISR 对 TS 类 hacking 的盲区意味着其作为独立诊断指标的能力比论文标题/摘要暗示的更窄；(3) 摘要中的 headline 定量声明（≤1.4%、99.5%）难以从 tables 直接追溯，存在潜在误导。

如果 W1（增加模型）和 W2（修正 headline 数字的表述）能被解决，本文可以达到 Conference level (4.0)。当前版本更适合 Findings。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | 主要 claims 有实验支撑，但单模型+3seeds+高方差设计使定量声明可靠性受限；摘要 headline 数字追溯困难 |
| Excitement | 3.5/5 | 诊断框架新颖，hacking taxonomy 实用，揭示了一个真实且被忽视的问题；但 ISR 对 TS 盲区和实验规模限制了影响力 |
| Overall Assessment | 3.5/5 (Borderline Conference) | 有价值的诊断贡献，但实验规模和某些方法论问题需在 revision 中解决 |
| Confidence | 4/5 | 仔细阅读全文包括附录；熟悉 neurosymbolic reasoning 和 RL reward hacking 文献 |
| Reproducibility | 3/5 | 超参数表格完整（Table 3），但 seed 43/44 ISR checkpoints 被删除无法审计，seed 43 使用不同 eval 协议，不同 seeds 训练步数不一致 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1628 · 2026-05-20T06:45:30.275381+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n**审查侧重**: 新颖性 + 相关工作完整性 + 写作质量 + 格式合规\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，将软件测试中的 LOO 变异消融应用于 GRPO 训练的神经符号推理器，通过 ISR 指标量化形式化输出的结构质量。核心发现：(1) exec-only GRPO 训练导致 99.5% 结构坍塌，(2) ISR 纳入奖励引发 Goodhart 效应，(3) 跨域泛化结果依赖数据集。实验基于 Qwen3-4B，6 种奖励条件 × 3 seeds × 2 种逻辑类型 × 2 个数据集族。\n\n## Strengths\n\n**S1. 创造性的跨学科连接。** 将 mutation testing 的 LOO 消融迁移到神经符号 RL 诊断，是新颖的 framing（Section 3.2, Algorithm 1）。\n\n**S2. 系统的实验设计。** 6 种奖励条件 × 3 seeds × 2 逻辑后端 × 2 数据集族。100-step BL checkpoint 和 matched random control 体现方法论审慎。\n\n**S3. 重要的 cautionary finding。** exec-only GRPO PR 达 97% 时 ISR 坍塌至 ≤1.4%（Section 4.1, Figure 2），对 RLVR 社区有直接警示价值。\n\n**S4. Goodhart 效应的实证。** ISR-as-reward 的 Goodhart advantage 从 1.06× 退化到与 random 无显著差异（Section 4.3），且提供了 multiplicative coupling 机制解释。\n\n**S5. Hacking taxonomy 实用。** 8 种 hacking mode（Table 2, Appendix D）为未来工作提供可检查的 pattern checklist。\n\n**S6. 引用完整。** 39 篇引用无 orphan/missing，所有近期关键工作已覆盖。\n\n## Weaknesses\n\n**W1 [Must-Fix] 单模型局限性严重削弱泛化声明。**\n- 位置：全文实验仅 Qwen3-4B；Limitations Section 6\n- 问题：标题和 abstract 使用泛化措辞，但证据仅来自一个模型。LLaMA-3.2-3B 的 cold-start failure 是能力不足，不是退化泛化验证。\n- 建议：增加至少一个不同架构模型的关键条件（exec-only + ISR β=0.1），或明确缩窄 claim scope。\n\n**W2 [Must-Fix] 与 Kim et al. (2026) 区分不充分。**\n- 位置：Related Work Section 2 第 17 行\n- 问题：Kim et al. 同样研究 FOLIO 上的 formalization gaming，论文仅一句话区分（training vs. inference）。核心观察高度重叠。\n- 建议：增加系统对比 paragraph/table，说明两者在诊断目标、实验设置、发现范围的差异和互补性。\n\n**W3 [Should-Fix] Goodhart 发现可预测性削弱新颖性。**\n- 位置：Section 4.3\n- 问题：将诊断指标直接纳入奖励后观察 Goodhart 效应在理论上高度可预测。更有价值的问题是是否存在 Goodhart-resistant 的 ISR 变体，论文未探索。\n- 建议：将 Goodhart 定位为\"验证性实验\"，并讨论可能的 resistant 变体。\n\n**W4 [Should-Fix] 3 seeds + 高方差导致统计效力不足。**\n- 位置：Table 7, Section 4.1\n- 问题：ISR β=0.1 下 3 seeds 收敛到定性完全不同的模式，PR 跨 0.18-0.95。3 seeds 不足以刻画 multi-attractor landscape。\n- 建议：增至 5-8 seeds，或将 seed-level 分析定位为 exploratory。\n\n**W5 [Should-Fix] Abstract 信息过载。**\n- 位置：Page 1\n- 问题：Abstract 压缩过多数字和发现，可读性下降。\n- 建议：精简至 150-180 词，聚焦核心 message。\n\n**W6 [Should-Fix] 缺乏 actionable mitigation。**\n- 位置：Section 5\n- 问题：Mitigation directions 仅占 3.5 行，无实验验证。诊断之后缺乏\"怎么办\"。\n- 建议：增加轻量 proof-of-concept（如 ISR filter + retrain）。\n\n**W7 [Minor] 术语密度过高。** ISR/ISR*/STA/CE/TS/PG/CI/N-H 等缩写过多，建议减少正文缩写依赖。\n\n**W8 [Minor] Figure 2, 5 可读性不足。** 字体过小，颜色区分度有限。\n\n**W9 [Minor] FOLIO bib 年份 (2024) 与首发 (2022) 不一致——发表年份正确但应确保全文一致。\n\n## Questions\n\n**Q1.** ISR=0 不区分\"冗余\"和\"退化\"——高度冗余但语义正确的形式化也会 ISR→0。如何量化冗余 vs. 退化比例？\n\n**Q2.** ProofFOL silver 翻译 noise 是否导致 ISR 坍塌部分归因于数据质量？\n\n**Q3.** LOO 的 n+1 开销如何 scale 到更长 formalization（如 Lean 4 证明）？\n\n**Q4.** Random β=0.1 的对照价值是什么？ISR≈0 是 trivially expected。\n\n**Q5.** Hacking mode classifier 的 precision/recall？50 样本验证的置信区间很宽。\n\n## Missing References\n\n1. **Xie et al. (2025). \"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification.\"** arXiv:2601.22642。使用 formal-logic verification 作为训练信号，发现 reward hacking。\n\n2. **\"Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts\"** (2025, arXiv:2601.11061)。RLVR memorization shortcut 的机制分析。\n\n3. **\"Reward Hacking Mitigation using Verifiable Composite Rewards\"** (2025, arXiv:2509.15557)。composite reward 缓解 hacking 方法。\n\n4. **Lean 4 RL 工作**（Kimina-Prover, Leanabell-Prover）——形式验证 RL 的 parallel track，Limitations 中应提及。\n\n## Overall Assessment\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Overall** | **3.0** (Findings) | 诊断贡献真实但方法增量、泛化不足、无解法 |\n| Soundness | 3.5/5 | 设计系统但单模型+3seeds+小数据集限制结论可靠性 |\n| Excitement | 2.5/5 | LOO 不新、Goodhart 可预测、无 actionable 解法 |\n| Reproducibility | 4/5 | 细节充分，代码承诺开源 |\n| Confidence | 4/5 | 熟悉领域，仔细阅读全文及附录 |\n\n---\n\n请逐条回应上述所有 Weaknesses 和 Questions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n**审查侧重**: 新颖性 + 相关工作完整性 + 写作质量 + 格式合规\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，将软件测试中的 LOO 变异消融应用于 GRPO 训练的神经符号推理器，通过 ISR 指标量化形式化输出的结构质量。核心发现：(1) exec-only GRPO 训练导致 99.5% 结构坍塌，(2) ISR 纳入奖励引发 Goodhart 效应，(3) 跨域泛化结果依赖数据集。实验基于 Qwen3-4B，6 种奖励条件 × 3 seeds × 2 种逻辑类型 × 2 个数据集族。\n\n## Strengths\n\n**S1. 创造性的跨学科连接。** 将 mutation testing 的 LOO 消融迁移到神经符号 RL 诊断，是新颖的 framing（Section 3.2, Algorithm 1）。\n\n**S2. 系统的实验设计。** 6 种奖励条件 × 3 seeds × 2 逻辑后端 × 2 数据集族。100-step BL checkpoint 和 matched random control 体现方法论审慎。\n\n**S3. 重要的 cautionary finding。** exec-only GRPO PR 达 97% 时 ISR 坍塌至 ≤1.4%（Section 4.1, Figure 2），对 RLVR 社区有直接警示价值。\n\n**S4. Goodhart 效应的实证。** ISR-as-reward 的 Goodhart advantage 从 1.06× 退化到与 random 无显著差异（Section 4.3），且提供了 multiplicative coupling 机制解释。\n\n**S5. Hacking taxonomy 实用。** 8 种 hacking mode（Table 2, Appendix D）为未来工作提供可检查的 pattern checklist。\n\n**S6. 引用完整。** 39 篇引用无 orphan/missing，所有近期关键工作已覆盖。\n\n## Weaknesses\n\n**W1 [Must-Fix] 单模型局限性严重削弱泛化声明。**\n- 位置：全文实验仅 Qwen3-4B；Limitations Section 6\n- 问题：标题和 abstract 使用泛化措辞，但证据仅来自一个模型。LLaMA-3.2-3B 的 cold-start failure 是能力不足，不是退化泛化验证。\n- 建议：增加至少一个不同架构模型的关键条件（exec-only + ISR β=0.1），或明确缩窄 claim scope。\n\n**W2 [Must-Fix] 与 Kim et al. (2026) 区分不充分。**\n- 位置：Related Work Section 2 第 17 行\n- 问题：Kim et al. 同样研究 FOLIO 上的 formalization gaming，论文仅一句话区分（training vs. inference）。核心观察高度重叠。\n- 建议：增加系统对比 paragraph/table，说明两者在诊断目标、实验设置、发现范围的差异和互补性。\n\n**W3 [Should-Fix] Goodhart 发现可预测性削弱新颖性。**\n- 位置：Section 4.3\n- 问题：将诊断指标直接纳入奖励后观察 Goodhart 效应在理论上高度可预测。更有价值的问题是是否存在 Goodhart-resistant 的 ISR 变体，论文未探索。\n- 建议：将 Goodhart 定位为\"验证性实验\"，并讨论可能的 resistant 变体。\n\n**W4 [Should-Fix] 3 seeds + 高方差导致统计效力不足。**\n- 位置：Table 7, Section 4.1\n- 问题：ISR β=0.1 下 3 seeds 收敛到定性完全不同的模式，PR 跨 0.18-0.95。3 seeds 不足以刻画 multi-attractor landscape。\n- 建议：增至 5-8 seeds，或将 seed-level 分析定位为 exploratory。\n\n**W5 [Should-Fix] Abstract 信息过载。**\n- 位置：Page 1\n- 问题：Abstract 压缩过多数字和发现，可读性下降。\n- 建议：精简至 150-180 词，聚焦核心 message。\n\n**W6 [Should-Fix] 缺乏 actionable mitigation。**\n- 位置：Section 5\n- 问题：Mitigation directions 仅占 3.5 行，无实验验证。诊断之后缺乏\"怎么办\"。\n- 建议：增加轻量 proof-of-concept（如 ISR filter + retrain）。\n\n**W7 [Minor] 术语密度过高。** ISR/ISR*/STA/CE/TS/PG/CI/N-H 等缩写过多，建议减少正文缩写依赖。\n\n**W8 [Minor] Figure 2, 5 可读性不足。** 字体过小，颜色区分度有限。\n\n**W9 [Minor] FOLIO bib 年份 (2024) 与首发 (2022) 不一致——发表年份正确但应确保全文一致。\n\n## Questions\n\n**Q1.** ISR=0 不区分\"冗余\"和\"退化\"——高度冗余但语义正确的形式化也会 ISR→0。如何量化冗余 vs. 退化比例？\n\n**Q2.** ProofFOL silver 翻译 noise 是否导致 ISR 坍塌部分归因于数据质量？\n\n**Q3.** LOO 的 n+1 开销如何 scale 到更长 formalization（如 Lean 4 证明）？\n\n**Q4.** Random β=0.1 的对照价值是什么？ISR≈0 是 trivially expected。\n\n**Q5.** Hacking mode classifier 的 precision/recall？50 样本验证的置信区间很宽。\n\n## Missing References\n\n1. **Xie et al. (2025). \"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification.\"** arXiv:2601.22642。使用 formal-logic verification 作为训练信号，发现 reward hacking。\n\n2. **\"Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts\"** (2025, arXiv:2601.11061)。RLVR memorization shortcut 的机制分析。\n\n3. **\"Reward Hacking Mitigation using Verifiable Composite Rewards\"** (2025, arXiv:2509.15557)。composite reward 缓解 hacking 方法。\n\n4. **Lean 4 RL 工作**（Kimina-Prover, Leanabell-Prover）——形式验证 RL 的 parallel track，Limitations 中应提及。\n\n## Overall Assessment\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Overall** | **3.0** (Findings) | 诊断贡献真实但方法增量、泛化不足、无解法 |\n| Soundness | 3.5/5 | 设计系统但单模型+3seeds+小数据集限制结论可靠性 |\n| Excitement | 2.5/5 | LOO 不新、Goodhart 可预测、无 actionable 解法 |\n| Reproducibility | 4/5 | 细节充分，代码承诺开源 |\n| Confidence | 4/5 | 熟悉领域，仔细阅读全文及附录 |\n\n---\n\n请逐条回应上述所有 Weaknesses 和 Questions。"
  }
}
```

</details>

---


### Tool result

_source line 1629 · 2026-05-20T06:46:05.526661+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 35251
}
```

</details>

---


### Tool call

_source line 1630 · 2026-05-20T06:46:05.728023+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，通过 ISR 指标量化 GRPO 训练的神经符号推理器中的结构退化。核心发现：(1) 执行率 93-96% 掩盖了 ISR 从 0.642 降至近零的结构性坍塌；(2) ISR 作为训练奖励产生 Goodhart 效应（TS 放大 ~5×）；(3) 跨数据集泛化呈 dataset-dependent 结果。论文定义了 8 种 hacking 模式分类法，用 3 seeds × 6 reward conditions × 2 datasets 进行了系统实验。\n\n## Strengths\n\n**S1. 诊断框架新颖且有实际价值。** STA/ISR 揭示了一个被执行率指标完全隐藏的问题——GRPO 训练的形式化器在 prove rate 持续上升时发生结构性退化。\n\n**S2. Hacking 分类法系统详尽。** 8 种 hacking 模式每种都有 FOL/Prolog 示例、ISR 交互分析和检测标准。\n\n**S3. 负面结果的诚实报告。** ISR-as-reward 的 Goodhart 效应、LLaMA-3.2-3B 冷启动失败、ProofFOL p=0.10 标为 exploratory、checkpoint 被删除无法审计——这些透明披露增强了论文可信度。\n\n**S4. 统计分析框架合理。** Fisher exact tests + Bonferroni 校正 + CMH 分层检验 + premise-count deconfounding。\n\n**S5. 写作质量高，叙事结构清晰。**\n\n## Weaknesses\n\n**W1 [Must-Fix] 单模型 + 3 seeds：核心声明的泛化性严重不足。**\n- 全部实验基于 Qwen3-4B 一个模型。3 seeds 展现质性完全不同的行为（seed 42 reward collapse/PR=0.18, seed 43 CE shortcutting/PR=0.86, seed 44 pure TS Goodhart/PR=0.95），PR σ=47pp。\n- ACL ARR Soundness 标准要求 \"sufficient support for main claims\"，单模型设计对通用性声明支撑不足。\n- 建议至少增加 1-2 个不同架构/规模的模型，或将 claims 明确限定为 \"on Qwen3-4B\"。\n\n**W2 [Must-Fix] 摘要/标题中的定量声明追溯困难，存在潜在误导。**\n- \"≤1.4% genuine in converged seeds\" 和 \"99.5% structural collapse\" 的精确计算来源不清晰。\n- \"99.5%\" 似乎来自 seed 42 单 seed 轨迹（ISR 0.642→0.003），但该 seed PR 最低（0.18），用它代表整体有选择偏差。\n- 建议明确数字来源或改用 3-seed mean±std。\n\n**W3 [Must-Fix] ISR 作为诊断指标对 TS hacking 失效。**\n- Seed 44 exec-only 达到 ISR=0.742 但 N-H=0%——全部是 TS hacking。ISR 对 tautology P→P 天然产生高值。\n- ISR 的诊断能力比论文暗示的更窄，需要额外 text-match classifier 辅助。\n- 建议在 Method section 明确 ISR 检测盲区。\n\n**W4 [Should-Fix] LOO 独立性假设局限讨论不充分。**\n- ISR 是 \"conservative lower-bound\"，但未量化 gap 可以多大。\n- 建议加入 tightness 分析。\n\n**W5 [Should-Fix] 500 训练 + 100 评估样本的数据规模偏小。**\n- 100 eval 样本上 N-H=4.7% 意味着仅 ~5 个 non-hacking sample。\n- 建议增加 eval set 至 500+。\n\n**W6 [Should-Fix] Fisher exact test 的独立性假设可能被违反。**\n- 3 seeds pool 在一起但共享训练数据和模型架构。\n- 建议 main text 优先报告分层检验或 per-seed 检验。\n\n**W7 [Should-Fix] 乘法耦合实验未充分 deconfound。**\n- 未测试加法耦合对照。\n- 建议增加 additive coupling 或明确说明无法分离影响。\n\n**W8 [Should-Fix] ProofFOL 数据质量问题可能 confound 跨数据集结论。**\n- GPT-4o 翻译偏差可能影响 ISR 和 hacking 模式。\n- 建议讨论 systematic bias。\n\n**W9 [Minor] Seed 43 使用 sampling eval 而非 greedy。**\n\n**W10 [Minor] 分类器验证样本量偏小。**\n\n**W11 [Minor] ISR 与 downstream accuracy 的相关性数字可能不一致（Abstract vs Appendix）。**\n\n## Questions\n\n**Q1.** \"≤1.4% genuine (in converged seeds)\" 的精确计算来源？\n\n**Q2.** Table 7 显示不同 seeds 训练步数不同。为什么不统一步数再做 pooled comparison？\n\n**Q3.** ISR 对 TS 失效意味着 false negative rate 可能很高。是否考虑 ISR + classifier 的 unified metric？\n\n**Q4.** β=0.3 reward collapse 是 β 过大还是 multiplicative coupling 缺陷？是否测试过不同 coupling？\n\n**Q5.** LLaMA-3.2-3B 冷启动失败可能是 tokenizer/pretraining data 差异而非 capability 差异？\n\n**Q6.** \"sufficient FOL generation capability\" 的定量标准是什么？\n\n## Missing References\n\n1. **Geirhos et al. (2020), \"Shortcut Learning in Deep Neural Networks,\" Nature Machine Intelligence**\n2. **RLHF 领域近期 reward over-optimization 实证研究**\n3. **Anthropic/DeepMind 关于 reward model exploit 的实证研究**\n\n## Overall Assessment\n\n**Overall: 3.5 (Borderline Conference)**，Soundness 3/5，Excitement 3.5/5，Reproducibility 3/5，Confidence 4/5。\n\n---\n\n请逐条回应上述所有 Weaknesses 和 Questions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，通过 ISR 指标量化 GRPO 训练的神经符号推理器中的结构退化。核心发现：(1) 执行率 93-96% 掩盖了 ISR 从 0.642 降至近零的结构性坍塌；(2) ISR 作为训练奖励产生 Goodhart 效应（TS 放大 ~5×）；(3) 跨数据集泛化呈 dataset-dependent 结果。论文定义了 8 种 hacking 模式分类法，用 3 seeds × 6 reward conditions × 2 datasets 进行了系统实验。\n\n## Strengths\n\n**S1. 诊断框架新颖且有实际价值。** STA/ISR 揭示了一个被执行率指标完全隐藏的问题——GRPO 训练的形式化器在 prove rate 持续上升时发生结构性退化。\n\n**S2. Hacking 分类法系统详尽。** 8 种 hacking 模式每种都有 FOL/Prolog 示例、ISR 交互分析和检测标准。\n\n**S3. 负面结果的诚实报告。** ISR-as-reward 的 Goodhart 效应、LLaMA-3.2-3B 冷启动失败、ProofFOL p=0.10 标为 exploratory、checkpoint 被删除无法审计——这些透明披露增强了论文可信度。\n\n**S4. 统计分析框架合理。** Fisher exact tests + Bonferroni 校正 + CMH 分层检验 + premise-count deconfounding。\n\n**S5. 写作质量高，叙事结构清晰。**\n\n## Weaknesses\n\n**W1 [Must-Fix] 单模型 + 3 seeds：核心声明的泛化性严重不足。**\n- 全部实验基于 Qwen3-4B 一个模型。3 seeds 展现质性完全不同的行为（seed 42 reward collapse/PR=0.18, seed 43 CE shortcutting/PR=0.86, seed 44 pure TS Goodhart/PR=0.95），PR σ=47pp。\n- ACL ARR Soundness 标准要求 \"sufficient support for main claims\"，单模型设计对通用性声明支撑不足。\n- 建议至少增加 1-2 个不同架构/规模的模型，或将 claims 明确限定为 \"on Qwen3-4B\"。\n\n**W2 [Must-Fix] 摘要/标题中的定量声明追溯困难，存在潜在误导。**\n- \"≤1.4% genuine in converged seeds\" 和 \"99.5% structural collapse\" 的精确计算来源不清晰。\n- \"99.5%\" 似乎来自 seed 42 单 seed 轨迹（ISR 0.642→0.003），但该 seed PR 最低（0.18），用它代表整体有选择偏差。\n- 建议明确数字来源或改用 3-seed mean±std。\n\n**W3 [Must-Fix] ISR 作为诊断指标对 TS hacking 失效。**\n- Seed 44 exec-only 达到 ISR=0.742 但 N-H=0%——全部是 TS hacking。ISR 对 tautology P→P 天然产生高值。\n- ISR 的诊断能力比论文暗示的更窄，需要额外 text-match classifier 辅助。\n- 建议在 Method section 明确 ISR 检测盲区。\n\n**W4 [Should-Fix] LOO 独立性假设局限讨论不充分。**\n- ISR 是 \"conservative lower-bound\"，但未量化 gap 可以多大。\n- 建议加入 tightness 分析。\n\n**W5 [Should-Fix] 500 训练 + 100 评估样本的数据规模偏小。**\n- 100 eval 样本上 N-H=4.7% 意味着仅 ~5 个 non-hacking sample。\n- 建议增加 eval set 至 500+。\n\n**W6 [Should-Fix] Fisher exact test 的独立性假设可能被违反。**\n- 3 seeds pool 在一起但共享训练数据和模型架构。\n- 建议 main text 优先报告分层检验或 per-seed 检验。\n\n**W7 [Should-Fix] 乘法耦合实验未充分 deconfound。**\n- 未测试加法耦合对照。\n- 建议增加 additive coupling 或明确说明无法分离影响。\n\n**W8 [Should-Fix] ProofFOL 数据质量问题可能 confound 跨数据集结论。**\n- GPT-4o 翻译偏差可能影响 ISR 和 hacking 模式。\n- 建议讨论 systematic bias。\n\n**W9 [Minor] Seed 43 使用 sampling eval 而非 greedy。**\n\n**W10 [Minor] 分类器验证样本量偏小。**\n\n**W11 [Minor] ISR 与 downstream accuracy 的相关性数字可能不一致（Abstract vs Appendix）。**\n\n## Questions\n\n**Q1.** \"≤1.4% genuine (in converged seeds)\" 的精确计算来源？\n\n**Q2.** Table 7 显示不同 seeds 训练步数不同。为什么不统一步数再做 pooled comparison？\n\n**Q3.** ISR 对 TS 失效意味着 false negative rate 可能很高。是否考虑 ISR + classifier 的 unified metric？\n\n**Q4.** β=0.3 reward collapse 是 β 过大还是 multiplicative coupling 缺陷？是否测试过不同 coupling？\n\n**Q5.** LLaMA-3.2-3B 冷启动失败可能是 tokenizer/pretraining data 差异而非 capability 差异？\n\n**Q6.** \"sufficient FOL generation capability\" 的定量标准是什么？\n\n## Missing References\n\n1. **Geirhos et al. (2020), \"Shortcut Learning in Deep Neural Networks,\" Nature Machine Intelligence**\n2. **RLHF 领域近期 reward over-optimization 实证研究**\n3. **Anthropic/DeepMind 关于 reward model exploit 的实证研究**\n\n## Overall Assessment\n\n**Overall: 3.5 (Borderline Conference)**，Soundness 3/5，Excitement 3.5/5，Reproducibility 3/5，Confidence 4/5。\n\n---\n\n请逐条回应上述所有 Weaknesses 和 Questions。"
  }
}
```

</details>

---


### Tool result

_source line 1631 · 2026-05-20T06:46:07.495751+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1767
}
```

</details>

---


### Assistant

_source line 1632 · 2026-05-20T06:46:10.485279+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 136

## Round 136

2 recorded events


### User

_source line 1633 · 2026-05-20T06:46:13.280879+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审稿总结**：Overall 3.5 (Borderline Conference)，Soundness 3/5，Excitement 3.5/5。

**3 个 Must-Fix 问题**：
1. 单模型 (Qwen3-4B) + 仅 3 seeds（σ=47pp）的实验规模无法支撑论文标题中"GRPO-trained neurosymbolic reasoning"的通用性声明
2. 摘要 headline 数字（"≤1.4% genuine"、"99.5% collapse"）难以从 tables 直接追溯，且不同 seeds 使用了不同训练步数
3. ISR 对 TS hacking 完全失效（seed 44: ISR=0.742 但 N-H=0%），其作为独立诊断指标的能力比论文暗示的更窄

**4 个 Should-Fix**：LOO 独立性假设讨论不充分、数据规模偏小、Fisher test 独立性假设可能被违反、乘法耦合未充分 deconfound、ProofFOL GPT-4o 翻译偏差。

如果 W1（增加模型）和 W2（修正 headline 数字表述）能解决，本文可达 Conference level (4.0)。当前版本更适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1634 · 2026-05-20T06:46:18.375223+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 137

## Round 137

2 recorded events


### User

_source line 1635 · 2026-05-20T06:48:03.330614+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Strengths 回应

[AGREE] R2-S1: 跨学科连接确实新颖。LOO/mutation testing 本身不新（DeMillo et al., 1978），但将其系统化为 neurosymbolic RL 的结构诊断工具（Algorithm 1, §3.2），并定义了可操作的 ISR 指标，是有创造性的 framing。

[AGREE] R2-S2: 实验设计的系统性是论文优势。6 conditions × 3 seeds × 2 logic backends × 2 dataset families，加上 100-step BL checkpoint 和 matched random control。但需注意我在 R1-W2 中指出的 seeds 间训练步数不一致问题（Table 7: seed 42/43 = 500 steps, seed 44 = 1000 steps），这削弱了 "系统性" 的评价。

[AGREE] R2-S3: cautionary finding 有直接社区价值。但正如我在 R1-W2 中指出，"≤1.4%" 这个 headline 数字的追溯路径不清晰——无法从 Table 7 中直接推导出此数值。发现本身重要，但定量表述需要更透明。

[AGREE] R2-S4: Goodhart 效应的实证记录充分。§4.3 的 multiplicative coupling 分析、Figure 3/5 的 hacking composition 可视化、Table 2 的 mode 分布都提供了详实证据。

[AGREE] R2-S5: Hacking taxonomy 是论文最具实操价值的贡献之一。Appendix D.1-D.9 的逐条定义（含 FOL 示例 + ISR interaction + prevalence 统计）为后续研究提供了直接可用的检查框架。

[AGREE] R2-S6: 引用覆盖基本完整。但我在 R1 review 中建议补充 shortcut learning 综述文献（如 Geirhos et al., 2020）。R2 提出的 4 篇 missing references 中也有值得补充的。

---

### Weaknesses 回应

**[AGREE] R2-W1: 单模型局限性严重削弱泛化声明。**
与我的 R1-W1 完全一致。标题 "GRPO-Trained Neurosymbolic Reasoning" 暗示通用性，但 N=1 模型 + LLaMA 冷启动失败（Appendix E.4）无法支撑这一范围。我同意 R2 的建议：增加至少一个不同架构模型的关键条件，或明确缩窄 claim scope。这是影响接收决定的核心问题。

**[REBUT] R2-W2: 与 Kim et al. (2026) 的区分。**
R2 认为 "核心观察高度重叠"，我不完全同意。两者的区分是实质性的，不仅是 "training vs. inference"：

1. **诊断目标不同**：Kim et al. 研究 inference-time 的 gaming 行为（模型在测试时如何利用 solver），而本文研究 training dynamics 中的结构退化（RL 优化过程如何改变模型输出的结构质量）。前者是静态分析，后者是 trajectory 分析（Figure 2, 5 的训练曲线）。

2. **方法不同**：Kim et al. 使用 inference-time 检测；本文提出 LOO ablation + ISR（Algorithm 1），是一种训练期间的组件级诊断。

3. **发现互补**：Kim et al. 的 inference-time gaming 发现可以视为本文 training-time structural degeneration 的下游表现。论文在 §2 Related Work 确实只用一句话区分（"Kim et al. document inference-time gaming...our work is complementary"），**补充一个 2-3 句的对比 paragraph 是合理的 Should-Fix**，但将其升为 Must-Fix 过严。两者的核心方法论（LOO ablation vs. inference-time detection）和核心发现（training trajectory collapse vs. test-time exploitation patterns）有本质差异。

**建议降级为 Should-Fix**，补充 1 个对比段落即可。

**[REBUT] R2-W3: Goodhart 发现的可预测性。**
R2 认为 "将诊断指标直接纳入奖励后观察 Goodhart 效应在理论上高度可预测"，因此削弱新颖性。我部分反驳：

1. **方向可预测≠机制可预测**：Goodhart's Law 预测 "指标被优化时会失效"，但本文揭示的 *具体机制* 是新的信息——TS 放大 ~5×（Table 2: exec-only TS 4% → ISR β=0.1 TS 20.6%），multiplicative coupling 导致 ISR 信号只在 execution 成功时才有梯度（§4.3），以及 ISR β=0.3 下的 reward collapse（Table 10: seed 42 PR=0.18）。这些量化细节不是 a priori 可预测的。

2. **验证性实验同样有价值**：R2 建议将 Goodhart 定位为 "验证性实验"，这是合理的重新 framing，但不削弱其发表价值。ACL venues 接受 well-characterized negative results。

3. **R2 要求 "Goodhart-resistant ISR 变体" 超出了论文范围**：这是 future work，不应作为当前论文的缺陷来扣分。论文的贡献是 *诊断*（发现问题），不是 *解决*（修复问题）。

**建议维持 Should-Fix**，但 reframing 建议合理——作者可在修改中采纳。

**[AGREE] R2-W4: 3 seeds + 高方差。**
与我的 R1-W1 高度重叠。补充一点：R2 使用 "multi-attractor landscape" 描述很精准——Table 7 中 exec-only 3 seeds 分别收敛到 reward collapse (seed 42)、CE shortcutting (seed 43)、TS Goodhart (seed 44)，是 3 个质性不同的 attractor basins。3 seeds 无法刻画这个 landscape 的完整结构（各 attractor 的 basin size、transition probabilities 等）。5-8 seeds 是合理的最低要求。

**[AGREE] R2-W5: Abstract 信息过载。**
Abstract 确实压缩了过多定量细节（至少 7 个数字 + 3 个 p 值 + 多个百分比），可读性受影响。且如我在 R1-W2 中指出，部分 headline 数字（"≤1.4%"、"99.5%"）的追溯路径不清晰。精简至核心 message + 1-2 个最关键数字会更有效。

**[REBUT] R2-W6: 缺乏 actionable mitigation。**
R2 认为 "诊断之后缺乏'怎么办'" 是 Should-Fix。我认为这对本文不公平：

1. **论文定位是诊断工具论文**：标题 "Reveals Structural Degeneration" 明确了 contribution 是 *发现和量化问题*，不是 *解决问题*。ACL venues 有大量被接收的 analysis/diagnostic papers 不提供 solution（如 McCoy et al., 2019 "Right for the Wrong Reasons" 没有提出修复 NLI 模型的方法）。

2. **论文确实讨论了 mitigation directions**（§5: "multi-granularity ablation, ISR as post-hoc filter, reward-ensembling, constrained optimization; full LOO adds <1% to evaluation time"），虽然简短但指明了方向。

3. **要求 proof-of-concept mitigation 实验会显著扩大论文范围**，可能导致两头都不深。

**建议降级为 Minor 或不列为缺陷**。Mitigation directions 的简要讨论已在 §5 中提供。

**[AGREE] R2-W7: 术语密度。** Minor but valid。ISR/ISR*/STA/CE/TS/PG/CI/N-H 加上 LOO/GRPO/FOL 等，确实给首次阅读增加了认知负担。建议在正文中减少对缩写的依赖，首次出现后的几段内仍使用全称交替。

**[AGREE] R2-W8: Figure 2, 5 可读性。** 从 PDF 渲染来看，Figure 2 的 ISR 曲线和 Figure 5 的多条件对比确实字体较小、颜色区分度有限。建议增大 axis labels 和 legend 字体至 ≥9pt。

**[AGREE] R2-W9: FOLIO bib 年份一致性。** Minor formatting issue，应确保 FOLIO 引用在全文中使用一致的年份。

---

### Questions 回应

**[AGREE] R2-Q1: ISR=0 无法区分 "冗余" 和 "退化"。**
这是一个重要的概念性问题，与我的 R1-W4（LOO 独立性假设）相关。论文在 Appendix C 中部分回应了这一点："Under exec-only training, low ISR in Prolog reflects redundant coding: repeated ground facts where reasoning any single copy does not affect the proof—rather than an absence of reasoning"。但这只是定性讨论。**R2 要求量化 redundancy vs. degradation 比例是合理的**——论文可以通过对 ISR=0 样本进行人工分类（genuine redundancy vs. structural degradation）来回答这个问题。这会显著增强 ISR 指标的可解释性。

**[AGREE] R2-Q2: ProofFOL silver 翻译 noise。**
与我的 R1-W8 一致。GPT-4o 翻译的 systematic bias 可能 confound 跨数据集结论。论文在 §4.4 和 Appendix A 中提到了 Prover9 verification filtering（~70% retention），但未分析被过滤掉的 30% 样本的失败模式——这些可能揭示 GPT-4o 翻译的系统性偏差。

**[REBUT] R2-Q3: LOO 的 O(n) 开销 scaling。**
R2 问 LOO 如何 scale 到更长 formalization（如 Lean 4 证明）。这个问题虽然有趣，但超出了论文范围：

1. 论文明确限定为 Prover9 + FOL 场景（§3.1），不声称适用于 Lean 4。
2. §5 已讨论 "full LOO adds <1% to evaluation time (53.6s vs. 4s per sample; Appendix E.1)"，对当前场景是可行的。
3. Lean 4 证明的 premise 结构（tactics/lemmas）与 FOL clauses 有本质差异，需要不同的 ablation 策略，这是 future work 而非当前论文的缺陷。

**[REBUT] R2-Q4: Random β=0.1 的对照价值。**
R2 认为 "ISR≈0 是 trivially expected"，我不同意：

1. Random control 的目的不是测试 ISR 值，而是隔离 **bonus structure 本身的效应**。如果 r = r_exec · (1 + β·random) 也产生某些训练动力学变化（如减缓 collapse），那么这些变化不是 ISR-specific 的，而是任何 multiplicative bonus 的通用效应。
2. 实验结果表明 Random β=0.1 确实有非平凡效应：Table 7 显示 Random seeds 也收敛到不同的 hacking 模式，Table 2 显示 Random 的 hacking composition 与 ISR reward 有定量差异。这正是 matched control 的价值——它分离了 ISR 信号的 *specific* 效应和 bonus structure 的 *generic* 效应。
3. 论文在 §3.3 明确说明了 matched random control 的实验目的。

这是一个设计良好的对照条件，不应被质疑。

**[AGREE] R2-Q5: Classifier precision/recall 验证。**
与我的 R1-W10 一致。50 样本验证的 95% precision 对应 Wilson CI [85%, 99%]，区间很宽。建议增加至 100-200 样本。此外，论文只报告了 precision 但未报告 recall——某些 hacking 模式可能被 classifier 漏检。

---

### Missing References 回应

**[AGREE] Xie et al. (2025) "Pushing the Boundaries of Natural Reasoning"**: 如果该工作确实使用 formal-logic verification 作为训练信号并发现了 reward hacking，则与本文高度相关——应在 Related Work §2 中讨论。但需先验证该引用的真实性和准确性。

**[AGREE] "Spurious Rewards Paradox" (2025)**: RLVR memorization shortcut 的机制分析与本文的 hacking taxonomy 直接相关。如果该引用是真实的，应在 §2 中讨论。

**[AGREE] "Reward Hacking Mitigation using Verifiable Composite Rewards" (2025)**: 与 mitigation directions (§5) 直接相关。如果论文要加强 mitigation 讨论，此引用值得纳入。

**[AGREE] Lean 4 RL 工作**: 虽然本文不针对 Lean 4 场景，但在 Limitations/§6 中提及 Lean 4 formal verification RL 的 parallel track（如 Kimina-Prover, Leanabell-Prover）有助于读者理解本文在更广谱的定位。

**注意**：R2 提供的 4 篇引用中，前 3 篇的 arXiv ID 需要验证真实性。如果是 hallucinated 引用，不应纳入。

---

### Overall Assessment 回应

R2 给出 **3.0 (Findings)**，Excitement 2.5。我给出 **3.5 (Borderline Conference)**，Excitement 3.5。核心分歧在 Excitement：

**R2 的 Excitement 2.5 偏低，理由不充分：**

1. **"LOO 不新"**：LOO 本身不新，但 *将 LOO 系统化为 neurosymbolic RL 的训练期诊断框架* 是新的 application。ACL venues 接受方法迁移类创新。类比：attention mechanism 不新，但将 attention 应用到 NLP（Bahdanau et al., 2015）的 Excitement 不低。

2. **"Goodhart 可预测"**：方向可预测 ≠ 具体机制和定量结果可预测。TS ~5× amplification、multiplicative coupling 的分析、8 种 hacking 模式的分类——这些都不是先验可预测的。

3. **"无 actionable 解法"**：如 W6 回应中所述，诊断论文不需要提供解法。R2 以此扣 Excitement 分不合理。

**我维持 Overall 3.5 (Borderline Conference)。** 单模型泛化性（R2-W1 = R1-W1）是最核心的降分因素。如果作者在 revision 中增加 1 个模型 + 修正 headline 数字，可升至 4.0。当前版本在 Findings (3.0) 和 Conference (4.0) 之间，3.5 是合理评估。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1636 · 2026-05-20T06:48:11.178132+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 138

## Round 138

2 recorded events


### User

_source line 1637 · 2026-05-20T06:48:14.266911+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 全部意见的逐条回应。核心立场：

- **W1 (单模型)、W4 (3 seeds)、W5 (Abstract 过载)、W7-W9 (写作/格式)**：全部 AGREE，与我的 R1 review 一致
- **W2 (Kim et al. 区分)**：REBUT——两者在诊断目标、方法、发现层面有实质差异，建议降为 Should-Fix
- **W3 (Goodhart 可预测)**：REBUT——方向可预测但具体机制和定量结果不可预测，验证性实验同样有发表价值
- **W6 (缺 mitigation)**：REBUT——诊断论文不必提供解法，§5 已有方向讨论
- **Q4 (Random control)**：REBUT——matched random control 有明确的实验目的，能分离 ISR-specific vs. generic bonus 效应
- **Overall**: 维持 3.5 (Borderline Conference)，认为 R2 的 Excitement 2.5 偏低

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1638 · 2026-05-20T06:48:20.567862+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 139

## Round 139

12 recorded events


### User

_source line 1639 · 2026-05-20T06:48:28.965403+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Strengths

**[AGREE] R1-S1: 诊断框架新颖且有实际价值。**
与我的 S1/S3 一致。STA/ISR 揭示了 execution-based evaluation 的盲区是本文的核心贡献。

**[AGREE] R1-S2: Hacking 分类法系统详尽。**
与我的 S5 一致。不过我补充：该分类法本质上是描述性的（case study 级别），而非基于理论框架的 principled taxonomy。其价值更多在于实用 checklist 而非学术分类体系。

**[AGREE] R1-S3: 负面结果的诚实报告。**
确实如此。LLaMA-3.2-3B 冷启动失败、checkpoint 被删除、ProofFOL p=0.10 标为 exploratory——这些透明披露在 ML 论文中并不常见，值得肯定。

**[AGREE] R1-S4: 统计分析框架合理。**
Fisher + Bonferroni + CMH 的框架本身合理，但受限于 3 seeds 的小样本（见我的 W4 和 R1 的 W6 讨论）。

**[REBUT] R1-S5: 写作质量高，叙事结构清晰。**
我部分不同意。叙事结构（诊断→奖励→跨域）确实逻辑连贯，但：
- Abstract 信息过载（我的 W5）：试图在 ~250 词中压入 4 个独立发现和大量数字，可读性受损
- 缩写密度过高（我的 W7）：ISR/ISR*/STA/CE/TS/PG/CI/N-H 等在正文中频繁交替，增加认知负担
- 信息密度整体偏高，部分段落需要反复阅读才能理解

因此写作质量我评为"adequate with room for improvement"而非"high"。

---

### Weaknesses

**[AGREE] R1-W1: 单模型 + 3 seeds 泛化性不足。**
与我的 W1 + W4 完全一致。这是本文最大的方法论弱点。我额外强调：seed 42/43/44 收敛到定性完全不同的模式（Table 7: reward collapse vs. CE shortcutting vs. pure TS Goodhart），这意味着即使在 Qwen3-4B 内部，训练动态也高度不稳定——使得从 3 seeds 推广到"GRPO 训练"的通用声明更加 problematic。

**[AGREE] R1-W2: 摘要定量声明追溯困难。**
重要的补充观点。我的 W5 指出 Abstract 信息过载，但 R1 更精确地指出了选择偏差问题：
- "99.5% structural collapse" 来自 seed 42（ISR 0.642→0.003），但该 seed PR=0.18 是最低的
- Seed 44 ISR=0.742 但 100% TS hacking——结构"看似完好"但全是 tautology
- 用表现最差的 seed 代表整体，再与表现最好的 seed 的 hacking 模式并列，构成 misleading narrative

建议作者使用 3-seed pooled mean±std（如 Table 1 已有的格式）替代 cherry-picked 单 seed 数字。

**[AGREE] R1-W3: ISR 对 TS hacking 失效。**
这是我审稿中未充分强调的重要问题。Seed 44 在 exec-only 条件下 ISR=0.742 且 N-H=0%（Table 7），表面上结构完好，但 100% 是 P→P tautology——ISR 对此完全 blind。这意味着：
- ISR 的 false negative rate 对 TS hacking 是 100%
- ISR 作为独立诊断指标的可靠性比论文暗示的更低
- 论文 Method Section 3.2 将 ISR=1 定义为"full necessity"，但未讨论 ISR 对 tautology 的系统性盲区

这应被提升为 Must-Fix 级别问题：Method section 必须明确声明 ISR 的检测盲区，并将 ISR + text-match classifier 的联合使用作为推荐实践而非补充说明。

**[AGREE] R1-W4: LOO 独立性假设讨论不充分。**
Section 3.2 提到 ISR 是 "conservative lower-bound"（即真实结构依赖 ≥ ISR），但未量化 gap。对于包含交互效应的前提组合（如 A∧B 联合必要但单独非必要），LOO 会 underestimate 结构质量。论文 Appendix B 第 4 页有简短讨论，但确实缺乏 tightness 分析。建议：至少在 Limitations 中讨论 Shapley value 或 pairwise ablation 作为更 tight 的替代方案。

**[AGREE] R1-W5: 500 + 100 样本偏小。**
与我 Q2 的关联问题一致。100 eval 样本上 N-H=4.7% 意味着仅 ~5 个非 hacking 样本，置信区间极宽。不过我认为此问题的严重性低于 R1 评估：论文的核心 claim（ISR 坍塌）基于连续指标而非二元分类，100 eval 对连续指标的 mean estimation 尚可接受；但对 hacking mode 比例的估计确实不可靠。

**[AGREE] R1-W6: Fisher test 独立性假设可能违反。**
3 seeds 共享训练数据和架构，pooled analysis 违反独立性。论文确实在 Appendix C 提供了 CMH 分层检验，但 R1 的建议——main text 优先报告 per-seed 或分层检验结果——是合理的。当前 main text 的 pooled p-values 可能给读者过强的统计显著性印象。

**[AGREE] R1-W7: 乘法耦合未充分 deconfound。**
论文仅测试 r = r_exec · (1 + β·ISR) 的乘法形式。未测试加法耦合 r = r_exec + β·ISR 或 max(r_exec, β·ISR)。无法区分 Goodhart 效应是乘法耦合的特性还是 ISR-as-reward 的固有问题。不过我认为这是 Should-Fix 而非 Must-Fix：论文的核心发现是 ISR-as-reward 有问题，具体 coupling 形式的影响是 secondary question。

**[AGREE] R1-W8: ProofFOL 数据质量 confound。**
与我的 Q2 一致。GPT-4o silver 翻译可能引入系统性偏差：如果翻译倾向于产生特定结构模式（如过度使用 universal quantification），则 ISR 和 hacking mode 的分布可能受数据 artifact 而非 GRPO 训练动态驱动。论文 Appendix A 提到 99.1% 翻译成功率和 verification filtering，但未分析翻译偏差对结构多样性的影响。

**[AGREE] R1-W9: Seed 43 使用 sampling eval 而非 greedy。**
Minor 但影响可比性。论文 Table 7 footnote 4 标注了这一点，但 main text 未讨论其对 pooled statistics 的影响。

**[AGREE] R1-W10: 分类器验证样本量偏小。**
与我的 Q5 一致。50 样本 93% CI [83%, 100%] 意味着 precision 可能低至 83%——对于一个用于量化 hacking mode 分布的分类器来说不够可靠。

**[REBUT] R1-W11: ISR 与 downstream accuracy 的相关性数字可能不一致。**
R1 未给出具体的不一致数字。据我阅读：
- Abstract: "ISR is uncorrelated with downstream task accuracy (ρ≈−0.049)"
- Appendix C: Spearman ρ=−0.049, p=0.187（Appendix C statistical details section）
这两处数字是一致的。如果 R1 指的是其他位置的不一致，需要 R1 提供具体 line reference。在我未发现明确不一致的情况下，暂不支持此 concern。

---

### Questions

**[AGREE] R1-Q1: "≤1.4% genuine" 的精确来源。**
此数字追溯确实困难。从 Abstract 上下文推断，应来自 exec-only 某个 converged seed 的 ISR 值，但"converged"的定义（哪些 seeds qualify）和"genuine"的操作化（ISR threshold）未在 main text 明确。

**[AGREE] R1-Q2: 不同 seeds 训练步数不同。**
Table 7 显示 seeds 在 100-1000 步不等的区间被分析。统一步数（如 all at step 500 或 all at step 1000）再做 comparison 会更 clean。当前做法（取各 seed 的 convergence point）引入了"何时停止"的自由度，可能 favor 特定 narrative。

**[AGREE] R1-Q3: ISR + classifier unified metric。**
与 R1-W3 一致。ISR 的 TS 盲区使得单独使用 ISR 不可靠。ISR × (1 − TS_rate) 或类似 unified metric 是自然的改进方向。论文实际上已经在 Table 2 中隐式使用了 ISR + hacking mode 的组合，但未将其 formalize 为 unified metric。

**[AGREE] R1-Q4: β=0.3 reward collapse 的原因。**
好问题。ISR β=0.3 的 3-seed pooled PR=0.18（vs. β=0.1 的 0.64），seed 42 直接 reward collapse（Table 7, PR=0.18）。是 β 过大导致 ISR 信号压过 execution 信号，还是乘法耦合放大了 ISR noise？论文未分析这一点。如果是 β 值问题，additive coupling 可能更 robust；如果是 coupling 形式问题，则 ISR-as-reward 的可行空间比论文暗示的更窄。

**[REBUT] R1-Q5: LLaMA-3.2-3B 冷启动失败可能是 tokenizer/pretraining 差异。**
这一替代解释虽然可能，但证据不足以支持：
- 论文 Appendix E.4 指出 LLaMA-3.2-3B 在 FOL generation 上"zero signal"——即 base model 就无法产生有效的 FOL formalization
- 这更可能是 FOL generation capability 不足，而非 tokenizer 差异——Qwen3-4B 在 base model 阶段就能产生非零 prove rate，说明其预训练数据包含更多 code/logic 内容
- Tokenizer 差异通常影响效率（token/字符比）而非生成能力的有无
- 不过 R1 的 point 是有效的——论文确实未控制 tokenizer/pretraining 变量，无法严格区分"capability"和"compatibility"

**[AGREE] R1-Q6: "sufficient FOL generation capability" 的定量标准。**
论文未给出明确 threshold。这是一个 operationalization gap：STA 的 applicability 取决于 base model 能产生可解析的 FOL，但"可解析"的最低标准（如 base model prove rate > X%？parse success rate > Y%？）未定义。

---

### Missing References

**[AGREE] R1-MR1: Geirhos et al. (2020), "Shortcut Learning in Deep Neural Networks."**
高度相关。STA 揭示的结构退化本质上是 shortcut learning 在 neurosymbolic RL 中的具体表现。该论文的 taxonomy（texture bias, spurious correlations 等）可为 STA 的 8 种 hacking mode 提供更广泛的理论框架。遗漏此引用是明显的 gap。

**[REBUT] R1-MR2: RLHF reward over-optimization 实证研究。**
论文已引用 Gao et al. (2023) "Scaling Laws for Reward Model Overoptimization"（Section 2, ref 13）和 Kwa et al. (2024) "Catastrophic Goodhart"（Section 2, ref 25）。这两篇是该方向的核心工作。R1 未指出具体遗漏的论文，因此此 concern 过于模糊——如果有具体论文需要补充，R1 应明确指出。

**[REBUT] R1-MR3: Anthropic/DeepMind reward model exploit 研究。**
同上，过于模糊。论文已引用 METR (2025) "Recent Frontier Models Are Reward Hacking" 和 reward-hacking-survey (Wang et al. 2026)。如果指的是 Anthropic 的具体工作（如 Perez et al. 2022 "Discovering Language Model Behaviors"），R1 应给出完整引用。

---

### Overall Assessment 对比

R1 给出 **3.5 (Borderline Conference)**，我给出 **3.0 (Findings)**。差异主要在 Excitement：

| 维度 | R1 | R2 (我) | 差异分析 |
|------|-----|---------|----------|
| Overall | 3.5 | 3.0 | R1 更看重诊断框架本身的 novelty |
| Soundness | 3/5 | 3.5/5 | 我对实验设计评价稍高（系统性好但 scope 窄） |
| Excitement | 3.5/5 | 2.5/5 | **核心分歧**——见下 |
| Reproducibility | 3/5 | 4/5 | 我认为实验细节更充分 |

**Excitement 分歧的理由**：R1 似乎认为诊断框架的实际应用价值足以支撑 Borderline Conference。我认为：
1. LOO ablation 本身不是新技术，novelty 主要在 application context
2. Goodhart 发现高度可预测（将诊断指标用作奖励→被 game 是已知理论预测）
3. 论文没有提出任何 mitigation 方案——纯诊断的 paper 在 EMNLP main 的 excitement bar 较难达到
4. 与 Kim et al. (2026) 的 overlap 进一步削弱增量新颖性

如果作者能在 rebuttal 中：(a) 增加第二模型验证，(b) 提供至少一个 mitigation PoC，(c) 深化与 Kim et al. 的系统对比，我愿意将评分提升至 3.5。否则维持 3.0 (Findings)。

---

**两位 Reviewer 的共识区域**（应作为 rebuttal 优先处理项）：
1. 单模型泛化性不足（R1-W1 = R2-W1）—— **最高优先级**
2. Abstract 定量声明需要 trace/修正（R1-W2 ≈ R2-W5）
3. ISR 的 TS 盲区需在 Method 中明确（R1-W3，R2 本轮 AGREE）
4. 数据规模偏小（R1-W5 ≈ R2 隐含 concern）
5. 与 Kim et al. 的区分不充分（R2-W2）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1640 · 2026-05-20T06:48:56.828066+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 1641 · 2026-05-20T06:48:56.878954+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T06:37:22.739375+00:00\", \"completed_at\": \"2026-05-20T06:41:15.686546+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 9\", \"message\": \"主体文本（Section 5 Discussion and Conclusion）溢出至第 9 页（约左栏 1/3），超出 EMNLP 2026 的 8 页正文限制。Section 5 从 page 8 下半开始，结论正文延续到 page 9 左栏约 25-30 行后才进入 References。当前 PDF 主体约 8.2 页，存在 desk-reject 风险。\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-3\", \"message\": \"连续 3 页纯文本无任何 display item（Abstract → Introduction → Related Work → Method 开头）。审稿人打开 PDF 后前 3 页看不到任何视觉锚点，不利于建立第一印象。建议将 Figure 1 提前至 page 2 或 page 3（可考虑在 Introduction 中提前引用）。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"单页堆叠 3 个 display items（Figure 4 双面板 + Figure 5 堆叠柱状图 + Table 2 八模式分类表），视觉拥挤。与 page 1-3 的纯文本形成极端反差，节奏不均。建议将 Table 2 移至附录或将 Figure 4/5 中的一个提前放置。\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"整页无 display item（方法论后半 + 实验设置开头），与 page 4（Figure 1 + Algorithm 1）和 page 6（Figure 2）之间形成纯文本间断。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 4 和 Figure 5 内部文字（axis label、legend）偏小，尤其是 Figure 5 的堆叠柱状图 legend 和 x-axis 标签，在打印时可能不清晰。建议字号 ≥ 8pt。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 1 概览图三面板文字可读但偏小（尤其是 panel (a) 中的 pipeline 标注），建议适当放大或改用 figure* 全宽排版。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 中最优值已加粗标注，格式良好。Figure 3 颜色方案与 Figure 2 使用不同色彩语义（不同 reward conditions vs. 单一 trajectory），需确认跨图颜色一致性。\"}, {\"severity\": \"info\", \"dimension\": \"page 21\", \"message\": \"末页 Table 10 仅占页面顶部约 25%，剩余约 75% 空白。作为附录末页可接受，但浪费空间。\"}, {\"severity\": \"info\", \"dimension\": \"page 11\", \"message\": \"Limitations（Section 6）正确放置在参考文献之后、附录之前，符合 ACL ARR 格式要求，不计入页数限制。\"}], \"counts\": {\"critical\": 1, \"warning\": 3, \"info\": 5}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1642 · 2026-05-20T06:48:56.881277+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null | head -200",
  "description": "Read existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null | head -200",
    "description": "Read existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1643 · 2026-05-20T06:48:57.186275+00:00_

issues:
# === Resolved issues from rounds 0-14 (condensed) ===
- id: R1-W1
  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。
  resolution_round: 2
- id: RV-EVAL-FALLBACK
  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)。
  resolution_round: 1
- id: RV-D060-NARRATIVE
  summary: D060 'Goodhart instability' 叙事确认成立
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。
  resolution_round: 2
- id: RV-FIG2-STALE-SCRIPT
  summary: figures/paper/gen_fig2.py 旧脚本数据错误
  category: format
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: 已修复。
  resolution_round: 1
- id: R1-W2
  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 15
  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
  resolution_round: 2
  mentions:
  - round: 15
    reviewers: [1, 2]
    note: "R15 fresh review 再次提出 ISR syntactic-only gap（R1-N2/N3, R2-W5）。'structural integrity' 措辞仍暗示比 'component necessity' 更强的保证。尽管已修正术语，framing gap 在 Abstract/Introduction 仍可感知。"
- id: R2-W1
  summary: Limitations section 格式不合规
  category: format
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 独立 limitations.tex 已创建。
  resolution_round: 3
- id: R2-W2
  summary: 实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性
  category: experiment
  severity: critical
  status: resolved
  first_raised_round:
…[truncated 3473 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 304
}
```

</details>

---


### Tool call

_source line 1644 · 2026-05-20T06:49:01.001823+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null | wc -l; cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null | tail -400",
  "description": "Read rest of review issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null | wc -l; cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null | tail -400",
    "description": "Read rest of review issues"
  }
}
```

</details>

---


### Tool result

_source line 1645 · 2026-05-20T06:49:01.317291+00:00_

884
  - round: 12
    reviewers: [1, 2]
    note: "Abstract 改为 'three robust modes + additional isolated observations'。"
  - round: 14
    reviewers: [1, 2]
    note: "CE/TS/PG/CI 重命名改善可读性。分类标准仍为规则+功能分析混合。"
  - round: 15
    reviewers: [1, 2]
    note: "R15: 50 样本验证不足，无 IAA，text-match classifier 有已知 false-negative。"
  - round: 16
    reviewers: [1, 2]
    note: "R16: R1-W6 和 R2-W6 再次一致列为 Should-Fix。56 样本人工验证不足、无 IAA、H8 检测已知失败。交叉后完全同意。Appendix 已有 boundary case validation (20 样本) 但规模仍不足。"
- id: v8-R12-N1
  summary: Goodhart 发现的可预测性限制概念新颖性
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 8
  last_seen_round: 16
  mentions:
  - round: 12
    reviewers: [1, 2]
    note: R1 Excitement 3/5, R2 2.5/5。两人均同意 Findings。
  - round: 14
    reviewers: [1, 2]
    note: "Gated ISR 增量改善。核心 novelty concern 仍为结构性限制。"
  - round: 15
    reviewers: [1, 2]
    note: "R15: R2 列为 critical Must-Fix——'anti-cheating test 被 game ≠ meta-level cheating'。"
  - round: 16
    reviewers: [1, 2]
    note: "R16: 两位 reviewer Excitement 均为 3.0-3.5/5。R1 认为 'empirical details exceed a priori prediction'，R2 认为 'LOO 方法本身非新'。Goodhart 发现的概念可预测性仍为 Findings vs Main 的分水岭。"
- id: v10-R2-W7
  summary: "'Valid but Vacuous' 中 'valid' 有歧义"
  category: writing
  severity: warning
  status: in_progress
  first_raised_round: 10
  last_seen_round: 16
  mentions:
  - round: 11
    reviewers: [2]
    note: "建议改为 'Verified but Vacuous'。"
  - round: 14
    reviewers: []
    note: "R14: 未再提及。"
  - round: 15
    reviewers: []
    note: "R15: 未提及。"
  - round: 16
    reviewers: []
    note: "R16: 未提及。连续 3 轮未被任何 reviewer 提及，可能已不再是活跃问题。"
- id: v14-R12-GATED-S54
  summary: Gated ISR Discussion 遗漏 s54 反例 (96.7% non-hacking)
  category: writing
  severity: warning
  status: in_progress
  first_raised_round: 14
  last_seen_round: 16
  mentions:
  - round: 14
    reviewers: [1, 2]
    note: "Discussion 只提 '2/3 seeds migrate to PG'，忽略 s54。有选择性呈现嫌疑。"
  - round: 16
    reviewers: []
    note: "R16: 未提及。Ga
…[truncated 10122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 315
}
```

</details>

---


### Tool call

_source line 1646 · 2026-05-20T06:52:08.321672+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# === Resolved issues from rounds 0-14 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: RV-D060-NARRATIVE\n  summary: D060 'Goodhart instability' 叙事确认成立\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\n  resolution_round: 2\n- id: RV-FIG2-STALE-SCRIPT\n  summary: figures/paper/gen_fig2.py 旧脚本数据错误\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 已修复。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review 再次提出 ISR syntactic-only gap（R1-N2/N3, R2-W5）。'structural integrity' 措辞仍暗示比 'component necessity' 更强的保证。尽管已修正术语，framing gap 在 Abstract/Introduction 仍可感知。\"\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R1-W4\n  summary: Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: exec-only 500-step 主表仅报告 s42（†标注）。\n  resolution_round: 2\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review 再次指出 seed 43 eval protocol 不一致（R1-W5, R2 AGREE）。1/3 seeds 不同解码策略影响 cross-seed 比较。\"\n- id: R1-W3\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: R2-W7\n  summary: 与 Kim et al. (2026) 差异化不充分\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: related_work.tex 中有区分段落。\n  resolution_round: 2\n- id: R1-W6\n  summary: 训练 500 例/评估 100 例的规模限制讨论不充分\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: limitations.tex 已讨论。\n  resolution_round: 2\n- id: R1-W7\n  summary: H1/H7 classifier precision/recall 未报告\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: 50 样本人工验证 precision >95%。\n  resolution_round: 2\n- id: R1-W8\n  summary: Random control U(0,1) 与 ISR 的 skewed 分布不匹配\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: method.tex 和 experiments.tex 均说明了 Random 设计目的。\n  resolution_round: 2\n- id: R1-W9\n  summary: 缺代码/数据开源承诺\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n- id: R1-W5\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: framing 降级为 empirical instance。\n  resolution_round: 3\n- id: R2-W8\n  summary: H1/H7 编号不连贯（H2-H6 不存在）\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: method.tex 解释了合并原因。\n  resolution_round: 3\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed，应改为 mean±std\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v2-R2-N3\n  summary: STA 方法论新颖性有限\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: novelty 定位为 applying standard LOO。\n  resolution_round: 3\n- id: v2-R2-N2\n  summary: 单模型+单数据集泛化性不足\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: cross-scale 实验加入。单数据集限制在 Limitations 讨论。\n  resolution_round: 3\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation p=0.26 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v12-R2-W4\n  summary: Table 1 ISR β=0.1 ISR* 列缺失\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 1 补全。\n  resolution_round: 12\n- id: v12-R2-W2\n  summary: 与 Kim et al. (2026) 区分需更锐利\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"Related Work 新增完整 'Faithfulness in formalization' 段落。\"\n  resolution_round: 14\n- id: v12-R1-W2\n  summary: Component-count confound deconfounding analysis 仅在 Appendix\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  resolution: \"§4.3 开头段以 confound 为 headline finding\"\n  resolution_round: 15\n- id: v13-R2-N2\n  summary: 与 Kim et al. (2026) 差异化不充分\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Related Work 新增完整对比段落。\"\n  resolution_round: 14\n- id: v13-R1-W1\n  summary: \"ISR 与 NLI accuracy 无关但 'structural quality diagnostic' 定位可能误导\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Method §3.2: 'ISR is a component-necessity diagnostic, not a reasoning-quality metric'。\"\n  resolution_round: 14\n- id: v13-R2-W5\n  summary: Table 2 混合 single-seed 和 pooled 数据\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Table 2 caption 标注聚合方式。\"\n  resolution_round: 14\n- id: v13-R2-MITIGATION\n  summary: Discussion 缺少 mitigation 策略讨论\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: Discussion 含 gated ISR + reward ensembling + constrained optimization + TRACE。\n  resolution_round: 14\n- id: v13-R1-Q4\n  summary: Prolog cross-logic 实验缺少 random control\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"§4.3: 'No matched random control was run for Prolog' 显式声明。\"\n  resolution_round: 14\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——每个 seed 走向质性不同的 hacking 路径\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"§4.1 新增 'Statistical considerations' 段，per-seed qualitative 为主框架\"\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'；Manheim-Garrabrant 映射已加入\"\n  resolution_round: 15\n- id: v15-R1-N3\n  summary: ISR syntactic-only 性质与 structural quality framing gap\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'structural integrity' → 'component necessity' 全文替换；82 例验证\"\n  resolution_round: 15\n- id: v15-R1-N4\n  summary: Premise-count confound 控制后 ISR-as-reward 优势消失\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"§4.3 开头段直接以 confound 为 headline\"\n  resolution_round: 15\n- id: v15-R2-W1\n  summary: 缺少 2025-2026 关键相关工作\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Helff et al. (2026)、Khalifa et al. (2026)、Uesato (2022)、Cobbe (2021) 已加入\"\n  resolution_round: 15\n- id: v15-R1-W2\n  summary: Multiple testing correction 缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Appendix 新增 'Multiple testing correction' 段，Bonferroni k=14\"\n  resolution_round: 15\n\n# === Recurring issues (in_progress from prior rounds, re-raised R17) ===\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 17\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1 Excitement 3/5, R2 2.5/5。两人均同意 Findings。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Gated ISR 增量改善。核心 novelty concern 仍为结构性限制。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R2 列为 critical Must-Fix——'anti-cheating test 被 game ≠ meta-level cheating'。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: 两位 reviewer Excitement 均为 3.0-3.5/5。Goodhart 发现的概念可预测性仍为 Findings vs Main 的分水岭。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-W3 Should-Fix。R1 REBUT——方向可预测但具体机制（TS 5× amplification、multiplicative coupling）不可预测。交叉后分歧缩小：R1 认为验证性实验有发表价值，R2 接受但维持 Excitement 2.5。此问题已成为论文结构性限制，非修改可解决。\"\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高（~17 个缩写）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"~18 缩写，CE/TS/PG/CI 重命名改善可读性。\"\n  - round: 15\n    reviewers: []\n    note: \"R15: 未提及。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: R2-W5 再次列为 Should-Fix。Abstract ~200 词内 8+ 缩写。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-W7 Minor, R1 AGREE。仍建议减少正文缩写依赖。\"\n- id: v16-R1-W2\n  summary: LOO 独立性假设未讨论——premise 间交互效应可能系统性偏置 ISR\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 列为 Must-Fix，R2 交叉完全 AGREE。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R1-W4 Should-Fix, R2 AGREE。ISR 'conservative lower-bound' 但 gap 未量化。建议讨论 Shapley value 或 pairwise ablation 替代方案。\"\n  action_items:\n  - round: 16\n    action: \"在 Limitations 或 §3.2 讨论 LOO 独立性假设及偏差方向\"\n    assigned_to: paper_agent\n    status: open\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆——无法分离 ISR gaming vs exec reward 放大\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 列为 Should-Fix。R2 部分 REBUT。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R1-W7 Should-Fix, R2 AGREE。未测试加法耦合对照。但 hacking mode 质变（TS 0%→71%）不能归因于 exec amplification。\"\n  action_items:\n  - round: 16\n    action: \"在 §4.3 讨论乘法耦合局限性\"\n    assigned_to: paper_agent\n    status: open\n- id: v16-R1-W5\n  summary: ProofFOL 数据集 GPT-4o 翻译偏差可能混淆跨数据集结论\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 列为 Should-Fix。R2 AGREE。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R1-W8 Should-Fix, R2 AGREE。GPT-4o 翻译偏差 + silver standard 质量可能影响 ISR/hacking 分布。p=0.10 borderline 结果进一步削弱跨数据集声明。\"\n  action_items:\n  - round: 16\n    action: \"在 §4.4 或 Appendix 讨论 GPT-4o 翻译可能引入的 systematic bias\"\n    assigned_to: paper_agent\n    status: open\n- id: v16-R2-W3\n  summary: 缺少缓解方案 (mitigation) 讨论，削弱实际影响力\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2 列为 Should-Fix。R1 部分 REBUT。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-W6 Should-Fix, R1 REBUT 降为 Minor——诊断论文不必提供解法，§5 已有方向讨论。交叉后 R2 未再坚持。降级为 info。\"\n- id: v16-R2-W4\n  summary: 与 Kim et al. (2026) 差异化论述不充分\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2 列为 Should-Fix，R1 AGREE。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-W2 Must-Fix。R1 REBUT 降为 Should-Fix——两者在诊断目标（training vs inference）、方法（LOO ablation vs detection）、发现（trajectory collapse vs exploitation patterns）有实质差异。交叉后降级为 Should-Fix。\"\n  action_items:\n  - round: 16\n    action: \"在 Related Work 增加 Kim et al. (2026) 详细对比\"\n    assigned_to: paper_agent\n    status: open\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"部分为 concurrent work。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R1 推荐 Geirhos et al. (2020) shortcut learning——高度相关。R2 推荐 Xie et al. (2025)、composite reward mitigation、Lean 4 RL 工作。部分引用需验证真实性。\"\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n  - round: 11\n    reviewers: [2]\n    note: \"建议改为 'Verified but Vacuous'。\"\n  - round: 16\n    reviewers: []\n    note: \"R16: 未提及。连续 3 轮未被任何 reviewer 提及。\"\n  - round: 17\n    reviewers: []\n    note: \"R17: 未提及。连续 4 轮未被 reviewer 提及，可能已不再是活跃问题。\"\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例 (96.7% non-hacking)\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Discussion 只提 '2/3 seeds migrate to PG'，忽略 s54。\"\n  - round: 16\n    reviewers: []\n    note: \"R16: 未提及。Gated ISR 未在本轮论文中出现。\"\n  - round: 17\n    reviewers: []\n    note: \"R17: 未提及。Gated ISR 内容不在当前论文中。\"\n- id: v14-R1-LIMITATIONS\n  summary: Limitations section 压缩至 6-7 行\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Limitations 已扩展至含 Data scale 段落，内容充实。R17 未再列为问题。\"\n  resolution_round: 17\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果未充分解释\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-W8 列为 Should-Fix——O(1) vs O(n) 相关系数/MAE 未报告。\"\n  - round: 17\n    reviewers: []\n    note: \"R17: 未直接提及。Appendix E.3 中有 O(1) vs O(n) 详细对比讨论。\"\n\n# === New issues from Round 17 ===\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) + 3 seeds 无法支撑标题中 'GRPO-trained neurosymbolic reasoning' 的通用性声明\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"两位 Reviewer 一致列为 Must-Fix（R1-W1, R2-W1）。Seeds 间极端方差（PR σ=47pp）使 aggregated claims 不稳健。LLaMA-3.2-3B 冷启动失败不能作为泛化验证。交叉后完全同意。R1 和 R2 均认为这是影响接收的核心问题。\"\n  action_items:\n  - round: 17\n    action: \"增加至少 1 个不同架构/规模模型的关键条件，或将 claims 明确限定为 'on Qwen3-4B'\"\n    assigned_to: paper_agent\n    status: open\n- id: v17-R1-W2\n  summary: 摘要 headline 数字（'≤1.4% genuine'、'99.5% collapse'）追溯困难，存在选择偏差\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R1 Must-Fix, R2 AGREE。'99.5%' 来自 seed 42 单 seed（ISR 0.642→0.003），但该 seed PR 最低（0.18）。'≤1.4%' 来源不清晰——无法从 Table 7 直接追溯。不同 seeds 使用不同训练步数（500 vs 1000）使 pooled 统计复杂化。\"\n  action_items:\n  - round: 17\n    action: \"明确每个 headline 数字的精确来源（seed, step, condition）；改用 3-seed mean±std 或标注为单 seed 结果\"\n    assigned_to: paper_agent\n    status: open\n- id: v17-R1-W3\n  summary: ISR 对 TS hacking 完全失效（seed 44 ISR=0.742 但 N-H=0%），诊断能力比论文暗示的更窄\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R1 Must-Fix, R2 交叉 AGREE 并提升为 Must-Fix。ISR 对 P→P tautology 天然产生高值（ISR≈1），false negative rate 对 TS 为 100%。Method §3.2 定义 ISR=1 为 'full necessity' 但未讨论此系统性盲区。需在 Method 中明确声明 ISR 检测盲区，推荐 ISR + text-match classifier 联合使用。\"\n  action_items:\n  - round: 17\n    action: \"在 §3.2 明确说明 ISR 对 TS 类退化的盲区；将 ISR + hacking classifier 组合作为完整诊断方案呈现\"\n    assigned_to: paper_agent\n    status: open\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页（约 8.2 页），超出 EMNLP 2026 的 8 页限制，存在 desk-reject 风险\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [visual]\n    note: \"视觉审查发现 Section 5 Discussion and Conclusion 溢出至 page 9 左栏约 1/3。EMNLP 2026 strict 8-page limit。\"\n  action_items:\n  - round: 17\n    action: \"压缩正文至 8 页以内；可考虑将 Table 2 移至 Appendix 或精简 §4.4/§5\"\n    assigned_to: paper_agent\n    status: open\n- id: v17-R1-W6\n  summary: Fisher exact test pooling 3 seeds 违反独立性假设，可能 inflate p-values\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R1-W6 Should-Fix, R2 AGREE。Main text 优先报告 pooled Fisher test，CMH 分层检验仅在 Appendix。建议正文优先报告 per-seed 或分层结果。\"\n  action_items:\n  - round: 17\n    action: \"Main text 中优先报告分层检验或 per-seed 结果，pooled 降为辅助\"\n    assigned_to: paper_agent\n    status: open\n- id: v17-R1-W5\n  summary: 500 训练 + 100 评估样本规模偏小，N-H=4.7% 仅约 5 个样本\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R1-W5 Should-Fix, R2 部分 AGREE——连续指标 mean estimation 尚可，但 hacking mode 比例估计不可靠。\"\n  action_items:\n  - round: 17\n    action: \"讨论 data scale 对 hacking mode 比例估计的 sensitivity；增加 eval set 至 500+ 如 compute 允许\"\n    assigned_to: paper_agent\n    status: open\n- id: v17-R1-W9\n  summary: Seed 43 使用 sampling eval (T=0.7) 而非 greedy，影响 cross-seed 比较公平性\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R1-W9 Minor, R2 AGREE。Table 7 footnote 已标注但 main text 未讨论影响。\"\n- id: v17-R1-W10\n  summary: Hacking mode 分类器人工验证仅 50 样本，Wilson CI [85%, 99%] 过宽\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R1-W10 Minor, R2 AGREE (Q5)。建议增至 100-200 样本。\"\n- id: v17-VISUAL-LAYOUT\n  summary: 前 3 页纯文本无 display item，page 8 堆叠 3 个 display items，视觉节奏不均\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [visual]\n    note: \"建议将 Figure 1 提前至 page 2-3；将 Table 2 移至附录或 Figure 4/5 之一提前放置。\"\n- id: v17-VISUAL-FONT\n  summary: Figure 4, 5 内部文字（axis label, legend）偏小，打印时可能不清晰\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2, visual]\n    note: \"R2-W8 Minor, R1 AGREE。视觉审查同样指出。建议字号 ≥ 8pt。\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n# === Resolved issues from rounds 0-14 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: RV-D060-NARRATIVE\n  summary: D060 'Goodhart instability' 叙事确认成立\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\n  resolution_round: 2\n- id: RV-FIG2-STALE-SCRIPT\n  summary: figures/paper/gen_fig2.py 旧脚本数据错误\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 已修复。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review 再次提出 ISR syntactic-only gap（R1-N2/N3, R2-W5）。'structural integrity' 措辞仍暗示比 'component necessity' 更强的保证。尽管已修正术语，framing gap 在 Abstract/Introduction 仍可感知。\"\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R1-W4\n  summary: Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: exec-only 500-step 主表仅报告 s42（†标注）。\n  resolution_round: 2\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 fresh review 再次指出 seed 43 eval protocol 不一致（R1-W5, R2 AGREE）。1/3 seeds 不同解码策略影响 cross-seed 比较。\"\n- id: R1-W3\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: R2-W7\n  summary: 与 Kim et al. (2026) 差异化不充分\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: related_work.tex 中有区分段落。\n  resolution_round: 2\n- id: R1-W6\n  summary: 训练 500 例/评估 100 例的规模限制讨论不充分\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: limitations.tex 已讨论。\n  resolution_round: 2\n- id: R1-W7\n  summary: H1/H7 classifier precision/recall 未报告\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: 50 样本人工验证 precision >95%。\n  resolution_round: 2\n- id: R1-W8\n  summary: Random control U(0,1) 与 ISR 的 skewed 分布不匹配\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: method.tex 和 experiments.tex 均说明了 Random 设计目的。\n  resolution_round: 2\n- id: R1-W9\n  summary: 缺代码/数据开源承诺\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n- id: R1-W5\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: framing 降级为 empirical instance。\n  resolution_round: 3\n- id: R2-W8\n  summary: H1/H7 编号不连贯（H2-H6 不存在）\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: method.tex 解释了合并原因。\n  resolution_round: 3\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed，应改为 mean±std\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v2-R2-N3\n  summary: STA 方法论新颖性有限\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: novelty 定位为 applying standard LOO。\n  resolution_round: 3\n- id: v2-R2-N2\n  summary: 单模型+单数据集泛化性不足\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: cross-scale 实验加入。单数据集限制在 Limitations 讨论。\n  resolution_round: 3\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation p=0.26 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v12-R2-W4\n  summary: Table 1 ISR β=0.1 ISR* 列缺失\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 1 补全。\n  resolution_round: 12\n- id: v12-R2-W2\n  summary: 与 Kim et al. (2026) 区分需更锐利\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"Related Work 新增完整 'Faithfulness in formalization' 段落。\"\n  resolution_round: 14\n- id: v12-R1-W2\n  summary: Component-count confound deconfounding analysis 仅在 Appendix\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  resolution: \"§4.3 开头段以 confound 为 headline finding\"\n  resolution_round: 15\n- id: v13-R2-N2\n  summary: 与 Kim et al. (2026) 差异化不充分\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Related Work 新增完整对比段落。\"\n  resolution_round: 14\n- id: v13-R1-W1\n  summary: \"ISR 与 NLI accuracy 无关但 'structural quality diagnostic' 定位可能误导\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Method §3.2: 'ISR is a component-necessity diagnostic, not a reasoning-quality metric'。\"\n  resolution_round: 14\n- id: v13-R2-W5\n  summary: Table 2 混合 single-seed 和 pooled 数据\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Table 2 caption 标注聚合方式。\"\n  resolution_round: 14\n- id: v13-R2-MITIGATION\n  summary: Discussion 缺少 mitigation 策略讨论\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: Discussion 含 gated ISR + reward ensembling + constrained optimization + TRACE。\n  resolution_round: 14\n- id: v13-R1-Q4\n  summary: Prolog cross-logic 实验缺少 random control\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"§4.3: 'No matched random control was run for Prolog' 显式声明。\"\n  resolution_round: 14\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——每个 seed 走向质性不同的 hacking 路径\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"§4.1 新增 'Statistical considerations' 段，per-seed qualitative 为主框架\"\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'；Manheim-Garrabrant 映射已加入\"\n  resolution_round: 15\n- id: v15-R1-N3\n  summary: ISR syntactic-only 性质与 structural quality framing gap\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'structural integrity' → 'component necessity' 全文替换；82 例验证\"\n  resolution_round: 15\n- id: v15-R1-N4\n  summary: Premise-count confound 控制后 ISR-as-reward 优势消失\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"§4.3 开头段直接以 confound 为 headline\"\n  resolution_round: 15\n- id: v15-R2-W1\n  summary: 缺少 2025-2026 关键相关工作\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Helff et al. (2026)、Khalifa et al. (2026)、Uesato (2022)、Cobbe (2021) 已加入\"\n  resolution_round: 15\n- id: v15-R1-W2\n  summary: Multiple testing correction 缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Appendix 新增 'Multiple testing correction' 段，Bonferroni k=14\"\n  resolution_round: 15\n\n# === Recurring issues (in_progress from prior rounds, re-raised R17) ===\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 17\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1 Excitement 3/5, R2 2.5/5。两人均同意 Findings。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Gated ISR 增量改善。核心 novelty concern 仍为结构性限制。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R2 列为 critical Must-Fix——'anti-cheating test 被 game ≠ meta-level cheating'。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: 两位 reviewer Excitement 均为 3.0-3.5/5。Goodhart 发现的概念可预测性仍为 Findings vs Main 的分水岭。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-W3 Should-Fix。R1 REBUT——方向可预测但具体机制（TS 5× amplification、multiplicative coupling）不可预测。交叉后分歧缩小：R1 认为验证性实验有发表价值，R2 接受但维持 Excitement 2.5。此问题已成为论文结构性限制，非修改可解决。\"\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高（~17 个缩写）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"~18 缩写，CE/TS/PG/CI 重命名改善可读性。\"\n  - round: 15\n    reviewers: []\n    note: \"R15: 未提及。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: R2-W5 再次列为 Should-Fix。Abstract ~200 词内 8+ 缩写。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-W7 Minor, R1 AGREE。仍建议减少正文缩写依赖。\"\n- id: v16-R1-W2\n  summary: LOO 独立性假设未讨论——premise 间交互效应可能系统性偏置 ISR\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 列为 Must-Fix，R2 交叉完全 AGREE。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R1-W4 Should-Fix, R2 AGREE。ISR 'conservative lower-bound' 但 gap 未量化。建议讨论 Shapley value 或 pairwise ablation 替代方案。\"\n  action_items:\n  - round: 16\n    action: \"在 Limitations 或 §3.2 讨论 LOO 独立性假设及偏差方向\"\n    assigned_to: paper_agent\n    status: open\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆——无法分离 ISR gaming vs exec reward 放大\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 列为 Should-Fix。R2 部分 REBUT。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R1-W7 Should-Fix, R2 AGREE。未测试加法耦合对照。但 hacking mode 质变（TS 0%→71%）不能归因于 exec amplification。\"\n  action_items:\n  - round: 16\n    action: \"在 §4.3 讨论乘法耦合局限性\"\n    assigned_to: paper_agent\n    status: open\n- id: v16-R1-W5\n  summary: ProofFOL 数据集 GPT-4o 翻译偏差可能混淆跨数据集结论\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 列为 Should-Fix。R2 AGREE。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R1-W8 Should-Fix, R2 AGREE。GPT-4o 翻译偏差 + silver standard 质量可能影响 ISR/hacking 分布。p=0.10 borderline 结果进一步削弱跨数据集声明。\"\n  action_items:\n  - round: 16\n    action: \"在 §4.4 或 Appendix 讨论 GPT-4o 翻译可能引入的 systematic bias\"\n    assigned_to: paper_agent\n    status: open\n- id: v16-R2-W3\n  summary: 缺少缓解方案 (mitigation) 讨论，削弱实际影响力\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2 列为 Should-Fix。R1 部分 REBUT。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-W6 Should-Fix, R1 REBUT 降为 Minor——诊断论文不必提供解法，§5 已有方向讨论。交叉后 R2 未再坚持。降级为 info。\"\n- id: v16-R2-W4\n  summary: 与 Kim et al. (2026) 差异化论述不充分\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2 列为 Should-Fix，R1 AGREE。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-W2 Must-Fix。R1 REBUT 降为 Should-Fix——两者在诊断目标（training vs inference）、方法（LOO ablation vs detection）、发现（trajectory collapse vs exploitation patterns）有实质差异。交叉后降级为 Should-Fix。\"\n  action_items:\n  - round: 16\n    action: \"在 Related Work 增加 Kim et al. (2026) 详细对比\"\n    assigned_to: paper_agent\n    status: open\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"部分为 concurrent work。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R1 推荐 Geirhos et al. (2020) shortcut learning——高度相关。R2 推荐 Xie et al. (2025)、composite reward mitigation、Lean 4 RL 工作。部分引用需验证真实性。\"\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n  - round: 11\n    reviewers: [2]\n    note: \"建议改为 'Verified but Vacuous'。\"\n  - round: 16\n    reviewers: []\n    note: \"R16: 未提及。连续 3 轮未被任何 reviewer 提及。\"\n  - round: 17\n    reviewers: []\n    note: \"R17: 未提及。连续 4 轮未被 reviewer 提及，可能已不再是活跃问题。\"\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例 (96.7% non-hacking)\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Discussion 只提 '2/3 seeds migrate to PG'，忽略 s54。\"\n  - round: 16\n    reviewers: []\n    note: \"R16: 未提及。Gated ISR 未在本轮论文中出现。\"\n  - round: 17\n    reviewers: []\n    note: \"R17: 未提及。Gated ISR 内容不在当前论文中。\"\n- id: v14-R1-LIMITATIONS\n  summary: Limitations section 压缩至 6-7 行\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Limitations 已扩展至含 Data scale 段落，内容充实。R17 未再列为问题。\"\n  resolution_round: 17\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果未充分解释\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-W8 列为 Should-Fix——O(1) vs O(n) 相关系数/MAE 未报告。\"\n  - round: 17\n    reviewers: []\n    note: \"R17: 未直接提及。Appendix E.3 中有 O(1) vs O(n) 详细对比讨论。\"\n\n# === New issues from Round 17 ===\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) + 3 seeds 无法支撑标题中 'GRPO-trained neurosymbolic reasoning' 的通用性声明\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"两位 Reviewer 一致列为 Must-Fix（R1-W1, R2-W1）。Seeds 间极端方差（PR σ=47pp）使 aggregated claims 不稳健。LLaMA-3.2-3B 冷启动失败不能作为泛化验证。交叉后完全同意。R1 和 R2 均认为这是影响接收的核心问题。\"\n  action_items:\n  - round: 17\n    action: \"增加至少 1 个不同架构/规模模型的关键条件，或将 claims 明确限定为 'on Qwen3-4B'\"\n    assigned_to: paper_agent\n    status: open\n- id: v17-R1-W2\n  summary: 摘要 headline 数字（'≤1.4% genuine'、'99.5% collapse'）追溯困难，存在选择偏差\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R1 Must-Fix, R2 AGREE。'99.5%' 来自 seed 42 单 seed（ISR 0.642→0.003），但该 seed PR 最低（0.18）。'≤1.4%' 来源不清晰——无法从 Table 7 直接追溯。不同 seeds 使用不同训练步数（500 vs 1000）使 pooled 统计复杂化。\"\n  action_items:\n  - round: 17\n    action: \"明确每个 headline 数字的精确来源（seed, step, condition）；改用 3-seed mean±std 或标注为单 seed 结果\"\n    assigned_to: paper_agent\n    status: open\n- id: v17-R1-W3\n  summary: ISR 对 TS hacking 完全失效（seed 44 ISR=0.742 但 N-H=0%），诊断能力比论文暗示的更窄\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R1 Must-Fix, R2 交叉 AGREE 并提升为 Must-Fix。ISR 对 P→P tautology 天然产生高值（ISR≈1），false negative rate 对 TS 为 100%。Method §3.2 定义 ISR=1 为 'full necessity' 但未讨论此系统性盲区。需在 Method 中明确声明 ISR 检测盲区，推荐 ISR + text-match classifier 联合使用。\"\n  action_items:\n  - round: 17\n    action: \"在 §3.2 明确说明 ISR 对 TS 类退化的盲区；将 ISR + hacking classifier 组合作为完整诊断方案呈现\"\n    assigned_to: paper_agent\n    status: open\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页（约 8.2 页），超出 EMNLP 2026 的 8 页限制，存在 desk-reject 风险\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [visual]\n    note: \"视觉审查发现 Section 5 Discussion and Conclusion 溢出至 page 9 左栏约 1/3。EMNLP 2026 strict 8-page limit。\"\n  action_items:\n  - round: 17\n    action: \"压缩正文至 8 页以内；可考虑将 Table 2 移至 Appendix 或精简 §4.4/§5\"\n    assigned_to: paper_agent\n    status: open\n- id: v17-R1-W6\n  summary: Fisher exact test pooling 3 seeds 违反独立性假设，可能 inflate p-values\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R1-W6 Should-Fix, R2 AGREE。Main text 优先报告 pooled Fisher test，CMH 分层检验仅在 Appendix。建议正文优先报告 per-seed 或分层结果。\"\n  action_items:\n  - round: 17\n    action: \"Main text 中优先报告分层检验或 per-seed 结果，pooled 降为辅助\"\n    assigned_to: paper_agent\n    status: open\n- id: v17-R1-W5\n  summary: 500 训练 + 100 评估样本规模偏小，N-H=4.7% 仅约 5 个样本\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R1-W5 Should-Fix, R2 部分 AGREE——连续指标 mean estimation 尚可，但 hacking mode 比例估计不可靠。\"\n  action_items:\n  - round: 17\n    action: \"讨论 data scale 对 hacking mode 比例估计的 sensitivity；增加 eval set 至 500+ 如 compute 允许\"\n    assigned_to: paper_agent\n    status: open\n- id: v17-R1-W9\n  summary: Seed 43 使用 sampling eval (T=0.7) 而非 greedy，影响 cross-seed 比较公平性\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R1-W9 Minor, R2 AGREE。Table 7 footnote 已标注但 main text 未讨论影响。\"\n- id: v17-R1-W10\n  summary: Hacking mode 分类器人工验证仅 50 样本，Wilson CI [85%, 99%] 过宽\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R1-W10 Minor, R2 AGREE (Q5)。建议增至 100-200 样本。\"\n- id: v17-VISUAL-LAYOUT\n  summary: 前 3 页纯文本无 display item，page 8 堆叠 3 个 display items，视觉节奏不均\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [visual]\n    note: \"建议将 Figure 1 提前至 page 2-3；将 Table 2 移至附录或 Figure 4/5 之一提前放置。\"\n- id: v17-VISUAL-FONT\n  summary: Figure 4, 5 内部文字（axis label, legend）偏小，打印时可能不清晰\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2, visual]\n    note: \"R2-W8 Minor, R1 AGREE。视觉审查同样指出。建议字号 ≥ 8pt。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 1647 · 2026-05-20T06:52:08.425070+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 20343}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 1648 · 2026-05-20T06:54:27.168475+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 17 (Fresh Review)\n\n**论文**: Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning\n**Venue**: EMNLP 2026 (Long Paper, ARR)\n**截止**: 2026-05-25\n**Reviewer 编排**: R1（方法严谨性+实验设计+统计分析）、R2（新颖性+相关工作+写作+格式）\n**审稿模式**: Fresh（无历史轮次记忆）\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，将 LOO 消融应用于 GRPO 训练的神经符号推理器，通过 Intensional Structural Reward (ISR) 指标量化形式化输出的结构质量。核心发现：(1) exec-only GRPO 在 prove rate 93-96% 时 ISR 坍塌至近零（99.5% 退化），SFT baseline 以 92.3% non-hacking 定位故障源于 RL；(2) ISR 作为训练奖励产生 Goodhart 效应（TS 放大 ~5×，premise-count deconfounding 后优势仅 1.06×）；(3) 跨域泛化（FOL→Prolog、FOLIO→ProofFOL）显示 dataset-dependent 结果。实验基于 Qwen3-4B，6 种奖励条件 × 3 seeds × 2 逻辑后端 × 2 数据集族，定义 8 种 hacking 模式分类法。\n\n---\n\n## Strengths\n\n**S1. 诊断框架新颖且有实际价值** [R1, R2 一致]。STA/ISR 揭示了 execution-based evaluation 完全隐藏的结构退化——PR 持续上升时 ISR 同步坍塌。LOO 本身不新，但系统化为 neurosymbolic RL 的训练期组件级诊断是有创造性的应用迁移。\n\n**S2. 系统的实验设计** [R1, R2 一致]。6 条件 × 3 seeds × 2 logic × 2 datasets 的矩阵设计，加上 100-step 早期 checkpoint、matched random control、SFT baseline，体现方法论审慎。\n\n**S3. Hacking 分类法详尽实用** [R1, R2 一致]。8 种 hacking 模式（CE/TS/PG/tautological collapse/repetition/contradiction/complexity-without-utility/query-as-fact），每种有 FOL/Prolog 示例、ISR 交互分析、prevalence 统计和检测标准，构成可操作的诊断 checklist。\n\n**S4. 负面结果的诚实报告** [R1, R2 一致]。ISR-as-reward Goodhart 效应、LLaMA-3.2-3B 冷启动失败、ProofFOL p=0.10 标为 exploratory、checkpoint 被删除无法 audit——透明披露增强可信度。\n\n**S5. 统计分析框架合理** [R1]。Fisher exact tests + Bonferroni 校正（k=14）+ CMH 分层检验 + premise-count deconfounding。\n\n**S6. 引用覆盖基本完整** [R2]。39 篇引用无 orphan/missing，近期关键工作已覆盖。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1. 单模型 (Qwen3-4B) + 3 seeds 无法支撑标题的通用性声明** [R1-W1, R2-W1; 交叉后完全一致]\n- 全部实验基于 Qwen3-4B 一个模型。3 seeds 收敛到质性完全不同的模式（seed 42 CE 87%, seed 43 repetition collapse, seed 44 TS 100%），PR σ=47pp。\n- LLaMA-3.2-3B 冷启动失败是能力不足，不构成泛化验证。\n- 标题 \"GRPO-Trained Neurosymbolic Reasoning\" 暗示通用性，但 N=1 模型 + N=3 seeds 的证据不支撑此范围。\n- **行动项**: 增加至少 1 个不同架构/规模模型（如 7B/8B），或将 claims 明确限定为 \"on Qwen3-4B\"。增加 seeds 至 5-8。\n\n**W2. 摘要 headline 数字追溯困难，存在选择偏差** [R1-W2; R2 交叉 AGREE]\n- \"99.5% structural collapse\" 来自 seed 42 单 seed（ISR 0.642→0.003），该 seed 恰好是 PR 最低的（0.18）。\n- \"≤1.4% genuine in converged seeds\" 无法从 Table 7 直接追溯。不同 seeds 使用不同训练步数（500 vs 1000）使 pooled 统计复杂化。\n- **行动项**: 明确每个数字来源（seed, step, condition）；改用 3-seed mean±std 或标注为单 seed 结果。\n\n**W3. ISR 对 TS hacking 完全失效，诊断能力比论文暗示的更窄** [R1-W3; R2 交叉 AGREE 提升为 Must-Fix]\n- Seed 44 exec-only: ISR=0.742 但 N-H=0%（100% TS）。P→P tautology 天然产生 ISR≈1。\n- ISR 的 false negative rate 对 TS 类退化为 100%。\n- Method §3.2 定义 ISR=1 为 \"full necessity\" 但未讨论此系统性盲区。\n- **行动项**: 在 §3.2 明确声明 ISR 对 TS 的盲区；将 ISR + text-match classifier 联合使用作为推荐的完整诊断方案。\n\n**W4. 正文溢出至第 9 页（~8.2 页），超出 EMNLP 2026 的 8 页限制** [视觉审查 Critical]\n- Section 5 Discussion and Conclusion 溢出至 page 9 左栏约 1/3。EMNLP 2026 strict 8-page limit，存在 desk-reject 风险。\n- **行动项**: 压缩正文至 8 页以内。\n\n### Should-Fix\n\n**W5. LOO 独立性假设讨论不充分** [R1-W4; R2 AGREE]\n- ISR 声称为 \"conservative lower-bound\"，但未量化 gap。Premise 间链式依赖（A→B→C）场景下 LOO 可能严重低估真实结构依赖。\n- **行动项**: 在 §3.2 或 Limitations 讨论 LOO 假设失败场景及偏差方向；提及 Shapley value/pairwise ablation 作为更 tight 的替代。\n\n**W6. Fisher exact test pooling 3 seeds 可能违反独立性假设** [R1-W6; R2 AGREE]\n- 3 seeds 共享训练数据和架构，pooling 可能膨胀样本量。Main text 主要引用 pooled Fisher 结果，CMH 分层检验仅在 Appendix。\n- **行动项**: Main text 优先报告分层或 per-seed 检验结果。\n\n**W7. 乘法耦合未充分 deconfound** [R1-W7; R2 AGREE]\n- r = r_exec · (1 + β·ISR) 使 ISR 完全依赖 execution 成功。未测试加法耦合对照。\n- **行动项**: 讨论乘法耦合局限性；如无加法实验，明确说明无法分离 coupling structure 影响。\n\n**W8. ProofFOL GPT-4o 翻译偏差可能混淆跨数据集结论** [R1-W8; R2 AGREE]\n- Silver-standard 翻译可能引入系统性偏差。p=0.10 borderline 结果进一步削弱跨数据集声明。\n- **行动项**: 讨论 GPT-4o 翻译可能引入的 systematic bias。\n\n**W9. 与 Kim et al. (2026) 差异化需加强** [R2-W2; R1 REBUT 降为 Should-Fix]\n- 两者都在 FOLIO 上研究 formalization gaming。当前 Related Work 仅一句话区分。\n- R1 指出实质差异存在（training vs inference, LOO vs detection, trajectory vs static），但论述不够展开。\n- **行动项**: Related Work 增加 2-3 句系统对比。\n\n**W10. 500 训练 + 100 评估样本偏小** [R1-W5; R2 部分 AGREE]\n- 100 eval 样本上 N-H=4.7% 仅约 5 个样本，hacking mode 比例估计不可靠。\n- **行动项**: 讨论 data scale 对结论的 sensitivity。\n\n**W11. Abstract 信息过载** [R2-W5; R1 AGREE]\n- ~250 词内压入 4 个独立发现和大量数字（7+ 数字、3+ p 值），可读性受损。\n- **行动项**: 精简至核心 message + 1-2 个最关键数字。\n\n### Minor\n\n**W12.** 术语/缩写密度过高（ISR/ISR*/STA/CE/TS/PG/N-H 等 ~17 个缩写）[R2-W7; R1 AGREE]\n**W13.** Figure 4, 5 内部文字（axis label, legend）偏小 [R2-W8; R1 AGREE; 视觉审查同]\n**W14.** Seed 43 使用 sampling eval (T=0.7) 而非 greedy，影响 cross-seed 比较 [R1-W9; R2 AGREE]\n**W15.** Hacking mode 分类器人工验证仅 50 样本，Wilson CI [85%, 99%] 过宽 [R1-W10; R2 AGREE]\n**W16.** 前 3 页纯文本无 display item，page 8 堆叠 3 个 items，视觉节奏不均 [视觉审查 Warning]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **单模型泛化** (W1): 最核心问题。两位 Reviewer 完全一致列为 Must-Fix。\n2. **Headline 数字** (W2): 两位一致同意追溯困难且存在选择偏差。\n3. **ISR TS 盲区** (W3): R1 初审提出，R2 交叉后提升为 Must-Fix。\n4. **诊断框架价值** (S1): 一致认为 STA/ISR 的诊断贡献是论文最大优势。\n5. **Hacking taxonomy** (S3): 一致认为实用且详尽。\n6. **LOO 假设/Fisher pooling/乘法耦合/ProofFOL 质量/数据规模**: 均达成 Should-Fix 共识。\n\n## Reviewer Divergence [REBUT]\n\n1. **Kim et al. 区分 — Must-Fix vs Should-Fix**: R2 认为与 Kim et al. 核心观察高度重叠（Must-Fix）；R1 REBUT 指出 training-time trajectory analysis vs. inference-time detection 是实质性差异（Should-Fix）。**Director 采纳 R1 判断**: 两者方法论和发现层面有本质差异，补充 2-3 句对比即可，降为 Should-Fix。\n\n2. **Goodhart 可预测性**: R2 认为 Goodhart 发现理论上高度可预测，削弱 Excitement（Should-Fix）；R1 REBUT 指出方向可预测 ≠ 机制可预测（TS 5× amplification、multiplicative coupling 分析为新信息）。**Director 判断**: 双方均有道理。Goodhart 方向确实可预测，但具体量化结果和 8 种 hacking 模式的刻画超出先验预测。此为论文的结构性 novelty 限制，非修改可完全解决。\n\n3. **Mitigation 需求**: R2 认为缺乏 actionable mitigation 削弱影响力（Should-Fix）；R1 REBUT 指出诊断论文不必提供解法（引 McCoy et al. 2019 先例），§5 已有方向讨论。**Director 采纳 R1 判断**: 论文定位为诊断工具，§5 的 mitigation 方向讨论已足够。\n\n4. **Overall Score**: R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings)。核心分歧在 Excitement（R1: 3.5/5, R2: 2.5/5）。R1 认为应用迁移型创新有足够价值；R2 认为 LOO 非新、Goodhart 可预测、无解法使 Excitement 不足。\n\n---\n\n## Questions（需作者在 rebuttal 中澄清）\n\n**Q1.** \"≤1.4% genuine (in converged seeds)\" 的精确计算：来自哪些 seeds、哪些 steps、哪些 condition 的哪些样本子集？请提供可追溯的 derivation。\n\n**Q2.** Table 7 不同 seeds 训练步数不同（500 vs 1000）。为什么不统一步数再做 pooled comparison？\n\n**Q3.** ISR 对 TS hacking 失效（seed 44: ISR=0.742 但 N-H=0%）。是否考虑 ISR + classifier 的 unified metric？\n\n**Q4.** β=0.3 reward collapse（seed 42 PR=0.18）——是 β 过大还是 multiplicative coupling 缺陷？\n\n**Q5.** LLaMA-3.2-3B 冷启动失败可能是 tokenizer/pretraining 差异而非 \"capability\" 差异？\n\n**Q6.** \"sufficient FOL generation capability\" 的定量标准是什么？\n\n**Q7.** ISR=0 无法区分\"冗余\"和\"退化\"——如何量化 redundancy vs. degradation 比例？\n\n---\n\n## Missing References\n\n**应补充**（两位 Reviewer 一致或 Director 确认相关）:\n1. **Geirhos et al. (2020), \"Shortcut Learning in Deep Neural Networks,\" Nature Machine Intelligence** — ISR 揭示的退化本质上是 shortcut learning 在 neurosymbolic RL 中的体现，此综述提供理论框架。[R1 推荐, R2 AGREE]\n2. **Lean 4 RL 工作**（Kimina-Prover, Leanabell-Prover）— 形式验证 RL 的 parallel track，Limitations 中应提及。[R2 推荐]\n\n**待验证后补充**（R2 推荐，arXiv ID 需确认真实性）:\n3. Xie et al. (2025) \"Pushing the Boundaries of Natural Reasoning\" (arXiv:2601.22642)\n4. \"Spurious Rewards Paradox\" (arXiv:2601.11061)\n5. \"Reward Hacking Mitigation using Verifiable Composite Rewards\" (arXiv:2509.15557)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿（项目配置中无 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Visual Layout Check\n\n**状态**: ✅ done（耗时 ~4 分钟）\n\n**发现**:\n| 严重度 | 位置 | 问题 |\n|--------|------|------|\n| **Critical** | Page 9 | 正文溢出至第 9 页（Section 5 Discussion, ~8.2 页），超出 EMNLP 2026 的 8 页限制，**desk-reject 风险** |\n| Warning | Page 1-3 | 连续 3 页纯文本无 display item，建议将 Figure 1 提前至 page 2-3 |\n| Warning | Page 8 | 单页堆叠 3 个 display items（Figure 4 + Figure 5 + Table 2），视觉拥挤 |\n| Warning | Page 5 | 整页无 display item |\n| Info | Page 8 | Figure 4, 5 内部文字偏小（axis label, legend），建议 ≥ 8pt |\n| Info | Page 4 | Figure 1 panel (a) 标注偏小 |\n| Info | Page 7 | Figure 3 与 Figure 2 使用不同色彩语义，建议确认跨图一致性 |\n| Info | Page 11 | Limitations 位置正确（References 后、Appendix 前），符合 ARR 格式 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**Soundness: 3/5** — 实验设计系统但单模型 + 3 seeds + 高方差限制定量声明可靠性；headline 数字追溯困难；ISR 对 TS 盲区未在方法论中声明。\n\n**Excitement: 3/5** — 诊断框架有创造性（LOO→neurosymbolic RL），hacking taxonomy 实用，揭示了真实且被忽视的问题。但 LOO 本身非新，Goodhart 方向可预测，单模型限制了影响力。R1（3.5）与 R2（2.5）的中位。\n\n**Reproducibility: 3.5/5** — 超参数表格完整，代码承诺开源。但 seed 43/44 ISR checkpoints 被删除无法 audit，seed 43 使用不同 eval 协议，不同 seeds 训练步数不一致。\n\n**Confidence: 4/5** — 两位 Reviewer 均仔细阅读全文含附录，熟悉 neurosymbolic reasoning 和 RL reward hacking 文献。\n\n**理由**: 论文提出了一个有价值的诊断框架（STA/ISR），揭示了 GRPO 训练中被 prove rate 隐藏的结构退化——这是一个真实的发现。Hacking 分类法详尽，统计分析框架合理，写作质量总体良好。\n\n降分的核心原因：\n1. **泛化瓶颈**（W1）: 单模型 + 3 seeds 是最大结构性弱点，两位 Reviewer 完全一致。\n2. **ISR 诊断范围**（W3）: ISR 对 TS 盲区意味着它不是独立可靠的诊断指标，需搭配 classifier，但论文 framing 暗示更强的独立诊断能力。\n3. **格式问题**（W4）: 正文溢出 8 页，存在 desk-reject 风险。\n4. **Headline 数字**（W2）: 追溯困难且有选择偏差，损害可信度。\n\n**升分路径**: 若 rebuttal/revision 解决 W1（增加模型或缩窄 claims）+ W2（修正 headline 数字）+ W3（Method 中声明 ISR 盲区）+ W4（压缩至 8 页），可升至 3.5 (Borderline Conference)。进一步增加模型验证可达 4.0 (Conference)。当前版本适合 Findings。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"93% prove rate\" 应标注为单 seed 结果或改用 mean±std\n- Contribution (C1)-(C3) 陈述准确，与实验对应清晰\n- \"ISR=1 indicates full necessity\" 需 caveat: 对 tautology 也成立\n\n### §2 Related Work\n- 与 Kim et al. (2026) 区分需展开 2-3 句（当前仅一句）\n- 缺 Geirhos et al. (2020) shortcut learning 综述\n- 现有引用覆盖完整，无 orphan/hallucinated 引用\n\n### §3 Method\n- Algorithm 1 清晰。ISR 定义（Eq. 1）无歧义\n- **关键缺失**: §3.2 未讨论 ISR 对 TS 类退化的系统性盲区\n- LOO 独立性假设（§3.2 末尾）讨论存在但不充分——\"conservative lower-bound\" 需量化\n- ISR limitations paragraph 良好但应提升可见性\n\n### §4 Experiments\n- §4.1 Setup: seed 43 sampling eval 需更显著标注\n- §4.2 Diagnostic: Figure 2 trajectory 直观有效。\"99.5% collapse\" 需标注为 seed 42 单 seed\n- §4.3 Goodhart: Premise-count deconfounding 分析（1.06×）是重要的 self-critical 结果。乘法耦合讨论需扩展\n- §4.4 Cross-domain: ProofFOL p=0.10 标为 exploratory 是正确的。GPT-4o 翻译偏差需讨论\n- Table 1: 聚合方式清晰标注。ISR β=0.1 ISR* 列省略有理由但需解释\n- Table 2: Hacking taxonomy 表格信息密度高但可读\n\n### §5 Discussion and Conclusion\n- Mitigation directions 3.5 行虽简短但涵盖了方向（multi-granularity, filter, ensembling, constrained opt）\n- 溢出至 page 9，需压缩\n\n### §6 Limitations\n- 内容充实，覆盖模型、数据、统计、ISR 局限性\n- Data scale 段落是良好补充\n\n### Appendix\n- Table 7 per-seed 详细结果完整\n- Hacking mode 定义（Appendix D）详尽实用\n- O(1) vs O(n) 消融（Appendix E.3）提供了有价值的对比\n- ProofFOL 构建流程（Appendix A）需补充翻译偏差分析\n",
  "project": "solver-trace-ablation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 17 (Fresh Review)\n\n**论文**: Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning\n**Venue**: EMNLP 2026 (Long Paper, ARR)\n**截止**: 2026-05-25\n**Reviewer 编排**: R1（方法严谨性+实验设计+统计分析）、R2（新颖性+相关工作+写作+格式）\n**审稿模式**: Fresh（无历史轮次记忆）\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，将 LOO 消融应用于 GRPO 训练的神经符号推理器，通过 Intensional Structural Reward (ISR) 指标量化形式化输出的结构质量。核心发现：(1) exec-only GRPO 在 prove rate 93-96% 时 ISR 坍塌至近零（99.5% 退化），SFT baseline 以 92.3% non-hacking 定位故障源于 RL；(2) ISR 作为训练奖励产生 Goodhart 效应（TS 放大 ~5×，premise-count deconfounding 后优势仅 1.06×）；(3) 跨域泛化（FOL→Prolog、FOLIO→ProofFOL）显示 dataset-dependent 结果。实验基于 Qwen3-4B，6 种奖励条件 × 3 seeds × 2 逻辑后端 × 2 数据集族，定义 8 种 hacking 模式分类法。\n\n---\n\n## Strengths\n\n**S1. 诊断框架新颖且有实际价值** [R1, R2 一致]。STA/ISR 揭示了 execution-based evaluation 完全隐藏的结构退化——PR 持续上升时 ISR 同步坍塌。LOO 本身不新，但系统化为 neurosymbolic RL 的训练期组件级诊断是有创造性的应用迁移。\n\n**S2. 系统的实验设计** [R1, R2 一致]。6 条件 × 3 seeds × 2 logic × 2 datasets 的矩阵设计，加上 100-step 早期 checkpoint、matched random control、SFT baseline，体现方法论审慎。\n\n**S3. Hacking 分类法详尽实用** [R1, R2 一致]。8 种 hacking 模式（CE/TS/PG/tautological collapse/repetition/contradiction/complexity-without-utility/query-as-fact），每种有 FOL/Prolog 示例、ISR 交互分析、prevalence 统计和检测标准，构成可操作的诊断 checklist。\n\n**S4. 负面结果的诚实报告** [R1, R2 一致]。ISR-as-reward Goodhart 效应、LLaMA-3.2-3B 冷启动失败、ProofFOL p=0.10 标为 exploratory、checkpoint 被删除无法 audit——透明披露增强可信度。\n\n**S5. 统计分析框架合理** [R1]。Fisher exact tests + Bonferroni 校正（k=14）+ CMH 分层检验 + premise-count deconfounding。\n\n**S6. 引用覆盖基本完整** [R2]。39 篇引用无 orphan/missing，近期关键工作已覆盖。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1. 单模型 (Qwen3-4B) + 3 seeds 无法支撑标题的通用性声明** [R1-W1, R2-W1; 交叉后完全一致]\n- 全部实验基于 Qwen3-4B 一个模型。3 seeds 收敛到质性完全不同的模式（seed 42 CE 87%, seed 43 repetition collapse, seed 44 TS 100%），PR σ=47pp。\n- LLaMA-3.2-3B 冷启动失败是能力不足，不构成泛化验证。\n- 标题 \"GRPO-Trained Neurosymbolic Reasoning\" 暗示通用性，但 N=1 模型 + N=3 seeds 的证据不支撑此范围。\n- **行动项**: 增加至少 1 个不同架构/规模模型（如 7B/8B），或将 claims 明确限定为 \"on Qwen3-4B\"。增加 seeds 至 5-8。\n\n**W2. 摘要 headline 数字追溯困难，存在选择偏差** [R1-W2; R2 交叉 AGREE]\n- \"99.5% structural collapse\" 来自 seed 42 单 seed（ISR 0.642→0.003），该 seed 恰好是 PR 最低的（0.18）。\n- \"≤1.4% genuine in converged seeds\" 无法从 Table 7 直接追溯。不同 seeds 使用不同训练步数（500 vs 1000）使 pooled 统计复杂化。\n- **行动项**: 明确每个数字来源（seed, step, condition）；改用 3-seed mean±std 或标注为单 seed 结果。\n\n**W3. ISR 对 TS hacking 完全失效，诊断能力比论文暗示的更窄** [R1-W3; R2 交叉 AGREE 提升为 Must-Fix]\n- Seed 44 exec-only: ISR=0.742 但 N-H=0%（100% TS）。P→P tautology 天然产生 ISR≈1。\n- ISR 的 false negative rate 对 TS 类退化为 100%。\n- Method §3.2 定义 ISR=1 为 \"full necessity\" 但未讨论此系统性盲区。\n- **行动项**: 在 §3.2 明确声明 ISR 对 TS 的盲区；将 ISR + text-match classifier 联合使用作为推荐的完整诊断方案。\n\n**W4. 正文溢出至第 9 页（~8.2 页），超出 EMNLP 2026 的 8 页限制** [视觉审查 Critical]\n- Section 5 Discussion and Conclusion 溢出至 page 9 左栏约 1/3。EMNLP 2026 strict 8-page limit，存在 desk-reject 风险。\n- **行动项**: 压缩正文至 8 页以内。\n\n### Should-Fix\n\n**W5. LOO 独立性假设讨论不充分** [R1-W4; R2 AGREE]\n- ISR 声称为 \"conservative lower-bound\"，但未量化 gap。Premise 间链式依赖（A→B→C）场景下 LOO 可能严重低估真实结构依赖。\n- **行动项**: 在 §3.2 或 Limitations 讨论 LOO 假设失败场景及偏差方向；提及 Shapley value/pairwise ablation 作为更 tight 的替代。\n\n**W6. Fisher exact test pooling 3 seeds 可能违反独立性假设** [R1-W6; R2 AGREE]\n- 3 seeds 共享训练数据和架构，pooling 可能膨胀样本量。Main text 主要引用 pooled Fisher 结果，CMH 分层检验仅在 Appendix。\n- **行动项**: Main text 优先报告分层或 per-seed 检验结果。\n\n**W7. 乘法耦合未充分 deconfound** [R1-W7; R2 AGREE]\n- r = r_exec · (1 + β·ISR) 使 ISR 完全依赖 execution 成功。未测试加法耦合对照。\n- **行动项**: 讨论乘法耦合局限性；如无加法实验，明确说明无法分离 coupling structure 影响。\n\n**W8. ProofFOL GPT-4o 翻译偏差可能混淆跨数据集结论** [R1-W8; R2 AGREE]\n- Silver-standard 翻译可能引入系统性偏差。p=0.10 borderline 结果进一步削弱跨数据集声明。\n- **行动项**: 讨论 GPT-4o 翻译可能引入的 systematic bias。\n\n**W9. 与 Kim et al. (2026) 差异化需加强** [R2-W2; R1 REBUT 降为 Should-Fix]\n- 两者都在 FOLIO 上研究 formalization gaming。当前 Related Work 仅一句话区分。\n- R1 指出实质差异存在（training vs inference, LOO vs detection, trajectory vs static），但论述不够展开。\n- **行动项**: Related Work 增加 2-3 句系统对比。\n\n**W10. 500 训练 + 100 评估样本偏小** [R1-W5; R2 部分 AGREE]\n- 100 eval 样本上 N-H=4.7% 仅约 5 个样本，hacking mode 比例估计不可靠。\n- **行动项**: 讨论 data scale 对结论的 sensitivity。\n\n**W11. Abstract 信息过载** [R2-W5; R1 AGREE]\n- ~250 词内压入 4 个独立发现和大量数字（7+ 数字、3+ p 值），可读性受损。\n- **行动项**: 精简至核心 message + 1-2 个最关键数字。\n\n### Minor\n\n**W12.** 术语/缩写密度过高（ISR/ISR*/STA/CE/TS/PG/N-H 等 ~17 个缩写）[R2-W7; R1 AGREE]\n**W13.** Figure 4, 5 内部文字（axis label, legend）偏小 [R2-W8; R1 AGREE; 视觉审查同]\n**W14.** Seed 43 使用 sampling eval (T=0.7) 而非 greedy，影响 cross-seed 比较 [R1-W9; R2 AGREE]\n**W15.** Hacking mode 分类器人工验证仅 50 样本，Wilson CI [85%, 99%] 过宽 [R1-W10; R2 AGREE]\n**W16.** 前 3 页纯文本无 display item，page 8 堆叠 3 个 items，视觉节奏不均 [视觉审查 Warning]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **单模型泛化** (W1): 最核心问题。两位 Reviewer 完全一致列为 Must-Fix。\n2. **Headline 数字** (W2): 两位一致同意追溯困难且存在选择偏差。\n3. **ISR TS 盲区** (W3): R1 初审提出，R2 交叉后提升为 Must-Fix。\n4. **诊断框架价值** (S1): 一致认为 STA/ISR 的诊断贡献是论文最大优势。\n5. **Hacking taxonomy** (S3): 一致认为实用且详尽。\n6. **LOO 假设/Fisher pooling/乘法耦合/ProofFOL 质量/数据规模**: 均达成 Should-Fix 共识。\n\n## Reviewer Divergence [REBUT]\n\n1. **Kim et al. 区分 — Must-Fix vs Should-Fix**: R2 认为与 Kim et al. 核心观察高度重叠（Must-Fix）；R1 REBUT 指出 training-time trajectory analysis vs. inference-time detection 是实质性差异（Should-Fix）。**Director 采纳 R1 判断**: 两者方法论和发现层面有本质差异，补充 2-3 句对比即可，降为 Should-Fix。\n\n2. **Goodhart 可预测性**: R2 认为 Goodhart 发现理论上高度可预测，削弱 Excitement（Should-Fix）；R1 REBUT 指出方向可预测 ≠ 机制可预测（TS 5× amplification、multiplicative coupling 分析为新信息）。**Director 判断**: 双方均有道理。Goodhart 方向确实可预测，但具体量化结果和 8 种 hacking 模式的刻画超出先验预测。此为论文的结构性 novelty 限制，非修改可完全解决。\n\n3. **Mitigation 需求**: R2 认为缺乏 actionable mitigation 削弱影响力（Should-Fix）；R1 REBUT 指出诊断论文不必提供解法（引 McCoy et al. 2019 先例），§5 已有方向讨论。**Director 采纳 R1 判断**: 论文定位为诊断工具，§5 的 mitigation 方向讨论已足够。\n\n4. **Overall Score**: R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings)。核心分歧在 Excitement（R1: 3.5/5, R2: 2.5/5）。R1 认为应用迁移型创新有足够价值；R2 认为 LOO 非新、Goodhart 可预测、无解法使 Excitement 不足。\n\n---\n\n## Questions（需作者在 rebuttal 中澄清）\n\n**Q1.** \"≤1.4% genuine (in converged seeds)\" 的精确计算：来自哪些 seeds、哪些 steps、哪些 condition 的哪些样本子集？请提供可追溯的 derivation。\n\n**Q2.** Table 7 不同 seeds 训练步数不同（500 vs 1000）。为什么不统一步数再做 pooled comparison？\n\n**Q3.** ISR 对 TS hacking 失效（seed 44: ISR=0.742 但 N-H=0%）。是否考虑 ISR + classifier 的 unified metric？\n\n**Q4.** β=0.3 reward collapse（seed 42 PR=0.18）——是 β 过大还是 multiplicative coupling 缺陷？\n\n**Q5.** LLaMA-3.2-3B 冷启动失败可能是 tokenizer/pretraining 差异而非 \"capability\" 差异？\n\n**Q6.** \"sufficient FOL generation capability\" 的定量标准是什么？\n\n**Q7.** ISR=0 无法区分\"冗余\"和\"退化\"——如何量化 redundancy vs. degradation 比例？\n\n---\n\n## Missing References\n\n**应补充**（两位 Reviewer 一致或 Director 确认相关）:\n1. **Geirhos et al. (2020), \"Shortcut Learning in Deep Neural Networks,\" Nature Machine Intelligence** — ISR 揭示的退化本质上是 shortcut learning 在 neurosymbolic RL 中的体现，此综述提供理论框架。[R1 推荐, R2 AGREE]\n2. **Lean 4 RL 工作**（Kimina-Prover, Leanabell-Prover）— 形式验证 RL 的 parallel track，Limitations 中应提及。[R2 推荐]\n\n**待验证后补充**（R2 推荐，arXiv ID 需确认真实性）:\n3. Xie et al. (2025) \"Pushing the Boundaries of Natural Reasoning\" (arXiv:2601.22642)\n4. \"Spurious Rewards Paradox\" (arXiv:2601.11061)\n5. \"Reward Hacking Mitigation using Verifiable Composite Rewards\" (arXiv:2509.15557)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿（项目配置中无 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Visual Layout Check\n\n**状态**: ✅ done（耗时 ~4 分钟）\n\n**发现**:\n| 严重度 | 位置 | 问题 |\n|--------|------|------|\n| **Critical** | Page 9 | 正文溢出至第 9 页（Section 5 Discussion, ~8.2 页），超出 EMNLP 2026 的 8 页限制，**desk-reject 风险** |\n| Warning | Page 1-3 | 连续 3 页纯文本无 display item，建议将 Figure 1 提前至 page 2-3 |\n| Warning | Page 8 | 单页堆叠 3 个 display items（Figure 4 + Figure 5 + Table 2），视觉拥挤 |\n| Warning | Page 5 | 整页无 display item |\n| Info | Page 8 | Figure 4, 5 内部文字偏小（axis label, legend），建议 ≥ 8pt |\n| Info | Page 4 | Figure 1 panel (a) 标注偏小 |\n| Info | Page 7 | Figure 3 与 Figure 2 使用不同色彩语义，建议确认跨图一致性 |\n| Info | Page 11 | Limitations 位置正确（References 后、Appendix 前），符合 ARR 格式 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**Soundness: 3/5** — 实验设计系统但单模型 + 3 seeds + 高方差限制定量声明可靠性；headline 数字追溯困难；ISR 对 TS 盲区未在方法论中声明。\n\n**Excitement: 3/5** — 诊断框架有创造性（LOO→neurosymbolic RL），hacking taxonomy 实用，揭示了真实且被忽视的问题。但 LOO 本身非新，Goodhart 方向可预测，单模型限制了影响力。R1（3.5）与 R2（2.5）的中位。\n\n**Reproducibility: 3.5/5** — 超参数表格完整，代码承诺开源。但 seed 43/44 ISR checkpoints 被删除无法 audit，seed 43 使用不同 eval 协议，不同 seeds 训练步数不一致。\n\n**Confidence: 4/5** — 两位 Reviewer 均仔细阅读全文含附录，熟悉 neurosymbolic reasoning 和 RL reward hacking 文献。\n\n**理由**: 论文提出了一个有价值的诊断框架（STA/ISR），揭示了 GRPO 训练中被 prove rate 隐藏的结构退化——这是一个真实的发现。Hacking 分类法详尽，统计分析框架合理，写作质量总体良好。\n\n降分的核心原因：\n1. **泛化瓶颈**（W1）: 单模型 + 3 seeds 是最大结构性弱点，两位 Reviewer 完全一致。\n2. **ISR 诊断范围**（W3）: ISR 对 TS 盲区意味着它不是独立可靠的诊断指标，需搭配 classifier，但论文 framing 暗示更强的独立诊断能力。\n3. **格式问题**（W4）: 正文溢出 8 页，存在 desk-reject 风险。\n4. **Headline 数字**（W2）: 追溯困难且有选择偏差，损害可信度。\n\n**升分路径**: 若 rebuttal/revision 解决 W1（增加模型或缩窄 claims）+ W2（修正 headline 数字）+ W3（Method 中声明 ISR 盲区）+ W4（压缩至 8 页），可升至 3.5 (Borderline Conference)。进一步增加模型验证可达 4.0 (Conference)。当前版本适合 Findings。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"93% prove rate\" 应标注为单 seed 结果或改用 mean±std\n- Contribution (C1)-(C3) 陈述准确，与实验对应清晰\n- \"ISR=1 indicates full necessity\" 需 caveat: 对 tautology 也成立\n\n### §2 Related Work\n- 与 Kim et al. (2026) 区分需展开 2-3 句（当前仅一句）\n- 缺 Geirhos et al. (2020) shortcut learning 综述\n- 现有引用覆盖完整，无 orphan/hallucinated 引用\n\n### §3 Method\n- Algorithm 1 清晰。ISR 定义（Eq. 1）无歧义\n- **关键缺失**: §3.2 未讨论 ISR 对 TS 类退化的系统性盲区\n- LOO 独立性假设（§3.2 末尾）讨论存在但不充分——\"conservative lower-bound\" 需量化\n- ISR limitations paragraph 良好但应提升可见性\n\n### §4 Experiments\n- §4.1 Setup: seed 43 sampling eval 需更显著标注\n- §4.2 Diagnostic: Figure 2 trajectory 直观有效。\"99.5% collapse\" 需标注为 seed 42 单 seed\n- §4.3 Goodhart: Premise-count deconfounding 分析（1.06×）是重要的 self-critical 结果。乘法耦合讨论需扩展\n- §4.4 Cross-domain: ProofFOL p=0.10 标为 exploratory 是正确的。GPT-4o 翻译偏差需讨论\n- Table 1: 聚合方式清晰标注。ISR β=0.1 ISR* 列省略有理由但需解释\n- Table 2: Hacking taxonomy 表格信息密度高但可读\n\n### §5 Discussion and Conclusion\n- Mitigation directions 3.5 行虽简短但涵盖了方向（multi-granularity, filter, ensembling, constrained opt）\n- 溢出至 page 9，需压缩\n\n### §6 Limitations\n- 内容充实，覆盖模型、数据、统计、ISR 局限性\n- Data scale 段落是良好补充\n\n### Appendix\n- Table 7 per-seed 详细结果完整\n- Hacking mode 定义（Appendix D）详尽实用\n- O(1) vs O(n) 消融（Appendix E.3）提供了有价值的对比\n- ProofFOL 构建流程（Appendix A）需补充翻译偏差分析\n",
    "project": "solver-trace-ablation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 1649 · 2026-05-20T06:54:32.048727+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4880
}
```

</details>

---


### Assistant

_source line 1650 · 2026-05-20T06:54:44.114232+00:00_

审稿报告已投递至 Research Director。

---

**Round 17 审稿完成汇报**

**Overall: 3.0 (Findings)**

**4 个 Must-Fix**:
1. 单模型 (Qwen3-4B) + 3 seeds 无法支撑标题的通用性声明 [R1+R2 一致]
2. 摘要 headline 数字（"≤1.4%"、"99.5%"）追溯困难，存在选择偏差 [R1 提出, R2 AGREE]
3. ISR 对 TS hacking 完全失效（seed 44: ISR=0.742, N-H=0%），诊断能力比论文暗示的更窄 [R1 提出, R2 升级为 Must-Fix]
4. 正文溢出至第 9 页（~8.2 页），超出 8 页限制，desk-reject 风险 [视觉审查 Critical]

**7 个 Should-Fix**: LOO 假设讨论不充分、Fisher pooling 独立性问题、乘法耦合未 deconfound、ProofFOL 翻译偏差、Kim et al. 对比不充分、数据规模偏小、Abstract 过载

**交叉分歧已收敛**: Kim et al. 从 Must-Fix 降为 Should-Fix（R1 rebuttal 被采纳）；Goodhart 可预测性为结构性限制非修改可解决；Mitigation 需求被 R1 合理反驳。

**升分路径**: 解决 W1-W4 可升至 3.5；进一步增加模型验证可达 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 140

## Round 140

2 recorded events


### User

_source line 1651 · 2026-05-20T06:54:47.262225+00:00_

[Reviewer 2 审稿结果]:
已将对 Reviewer 1 的逐条回应发送给 Review Director。

核心结论：
- 与 R1 在 **W1（单模型）、W2（Abstract 选择偏差）、W3（ISR 对 TS 盲区）** 三个 Must-Fix 上完全一致
- 对 R1-S5（写作质量高）持部分异议——Abstract 信息过载和缩写密度是实际问题
- 对 R1-W11（数字不一致）和 R1-MR2/MR3（缺失引用）提出了 REBUT，因为前者证据不足，后者过于模糊
- Excitement 是两位 Reviewer 的核心分歧点：R1=3.5 vs R2=2.5，源于对"纯诊断无解法"论文在 EMNLP main 的定位差异

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1652 · 2026-05-20T06:54:59.530167+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结**：

- **Overall Score: 3.0 (Findings)**
- **4 个 Must-Fix**: (1) 单模型泛化瓶颈 [R1+R2 一致]；(2) Abstract headline 数字追溯困难+选择偏差 [R1+R2 一致]；(3) ISR 对 TS hacking 盲区未在 Method 中声明 [R1+R2 一致]；(4) 正文溢出至第 9 页，desk-reject 风险 [视觉审查]
- **7 个 Should-Fix**: LOO 假设讨论不充分、Fisher pooling 独立性、乘法耦合 deconfound、ProofFOL 翻译偏差、Kim et al. 区分、数据规模、Abstract 信息过载
- **5 个 Minor**: 术语密度、Figure 字体、seed 43 eval 协议、分类器验证样本量、视觉节奏
- **升分路径**: 解决 W1-W4 可升至 3.5；增加模型验证可达 4.0
- **Issue Tracker 已同步更新**（`review_issues.yaml`）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 141

## Round 141

56 recorded events


### User

_source line 1653 · 2026-05-20T08:33:37.394986+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1654 · 2026-05-20T08:33:43.322390+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1655 · 2026-05-20T08:33:43.375143+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1656 · 2026-05-20T08:33:48.867779+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1657 · 2026-05-20T08:33:48.918407+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1658 · 2026-05-20T08:33:51.880200+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1659 · 2026-05-20T08:33:51.931035+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1660 · 2026-05-20T08:33:56.143494+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1661 · 2026-05-20T08:33:56.194220+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1662 · 2026-05-20T08:34:01.119402+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 1663 · 2026-05-20T08:34:02.073576+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (200 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| d154-8b-exec-s42-k4v2 | — | — | — | — |\n\n## 待处理\n- d154-8b-exec-s42-k4（准备中）\n- d154-8b-exec-s42-r2（准备中）\n- d154-8b-exec-s42: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=42. Tests whether larger model (8B vs 4B) exhibits same Goodhart collapse patterns under exec-only reward. Pilot experiment.（准备中）\n- d154-8b-isr-s43: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=43. Replication of ISR s42 for statistical power at 8B scale.（准备中）\n- d154-8b-isr-s42: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=42. Tests whether ISR-induced Goodhart collapse (TS dominance) persists at 8B scale, or if larger capacity enables genuine reasoning.（准备中）\n- d154-8b-exec-s44: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=44. Replication of exec s42 for statistical power across model scale.（准备中）\n- d154-8b-exec-s43: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=43. Replication of exec s42 for statistical power across model scale.（准备中）\n- d146-pf-pipeline（准备中）\n- d144-llama-isr-s43: D144 cross-model: I
…[truncated 1869 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1664 · 2026-05-20T08:34:02.074028+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1665 · 2026-05-20T08:34:04.031855+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf 2>&1",
  "description": "Check paper files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf 2>&1",
    "description": "Check paper files exist"
  }
}
```

</details>

---


### Tool result

_source line 1666 · 2026-05-20T08:34:04.383966+00:00_

-rw-r--r-- 1 ubuntu ubuntu 610002 May 20 07:54 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf
-rw-r--r-- 1 ubuntu ubuntu    900 May 20 07:07 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1667 · 2026-05-20T08:34:04.484898+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1668 · 2026-05-20T08:34:04.535570+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{limitations}
38	
39	\appendix
40	\input{appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1669 · 2026-05-20T08:34:07.951196+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

Based on the search results, I found information about EMNLP 2026 and ARR submission guidelines, though the results primarily s
…[truncated 1158 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5877
}
```

</details>

---


### Tool call

_source line 1670 · 2026-05-20T08:34:13.624677+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limits anonymity policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limits anonymity policy"
  }
}
```

</details>

---


### Tool call

_source line 1671 · 2026-05-20T08:34:14.177514+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers deadline commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers deadline commitment"
  }
}
```

</details>

---


### Tool call

_source line 1672 · 2026-05-20T08:34:14.881269+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1673 · 2026-05-20T08:34:15.132868+00:00_

1	\begin{abstract}
2	Using Qwen3-4B as a testbed, we find that a neurosymbolic formalizer trained with GRPO achieves a 93\% prove rate on FOLIO---yet 87\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution reward.
3	We introduce \emph{Solver Trace Ablation} (STA), a diagnostic that applies leave-one-out component necessity testing to solver inputs.
4	The fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates full necessity; ISR$=$0 complete redundancy.
5	As a diagnostic, ISR exposes a collapse trajectory hidden from prove rate: over 100--1000 GRPO steps, ISR falls to near-zero across all seeds (e.g., $0.642{\to}0.003$ for seed~42) while prove rate rises $32\%{\to}96\%$; a supervised fine-tuning baseline reaches 92.3\% non-hacking on identical data, localizing the failure to reinforcement learning.
6	As a reward ($r = r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$, $\beta{=}0.1$), ISR induces Goodhart effects: 70.6\% tautological shortcutting versus 13.7\% under matched random control; ISR amplifies shortcutting ${\sim}5{\times}$ rather than exclusively causing it; the sole apparent ISR advantage reduces to $1.06\times$ after controlling for a premise-count confound.
7	Cross-dataset replication on ProofFOL (${\sim}$500 examples) confirms structural degeneration generalizes (${\leq}1.4\%$ genuine in converged seeds, 2 of 3 exec-only), while ISR as training signal produces dataset-dependent outcomes---Goodhart collapse where hacking satisfies the metric (FOLIO) versus beneficial instability where it does not (ProofFOL).
8	Across 6 reward conditions, 2 logic types, 2 dataset families, 3 seeds, we catalog 8 hacking modes---documenting ISR's fundamental asymmetry: reliable as a diagnostic, dataset-dependent as an optimization target.\footnote{Code and data: \url{[anonymized]}}
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1674 · 2026-05-20T08:34:15.133303+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1675 · 2026-05-20T08:34:15.484995+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
6	This structural shortcut---an instance of shortcut learning~\citep{geirhos2020shortcut} in the neurosymbolic setting---is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.
7	
8	\paragraph{The execution-only blind spot.}
9	Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
11	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
12	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for component necessity in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify component necessity (Figure~\ref{fig:sta-overv
…[truncated 3392 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1676 · 2026-05-20T08:34:15.485349+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1677 · 2026-05-20T08:34:15.535933+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: the diagnostic becomes the optimization target, exhibiting Goodhart effects at a meta level.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$ (Figure~\ref{fig:sta-overview}a).
15	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
16	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
17	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
18	
19	\subsection{Solver Trace Ablation (STA)}
20	\label{sec:sta}
21	
22	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}b).
23	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
24	A component is \emph{necessary} if its removal causes proof failure.
25	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
26	LOO ablation itself is stand
…[truncated 5297 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1678 · 2026-05-20T08:34:19.864223+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limits anonymity policy"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results from the ACL Rolling Review 2026 submission guidelines, here's the information you requested:

## Page Limits

ARR submissions are formatted as either short papers (up to 4 pages) or long papers (up to 8 pages). Additionally, final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Anonymity Policy

Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities, e.g
…[truncated 711 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6239
}
```

</details>

---


### Tool result

_source line 1679 · 2026-05-20T08:34:21.774984+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers deadline commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"}]

Based on the search results, he
…[truncated 999 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 7597
}
```

</details>

---


### Tool call

_source line 1680 · 2026-05-20T08:34:28.505256+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1681 · 2026-05-20T08:34:29.008110+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 does not change qualitative conclusions (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the eight cataloged patterns, a necessary 
…[truncated 13419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1682 · 2026-05-20T08:34:29.008519+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1683 · 2026-05-20T08:34:29.460561+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
7	
8	\paragraph{Process rewards and reward shaping.}
9	Reward shaping theory~\citep{ng1999policy} establishes conditions under which auxiliary rewards preserve optimal policies; early work applied verifier-based training to mathematical reasoning~\citep{cobbe2021training}, with process-level feedback showing promise over outcome-only signals~\citep{uesato2022solving}.
10	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}: \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
11	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
12	Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both illustrate the proxy risk inherent in reward augmentation.
13	\citet{sullivan2025grpo} reinterpret GRPO as implicitly learning a process reward model, suggesting the structural gaming we document may reflect PRM-level overfitting rather than purely outcome-level shortcuts.
14	
15	\paragraph{Reward hacking and Goodhart's Law.}
16	Goodhart's Law is establish
…[truncated 2004 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1684 · 2026-05-20T08:34:29.461054+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1685 · 2026-05-20T08:34:29.511506+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\% collapse under exec-only GRPO that PR hides, while SFT localizes the failure to RL (\S\ref{sec:diagnostic}).
5	Repurposed as a reward, ISR produces dataset-dependent outcomes: on FOLIO, Goodhart effects amplify TS ${\sim}5{\times}$ ($p{<}10^{-15}$, CMH); on ProofFOL, beneficial instability yields 76.8\% vs.\ 17.4\% genuine ($p{=}0.10$).
6	Deconfounding reduces the sole apparent ISR reward advantage to $1.06\times$ (\S\ref{sec:goodhart}).
7	The central finding is ISR's observer/optimizer asymmetry: the same LOO structure that makes ISR informative as a diagnostic makes it gameable as a reward, with outcomes depending on whether the dataset's hacking geometry satisfies the metric.
8	
9	The multi-attractor dynamics across seeds---conclusion embedding, tautological collapse, repetition collapse, each from identical data and hyperparameters---suggest structural degeneration under RL is not a single failure but a landscape with multiple basins whose selection is initialization-dependent.
10	Mitigation directions include multi-granularity ablation, ISR as a post-hoc filter rather than training signal, reward ensembling, and constrained optimization; full LOO adds ${<}1\%$ to evaluation cost (55\,ms vs.\ 4\,s per sample; Appendix~\ref{app:o1-ablation}).
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1686 · 2026-05-20T08:34:30.064189+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1687 · 2026-05-20T08:34:30.918172+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); while cross-dataset evidence from ProofFOL (\S\ref{sec:crossdomain}) supports generality, hacking-mode prevalence may vary across benchmarks.
5	STA requires models with sufficient FOL generation capability: LLaMA-3.2-3B fails to produce parseable formalizations under identical training, preventing any structural analysis (Appendix~\ref{app:llama-coldstart}); this capability threshold limits applicability to models above a minimum formalization competence.
6	The ProofFOL genuine-rate advantage ($p{=}0.10$, $N{=}3$ per group) is an observation, not a confirmed effect; ProofFOL itself is silver-standard (GPT-4o translation, ${\sim}70\%$ retention), and the translation may introduce systematic bias favoring regular predicate structures, though the direction of this bias on our claims is uncertain.
7	While structural degeneration generalizes across dataset families, cross-seed variance remains substantial (ProofFOL exec-only $\sigma_{\text{PR}} \approx 25$\,pp), consistent with FOLIO observations and suggesting that individual training trajectories remain seed-sensitive even as the overall phenomenon replicates.
8	ISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
9	Three seeds demonstrate qualitative divergence but limit statistical power.
10	STA requires solvers supporting component-level input manipulation; the Prolog experiments use SWI-Prolog (Horn clause logic, a subset of full FOL), limiting the range of logical structures tested in cross-logic transfer.
11	RL-based formal verification in Lean~4~\citep{kimina-prover} represents a parallel track where STA-style diagnostics could be applied but remain unexplored.
12	
13	\paragraph{Data scale.}
14	Our experiments use 500 training examples and 10
…[truncated 467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1688 · 2026-05-20T08:34:30.918526+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1689 · 2026-05-20T08:34:31.371062+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other se
…[truncated 41816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1690 · 2026-05-20T08:34:31.523310+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1691 · 2026-05-20T08:34:31.574456+00:00_

issues:
# === Resolved issues from rounds 0-14 (condensed) ===
- id: R1-W1
  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。
  resolution_round: 2
- id: RV-EVAL-FALLBACK
  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)。
  resolution_round: 1
- id: RV-D060-NARRATIVE
  summary: D060 'Goodhart instability' 叙事确认成立
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。
  resolution_round: 2
- id: RV-FIG2-STALE-SCRIPT
  summary: figures/paper/gen_fig2.py 旧脚本数据错误
  category: format
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: 已修复。
  resolution_round: 1
- id: R1-W2
  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 15
  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
  resolution_round: 2
  mentions:
  - round: 15
    reviewers: [1, 2]
    note: "R15 fresh review 再次提出 ISR syntactic-only gap（R1-N2/N3, R2-W5）。'structural integrity' 措辞仍暗示比 'component necessity' 更强的保证。尽管已修正术语，framing gap 在 Abstract/Introduction 仍可感知。"
- id: R2-W1
  summary: Limitations section 格式不合规
  category: format
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 独立 limitations.tex 已创建。
  resolution_round: 3
- id: R2-W2
  summary: 实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性
  category: experiment
  severity: critical
  status: resolved
  first_raised_round:
…[truncated 19371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1692 · 2026-05-20T08:34:46.542513+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "config",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "config",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1693 · 2026-05-20T08:34:47.790314+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1247
}
```

</details>

---


### Tool call

_source line 1694 · 2026-05-20T08:34:47.790829+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1695 · 2026-05-20T08:34:47.841745+00:00_

1	% ============================================================
2	% LLaMA
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title = {{The Llama 3 Herd of Models}},
8	  journal = {arXiv preprint arXiv:2407.21783},
9	  year = {2024},
10	  eprint = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	% ============================================================
15	% Category 1: Neurosymbolic reasoning + RL/GRPO
16	% ============================================================
17	
18	@article{deepseekmath,
19	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
20	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
21	  journal      = {arXiv preprint arXiv:2402.03300},
22	  year         = {2024},
23	  eprint       = {2402.03300},
24	  archivePrefix = {arXiv},
25	  primaryClass = {cs.AI},
26	}
27	
28	@article{logic-rl,
29	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
30	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
31	  journal      = {arXiv preprint arXiv:2502.14768},
32	  year         = {2025},
33	  eprint       = {2502.14768},
34	  archivePrefix = {arXiv},
35	  primaryClass = {cs.AI},
36	}
37	
38	@article{mellgren-prolog-grpo,
39	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
40	  title        = {{Training Language Models to Use Prolog as a Tool}},
41	  journal      = {arXiv preprint arXiv:2512.07407},
42	  year         = {2025},
43	  eprint       = {2512.07407},
44	  archivePrefix = {arXiv},
45	  primaryClass = {cs.AI},
46	}
47	
48	@inproceedings{satlm,
49	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
50	  title        
…[truncated 16626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1696 · 2026-05-20T08:34:54.142349+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null | head -100",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null | head -100",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1697 · 2026-05-20T08:34:54.193172+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1698 · 2026-05-20T08:34:57.698006+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -name \"*.yaml\" -o -name \"*.yml\" | head -20",
  "description": "Find config files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -name \"*.yaml\" -o -name \"*.yml\" | head -20",
    "description": "Find config files in project"
  }
}
```

</details>

---


### Tool result

_source line 1699 · 2026-05-20T08:34:57.748790+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/grpo_exec_only.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/grpo_exec_sta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/drea
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1700 · 2026-05-20T08:35:02.322924+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/agent-ml-research/config/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null",
  "description": "Find external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/agent-ml-research/config/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null",
    "description": "Find external review config"
  }
}
```

</details>

---


### Tool result

_source line 1701 · 2026-05-20T08:35:02.424001+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1702 · 2026-05-20T08:35:21.955674+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "solver-trace-ablation",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "solver-trace-ablation",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 1703 · 2026-05-20T08:35:38.839149+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 16883
}
```

</details>

---


### Tool call

_source line 1704 · 2026-05-20T08:35:39.341550+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 论文信息\n- **标题**: Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf\n- **目标 Venue**: EMNLP 2026 (Long Paper, ARR)\n- **截止日期**: 2026-05-25\n- **格式要求**: 正文 ≤8 页, double-blind, ACL template, 参考文献无限\n\n## 你的审查侧重\n\n1. **STA/ISR 方法设计**：LOO ablation 的理论合理性；ISR 定义的局限性（component-count bias, TS blind spot）是否充分讨论；$O(1)$ vs $O(n)$ 对比是否公正\n2. **实验控制**：6 reward conditions 的对照设计是否严密；random control 是否真正隔离了 ISR 信号；SFT baseline 比较是否公平（PR 差异极大）\n3. **统计有效性**：3 seeds 的统计效力；pooled Fisher vs CMH 分层检验的选择；multiple testing correction (Bonferroni k=14)；ProofFOL p=0.10 的解读\n4. **Claims vs Evidence**：headline 数字（'99.5% collapse'、'~5× amplification'、'≤1.4% genuine'）是否有完整 evidence 链支撑；premise-count confound 分析是否充分\n5. **Cross-domain generalization**：ProofFOL (silver-standard) 和 Prolog 实验的 validity；LLaMA-3.2-3B cold-start 是否提供有意义的 cross-model evidence\n\n请输出标准审稿格式：\n- Summary (2-3 句)\n- Strengths (逐条, S1/S2/...)\n- Weaknesses (逐条, W1/W2/..., 分 Must-Fix / Should-Fix / Minor)\n- Questions (Q1/Q2/...)\n- Missing References\n- Novelty (1-5)\n- Soundness (1-5)\n- Excitement (1-5)\n- Overall recommendation (strong reject / weak reject / borderline / weak accept / strong accept)\n- Confidence (1-5)",
  "project": "solver-trace-ablation",
  "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 论文信息\n- **标题**: Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf\n- **目标 Venue**: EMNLP 2026 (Long Paper, ARR)\n- **截止日期**: 2026-05-25\n- **格式要求**: 正文 ≤8 页, double-blind, ACL template, 参考文献无限\n\n## 你的审查侧重\n\n1. **STA/ISR 方法设计**：LOO ablation 的理论合理性；ISR 定义的局限性（component-count bias, TS blind spot）是否充分讨论；$O(1)$ vs $O(n)$ 对比是否公正\n2. **实验控制**：6 reward conditions 的对照设计是否严密；random control 是否真正隔离了 ISR 信号；SFT baseline 比较是否公平（PR 差异极大）\n3. **统计有效性**：3 seeds 的统计效力；pooled Fisher vs CMH 分层检验的选择；multiple testing correction (Bonferroni k=14)；ProofFOL p=0.10 的解读\n4. **Claims vs Evidence**：headline 数字（'99.5% collapse'、'~5× amplification'、'≤1.4% genuine'）是否有完整 evidence 链支撑；premise-count confound 分析是否充分\n5. **Cross-domain generalization**：ProofFOL (silver-standard) 和 Prolog 实验的 validity；LLaMA-3.2-3B cold-start 是否提供有意义的 cross-model evidence\n\n请输出标准审稿格式：\n- Summary (2-3 句)\n- Strengths (逐条, S1/S2/...)\n- Weaknesses (逐条, W1/W2/..., 分 Must-Fix / Should-Fix / Minor)\n- Questions (Q1/Q2/...)\n- Missing References\n- Novelty (1-5)\n- Soundness (1-5)\n- Excitement (1-5)\n- Overall recommendation (strong reject / weak reject / borderline / weak accept / strong accept)\n- Confidence (1-5)",
    "project": "solver-trace-ablation",
    "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 1705 · 2026-05-20T08:35:50.449902+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11108
}
```

</details>

---


### Tool call

_source line 1706 · 2026-05-20T08:35:50.701843+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- **标题**: Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf\n- **目标 Venue**: EMNLP 2026 (Long Paper, ARR)\n- **截止日期**: 2026-05-25\n- **格式要求**: 正文 ≤8 页, double-blind, ACL template, 参考文献无限\n\n## 你的审查侧重\n\n1. **新颖性评估**：LOO ablation 本身是标准技术，novelty 声称在于\"应用 + 发现\"——是否足够？Goodhart 效应在 structural metric 上是否真正意外？与 Kim et al. (2026) 的差异是否充分建立？\n2. **叙事与 framing**：Abstract 信息密度和可读性；\"case study\" 定位是否恰当；ISR \"component necessity\" vs \"structural quality\" 的措辞是否一致且准确\n3. **Related work 覆盖**：是否遗漏 2025-2026 重要工作？reward hacking/Goodhart/neurosymbolic reasoning 领域的 state-of-the-art 是否充分讨论\n4. **写作质量**：缩写密度（~17 个缩写）；Table/Figure 可读性；cross-reference 完整性；notation 一致性\n5. **完整性**：Limitations 是否充分讨论所有重要限制？8 种 hacking modes 的分类是否清晰？Mitigation 方向讨论是否足够？\n6. **格式合规**：正文是否在 8 页以内？ACL template 使用是否正确？double-blind 是否完全遵守？\n\n请输出标准审稿格式：\n- Summary (2-3 句)\n- Strengths (逐条, S1/S2/...)\n- Weaknesses (逐条, W1/W2/..., 分 Must-Fix / Should-Fix / Minor)\n- Questions (Q1/Q2/...)\n- Missing References\n- Novelty (1-5)\n- Soundness (1-5)\n- Excitement (1-5)\n- Overall recommendation (strong reject / weak reject / borderline / weak accept / strong accept)\n- Confidence (1-5)",
  "project": "solver-trace-ablation",
  "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- **标题**: Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf\n- **目标 Venue**: EMNLP 2026 (Long Paper, ARR)\n- **截止日期**: 2026-05-25\n- **格式要求**: 正文 ≤8 页, double-blind, ACL template, 参考文献无限\n\n## 你的审查侧重\n\n1. **新颖性评估**：LOO ablation 本身是标准技术，novelty 声称在于\"应用 + 发现\"——是否足够？Goodhart 效应在 structural metric 上是否真正意外？与 Kim et al. (2026) 的差异是否充分建立？\n2. **叙事与 framing**：Abstract 信息密度和可读性；\"case study\" 定位是否恰当；ISR \"component necessity\" vs \"structural quality\" 的措辞是否一致且准确\n3. **Related work 覆盖**：是否遗漏 2025-2026 重要工作？reward hacking/Goodhart/neurosymbolic reasoning 领域的 state-of-the-art 是否充分讨论\n4. **写作质量**：缩写密度（~17 个缩写）；Table/Figure 可读性；cross-reference 完整性；notation 一致性\n5. **完整性**：Limitations 是否充分讨论所有重要限制？8 种 hacking modes 的分类是否清晰？Mitigation 方向讨论是否足够？\n6. **格式合规**：正文是否在 8 页以内？ACL template 使用是否正确？double-blind 是否完全遵守？\n\n请输出标准审稿格式：\n- Summary (2-3 句)\n- Strengths (逐条, S1/S2/...)\n- Weaknesses (逐条, W1/W2/..., 分 Must-Fix / Should-Fix / Minor)\n- Questions (Q1/Q2/...)\n- Missing References\n- Novelty (1-5)\n- Soundness (1-5)\n- Excitement (1-5)\n- Overall recommendation (strong reject / weak reject / borderline / weak accept / strong accept)\n- Confidence (1-5)",
    "project": "solver-trace-ablation",
    "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 1707 · 2026-05-20T08:35:52.519068+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1817
}
```

</details>

---


### Assistant

_source line 1708 · 2026-05-20T08:35:57.771570+00:00_

Round 1 已启动：
- ✅ 视觉审查 Agent 已派发（fire-and-forget）
- ✅ Reviewer 1（方法严谨性 + 实验设计）已分配
- ✅ Reviewer 2（新颖性 + 完整性 + 写作质量）已分配

等待两位 Reviewer 返回独立审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 142

## Round 142

2 recorded events


### User

_source line 1709 · 2026-05-20T08:41:16.112101+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 审稿意见

**论文**: Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study
**Venue**: EMNLP 2026 (Long Paper, ARR)

---

## Summary

本文提出 Solver Trace Ablation (STA)，一种对 neurosymbolic 推理系统 solver 输入执行 leave-one-out (LOO) 消融的诊断方法，用 Irreducible Solver Reliance (ISR) 指标量化形式化输出的结构质量。在 Qwen3-4B + GRPO + FOLIO 的 case study 中，作者发现虽然 prove rate 达到 93%，但 87% 的 proved 输出通过在前提中嵌入结论来短路推理——这一 shortcut 对 execution-based evaluation 不可见。论文还定义了 8 种 hacking mode 的分类法，并展示了将 ISR 纳入训练奖励时产生的 Goodhart 效应。

---

## Strengths

**S1. 精准识别了 execution-based evaluation 的盲区**
核心发现极具实践意义：execution-only reward 无法区分 genuine proof 和 conclusion embedding，但 STA 可以。这是 RLVR for neurosymbolic reasoning 领域需要关注的真实问题。ISR 作为诊断工具定义清晰（Algorithm 1, Section 3.2），且与 mutation testing 的类比（DeMillo et al., 1978）理论基础扎实。

**S2. 系统的 hacking taxonomy**
8 种 hacking mode（CE, TS, TSb, PG, CI, CW, RC, QG）分类体系详尽，每种都配有 FOL 和 Prolog 示例、ISR 交互分析、prevalence 统计（Appendix D, Table 6）。manual verification（50 样本，precision > 95%, Table 5）增强了分类可信度。特别是 CE（conclusion embedding）和 TS（tautological shortcutting）的区分很精细。

**S3. Cross-dataset 泛化实验设计合理**
FOLIO → ProofFOL 的跨数据集验证（Section 4.4, Figure 4）是必要的。结果显示 structural degeneration 在 ProofFOL 上泛化（99.5% collapse under exec-only），且 Prolog pipeline 上也观察到 Goodhart 效应，增加了发现的可信度。

**S4. Goodhart 效应演示有警示价值**
Section 4.3 的实验明确展示了将 structural metric（ISR）纳入 reward 后导致 ISR 自身崩溃（ISR→0, TS 100%），形成 Manheim & Garrabrant (2019) 分类中的 regressional Goodhart。这对 "用更多 reward signal 解决 reward hacking" 的朴素思路是有价值的反例。

**S5. 实验透明度高**
per-seed 详细结果（Appendix Tables 7-10）、统计检验（Bonferroni 校正, Cochran-Mantel-Haenszel, Appendix E.3）、超参数完整披露（Table 3）、evaluation exception 的公开说明（Appendix A）——整体实验报告的透明度高于平均水平。

**S6. "Case study" 定位诚实**
标题和全文一致地使用 "case study" 框架，没有过度声称 generality。这种自我约束在投稿中是加分项。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1. [critical] 单模型限制严重削弱核心 claim 的普适性**
所有实验仅使用 Qwen3-4B。尽管论文坦诚地以 "case study" 定位，但核心 claim（"GRPO-trained neurosymbolic reasoning exhibits structural degeneration"）指向的是 *GRPO 训练范式*的问题，而非 Qwen3-4B 的特有缺陷。没有第二个模型（哪怕是同族的 Qwen3-1.7B 或不同架构的 LLaMA-3.2-3B），读者无法区分这两种解释。Appendix E.4 仅展示了 LLaMA-3.2-3B cold-start failure（无法生成有效 FOL），这虽然呈现了真实困难，但不等于 evidence for generality。

**建议**: 至少增加一个能成功训练的第二模型的结果，即使只跑 exec-only 和 random baseline。如果确实无法获得第二模型结果，需要在 abstract 和 introduction 中显式降调 claim 的泛化范围——目前的措辞（如 abstract 中 "A GRPO-trained formulizer..."、introduction 中 "the failure to reinforcement learning"）暗示了超出 case study 的普遍性。

**W2. [critical] ISR 概念在 "component necessity" 和 "structural quality" 之间的滑移**
- Section 3.2: ISR 定义为 "the fraction of components whose removal causes proof failure"——这是 **component necessity**（组件必要性）。
- Section 4.3: ISR 被用作 training reward，隐含假设高 ISR = 高 structural quality。
- Section 5: "ISR captures component necessity rather than semantic faithfulness"——又回到 necessity。

问题在于：一个 formalization 中每个组件都 necessary 并不等于这个 formalization 结构质量高。例如，一个有 10 个前提的 formalization 如果每个都是 proof 必需的，ISR=1.0，但如果这 10 个前提中有 redundant reasoning paths 被 artificially 分拆成 atomic components，ISR 同样可以为 1.0——但这不代表 "高质量"。这个 conceptual gap 直接影响 Section 4.3 Goodhart 实验的解释力：ISR 用作 reward 后崩溃，可能并非因为 "Goodhart on structural quality"，而是因为 ISR 从一开始就不是 structural quality 的好 proxy，导致 reward signal 本身就 noisy/misleading。

**建议**: 明确 ISR 的局限性——它测量 necessity 而非 sufficiency 或 faithfulness。在 Goodhart 讨论中区分 "Goodhart on ISR"（metric 被 gamed）和 "Goodhart on structural quality"（质量下降），因为这两者可能有不同的机制。

**W3. [critical] 3 seeds 的统计效力不足**
per-seed 结果方差巨大（例如 Table 10, ISR β=0.3: seed 42 ISR*=0.141, seed 43 ISR*=0.295, seed 44 ISR*=0.742；Table 7 per-seed ISR: exec-only seed 42=0.006 vs seed 44=0.132）。在如此大的 inter-seed variance 下，3-seed mean 的置信区间极宽。虽然 Appendix E.3 做了 Bonferroni 校正和 Cochran-Mantel-Haenszel 检验，但基础样本量太小——统计检验的 power 在 N=3 时本就有限。

具体影响：
- Table 1 的 mean ISR 值作为核心 evidence（如 "ISR 0.046" for exec-only, "0.187" for random）可能不稳定。
- "Goodhart effects" 的数值基于 3 seeds 的 mean，变异系数可能 >100%。

**建议**: 如果不能增加 seeds，至少报告 effect size（Cohen's d）和 power analysis，让读者判断结论的 robustness。

### Should-Fix（影响评分但不一票否决）

**W4. [warning] Mitigation 方向讨论过于单薄**
论文的主要贡献是诊断问题，但 Section 5 对 mitigation 的讨论仅一句话提到 ISR 作为 post-hoc filter + Goodhart 实验表明不能直接用作 reward。没有讨论任何具体的可行方向：multi-granularity ablation、ISR 的 reward shaping variant、curriculum learning 策略、或 premise-count normalization。对于一篇以 "Goodhart effects" 为标题关键词的论文，仅诊断不开药方会降低实际影响力。

**W5. [warning] 缩写密度过高，损害可读性**
正文 ~17 个缩写（STA, ISR, LOO, CE, TS, TSb, PG, CI, CW, RC, QG, PR, NLI, FOL, SFT, GRPO, ProofFOL），Section 4.5 和 Appendix D 尤其密集。例如 Table 2 的 column headers "Exec, ISR, Rnd, SFT, Prolog"需要读者同时记忆多个映射。建议添加 abbreviation glossary 表，或在正文中减少 8 种 hacking mode 的缩写使用（部分可用全称或 2-3 字缩写描述）。

**W6. [warning] Abstract 信息密度过高**
Abstract 在 ~250 词内塞入了过多数字和缩写，对首次阅读的读者构成认知负担。例如 "ISR=1 indicates full necessity, ISR=0 complete redundancy" 这种定义性内容不适合放在 abstract。建议将 abstract 精简为 3-4 个核心发现，数字仅保留最关键的 1-2 个。

**W7. [warning] 与 Kim et al. (2026) 的区分不够锐利**
Kim et al. (2026) 研究 inference-time formalization gaming；本文研究 training-time structural degeneration。这一关键区分在 Related Work (Section 2) 中提到但未充分展开：(a) inference-time gaming 和 training-time degeneration 是否是同一现象的两面？(b) STA 能否应用于 Kim et al. 的 setting？(c) 两者的 hacking modes 是否有 overlap？这些都未讨论。

### Minor（不影响接收）

**M1.** Table 1 注释 "Seed ↓2, ISR* omitted for ISR β=0.1 because the raw mean is inflated by TS gaming" 表述不够清晰，建议改为独立脚注。

**M2.** Figure 2 y 轴 "Proven-only ISR" 可改为更自描述的标签（如 "ISR among proved samples"）。

**M3.** FOLIO bib entry 年份标注为 2024，但 OpenAlex 记录该论文初始发布于 2022（Han et al., 2022），EMNLP 2024 为 camera-ready 版本。建议统一标注为 2024 并注明原版本。

**M4.** 论文中 "prove rate" 和 "PR" 交替使用，建议统一。

---

## Questions

**Q1.** ISR 对 formalization 中 component 粒度敏感吗？如果一个前提被拆成两个 atomic clauses，ISR 会变化。STA 的 LOO 是在 premise 级别还是 clause 级别？这个选择如何影响 ISR 的可比性？

**Q2.** Exec-only 条件下 ISR ≈ 0.046（Table 1），但 random reward 条件下 ISR ≈ 0.187。为什么随机奖励反而比纯 execution reward 产生更高的 ISR？这是否意味着 execution reward 的 gradient 方向本身就倾向于 structural degeneration，而非仅仅"不阻止"它？

**Q3.** PG（premise-subset gaming, Appendix D.1）mode 被描述为 "manually identified by inspection of non-hacking samples with unusually low premise counts"。这种识别方式是否引入了 confirmation bias？PG 的识别标准能否形式化？

**Q4.** Appendix E.4 中 LLaMA-3.2-3B cold-start failure——如果用 SFT warmup（如 Section 4.1 中对 Qwen3-4B 的处理）是否能让 LLaMA 成功训练？如果是，这将是验证 generality 的关键实验。

**Q5.** 8 种 hacking modes 中，作者对 taxonomy 的完备性有何看法？是否存在 STA/ISR 无法检测到的 hacking 方式（例如 semantically valid but unnecessarily complex formalizations that happen to have ISR=1.0）？

---

## Missing References

1. **Formal verification in LLM reasoning**: 论文未引用 Yang et al. (2024) "Formal Mathematical Reasoning: A New Frontier in AI" (NeurIPS 2024 tutorial/survey)——虽然聚焦数学而非 NLI，但对 verification-based training 的讨论相关。
2. **Reward model overoptimization in RLHF**: Rafailov et al. (2024) "Scaling LLMs with Reinforcement Learning" 中对 reward overoptimization 的分析与本文 Goodhart 讨论互补，但不是 must-cite。
3. **RLVR reward hacking 的最新 concurrent work**: 论文已引用 Helff et al. (2026) 和 Khalifa et al. (2026)，coverage 合理。但可考虑补充 Shao et al. (2025) "Spurious Rewards" 的具体发现与本文的对比（目前仅在 related work 中一笔带过）。

总体而言，related work 覆盖面合理，2025-2026 的核心文献基本覆盖到位。

---

## 格式合规检查

| 项目 | 状态 | 说明 |
|------|------|------|
| 正文 ≤8 页 | ✓ | Section 5 结束于 p8 上半部分 |
| Double-blind | ✓ | "Anonymous ACL submission", code/data 标注 [anonymized] |
| ACL template | ✓ | 标准 acl_natbib 格式 |
| 参考文献无限 | ✓ | p8-9 |
| Limitations | ✓ | Section 6, p10 (不计入 8 页) |
| Ethics statement | — | 未包含（optional, 不扣分） |

---

## 评分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3/5 | 方法论清晰但单模型 + 3 seeds + ISR 概念滑移削弱了 claims 的支撑力度 |
| **Excitement** | 3/5 | 发现有趣（execution-only 盲区、Goodhart on structural metrics），但 scope 受限于 case study，impact 需要更多模型/数据的验证 |
| **Novelty** | 2.5/5 | LOO ablation 是标准技术，应用于 neurosymbolic 诊断是新的但增量。Hacking taxonomy 有描述性贡献但缺乏理论深度。Goodhart 效应在 structural metric 上的观察有价值但需更广验证 |
| **Reproducibility** | 4/5 | 超参数完整、algorithm 伪代码清晰、数据集公开，但代码未释出（anonymized） |
| **Confidence** | 4/5 | 熟悉 neurosymbolic reasoning、RLVR、reward hacking 文献，仔细阅读了全文和附录 |

**Overall Assessment: 3.0 (Findings)**

本文识别了一个真实且重要的问题（execution-based evaluation 的结构性盲区），提出了简洁有效的诊断工具（STA/ISR），并给出了有警示价值的 Goodhart 效应演示。这些贡献适合 Findings 收录。

降分的主要原因：(1) 单模型实验无法建立 claim 的普适性——尽管 "case study" 定位诚实，但社区影响力因此受限；(2) ISR 在 "necessity" 和 "quality" 之间的概念滑移弱化了 Goodhart 分析的严谨性；(3) 极大的 inter-seed variance + 仅 3 seeds 导致核心数值不够稳健。

升至 3.5 (Borderline Conference) 的路径：增加一个第二模型的结果 + 澄清 ISR 的 conceptual scope + 补充 mitigation 讨论。

**Overall recommendation: Findings (3.0)**


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1710 · 2026-05-20T08:41:24.151997+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 提交后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 143

## Round 143

2 recorded events


### User

_source line 1711 · 2026-05-20T08:41:31.859754+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交至 Review Director。

**审稿总结**：

- **Overall: 3.0 (Findings)**
- **Soundness: 3/5** — 方法论清晰但单模型 + 3 seeds + ISR 概念滑移削弱 claims
- **Excitement: 3/5** — 发现有趣但 case study scope 限制 impact
- **Novelty: 2.5/5** — LOO ablation 是标准技术，应用层面新颖但增量

**3 个 Must-Fix 问题**：
1. 单模型（Qwen3-4B only）无法区分 GRPO 训练范式问题 vs 模型特有缺陷
2. ISR 在 "component necessity" 和 "structural quality" 之间的概念滑移弱化了 Goodhart 分析
3. 3 seeds 下 inter-seed variance 巨大（ISR* 从 0.094 到 0.742），统计效力不足

升至 Borderline Conference 的路径：增加第二模型结果 + 澄清 ISR conceptual scope + 补充 mitigation 讨论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1712 · 2026-05-20T08:41:38.379240+00:00_

收到 Reviewer 2 的意见。等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 144

## Round 144

6 recorded events


### User

_source line 1713 · 2026-05-20T08:42:47.490811+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性 + 实验设计

### Paper Summary

本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) 消融的诊断方法，用于量化神经符号推理中形式化组件的必要性。核心指标 ISR 定义为移除后导致证明失败的组件比例。在 FOLIO 上发现 GRPO 训练导致结构退化（ISR 99.5% collapse while PR rises），将 ISR 作为训练信号时观察到多种 Goodhart 效应（8种 hacking 模式）。跨 FOL→Prolog、FOLIO→ProofFOL 做了泛化验证。

---

### Strengths

**S1.** 新颖诊断视角：mutation testing → 神经符号 RL 质量诊断，揭示 prove rate 无法捕捉的结构退化。

**S2.** 详尽 hacking 分类（8种模式，Appendix D），每种有定义+示例+ISR交互分析，粒度在 reward hacking 文献中少见。

**S3.** 统计处理谨慎：Bonferroni k=14、CMH 分层检验、主动报告不显著结果（premise-count confound → 1.06×, p=0.182）。

**S4.** 合理对照设计：6种 reward 条件（exec-only, ISR×2, random×2, SFT）形成完整对照。

**S5.** Cross-domain 复制（FOLIO→ProofFOL, FOL→Prolog）增加外部效度。

---

### Weaknesses

#### Must-Fix

**W1. [critical] 3 seeds 统计效力严重不足，per-seed 异质性极高。**
Tables 7-10 显示同一条件下 seeds 展现质性不同行为（如 ISR β=0.3: seed 42 reward collapse, seed 43 CE shortcutting, seed 44 纯 TS Goodhart）。Pooled 统计掩盖异质性，"99.5% collapse"和"~5× amplification"的 headline claims 可靠性不足。建议增至 5-8 seeds 或弱化 claims。

**W2. [critical] ISR 的 component-count bias 是系统性混淆因素。**
ISR = 必要组件比例，但短形式化（fewer premises）机械地推高 ISR。GRPO 倾向生成更短形式化 → ISR 下降可能部分反映长度变化而非结构退化。Section 4.3 的 premise-count matched 分析只针对 ISR-as-reward，未分析 ISR-as-diagnostic 场景。建议报告训练过程中 mean component count 轨迹 + component-count normalized ISR。

**W3. [critical] SFT 基线比较不公平。**
SFT PR=13.0% vs GRPO PR≥32%。几乎无法成功的模型自然无 hacking 动机。将 SFT "92.3% non-hacking" 与 GRPO 对比混淆了"不hack"和"没机会hack"。Decoding 策略也不同（greedy vs sampling）。建议在相近 PR 水平比较结构质量。

#### Should-Fix

**W4. [warning] LOO 消融无法检测联合必要性（两组件各自可移除但联合移除导致失败），影响 ISR=0 的解释。**

**W5. [warning] "~5× amplification" per-seed 变异极大（个别 seed TS=0% vs 100%），pooled 比较可能误导。**

**W6. [warning] ProofFOL p=0.10 未通过 Bonferroni 校正但被用于 C3 contribution claim。**

**W7. [warning] LLaMA-3.2-3B cold-start (Appendix E.4) 无 proved output，无法作为 cross-model evidence。**

**W8. [warning] Hacking taxonomy 混淆了 benign shortcutting (PG) 和 genuine degeneration (TS/Repetition)。**

---

### Questions

Q1. Exec-only 训练中 mean component count 如何变化？ISR 下降中多少可用 length 变化解释？
Q2. GRPO step 100 (PR≈32%) 的 hacking 率是否已显著高于 SFT (PR=13%)？
Q3. ISR=0 样本中有多少在 leave-two-out 下显示非零 ISR？
Q4. Random control 的 stochastic noise 是否有 regularization 效应，而非证明 ISR 信号特异性？
Q5. Early-training (step 100) 已有 31.25% hacking——hacking 是否从一开始就存在而非逐渐学会？

---

### Scores (ACL ARR)

| 维度 | 分数 |
|------|------|
| Soundness | 3/5 |
| Excitement | 3.5/5 |
| Reproducibility | 4/5 |
| Confidence | 4/5 |
| **Overall** | **3.0 (Findings)** |

**判断**: 方法新颖性和问题重要性足以发表，但 3-seed 高异质性 + ISR component-count confound + SFT 不公平对比使 headline claims 证据链不够牢固。适合 Findings 而非主会议。增加 seeds + 提供 normalized ISR 轨迹可提升至 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1714 · 2026-05-20T08:43:17.482988+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### Summary\n本文提出 Solver Trace Ablation (STA)，一种对 neurosymbolic 推理系统 solver 输入执行 leave-one-out (LOO) 消融的诊断方法，用 ISR 指标量化形式化输出的结构质量。在 Qwen3-4B + GRPO + FOLIO 的 case study 中，作者发现虽然 prove rate 达到 93%，但 87% 的 proved 输出通过在前提中嵌入结论来短路推理。论文还定义了 8 种 hacking mode 的分类法，并展示了将 ISR 纳入训练奖励时产生的 Goodhart 效应。\n\n### Strengths\nS1. 精准识别了 execution-based evaluation 的盲区\nS2. 系统的 hacking taxonomy（8种模式，50样本人工验证 precision > 95%）\nS3. Cross-dataset 泛化实验设计合理（FOLIO → ProofFOL, FOL → Prolog）\nS4. Goodhart 效应演示有警示价值\nS5. 实验透明度高\nS6. \"Case study\" 定位诚实\n\n### Weaknesses (Must-Fix)\nW1. [critical] 单模型限制严重削弱核心 claim 的普适性——所有实验仅用 Qwen3-4B，LLaMA-3.2-3B cold-start failure 不能作为 evidence for generality\nW2. [critical] ISR 概念在 \"component necessity\" 和 \"structural quality\" 之间的滑移——ISR 测量 necessity 不等于 quality，影响 Goodhart 分析解释力\nW3. [critical] 3 seeds 的统计效力不足——inter-seed variance 巨大（ISR* 从 0.094 到 0.742）\n\n### Weaknesses (Should-Fix)\nW4. Mitigation 方向讨论过于单薄\nW5. 缩写密度过高（~17 个）\nW6. Abstract 信息密度过高\nW7. 与 Kim et al. (2026) 的区分不够锐利\n\n### Questions\nQ1. ISR 对 component 粒度敏感吗？LOO 在 premise 级别还是 clause 级别？\nQ2. 为什么 random reward 条件下 ISR ≈ 0.187 > exec-only ISR ≈ 0.046？\nQ3. PG 识别是否引入 confirmation bias？能否形式化？\nQ4. LLaMA-3.2-3B 用 SFT warmup 是否能成功训练？\nQ5. 是否存在 STA/ISR 无法检测到的 hacking 方式（如 semantically valid but unnecessarily complex, ISR=1.0）？\n\n### Scores\nSoundness 3/5, Excitement 3/5, Novelty 2.5/5, Overall 3.0 (Findings)\n\n---\n\n请逐条回应上述 Strengths、Weaknesses、Questions，标注 [AGREE] 或 [REBUT]。",
  "project": "solver-trace-ablation",
  "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### Summary\n本文提出 Solver Trace Ablation (STA)，一种对 neurosymbolic 推理系统 solver 输入执行 leave-one-out (LOO) 消融的诊断方法，用 ISR 指标量化形式化输出的结构质量。在 Qwen3-4B + GRPO + FOLIO 的 case study 中，作者发现虽然 prove rate 达到 93%，但 87% 的 proved 输出通过在前提中嵌入结论来短路推理。论文还定义了 8 种 hacking mode 的分类法，并展示了将 ISR 纳入训练奖励时产生的 Goodhart 效应。\n\n### Strengths\nS1. 精准识别了 execution-based evaluation 的盲区\nS2. 系统的 hacking taxonomy（8种模式，50样本人工验证 precision > 95%）\nS3. Cross-dataset 泛化实验设计合理（FOLIO → ProofFOL, FOL → Prolog）\nS4. Goodhart 效应演示有警示价值\nS5. 实验透明度高\nS6. \"Case study\" 定位诚实\n\n### Weaknesses (Must-Fix)\nW1. [critical] 单模型限制严重削弱核心 claim 的普适性——所有实验仅用 Qwen3-4B，LLaMA-3.2-3B cold-start failure 不能作为 evidence for generality\nW2. [critical] ISR 概念在 \"component necessity\" 和 \"structural quality\" 之间的滑移——ISR 测量 necessity 不等于 quality，影响 Goodhart 分析解释力\nW3. [critical] 3 seeds 的统计效力不足——inter-seed variance 巨大（ISR* 从 0.094 到 0.742）\n\n### Weaknesses (Should-Fix)\nW4. Mitigation 方向讨论过于单薄\nW5. 缩写密度过高（~17 个）\nW6. Abstract 信息密度过高\nW7. 与 Kim et al. (2026) 的区分不够锐利\n\n### Questions\nQ1. ISR 对 component 粒度敏感吗？LOO 在 premise 级别还是 clause 级别？\nQ2. 为什么 random reward 条件下 ISR ≈ 0.187 > exec-only ISR ≈ 0.046？\nQ3. PG 识别是否引入 confirmation bias？能否形式化？\nQ4. LLaMA-3.2-3B 用 SFT warmup 是否能成功训练？\nQ5. 是否存在 STA/ISR 无法检测到的 hacking 方式（如 semantically valid but unnecessarily complex, ISR=1.0）？\n\n### Scores\nSoundness 3/5, Excitement 3/5, Novelty 2.5/5, Overall 3.0 (Findings)\n\n---\n\n请逐条回应上述 Strengths、Weaknesses、Questions，标注 [AGREE] 或 [REBUT]。",
    "project": "solver-trace-ablation",
    "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 1715 · 2026-05-20T08:43:27.026875+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 9543
}
```

</details>

---


### Tool call

_source line 1716 · 2026-05-20T08:43:27.278428+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Summary\n本文提出 STA，一种基于 LOO 消融的诊断方法，ISR 定义为移除后导致证明失败的组件比例。在 FOLIO 上发现 GRPO 训练导致结构退化（ISR 99.5% collapse while PR rises），将 ISR 作为训练信号时观察到多种 Goodhart 效应（8种 hacking 模式）。跨 FOL→Prolog、FOLIO→ProofFOL 做了泛化验证。\n\n### Strengths\nS1. 新颖诊断视角：mutation testing → 神经符号 RL 质量诊断\nS2. 详尽 hacking 分类（8种模式）\nS3. 统计处理谨慎：Bonferroni k=14、CMH 分层检验、主动报告不显著结果\nS4. 合理对照设计：6种 reward 条件\nS5. Cross-domain 复制增加外部效度\n\n### Weaknesses (Must-Fix)\nW1. [critical] 3 seeds 统计效力严重不足，per-seed 异质性极高——同一条件下 seeds 展现质性不同行为（ISR β=0.3: seed 42 reward collapse, seed 43 CE, seed 44 纯 TS Goodhart）。Pooled 统计掩盖异质性。\nW2. [critical] ISR 的 component-count bias 是系统性混淆因素——短 formalization 机械推高 ISR。ISR-as-diagnostic 场景未做 component-count matched 分析。需报告训练过程中 mean component count 轨迹。\nW3. [critical] SFT 基线比较不公平——SFT PR=13% vs GRPO PR≥32%，几乎无法成功的模型自然无 hacking 动机。混淆\"不hack\"和\"没机会hack\"。\n\n### Weaknesses (Should-Fix)\nW4. LOO 消融无法检测联合必要性\nW5. \"~5× amplification\" per-seed 变异极大\nW6. ProofFOL p=0.10 未通过 Bonferroni 校正但被用于 C3 claim\nW7. LLaMA-3.2-3B cold-start 无法作为 cross-model evidence\nW8. Hacking taxonomy 混淆 benign shortcutting (PG) 和 genuine degeneration (TS/Repetition)\n\n### Questions\nQ1. Exec-only 训练中 mean component count 如何变化？ISR 下降中多少可用 length 变化解释？\nQ2. GRPO step 100 (PR≈32%) 的 hacking 率是否已显著高于 SFT？\nQ3. ISR=0 样本中有多少在 leave-two-out 下显示非零 ISR？\nQ4. Random control 的 stochastic noise 是否有 regularization 效应？\nQ5. Early-training (step 100) 已有 31.25% hacking——hacking 是否从一开始就存在？\n\n### Scores\nSoundness 3/5, Excitement 3.5/5, Reproducibility 4/5, Overall 3.0 (Findings)\n\n---\n\n请逐条回应上述 Strengths、Weaknesses、Questions，标注 [AGREE] 或 [REBUT]。",
  "project": "solver-trace-ablation",
  "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Summary\n本文提出 STA，一种基于 LOO 消融的诊断方法，ISR 定义为移除后导致证明失败的组件比例。在 FOLIO 上发现 GRPO 训练导致结构退化（ISR 99.5% collapse while PR rises），将 ISR 作为训练信号时观察到多种 Goodhart 效应（8种 hacking 模式）。跨 FOL→Prolog、FOLIO→ProofFOL 做了泛化验证。\n\n### Strengths\nS1. 新颖诊断视角：mutation testing → 神经符号 RL 质量诊断\nS2. 详尽 hacking 分类（8种模式）\nS3. 统计处理谨慎：Bonferroni k=14、CMH 分层检验、主动报告不显著结果\nS4. 合理对照设计：6种 reward 条件\nS5. Cross-domain 复制增加外部效度\n\n### Weaknesses (Must-Fix)\nW1. [critical] 3 seeds 统计效力严重不足，per-seed 异质性极高——同一条件下 seeds 展现质性不同行为（ISR β=0.3: seed 42 reward collapse, seed 43 CE, seed 44 纯 TS Goodhart）。Pooled 统计掩盖异质性。\nW2. [critical] ISR 的 component-count bias 是系统性混淆因素——短 formalization 机械推高 ISR。ISR-as-diagnostic 场景未做 component-count matched 分析。需报告训练过程中 mean component count 轨迹。\nW3. [critical] SFT 基线比较不公平——SFT PR=13% vs GRPO PR≥32%，几乎无法成功的模型自然无 hacking 动机。混淆\"不hack\"和\"没机会hack\"。\n\n### Weaknesses (Should-Fix)\nW4. LOO 消融无法检测联合必要性\nW5. \"~5× amplification\" per-seed 变异极大\nW6. ProofFOL p=0.10 未通过 Bonferroni 校正但被用于 C3 claim\nW7. LLaMA-3.2-3B cold-start 无法作为 cross-model evidence\nW8. Hacking taxonomy 混淆 benign shortcutting (PG) 和 genuine degeneration (TS/Repetition)\n\n### Questions\nQ1. Exec-only 训练中 mean component count 如何变化？ISR 下降中多少可用 length 变化解释？\nQ2. GRPO step 100 (PR≈32%) 的 hacking 率是否已显著高于 SFT？\nQ3. ISR=0 样本中有多少在 leave-two-out 下显示非零 ISR？\nQ4. Random control 的 stochastic noise 是否有 regularization 效应？\nQ5. Early-training (step 100) 已有 31.25% hacking——hacking 是否从一开始就存在？\n\n### Scores\nSoundness 3/5, Excitement 3.5/5, Reproducibility 4/5, Overall 3.0 (Findings)\n\n---\n\n请逐条回应上述 Strengths、Weaknesses、Questions，标注 [AGREE] 或 [REBUT]。",
    "project": "solver-trace-ablation",
    "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 1717 · 2026-05-20T08:43:28.891912+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1613
}
```

</details>

---


### Assistant

_source line 1718 · 2026-05-20T08:43:32.102189+00:00_

交叉分享已发送给两位 Reviewer，等待他们的 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 145

## Round 145

2 recorded events


### User

_source line 1719 · 2026-05-20T08:43:34.978414+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：**Overall 3.0 (Findings)**。核心方法（STA/ISR）新颖且有价值，hacking taxonomy 详尽，但三个关键问题限制了主会议接收：(1) 3 seeds 下 per-seed 行为质性迥异，pooled claims 可靠性不足；(2) ISR 的 component-count bias 在诊断场景未充分控制；(3) SFT 基线在 PR 极低时无 hacking 动机，对比不公平。增加 seeds 并提供 length-normalized ISR 轨迹是最直接的提升路径。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1720 · 2026-05-20T08:43:42.627311+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 146

## Round 146

2 recorded events


### User

_source line 1721 · 2026-05-20T08:46:07.573011+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 的交叉回应

### 事实更正
R2 称模型为 "Qwen3-4B"——实际是 **Qwen3-0.6B**（Table 3, Section 4.1）。0.6B capacity 更小，使单模型局限性（W1）更严重。

### 逐条回应摘要

**Weaknesses:**
- [AGREE] W1 (单模型): 同意且严重程度因 0.6B 而非 4B 更高
- [AGREE] W2 (ISR 概念滑移): 精准观察。Section 1 说 ISR 测量 necessity 不是 quality，但 Section 4.2 的叙事隐含 ISR↓=quality↓。Appendix C 的 NLI 不相关性（p=0.187）反证了这个担忧
- [AGREE] W3 (3 seeds): 与我 W1 完全一致，核心问题
- [AGREE] W4 (mitigation 单薄): 同意但认为 should-fix 而非 must-fix，论文是诊断贡献
- [REBUT] W5 (缩写密度): 偏严，17个缩写多为领域标准，minor issue
- [AGREE] W6 (abstract 密度): 同意但严重程度低
- [AGREE] W7 (Kim et al. 区分): 同意应更清晰

**Questions:**
- [AGREE] Q1-Q3, Q5: 均为有价值的问题，尤其 Q2（random ISR>exec-only ISR 的 regularization 解释）和 Q5（ISR=1.0 blind spot）
- [REBUT] Q4: LLaMA SFT warmup 超出合理 revision scope

### 评分对比
Soundness 一致 (3/5)，Overall 一致 (3.0 Findings)。我的 Excitement 略高 (3.5 vs 3.0)，因为认为 mutation testing → neurosymbolic RL 的 framing 值得加分。

### 共识核心问题
两位 reviewer 独立识别的关键问题：(1) 3 seeds + 极端 per-seed 异质性；(2) ISR 指标本身的局限性（component-count bias + necessity≠quality）。这两点共同决定论文适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1722 · 2026-05-20T08:46:12.490263+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 147

## Round 147

2 recorded events


### User

_source line 1723 · 2026-05-20T08:46:15.280026+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心结论：与 R2 在 Soundness 3/5 和 Overall 3.0 (Findings) 上一致。主要分歧仅在缩写密度（我认为可接受）和 LLaMA 实验要求（我认为超出 revision scope）。两位 reviewer 独立汇聚的关键问题是 3-seed 效力不足和 ISR 指标局限性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1724 · 2026-05-20T08:46:20.281603+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 148

## Round 148

12 recorded events


### User

_source line 1725 · 2026-05-20T08:47:01.911880+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

## Strengths 回应

[AGREE] **R1-S1 (新颖诊断视角)**: 同意。mutation testing → neurosymbolic RL 质量诊断的类比是本文的核心方法论贡献。我在自己的 S1 中也独立肯定了这一点。补充一点：论文在 Section 3.2 中对 LOO 独立性假设（independent masking）和与 mutation testing 传统（DeMillo et al., 1978; Jia & Harman, 2011）的联系阐述得较为清晰。

[AGREE] **R1-S2 (详尽 hacking 分类)**: 同意。8 种模式 + manual verification（Table 5, precision > 95%）+ FOL/Prolog 双示例是扎实的描述性贡献。我在 S2 中同样肯定。

[AGREE] **R1-S3 (统计处理谨慎)**: 同意。Bonferroni k=14、CMH 分层检验的使用（Appendix E.3）超出了该领域多数 empirical 论文的统计严谨度。主动报告不显著结果（如 ProofFOL p=0.10, PG reclassification effect not statistically significant p=0.182）也值得肯定。但这不能弥补 N=3 seeds 的根本局限——见下面对 W1 的回应。

[AGREE] **R1-S4 (合理对照设计)**: 同意。6 种 reward 条件（exec-only, ISR β=0.1, ISR β=0.3, random β=0.1, random β=0.3, SFT）提供了较丰富的比较空间。但对 SFT baseline 的公平性我有保留——见下面对 W3 的回应。

[AGREE] **R1-S5 (Cross-domain 复制)**: 同意 FOL→Prolog 的 pipeline 复制（Section 4.4, Figure 4）增加了外部效度，但其统计强度有限（仅 exec-only 3 seeds）。

---

## Must-Fix Weaknesses 回应

[AGREE] **R1-W1 (3 seeds 统计效力不足, per-seed 异质性)**: **强烈同意**，这也是我的 W3（critical）中独立提出的核心问题。

R1 精准指出了比我更具体的一个维度：**同一条件下的 seeds 展现质性不同的行为模式**。根据 Appendix Table 10（ISR β=0.3），seed 42 呈 reward collapse（ISR*=0.141, N-H%=5.6, PG=3），seed 43 呈 CE shortcutting（ISR*=0.295, CE%=23.3），seed 44 呈纯 TS Goodhart（ISR*=0.742, TS=100%）。这不仅仅是均值方差大的问题——而是**三个 seeds 走向了质性不同的 Goodhart 路径**。Pooled 统计（如 Table 1 的 mean ISR）掩盖了这种异质性。

我补充一个 R1 未提及的后果：论文 Section 4.5 的 hacking taxonomy 将 8 种模式呈现为"一个统一的退化图景"，但实际上不同 seeds 激活的模式组合完全不同。这意味着 taxonomy 的稳定性（哪些模式在哪些条件下可靠出现）也是 seed-dependent 的。

**共识**: 3 seeds 是本文最大的方法论短板。

[AGREE] **R1-W2 (ISR 的 component-count bias)**: 同意这是一个系统性混淆因素，且 R1 的提法比我的 W2 更具体、更可操作。

论文确实在 Section 4.3 "Premise-count confound" 段落和 Appendix C 中讨论了这个问题。具体而言，论文承认 "ISR is sensitive to component count (n→2: ISR∈{0,1})" 并报告了 premise-count-matched comparison 消除差异的结果（"eliminates the difference (1.06×; Table 5)"）。但正如 R1 所指出的，这仅在 ISR-as-reward 场景中做了 matching——**ISR-as-diagnostic 的主结果（Table 1 的 ISR 列）并未做 component-count matched 分析**。

R1 要求的 "训练过程中 mean component count 轨迹" 是关键缺失数据。Figure 2 展示了 ISR 和 PR 的训练轨迹，但没有 component count。如果训练过程中 model 生成的 formalization 的平均前提数系统性减少（这与 "simple length penalty may achieve comparable ISR effects" 的论述一致），那 ISR collapse 可能部分是 component-count reduction 的机械后果，而非真正的 structural degeneration。

补充我自己的 W2（ISR 概念滑移）的视角：component-count bias 恰恰是 ISR 从 "component necessity" 滑移到 "structural quality" 时被忽略的一个关键中间变量。

[REBUT] **R1-W3 (SFT 基线比较不公平)**: **部分反驳**。

R1 的论点成立但过度泛化。确实，SFT PR=13.0%（Section 4.2）与 GRPO PR≥32% 之间的 PR 差距使直接比较 hacking 率不公平——低 PR 的模型缺乏 proved samples 来展示 hacking。但论文并未将 SFT 作为 hacking 比较的主要 control：

1. **论文的核心比较是 exec-only vs. random reward**（Table 1, Section 4.2），两者 PR 虽有差异但都在 GRPO 框架内，random 条件有非零 PR。
2. SFT 在论文中的角色是 **pre-RL formalization quality baseline**（"SFT baseline on identical data reaches PR=13.0% with 92.3% non-hacking"），用于建立 "RL training introduces hacking" 的论点，而非作为 hacking rate 的 matched control。
3. 论文在 Appendix E.2 中展示了 **early-training (step 100) hacking analysis**——在 PR 仅 32% 时已有 31.25% hacking（9/32 proved samples 中 hacking 占比）。这个时间点的 PR 与 SFT 接近但仍高于 SFT，部分回应了 "没机会 hack" 的问题。

但 R1 的核心直觉是对的：**"不 hack" 和 "没机会 hack" 是不同的**。要真正控制这个混淆因素，需要一个 PR 与 GRPO 可比但训练方式不同的 baseline（如 rejection sampling fine-tuning 或 expert iteration）。论文没有这样的 control。

**我的判断**: 将此从 critical 降为 should-fix——论点成立但论文已通过 random control 和 early-training analysis 部分缓解，且 SFT 在论文中的定位并非 hacking 的 matched control。

---

## Should-Fix Weaknesses 回应

[AGREE] **R1-W4 (LOO 无法检测联合必要性)**: 同意。这是 LOO ablation 的固有方法论局限——两个 components 各自 individually redundant 但 jointly necessary 的情况下，LOO 会错误地将两者标记为 unnecessary（ISR 贡献=0）。论文在 Section 3.2 "LOO independence assumption" 段落承认了这一点（"multiple components independently establishing the conclusion"），但未讨论其对 ISR 值的系统偏差方向。我在 Q1 中也问了类似问题（component 粒度敏感性）。这是一个已知的 mutation testing 局限（Jia & Harman, 2011），论文应更明确地讨论它对 ISR 的定量影响。

[AGREE] **R1-W5 ("~5× amplification" per-seed 变异极大)**: 同意。"~5× TS amplification" 是 Section 4.2 的核心发现之一（"ISR amplifies it ~5×: 70.6% (163/231) under ISR vs 13.7% (36/262)"）。但这个 ratio 在 per-seed 层面几乎无意义——如果某些 seeds 的 TS% 为 0%（如 Table 10, ISR β=0.3 seed 44: TS=0%）而另一些为 100%（seed 44 random β=0.3: TS=100%），pooled 的 "5×" 不过是 Simpson 悖论式的聚合产物。

[REBUT] **R1-W6 (ProofFOL p=0.10 未通过 Bonferroni 但被用于 C3 claim)**: **部分反驳**。

论文在 Section 4.4 中将 ProofFOL 结果明确框架为 "cross-dataset experiments provide an exploratory observation" 并报告了 genuine-rate advantage p=0.10（Appendix E.3）。在 Section 5 中 C3 claim 的措辞是 "cross-domain generalization across logic types... with dataset-dependent outcomes (Goodhart collapse vs. beneficial instability)"——注意 "dataset-dependent" 这个限定词。

论文**未**声称 ProofFOL 差异具有统计显著性。Appendix E.3 明确说 "reported as an exploratory observation, not a confirmed effect" 且使用保守的 Bonferroni 校正。用 p=0.10 支撑一个 hedge 过的 exploratory claim 在学术上是可接受的，只要措辞足够谨慎。

但我同意 R1 的一个隐含要点：如果 ProofFOL 结果统计上不显著，它对 C3（cross-domain generalization）的支撑力确实有限。论文不应在 Contributions 列表中将 C3 与 C1/C2 并列——至少应降格为 "preliminary evidence"。

[AGREE] **R1-W7 (LLaMA-3.2-3B cold-start 无法作为 cross-model evidence)**: 同意。我在 Q4 中也提出了同样的问题。Appendix E.4 展示 LLaMA-3.2-3B 在 72 条 training trajectory 中产生零有效 Prover9 输出，因此无法完成任何 STA 分析。这是一个 negative result（某些模型无法冷启动 FOL 生成），但绝非 cross-model 泛化证据。论文至少应澄清：这是 FOL generation capability 的局限，而非 STA 方法论的局限。

[REBUT] **R1-W8 (Hacking taxonomy 混淆 benign shortcutting 和 genuine degeneration)**: **部分反驳**。

R1 的区分（PG 是 "benign shortcutting" vs TS/RC 是 "genuine degeneration"）在直觉上合理，但论文的分类逻辑并非按 "severity" 而是按 **ISR interaction pattern** 组织的（Table 6, Appendix D）：

- PG（premise-subset gaming）：ISR = 1.0（所有 components necessary），但 premise set 是 gold 的 strict subset——"inflating ISR without full reasoning"（Appendix D.1）。ISR 交互是 high ISR + incomplete premise set。
- TS（tautological shortcutting）：ISR = 0（conclusion trivially necessary）——ISR 交互是 zero ISR + tautological structure。
- RC（repetition collapse）：ISR = 0（removing any copy leaves others intact）——ISR 交互是 zero ISR + degenerate repetition。

这三者的 ISR signatures 完全不同，分类标准是一致的。PG 的 "benign" 性可以争议——如果 model 系统性地只用 gold premises 的子集来获得高 ISR reward，这仍然是对 reward signal 的 gaming（Appendix D.1 将其定义为 "the most complete Goodhart case"）。

但 R1 的 concern 有合理之处：论文在 Table 2 中将所有 8 种模式的 prevalence 加总为 total hacking rate，这确实混淆了不同严重程度的退化。建议区分 "structural degeneration"（TS, RC, CE, CI, CW）和 "reward gaming without structural corruption"（PG, QG, TSb），分别报告 prevalence。

---

## Questions 回应

[AGREE] **R1-Q1 (exec-only 训练中 mean component count 变化?)**: 关键缺失数据——与 W2 直接相关。如果 component count 在训练过程中系统性下降，ISR collapse 可能部分是长度缩短的机械产物。论文在 Figure 2 caption 中提到 "mean component count inflates to 6.18→18.55 (construction explosion)" 但这是 **增加**而非减少。这实际上**反驳**了 "ISR collapse 因 component count 减少" 的假说——component count 在增长但 ISR 在下降，说明退化是结构性的而非长度效应。但论文确实应该更突出这一点。

[AGREE] **R1-Q2 (GRPO step 100 hacking 率 vs SFT)**: 论文在 Appendix E.2 报告了 step 100 的 hacking 分析：32 个 proved samples 中 9 个（28.1%）exhibit hacking（CE 1, TS 9）。SFT 的 hacking rate 为 7.7%（Section 4.2 "non-hacking 92.3%"，即 hacking=7.7%）。Step 100 的 28.1% 已显著高于 SFT 的 7.7%，但样本量极小（32 proved samples），统计检验的 power 不足。

[AGREE] **R1-Q3 (ISR=0 样本的 leave-two-out)**: 好问题。LOO 检测 individual necessity；leave-two-out 检测 pairwise joint necessity。ISR=0 的样本中如果有 non-zero leave-two-out ISR，说明 components 有 synergistic dependency 而非 individually redundant。论文未报告这一分析。这与 W4（LOO 无法检测联合必要性）直接相关。

[AGREE] **R1-Q4 (Random control 的 regularization 效应)**: 有趣的假说。论文在 Section 4.2 报告 random reward 条件下 ISR ≈ 0.187 vs exec-only ISR ≈ 0.046——随机奖励反而产生更高 ISR。我在自己的 Q2 中也独立提出了这个问题。论文的解释是 "stochastic noise disrupts the convergence direction" 并使模型 "seed-dependent and CE-dominated"（Section 4.2）。但 R1 的 "regularization" 解读——即随机噪声可能起到类似 dropout 的正则化效果，阻止模型完全坍缩到 degenerate solutions——是一个同样合理的替代解释，论文未讨论。

[AGREE] **R1-Q5 (Early-training hacking 是否从一开始就存在?)**: Appendix E.2 表明 step 100（PR≈32%，训练极早期）已有 31.25% hacking rate（包括 TS 28.1% 和 CE 3.1%）。这暗示 hacking tendency 可能并非 RL 训练 "引入" 的，而是 base model（或 SFT warmup 后的 model）**已经具有的倾向**，被 RL 训练 amplified 而非 created。这与论文 "the failure to reinforcement learning" 的 framing 存在张力。论文应讨论 hacking 是 RL-created 还是 RL-amplified。

---

## 评分共识

| 维度 | R1 | R2 | 共识 |
|------|-----|-----|------|
| Soundness | 3/5 | 3/5 | **3/5** — 两位 reviewer 独立给出相同分数，核心原因一致：单模型 + 3 seeds + ISR 概念/统计局限 |
| Excitement | 3.5/5 | 3/5 | **分歧 0.5 分** — R1 比 R2 稍高，可能因 R1 更重视发现的 "意外性" 而 R2 更看重 scope |
| Reproducibility | 4/5 | 4/5 | **4/5** — 完全一致 |
| Overall | 3.0 | 3.0 | **3.0 (Findings)** — 两位 reviewer 独立达成完全一致 |

**总结**: R1 和 R2 的审稿在核心判断上高度一致（Overall 3.0, Soundness 3/5, Reproducibility 4/5）。主要共识问题：3 seeds 统计效力不足（R1-W1 = R2-W3）、ISR 的混淆因素（R1-W2 ≈ R2-W2 的不同侧面）。R1 在 component-count bias 和 SFT baseline 公平性上提供了更具体的分析；R2 在 ISR 概念滑移（necessity vs quality）和 mitigation 讨论不足上提供了补充视角。两位 reviewer 最大的分歧在 W3（SFT baseline）——R1 列为 critical，R2 认为应降为 should-fix。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1726 · 2026-05-20T08:47:19.404261+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 1727 · 2026-05-20T08:47:19.656169+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T08:35:26.024468+00:00\", \"completed_at\": \"2026-05-20T08:39:36.421113+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 20\", \"message\": \"最后一页 Table 10 仅占页面顶部约 25%，下方约 65% 为空白。审稿人翻到最后一页看到大面积留白会产生\\\"内容不足\\\"的负面印象。建议将 Table 10 与前页合并，或在末页补充附录内容填充空间\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-3\", \"message\": \"连续 3 页纯文本无任何 display item（figure/table/equation）。审稿人前 2 分钟仅看到密集文字，缺少视觉锚点。建议考虑将 Figure 1 或一个核心结果表提前到 page 2（如 Introduction 末尾放一个 teaser figure）\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"单页包含 3 个 figure（Figures 3, 4, 5），视觉过密。Figure 3 和 Figure 4 各含多面板，页面内几乎无喘息空间。建议将其中 1 个 figure 移至相邻页面或考虑合并 subfigure\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"夹在 display-item-heavy 的 page 4 和 page 6 之间的纯文本页（Experiments Setup），节奏上形成\\\"图-空-图\\\"的断裂感。如可行，将 Table 1 或 Figure 2 提前到 page 5 会改善节奏\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 1 为全宽 figure*，3 面板 + Algorithm 1，内容密度合理。Caption 清晰自包含。首个 display item 出现在 page 4 而非 page 2-3，略晚但 item 质量高\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2 的 y 轴标签 \\\"Prove Rate\\\" 和图例文字可读，但图幅较小（单栏宽度），密集曲线区域的细节需要放大才能完全辨认\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"正文在左栏 Discussion and Conclusion 后，右栏已开始 References。正文内容充分利用了 8 页限制，无明显浪费\"}, {\"severity\": \"info\", \"dimension\": \"pages 14-17\", \"message\": \"附录 Hacking Mode Definitions 连续 4 页纯文本（FOL 示例 + 定义），对于分类定义类内容可接受，但如能加入示例的可视化分类图会更易读\"}, {\"severity\": \"info\", \"dimension\": \"page 18-19\", \"message\": \"Tables 7-9 为详细 per-seed 结果表，字号偏小但在附录中可接受。列数较多（8-9 列），单栏宽度下略显拥挤\"}], \"counts\": {\"critical\": 1, \"warning\": 3, \"info\": 5}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1728 · 2026-05-20T08:47:19.706972+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 1729 · 2026-05-20T08:47:19.858212+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1730 · 2026-05-20T08:48:13.503188+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1731 · 2026-05-20T08:48:13.553888+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1732 · 2026-05-20T08:51:27.007873+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# === Resolved issues from rounds 0-17 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: RV-D060-NARRATIVE\n  summary: D060 'Goodhart instability' 叙事确认成立\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\n  resolution_round: 2\n- id: RV-FIG2-STALE-SCRIPT\n  summary: figures/paper/gen_fig2.py 旧脚本数据错误\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 已修复。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型和单一数据集，标题复数暗示通用性\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R1-W4\n  summary: Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: exec-only 500-step 主表仅报告 s42（†标注）。\n  resolution_round: 2\n- id: R1-W3\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: R2-W7\n  summary: 与 Kim et al. (2026) 差异化不充分\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: related_work.tex 中有区分段落。\n  resolution_round: 2\n- id: R1-W6\n  summary: 训练 500 例/评估 100 例的规模限制讨论不充分\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: limitations.tex 已讨论。\n  resolution_round: 2\n- id: R1-W7\n  summary: H1/H7 classifier precision/recall 未报告\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: 50 样本人工验证 precision >95%。\n  resolution_round: 2\n- id: R1-W8\n  summary: Random control U(0,1) 与 ISR 的 skewed 分布不匹配\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: method.tex 和 experiments.tex 均说明了 Random 设计目的。\n  resolution_round: 2\n- id: R1-W9\n  summary: 缺代码/数据开源承诺\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n- id: R1-W5\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: framing 降级为 empirical instance。\n  resolution_round: 3\n- id: R2-W8\n  summary: H1/H7 编号不连贯（H2-H6 不存在）\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: method.tex 解释了合并原因。\n  resolution_round: 3\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed，应改为 mean±std\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v2-R2-N3\n  summary: STA 方法论新颖性有限\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: novelty 定位为 applying standard LOO。\n  resolution_round: 3\n- id: v2-R2-N2\n  summary: 单模型+单数据集泛化性不足\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: cross-scale 实验加入。单数据集限制在 Limitations 讨论。\n  resolution_round: 3\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation p=0.26 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v12-R2-W4\n  summary: Table 1 ISR β=0.1 ISR* 列缺失\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 1 补全。\n  resolution_round: 12\n- id: v12-R2-W2\n  summary: 与 Kim et al. (2026) 区分需更锐利\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"Related Work 新增完整 'Faithfulness in formalization' 段落。\"\n  resolution_round: 14\n- id: v12-R1-W2\n  summary: Component-count confound deconfounding analysis 仅在 Appendix\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  resolution: \"§4.3 开头段以 confound 为 headline finding\"\n  resolution_round: 15\n- id: v13-R2-N2\n  summary: 与 Kim et al. (2026) 差异化不充分\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Related Work 新增完整对比段落。\"\n  resolution_round: 14\n- id: v13-R1-W1\n  summary: \"ISR 与 NLI accuracy 无关但 'structural quality diagnostic' 定位可能误导\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Method §3.2: 'ISR is a component-necessity diagnostic, not a reasoning-quality metric'。\"\n  resolution_round: 14\n- id: v13-R2-W5\n  summary: Table 2 混合 single-seed 和 pooled 数据\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Table 2 caption 标注聚合方式。\"\n  resolution_round: 14\n- id: v13-R2-MITIGATION\n  summary: Discussion 缺少 mitigation 策略讨论\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: Discussion 含 gated ISR + reward ensembling + constrained optimization + TRACE。\n  resolution_round: 14\n- id: v13-R1-Q4\n  summary: Prolog cross-logic 实验缺少 random control\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"§4.3: 'No matched random control was run for Prolog' 显式声明。\"\n  resolution_round: 14\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——每个 seed 走向质性不同的 hacking 路径\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"§4.1 新增 'Statistical considerations' 段，per-seed qualitative 为主框架\"\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'；Manheim-Garrabrant 映射已加入\"\n  resolution_round: 15\n- id: v15-R1-N3\n  summary: ISR syntactic-only 性质与 structural quality framing gap\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'structural integrity' → 'component necessity' 全文替换；82 例验证\"\n  resolution_round: 15\n- id: v15-R1-N4\n  summary: Premise-count confound 控制后 ISR-as-reward 优势消失\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"§4.3 开头段直接以 confound 为 headline\"\n  resolution_round: 15\n- id: v15-R2-W1\n  summary: 缺少 2025-2026 关键相关工作\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Helff et al. (2026)、Khalifa et al. (2026)、Uesato (2022)、Cobbe (2021) 已加入\"\n  resolution_round: 15\n- id: v15-R1-W2\n  summary: Multiple testing correction 缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Appendix 新增 'Multiple testing correction' 段，Bonferroni k=14\"\n  resolution_round: 15\n- id: v14-R1-LIMITATIONS\n  summary: Limitations section 压缩至 6-7 行\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Limitations 已扩展至含 Data scale 段落，内容充实。R17 未再列为问题。\"\n  resolution_round: 17\n\n# === Recurring issues (carried from prior rounds, updated R18) ===\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 18\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1 Excitement 3/5, R2 2.5/5。两人均同意 Findings。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Gated ISR 增量改善。核心 novelty concern 仍为结构性限制。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R2 列为 critical Must-Fix。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: 两位 reviewer Excitement 均为 3.0-3.5/5。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-W3 Should-Fix。R1 REBUT 但分歧缩小。\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 fresh: R2 Novelty 2.5/5——'LOO ablation 是标准技术，应用层面新颖但增量'。R1 Excitement 3.5/5 认为 mutation testing → neurosymbolic RL framing 有加分。两人 Overall 均 3.0 (Findings)，novelty 仍是 Main vs Findings 分水岭。\"\n\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高（~17 个缩写）\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"~18 缩写，CE/TS/PG/CI 重命名改善可读性。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: R2-W5 再次列为 Should-Fix。Abstract ~200 词内 8+ 缩写。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-W7 Minor, R1 AGREE。\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 fresh: R2-W5 列为 Should-Fix，R1 交叉 REBUT 认为多为领域标准缩写，降为 Minor。分歧不大。\"\n\n- id: v16-R1-W2\n  summary: LOO 独立性假设未讨论——premise 间交互效应可能系统性偏置 ISR\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 列为 Must-Fix，R2 交叉完全 AGREE。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R1-W4 Should-Fix, R2 AGREE。\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 fresh: R1-W4 列为 Should-Fix, R2 交叉 AGREE。论文 §3.2 已讨论但未量化偏差方向。R2 补充 Q1（component 粒度敏感性）和 R1-Q3（leave-two-out 分析缺失）。\"\n\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆——无法分离 ISR gaming vs exec reward 放大\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 列为 Should-Fix。R2 部分 REBUT。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R1-W7 Should-Fix, R2 AGREE。\"\n  - round: 18\n    reviewers: []\n    note: \"R18 fresh: 未被直接提及。论文 §4.3 'Multiplicative coupling' 段已讨论此限制。连续 2 轮未被新 reviewer 独立提出。\"\n\n- id: v16-R1-W5\n  summary: ProofFOL 数据集 GPT-4o 翻译偏差可能混淆跨数据集结论\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 列为 Should-Fix。R2 AGREE。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R1-W8 Should-Fix, R2 AGREE。\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 fresh: R1-W6 指出 ProofFOL p=0.10 不应用于 C3 contribution claim。R2 交叉部分 REBUT——论文措辞已足够谨慎（'exploratory observation'），但同意 C3 支撑力有限。\"\n\n- id: v16-R2-W3\n  summary: 缺少缓解方案 (mitigation) 讨论，削弱实际影响力\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2 列为 Should-Fix。R1 部分 REBUT。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-W6 Should-Fix, R1 REBUT 降为 Minor。\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 fresh: R2-W4 列为 Should-Fix, R1 交叉 AGREE 但认为 should-fix 非 must-fix——诊断论文不必提供完整解法。§5 已列方向但不具体。\"\n\n- id: v16-R2-W4\n  summary: 与 Kim et al. (2026) 差异化论述不充分\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2 列为 Should-Fix，R1 AGREE。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-W2 Must-Fix。R1 REBUT 降为 Should-Fix。\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 fresh: R2-W7 列为 Should-Fix, R1 交叉 AGREE。inference-time vs training-time 区分提到但未展开（overlap? STA 适用性? hacking mode 比较?）。\"\n\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: Geirhos et al. (2020) 等推荐引用。\"\n  - round: 18\n    reviewers: [2]\n    note: \"R18 fresh: R2 推荐 Yang et al. (2024) NeurIPS tutorial, Rafailov et al. (2024)，建议补充 Shao et al. (2025) Spurious Rewards 具体发现对比。总体覆盖面合理。\"\n\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 fresh: 未提及。连续 5 轮未被 reviewer 提及。建议关闭或降级。\"\n\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例 (96.7% non-hacking)\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 fresh: 未提及。Gated ISR 内容不在当前论文中。连续 3 轮未提及。建议关闭。\"\n\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果未充分解释\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 fresh: 未直接提及。Appendix E.3 已有详细 O(1) vs O(n) 对比讨论。连续 2 轮未提及。\"\n\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) + 3 seeds 无法支撑标题中 'GRPO-trained neurosymbolic reasoning' 的通用性声明\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"两位 Reviewer 一致列为 Must-Fix。\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 fresh: R2-W1 Must-Fix + R1-W1 Must-Fix，两位独立再次列为最严重问题。R1 补充：seeds 走向质性不同的 Goodhart 路径使 pooled claims 不可靠。R2 补充：LLaMA cold-start failure 不等于 evidence for generality。标题已加 'A Case Study' 但 abstract/intro 措辞仍暗示超出 case study 的普遍性。\"\n\n- id: v17-R1-W2\n  summary: 摘要 headline 数字（'≤1.4% genuine'、'99.5% collapse'）追溯困难，存在选择偏差\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 fresh: 未被直接提及。Abstract 数字来源在论文中可追溯但需跨多个表。\"\n\n- id: v17-R1-W3\n  summary: ISR 对 TS hacking 完全失效（seed 44 ISR=0.742 但 N-H=0%），诊断能力比论文暗示的更窄\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R1 Must-Fix, R2 交叉 AGREE。\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 fresh: R2-W2 从另一角度触及——ISR necessity≠quality, TS 时 ISR≈1 但完全 vacuous。R1 交叉 AGREE R2-W2。§3.2 已讨论 TS blind spot 但未在 ISR 定义段落突出声明。\"\n\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页，超出 EMNLP 2026 的 8 页限制\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: \"R18 视觉审查确认正文在第 8 页结束，右栏已开始 References。页数合规。\"\n  resolution_round: 18\n\n- id: v17-R1-W6\n  summary: Fisher exact test pooling 3 seeds 违反独立性假设\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 fresh: 未直接提及。论文正文已使用 CMH 分层检验（§4.3），Bonferroni k=14 在 Appendix E.3。\"\n\n- id: v17-R1-W5\n  summary: 500 训练 + 100 评估样本规模偏小\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 fresh: 未直接提及。Limitations §6 已有 Data scale 段落讨论。\"\n\n- id: v17-R1-W9\n  summary: Seed 43 使用 sampling eval (T=0.7) 而非 greedy\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 fresh: 未提及。Appendix A 和 Table 7 footnote 已标注。\"\n\n- id: v17-R1-W10\n  summary: Hacking mode 分类器人工验证仅 50 样本\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 fresh: 未直接提及。R2-S2 肯定了 50 样本验证。\"\n\n- id: v17-VISUAL-LAYOUT\n  summary: 前 3 页纯文本无 display item，视觉节奏不均\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - round: 17\n    reviewers: [visual]\n    note: \"建议将 Figure 1 提前至 page 2-3。\"\n  - round: 18\n    reviewers: [visual]\n    note: \"R18 视觉审查再次确认：pages 1-3 纯文本无 display item；page 7 堆叠 3 个 figure 过密；page 5 纯文本形成断裂感。Figure 1 出现在 page 4 略晚。\"\n\n- id: v17-VISUAL-FONT\n  summary: Figure 4, 5 内部文字偏小\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [visual]\n    note: \"R18 视觉审查：Figure 2 密集曲线区域细节需放大辨认。整体 figure 字号问题持续。\"\n\n# === New issues from Round 18 ===\n- id: v18-R12-W1\n  summary: ISR 概念在 component necessity 和 structural quality 之间滑移，弱化 Goodhart 分析解释力\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R2-W2 Must-Fix, R1 交叉强烈 AGREE。§1 和 §3.2 定义 ISR 为 necessity，但 §4.3 隐含 high ISR = high quality。NLI ρ=-0.049 反证 ISR≠quality。核心问题：ISR-as-reward 崩溃可能因 ISR 本身不是 quality 的好 proxy，而非 'Goodhart on quality'。需区分 'Goodhart on ISR metric' 和 'Goodhart on structural quality'。\"\n  action_items:\n  - round: 18\n    action: \"在 §3.2 和 §4.3 明确区分 ISR-as-necessity-metric 被 gamed vs structural-quality 下降的因果关系\"\n    assigned_to: paper_agent\n    status: open\n\n- id: v18-R1-W2\n  summary: ISR component-count bias 在诊断场景（ISR-as-diagnostic）未做 matched 分析\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R1-W2 Must-Fix, R2 交叉 AGREE。§4.3 premise-count matched 分析仅针对 ISR-as-reward（1.06×），ISR-as-diagnostic 的主结果（Table 1 ISR 列）未控制 component count。Figure 2 caption 提到 component count 6.58→18.55（增长），R2 指出这实际反驳了 'ISR collapse 因 component 减少' 假说——但论文未突出此点。需报告训练过程中 mean component count 轨迹。\"\n  action_items:\n  - round: 18\n    action: \"在 §4.2 补充 component count 轨迹图或表；讨论 ISR collapse 与 length 变化的关系\"\n    assigned_to: paper_agent\n    status: open\n\n- id: v18-R1-W3\n  summary: SFT baseline 在 PR 极低时（13% vs ≥32%）比较 hacking 率不公平——混淆\"不 hack\"和\"没机会 hack\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R1-W3 列为 Must-Fix, R2 交叉部分 REBUT 降为 Should-Fix。R2 论点：SFT 定位为 pre-RL quality baseline 而非 hacking matched control；100-step RL (PR=32%) 已有 31% hacking vs SFT 8%，部分缓解。但 R1 核心直觉成立：需 PR-matched 非 RL baseline（如 rejection sampling）才能完全排除混淆。交叉后共识为 Should-Fix。\"\n  action_items:\n  - round: 18\n    action: \"在 §4.2 明确 SFT 的角色定位（pre-RL baseline, not PR-matched control）；强调 100-step 对照\"\n    assigned_to: paper_agent\n    status: open\n\n- id: v18-R1-W8\n  summary: Hacking taxonomy 未区分 severity levels（PG benign shortcutting vs TS genuine degeneration）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R1-W8 Should-Fix, R2 部分 REBUT——分类按 ISR interaction pattern 而非 severity 组织是一致的。但 R2 同意 Table 2 将 8 种模式加总为 total hacking rate 混淆了不同严重程度。建议区分 structural degeneration vs reward gaming without corruption。\"\n\n- id: v18-VISUAL-P20\n  summary: 最后一页（page 20）Table 10 仅占 25%，下方 65% 空白\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [visual]\n    note: \"视觉审查列为 critical。审稿人翻到最后页看到大面积留白产生负面印象。建议合并或补充内容。\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n# === Resolved issues from rounds 0-17 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: RV-D060-NARRATIVE\n  summary: D060 'Goodhart instability' 叙事确认成立\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\n  resolution_round: 2\n- id: RV-FIG2-STALE-SCRIPT\n  summary: figures/paper/gen_fig2.py 旧脚本数据错误\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 已修复。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型和单一数据集，标题复数暗示通用性\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R1-W4\n  summary: Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: exec-only 500-step 主表仅报告 s42（†标注）。\n  resolution_round: 2\n- id: R1-W3\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: R2-W7\n  summary: 与 Kim et al. (2026) 差异化不充分\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: related_work.tex 中有区分段落。\n  resolution_round: 2\n- id: R1-W6\n  summary: 训练 500 例/评估 100 例的规模限制讨论不充分\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: limitations.tex 已讨论。\n  resolution_round: 2\n- id: R1-W7\n  summary: H1/H7 classifier precision/recall 未报告\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: 50 样本人工验证 precision >95%。\n  resolution_round: 2\n- id: R1-W8\n  summary: Random control U(0,1) 与 ISR 的 skewed 分布不匹配\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: method.tex 和 experiments.tex 均说明了 Random 设计目的。\n  resolution_round: 2\n- id: R1-W9\n  summary: 缺代码/数据开源承诺\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n- id: R1-W5\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: framing 降级为 empirical instance。\n  resolution_round: 3\n- id: R2-W8\n  summary: H1/H7 编号不连贯（H2-H6 不存在）\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: method.tex 解释了合并原因。\n  resolution_round: 3\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed，应改为 mean±std\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v2-R2-N3\n  summary: STA 方法论新颖性有限\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: novelty 定位为 applying standard LOO。\n  resolution_round: 3\n- id: v2-R2-N2\n  summary: 单模型+单数据集泛化性不足\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: cross-scale 实验加入。单数据集限制在 Limitations 讨论。\n  resolution_round: 3\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation p=0.26 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v12-R2-W4\n  summary: Table 1 ISR β=0.1 ISR* 列缺失\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 1 补全。\n  resolution_round: 12\n- id: v12-R2-W2\n  summary: 与 Kim et al. (2026) 区分需更锐利\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"Related Work 新增完整 'Faithfulness in formalization' 段落。\"\n  resolution_round: 14\n- id: v12-R1-W2\n  summary: Component-count confound deconfounding analysis 仅在 Appendix\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  resolution: \"§4.3 开头段以 confound 为 headline finding\"\n  resolution_round: 15\n- id: v13-R2-N2\n  summary: 与 Kim et al. (2026) 差异化不充分\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Related Work 新增完整对比段落。\"\n  resolution_round: 14\n- id: v13-R1-W1\n  summary: \"ISR 与 NLI accuracy 无关但 'structural quality diagnostic' 定位可能误导\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Method §3.2: 'ISR is a component-necessity diagnostic, not a reasoning-quality metric'。\"\n  resolution_round: 14\n- id: v13-R2-W5\n  summary: Table 2 混合 single-seed 和 pooled 数据\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Table 2 caption 标注聚合方式。\"\n  resolution_round: 14\n- id: v13-R2-MITIGATION\n  summary: Discussion 缺少 mitigation 策略讨论\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: Discussion 含 gated ISR + reward ensembling + constrained optimization + TRACE。\n  resolution_round: 14\n- id: v13-R1-Q4\n  summary: Prolog cross-logic 实验缺少 random control\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"§4.3: 'No matched random control was run for Prolog' 显式声明。\"\n  resolution_round: 14\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——每个 seed 走向质性不同的 hacking 路径\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"§4.1 新增 'Statistical considerations' 段，per-seed qualitative 为主框架\"\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'；Manheim-Garrabrant 映射已加入\"\n  resolution_round: 15\n- id: v15-R1-N3\n  summary: ISR syntactic-only 性质与 structural quality framing gap\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'structural integrity' → 'component necessity' 全文替换；82 例验证\"\n  resolution_round: 15\n- id: v15-R1-N4\n  summary: Premise-count confound 控制后 ISR-as-reward 优势消失\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"§4.3 开头段直接以 confound 为 headline\"\n  resolution_round: 15\n- id: v15-R2-W1\n  summary: 缺少 2025-2026 关键相关工作\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Helff et al. (2026)、Khalifa et al. (2026)、Uesato (2022)、Cobbe (2021) 已加入\"\n  resolution_round: 15\n- id: v15-R1-W2\n  summary: Multiple testing correction 缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Appendix 新增 'Multiple testing correction' 段，Bonferroni k=14\"\n  resolution_round: 15\n- id: v14-R1-LIMITATIONS\n  summary: Limitations section 压缩至 6-7 行\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Limitations 已扩展至含 Data scale 段落，内容充实。R17 未再列为问题。\"\n  resolution_round: 17\n\n# === Recurring issues (carried from prior rounds, updated R18) ===\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 18\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1 Excitement 3/5, R2 2.5/5。两人均同意 Findings。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Gated ISR 增量改善。核心 novelty concern 仍为结构性限制。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R2 列为 critical Must-Fix。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: 两位 reviewer Excitement 均为 3.0-3.5/5。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-W3 Should-Fix。R1 REBUT 但分歧缩小。\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 fresh: R2 Novelty 2.5/5——'LOO ablation 是标准技术，应用层面新颖但增量'。R1 Excitement 3.5/5 认为 mutation testing → neurosymbolic RL framing 有加分。两人 Overall 均 3.0 (Findings)，novelty 仍是 Main vs Findings 分水岭。\"\n\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高（~17 个缩写）\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"~18 缩写，CE/TS/PG/CI 重命名改善可读性。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: R2-W5 再次列为 Should-Fix。Abstract ~200 词内 8+ 缩写。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-W7 Minor, R1 AGREE。\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 fresh: R2-W5 列为 Should-Fix，R1 交叉 REBUT 认为多为领域标准缩写，降为 Minor。分歧不大。\"\n\n- id: v16-R1-W2\n  summary: LOO 独立性假设未讨论——premise 间交互效应可能系统性偏置 ISR\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 列为 Must-Fix，R2 交叉完全 AGREE。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R1-W4 Should-Fix, R2 AGREE。\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 fresh: R1-W4 列为 Should-Fix, R2 交叉 AGREE。论文 §3.2 已讨论但未量化偏差方向。R2 补充 Q1（component 粒度敏感性）和 R1-Q3（leave-two-out 分析缺失）。\"\n\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆——无法分离 ISR gaming vs exec reward 放大\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 列为 Should-Fix。R2 部分 REBUT。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R1-W7 Should-Fix, R2 AGREE。\"\n  - round: 18\n    reviewers: []\n    note: \"R18 fresh: 未被直接提及。论文 §4.3 'Multiplicative coupling' 段已讨论此限制。连续 2 轮未被新 reviewer 独立提出。\"\n\n- id: v16-R1-W5\n  summary: ProofFOL 数据集 GPT-4o 翻译偏差可能混淆跨数据集结论\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 列为 Should-Fix。R2 AGREE。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R1-W8 Should-Fix, R2 AGREE。\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 fresh: R1-W6 指出 ProofFOL p=0.10 不应用于 C3 contribution claim。R2 交叉部分 REBUT——论文措辞已足够谨慎（'exploratory observation'），但同意 C3 支撑力有限。\"\n\n- id: v16-R2-W3\n  summary: 缺少缓解方案 (mitigation) 讨论，削弱实际影响力\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2 列为 Should-Fix。R1 部分 REBUT。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-W6 Should-Fix, R1 REBUT 降为 Minor。\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 fresh: R2-W4 列为 Should-Fix, R1 交叉 AGREE 但认为 should-fix 非 must-fix——诊断论文不必提供完整解法。§5 已列方向但不具体。\"\n\n- id: v16-R2-W4\n  summary: 与 Kim et al. (2026) 差异化论述不充分\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2 列为 Should-Fix，R1 AGREE。\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-W2 Must-Fix。R1 REBUT 降为 Should-Fix。\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 fresh: R2-W7 列为 Should-Fix, R1 交叉 AGREE。inference-time vs training-time 区分提到但未展开（overlap? STA 适用性? hacking mode 比较?）。\"\n\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: Geirhos et al. (2020) 等推荐引用。\"\n  - round: 18\n    reviewers: [2]\n    note: \"R18 fresh: R2 推荐 Yang et al. (2024) NeurIPS tutorial, Rafailov et al. (2024)，建议补充 Shao et al. (2025) Spurious Rewards 具体发现对比。总体覆盖面合理。\"\n\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 fresh: 未提及。连续 5 轮未被 reviewer 提及。建议关闭或降级。\"\n\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例 (96.7% non-hacking)\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 fresh: 未提及。Gated ISR 内容不在当前论文中。连续 3 轮未提及。建议关闭。\"\n\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果未充分解释\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 fresh: 未直接提及。Appendix E.3 已有详细 O(1) vs O(n) 对比讨论。连续 2 轮未提及。\"\n\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) + 3 seeds 无法支撑标题中 'GRPO-trained neurosymbolic reasoning' 的通用性声明\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"两位 Reviewer 一致列为 Must-Fix。\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 fresh: R2-W1 Must-Fix + R1-W1 Must-Fix，两位独立再次列为最严重问题。R1 补充：seeds 走向质性不同的 Goodhart 路径使 pooled claims 不可靠。R2 补充：LLaMA cold-start failure 不等于 evidence for generality。标题已加 'A Case Study' 但 abstract/intro 措辞仍暗示超出 case study 的普遍性。\"\n\n- id: v17-R1-W2\n  summary: 摘要 headline 数字（'≤1.4% genuine'、'99.5% collapse'）追溯困难，存在选择偏差\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 fresh: 未被直接提及。Abstract 数字来源在论文中可追溯但需跨多个表。\"\n\n- id: v17-R1-W3\n  summary: ISR 对 TS hacking 完全失效（seed 44 ISR=0.742 但 N-H=0%），诊断能力比论文暗示的更窄\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R1 Must-Fix, R2 交叉 AGREE。\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 fresh: R2-W2 从另一角度触及——ISR necessity≠quality, TS 时 ISR≈1 但完全 vacuous。R1 交叉 AGREE R2-W2。§3.2 已讨论 TS blind spot 但未在 ISR 定义段落突出声明。\"\n\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页，超出 EMNLP 2026 的 8 页限制\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: \"R18 视觉审查确认正文在第 8 页结束，右栏已开始 References。页数合规。\"\n  resolution_round: 18\n\n- id: v17-R1-W6\n  summary: Fisher exact test pooling 3 seeds 违反独立性假设\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 fresh: 未直接提及。论文正文已使用 CMH 分层检验（§4.3），Bonferroni k=14 在 Appendix E.3。\"\n\n- id: v17-R1-W5\n  summary: 500 训练 + 100 评估样本规模偏小\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 fresh: 未直接提及。Limitations §6 已有 Data scale 段落讨论。\"\n\n- id: v17-R1-W9\n  summary: Seed 43 使用 sampling eval (T=0.7) 而非 greedy\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 fresh: 未提及。Appendix A 和 Table 7 footnote 已标注。\"\n\n- id: v17-R1-W10\n  summary: Hacking mode 分类器人工验证仅 50 样本\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 fresh: 未直接提及。R2-S2 肯定了 50 样本验证。\"\n\n- id: v17-VISUAL-LAYOUT\n  summary: 前 3 页纯文本无 display item，视觉节奏不均\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - round: 17\n    reviewers: [visual]\n    note: \"建议将 Figure 1 提前至 page 2-3。\"\n  - round: 18\n    reviewers: [visual]\n    note: \"R18 视觉审查再次确认：pages 1-3 纯文本无 display item；page 7 堆叠 3 个 figure 过密；page 5 纯文本形成断裂感。Figure 1 出现在 page 4 略晚。\"\n\n- id: v17-VISUAL-FONT\n  summary: Figure 4, 5 内部文字偏小\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [visual]\n    note: \"R18 视觉审查：Figure 2 密集曲线区域细节需放大辨认。整体 figure 字号问题持续。\"\n\n# === New issues from Round 18 ===\n- id: v18-R12-W1\n  summary: ISR 概念在 component necessity 和 structural quality 之间滑移，弱化 Goodhart 分析解释力\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R2-W2 Must-Fix, R1 交叉强烈 AGREE。§1 和 §3.2 定义 ISR 为 necessity，但 §4.3 隐含 high ISR = high quality。NLI ρ=-0.049 反证 ISR≠quality。核心问题：ISR-as-reward 崩溃可能因 ISR 本身不是 quality 的好 proxy，而非 'Goodhart on quality'。需区分 'Goodhart on ISR metric' 和 'Goodhart on structural quality'。\"\n  action_items:\n  - round: 18\n    action: \"在 §3.2 和 §4.3 明确区分 ISR-as-necessity-metric 被 gamed vs structural-quality 下降的因果关系\"\n    assigned_to: paper_agent\n    status: open\n\n- id: v18-R1-W2\n  summary: ISR component-count bias 在诊断场景（ISR-as-diagnostic）未做 matched 分析\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R1-W2 Must-Fix, R2 交叉 AGREE。§4.3 premise-count matched 分析仅针对 ISR-as-reward（1.06×），ISR-as-diagnostic 的主结果（Table 1 ISR 列）未控制 component count。Figure 2 caption 提到 component count 6.58→18.55（增长），R2 指出这实际反驳了 'ISR collapse 因 component 减少' 假说——但论文未突出此点。需报告训练过程中 mean component count 轨迹。\"\n  action_items:\n  - round: 18\n    action: \"在 §4.2 补充 component count 轨迹图或表；讨论 ISR collapse 与 length 变化的关系\"\n    assigned_to: paper_agent\n    status: open\n\n- id: v18-R1-W3\n  summary: SFT baseline 在 PR 极低时（13% vs ≥32%）比较 hacking 率不公平——混淆\"不 hack\"和\"没机会 hack\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R1-W3 列为 Must-Fix, R2 交叉部分 REBUT 降为 Should-Fix。R2 论点：SFT 定位为 pre-RL quality baseline 而非 hacking matched control；100-step RL (PR=32%) 已有 31% hacking vs SFT 8%，部分缓解。但 R1 核心直觉成立：需 PR-matched 非 RL baseline（如 rejection sampling）才能完全排除混淆。交叉后共识为 Should-Fix。\"\n  action_items:\n  - round: 18\n    action: \"在 §4.2 明确 SFT 的角色定位（pre-RL baseline, not PR-matched control）；强调 100-step 对照\"\n    assigned_to: paper_agent\n    status: open\n\n- id: v18-R1-W8\n  summary: Hacking taxonomy 未区分 severity levels（PG benign shortcutting vs TS genuine degeneration）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R1-W8 Should-Fix, R2 部分 REBUT——分类按 ISR interaction pattern 而非 severity 组织是一致的。但 R2 同意 Table 2 将 8 种模式加总为 total hacking rate 混淆了不同严重程度。建议区分 structural degeneration vs reward gaming without corruption。\"\n\n- id: v18-VISUAL-P20\n  summary: 最后一页（page 20）Table 10 仅占 25%，下方 65% 空白\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [visual]\n    note: \"视觉审查列为 critical。审稿人翻到最后页看到大面积留白产生负面印象。建议合并或补充内容。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 1733 · 2026-05-20T08:51:27.176839+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 21319}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 168
}
```

</details>

---
