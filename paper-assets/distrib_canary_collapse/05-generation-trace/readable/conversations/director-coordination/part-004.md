# Director coordination — Part 4 of 6

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../director-coordination.md) · [Part 5 →](part-005.md) · [Structured JSON](../../../sessions/c6/c6f03cee0ffebd7a6573.json)

## Round 97

### Tool call

_source line 998 · 2026-05-24T11:53:35.859151+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distrib_canary_collapse",
  "issues_yaml": "issues:\n# ============================================================\n# Round 1-7 (历史 resolved) — 保留跨轮次记录\n# ============================================================\n- id: \"R1-N1\"\n  summary: \"Ground-truth pairs 定义存在循环论证\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Effect-size GT 重定义完成。\"\n  resolution_round: 1\n\n- id: \"R1-N2\"\n  summary: \"FPR=0% 标定仅基于单 seed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"α=0.0 三 seed FPR 验证完成。\"\n  resolution_round: 1\n\n- id: \"R1-N3\"\n  summary: \"α=0.50 和 α=0.75 仅 1 seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Multi-seed 补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-N1\"\n  summary: \"核心方法论为计量经济学已有知识的直接迁移，新颖性有限\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Round 1 三层定位 reframe 完成。\"\n  resolution_round: 1\n\n- id: \"R2-N2\"\n  summary: \"α=0.75 multi-seed 实验未完成 + Appendix A 缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-N3\"\n  summary: \"实验规模过窄\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"跨架构验证已扩展至 15 model-seed 组合。\"\n  resolution_round: 1\n\n- id: \"R1-W1\"\n  summary: \"Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"核心修复完成。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"PermG 缺少 power analysis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Appendix N power analysis 完成。\"\n  resolution_round: 1\n\n- id: \"R1-W3\"\n  summary: \"75% spurious-signal rate headline 依赖 underpowered T-Y\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W4\"\n  summary: \"α=0.75 单 seed borderline 结果不应出现在 abstract\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W5\"\n  summary: \"Toda-Yamamoto 纳入理由表述不充分\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W6\"\n  summary: \"可重复性信息不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"超参补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-W3\"\n  summary: \"Token entropy canary 仅在 α=1.0 验证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"缺少独立 Limitations section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W5\"\n  summary: \"缺少 AI Writing Disclosure\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W6\"\n  summary: \"缺少 canary→perplexity 为何 spurious 的深入解释\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF1\"\n  summary: \"遗漏 Granger & Newbold (1974)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF2\"\n  summary: \"遗漏 Hataya et al. (2023) 和 Seddik et al. (2024)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W1-old\"\n  summary: \"Citation key chen2025scales 与实际作者不匹配\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"F2-W3\"\n  summary: \"Section 3 承诺的三项附录内容缺失\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"附录内容补充完成。\"\n  resolution_round: 3\n\n- id: \"F2-W8\"\n  summary: \"格式不合规：未使用 ACL 模板\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"ACL 模板迁移完成。\"\n  resolution_round: 2\n\n- id: \"F2-REF1\"\n  summary: \"遗漏 arXiv:2502.15654\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF1\"\n  summary: \"遗漏 arXiv:2602.10531\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF2\"\n  summary: \"遗漏 arXiv:2505.19046\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF3\"\n  summary: \"遗漏 arXiv:2510.16657\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF5\"\n  summary: \"Appendix H CUSUM 未引用 Page (1954)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F4-REF1\"\n  summary: \"遗漏 Truong & Truong (2026)\"\n  category: reference\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"引用已添加并在 §1/§2 讨论。\"\n  resolution_round: 6\n\n- id: \"F4-REF3\"\n  summary: \"遗漏 Benjamini & Yekutieli (2001)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"§4 现引用 benjamini2001control。\"\n  resolution_round: 5\n\n- id: \"F2-REF3\"\n  summary: \"Dakos et al. (2012) + Schreiber (2000) + Phipson & Smyth (2010) 在 bib 中但正文未引用\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"引用补充完成。\"\n  resolution_round: 4\n\n- id: \"F6-W2\"\n  summary: \"页数可能超限\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"R8 PDF 审查确认主体 8 页合规。\"\n  resolution_round: 8\n\n- id: \"F2-W6b\"\n  summary: \"'Methodological pitfalls' 有 straw-man 倾向\"\n  category: framing\n  severity: major\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 8\n  resolution: \"全文已改为 'design considerations'。R8 fresh review 未再提及。\"\n  resolution_round: 8\n\n# ============================================================\n# 活跃 issues — 历史轮次 + Round 10 Fresh Review 更新\n# ============================================================\n\n- id: \"F3-J4\"\n  summary: \"PermG FPR 超出 nominal 5%，architecture-dependent\"\n  category: method\n  severity: critical\n  status: open\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 3\n  last_seen_round: 10\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R8 fresh review 双方最高优先级共识。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 CI 报告统一完成，但 FPR 本身仍偏高。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10 MF-3: FPR=11.1% (CI [1.2%,30.4%]) 超出 nominal 5%。CI 上界 30.4% 动摇方法推荐。GPT-2 medium FPR=50% 说明 architecture-dependent。交叉共识：AGREE。\"\n\n- id: \"F5-N2\"\n  summary: \"T=10 统计效力不足(power≈37%), sharp onset 可能是 power artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Power simulation 重写通过 Reviewer #75。Steepness comparison k_obs=18.79 vs k_H0=6.14 (ratio 3.06×, CI non-overlapping) 写入 method.tex + experiments.tex + appendix。Dense α 证据 (17 points, sigmoid k=15.7) 额外支撑。\"\n  resolution_round: 9\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n\n- id: \"F2-W4b\"\n  summary: \"Proposition 3 本质是 curve fitting / empirical scaling，非理论推导\"\n  category: framing\n  severity: critical\n  status: open\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 已降级为 'empirical scaling observation'，β CI 诚实报告。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10 MF-4: 仍以 Proposition 3 形式呈现。5T 拟合 2 参数仅 3 DF。γ CI [0.24,0.78] 跨 3× 范围。未与 linear/log-linear 做 AIC/BIC 比较。交叉共识：AGREE。\"\n\n- id: \"F2-W2b\"\n  summary: \"'Detectability landscape' framing 承诺超过交付\"\n  category: framing\n  severity: critical\n  status: open\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 framing 调整为 'detection boundary characterization'。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10 MF-2: 完整 (α,T) grid 仅 Pythia-410M。跨架构仅 α=1.0，4/15 失败(27%)。Abstract '345M-6.9B' 与实际不符(max 3B)。交叉共识：AGREE。\"\n\n- id: \"F2-W1\"\n  summary: \"α=0.60 sync dip：precision sensitivity (bf16 0/8 vs fp32 6/8)\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 3\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10 SF-2: sync-dip 解释是 post-hoc (canary-triggered cessation 为实验 artifact)。排除后声称 15/15 拟合是 cherry-picking。交叉共识：AGREE。\"\n\n- id: \"F2-W10\"\n  summary: \"Cross-architecture 'coupling preserved' 条件 post-hoc 循环论证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10: 26.7% 失败率(4/15)。SmolLM3-3B non-monotonic entropy 违反 Design Principle 1。R1 部分 REBUT R2-N3 循环论证标签，但同意 Appendix X 假设未独立验证。\"\n\n- id: \"F2-W6\"\n  summary: \"Detection boundary 验证不足 (2T 拟合 2 参数=零自由度)\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n      note: \"与 F2-W4b 合并：LOO-CV MAE=0.037 未报告 CI 宽度。LOO MAE < split MAE 反常需解释。交叉共识：AGREE。\"\n\n- id: \"F2-W7\"\n  summary: \"Intervention 实验薄弱：post hoc threshold, n=2, 仅 α=1.0, CI 29-64%\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10 MF-5: N=2 seeds, α=1.0 only, 无 CI。Table 8 seed variability (p=0.001 vs 0.058) 说明 N=2 不足。Abstract 呈现 '64% perplexity reduction' 给人稳健印象。交叉共识：AGREE。\"\n\n- id: \"F5-N1\"\n  summary: \"核心方法是计量经济学标准技术的直接移植，贡献定位不清\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 10\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 贡献重定位为 'formalized observation'。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10 SF-1: Design Principles 仍以 'theoretical contribution' 权重呈现。R2 判定循环论证，R1 部分 REBUT（结构是假说-演绎法，不是循环）但同意 'formal' 过度。共识：降级为 'theoretically motivated, empirically validated design principles'。\"\n\n- id: \"F5-W1\"\n  summary: \"Proposition 1 数学深度有限，仅 Jensen 不等式\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 10\n  mentions:\n    - round: 5\n      reviewers: [2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n      note: \"与 F5-N1 合并。Appendix X mode amplification 假设未独立验证。SmolLM3-3B non-monotonic entropy 可能是假设失效实例。\"\n\n- id: \"F2-W5\"\n  summary: \"Token entropy → distinct-n 机械耦合 confound 未排除\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Metric structure 分析完成：mauve attribution 100% 确认非 metric coupling。ECE→distinct 独立于 token_entropy→distinct 路径。讨论已添加到 discussion.tex。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 9\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [2]\n    - round: 8\n      reviewers: [1, 2]\n\n- id: \"F2-W11\"\n  summary: \"α_c SE=0.006 低估真实 seed 不确定性\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 8\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1]\n    - round: 10\n      reviewers: []\n      note: \"R10 fresh review 未单独提及，但被 F2-W4b/F2-W6 的统计基础问题覆盖。\"\n\n- id: \"F2-W2\"\n  summary: \"Specification curve analysis 定位不精确\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Appendix E 已改称 'systematic robustness analysis'。R8/R9 fresh review 未再提及。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 8\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: []\n\n- id: \"F8-C2\"\n  summary: \"Discussion §6 过于简短(~100词)\"\n  category: writing\n  severity: major\n  status: resolved\n  resolution: \"Discussion 扩展至 20 行（metric-specific ceiling + practical implications + domain-dependent directionality）。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n\n- id: \"F8-C3\"\n  summary: \"与 Schaeffer et al. (2025) '8 种 collapse 定义' 的关系讨论不充分\"\n  category: framing\n  severity: major\n  status: resolved\n  resolution: \"Schaeffer taxonomy 映射已添加到 related_work.tex L5-6。检测框架显式对应 distributional shift 定义 (D4-D6)。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n\n- id: \"F8-C1\"\n  summary: \"Du & Tanaka-Ishii (2026) 引用三重错误：arXiv ID、标题、研究对象\"\n  category: reference\n  severity: critical\n  status: resolved\n  resolution: \"§2 已修正为 'related but distinct phenomenon'。R9 fresh review 未再提及。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: []\n\n- id: \"F4-REF5\"\n  summary: \"bib first author mismatch: dey2024breaking 实为 Gerstgrasser\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 4\n      reviewers: [2]\n    - round: 6\n      reviewers: [2]\n    - round: 8\n      reviewers: []\n    - round: 10\n      reviewers: []\n      note: \"R10 未提及，可能已修复，待确认。\"\n\n- id: \"F2-W9b\"\n  summary: \"孤立 bib entries (orphan)\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 2\n  last_seen_round: 8\n  mentions:\n    - round: 2\n      reviewers: [2]\n    - round: 6\n      reviewers: [2]\n    - round: 8\n      reviewers: []\n    - round: 10\n      reviewers: []\n      note: \"R10 未提及，可能已修复，待确认。\"\n\n- id: \"F6-C2\"\n  summary: \"buffa2026entropy 引用标题与 arXiv 实际论文不匹配\"\n  category: reference\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [2]\n    - round: 8\n      reviewers: []\n    - round: 10\n      reviewers: []\n      note: \"R10 未提及，可能已修复，待确认。\"\n\n- id: \"F8-W1\"\n  summary: \"数字一致性：'13' vs '12' contamination levels\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n    - round: 10\n      reviewers: []\n      note: \"R10 未提及，可能已修复，待确认。\"\n\n- id: \"F8-W2\"\n  summary: \"Figure 1/2 子图内文字偏小，Figure 2 灰度打印难区分\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [2, visual_check]\n    - round: 10\n      reviewers: [visual_check]\n      note: \"R10 视觉审查再次指出 Figure legend/tick label 字号约正文 60-65%，接近可读性下限。\"\n\n- id: \"F8-N1\"\n  summary: \"BH-FDR 在强正回归依赖下适用性讨论不充分\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"跨 pair correlation 结构报告在 method.tex。PRDS 假设适用性讨论已添加。FPR sensitivity analysis 额外支撑。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10 R1-SF-3 提及 PRDS 未验证，R2 REBUT 降级为 minor（K=8 下 BH vs BY 差异有限）。共识：minor。\"\n\n- id: \"F8-N2\"\n  summary: \"未讨论为何选择经典 permutation Granger 而非 neural Granger causality\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: []\n      note: \"R10 未提及，可能已修复，待确认。\"\n\n- id: \"F8-N3\"\n  summary: \"Appendix 关键验证内容(T=20 predict-then-verify, power analysis)应纳入正文\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: []\n      note: \"R10 未提及。\"\n\n- id: \"F8-N4\"\n  summary: \"Appendix Z V1/V2 predict-then-verify 存在 post-hoc adjustment 嫌疑\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: []\n      note: \"R10 未提及。\"\n\n- id: \"F8-REF1\"\n  summary: \"遗漏引用：online/continual learning 下 model collapse 检测\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"related_work.tex 已添加 scope 区分（iterative from-scratch vs continual learning）。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n\n# ============================================================\n# Round 9 issues\n# ============================================================\n\n- id: \"R9-C1\"\n  summary: \"FPR CI method.tex 内部矛盾：L16 [0,0] vs L24 [0%,41%]\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"FPR=10% MMCT sensitivity analysis 完成。K≥3 不受影响。Paper Agent 统一 CI 处理。\"\n  resolution_round: 9\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n\n- id: \"R9-m5\"\n  summary: \"Granger 'precedence' vs 'causality' 术语不一致\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10 R2-W4 提出，R1 REBUT（论文术语使用 disciplined，PermG 是文献标准名称）。共识：§3/§4 开头增加 1-2 句澄清即可，minor。\"\n\n- id: \"R9-REF1\"\n  summary: \"遗漏引用：Gerstgrasser et al. (2024) data accumulation vs replacement\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [2]\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10 R2-W1 再次提及。与 R10-SF2 关联。\"\n\n- id: \"R9-REF2\"\n  summary: \"遗漏引用：Steegen et al. (2016) multiverse analysis\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [2]\n    - round: 10\n      reviewers: [1, 2]\n      note: \"与 Appendix E specification curve 直接相关。交叉共识：AGREE。\"\n\n# ============================================================\n# Round 10 Fresh Review — 新 issues\n# ============================================================\n\n- id: \"R10-MF5\"\n  summary: \"'Five families (345M-6.9B)' 数字自洽性错误\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract '345M-6.9B' 实际 max 3B。'Five families' 实为 3 distinct families。Limitations 承认 >7B untested。交叉共识：AGREE，must-fix。\"\n\n- id: \"R10-SF2\"\n  summary: \"Data accumulation vs replacement paradigm 未讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"所有实验用 replacement。Discussion 应讨论 accumulation 下 landscape 的预期变化。\"\n\n- id: \"R10-SF3\"\n  summary: \"单一解码策略 (temperature 1.0/top-k=50) 需定性讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Limitations 仅半句。应讨论 lower temperature/nucleus sampling 预期方向。\"\n\n- id: \"R10-REF1\"\n  summary: \"遗漏引用：Hataya et al. (2023) ICCV model collapse\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"早期 model collapse 研究，image generation 视角。\"\n\n- id: \"R10-SF4\"\n  summary: \"方法敏感性 '3%-92%' framing 混淆失效方法与真正 sensitivity\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"NaiveXCorr FPR=91.7% 是失效方法。Abstract '3% to 92%' 暗示连续谱，实际是 4 合格方法(2.8%-38.9%)+1 失效方法。R1 partial REBUT：纳入有警示价值，但 abstract framing 需修正。共识：保留分析，修正 abstract 表述。\"\n\n- id: \"R10-SF5\"\n  summary: \"Bivariate confounding：entropy/diversity 可能同受 distribution shift 驱动\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Entropy 连续指标灵敏度高于 diversity 离散 n-gram 指标。观察到的 'entropy leads diversity' 可能仅反映测量灵敏度差异而非因果先后。与 F5-N1 Design Principle 1 关联。交叉共识：AGREE。\"\n\n- id: \"R10-SF6\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"6/8 的 Clopper-Pearson 95% CI = [0.25, 0.92]。相邻 cell 差异可能不显著，削弱 'sharp onset' narrative。交叉共识：AGREE。\"\n\n- id: \"R10-SF7\"\n  summary: \"3-4 seeds replication power 有限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Table 8 显示 seed variability 存在。Specification curve 评估方法稳健性，不等同于采样稳健性。交叉共识：AGREE。\"\n\n- id: \"R10-m1\"\n  summary: \"Figure 3 y 轴标签 'FDR-significant pairs' 含义不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"建议添加括注如 'out of 8 canary→downstream pairs'。交叉共识：AGREE。\"\n\n- id: \"R10-m2\"\n  summary: \"Table 2 'x/8' 列含义未在 caption 定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"定义在 Figure 1 caption (p.3)，与 Table 2 (p.8) 相隔 5 页。R1 partial REBUT：已有定义但应在 Table 2 caption 重复。\"\n\n- id: \"R10-m3\"\n  summary: \"§5.1 '(§5.5)' 前向引用缺上下文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"交叉共识：AGREE。\"\n\n- id: \"R10-REF2\"\n  summary: \"遗漏引用：Mitchell et al. (2023) DetectGPT\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"AI text detection 领域最相关方法论。§2 应讨论 single-generation token-level vs multi-generation distributional 区别。交叉共识：AGREE。\"\n\n- id: \"R10-REF3\"\n  summary: \"遗漏引用：Runge et al. (2019) 短时间序列因果发现\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"与 T≤25 短序列设置直接相关。交叉共识：AGREE。\"\n\n- id: \"R10-REF4\"\n  summary: \"遗漏引用：Padmakumar et al. (2024) LM 对文本多样性影响\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"互补角度。交叉共识：AGREE。\"\n\n- id: \"R10-REF5\"\n  summary: \"遗漏引用：Montgomery SPC 经典文献\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"与 Appendix H/T CUSUM 讨论相关。交叉共识：AGREE。\"\n\n- id: \"R10-VIS1\"\n  summary: \"Discussion §6 溢出到第 9 页，可能违反 EMNLP 2026 八页主文限制\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [visual_check]\n      note: \"视觉审查发现 'Broader implications' 段落延伸到第 9 页顶部。需压缩 Discussion 或移入 Limitations/Ethics 区域。\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "issues_yaml": "issues:\n# ============================================================\n# Round 1-7 (历史 resolved) — 保留跨轮次记录\n# ============================================================\n- id: \"R1-N1\"\n  summary: \"Ground-truth pairs 定义存在循环论证\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Effect-size GT 重定义完成。\"\n  resolution_round: 1\n\n- id: \"R1-N2\"\n  summary: \"FPR=0% 标定仅基于单 seed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"α=0.0 三 seed FPR 验证完成。\"\n  resolution_round: 1\n\n- id: \"R1-N3\"\n  summary: \"α=0.50 和 α=0.75 仅 1 seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Multi-seed 补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-N1\"\n  summary: \"核心方法论为计量经济学已有知识的直接迁移，新颖性有限\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Round 1 三层定位 reframe 完成。\"\n  resolution_round: 1\n\n- id: \"R2-N2\"\n  summary: \"α=0.75 multi-seed 实验未完成 + Appendix A 缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-N3\"\n  summary: \"实验规模过窄\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"跨架构验证已扩展至 15 model-seed 组合。\"\n  resolution_round: 1\n\n- id: \"R1-W1\"\n  summary: \"Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"核心修复完成。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"PermG 缺少 power analysis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Appendix N power analysis 完成。\"\n  resolution_round: 1\n\n- id: \"R1-W3\"\n  summary: \"75% spurious-signal rate headline 依赖 underpowered T-Y\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W4\"\n  summary: \"α=0.75 单 seed borderline 结果不应出现在 abstract\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W5\"\n  summary: \"Toda-Yamamoto 纳入理由表述不充分\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W6\"\n  summary: \"可重复性信息不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"超参补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-W3\"\n  summary: \"Token entropy canary 仅在 α=1.0 验证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"缺少独立 Limitations section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W5\"\n  summary: \"缺少 AI Writing Disclosure\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W6\"\n  summary: \"缺少 canary→perplexity 为何 spurious 的深入解释\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF1\"\n  summary: \"遗漏 Granger & Newbold (1974)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF2\"\n  summary: \"遗漏 Hataya et al. (2023) 和 Seddik et al. (2024)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W1-old\"\n  summary: \"Citation key chen2025scales 与实际作者不匹配\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"F2-W3\"\n  summary: \"Section 3 承诺的三项附录内容缺失\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"附录内容补充完成。\"\n  resolution_round: 3\n\n- id: \"F2-W8\"\n  summary: \"格式不合规：未使用 ACL 模板\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"ACL 模板迁移完成。\"\n  resolution_round: 2\n\n- id: \"F2-REF1\"\n  summary: \"遗漏 arXiv:2502.15654\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF1\"\n  summary: \"遗漏 arXiv:2602.10531\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF2\"\n  summary: \"遗漏 arXiv:2505.19046\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF3\"\n  summary: \"遗漏 arXiv:2510.16657\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF5\"\n  summary: \"Appendix H CUSUM 未引用 Page (1954)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F4-REF1\"\n  summary: \"遗漏 Truong & Truong (2026)\"\n  category: reference\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"引用已添加并在 §1/§2 讨论。\"\n  resolution_round: 6\n\n- id: \"F4-REF3\"\n  summary: \"遗漏 Benjamini & Yekutieli (2001)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"§4 现引用 benjamini2001control。\"\n  resolution_round: 5\n\n- id: \"F2-REF3\"\n  summary: \"Dakos et al. (2012) + Schreiber (2000) + Phipson & Smyth (2010) 在 bib 中但正文未引用\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"引用补充完成。\"\n  resolution_round: 4\n\n- id: \"F6-W2\"\n  summary: \"页数可能超限\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"R8 PDF 审查确认主体 8 页合规。\"\n  resolution_round: 8\n\n- id: \"F2-W6b\"\n  summary: \"'Methodological pitfalls' 有 straw-man 倾向\"\n  category: framing\n  severity: major\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 8\n  resolution: \"全文已改为 'design considerations'。R8 fresh review 未再提及。\"\n  resolution_round: 8\n\n# ============================================================\n# 活跃 issues — 历史轮次 + Round 10 Fresh Review 更新\n# ============================================================\n\n- id: \"F3-J4\"\n  summary: \"PermG FPR 超出 nominal 5%，architecture-dependent\"\n  category: method\n  severity: critical\n  status: open\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 3\n  last_seen_round: 10\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R8 fresh review 双方最高优先级共识。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 CI 报告统一完成，但 FPR 本身仍偏高。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10 MF-3: FPR=11.1% (CI [1.2%,30.4%]) 超出 nominal 5%。CI 上界 30.4% 动摇方法推荐。GPT-2 medium FPR=50% 说明 architecture-dependent。交叉共识：AGREE。\"\n\n- id: \"F5-N2\"\n  summary: \"T=10 统计效力不足(power≈37%), sharp onset 可能是 power artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Power simulation 重写通过 Reviewer #75。Steepness comparison k_obs=18.79 vs k_H0=6.14 (ratio 3.06×, CI non-overlapping) 写入 method.tex + experiments.tex + appendix。Dense α 证据 (17 points, sigmoid k=15.7) 额外支撑。\"\n  resolution_round: 9\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n\n- id: \"F2-W4b\"\n  summary: \"Proposition 3 本质是 curve fitting / empirical scaling，非理论推导\"\n  category: framing\n  severity: critical\n  status: open\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 已降级为 'empirical scaling observation'，β CI 诚实报告。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10 MF-4: 仍以 Proposition 3 形式呈现。5T 拟合 2 参数仅 3 DF。γ CI [0.24,0.78] 跨 3× 范围。未与 linear/log-linear 做 AIC/BIC 比较。交叉共识：AGREE。\"\n\n- id: \"F2-W2b\"\n  summary: \"'Detectability landscape' framing 承诺超过交付\"\n  category: framing\n  severity: critical\n  status: open\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 framing 调整为 'detection boundary characterization'。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10 MF-2: 完整 (α,T) grid 仅 Pythia-410M。跨架构仅 α=1.0，4/15 失败(27%)。Abstract '345M-6.9B' 与实际不符(max 3B)。交叉共识：AGREE。\"\n\n- id: \"F2-W1\"\n  summary: \"α=0.60 sync dip：precision sensitivity (bf16 0/8 vs fp32 6/8)\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 3\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10 SF-2: sync-dip 解释是 post-hoc (canary-triggered cessation 为实验 artifact)。排除后声称 15/15 拟合是 cherry-picking。交叉共识：AGREE。\"\n\n- id: \"F2-W10\"\n  summary: \"Cross-architecture 'coupling preserved' 条件 post-hoc 循环论证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10: 26.7% 失败率(4/15)。SmolLM3-3B non-monotonic entropy 违反 Design Principle 1。R1 部分 REBUT R2-N3 循环论证标签，但同意 Appendix X 假设未独立验证。\"\n\n- id: \"F2-W6\"\n  summary: \"Detection boundary 验证不足 (2T 拟合 2 参数=零自由度)\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n      note: \"与 F2-W4b 合并：LOO-CV MAE=0.037 未报告 CI 宽度。LOO MAE < split MAE 反常需解释。交叉共识：AGREE。\"\n\n- id: \"F2-W7\"\n  summary: \"Intervention 实验薄弱：post hoc threshold, n=2, 仅 α=1.0, CI 29-64%\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10 MF-5: N=2 seeds, α=1.0 only, 无 CI。Table 8 seed variability (p=0.001 vs 0.058) 说明 N=2 不足。Abstract 呈现 '64% perplexity reduction' 给人稳健印象。交叉共识：AGREE。\"\n\n- id: \"F5-N1\"\n  summary: \"核心方法是计量经济学标准技术的直接移植，贡献定位不清\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 10\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 贡献重定位为 'formalized observation'。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10 SF-1: Design Principles 仍以 'theoretical contribution' 权重呈现。R2 判定循环论证，R1 部分 REBUT（结构是假说-演绎法，不是循环）但同意 'formal' 过度。共识：降级为 'theoretically motivated, empirically validated design principles'。\"\n\n- id: \"F5-W1\"\n  summary: \"Proposition 1 数学深度有限，仅 Jensen 不等式\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 10\n  mentions:\n    - round: 5\n      reviewers: [2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n      note: \"与 F5-N1 合并。Appendix X mode amplification 假设未独立验证。SmolLM3-3B non-monotonic entropy 可能是假设失效实例。\"\n\n- id: \"F2-W5\"\n  summary: \"Token entropy → distinct-n 机械耦合 confound 未排除\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Metric structure 分析完成：mauve attribution 100% 确认非 metric coupling。ECE→distinct 独立于 token_entropy→distinct 路径。讨论已添加到 discussion.tex。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 9\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [2]\n    - round: 8\n      reviewers: [1, 2]\n\n- id: \"F2-W11\"\n  summary: \"α_c SE=0.006 低估真实 seed 不确定性\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 8\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1]\n    - round: 10\n      reviewers: []\n      note: \"R10 fresh review 未单独提及，但被 F2-W4b/F2-W6 的统计基础问题覆盖。\"\n\n- id: \"F2-W2\"\n  summary: \"Specification curve analysis 定位不精确\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Appendix E 已改称 'systematic robustness analysis'。R8/R9 fresh review 未再提及。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 8\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: []\n\n- id: \"F8-C2\"\n  summary: \"Discussion §6 过于简短(~100词)\"\n  category: writing\n  severity: major\n  status: resolved\n  resolution: \"Discussion 扩展至 20 行（metric-specific ceiling + practical implications + domain-dependent directionality）。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n\n- id: \"F8-C3\"\n  summary: \"与 Schaeffer et al. (2025) '8 种 collapse 定义' 的关系讨论不充分\"\n  category: framing\n  severity: major\n  status: resolved\n  resolution: \"Schaeffer taxonomy 映射已添加到 related_work.tex L5-6。检测框架显式对应 distributional shift 定义 (D4-D6)。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n\n- id: \"F8-C1\"\n  summary: \"Du & Tanaka-Ishii (2026) 引用三重错误：arXiv ID、标题、研究对象\"\n  category: reference\n  severity: critical\n  status: resolved\n  resolution: \"§2 已修正为 'related but distinct phenomenon'。R9 fresh review 未再提及。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: []\n\n- id: \"F4-REF5\"\n  summary: \"bib first author mismatch: dey2024breaking 实为 Gerstgrasser\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 4\n      reviewers: [2]\n    - round: 6\n      reviewers: [2]\n    - round: 8\n      reviewers: []\n    - round: 10\n      reviewers: []\n      note: \"R10 未提及，可能已修复，待确认。\"\n\n- id: \"F2-W9b\"\n  summary: \"孤立 bib entries (orphan)\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 2\n  last_seen_round: 8\n  mentions:\n    - round: 2\n      reviewers: [2]\n    - round: 6\n      reviewers: [2]\n    - round: 8\n      reviewers: []\n    - round: 10\n      reviewers: []\n      note: \"R10 未提及，可能已修复，待确认。\"\n\n- id: \"F6-C2\"\n  summary: \"buffa2026entropy 引用标题与 arXiv 实际论文不匹配\"\n  category: reference\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [2]\n    - round: 8\n      reviewers: []\n    - round: 10\n      reviewers: []\n      note: \"R10 未提及，可能已修复，待确认。\"\n\n- id: \"F8-W1\"\n  summary: \"数字一致性：'13' vs '12' contamination levels\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n    - round: 10\n      reviewers: []\n      note: \"R10 未提及，可能已修复，待确认。\"\n\n- id: \"F8-W2\"\n  summary: \"Figure 1/2 子图内文字偏小，Figure 2 灰度打印难区分\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [2, visual_check]\n    - round: 10\n      reviewers: [visual_check]\n      note: \"R10 视觉审查再次指出 Figure legend/tick label 字号约正文 60-65%，接近可读性下限。\"\n\n- id: \"F8-N1\"\n  summary: \"BH-FDR 在强正回归依赖下适用性讨论不充分\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"跨 pair correlation 结构报告在 method.tex。PRDS 假设适用性讨论已添加。FPR sensitivity analysis 额外支撑。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10 R1-SF-3 提及 PRDS 未验证，R2 REBUT 降级为 minor（K=8 下 BH vs BY 差异有限）。共识：minor。\"\n\n- id: \"F8-N2\"\n  summary: \"未讨论为何选择经典 permutation Granger 而非 neural Granger causality\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: []\n      note: \"R10 未提及，可能已修复，待确认。\"\n\n- id: \"F8-N3\"\n  summary: \"Appendix 关键验证内容(T=20 predict-then-verify, power analysis)应纳入正文\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: []\n      note: \"R10 未提及。\"\n\n- id: \"F8-N4\"\n  summary: \"Appendix Z V1/V2 predict-then-verify 存在 post-hoc adjustment 嫌疑\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: []\n      note: \"R10 未提及。\"\n\n- id: \"F8-REF1\"\n  summary: \"遗漏引用：online/continual learning 下 model collapse 检测\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"related_work.tex 已添加 scope 区分（iterative from-scratch vs continual learning）。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n\n# ============================================================\n# Round 9 issues\n# ============================================================\n\n- id: \"R9-C1\"\n  summary: \"FPR CI method.tex 内部矛盾：L16 [0,0] vs L24 [0%,41%]\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"FPR=10% MMCT sensitivity analysis 完成。K≥3 不受影响。Paper Agent 统一 CI 处理。\"\n  resolution_round: 9\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n\n- id: \"R9-m5\"\n  summary: \"Granger 'precedence' vs 'causality' 术语不一致\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10 R2-W4 提出，R1 REBUT（论文术语使用 disciplined，PermG 是文献标准名称）。共识：§3/§4 开头增加 1-2 句澄清即可，minor。\"\n\n- id: \"R9-REF1\"\n  summary: \"遗漏引用：Gerstgrasser et al. (2024) data accumulation vs replacement\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [2]\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10 R2-W1 再次提及。与 R10-SF2 关联。\"\n\n- id: \"R9-REF2\"\n  summary: \"遗漏引用：Steegen et al. (2016) multiverse analysis\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [2]\n    - round: 10\n      reviewers: [1, 2]\n      note: \"与 Appendix E specification curve 直接相关。交叉共识：AGREE。\"\n\n# ============================================================\n# Round 10 Fresh Review — 新 issues\n# ============================================================\n\n- id: \"R10-MF5\"\n  summary: \"'Five families (345M-6.9B)' 数字自洽性错误\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract '345M-6.9B' 实际 max 3B。'Five families' 实为 3 distinct families。Limitations 承认 >7B untested。交叉共识：AGREE，must-fix。\"\n\n- id: \"R10-SF2\"\n  summary: \"Data accumulation vs replacement paradigm 未讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"所有实验用 replacement。Discussion 应讨论 accumulation 下 landscape 的预期变化。\"\n\n- id: \"R10-SF3\"\n  summary: \"单一解码策略 (temperature 1.0/top-k=50) 需定性讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Limitations 仅半句。应讨论 lower temperature/nucleus sampling 预期方向。\"\n\n- id: \"R10-REF1\"\n  summary: \"遗漏引用：Hataya et al. (2023) ICCV model collapse\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"早期 model collapse 研究，image generation 视角。\"\n\n- id: \"R10-SF4\"\n  summary: \"方法敏感性 '3%-92%' framing 混淆失效方法与真正 sensitivity\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"NaiveXCorr FPR=91.7% 是失效方法。Abstract '3% to 92%' 暗示连续谱，实际是 4 合格方法(2.8%-38.9%)+1 失效方法。R1 partial REBUT：纳入有警示价值，但 abstract framing 需修正。共识：保留分析，修正 abstract 表述。\"\n\n- id: \"R10-SF5\"\n  summary: \"Bivariate confounding：entropy/diversity 可能同受 distribution shift 驱动\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Entropy 连续指标灵敏度高于 diversity 离散 n-gram 指标。观察到的 'entropy leads diversity' 可能仅反映测量灵敏度差异而非因果先后。与 F5-N1 Design Principle 1 关联。交叉共识：AGREE。\"\n\n- id: \"R10-SF6\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"6/8 的 Clopper-Pearson 95% CI = [0.25, 0.92]。相邻 cell 差异可能不显著，削弱 'sharp onset' narrative。交叉共识：AGREE。\"\n\n- id: \"R10-SF7\"\n  summary: \"3-4 seeds replication power 有限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Table 8 显示 seed variability 存在。Specification curve 评估方法稳健性，不等同于采样稳健性。交叉共识：AGREE。\"\n\n- id: \"R10-m1\"\n  summary: \"Figure 3 y 轴标签 'FDR-significant pairs' 含义不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"建议添加括注如 'out of 8 canary→downstream pairs'。交叉共识：AGREE。\"\n\n- id: \"R10-m2\"\n  summary: \"Table 2 'x/8' 列含义未在 caption 定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"定义在 Figure 1 caption (p.3)，与 Table 2 (p.8) 相隔 5 页。R1 partial REBUT：已有定义但应在 Table 2 caption 重复。\"\n\n- id: \"R10-m3\"\n  summary: \"§5.1 '(§5.5)' 前向引用缺上下文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"交叉共识：AGREE。\"\n\n- id: \"R10-REF2\"\n  summary: \"遗漏引用：Mitchell et al. (2023) DetectGPT\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"AI text detection 领域最相关方法论。§2 应讨论 single-generation token-level vs multi-generation distributional 区别。交叉共识：AGREE。\"\n\n- id: \"R10-REF3\"\n  summary: \"遗漏引用：Runge et al. (2019) 短时间序列因果发现\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"与 T≤25 短序列设置直接相关。交叉共识：AGREE。\"\n\n- id: \"R10-REF4\"\n  summary: \"遗漏引用：Padmakumar et al. (2024) LM 对文本多样性影响\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"互补角度。交叉共识：AGREE。\"\n\n- id: \"R10-REF5\"\n  summary: \"遗漏引用：Montgomery SPC 经典文献\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"与 Appendix H/T CUSUM 讨论相关。交叉共识：AGREE。\"\n\n- id: \"R10-VIS1\"\n  summary: \"Discussion §6 溢出到第 9 页，可能违反 EMNLP 2026 八页主文限制\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [visual_check]\n      note: \"视觉审查发现 'Broader implications' 段落延伸到第 9 页顶部。需压缩 Discussion 或移入 Limitations/Ethics 区域。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 999 · 2026-05-24T11:53:36.010627+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml\", \"bytes\": 24810}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1000 · 2026-05-24T11:56:04.890540+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 10 Consolidated Review Report\n\n## Summary\n\n本文系统研究 model collapse（语言模型在自身输出上迭代训练导致的退化）的可检测性，通过在 contamination ratio (α) 和训练代数 (T) 构成的二维空间上映射\"检测景观\"。使用 permutation Granger causality (PermG) 作为核心统计工具，应用于 canary metrics（token entropy, distinct-n diversity），刻画检测边界、识别四种检测 regime，并展示 proof-of-concept 干预。在五个模型族上进行跨架构验证。目标投稿 EMNLP 2026 (ARR)。\n\n## Strengths\n\n1. **系统性实验设计**：首次在密集 (α, T) 网格（13 个 α 值 × 多个 T 值）上映射 model collapse 可检测性。Robustness 验证全面：specification curve analysis (1,160 configurations)、Shapley value decomposition、power simulation、CUSUM comparison、transfer entropy analysis。\n\n2. **方法论严谨度高于领域平均**：Multi-seed replication、BH-FDR correction、multi-method consensus test (MMCT)、leave-one-T-out cross-validation。执行质量超过该领域多数现有工作。\n\n3. **方法敏感性的警示价值**：同一数据上五种统计方法给出截然不同结论（从 universal detection 到 complete null），对后续工作有真正的警示意义——不能依赖单一检验下结论。\n\n4. **Phase diagram 可视化**：Figure 1 热力图有效压缩复杂多维结果为直观视觉，提供清晰的检测\"地图\"。\n\n5. **可重复性**：实验细节详尽（超参、seed、FDR 阈值），附录提供完整 specification curve 和消融分析。\n\n## Weaknesses\n\n### Must-Fix（5 个，共识）\n\n**MF-1** [Consensus AGREE] **Abstract 模型规模范围事实性错误**\nAbstract 声称 \"345M–6.9B\" 但 Table 2 (p.8) 最大模型为 SmolLM3-3B (~3B)。Limitations (p.9) 明确声明 \">7B is untested\"。\"Five families\" 同样夸大——Table 2 仅含 3 个可辨识独立 family (Pythia, GPT-2, SmolLM3)；同 family 不同 scale 不构成独立 family。Abstract 中的事实性错误。\n*Tracker: R10-MF5 + F2-W2b*\n\n**MF-2** [Consensus AGREE] **\"Detectability Landscape\" 承诺超过交付**\n完整 (α, T) grid 仅存在于 Pythia-410M。跨架构验证仅覆盖 α=1.0（最极端条件）。4/15 跨架构条件不支持 forward detection（27% 失败率）。Title \"Characterizing the Detectability Landscape\" 暗示通用性，但实验证据不支持。Abstract 应明确将 landscape scope 限定于 Pythia-410M 并注明跨架构局限性。\n*Tracker: F2-W2b（Round 2→10，持续 open）*\n\n**MF-3** [Consensus AGREE] **PermG FPR CI [1.2%, 30.4%] 动摇方法推荐**\n点估计 11.1% 已超标准 5% 阈值。CI 上界 30.4% 意味着最坏情况 ~1/3 null condition false reject。GPT-2 medium FPR=50% 揭示 architecture-dependence。削弱 Section 6 整个方法推荐框架的可信度。论文承认 FPR>5% 但未充分讨论 CI 对实际使用的影响。\n*Tracker: F3-J4（Round 3→10，持续 open）*\n\n**MF-4** [Consensus AGREE] **Power-law 检测边界统计基础薄弱**\nα_c(T) = A·T^{-γ} 用 2 参数拟合仅 11 个数据点（排除 ~25% sync-dip cells 后）。此样本量下 R²=0.969 无说服力。γ CI 跨 [0.24, 0.78]（3× 范围）。未与更简单替代模型（linear, log-linear）进行 AIC/BIC 正式比较。LOO-CV MAE=0.037 未报告 CI 宽度分布。仍以 \"Proposition 3\" 形式呈现，此前多轮已要求降级。\n*Tracker: F2-W4b + F2-W6（Round 2→10，持续 open）*\n\n**MF-5** [Consensus AGREE] **Intervention 证据不足但高调呈现**\nSection 5.6 intervention 仅在 N=2 seeds、α=1.0（最极端条件）、Pythia-410M 上测试，无置信区间。Abstract 中 \"64% perplexity reduction\" 给人稳健通用结论的印象。Seed variability 证据（Table 8: seed 42 p=0.001 vs seed 43 p=0.058）说明 N=2 不足。至少应在 abstract 加 \"proof-of-concept\" 限定词。\n*Tracker: F2-W7（Round 2→10，持续 open）*\n\n### Should-Fix（7 个）\n\n**SF-1** [Partial Consensus] **Design Principles overclaimed as \"formal/theoretical\"**\nR2 判定循环论证（经验证据 = 待证结论）；R1 部分反驳（结构是标准假说-演绎法，非循环），但同意 \"formal design rationale\" 过度。Appendix X propositions 依赖未独立验证的 mode amplification 假设。SmolLM3-3B non-monotonic entropy 可能是假设失效实例。共识：从 \"formal design rationale\" / \"theoretical contribution\" 降级为 \"theoretically motivated, empirically validated design principles\"，不与实证贡献并列为同等权重。\n*Tracker: F5-N1 + F5-W1（Round 5→10）*\n\n**SF-2** [Consensus AGREE] **Sync-dip 解释是 post-hoc**\nCanary-triggered cessation 机制是实验设计的产物（基于人工设定的 entropy threshold），非通用 regime。排除 sync-dip cells 后声称 \"15/15 match theory\" 是方法论上的 cherry-picking。应重新定位为 setting-specific artifact 或提供其他训练协议中也存在的证据。\n*Tracker: F2-W1（Round 2→10）*\n\n**SF-3** [Consensus AGREE] **Bivariate confounding 替代解释不足**\nEntropy 和 diversity 可能同受 underlying distribution shift 驱动，entropy 作为连续指标的测量灵敏度天然高于 diversity 的离散 n-gram 阈值。观察到的 \"entropy leads diversity\" 可能仅反映灵敏度差异而非因果先后。论文讨论不足。\n*Tracker: R10-SF5（新）*\n\n**SF-4** [Partial Consensus] **方法敏感性 \"3%–92%\" framing 有误导性**\nNaiveXCorr FPR=91.7% 是失效方法而非\"敏感\"方法。R1 部分反驳：纳入有警示价值，但同意 abstract \"3% to 92%\" framing 暗示五种方法形成连续谱，实际是 4 合格方法 (2.8%–38.9%) + 1 失效方法。共识：保留正文分析，修正 abstract 表述区分 \"失效基线\" 与 \"合格方法间的真正 sensitivity\"。\n*Tracker: R10-SF4（新）*\n\n**SF-5** [Consensus AGREE] **缺少与 AI text detection 文献的联系**\nRelated Work (§2) 完全未提及 AI-generated text detection (DetectGPT 等)。Single-generation token-level detection vs. multi-generation distributional detection 是值得讨论的关键区别。遗漏可能被 reviewer 标记为重大 gap。\n*Tracker: R10-REF2*\n\n**SF-6** [Consensus AGREE] **每 cell 仅 8 pairs → 极宽 binomial CI**\n6/8 的 Clopper-Pearson 95% CI = [0.25, 0.92]。Phase diagram 相邻 cell 差异可能在统计上不显著，削弱 \"sharp onset\" narrative (§5.2)。\n*Tracker: R10-SF6（新）*\n\n**SF-7** [Consensus AGREE] **3-4 seeds replication power 有限**\nSeed variability 有记录（Table 8）但未系统量化。Specification curve (1,160 configs) 部分补偿，但评估的是方法稳健性而非采样稳健性。\n*Tracker: R10-SF7（新）*\n\n### Minor Issues（9 个）\n\n- **m1**: Figure 3 y 轴标签 \"FDR-significant pairs\" 需括注说明（如 \"out of 8 canary→downstream pairs\"）[R2-m1, R1 AGREE]\n- **m2**: Table 2 \"x/8\" 列含义未在 table caption 定义（定义在 Figure 1 caption，相隔 5 页）[R2-m2, R1 partial]\n- **m3**: §5.1 前向引用 \"five families (§5.5)\" 首次出现时缺上下文 [R2-m3, R1 AGREE]\n- **m4**: Granger precedence vs. causality 术语——R2 认为不一致，R1 反驳（PermG 是文献标准名称，论文已三层处理）。共识：§3/§4 开头增加 1-2 句澄清 [DIVERGENCE]\n- **m5**: 小样本 bootstrap CI 可靠性应标注 caveat [R1-m5, R2 AGREE]\n- **m6**: BH-FDR PRDS 假设——R1 标为 should-fix，R2 反驳：K=8 下 BH vs BY 差异 ~log(8)≈2× 调整，应降为 minor。共识：minor，加一句说明 [R1-SF-3 降级]\n- **m7**: Figure 1 legend 符号偏小，打印分辨率下勉强可读 [visual check]\n- **m8**: 第 1-2 页和第 4-5 页连续纯文本无 display item，\"文字墙\"第一印象 [visual check]\n- **m9**: Appendix 18 页 (~3× 正文)——R2 认为增加审阅负担，R1 反驳（ARR 无长度限制，thoroughness 是优点）[DIVERGENCE]\n\n## Reviewer Consensus\n\n两位 Reviewer 独立给出 **Overall 3.5 (Borderline Conference)**，在以下核心问题上高度一致：\n\n1. **系统性 overclaim 模式**：Abstract/Title 承诺超过实验交付（模型规模范围、landscape 通用性、intervention 稳健性）\n2. **统计基础需加强**：PermG FPR CI 过宽不足以支撑推荐、power-law boundary 拟合不足、全文多处小样本\n3. **执行质量是真正优势**：实验方法论、robustness 验证、文档记录高于领域平均\n4. **存在接收路径**：如修正 overclaim 并诚实呈现统计 caveat，实证贡献足以达到 Conference 水平\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | 结论 |\n|------|---------|---------|------|\n| Design Principles 循环论证 (R2-N3) | 标准假说-演绎法，非循环；但 \"formal\" 过度 | 循环论证：经验证据 = 待证结论 | 部分收敛：均同意 overclaimed，对机制有分歧 |\n| NaiveXCorr 纳入 (R2-W2) | 纳入有真正警示价值；但 abstract framing 误导 | 失效方法不应与合格方法并列 | 部分收敛：保留正文，修正 abstract framing |\n| Granger 术语 (R2-W4) | 论文术语 disciplined；PermG 是标准名称 | 不一致，对 NLP 读者困惑 | Minor 分歧：加澄清句 |\n| Appendix 长度 (R2-m4) | Thoroughness 支持 reproducibility；ARR 无限制 | 审阅负担；部分 appendix 是 extras | Minor 分歧：不可操作 |\n| Excitement | 3.5（问题及时性） | 3.0（标准工具，新颖性有限） | 分歧 |\n\n## Questions for Authors\n\n1. 为什么跨架构验证仅在 α=1.0 下进行？能否对一个非 Pythia 架构补充 3-5 个中间 α 值以支撑 \"landscape\" claim？\n2. Sync-dip 在 Pythia-1.4B 上是否也存在？如果是 scale-dependent，对 four-regime narrative 意味什么？\n3. 实际部署中（无 canary-triggered cessation），PermG 的检测价值如何体现？\n4. 鉴于 FPR 从 2.8% 到 91.7%，是否考虑过 MMCT 按 FPR 控制能力加权投票？\n5. 能否提供 power-law vs. linear/log-linear boundary model 的 AIC/BIC 比较？\n6. 在 data accumulation（vs. replacement）和 lower-temperature decoding 下，检测边界的预期方向如何？\n\n## Missing References\n\n两位 Reviewer 共识：\n- **Mitchell et al. (2023)** \"DetectGPT\" — AI text detection，方法论相邻\n- **Runge et al. (2019)** — 短时间序列因果发现，与 T≤25 设置直接相关\n- **Padmakumar et al. (2024)** — LM 对文本多样性影响的互补视角\n- **Montgomery \"Statistical Quality Control\"** — SPC 框架，与 CUSUM 讨论相关\n- **Steegen et al. (2016)** — Multiverse analysis，与 specification curve (Appendix E) 直接相关\n- **Hataya et al. (2023)** — ICCV model collapse（image generation 视角）\n- **Gerstgrasser et al. (2024)** — Data accumulation vs. replacement paradigm\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求外部审稿。\n\n## Visual Layout Check（非评分项）\n\n**状态: 已完成**（耗时 ~5 分钟）\n\n- **[CRITICAL]** 第 9 页：Discussion §6 \"Broader implications\" 段落溢出到第 9 页顶部，属主文内容（非 Limitations/Ethics），可能违反 EMNLP 2026 八页主文限制。需压缩 Discussion 至第 8 页内或将该段移入不计页数区域。\n- **[WARNING]** 第 1-2 页：连续 2 页纯文本无 display item，Figure 1 直到第 3 页。审稿人前 2 分钟无视觉锚点。\n- **[WARNING]** 第 4-5 页：Method §4 + Experiments §5.1 连续密集文本，Table 1 直到第 6 页。\n- **[INFO]** Figure 1 legend 符号偏小（150dpi 勉强可读）；Figure 2 axis tick labels 约正文 60-65%，接近可读下限。色盲友好度尚可。全文无 margin overflow、LaTeX 错误残留。\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3 | 3.5 | 3 |\n| Excitement | 3.5 | 3 | 3 |\n| Reproducibility | — | 4 | 4 |\n| Overall | 3.5 | 3.5 | **3.5** |\n| Confidence | — | 4 | 4 |\n\n**判断依据**：实证贡献扎实（系统性 landscape mapping + 方法敏感性警示），但存在系统性 overclaim 模式（Abstract 模型规模虚报、landscape 通用性暗示、intervention 证据强度夸大），统计基础在多处偏弱（PermG FPR CI、power-law 拟合、小样本），方法新颖性有限（标准计量经济学工具的领域迁移）。\n\n**如果作者能**：(1) 修正所有事实性错误；(2) 将 Title/Abstract scope 收窄至实际覆盖范围；(3) 将 Design Principles 从 \"theoretical contribution\" 降级；(4) 在正文中诚实讨论 PermG FPR CI 和 boundary model 局限性；(5) 给 intervention 加 \"proof-of-concept\" 限定——论文有潜力达到 4.0 (Conference) 水平。当前状态为 Borderline Conference。\n\n**Confidence: 4/5** — 两位 Reviewer 均熟悉 model collapse 文献和 Granger causality 方法论，核心判断高度一致。\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 修正 \"345M–6.9B\" 为实际范围 (~345M–3B)\n- 修正 \"five families\" 为准确数量\n- \"3% to 92%\" framing 应区分失效方法与合格方法\n- \"64% perplexity reduction\" 加 \"proof-of-concept\" 限定\n\n### §1 Introduction\n- Contribution 2 的 \"formal design rationale\" 降级为 \"empirically grounded design heuristics\"\n- Contribution 3 的 \"power-law\" 限定统计支撑程度\n\n### §2 Related Work\n- 增加与 AI text detection 文献的定位讨论（single-generation vs. multi-generation）\n- 增加 data accumulation vs. replacement paradigm 讨论\n\n### §3 Design Rationale\n- \"Design Principles\" 框架降级，不使用 \"formal\" / \"theoretical contribution\" 措辞\n- 标注 mode amplification 假设的局限性和适用条件\n\n### §4 Method\n- PermG FPR CI [1.2%, 30.4%] 在正文中讨论含义（而非仅在附录引用）\n- \"Five statistical methods\" 比较中区分合格方法与失效基线\n- Proposition 3 从 \"Proposition\" 降级为 empirical observation\n\n### §5 Experiments\n- 明确 primary landscape 来自 Pythia-410M\n- Cross-architecture 27% 失败率在叙述中呈现\n- Sync-dip 定位为 setting-specific artifact\n- Intervention 加充分 scope limitation\n\n### §6 Discussion\n- 压缩至第 8 页内（视觉审查 critical finding）\n- 增加 accumulation vs. replacement 定性讨论\n- 增加 decoding strategy 影响定性讨论\n\n### Limitations\n- 模型规模上界与 abstract 一致\n- 补充 single decoding strategy 讨论\n- bf16/fp32 precision sensitivity 加一句\n\n### References\n- 补充 7 篇缺失引用",
  "project": "distrib_canary_collapse",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 10 Consolidated Review Report\n\n## Summary\n\n本文系统研究 model collapse（语言模型在自身输出上迭代训练导致的退化）的可检测性，通过在 contamination ratio (α) 和训练代数 (T) 构成的二维空间上映射\"检测景观\"。使用 permutation Granger causality (PermG) 作为核心统计工具，应用于 canary metrics（token entropy, distinct-n diversity），刻画检测边界、识别四种检测 regime，并展示 proof-of-concept 干预。在五个模型族上进行跨架构验证。目标投稿 EMNLP 2026 (ARR)。\n\n## Strengths\n\n1. **系统性实验设计**：首次在密集 (α, T) 网格（13 个 α 值 × 多个 T 值）上映射 model collapse 可检测性。Robustness 验证全面：specification curve analysis (1,160 configurations)、Shapley value decomposition、power simulation、CUSUM comparison、transfer entropy analysis。\n\n2. **方法论严谨度高于领域平均**：Multi-seed replication、BH-FDR correction、multi-method consensus test (MMCT)、leave-one-T-out cross-validation。执行质量超过该领域多数现有工作。\n\n3. **方法敏感性的警示价值**：同一数据上五种统计方法给出截然不同结论（从 universal detection 到 complete null），对后续工作有真正的警示意义——不能依赖单一检验下结论。\n\n4. **Phase diagram 可视化**：Figure 1 热力图有效压缩复杂多维结果为直观视觉，提供清晰的检测\"地图\"。\n\n5. **可重复性**：实验细节详尽（超参、seed、FDR 阈值），附录提供完整 specification curve 和消融分析。\n\n## Weaknesses\n\n### Must-Fix（5 个，共识）\n\n**MF-1** [Consensus AGREE] **Abstract 模型规模范围事实性错误**\nAbstract 声称 \"345M–6.9B\" 但 Table 2 (p.8) 最大模型为 SmolLM3-3B (~3B)。Limitations (p.9) 明确声明 \">7B is untested\"。\"Five families\" 同样夸大——Table 2 仅含 3 个可辨识独立 family (Pythia, GPT-2, SmolLM3)；同 family 不同 scale 不构成独立 family。Abstract 中的事实性错误。\n*Tracker: R10-MF5 + F2-W2b*\n\n**MF-2** [Consensus AGREE] **\"Detectability Landscape\" 承诺超过交付**\n完整 (α, T) grid 仅存在于 Pythia-410M。跨架构验证仅覆盖 α=1.0（最极端条件）。4/15 跨架构条件不支持 forward detection（27% 失败率）。Title \"Characterizing the Detectability Landscape\" 暗示通用性，但实验证据不支持。Abstract 应明确将 landscape scope 限定于 Pythia-410M 并注明跨架构局限性。\n*Tracker: F2-W2b（Round 2→10，持续 open）*\n\n**MF-3** [Consensus AGREE] **PermG FPR CI [1.2%, 30.4%] 动摇方法推荐**\n点估计 11.1% 已超标准 5% 阈值。CI 上界 30.4% 意味着最坏情况 ~1/3 null condition false reject。GPT-2 medium FPR=50% 揭示 architecture-dependence。削弱 Section 6 整个方法推荐框架的可信度。论文承认 FPR>5% 但未充分讨论 CI 对实际使用的影响。\n*Tracker: F3-J4（Round 3→10，持续 open）*\n\n**MF-4** [Consensus AGREE] **Power-law 检测边界统计基础薄弱**\nα_c(T) = A·T^{-γ} 用 2 参数拟合仅 11 个数据点（排除 ~25% sync-dip cells 后）。此样本量下 R²=0.969 无说服力。γ CI 跨 [0.24, 0.78]（3× 范围）。未与更简单替代模型（linear, log-linear）进行 AIC/BIC 正式比较。LOO-CV MAE=0.037 未报告 CI 宽度分布。仍以 \"Proposition 3\" 形式呈现，此前多轮已要求降级。\n*Tracker: F2-W4b + F2-W6（Round 2→10，持续 open）*\n\n**MF-5** [Consensus AGREE] **Intervention 证据不足但高调呈现**\nSection 5.6 intervention 仅在 N=2 seeds、α=1.0（最极端条件）、Pythia-410M 上测试，无置信区间。Abstract 中 \"64% perplexity reduction\" 给人稳健通用结论的印象。Seed variability 证据（Table 8: seed 42 p=0.001 vs seed 43 p=0.058）说明 N=2 不足。至少应在 abstract 加 \"proof-of-concept\" 限定词。\n*Tracker: F2-W7（Round 2→10，持续 open）*\n\n### Should-Fix（7 个）\n\n**SF-1** [Partial Consensus] **Design Principles overclaimed as \"formal/theoretical\"**\nR2 判定循环论证（经验证据 = 待证结论）；R1 部分反驳（结构是标准假说-演绎法，非循环），但同意 \"formal design rationale\" 过度。Appendix X propositions 依赖未独立验证的 mode amplification 假设。SmolLM3-3B non-monotonic entropy 可能是假设失效实例。共识：从 \"formal design rationale\" / \"theoretical contribution\" 降级为 \"theoretically motivated, empirically validated design principles\"，不与实证贡献并列为同等权重。\n*Tracker: F5-N1 + F5-W1（Round 5→10）*\n\n**SF-2** [Consensus AGREE] **Sync-dip 解释是 post-hoc**\nCanary-triggered cessation 机制是实验设计的产物（基于人工设定的 entropy threshold），非通用 regime。排除 sync-dip cells 后声称 \"15/15 match theory\" 是方法论上的 cherry-picking。应重新定位为 setting-specific artifact 或提供其他训练协议中也存在的证据。\n*Tracker: F2-W1（Round 2→10）*\n\n**SF-3** [Consensus AGREE] **Bivariate confounding 替代解释不足**\nEntropy 和 diversity 可能同受 underlying distribution shift 驱动，entropy 作为连续指标的测量灵敏度天然高于 diversity 的离散 n-gram 阈值。观察到的 \"entropy leads diversity\" 可能仅反映灵敏度差异而非因果先后。论文讨论不足。\n*Tracker: R10-SF5（新）*\n\n**SF-4** [Partial Consensus] **方法敏感性 \"3%–92%\" framing 有误导性**\nNaiveXCorr FPR=91.7% 是失效方法而非\"敏感\"方法。R1 部分反驳：纳入有警示价值，但同意 abstract \"3% to 92%\" framing 暗示五种方法形成连续谱，实际是 4 合格方法 (2.8%–38.9%) + 1 失效方法。共识：保留正文分析，修正 abstract 表述区分 \"失效基线\" 与 \"合格方法间的真正 sensitivity\"。\n*Tracker: R10-SF4（新）*\n\n**SF-5** [Consensus AGREE] **缺少与 AI text detection 文献的联系**\nRelated Work (§2) 完全未提及 AI-generated text detection (DetectGPT 等)。Single-generation token-level detection vs. multi-generation distributional detection 是值得讨论的关键区别。遗漏可能被 reviewer 标记为重大 gap。\n*Tracker: R10-REF2*\n\n**SF-6** [Consensus AGREE] **每 cell 仅 8 pairs → 极宽 binomial CI**\n6/8 的 Clopper-Pearson 95% CI = [0.25, 0.92]。Phase diagram 相邻 cell 差异可能在统计上不显著，削弱 \"sharp onset\" narrative (§5.2)。\n*Tracker: R10-SF6（新）*\n\n**SF-7** [Consensus AGREE] **3-4 seeds replication power 有限**\nSeed variability 有记录（Table 8）但未系统量化。Specification curve (1,160 configs) 部分补偿，但评估的是方法稳健性而非采样稳健性。\n*Tracker: R10-SF7（新）*\n\n### Minor Issues（9 个）\n\n- **m1**: Figure 3 y 轴标签 \"FDR-significant pairs\" 需括注说明（如 \"out of 8 canary→downstream pairs\"）[R2-m1, R1 AGREE]\n- **m2**: Table 2 \"x/8\" 列含义未在 table caption 定义（定义在 Figure 1 caption，相隔 5 页）[R2-m2, R1 partial]\n- **m3**: §5.1 前向引用 \"five families (§5.5)\" 首次出现时缺上下文 [R2-m3, R1 AGREE]\n- **m4**: Granger precedence vs. causality 术语——R2 认为不一致，R1 反驳（PermG 是文献标准名称，论文已三层处理）。共识：§3/§4 开头增加 1-2 句澄清 [DIVERGENCE]\n- **m5**: 小样本 bootstrap CI 可靠性应标注 caveat [R1-m5, R2 AGREE]\n- **m6**: BH-FDR PRDS 假设——R1 标为 should-fix，R2 反驳：K=8 下 BH vs BY 差异 ~log(8)≈2× 调整，应降为 minor。共识：minor，加一句说明 [R1-SF-3 降级]\n- **m7**: Figure 1 legend 符号偏小，打印分辨率下勉强可读 [visual check]\n- **m8**: 第 1-2 页和第 4-5 页连续纯文本无 display item，\"文字墙\"第一印象 [visual check]\n- **m9**: Appendix 18 页 (~3× 正文)——R2 认为增加审阅负担，R1 反驳（ARR 无长度限制，thoroughness 是优点）[DIVERGENCE]\n\n## Reviewer Consensus\n\n两位 Reviewer 独立给出 **Overall 3.5 (Borderline Conference)**，在以下核心问题上高度一致：\n\n1. **系统性 overclaim 模式**：Abstract/Title 承诺超过实验交付（模型规模范围、landscape 通用性、intervention 稳健性）\n2. **统计基础需加强**：PermG FPR CI 过宽不足以支撑推荐、power-law boundary 拟合不足、全文多处小样本\n3. **执行质量是真正优势**：实验方法论、robustness 验证、文档记录高于领域平均\n4. **存在接收路径**：如修正 overclaim 并诚实呈现统计 caveat，实证贡献足以达到 Conference 水平\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | 结论 |\n|------|---------|---------|------|\n| Design Principles 循环论证 (R2-N3) | 标准假说-演绎法，非循环；但 \"formal\" 过度 | 循环论证：经验证据 = 待证结论 | 部分收敛：均同意 overclaimed，对机制有分歧 |\n| NaiveXCorr 纳入 (R2-W2) | 纳入有真正警示价值；但 abstract framing 误导 | 失效方法不应与合格方法并列 | 部分收敛：保留正文，修正 abstract framing |\n| Granger 术语 (R2-W4) | 论文术语 disciplined；PermG 是标准名称 | 不一致，对 NLP 读者困惑 | Minor 分歧：加澄清句 |\n| Appendix 长度 (R2-m4) | Thoroughness 支持 reproducibility；ARR 无限制 | 审阅负担；部分 appendix 是 extras | Minor 分歧：不可操作 |\n| Excitement | 3.5（问题及时性） | 3.0（标准工具，新颖性有限） | 分歧 |\n\n## Questions for Authors\n\n1. 为什么跨架构验证仅在 α=1.0 下进行？能否对一个非 Pythia 架构补充 3-5 个中间 α 值以支撑 \"landscape\" claim？\n2. Sync-dip 在 Pythia-1.4B 上是否也存在？如果是 scale-dependent，对 four-regime narrative 意味什么？\n3. 实际部署中（无 canary-triggered cessation），PermG 的检测价值如何体现？\n4. 鉴于 FPR 从 2.8% 到 91.7%，是否考虑过 MMCT 按 FPR 控制能力加权投票？\n5. 能否提供 power-law vs. linear/log-linear boundary model 的 AIC/BIC 比较？\n6. 在 data accumulation（vs. replacement）和 lower-temperature decoding 下，检测边界的预期方向如何？\n\n## Missing References\n\n两位 Reviewer 共识：\n- **Mitchell et al. (2023)** \"DetectGPT\" — AI text detection，方法论相邻\n- **Runge et al. (2019)** — 短时间序列因果发现，与 T≤25 设置直接相关\n- **Padmakumar et al. (2024)** — LM 对文本多样性影响的互补视角\n- **Montgomery \"Statistical Quality Control\"** — SPC 框架，与 CUSUM 讨论相关\n- **Steegen et al. (2016)** — Multiverse analysis，与 specification curve (Appendix E) 直接相关\n- **Hataya et al. (2023)** — ICCV model collapse（image generation 视角）\n- **Gerstgrasser et al. (2024)** — Data accumulation vs. replacement paradigm\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求外部审稿。\n\n## Visual Layout Check（非评分项）\n\n**状态: 已完成**（耗时 ~5 分钟）\n\n- **[CRITICAL]** 第 9 页：Discussion §6 \"Broader implications\" 段落溢出到第 9 页顶部，属主文内容（非 Limitations/Ethics），可能违反 EMNLP 2026 八页主文限制。需压缩 Discussion 至第 8 页内或将该段移入不计页数区域。\n- **[WARNING]** 第 1-2 页：连续 2 页纯文本无 display item，Figure 1 直到第 3 页。审稿人前 2 分钟无视觉锚点。\n- **[WARNING]** 第 4-5 页：Method §4 + Experiments §5.1 连续密集文本，Table 1 直到第 6 页。\n- **[INFO]** Figure 1 legend 符号偏小（150dpi 勉强可读）；Figure 2 axis tick labels 约正文 60-65%，接近可读下限。色盲友好度尚可。全文无 margin overflow、LaTeX 错误残留。\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3 | 3.5 | 3 |\n| Excitement | 3.5 | 3 | 3 |\n| Reproducibility | — | 4 | 4 |\n| Overall | 3.5 | 3.5 | **3.5** |\n| Confidence | — | 4 | 4 |\n\n**判断依据**：实证贡献扎实（系统性 landscape mapping + 方法敏感性警示），但存在系统性 overclaim 模式（Abstract 模型规模虚报、landscape 通用性暗示、intervention 证据强度夸大），统计基础在多处偏弱（PermG FPR CI、power-law 拟合、小样本），方法新颖性有限（标准计量经济学工具的领域迁移）。\n\n**如果作者能**：(1) 修正所有事实性错误；(2) 将 Title/Abstract scope 收窄至实际覆盖范围；(3) 将 Design Principles 从 \"theoretical contribution\" 降级；(4) 在正文中诚实讨论 PermG FPR CI 和 boundary model 局限性；(5) 给 intervention 加 \"proof-of-concept\" 限定——论文有潜力达到 4.0 (Conference) 水平。当前状态为 Borderline Conference。\n\n**Confidence: 4/5** — 两位 Reviewer 均熟悉 model collapse 文献和 Granger causality 方法论，核心判断高度一致。\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 修正 \"345M–6.9B\" 为实际范围 (~345M–3B)\n- 修正 \"five families\" 为准确数量\n- \"3% to 92%\" framing 应区分失效方法与合格方法\n- \"64% perplexity reduction\" 加 \"proof-of-concept\" 限定\n\n### §1 Introduction\n- Contribution 2 的 \"formal design rationale\" 降级为 \"empirically grounded design heuristics\"\n- Contribution 3 的 \"power-law\" 限定统计支撑程度\n\n### §2 Related Work\n- 增加与 AI text detection 文献的定位讨论（single-generation vs. multi-generation）\n- 增加 data accumulation vs. replacement paradigm 讨论\n\n### §3 Design Rationale\n- \"Design Principles\" 框架降级，不使用 \"formal\" / \"theoretical contribution\" 措辞\n- 标注 mode amplification 假设的局限性和适用条件\n\n### §4 Method\n- PermG FPR CI [1.2%, 30.4%] 在正文中讨论含义（而非仅在附录引用）\n- \"Five statistical methods\" 比较中区分合格方法与失效基线\n- Proposition 3 从 \"Proposition\" 降级为 empirical observation\n\n### §5 Experiments\n- 明确 primary landscape 来自 Pythia-410M\n- Cross-architecture 27% 失败率在叙述中呈现\n- Sync-dip 定位为 setting-specific artifact\n- Intervention 加充分 scope limitation\n\n### §6 Discussion\n- 压缩至第 8 页内（视觉审查 critical finding）\n- 增加 accumulation vs. replacement 定性讨论\n- 增加 decoding strategy 影响定性讨论\n\n### Limitations\n- 模型规模上界与 abstract 一致\n- 补充 single decoding strategy 讨论\n- bf16/fp32 precision sensitivity 加一句\n\n### References\n- 补充 7 篇缺失引用",
    "project": "distrib_canary_collapse",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
  }
}
```

</details>

---


### Tool result

_source line 1001 · 2026-05-24T11:56:08.957458+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_150c7ce908e05d7932315e0288cf5bfb:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4066
}
```

</details>

---


### Assistant

_source line 1002 · 2026-05-24T11:56:24.981802+00:00_

Round 10 审稿圆桌会议完成，报告已投递至 Research Director。

**审稿结论：Overall 3.5 (Borderline Conference)**

两位 Reviewer 核心判断高度一致（13/15 条 AGREE），关键共识：

| 类别 | 数量 | 核心问题 |
|------|------|----------|
| Must-Fix | 5 | Abstract 规模虚报、landscape 通用性 gap、PermG FPR CI 过宽、power-law 拟合不足、intervention underpowered |
| Should-Fix | 7 | Design Principles overclaim、sync-dip post-hoc、bivariate confounding、method sensitivity framing、缺 AI text detection 文献、binomial CI 宽、seed 不足 |
| Minor | 9 | 标签清晰度、术语统一、bootstrap caveat、PRDS 降级、视觉排版等 |
| 缺失引用 | 7 | DetectGPT、Runge(2019)、Padmakumar(2024)、Montgomery SPC、Steegen(2016)、Hataya(2023)、Gerstgrasser(2024) |

**视觉审查发现 1 个 critical**：Discussion 溢出至第 9 页，可能违反 EMNLP 2026 八页限制。

**路径到 4.0 (Conference)**：修正事实错误 + 收窄 scope + 降级 Design Principles + 诚实呈现统计局限性 + intervention 加 proof-of-concept 限定。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 98

## Round 98

2 recorded events


### User

_source line 1003 · 2026-05-24T11:56:27.524503+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **与 R2 一致的 Must-Fix**：N1（模型规模虚报）、N2（landscape scope 与 claims 不匹配）
- **反驳 R2 的 Must-Fix**：N3（循环论证指控过重，应为"理论措辞 overstate"而非逻辑谬误）
- **与 R2 一致的 Should-Fix**：W1（sync-dip post-hoc）、W3（boundary 统计基础）、W5（缺失文献）
- **反驳 R2 的 Should-Fix**：W2（NaiveXCorr 纳入有警示价值，但 Abstract framing 确需修正）、W4（术语已足够 disciplined，"Granger causality" 是方法标准名称）
- **补充 R2 未覆盖的关键问题**：PermG FPR 11.1% 应为 Must-Fix（非 minor）、Intervention 实验 underpowered、每 cell 8 pairs 的 binomial CI 问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1004 · 2026-05-24T11:56:41.084744+00:00_

Round 10 圆桌审稿已完成。

**审稿报告已投递至 Research Director。**

核心结论：**Overall 3.5 (Borderline Conference)**，两位 Reviewer 独立评分一致。

关键发现摘要：
- **5 个 Must-Fix**（共识）：Abstract 模型规模虚报、landscape 通用性 overclaim、PermG FPR CI 过宽、power-law 边界统计基础薄弱、intervention 证据不足但高调呈现
- **7 个 Should-Fix**：Design Principles 理论定位过度、sync-dip post-hoc、bivariate confounding、方法敏感性 framing 误导、缺失 AI text detection 文献、binomial CI 宽、seed replication power 有限
- **视觉审查**：Discussion 可能溢出第 8 页限制（critical）、首 2 页无 display item（warning）
- **主要分歧**：Design Principles 是否构成"循环论证"（R1 反驳）、NaiveXCorr 纳入价值（R1 部分反驳）、Granger 术语一致性（R1 反驳）、Excitement 评分（R1: 3.5 vs R2: 3.0）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 99

## Round 99

50 recorded events


### User

_source line 1005 · 2026-05-24T13:14:45.480782+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distrib_canary_collapse
- 论文路径: projects/distrib_canary_collapse/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1006 · 2026-05-24T13:14:52.518903+00:00_

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
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1007 · 2026-05-24T13:14:52.570027+00:00_

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
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-24T13:14:59.505284+00:00_

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
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
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

_source line 1009 · 2026-05-24T13:14:59.557447+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-24T13:15:05.134233+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1011 · 2026-05-24T13:15:07.042604+00:00_

{"result":"# 项目 distrib_canary_collapse 概况\n\n## 实验状态 (214 个)\n\n- **gen_wiki_gpt2m_a100_s42_v3**: DONE (success) — \n- **mvp_v4_rep44**: DONE (success) — \n- **plan_006_s42**: DONE (failed) — \n- **plan_006_s42_resume**: DONE (killed) — \n- **gen_wiki_gpt2m_a100_s42_v2**: DONE (killed) — \n- **method_ablation_phase2**: DONE (success) — \n- **alpha_sweep_a025_s42_v3**: DONE (success) — \n- **method_ablation_phase1**: DONE (success) — \n- **plan_009_bootstrap_ty**: DONE (success) — \n- **mvp_v3_rep43**: DONE (failed) — \n- **mvp_v3_rep42**: DONE (failed) — \n- **mvp_v2_rep43**: DONE (killed) — \n- **mvp_v2_rep42**: DONE (killed) — \n- **mvp_rep43**: DONE (killed) — \n- **mvp_rep42**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- 14b_t10_a060_s43（准备中）\n- 14b_t10_a075_s43（准备中）\n- 14b_t10_a050_s43（准备中）\n- t15_a050_s42_fp32（准备中）\n- qwen35_dryrun_launch（准备中）\n\n## 近期结论\n- **null_t15_s42_fp32** (success): FPR verification at T=15: null condition (α=0.00) should show 0% PermG detection rate with longer observation window, confirming FPR control generalizes across T\n- **null_t15_s43_fp32** (success): FPR verification at T=15: null condition (α=0.00) should show 0% PermG detection rate with longer observation window, confirming FPR control generalizes across T\n- **null_gpt2m_s43_fp32** (success): Cross-architecture FPR verification: GPT-2-medium null (α=0.00) should show 0% PermG detection rate, confirming method is not architecture-specific\n\n## 趋势\n成功 153 / 负向 4 / 失败 22 / 共 209\n累计 GPU: 8.4h\nrobust_pairs_K3: 0 →（近 3 次 success）\ntotal_pairs: 6 →（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-17855: 无 GPU 信息\nwestd-19828: 空闲 cuda:0, cuda:1\n\n## 告警\n- mvp_rep42: 已被终止 — unknown\n- mvp_rep43: 已被终止 — unknown\n- mvp_rep44: 已被终止 — unknown\n- mvp_v2_rep42: 已被终止 — unknown\n- mvp_v2_rep43: 已被终止 — unknown\n- mvp_v2_rep44: 已被终止 — unknown\n- mvp_v3_rep42: 训练失败 — unknown\n- mvp_v3_rep43: 
…[truncated 1803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1908
}
```

</details>

---


### Tool call

_source line 1012 · 2026-05-24T13:15:07.042964+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1013 · 2026-05-24T13:15:07.545243+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{graphicx}
13	\usepackage{booktabs}
14	\usepackage{subcaption}
15	\usepackage{algorithm}
16	\usepackage{algpseudocode}
17	\usepackage{amsthm}
18	\newtheorem{theorem}{Theorem}
19	\newtheorem{proposition}[theorem]{Proposition}
20	\newtheorem{designprinciple}[theorem]{Design Principle}
21	\theoremstyle{definition}
22	\newtheorem{assumption}[theorem]{Assumption}
23	
24	\title{Characterizing the Detectability Landscape of Iterative Model Collapse}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\maketitle
30	
31	\input{abstract}
32	\input{introduction}
33	\input{related_work}
34	\input{theory}
35	\input{method}
36	\input{experiments}
37	\input{discussion}
38	\input{limitations}
39	\bibliography{references}
40	
41	\input{appendix}
42	
43	\end{document}
44	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1014 · 2026-05-24T13:15:07.595916+00:00_

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
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
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

_source line 1015 · 2026-05-24T13:15:07.646560+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1016 · 2026-05-24T13:15:14.076486+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission deadline call for papers"
  }
}
```

</details>

---


### Tool call

_source line 1017 · 2026-05-24T13:15:14.227498+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1018 · 2026-05-24T13:15:14.278138+00:00_

1	\begin{abstract}
2	Iterative training on model-generated text degrades distributional quality well before standard metrics flag collapse, yet detecting this degradation is difficult: the time series are short ($T{\leq}25$ generations), the signal grows sub-linearly with contamination fraction, and, as we show, the choice of statistical test alone can shift conclusions from universal detection to complete null.
3	We characterize the detectability landscape of this process on Pythia-410M across 13 contamination levels with cross-architecture validation (five families, 345M--6.9B, at $\alpha{=}1.0$).
4	Permutation Granger causality\footnote{Granger precedence establishes temporal predictive improvement, not true causation~\cite{shojaie2022granger}.} (PermG) reveals a power-law detection boundary $\alpha_c(T) \propto T^{-2.08}$ (leave-one-$T$-out CV: MAE${=}0.037$, 15/15 within CI) and four regimes, including a sharp onset where detection jumps from 0/8 to 6/8 within a 2-percentage-point contamination interval.
5	Five methods applied to identical data yield null-control false positive rates from 3\% to 92\%, exposing method sensitivity as a primary concern.
6	Entropy Granger-precedes diversity collapse by ${\geq}1$ generation (14/15 experiments), providing a canary whose triggered cessation reduces peak perplexity by 64\%.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1019 · 2026-05-24T13:15:20.611500+00:00_

Web search results for query: "EMNLP 2026 ARR submission deadline call for papers"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here are the key details about EMNLP 2026 ARR submission deadline and call for papers:

## ARR Submission Deadline

The ARR submission deadline for EMNLP 2026 is May 25, 2026.

## Paper Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. In addition to traditional research results, papers may contribute negativ
…[truncated 969 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "elapsed_ms": 6535
}
```

</details>

---


### Tool call

_source line 1020 · 2026-05-24T13:15:27.530805+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines formatting page limit template",
  "allowed_domains": "['aclrollingreview.org', '2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 author guidelines formatting page limit template",
    "allowed_domains": "['aclrollingreview.org', '2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 1021 · 2026-05-24T13:15:28.484684+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1022 · 2026-05-24T13:15:28.585538+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\cite{shumailov2024curse,alemohammad2024mad}.
5	This process can be triggered by vanishingly small synthetic fractions~\cite{dohmatob2025strong}: lexical diversity narrows, calibration deteriorates, and each generation inherits the biases of its predecessors.
6	As machine-generated text grows prevalent on the web, such feedback loops pose a growing risk to production pipelines, and by the time standard quality metrics register degradation, the distribution may have already shifted irreversibly.
7	
8	This threat motivates a fundamental question: \emph{what does the detectability landscape of model collapse look like?}
9	At what contamination level does statistical detection become possible, how does this boundary depend on observation length, and what structure does the landscape exhibit?
10	These questions are nontrivial because iterative training produces short, noisy time series (often fewer than 15 points), where detection power drops sharply~\cite{boettiger2012limits}. Moreover, model collapse is a first-order transition~\cite{truong2026phase}, structurally ruling out the critical-slowing-down early-warning signals that ecologists rely on~\cite{scheffer2009early} (\S\ref{sec:related_work}).
11	
12	We map this landscape on Pythia-410M~\cite{biderman2023pythia} across 13 contamination levels with multi-seed replication (Figure~\ref{fig:regime_map}), and find structured terrain rather than smooth degradation: detection is absent through $\alpha{=}0.45$, then jumps from 0/8 to 6/8 significant pairs within a 2-percentage-point interval, before a non-monotonic dip and eventual reliable detection above a power-law boundary $\alpha_c(T) \propto T^{-2.08}$.
13	Cross-architecture validation across five families (345M--6.9B) confirms that this structure generaliz
…[truncated 2542 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1023 · 2026-05-24T13:15:28.636178+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1024 · 2026-05-24T13:15:28.636717+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\paragraph{Design considerations.}
5	\label{sec:pitfalls}
6	We use Granger causality~\cite{granger1969investigating} to test temporal precedence---whether past canary values improve prediction of downstream metrics---not mechanistic causation; bivariate Granger tests cannot exclude confounders~\cite{shojaie2022granger}.
7	Lead-lag analysis in iterative model collapse is fragile along three axes, each documented with data from \S\ref{sec:regime}--\ref{sec:dose_response}.
8	\emph{Method sensitivity}: five detection methods applied to identical data yield forward significance rates spanning 0\% to 92\%, with inter-method agreement at $\kappa{=}0.185$.
9	\emph{Spurious regression}: first-differencing eliminates canary$\to$perplexity associations ($F{\approx}0$, $p{=}0.99$) while preserving canary$\to$diversity (24/24$\to$24/24), exposing an entire analysis channel as trend-driven~\cite{granger1974spurious}.
10	\emph{Regime dependence}: the same Granger test shifts from 0/8 to 6/8 significant pairs within a 2-percentage-point interval ($\alpha{=}0.48 \to 0.50$).
11	
12	\begin{figure*}[t]
13	\centering
14	\includegraphics[width=\textwidth]{figures/fig_framework.pdf}
15	\caption{Analytical framework. (a)~Iterative contamination loop: each generation trains on an $\alpha$-fraction synthetic mixture, from which canary (entropy) and downstream (distinct-$n$) metrics are extracted. (b)~Multi-method consensus test (MMCT): five detection methods with varying FPR profiles converge to a $K{\geq}3$ majority vote; PermG is selected as the lowest-FPR directional method. (c)~Signal$\times$Resolution model: sub-linear signal $S(\alpha)$ and finite resolution $R(\alpha)$ produce four detection regimes (blind, onset, dip, detection), with boundary $\alpha_c(T) \propto T^{-2.08}$.}
16	\label{fig:framework}
17	\end{figure*}
18	
19	\subsection{Method Sensitivity Analysis}
20	\label{sec:mmct}
21	We compare five lead-lag detection methods in a mult
…[truncated 7313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 1025 · 2026-05-24T13:15:36.316744+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines formatting page limit template"

Links: [{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Discontinuation of the MS Word Template – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/discontinuation-word-template"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results, I found information about ACL Rolling Review 2026. Here are the key points regarding author guidelines:

## Key Author Guidelines for ACL Rolling Review 2026:

**Paper Requirements:**
- All submitted papers are expected to describe original, completed and unpublished work.
- Papers must not include authors' names and affiliations.
- Re-use of text from other publications should not exceed 10% total tokens.

**Template Requirements:**
- ARR abandons the MS Word Template for conference submissions. The s
…[truncated 729 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "elapsed_ms": 8785
}
```

</details>

---


### Tool call

_source line 1026 · 2026-05-24T13:15:46.809352+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1027 · 2026-05-24T13:15:47.421757+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study the detectability landscape of iterative training collapse using Pythia-410M~\cite{biderman2023pythia} (410M parameters, decoder-only) as the primary architecture, with cross-architecture validation on five families (later verified in \S\ref{sec:generalization}).
8	Training data is drawn from WikiText-103~\cite{merity2017pointer} following the replace paradigm of~\citet{shumailov2024curse}: each generation fine-tunes on a mixture of $\alpha$ synthetic and $(1{-}\alpha)$ real data, generates 5{,}000 replacement samples, and fully replaces the synthetic pool (hyperparameters in Appendix~\ref{app:training_details}; notation in Appendix~\ref{app:background}).
9	We run $T{=}10$ generations across 13 contamination levels ($\alpha \in \{0.00, 0.05, 0.10, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.75, 1.00\}$, including null control) with multi-seed replication (4 seeds at $\alpha{=}1.0$; 3 at primary levels).
10	
11	We track two \emph{canary metrics} (token entropy and ECE) and three \emph{downstream metrics}: distinct-1, distinct-2~\cite{li2016diversity}, and perplexity (distinct-3: Appendix~\ref{app:distinct3}).
12	All hypothesis tests apply BH-FDR correction~\cite{benjamini1995controlling} at $q{=}0.05$; PermG uses 5{,}000 permutations on first-differenced series~\cite{shojaie2022granger} with maximum lag~5 (window sensitivity: Appendix~\ref{app:window_sensitivity}).
13	As in \S\ref{sec:method}, PermG tests temporal precedence, not causation.
14	
15	
16	\subsection{Sharp Detection Onset}
17	\label{sec:regime}
18	
19	Diversity collapse occurs at every contamination level: distinct-1 declines by $14.1\%$ even at $\alpha{=}0.0$ (fine-tuning drift) and by $40.3{\pm}0.3\%$ at $\alpha{=}0.25$ (3-seed mean).
20	Despite this ubiquitous degradation, Granger detectability is sharply regime-dependent.
21	PermG finds 0/8 canary$\to$downstream pairs FDR-sig
…[truncated 11286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 612
}
```

</details>

---


### Tool call

_source line 1028 · 2026-05-24T13:15:47.422290+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 1029 · 2026-05-24T13:15:47.974771+00:00_

1	\section{Cascade Ordering}
2	\label{sec:cascade}
3	
4	If distributional collapse follows a predictable ordering across metrics, the earliest-responding metric can serve as a canary signal.
5	We formalize known metric properties---entropy as a continuous indicator of mode concentration, diversity as a threshold indicator of lexical coverage---under mode amplification~\cite{shumailov2024curse,dohmatob2024tale} (derivations in Appendix~\ref{app:cascade_theory}).
6	
7	\begin{designprinciple}[Entropy responds before diversity]\label{thm:entropy_leads}
8	Under mode amplification: \textup{(a)} entropy can decrease while the $\epsilon$-effective support $S_\epsilon(p) {=} |\{i: p_i > \epsilon\}|$ (hence distinct-$n$) is unchanged; \textup{(b)} if distinct-$n$ decreases, entropy has already decreased.
9	\end{designprinciple}
10	
11	The asymmetry arises because entropy responds to any mass redistribution (first-order), while diversity changes only when a token probability crosses the generation threshold~$\epsilon$; the margin $\gamma = \min_{i: p_i > \epsilon}(p_i - \epsilon)$ quantifies how much shift diversity absorbs silently.
12	
13	\begin{designprinciple}[Diversity lag $\geq 1$ generation]\label{prop:div_lag}
14	If the per-generation perturbation satisfies $\alpha\|\mathcal{T}(p_t) - p_t\|_\infty < \gamma(p_t, \epsilon)$ through entropy onset $t_H$, then diversity onset $t_D \geq t_H + 1$.
15	\end{designprinciple}
16	
17	ECE co-moves with entropy at zero lag: peakier conditionals simultaneously decrease per-token entropy and increase confidence ($\Delta\mathrm{ECE} \approx \Delta C > 0$ whenever $\Delta\bar{H} < 0$; qualitative argument in Appendix~\ref{app:cascade_theory}).
18	The predicted cascade $\{H, \mathrm{ECE}\} \to \mathrm{Distinct}$-$n$ holds in 14/15 experiments at $\alpha \geq 0.30$ (GPT-2-medium s43 bidirectional; within-domain WikiText, $2\sigma$ onset threshold): entropy and ECE onset at generation~1, distinct-$n$ at generation~2 ($t_H{=}t_{\mathrm{ECE}
…[truncated 653 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1030 · 2026-05-24T13:15:48.025488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1031 · 2026-05-24T13:15:48.126366+00:00_

1	\section{Discussion and Conclusion}\label{sec:discussion}
2	
3	\paragraph{Scope of claims.}
4	Our Granger-precedence claim is scoped to temporal predictive improvement~\cite{granger1969investigating,shojaie2022granger}: bivariate tests cannot exclude confounders, and the FPR CI ($[1.2\%, 30.4\%]$; \S\ref{sec:limitations}) means Type~I error may be non-negligible.
5	Entropy's greater sensitivity to distributional shifts than $n$-gram diversity means the temporal lead may partly reflect measurement sensitivity.
6	Five sync-dip cells are excluded from the boundary fit; including them raises MAE to 0.203 (Appendix~\ref{app:alpha_c_proof}).
7	Four of fifteen cross-architecture conditions do not confirm forward detection (\S\ref{sec:generalization}): non-monotonic entropy (SmolLM3-3B), precision sensitivity (GPT-2), and seed dependence (Pythia-1.4B; Appendices~\ref{app:cross_arch_fpr},~\ref{app:scale_14b}); $K{\geq}3$ consensus provides a fallback.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1032 · 2026-05-24T13:15:52.844114+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1033 · 2026-05-24T13:15:53.747486+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and canary metrics.}
5	Iterative training collapse was formalized by \citet{shumailov2024curse} and \citet{alemohammad2024mad}, who showed that recursively replacing real data with model-generated text causes progressive tail erosion; \citet{hataya2023will} demonstrated analogous degradation in image generation; \citet{briesch2023large} confirmed diversity decline in self-consuming loops; \citet{dey2024breaking} showed that accumulation mitigates collapse; \citet{schaeffer2025position} systematize eight distinct notions of ``collapse'' that this literature conflates.
6	Our operationalization (declining detection rate of Granger-precedence canary$\to$diversity links across generations) aligns most closely with Schaeffer et al.'s \emph{distributional shift} family (definitions~D4--D6 in their taxonomy), measuring how the generated distribution departs from the real-data baseline rather than tracking population risk or scaling-law exponents.
7	Theoretical analyses have sharpened these results: \citet{dohmatob2024tale} recast collapse as a change in scaling-law exponents, \citet{dohmatob2025strong} proved that collapse can occur even at vanishingly small synthetic fractions, \citet{seddik2026statistical} provide a statistical analysis of iterative contamination dynamics, and \citet{marchi2025challenging} challenge the universality of collapse under diverse training conditions.
8	Several works have proposed monitoring metrics: \citet{du2025scales} report ECE increases at 30\% contamination before accuracy drops, \citet{gambetta2024surplexity} introduces surplexity as a collapse detector, \citet{drayson2025detection} show that machine-generated text detection can prevent collapse, \citet{li2025verification} propose verification-based mitigation, and \citet{feng2024beyond} show that even imperfect verifiers can prevent collapse at scale.
9	\citet{padmakumar2024writing} show that writing with
…[truncated 4296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1034 · 2026-05-24T13:15:53.798077+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1035 · 2026-05-24T13:15:54.150317+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our landscape characterization uses Pythia-410M as the primary architecture; the phase diagram is Pythia-family-only (410M and 1.4B), and frontier-scale behavior ($>$7B) is untested.
5	With $T{\leq}25$ observations, statistical power remains limited ($\hat{\beta}{=}0.66$, CI $[0.24, 0.78]$); PermG's empirical FPR of $4/36$ (11.1\%, 6 seeds) is the lowest among directionally-specific methods but non-zero; the cluster-adjusted 95\% CI is $[1.2\%, 30.4\%]$ (within-seed ICC${=}0.14$).
6	Each cell's detection rate (e.g., 6/8) carries a wide binomial confidence interval (Clopper-Pearson: $[0.25, 0.92]$ for 6/8); the phase diagram should be read as a coarse topology rather than a precise probability surface.
7	Preliminary cross-architecture evaluation on GPT-2-medium reveals a substantially higher PermG FPR (6/12 pooled, 50\%), driven by ${\sim}4{\times}$ stronger null drift in entropy and ${\sim}7{\times}$ in distinct-3 (Appendix~\ref{app:cross_arch_fpr}); $K{\geq}3$ consensus maintains 0\% FPR across both architectures, though with a narrow margin (max 2/5 votes in the worst-case seed).
8	All experiments use full replacement~\cite{shumailov2024curse}; under data accumulation~\cite{dey2024breaking}, $\alpha_c$ would right-shift and the blind zone widen.
9	The sync-dip mechanism at $\alpha{=}0.60$ remains open.
10	All experiments use a single decoding strategy (temperature~$1.0$, top-$k{=}50$).
11	Lower temperatures accelerate mode concentration and should left-shift the detection boundary; nucleus sampling alters the effective diversity threshold $\epsilon$ in Design Principle~\ref{thm:entropy_leads}.
12	The directional effects are predictable---lower temperature compresses the landscape toward earlier detection---but the quantitative shift requires empirical calibration.
13	At boundary contamination levels ($\alpha \approx \alpha_c$), numerical precision (bf16 vs.\ fp32) can affect detection outcomes (GPT-2-medium: 
…[truncated 397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1036 · 2026-05-24T13:15:54.201150+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1037 · 2026-05-24T13:15:54.252050+00:00_

1	\appendix
2	
3	\section{Training Details and Metric Drift}
4	\label{app:training_details}
5	\label{app:drift}
6	
7	\paragraph{Hyperparameters.}
8	Each generation fine-tunes for 5{,}000 steps using AdamW (learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium).
9	Generation uses temperature $1.0$, top-$k{=}50$, max length 512 tokens, producing 5{,}000 samples per generation from 5{,}000-sample subsets of WikiText-103.
10	Canary metrics: token entropy $H(p_\theta | \text{context})$ over 1{,}000 held-out samples; ECE with 15 bins.
11	Additional downstream metrics (distinct-3, effective rank, Self-BLEU) appear in subsequent appendix sections.
12	
13	\paragraph{Metric drift.}
14	
15	\begin{table}[h]
16	\centering
17	\small
18	\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
19	\label{tab:drift_summary}
20	\resizebox{\columnwidth}{!}{%
21	\begin{tabular}{lccccc}
22	\toprule
23	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
24	\midrule
25	0.00 & $-4.6{\pm}0.4$ & $+37.6{\pm}14$ & $-14.1{\pm}0.4$ & $-9.6{\pm}0.4$ & $-20.6{\pm}1.0$ \\
26	0.10$^\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\
27	0.25 & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & $-18.1{\pm}0.8$ \\
28	0.50 & $-18.0{\pm}0.5$ & $+822.6{\pm}18.3$ & $-37.1{\pm}0.4$ & $-50.4{\pm}1.0$ & $+21.0{\pm}0.1$ \\
29	0.75 & $-27.6{\pm}0.2$ & $+1791{\pm}18$ & $-32.3{\pm}0.5$ & $-41.0{\pm}1.0$ & $+182.6{\pm}
…[truncated 5165 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1038 · 2026-05-24T13:16:10.466725+00:00_

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
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
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

_source line 1039 · 2026-05-24T13:16:10.517619+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1040 · 2026-05-24T13:16:15.939432+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1041 · 2026-05-24T13:16:16.793218+00:00_

issues:
# ============================================================
# Round 1-7 (历史 resolved) — 保留跨轮次记录
# ============================================================
- id: "R1-N1"
  summary: "Ground-truth pairs 定义存在循环论证"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Effect-size GT 重定义完成。"
  resolution_round: 1

- id: "R1-N2"
  summary: "FPR=0% 标定仅基于单 seed"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "α=0.0 三 seed FPR 验证完成。"
  resolution_round: 1

- id: "R1-N3"
  summary: "α=0.50 和 α=0.75 仅 1 seed"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Multi-seed 补充完成。"
  resolution_round: 1

- id: "R2-N1"
  summary: "核心方法论为计量经济学已有知识的直接迁移，新颖性有限"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Round 1 三层定位 reframe 完成。"
  resolution_round: 1

- id: "R2-N2"
  summary: "α=0.75 multi-seed 实验未完成 + Appendix A 缺失"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "完成。"
  resolution_round: 1

- id: "R2-N3"
  summary: "实验规模过窄"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "跨架构验证已扩展至 15 model-seed 组合。"
  resolution_round: 1

- id: "R1-W1"
  summary: "Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致"
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "核心修复完成。"
  resolution_round: 1

- id: "R1-W2"
  summary: "PermG 缺少 power analysis"
  category: method
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Appendix N power analysis 完成。"
  resolution_round: 1

- id: "R1-W3"
  summary: "75% spurious-signal rate headline 依赖 und
…[truncated 22809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1042 · 2026-05-24T13:16:16.944302+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review setting"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review setting"
  }
}
```

</details>

---


### Tool result

_source line 1043 · 2026-05-24T13:16:16.994976+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1044 · 2026-05-24T13:16:25.227061+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/agent/ -name \"config.yaml\" -o -name \"*.yaml\" | head -5 && echo \"---\" && find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/ -maxdepth 1 -name \"config.yaml\" 2>/dev/null",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/agent/ -name \"config.yaml\" -o -name \"*.yaml\" | head -5 && echo \"---\" && find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/ -maxdepth 1 -name \"config.yaml\" 2>/dev/null",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 1045 · 2026-05-24T13:16:25.327964+00:00_

find: ‘/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/agent/’: No such file or directory
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1046 · 2026-05-24T13:16:30.247068+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/ -maxdepth 2 -name \"config.yaml\" 2>/dev/null && echo \"---\" && find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/ -path \"*distrib_canary*\" -name \"*.yaml\" ! -path \"*review_issues*\" ! -path \"*artifacts*\" 2>/dev/null | head -10",
  "description": "Find config files for the project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/ -maxdepth 2 -name \"config.yaml\" 2>/dev/null && echo \"---\" && find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/ -path \"*distrib_canary*\" -name \"*.yaml\" ! -path \"*review_issues*\" ! -path \"*artifacts*\" 2>/dev/null | head -10",
    "description": "Find config files for the project"
  }
}
```

</details>

---


### Tool result

_source line 1047 · 2026-05-24T13:16:30.347899+00:00_

---
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/guo2024linguistic.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/dohmatob2025strong.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/gu2025datamixing.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/noci2024mind.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/barzilai2025consistency.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/gambetta2024surplexity.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/jing2022understanding.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/wang2026contaminated.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/chen2025scales.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/briesch2024selfconsuming.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1048 · 2026-05-24T13:16:55.545755+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "distrib_canary_collapse",
  "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
  }
}
```

</details>

---


### Tool result

_source line 1049 · 2026-05-24T13:17:15.377212+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 19831
}
```

</details>

---


### Tool call

_source line 1050 · 2026-05-24T13:17:16.230813+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 统计验证 + 实验有效性**。\n\n## 论文信息\n- 标题: \"Characterizing the Detectability Landscape of Iterative Model Collapse\"\n- 路径: `projects/distrib_canary_collapse/docs/paper/main.tex`（多文件结构，各 section 为独立 .tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_11/submitted.pdf`\n\n## Venue 要求\n- **EMNLP 2026** via ACL Rolling Review (ARR)\n- ARR 提交截止: 2026-05-25\n- 页数限制: 正文 8 页（严格），参考文献无限制，Limitations 不计入页数\n- 模板: ACL LaTeX template (`\\usepackage[review]{acl}`)\n- 匿名: double-blind\n- Long paper\n\n## 评分标准 (ARR Overall Assessment)\n5=Consider for Award (~top 2.5%), 4.5=Borderline Award, 4=Conference (主会议可接收), 3.5=Borderline Conference, 3=Findings (Findings 可接收), 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查重点\n\n1. **统计方法有效性**：\n   - PermG 的 FPR 控制（论文报告 11.1%，CI [1.2%, 30.4%]——超出 nominal 5%）\n   - BH-FDR correction 在正依赖结构下的适用性\n   - First-differencing 对 power 的影响\n   - 5,000 permutations 是否充分\n\n2. **Detection boundary 声称**：\n   - α_c(T) ∝ T^{-2.08} 的拟合基础（5 个 T 值拟合 2 参数）\n   - LOO-CV MAE=0.037 的可信度\n   - β CI [0.24, 0.78] 的宽度是否动摇结论\n   - sync-dip 排除是否合理\n\n3. **实验设计**：\n   - Multi-seed replication 的充分性（3-4 seeds）\n   - Cross-architecture validation: 4/15 失败条件的影响\n   - 每 cell 8 pairs 的 binomial CI 宽度\n   - Intervention 实验: N=2, α=1.0 only, post-hoc threshold\n\n4. **因果推断声称的 scope**：\n   - Granger precedence vs causality 的区分是否充分\n   - Bivariate confounding 的讨论\n   - 测量灵敏度差异 vs 真正 temporal lead\n\n请按 ARR 标准给出完整审稿意见：Summary, Strengths, Weaknesses, Questions, Overall Assessment (含评分和置信度)。",
  "reviewer_id": "1",
  "project": "distrib_canary_collapse",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 统计验证 + 实验有效性**。\n\n## 论文信息\n- 标题: \"Characterizing the Detectability Landscape of Iterative Model Collapse\"\n- 路径: `projects/distrib_canary_collapse/docs/paper/main.tex`（多文件结构，各 section 为独立 .tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_11/submitted.pdf`\n\n## Venue 要求\n- **EMNLP 2026** via ACL Rolling Review (ARR)\n- ARR 提交截止: 2026-05-25\n- 页数限制: 正文 8 页（严格），参考文献无限制，Limitations 不计入页数\n- 模板: ACL LaTeX template (`\\usepackage[review]{acl}`)\n- 匿名: double-blind\n- Long paper\n\n## 评分标准 (ARR Overall Assessment)\n5=Consider for Award (~top 2.5%), 4.5=Borderline Award, 4=Conference (主会议可接收), 3.5=Borderline Conference, 3=Findings (Findings 可接收), 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查重点\n\n1. **统计方法有效性**：\n   - PermG 的 FPR 控制（论文报告 11.1%，CI [1.2%, 30.4%]——超出 nominal 5%）\n   - BH-FDR correction 在正依赖结构下的适用性\n   - First-differencing 对 power 的影响\n   - 5,000 permutations 是否充分\n\n2. **Detection boundary 声称**：\n   - α_c(T) ∝ T^{-2.08} 的拟合基础（5 个 T 值拟合 2 参数）\n   - LOO-CV MAE=0.037 的可信度\n   - β CI [0.24, 0.78] 的宽度是否动摇结论\n   - sync-dip 排除是否合理\n\n3. **实验设计**：\n   - Multi-seed replication 的充分性（3-4 seeds）\n   - Cross-architecture validation: 4/15 失败条件的影响\n   - 每 cell 8 pairs 的 binomial CI 宽度\n   - Intervention 实验: N=2, α=1.0 only, post-hoc threshold\n\n4. **因果推断声称的 scope**：\n   - Granger precedence vs causality 的区分是否充分\n   - Bivariate confounding 的讨论\n   - 测量灵敏度差异 vs 真正 temporal lead\n\n请按 ARR 标准给出完整审稿意见：Summary, Strengths, Weaknesses, Questions, Overall Assessment (含评分和置信度)。",
    "reviewer_id": "1",
    "project": "distrib_canary_collapse",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1051 · 2026-05-24T13:17:31.819592+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15588
}
```

</details>

---


### Tool call

_source line 1052 · 2026-05-24T13:17:31.920355+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责 **新颖性/贡献定位 + 完整性 + 写作质量 + 格式合规**。\n\n## 论文信息\n- 标题: \"Characterizing the Detectability Landscape of Iterative Model Collapse\"\n- 路径: `projects/distrib_canary_collapse/docs/paper/main.tex`（多文件结构，各 section 为独立 .tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_11/submitted.pdf`\n\n## Venue 要求\n- **EMNLP 2026** via ACL Rolling Review (ARR)\n- ARR 提交截止: 2026-05-25\n- 页数限制: 正文 8 页（严格），参考文献无限制，Limitations 不计入页数\n- 模板: ACL LaTeX template (`\\usepackage[review]{acl}`)\n- 匿名: double-blind\n- Long paper\n\n## 评分标准 (ARR Overall Assessment)\n5=Consider for Award (~top 2.5%), 4.5=Borderline Award, 4=Conference (主会议可接收), 3.5=Borderline Conference, 3=Findings (Findings 可接收), 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查重点\n\n1. **新颖性与贡献定位**：\n   - 核心方法（Permutation Granger causality）是计量经济学标准技术的移植——novelty 在哪里？\n   - \"Detectability landscape\" 这一 framing 是否过度承诺？\n   - Design Principle 1-2 的理论深度（Jensen 不等式级别）\n   - 与 existing model collapse 文献（Shumailov, Dohmatob, Schaeffer 等）的差异化定位\n\n2. **完整性与 scope**：\n   - 实验是否全面覆盖了 \"landscape\" 的声称？\n   - Cross-architecture validation 仅 α=1.0，landscape 仅 Pythia-410M——这够吗？\n   - 与 data accumulation paradigm 的关系讨论\n   - 单一解码策略的讨论\n\n3. **写作质量**：\n   - Abstract 是否准确反映结果（注意 \"345M-6.9B\" vs 实际最大 3B）\n   - 术语一致性（Granger causality vs precedence）\n   - 方法敏感性 \"3%-92%\" 的 framing 是否误导（含失效方法 NaiveXCorr 91.7%）\n   - Figure/Table caption 信息完整性\n\n4. **格式合规**：\n   - 8 页限制（注意 Discussion 是否溢出）\n   - 匿名性\n   - Limitations section 位置和长度\n   - Abstract 是否 ≤200 words\n\n5. **Related Work 与 Missing References**：\n   - Mitchell et al. (2023) DetectGPT — AI text detection 最相关方法\n   - Runge et al. (2019) 短时间序列因果发现\n   - Padmakumar et al. (2024) LM 对文本多样性影响\n   - Steegen et al. (2016) multiverse analysis\n   - Gerstgrasser et al. (2024) data accumulation\n\n请按 ARR 标准给出完整审稿意见：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (含评分和置信度)。",
  "reviewer_id": "2",
  "project": "distrib_canary_collapse",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责 **新颖性/贡献定位 + 完整性 + 写作质量 + 格式合规**。\n\n## 论文信息\n- 标题: \"Characterizing the Detectability Landscape of Iterative Model Collapse\"\n- 路径: `projects/distrib_canary_collapse/docs/paper/main.tex`（多文件结构，各 section 为独立 .tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_11/submitted.pdf`\n\n## Venue 要求\n- **EMNLP 2026** via ACL Rolling Review (ARR)\n- ARR 提交截止: 2026-05-25\n- 页数限制: 正文 8 页（严格），参考文献无限制，Limitations 不计入页数\n- 模板: ACL LaTeX template (`\\usepackage[review]{acl}`)\n- 匿名: double-blind\n- Long paper\n\n## 评分标准 (ARR Overall Assessment)\n5=Consider for Award (~top 2.5%), 4.5=Borderline Award, 4=Conference (主会议可接收), 3.5=Borderline Conference, 3=Findings (Findings 可接收), 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查重点\n\n1. **新颖性与贡献定位**：\n   - 核心方法（Permutation Granger causality）是计量经济学标准技术的移植——novelty 在哪里？\n   - \"Detectability landscape\" 这一 framing 是否过度承诺？\n   - Design Principle 1-2 的理论深度（Jensen 不等式级别）\n   - 与 existing model collapse 文献（Shumailov, Dohmatob, Schaeffer 等）的差异化定位\n\n2. **完整性与 scope**：\n   - 实验是否全面覆盖了 \"landscape\" 的声称？\n   - Cross-architecture validation 仅 α=1.0，landscape 仅 Pythia-410M——这够吗？\n   - 与 data accumulation paradigm 的关系讨论\n   - 单一解码策略的讨论\n\n3. **写作质量**：\n   - Abstract 是否准确反映结果（注意 \"345M-6.9B\" vs 实际最大 3B）\n   - 术语一致性（Granger causality vs precedence）\n   - 方法敏感性 \"3%-92%\" 的 framing 是否误导（含失效方法 NaiveXCorr 91.7%）\n   - Figure/Table caption 信息完整性\n\n4. **格式合规**：\n   - 8 页限制（注意 Discussion 是否溢出）\n   - 匿名性\n   - Limitations section 位置和长度\n   - Abstract 是否 ≤200 words\n\n5. **Related Work 与 Missing References**：\n   - Mitchell et al. (2023) DetectGPT — AI text detection 最相关方法\n   - Runge et al. (2019) 短时间序列因果发现\n   - Padmakumar et al. (2024) LM 对文本多样性影响\n   - Steegen et al. (2016) multiverse analysis\n   - Gerstgrasser et al. (2024) data accumulation\n\n请按 ARR 标准给出完整审稿意见：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (含评分和置信度)。",
    "reviewer_id": "2",
    "project": "distrib_canary_collapse",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1053 · 2026-05-24T13:17:33.278152+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1357
}
```

</details>

---


### Assistant

_source line 1054 · 2026-05-24T13:17:47.071289+00:00_

**圆桌审稿 Round 11 已启动（Fresh 模式）**

| 组件 | 状态 |
|------|------|
| Reviewer 1（方法严谨性 + 实验验证） | ✅ 已派发 |
| Reviewer 2（新颖性 + 完整性 + 写作） | ✅ 已派发 |
| 视觉审查 Agent | ✅ 已启动（并行） |
| 外部审稿（Stanford Agentic Reviewer） | ⏭️ 未配置，跳过 |

**Venue 确认：** EMNLP 2026 via ARR，截止 2026-05-25，Long paper 8 页限制，double-blind，ACL LaTeX 模板。

等待两位 Reviewer 完成独立初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 100

## Round 100

2 recorded events


### User

_source line 1055 · 2026-05-24T13:26:22.947454+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性 + 统计验证 + 实验有效性

**论文**: "Characterizing the Detectability Landscape of Iterative Model Collapse"
**Venue**: EMNLP 2026 via ACL Rolling Review

---

## Summary

本文系统研究迭代模型坍缩（iterative model collapse）的可检测性边界：在给定合成数据污染比例 α 和观测窗口长度 T 的条件下，何时能够统计显著地检测到分布退化。主要贡献包括：(1) 以 Pythia-410M 为主架构，在 13 个污染水平 × 6 个 T 值上构建检测相图（Figure 1）；(2) 提出 PermG（置换 Granger 因果检验）作为核心检测方法，拟合幂律检测边界 α_c(T) ∝ T^{−β}；(3) 跨 5 个模型家族的交叉架构验证；(4) 证明 entropy-diversity canary 指标在时间上先于下游质量指标退化（Granger precedence）；(5) 概念验证性的 canary-triggered 干预实验。

论文附有 21 页补充材料，包括 specification curve analysis（1,160 配置）、Shapley 值分解、功率分析和模拟研究。

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 重要且新颖的研究问题，方法论有创意，但统计基础存在多处脆弱性（FPR 膨胀、低功率、有限种子数），定量结论的精度不足以支撑论文的核心声称。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 主要声称（检测随 T 改善、存在幂律边界、entropy 先于 diversity）有方向性支撑，但 FPR 膨胀（11.1% vs nominal 5%）、统计功率 CI 极宽（[0.24, 0.78]）、仅 3-4 seeds 使定量边界的精度大打折扣。Specification curve 和交叉架构验证部分弥补但未完全消解。 |
| Excitement | 3.5/5 | 可检测性景观（detectability landscape）是 model collapse 文献中的新框架，将 Granger 方法引入迭代训练、MMCT 共识检验结合 Shapley 分解具有方法论新颖性。但实际应用受限于狭窄的实验范围（单一主架构、WikiText、短序列）。 |
| Reproducibility | 4/5 | 超参数、数据集、评估流程描述详尽（Appendix A）。5,000 permutation 的稳定性已验证（Table 5）。代码未公开但方法描述足以复现。 |
| Confidence | 4/5 | 本人熟悉置换检验、多重比较校正、Granger 因果方法和实验设计。对 model collapse 特定文献的覆盖可能不完整。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] PermG 的 FPR 膨胀严重削弱检测边界的可信度

- 具体位置：Section 4.1 (p4-5), Limitations (p9), Appendix R (p22)
- 问题：论文报告 PermG 在 null 条件（α=0）下的经验 FPR 为 11.1%，95% CI [1.2%, 30.4%]，远超 nominal 5%。这意味着在检测边界附近（α≈0.45-0.50），部分"检测成功"可能是假阳性。虽然论文使用了 BH-FDR 校正并在 Limitations 中坦承此问题，但核心声称——检测从 0/8 跳至 6/8 的精确污染区间（2 个百分点内）——直接依赖于 FPR 的控制。当 FPR 可能高达 30%（CI 上界）时，这个"sharp transition"可能部分是统计伪迹。
- Appendix R 的 Shapley 分析（p22-23）表明 PermG 在方向性方法中 FPR 最低，但这是相对优势，不解决绝对 FPR 膨胀的问题。Appendix T（p22, Table 24）显示 null-control FPR 在 6-pair basis 上为 4/36 (11.1%)，而 Naive XCorr 超过 90%——PermG 确实最优，但 11.1% 仍不可接受用于精确边界估计。
- 为什么影响接收：这是论文最核心定量声称（detection boundary α_c(T)）的统计基础。如果 FPR 不可控，整个检测相图的精度存疑。
- 建议修改方向：(1) 增加 null-condition seeds（当前仅 3-4 个）以收窄 FPR 的 CI；(2) 报告 FPR-adjusted detection rates（如 Table 7 中已部分做到）；(3) 考虑用更保守的校正方法（如 Bonferroni）作为 sensitivity analysis。

**N2** [critical] 统计功率 β=0.66, CI [0.24, 0.78] 使检测边界的定量解读不可靠

- 具体位置：Limitations (p9), Appendix N (p20)
- 问题：论文报告的统计功率仅为 0.66，且 95% CI 极宽 [0.24, 0.78]。这意味着该检验在真实效应存在时，可能有 22%-76% 的概率未能检测到。当功率低至 0.24 时，检测边界 α_c(T) 会被严重高估（即真实可检测的最低 α 远低于报告值）。幂律拟合 T^{−2.08} 可能反映的不是信号特性，而是检验功率随 T 的变化。
- Appendix N (p20) 的功率分析显示：在 T≤8 时功率不足 50%，在 T=20 时也仅接近 β_50 所需的信号强度。Table 19 明确指出 "β < 2.0 under FDR correction" 且 "Dashes indicate <50% power not reached within β∈[−2, 2]"。这证实了功率严重不足。
- 为什么影响接收：如果功率不足导致检测失败被误读为"不可检测"，那么整个 detectability landscape 的形状都不可靠。论文的核心贡献——"characterizing the landscape"——的精度直接取决于功率。
- 建议修改方向：(1) 在正文中更显著地呈现功率限制对边界解读的影响（目前仅在 Limitations 一句带过）；(2) 提供功率校正后的检测边界估计；(3) 明确区分"未检测到"与"不可检测"，在讨论中充分量化功率不足可能导致的边界偏移幅度。

**N3** [critical] 幂律边界 α_c(T) ∝ T^{−2.08} 的拟合基础过于薄弱

- 具体位置：Section 4.2 (p5), Appendix S (p27), Appendix X (p6 提及)
- 问题：2 参数幂律模型（A, β）从 5 个 T 值拟合（T ∈ {5, 10, 15, 20, 25}），其中 T=10 的 sync-dip 被排除，实际有效拟合点仅 4 个（2 自由度）。LOO-CV MAE=0.037 在 4-5 个点上的信息量极为有限——任何合理的单调递减函数都能达到类似 MAE。sync-dip 的排除是事后的（post-hoc），削弱了模型选择的客观性。
- 从 Appendix S (p27) 的推导看，α_c(T) 的 T 指数为 −1/(2β_signal)，其中 β_signal 是信号模型 S(α)=c·α^β 的指数。如果 β_signal 的不确定性很大（与功率 CI 的宽度一致），那么 T 指数的不确定性也很大，可能从 −0.64 到 −2.08——这意味着检测边界的实际陡度可能比声称的平坦 3 倍。
- 论文 Section 4.2 中声称 "model comparison favors the power-probit (M2) over a linear boundary (M1) only when sync-dip data are included (ΔIC=1.15 without)"——这进一步说明模型选择依赖于被排除的数据点，证据不够稳固。
- 为什么影响接收：T^{−2.08} scaling 是论文的标志性结论（出现在 abstract 和 introduction），如果这个数字不可靠，论文的核心定量贡献被大幅削弱。
- 建议修改方向：(1) 在 T 值范围内补充更多观测点（如 T=7, 12, 18）以增加拟合自由度；(2) 报告 T 指数的完整置信区间，而非仅报告点估计；(3) 将幂律声称降级为"与幂律一致"而非"确认幂律"；(4) 提供替代函数形式的系统比较（不仅 M1 vs M2）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 交叉架构验证的 27% 失败率削弱泛化声称

- 具体位置：Table 1 (p9), Section 5.5 (p7)
- 问题：15 个模型-种子组合中 4 个未检测到 forward detection（Pythia-1.4B 两个种子均为 0/8，另有 2 个条件失败）。论文将此归因于"domain-specific mode structure affects detectability"（p7），但未提供独立证据支持这一解释。27% 的失败率意味着 PermG 的适用性受限于特定架构条件，而这些条件未被充分表征。
- Figure 10 (p30) 的交叉架构柱状图清楚展示了 Pythia-1.4B 和 SmallLM3-1B 的低检测率，但正文中"cross-architecture validation across five families (345M-6.9B) confirms this structure"（abstract, p1）的措辞过于乐观。
- 建议：(1) 在 abstract 和 introduction 中明确注明失败条件的比例和范围；(2) 分析失败条件的共同特征（模型大小？训练数据？），将"confirmation"措辞改为"partial validation with notable exceptions"。

**W2** [warning] 干预实验的证据力度极弱

- 具体位置：Section 5.5 (p7), Figure 6 (p9)
- 问题：proof-of-concept 干预仅在 α=1.0（完全合成数据）、N=2 seeds 下执行，阈值（15% entropy drop）为事后选择。"Zero false alarms"来自 2 个种子的观测，在统计上没有意义。论文虽称之为"illustrative proof-of-concept"，但仍将其列为正文贡献（Contribution list 未编号但在 p1 提及 "canary-triggered cessation reduces peak perplexity by 64%"）。
- 建议：(1) 要么扩大干预实验（多个 α 水平、更多种子、预注册阈值），要么将其完全移至 appendix 并从 contribution list 中删除；(2) 当前描述中 "reduces peak perplexity by 64%" 的精确数字在 N=2 下不应出现在 abstract 中。

**W3** [warning] Granger precedence 的混淆因素讨论不充分

- 具体位置：Section 4 (p4), Section 6 (p8), Appendix U (p24-25)
- 问题：论文正确区分了 Granger precedence 与 Granger causality（p4 脚注, p8 "temporal precedence, not true causation"），但对 bivariate confounding 的讨论不足。First-differencing 消除了共同趋势混淆，但未消除以下可能性：(a) 未测量的第三变量同时驱动 canary 和 downstream metrics；(b) entropy 对微小分布变化的测量灵敏度本身高于 diversity metrics，导致 temporal lead 仅反映测量灵敏度差异而非真正的因果先行。
- Appendix U (p24-25) 的 Channel Effect Size Analysis 表明 first-differencing 消除了 canary→perplexity 关联但保留了 canary→diversity，这是重要的诊断证据。但论文未排除 entropy 灵敏度优势这一替代解释。
- 建议：在 Discussion 中增加一段明确讨论 measurement sensitivity 差异作为替代解释的段落，并评估其对"canary as early-warning"叙事的影响。

**W4** [warning] 每个 cell 仅 8 pairs 导致二项式 CI 极宽

- 具体位置：Section 5.1 (p6), Limitations (p9)
- 问题：检测相图（Figure 1）的每个 cell 基于 8 个 canary→downstream pairs（2 canary × 4 downstream metrics）。6/8 的 Clopper-Pearson 95% CI 为 [0.25, 0.92]——论文在 Limitations 中承认了这一点。但这意味着 Figure 1 中"检测成功"（蓝色 6/8 或 5/8）与"未检测到"（白色 0/8）之间的视觉对比可能夸大了实际的统计区分度。
- 建议：(1) 在 Figure 1 中标注每个 cell 的 CI（如用颜色深浅表示置信度）；(2) 或在正文中提供一个基于 CI 的"conservative"检测相图。

---

## 小问题（不影响接收）

- **符号重用**：Limitations 中 "β=0.66, CI [0.24, 0.78]" 的 β 指统计功率，而 Section 4.2 中 β 指幂律指数。在同一论文中用相同符号表示不同概念，容易混淆。建议对功率用 1−β 或 π 等不同符号。
- **页面边界**：Table 1 和 Figure 6 作为正文内容浮动到了第 9 页（与 Limitations 同页）。严格来看这可能触及 8 页限制的边界，虽然 LaTeX float 导致的溢出通常被接受。
- **CUSUM 扩展**（Appendix H）：有趣但与正文主要贡献的连接较弱，可考虑在正文中加一句前瞻性提及。
- **Appendix E specification curve**：1,160 个规格的分析令人印象深刻，但 Figure 7 的可读性较差（密集的细线难以区分方法）。建议改为热力图或分面展示。

---

## 主要优势

1. **新颖且重要的研究问题**：model collapse 的可检测性景观是该领域的空白，本文首次系统填充了这一空白。将问题框架化为 (α, T) 二维空间中的相图，具有很强的概念清晰度。

2. **Specification curve analysis 的严谨性**：在 1,160 种分析配置下验证核心发现的鲁棒性（Appendix E, Figure 7），这在 NLP 实证研究中罕见，显著增强了结论的可信度——至少在方向性上。

3. **方法论透明度异常出色**：论文对自身统计局限的坦诚程度（FPR CI、功率不足、8-pair CI 宽度）超过了大多数同类工作。Limitations section 直接引用了 Clopper-Pearson CI 并承认"coarse topology rather than precise probability surface"。

4. **First-differencing 作为诊断工具**：发现 first-differencing 消除 canary→perplexity 但保留 canary→diversity（Section 4, p4），证明 Granger precedence 特定于 diversity channel 而非一般性趋势——这是一个有方法论价值的发现。

5. **多方法比较与 Shapley 归因**：系统比较 5 种检测方法，用 Shapley 值分解各方法对 MMCT consensus 的贡献（Appendix Q-R），为方法选择提供了有依据的指导。

6. **充实的 appendix 体系**：功率分析（N）、非平稳鲁棒性模拟（O）、specification curve（E）、Shapley 分析（Q-R）、预测-验证对比（Z）等 20+ 个附录，展示了远超平均水平的实证thoroughness。

---

## Questions for Authors

1. 如果将 null-condition seeds 增加到 10-20 个并重新估计 FPR，你们预期 FPR 的点估计会收敛到什么水平？如果收敛值仍显著高于 5%，检测边界声称是否需要根本性修改？

2. 对于 T^{−2.08} 幂律拟合，你们是否考虑过在 T 指数上报告完整的 bootstrap CI？如果 CI 覆盖了很宽的范围（如 [−0.5, −2.5]），这对论文的叙事有何影响？

3. Cross-architecture validation 中 Pythia-1.4B 的两个种子均失败（0/8），是否有证据表明这是 1.4B 规模的系统性问题而非随机变异？如果是系统性的，这对 "detection improves with model size" 的隐含假设有何影响？

4. First-differencing 消除了 canary→perplexity 关联——你们如何排除这仅仅反映 entropy 对分布微扰的测量灵敏度更高（而非真正的 temporal precedence）？

---

## 格式合规检查

- ✅ Double-blind: "Anonymous ACL submission"（p1）
- ✅ 模板: ACL LaTeX template with `[review]` option
- ⚠️ 页数: 正文文本 8 页合规，但 Table 1 和 Figure 6 浮动到第 9 页（与 Limitations 共页），属边界情况
- ✅ Limitations section 存在且覆盖 3 个核心限制点
- ✅ Abstract ≤ 200 words（目测约 150 words）
- ✅ AI assistance disclosure 存在（p29-30）



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1056 · 2026-05-24T13:26:31.907162+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成独立审稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 101

## Round 101

2 recorded events


### User

_source line 1057 · 2026-05-24T13:26:49.327754+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：Overall 3.5（Borderline Conference），Soundness 3/5，Excitement 3.5/5。

三个 Must-Fix 问题：
1. PermG 的 FPR 膨胀（11.1% vs 5% nominal，CI 上界达 30%）削弱检测边界的精度
2. 统计功率仅 0.66 且 CI 极宽 [0.24, 0.78]，使"不可检测"与"功率不足"无法区分
3. 幂律 T^{−2.08} 从 4-5 个点拟合 2 参数，拟合基础过于薄弱

四个 Should-Fix：交叉架构 27% 失败率、干预实验 N=2 证据力不足、Granger precedence 混淆讨论不充分、每 cell 8 pairs 的 CI 宽度问题。

主要优势：研究问题新颖重要、specification curve（1,160 配置）严谨、方法论透明度出色、first-differencing 诊断有方法论价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1058 · 2026-05-24T13:27:01.877393+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成审稿后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 102

## Round 102

6 recorded events


### User

_source line 1059 · 2026-05-24T13:29:18.613336+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告

## Paper Summary

本文研究迭代模型坍塌（iterative model collapse）何时以及如何能被统计检测。核心贡献是对"可检测性景观"（detectability landscape）的实证刻画——一个展示检测如何依赖于污染强度 α 和观测窗口长度 T 的相图（phase diagram）。论文在 Pythia-410M 上比较了 5 种 lead-lag 检测方法，发现 permutation Granger causality (PermG) 在灵敏度和特异性之间取得了最佳平衡。两个基于 Jensen 不等式的 Design Principles 为使用 entropy 作为 diversity collapse 的先导 canary 指标提供了形式化依据。跨架构验证在 α=1.0 下覆盖了 5 个模型族（345M–6.9B）。一个概念验证干预（canary-triggered intervention）将峰值困惑度降低了 64%。

---

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 在给定范围内实验严谨（BH-FDR 校正、5000 permutations、多种子复制、specification curve 1160 配置），但"landscape"声称与单模型证据之间存在缺口；跨架构异质性（SmallLM3 0/8, GPT-2-medium 50% null FPR）削弱了泛化性 |
| Excitement | 3.0/5 | 话题及时且有用（method comparison, canary metric），但核心方法直接移植自计量经济学未作适配，novelty 天花板有限 |
| Reproducibility | 4.0/5 | 超参数详尽（Appendix A），5000 permutations，多种子复制，specification curve 1160 配置。未提供代码但实验细节充分 |
| Confidence | 4/5 | 熟悉 model collapse 文献、Granger causality 方法体系和所用统计框架 |

---

## 总体评分

**Overall**: 3.5（Borderline Conference）

**一句话总结**: 使用标准统计工具对模型坍塌可检测性进行了扎实的实证刻画，方法敏感性发现（FPR 3%–92%）是最强贡献，但"detectability landscape"这一宏大 framing 与核心实验仅限单一模型的实际范围之间存在显著落差。

---

## 主要优势

1. **系统且严谨的实验设计**：在完全相同的数据上测试 5 种检测方法，配合严格的统计控制（BH-FDR 校正、5000 permutations、多种子复制）。null-control FPR 在方法间从 ~0% 到 ~92% 的变化是一个重要发现——它揭示了 model collapse 可检测性结论的方法依赖性，这在现有文献中被低估了。

2. **审慎的 claim 校准**：论文在 scope 控制方面做得好。Limitations 明确承认架构范围窄、统计功效有限（J=0.66）、单一解码策略。proof-of-concept 干预被恰当标注为概念验证而非成熟方案。

3. **有效的可视化**：Figure 1 的相图将 landscape 概念直观可达——颜色编码（theory vs. sync-dip vs. dissipation）清晰传达了 regime 结构。

4. **异常详尽的 appendix**（21页）：specification curve analysis（1,160 配置，Appendix E）、power analysis（Appendix N）、Shapley value 分解（Appendix P）、CUSUM 监控扩展（Appendix H）、predict-then-verify（Appendix Z）。这一级别的鲁棒性验证实质性地增强了实证声称的可信度。

5. **Canary 概念的实用价值**：entropy→diversity Granger precedence 在 14/15 实验中得到确认，提供了一个具体的监控工具。canary-triggered intervention（§5.6）展示了可操作价值。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **核心方法的 novelty 有限：直接移植自计量经济学**
- 具体位置：§4 Method, Algorithm 1 (Appendix J), §3 Design Principles
- 问题：Permutation Granger causality (PermG) 是计量经济学中的成熟技术（Granger, 1969; Toda and Yamamoto, 1995），论文将其直接应用于 model collapse 时间序列，未作方法层面的修改或适配。MMCT（Algorithm 1）是现有方法之上的简单投票程序，作者自己也承认"MMCT is a consensus testing protocol, not a novel statistical method"（Appendix J）。Design Principles 1-2 依赖 Jensen 不等式——一个基础性数学工具。整体 novelty 主要在于实证应用场景和系统比较，这限制了作为主会议论文的贡献天花板。
- 为什么影响接收：ARR 的 Excitement 维度要求工作"would mention to colleagues"或更高水平的创新贡献。纯应用性实证工作更适合 Findings 定位。
- 建议修改方向：（a）强化方法贡献：例如为短时间序列（T≤25）场景提出 PermG 的理论功效保证或适配性改进；（b）或在 framing 上更明确地将贡献定位为"empirical characterization + practical guidelines"而非方法创新。

**N2** [critical] **"Detectability landscape" framing 与证据范围之间的落差**
- 具体位置：Title, Abstract, Contribution 1
- 问题：标题声称刻画"the detectability landscape"，但完整的 landscape（α × T grid, Figure 1）仅在 Pythia-410M 上映射。跨架构验证被限制在 α=1.0——最容易检测的场景（完全合成替换）。论文无法回答 phase-diagram 结构（四个 regime、power-law boundary）是否适用于 GPT-2、Qwen 或 SmallLM3 在中间污染水平下的情况。所谓"landscape"实际上是单模型案例研究加上其他设置的抽样验证。
- 证据：§5.5 显示"At α=1.0, all 24 canary→downstream pairs reach FDR significance"，但这仅是一个操作点。Table 16（Appendix L）显示 1.4B 尺度下的 phase-diagram 结构存在架构差异。
- 为什么影响接收：标题和 abstract 的 framing 与实际证据范围之间的系统性不匹配是 soundness 问题——读者会期望"the landscape"具有跨模型的一般性。
- 建议修改方向：（a）标题和 abstract 调整为更准确反映范围，例如"Characterizing the Detectability Landscape of Iterative Model Collapse: A Case Study on Pythia-410M"；（b）或提供至少一个额外架构的完整 α × T grid（即使是缩减版）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **"3% to 92%" FPR 范围被失效方法夸大**
- 具体位置：Abstract, Contribution 3, §4.1
- 问题：Abstract 中突出展示"null-control false positive rates from 3% to 92%"。92% 来自 NaiveXCorr——该方法在 null 数据上也有 7-8/8 的显著对（Figure 11, Appendix M），本质上是一个失效的 baseline。将一个未通过基本验证的方法纳入范围计算，夸大了 method sensitivity 叙事。排除 NaiveXCorr 后的范围仍然能展示有意义的变化，但不如现在这样戏剧化。
- 建议：在报告范围时区分"通过 null 验证的方法"和"所有方法"，或至少在 abstract 中注明 92% 来自一个 baseline 方法。

**W2** [warning] **跨架构验证暴露出令人担忧的异质性**
- 具体位置：Table 1 (p.9), §5.5, Appendix L
- 问题：Table 1 显示在 α=1.0 下各架构表现差异很大：Pythia-410M 实现 4/8 或 6/8 PermG 前向检测，GPT-2-medium 为 0/8（两个种子），SmallLM3 为 0/8 或 3/8。论文讨论了 GPT-2-medium 的异常 null FPR（50%, Appendix L, p.18），但未充分解释 SmallLM3（1.7B, 一个种子 0/8）在完全污染下为何无法检测。如果 PermG 在 α=1.0 下无法可靠检测所有架构的坍塌，Pythia-410M 上导出的 landscape boundary α_c(T) 可能无法迁移。
- 建议：Discussion 中应更充分地讨论跨架构异质性对 landscape 泛化性的影响，并明确指出哪些 landscape 特征是 Pythia-specific 的。

**W3** [warning] **单一解码策略限制了 landscape 范围**
- 具体位置：Appendix A (Hyperparameters), Limitations
- 问题：所有实验使用 temperature=1.0, top-k=50。论文在 Limitations 中承认"Lower temperatures accelerate mode concentration and should left-shift the detection boundary"，但不同解码策略（nucleus sampling, beam search, 不同温度）可能从根本上改变 landscape 的结构——而不仅仅是平移。对于一篇声称刻画"the landscape"的论文，仅测试一种解码配置是显著的范围限制。
- 建议：在 Limitations 或 Discussion 中更明确地讨论解码策略可能对 landscape 结构（而非仅是边界位置）的影响。

**W4** [warning] **Table 1 和 Figure 6 浮动到第 9 页——边界页数合规性**
- 具体位置：Page 9
- 问题：Table 1（跨架构结果，在 §5.5 引用）和 Figure 6（canary 干预，在 §5.6 引用）出现在第 9 页，超出了 8 页正文限制。虽然 LaTeX 浮动位置不完全可控，但两个重要的正文内容元素同时出现在限制之外是格式问题。
- 建议：考虑将 Table 1 移至 Appendix（在正文中引用 Appendix 表格），或压缩正文腾出空间。

---

## 小问题（不影响接收）

- **Abstract 内脚注**（fn.1，定义 Granger precedence vs. causation）：在 ACL 论文的 abstract 中放脚注不常见，可能在某些索引系统（ACL Anthology, Semantic Scholar）中不能正确渲染。建议将此澄清整合到 abstract 正文中。
- **"five families" 计数**：Abstract 和 Table 1 标题都说"five families"，但 Table 1 正文列出 Pythia, GPT-2, Qwen, SmallLM3 四个，然后说"Padding-410M is a Pythia variant"。如果 Padding 是 Pythia 变体，严格来说只有 4 个独立架构族。建议明确说明。

---

## Questions for Authors

1. **NaiveXCorr 在"3%-92%"范围中的角色**：如果目的是展示合理方法间的 sensitivity，NaiveXCorr 的 ~92% FPR 说明它是一个无效方法，而非 landscape 的方法敏感性。通过基本 null 验证（FPR < 10%）的方法之间 FPR 范围是多少？

2. **能否为至少一个额外架构提供完整的 α × T grid**（例如 GPT-2 或 Qwen），以验证 phase-diagram 结构？即使是缩减版（如 5 个 α 水平 × 3 个 T 窗口）也将实质性地加强 landscape 声称。

3. **SmallLM3 在 α=1.0 下一个种子显示 0/8 检测（Table 1）**：什么解释了在完全污染下的检测失败？这反映的是 PermG 对某些架构的根本局限，还是统计功效问题？

4. **Canary 干预阈值（15%）是事后选择的**。64% 困惑度降低对此阈值有多敏感？您提到"robust band [10%, 22%]"——干预质量在此范围外是否退化？

5. **Data accumulation（Gerstgrasser et al., 2024）**：框架假设完全替换。在 data accumulation 下（各代混入真实数据），landscape 如何变化？这可以说是更现实的设置。

---

## Missing References

论文已经引用了该领域大部分关键文献。一个值得注意的缺失：

- **Runge et al. (2019)** "Detecting and quantifying causal associations in large nonlinear time series datasets." *Science Advances*. — 与论文核心技术设置（短非线性时间序列中的因果发现）直接相关。论文引用了较早的 Granger 因果文献，但未引用这项关于将因果发现扩展到短、非线性序列的较新工作。

Director 建议检查的其他文献（Mitchell et al., 2023; Padmakumar et al., 2024; Steegen et al., 2016; Gerstgrasser et al., 2024）论文均已引用。

---

## 格式合规

- **页数限制**：正文主体在第 8 页结束 ✓（但 Table 1 和 Figure 6 浮动到第 9 页——见 W4）
- **匿名性**：标注"Anonymous ACL submission"，未发现作者/机构名称 ✓
- **Abstract**：约 154 词，远低于 200 词限制 ✓
- **Limitations**：在第 9 页，适当长度（约 3 个关键点）✓
- **模板**：使用 `\usepackage[review]{acl}` ✓
- **AI 使用声明**：在第 29-30 页披露使用 Claude，透明且合规 ✓


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1060 · 2026-05-24T13:29:41.542454+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个要点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告\n\n## Overall: 3.5（Borderline Conference）\nSoundness 3.5/5, Excitement 3.0/5, Reproducibility 4.0/5, Confidence 4/5\n\n## Must-Fix 问题\n\n**N1** [critical] 核心方法的 novelty 有限：直接移植自计量经济学\n- PermG 是计量经济学成熟技术（Granger 1969; Toda-Yamamoto 1995），论文直接应用未作方法层面修改\n- MMCT（Algorithm 1）是简单投票程序，作者自己承认\"not a novel statistical method\"\n- Design Principles 1-2 依赖 Jensen 不等式——基础数学工具\n- 整体 novelty 主要在于实证应用场景和系统比较，限制了主会议论文的贡献天花板\n- 建议：强化方法贡献或更明确定位为\"empirical characterization + practical guidelines\"\n\n**N2** [critical] \"Detectability landscape\" framing 与证据范围之间的落差\n- 完整 landscape（α × T grid）仅在 Pythia-410M 上映射\n- 跨架构验证限制在 α=1.0——最容易检测的场景\n- 无法回答 phase-diagram 结构是否适用于其他架构在中间污染水平下的情况\n- 建议：标题调整为 case study，或提供额外架构完整 grid\n\n## Should-Fix 问题\n\n**W1** [warning] \"3% to 92%\" FPR 范围被失效方法 NaiveXCorr 夸大\n- 92% 来自 NaiveXCorr，本质是失效 baseline\n- 排除后范围仍有意义但不如现在戏剧化\n- 建议：区分\"通过 null 验证的方法\"和\"所有方法\"\n\n**W2** [warning] 跨架构验证暴露令人担忧的异质性\n- GPT-2-medium null FPR=50%，SmallLM3 α=1.0 下 0/8\n- Pythia-410M 上的 boundary 可能无法迁移\n- 建议：Discussion 更充分讨论跨架构异质性\n\n**W3** [warning] 单一解码策略限制 landscape 范围\n- 所有实验 temperature=1.0, top-k=50\n- 不同解码策略可能从根本上改变 landscape 结构而非仅平移\n- 建议：Discussion 更明确讨论解码策略对 landscape 结构的影响\n\n**W4** [warning] Table 1 和 Figure 6 浮动到第 9 页——页数合规性问题\n\n## 小问题\n- Abstract 脚注不常见\n- \"five families\"计数：Padding-410M 是 Pythia variant，严格只有 4 个独立族\n\n## Missing References\n- Runge et al. (2019) \"Detecting and quantifying causal associations in large nonlinear time series datasets\" — 短非线性时间序列因果发现\n\n---\n\n请逐条回应以上所有要点（Must-Fix、Should-Fix、小问题、Missing References），每条标注 [AGREE] 或 [REBUT]。",
  "reviewer_id": "1",
  "project": "distrib_canary_collapse",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个要点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告\n\n## Overall: 3.5（Borderline Conference）\nSoundness 3.5/5, Excitement 3.0/5, Reproducibility 4.0/5, Confidence 4/5\n\n## Must-Fix 问题\n\n**N1** [critical] 核心方法的 novelty 有限：直接移植自计量经济学\n- PermG 是计量经济学成熟技术（Granger 1969; Toda-Yamamoto 1995），论文直接应用未作方法层面修改\n- MMCT（Algorithm 1）是简单投票程序，作者自己承认\"not a novel statistical method\"\n- Design Principles 1-2 依赖 Jensen 不等式——基础数学工具\n- 整体 novelty 主要在于实证应用场景和系统比较，限制了主会议论文的贡献天花板\n- 建议：强化方法贡献或更明确定位为\"empirical characterization + practical guidelines\"\n\n**N2** [critical] \"Detectability landscape\" framing 与证据范围之间的落差\n- 完整 landscape（α × T grid）仅在 Pythia-410M 上映射\n- 跨架构验证限制在 α=1.0——最容易检测的场景\n- 无法回答 phase-diagram 结构是否适用于其他架构在中间污染水平下的情况\n- 建议：标题调整为 case study，或提供额外架构完整 grid\n\n## Should-Fix 问题\n\n**W1** [warning] \"3% to 92%\" FPR 范围被失效方法 NaiveXCorr 夸大\n- 92% 来自 NaiveXCorr，本质是失效 baseline\n- 排除后范围仍有意义但不如现在戏剧化\n- 建议：区分\"通过 null 验证的方法\"和\"所有方法\"\n\n**W2** [warning] 跨架构验证暴露令人担忧的异质性\n- GPT-2-medium null FPR=50%，SmallLM3 α=1.0 下 0/8\n- Pythia-410M 上的 boundary 可能无法迁移\n- 建议：Discussion 更充分讨论跨架构异质性\n\n**W3** [warning] 单一解码策略限制 landscape 范围\n- 所有实验 temperature=1.0, top-k=50\n- 不同解码策略可能从根本上改变 landscape 结构而非仅平移\n- 建议：Discussion 更明确讨论解码策略对 landscape 结构的影响\n\n**W4** [warning] Table 1 和 Figure 6 浮动到第 9 页——页数合规性问题\n\n## 小问题\n- Abstract 脚注不常见\n- \"five families\"计数：Padding-410M 是 Pythia variant，严格只有 4 个独立族\n\n## Missing References\n- Runge et al. (2019) \"Detecting and quantifying causal associations in large nonlinear time series datasets\" — 短非线性时间序列因果发现\n\n---\n\n请逐条回应以上所有要点（Must-Fix、Should-Fix、小问题、Missing References），每条标注 [AGREE] 或 [REBUT]。",
    "reviewer_id": "1",
    "project": "distrib_canary_collapse",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1061 · 2026-05-24T13:30:08.142433+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 26599
}
```

</details>

---


### Tool call

_source line 1062 · 2026-05-24T13:30:10.552539+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个要点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见\n\n## Overall: 3.5（Borderline Conference）\nSoundness 3/5, Excitement 3.5/5, Reproducibility 4/5, Confidence 4/5\n\n## Must-Fix 问题\n\n**N1** [critical] PermG 的 FPR 膨胀严重削弱检测边界的可信度\n- 经验 FPR 11.1%，CI [1.2%, 30.4%]，远超 nominal 5%\n- 检测边界附近（α≈0.45-0.50）部分\"检测成功\"可能是假阳性\n- 当 FPR 可能高达 30%（CI 上界）时\"sharp transition\"可能部分是统计伪迹\n- 建议：增加 null seeds，报告 FPR-adjusted detection rates，考虑 Bonferroni 作 sensitivity analysis\n\n**N2** [critical] 统计功率 β=0.66, CI [0.24, 0.78] 使检测边界定量解读不可靠\n- 功率低至 0.24 时检测边界 α_c(T) 会被严重高估\n- T^{-2.08} 可能反映检验功率随 T 变化而非信号特性\n- Appendix N：T≤8 时功率不足 50%\n- 建议：正文显著呈现功率限制，提供功率校正后的边界估计\n\n**N3** [critical] 幂律边界 α_c(T) ∝ T^{-2.08} 拟合基础过于薄弱\n- 5 个 T 值拟合 2 参数，排除 sync-dip 后仅 4 个有效点（2 自由度）\n- LOO-CV MAE=0.037 在 4-5 个点上信息量极有限\n- sync-dip 排除是 post-hoc，削弱模型选择客观性\n- ΔAIC=4.15 仅在包含 sync-dip 时才支持 power-probit 优于 linear\n- 建议：补充更多 T 值，报告 T 指数完整 CI，降级为\"与幂律一致\"\n\n## Should-Fix 问题\n\n**W1** [warning] 交叉架构验证 27% 失败率削弱泛化声称\n- 4/15 条件未检测到 forward detection\n- Abstract \"cross-architecture validation confirms\" 措辞过于乐观\n- 建议：明确注明失败比例，改为\"partial validation with notable exceptions\"\n\n**W2** [warning] 干预实验证据力极弱\n- α=1.0, N=2 seeds, post-hoc threshold\n- \"64% perplexity reduction\" 不应出现在 abstract\n- 建议：扩大或移至 appendix\n\n**W3** [warning] Granger precedence 混淆因素讨论不充分\n- First-differencing 消除共同趋势但未消除：(a) 未测量第三变量；(b) entropy 测量灵敏度本身高于 diversity\n- 建议：Discussion 增加 measurement sensitivity 差异作为替代解释\n\n**W4** [warning] 每 cell 8 pairs 的二项式 CI 极宽\n- 6/8 的 Clopper-Pearson 95% CI = [0.25, 0.92]\n- 检测 vs 未检测的视觉对比可能夸大统计区分度\n- 建议：Figure 1 标注 CI 或提供 conservative 检测相图\n\n## 小问题\n- β 符号重用（功率 vs 幂律指数）\n- 页面边界：Table 1 / Figure 6 浮动到第 9 页\n- Appendix E specification curve Figure 7 可读性较差\n\n---\n\n请逐条回应以上所有要点（Must-Fix、Should-Fix、小问题），每条标注 [AGREE] 或 [REBUT]。",
  "reviewer_id": "2",
  "project": "distrib_canary_collapse",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个要点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见\n\n## Overall: 3.5（Borderline Conference）\nSoundness 3/5, Excitement 3.5/5, Reproducibility 4/5, Confidence 4/5\n\n## Must-Fix 问题\n\n**N1** [critical] PermG 的 FPR 膨胀严重削弱检测边界的可信度\n- 经验 FPR 11.1%，CI [1.2%, 30.4%]，远超 nominal 5%\n- 检测边界附近（α≈0.45-0.50）部分\"检测成功\"可能是假阳性\n- 当 FPR 可能高达 30%（CI 上界）时\"sharp transition\"可能部分是统计伪迹\n- 建议：增加 null seeds，报告 FPR-adjusted detection rates，考虑 Bonferroni 作 sensitivity analysis\n\n**N2** [critical] 统计功率 β=0.66, CI [0.24, 0.78] 使检测边界定量解读不可靠\n- 功率低至 0.24 时检测边界 α_c(T) 会被严重高估\n- T^{-2.08} 可能反映检验功率随 T 变化而非信号特性\n- Appendix N：T≤8 时功率不足 50%\n- 建议：正文显著呈现功率限制，提供功率校正后的边界估计\n\n**N3** [critical] 幂律边界 α_c(T) ∝ T^{-2.08} 拟合基础过于薄弱\n- 5 个 T 值拟合 2 参数，排除 sync-dip 后仅 4 个有效点（2 自由度）\n- LOO-CV MAE=0.037 在 4-5 个点上信息量极有限\n- sync-dip 排除是 post-hoc，削弱模型选择客观性\n- ΔAIC=4.15 仅在包含 sync-dip 时才支持 power-probit 优于 linear\n- 建议：补充更多 T 值，报告 T 指数完整 CI，降级为\"与幂律一致\"\n\n## Should-Fix 问题\n\n**W1** [warning] 交叉架构验证 27% 失败率削弱泛化声称\n- 4/15 条件未检测到 forward detection\n- Abstract \"cross-architecture validation confirms\" 措辞过于乐观\n- 建议：明确注明失败比例，改为\"partial validation with notable exceptions\"\n\n**W2** [warning] 干预实验证据力极弱\n- α=1.0, N=2 seeds, post-hoc threshold\n- \"64% perplexity reduction\" 不应出现在 abstract\n- 建议：扩大或移至 appendix\n\n**W3** [warning] Granger precedence 混淆因素讨论不充分\n- First-differencing 消除共同趋势但未消除：(a) 未测量第三变量；(b) entropy 测量灵敏度本身高于 diversity\n- 建议：Discussion 增加 measurement sensitivity 差异作为替代解释\n\n**W4** [warning] 每 cell 8 pairs 的二项式 CI 极宽\n- 6/8 的 Clopper-Pearson 95% CI = [0.25, 0.92]\n- 检测 vs 未检测的视觉对比可能夸大统计区分度\n- 建议：Figure 1 标注 CI 或提供 conservative 检测相图\n\n## 小问题\n- β 符号重用（功率 vs 幂律指数）\n- 页面边界：Table 1 / Figure 6 浮动到第 9 页\n- Appendix E specification curve Figure 7 可读性较差\n\n---\n\n请逐条回应以上所有要点（Must-Fix、Should-Fix、小问题），每条标注 [AGREE] 或 [REBUT]。",
    "reviewer_id": "2",
    "project": "distrib_canary_collapse",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1063 · 2026-05-24T13:30:11.928443+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1375
}
```

</details>

---


### Assistant

_source line 1064 · 2026-05-24T13:30:15.387716+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 103

## Round 103

2 recorded events


### User

_source line 1065 · 2026-05-24T13:30:17.913153+00:00_

[Reviewer 2 审稿结果]:
审稿完成。总结：

**Overall: 3.5 (Borderline Conference)**

两个 Must-Fix 问题：
- **N1**: 核心方法（PermG）直接移植自计量经济学，无方法层面创新，novelty 天花板有限
- **N2**: "Detectability landscape" 标题/framing 与实际证据范围（仅 Pythia-410M 完整 grid）之间存在显著落差

四个 Should-Fix 问题：
- **W1**: "3%–92%" FPR 范围包含失效方法 NaiveXCorr，夸大了 method sensitivity 叙事
- **W2**: 跨架构异质性（SmallLM3 0/8, GPT-2-medium 50% null FPR）削弱泛化声称
- **W3**: 单一解码策略限制 landscape 范围
- **W4**: Table 1 和 Figure 6 浮动到第 9 页，边界页数合规

格式方面基本合规（abstract 154 词、匿名性、Limitations 位置均通过）。论文最强的贡献是方法敏感性的系统实证发现和详尽的鲁棒性验证（21 页 appendix）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1066 · 2026-05-24T13:30:25.033108+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 104

## Round 104

10 recorded events


### User

_source line 1067 · 2026-05-24T13:32:13.768615+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix 问题

### R2-N1: 核心方法 novelty 有限——直接移植自计量经济学

[REBUT] 部分不同意。R2 的事实判断正确（PermG 源自 Granger 1969，MMCT 是投票程序），但对贡献类型的评价标准有偏差。

**理由：**

1. **论文的定位本就是 empirical characterization，不是方法创新。** 论文标题"Characterizing the Detectability Landscape"明确了其贡献类型。在 NLP/ML 顶会中，将成熟统计方法系统应用于新领域的实证工作（如 specification curve analysis 在心理学中的应用后被引入 NLP）是被接受的贡献模式。

2. **方法组合的 integration 本身有价值。** 论文不是简单地跑一个 Granger test——它将 PermG + first-differencing + BH-FDR correction + MMCT consensus + Shapley 值分解 + specification curve analysis（1,160 specs, Appendix E）整合为一个诊断框架。这个 pipeline 的设计（特别是 first-differencing 作为 trend vs. genuine precedence 的诊断，Section 4 p4）对 model collapse 领域有方法论贡献。

3. **但 R2 关于 contribution 天花板的担忧部分成立。** 如果论文的定量结论不够稳健（参见我的 N1-N3），那么剩余贡献确实主要是实证性的。我的建议是：与其争论 novelty，不如加固统计基础——如果检测边界和 Granger precedence 的证据更加稳健，empirical contribution 的价值自然提升。

4. **Design Principles 1-2 的 Jensen 不等式论证确实不构成理论贡献**——这点我同意 R2。但它们作为实验设计的 motivation 是合理的。

**结论：** R2 对方法 novelty 的评估过于严格。将成熟方法引入新领域并系统验证，在 Findings 级别（甚至 borderline conference）是合理的贡献。但如果定量结论不稳健，这个贡献确实不足以支撑主会议。

---

### R2-N2: "Detectability landscape" framing 与证据范围的落差

[AGREE] R2-N2: 同意这是一个真实的 framing gap。

**理由：**

1. **完整 α×T grid 仅在 Pythia-410M 上。** Table 1 (p9) 确认跨架构验证限于 α=1.0 和 null (α=0) 两个极端条件。论文无法回答：GPT-2-medium 或 Qwen 在 α=0.25-0.50 范围内是否展现相同的 phase-diagram 结构。

2. **这与我的 W1 一致。** 我在初审中指出 27% 的跨架构失败率（4/15）削弱了泛化声称。R2 将这个问题上升到 framing 层面，我认为是合理的。

3. **但 "case study" 标签可能过度贬低。** 论文确实提供了 15 个跨架构条件、1,160 个 specification curve 配置（Appendix E）、以及理论 motivation（Design Principles 1-2）。这超出了典型 case study 的范围。更合理的修改是：将标题/abstract 中的 "characterize" 限定为 "characterize... on Pythia-410M with cross-architecture probes"，在 Discussion 中明确哪些结论可能泛化（定性结构：entropy leads diversity）、哪些不一定（定量边界 α_c(T)）。

4. **Limitations (p9) 已部分承认**："Our landscape characterization uses Pythia-410M as the primary architecture; the phase diagram for Pythia-family-only (410M and 1.4B) is untested."——但 abstract 和 introduction 的措辞仍然过于宽泛。

---

## Should-Fix 问题

### R2-W1: "3% to 92%" FPR 范围被 NaiveXCorr 夸大

[AGREE] R2-W1: 完全同意。

**理由：**

Abstract (p1) 写 "Five methods applied to identical data yield null-control false positive rates from 3% to 92%"——92% 来自 NaiveXCorr，本质上是一个不做任何校正的 baseline（naive cross-correlation）。将一个已知失效的 baseline 的 FPR 纳入范围描述，确实在修辞上夸大了方法选择的影响。

更诚实的表述应该是："Among the four methods that passed null validation, FPR ranges from 3% to 39%"或类似措辞，将 NaiveXCorr 明确标注为 failed baseline。这与论文 Section 4.1 (p4) 的实际分析一致——论文已经将 NaiveXCorr 识别为 FPR 最高的方法，但 abstract 的表述未做此区分。

---

### R2-W2: 跨架构验证暴露令人担忧的异质性

[AGREE] R2-W2: 同意，这与我的 W1 高度一致。

**补充发现：**

R2 提到 GPT-2-medium null FPR=50%——我确认这来自 Table 1 (p9)，GPT-2-medium 在 null 条件下 PermG forward 为 0/8 但论文其他位置提到 GPT-2-medium 的结果不一致。更关键的是 Pythia-1.4B 两个种子均为 0/8 forward detection（Table 1），以及 SmallLM3-1B 在 α=1.0 下仅 3/8。

这三个失败模式覆盖了不同的架构规模和家族，说明失败不是随机变异——可能存在系统性的架构敏感性。论文 Discussion (p8) 仅用一句 "domain-specific mode structure" 带过，未提供独立证据。

---

### R2-W3: 单一解码策略限制 landscape 范围

[REBUT] 部分不同意——这是合理的 scope limitation。

**理由：**

1. **Limitations (p9) 已明确承认**："All experiments use a single decoding strategy (temperature 1.0, top-k≤50). Lower temperatures accelerate mode concentration and should left-shift the detection boundary."论文不仅承认了这一限制，还给出了定性预测（low temperature → 更容易检测）。

2. **解码策略的系统探索是另一篇论文的工作量。** 每增加一个解码设置（temperature × top-k × top-p），就需要完整的 α×T grid 实验——在当前实验规模下（每个 grid 需要约 60 个独立训练 run），这不是一个合理的 revision 要求。

3. **但 R2 关于"结构性改变 vs 平移"的观点是对的。** 论文说 "should left-shift"（暗示平移），但没有证据排除解码策略改变 landscape 的拓扑结构（如消除 sync-dip 或改变 phase transition 的陡度）。Discussion 可以加一句定性讨论。

**结论：** 作为 limitation 已充分承认；作为 should-fix 要求过高。建议在 Discussion 中补充一句关于结构性改变可能性的 caveat。

---

### R2-W4: Table 1 和 Figure 6 浮动到第 9 页

[AGREE] R2-W4: 同意，与我在小问题中的观察一致。

Table 1 和 Figure 6 是正文内容（分别从 Section 5.5 p7 和 Section 5.5 p7 引用），但浮动到了 Limitations 所在的第 9 页。严格来说这触及 8 页限制。实际操作中，LaTeX float 溢出通常被 reviewers 接受，但作者应尝试将这些元素调整回第 8 页内，或将部分内容移至 appendix。

---

## 小问题

### Abstract 脚注

[AGREE] 同意这不常见。Abstract 中的脚注（p1 脚注 1: "Granger precedence establishes temporal predictive improvement, not true causation"）虽然内容重要，但放在 abstract 中在格式上不标准。建议移至 Introduction 首次提及 Granger 时。

---

### "Five families" 计数——Padding-410M 是 Pythia variant

[AGREE] 同意。Table 1 (p9) 脚注明确标注 "Padding-410M is a Pythia variant"。将同一架构的 padding 变体计为独立家族确实夸大了交叉架构验证的范围。严格来说是 4 个独立家族（Pythia, GPT-2, Qwen, SmallLM3）+ 1 个 Pythia 变体。Abstract 和正文中 "five families" 的表述应修改为 "four families plus one architectural variant" 或类似措辞。

这进一步加强了 R2-N2 和我的 W1 的观点：跨架构验证的实际覆盖范围比论文声称的更窄。

---

## Missing References

### Runge et al. (2019) "Detecting and quantifying causal associations in large nonlinear time series datasets"

[AGREE] 同意应引用。该论文（发表于 Science Advances）提出了 PCMCI 算法用于短非线性时间序列的因果发现，直接相关于本文面临的方法论挑战：短序列（T=5-25）中的因果推断。论文 Related Work (p2-3) 讨论了 Granger 方法和 Toda-Yamamoto，但未覆盖非线性因果发现方法。引用 Runge et al. 可以：(1) 更全面地定位方法选择；(2) 讨论为何选择线性 Granger 而非 PCMCI 等非线性替代方案。

---

## 总结

在 R2 的 2 个 Must-Fix 中，我 REBUT 了 N1（novelty 评价过严，但部分成立）、AGREE 了 N2（framing gap 真实存在）。在 4 个 Should-Fix 中，我 AGREE 了 W1、W2、W4，REBUT 了 W3（合理的 scope limitation，但可加 caveat）。小问题和 missing reference 全部 AGREE。

R2 的审稿整体质量高，与我的审查在跨架构异质性（R2-W2 ≈ 我的 W1）和页面合规（R2-W4 ≈ 我的小问题）上高度一致。主要分歧在于 novelty 评价——我认为 empirical characterization 在这个领域足以支撑 borderline conference，前提是定量结论被加固。


---

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应：Reviewer 1 审稿意见

---

## Must-Fix 问题

### [AGREE] R1-N1: PermG 的 FPR 膨胀严重削弱检测边界的可信度

同意这是一个实质性问题。pooled FPR 11.1%（4/36）配合 CI [1.2%, 30.4%] 确实令人担忧，特别是在检测边界附近（α≈0.45-0.50），假阳性和真阳性的区分变得困难。

但需要补充一点 nuance：论文报告的"sharp transition"是从 0/8 跳到 6/8（即从 0% 到 75% 检测率），这一跳跃幅度很难完全用 11% FPR 解释。即使 FPR 真实值在 CI 上界 30%，从 0 到 6 的跳跃仍然意味着至少一部分检测是真实信号。然而，R1 的核心论点成立——在不进行 FPR 校正的情况下，我们无法量化这一跳跃中有多少比例来自真实信号 vs 假阳性膨胀。

R1 建议的"报告 FPR-adjusted detection rates"是合理且可操作的。

### [AGREE] R1-N2: 统计功率 β=0.66 使检测边界定量解读不可靠

同意。这是我在自己的审稿中未充分强调的一个重要问题。R1 的关键洞察是：T^{-2.08} 指数可能反映的是*检验功率随 T 衰减*而非*信号的物理特性*。论文 Appendix N 已经表明 T≤8 时功率不足 50%（Table 19, p.20），这直接意味着短观测窗口下的"未检测"可能是 Type II error 而非真正的零信号。

论文确实在 Limitations（p.9）中承认了功率限制（"statistical power remains limited, J=0.66"），但 R1 说得对——这个限制应在正文中更显著地呈现，因为它直接影响对 α_c(T) 曲线的解读。功率校正后的边界估计将使读者能区分"未检测到信号"和"检验力不足以检测"。

### [AGREE] R1-N3: 幂律边界拟合基础过于薄弱

同意，但需要分级讨论。

R1 的核心论点（5 个 T 值拟合 2 参数 → 2 自由度 → 过拟合风险）是统计学上成立的。sync-dip 排除使有效点减至 4 个更加剧了这一问题。LOO-CV MAE=0.037 在 4-5 个点上的确信息量有限——任何足够灵活的 2 参数模型都可能在 4 个点上达到类似的 LOO-CV 表现。

然而，我认为论文有几个 mitigating factor R1 未充分考虑：
1. 论文提供了 probit 对比 linear 的 ΔAIC 分析（§5.3, p.6-7），这至少是在尝试模型选择而非盲目拟合
2. 15/15 within CI 的 LOO 结果意味着模型没有系统性偏差的迹象
3. Appendix N 的 power analysis（Table 19-20）提供了*独立于拟合的*理论预测（√T scaling），与经验指数方向一致

尽管如此，R1 建议降级为"consistent with a power law"是审慎的。2 自由度不足以区分 power law、exponential 或其他函数形式。

---

## Should-Fix 问题

### [AGREE] R1-W1: 跨架构 27% 失败率削弱泛化声称

完全同意。这与我自己的 W2 问题一致。4/15 条件未检测到 forward detection，Abstract 中"cross-architecture validation confirms"的措辞确实过于乐观。R1 建议改为"partial validation with notable exceptions"更准确反映证据。

补充我自己的发现：SmallLM3 在 α=1.0 下一个种子 0/8 检测特别令人担忧——在完全合成替换下仍无法检测，暗示 landscape 结构可能在某些架构上根本不同，而非仅仅是边界位移。

### [REBUT] R1-W2: 干预实验证据力极弱，"64%" 不应出现在 abstract

部分反驳。R1 对证据力的评估（α=1.0, N=2, post-hoc）是准确的。但论文在 §5.6 中将此明确标注为"illustrative proof-of-concept"（p.7），而 abstract 中的措辞是"providing a canary whose triggered cessation reduces peak perplexity by 64%"——读者可以从上下文判断这是 canary 概念的证据，而非一个工程化的成熟方案。

然而，R1 说得对，abstract 中的具体数字"64%"赋予了这个结果过多的权重。在仅 2 个种子的情况下，64% 这个精确数字的可信区间极宽。**我同意应将 64% 从 abstract 中移除或替换为定性描述**（如"substantially reduces peak perplexity"），同时保留 §5.6 中的详细定量描述。

所以这是一个 partial agree：核心 framing（proof-of-concept）可以保留在 abstract 中，但具体数字应弱化。

### [REBUT] R1-W3: Granger precedence 混淆因素讨论不充分

反驳。论文的 Discussion（§6, p.8）已经直接讨论了 R1 提出的 measurement sensitivity 替代解释。原文："Entropy's greater sensitivity to distributional shifts than n-gram diversity means the temporal lead may partly reflect measurement sensitivity."（§6, 右栏）。论文进一步讨论了这一点，指出"five sync-dip cells are excluded from the boundary fit; including them raises MAE to 0.203"（Appendix L, p.18），暗示 entropy 和 diversity 的测量特性差异确实会影响结果。

对于 R1 提到的"未测量第三变量"：论文的 first-differencing 处理消除了共同线性趋势（§4, p.4："first-differencing eliminates canary→perplexity associations (F=0.6, p=0.59) while preserving canary→diversity"）。Appendix U（Channel Effect Size Analysis, p.24-25）进一步分析了 first-differencing 后的 correlation retention 和 temporal structure。

我认为论文已经对这个问题进行了合理程度的讨论。当然，作为因果推断文献的标准，对所有可能混淆因素的详尽讨论永远可以更多，但在 8 页正文限制内，现有讨论是充分的。

### [AGREE] R1-W4: 每 cell 8 pairs 的二项式 CI 极宽

同意。这与我对论文的整体观察一致。论文在 Limitations（p.9）中明确承认了这一点："Each cell's detection rate (e.g., 6/8) carries a wide bootstrap confidence interval (Cooper-Pearson: 0.25, 0.92 for 6/8); the phase diagram should be read as a coarse topology rather than a precise probability surface."

R1 的建议（Figure 1 标注 CI）是建设性的且可操作。Phase diagram 的视觉设计目前用 color-coding 区分"检测/未检测"，这种二值化呈现确实可能夸大统计区分度。标注 CI 或使用连续色阶（如按检测概率的点估计+不确定性着色）将更准确地传达信息。

---

## 小问题

### [AGREE] β 符号重用
同意这是一个排版问题。统计功率通常用 1-β 表示，如果论文中其他地方也使用了 β（如回归系数），应使用不同符号以避免混淆。

### [AGREE] Table 1 / Figure 6 浮动到第 9 页
同意，与我的 W4 一致。两个主要的正文元素同时浮动到页数限制之外是格式问题。

### [AGREE] Figure 7 specification curve 可读性
同意。1,160 个配置的 specification curve（Appendix E, p.15）在当前分辨率下确实难以辨别单个数据点。但考虑到这是 Appendix 中的补充分析，可读性问题的严重程度低于主文 Figure。

---

## 总结

R1 的审稿整体质量高，特别是在统计方法论方面的深入分析（N1-N3）超过了我的审查深度。我的主要分歧在于：

1. **W3（Granger precedence 混淆因素）**：论文已在 §6 中讨论了 measurement sensitivity 替代解释，R1 可能未充分注意到该段落。
2. **W2（干预实验）**：partial agree——同意 abstract 中不应出现精确数字"64%"，但 proof-of-concept framing 本身可以保留。

在 Overall Assessment 上我与 R1 一致（3.5, Borderline Conference），但我们的侧重不同：R1 更关注统计方法论的内部效度，我更关注 novelty/framing 与证据范围的匹配。两个视角的综合指向同一结论——这是一篇扎实但 scope/framing 需要调整的论文，定位在 Findings 和 Conference 之间。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1068 · 2026-05-24T13:32:46.611534+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1069 · 2026-05-24T13:32:46.812721+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T13:16:58.998064+00:00\", \"completed_at\": \"2026-05-24T13:21:47.214210+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 6-7\", \"message\": \"实验章节（§5.1–§5.5）连续 2 页纯文本无任何 display item，结果讨论与支撑图表（Figures 3-5）分离。审稿人在这两页会失去视觉锚点。建议将至少 1 个 figure（如 Figure 3 或 Figure 4）提前到 page 6 或 7。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figures 3、4、5 三图堆叠在同一页，每图仅占约 1/3 页高度，图内文字（axis labels、legend）偏小（接近正文字号 60-65%），在打印或低分辨率屏幕上可能影响可读性。建议拆分至 2 页或将其中 1-2 个上移至 pages 6-7。\"}, {\"severity\": \"warning\", \"dimension\": \"page 9\", \"message\": \"Table 1 和 Figure 6 作为主文 display items 浮动到第 9 页（超出 8 页主文边界）。虽然 Limitations 和 References 不计入页数限制，但浮动体位于 Limitations 同页可能引起审稿人对页数合规性的疑虑。建议通过调整 float placement 或压缩前文空间将两者拉回 page 8。\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-2\", \"message\": \"前 2 页为纯文本（Introduction + Related Work），无 display item。Figure 1 在 page 3 顶部出现，符合\\\"前 3 页内有视觉锚点\\\"的建议。如能将一个概念图或 teaser figure 提前到 page 1 底部则更佳。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figures 3-5 的图内 tick labels 和 legend 字号约为正文的 60-65%，刚好在可读性边界。若调整布局释放空间，可适当放大。\"}, {\"severity\": \"info\", \"dimension\": \"page 30\", \"message\": \"最后一页（appendix）底部约 35% 为空白（AI Assistants 声明后），appendix 页面不影响主文评价。\"}], \"counts\": {\"critical\": 0, \"warning\": 3, \"info\": 3}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1070 · 2026-05-24T13:32:46.813214+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1071 · 2026-05-24T13:32:46.913972+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1072 · 2026-05-24T13:36:17.252894+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distrib_canary_collapse",
  "issues_yaml": "issues:\n# ============================================================\n# Round 1-10 历史 resolved — 保留跨轮次记录\n# ============================================================\n- id: \"R1-N1\"\n  summary: \"Ground-truth pairs 定义存在循环论证\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Effect-size GT 重定义完成。\"\n  resolution_round: 1\n\n- id: \"R1-N2\"\n  summary: \"FPR=0% 标定仅基于单 seed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"α=0.0 三 seed FPR 验证完成。\"\n  resolution_round: 1\n\n- id: \"R1-N3\"\n  summary: \"α=0.50 和 α=0.75 仅 1 seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Multi-seed 补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-N1\"\n  summary: \"核心方法论为计量经济学已有知识的直接迁移，新颖性有限\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Round 1 三层定位 reframe 完成。\"\n  resolution_round: 1\n\n- id: \"R2-N2\"\n  summary: \"α=0.75 multi-seed 实验未完成 + Appendix A 缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-N3\"\n  summary: \"实验规模过窄\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"跨架构验证已扩展至 15 model-seed 组合。\"\n  resolution_round: 1\n\n- id: \"R1-W1\"\n  summary: \"Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"核心修复完成。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"PermG 缺少 power analysis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Appendix N power analysis 完成。\"\n  resolution_round: 1\n\n- id: \"R1-W3\"\n  summary: \"75% spurious-signal rate headline 依赖 underpowered T-Y\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W4\"\n  summary: \"α=0.75 单 seed borderline 结果不应出现在 abstract\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W5\"\n  summary: \"Toda-Yamamoto 纳入理由表述不充分\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W6\"\n  summary: \"可重复性信息不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"超参补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-W3\"\n  summary: \"Token entropy canary 仅在 α=1.0 验证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"缺少独立 Limitations section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W5\"\n  summary: \"缺少 AI Writing Disclosure\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W6\"\n  summary: \"缺少 canary→perplexity 为何 spurious 的深入解释\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF1\"\n  summary: \"遗漏 Granger & Newbold (1974)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF2\"\n  summary: \"遗漏 Hataya et al. (2023) 和 Seddik et al. (2024)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W1-old\"\n  summary: \"Citation key chen2025scales 与实际作者不匹配\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"F2-W3\"\n  summary: \"Section 3 承诺的三项附录内容缺失\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"附录内容补充完成。\"\n  resolution_round: 3\n\n- id: \"F2-W8\"\n  summary: \"格式不合规：未使用 ACL 模板\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"ACL 模板迁移完成。\"\n  resolution_round: 2\n\n- id: \"F2-REF1\"\n  summary: \"遗漏 arXiv:2502.15654\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF1\"\n  summary: \"遗漏 arXiv:2602.10531\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF2\"\n  summary: \"遗漏 arXiv:2505.19046\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF3\"\n  summary: \"遗漏 arXiv:2510.16657\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF5\"\n  summary: \"Appendix H CUSUM 未引用 Page (1954)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F4-REF1\"\n  summary: \"遗漏 Truong & Truong (2026)\"\n  category: reference\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"引用已添加并在 §1/§2 讨论。\"\n  resolution_round: 6\n\n- id: \"F4-REF3\"\n  summary: \"遗漏 Benjamini & Yekutieli (2001)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"§4 现引用 benjamini2001control。\"\n  resolution_round: 5\n\n- id: \"F2-REF3\"\n  summary: \"Dakos et al. (2012) + Schreiber (2000) + Phipson & Smyth (2010) 在 bib 中但正文未引用\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"引用补充完成。\"\n  resolution_round: 4\n\n- id: \"F6-W2\"\n  summary: \"页数可能超限\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"R8 PDF 审查确认主体 8 页合规。\"\n  resolution_round: 8\n\n- id: \"F2-W6b\"\n  summary: \"'Methodological pitfalls' 有 straw-man 倾向\"\n  category: framing\n  severity: major\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 8\n  resolution: \"全文已改为 'design considerations'。R8 fresh review 未再提及。\"\n  resolution_round: 8\n\n- id: \"F5-N2\"\n  summary: \"T=10 统计效力不足(power≈37%), sharp onset 可能是 power artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Power simulation 重写通过 Reviewer #75。Steepness comparison k_obs=18.79 vs k_H0=6.14 (ratio 3.06×, CI non-overlapping) 写入 method.tex + experiments.tex + appendix。Dense α 证据 (17 points, sigmoid k=15.7) 额外支撑。\"\n  resolution_round: 9\n  first_raised_round: 5\n  last_seen_round: 9\n\n- id: \"F2-W5\"\n  summary: \"Token entropy → distinct-n 机械耦合 confound 未排除\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Metric structure 分析完成：mauve attribution 100% 确认非 metric coupling。ECE→distinct 独立于 token_entropy→distinct 路径。讨论已添加到 discussion.tex。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 9\n\n- id: \"F2-W2\"\n  summary: \"Specification curve analysis 定位不精确\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Appendix E 已改称 'systematic robustness analysis'。R8/R9 fresh review 未再提及。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 8\n\n- id: \"F8-C2\"\n  summary: \"Discussion §6 过于简短(~100词)\"\n  category: writing\n  severity: major\n  status: resolved\n  resolution: \"Discussion 扩展至 20 行（metric-specific ceiling + practical implications + domain-dependent directionality）。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C3\"\n  summary: \"与 Schaeffer et al. (2025) '8 种 collapse 定义' 的关系讨论不充分\"\n  category: framing\n  severity: major\n  status: resolved\n  resolution: \"Schaeffer taxonomy 映射已添加到 related_work.tex L5-6。检测框架显式对应 distributional shift 定义 (D4-D6)。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C1\"\n  summary: \"Du & Tanaka-Ishii (2026) 引用三重错误：arXiv ID、标题、研究对象\"\n  category: reference\n  severity: critical\n  status: resolved\n  resolution: \"§2 已修正为 'related but distinct phenomenon'。R9 fresh review 未再提及。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"R9-C1\"\n  summary: \"FPR CI method.tex 内部矛盾：L16 [0,0] vs L24 [0%,41%]\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"FPR=10% MMCT sensitivity analysis 完成。K≥3 不受影响。Paper Agent 统一 CI 处理。\"\n  resolution_round: 9\n  first_raised_round: 9\n  last_seen_round: 9\n\n- id: \"F8-N1\"\n  summary: \"BH-FDR 在强正回归依赖下适用性讨论不充分\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"跨 pair correlation 结构报告在 method.tex。PRDS 假设适用性讨论已添加。FPR sensitivity analysis 额外支撑。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 10\n\n- id: \"F8-REF1\"\n  summary: \"遗漏引用：online/continual learning 下 model collapse 检测\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"related_work.tex 已添加 scope 区分（iterative from-scratch vs continual learning）。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F2-W11\"\n  summary: \"α_c SE=0.006 低估真实 seed 不确定性\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"被 F2-W4b/F2-W6 的统计基础问题覆盖，单独不再追踪。\"\n  resolution_round: 11\n  first_raised_round: 2\n  last_seen_round: 10\n\n# ============================================================\n# 活跃 issues — Round 11 Fresh Review 更新\n# ============================================================\n\n- id: \"F3-J4\"\n  summary: \"PermG FPR 超出 nominal 5%，architecture-dependent\"\n  category: method\n  severity: critical\n  status: open\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 3\n  last_seen_round: 11\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 双方最高优先级共识。FPR=11.1% CI [1.2%,30.4%] 使 detection boundary 附近结论不可靠。GPT-2 medium FPR=50% 说明 architecture-dependent。建议：增加 null seeds、报告 FPR-adjusted rates、Bonferroni sensitivity。\"\n\n- id: \"F2-W4b\"\n  summary: \"Proposition 3 本质是 curve fitting / empirical scaling，非理论推导\"\n  category: framing\n  severity: critical\n  status: open\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 11\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11: 5T 拟合 2 参数仅 2-3 DF。LOO-CV MAE=0.037 在 4-5 点上信息量极有限。sync-dip 排除 post-hoc。ΔAIC=4.15 仅含 sync-dip 时支持 power-probit。R2 补充 mitigating factors (ΔAIC analysis, 15/15 within CI) 但同意降级为 'consistent with power law'。交叉共识：AGREE。\"\n\n- id: \"F2-W2b\"\n  summary: \"'Detectability landscape' framing 承诺超过交付\"\n  category: framing\n  severity: critical\n  status: open\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 11\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11: 完整 α×T grid 仅 Pythia-410M。跨架构仅 α=1.0（最容易检测）。无法回答其他架构中间 α 水平的 phase-diagram 结构。R1 同意但反对'case study'标签——建议限定 scope 而非降级标题。交叉共识：AGREE（framing gap 真实存在）。\"\n\n- id: \"F2-W1\"\n  summary: \"α=0.60 sync dip：precision sensitivity (bf16 0/8 vs fp32 6/8)\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 3\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: []\n      note: \"R11 未单独提及 sync-dip 作为独立问题，但被 F2-W4b (power law fit) 中 sync-dip 排除的 post-hoc 性覆盖。\"\n\n- id: \"F2-W10\"\n  summary: \"Cross-architecture 'coupling preserved' 条件 post-hoc 循环论证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 11\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11: 27% failure rate (4/15)。SmolLM3-3B 在 α=1.0 下仅 3/8。GPT-2-medium null FPR=50%。Abstract 'confirms' 措辞过于乐观。R1/R2 一致建议改为 'partial validation with notable exceptions'。交叉共识：AGREE。\"\n\n- id: \"F2-W6\"\n  summary: \"Detection boundary 验证不足 (2T 拟合 2 参数=零自由度)\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 11\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"与 F2-W4b 合并。R11 R1 提议补充 T=7/12/18 增加自由度。R2 同意方向但认为 mitigating factors 存在。交叉共识：AGREE 需降级声称。\"\n\n- id: \"F2-W7\"\n  summary: \"Intervention 实验薄弱：post hoc threshold, n=2, 仅 α=1.0, CI 29-64%\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 11\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11: R1 要求移除 abstract 中 '64%'。R2 partial REBUT——proof-of-concept framing 可保留，但精确数字在 N=2 下不可信。共识：abstract 中用定性描述替代 '64%'，§5.6 保留详细数据。\"\n\n- id: \"F5-N1\"\n  summary: \"核心方法是计量经济学标准技术的直接移植，贡献定位不清\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 11\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 R2 再次标为 must-fix (novelty ceiling)。R1 partial REBUT：empirical characterization 是合理贡献模式，pipeline integration (PermG + first-diff + BH-FDR + MMCT + Shapley + spec curve) 有方法论价值。但同意 Design Principles 1-2 不构成理论贡献。分歧：R2 认为 novelty 不足以支撑 main conference，R1 认为在 Findings-borderline Conference 范围合理。\"\n\n- id: \"F5-W1\"\n  summary: \"Proposition 1 数学深度有限，仅 Jensen 不等式\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 11\n  mentions:\n    - round: 5\n      reviewers: [2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 双方同意 Design Principles 不构成理论贡献，但作为实验设计 motivation 合理。\"\n\n- id: \"R11-N1\"\n  summary: \"统计功率 β=0.66 CI [0.24,0.78] 使检测边界定量解读不可靠\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 首次以 must-fix 提出。功率低至 0.24 时 α_c(T) 会被严重高估。T^{-2.08} 可能反映功率变化而非信号特性。R2 AGREE：Appendix N 确认 T≤8 功率不足 50%。共识：正文应更显著呈现功率限制对边界解读的影响，区分'未检测到'与'不可检测'。\"\n\n- id: \"R11-W1\"\n  summary: \"'3%-92%' FPR 范围含失效方法 NaiveXCorr，abstract framing 夸大\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"92% 来自 NaiveXCorr（本质失效 baseline）。排除后合格方法范围为 3%-39%。Abstract 应区分通过 null 验证的方法和所有方法。交叉共识：AGREE。\"\n\n- id: \"R11-W2\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽 [0.25, 0.92]\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"6/8 Clopper-Pearson CI = [0.25, 0.92]。相邻 cell 差异可能不显著。Figure 1 的二值化呈现可能夸大统计区分度。建议标注 CI 或用连续色阶。交叉共识：AGREE。Limitations 已承认但正文视觉呈现未反映。\"\n\n- id: \"R9-m5\"\n  summary: \"Granger 'precedence' vs 'causality' 术语不一致\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: []\n      note: \"R11 未单独提及。R2 在交叉回应中引用 §6 已有讨论。可能已充分处理。\"\n\n- id: \"R9-REF1\"\n  summary: \"遗漏引用：Gerstgrasser et al. (2024) data accumulation vs replacement\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 9\n      reviewers: [2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: []\n      note: \"R11 未单独提及。论文 §2 已引用 dey2024breaking，但 Gerstgrasser 作为 accumulation paradigm 的核心参考仍建议补充。\"\n\n- id: \"R9-REF2\"\n  summary: \"遗漏引用：Steegen et al. (2016) multiverse analysis\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 (related_work.tex L29) 已引用 steegen2016increasing。\"\n  resolution_round: 11\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 9\n      reviewers: [2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [2]\n      note: \"R11 R2 在 missing references 中确认论文已引用。\"\n\n- id: \"R10-MF5\"\n  summary: \"'Five families (345M-6.9B)' 数字自洽性错误\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 双方再次确认。Padding-410M 是 Pythia variant，严格仅 4 独立族。'345M-6.9B' 与最大 3B 不符。交叉共识：AGREE。\"\n\n- id: \"R10-SF2\"\n  summary: \"Data accumulation vs replacement paradigm 未讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 R2 在 Questions 中再次提出。Limitations 已承认 'full replacement' 但未讨论 accumulation 下 landscape 预期变化。\"\n\n- id: \"R10-SF3\"\n  summary: \"单一解码策略 (temperature 1.0/top-k=50) 需定性讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 R2 提为 should-fix，R1 REBUT（已在 Limitations 承认，属合理 scope limitation）。共识：不需额外实验，但 Discussion 可加 1 句关于结构性改变可能性的 caveat。\"\n\n- id: \"R10-SF4\"\n  summary: \"方法敏感性 '3%-92%' framing 混淆失效方法与真正 sensitivity\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"与 R11-W1 合并。交叉共识：AGREE。\"\n\n- id: \"R10-SF6\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"与 R11-W2 合并。交叉共识：AGREE。\"\n\n- id: \"R10-m1\"\n  summary: \"Figure 3 y 轴标签 'FDR-significant pairs' 含义不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及。\"\n\n- id: \"R10-m2\"\n  summary: \"Table 2 'x/8' 列含义未在 caption 定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及。\"\n\n- id: \"R10-m3\"\n  summary: \"§5.1 '(§5.5)' 前向引用缺上下文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及。\"\n\n- id: \"R10-REF3\"\n  summary: \"遗漏引用：Runge et al. (2019) 短时间序列因果发现\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 R2 再次在 Missing References 中提出。R1 AGREE。PCMCI 算法与本文 T≤25 短序列因果推断直接相关。\"\n\n- id: \"R10-VIS1\"\n  summary: \"Discussion §6 溢出到第 9 页，可能违反 EMNLP 2026 八页主文限制\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [visual_check]\n    - round: 11\n      reviewers: [1, 2, visual_check]\n      note: \"R11 视觉审查确认：Table 1 和 Figure 6 浮动到第 9 页。R1/R2 交叉共识：AGREE，属格式边界问题。建议调整 float placement 或压缩正文。\"\n\n- id: \"R11-VIS2\"\n  summary: \"Pages 6-7 连续纯文本无 display item，图表堆叠在 page 8\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [visual_check]\n      note: \"Figures 3/4/5 三图堆叠在 page 8，每图仅 1/3 页高度。Pages 6-7 纯文本。建议至少 1 图上移至 page 6-7 改善视觉节奏。\"\n\n- id: \"F8-W2\"\n  summary: \"Figure 1/2 子图内文字偏小，Figure 2 灰度打印难区分\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 8\n      reviewers: [2, visual_check]\n    - round: 10\n      reviewers: [visual_check]\n    - round: 11\n      reviewers: [visual_check]\n      note: \"R11 视觉审查确认：Figures 3-5 tick labels/legend 字号约正文 60-65%，在可读性边界。\"\n\n- id: \"F4-REF5\"\n  summary: \"bib first author mismatch: dey2024breaking 实为 Gerstgrasser\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 4\n  last_seen_round: 11\n  mentions:\n    - round: 4\n      reviewers: [2]\n    - round: 6\n      reviewers: [2]\n    - round: 8\n      reviewers: []\n    - round: 10\n      reviewers: []\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及，可能已修复，待确认。\"\n\n- id: \"F2-W9b\"\n  summary: \"孤立 bib entries (orphan)\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 2\n  last_seen_round: 8\n  mentions:\n    - round: 2\n      reviewers: [2]\n    - round: 6\n      reviewers: [2]\n    - round: 8\n      reviewers: []\n    - round: 10\n      reviewers: []\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及，可能已修复，待确认。\"\n\n- id: \"F6-C2\"\n  summary: \"buffa2026entropy 引用标题与 arXiv 实际论文不匹配\"\n  category: reference\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [2]\n    - round: 8\n      reviewers: []\n    - round: 10\n      reviewers: []\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及，可能已修复，待确认。\"\n\n- id: \"F8-N2\"\n  summary: \"未讨论为何选择经典 permutation Granger 而非 neural Granger causality\"\n  category: method\n  severity: minor\n  status: resolved\n  resolution: \"§4 (method.tex L34) 已添加: 'We use classical rather than neural Granger methods because T≤25 provides insufficient observations for neural network parameter estimation.' Related work §2 引用 tank2021neural, marcinkevics2022neural 并说明选择理由。\"\n  resolution_round: 11\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [2]\n      note: \"R11 R2 在 Missing References 中确认论文已引用 neural Granger 文献。§4 已解释选择理由。\"\n\n- id: \"F8-N3\"\n  summary: \"Appendix 关键验证内容(T=20 predict-then-verify, power analysis)应纳入正文\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: []\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及。8 页限制下难以纳入更多内容。\"\n\n- id: \"F8-N4\"\n  summary: \"Appendix Z V1/V2 predict-then-verify 存在 post-hoc adjustment 嫌疑\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: []\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及。\"\n\n- id: \"R10-SF5\"\n  summary: \"Bivariate confounding：entropy/diversity 可能同受 distribution shift 驱动\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 R1 提为 W3。R2 REBUT：§6 已讨论 measurement sensitivity 替代解释。R1 可能未注意到。共识：现有讨论基本充分，但可更显著。\"\n\n- id: \"R10-SF7\"\n  summary: \"3-4 seeds replication power 有限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 R1 在 N1 context 中再次提及（null seeds 不足）。Specification curve 1160 配置部分补偿但不等同于采样稳健性。\"\n\n- id: \"R10-REF2\"\n  summary: \"遗漏引用：Mitchell et al. (2023) DetectGPT\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 (related_work.tex L12) 已引用 mitchell2023detectgpt 并区分 single-generation detection vs multi-generation distributional tracking。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [2]\n      note: \"R11 R2 确认已引用。\"\n\n- id: \"R10-REF4\"\n  summary: \"遗漏引用：Padmakumar et al. (2024) LM 对文本多样性影响\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 (related_work.tex L9) 已引用 padmakumar2024writing。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [2]\n      note: \"R11 R2 确认已引用。\"\n\n- id: \"R10-REF5\"\n  summary: \"遗漏引用：Montgomery SPC 经典文献\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及。\"\n\n- id: \"R11-FMT1\"\n  summary: \"Abstract 脚注不标准\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Abstract 中放脚注在 ACL 论文中不常见，可能影响索引系统渲染。建议移至 Introduction。交叉共识：AGREE。\"\n\n- id: \"R11-SYM1\"\n  summary: \"β 符号重用：统计功率 vs 幂律指数\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"同一论文中 β 表示统计功率又表示幂律指数，易混淆。建议对功率用不同符号。交叉共识：AGREE。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "issues_yaml": "issues:\n# ============================================================\n# Round 1-10 历史 resolved — 保留跨轮次记录\n# ============================================================\n- id: \"R1-N1\"\n  summary: \"Ground-truth pairs 定义存在循环论证\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Effect-size GT 重定义完成。\"\n  resolution_round: 1\n\n- id: \"R1-N2\"\n  summary: \"FPR=0% 标定仅基于单 seed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"α=0.0 三 seed FPR 验证完成。\"\n  resolution_round: 1\n\n- id: \"R1-N3\"\n  summary: \"α=0.50 和 α=0.75 仅 1 seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Multi-seed 补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-N1\"\n  summary: \"核心方法论为计量经济学已有知识的直接迁移，新颖性有限\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Round 1 三层定位 reframe 完成。\"\n  resolution_round: 1\n\n- id: \"R2-N2\"\n  summary: \"α=0.75 multi-seed 实验未完成 + Appendix A 缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-N3\"\n  summary: \"实验规模过窄\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"跨架构验证已扩展至 15 model-seed 组合。\"\n  resolution_round: 1\n\n- id: \"R1-W1\"\n  summary: \"Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"核心修复完成。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"PermG 缺少 power analysis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Appendix N power analysis 完成。\"\n  resolution_round: 1\n\n- id: \"R1-W3\"\n  summary: \"75% spurious-signal rate headline 依赖 underpowered T-Y\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W4\"\n  summary: \"α=0.75 单 seed borderline 结果不应出现在 abstract\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W5\"\n  summary: \"Toda-Yamamoto 纳入理由表述不充分\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W6\"\n  summary: \"可重复性信息不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"超参补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-W3\"\n  summary: \"Token entropy canary 仅在 α=1.0 验证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"缺少独立 Limitations section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W5\"\n  summary: \"缺少 AI Writing Disclosure\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W6\"\n  summary: \"缺少 canary→perplexity 为何 spurious 的深入解释\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF1\"\n  summary: \"遗漏 Granger & Newbold (1974)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF2\"\n  summary: \"遗漏 Hataya et al. (2023) 和 Seddik et al. (2024)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W1-old\"\n  summary: \"Citation key chen2025scales 与实际作者不匹配\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"F2-W3\"\n  summary: \"Section 3 承诺的三项附录内容缺失\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"附录内容补充完成。\"\n  resolution_round: 3\n\n- id: \"F2-W8\"\n  summary: \"格式不合规：未使用 ACL 模板\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"ACL 模板迁移完成。\"\n  resolution_round: 2\n\n- id: \"F2-REF1\"\n  summary: \"遗漏 arXiv:2502.15654\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF1\"\n  summary: \"遗漏 arXiv:2602.10531\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF2\"\n  summary: \"遗漏 arXiv:2505.19046\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF3\"\n  summary: \"遗漏 arXiv:2510.16657\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF5\"\n  summary: \"Appendix H CUSUM 未引用 Page (1954)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F4-REF1\"\n  summary: \"遗漏 Truong & Truong (2026)\"\n  category: reference\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"引用已添加并在 §1/§2 讨论。\"\n  resolution_round: 6\n\n- id: \"F4-REF3\"\n  summary: \"遗漏 Benjamini & Yekutieli (2001)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"§4 现引用 benjamini2001control。\"\n  resolution_round: 5\n\n- id: \"F2-REF3\"\n  summary: \"Dakos et al. (2012) + Schreiber (2000) + Phipson & Smyth (2010) 在 bib 中但正文未引用\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"引用补充完成。\"\n  resolution_round: 4\n\n- id: \"F6-W2\"\n  summary: \"页数可能超限\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"R8 PDF 审查确认主体 8 页合规。\"\n  resolution_round: 8\n\n- id: \"F2-W6b\"\n  summary: \"'Methodological pitfalls' 有 straw-man 倾向\"\n  category: framing\n  severity: major\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 8\n  resolution: \"全文已改为 'design considerations'。R8 fresh review 未再提及。\"\n  resolution_round: 8\n\n- id: \"F5-N2\"\n  summary: \"T=10 统计效力不足(power≈37%), sharp onset 可能是 power artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Power simulation 重写通过 Reviewer #75。Steepness comparison k_obs=18.79 vs k_H0=6.14 (ratio 3.06×, CI non-overlapping) 写入 method.tex + experiments.tex + appendix。Dense α 证据 (17 points, sigmoid k=15.7) 额外支撑。\"\n  resolution_round: 9\n  first_raised_round: 5\n  last_seen_round: 9\n\n- id: \"F2-W5\"\n  summary: \"Token entropy → distinct-n 机械耦合 confound 未排除\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Metric structure 分析完成：mauve attribution 100% 确认非 metric coupling。ECE→distinct 独立于 token_entropy→distinct 路径。讨论已添加到 discussion.tex。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 9\n\n- id: \"F2-W2\"\n  summary: \"Specification curve analysis 定位不精确\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Appendix E 已改称 'systematic robustness analysis'。R8/R9 fresh review 未再提及。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 8\n\n- id: \"F8-C2\"\n  summary: \"Discussion §6 过于简短(~100词)\"\n  category: writing\n  severity: major\n  status: resolved\n  resolution: \"Discussion 扩展至 20 行（metric-specific ceiling + practical implications + domain-dependent directionality）。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C3\"\n  summary: \"与 Schaeffer et al. (2025) '8 种 collapse 定义' 的关系讨论不充分\"\n  category: framing\n  severity: major\n  status: resolved\n  resolution: \"Schaeffer taxonomy 映射已添加到 related_work.tex L5-6。检测框架显式对应 distributional shift 定义 (D4-D6)。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C1\"\n  summary: \"Du & Tanaka-Ishii (2026) 引用三重错误：arXiv ID、标题、研究对象\"\n  category: reference\n  severity: critical\n  status: resolved\n  resolution: \"§2 已修正为 'related but distinct phenomenon'。R9 fresh review 未再提及。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"R9-C1\"\n  summary: \"FPR CI method.tex 内部矛盾：L16 [0,0] vs L24 [0%,41%]\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"FPR=10% MMCT sensitivity analysis 完成。K≥3 不受影响。Paper Agent 统一 CI 处理。\"\n  resolution_round: 9\n  first_raised_round: 9\n  last_seen_round: 9\n\n- id: \"F8-N1\"\n  summary: \"BH-FDR 在强正回归依赖下适用性讨论不充分\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"跨 pair correlation 结构报告在 method.tex。PRDS 假设适用性讨论已添加。FPR sensitivity analysis 额外支撑。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 10\n\n- id: \"F8-REF1\"\n  summary: \"遗漏引用：online/continual learning 下 model collapse 检测\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"related_work.tex 已添加 scope 区分（iterative from-scratch vs continual learning）。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F2-W11\"\n  summary: \"α_c SE=0.006 低估真实 seed 不确定性\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"被 F2-W4b/F2-W6 的统计基础问题覆盖，单独不再追踪。\"\n  resolution_round: 11\n  first_raised_round: 2\n  last_seen_round: 10\n\n# ============================================================\n# 活跃 issues — Round 11 Fresh Review 更新\n# ============================================================\n\n- id: \"F3-J4\"\n  summary: \"PermG FPR 超出 nominal 5%，architecture-dependent\"\n  category: method\n  severity: critical\n  status: open\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 3\n  last_seen_round: 11\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 双方最高优先级共识。FPR=11.1% CI [1.2%,30.4%] 使 detection boundary 附近结论不可靠。GPT-2 medium FPR=50% 说明 architecture-dependent。建议：增加 null seeds、报告 FPR-adjusted rates、Bonferroni sensitivity。\"\n\n- id: \"F2-W4b\"\n  summary: \"Proposition 3 本质是 curve fitting / empirical scaling，非理论推导\"\n  category: framing\n  severity: critical\n  status: open\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 11\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11: 5T 拟合 2 参数仅 2-3 DF。LOO-CV MAE=0.037 在 4-5 点上信息量极有限。sync-dip 排除 post-hoc。ΔAIC=4.15 仅含 sync-dip 时支持 power-probit。R2 补充 mitigating factors (ΔAIC analysis, 15/15 within CI) 但同意降级为 'consistent with power law'。交叉共识：AGREE。\"\n\n- id: \"F2-W2b\"\n  summary: \"'Detectability landscape' framing 承诺超过交付\"\n  category: framing\n  severity: critical\n  status: open\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 11\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11: 完整 α×T grid 仅 Pythia-410M。跨架构仅 α=1.0（最容易检测）。无法回答其他架构中间 α 水平的 phase-diagram 结构。R1 同意但反对'case study'标签——建议限定 scope 而非降级标题。交叉共识：AGREE（framing gap 真实存在）。\"\n\n- id: \"F2-W1\"\n  summary: \"α=0.60 sync dip：precision sensitivity (bf16 0/8 vs fp32 6/8)\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 3\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: []\n      note: \"R11 未单独提及 sync-dip 作为独立问题，但被 F2-W4b (power law fit) 中 sync-dip 排除的 post-hoc 性覆盖。\"\n\n- id: \"F2-W10\"\n  summary: \"Cross-architecture 'coupling preserved' 条件 post-hoc 循环论证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 11\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11: 27% failure rate (4/15)。SmolLM3-3B 在 α=1.0 下仅 3/8。GPT-2-medium null FPR=50%。Abstract 'confirms' 措辞过于乐观。R1/R2 一致建议改为 'partial validation with notable exceptions'。交叉共识：AGREE。\"\n\n- id: \"F2-W6\"\n  summary: \"Detection boundary 验证不足 (2T 拟合 2 参数=零自由度)\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 11\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"与 F2-W4b 合并。R11 R1 提议补充 T=7/12/18 增加自由度。R2 同意方向但认为 mitigating factors 存在。交叉共识：AGREE 需降级声称。\"\n\n- id: \"F2-W7\"\n  summary: \"Intervention 实验薄弱：post hoc threshold, n=2, 仅 α=1.0, CI 29-64%\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 11\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11: R1 要求移除 abstract 中 '64%'。R2 partial REBUT——proof-of-concept framing 可保留，但精确数字在 N=2 下不可信。共识：abstract 中用定性描述替代 '64%'，§5.6 保留详细数据。\"\n\n- id: \"F5-N1\"\n  summary: \"核心方法是计量经济学标准技术的直接移植，贡献定位不清\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 11\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 R2 再次标为 must-fix (novelty ceiling)。R1 partial REBUT：empirical characterization 是合理贡献模式，pipeline integration (PermG + first-diff + BH-FDR + MMCT + Shapley + spec curve) 有方法论价值。但同意 Design Principles 1-2 不构成理论贡献。分歧：R2 认为 novelty 不足以支撑 main conference，R1 认为在 Findings-borderline Conference 范围合理。\"\n\n- id: \"F5-W1\"\n  summary: \"Proposition 1 数学深度有限，仅 Jensen 不等式\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 11\n  mentions:\n    - round: 5\n      reviewers: [2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 双方同意 Design Principles 不构成理论贡献，但作为实验设计 motivation 合理。\"\n\n- id: \"R11-N1\"\n  summary: \"统计功率 β=0.66 CI [0.24,0.78] 使检测边界定量解读不可靠\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 首次以 must-fix 提出。功率低至 0.24 时 α_c(T) 会被严重高估。T^{-2.08} 可能反映功率变化而非信号特性。R2 AGREE：Appendix N 确认 T≤8 功率不足 50%。共识：正文应更显著呈现功率限制对边界解读的影响，区分'未检测到'与'不可检测'。\"\n\n- id: \"R11-W1\"\n  summary: \"'3%-92%' FPR 范围含失效方法 NaiveXCorr，abstract framing 夸大\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"92% 来自 NaiveXCorr（本质失效 baseline）。排除后合格方法范围为 3%-39%。Abstract 应区分通过 null 验证的方法和所有方法。交叉共识：AGREE。\"\n\n- id: \"R11-W2\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽 [0.25, 0.92]\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"6/8 Clopper-Pearson CI = [0.25, 0.92]。相邻 cell 差异可能不显著。Figure 1 的二值化呈现可能夸大统计区分度。建议标注 CI 或用连续色阶。交叉共识：AGREE。Limitations 已承认但正文视觉呈现未反映。\"\n\n- id: \"R9-m5\"\n  summary: \"Granger 'precedence' vs 'causality' 术语不一致\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: []\n      note: \"R11 未单独提及。R2 在交叉回应中引用 §6 已有讨论。可能已充分处理。\"\n\n- id: \"R9-REF1\"\n  summary: \"遗漏引用：Gerstgrasser et al. (2024) data accumulation vs replacement\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 9\n      reviewers: [2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: []\n      note: \"R11 未单独提及。论文 §2 已引用 dey2024breaking，但 Gerstgrasser 作为 accumulation paradigm 的核心参考仍建议补充。\"\n\n- id: \"R9-REF2\"\n  summary: \"遗漏引用：Steegen et al. (2016) multiverse analysis\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 (related_work.tex L29) 已引用 steegen2016increasing。\"\n  resolution_round: 11\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 9\n      reviewers: [2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [2]\n      note: \"R11 R2 在 missing references 中确认论文已引用。\"\n\n- id: \"R10-MF5\"\n  summary: \"'Five families (345M-6.9B)' 数字自洽性错误\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 双方再次确认。Padding-410M 是 Pythia variant，严格仅 4 独立族。'345M-6.9B' 与最大 3B 不符。交叉共识：AGREE。\"\n\n- id: \"R10-SF2\"\n  summary: \"Data accumulation vs replacement paradigm 未讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 R2 在 Questions 中再次提出。Limitations 已承认 'full replacement' 但未讨论 accumulation 下 landscape 预期变化。\"\n\n- id: \"R10-SF3\"\n  summary: \"单一解码策略 (temperature 1.0/top-k=50) 需定性讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 R2 提为 should-fix，R1 REBUT（已在 Limitations 承认，属合理 scope limitation）。共识：不需额外实验，但 Discussion 可加 1 句关于结构性改变可能性的 caveat。\"\n\n- id: \"R10-SF4\"\n  summary: \"方法敏感性 '3%-92%' framing 混淆失效方法与真正 sensitivity\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"与 R11-W1 合并。交叉共识：AGREE。\"\n\n- id: \"R10-SF6\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"与 R11-W2 合并。交叉共识：AGREE。\"\n\n- id: \"R10-m1\"\n  summary: \"Figure 3 y 轴标签 'FDR-significant pairs' 含义不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及。\"\n\n- id: \"R10-m2\"\n  summary: \"Table 2 'x/8' 列含义未在 caption 定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及。\"\n\n- id: \"R10-m3\"\n  summary: \"§5.1 '(§5.5)' 前向引用缺上下文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及。\"\n\n- id: \"R10-REF3\"\n  summary: \"遗漏引用：Runge et al. (2019) 短时间序列因果发现\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 R2 再次在 Missing References 中提出。R1 AGREE。PCMCI 算法与本文 T≤25 短序列因果推断直接相关。\"\n\n- id: \"R10-VIS1\"\n  summary: \"Discussion §6 溢出到第 9 页，可能违反 EMNLP 2026 八页主文限制\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [visual_check]\n    - round: 11\n      reviewers: [1, 2, visual_check]\n      note: \"R11 视觉审查确认：Table 1 和 Figure 6 浮动到第 9 页。R1/R2 交叉共识：AGREE，属格式边界问题。建议调整 float placement 或压缩正文。\"\n\n- id: \"R11-VIS2\"\n  summary: \"Pages 6-7 连续纯文本无 display item，图表堆叠在 page 8\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [visual_check]\n      note: \"Figures 3/4/5 三图堆叠在 page 8，每图仅 1/3 页高度。Pages 6-7 纯文本。建议至少 1 图上移至 page 6-7 改善视觉节奏。\"\n\n- id: \"F8-W2\"\n  summary: \"Figure 1/2 子图内文字偏小，Figure 2 灰度打印难区分\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 8\n      reviewers: [2, visual_check]\n    - round: 10\n      reviewers: [visual_check]\n    - round: 11\n      reviewers: [visual_check]\n      note: \"R11 视觉审查确认：Figures 3-5 tick labels/legend 字号约正文 60-65%，在可读性边界。\"\n\n- id: \"F4-REF5\"\n  summary: \"bib first author mismatch: dey2024breaking 实为 Gerstgrasser\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 4\n  last_seen_round: 11\n  mentions:\n    - round: 4\n      reviewers: [2]\n    - round: 6\n      reviewers: [2]\n    - round: 8\n      reviewers: []\n    - round: 10\n      reviewers: []\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及，可能已修复，待确认。\"\n\n- id: \"F2-W9b\"\n  summary: \"孤立 bib entries (orphan)\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 2\n  last_seen_round: 8\n  mentions:\n    - round: 2\n      reviewers: [2]\n    - round: 6\n      reviewers: [2]\n    - round: 8\n      reviewers: []\n    - round: 10\n      reviewers: []\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及，可能已修复，待确认。\"\n\n- id: \"F6-C2\"\n  summary: \"buffa2026entropy 引用标题与 arXiv 实际论文不匹配\"\n  category: reference\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [2]\n    - round: 8\n      reviewers: []\n    - round: 10\n      reviewers: []\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及，可能已修复，待确认。\"\n\n- id: \"F8-N2\"\n  summary: \"未讨论为何选择经典 permutation Granger 而非 neural Granger causality\"\n  category: method\n  severity: minor\n  status: resolved\n  resolution: \"§4 (method.tex L34) 已添加: 'We use classical rather than neural Granger methods because T≤25 provides insufficient observations for neural network parameter estimation.' Related work §2 引用 tank2021neural, marcinkevics2022neural 并说明选择理由。\"\n  resolution_round: 11\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [2]\n      note: \"R11 R2 在 Missing References 中确认论文已引用 neural Granger 文献。§4 已解释选择理由。\"\n\n- id: \"F8-N3\"\n  summary: \"Appendix 关键验证内容(T=20 predict-then-verify, power analysis)应纳入正文\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: []\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及。8 页限制下难以纳入更多内容。\"\n\n- id: \"F8-N4\"\n  summary: \"Appendix Z V1/V2 predict-then-verify 存在 post-hoc adjustment 嫌疑\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: []\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及。\"\n\n- id: \"R10-SF5\"\n  summary: \"Bivariate confounding：entropy/diversity 可能同受 distribution shift 驱动\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 R1 提为 W3。R2 REBUT：§6 已讨论 measurement sensitivity 替代解释。R1 可能未注意到。共识：现有讨论基本充分，但可更显著。\"\n\n- id: \"R10-SF7\"\n  summary: \"3-4 seeds replication power 有限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 R1 在 N1 context 中再次提及（null seeds 不足）。Specification curve 1160 配置部分补偿但不等同于采样稳健性。\"\n\n- id: \"R10-REF2\"\n  summary: \"遗漏引用：Mitchell et al. (2023) DetectGPT\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 (related_work.tex L12) 已引用 mitchell2023detectgpt 并区分 single-generation detection vs multi-generation distributional tracking。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [2]\n      note: \"R11 R2 确认已引用。\"\n\n- id: \"R10-REF4\"\n  summary: \"遗漏引用：Padmakumar et al. (2024) LM 对文本多样性影响\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 (related_work.tex L9) 已引用 padmakumar2024writing。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [2]\n      note: \"R11 R2 确认已引用。\"\n\n- id: \"R10-REF5\"\n  summary: \"遗漏引用：Montgomery SPC 经典文献\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及。\"\n\n- id: \"R11-FMT1\"\n  summary: \"Abstract 脚注不标准\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Abstract 中放脚注在 ACL 论文中不常见，可能影响索引系统渲染。建议移至 Introduction。交叉共识：AGREE。\"\n\n- id: \"R11-SYM1\"\n  summary: \"β 符号重用：统计功率 vs 幂律指数\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"同一论文中 β 表示统计功率又表示幂律指数，易混淆。建议对功率用不同符号。交叉共识：AGREE。\""
  }
}
```

</details>

---


### Tool result

_source line 1073 · 2026-05-24T13:36:17.354221+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml\", \"bytes\": 26562}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1074 · 2026-05-24T13:38:49.667540+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 11 (Fresh Review)\n\n**论文**: \"Characterizing the Detectability Landscape of Iterative Model Collapse\"\n**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer**: 2 人（R1: 方法严谨性+统计验证+实验有效性; R2: 新颖性/贡献定位+完整性+写作质量+格式合规）\n\n---\n\n## Summary\n\n本文系统研究迭代模型坍塌的可检测性边界：在给定合成数据污染比例 α 和观测窗口长度 T 的条件下，何时能统计显著地检测到分布退化。以 Pythia-410M 为主架构，在 13 个 α 水平 × 多个 T 值上构建检测相图，发现四个 regime（blind / onset / sync-dip / detection），拟合幂律检测边界 α_c(T) ∝ T^{−2.08}。跨 5 个模型族（345M–6.9B）在 α=1.0 下验证泛化性。证明 entropy Granger-precedes diversity by ≥1 generation（14/15 实验），并展示 canary-triggered intervention 的概念验证（64% peak perplexity reduction, N=2）。方法敏感性分析表明 5 种检测方法在相同数据上产生 FPR 从 3% 到 92% 的差异。\n\n---\n\n## Strengths\n\n1. **新颖且重要的研究问题**：model collapse 的可检测性景观是该领域空白，将问题框架化为 (α, T) 二维相图具有很强的概念清晰度。\n\n2. **方法论透明度异常出色**：论文对自身统计局限的坦诚程度（FPR CI、功率不足、8-pair CI 宽度、β CI 宽度）超过同类工作。Limitations section 直接引用 Clopper-Pearson CI 并承认\"coarse topology rather than precise probability surface\"。\n\n3. **方法敏感性是最强贡献**：5 种方法在相同数据上产生截然不同的结论（从 universal detection 到 complete null），这一发现对 model collapse 文献中方法选择的随意性具有重要警示意义。\n\n4. **异常详尽的鲁棒性验证**（21 页 appendix）：specification curve analysis（1,160 配置）、Shapley 值分解、功率分析、非平稳鲁棒性模拟、predict-then-verify 等，远超平均水平。\n\n5. **First-differencing 作为诊断工具**：发现 first-differencing 消除 canary→perplexity 但保留 canary→diversity（24/24→24/24），精确 scope 了 Granger precedence claim，具有独立方法论价值。\n\n6. **系统且严谨的实验控制**：BH-FDR 校正、5000 permutations、多种子复制、null-control calibration，在 NLP 实证工作中罕见。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1** [critical] PermG 的 FPR 膨胀削弱检测边界精度\n- PermG null-control FPR = 11.1%（4/36），CI [1.2%, 30.4%]，超出 nominal 5%\n- 在检测边界附近（α≈0.45-0.50），假阳性和真阳性难以区分\n- 虽然 0/8→6/8 的跳跃幅度不能完全由 FPR 解释，但精确边界位置不可靠\n- GPT-2-medium 上 FPR=50% 说明该问题是 architecture-dependent\n- **共识**: 双方 AGREE，must-fix\n\n**MF-2** [critical] \"Detectability landscape\" framing 与证据范围显著落差\n- 完整 α×T grid 仅在 Pythia-410M 上映射\n- 跨架构验证限于 α=1.0（最容易检测的极端场景）\n- 无法回答：phase-diagram 的四 regime 结构是否适用于其他架构在中间 α 水平下的情况\n- \"Five families (345M–6.9B)\" 实为 4 个独立族 + 1 Pythia variant；最大实测 3B，非 6.9B\n- Abstract \"cross-architecture validation confirms\" 措辞过于乐观（27% 失败率=4/15 条件）\n- **共识**: 双方 AGREE，framing gap 真实存在\n\n**MF-3** [critical] 幂律边界 α_c(T) ∝ T^{−2.08} 拟合基础过于薄弱\n- 5 个 T 值拟合 2 参数（A, β_signal），排除 sync-dip 后仅 4 有效点（2 自由度）\n- LOO-CV MAE=0.037 在 4-5 个点上信息量极有限——任何合理单调函数均可达到\n- sync-dip 排除是 post-hoc，ΔAIC=4.15 仅在包含 sync-dip 时支持 power-probit\n- β_signal MLE CI [0.24, 0.78] 意味着 T 指数不确定性极大（可能从 −0.64 到 −2.08）\n- **共识**: 双方 AGREE。R2 补充 mitigating factors（15/15 within CI, ΔAIC analysis）但同意应降级为\"consistent with power law\"\n\n**MF-4** [critical] 统计功率 β=0.66 CI [0.24, 0.78] 使\"不可检测\"无法区分于\"功率不足\"\n- 功率低至 0.24 时，α_c(T) 会被严重高估\n- T^{−2.08} 指数可能反映检验功率随 T 衰减而非信号物理特性\n- Appendix N 确认：T≤8 时功率不足 50%\n- 正文对此限制的呈现不够显著（仅 Limitations 一句）\n- **共识**: 双方 AGREE\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1** [warning] 核心方法 novelty 有限：计量经济学标准技术直接移植\n- PermG 源自 Granger (1969)，MMCT 是简单投票，Design Principles 依赖 Jensen 不等式\n- R1 partial REBUT：pipeline integration (PermG + first-diff + BH-FDR + MMCT + Shapley + spec curve) 有方法论价值；empirical characterization 是合理贡献模式\n- **分歧**: R2 认为 novelty 不足以支撑 main conference；R1 认为在 Findings-borderline Conference 范围合理\n\n**SF-2** [warning] Intervention 实验证据力不足\n- 仅 α=1.0, N=2 seeds, post-hoc threshold (15%)\n- Abstract 中 \"64% perplexity reduction\" 在 N=2 下精确数字不可信\n- **共识**: 双方同意 abstract 应用定性描述替代精确数字；proof-of-concept framing 可保留\n\n**SF-3** [warning] 跨架构验证暴露系统性异质性\n- SmolLM3 在 α=1.0 下仅 3/8（non-monotonic entropy violates Design Principle 1）\n- GPT-2-medium null FPR=50%；Pythia-1.4B seed-dependent (2/8 vs 6/8)\n- 三种失败覆盖不同规模和家族，说明非随机变异\n- **共识**: 双方 AGREE，建议改为\"partial validation with notable exceptions\"\n\n**SF-4** [warning] \"3%–92%\" FPR 范围含失效方法 NaiveXCorr\n- 92% 来自 NaiveXCorr——本质上是未通过 null 验证的 failed baseline\n- 合格方法范围实为 3%–39%，仍有意义但不如 92% 戏剧化\n- **共识**: 双方 AGREE，abstract 应区分 validated methods vs all methods\n\n**SF-5** [warning] 每 cell 仅 8 pairs → binomial CI 极宽\n- 6/8 的 Clopper-Pearson 95% CI = [0.25, 0.92]\n- Figure 1 的二值化色彩编码可能夸大相邻 cell 的统计区分度\n- Limitations 已承认但视觉呈现未反映不确定性\n- **共识**: 双方 AGREE\n\n### Minor Issues\n\n- β 符号重用：统计功率 vs 幂律指数，同一论文中易混淆（双方 AGREE）\n- Table 1 / Figure 6 浮动到第 9 页，触及 8 页限制边界（双方 AGREE）\n- Abstract 脚注不标准，可能影响索引系统（双方 AGREE）\n- \"Five families\" 含 Padding-410M（Pythia variant），严格仅 4 独立族（双方 AGREE）\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成完全共识 [AGREE]：\n\n1. FPR 膨胀是核心定量声称的薄弱环节（MF-1）\n2. 幂律拟合自由度不足，应降级为\"consistent with\"（MF-3）\n3. 统计功率限制使 landscape 解读存在系统性偏差（MF-4）\n4. Framing 与证据范围存在落差（MF-2）\n5. 跨架构 27% 失败率需要更审慎的措辞（SF-3）\n6. \"3%–92%\" 含 NaiveXCorr 夸大了 method sensitivity（SF-4）\n7. 8 pairs/cell 的 CI 宽度应在视觉呈现中反映（SF-5）\n8. Intervention 的 \"64%\" 不应以精确数字出现在 abstract（SF-2）\n9. \"Five families\" 计数和 \"345M–6.9B\" 范围不准确（minor）\n10. 页数边界问题需要调整 float placement（minor）\n\n---\n\n## Reviewer Divergence\n\n1. **Novelty 评价** (SF-1)：\n   - R2: PermG 直接移植，novelty 天花板限制主会议定位\n   - R1: Empirical characterization + pipeline integration 是合理贡献模式，前提是定量结论稳健\n   - 综合：novelty 有限是事实，但不是一票否决因素——关键取决于统计基础能否加固\n\n2. **Granger precedence confounding 讨论充分性** (R1-W3)：\n   - R1: 讨论不充分，measurement sensitivity 替代解释未充分排除\n   - R2: §6 已讨论（\"Entropy's greater sensitivity... means the temporal lead may partly reflect measurement sensitivity\"）\n   - 综合：论文已有讨论但不够显著；不构成 must-fix\n\n---\n\n## Questions\n\n1. 如果 null-condition seeds 增加到 10-20 个，FPR 点估计预期收敛到什么水平？如果仍 >5%，检测边界声称是否需要根本性修改？\n\n2. 能否为 T^{−2.08} 指数报告完整 bootstrap CI？如果覆盖 [−0.5, −2.5]，对 abstract 中的定量表述有何影响？\n\n3. SmolLM3 在 α=1.0 下 0/8 检测——什么解释了完全污染下的检测失败？这是 PermG 的根本局限还是统计功效问题？\n\n4. 能否为至少一个额外架构提供缩减版 α×T grid（如 5α × 3T），以验证 phase-diagram 结构的可迁移性？\n\n5. Data accumulation 设置下 landscape 如何变化？这是否是一个比 full replacement 更现实的场景？\n\n---\n\n## Missing References\n\n- **Runge et al. (2019)** \"Detecting and quantifying causal associations in large nonlinear time series datasets.\" *Science Advances*. — 与本文核心设置（短非线性时间序列中的因果发现）直接相关，PCMCI 算法应在 §2 讨论并解释为何选择线性 PermG。（双方 AGREE）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warnings, 3 info）：\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ warning | pp.6-7 | 实验章节连续 2 页纯文本无 display item，结果与图表分离 |\n| ⚠️ warning | p.8 | Figures 3/4/5 三图堆叠同页，每图仅 1/3 页高，图内文字偏小（正文 60-65%） |\n| ⚠️ warning | p.9 | Table 1 和 Figure 6 浮动超出 8 页主文边界 |\n| ℹ️ info | pp.1-2 | 前 2 页纯文本，Figure 1 在 p.3 出现（合格但非最优） |\n| ℹ️ info | p.8 | Tick labels/legend 字号约 60-65%，在可读性边界 |\n| ℹ️ info | p.30 | Appendix 最后页 ~35% 空白（不影响评价） |\n\n建议：将至少 1 个 figure 上移至 pp.6-7 改善视觉节奏；调整 float 将 Table 1/Figure 6 拉回 p.8 内。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 (Borderline Conference)\n**置信度**: 4/5（双方 Reviewer 均熟悉统计方法和 model collapse 文献）\n\n**评分理由**:\n\n论文提出了一个新颖且重要的研究问题（model collapse 的可检测性景观），实验设计严谨（specification curve 1,160 配置、5,000 permutations、multi-seed 复制），方法论透明度出色（对自身局限性的坦诚程度超过同类工作）。方法敏感性发现（同一数据上 5 种方法得出截然不同结论）是最强贡献。\n\n然而，核心定量声称的统计基础存在多处脆弱性：FPR 膨胀（11.1%, CI 上界 30%）使精确边界不可靠；幂律拟合自由度极低（4-5 点拟合 2 参数）；统计功率 CI [0.24, 0.78] 无法区分\"不可检测\"与\"功率不足\"。\"Detectability landscape\" 的宏大 framing 与实际证据范围（单模型完整 grid + 极端条件下的跨架构抽样验证）之间存在落差。跨架构验证暴露 27% 的系统性失败率。\n\n**推荐路径**:\n- 如果定量结论的统计基础能显著加固（更多 null seeds 收窄 FPR CI、更多 T 值增加拟合自由度）+ framing 调整为更准确反映单模型范围 → Conference (4.0)\n- 当前状态下，方法敏感性 + first-differencing 诊断的实证贡献已达 Findings 水平 → 3.0-3.5\n- Novelty 不是决定性障碍（empirical characterization 是合理贡献模式），关键是统计可信度\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"345M–6.9B\"：实测最大 3B（SmolLM3），6.9B 仅 Pythia-6.9B 一个条件且为 bf16。建议修正为实际范围。\n- \"five families\"：Padding-410M 是 Pythia variant，严格 4 族。建议 \"four families plus one architectural variant\"。\n- \"null-control false positive rates from 3% to 92%\"：92% 来自 NaiveXCorr（failed baseline）。建议区分或注明。\n- \"reduces peak perplexity by 64%\"：N=2, post-hoc threshold, α=1.0 only。建议替换为定性描述。\n- 脚注 1 在 abstract 中不标准，建议移至 §1。\n\n### §3 Cascade Ordering (Design Principles)\n- Design Principles 1-2 数学深度有限（Jensen 不等式级别），不构成独立理论贡献。\n- 但作为实验设计 motivation 和 canary metric 选择的形式化依据，其角色是合理的。\n- 建议：明确定位为\"theoretically motivated, empirically validated design principles\"而非\"theoretical contribution\"。\n\n### §4 Method\n- PermG FPR=11.1% CI [1.2%, 30.4%] 是全文最关键的统计弱点。建议正文中更显著地讨论其对边界精度的影响。\n- β 符号同时用于统计功率和幂律指数，建议区分。\n- 幂律拟合应降级为\"empirical observation consistent with power-law scaling\"而非确认幂律。\n\n### §5 Experiments\n- §5.1 sharp onset（0/8→6/8）：统计上显著（Fisher exact p=3.45×10^{-11}），但 CI 宽度意味着相邻 cell 差异不一定显著。建议在正文中注明 6/8 的 CI。\n- §5.5 Cross-architecture：4/15 失败率需更审慎措辞。建议表述为 \"PermG forward detection reaches ≥6/8 in 11/15 conditions, with four non-confirming conditions isolating distinct failure modes\"（论文已有类似表述但 abstract 未反映）。\n- §5.6 Intervention：proof-of-concept framing 恰当，但应从 abstract 移除精确数字。\n\n### §6 Discussion\n- 已讨论 measurement sensitivity 替代解释（\"Entropy's greater sensitivity...\"），这是积极的。\n- 缺少对 data accumulation paradigm 的讨论——所有实验用 full replacement，Gerstgrasser et al. (2024) 表明 accumulation 可 mitigate collapse，应讨论 landscape 在 accumulation 下的预期变化。\n- 单一解码策略：Limitations 已承认，建议补充一句关于结构性改变（非仅平移）的可能性。\n\n### Format\n- Table 1 / Figure 6 浮动到 p.9：需调整 float placement 确保 8 页合规。\n- pp.6-7 纯文本缺 display item：建议至少 1 figure 上移改善视觉节奏。\n- Figure 3-5 tick labels 偏小（~60-65% 正文字号）：建议在布局调整后适当放大。",
  "project": "distrib_canary_collapse",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 (Borderline Conference)",
  "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 11 (Fresh Review)\n\n**论文**: \"Characterizing the Detectability Landscape of Iterative Model Collapse\"\n**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer**: 2 人（R1: 方法严谨性+统计验证+实验有效性; R2: 新颖性/贡献定位+完整性+写作质量+格式合规）\n\n---\n\n## Summary\n\n本文系统研究迭代模型坍塌的可检测性边界：在给定合成数据污染比例 α 和观测窗口长度 T 的条件下，何时能统计显著地检测到分布退化。以 Pythia-410M 为主架构，在 13 个 α 水平 × 多个 T 值上构建检测相图，发现四个 regime（blind / onset / sync-dip / detection），拟合幂律检测边界 α_c(T) ∝ T^{−2.08}。跨 5 个模型族（345M–6.9B）在 α=1.0 下验证泛化性。证明 entropy Granger-precedes diversity by ≥1 generation（14/15 实验），并展示 canary-triggered intervention 的概念验证（64% peak perplexity reduction, N=2）。方法敏感性分析表明 5 种检测方法在相同数据上产生 FPR 从 3% 到 92% 的差异。\n\n---\n\n## Strengths\n\n1. **新颖且重要的研究问题**：model collapse 的可检测性景观是该领域空白，将问题框架化为 (α, T) 二维相图具有很强的概念清晰度。\n\n2. **方法论透明度异常出色**：论文对自身统计局限的坦诚程度（FPR CI、功率不足、8-pair CI 宽度、β CI 宽度）超过同类工作。Limitations section 直接引用 Clopper-Pearson CI 并承认\"coarse topology rather than precise probability surface\"。\n\n3. **方法敏感性是最强贡献**：5 种方法在相同数据上产生截然不同的结论（从 universal detection 到 complete null），这一发现对 model collapse 文献中方法选择的随意性具有重要警示意义。\n\n4. **异常详尽的鲁棒性验证**（21 页 appendix）：specification curve analysis（1,160 配置）、Shapley 值分解、功率分析、非平稳鲁棒性模拟、predict-then-verify 等，远超平均水平。\n\n5. **First-differencing 作为诊断工具**：发现 first-differencing 消除 canary→perplexity 但保留 canary→diversity（24/24→24/24），精确 scope 了 Granger precedence claim，具有独立方法论价值。\n\n6. **系统且严谨的实验控制**：BH-FDR 校正、5000 permutations、多种子复制、null-control calibration，在 NLP 实证工作中罕见。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1** [critical] PermG 的 FPR 膨胀削弱检测边界精度\n- PermG null-control FPR = 11.1%（4/36），CI [1.2%, 30.4%]，超出 nominal 5%\n- 在检测边界附近（α≈0.45-0.50），假阳性和真阳性难以区分\n- 虽然 0/8→6/8 的跳跃幅度不能完全由 FPR 解释，但精确边界位置不可靠\n- GPT-2-medium 上 FPR=50% 说明该问题是 architecture-dependent\n- **共识**: 双方 AGREE，must-fix\n\n**MF-2** [critical] \"Detectability landscape\" framing 与证据范围显著落差\n- 完整 α×T grid 仅在 Pythia-410M 上映射\n- 跨架构验证限于 α=1.0（最容易检测的极端场景）\n- 无法回答：phase-diagram 的四 regime 结构是否适用于其他架构在中间 α 水平下的情况\n- \"Five families (345M–6.9B)\" 实为 4 个独立族 + 1 Pythia variant；最大实测 3B，非 6.9B\n- Abstract \"cross-architecture validation confirms\" 措辞过于乐观（27% 失败率=4/15 条件）\n- **共识**: 双方 AGREE，framing gap 真实存在\n\n**MF-3** [critical] 幂律边界 α_c(T) ∝ T^{−2.08} 拟合基础过于薄弱\n- 5 个 T 值拟合 2 参数（A, β_signal），排除 sync-dip 后仅 4 有效点（2 自由度）\n- LOO-CV MAE=0.037 在 4-5 个点上信息量极有限——任何合理单调函数均可达到\n- sync-dip 排除是 post-hoc，ΔAIC=4.15 仅在包含 sync-dip 时支持 power-probit\n- β_signal MLE CI [0.24, 0.78] 意味着 T 指数不确定性极大（可能从 −0.64 到 −2.08）\n- **共识**: 双方 AGREE。R2 补充 mitigating factors（15/15 within CI, ΔAIC analysis）但同意应降级为\"consistent with power law\"\n\n**MF-4** [critical] 统计功率 β=0.66 CI [0.24, 0.78] 使\"不可检测\"无法区分于\"功率不足\"\n- 功率低至 0.24 时，α_c(T) 会被严重高估\n- T^{−2.08} 指数可能反映检验功率随 T 衰减而非信号物理特性\n- Appendix N 确认：T≤8 时功率不足 50%\n- 正文对此限制的呈现不够显著（仅 Limitations 一句）\n- **共识**: 双方 AGREE\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1** [warning] 核心方法 novelty 有限：计量经济学标准技术直接移植\n- PermG 源自 Granger (1969)，MMCT 是简单投票，Design Principles 依赖 Jensen 不等式\n- R1 partial REBUT：pipeline integration (PermG + first-diff + BH-FDR + MMCT + Shapley + spec curve) 有方法论价值；empirical characterization 是合理贡献模式\n- **分歧**: R2 认为 novelty 不足以支撑 main conference；R1 认为在 Findings-borderline Conference 范围合理\n\n**SF-2** [warning] Intervention 实验证据力不足\n- 仅 α=1.0, N=2 seeds, post-hoc threshold (15%)\n- Abstract 中 \"64% perplexity reduction\" 在 N=2 下精确数字不可信\n- **共识**: 双方同意 abstract 应用定性描述替代精确数字；proof-of-concept framing 可保留\n\n**SF-3** [warning] 跨架构验证暴露系统性异质性\n- SmolLM3 在 α=1.0 下仅 3/8（non-monotonic entropy violates Design Principle 1）\n- GPT-2-medium null FPR=50%；Pythia-1.4B seed-dependent (2/8 vs 6/8)\n- 三种失败覆盖不同规模和家族，说明非随机变异\n- **共识**: 双方 AGREE，建议改为\"partial validation with notable exceptions\"\n\n**SF-4** [warning] \"3%–92%\" FPR 范围含失效方法 NaiveXCorr\n- 92% 来自 NaiveXCorr——本质上是未通过 null 验证的 failed baseline\n- 合格方法范围实为 3%–39%，仍有意义但不如 92% 戏剧化\n- **共识**: 双方 AGREE，abstract 应区分 validated methods vs all methods\n\n**SF-5** [warning] 每 cell 仅 8 pairs → binomial CI 极宽\n- 6/8 的 Clopper-Pearson 95% CI = [0.25, 0.92]\n- Figure 1 的二值化色彩编码可能夸大相邻 cell 的统计区分度\n- Limitations 已承认但视觉呈现未反映不确定性\n- **共识**: 双方 AGREE\n\n### Minor Issues\n\n- β 符号重用：统计功率 vs 幂律指数，同一论文中易混淆（双方 AGREE）\n- Table 1 / Figure 6 浮动到第 9 页，触及 8 页限制边界（双方 AGREE）\n- Abstract 脚注不标准，可能影响索引系统（双方 AGREE）\n- \"Five families\" 含 Padding-410M（Pythia variant），严格仅 4 独立族（双方 AGREE）\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成完全共识 [AGREE]：\n\n1. FPR 膨胀是核心定量声称的薄弱环节（MF-1）\n2. 幂律拟合自由度不足，应降级为\"consistent with\"（MF-3）\n3. 统计功率限制使 landscape 解读存在系统性偏差（MF-4）\n4. Framing 与证据范围存在落差（MF-2）\n5. 跨架构 27% 失败率需要更审慎的措辞（SF-3）\n6. \"3%–92%\" 含 NaiveXCorr 夸大了 method sensitivity（SF-4）\n7. 8 pairs/cell 的 CI 宽度应在视觉呈现中反映（SF-5）\n8. Intervention 的 \"64%\" 不应以精确数字出现在 abstract（SF-2）\n9. \"Five families\" 计数和 \"345M–6.9B\" 范围不准确（minor）\n10. 页数边界问题需要调整 float placement（minor）\n\n---\n\n## Reviewer Divergence\n\n1. **Novelty 评价** (SF-1)：\n   - R2: PermG 直接移植，novelty 天花板限制主会议定位\n   - R1: Empirical characterization + pipeline integration 是合理贡献模式，前提是定量结论稳健\n   - 综合：novelty 有限是事实，但不是一票否决因素——关键取决于统计基础能否加固\n\n2. **Granger precedence confounding 讨论充分性** (R1-W3)：\n   - R1: 讨论不充分，measurement sensitivity 替代解释未充分排除\n   - R2: §6 已讨论（\"Entropy's greater sensitivity... means the temporal lead may partly reflect measurement sensitivity\"）\n   - 综合：论文已有讨论但不够显著；不构成 must-fix\n\n---\n\n## Questions\n\n1. 如果 null-condition seeds 增加到 10-20 个，FPR 点估计预期收敛到什么水平？如果仍 >5%，检测边界声称是否需要根本性修改？\n\n2. 能否为 T^{−2.08} 指数报告完整 bootstrap CI？如果覆盖 [−0.5, −2.5]，对 abstract 中的定量表述有何影响？\n\n3. SmolLM3 在 α=1.0 下 0/8 检测——什么解释了完全污染下的检测失败？这是 PermG 的根本局限还是统计功效问题？\n\n4. 能否为至少一个额外架构提供缩减版 α×T grid（如 5α × 3T），以验证 phase-diagram 结构的可迁移性？\n\n5. Data accumulation 设置下 landscape 如何变化？这是否是一个比 full replacement 更现实的场景？\n\n---\n\n## Missing References\n\n- **Runge et al. (2019)** \"Detecting and quantifying causal associations in large nonlinear time series datasets.\" *Science Advances*. — 与本文核心设置（短非线性时间序列中的因果发现）直接相关，PCMCI 算法应在 §2 讨论并解释为何选择线性 PermG。（双方 AGREE）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warnings, 3 info）：\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ warning | pp.6-7 | 实验章节连续 2 页纯文本无 display item，结果与图表分离 |\n| ⚠️ warning | p.8 | Figures 3/4/5 三图堆叠同页，每图仅 1/3 页高，图内文字偏小（正文 60-65%） |\n| ⚠️ warning | p.9 | Table 1 和 Figure 6 浮动超出 8 页主文边界 |\n| ℹ️ info | pp.1-2 | 前 2 页纯文本，Figure 1 在 p.3 出现（合格但非最优） |\n| ℹ️ info | p.8 | Tick labels/legend 字号约 60-65%，在可读性边界 |\n| ℹ️ info | p.30 | Appendix 最后页 ~35% 空白（不影响评价） |\n\n建议：将至少 1 个 figure 上移至 pp.6-7 改善视觉节奏；调整 float 将 Table 1/Figure 6 拉回 p.8 内。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 (Borderline Conference)\n**置信度**: 4/5（双方 Reviewer 均熟悉统计方法和 model collapse 文献）\n\n**评分理由**:\n\n论文提出了一个新颖且重要的研究问题（model collapse 的可检测性景观），实验设计严谨（specification curve 1,160 配置、5,000 permutations、multi-seed 复制），方法论透明度出色（对自身局限性的坦诚程度超过同类工作）。方法敏感性发现（同一数据上 5 种方法得出截然不同结论）是最强贡献。\n\n然而，核心定量声称的统计基础存在多处脆弱性：FPR 膨胀（11.1%, CI 上界 30%）使精确边界不可靠；幂律拟合自由度极低（4-5 点拟合 2 参数）；统计功率 CI [0.24, 0.78] 无法区分\"不可检测\"与\"功率不足\"。\"Detectability landscape\" 的宏大 framing 与实际证据范围（单模型完整 grid + 极端条件下的跨架构抽样验证）之间存在落差。跨架构验证暴露 27% 的系统性失败率。\n\n**推荐路径**:\n- 如果定量结论的统计基础能显著加固（更多 null seeds 收窄 FPR CI、更多 T 值增加拟合自由度）+ framing 调整为更准确反映单模型范围 → Conference (4.0)\n- 当前状态下，方法敏感性 + first-differencing 诊断的实证贡献已达 Findings 水平 → 3.0-3.5\n- Novelty 不是决定性障碍（empirical characterization 是合理贡献模式），关键是统计可信度\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"345M–6.9B\"：实测最大 3B（SmolLM3），6.9B 仅 Pythia-6.9B 一个条件且为 bf16。建议修正为实际范围。\n- \"five families\"：Padding-410M 是 Pythia variant，严格 4 族。建议 \"four families plus one architectural variant\"。\n- \"null-control false positive rates from 3% to 92%\"：92% 来自 NaiveXCorr（failed baseline）。建议区分或注明。\n- \"reduces peak perplexity by 64%\"：N=2, post-hoc threshold, α=1.0 only。建议替换为定性描述。\n- 脚注 1 在 abstract 中不标准，建议移至 §1。\n\n### §3 Cascade Ordering (Design Principles)\n- Design Principles 1-2 数学深度有限（Jensen 不等式级别），不构成独立理论贡献。\n- 但作为实验设计 motivation 和 canary metric 选择的形式化依据，其角色是合理的。\n- 建议：明确定位为\"theoretically motivated, empirically validated design principles\"而非\"theoretical contribution\"。\n\n### §4 Method\n- PermG FPR=11.1% CI [1.2%, 30.4%] 是全文最关键的统计弱点。建议正文中更显著地讨论其对边界精度的影响。\n- β 符号同时用于统计功率和幂律指数，建议区分。\n- 幂律拟合应降级为\"empirical observation consistent with power-law scaling\"而非确认幂律。\n\n### §5 Experiments\n- §5.1 sharp onset（0/8→6/8）：统计上显著（Fisher exact p=3.45×10^{-11}），但 CI 宽度意味着相邻 cell 差异不一定显著。建议在正文中注明 6/8 的 CI。\n- §5.5 Cross-architecture：4/15 失败率需更审慎措辞。建议表述为 \"PermG forward detection reaches ≥6/8 in 11/15 conditions, with four non-confirming conditions isolating distinct failure modes\"（论文已有类似表述但 abstract 未反映）。\n- §5.6 Intervention：proof-of-concept framing 恰当，但应从 abstract 移除精确数字。\n\n### §6 Discussion\n- 已讨论 measurement sensitivity 替代解释（\"Entropy's greater sensitivity...\"），这是积极的。\n- 缺少对 data accumulation paradigm 的讨论——所有实验用 full replacement，Gerstgrasser et al. (2024) 表明 accumulation 可 mitigate collapse，应讨论 landscape 在 accumulation 下的预期变化。\n- 单一解码策略：Limitations 已承认，建议补充一句关于结构性改变（非仅平移）的可能性。\n\n### Format\n- Table 1 / Figure 6 浮动到 p.9：需调整 float placement 确保 8 页合规。\n- pp.6-7 纯文本缺 display item：建议至少 1 figure 上移改善视觉节奏。\n- Figure 3-5 tick labels 偏小（~60-65% 正文字号）：建议在布局调整后适当放大。",
    "project": "distrib_canary_collapse",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 (Borderline Conference)",
    "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
  }
}
```

</details>

---


### Tool result

_source line 1075 · 2026-05-24T13:38:53.733609+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_150c7ce908e05d7932315e0288cf5bfb:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4066
}
```

</details>

---


### Assistant

_source line 1076 · 2026-05-24T13:39:00.500911+00:00_

审稿报告已投递给 Research Director。

**Round 11 审稿完成。**

总结：
- **Overall**: 3.5 (Borderline Conference)
- **4 个 Must-Fix**：FPR 膨胀、framing 落差、幂律拟合基础薄弱、统计功率不足
- **5 个 Should-Fix**：novelty 有限、intervention 证据弱、跨架构异质性、FPR 范围夸大、CI 宽度问题
- **核心建议路径**：加固统计基础（更多 null seeds + 更多 T 值）+ 调整 framing 精确度 → 可升至 Conference (4.0)；当前方法敏感性贡献已达 Findings 水平

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 105

## Round 105

2 recorded events


### User

_source line 1077 · 2026-05-24T13:39:01.557722+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

总结：对 R1 的 11 个要点中，我标注了 **8 个 [AGREE]**（含 1 个 partial agree on W2）和 **2 个 [REBUT]**（W2 partial, W3 full）。主要分歧在于：

- **W3**（Granger 混淆因素）：论文 §6 Discussion 已直接讨论了 measurement sensitivity 替代解释，R1 可能遗漏了该段落
- **W2**（干预实验）：同意 abstract 不应放 "64%" 精确数字，但 proof-of-concept framing 本身合理

R1 在统计方法论深度上（FPR 膨胀、功率分析、幂律拟合自由度）比我的审稿更细致，我认为其 N1-N3 的分析是站得住脚的。

---

[Reviewer 1 审稿结果]:
已完成对 Reviewer 2 全部意见的逐条回应并提交给 Director。

汇总：
- **Must-Fix**: N1 (novelty) REBUT（empirical characterization 是合理贡献类型，但部分同意天花板受限于定量结论稳健性）；N2 (framing gap) AGREE（完整 grid 仅 Pythia-410M，跨架构仅 α=1.0）
- **Should-Fix**: W1 (FPR 范围夸大) AGREE；W2 (跨架构异质性) AGREE；W3 (解码策略) REBUT（合理 scope limitation）；W4 (页面合规) AGREE
- **小问题 + Missing Ref**: 全部 AGREE

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1078 · 2026-05-24T13:39:12.112785+00:00_

审稿流程已完成。

**Round 11 审稿报告已投递给 Research Director。**

核心结论：
- **Overall: 3.5 (Borderline Conference)**
- 4 个 Must-Fix（FPR 膨胀、framing gap、幂律拟合薄弱、统计功率不足）
- 5 个 Should-Fix（novelty 天花板、intervention 证据力、跨架构异质性、FPR 范围表述、CI 宽度）
- 两位 Reviewer 在关键问题上达成高度共识，仅在 novelty 严重程度和 confounding 讨论充分性上存在分歧

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 106

## Round 106

52 recorded events


### User

_source line 1079 · 2026-05-24T13:57:26.499552+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distrib_canary_collapse
- 论文路径: projects/distrib_canary_collapse/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1080 · 2026-05-24T13:57:35.053374+00:00_

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
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1081 · 2026-05-24T13:57:35.154818+00:00_

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
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1082 · 2026-05-24T13:57:41.514593+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "9"
  }
}
```

</details>

---


### Tool result

_source line 1083 · 2026-05-24T13:57:41.514944+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1084 · 2026-05-24T13:57:41.766165+00:00_

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
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
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

_source line 1085 · 2026-05-24T13:57:41.816798+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1086 · 2026-05-24T13:57:49.999269+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1087 · 2026-05-24T13:57:51.856497+00:00_

{"result":"# 项目 distrib_canary_collapse 概况\n\n## 实验状态 (214 个)\n\n- **gen_wiki_gpt2m_a100_s42_v3**: DONE (success) — \n- **mvp_v4_rep44**: DONE (success) — \n- **plan_006_s42**: DONE (failed) — \n- **plan_006_s42_resume**: DONE (killed) — \n- **gen_wiki_gpt2m_a100_s42_v2**: DONE (killed) — \n- **method_ablation_phase2**: DONE (success) — \n- **alpha_sweep_a025_s42_v3**: DONE (success) — \n- **method_ablation_phase1**: DONE (success) — \n- **plan_009_bootstrap_ty**: DONE (success) — \n- **mvp_v3_rep43**: DONE (failed) — \n- **mvp_v3_rep42**: DONE (failed) — \n- **mvp_v2_rep43**: DONE (killed) — \n- **mvp_v2_rep42**: DONE (killed) — \n- **mvp_rep43**: DONE (killed) — \n- **mvp_rep42**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- 14b_t10_a060_s43（准备中）\n- 14b_t10_a075_s43（准备中）\n- 14b_t10_a050_s43（准备中）\n- t15_a050_s42_fp32（准备中）\n- qwen35_dryrun_launch（准备中）\n\n## 近期结论\n- **null_t15_s42_fp32** (success): FPR verification at T=15: null condition (α=0.00) should show 0% PermG detection rate with longer observation window, confirming FPR control generalizes across T\n- **null_t15_s43_fp32** (success): FPR verification at T=15: null condition (α=0.00) should show 0% PermG detection rate with longer observation window, confirming FPR control generalizes across T\n- **null_gpt2m_s43_fp32** (success): Cross-architecture FPR verification: GPT-2-medium null (α=0.00) should show 0% PermG detection rate, confirming method is not architecture-specific\n\n## 趋势\n成功 153 / 负向 4 / 失败 22 / 共 209\n累计 GPU: 8.4h\nrobust_pairs_K3: 0 →（近 3 次 success）\ntotal_pairs: 6 →（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-17855: 无 GPU 信息\nwestd-19828: 空闲 cuda:0, cuda:1\n\n## 告警\n- mvp_rep42: 已被终止 — unknown\n- mvp_rep43: 已被终止 — unknown\n- mvp_rep44: 已被终止 — unknown\n- mvp_v2_rep42: 已被终止 — unknown\n- mvp_v2_rep43: 已被终止 — unknown\n- mvp_v2_rep44: 已被终止 — unknown\n- mvp_v3_rep42: 训练失败 — unknown\n- mvp_v3_rep43: 
…[truncated 1803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1857
}
```

</details>

---


### Tool call

_source line 1088 · 2026-05-24T13:57:51.856856+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1089 · 2026-05-24T13:57:52.509463+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{graphicx}
13	\usepackage{booktabs}
14	\usepackage{subcaption}
15	\usepackage{algorithm}
16	\usepackage{algpseudocode}
17	\usepackage{amsthm}
18	\newtheorem{theorem}{Theorem}
19	\newtheorem{proposition}[theorem]{Proposition}
20	\newtheorem{designprinciple}[theorem]{Design Principle}
21	\theoremstyle{definition}
22	\newtheorem{assumption}[theorem]{Assumption}
23	
24	\title{Characterizing the Detectability Landscape of Iterative Model Collapse}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\maketitle
30	
31	\input{abstract}
32	\input{introduction}
33	\input{related_work}
34	\input{theory}
35	\input{method}
36	\input{experiments}
37	\input{discussion}
38	\input{limitations}
39	\bibliography{references}
40	
41	\input{appendix}
42	
43	\end{document}
44	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 1090 · 2026-05-24T13:57:52.560063+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission deadline author guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission deadline author guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 1091 · 2026-05-24T13:57:59.285528+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission deadline author guidelines site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"}]

I found search results related to EMNLP 2026 and ACL conferences, but the results don't contain a specific EMNLP 20
…[truncated 1081 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "elapsed_ms": 6725
}
```

</details>

---


### Tool call

_source line 1092 · 2026-05-24T13:58:05.533964+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission deadlines ARR cycle June July"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission deadlines ARR cycle June July"
  }
}
```

</details>

---


### Tool call

_source line 1093 · 2026-05-24T13:58:06.136653+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 conference date location commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 conference date location commitment deadline"
  }
}
```

</details>

---


### Tool result

_source line 1094 · 2026-05-24T13:58:11.858848+00:00_

Web search results for query: "EMNLP 2026 conference date location commitment deadline"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Conference on Empirical Methods in Natural Language Processing (EMNLP), 2026 | ServiceNow AI Research","url":"https://www.servicenow.com/research/event/2026-emnlp.html"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"EMNLP 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Update EMNLP System Demonstrations Track with 2026 conference data · huggingface/ai-deadlines at 6a94f2c","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/6a94f2c940ba976564775b34f6b224b0f9ad638d"},{"title":"EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/emnlp"},{"title":"When is EMNLP 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/emnlp"}]

Based on the search results, here is the information about EMNLP 2026:

**Conference Date and Location:**
The conference will be held October 24-29 in Budapest, Hungary.

**Important Deadlines:**
Key dates include:
- ARR submission deadline (long & short papers): May 25, 2026
- Reviewer registration deadline for ALL authors: May 27, 2026
- 
…[truncated 616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "elapsed_ms": 5722
}
```

</details>

---


### Tool result

_source line 1095 · 2026-05-24T13:58:11.959940+00:00_

Web search results for query: "ACL Rolling Review 2026 submission deadlines ARR cycle June July"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL Rolling Review 2026 submission deadlines for the ARR cycle in June and July:

## ARR Cycle Schedule Changes

After extensive deliberation and soliciting community feedback, the ACL Peer Review Committee recommended to ACL exec to switch to 10-week cycles, with the new schedule starting in May 2025. This means that instead of 6 cycles a year there will generally be 5, but with more reasonable timelines for the review tasks and author response.

## Submission Deadline Pattern

The submission deadline is always the 15th of the month; other dates vary due to the leng
…[truncated 655 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "elapsed_ms": 6425
}
```

</details>

---


### Tool call

_source line 1096 · 2026-05-24T13:58:21.497885+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ACL Rolling Review\" 2026 author guidelines formatting template page limit anonymity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ACL Rolling Review\" 2026 author guidelines formatting template page limit anonymity"
  }
}
```

</details>

---


### Tool call

_source line 1097 · 2026-05-24T13:58:23.104470+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1098 · 2026-05-24T13:58:23.155187+00:00_

1	\begin{abstract}
2	Iterative training on model-generated text degrades distributional quality well before standard metrics flag collapse, yet detecting this degradation is difficult: the time series are short ($T{\leq}25$ generations), the signal grows sub-linearly with contamination fraction, and, as we show, the choice of statistical test alone can shift conclusions from universal detection to complete null.
3	We map the detectability landscape of this process on Pythia-410M across 13 contamination levels; cross-architecture evaluation at $\alpha{=}1.0$ supports forward detection in 11/15 conditions across five families (345M--6.9B), with four non-confirming conditions isolating distinct failure modes.
4	Permutation Granger causality (PermG) reveals a detection boundary that follows power-law scaling in observation length (leave-one-$T$-out CV: MAE${=}0.037$, 15/15 within CI) and four regimes, including a sharp onset where detection jumps from 0/8 to 6/8 within a 2-percentage-point contamination interval.
5	Five methods applied to identical data yield null-control false positive rates from 3\% to 92\%, exposing method sensitivity as a primary concern.
6	Entropy Granger-precedes diversity collapse by ${\geq}1$ generation (14/15 experiments), providing a canary whose triggered cessation substantially reduces peak perplexity in a proof-of-concept demonstration ($N{=}2$, $\alpha{=}1.0$).
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1099 · 2026-05-24T13:58:29.127228+00:00_

Web search results for query: ""ACL Rolling Review" 2026 author guidelines formatting template page limit anonymity"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, here's what I found about ACL Rolling Review 2026 author guidelines:

## Formatting and Template

Paper submissions must use the official ACL style template, and templates are available as an Overleaf template and also downloadable directly (Latex and Word). However, submissions based on the Word template will be desk-rejected starting from March 2026.

## Page Limits

The paper follows page limits (8 for long, 4 for short, not including limitations and ethical considerations). Additionally, the "Limitations" section (along with, optionally, a section for ethical considerations) may be up to one page and will not count toward the final page limit.

## Anonymity

Papers must not include authors' names and affiliations. More specifically, the submission must no
…[truncated 576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "elapsed_ms": 7629
}
```

</details>

---


### Tool call

_source line 1100 · 2026-05-24T13:58:46.657956+00:00_

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
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
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

_source line 1101 · 2026-05-24T13:58:47.461523+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1102 · 2026-05-24T13:58:53.794631+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1103 · 2026-05-24T13:58:54.800909+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 1104 · 2026-05-24T13:58:55.052192+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1105 · 2026-05-24T13:58:55.052642+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\cite{shumailov2024curse,alemohammad2024mad}.
5	This process can be triggered by vanishingly small synthetic fractions~\cite{dohmatob2025strong}: lexical diversity narrows, calibration deteriorates, and each generation inherits the biases of its predecessors.
6	As machine-generated text grows prevalent on the web, such feedback loops pose a growing risk to production pipelines, and by the time standard quality metrics register degradation, the distribution may have already shifted irreversibly.
7	
8	This threat motivates a fundamental question: \emph{what does the detectability landscape of model collapse look like?}
9	At what contamination level does statistical detection become possible, how does this boundary depend on observation length, and what structure does the landscape exhibit?
10	These questions are nontrivial because iterative training produces short, noisy time series (often fewer than 15 points), where detection power drops sharply~\cite{boettiger2012limits}. Moreover, model collapse is a first-order transition~\cite{truong2026phase}, structurally ruling out the critical-slowing-down early-warning signals that ecologists rely on~\cite{scheffer2009early} (\S\ref{sec:related_work}).
11	
12	We map this landscape on Pythia-410M~\cite{biderman2023pythia} across 13 contamination levels with multi-seed replication (Figure~\ref{fig:regime_map}), and find structured terrain rather than smooth degradation: detection is absent through $\alpha{=}0.45$, then jumps from 0/8 to 6/8 significant pairs within a 2-percentage-point interval, before a non-monotonic dip and eventual reliable detection above a power-law boundary $\alpha_c(T)$ (Eq.~\ref{eq:alpha-c-theory}).
13	Cross-architecture evaluation at $\alpha{=}1.0$ across five families (345M--6.9B) supports
…[truncated 2723 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1106 · 2026-05-24T13:58:55.554832+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 1107 · 2026-05-24T13:58:56.006975+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\paragraph{Design considerations.}
5	\label{sec:pitfalls}
6	We use Granger causality~\cite{granger1969investigating} to test temporal precedence---whether past canary values improve prediction of downstream metrics---not mechanistic causation; bivariate Granger tests cannot exclude confounders~\cite{shojaie2022granger}.
7	Lead-lag analysis in iterative model collapse is fragile along three axes, each documented with data from \S\ref{sec:regime}--\ref{sec:dose_response}.
8	\emph{Method sensitivity}: five detection methods applied to identical data yield forward significance rates spanning 0\% to 92\%, with inter-method agreement at $\kappa{=}0.185$.
9	\emph{Spurious regression}: first-differencing eliminates canary$\to$perplexity associations ($F{\approx}0$, $p{=}0.99$) while preserving canary$\to$diversity (24/24$\to$24/24), exposing an entire analysis channel as trend-driven~\cite{granger1974spurious}.
10	\emph{Regime dependence}: the same Granger test shifts from 0/8 to 6/8 significant pairs within a 2-percentage-point interval ($\alpha{=}0.48 \to 0.50$).
11	
12	\begin{figure*}[t]
13	\centering
14	\includegraphics[width=\textwidth]{figures/fig_framework.pdf}
15	\caption{Analytical framework. (a)~Iterative contamination loop: each generation trains on an $\alpha$-fraction synthetic mixture, from which canary (entropy) and downstream (distinct-$n$) metrics are extracted. (b)~Multi-method consensus test (MMCT): five detection methods with varying FPR profiles converge to a $K{\geq}3$ majority vote; PermG is selected as the lowest-FPR directional method. (c)~Signal$\times$Resolution model: sub-linear signal $S(\alpha)$ and finite resolution $R(\alpha)$ produce four detection regimes (blind, onset, dip, detection), with boundary $\alpha_c(T) \sim T^{-\gamma}$.}
16	\label{fig:framework}
17	\end{figure*}
18	
19	\subsection{Method Sensitivity Analysis}
20	\label{sec:mmct}
21	We compare five lead-lag detection methods in a multi
…[truncated 4899 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1108 · 2026-05-24T13:58:56.007425+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1109 · 2026-05-24T13:58:56.961118+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study the detectability landscape of iterative training collapse using Pythia-410M~\cite{biderman2023pythia} (410M parameters, decoder-only) as the primary architecture, with cross-architecture validation on five families (later verified in \S\ref{sec:generalization}).
8	Training data is drawn from WikiText-103~\cite{merity2017pointer} following the replace paradigm of~\citet{shumailov2024curse}: each generation fine-tunes on a mixture of $\alpha$ synthetic and $(1{-}\alpha)$ real data, generates 5{,}000 replacement samples, and fully replaces the synthetic pool (hyperparameters in Appendix~\ref{app:training_details}; notation in Appendix~\ref{app:background}).
9	We run $T{=}10$ generations across 13 contamination levels ($\alpha \in \{0.00, 0.05, 0.10, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.75, 1.00\}$, including null control) with multi-seed replication (4 seeds at $\alpha{=}1.0$; 3 at primary levels).
10	
11	We track two \emph{canary metrics} (token entropy and ECE) and three \emph{downstream metrics}: distinct-1, distinct-2~\cite{li2016diversity}, and perplexity (distinct-3: Appendix~\ref{app:distinct3}).
12	All hypothesis tests apply BH-FDR correction~\cite{benjamini1995controlling} at $q{=}0.05$; PermG uses 5{,}000 permutations on first-differenced series~\cite{shojaie2022granger} with maximum lag~5 (window sensitivity: Appendix~\ref{app:window_sensitivity}).
13	As in \S\ref{sec:method}, PermG tests temporal precedence, not causation.
14	
15	
16	\subsection{Sharp Detection Onset}
17	\label{sec:regime}
18	
19	Diversity collapse occurs at every contamination level: distinct-1 declines by $14.1\%$ even at $\alpha{=}0.0$ (fine-tuning drift) and by $40.3{\pm}0.3\%$ at $\alpha{=}0.25$ (3-seed mean).
20	Despite this ubiquitous degradation, Granger detectability is sharply regime-dependent.
21	PermG finds 0/8 canary$\to$downstream pairs FDR-sig
…[truncated 6992 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1110 · 2026-05-24T13:58:57.112121+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1111 · 2026-05-24T13:58:57.163511+00:00_

issues:
# ============================================================
# Round 1-10 历史 resolved — 保留跨轮次记录
# ============================================================
- id: "R1-N1"
  summary: "Ground-truth pairs 定义存在循环论证"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Effect-size GT 重定义完成。"
  resolution_round: 1

- id: "R1-N2"
  summary: "FPR=0% 标定仅基于单 seed"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "α=0.0 三 seed FPR 验证完成。"
  resolution_round: 1

- id: "R1-N3"
  summary: "α=0.50 和 α=0.75 仅 1 seed"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Multi-seed 补充完成。"
  resolution_round: 1

- id: "R2-N1"
  summary: "核心方法论为计量经济学已有知识的直接迁移，新颖性有限"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Round 1 三层定位 reframe 完成。"
  resolution_round: 1

- id: "R2-N2"
  summary: "α=0.75 multi-seed 实验未完成 + Appendix A 缺失"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "完成。"
  resolution_round: 1

- id: "R2-N3"
  summary: "实验规模过窄"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "跨架构验证已扩展至 15 model-seed 组合。"
  resolution_round: 1

- id: "R1-W1"
  summary: "Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致"
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "核心修复完成。"
  resolution_round: 1

- id: "R1-W2"
  summary: "PermG 缺少 power analysis"
  category: method
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Appendix N power analysis 完成。"
  resolution_round: 1

- id: "R1-W3"
  summary: "75% spurious-signal rate headline 依赖 unde
…[truncated 20907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1112 · 2026-05-24T13:59:17.632933+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read full project config head"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read full project config head"
  }
}
```

</details>

---


### Tool result

_source line 1113 · 2026-05-24T13:59:17.683727+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1114 · 2026-05-24T13:59:17.885459+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
  "offset": "80",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
    "offset": "80",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 1115 · 2026-05-24T13:59:18.036668+00:00_

80	The $\alpha{=}0.45$ column provides the sharpest validation of this left-shift: undetectable at $T{\leq}10$ (0/8), it crosses into reliable detection at $T{=}15$ (6/8, dual-seed) and remains there at $T{=}20$ (5/8) and $T{=}25$ (6/8).
81	The systematic 2/8 gap reflects MAUVE~\cite{pillutla2021mauve} floor saturation ($\mu{=}0.029$; \S\ref{sec:discussion}).
82	Cross-seed replication shows PermG within ${\pm}1$, though boundary cells exhibit sensitivity: $[0, 6]/8$ at ($T{=}10$, $\alpha{=}0.50$); $[0, 3]/8$ at ($T{=}20$, $\alpha{=}0.60$).
83	The $\alpha{=}0.60$ dip dissolves by $T{=}25$ ($5/8$), validating $\sqrt{T}$ power scaling; predict-then-verify yields 2/4 boundary predictions within CI (Appendix~\ref{app:t20_prediction_timeline}).
84	
85	
86	\subsection{Cross-Architecture Validation}
87	\label{sec:generalization}
88	
89	To test whether the phase-diagram structure is Pythia-specific, we evaluate PermG across 15 model-seed combinations spanning five families, scales 345M--6.9B, and two domains (Table~\ref{tab:generalization}).
90	Forward detection reaches ${\geq}6/8$ in 11/15 conditions, confirming that PermG generalizes to architectures satisfying the monotonic entropy decline assumption (Design Principle~\ref{thm:entropy_leads}).
91	Domain matters: C4 yields the strongest detection (Pythia-1.4B: 2/8 WikiText $\to$ 8/8 C4), suggesting that domain-specific mode structure affects detectability.
92	The four non-confirming conditions each isolate a distinct failure mode: precision sensitivity (GPT-2 bf16: 0/8 vs fp32: 6/8), bidirectional confounding (GPT-2 s43), seed dependence (Pythia-1.4B: s42 2/8, s43 6/8), and entropy decoupling (SmolLM3-3B: 3/8, whose non-monotonic entropy violates Design Principle~\ref{thm:entropy_leads}).
93	
94	\begin{table}[t]
95	\centering
96	\small
97	\caption{Cross-architecture PermG forward detection ($\alpha{=}1.0$, 15 model-seed combinations across five families---Pythia, GPT-2, OPT, Qwen, SmolLM3---and two domains; Padding-410M is
…[truncated 2616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1116 · 2026-05-24T13:59:23.864122+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1117 · 2026-05-24T13:59:24.215873+00:00_

1	\section{Discussion and Conclusion}\label{sec:discussion}
2	
3	\paragraph{Scope of claims.}
4	Our Granger-precedence claim is scoped to temporal predictive improvement~\cite{granger1969investigating,shojaie2022granger}: bivariate tests cannot exclude confounders, and the FPR CI ($[1.2\%, 30.4\%]$; \S\ref{sec:limitations}) means Type~I error may be non-negligible.
5	Entropy's greater sensitivity to distributional shifts than $n$-gram diversity means the temporal lead may partly reflect measurement sensitivity.
6	Five sync-dip cells are excluded from the boundary fit; including them raises MAE to 0.203 (Appendix~\ref{app:alpha_c_proof}).
7	Four of fifteen cross-architecture conditions do not confirm forward detection (\S\ref{sec:generalization}): non-monotonic entropy (SmolLM3-3B), precision sensitivity (GPT-2), and seed dependence (Pythia-1.4B; Appendices~\ref{app:cross_arch_fpr},~\ref{app:scale_14b}); $K{\geq}3$ consensus provides a fallback.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1118 · 2026-05-24T13:59:24.216276+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1119 · 2026-05-24T13:59:24.266806+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our landscape characterization uses Pythia-410M as the primary architecture; the phase diagram is Pythia-family-only (410M and 1.4B), and frontier-scale behavior ($>$7B) is untested.
5	With $T{\leq}25$ observations, statistical power remains limited ($\hat{\beta}{=}0.66$, CI $[0.24, 0.78]$); PermG's empirical FPR of $4/36$ (11.1\%, 6 seeds) is the lowest among directionally-specific methods but non-zero; the cluster-adjusted 95\% CI is $[1.2\%, 30.4\%]$ (within-seed ICC${=}0.14$).
6	Each cell's detection rate (e.g., 6/8) carries a wide binomial confidence interval (Clopper-Pearson: $[0.25, 0.92]$ for 6/8); the phase diagram should be read as a coarse topology rather than a precise probability surface.
7	Preliminary cross-architecture evaluation on GPT-2-medium reveals a substantially higher PermG FPR (6/12 pooled, 50\%), driven by ${\sim}4{\times}$ stronger null drift in entropy and ${\sim}7{\times}$ in distinct-3 (Appendix~\ref{app:cross_arch_fpr}); $K{\geq}3$ consensus maintains 0\% FPR across both architectures, though with a narrow margin (max 2/5 votes in the worst-case seed).
8	All experiments use full replacement~\cite{shumailov2024curse}; under data accumulation~\cite{dey2024breaking}, $\alpha_c$ would right-shift and the blind zone widen.
9	The sync-dip mechanism at $\alpha{=}0.60$ remains open.
10	All experiments use a single decoding strategy (temperature~$1.0$, top-$k{=}50$).
11	Lower temperatures accelerate mode concentration and should left-shift the detection boundary; nucleus sampling alters the effective diversity threshold $\epsilon$ in Design Principle~\ref{thm:entropy_leads}.
12	The directional effects are predictable---lower temperature compresses the landscape toward earlier detection---but the quantitative shift requires empirical calibration.
13	At boundary contamination levels ($\alpha \approx \alpha_c$), numerical precision (bf16 vs.\ fp32) can affect detection outcomes (GPT-2-medium: 
…[truncated 397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1120 · 2026-05-24T13:59:39.269101+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/agent/ -name \"*.yaml\" -o -name \"*.yml\" | xargs grep -l \"external_review\" 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Find external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/agent/ -name \"*.yaml\" -o -name \"*.yml\" | xargs grep -l \"external_review\" 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Find external review config"
  }
}
```

</details>

---


### Tool result

_source line 1121 · 2026-05-24T13:59:40.273632+00:00_

find: ‘/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/agent/’: No such file or directory
NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1122 · 2026-05-24T13:59:40.476494+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_12/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_12/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1123 · 2026-05-24T13:59:40.577417+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_12/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1124 · 2026-05-24T13:59:55.589160+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "distrib_canary_collapse",
  "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
  }
}
```

</details>

---


### Tool result

_source line 1125 · 2026-05-24T14:00:12.790682+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 17201
}
```

</details>

---


### Tool call

_source line 1126 · 2026-05-24T14:00:14.346840+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 统计有效性 + 实验设计**。\n\n## 论文信息\n- 标题: \"Characterizing the Detectability Landscape of Iterative Model Collapse\"\n- 论文路径: `projects/distrib_canary_collapse/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_12/submitted.pdf`\n\n## Venue 要求\n- **EMNLP 2026** (via ACL Rolling Review)\n- ARR 提交截止: 2026-05-25\n- Long paper: 8 页正文（不含 Limitations + Ethics），无限参考文献\n- ACL 模板, Double-blind\n- Limitations section 必须，最多 1 页，不计入页数\n\n## 你的审查侧重\n\n**核心关注**：\n1. **统计方法有效性**：PermG 的 FPR 控制（报告 11.1%，CI [1.2%, 30.4%]）、BH-FDR 在正依赖下的适用性、permutation test 在非平稳短序列上的可靠性\n2. **实验设计充分性**：每 cell 8 pairs 的统计效力、3-4 seeds 的 replication power、power-law boundary fit 的数据支撑\n3. **Claim 与证据匹配**：abstract/contributions 的 claim 是否被实验数据充分支撑（特别关注 cross-architecture \"five families\" 的实际覆盖度、intervention proof-of-concept 的证据强度）\n4. **方法论新颖性**：核心方法（permutation Granger）是计量经济学标准技术——迁移到 model collapse 领域的增量贡献评估\n5. **Detection boundary 的可靠性**：α_c(T) 幂律拟合仅基于 3 个 T 值（排除 sync-dip 后），γ=2.08 的置信度\n\n**附加检查**：\n- 多重比较校正是否恰当\n- 是否存在 p-hacking / post-hoc adjustment 风险\n- Null control 设计的充分性（6 seeds）\n- 数值精度（bf16 vs fp32）对结论的影响范围\n\n请按 ARR 审稿标准输出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment。",
  "project": "distrib_canary_collapse",
  "chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3",
  "director_session_key": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 统计有效性 + 实验设计**。\n\n## 论文信息\n- 标题: \"Characterizing the Detectability Landscape of Iterative Model Collapse\"\n- 论文路径: `projects/distrib_canary_collapse/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_12/submitted.pdf`\n\n## Venue 要求\n- **EMNLP 2026** (via ACL Rolling Review)\n- ARR 提交截止: 2026-05-25\n- Long paper: 8 页正文（不含 Limitations + Ethics），无限参考文献\n- ACL 模板, Double-blind\n- Limitations section 必须，最多 1 页，不计入页数\n\n## 你的审查侧重\n\n**核心关注**：\n1. **统计方法有效性**：PermG 的 FPR 控制（报告 11.1%，CI [1.2%, 30.4%]）、BH-FDR 在正依赖下的适用性、permutation test 在非平稳短序列上的可靠性\n2. **实验设计充分性**：每 cell 8 pairs 的统计效力、3-4 seeds 的 replication power、power-law boundary fit 的数据支撑\n3. **Claim 与证据匹配**：abstract/contributions 的 claim 是否被实验数据充分支撑（特别关注 cross-architecture \"five families\" 的实际覆盖度、intervention proof-of-concept 的证据强度）\n4. **方法论新颖性**：核心方法（permutation Granger）是计量经济学标准技术——迁移到 model collapse 领域的增量贡献评估\n5. **Detection boundary 的可靠性**：α_c(T) 幂律拟合仅基于 3 个 T 值（排除 sync-dip 后），γ=2.08 的置信度\n\n**附加检查**：\n- 多重比较校正是否恰当\n- 是否存在 p-hacking / post-hoc adjustment 风险\n- Null control 设计的充分性（6 seeds）\n- 数值精度（bf16 vs fp32）对结论的影响范围\n\n请按 ARR 审稿标准输出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment。",
    "project": "distrib_canary_collapse",
    "chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3",
    "director_session_key": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
  }
}
```

</details>

---


### Tool result

_source line 1127 · 2026-05-24T14:00:25.834987+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11488
}
```

</details>

---


### Tool call

_source line 1128 · 2026-05-24T14:00:26.539383+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + Framing + 写作质量 + 完整性**。\n\n## 论文信息\n- 标题: \"Characterizing the Detectability Landscape of Iterative Model Collapse\"\n- 论文路径: `projects/distrib_canary_collapse/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_12/submitted.pdf`\n\n## Venue 要求\n- **EMNLP 2026** (via ACL Rolling Review)\n- ARR 提交截止: 2026-05-25\n- Long paper: 8 页正文（不含 Limitations + Ethics），无限参考文献\n- ACL 模板, Double-blind\n- Limitations section 必须，最多 1 页，不计入页数\n\n## 你的审查侧重\n\n**核心关注**：\n1. **新颖性评估**：论文的核心贡献（detectability landscape mapping + method sensitivity as primary finding + canary mechanism）在 model collapse 文献中的增量知识——对比 Shumailov et al. (2024), Dohmatob et al. (2025), Truong & Truong (2026) 等\n2. **Framing 精准度**：title \"detectability landscape\" 是否准确反映内容（主要是 Pythia-410M 的 phase diagram + α=1.0 cross-arch）；contributions 的 scope 是否与实际交付匹配\n3. **Related Work 完整性**：是否遗漏关键相关工作（model collapse 检测/缓解、Granger causality 在 ML 中的应用、early warning signals 文献）\n4. **写作质量**：信息密度、可读性、逻辑流、notation 一致性、figure/table 信息效率\n5. **完整性**：是否所有 claim 都有对应的证据/引用、appendix 引用是否完整、limitations 是否诚实全面\n\n**附加检查**：\n- Abstract 是否在 200 words 以内（ARR 硬性要求）\n- 匿名规则是否遵守（无 self-citation leak）\n- 论文结构是否标准（Intro → Related Work → Theory/Method → Experiments → Discussion → Limitations）\n- 参考文献格式一致性\n\n请按 ARR 审稿标准输出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment。",
  "project": "distrib_canary_collapse",
  "chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3",
  "director_session_key": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查 **新颖性 + Framing + 写作质量 + 完整性**。\n\n## 论文信息\n- 标题: \"Characterizing the Detectability Landscape of Iterative Model Collapse\"\n- 论文路径: `projects/distrib_canary_collapse/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_12/submitted.pdf`\n\n## Venue 要求\n- **EMNLP 2026** (via ACL Rolling Review)\n- ARR 提交截止: 2026-05-25\n- Long paper: 8 页正文（不含 Limitations + Ethics），无限参考文献\n- ACL 模板, Double-blind\n- Limitations section 必须，最多 1 页，不计入页数\n\n## 你的审查侧重\n\n**核心关注**：\n1. **新颖性评估**：论文的核心贡献（detectability landscape mapping + method sensitivity as primary finding + canary mechanism）在 model collapse 文献中的增量知识——对比 Shumailov et al. (2024), Dohmatob et al. (2025), Truong & Truong (2026) 等\n2. **Framing 精准度**：title \"detectability landscape\" 是否准确反映内容（主要是 Pythia-410M 的 phase diagram + α=1.0 cross-arch）；contributions 的 scope 是否与实际交付匹配\n3. **Related Work 完整性**：是否遗漏关键相关工作（model collapse 检测/缓解、Granger causality 在 ML 中的应用、early warning signals 文献）\n4. **写作质量**：信息密度、可读性、逻辑流、notation 一致性、figure/table 信息效率\n5. **完整性**：是否所有 claim 都有对应的证据/引用、appendix 引用是否完整、limitations 是否诚实全面\n\n**附加检查**：\n- Abstract 是否在 200 words 以内（ARR 硬性要求）\n- 匿名规则是否遵守（无 self-citation leak）\n- 论文结构是否标准（Intro → Related Work → Theory/Method → Experiments → Discussion → Limitations）\n- 参考文献格式一致性\n\n请按 ARR 审稿标准输出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment。",
    "project": "distrib_canary_collapse",
    "chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3",
    "director_session_key": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
  }
}
```

</details>

---


### Tool result

_source line 1129 · 2026-05-24T14:00:28.100340+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1560
}
```

</details>

---


### Assistant

_source line 1130 · 2026-05-24T14:00:42.782708+00:00_

**Round 12 审稿已启动：**

| 角色 | 状态 | 侧重 |
|------|------|------|
| Reviewer 1 | ✅ 已派发 | 方法严谨性 + 统计有效性 + 实验设计 |
| Reviewer 2 | ✅ 已派发 | 新颖性 + Framing + 写作质量 + 完整性 |
| 视觉审查 | ✅ 已派发 | PDF 排版质量（非评分项） |
| 外部审稿 | ⏭️ 未启用 | — |

等待 Reviewer 返回独立审稿意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 107

## Round 107

2 recorded events


### User

_source line 1131 · 2026-05-24T14:08:40.223546+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：Characterizing the Detectability Landscape of Iterative Model Collapse

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 方法敏感性发现（同一数据 FPR 3%–92%）具有真正的实践价值，统计方法论严谨，但"detectability landscape"主要限于 Pythia-410M 单一架构，canary 机制（entropy 领先 diversity）近乎 tautological，标题的泛化承诺与实际交付的单架构 scope 不匹配。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法论严谨（BH-FDR、permutation test、specification curve），但 β 参数识别极差（MLE β̂=0.66 vs CV β=0.24，CI [0.24, 0.78]），PermG FPR CI 过宽 [1.2%, 30.4%]，削弱了 detection boundary 模型的可信度 |
| Excitement | 3.0/5 | 方法敏感性发现有实用价值，相图框架有新意；但 canary 机制（连续量先于阈值量）近乎 trivial，landscape 局限于单架构减弱了影响力 |
| Reproducibility | 4.0/5 | 超参详尽（Appendix A），5000 permutations、BH-FDR $q$=0.05 明确，1160 configuration specification curve，代码细节充分 |
| Reviewer Confidence | 4/5 | 熟悉 model collapse、Granger causality、统计检验文献，仔细检查了核心 claims |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Detection boundary 模型的参数不可识别性严重削弱 Contribution 1 的理论成分

- 具体位置：Section 4.2, Eq. 3, §4.2 para "However, β is poorly identified"
- 问题：power-law boundary $\alpha_c(T) = A \cdot T^{-1/(2\beta)}$ 的核心参数 $\beta$ 的 MLE 估计 $\hat{\beta}=0.66$（对应 $\gamma \approx 0.76$）与 cross-validation 估计 $\beta=0.24$（对应 $\gamma=2.08$）相差近 3 倍，profile 95% CI 为 [0.24, 0.78]。这意味着指数 $\gamma$ 可以从 0.64 到 2.08 之间任意取值，detection boundary 的形状本质上是未确定的。
- 为什么影响接收：Contribution 1 将 power-law detection boundary 列为核心发现之一（"PermG identifies a power-law detection boundary $\alpha_c(T)$"），但该 boundary 的定量形式高度不确定。定性结论（$T$ 越长检测越好）不需要 power-law 模型就能得出；定量 boundary 模型在现有数据量（$T \leq 25$, 13 个 $\alpha$ 值）下无法可靠标定。
- 建议修改方向：(1) 降低 power-law boundary 在 contribution statement 中的地位，明确标注为 exploratory/descriptive 而非 confirmed finding；(2) 或增加更多 $T$ 值的数据点以收窄 CI；(3) 在 abstract 和 introduction 中对 boundary 模型的不确定性给出更显著的 caveat。

**N2** [critical] 标题"Detectability Landscape"的 scope 与实际交付不匹配

- 具体位置：Title, Abstract, Contribution 1 (§1)
- 问题："Characterizing the Detectability Landscape" 暗示对 model collapse 可检测性的全面刻画，但实际上：(a) 完整的 $\alpha \times T$ phase diagram 仅在 Pythia-410M 上构建；(b) cross-architecture validation（Table 1）仅测试 $\alpha=1.0$（最极端情况），未测试中间 $\alpha$ 值的 landscape structure；(c) Pythia-1.4B 的部分 phase diagram（Appendix P, Table 15）仅覆盖 4 个 $\alpha$ 值 × 2 个 $T$ 值。cross-architecture 的 "landscape" 实际上只是 "one point on the landscape"（$\alpha=1.0$），不足以验证 landscape structure 是否跨架构保持。
- 为什么影响接收：Reviewer 和读者对标题设定的期望与论文实际交付之间存在显著落差。一个诚实的标题应反映这主要是 Pythia-410M 上的发现。
- 建议修改方向：(1) 修改标题以反映实际 scope，如 "Mapping Detection Regimes of Iterative Model Collapse on Pythia-410M"；(2) 或在 cross-architecture validation 中至少测试 2–3 个中间 $\alpha$ 值（如 0.50, 0.75），以验证 onset boundary 的跨架构一致性。

**N3** [critical] Canary 机制的 "formal design rationale"（Contribution 2）形式化了一个近乎 trivial 的关系

- 具体位置：Section 3 (Cascade Ordering), Design Principles 1–2
- 问题：Design Principle 1 本质上说的是 "连续度量（entropy）比离散阈值度量（distinct-n）更早响应分布变化"——这在信息论中几乎是公理性的。Entropy 对任何概率质量重分配都有一阶响应，而 distinct-n 只在 token 概率越过生成阈值 $\epsilon$ 时才变化。将此关系包装为 "Design Principle" 并作为三大贡献之一呈现，高估了其理论贡献。Design Principle 2（diversity lag $\geq 1$ generation）直接从 Principle 1 推出，不构成独立贡献。
- 为什么影响接收：将 well-known 的信息论直觉 formalize 后作为核心贡献 oversells the novelty。审稿人预期 "formal design rationale" 应提供 non-obvious 的 insights。
- 建议修改方向：(1) 将 cascade ordering 定位为 methodology 的一部分而非独立贡献；(2) 或者深化理论分析——例如推导 entropy-diversity lag 如何依赖于 $\alpha$、架构、数据分布的具体形式，给出可验证的定量预测。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Non-monotonic dip at $\alpha=0.60$ 作为 "四大 regime" 之一但机制完全未解释

- 具体位置：Section 5.3 (Fig. 4), Section 6, Limitations
- 问题：论文将 detection landscape 划分为四个 regime（blind, onset, dip, detection），但 "dip" regime（$\alpha=0.60$ 处 PermG 降至 0/8）的机制在全文中始终未解释（Limitations："the sync-dip mechanism at $\alpha=0.60$ remains open"）。一个核心发现的 1/4 是 unexplained anomaly，削弱了 "landscape characterization" 的完整性。Appendix F 的 TE 分析中 "high MI, low TE" 假设仅被 2/8 pairs 支持，被作者自己否定。
- 建议：(1) 考虑将 "four regimes" 降级为 "three regimes + one anomaly"；(2) 或提供更有力的机制假设并设计针对性实验。

**W2** [warning] Proof-of-concept intervention 极度有限但仍被列入 Contribution 1

- 具体位置：Section 5.6, Contribution 1 ("Canary-triggered cessation substantially reduces peak perplexity")
- 问题：intervention 实验仅在 $N=2$ architectures、$\alpha=1.0$（最极端条件）、post-hoc threshold（15%, "robust band" [10%, 22%]）下测试。这不是 "substantially reduces" 的充分证据，而是一个极窄条件下的 toy demonstration。CUSUM comparison（Appendix H）显示甚至简单阈值 detector 也能获得相同效果。
- 建议：(1) 从 Contribution 1 中剥离 intervention claim，改为独立的 "proof-of-concept" paragraph；(2) 或扩展到中间 $\alpha$ 值（如 0.50, 0.75）。

**W3** [warning] PermG FPR 的置信区间过宽，主方法的 standalone 可靠性存疑

- 具体位置：Section 4.1, Limitations
- 问题：PermG 的 pooled FPR 为 11.1%（4/36），cluster-adjusted 95% CI 为 [1.2%, 30.4%]。6 个 null seeds 的样本量不足以精确估计 FPR。虽然论文通过 MMCT consensus（K≥3, 0% FPR）来 condition all claims，但这本质上是用 ensemble 来掩盖单方法的不可靠——而 PermG 又被选为 "primary method"。GPT-2 上的 cross-architecture FPR 更高（6/12 = 50%），进一步削弱了泛化声明。
- 建议：(1) 增加 null seeds 到 $\geq 12$ 以收窄 FPR CI；(2) 更明确地区分 "PermG standalone" 和 "MMCT consensus" 的 reliability levels。

**W4** [warning] 页数可能超出 8 页限制

- 具体位置：PDF pages 8–9
- 问题：从 PDF 排版看，main text（Section 1–6，包含所有 figures/tables）延伸至 page 9 的约 60% 位置，然后才出现 Limitations section。估计 main text 约 8.5–8.6 pages，超出 EMNLP 2026 的 8-page strict limit 约 0.5 页。Table 1 和 Figure 6 被 LaTeX 浮动到 page 9，属于正文 Section 5.5/5.6 的内容。
- 建议：压缩正文（如合并 Section 3 到 Section 4 作为 subsection，或将 Table 1 移至 Appendix）以严格遵守 8 页限制。

**W5** [warning] 写作信息密度过高，可读性受影响

- 具体位置：全文，尤其是 Section 5.2–5.4
- 问题：几乎每句话都包含多个具体数字（如 "distinct-1 declines by 14.1% even at α=0.0 (fine-tuning drift) and by 40.3±0.3% at α=0.25 (3-seed mean)"），这使得关键 finding 淹没在数字洪流中。Phase diagram 的四个 regime 在 Section 5.3 才正式定义，但 Section 5.2 和 4.1 已大量使用这些术语。Abstract 虽然在 200 words 以内（~167 words），但同样过于拥挤。
- 建议：(1) 将精确数字移到 tables/figures，正文保留 qualitative 描述和关键 numbers；(2) 统一术语引入顺序——先定义四个 regime（可以在 Method 或 Experiments 开头用一段话），再在后续 sections 引用。

---

## 小问题（不影响接收）

- Section 4.2, Eq. 1: sigmoid 公式中 0.70 这个上界看起来是经验值（detection rate 的天花板），但没有给出选择理由。
- Section 5.1: $\alpha \in \{0.00, 0.05, 0.10, 0.25, ...\}$，从 0.10 到 0.25 的间隔突然变大（跳过了 0.15, 0.20），但 0.25–0.50 区间又密集采样——这一不均匀采样的理由未解释。
- Table 1 footnotes: "$^\dagger$Seed-dep." 和 "$^\S$s42 fp32: 6/8 fwd" 等脚注信息密集且难以解析，建议以完整 appendix table 替代。
- Section 2, para 1: "eight distinct notions of 'collapse'" (Schaeffer et al.) 被引用但未说明本文使用的是 D4–D6 中的哪一个具体 definition。虽然下文提到 "distributional shift family"，但建议明确选择理由。
- Appendix K (Table 5): SIGMA 和 DCES 在对比表中被标为 $\times$ across most dimensions，但 SIGMA (arXiv 2601.03385) 实际上有多架构验证（论文中 Fig. 4 覆盖了多个 LLM families）。建议核实对比表的准确性。
- Design Principle 使用 `\newtheorem{designprinciple}[theorem]{Design Principle}` 与 theorem 共享计数器——标号为 Design Principle 1 和 2 但显示为 Theorem 编号序列的一部分，导致 Theorem、Proposition、Design Principle 混在一个序列中，可能令读者混淆。

---

## 遗漏的相关工作

- **Distributional testing methods**: 论文仅比较了 time-series methods（Granger, cross-correlation），但未讨论 two-sample distributional tests（MMD, KS test, Wasserstein distance）作为替代 detection 方案。虽然 MAUVE 出现在部分实验中，但未被系统地比较或讨论其与 Granger-based methods 的互补性。
- **Online change-point detection literature**: 论文在 Appendix G 使用了 change-point detection，但 Related Work 未覆盖 online change-point detection 的经典文献（如 Adams & MacKay, 2007, Bayesian online changepoint detection），这些方法在 monitoring setting 中可能比 Granger causality 更自然。
- **Shi et al. (2025)** (cited as arXiv:2501.xxxxx, "A Closer Look at Model Collapse"): 虽然已在 Related Work 中引用，但其使用 entropy 作为 collapse diagnostic in diffusion models ($r=0.91$) 的发现与本文的 Design Principle 1 高度相关，应更充分地讨论异同。

---

## 主要优势

1. **方法敏感性发现是真正的贡献**：同一数据集上 5 种方法产生 FPR 3%–92% 的结果（Section 4.1, Fig. 5），这对 model collapse 文献是一个重要警示。将方法选择敏感性提升为 primary finding 而非 robustness check，体现了良好的科学态度。

2. **统计方法论严谨**：BH-FDR correction、null-control calibration、specification curve analysis（1,160 configurations, Appendix E）、Shapley value method decomposition（Appendix L）——这种级别的 robustness analysis 在 model collapse 文献中罕见。

3. **诚实的 Limitations section**：承认了 β 不可识别性、FPR CI 宽度、sync-dip 未解释、单架构局限性等问题。这比许多同类论文更透明。

4. **Appendix 的全面性**：19 页附录覆盖了 power analysis、non-stationarity robustness、Shapley decomposition、naive baselines comparison、CUSUM comparison 等，为主要 claims 提供了多角度支撑。

5. **Phase diagram 可视化**（Figure 1）直观地展示了 detection 的 regime structure，作为分析工具具有可复用性。

---

## 格式检查

| 检查项 | 状态 | 备注 |
|--------|------|------|
| Abstract ≤ 200 words | ✓ | ~167 words |
| Main text ≤ 8 pages | **可能违规** | ~8.5–8.6 pages (Table 1 + Figure 6 溢出到 page 9) |
| Limitations section | ✓ | 约 0.6 页，覆盖 6+ 个限制点 |
| Anonymity | ✓ | "Anonymous ACL submission"，无可识别的 self-citation |
| ACL template | ✓ | \usepackage[review]{acl} |
| Double-blind | ✓ | 未发现匿名泄露 |
| References format | ✓ | natbib, acl_natbib style |

---

**总结**：论文的方法敏感性发现和统计严谨性是真正的优势，但三个 Must-Fix 问题——detection boundary 模型的参数不可识别性（N1）、标题 scope 与实际交付的落差（N2）、以及 canary contribution 的 novelty overselling（N3）——共同将论文拉至 borderline。如果作者能 (a) 降低 power-law boundary 和 canary design rationale 的 claim 级别，(b) 修改标题以准确反映单架构 scope，(c) 增加至少 2–3 个中间 $\alpha$ 值的 cross-architecture validation，论文可以上升至 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1132 · 2026-05-24T14:08:48.833397+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 108

## Round 108

2 recorded events


### User

_source line 1133 · 2026-05-24T14:09:06.997594+00:00_

[Reviewer 2 审稿结果]:
已清理完毕（图片已被自动清理）。

**审稿完成。** 核心评分：Overall 3.5（Borderline Conference），Soundness 3.5，Excitement 3.0，Reproducibility 4.0。

三个 Must-Fix 问题：
1. Detection boundary 的 β 参数不可识别（MLE 0.66 vs CV 0.24），power-law 模型的定量形式高度不确定
2. 标题 "Detectability Landscape" 暗示跨架构全面刻画，但 phase diagram 仅在 Pythia-410M 上构建，cross-arch 仅测 α=1.0
3. Canary 机制（entropy 领先 diversity）近乎 tautological，作为三大贡献之一 oversells novelty

主要优势：方法敏感性发现（同一数据 FPR 3%–92%）是真正有价值的贡献，统计方法论严谨度在 model collapse 文献中罕见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1134 · 2026-05-24T14:09:17.758574+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 109

## Round 109

6 recorded events


### User

_source line 1135 · 2026-05-24T14:10:09.942205+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall Assessment**: 3.0 / 5 — Findings
**Confidence**: 4 / 5
**一句话总结**: 框架构想优秀且诚实报告了统计局限，但 PermG 的 FPR 膨胀（11.1%，CI 上界 30.4%）使检测边界的定量可靠性不足以支撑 abstract 所暗示的精度；跨架构 "five families" 宣称显著过度。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3 / 5 | 核心 Granger-precedence 框架合理；但 FPR 膨胀（11.1%，名义 5%）、幂律指数 poorly identified（§5.1 自认）、跨架构 FPR 50%（GPT-2-medium）构成实质性统计缺陷。方向性结论可信，定量精度不足。 |
| Excitement | 3 / 5 | 问题重要且时机恰当；相图式 detectability 刻画具有原创性；method-sensitivity finding（Claim 3）最有价值。但核心方法是标准计量经济学技术的迁移应用，landscape 仅覆盖一个模型族的完整 α 扫描。 |
| Reproducibility | 3.5 / 5 | 附录细节充分（超参、指标定义、seed 信息），specification curve 分析（1,160 配置）透明度高。未提及代码仓库（可能因 blind review），部分关键实现（permutation test、MMCT）需可运行代码验证。 |
| Datasets | 3 / 5 | 基于公开数据（WikiText-103, Pythia）但未发布处理后的实验数据或生成的训练语料。 |
| Software | 2 / 5 | 未提及任何代码/软件发布计划。 |

---

## Must-Fix 问题（影响接收决定）

**N1 [critical]: PermG FPR 11.1%（CI 上界 30.4%）使检测边界区域的 findings 不可靠**

- **具体位置**: §4.1, §5.1, §5.2, Table 7 (Appendix D), Limitations §6
- **问题**: 
  BH-FDR 校正在 q=0.05 下，名义 FPR 应 ≤5%。实际观测 FPR = 4/36 = 11.1%，cluster-adjusted 95% CI [1.2%, 30.4%]——上界达名义水平的 6 倍。

  核心矛盾在于：论文的检测 onset（§5.2 报告 α≈0.45→0.50 从 0/8 跳至 6/8）恰好位于 "信号勉强超过噪声" 的区域——这正是 FPR 膨胀最危险的地带。Table 7（Appendix D）显示 α=0.45 时两颗 seed 的 minimum BH-corrected p 分别为 0.059 和 0.091，仅略高于 q=0.05 阈值。如果真实 FPR 接近 CI 上界，那么 α∈[0.50, 0.60] 的 "检测" 中有多少是 FPR 驱动的？

  根源是 null control 样本太小：6 seeds × 6 pairs = 36 tests。Clopper-Pearson CI 在 N=36 时必然很宽，无法可靠估计 FPR 是否受控。

- **为什么影响接收**: 检测边界 α_c(T)——论文的核心贡献——正是从 detection onset 校准的。如果 α_c 因 FPR 膨胀向下偏移哪怕 0.05，整个 landscape 刻画都会移位。
- **建议修改方向**: (a) 增加 null control seeds 至 ≥12（≥72 tests，CI 宽度减半）；(b) 作为敏感性分析，用 Bonferroni 或更保守的校正重复主要结果；(c) 在 FPR CI 上界条件下报告保守版检测边界。

---

**N2 [critical]: 跨架构 "five families" 宣称显著过度**

- **具体位置**: Abstract, §5.5, Table 1 (p.9), Appendix Z (p.29)
- **问题**: 
  Abstract 称 "Cross-architecture evaluation at α=1.0 across five families...supports forward detection in 11/15 conditions。" 但存在三个关键问题：

  (1) **仅测试 α=1.0**（100% 合成数据）——这是最极端的情形，完整 landscape（α 扫描）仅存在于 Pythia-410M。α=1.0 的检测是最低标杆测试。

  (2) **GPT-2 medium null-control FPR 高达 50%**（Appendix Z, p.29: "50% vs. 11.1%, 6-pair basis"）。在 50% FPR 下，GPT-2 medium 上的任何 "检测" 都不可靠——coin flip 也能达到类似 detection rate。

  (3) 4 个 non-confirming cases 被归因为 "distinct failure modes"（§5.5），但同样可以解释为不同架构下 PermG 的 FPR 特征差异。论文没有区分这两种解释。

- **为什么影响接收**: 读者会将 "five families" 理解为广泛的可推广性，但实际证据支持的是 "一个模型族详细刻画，四个在最极端条件下浅尝辄止"。
- **建议修改方向**: (a) Abstract 重新措辞为 "Pythia-410M landscape with exploratory cross-architecture probes at α=1.0"；(b) GPT-2 medium 的 50% FPR 必须在正文（而非仅附录）中显著说明；(c) 从 contributions 中移除或大幅限定 "five families" 表述。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1 [warning]: 幂律边界指数 poorly identified 但在 abstract 中被高精度呈现**

- **具体位置**: §4.2, §5.1, Abstract (Eq. 3)
- **问题**: Abstract 呈现检测边界为干净的幂律，声称 "LOO-CV MAE=0.037, 15/15 within CI"。但 §5.1 明确承认 "β̂ is poorly identified: the MLE center estimate β̂=0.66...diverges substantially from the cross-validation estimate"。边界 α_c(T) = A·T^{−1/γ} 至多基于 5 个 T 值（T∈{5,10,15,20,25}），且 T=5 处 power <50%（Appendix N），实际可靠数据点仅 3-4 个用于拟合 2 参数模型——勉强可识别。

  LOO-CV MAE 0.037 具有误导性：在 3-4 个点上，几乎任何光滑单调函数都能拟合良好。它衡量的是样本内预测残差，不能代表参数识别精度。

  Appendix S (p.24) 进一步表明：sigmoid 形状回归的 SE(β) ≈ β，即形状参数本质上 unidentified。

- **建议**: (a) 显著报告指数的置信区间；(b) 将边界呈现为定性趋势（α_c 随 T 递减）而非精确幂律；(c) 校准 abstract 的精度声明。

**W2 [warning]: Sync-dip 排除是 post-hoc 操作，缺乏形式化证明**

- **具体位置**: §4.2, §5.3, Appendix S (p.24)
- **问题**: α∈[0.55, 0.65] 的非单调 dip 被排除在边界模型拟合之外，理由是它不符合幂律模式。但如果边界模型无法解释这一现象，可能说明模型本身是 mis-specified——也许真实边界不是简单幂律。论文提供了 post-hoc 解释（dip "eventually overcomes" with √T scaling），但没有正式检验 dip 是统计噪声还是真实现象。
- **建议**: 呈现包含和排除 sync-dip 的两组边界拟合；对 dip 的统计显著性进行形式化检验。

**W3 [warning]: Intervention proof-of-concept 证据过薄**

- **具体位置**: §5.6, Abstract ("proof-of-concept demonstration")
- **问题**: 干预仅在单一条件下测试（α=1.0, full replacement, Pythia-410M, V=2）。这是最有利于干预效果的设定。没有证据表明：(1) 干预在较低 α（检测本身不确定的区域）有效；(2) canary trigger 在正确时间触发（在下游损害之前）；(3) 干预不会在其他维度损害模型质量。
- **建议**: 至少扩展到 2-3 个 α 水平，或将措辞从 "proof-of-concept" 降级为 "illustrative example under favorable conditions"。

**W4 [warning]: MMCT 共识算法对 FPR 差异巨大的方法做等权投票缺乏正式证明**

- **具体位置**: §4.1, Appendix J (p.17)
- **问题**: MMCT 对 5 种方法等权投票，但这些方法的 FPR 从 3%（naive cross-correlation）到 92% 不等。等权 majority voting 意味着共识被高 FPR 方法主导。K≥3 阈值的选择缺乏对结果 Type I error rate 的正式分析。Appendix Q 显示 FPR-inverse weighting 不显著改变结果，但分析有限。
- **建议**: 提供 MMCT 共识在不同加权方案下的 analytical FPR。

**W5 [warning]: (α, T) grid 上的多重比较未校正**

- **具体位置**: §5, Figure 1
- **问题**: Phase diagram 在 ~65 个 (α,T) cell 上测试检测。"Sharp onset" 和 "phase boundary" 的声称源自该 grid 上的模式识别，但 cell 间未做多重比较校正。Specification curve（Appendix E）有助于缓解但未完全解决。

---

## 小问题（不影响接收）

1. **CUSUM 负面结果值得主文提及**: Appendix H 显示 CUSUM sequential monitoring 不优于简单阈值——这一实用性负面发现对从业者很重要，应在 §5.6 或 §6 中简要提及。
2. **术语 "14SM-6/8"（abstract）首次阅读不清晰**，需要上下文推断。
3. **表述精度矛盾**: 论文在 "MAE=0.037"（暗示高精度）和 "β̂ poorly identified"（承认低精度）之间交替使用，对粗略阅读者可能产生误导。
4. **bf16 vs fp32 影响**: §5.1 和 §5.5 报告 bf16 可改变检测结果（GPT-2-medium: 0/8 bf16 vs. 6/8 fp32），但这一关键敏感性在 abstract/contributions 中未反映。
5. **引用方面**: 可更多接合短时间序列变点检测的统计文献，以及置换 Granger 因果性验证方面的工作（如 Papana et al. 2013, Siggiridou & Kugiumtzis 2016）。

---

## 主要优势

1. **系统性相图方法**: 将 detectability 刻画为 (α, T) 空间中的结构化地形——这一框架视角在 model collapse 文献中是新颖的，为后续工作提供了有用的概念工具。
2. **Method-sensitivity finding（Claim 3）是最强贡献**: FPR 从 3% 到 92% 跨方法变化——这一元方法论发现具有超出本文具体应用的广泛价值，警示后续研究者检测方法选择本身是未被充分认识的混淆因素。
3. **诚实的 Limitations 章节**: §6 坦率承认 FPR 膨胀、power 限制和范围约束。这种 intellectual honesty 在投稿中少见，增加了可信度。
4. **Specification curve 分析**: 1,160 配置的系统变异展示了严肃的方法论意识，部分缓解了 researcher degrees of freedom 的担忧。
5. **Design Principles 1-2（§3）**: 为 canary metric 选择提供了清晰的理论框架（mode amplification → entropy responds first → diversity ≥ 2 generation cascade），将实证工作锚定在理论基础上。
6. **Entropy-leads-diversity cascade ordering**: 14/15 实验中 entropy Granger-precedes diversity collapse by 2+ generations——这一发现如果 FPR 问题解决后仍然稳健，具有实践预警价值。

---

## 给作者的问题

1. 如果 FPR 恰好在 5% 名义水平，检测边界会如何移动？能否提供 α_c(T) 在 FPR=5% vs 观测 11.1% 下的敏感性分析？
2. GPT-2 medium 的 50% FPR 是 PermG 在高 null drift 架构上的根本局限，还是可以通过架构特定校准解决？
3. Sync-dip 是否在所有 seed 中一致出现？有无证据排除 seed-specific artifact 的可能？
4. 要在 α=0.50 达到 ≥80% power，minimum T 是多少？Appendix N 的 power simulation 能否回答此问题？

---

## 总结

这篇论文以系统的框架视角处理了一个重要且时机恰当的问题。相图方法和 method-sensitivity finding 是真正的贡献。但统计层面存在实质性问题：(1) FPR 膨胀使边界区域的定量可靠性存疑；(2) 跨架构声称远超证据支撑；(3) 幂律指数 poorly identified 但被高精度呈现。这些问题可以通过增加 null control 样本、校准 claim 精度和限定 generalization 范围来解决。当前版本适合 Findings track；若统计基础加固并校准 claims，有潜力达到 Borderline Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1136 · 2026-05-24T14:10:48.017934+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] Detection boundary 模型的参数不可识别性严重削弱 Contribution 1 的理论成分\n- power-law boundary α_c(T) = A·T^{-1/(2β)} 的核心参数 β 的 MLE 估计 β̂=0.66 与 cross-validation 估计 β=0.24 相差近 3 倍，profile 95% CI 为 [0.24, 0.78]。指数 γ 可以从 0.64 到 2.08 之间任意取值，detection boundary 的形状本质上是未确定的。\n- 定性结论（T 越长检测越好）不需要 power-law 模型就能得出；定量 boundary 模型在现有数据量下无法可靠标定。\n\n**N2** [critical] 标题\"Detectability Landscape\"的 scope 与实际交付不匹配\n- 完整 α×T phase diagram 仅在 Pythia-410M 上构建；cross-architecture validation 仅测试 α=1.0（最极端情况）；Pythia-1.4B 的部分 phase diagram 仅覆盖 4α×2T。\n- 标题暗示跨架构全面刻画，实际主要是单架构 study。\n\n**N3** [critical] Canary 机制的 \"formal design rationale\"（Contribution 2）形式化了一个近乎 trivial 的关系\n- Design Principle 1 本质上说 \"连续度量（entropy）比离散阈值度量（distinct-n）更早响应分布变化\"——这在信息论中几乎是公理性的。\n- 将此关系包装为 \"Design Principle\" 并作为三大贡献之一，oversells novelty。\n\n### Should-Fix 问题\n\n**W1** Non-monotonic dip at α=0.60 作为 \"四大 regime\" 之一但机制完全未解释\n**W2** Proof-of-concept intervention 极度有限但仍被列入 Contribution 1\n**W3** PermG FPR 的置信区间过宽，主方法的 standalone 可靠性存疑\n**W4** 页数可能超出 8 页限制（Table 1 + Figure 6 溢出到 page 9）\n**W5** 写作信息密度过高，可读性受影响\n\n### 主要优势\n1. 方法敏感性发现（FPR 3%–92%）是真正的贡献\n2. 统计方法论严谨（BH-FDR、specification curve 1160 配置）\n3. 诚实的 Limitations section\n4. Appendix 全面性（19 页）\n5. Phase diagram 可视化具可复用性\n\n---\n\n请对以上 Must-Fix（N1-N3）和 Should-Fix（W1-W5）逐条回应 [AGREE] 或 [REBUT]。",
  "project": "distrib_canary_collapse",
  "chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3",
  "director_session_key": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] Detection boundary 模型的参数不可识别性严重削弱 Contribution 1 的理论成分\n- power-law boundary α_c(T) = A·T^{-1/(2β)} 的核心参数 β 的 MLE 估计 β̂=0.66 与 cross-validation 估计 β=0.24 相差近 3 倍，profile 95% CI 为 [0.24, 0.78]。指数 γ 可以从 0.64 到 2.08 之间任意取值，detection boundary 的形状本质上是未确定的。\n- 定性结论（T 越长检测越好）不需要 power-law 模型就能得出；定量 boundary 模型在现有数据量下无法可靠标定。\n\n**N2** [critical] 标题\"Detectability Landscape\"的 scope 与实际交付不匹配\n- 完整 α×T phase diagram 仅在 Pythia-410M 上构建；cross-architecture validation 仅测试 α=1.0（最极端情况）；Pythia-1.4B 的部分 phase diagram 仅覆盖 4α×2T。\n- 标题暗示跨架构全面刻画，实际主要是单架构 study。\n\n**N3** [critical] Canary 机制的 \"formal design rationale\"（Contribution 2）形式化了一个近乎 trivial 的关系\n- Design Principle 1 本质上说 \"连续度量（entropy）比离散阈值度量（distinct-n）更早响应分布变化\"——这在信息论中几乎是公理性的。\n- 将此关系包装为 \"Design Principle\" 并作为三大贡献之一，oversells novelty。\n\n### Should-Fix 问题\n\n**W1** Non-monotonic dip at α=0.60 作为 \"四大 regime\" 之一但机制完全未解释\n**W2** Proof-of-concept intervention 极度有限但仍被列入 Contribution 1\n**W3** PermG FPR 的置信区间过宽，主方法的 standalone 可靠性存疑\n**W4** 页数可能超出 8 页限制（Table 1 + Figure 6 溢出到 page 9）\n**W5** 写作信息密度过高，可读性受影响\n\n### 主要优势\n1. 方法敏感性发现（FPR 3%–92%）是真正的贡献\n2. 统计方法论严谨（BH-FDR、specification curve 1160 配置）\n3. 诚实的 Limitations section\n4. Appendix 全面性（19 页）\n5. Phase diagram 可视化具可复用性\n\n---\n\n请对以上 Must-Fix（N1-N3）和 Should-Fix（W1-W5）逐条回应 [AGREE] 或 [REBUT]。",
    "project": "distrib_canary_collapse",
    "chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3",
    "director_session_key": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
  }
}
```

</details>

---


### Tool result

_source line 1137 · 2026-05-24T14:11:07.860918+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19842
}
```

</details>

---


### Tool call

_source line 1138 · 2026-05-24T14:11:08.363402+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n**Overall**: 3.0 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical]: PermG FPR 11.1%（CI 上界 30.4%）使检测边界区域的 findings 不可靠\n- BH-FDR 校正在 q=0.05 下，名义 FPR 应 ≤5%。实际 FPR = 4/36 = 11.1%，CI [1.2%, 30.4%]。\n- 检测 onset（α≈0.45→0.50 从 0/8 跳至 6/8）恰好位于 \"信号勉强超过噪声\" 的区域。如果真实 FPR 接近 CI 上界，α∈[0.50, 0.60] 的 \"检测\" 中有多少是 FPR 驱动的？\n- Null control 仅 6 seeds × 6 pairs = 36 tests，太小无法可靠估计 FPR。\n- 建议：增加 null seeds 至 ≥12；用 Bonferroni 做敏感性分析；报告保守版检测边界。\n\n**N2** [critical]: 跨架构 \"five families\" 宣称显著过度\n- 仅测试 α=1.0（最极端情形），完整 landscape 仅存在于 Pythia-410M。\n- GPT-2 medium null-control FPR 高达 50%（Appendix Z），在此 FPR 下任何 \"检测\" 都不可靠。\n- 4 个 non-confirming cases 被归因为 \"distinct failure modes\"，但同样可以解释为不同架构下 PermG 的 FPR 特征差异。\n- 建议：Abstract 重新措辞；GPT-2 的 50% FPR 必须在正文显著说明；限定 \"five families\" 表述。\n\n### Should-Fix 问题\n\n**W1** 幂律边界指数 poorly identified 但在 abstract 中被高精度呈现\n- 基于 ≤5 个 T 值拟合 2 参数模型。LOO-CV MAE 0.037 具有误导性（3-4 点上几乎任何光滑函数都能拟合良好）。\n- 建议：呈现为定性趋势而非精确幂律��校准 abstract 精度声明。\n\n**W2** Sync-dip 排除是 post-hoc 操作，缺乏形式化证明\n- 如果边界模型无法解释 dip，可能说明模型 mis-specified。\n- 建议：呈现包含和排除 sync-dip 的两组拟合；对 dip 的统计显著性做形式化检验。\n\n**W3** Intervention proof-of-concept 证据过薄\n- 仅在 α=1.0, full replacement, N=2 下测试。无证据表明在较低 α 有效。\n- 建议：扩展到 2-3 个 α 水平，或降级措辞。\n\n**W4** MMCT 共识算法对 FPR 差异巨大的方法做等权投票缺乏正式证明\n- 5 种方法 FPR 从 3% 到 92%，等权投票被高 FPR 方法主导。K≥3 阈值选择缺乏 Type I error 分析。\n\n**W5** (α, T) grid 上的多重比较未校正\n- Phase diagram 在 ~65 个 cells 上测试，\"sharp onset\" 的声称源自 grid 模式识别，cell 间未做多重比较校正。\n\n### 主要优势\n1. 系统性相图方法——框架视角在 model collapse 文献中新颖\n2. Method-sensitivity finding（FPR 3%→92%）是最强贡献\n3. 诚实的 Limitations 章节\n4. Specification curve 分析（1,160 配置）\n5. Design Principles 1-2 为 canary 选择提供清晰理论框架\n6. Entropy-leads-diversity cascade（14/15 实验）有实践预警价值\n\n---\n\n请对以上 Must-Fix（N1-N2）和 Should-Fix（W1-W5）逐条回应 [AGREE] 或 [REBUT]。",
  "project": "distrib_canary_collapse",
  "chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3",
  "director_session_key": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n**Overall**: 3.0 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical]: PermG FPR 11.1%（CI 上界 30.4%）使检测边界区域的 findings 不可靠\n- BH-FDR 校正在 q=0.05 下，名义 FPR 应 ≤5%。实际 FPR = 4/36 = 11.1%，CI [1.2%, 30.4%]。\n- 检测 onset（α≈0.45→0.50 从 0/8 跳至 6/8）恰好位于 \"信号勉强超过噪声\" 的区域。如果真实 FPR 接近 CI 上界，α∈[0.50, 0.60] 的 \"检测\" 中有多少是 FPR 驱动的？\n- Null control 仅 6 seeds × 6 pairs = 36 tests，太小无法可靠估计 FPR。\n- 建议：增加 null seeds 至 ≥12；用 Bonferroni 做敏感性分析；报告保守版检测边界。\n\n**N2** [critical]: 跨架构 \"five families\" 宣称显著过度\n- 仅测试 α=1.0（最极端情形），完整 landscape 仅存在于 Pythia-410M。\n- GPT-2 medium null-control FPR 高达 50%（Appendix Z），在此 FPR 下任何 \"检测\" 都不可靠。\n- 4 个 non-confirming cases 被归因为 \"distinct failure modes\"，但同样可以解释为不同架构下 PermG 的 FPR 特征差异。\n- 建议：Abstract 重新措辞；GPT-2 的 50% FPR 必须在正文显著说明；限定 \"five families\" 表述。\n\n### Should-Fix 问题\n\n**W1** 幂律边界指数 poorly identified 但在 abstract 中被高精度呈现\n- 基于 ≤5 个 T 值拟合 2 参数模型。LOO-CV MAE 0.037 具有误导性（3-4 点上几乎任何光滑函数都能拟合良好）。\n- 建议：呈现为定性趋势而非精确幂律��校准 abstract 精度声明。\n\n**W2** Sync-dip 排除是 post-hoc 操作，缺乏形式化证明\n- 如果边界模型无法解释 dip，可能说明模型 mis-specified。\n- 建议：呈现包含和排除 sync-dip 的两组拟合；对 dip 的统计显著性做形式化检验。\n\n**W3** Intervention proof-of-concept 证据过薄\n- 仅在 α=1.0, full replacement, N=2 下测试。无证据表明在较低 α 有效。\n- 建议：扩展到 2-3 个 α 水平，或降级措辞。\n\n**W4** MMCT 共识算法对 FPR 差异巨大的方法做等权投票缺乏正式证明\n- 5 种方法 FPR 从 3% 到 92%，等权投票被高 FPR 方法主导。K≥3 阈值选择缺乏 Type I error 分析。\n\n**W5** (α, T) grid 上的多重比较未校正\n- Phase diagram 在 ~65 个 cells 上测试，\"sharp onset\" 的声称源自 grid 模式识别，cell 间未做多重比较校正。\n\n### 主要优势\n1. 系统性相图方法——框架视角在 model collapse 文献中新颖\n2. Method-sensitivity finding（FPR 3%→92%）是最强贡献\n3. 诚实的 Limitations 章节\n4. Specification curve 分析（1,160 配置）\n5. Design Principles 1-2 为 canary 选择提供清晰理论框架\n6. Entropy-leads-diversity cascade（14/15 实验）有实践预警价值\n\n---\n\n请对以上 Must-Fix（N1-N2）和 Should-Fix（W1-W5）逐条回应 [AGREE] 或 [REBUT]。",
    "project": "distrib_canary_collapse",
    "chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3",
    "director_session_key": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
  }
}
```

</details>

---


### Tool result

_source line 1139 · 2026-05-24T14:11:09.781595+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1418
}
```

</details>

---


### Assistant

_source line 1140 · 2026-05-24T14:11:13.941400+00:00_

交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 110

## Round 110

2 recorded events


### User

_source line 1141 · 2026-05-24T14:11:16.461625+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**评分**: Overall 3.0 (Findings)，Soundness 3/5，Excitement 3/5，Confidence 4/5。

**核心问题**（2 个 Must-Fix）：
1. PermG FPR 11.1%（CI 上界 30.4%）使检测边界区域的定量可靠性存疑——null control 仅 6 seeds/36 tests，太小无法精确估计 FPR
2. 跨架构 "five families" 显著过度宣称——仅测试 α=1.0 极端条件，GPT-2 medium FPR 高达 50%

**5 个 Should-Fix**：幂律指数 poorly identified 但高精度呈现、sync-dip 排除 post-hoc、intervention proof-of-concept 仅单一条件、MMCT 等权投票缺乏证明、(α,T) grid 多重比较未校正。

**主要优势**：系统性相图框架、method-sensitivity finding（FPR 3%→92%）是最强贡献、诚实的 Limitations 章节、1,160 配置的 specification curve 分析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1142 · 2026-05-24T14:11:24.999955+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 111

## Round 111

2 recorded events


### User

_source line 1143 · 2026-05-24T14:13:06.594482+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix

**[REBUT] R1-N1: PermG FPR 11.1%（CI 上界 30.4%）使检测边界区域的 findings 不可靠**

R1 的 FPR 担忧有道理，但"findings 不可靠"的结论过强，有三层证据缓解：

1. **Fisher exact test 提供了独立于 FPR 估计的 evidence**：Section 5.2 报告 0/64 pairs FDR-significant at α≤0.45 vs 18/32 at α≥0.50，p = 3.45×10⁻¹¹。即使 PermG 的真实 FPR 为 CI 上界 30%，在 64 次检测中全部为阴性（0/64）的概率 ≈ (0.70)⁶⁴ ≈ 10⁻¹⁰——这与 α≤0.45 的完全静默（0/64）不一致。因此 onset 的 **存在性** 不依赖于 FPR 的精确值。

2. **Cross-seed consistency**：Section 5.2 明确报告 3/3 fp32 seeds 在 α=0.50 均展示 0/8→6/8 跳变，且 α=0.45 处的 sub-threshold p 值为 0.059–0.091（Section 5.2, Appendix D Table 7），呈现连续梯度而非随机噪声。如果 6/8 来自 FPR，不同 seed 应产生不同数量的 false positives，而非统一的 6/8。

3. **MMCT consensus（K≥3）的 empirical FPR = 0%**：Section 4.1 明确说明所有 detection claims 都 conditioned on K≥3 consensus，在 null 条件下 0% FPR。R1 的 concern 更适用于 standalone PermG 而非论文实际使用的 consensus protocol。

**但我同意**：36-test null sample 确实太小。R1 建议增加至 ≥12 seeds 是合理的，也与我自己提出的 W3 一致。论文应更清楚地在正文中区分 "PermG standalone results"（FPR 不确定）和 "MMCT-conditioned findings"（empirically controlled FPR）。

**结论**：onset 的存在性是 robust 的（Fisher test + cross-seed），但 onset 的精确位置（α_c = 0.483 ± 0.006）在 FPR 不确定性下需要更宽的 error bars。R1 的要求（增加 null seeds、Bonferroni 敏感性）是合理的改进方向，但不构成否定 core finding 的理由。

---

**[AGREE] R1-N2: 跨架构 "five families" 宣称显著过度**

完全同意。这与我的 N2 几乎完全重合。补充两点强化 R1 的论点：

1. **GPT-2 medium 的 50% standalone FPR**（Appendix, cross-arch FPR section）是一个 disqualifying 级别的问题。论文虽然在 Limitations 中提及（"driven by ~4× stronger null drift in entropy and ~7× in distinct-3"），但 (a) 这一信息被埋在 Limitations 末尾而非正文显著位置，(b) GPT-2 在 Table 1 中仍然显示为 "6/8" 检测（s42 fp32），给读者以 cross-architecture validation 成功的印象，未充分警告其 FPR 背景。

2. **R1 提出的替代解释更值得重视**：4 个 non-confirming cases 被论文归因为 4 种 "distinct failure modes"（precision sensitivity, bidirectional confounding, seed dependence, entropy decoupling; Section 5.5），但同样可以解释为 PermG 在不同架构下 FPR/power 特征的差异——这是更简约的解释（1 个原因 vs 4 个 ad-hoc 原因）。论文未讨论这一 alternative explanation。

**建议**：Abstract 应将 "cross-architecture evaluation at α=1.0 across five families" 重新措辞为更审慎的表述，例如 "preliminary cross-architecture probes at α=1.0"；GPT-2 的 50% FPR 应在 Section 5.5 正文中以 caveat paragraph 形式呈现，而非仅在 Limitations 和 Appendix 中。

---

### Should-Fix

**[AGREE] R1-W1: 幂律边界指数 poorly identified 但被高精度呈现**

强烈同意。这与我的 N1 一致。补充一点：Abstract 中 "LOO-CV: MAE=0.037, 15/15 within CI" 读起来像是一个高精度的定量验证，但实际上 (a) LOO-CV 在 5 个 T 值上本质是 leave-one-out on 5 points，几乎任何单调函数都能获得类似 MAE；(b) "15/15 within CI" 反映的是 CI 足够宽（因为 β 本身的 CI [0.24, 0.78] 极宽），不是模型的高精度。这在 Section 4.2 中有 honest disclosure，但 Abstract 的措辞具有误导性。

---

**[AGREE] R1-W2: Sync-dip 排除是 post-hoc 操作**

同意。我在自己的 W1 中也提出了类似问题。补充：论文在 Section 6 报告了 sync-dip included 的 MAE = 0.203（vs excluded 0.037），这是一个 5.5× 的降级——说明 sync-dip 不是 boundary model 的 minor deviation，而是模型的 systematic failure。论文将 sync-dip 视为 "anomaly to be excluded" 而非 "evidence of model misspecification"，这一选择需要更强的 justification。

R1 建议并列呈现 included/excluded 两组拟合，是最低限度的修改。我进一步建议：如果 boundary model 无法解释 25% 的 grid cells（5 个 sync-dip cells out of ~20 above-boundary cells），应考虑 alternative models（如 piecewise sigmoid 或 non-parametric boundary）。

---

**[AGREE] R1-W3: Intervention proof-of-concept 证据过薄**

完全同意，与我的 W2 一致。补充：Appendix H 的 CUSUM 比较进一步削弱了 intervention 贡献——simple calibrated threshold 与 CUSUM 产生完全相同的 alarm time（generation 1），说明 canary mechanism 的 practical advantage 不来自 Granger-precedence 框架本身，而仅来自 entropy metric 的选择。一个 trivial 的 "monitor entropy, stop if it drops >15%" rule 无需任何 Granger analysis 即可实现相同效果。

---

**[REBUT] R1-W4: MMCT 等权投票缺乏正式证明**

部分不同意。R1 的 concern（高 FPR 方法主导投票）在理论上成立，但论文提供了充分的 empirical mitigation：

1. **Appendix M（Table 16）**：4 种 weighting schemes（equal, cap-5, cap-10, FPR-inverse cap-100）下 PermG 的 directional-method ranking 一致。Cap-10 和 cap-100 产生 identical Shapley values，因为 K≥3 threshold 由 3 个最小权重方法决定，不受高权重方法影响。

2. **NaiveXCorr 的影响被 K≥3 threshold 自然限制**：K≥3 要求至少 3/5 方法同意。NaiveXCorr（91.7% FPR）+ Threshold（27.8%）+ 任何第三个 = consensus。但在 null control 下，DiffXCorr（2.8% FPR）和 PermG（11.1%）很少同时给出 positive，所以 NaiveXCorr + Threshold 需要 TY（38.9%）来凑齐 K=3。empirical 结果是 null MMCT FPR = 0%。

3. **等权投票是论文的 deliberate choice**：Section 4.1 明确说明 FPR-inverse weighting 仅用于 exploratory ranking（Appendix），实际 detection results 用等权 K≥3。这避免了 weight 选择引入的另一层 degrees of freedom。

**但我同意**：K≥3 的 Type I error guarantee 是 empirical（0/null = 0%）而非 theoretical。对于 sample size = 36 的 null，0% empirical FPR 的 95% CI 上界约 8%（Clopper-Pearson）。论文应报告这个 CI。

---

**[REBUT] R1-W5: (α,T) grid 上的多重比较未校正**

部分不同意。R1 的 concern 在 principle 上合理，但对本文不完全适用：

1. **Phase diagram 的 primary claim 不是 "哪些 cells 显著"，而是 "onset 的存在和位置"**。论文使用 sigmoid regression（Section 5.2, R²=0.969）和 Fisher exact test（p=3.45×10⁻¹¹）来测试 onset——这些是 aggregate-level tests，不是 per-cell tests。Sigmoid regression 在 13 个 α 值上拟合一个 curve，这是一个 single test，不存在 multiplicity issue。

2. **Specification curve analysis（Appendix E, 1,160 configs）** 已经 systematically 检验了 onset 是否依赖于特定 analytical choices。这实质上是一种 multiverse analysis，功能上类似于 multiplicity correction。

3. **但 R1 有一个 valid 子点**：Phase diagram 中 "four regimes" 的识别确实来自 visual pattern recognition（Fig. 1），没有 formal test。特别是 sync-dip "regime" 仅基于 α=0.60 的 1–2 个 cells，这不足以构成 formal regime。

**结论**：Onset 的 primary claim 有 adequate 的统计支撑（sigmoid fit + Fisher test + spec curve），但 "four regimes" 的命名和分类需要更谨慎——如我在 W1 中建议，sync-dip 应从 "regime" 降级为 "unexplained anomaly"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1144 · 2026-05-24T14:13:16.948671+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 112

## Round 112

10 recorded events


### User

_source line 1145 · 2026-05-24T14:13:19.509155+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: Detection boundary 参数不可识别性**

同意 R2 的判断和严重性定级。我在自己的 W1 中也提出了同一问题，但 R2 正确地将其升级为 critical——因为定量 boundary 是 Contribution 1 的核心理论成分，而非锦上添花。

补充证据：
- §5.1 原文承认 "β̂ is poorly identified: the MLE center estimate β̂=0.66...diverges substantially from the cross-validation estimate"
- Appendix S (p.24) 的 sigmoid 形状回归显示 SE(β) ≈ β，即参数本质上 unidentified
- Abstract 的 "LOO-CV MAE=0.037, 15/15 within CI" 掩盖了参数不可识别性：在 3-5 个 T 值上任何光滑单调函数都能达到类似 MAE
- 如 R2 所说，"T 越长检测越好" 不需要幂律模型即可得出——这恰好与我的 W1 建议一致：应将边界呈现为定性趋势而非精确幂律

与我的评审的关系：R2-N1 与我的 W1 实质相同，但 R2 的严重性判定更准确。我修正自己的评估，同意这是 critical 级别。

---

**[AGREE] R2-N2: 标题 scope 与实际交付不匹配**

完全同意，这与我的 N2（跨架构 "five families" 过度宣称）本质上是同一个问题的不同表述。

补充证据：
- Table 1 (p.9)：跨架构仅测试 α=1.0，这是最极端的条件
- Appendix Z (p.29)：GPT-2 medium 的 null-control FPR 高达 50%（"50% vs. 11.1%, 6-pair basis"），使该架构上的任何 "检测" 都不可靠
- Pythia-1.4B 的 partial phase diagram 仅覆盖 "4α × 2T"（R2 观察准确），不足以独立构建 landscape
- 标题 "Detectability Landscape" 强烈暗示跨条件的全面刻画，但实际 landscape 仅在 Pythia-410M 一个架构上完整

R2 的 "标题-内容 scope mismatch" 框架比我的 "cross-architecture overclaiming" 更准确地捕捉了问题——不仅是跨架构声称过度，整个标题所承诺的 generality 都超出了实际交付。

---

**[REBUT] R2-N3: Design Principle 的 "near-trivial" 判定过于笼统**

R2 将 Design Principle 1 简化为 "连续度量比离散阈值度量更早响应"，认为这是信息论公理。我认为这一归纳不够精确，有两点 R2 未充分考虑：

(1) **Design Principle 1 的实质不是 "连续 vs 离散敏感性"，而是 mode amplification 下的特定级联机制**。§3 (p.3) 原文定义的是：在 iterative training 的 mode amplification 下，entropy 先于 diversity 下降，因为高概率 token 被进一步放大（概率质量集中），而 distinct-n 只有在 token 概率低于生成阈值后才变化。这不是通用信息论命题，而是关于 iterative model collapse 特定动力学的机制性陈述。

(2) **经验验证提供了非 trivial 的定量结果**：14/15 实验中 entropy Granger-precedes diversity by ≥2 generations（§4.1, §5.2）。≥2 generation 的 lag 结构不能从 "entropy 比 distinct-n 更敏感" 这一直觉先验推导出来——lag 可以是 0、1、或更多代。这个定量结果在先验上是 uncertain 的。

但我**部分同意** R2 的关切：将此经验发现包装为 "formal design rationale" 并列为三大 contributions 之一确实 oversells——它更适合定位为 "empirically validated ordering principle" 而非 "formal design rationale"。贡献的核心在经验验证，不在形式化本身。

**结论：R2 对 overclaiming 的诊断正确，但 "near-trivial" 的判定过强。建议降级贡献措辞而非质疑内容本身。严重性应为 should-fix 而非 critical。**

---

### Should-Fix 问题

**[AGREE] R2-W1: Sync-dip 机制未解释**

同意。我在 W2 中提出了相关问题（post-hoc 排除缺乏形式化证明）。§5.3 提供的 "synchronous diversity-perplexity co-movement" 解释是描述性的，未给出 α≈0.60 处特异性发生的机制性原因。将 dip 命名为 "四大 regime 之一" 但无法解释其成因，确实降低了 landscape 刻画的完整性。

---

**[AGREE] R2-W2: Intervention proof-of-concept 过于有限**

完全同意，与我的 W3 一致。单一条件（α=1.0, Pythia-410M, V=2）是最有利情形。将其列入 Contribution 1 进一步加重了 overclaiming。

---

**[REBUT] R2-W3: PermG FPR 的严重性被低估——应升级为 Must-Fix**

我与 R2 在问题识别上完全一致，但**不同意将其仅列为 should-fix**。

我在自己的审稿中将 PermG FPR 问题列为 **N1 [critical]**，理由如下：
- FPR 11.1%（4/36），cluster-adjusted 95% CI [1.2%, 30.4%]——上界达名义 5% 的 6 倍（§5.1, Limitations §6）
- Table 7 (Appendix D)：α=0.45 时 min BH-corrected p 为 0.059 和 0.091，仅略高于 q=0.05。这意味着检测 onset 区域的 findings 位于 FPR 膨胀最危险的地带
- Null control 仅 6 seeds（36 tests），CI 在此样本量下必然极宽
- GPT-2 medium 的 FPR 高达 50%（Appendix Z），表明这不是 Pythia-specific 的 artifact

FPR 膨胀直接威胁检测边界 α_c(T) 的校准——边界从 detection onset 推导，而 onset 恰好在 FPR 影响最大的区域。这不是 "影响评分但不一票否决" 的问题，而是动摇核心 quantitative claim 的问题。

**建议 Director 将此升级为 Must-Fix 级别。**

---

**[AGREE] R2-W4: 页数可能超限**

R2 的观察合理。Table 1 和 Figure 6 是 §5 主文内容（分别被 §5.5 和 §5.6 引用），但位于 page 9。根据 EMNLP 2026 规则，主文限 8 页（Limitations 不计入），主文元素溢出到 page 9 构成超限。

补充：这可能是 LaTeX float 机制导致的技术性问题（table/figure 被 LaTeX 浮动到下一页），通过调整 float placement 可修复。但作者有责任确保提交版本符合页数要求。如果 Table 1 被移至 Appendix 并在正文中引用，可同时解决页数问题和信息密度问题。

---

**[AGREE] R2-W5: 写作信息密度过高**

同意。主文在 8 页内尝试覆盖：phase diagram、detection boundary model、method sensitivity、cascade ordering、cross-architecture validation、intervention proof-of-concept——六大主题。每个主题都被压缩到难以充分展开的程度。

建议：将 cross-architecture validation（§5.5）和 intervention（§5.6）移至 appendix 作为 preliminary results，主文聚焦 Pythia-410M landscape + method sensitivity + cascade ordering 三个核心主题。这也有助于解决 R2-N2 的 scope mismatch 问题。

---

### 总结：两位 Reviewer 的共识与分歧

| 问题 | R1 评级 | R2 评级 | 共识 |
|------|---------|---------|------|
| 幂律参数不可识别 | W1 (should-fix) | N1 (critical) | **共识：critical**（R1 修正） |
| 标题/跨架构 scope | N2 (critical) | N2 (critical) | **共识：critical** |
| Design Principle trivial | 未提 | N3 (critical) | **分歧：R1 认为 should-fix** |
| Sync-dip 机制 | W2 (should-fix) | W1 (should-fix) | **共识：should-fix** |
| Intervention 过薄 | W3 (should-fix) | W2 (should-fix) | **共识：should-fix** |
| PermG FPR | N1 (critical) | W3 (should-fix) | **分歧：R1 认为 critical** |
| 页数超限 | 未提 | W4 (should-fix) | R1 同意 |
| 信息密度 | 未提 | W5 (should-fix) | R1 同意 |

**关键分歧点**：R2-N3（Design Principle trivial）和 R2-W3/R1-N1（PermG FPR 严重性）。建议 Director 对这两点做出裁决。

---

[Reviewer 2 审稿结果]:
交叉回应已提交。

汇总：7 条中 **5 条 AGREE**（R1-N2, W1, W2, W3 完全同意；R1-N1 同意 null sample 不足但反驳 "findings 不可靠" 的结论），**2 条 REBUT**（W4 等权投票有 empirical mitigation；W5 primary onset claim 有 adequate 统计支撑，但 "four regimes" 命名需降级）。与 R1 的核心共识：cross-architecture scope 被 oversold、power-law boundary 参数不可识别、intervention 证据过薄。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1146 · 2026-05-24T14:13:40.790744+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1147 · 2026-05-24T14:13:41.092468+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T13:59:58.947992+00:00\", \"completed_at\": \"2026-05-24T14:04:03.073069+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 6-7-8\", \"message\": \"布局节奏失衡：pages 6-7 连续纯文本无任何 display item，而 page 8 塞入 Figures 3/4/5 三个图导致每图面积偏小。建议将 Figure 3 或 Figure 4 前移至 page 6 或 7，均衡视觉节奏\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figures 3-5 因压缩导致 axis labels、legend 字号接近可读下限（约正文 65-70%），建议至少保证 ≥70%\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-2\", \"message\": \"前 2 页无视觉锚点，第一个 display item 在 page 3。ACL 格式下可接受，但若能在 page 2 底部引入一个小型概览图或将 Figure 1 提前，可强化审稿人第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 30\", \"message\": \"末页内容填充约 55-60%，略低于 2/3 标准（appendix 末页，非严重问题）\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 热力图单元格内分数标注（如 \\\"5/8\\\"）字号偏小，高分辨率打印下可读但 PDF 屏幕阅读时需放大\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1148 · 2026-05-24T14:13:41.092810+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1149 · 2026-05-24T14:13:41.143531+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1150 · 2026-05-24T14:17:30.105794+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distrib_canary_collapse",
  "issues_yaml": "issues:\n# ============================================================\n# Round 1-11 历史 resolved — 保留跨轮次记录\n# ============================================================\n- id: \"R1-N1\"\n  summary: \"Ground-truth pairs 定义存在循环论证\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Effect-size GT 重定义完成。\"\n  resolution_round: 1\n\n- id: \"R1-N2\"\n  summary: \"FPR=0% 标定仅基于单 seed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"α=0.0 三 seed FPR 验证完成。\"\n  resolution_round: 1\n\n- id: \"R1-N3\"\n  summary: \"α=0.50 和 α=0.75 仅 1 seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Multi-seed 补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-N1\"\n  summary: \"核心方法论为计量经济学已有知识的直接迁移，新颖性有限\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Round 1 三层定位 reframe 完成。\"\n  resolution_round: 1\n\n- id: \"R2-N2\"\n  summary: \"α=0.75 multi-seed 实验未完成 + Appendix A 缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-N3\"\n  summary: \"实验规模过窄\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"跨架构验证已扩展至 15 model-seed 组合。\"\n  resolution_round: 1\n\n- id: \"R1-W1\"\n  summary: \"Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"核心修复完成。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"PermG 缺少 power analysis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Appendix N power analysis 完成。\"\n  resolution_round: 1\n\n- id: \"R1-W3\"\n  summary: \"75% spurious-signal rate headline 依赖 underpowered T-Y\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W4\"\n  summary: \"α=0.75 单 seed borderline 结果不应出现在 abstract\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W5\"\n  summary: \"Toda-Yamamoto 纳入理由表述不充分\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W6\"\n  summary: \"可重复性信息不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"超参补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-W3\"\n  summary: \"Token entropy canary 仅在 α=1.0 验证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"缺少独立 Limitations section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W5\"\n  summary: \"缺少 AI Writing Disclosure\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W6\"\n  summary: \"缺少 canary→perplexity 为何 spurious 的深入解释\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF1\"\n  summary: \"遗漏 Granger & Newbold (1974)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF2\"\n  summary: \"遗漏 Hataya et al. (2023) 和 Seddik et al. (2024)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W1-old\"\n  summary: \"Citation key chen2025scales 与实际作者不匹配\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"F2-W3\"\n  summary: \"Section 3 承诺的三项附录内容缺失\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"附录内容补充完成。\"\n  resolution_round: 3\n\n- id: \"F2-W8\"\n  summary: \"格式不合规：未使用 ACL 模板\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"ACL 模板迁移完成。\"\n  resolution_round: 2\n\n- id: \"F2-REF1\"\n  summary: \"遗漏 arXiv:2502.15654\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF1\"\n  summary: \"遗漏 arXiv:2602.10531\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF2\"\n  summary: \"遗漏 arXiv:2505.19046\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF3\"\n  summary: \"遗漏 arXiv:2510.16657\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF5\"\n  summary: \"Appendix H CUSUM 未引用 Page (1954)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F4-REF1\"\n  summary: \"遗漏 Truong & Truong (2026)\"\n  category: reference\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"引用已添加并在 §1/§2 讨论。\"\n  resolution_round: 6\n\n- id: \"F4-REF3\"\n  summary: \"遗漏 Benjamini & Yekutieli (2001)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"§4 现引用 benjamini2001control。\"\n  resolution_round: 5\n\n- id: \"F2-REF3\"\n  summary: \"Dakos et al. (2012) + Schreiber (2000) + Phipson & Smyth (2010) 在 bib 中但正文未引用\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"引用补充完成。\"\n  resolution_round: 4\n\n- id: \"F6-W2\"\n  summary: \"页数可能超限\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"R8 PDF 审查确认主体 8 页合规。\"\n  resolution_round: 8\n\n- id: \"F2-W6b\"\n  summary: \"'Methodological pitfalls' 有 straw-man 倾向\"\n  category: framing\n  severity: major\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 8\n  resolution: \"全文已改为 'design considerations'。R8 fresh review 未再提及。\"\n  resolution_round: 8\n\n- id: \"F5-N2\"\n  summary: \"T=10 统计效力不足(power≈37%), sharp onset 可能是 power artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Power simulation 重写通过 Reviewer #75。Steepness comparison k_obs=18.79 vs k_H0=6.14 (ratio 3.06×, CI non-overlapping) 写入 method.tex + experiments.tex + appendix。Dense α 证据 (17 points, sigmoid k=15.7) 额外支撑。\"\n  resolution_round: 9\n  first_raised_round: 5\n  last_seen_round: 9\n\n- id: \"F2-W5\"\n  summary: \"Token entropy → distinct-n 机械耦合 confound 未排除\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Metric structure 分析完成：mauve attribution 100% 确认非 metric coupling。ECE→distinct 独立于 token_entropy→distinct 路径。讨论已添加到 discussion.tex。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 9\n\n- id: \"F2-W2\"\n  summary: \"Specification curve analysis 定位不精确\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Appendix E 已改称 'systematic robustness analysis'。R8/R9 fresh review 未再提及。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 8\n\n- id: \"F8-C2\"\n  summary: \"Discussion §6 过于简短(~100词)\"\n  category: writing\n  severity: major\n  status: resolved\n  resolution: \"Discussion 扩展至 20 行。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C3\"\n  summary: \"与 Schaeffer et al. (2025) '8 种 collapse 定义' 的关系讨论不充分\"\n  category: framing\n  severity: major\n  status: resolved\n  resolution: \"Schaeffer taxonomy 映射已添加到 related_work.tex。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C1\"\n  summary: \"Du & Tanaka-Ishii (2026) 引用三重错误\"\n  category: reference\n  severity: critical\n  status: resolved\n  resolution: \"§2 已修正为 'related but distinct phenomenon'。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"R9-C1\"\n  summary: \"FPR CI method.tex 内部矛盾\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"FPR=10% MMCT sensitivity analysis 完成。Paper Agent 统一 CI 处理。\"\n  resolution_round: 9\n  first_raised_round: 9\n  last_seen_round: 9\n\n- id: \"F8-N1\"\n  summary: \"BH-FDR 在强正回归依赖下适用性讨论不充分\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"PRDS 假设适用性讨论已添加。FPR sensitivity analysis 额外支撑。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 10\n\n- id: \"F8-REF1\"\n  summary: \"遗漏引用：online/continual learning 下 model collapse 检测\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"related_work.tex 已添加 scope 区分。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F2-W11\"\n  summary: \"α_c SE=0.006 低估真实 seed 不确定性\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"被 F2-W4b/F2-W6 的统计基础问题覆盖。\"\n  resolution_round: 11\n  first_raised_round: 2\n  last_seen_round: 10\n\n- id: \"F8-N2\"\n  summary: \"未讨论为何选择经典 permutation Granger 而非 neural Granger causality\"\n  category: method\n  severity: minor\n  status: resolved\n  resolution: \"§4 已添加 T≤25 理由。§2 引用 neural Granger 文献。\"\n  resolution_round: 11\n  first_raised_round: 8\n  last_seen_round: 11\n\n- id: \"R9-REF2\"\n  summary: \"遗漏引用：Steegen et al. (2016) multiverse analysis\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 steegen2016increasing。\"\n  resolution_round: 11\n  first_raised_round: 9\n  last_seen_round: 11\n\n- id: \"R10-REF2\"\n  summary: \"遗漏引用：Mitchell et al. (2023) DetectGPT\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 mitchell2023detectgpt。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-REF4\"\n  summary: \"遗漏引用：Padmakumar et al. (2024)\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 padmakumar2024writing。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n\n# ============================================================\n# 活跃 issues — Round 12\n# ============================================================\n\n- id: \"F3-J4\"\n  summary: \"PermG FPR 超出 nominal 5%，architecture-dependent\"\n  category: method\n  severity: critical\n  status: open\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 3\n  last_seen_round: 12\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 MF-1。6轮 mild hedging 失败。本轮更激进：boundary 加 ±0.05 uncertainty，onset 加 expected FP under null=0.9/8 论证。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 双方共识 critical。R1 主张 onset 区域 (α≈0.50) 恰好在 FPR 膨胀最危险地带。R2 缓解：Fisher exact p=3.45e-11 + cross-seed 3/3 一致性证明 onset 存在性 robust，但精确位置需更宽 error bars。GPT-2 50% FPR 仍仅在 Appendix/Limitations。\"\n  action_items:\n    - round: 12\n      action: \"增加 null seeds 至 ≥12 或在正文报告保守版边界（Bonferroni sensitivity）；GPT-2 50% FPR 移入正文 §5.5 显著标注\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W4b\"\n  summary: \"幂律边界 α_c(T) 拟合基础薄弱\"\n  category: framing\n  severity: critical\n  status: open\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 12\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 MF-3。6轮降级不够。本轮：abstract 删除具体 γ，method.tex 改为 'consistent with power-law scaling'。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 双方共识 critical。β MLE=0.66 vs CV=0.24 (CI [0.24,0.78]) 使 γ 从 0.64 到 2.08 任意。LOO-CV MAE=0.037 在 3-5 点上无鉴别力。R11 的 'consistent with' 降级被判定不够——abstract 仍呈现为高精度定量结果。\"\n  action_items:\n    - round: 12\n      action: \"Abstract 删除 MAE=0.037 和 15/15 within CI；将 boundary 重新定位为 qualitative trend（α_c 随 T 递减）而非精确幂律；正文报告 γ 的完整 CI\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W2b\"\n  summary: \"'Detectability landscape' framing 承诺超过交付\"\n  category: framing\n  severity: critical\n  status: open\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 12\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 MF-2。本轮 scope 收紧 abstract/intro：full grid 限定 Pythia-410M，cross-arch 限定 α=1.0。保留 title 和 five families。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 双方共识 critical。R11 的收紧被判定仍不够。标题暗示跨架构全面刻画，实际 landscape 仅 Pythia-410M；cross-arch 仅 α=1.0 最极端条件。GPT-2 50% FPR 使该架构 findings 不可靠。R1 提出 4 个 non-confirming cases 可能是 FPR 差异而非 distinct failure modes（更简约解释）。\"\n  action_items:\n    - round: 12\n      action: \"标题考虑修改以反映实际 scope；Abstract 将 cross-arch 重新措辞为 exploratory probes；正文 §5.5 添加 alternative explanation paragraph（FPR 差异 vs distinct failure modes）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W10\"\n  summary: \"Cross-architecture 'coupling preserved' 条件 post-hoc\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 12\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 SF-3。改为 'partial validation with notable exceptions'。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 与 F2-W2b 合并。4 non-confirming cases 的 post-hoc failure mode 归因缺乏独立验证。\"\n  action_items:\n    - round: 12\n      action: \"合并到 F2-W2b 的 scope 重新定位\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-N1\"\n  summary: \"统计功率 β=0.66 CI [0.24,0.78] 使检测边界定量解读不可靠\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"新 MF-4。method.tex 加 power limitation 句：T≤8 power <50%，短 T 的 boundary 是上界。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 与 F2-W4b 合并。β 不可识别性使整个 boundary model 的定量形式不确定。\"\n\n- id: \"F2-W7\"\n  summary: \"Intervention 实验薄弱\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 12\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 SF-2。Abstract 删 '64%'，改为定性 + proof-of-concept。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 双方共识 should-fix。仅 α=1.0/N=2/post-hoc threshold。R2 补充：Appendix H CUSUM comparison 显示 simple threshold 同效，削弱 Granger 框架的 practical advantage。建议从 Contribution 1 剥离。\"\n  action_items:\n    - round: 12\n      action: \"从 Contribution 1 剥离 intervention；独立为 proof-of-concept paragraph 或 appendix\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R12-N1\"\n  summary: \"Design Principle 'formal design rationale' 作为独立贡献 oversells\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 判 critical（near-trivial），R1 rebut（mode amplification 下的特定机制非公理，≥2 gen lag 非先验可知）。Director 裁定 warning：内容非 trivial 但 contribution framing 需降级。\"\n  action_items:\n    - round: 12\n      action: \"将 Contribution 2 从 'formal design rationale' 降级为 'empirically validated ordering principle'；不作为独立 numbered contribution\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-W1\"\n  summary: \"'3%-92%' FPR 范围含失效方法 NaiveXCorr\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"保留 3%-92% 全范围但正文首次出现时区分。与 R10-SF4 合并。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独提及。可能已充分处理。\"\n\n- id: \"R11-W2\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§5.2 onset 加 Clopper-Pearson CI [0.25, 0.92]。与 R10-SF6 合并。\"\n    - round: 12\n      reviewers: [1]\n      note: \"R12 R1 在 context 中提及（每 cell 8 pairs 的 CI 极宽），与 boundary 不确定性合并讨论。\"\n\n- id: \"R10-VIS1\"\n  summary: \"Table 1 / Figure 6 浮动超出 8 页主文边界\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2, visual_check]\n      note: \"调整 float placement。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 双方确认仍超限。Table 1 + Figure 6 在 page 9。估计主文约 8.5-8.6 页。\"\n  action_items:\n    - round: 12\n      action: \"压缩正文或将 Table 1 移至 Appendix；调整 float placement 使主文严格 ≤8 页\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R12-W1\"\n  summary: \"写作信息密度过高，关键 findings 淹没在数字洪流中\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 同意。Section 5.2-5.4 尤其密集。建议精确数字移到 tables/figures，正文保留定性描述。四个 regime 术语引入顺序不统一。\"\n  action_items:\n    - round: 12\n      action: \"正文精简数字密度；统一术语引入顺序\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-FMT1\"\n  summary: \"Abstract 脚注不标准\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"移至 §1 Introduction。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未提及。\"\n\n- id: \"R11-SYM1\"\n  summary: \"β 符号重用：统计功率 vs 幂律指数\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"区分符号。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未提及。\"\n\n- id: \"F5-N1\"\n  summary: \"核心方法是计量经济学标准技术的直接移植\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 12\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 SF-1。Novelty 天花板不可改变。R1/R2 分歧。不做额外修改——3.5→4.0 关键在统计可信度而非 novelty。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 双方再次确认。R1 Excitement 3/5，R2 Excitement 3/5。Novelty 主要来自 method-sensitivity finding 和 phase-diagram framing，非技术方法本身。\"\n\n- id: \"F5-W1\"\n  summary: \"Design Principles 数学深度有限\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 12\n  mentions:\n    - round: 5\n      reviewers: [2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 双方同意不构成理论贡献但作为 motivation 合理。不做额外修改。\"\n    - round: 12\n      reviewers: [2]\n      note: \"R12 R2 升级为 N3 (critical)。R1 rebut：content non-trivial，但同意 contribution framing oversells。Director 裁定合并到 R12-N1。\"\n\n- id: \"F2-W1\"\n  summary: \"α=0.60 sync dip：mechanism unexplained\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"R11 未单独提及。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 双方 should-fix。四大 regime 中 1/4 无机制解释削弱 landscape 完整性。建议降级为 'three regimes + one anomaly'。\"\n  action_items:\n    - round: 12\n      action: \"考虑将 'four regimes' 降级为 'three confirmed regimes + one unexplained anomaly'\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W6\"\n  summary: \"Detection boundary 验证不足\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"与 F2-W4b 合并处理。降级 claim 精度。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 与 F2-W4b 继续合并。sync-dip 排除后仅 15 cells 可用；boundary 是 post-hoc descriptive fit。\"\n\n- id: \"R10-MF5\"\n  summary: \"'Five families (345M-6.9B)' 数字自洽性\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Reviewer 独立验证：five families 是正确计数。保留。345M-6.9B 保留但加注 6.9B 是单条件 bf16。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 计数无误，但 'five families' 措辞给读者广泛可推广印象。与 F2-W2b 合并——问题不在计数正确性而在 framing。\"\n\n- id: \"R10-SF2\"\n  summary: \"Data accumulation vs replacement paradigm 未讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Limitations 已覆盖。Discussion 页面预算不允许额外内容。保持现状。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未提及。\"\n\n- id: \"R10-SF3\"\n  summary: \"单一解码策略需定性讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Limitations 已覆盖。保持现状。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未提及。\"\n\n- id: \"R10-SF4\"\n  summary: \"方法敏感性 '3%-92%' framing\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"与 R11-W1 合并处理。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独提及。\"\n\n- id: \"R10-SF5\"\n  summary: \"Bivariate confounding\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Discussion 已有讨论。Reviewer 确认充分。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未提及。\"\n\n- id: \"R10-SF6\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"与 R11-W2 合并处理。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 在 context 中提及，不作为独立 issue。\"\n\n- id: \"R10-SF7\"\n  summary: \"3-4 seeds replication power 有限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Spec curve 1160 配置部分补偿。不补实验。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独提及。\"\n\n- id: \"R11-VIS2\"\n  summary: \"Pages 6-7 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [visual_check]\n      note: \"LaTeX float 问题。尝试调整但不保证。\"\n    - round: 12\n      reviewers: [visual_check]\n      note: \"R12 视觉审查再次确认：pages 6-7-8 布局节奏失衡。\"\n\n- id: \"F8-W2\"\n  summary: \"Figure 子图内文字偏小\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [visual_check]\n      note: \"Figures 3-5 tick labels 60-65%。在可读性边界。\"\n    - round: 12\n      reviewers: [visual_check]\n      note: \"R12 视觉审查确认 Figures 3-5 axis labels 65-70%，接近可读下限。\"\n\n- id: \"R10-REF3\"\n  summary: \"遗漏引用：Runge et al. (2019) PCMCI\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"已在 bib 中且 §2 引用。加 PCMCI vs PermG 选择理由。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未提及。可能已充分。\"\n\n- id: \"R9-m5\"\n  summary: \"Granger 'precedence' vs 'causality' 术语不一致\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及。可能已充分。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未提及。\"\n\n- id: \"R9-REF1\"\n  summary: \"遗漏引用：Gerstgrasser et al. (2024) data accumulation\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"dey2024breaking 在 bib 中但可能就是 Gerstgrasser。待确认。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未提及。\"\n\n- id: \"R10-m1\"\n  summary: \"Figure 3 y 轴标签含义不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-m2\"\n  summary: \"Table 2 'x/8' 列含义未定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-m3\"\n  summary: \"§5.1 前向引用缺上下文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-REF5\"\n  summary: \"遗漏引用：Montgomery SPC\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"F4-REF5\"\n  summary: \"bib first author mismatch: dey2024breaking\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 4\n  last_seen_round: 11\n\n- id: \"F2-W9b\"\n  summary: \"孤立 bib entries\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 2\n  last_seen_round: 8\n\n- id: \"F6-C2\"\n  summary: \"buffa2026entropy 引用标题不匹配\"\n  category: reference\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 8\n\n- id: \"F8-N3\"\n  summary: \"Appendix 关键验证内容应纳入正文\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"F8-N4\"\n  summary: \"predict-then-verify post-hoc adjustment 嫌疑\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"R12-REF1\"\n  summary: \"遗漏引用：Adams & MacKay (2007) Bayesian online changepoint detection\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [2]\n      note: \"Related Work 未覆盖 online change-point detection 经典文献，在 monitoring setting 中可能比 Granger 更自然。\"\n\n- id: \"R12-REF2\"\n  summary: \"遗漏引用：Papana et al. (2013) / Siggiridou & Kugiumtzis (2016) permutation Granger validation\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1]\n      note: \"置换 Granger 因果性验证方面的相关工作。\"\n\n- id: \"R12-W2\"\n  summary: \"Eq.1 sigmoid 上界 0.70 选择理由未说明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [2]\n\n- id: \"R12-W3\"\n  summary: \"α 采样间隔不均匀（0.10→0.25 跳跃）理由未解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [2]\n\n- id: \"R12-W4\"\n  summary: \"Schaeffer et al. 8 种 collapse 定义中本文使用哪种未明确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [2]\n      note: \"§2 提到 'distributional shift family' 但未明确选择理由。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "issues_yaml": "issues:\n# ============================================================\n# Round 1-11 历史 resolved — 保留跨轮次记录\n# ============================================================\n- id: \"R1-N1\"\n  summary: \"Ground-truth pairs 定义存在循环论证\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Effect-size GT 重定义完成。\"\n  resolution_round: 1\n\n- id: \"R1-N2\"\n  summary: \"FPR=0% 标定仅基于单 seed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"α=0.0 三 seed FPR 验证完成。\"\n  resolution_round: 1\n\n- id: \"R1-N3\"\n  summary: \"α=0.50 和 α=0.75 仅 1 seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Multi-seed 补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-N1\"\n  summary: \"核心方法论为计量经济学已有知识的直接迁移，新颖性有限\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Round 1 三层定位 reframe 完成。\"\n  resolution_round: 1\n\n- id: \"R2-N2\"\n  summary: \"α=0.75 multi-seed 实验未完成 + Appendix A 缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-N3\"\n  summary: \"实验规模过窄\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"跨架构验证已扩展至 15 model-seed 组合。\"\n  resolution_round: 1\n\n- id: \"R1-W1\"\n  summary: \"Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"核心修复完成。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"PermG 缺少 power analysis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Appendix N power analysis 完成。\"\n  resolution_round: 1\n\n- id: \"R1-W3\"\n  summary: \"75% spurious-signal rate headline 依赖 underpowered T-Y\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W4\"\n  summary: \"α=0.75 单 seed borderline 结果不应出现在 abstract\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W5\"\n  summary: \"Toda-Yamamoto 纳入理由表述不充分\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W6\"\n  summary: \"可重复性信息不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"超参补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-W3\"\n  summary: \"Token entropy canary 仅在 α=1.0 验证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"缺少独立 Limitations section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W5\"\n  summary: \"缺少 AI Writing Disclosure\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W6\"\n  summary: \"缺少 canary→perplexity 为何 spurious 的深入解释\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF1\"\n  summary: \"遗漏 Granger & Newbold (1974)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF2\"\n  summary: \"遗漏 Hataya et al. (2023) 和 Seddik et al. (2024)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W1-old\"\n  summary: \"Citation key chen2025scales 与实际作者不匹配\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"F2-W3\"\n  summary: \"Section 3 承诺的三项附录内容缺失\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"附录内容补充完成。\"\n  resolution_round: 3\n\n- id: \"F2-W8\"\n  summary: \"格式不合规：未使用 ACL 模板\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"ACL 模板迁移完成。\"\n  resolution_round: 2\n\n- id: \"F2-REF1\"\n  summary: \"遗漏 arXiv:2502.15654\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF1\"\n  summary: \"遗漏 arXiv:2602.10531\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF2\"\n  summary: \"遗漏 arXiv:2505.19046\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF3\"\n  summary: \"遗漏 arXiv:2510.16657\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF5\"\n  summary: \"Appendix H CUSUM 未引用 Page (1954)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F4-REF1\"\n  summary: \"遗漏 Truong & Truong (2026)\"\n  category: reference\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"引用已添加并在 §1/§2 讨论。\"\n  resolution_round: 6\n\n- id: \"F4-REF3\"\n  summary: \"遗漏 Benjamini & Yekutieli (2001)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"§4 现引用 benjamini2001control。\"\n  resolution_round: 5\n\n- id: \"F2-REF3\"\n  summary: \"Dakos et al. (2012) + Schreiber (2000) + Phipson & Smyth (2010) 在 bib 中但正文未引用\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"引用补充完成。\"\n  resolution_round: 4\n\n- id: \"F6-W2\"\n  summary: \"页数可能超限\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"R8 PDF 审查确认主体 8 页合规。\"\n  resolution_round: 8\n\n- id: \"F2-W6b\"\n  summary: \"'Methodological pitfalls' 有 straw-man 倾向\"\n  category: framing\n  severity: major\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 8\n  resolution: \"全文已改为 'design considerations'。R8 fresh review 未再提及。\"\n  resolution_round: 8\n\n- id: \"F5-N2\"\n  summary: \"T=10 统计效力不足(power≈37%), sharp onset 可能是 power artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Power simulation 重写通过 Reviewer #75。Steepness comparison k_obs=18.79 vs k_H0=6.14 (ratio 3.06×, CI non-overlapping) 写入 method.tex + experiments.tex + appendix。Dense α 证据 (17 points, sigmoid k=15.7) 额外支撑。\"\n  resolution_round: 9\n  first_raised_round: 5\n  last_seen_round: 9\n\n- id: \"F2-W5\"\n  summary: \"Token entropy → distinct-n 机械耦合 confound 未排除\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Metric structure 分析完成：mauve attribution 100% 确认非 metric coupling。ECE→distinct 独立于 token_entropy→distinct 路径。讨论已添加到 discussion.tex。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 9\n\n- id: \"F2-W2\"\n  summary: \"Specification curve analysis 定位不精确\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Appendix E 已改称 'systematic robustness analysis'。R8/R9 fresh review 未再提及。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 8\n\n- id: \"F8-C2\"\n  summary: \"Discussion §6 过于简短(~100词)\"\n  category: writing\n  severity: major\n  status: resolved\n  resolution: \"Discussion 扩展至 20 行。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C3\"\n  summary: \"与 Schaeffer et al. (2025) '8 种 collapse 定义' 的关系讨论不充分\"\n  category: framing\n  severity: major\n  status: resolved\n  resolution: \"Schaeffer taxonomy 映射已添加到 related_work.tex。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C1\"\n  summary: \"Du & Tanaka-Ishii (2026) 引用三重错误\"\n  category: reference\n  severity: critical\n  status: resolved\n  resolution: \"§2 已修正为 'related but distinct phenomenon'。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"R9-C1\"\n  summary: \"FPR CI method.tex 内部矛盾\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"FPR=10% MMCT sensitivity analysis 完成。Paper Agent 统一 CI 处理。\"\n  resolution_round: 9\n  first_raised_round: 9\n  last_seen_round: 9\n\n- id: \"F8-N1\"\n  summary: \"BH-FDR 在强正回归依赖下适用性讨论不充分\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"PRDS 假设适用性讨论已添加。FPR sensitivity analysis 额外支撑。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 10\n\n- id: \"F8-REF1\"\n  summary: \"遗漏引用：online/continual learning 下 model collapse 检测\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"related_work.tex 已添加 scope 区分。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F2-W11\"\n  summary: \"α_c SE=0.006 低估真实 seed 不确定性\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"被 F2-W4b/F2-W6 的统计基础问题覆盖。\"\n  resolution_round: 11\n  first_raised_round: 2\n  last_seen_round: 10\n\n- id: \"F8-N2\"\n  summary: \"未讨论为何选择经典 permutation Granger 而非 neural Granger causality\"\n  category: method\n  severity: minor\n  status: resolved\n  resolution: \"§4 已添加 T≤25 理由。§2 引用 neural Granger 文献。\"\n  resolution_round: 11\n  first_raised_round: 8\n  last_seen_round: 11\n\n- id: \"R9-REF2\"\n  summary: \"遗漏引用：Steegen et al. (2016) multiverse analysis\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 steegen2016increasing。\"\n  resolution_round: 11\n  first_raised_round: 9\n  last_seen_round: 11\n\n- id: \"R10-REF2\"\n  summary: \"遗漏引用：Mitchell et al. (2023) DetectGPT\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 mitchell2023detectgpt。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-REF4\"\n  summary: \"遗漏引用：Padmakumar et al. (2024)\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 padmakumar2024writing。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n\n# ============================================================\n# 活跃 issues — Round 12\n# ============================================================\n\n- id: \"F3-J4\"\n  summary: \"PermG FPR 超出 nominal 5%，architecture-dependent\"\n  category: method\n  severity: critical\n  status: open\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 3\n  last_seen_round: 12\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 MF-1。6轮 mild hedging 失败。本轮更激进：boundary 加 ±0.05 uncertainty，onset 加 expected FP under null=0.9/8 论证。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 双方共识 critical。R1 主张 onset 区域 (α≈0.50) 恰好在 FPR 膨胀最危险地带。R2 缓解：Fisher exact p=3.45e-11 + cross-seed 3/3 一致性证明 onset 存在性 robust，但精确位置需更宽 error bars。GPT-2 50% FPR 仍仅在 Appendix/Limitations。\"\n  action_items:\n    - round: 12\n      action: \"增加 null seeds 至 ≥12 或在正文报告保守版边界（Bonferroni sensitivity）；GPT-2 50% FPR 移入正文 §5.5 显著标注\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W4b\"\n  summary: \"幂律边界 α_c(T) 拟合基础薄弱\"\n  category: framing\n  severity: critical\n  status: open\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 12\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 MF-3。6轮降级不够。本轮：abstract 删除具体 γ，method.tex 改为 'consistent with power-law scaling'。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 双方共识 critical。β MLE=0.66 vs CV=0.24 (CI [0.24,0.78]) 使 γ 从 0.64 到 2.08 任意。LOO-CV MAE=0.037 在 3-5 点上无鉴别力。R11 的 'consistent with' 降级被判定不够——abstract 仍呈现为高精度定量结果。\"\n  action_items:\n    - round: 12\n      action: \"Abstract 删除 MAE=0.037 和 15/15 within CI；将 boundary 重新定位为 qualitative trend（α_c 随 T 递减）而非精确幂律；正文报告 γ 的完整 CI\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W2b\"\n  summary: \"'Detectability landscape' framing 承诺超过交付\"\n  category: framing\n  severity: critical\n  status: open\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 12\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 MF-2。本轮 scope 收紧 abstract/intro：full grid 限定 Pythia-410M，cross-arch 限定 α=1.0。保留 title 和 five families。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 双方共识 critical。R11 的收紧被判定仍不够。标题暗示跨架构全面刻画，实际 landscape 仅 Pythia-410M；cross-arch 仅 α=1.0 最极端条件。GPT-2 50% FPR 使该架构 findings 不可靠。R1 提出 4 个 non-confirming cases 可能是 FPR 差异而非 distinct failure modes（更简约解释）。\"\n  action_items:\n    - round: 12\n      action: \"标题考虑修改以反映实际 scope；Abstract 将 cross-arch 重新措辞为 exploratory probes；正文 §5.5 添加 alternative explanation paragraph（FPR 差异 vs distinct failure modes）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W10\"\n  summary: \"Cross-architecture 'coupling preserved' 条件 post-hoc\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 12\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 SF-3。改为 'partial validation with notable exceptions'。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 与 F2-W2b 合并。4 non-confirming cases 的 post-hoc failure mode 归因缺乏独立验证。\"\n  action_items:\n    - round: 12\n      action: \"合并到 F2-W2b 的 scope 重新定位\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-N1\"\n  summary: \"统计功率 β=0.66 CI [0.24,0.78] 使检测边界定量解读不可靠\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"新 MF-4。method.tex 加 power limitation 句：T≤8 power <50%，短 T 的 boundary 是上界。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 与 F2-W4b 合并。β 不可识别性使整个 boundary model 的定量形式不确定。\"\n\n- id: \"F2-W7\"\n  summary: \"Intervention 实验薄弱\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 12\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 SF-2。Abstract 删 '64%'，改为定性 + proof-of-concept。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 双方共识 should-fix。仅 α=1.0/N=2/post-hoc threshold。R2 补充：Appendix H CUSUM comparison 显示 simple threshold 同效，削弱 Granger 框架的 practical advantage。建议从 Contribution 1 剥离。\"\n  action_items:\n    - round: 12\n      action: \"从 Contribution 1 剥离 intervention；独立为 proof-of-concept paragraph 或 appendix\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R12-N1\"\n  summary: \"Design Principle 'formal design rationale' 作为独立贡献 oversells\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 判 critical（near-trivial），R1 rebut（mode amplification 下的特定机制非公理，≥2 gen lag 非先验可知）。Director 裁定 warning：内容非 trivial 但 contribution framing 需降级。\"\n  action_items:\n    - round: 12\n      action: \"将 Contribution 2 从 'formal design rationale' 降级为 'empirically validated ordering principle'；不作为独立 numbered contribution\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-W1\"\n  summary: \"'3%-92%' FPR 范围含失效方法 NaiveXCorr\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"保留 3%-92% 全范围但正文首次出现时区分。与 R10-SF4 合并。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独提及。可能已充分处理。\"\n\n- id: \"R11-W2\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§5.2 onset 加 Clopper-Pearson CI [0.25, 0.92]。与 R10-SF6 合并。\"\n    - round: 12\n      reviewers: [1]\n      note: \"R12 R1 在 context 中提及（每 cell 8 pairs 的 CI 极宽），与 boundary 不确定性合并讨论。\"\n\n- id: \"R10-VIS1\"\n  summary: \"Table 1 / Figure 6 浮动超出 8 页主文边界\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2, visual_check]\n      note: \"调整 float placement。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 双方确认仍超限。Table 1 + Figure 6 在 page 9。估计主文约 8.5-8.6 页。\"\n  action_items:\n    - round: 12\n      action: \"压缩正文或将 Table 1 移至 Appendix；调整 float placement 使主文严格 ≤8 页\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R12-W1\"\n  summary: \"写作信息密度过高，关键 findings 淹没在数字洪流中\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 同意。Section 5.2-5.4 尤其密集。建议精确数字移到 tables/figures，正文保留定性描述。四个 regime 术语引入顺序不统一。\"\n  action_items:\n    - round: 12\n      action: \"正文精简数字密度；统一术语引入顺序\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-FMT1\"\n  summary: \"Abstract 脚注不标准\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"移至 §1 Introduction。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未提及。\"\n\n- id: \"R11-SYM1\"\n  summary: \"β 符号重用：统计功率 vs 幂律指数\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"区分符号。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未提及。\"\n\n- id: \"F5-N1\"\n  summary: \"核心方法是计量经济学标准技术的直接移植\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 12\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 SF-1。Novelty 天花板不可改变。R1/R2 分歧。不做额外修改——3.5→4.0 关键在统计可信度而非 novelty。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 双方再次确认。R1 Excitement 3/5，R2 Excitement 3/5。Novelty 主要来自 method-sensitivity finding 和 phase-diagram framing，非技术方法本身。\"\n\n- id: \"F5-W1\"\n  summary: \"Design Principles 数学深度有限\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 12\n  mentions:\n    - round: 5\n      reviewers: [2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 双方同意不构成理论贡献但作为 motivation 合理。不做额外修改。\"\n    - round: 12\n      reviewers: [2]\n      note: \"R12 R2 升级为 N3 (critical)。R1 rebut：content non-trivial，但同意 contribution framing oversells。Director 裁定合并到 R12-N1。\"\n\n- id: \"F2-W1\"\n  summary: \"α=0.60 sync dip：mechanism unexplained\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"R11 未单独提及。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 双方 should-fix。四大 regime 中 1/4 无机制解释削弱 landscape 完整性。建议降级为 'three regimes + one anomaly'。\"\n  action_items:\n    - round: 12\n      action: \"考虑将 'four regimes' 降级为 'three confirmed regimes + one unexplained anomaly'\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W6\"\n  summary: \"Detection boundary 验证不足\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"与 F2-W4b 合并处理。降级 claim 精度。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 与 F2-W4b 继续合并。sync-dip 排除后仅 15 cells 可用；boundary 是 post-hoc descriptive fit。\"\n\n- id: \"R10-MF5\"\n  summary: \"'Five families (345M-6.9B)' 数字自洽性\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Reviewer 独立验证：five families 是正确计数。保留。345M-6.9B 保留但加注 6.9B 是单条件 bf16。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 计数无误，但 'five families' 措辞给读者广泛可推广印象。与 F2-W2b 合并——问题不在计数正确性而在 framing。\"\n\n- id: \"R10-SF2\"\n  summary: \"Data accumulation vs replacement paradigm 未讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Limitations 已覆盖。Discussion 页面预算不允许额外内容。保持现状。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未提及。\"\n\n- id: \"R10-SF3\"\n  summary: \"单一解码策略需定性讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Limitations 已覆盖。保持现状。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未提及。\"\n\n- id: \"R10-SF4\"\n  summary: \"方法敏感性 '3%-92%' framing\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"与 R11-W1 合并处理。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独提及。\"\n\n- id: \"R10-SF5\"\n  summary: \"Bivariate confounding\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Discussion 已有讨论。Reviewer 确认充分。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未提及。\"\n\n- id: \"R10-SF6\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"与 R11-W2 合并处理。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 在 context 中提及，不作为独立 issue。\"\n\n- id: \"R10-SF7\"\n  summary: \"3-4 seeds replication power 有限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Spec curve 1160 配置部分补偿。不补实验。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独提及。\"\n\n- id: \"R11-VIS2\"\n  summary: \"Pages 6-7 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [visual_check]\n      note: \"LaTeX float 问题。尝试调整但不保证。\"\n    - round: 12\n      reviewers: [visual_check]\n      note: \"R12 视觉审查再次确认：pages 6-7-8 布局节奏失衡。\"\n\n- id: \"F8-W2\"\n  summary: \"Figure 子图内文字偏小\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [visual_check]\n      note: \"Figures 3-5 tick labels 60-65%。在可读性边界。\"\n    - round: 12\n      reviewers: [visual_check]\n      note: \"R12 视觉审查确认 Figures 3-5 axis labels 65-70%，接近可读下限。\"\n\n- id: \"R10-REF3\"\n  summary: \"遗漏引用：Runge et al. (2019) PCMCI\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"已在 bib 中且 §2 引用。加 PCMCI vs PermG 选择理由。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未提及。可能已充分。\"\n\n- id: \"R9-m5\"\n  summary: \"Granger 'precedence' vs 'causality' 术语不一致\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"R11 未提及。可能已充分。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未提及。\"\n\n- id: \"R9-REF1\"\n  summary: \"遗漏引用：Gerstgrasser et al. (2024) data accumulation\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"dey2024breaking 在 bib 中但可能就是 Gerstgrasser。待确认。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未提及。\"\n\n- id: \"R10-m1\"\n  summary: \"Figure 3 y 轴标签含义不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-m2\"\n  summary: \"Table 2 'x/8' 列含义未定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-m3\"\n  summary: \"§5.1 前向引用缺上下文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-REF5\"\n  summary: \"遗漏引用：Montgomery SPC\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"F4-REF5\"\n  summary: \"bib first author mismatch: dey2024breaking\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 4\n  last_seen_round: 11\n\n- id: \"F2-W9b\"\n  summary: \"孤立 bib entries\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 2\n  last_seen_round: 8\n\n- id: \"F6-C2\"\n  summary: \"buffa2026entropy 引用标题不匹配\"\n  category: reference\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 8\n\n- id: \"F8-N3\"\n  summary: \"Appendix 关键验证内容应纳入正文\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"F8-N4\"\n  summary: \"predict-then-verify post-hoc adjustment 嫌疑\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"R12-REF1\"\n  summary: \"遗漏引用：Adams & MacKay (2007) Bayesian online changepoint detection\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [2]\n      note: \"Related Work 未覆盖 online change-point detection 经典文献，在 monitoring setting 中可能比 Granger 更自然。\"\n\n- id: \"R12-REF2\"\n  summary: \"遗漏引用：Papana et al. (2013) / Siggiridou & Kugiumtzis (2016) permutation Granger validation\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1]\n      note: \"置换 Granger 因果性验证方面的相关工作。\"\n\n- id: \"R12-W2\"\n  summary: \"Eq.1 sigmoid 上界 0.70 选择理由未说明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [2]\n\n- id: \"R12-W3\"\n  summary: \"α 采样间隔不均匀（0.10→0.25 跳跃）理由未解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [2]\n\n- id: \"R12-W4\"\n  summary: \"Schaeffer et al. 8 种 collapse 定义中本文使用哪种未明确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [2]\n      note: \"§2 提到 'distributional shift family' 但未明确选择理由。\""
  }
}
```

</details>

---


### Tool result

_source line 1151 · 2026-05-24T14:17:30.207242+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml\", \"bytes\": 27564}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1152 · 2026-05-24T14:19:49.326578+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 12 审稿报告：Characterizing the Detectability Landscape of Iterative Model Collapse\n\n**Target Venue**: EMNLP 2026 (Long Paper, via ARR)\n**Review Mode**: Fresh (Round 12)\n**Reviewers**: R1 (方法严谨性 + 统计有效性), R2 (新颖性 + Framing + 完整性)\n\n---\n\n## Summary\n\n本文在 Pythia-410M 上系统构建了 iterative model collapse 的检测相图（13 个 contamination levels × 多个 observation windows），使用 Permutation Granger Causality (PermG) 识别出 sharp detection onset、power-law detection boundary 和 non-monotonic dip 等结构。在 α=1.0 下对 5 个模型族进行了跨架构探索。核心发现包括：(1) 方法敏感性——同一数据上 5 种检测方法产生 FPR 3%–92%；(2) entropy Granger-precedes diversity collapse by ≥1 generation (14/15 experiments)；(3) canary-triggered intervention proof-of-concept。\n\n---\n\n## Strengths\n\n1. **Method-sensitivity finding 是真正有价值的贡献** [双方共识]：同一数据集上 5 种方法产生 FPR 3%–92%，将方法选择敏感性提升为 primary finding 而非 robustness check，对 model collapse 文献是重要警示。\n\n2. **系统性相图框架** [双方共识]：将 detectability 刻画为 (α, T) 空间中的结构化地形，这一概念工具在 model collapse 文献中具有原创性和可复用性。\n\n3. **统计方法论严谨度罕见** [双方共识]：BH-FDR correction、null-control calibration、specification curve analysis (1,160 configurations)、Shapley value method decomposition——在 model collapse 文献中少见的 robustness 水平。\n\n4. **诚实的 Limitations section** [双方共识]：坦率承认 FPR 膨胀、power 限制、β 不可识别、sync-dip 未解释、单架构局限性。\n\n5. **Reproducibility 较好**：超参详尽（Appendix A），5000 permutations、BH-FDR q=0.05 明确，seed 信息完整。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1 [critical, 双方共识]: PermG FPR 11.1% (CI [1.2%, 30.4%]) 使检测边界区域的定量可靠性不足**\n\nPermG 实际 FPR = 4/36 = 11.1%，超出 BH-FDR 名义 5%，cluster-adjusted CI 上界达名义水平的 6 倍。检测 onset (α≈0.50) 恰好位于 FPR 膨胀最危险的地带——Table 7 (Appendix D) 显示 α=0.45 处 min p_fdr = 0.059–0.091，仅略高于阈值。Null control 仅 6 seeds (36 tests)，样本量不足以可靠估计 FPR。GPT-2-medium 的 standalone FPR 高达 50% (Appendix Z)，但仅在 Limitations/Appendix 中提及。\n\n**缓解因素** (R2 提出)：Fisher exact test (0/64 vs 18/32, p=3.45×10⁻¹¹) + cross-seed 3/3 一致性证明 onset 的**存在性** robust；MMCT consensus (K≥3) 在 null 下 0% FPR。但 onset 的**精确位置** (α_c = 0.483 ± 0.006) 在当前 FPR 不确定性下需要更宽的 error bars。\n\n**Required action**: (a) 增加 null seeds 至 ≥12 或报告 Bonferroni-conservative 边界；(b) GPT-2 50% FPR 必须在正文 §5.5 显著标注；(c) 在 FPR CI 上界条件下报告保守版 α_c。\n\n---\n\n**MF-2 [critical, 双方共识]: 标题/Abstract 的 scope 承诺超过实际交付**\n\n\"Characterizing the Detectability Landscape\" + \"five families (345M–6.9B)\" 暗示跨架构全面刻画，但：\n- 完整 α×T phase diagram 仅在 Pythia-410M 上构建\n- Cross-architecture (Table 1) 仅测试 α=1.0（最极端情形）\n- GPT-2-medium standalone FPR=50% 使该架构上的 \"检测\" 本质上不可靠\n- 4 个 non-confirming cases 的 post-hoc \"failure mode\" 归因 vs 更简约的 \"PermG FPR 差异\" 解释未被讨论\n\n**Required action**: (a) 标题修改以反映实际 scope（主要是 Pythia-410M 的发现）；(b) Abstract 将 cross-arch 重新措辞为 \"exploratory probes at α=1.0\"；(c) §5.5 添加 alternative explanation paragraph。\n\n---\n\n**MF-3 [critical, 双方共识]: Power-law boundary 参数不可识别，但被高精度呈现**\n\nβ 的 MLE = 0.66 vs CV = 0.24，profile CI [0.24, 0.78]——指数 γ 从 0.64 到 2.08 任意取值。Abstract 中 \"LOO-CV: MAE=0.037, 15/15 within CI\" 在 3-5 个 T 值上无鉴别力（任何光滑单调函数都能达到类似 MAE）。Sync-dip excluded（5 cells）是 post-hoc 操作；included 后 MAE = 0.203 (5.5×)，暴露模型 systematic failure。\n\n**Required action**: (a) Abstract 删除 MAE=0.037 和 \"15/15 within CI\"；(b) 将 boundary 定位为 qualitative trend (α_c 随 T 递减) 而非精确幂律；(c) 正文报告 γ 的完整 CI；(d) 并列呈现 sync-dip included/excluded 两组拟合。\n\n---\n\n**MF-4 [critical, R2 主导，R1 同意超限]: 页数超出 EMNLP 2026 8 页限制**\n\nTable 1 和 Figure 6（§5.5/5.6 引用的正文元素）被 LaTeX 浮动到 page 9。估计主文约 8.5–8.6 页，超限约 0.5 页。EMNLP 2026 strict 8-page limit 不含 Limitations。\n\n**Required action**: 压缩正文（如将 Table 1 移至 Appendix，或合并 §5.5/5.6 到更紧凑的 subsection）以严格遵守 8 页。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1 [双方共识]: Intervention proof-of-concept 仅单一极端条件 (α=1.0, N=2, post-hoc threshold)**\n\n仍被列入 Contribution 1。Appendix H CUSUM comparison 显示 simple threshold 同效，削弱 Granger 框架的 practical advantage。建议从 Contribution 1 剥离为独立的 illustrative example。\n\n**SF-2 [R2 提出, R1 部分同意]: Design Principle 'formal design rationale' 作为独立贡献 oversells**\n\nR2 判 critical（near-trivial：连续量先于阈值量是信息论直觉）；R1 rebut（mode amplification 下的特定机制非公理，≥2 gen lag 非先验可知）。**Director 裁定 should-fix**：内容非 trivial，但 \"formal design rationale\" 的贡献措辞需降级为 \"empirically validated ordering principle\"。\n\n**SF-3 [双方共识]: Sync-dip (α=0.60) 作为 \"四大 regime 之一\" 但机制完全未解释**\n\nLimitations 承认 \"the sync-dip mechanism at α=0.60 remains open\"。建议降级为 \"three confirmed regimes + one unexplained anomaly\"。\n\n**SF-4 [R2 提出, R1 同意]: 写作信息密度过高**\n\n几乎每句含多个精确数字，关键 findings 淹没在数字洪流中。四 regime 术语引入顺序不统一。建议精确数字移到 tables/figures，正文保留定性描述。\n\n---\n\n### Minor Issues\n\n- Eq.1 sigmoid 上界 0.70 选择理由未说明\n- α 采样间隔不均匀 (0.10→0.25 跳跃) 理由未解释\n- Table 1 footnotes 信息过密，建议以 Appendix table 替代\n- Schaeffer et al. \"8 种 collapse 定义\" 中本文使用哪种未明确\n- Appendix K 对比表中 SIGMA 的 multi-architecture 标注可能不准确\n- Design Principle 与 Theorem 共享计数器，编号序列可能令读者混淆\n- bf16 vs fp32 的 sensitivity 在 abstract/contributions 中未反映\n- CUSUM 负面结果值得主文简要提及\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| PermG FPR 使 boundary 不可靠 | N1 critical | W3→升级 critical | **[AGREE] critical** |\n| 标题/cross-arch scope 过度 | N2 critical | N2 critical | **[AGREE] critical** |\n| Power-law 参数不可识别 | W1→升级 critical | N1 critical | **[AGREE] critical** |\n| 页数超限 | 同意 | W4 should-fix | **[AGREE] should-fix** |\n| Intervention 过薄 | W3 should-fix | W2 should-fix | **[AGREE] should-fix** |\n| Sync-dip 无解释 | W2 should-fix | W1 should-fix | **[AGREE] should-fix** |\n| 信息密度过高 | 同意 | W5 should-fix | **[AGREE] should-fix** |\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | Director 裁定 |\n|------|----|----|--------------|\n| Design Principle trivial? | should-fix (内容非 trivial，framing oversells) | N3 critical (近乎公理) | **should-fix** — R1 的 rebuttal 有理：mode amplification 下的特定机制和 ≥2 gen lag 非先验可知；但贡献措辞确实 oversells |\n| MMCT 等权投票 | W4 should-fix (缺 Type I 分析) | REBUT (有 empirical mitigation) | **minor** — Appendix M 的 4 种 weighting schemes 一致性 + null MMCT FPR=0% 提供了充分 empirical evidence |\n| Grid 多重比较 | W5 should-fix | REBUT (sigmoid fit 是 single test) | **minor** — onset claim 有 aggregate-level support (sigmoid + Fisher)，但 \"four regimes\" 命名应更谨慎 |\n\n---\n\n## Questions for Authors\n\n1. 如果 FPR 恰好在 5% 名义水平，α_c(T) 会如何移动？能否提供 FPR=5% vs 11.1% 下的敏感性分析？\n2. GPT-2-medium 的 50% FPR 是 PermG 在高 null-drift 架构上的根本局限，还是可通过架构特定校准解决？\n3. Sync-dip 是否在所有 seed 中一致出现？有无证据排除 seed-specific artifact？\n4. 如果仅保留 MMCT-conditioned claims (K≥3, 0% FPR)，abstract 和 contributions 的核心 findings 是否仍然成立？\n5. 为什么不使用 two-sample distributional tests (MMD, KS) 作为替代或补充 detection 方案？\n\n---\n\n## Missing References\n\n- **Adams & MacKay (2007)**: Bayesian online changepoint detection — Related Work 未覆盖 online change-point detection 经典文献\n- **Papana et al. (2013) / Siggiridou & Kugiumtzis (2016)**: 置换 Granger 因果性验证方面的工作\n- **Two-sample distributional testing literature** (MMD, Wasserstein): 作为替代 detection 方案未被系统讨论\n\n---\n\n## External Review\n\n**Status**: 未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**Status**: ✅ 完成\n\nFindings:\n- **[warning]** Pages 6-7-8 布局节奏失衡：pages 6-7 连续纯文本无 display item，page 8 塞入 Figures 3/4/5 导致每图面积偏小。建议将 Figure 3 或 4 前移均衡视觉节奏。\n- **[info]** Figures 3-5 axis labels、legend 字号约正文 65-70%，接近可读下限，建议 ≥70%。\n- **[info]** 前 2 页无视觉锚点，第一个 display item 在 page 3。ACL 格式下可接受。\n- **[info]** Figure 1 热力图分数标注字号偏小，PDF 屏幕阅读需放大。\n- **[info]** Appendix 末页填充约 55-60%（非严重问题）。\n\n---\n\n## Overall Assessment\n\n**Score: 3.0 — Findings**\n\n**Confidence: 4/5**\n\n**Rationale**:\n\n论文的 method-sensitivity finding（FPR 3%–92%）和 phase-diagram 框架具有真正的原创性和实用价值，统计方法论严谨度在 model collapse 文献中罕见。然而三个 critical 问题共同将论文拉至 Findings 水平：\n\n1. **FPR 膨胀 + null sample 不足** → 核心定量 claims (detection boundary) 的可靠性存疑\n2. **Scope overclaiming** → 标题和 abstract 承诺的泛化程度远超单架构 + α=1.0 探索的实际交付\n3. **Power-law boundary 参数不可识别** → Contribution 1 的定量核心本质上未确定\n\n这些问题不是 writing 问题——它们动摇了论文核心贡献的证据基础。如果作者能：(a) 增加 null control seeds 并报告保守版边界；(b) 校准标题/abstract 的 scope 与实际交付匹配；(c) 将 boundary 降级为定性趋势——论文有潜力从 Findings 上升至 Borderline Conference (3.5)。当前版本适合 Findings track。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 1 将 power-law boundary、canary mechanism 和 intervention 打包在一起，每项的 evidence level 差异很大（boundary: weak, canary: moderate, intervention: minimal）。建议拆分为独立 contributions 并明确各自的 evidence strength。\n- \"five families (345M–6.9B)\" 在第一页给读者设定了跨架构全面验证的期望，但实际仅 α=1.0 单点探索。\n\n### §3 Cascade Ordering\n- Design Principles 1-2 提供了有用的 motivation，但 \"formal design rationale\" 措辞暗示比实际提供的更深的形式化。建议改为 \"empirically motivated design principles\"。\n\n### §4 Method\n- PermG FPR 11.1% 的讨论足够诚实，但 MMCT consensus 作为 primary safeguard 的 role 应在 §4.1 开头而非末尾强调——让读者先知道 standalone PermG 的局限和论文的应对策略。\n- §4.2 的 boundary model 在参数不可识别的前提下，作为 contribution 的价值在于定性框架而非定量预测。\n\n### §5 Experiments\n- §5.2 的 sharp onset 是论文最引人注目的发现。Fisher exact test + cross-seed 一致性提供了 onset 存在性的强证据。但 α_c = 0.483 ± 0.006 的精度声明与 §5.1 自承认的 β 不可识别性矛盾。\n- §5.5 Cross-architecture: GPT-2-medium 的 50% standalone FPR 应在本节正文中以 caveat paragraph 呈现，而非仅在 Appendix Z 和 Limitations 中。读者可能只看 Table 1 的 \"6/8\"，不会注意到该结果在 50% FPR 背景下本质不可解读。\n- §5.6 Intervention: 从 page budget 角度，0.5 页用于 N=2 single-condition proof-of-concept 的 ROI 很低。该空间可更好地用于 §5.5 的 FPR caveat 或 §5.3 的 dip mechanism 讨论。\n\n### §6 Discussion\n- 篇幅合理但略显保守。鉴于 scope 需要收紧，Discussion 是添加 \"what this study does NOT claim\" 的自然位置。\n\n### Limitations\n- 全面且诚实。建议增加一句关于 intervention 的 limitation（仅在最有利条件下测试，practical applicability unknown）。\n\n### Format\n- **页数**: 需严格压缩至 8 页正文。\n- **Float placement**: Pages 6-7 纯文本 + page 8 图片堆积 = 不均衡，调整 float 命令。",
  "project": "distrib_canary_collapse",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
  "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 12 审稿报告：Characterizing the Detectability Landscape of Iterative Model Collapse\n\n**Target Venue**: EMNLP 2026 (Long Paper, via ARR)\n**Review Mode**: Fresh (Round 12)\n**Reviewers**: R1 (方法严谨性 + 统计有效性), R2 (新颖性 + Framing + 完整性)\n\n---\n\n## Summary\n\n本文在 Pythia-410M 上系统构建了 iterative model collapse 的检测相图（13 个 contamination levels × 多个 observation windows），使用 Permutation Granger Causality (PermG) 识别出 sharp detection onset、power-law detection boundary 和 non-monotonic dip 等结构。在 α=1.0 下对 5 个模型族进行了跨架构探索。核心发现包括：(1) 方法敏感性——同一数据上 5 种检测方法产生 FPR 3%–92%；(2) entropy Granger-precedes diversity collapse by ≥1 generation (14/15 experiments)；(3) canary-triggered intervention proof-of-concept。\n\n---\n\n## Strengths\n\n1. **Method-sensitivity finding 是真正有价值的贡献** [双方共识]：同一数据集上 5 种方法产生 FPR 3%–92%，将方法选择敏感性提升为 primary finding 而非 robustness check，对 model collapse 文献是重要警示。\n\n2. **系统性相图框架** [双方共识]：将 detectability 刻画为 (α, T) 空间中的结构化地形，这一概念工具在 model collapse 文献中具有原创性和可复用性。\n\n3. **统计方法论严谨度罕见** [双方共识]：BH-FDR correction、null-control calibration、specification curve analysis (1,160 configurations)、Shapley value method decomposition——在 model collapse 文献中少见的 robustness 水平。\n\n4. **诚实的 Limitations section** [双方共识]：坦率承认 FPR 膨胀、power 限制、β 不可识别、sync-dip 未解释、单架构局限性。\n\n5. **Reproducibility 较好**：超参详尽（Appendix A），5000 permutations、BH-FDR q=0.05 明确，seed 信息完整。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1 [critical, 双方共识]: PermG FPR 11.1% (CI [1.2%, 30.4%]) 使检测边界区域的定量可靠性不足**\n\nPermG 实际 FPR = 4/36 = 11.1%，超出 BH-FDR 名义 5%，cluster-adjusted CI 上界达名义水平的 6 倍。检测 onset (α≈0.50) 恰好位于 FPR 膨胀最危险的地带——Table 7 (Appendix D) 显示 α=0.45 处 min p_fdr = 0.059–0.091，仅略高于阈值。Null control 仅 6 seeds (36 tests)，样本量不足以可靠估计 FPR。GPT-2-medium 的 standalone FPR 高达 50% (Appendix Z)，但仅在 Limitations/Appendix 中提及。\n\n**缓解因素** (R2 提出)：Fisher exact test (0/64 vs 18/32, p=3.45×10⁻¹¹) + cross-seed 3/3 一致性证明 onset 的**存在性** robust；MMCT consensus (K≥3) 在 null 下 0% FPR。但 onset 的**精确位置** (α_c = 0.483 ± 0.006) 在当前 FPR 不确定性下需要更宽的 error bars。\n\n**Required action**: (a) 增加 null seeds 至 ≥12 或报告 Bonferroni-conservative 边界；(b) GPT-2 50% FPR 必须在正文 §5.5 显著标注；(c) 在 FPR CI 上界条件下报告保守版 α_c。\n\n---\n\n**MF-2 [critical, 双方共识]: 标题/Abstract 的 scope 承诺超过实际交付**\n\n\"Characterizing the Detectability Landscape\" + \"five families (345M–6.9B)\" 暗示跨架构全面刻画，但：\n- 完整 α×T phase diagram 仅在 Pythia-410M 上构建\n- Cross-architecture (Table 1) 仅测试 α=1.0（最极端情形）\n- GPT-2-medium standalone FPR=50% 使该架构上的 \"检测\" 本质上不可靠\n- 4 个 non-confirming cases 的 post-hoc \"failure mode\" 归因 vs 更简约的 \"PermG FPR 差异\" 解释未被讨论\n\n**Required action**: (a) 标题修改以反映实际 scope（主要是 Pythia-410M 的发现）；(b) Abstract 将 cross-arch 重新措辞为 \"exploratory probes at α=1.0\"；(c) §5.5 添加 alternative explanation paragraph。\n\n---\n\n**MF-3 [critical, 双方共识]: Power-law boundary 参数不可识别，但被高精度呈现**\n\nβ 的 MLE = 0.66 vs CV = 0.24，profile CI [0.24, 0.78]——指数 γ 从 0.64 到 2.08 任意取值。Abstract 中 \"LOO-CV: MAE=0.037, 15/15 within CI\" 在 3-5 个 T 值上无鉴别力（任何光滑单调函数都能达到类似 MAE）。Sync-dip excluded（5 cells）是 post-hoc 操作；included 后 MAE = 0.203 (5.5×)，暴露模型 systematic failure。\n\n**Required action**: (a) Abstract 删除 MAE=0.037 和 \"15/15 within CI\"；(b) 将 boundary 定位为 qualitative trend (α_c 随 T 递减) 而非精确幂律；(c) 正文报告 γ 的完整 CI；(d) 并列呈现 sync-dip included/excluded 两组拟合。\n\n---\n\n**MF-4 [critical, R2 主导，R1 同意超限]: 页数超出 EMNLP 2026 8 页限制**\n\nTable 1 和 Figure 6（§5.5/5.6 引用的正文元素）被 LaTeX 浮动到 page 9。估计主文约 8.5–8.6 页，超限约 0.5 页。EMNLP 2026 strict 8-page limit 不含 Limitations。\n\n**Required action**: 压缩正文（如将 Table 1 移至 Appendix，或合并 §5.5/5.6 到更紧凑的 subsection）以严格遵守 8 页。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1 [双方共识]: Intervention proof-of-concept 仅单一极端条件 (α=1.0, N=2, post-hoc threshold)**\n\n仍被列入 Contribution 1。Appendix H CUSUM comparison 显示 simple threshold 同效，削弱 Granger 框架的 practical advantage。建议从 Contribution 1 剥离为独立的 illustrative example。\n\n**SF-2 [R2 提出, R1 部分同意]: Design Principle 'formal design rationale' 作为独立贡献 oversells**\n\nR2 判 critical（near-trivial：连续量先于阈值量是信息论直觉）；R1 rebut（mode amplification 下的特定机制非公理，≥2 gen lag 非先验可知）。**Director 裁定 should-fix**：内容非 trivial，但 \"formal design rationale\" 的贡献措辞需降级为 \"empirically validated ordering principle\"。\n\n**SF-3 [双方共识]: Sync-dip (α=0.60) 作为 \"四大 regime 之一\" 但机制完全未解释**\n\nLimitations 承认 \"the sync-dip mechanism at α=0.60 remains open\"。建议降级为 \"three confirmed regimes + one unexplained anomaly\"。\n\n**SF-4 [R2 提出, R1 同意]: 写作信息密度过高**\n\n几乎每句含多个精确数字，关键 findings 淹没在数字洪流中。四 regime 术语引入顺序不统一。建议精确数字移到 tables/figures，正文保留定性描述。\n\n---\n\n### Minor Issues\n\n- Eq.1 sigmoid 上界 0.70 选择理由未说明\n- α 采样间隔不均匀 (0.10→0.25 跳跃) 理由未解释\n- Table 1 footnotes 信息过密，建议以 Appendix table 替代\n- Schaeffer et al. \"8 种 collapse 定义\" 中本文使用哪种未明确\n- Appendix K 对比表中 SIGMA 的 multi-architecture 标注可能不准确\n- Design Principle 与 Theorem 共享计数器，编号序列可能令读者混淆\n- bf16 vs fp32 的 sensitivity 在 abstract/contributions 中未反映\n- CUSUM 负面结果值得主文简要提及\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| PermG FPR 使 boundary 不可靠 | N1 critical | W3→升级 critical | **[AGREE] critical** |\n| 标题/cross-arch scope 过度 | N2 critical | N2 critical | **[AGREE] critical** |\n| Power-law 参数不可识别 | W1→升级 critical | N1 critical | **[AGREE] critical** |\n| 页数超限 | 同意 | W4 should-fix | **[AGREE] should-fix** |\n| Intervention 过薄 | W3 should-fix | W2 should-fix | **[AGREE] should-fix** |\n| Sync-dip 无解释 | W2 should-fix | W1 should-fix | **[AGREE] should-fix** |\n| 信息密度过高 | 同意 | W5 should-fix | **[AGREE] should-fix** |\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | Director 裁定 |\n|------|----|----|--------------|\n| Design Principle trivial? | should-fix (内容非 trivial，framing oversells) | N3 critical (近乎公理) | **should-fix** — R1 的 rebuttal 有理：mode amplification 下的特定机制和 ≥2 gen lag 非先验可知；但贡献措辞确实 oversells |\n| MMCT 等权投票 | W4 should-fix (缺 Type I 分析) | REBUT (有 empirical mitigation) | **minor** — Appendix M 的 4 种 weighting schemes 一致性 + null MMCT FPR=0% 提供了充分 empirical evidence |\n| Grid 多重比较 | W5 should-fix | REBUT (sigmoid fit 是 single test) | **minor** — onset claim 有 aggregate-level support (sigmoid + Fisher)，但 \"four regimes\" 命名应更谨慎 |\n\n---\n\n## Questions for Authors\n\n1. 如果 FPR 恰好在 5% 名义水平，α_c(T) 会如何移动？能否提供 FPR=5% vs 11.1% 下的敏感性分析？\n2. GPT-2-medium 的 50% FPR 是 PermG 在高 null-drift 架构上的根本局限，还是可通过架构特定校准解决？\n3. Sync-dip 是否在所有 seed 中一致出现？有无证据排除 seed-specific artifact？\n4. 如果仅保留 MMCT-conditioned claims (K≥3, 0% FPR)，abstract 和 contributions 的核心 findings 是否仍然成立？\n5. 为什么不使用 two-sample distributional tests (MMD, KS) 作为替代或补充 detection 方案？\n\n---\n\n## Missing References\n\n- **Adams & MacKay (2007)**: Bayesian online changepoint detection — Related Work 未覆盖 online change-point detection 经典文献\n- **Papana et al. (2013) / Siggiridou & Kugiumtzis (2016)**: 置换 Granger 因果性验证方面的工作\n- **Two-sample distributional testing literature** (MMD, Wasserstein): 作为替代 detection 方案未被系统讨论\n\n---\n\n## External Review\n\n**Status**: 未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**Status**: ✅ 完成\n\nFindings:\n- **[warning]** Pages 6-7-8 布局节奏失衡：pages 6-7 连续纯文本无 display item，page 8 塞入 Figures 3/4/5 导致每图面积偏小。建议将 Figure 3 或 4 前移均衡视觉节奏。\n- **[info]** Figures 3-5 axis labels、legend 字号约正文 65-70%，接近可读下限，建议 ≥70%。\n- **[info]** 前 2 页无视觉锚点，第一个 display item 在 page 3。ACL 格式下可接受。\n- **[info]** Figure 1 热力图分数标注字号偏小，PDF 屏幕阅读需放大。\n- **[info]** Appendix 末页填充约 55-60%（非严重问题）。\n\n---\n\n## Overall Assessment\n\n**Score: 3.0 — Findings**\n\n**Confidence: 4/5**\n\n**Rationale**:\n\n论文的 method-sensitivity finding（FPR 3%–92%）和 phase-diagram 框架具有真正的原创性和实用价值，统计方法论严谨度在 model collapse 文献中罕见。然而三个 critical 问题共同将论文拉至 Findings 水平：\n\n1. **FPR 膨胀 + null sample 不足** → 核心定量 claims (detection boundary) 的可靠性存疑\n2. **Scope overclaiming** → 标题和 abstract 承诺的泛化程度远超单架构 + α=1.0 探索的实际交付\n3. **Power-law boundary 参数不可识别** → Contribution 1 的定量核心本质上未确定\n\n这些问题不是 writing 问题——它们动摇了论文核心贡献的证据基础。如果作者能：(a) 增加 null control seeds 并报告保守版边界；(b) 校准标题/abstract 的 scope 与实际交付匹配；(c) 将 boundary 降级为定性趋势——论文有潜力从 Findings 上升至 Borderline Conference (3.5)。当前版本适合 Findings track。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 1 将 power-law boundary、canary mechanism 和 intervention 打包在一起，每项的 evidence level 差异很大（boundary: weak, canary: moderate, intervention: minimal）。建议拆分为独立 contributions 并明确各自的 evidence strength。\n- \"five families (345M–6.9B)\" 在第一页给读者设定了跨架构全面验证的期望，但实际仅 α=1.0 单点探索。\n\n### §3 Cascade Ordering\n- Design Principles 1-2 提供了有用的 motivation，但 \"formal design rationale\" 措辞暗示比实际提供的更深的形式化。建议改为 \"empirically motivated design principles\"。\n\n### §4 Method\n- PermG FPR 11.1% 的讨论足够诚实，但 MMCT consensus 作为 primary safeguard 的 role 应在 §4.1 开头而非末尾强调——让读者先知道 standalone PermG 的局限和论文的应对策略。\n- §4.2 的 boundary model 在参数不可识别的前提下，作为 contribution 的价值在于定性框架而非定量预测。\n\n### §5 Experiments\n- §5.2 的 sharp onset 是论文最引人注目的发现。Fisher exact test + cross-seed 一致性提供了 onset 存在性的强证据。但 α_c = 0.483 ± 0.006 的精度声明与 §5.1 自承认的 β 不可识别性矛盾。\n- §5.5 Cross-architecture: GPT-2-medium 的 50% standalone FPR 应在本节正文中以 caveat paragraph 呈现，而非仅在 Appendix Z 和 Limitations 中。读者可能只看 Table 1 的 \"6/8\"，不会注意到该结果在 50% FPR 背景下本质不可解读。\n- §5.6 Intervention: 从 page budget 角度，0.5 页用于 N=2 single-condition proof-of-concept 的 ROI 很低。该空间可更好地用于 §5.5 的 FPR caveat 或 §5.3 的 dip mechanism 讨论。\n\n### §6 Discussion\n- 篇幅合理但略显保守。鉴于 scope 需要收紧，Discussion 是添加 \"what this study does NOT claim\" 的自然位置。\n\n### Limitations\n- 全面且诚实。建议增加一句关于 intervention 的 limitation（仅在最有利条件下测试，practical applicability unknown）。\n\n### Format\n- **页数**: 需严格压缩至 8 页正文。\n- **Float placement**: Pages 6-7 纯文本 + page 8 图片堆积 = 不均衡，调整 float 命令。",
    "project": "distrib_canary_collapse",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
  }
}
```

</details>

---


### Tool result

_source line 1153 · 2026-05-24T14:19:53.495293+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_150c7ce908e05d7932315e0288cf5bfb:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4168
}
```

</details>

---


### Assistant

_source line 1154 · 2026-05-24T14:20:09.557748+00:00_

**Round 12 审稿完成。**

**Overall: 3.0 (Findings)**，R1 给 3.0，R2 给 3.5，综合裁定 3.0。

**4 个 Must-Fix**（双方共识 critical）：
1. PermG FPR 11.1% (CI 上界 30.4%) + null sample 仅 36 tests → 边界区域定量可靠性不足
2. 标题/Abstract scope 超过实际交付：landscape 仅 Pythia-410M，cross-arch 仅 α=1.0
3. Power-law boundary 参数 β 不可识别 (MLE 0.66 vs CV 0.24)，但被高精度呈现
4. 页数超出 8 页限制（Table 1 + Figure 6 溢出 page 9）

**4 个 Should-Fix**：intervention 过薄、Design Principle framing oversells、sync-dip 无机制解释、写作信息密度过高。

**核心优势**：method-sensitivity finding (FPR 3%–92%) 是真正有价值的贡献，phase-diagram 框架具原创性，统计方法论严谨度在同类文献中罕见。

报告已投递给 Research Director，Issue tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 113

## Round 113

2 recorded events


### User

_source line 1155 · 2026-05-24T14:20:12.114372+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心判断：

- **3 项共识**：幂律参数不可识别（升级为 critical）、标题 scope mismatch（critical）、sync-dip/intervention/页数/密度（should-fix）
- **2 项分歧**：我认为 PermG FPR 应为 critical（R2 仅列 should-fix）；我认为 Design Principle 不是 trivial 而是 overclaimed（R2 列 critical）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1156 · 2026-05-24T14:20:28.168570+00:00_

Round 12 审稿已完成。

**最终评分：3.0 — Findings**

报告已投递给 Research Director。核心结论：

- **4 个 Must-Fix (critical)**：PermG FPR 膨胀使边界定量不可靠、标题/cross-arch scope 过度宣称、power-law 参数不可识别但高精度呈现、页数超出 8 页限制
- **4 个 Should-Fix**：intervention 过薄、Design Principle framing oversells、sync-dip 机制未解释、写作信息密度过高
- **2 个 Reviewer 分歧**已由 Director 裁定：Design Principle → should-fix（非 trivial 但 overclaimed）；MMCT 等权投票 → minor（有充分 empirical mitigation）

论文的 method-sensitivity finding 和 phase-diagram 框架具有真正价值，但 FPR 不确定性、scope overclaiming、boundary 参数不可识别三个问题共同动摇了核心贡献的证据基础。Issue tracker 已同步更新（含 R12 全部新发现和历史 issue 状态）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 114

## Round 114

60 recorded events


### User

_source line 1157 · 2026-05-24T14:53:14.471983+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distrib_canary_collapse
- 论文路径: projects/distrib_canary_collapse/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1158 · 2026-05-24T14:53:20.297443+00:00_

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
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1159 · 2026-05-24T14:53:20.398711+00:00_

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
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1160 · 2026-05-24T14:53:30.603062+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1161 · 2026-05-24T14:53:30.603484+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1162 · 2026-05-24T14:53:34.770454+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1163 · 2026-05-24T14:53:35.675169+00:00_

{"result":"# 项目 distrib_canary_collapse 概况\n\n## 实验状态 (214 个)\n\n- **gen_wiki_gpt2m_a100_s42_v3**: DONE (success) — \n- **mvp_v4_rep44**: DONE (success) — \n- **plan_006_s42**: DONE (failed) — \n- **plan_006_s42_resume**: DONE (killed) — \n- **gen_wiki_gpt2m_a100_s42_v2**: DONE (killed) — \n- **method_ablation_phase2**: DONE (success) — \n- **alpha_sweep_a025_s42_v3**: DONE (success) — \n- **method_ablation_phase1**: DONE (success) — \n- **plan_009_bootstrap_ty**: DONE (success) — \n- **mvp_v3_rep43**: DONE (failed) — \n- **mvp_v3_rep42**: DONE (failed) — \n- **mvp_v2_rep43**: DONE (killed) — \n- **mvp_v2_rep42**: DONE (killed) — \n- **mvp_rep43**: DONE (killed) — \n- **mvp_rep42**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- 14b_t10_a060_s43（准备中）\n- 14b_t10_a075_s43（准备中）\n- 14b_t10_a050_s43（准备中）\n- t15_a050_s42_fp32（准备中）\n- qwen35_dryrun_launch（准备中）\n\n## 近期结论\n- **null_t15_s42_fp32** (success): FPR verification at T=15: null condition (α=0.00) should show 0% PermG detection rate with longer observation window, confirming FPR control generalizes across T\n- **null_t15_s43_fp32** (success): FPR verification at T=15: null condition (α=0.00) should show 0% PermG detection rate with longer observation window, confirming FPR control generalizes across T\n- **null_gpt2m_s43_fp32** (success): Cross-architecture FPR verification: GPT-2-medium null (α=0.00) should show 0% PermG detection rate, confirming method is not architecture-specific\n\n## 趋势\n成功 153 / 负向 4 / 失败 22 / 共 209\n累计 GPU: 8.4h\nrobust_pairs_K3: 0 →（近 3 次 success）\ntotal_pairs: 6 →（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-17855: 无 GPU 信息\nwestd-19828: 空闲 cuda:0, cuda:1\n\n## 告警\n- mvp_rep42: 已被终止 — unknown\n- mvp_rep43: 已被终止 — unknown\n- mvp_rep44: 已被终止 — unknown\n- mvp_v2_rep42: 已被终止 — unknown\n- mvp_v2_rep43: 已被终止 — unknown\n- mvp_v2_rep44: 已被终止 — unknown\n- mvp_v3_rep42: 训练失败 — unknown\n- mvp_v3_rep43: 
…[truncated 1803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1164 · 2026-05-24T14:53:35.675571+00:00_

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
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
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

_source line 1165 · 2026-05-24T14:53:35.776440+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1166 · 2026-05-24T14:53:40.796461+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 1167 · 2026-05-24T14:53:43.607438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 1168 · 2026-05-24T14:53:44.059449+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{graphicx}
13	\usepackage{booktabs}
14	\usepackage{subcaption}
15	\usepackage{algorithm}
16	\usepackage{algpseudocode}
17	\usepackage{amsthm}
18	\newtheorem{theorem}{Theorem}
19	\newtheorem{proposition}[theorem]{Proposition}
20	\newtheorem{designprinciple}[theorem]{Design Principle}
21	\theoremstyle{definition}
22	\newtheorem{assumption}[theorem]{Assumption}
23	
24	\title{Characterizing the Detectability Landscape of Iterative Model Collapse}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\maketitle
30	
31	\input{abstract}
32	\input{introduction}
33	\input{related_work}
34	\input{method}
35	\input{experiments}
36	\input{discussion}
37	\input{limitations}
38	\bibliography{references}
39	
40	\input{appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1169 · 2026-05-24T14:53:44.160309+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1170 · 2026-05-24T14:53:45.013907+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"EMNLP 2026 Workshop NLLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FNLLP_ARR_Commitment"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"}]

Based on the search results, here's the information about EMNLP 2026 call for papers submission deadline via ARR:

Papers must be submitted, at latest, by the ARR 2026 May cycle. More specifically, the ARR paper submission deadline is May 25, 2026.

Additionally, given that the ARR 2026 May cycle is aligned with two c
…[truncated 456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "elapsed_ms": 4217
}
```

</details>

---


### Tool result

_source line 1171 · 2026-05-24T14:53:45.014466+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'distrib_canary_collapse'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 1172 · 2026-05-24T14:53:51.790325+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 author guidelines page limit format template anonymity",
  "allowed_domains": "['2026.emnlp.org', 'aclweb.org', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 author guidelines page limit format template anonymity",
    "allowed_domains": "['2026.emnlp.org', 'aclweb.org', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 1173 · 2026-05-24T14:53:52.543705+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1174 · 2026-05-24T14:53:52.995718+00:00_

1	\begin{abstract}
2	Iterative training on model-generated text degrades distributional quality well before standard metrics flag collapse, yet detecting this degradation is difficult: the time series are short ($T{\leq}25$ generations), the signal grows sub-linearly with contamination fraction, and, as we show, the choice of statistical test alone can shift conclusions from universal detection to complete null.
3	We map the detectability landscape of this process on Pythia-410M across 13 contamination levels; cross-architecture evaluation at $\alpha{=}1.0$ supports forward detection in 11/15 conditions across five families (345M--6.9B), with four non-confirming conditions isolating distinct failure modes.
4	Permutation Granger causality (PermG) reveals a detection boundary consistent with power-law scaling in observation length and three confirmed regimes---blind, onset, detection---plus one unexplained non-monotonic anomaly, including a sharp onset where detection jumps from 0/8 to 6/8 within a 2-percentage-point interval.
5	Five methods applied to identical data yield null-control false positive rates from 3\% to 92\%, exposing method sensitivity as a primary concern.
6	Entropy Granger-precedes diversity collapse by ${\geq}1$ generation (14/15 experiments), providing a canary whose triggered cessation substantially reduces peak perplexity in a proof-of-concept demonstration ($N{=}2$, $\alpha{=}1.0$).
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1175 · 2026-05-24T14:53:52.996085+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1176 · 2026-05-24T14:53:53.247329+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\cite{shumailov2024curse,alemohammad2024mad}.
5	This process can be triggered by vanishingly small synthetic fractions~\cite{dohmatob2025strong}: lexical diversity narrows, calibration deteriorates, and each generation inherits the biases of its predecessors.
6	As machine-generated text grows prevalent on the web, such feedback loops pose a growing risk to production pipelines, and by the time standard quality metrics register degradation, the distribution may have already shifted irreversibly.
7	
8	This threat motivates a fundamental question: \emph{what does the detectability landscape of model collapse look like?}
9	At what contamination level does statistical detection become possible, how does this boundary depend on observation length, and what structure does the landscape exhibit?
10	These questions are nontrivial because iterative training produces short, noisy time series (often fewer than 15 points), where detection power drops sharply~\cite{boettiger2012limits}. Moreover, model collapse is a first-order transition~\cite{truong2026phase}, structurally ruling out the critical-slowing-down early-warning signals that ecologists rely on~\cite{scheffer2009early} (\S\ref{sec:related_work}).
11	
12	We map this landscape on Pythia-410M~\cite{biderman2023pythia} across 13 contamination levels with multi-seed replication (Figure~\ref{fig:regime_map}), and find structured terrain rather than smooth degradation: detection is absent through $\alpha{=}0.45$, then jumps from 0/8 to 6/8 significant pairs within a 2-percentage-point interval, before a non-monotonic dip and eventual reliable detection above a power-law boundary $\alpha_c(T)$ (Eq.~\ref{eq:alpha-c-theory}).
13	Cross-architecture evaluation at $\alpha{=}1.0$ across five families (345M--6.9B) supports
…[truncated 2541 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1177 · 2026-05-24T14:53:53.247674+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1178 · 2026-05-24T14:53:53.298176+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Cascade Ordering}
5	\label{sec:cascade}
6	
7	If distributional collapse follows a predictable ordering across metrics, the earliest-responding metric can serve as a canary signal.
8	We formalize known metric properties---entropy as a continuous indicator of mode concentration, diversity as a threshold indicator of lexical coverage---under mode amplification~\cite{shumailov2024curse,dohmatob2024tale} (derivations in Appendix~\ref{app:cascade_theory}).
9	
10	\begin{designprinciple}[Entropy responds before diversity]\label{thm:entropy_leads}
11	Under mode amplification: \textup{(a)} entropy can decrease while the $\epsilon$-effective support $S_\epsilon(p) {=} |\{i: p_i > \epsilon\}|$ (hence distinct-$n$) is unchanged; \textup{(b)} if distinct-$n$ decreases, entropy has already decreased.
12	\end{designprinciple}
13	
14	The asymmetry arises because entropy responds to any mass redistribution (first-order), while diversity changes only when a token probability crosses the generation threshold~$\epsilon$; the margin $\gamma = \min_{i: p_i > \epsilon}(p_i - \epsilon)$ quantifies how much shift diversity absorbs silently.
15	
16	\begin{designprinciple}[Diversity lag $\geq 1$ generation]\label{prop:div_lag}
17	If the per-generation perturbation satisfies $\alpha\|\mathcal{T}(p_t) - p_t\|_\infty < \gamma(p_t, \epsilon)$ through entropy onset $t_H$, then diversity onset $t_D \geq t_H + 1$.
18	\end{designprinciple}
19	
20	ECE co-moves with entropy at zero lag: peakier conditionals simultaneously decrease per-token entropy and increase confidence ($\Delta\mathrm{ECE} \approx \Delta C > 0$ whenever $\Delta\bar{H} < 0$; qualitative argument in Appendix~\ref{app:cascade_theory}).
21	The predicted cascade $\{H, \mathrm{ECE}\} \to \mathrm{Distinct}$-$n$ holds in 14/15 experiments at $\alpha \geq 0.30$ (GPT-2-medium s43 bidirectional; within-domain WikiText, $2\sigma$ onset threshold): entropy and ECE onset at generation~1, dis
…[truncated 10357 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1179 · 2026-05-24T14:53:57.957207+00:00_

Web search results for query: "EMNLP 2026 author guidelines page limit format template anonymity"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Empirical Methods in Natural Language Processing EMNLP 2022 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/empirical-methods-natural-language-processing-emnlp-2022"}]

Based on the search results, I found some information about EMNLP 2026 author guidelines. Here's what I found:

## EMNLP 2026 Author Guidelines

**Anonymity Requirements:**
Industry Track submissions must neither include the authors' names nor their affiliations. More broadly, papers must not include authors' names and affiliations, and self-references that reveal the authors' identities must be avoided. Additionally, submi
…[truncated 987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "elapsed_ms": 6166
}
```

</details>

---


### Tool call

_source line 1180 · 2026-05-24T14:54:04.211761+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1181 · 2026-05-24T14:54:04.614050+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study the detectability landscape of iterative training collapse using Pythia-410M~\cite{biderman2023pythia} (410M parameters, decoder-only) as the primary architecture, with cross-architecture validation on five families (later verified in \S\ref{sec:generalization}).
8	Training data is drawn from WikiText-103~\cite{merity2017pointer} following the replace paradigm of~\citet{shumailov2024curse}: each generation fine-tunes on a mixture of $\alpha$ synthetic and $(1{-}\alpha)$ real data, generates 5{,}000 replacement samples, and fully replaces the synthetic pool (hyperparameters in Appendix~\ref{app:training_details}; notation in Appendix~\ref{app:background}).
9	We run $T{=}10$ generations across 13 contamination levels ($\alpha \in \{0.00, 0.05, 0.10, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.75, 1.00\}$, including null control) with multi-seed replication (4 seeds at $\alpha{=}1.0$; 3 at primary levels).
10	
11	We track two \emph{canary metrics} (token entropy and ECE) and three \emph{downstream metrics}: distinct-1, distinct-2~\cite{li2016diversity}, and perplexity (distinct-3: Appendix~\ref{app:distinct3}).
12	All hypothesis tests apply BH-FDR correction~\cite{benjamini1995controlling} at $q{=}0.05$; PermG uses 5{,}000 permutations on first-differenced series~\cite{shojaie2022granger} with maximum lag~5 (window sensitivity: Appendix~\ref{app:window_sensitivity}).
13	As in \S\ref{sec:method}, PermG tests temporal precedence, not causation.
14	
15	
16	\subsection{Sharp Detection Onset}
17	\label{sec:regime}
18	
19	Diversity collapse occurs at every contamination level: distinct-1 declines by $14.1\%$ even at $\alpha{=}0.0$ (fine-tuning drift) and by $40.3{\pm}0.3\%$ at $\alpha{=}0.25$ (3-seed mean).
20	Despite this ubiquitous degradation, Granger detectability is sharply regime-dependent.
21	PermG finds 0/8 canary$\to$downstream pairs FDR-sig
…[truncated 10249 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1182 · 2026-05-24T14:54:04.714853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1183 · 2026-05-24T14:54:05.116830+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and monitoring.}
5	Iterative training collapse was formalized by \citet{shumailov2024curse} and \citet{alemohammad2024mad}; \citet{schaeffer2025position} systematize eight distinct notions of collapse---our operationalization aligns with their \emph{distributional shift} family (definitions~D4--D6).
6	Theoretical analyses sharpen these results: \citet{dohmatob2024tale} recast collapse as changed scaling-law exponents, \citet{dohmatob2025strong} proved collapse at vanishingly small synthetic fractions, and \citet{truong2026phase} prove entropy collapse is a first-order transition, structurally ruling out critical-slowing-down early-warning signals~\cite{scheffer2009early,scheffer2012anticipating}.
7	Monitoring metrics include ECE~\cite{du2025scales}, surplexity~\cite{gambetta2024surplexity}, and machine-generated text detection~\cite{drayson2025detection}; \citet{shi2025closer} independently validate entropy as a collapse diagnostic in diffusion models.
8	We differ from prior work by cross-validating five statistical methods, mapping detectability across contamination regimes, and treating method sensitivity as a primary finding (comparison: Appendix~\ref{app:method_comparison}).
9	
10	\paragraph{Phase transitions and lead-lag methodology.}
11	Critical mixture ratios separating qualitative outcomes have precedent: \citet{kazdan2025collapse} map collapse conditions, \citet{gu2024cmr} establish scaling laws for critical ratios, and \citet{gu2025datamixing} show data mixing induces phase transitions in knowledge acquisition.
12	For temporal precedence testing, Granger causality~\cite{granger1969investigating} is standard, with neural extensions~\citep{tank2021neural,runge2019detecting}; however, non-stationary series inflate rejection rates~\cite{granger1974spurious}, and short series ($T{\leq}25$) preclude reliable nonlinear estimation~\cite{boettiger2012limits}.
13	Our Granger-precedenc
…[truncated 397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1184 · 2026-05-24T14:54:05.167676+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1185 · 2026-05-24T14:54:05.418965+00:00_

1	\section{Discussion and Conclusion}\label{sec:discussion}
2	
3	\paragraph{Scope and failure modes.}
4	Our Granger-precedence claim is scoped to temporal predictive improvement~\cite{granger1969investigating,shojaie2022granger}: bivariate tests cannot exclude confounders, and the FPR CI ($[1.2\%, 30.4\%]$) means Type~I error may be non-negligible.
5	Entropy's greater sensitivity to distributional shifts than $n$-gram diversity means the temporal lead may partly reflect measurement sensitivity rather than a causal cascade.
6	Four of fifteen cross-architecture conditions do not confirm forward detection (\S\ref{sec:generalization}), each violating one PermG assumption: precision sensitivity (GPT-2 bf16), seed dependence (Pythia-1.4B), and entropy decoupling (SmolLM3-3B, where non-monotonic entropy breaks the cascade ordering entirely).
7	These patterns require verifying monotonic entropy response and architecture-specific null calibration (GPT-2 standalone FPR: 50\%) before deployment (Appendix~\ref{app:extended_discussion}).
8	
9	\paragraph{Conclusion.}
10	Method choice alone shifts null-control FPR from 2.8\% to 91.7\%, establishing that single-method analyses cannot reliably distinguish temporal precedence from artifacts.
11	PermG, the lowest-FPR directional method (11.1\%), yields token entropy one-generation-ahead precedence over diversity collapse (24/24 forward, 0/24 reverse at $\alpha{=}1.0$; ${\geq}6/8$ in 11/15 cross-architecture conditions).
12	The blind zone below $\alpha_c$ constrains practical deployment to settings with sufficient contamination; evaluation at ${>}$7B parameters remains open.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1186 · 2026-05-24T14:54:05.419480+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1187 · 2026-05-24T14:54:05.520140+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our landscape characterization uses Pythia-410M as the primary architecture; the phase diagram is Pythia-family-only, frontier-scale behavior (${>}$7B) is untested, and cross-architecture evaluation is limited to $\alpha{=}1.0$.
5	PermG's empirical FPR is 11.1\% (CI $[1.2\%, 30.4\%]$) and $K{\geq}3$ consensus yields 16.7\% (6/36); per-condition detection rates carry wide binomial CIs (e.g., $[0.25, 0.92]$ for 6/8), so the phase diagram represents a coarse topology rather than precise probability estimates.
6	All experiments use full replacement with a single decoding strategy (temperature~$1.0$, top-$k{=}50$); data accumulation~\cite{dey2024breaking} or lower temperatures would shift the landscape.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1188 · 2026-05-24T14:54:13.450711+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1189 · 2026-05-24T14:54:13.953017+00:00_

File content (35496 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1190 · 2026-05-24T14:54:13.953481+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "config.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "file": "config.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1191 · 2026-05-24T14:54:14.104376+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1192 · 2026-05-24T14:54:16.915816+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1193 · 2026-05-24T14:54:17.368145+00:00_

1	\appendix
2	
3	\section{Training Details and Metric Drift}
4	\label{app:training_details}
5	\label{app:drift}
6	
7	\paragraph{Hyperparameters.}
8	Each generation fine-tunes for 5{,}000 steps using AdamW (learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium).
9	Generation uses temperature $1.0$, top-$k{=}50$, max length 512 tokens, producing 5{,}000 samples per generation from 5{,}000-sample subsets of WikiText-103.
10	Canary metrics: token entropy $H(p_\theta | \text{context})$ over 1{,}000 held-out samples; ECE with 15 bins.
11	Additional downstream metrics (distinct-3, effective rank, Self-BLEU) appear in subsequent appendix sections.
12	
13	\paragraph{Metric drift.}
14	
15	\begin{table}[h]
16	\centering
17	\small
18	\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
19	\label{tab:drift_summary}
20	\resizebox{\columnwidth}{!}{%
21	\begin{tabular}{lccccc}
22	\toprule
23	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
24	\midrule
25	0.00 & $-4.6{\pm}0.4$ & $+37.6{\pm}14$ & $-14.1{\pm}0.4$ & $-9.6{\pm}0.4$ & $-20.6{\pm}1.0$ \\
26	0.10$^\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\
27	0.25 & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & $-18.1{\pm}0.8$ \\
28	0.50 & $-18.0{\pm}0.5$ & $+822.6{\pm}18.3$ & $-37.1{\pm}0.4$ & $-50.4{\pm}1.0$ & $+21.0{\pm}0.1$ \\
29	0.75 & $-27.6{\pm}0.2$ & $+1791{\pm}18$ & $-32.3{\pm}0.5$ & $-41.0{\pm}1.0$ & $+182.6{\pm}
…[truncated 11152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1194 · 2026-05-24T14:54:17.820363+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "glob": "*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
    "glob": "*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1195 · 2026-05-24T14:54:18.523679+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Grep",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 1196 · 2026-05-24T14:54:18.523984+00:00_

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
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
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

_source line 1197 · 2026-05-24T14:54:18.624508+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1198 · 2026-05-24T14:54:29.810435+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1199 · 2026-05-24T14:54:30.275382+00:00_

&lt;persisted-output>
Output too large (41.2KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-review-director-741faaa0/a0ad0191-8da0-4720-ae36-297d6a05b53c/tool-results/toolu_01B2MYhr853Ss2NyRf6ikKig.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_reports/round_8.md:162:**状态：未启用。** 项目配置未开启外部审稿（`external_review.paperreview_ai.enabled` 未配置）。
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/chats/worker_analysis_r3_intervention_threshold_sensitivity_20260520T155337.jsonl:5:[Omitted long matching line]
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:163:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:163:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_repo
…[truncated 259 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Grep",
  "elapsed_ms": 464
}
```

</details>

---


### Tool call

_source line 1200 · 2026-05-24T14:54:30.878329+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1201 · 2026-05-24T14:54:31.681707+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Glob",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1202 · 2026-05-24T14:54:31.732401+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "description": "Count appendix lines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "description": "Count appendix lines"
  }
}
```

</details>

---


### Tool result

_source line 1203 · 2026-05-24T14:54:31.883440+00:00_

1343 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1204 · 2026-05-24T14:54:38.061058+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-24T14:54:38.212247+00:00_

1	issues:
2	# ============================================================
3	# Round 1-11 历史 resolved — 保留跨轮次记录
4	# ============================================================
5	- id: "R1-N1"
6	  summary: "Ground-truth pairs 定义存在循环论证"
7	  category: method
8	  severity: critical
9	  status: resolved
10	  first_raised_round: 1
11	  last_seen_round: 1
12	  resolution: "Effect-size GT 重定义完成。"
13	  resolution_round: 1
14	
15	- id: "R1-N2"
16	  summary: "FPR=0% 标定仅基于单 seed"
17	  category: method
18	  severity: critical
19	  status: resolved
20	  first_raised_round: 1
21	  last_seen_round: 1
22	  resolution: "α=0.0 三 seed FPR 验证完成。"
23	  resolution_round: 1
24	
25	- id: "R1-N3"
26	  summary: "α=0.50 和 α=0.75 仅 1 seed"
27	  category: experiment
28	  severity: critical
29	  status: resolved
30	  first_raised_round: 1
31	  last_seen_round: 1
32	  resolution: "Multi-seed 补充完成。"
33	  resolution_round: 1
34	
35	- id: "R2-N1"
36	  summary: "核心方法论为计量经济学已有知识的直接迁移，新颖性有限"
37	  category: framing
38	  severity: critical
39	  status: resolved
40	  first_raised_round: 1
41	  last_seen_round: 2
42	  resolution: "Round 1 三层定位 reframe 完成。"
43	  resolution_round: 1
44	
45	- id: "R2-N2"
46	  summary: "α=0.75 multi-seed 实验未完成 + Appendix A 缺失"
47	  category: experiment
48	  severity: critical
49	  status: resolved
50	  first_raised_round: 1
51	  last_seen_round: 1
52	  resolution: "完成。"
53	  resolution_round: 1
54	
55	- id: "R2-N3"
56	  summary: "实验规模过窄"
57	  category: experiment
58	  severity: critical
59	  status: resolved
60	  first_raised_round: 1
61	  last_seen_round: 1
62	  resolution: "跨架构验证已扩展至 15 model-seed 组合。"
63	  resolution_round: 1
64	
65	- id: "R1-W1"
66	  summary: "Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致"
67	  category: writing
68	  severity: warning
69	  status: resolved
70	  first_raised_round: 1
71	  last_seen_round: 2
72	  resolution: "核心修复完成。"
73	  resolution_round: 1
74	
75	- id: "R1-W2"
76	  summary: "PermG 缺少 power analysis"
77	  category: metho
…[truncated 3041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1206 · 2026-05-24T14:54:40.019368+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_13/submitted.pdf",
  "pages": "1-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_13/submitted.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool call

_source line 1207 · 2026-05-24T14:54:40.274461+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1208 · 2026-05-24T14:54:40.425465+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_reports/round_11.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_reports/round_12.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 1209 · 2026-05-24T14:54:40.729611+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_13/submitted.pdf (1.1MB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 710
}
```

</details>

---


### Tool call

_source line 1210 · 2026-05-24T14:55:20.600925+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "distrib_canary_collapse",
  "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
  }
}
```

</details>

---


### Tool result

_source line 1211 · 2026-05-24T14:55:47.909654+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 27308
}
```

</details>

---


### Tool call

_source line 1212 · 2026-05-24T14:55:48.965158+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验有效性**。\n\n## 论文信息\n- **标题**: Characterizing the Detectability Landscape of Iterative Model Collapse\n- **路径**: projects/distrib_canary_collapse/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_13/submitted.pdf\n- **目标 venue**: EMNLP 2026 (ARR Long Paper)\n- **Deadline**: ARR May 2026 cycle (2026-05-25)\n- **格式**: ACL 模板, double-blind, 正文 ≤ 8 页, Limitations 不计入页数, 参考文献不限\n- **匿名规则**: Double-blind，不能包含作者信息，不能有非匿名代码链接\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 统计方法论\n- PermG (Permutation Granger causality) 的有效性：FPR 11.1% 超过 nominal 5%，CI [1.2%, 30.4%] 极宽，这是否undermines核心claims？\n- 第一差分处理的充分性：canary→perplexity 被 first-differencing 消除（F≈0, p=0.99），这是否说明连 canary→diversity 也可能受 shared-trend 影响？\n- K≥3 共识投票：五方法 FPR 从 3% 到 92%，κ=0.185（几乎无agreement），共识投票是否有统计理论支撑？\n- Detection boundary 的 power-law fitting：β 参数 poorly identified（MLE 0.66 vs CV 0.24），γ 的 95% CI 跨越 [0.64, 2.08]，这种拟合是否有实质意义？\n\n### 2. 实验设计\n- 主实验仅用 Pythia-410M (410M params)，cross-architecture 仅在 α=1.0（full replacement）验证——这是否足以支撑 \"landscape\" 的 claim？\n- Multi-seed replication：α=0.10 仅单 seed，其他 primary levels 仅 3 seeds——样本量是否足够？\n- WikiText-103 单一数据集 + full replacement paradigm——实际场景中数据累积 (accumulation) 更常见\n- 非单调异常 (α=0.60)：作者标注 \"unexplained\"——一个核心发现的解释缺失是否可接受？\n\n### 3. Claims vs Evidence 对齐\n- Abstract claims（\"canary whose triggered cessation substantially reduces peak perplexity\"）vs 实际 N=2、α=1.0、post-hoc threshold 的 proof-of-concept——是否夸大？\n- \"detectability landscape\" 的 claim vs 单架构 + 有限 α 网格的实际覆盖——是否过度泛化？\n- 14/15 experiments 的 cascade ordering claim——那 1/15 的例外是否削弱了 Design Principle 的理论性？\n\n### 4. Canary Intervention (§4.6)\n- N=2 architectures, post-hoc threshold, 单一 α=1.0——作为贡献点是否足够？\n- CUSUM 对比被放在 appendix 且标注 \"not rigorously evaluated\"——这是否应被移除或加强？\n\n请按以下结构输出审稿意见：\n1. Summary (2-3句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/major/minor)\n4. Questions (需作者回答)\n5. Missing References (如有)\n6. Overall Assessment (评分 + 理由，使用上述 EMNLP 评分标准)\n7. Confidence (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验有效性**。\n\n## 论文信息\n- **标题**: Characterizing the Detectability Landscape of Iterative Model Collapse\n- **路径**: projects/distrib_canary_collapse/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_13/submitted.pdf\n- **目标 venue**: EMNLP 2026 (ARR Long Paper)\n- **Deadline**: ARR May 2026 cycle (2026-05-25)\n- **格式**: ACL 模板, double-blind, 正文 ≤ 8 页, Limitations 不计入页数, 参考文献不限\n- **匿名规则**: Double-blind，不能包含作者信息，不能有非匿名代码链接\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 统计方法论\n- PermG (Permutation Granger causality) 的有效性：FPR 11.1% 超过 nominal 5%，CI [1.2%, 30.4%] 极宽，这是否undermines核心claims？\n- 第一差分处理的充分性：canary→perplexity 被 first-differencing 消除（F≈0, p=0.99），这是否说明连 canary→diversity 也可能受 shared-trend 影响？\n- K≥3 共识投票：五方法 FPR 从 3% 到 92%，κ=0.185（几乎无agreement），共识投票是否有统计理论支撑？\n- Detection boundary 的 power-law fitting：β 参数 poorly identified（MLE 0.66 vs CV 0.24），γ 的 95% CI 跨越 [0.64, 2.08]，这种拟合是否有实质意义？\n\n### 2. 实验设计\n- 主实验仅用 Pythia-410M (410M params)，cross-architecture 仅在 α=1.0（full replacement）验证——这是否足以支撑 \"landscape\" 的 claim？\n- Multi-seed replication：α=0.10 仅单 seed，其他 primary levels 仅 3 seeds——样本量是否足够？\n- WikiText-103 单一数据集 + full replacement paradigm——实际场景中数据累积 (accumulation) 更常见\n- 非单调异常 (α=0.60)：作者标注 \"unexplained\"——一个核心发现的解释缺失是否可接受？\n\n### 3. Claims vs Evidence 对齐\n- Abstract claims（\"canary whose triggered cessation substantially reduces peak perplexity\"）vs 实际 N=2、α=1.0、post-hoc threshold 的 proof-of-concept——是否夸大？\n- \"detectability landscape\" 的 claim vs 单架构 + 有限 α 网格的实际覆盖——是否过度泛化？\n- 14/15 experiments 的 cascade ordering claim——那 1/15 的例外是否削弱了 Design Principle 的理论性？\n\n### 4. Canary Intervention (§4.6)\n- N=2 architectures, post-hoc threshold, 单一 α=1.0——作为贡献点是否足够？\n- CUSUM 对比被放在 appendix 且标注 \"not rigorously evaluated\"——这是否应被移除或加强？\n\n请按以下结构输出审稿意见：\n1. Summary (2-3句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/major/minor)\n4. Questions (需作者回答)\n5. Missing References (如有)\n6. Overall Assessment (评分 + 理由，使用上述 EMNLP 评分标准)\n7. Confidence (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 1213 · 2026-05-24T14:56:09.103302+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20138
}
```

</details>

---


### Tool call

_source line 1214 · 2026-05-24T14:56:09.254634+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性**。\n\n## 论文信息\n- **标题**: Characterizing the Detectability Landscape of Iterative Model Collapse\n- **路径**: projects/distrib_canary_collapse/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_13/submitted.pdf\n- **目标 venue**: EMNLP 2026 (ARR Long Paper)\n- **Deadline**: ARR May 2026 cycle (2026-05-25)\n- **格式**: ACL 模板, double-blind, 正文 ≤ 8 页, Limitations 不计入页数, 参考文献不限\n- **匿名规则**: Double-blind，不能包含作者信息，不能有非匿名代码链接\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 贡献新颖性\n- 核心方法（Granger causality, permutation test, first-differencing）均为计量经济学成熟工具——直接迁移到 model collapse 检测是否构成足够的 methodological contribution？\n- \"Detectability landscape\" / \"phase diagram\" 的 framing 是否具有概念新颖性？还是对已知现象（detection power depends on effect size and sample size）的重新包装？\n- Design Principles 1-2 的理论贡献：entropy responds before diversity 是否在 information theory 层面显而易见？\n- 与 Gu et al. (2026) SIGMA（spectral insights for model collapse）的差异和互补性？\n\n### 2. Related Work 覆盖\n- 是否遗漏了 model collapse 领域的重要工作？特别关注 2025-2026 年的新进展\n- Granger causality 在 time series analysis 中的标准批评（Lucas critique, observational equivalence）是否被充分讨论？\n- 早期预警信号（early warning signals）领域的文献是否被充分利用？特别是 Dakos et al., Lenton et al. 等生态学 tipping point 工作\n- Phase transition 在 ML 中的文献（如 power law scaling, emergent abilities debate）是否应被引用？\n\n### 3. 写作质量\n- 论文结构是否清晰？Method 和 Experiments 的边界是否合理？\n- 术语使用一致性：Granger-causality vs Granger-precedence vs temporal predictive improvement\n- 数字密度过高（大量 X/Y pairs, CI, p-values）——是否影响可读性？\n- Abstract 是否在 200 words 以内？（EMNLP 2026 硬限制）\n- Conclusion 是否过短/缺少 future work？\n\n### 4. 格式合规\n- 正文是否严格 ≤ 8 页？（Limitations 不计入）\n- 是否 double-blind compliant？（检查作者信息、代码链接、致谢等）\n- 引用格式是否符合 ACL style（natbib）？\n- 附录是否合理组织？（1343 行——是否过多？审稿人不保证阅读附录）\n- Figure/Table 编号和引用是否一致？\n\n### 5. 实用性评估\n- 这项工作对 NLP 社区的实际价值是什么？谁会使用这些发现？\n- Canary intervention（§4.6）作为实用贡献是否足够成熟？\n- \"Blind zone\"（α≤0.45 不可检测）是否实际上削弱了整个方法的实用性？\n\n请按以下结构输出审稿意见：\n1. Summary (2-3句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/major/minor)\n4. Questions (需作者回答)\n5. Missing References (如有)\n6. Overall Assessment (评分 + 理由，使用上述 EMNLP 评分标准)\n7. Confidence (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性**。\n\n## 论文信息\n- **标题**: Characterizing the Detectability Landscape of Iterative Model Collapse\n- **路径**: projects/distrib_canary_collapse/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_13/submitted.pdf\n- **目标 venue**: EMNLP 2026 (ARR Long Paper)\n- **Deadline**: ARR May 2026 cycle (2026-05-25)\n- **格式**: ACL 模板, double-blind, 正文 ≤ 8 页, Limitations 不计入页数, 参考文献不限\n- **匿名规则**: Double-blind，不能包含作者信息，不能有非匿名代码链接\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 贡献新颖性\n- 核心方法（Granger causality, permutation test, first-differencing）均为计量经济学成熟工具——直接迁移到 model collapse 检测是否构成足够的 methodological contribution？\n- \"Detectability landscape\" / \"phase diagram\" 的 framing 是否具有概念新颖性？还是对已知现象（detection power depends on effect size and sample size）的重新包装？\n- Design Principles 1-2 的理论贡献：entropy responds before diversity 是否在 information theory 层面显而易见？\n- 与 Gu et al. (2026) SIGMA（spectral insights for model collapse）的差异和互补性？\n\n### 2. Related Work 覆盖\n- 是否遗漏了 model collapse 领域的重要工作？特别关注 2025-2026 年的新进展\n- Granger causality 在 time series analysis 中的标准批评（Lucas critique, observational equivalence）是否被充分讨论？\n- 早期预警信号（early warning signals）领域的文献是否被充分利用？特别是 Dakos et al., Lenton et al. 等生态学 tipping point 工作\n- Phase transition 在 ML 中的文献（如 power law scaling, emergent abilities debate）是否应被引用？\n\n### 3. 写作质量\n- 论文结构是否清晰？Method 和 Experiments 的边界是否合理？\n- 术语使用一致性：Granger-causality vs Granger-precedence vs temporal predictive improvement\n- 数字密度过高（大量 X/Y pairs, CI, p-values）——是否影响可读性？\n- Abstract 是否在 200 words 以内？（EMNLP 2026 硬限制）\n- Conclusion 是否过短/缺少 future work？\n\n### 4. 格式合规\n- 正文是否严格 ≤ 8 页？（Limitations 不计入）\n- 是否 double-blind compliant？（检查作者信息、代码链接、致谢等）\n- 引用格式是否符合 ACL style（natbib）？\n- 附录是否合理组织？（1343 行——是否过多？审稿人不保证阅读附录）\n- Figure/Table 编号和引用是否一致？\n\n### 5. 实用性评估\n- 这项工作对 NLP 社区的实际价值是什么？谁会使用这些发现？\n- Canary intervention（§4.6）作为实用贡献是否足够成熟？\n- \"Blind zone\"（α≤0.45 不可检测）是否实际上削弱了整个方法的实用性？\n\n请按以下结构输出审稿意见：\n1. Summary (2-3句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/major/minor)\n4. Questions (需作者回答)\n5. Missing References (如有)\n6. Overall Assessment (评分 + 理由，使用上述 EMNLP 评分标准)\n7. Confidence (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 1215 · 2026-05-24T14:56:10.614456+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1359
}
```

</details>

---


### Assistant

_source line 1216 · 2026-05-24T14:56:18.105345+00:00_

已派发：
- 视觉审查 Agent（fire-and-forget，不阻塞）
- Reviewer 1（方法严谨性 + 实验有效性）
- Reviewer 2（新颖性 + 完整性）

等待两名 Reviewer 返回 Round 1 初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 115

## Round 115

2 recorded events


### User

_source line 1217 · 2026-05-24T15:02:31.629995+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：Characterizing the Detectability Landscape of Iterative Model Collapse

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 一篇执行力强的实证研究，通过系统比较五种检测方法绘制了 model collapse 的可检测性相图，但核心方法全部借自计量经济学/时间序列分析，缺乏方法论创新，且盲区（α≤0.45）覆盖了实践中最相关的污染水平，削弱了实用价值。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计系统全面（13个污染级别、5种方法、多seed），统计方法运用正确（BH-FDR校正、置换检验），但主要分析仅基于Pythia-410M单一模型，Phase diagram的泛化性未充分验证 |
| Excitement | 2.5/5 | "可检测性相图"的framing有概念价值，但所有方法均为已有工具的直接应用；核心发现——检测能力依赖效应量和样本量——在统计学中是常识性结论 |
| Reproducibility | 4/5 | 实验细节详尽（Appendix A 超参数、Appendix J MMCT算法），但未提供代码链接（可能因double-blind），使用了AI辅助（page 28已披露） |
| Overall Assessment | 3.0/5 | Findings级别——实证工作扎实但方法论贡献不足以支撑主会议接收 |

## 1. Summary

本文研究 iterative model collapse 在什么条件下可被统计检测到。作者在 Pythia-410M 上跨13个污染级别（α∈[0.10, 1.0]）、T≤25代训练，系统比较了五种时间序列检测方法（naive cross-correlation, differenced cross-correlation, threshold onset, permutation Granger causality/PermG, Toda-Yamamoto），绘制了一张"可检测性相图"（phase diagram），发现三个区域（blind/onset/detection）及检测边界的幂律缩放关系。主要发现包括：(1) 方法选择对结论影响极大（null-control FPR从3%到92%）；(2) entropy 在diversity之前响应（Granger-precede ≥1代）；(3) 基于canary的干预概念验证。跨架构验证覆盖5个模型族（345M–6.9B）。

## 2. Strengths

**S1.** 方法敏感性分析是本文最有价值的发现。五种方法应用于同一数据，null-control FPR从3%（PermG）到92%（NaiveXCor），这个发现对社区有重要警示意义——它表明发表的 model collapse 检测结果高度依赖于方法选择，不同方法可从"全部检测到"翻转为"全部为null"（§3.3, Table 1）。

**S2.** 实验设计系统性强。13个污染级别 × 多seed × 5种方法 × T∈{5,10,15,20,25} × 跨架构验证，覆盖面在该领域罕见。MMCT（Multi-Method Consensus Test）共识框架（Algorithm 1, Appendix J）通过加权投票减少单一方法偏差，设计合理。

**S3.** "可检测性相图"（Figure 1）的概念贡献。将问题从"能否检测collapse"转化为"在什么(α, T)条件下检测成为可能"，这一reframing为后续工作提供了有用的分析框架。Phase diagram 的 blind/onset/detection 三区域划分及幂律边界（§3.4, Eq. 2）是有信息量的经验发现。

**S4.** 附录极为详尽（~20页），包含规范曲线分析（Appendix E）、Shapley分解（Appendix P）、非平稳性鲁棒性分析（Appendix O）、CUSUM对比（Appendix H）、互信息分析（Appendix V）等，展现了严谨的实证态度。

**S5.** Entropy → diversity 的 cascade ordering（Design Principle 1-2）有形式化推导（Appendix X, Propositions 4-5），从 mode amplification 假设出发给出了有理论支撑的解释。

## 3. Weaknesses

**W1. [Major] 方法论新颖性不足——所有核心方法均为成熟工具的直接迁移。**
- Granger causality（Granger, 1969）、置换检验（Phipson & Smyth, 2010）、first-differencing、CUSUM（Page, 1954）、Toda-Yamamoto（1995）均为计量经济学/统计过程控制的标准工具
- 本文的贡献是*应用*和*系统比较*，而非方法论创新。对于EMNLP主会议，纯应用性工作通常需要展示"迁移过程中的non-trivial技术挑战"或"领域特异性的方法适配"，但论文中这些工具的使用方式与其原始领域并无本质差异
- "Detectability landscape"本质上是检测功效（detection power）随效应量（α）和样本量（T）变化的二维映射——这在统计假设检验理论中是基本概念（power analysis），phase diagram的framing虽然直观，但概念新颖性有限

**W2. [Major] 盲区（α≤0.45, T≤10）覆盖了实践中最相关的污染场景，严重削弱实用价值。**
- 论文明确承认 α≤0.45 时 PermG 检测能力为 0/8（Figure 1）。在实际生产环境中，web-scraped 数据的合成内容比例通常在10%–40%范围（参见 Europol 2025 报告），恰好落在盲区内
- 这意味着本文提出的检测框架在最需要它的场景下无法工作
- §5 Discussion 仅用一句话提及"the blind zone below α_c ≈ 0.45"（p.8），未充分讨论这对实用性的影响，也未提供任何缓解方案

**W3. [Major] Phase diagram 的泛化性未充分验证——主要分析仅基于 Pythia-410M 单一模型。**
- 跨架构验证（§4.5）仅在 α=1.0（完全替换）这一极端条件下进行，4/15 conditions non-confirming
- α=1.0 是最容易检测的条件，在这个条件下 4/15 已经失败，说明泛化性存疑
- Phase diagram 的定量结论（幂律指数、检测边界位置）完全来自 Pythia-410M，对其他架构/规模的适用性未知
- Table 31（p.27）的跨架构结果显示 GPT-2-medium 的 null-control FPR 显著高于 Pythia-410M（100% vs. 11.1%），暗示架构依赖性可能根本性地改变相图

**W4. [Minor-Major] Canary intervention（§4.6）作为实用贡献严重不足。**
- 仅 N=2 seeds、α=1.0 单一条件的概念验证
- 干预策略是"stop training when canary fires"——这是最粗暴的二元干预，实际生产中几乎不可能直接停止训练
- 论文未讨论更细粒度的干预（如调整 synthetic data 比例、切换数据源等）
- Peak perplexity 降低 64% 的结果（Figure 6）来自 N=2 的极小样本，统计可靠性存疑

**W5. [Minor-Major] Design Principle 1（entropy responds before diversity）可能过于直观。**
- 在 mode amplification 下，entropy 是概率分布的全局汇总统计量，对任何概率质量的重新分配立即响应；而 distinct n-gram 计数只在 token 从生成文本中完全消失时才变化
- 这一排序在信息论层面较为直接——entropy 的连续性 vs. diversity 的离散性决定了前者的灵敏度必然更高
- 虽然 Propositions 4-5 提供了形式化证明，但证明的前提假设（Assumption 3: mode amplification）是非常强的，且结论的实质是"连续指标比离散指标更早响应微小变化"，这近乎 trivial
- 建议作者明确说明这一结果的 non-trivial 之处在哪里

**W6. [Minor] Related Work 存在重要遗漏。**
- **Early warning signals 文献**：论文仅引用了 Scheffer et al. (2009, 2012)，但完全未引用该领域的核心实证方法论贡献，特别是 Dakos et al. (2008, "Slowing down as an early warning signal for abrupt climate change", PNAS) 和 Dakos et al. (2012, "Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data", PLoS ONE)。鉴于本文的核心任务（从时间序列中检测系统性退化的早期信号）与 Dakos 的工作高度吻合，这一遗漏令人惊讶
- **Granger causality 的标准批评**：论文使用 Granger precedence 作为核心方法，但未讨论 Granger causality 在因果推断中的已知局限性（如 observational equivalence、Lucas critique 的相关性——检测到 collapse 后进行干预会改变训练动态，从而使 Granger 关系失效）
- **Guo et al. (2025)**：arXiv:2502.15654 "Machine-generated text detection prevents language model collapse" 与本文的 canary detection 主题直接相关，未引用

**W7. [Minor] 正文数字密度过高，影响可读性。**
- 仅 §3.3 一段就包含 "FPR 2.8%, 11.1%, 27.8%, 38.9%, 91.7%"、"(0/8 vs fp32: 6/8)"、"CI [1.2%, 30.4%]" 等大量数字对
- 建议将逐方法逐seed的 FPR 详细数据移至表格或附录，正文仅保留关键对比和趋势

**W8. [Minor] 术语一致性问题。**
- "Granger causality" vs "Granger-precedence" vs "temporal predictive improvement" 在文中交替使用。虽然 §3.1 做了区分（precedence ≠ causation），但后文时而回到 "Granger causality" 措辞，可能误导读者以为作者在做因果声明
- "Canary" 一词在不同上下文中含义不同：有时指 entropy metric 本身（"canary metric"），有时指 canary intervention 策略（§4.6）

## 4. Questions for Authors

**Q1.** Phase diagram 的检测边界（Eq. 2）在 Pythia-410M 上拟合得到，其幂律指数和边界参数对其他架构（如 GPT-2, Qwen）是否成立？如果不是，那么"detectability landscape"的主要贡献是否仅限于单一模型族的经验描述？

**Q2.** 在实际 web-scale 数据中，合成数据的污染比例通常是多少？如果普遍低于 α=0.45，那么本文的方法在实际部署中的适用范围是什么？作者是否考虑过增大 T（观察窗口）来补偿低 α 的检测困难？

**Q3.** 为什么不与 SIGMA（Gu et al., 2026）进行直接实验对比？两者都旨在监测 model collapse，SIGMA 使用 embedding 空间的谱分析，本文使用输出分布统计量——直接对比将大大增强贡献。

**Q4.** SmolLM1.3B 的非单调异常（p.7, Figure 5 注释）是否有进一步的解释？这是否暗示 phase diagram 的三区域划分可能不是普适的？

**Q5.** Design Principle 1 的核心insight——"连续统计量比离散统计量更早检测到微小分布偏移"——与信息论中的标准结果（如 entropy 对分布变化的连续响应性 vs. support size 的阶跃变化特征）有什么本质区别？

## 5. Missing References

- Dakos, V., et al. (2008). "Slowing down as an early warning signal for abrupt climate change." PNAS, 105(38), 14308-14312.
- Dakos, V., et al. (2012). "Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data." PLoS ONE, 7(7), e41010.
- Lenton, T.M., et al. (2008). "Tipping elements in the Earth's climate system." PNAS, 105(6), 1786-1793.
- Guo et al. (2025). "Machine-generated text detection prevents language model collapse." arXiv:2502.15654.
- 建议讨论 Granger causality 的标准局限性文献（如 Shojaie & Fox 2022 的 §4 "Limitations and extensions"，该文已被引用但相关限制未被讨论）

## 6. Overall Assessment

**评分: 3.0 (Findings)**

本文是一篇执行力强、实验覆盖面广的实证研究，其核心贡献在于：(1) 揭示了方法选择对 model collapse 检测结论的决定性影响（FPR 从3%到92%），(2) 绘制了可检测性相图并发现了检测边界的幂律缩放关系。这些发现对社区有参考价值。

但从EMNLP主会议的标准来看，存在三个核心不足：

**第一，方法论新颖性不足。** 所有核心方法（Granger causality, permutation test, first-differencing, CUSUM, Toda-Yamamoto）均为成熟工具的直接应用，论文的贡献本质上是"在model collapse领域做了一次系统性的方法对比实验"，而非提出或发展了新方法。

**第二，盲区限制实用性。** α≤0.45的盲区覆盖了实际场景中最可能出现的低-中污染水平，使得整个检测框架在最需要它的地方失效。论文未充分讨论这一问题，也未提供缓解方案。

**第三，泛化性未充分验证。** Phase diagram 仅在 Pythia-410M 上建立，跨架构验证限于 α=1.0 且有 4/15 失败，定量结论的可移植性不明。

综合来看，本文适合作为 Findings 接收——它提供了有价值的实证发现，但方法论和概念贡献不足以支撑主会议级别。

## 7. Confidence

**4/5** — 对 Granger causality、统计假设检验、model collapse 文献较为熟悉；对计量经济学方法在 NLP 中的应用有足够判断力。可能遗漏的细节主要在附录的某些鲁棒性分析中。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1218 · 2026-05-24T15:02:42.087509+00:00_

Reviewer 2 已提交审稿意见（评分 3.0 Findings）。等待 Reviewer 1 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 116

## Round 116

2 recorded events


### User

_source line 1219 · 2026-05-24T15:02:44.609452+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**核心结论：评分 3.0 (Findings)**

主要问题：
1. **方法论新颖性不足**：五种核心方法（Granger causality、置换检验、first-differencing、CUSUM、Toda-Yamamoto）全部是计量经济学成熟工具的直接迁移，无non-trivial的领域适配
2. **盲区削弱实用性**：α≤0.45不可检测，恰好覆盖了实际web数据中最常见的污染水平
3. **泛化性不足**：Phase diagram仅基于Pythia-410M，跨架构验证限于α=1.0且有4/15失败

主要优点：
1. 方法敏感性发现（FPR从3%到92%）对社区有重要警示
2. 可检测性相图的概念框架有用
3. 实验设计系统性强，附录极为详尽

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1220 · 2026-05-24T15:02:50.859734+00:00_

Reviewer 2 审稿已收到（3.0 Findings）。等待 Reviewer 1 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 117

## Round 117

6 recorded events


### User

_source line 1221 · 2026-05-24T15:05:53.571597+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：Characterizing the Detectability Landscape of Iterative Model Collapse

## 1. Summary

本文研究迭代模型坍缩（iterative model collapse）在不同合成数据污染水平（α）和观测窗口（T）下的统计可检测性。作者使用 Pythia-410M 在 WikiText-103 上，跨 13 个污染水平进行最多 10 代迭代训练，比较了五种时序检测方法（naive cross-correlation、differenced cross-correlation、threshold onset、Permutation Granger causality [PermG]、Toda-Yamamoto），并提出多方法共识测试（MMCT，K≥3 投票）。主要发现包括：(1) 检测在 α≈0.45 处经历尖锐相变（0/8 到 6/8 显著对），(2) canary 指标（entropy）在下游指标（distinct-1）之前响应，形成稳定的级联序，(3) 检测边界近似服从幂律缩放。论文还展示了基于 canary 触发的反应性干预概念验证（α=1.0，N=2 架构）。

## 2. Strengths

**S1. 问题定义新颖且及时。** 将研究问题从"模型坍缩是否发生"转向"何时可被检测到"是一个有价值的视角转换。检测相图（detection phase diagram, Figure 1）的框架创造性地将信号强度（α）与观测长度（T）组合呈现，为该领域提供了可操作的分析模板。

**S2. 多方法比较揭示了方法敏感性。** 五种方法在相同数据上产生 3%–92% 的 FPR 差异（§3.3），这一发现本身就具有重要警示价值。论文诚实报告了这一差异，而非选择性呈现最佳结果。FPR-inverse 加权方案（Appendix Q）和 Shapley 分解（Appendix P）提供了系统的方法比较框架。

**S3. 级联序（cascade ordering）实证稳健。** Entropy 在 14/15 实验中先于 distinct-1 响应（§3.1, §4.2），且有理论支撑——Design Principle 1-2（Appendix X）从 mode amplification 假设推导出 entropy 必然先于 diversity 下降。该发现跨越多个 α 水平和 seed 保持稳健，具有实际监控意义。

**S4. 理论推导提供形式化基础。** Appendix X 中的 Proposition 4（entropy 作为一阶指示器）和 Proposition 5（diversity 作为阈值指示器）从 mode amplification 假设出发，给出了级联序的充分条件。证明逻辑清晰，假设明确。

**S5. 补充材料极为详尽。** 19 页附录涵盖：specification curve 分析（Appendix E, 1,160 specifications）、DGP 功效分析（Appendix N）、Shapley 值分解（Appendix P）、FPR 独立性分析（Appendix R）、cross-architecture 详细结果（Appendix Z）。这种透明度超过了多数同类工作。

**S6. 诚实披露局限。** 论文明确承认 PermG FPR 膨胀、α=0.60 异常未解释、幂律参数不确定性大、canary 干预的初步性质——这种透明度值得肯定。

## 3. Weaknesses

**W1. [Critical] PermG FPR 膨胀严重削弱主检测器可靠性**
- 位置：§3.3（page 4）、Appendix R（page 21）
- 问题：PermG 经验 FPR 为 11.1%（4/36 null-control pairs），超过标称 5% 一倍以上。95% CI [1.2%, 30.4%] 极宽——在此 CI 下，真实 FPR 可能低至 1.2% 也可能高达 30.4%。PermG 是全文的主检测器（Figure 1 相图、§3.4 检测边界、§4.2 级联序均基于 PermG），因此 FPR 膨胀传播到所有核心发现。更关键的是，设计用于缓解此问题的 K≥3 共识（MMCT）反而具有**更高的** FPR（16.7%, 6/36），完全未实现其声称的鲁棒性目标。
- 影响接收原因：一篇以统计检测为核心贡献的论文，其主检测器的 FPR 无法控制在标称水平，这构成方法论缺陷。读者无法确定 Figure 1 中哪些"显著"检测点是真阳性、哪些是膨胀 FPR 的产物。
- 建议：(a) 提供 PermG FPR 在更大 null 样本上的估计（当前仅 36 对），例如通过 DGP 模拟扩大到数百对；(b) 解释为何 K≥3 共识的 FPR（16.7%）高于 standalone PermG（11.1%），并提供共识 FPR 的理论推导；(c) 考虑以 DiffXCorr（FPR=2.8%）为主检测器重做相图，即使失去方向性，至少可以验证相变结构是否依赖于方法选择。

**W2. [Critical] 实验范围过窄，不支撑 "landscape" 声称**
- 位置：标题、§1（page 1）、§4.1（page 5）、§4.5（page 7-8）
- 问题：标题为"Characterizing the Detectability Landscape"，但主实验仅用一个架构（Pythia-410M, 410M 参数）、一个数据集（WikiText-103）、一种污染范式（full replacement）。Cross-architecture 验证（§4.5）仅在 α=1.0 进行——这是坍缩最严重、检测最容易的情况（11/15 组合检测成功），完全未覆盖检测边界区域（α≈0.45–0.75）。Pythia-410M 是一个较小的模型；在更大模型（7B+）上检测边界可能显著不同（坍缩可能更慢或更快）。论文声称的"landscape"实质上是单一配置下的案例研究。
- 影响接收原因：标题和贡献声称的覆盖范围与实际实验证据之间存在显著落差。一个 reviewer 期望 "landscape" 至少覆盖 ≥2 架构在检测边界区域的交叉验证。
- 建议：(a) 至少在 α=0.50 对 2-3 个架构进行交叉验证（当前已有这些模型的 α=1.0 结果，只需补充中间 α）；(b) 或者将标题和声称范围缩小到 "Pythia-410M" 的范围。

**W3. [Major] 幂律边界拟合实质上不提供信息**
- 位置：§3.4（page 5）
- 问题：检测边界模型 o_α(T) = A·T^{-γ} 中，γ 的 95% CI 为 [0.64, 2.08]（page 5）。γ=0.64 意味着边界随 T 缓慢下降（需要很长观测窗口），γ=2.08 意味着边界快速下降（短窗口即可检测）——这是**定性不同**的预测。β 参数在 MLE（0.66）和 CV（0.24）之间分歧巨大。论文承认这是"descriptive rather than mechanistic"，但仍将其作为 §3.4 的核心结果呈现，并在 abstract 中提及"power law scaling"。一个无法区分其两种基本缩放机制的模型，不比直接报告原始检测率提供更多信息。
- 建议：(a) 将幂律拟合降级为探索性观察，而非§3.4的核心结论；(b) 明确报告需要多少额外数据点（更多 T 值）才能使 γ 的 CI 窄到有意义的程度。

**W4. [Major] α=0.60 非单调异常未解释，且被排除出拟合**
- 位置：Figure 1（page 3）、§3.4（page 5）、§5（page 8）
- 问题：在检测边界区域（α=0.45–0.75）的四个 α 值中，α=0.60 表现出非单调异常——检测率相对 α=0.50 下降。该异常被标注为"unexplained"并从幂律拟合中排除（"sine-dip excluded"）。排除一个不利数据点进行拟合，在方法论上是可疑的。论文在 §5 推测可能源于"architectural differences in attention or normalization"但无任何证据支持。
- 建议：(a) 增加 α=0.55 和 α=0.65 的实验以验证异常是否是离散采样伪像；(b) 检查各 seed 在 α=0.60 的个体轨迹，确认异常是跨 seed 一致还是由个别 seed 驱动；(c) 如果保留排除，至少报告包含 α=0.60 时拟合参数的变化。

**W5. [Major] K≥3 共识投票缺乏统计理论支撑**
- 位置：§3.3（page 3-4）、Algorithm 1（Appendix J, page 15）、Appendix R（page 21）
- 问题：五种方法的 FPR 从 3%（DiffXCorr）到 92%（Naive XCor）差异巨大，方法间一致性接近随机（κ=0.185）。在此条件下，K≥3 多数投票的 FPR 取决于高 FPR 方法的投票行为——实际结果证实了这一点（共识 FPR 16.7% > PermG 11.1%）。论文未提供 K 选择的理论依据（为什么不是 K=4 或 K=5？），也未推导给定各方法 FPR 时共识的期望 FPR。Shapley 分解（Appendix P）显示 PermG 主导共识，表明其他方法主要贡献噪声。
- 建议：(a) 推导 K≥3 共识在给定各方法 FPR 条件下的理论 FPR（可假设独立）；(b) 报告 K=4 和 K=5 时的 FPR 和检测力变化；(c) 如果共识主要依赖 PermG，考虑是否应该直接使用 PermG + 一个确认方法（如 DiffXCorr），而非五方法投票。

**W6. [Major] Cross-architecture 验证仅覆盖最易检测的条件**
- 位置：§4.5（page 7-8）、Figure 10（page 29）、Appendix Z（page 27-28）
- 问题：§4.5 在 5 个模型族上验证，但仅在 α=1.0（full replacement）条件下。α=1.0 是坍缩最极端的情况，此时检测几乎是 trivial 的（11/15 组合检测成功）。论文的核心贡献——检测相变和边界——位于 α≈0.45–0.75 区域，但这个区域没有任何 cross-architecture 数据。GPT-2-medium 的 null-control FPR 在 Appendix Z.3（Table 32）中显示比 Pythia-410M 更高，暗示不同架构的检测边界可能显著不同。
- 建议：至少在 α=0.50 对 GPT-2-medium（已有 null-control 数据）和一个 >1B 模型进行验证。

**W7. [Major] 关键 α 值的 seed 数量不足**
- 位置：Table 1（Appendix A, page 10）
- 问题：α=0.10 仅有单个 seed；α=0.25 仅 4 seeds；检测边界区域（α=0.45–0.75）各 3 seeds。对于声称刻画"landscape"的论文，这个采样密度过低。非单调异常（α=0.60）和检测边界的精确位置都受到 seed 采样不确定性的强烈影响。
- 建议：在 α=0.45, 0.50, 0.60 各增加至 ≥5 seeds，以验证相变的尖锐性和异常的稳健性。

**W8. [Minor] Canary 干预的展示超出证据强度**
- 位置：Abstract（page 1）、§4.6（page 8）、Figure 6（page 8）
- 问题：Abstract 称"canary whose triggered cessation substantially reduces peak perplexity"，但 §4.6 仅展示 N=2 架构、α=1.0、post-hoc 阈值选择（15%）。这是一个概念验证，而非稳健发现。CUSUM 对比（Appendix H）标注"not rigorously evaluated"，是一个不完整的贡献。
- 建议：(a) 在 abstract 中将 canary 干预明确标注为"proof-of-concept"；(b) 移除或完成 CUSUM 对比。

**W9. [Minor] Full replacement 范式限制生态效度**
- 位置：§4.1（page 5）
- 问题：论文采用 full replacement 范式（每代用 α 比例合成数据替换）。实际场景中更常见的是累积（accumulation）范式——来自前代的合成数据持续存在。两种范式下的检测 landscape 可能显著不同，但论文未测试也未充分讨论。
- 建议：在 Limitations 中明确讨论 full replacement vs. accumulation 的区别及其对结论泛化性的影响。

## 4. Questions for Authors

**Q1.** K≥3 共识的 FPR（16.7%）高于 standalone PermG（11.1%），这是否意味着高 FPR 方法（Naive XCor, Toda-Yam）的投票在 null 条件下系统性地与 PermG 共现？能否提供各方法在 null 条件下的 pairwise co-rejection 率？

**Q2.** 如果用 DiffXCorr（FPR=2.8%）替代 PermG 重绘 Figure 1 的相图，检测 onset 会移动吗？相变结构（sharp transition at α≈0.45）是否依赖于方法选择？

**Q3.** α=0.60 的非单调异常在各 seed 上是否一致？能否展示 α=0.55, 0.60, 0.65 三个 seed 的个体检测率，以排除离散采样伪像？

**Q4.** First-differencing 消除了 canary→perplexity 的信号（F≈0, p=0.99）。是否检验过 canary→diversity 在控制 generation number 后的偏相关？共享趋势是否也可能解释 canary→diversity 的关联？

**Q5.** 检测边界的幂律拟合仅基于 T=10 的 n=11 个数据点（排除 sine-dip）。如果纳入 T=5, 15, 20, 25 的数据作为额外约束，γ 的 CI 会收窄多少？

**Q6.** Cross-architecture 验证为何不在 α=0.50 进行？如果计算资源受限，GPT-2-medium 在 α=0.50 的单 seed 实验是否可行？

**Q7.** 论文在 Use of AI Assistants（page 28）中披露使用 Claude 进行代码编写和论文写作。AI 辅助写作是否可能影响了对结果不确定性的表述（如将 "poorly identified" 参数仍作为模型呈现）？

## 5. Missing References

未发现关键缺失引用。相关工作覆盖较全面。

次要建议：
- 论文引用了 Guo et al. (2024) 和 Gu et al. (2025) 关于 critical mixture ratios，但未充分讨论其发现与本文检测边界（α≈0.45）的关系——这些工作中的 "critical ratio" 与本文的 "detection onset" 是否对应同一现象？
- Martínez et al. (2023) 关于 multi-method consensus 在因果推断中的应用可能与 MMCT 的理论基础相关。

## 6. Overall Assessment

**Overall: 3.0（Findings）**

本文提出了一个及时且有价值的研究问题——模型坍缩何时可被统计检测？多方法比较框架和级联序发现是实质性贡献。但执行层面存在显著不足：

(1) **统计基础不稳固**：主检测器 PermG 的 FPR 膨胀（11.1% vs 5% 标称），且 CI 极宽（[1.2%, 30.4%]），使得核心发现（相图、检测边界）的可靠性存疑。共识方法（MMCT）的 FPR（16.7%）更高而非更低，未能实现其设计目标。

(2) **覆盖范围与声称不匹配**：标题声称"landscape"，但仅有单架构（410M）+ 单数据集 + 有限 seed 的支持，cross-architecture 验证仅在 trivial 条件（α=1.0）进行。

(3) **幂律边界参数不确定性过大**：γ ∈ [0.64, 2.08] 无法区分定性不同的缩放行为，使该模型的实际指导价值有限。

(4) **核心异常未解释**：α=0.60 的非单调行为被排除出拟合，而非被解释——这在检测边界区域（仅 4 个 α 值）中尤为突出。

框架思路和部分发现（方法敏感性、级联序）达到 Findings 水准，但统计问题和覆盖范围限制使其难以被主会议接收。

## 7. 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | PermG FPR 膨胀（11.1% vs 5%）+ CI 极宽；共识 FPR 更高（16.7%）；幂律 γ CI [0.64, 2.08] 跨越定性不同区域；α=0.60 异常排除出拟合。主要 claims 的统计支撑存在系统性问题。 |
| Excitement | 3/5 | 问题及时，框架有创意（检测相图、级联序），但结果受限于单架构和统计问题，实际贡献低于预期。 |
| Reproducibility | 4/5 | 实验细节充分（Appendix A 超参数、seed 列表），但代码未开源（匿名期合理），DGP 模拟细节完备。 |
| Overall Assessment | 3.0/5 (Findings) | 有价值的框架和部分稳健发现，但统计方法论问题和实验覆盖范围限制了置信度。 |
| Confidence | 4/5 | 熟悉统计时序方法（Granger causality、permutation testing、FDR correction）和 model collapse 文献。通读了全文含所有 appendix。 |

## 8. 主要优势（总结）

- 问题定义新颖：从"是否坍缩"转向"何时可检测"
- 多方法 FPR 差异（3%–92%）是对该领域的重要警示
- 级联序（entropy→diversity）实证稳健且有理论支撑
- 补充材料极为详尽（19 页 appendix，含 specification curve、Shapley 分解、DGP 分析）
- 对自身局限的诚实披露

Sources:
- [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines)
- [ARR Review Form](https://aclrollingreview.org/reviewform)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1222 · 2026-05-24T15:06:47.298765+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见\n\n## 总体评分：3.0 (Findings)\n\n## Strengths\n\n**S1.** 方法敏感性分析是本文最有价值的发现。五种方法应用于同一数据，null-control FPR从3%（PermG）到92%（NaiveXCor），这个发现对社区有重要警示意义。\n\n**S2.** 实验设计系统性强。13个污染级别 × 多seed × 5种方法 × T∈{5,10,15,20,25} × 跨架构验证，覆盖面在该领域罕见。\n\n**S3.** \"可检测性相图\"（Figure 1）的概念贡献。将问题从\"能否检测collapse\"转化为\"在什么(α, T)条件下检测成为可能\"，这一reframing为后续工作提供了有用的分析框架。\n\n**S4.** 附录极为详尽（~20页），包含规范曲线分析、Shapley分解、非平稳性鲁棒性分析、CUSUM对比、互信息分析等。\n\n**S5.** Entropy → diversity 的 cascade ordering（Design Principle 1-2）有形式化推导，从 mode amplification 假设出发给出了有理论支撑的解释。\n\n## Weaknesses\n\n**W1. [Major] 方法论新颖性不足——所有核心方法均为成熟工具的直接迁移。**\n- Granger causality、置换检验、first-differencing、CUSUM、Toda-Yamamoto均为计量经济学/统计过程控制的标准工具\n- 本文的贡献是应用和系统比较，而非方法论创新\n- \"Detectability landscape\"本质上是检测功效随效应量和样本量变化的二维映射——在统计假设检验理论中是基本概念\n\n**W2. [Major] 盲区（α≤0.45, T≤10）覆盖了实践中最相关的污染场景，严重削弱实用价值。**\n- web-scraped数据的合成内容比例通常在10%–40%范围，恰好落在盲区内\n- §5 Discussion 未充分讨论对实用性的影响，也未提供缓解方案\n\n**W3. [Major] Phase diagram 的泛化性未充分验证。**\n- 跨架构验证仅在α=1.0进行，4/15 non-confirming\n- GPT-2-medium null-control FPR显著高于Pythia-410M（100% vs. 11.1%）\n\n**W4. [Minor-Major] Canary intervention（§4.6）作为实用贡献严重不足。**\n- 仅N=2 seeds、α=1.0单一条件\n- 干预策略是最粗暴的二元干预，实际中不可能直接停止训练\n\n**W5. [Minor-Major] Design Principle 1可能过于直观。**\n- entropy连续性vs. diversity离散性决定了前者灵敏度必然更高\n- 结论近乎trivial：\"连续指标比离散指标更早响应微小变化\"\n\n**W6. [Minor] Related Work 遗漏：Dakos et al. (2008, 2012), Lenton et al. (2008), Guo et al. (2025)。**\n\n**W7. [Minor] 正文数字密度过高，影响可读性。**\n\n**W8. [Minor] 术语一致性：\"Granger causality\" vs \"Granger-precedence\" vs \"temporal predictive improvement\"交替使用。**\n\n## Questions\n\nQ1. Phase diagram检测边界对其他架构是否成立？\nQ2. 实际web-scale数据中合成污染比例通常是多少？盲区是否覆盖了最常见场景？\nQ3. 为什么不与SIGMA（Gu et al., 2026）进行直接实验对比？\nQ4. SmolLM3-3B的非单调异常是否暗示三区域划分可能不是普适的？\nQ5. Design Principle 1与信息论标准结果有何本质区别？\n\n## Missing References\n- Dakos et al. (2008, 2012), Lenton et al. (2008), Guo et al. (2025)\n- 建议讨论Shojaie &amp; Fox 2022 §4的局限性\n\n---\n\n请逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见\n\n## 总体评分：3.0 (Findings)\n\n## Strengths\n\n**S1.** 方法敏感性分析是本文最有价值的发现。五种方法应用于同一数据，null-control FPR从3%（PermG）到92%（NaiveXCor），这个发现对社区有重要警示意义。\n\n**S2.** 实验设计系统性强。13个污染级别 × 多seed × 5种方法 × T∈{5,10,15,20,25} × 跨架构验证，覆盖面在该领域罕见。\n\n**S3.** \"可检测性相图\"（Figure 1）的概念贡献。将问题从\"能否检测collapse\"转化为\"在什么(α, T)条件下检测成为可能\"，这一reframing为后续工作提供了有用的分析框架。\n\n**S4.** 附录极为详尽（~20页），包含规范曲线分析、Shapley分解、非平稳性鲁棒性分析、CUSUM对比、互信息分析等。\n\n**S5.** Entropy → diversity 的 cascade ordering（Design Principle 1-2）有形式化推导，从 mode amplification 假设出发给出了有理论支撑的解释。\n\n## Weaknesses\n\n**W1. [Major] 方法论新颖性不足——所有核心方法均为成熟工具的直接迁移。**\n- Granger causality、置换检验、first-differencing、CUSUM、Toda-Yamamoto均为计量经济学/统计过程控制的标准工具\n- 本文的贡献是应用和系统比较，而非方法论创新\n- \"Detectability landscape\"本质上是检测功效随效应量和样本量变化的二维映射——在统计假设检验理论中是基本概念\n\n**W2. [Major] 盲区（α≤0.45, T≤10）覆盖了实践中最相关的污染场景，严重削弱实用价值。**\n- web-scraped数据的合成内容比例通常在10%–40%范围，恰好落在盲区内\n- §5 Discussion 未充分讨论对实用性的影响，也未提供缓解方案\n\n**W3. [Major] Phase diagram 的泛化性未充分验证。**\n- 跨架构验证仅在α=1.0进行，4/15 non-confirming\n- GPT-2-medium null-control FPR显著高于Pythia-410M（100% vs. 11.1%）\n\n**W4. [Minor-Major] Canary intervention（§4.6）作为实用贡献严重不足。**\n- 仅N=2 seeds、α=1.0单一条件\n- 干预策略是最粗暴的二元干预，实际中不可能直接停止训练\n\n**W5. [Minor-Major] Design Principle 1可能过于直观。**\n- entropy连续性vs. diversity离散性决定了前者灵敏度必然更高\n- 结论近乎trivial：\"连续指标比离散指标更早响应微小变化\"\n\n**W6. [Minor] Related Work 遗漏：Dakos et al. (2008, 2012), Lenton et al. (2008), Guo et al. (2025)。**\n\n**W7. [Minor] 正文数字密度过高，影响可读性。**\n\n**W8. [Minor] 术语一致性：\"Granger causality\" vs \"Granger-precedence\" vs \"temporal predictive improvement\"交替使用。**\n\n## Questions\n\nQ1. Phase diagram检测边界对其他架构是否成立？\nQ2. 实际web-scale数据中合成污染比例通常是多少？盲区是否覆盖了最常见场景？\nQ3. 为什么不与SIGMA（Gu et al., 2026）进行直接实验对比？\nQ4. SmolLM3-3B的非单调异常是否暗示三区域划分可能不是普适的？\nQ5. Design Principle 1与信息论标准结果有何本质区别？\n\n## Missing References\n- Dakos et al. (2008, 2012), Lenton et al. (2008), Guo et al. (2025)\n- 建议讨论Shojaie &amp; Fox 2022 §4的局限性\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 1223 · 2026-05-24T15:07:14.846962+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27548
}
```

</details>

---


### Tool call

_source line 1224 · 2026-05-24T15:07:14.999518+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见\n\n## 总体评分：3.0 (Findings)\n\n## Strengths\n\n**S1.** 问题定义新颖且及时。将研究问题从\"模型坍缩是否发生\"转向\"何时可被检测到\"是一个有价值的视角转换。\n\n**S2.** 多方法比较揭示了方法敏感性。五种方法在相同数据上产生 3%–92% 的 FPR 差异，论文诚实报告了这一差异。\n\n**S3.** 级联序（cascade ordering）实证稳健。Entropy 在 14/15 实验中先于 distinct-1 响应，且有理论支撑。\n\n**S4.** 理论推导提供形式化基础。Appendix X 中的 Proposition 4-5 从 mode amplification 假设出发给出了级联序的充分条件。\n\n**S5.** 补充材料极为详尽。19页附录涵盖specification curve、DGP功效分析、Shapley值分解、FPR独立性分析等。\n\n**S6.** 诚实披露局限。论文明确承认PermG FPR膨胀、α=0.60异常未解释、幂律参数不确定性大。\n\n## Weaknesses\n\n**W1. [Critical] PermG FPR 膨胀严重削弱主检测器可靠性**\n- PermG经验FPR为11.1%（4/36 null-control pairs），超过标称5%一倍以上\n- 95% CI [1.2%, 30.4%] 极宽\n- K≥3 共识MMCT的FPR（16.7%）反而更高\n- 读者无法确定Figure 1中哪些\"显著\"检测点是真阳性\n- 建议：扩大null样本、推导共识FPR理论值、用DiffXCorr重做相图\n\n**W2. [Critical] 实验范围过窄，不支撑 \"landscape\" 声称**\n- 仅Pythia-410M + WikiText-103 + full replacement\n- Cross-architecture验证仅在α=1.0（最trivial条件）\n- 标题声称的覆盖范围与实际实验证据存在显著落差\n\n**W3. [Major] 幂律边界拟合不提供信息**\n- γ的95% CI为[0.64, 2.08]，跨越定性不同的缩放行为\n- β参数MLE（0.66）和CV（0.24）严重分歧\n- 一个无法区分基本缩放机制的模型不比直接报告原始检测率更有信息\n\n**W4. [Major] α=0.60非单调异常未解释且被排除出拟合**\n- 在检测边界区域的四个α值中排除一个不利数据点进行拟合\n- 建议增加α=0.55和α=0.65的实验\n\n**W5. [Major] K≥3共识投票缺乏统计理论支撑**\n- κ=0.185（方法间几乎无agreement）\n- 共识FPR 16.7% > PermG 11.1%\n- 未提供K选择的理论依据\n\n**W6. [Major] Cross-architecture验证仅覆盖最易检测条件**\n- 仅α=1.0，核心贡献所在的α≈0.45–0.75区域无任何cross-architecture数据\n\n**W7. [Major] 关键α值的seed数量不足**\n- α=0.10仅单seed；检测边界区域各3 seeds\n- 建议α=0.45, 0.50, 0.60各增加至≥5 seeds\n\n**W8. [Minor] Canary干预展示超出证据强度**\n- Abstract称\"substantially reduces\"但仅N=2、α=1.0、post-hoc threshold\n\n**W9. [Minor] Full replacement范式限制生态效度**\n- 实际场景中数据累积更常见\n\n## Questions\n\nQ1. K≥3共识FPR高于standalone PermG，是否说明高FPR方法在null条件下与PermG共现？\nQ2. 用DiffXCorr替代PermG重绘Figure 1，相变结构是否依赖方法选择？\nQ3. α=0.60异常在各seed上是否一致？\nQ4. canary→diversity在控制generation number后的偏相关如何？\nQ5. 纳入T=5,15,20,25数据后γ的CI会收窄多少？\nQ6. Cross-architecture验证为何不在α=0.50进行？\nQ7. AI辅助写作是否影响了对结果不确定性的表述？\n\n## Missing References\n- 未发现关键缺失引用（次要建议：与Gu et al. (2024/2025) critical ratio的关系、Martínez et al. (2023) multi-method consensus）\n\n---\n\n请逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见\n\n## 总体评分：3.0 (Findings)\n\n## Strengths\n\n**S1.** 问题定义新颖且及时。将研究问题从\"模型坍缩是否发生\"转向\"何时可被检测到\"是一个有价值的视角转换。\n\n**S2.** 多方法比较揭示了方法敏感性。五种方法在相同数据上产生 3%–92% 的 FPR 差异，论文诚实报告了这一差异。\n\n**S3.** 级联序（cascade ordering）实证稳健。Entropy 在 14/15 实验中先于 distinct-1 响应，且有理论支撑。\n\n**S4.** 理论推导提供形式化基础。Appendix X 中的 Proposition 4-5 从 mode amplification 假设出发给出了级联序的充分条件。\n\n**S5.** 补充材料极为详尽。19页附录涵盖specification curve、DGP功效分析、Shapley值分解、FPR独立性分析等。\n\n**S6.** 诚实披露局限。论文明确承认PermG FPR膨胀、α=0.60异常未解释、幂律参数不确定性大。\n\n## Weaknesses\n\n**W1. [Critical] PermG FPR 膨胀严重削弱主检测器可靠性**\n- PermG经验FPR为11.1%（4/36 null-control pairs），超过标称5%一倍以上\n- 95% CI [1.2%, 30.4%] 极宽\n- K≥3 共识MMCT的FPR（16.7%）反而更高\n- 读者无法确定Figure 1中哪些\"显著\"检测点是真阳性\n- 建议：扩大null样本、推导共识FPR理论值、用DiffXCorr重做相图\n\n**W2. [Critical] 实验范围过窄，不支撑 \"landscape\" 声称**\n- 仅Pythia-410M + WikiText-103 + full replacement\n- Cross-architecture验证仅在α=1.0（最trivial条件）\n- 标题声称的覆盖范围与实际实验证据存在显著落差\n\n**W3. [Major] 幂律边界拟合不提供信息**\n- γ的95% CI为[0.64, 2.08]，跨越定性不同的缩放行为\n- β参数MLE（0.66）和CV（0.24）严重分歧\n- 一个无法区分基本缩放机制的模型不比直接报告原始检测率更有信息\n\n**W4. [Major] α=0.60非单调异常未解释且被排除出拟合**\n- 在检测边界区域的四个α值中排除一个不利数据点进行拟合\n- 建议增加α=0.55和α=0.65的实验\n\n**W5. [Major] K≥3共识投票缺乏统计理论支撑**\n- κ=0.185（方法间几乎无agreement）\n- 共识FPR 16.7% > PermG 11.1%\n- 未提供K选择的理论依据\n\n**W6. [Major] Cross-architecture验证仅覆盖最易检测条件**\n- 仅α=1.0，核心贡献所在的α≈0.45–0.75区域无任何cross-architecture数据\n\n**W7. [Major] 关键α值的seed数量不足**\n- α=0.10仅单seed；检测边界区域各3 seeds\n- 建议α=0.45, 0.50, 0.60各增加至≥5 seeds\n\n**W8. [Minor] Canary干预展示超出证据强度**\n- Abstract称\"substantially reduces\"但仅N=2、α=1.0、post-hoc threshold\n\n**W9. [Minor] Full replacement范式限制生态效度**\n- 实际场景中数据累积更常见\n\n## Questions\n\nQ1. K≥3共识FPR高于standalone PermG，是否说明高FPR方法在null条件下与PermG共现？\nQ2. 用DiffXCorr替代PermG重绘Figure 1，相变结构是否依赖方法选择？\nQ3. α=0.60异常在各seed上是否一致？\nQ4. canary→diversity在控制generation number后的偏相关如何？\nQ5. 纳入T=5,15,20,25数据后γ的CI会收窄多少？\nQ6. Cross-architecture验证为何不在α=0.50进行？\nQ7. AI辅助写作是否影响了对结果不确定性的表述？\n\n## Missing References\n- 未发现关键缺失引用（次要建议：与Gu et al. (2024/2025) critical ratio的关系、Martínez et al. (2023) multi-method consensus）\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 1225 · 2026-05-24T15:07:16.367272+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1367
}
```

</details>

---


### Assistant

_source line 1226 · 2026-05-24T15:07:20.171583+00:00_

交叉分享已派发，等待两位 Reviewer 的 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 118

## Round 118

2 recorded events


### User

_source line 1227 · 2026-05-24T15:07:22.682574+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：我对本文评分为 **Overall 3.0（Findings）**，Soundness 2.5/5，Excitement 3/5。

核心问题：
1. **[Critical]** PermG 主检测器 FPR 膨胀至 11.1%（标称 5%），CI 极宽 [1.2%, 30.4%]；K≥3 共识的 FPR 更高（16.7%），未实现鲁棒性目标
2. **[Critical]** 标题声称"landscape"，但仅有单架构 + 单数据集 + cross-architecture 仅在 trivial 条件（α=1.0）验证
3. **[Major]** 幂律边界 γ ∈ [0.64, 2.08]，无法区分定性不同的缩放行为
4. **[Major]** α=0.60 非单调异常未解释且被排除出拟合
5. **[Major]** K≥3 投票缺乏理论推导，κ=0.185 近乎随机

主要优势在于问题新颖、多方法 FPR 差异的警示价值、级联序的实证稳健性和理论推导，以及极为详尽的附录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1228 · 2026-05-24T15:07:38.304459+00:00_

交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 119

## Round 119

2 recorded events


### User

_source line 1229 · 2026-05-24T15:09:09.633251+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Strengths 回应

**[AGREE] R2-S1（方法敏感性分析）：** 完全同意。这也是我审稿中的 S2。五种方法在同一数据上产生 3%–92% 的 FPR 差异（§3.3, page 4），这一发现本身就具有独立的警示价值，无论论文其他部分的问题如何。

**[AGREE] R2-S2（实验设计系统性）：** 同意覆盖面的广度。但我要补充：虽然 13 个 α 水平 × 多 T 值 × 多 seed 的设计看起来系统，但在关键区域（检测边界 α≈0.45–0.75）每个 α 仅 3 seeds（Table 1, Appendix A, page 10），α=0.10 仅单 seed，实际密度不如表面看起来那样充分。

**[AGREE] R2-S3（可检测性相图概念）：** 完全同意。这一 reframing 是论文最核心的概念贡献，我在 S1 中也强调了这一点。Figure 1 的呈现方式清晰有效。

**[AGREE] R2-S4（附录详尽）：** 同意。我在 S5 中也注意到 19 页附录的透明度超过多数同类工作。特别是 specification curve 分析（Appendix E, 1,160 specifications）和 Shapley 分解（Appendix P）是少见的严谨性检查。

**[AGREE] R2-S5（级联序理论推导）：** 同意。Design Principle 1-2（Appendix X）的推导逻辑清晰，从 mode amplification 假设出发给出了充分条件。但请见我对 W5 的回应——我对 R2 关于其"过于直观"的批评有不同看法。

---

## Weaknesses 回应

**[REBUT] R2-W1（方法论新颖性不足）：**

R2 认为所有核心方法（Granger causality、置换检验、CUSUM 等）均为标准工具的直接迁移，本文缺乏方法论创新。

我认为这一批评部分有道理但整体偏严苛，理由如下：

1. **本文的贡献定位是实证系统研究（empirical systems paper），而非方法论创新论文。** 论文 §1（page 2）明确将贡献定义为 "map the detectability landscape"、"document method sensitivity"、"formalize cascade ordering"——这三条均为实证/框架贡献，未声称方法论新颖性。以"方法论不新"批评一篇实证系统论文，存在评价维度错位。

2. **"检测功效随效应量和样本量变化的二维映射"确实是统计基本概念，但将其系统应用于 iterative model collapse 领域是新的。** 该领域此前的工作（Shumailov et al., 2024; Dohmatob et al., 2024）关注的是"collapse 是否发生"而非"何时可被检测"。问题的 reframing 本身是贡献。

3. **MMCT（Algorithm 1, Appendix J）虽然每个组件是标准的，但其组合方式（FPR-inverse 加权 + K≥3 共识 + PermG 方向选择）是针对 model collapse 时序特征设计的。** 这类似于 NLP 中将 attention mechanism 应用于新任务——组件不新但组合有针对性。

但我也同意 R2 的隐含关切：**论文不应将 MMCT 框架的呈现方式暗示为方法论创新**。当前 Algorithm 1 的呈现确实有过度强调之嫌——如果仅作为实验工具介绍而非作为"算法贡献"呈现，这个批评就不成立了。

**[AGREE] R2-W2（盲区覆盖实践最相关场景）：**

这是一个我在审稿中未充分强调的重要观点。完全同意。

论文的检测 onset 在 α≈0.45（§3.4, page 5, Figure 1），意味着 α<0.45 的污染不可检测。但如 R2 所指出，web-scraped 数据的合成内容比例通常在 10%–40% 范围（引用：Shumailov et al., 2024 估计; Schaeffer et al., 2025 关于 "Model collapse does not mean what you think" 的讨论）。这意味着**论文的方法在最需要检测的场景中恰好无法工作**。

§5 Discussion（page 8）仅简略提及 "evaluation at >7B parameters remains open" 和 "data accumulation"，但未正面讨论低 α 盲区的实用性影响。这是一个重要遗漏。我认为这构成一个 Major weakness，应补充到论文的 Limitations 中。

**[AGREE] R2-W3（Phase diagram 泛化性未充分验证）：**

完全同意，这与我的 W2（Critical）和 W6（Major）高度重叠。

补充一个 R2 提到但我在审稿中未充分展开的数据点：**GPT-2-medium 的 null-control FPR 为 100%**（Appendix Z.3, Table 32, page 27：pooled PermG fwd = 0/12 (50%)，6-pair basis）——等等，让我更仔细地回忆。R2 说 "GPT-2-medium null-control FPR显著高于Pythia-410M（100% vs. 11.1%）"。

查看论文 page 27, Table 32：GPT-2-medium null-control FPR 在 6-pair basis 下 pooled 0/12 (50%)，两个 seed 分别为 0/6 (100%) 和 0/6 (0%)。seed s42 的 FPR 是 0/6 = 0%... 实际上这里的数字需要更仔细解读。但 R2 的核心论点成立：不同架构的 null-control FPR 差异巨大，单一架构的检测边界不可泛化。

**[AGREE] R2-W4（Canary intervention 作为实用贡献不足）：**

同意，这与我的 W8 一致。R2 补充了一个我未提到的好观点：**实际中不可能直接停止训练**（"最粗暴的二元干预"）。论文的干预策略是"当 canary 超过阈值时切换到纯真实数据"——这在生产环境中的可行性值得质疑。一个更实际的干预可能是逐步降低合成数据比例，但这未被探索。

**[REBUT] R2-W5（Design Principle 1 过于直观）：**

R2 认为"连续指标比离散指标更早响应微小变化"近乎 trivial。我不完全同意：

1. **Design Principle 1 的贡献不仅是"entropy 比 diversity 更灵敏"，而是给出了具体的充分条件。** Proposition 4（Appendix X, page 24）证明了在 mode amplification 下，entropy 是 perturbation 的一阶指示器（ΔH(p+δ) ≈ -Σ δ_i log p_i + ...），而 Proposition 5 证明 diversity 是阈值指示器——只有当 perturbation 使某个 token 的概率越过阈值 ε 时才会改变。这不是"连续 vs 离散"的 trivial 区别，而是关于 **mode amplification 动力学下信息传播顺序**的特定结论。

2. **实证上，级联序并非总是成立**——14/15 实验支持但有 1/15 例外（α=0.60，§3.1, page 3）。如果结论真是 trivial，就不应有例外。例外的存在说明实际动力学比"连续 > 离散"的直觉更复杂。

3. **但我同意 R2 的部分关切**：论文在 §3.1 对 Design Principle 的呈现确实可以更清楚地区分"形式化一个直觉"和"发现一个非显然结论"。当前呈现有时给人"将显然之事形式化"的印象。

**[AGREE] R2-W6（Related Work 遗漏）：**

同意 Dakos et al. (2008, 2012) 和 Lenton et al. (2008) 的遗漏是一个有意义的缺失。这些工作来自生态学/气候科学的 "early warning signals for critical transitions" 文献，与论文的检测相变（phase transition）框架高度相关。特别是 Dakos et al. (2008) 关于 critical slowing down 作为 tipping point 前兆的工作，与论文的 canary → 检测 cascade 有直接概念联系。

Guo et al. (2025) 关于 cross-scale model behavior 的工作如果确实存在且相关，也应被引用。但我注意到论文已引用了 Guo et al. (2024) 关于 critical mixture ratios 的工作（page 5, §3.4 附近）。R2 可能指的是更新版本或不同工作？需要确认。

**[AGREE] R2-W7（正文数字密度过高）：**

部分同意。论文正文（8 页）中确实包含大量精确数字，例如 §3.3（page 4）密集引用 FPR 百分比、CI 区间、p 值。这影响了叙述流畅性。但我认为这是 minor issue——对于一篇统计方法论取向的论文，精确数字比模糊描述更好。建议将部分 FPR 对比表移入附录即可。

**[REBUT] R2-W8（术语不一致）：**

部分不同意。论文在 §3.2（page 4）明确解释了术语选择："PermG tests temporal precedence, not causation"——刻意使用 "Granger precedence" 而非 "Granger causality" 以避免过度因果声称。"temporal predictive improvement" 则是对 Granger 框架的操作性描述。这种区分是有意的、合理的。

但我同意首次出现时应更清晰地定义这三个术语的层级关系（"Granger causality" 作为方法名，"Granger precedence" 作为我们的操作解释，"temporal predictive improvement" 作为检测到的效应），当前确实在首次使用时缺少明确的术语层级说明。

---

## Questions 回应

**[AGREE] R2-Q1（Phase diagram 边界对其他架构是否成立）：**
这是核心问题，与我的 W2 和 W6 一致。我在审稿中明确要求了 α=0.50 的 cross-architecture 验证（我的 Q4、Q6）。没有这一数据，"landscape" 的泛化声称无法成立。

**[AGREE] R2-Q2（实际 web-scale 合成污染比例）：**
重要的实用性问题。如上述对 W2 的回应所述，如果常见污染比例在 10%–40%，恰好落在论文的检测盲区。作者应在 Discussion 或 Limitations 中正面回应这一问题。

**[REBUT] R2-Q3（为什么不与 SIGMA 直接实验对比）：**
我认为这一要求可能超出论文的合理范围。SIGMA（Gu et al., 2025/2026）是一种 *缓解策略*（mitigation strategy），而本文关注的是 *可检测性*（detectability）。两者的研究问题不同：SIGMA 问"如何防止 collapse"，本文问"何时能检测到 collapse 正在发生"。要求直接实验对比需要将两篇论文的实验框架统一，这可能超出了一轮修订的合理工作量。

但论文**确实应该在 Related Work 中更明确地讨论** SIGMA 与检测的关系——如果 SIGMA 的 dynamic censoring 成功缓解了 collapse，那么本文的检测框架与 SIGMA 是互补的（先检测，再缓解），这个讨论目前缺失。

**[AGREE] R2-Q4（SmolLM3-3B 非单调异常）：**
这与我的 W4（α=0.60 异常）相关。如果不同架构在不同 α 值出现非单调行为，三区域划分（blind / onset / detection）可能不是普适的——而是架构/数据依赖的。这进一步支持了我和 R2 共同的关切：单架构结论不可泛化。

**[REBUT] R2-Q5（Design Principle 1 vs 信息论标准结果）：**
如我对 W5 的回应所述，Design Principle 1 的贡献不仅是"连续指标更灵敏"这一信息论常识，而是在 mode amplification 的特定动力学假设下推导出的序关系。信息论中 entropy 对分布扰动的灵敏度（一阶导数 ≠ 0）确实是已知的，但 Proposition 4-5 的贡献在于：(a) 建立了 entropy 和 diversity 在 mode amplification 下的**特定响应顺序**，(b) 给出了 diversity 变化所需的**阈值条件**（token 概率越过 ε），这不是通用信息论能直接给出的。

不过，我认为作者如果在论文中明确讨论与信息论已有结果的关系（"我们的结果在 mode amplification 假设下特化了以下已知性质..."），会使贡献更清晰。

---

## Missing References 回应

**[AGREE]** Dakos et al. (2008, 2012) 和 Lenton et al. (2008) 是 early warning signals / critical transitions 文献的开创性工作，与本文的检测相变框架直接相关，应在 Related Work 中引用和讨论。

关于 Shojaie & Fox (2022) §4 的局限性——论文已引用该工作（page 4, §3.2; page 6），但确实未讨论其 §4 关于 bivariate Granger tests 在高维系统中局限性的警告。鉴于本文的 canary-downstream 系统实质是高维的（4 canary × 4 downstream metrics），这一讨论确有必要。

---

## 总体评估对比

R2 给出 Overall 3.0（Findings），与我的评分一致。

在具体维度上，R2 更强调方法论新颖性不足（W1）和实用性盲区（W2），我更强调统计方法论问题（PermG FPR 膨胀、K≥3 共识 FPR）和实验覆盖范围。两者互补。

我认为 R2 的 W1（方法论新颖性不足）值得讨论但不应是核心扣分点——该论文定位为 empirical systems paper。R2 的 W2（盲区覆盖实践场景）是我审稿中的一个重要遗漏，我认同其 Major 严重性。

综合两份审稿，我维持 **Overall 3.0（Findings）** 的评分不变。两份审稿共同指向的核心问题是：(1) 统计可靠性（PermG FPR），(2) 泛化性不足（单架构 + trivial cross-validation），(3) 实用性受限（检测盲区覆盖常见污染场景）。这三个问题中任意一个单独都不致命，但组合起来使论文难以达到主会议标准。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1230 · 2026-05-24T15:09:17.967817+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 120

## Round 120

10 recorded events


### User

_source line 1231 · 2026-05-24T15:09:22.169942+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 审稿意见的逐条回应。

核心立场：
- **8 条 [AGREE]**（S1-S5, W2-W4, W6-W7, Q1-Q2, Q4）——与 R2 在泛化性不足、实用性盲区、canary intervention 初步性等方面高度一致
- **4 条 [REBUT]**（W1 方法论新颖性、W5 Design Principle trivial、W8 术语不一致、Q3 SIGMA 对比要求）——论文定位是 empirical systems paper 而非方法论创新；Design Principle 的贡献在于特定动力学假设下的序关系推导，非简单"连续>离散"
- **维持 Overall 3.0（Findings）** 不变，两份审稿互补地指向统计可靠性 + 泛化性 + 实用性三重限制

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1232 · 2026-05-24T15:10:11.511978+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1233 · 2026-05-24T15:10:11.562642+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1234 · 2026-05-24T15:10:16.531686+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1235 · 2026-05-24T15:10:16.634676+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1236 · 2026-05-24T15:10:28.939888+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1237 · 2026-05-24T15:10:29.040787+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1238 · 2026-05-24T15:10:29.041128+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1239 · 2026-05-24T15:10:29.091759+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T14:55:24.112790+00:00\", \"completed_at\": \"2026-05-24T14:59:16.030909+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 5-6\", \"message\": \"主文连续两页纯文本（§4.1 Experimental Setup 至 §4.4 Detection Boundary Left-Shift），无 figure/table/equation 穿插。此处正是实验结果讨论区域，审稿人期望看到数据可视化。Figure 3-5 全部堆在第 7 页，建议将至少一个 figure 前移至第 5 或第 6 页以改善视觉节奏。\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"三个 figure（Figure 3、4、5）集中在同一页，每个图尺寸偏小（约占 1/3 栏宽 × 1/4 页高）。图内 axis label 和 legend 文字约 6-7pt，低于正文字号 70% 的可读性阈值。打印后可能难以辨认具体数值。\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"主文前两页无任何 display item（纯 title/abstract/intro/related work）。Figure 1 直到第 3 页才出现。虽非硬性要求，但审稿人打开 PDF 的前 2 分钟只看到文字，缺少视觉锚点建立第一印象。考虑在第 1 页底部或第 2 页加入 teaser figure。\"}, {\"severity\": \"info\", \"dimension\": \"page 1-8\", \"message\": \"主文 8 页中有 6 个 figure、0 个 table。所有定量结果表格均在 appendix。作为实证为主的论文，在主文中加入至少一个核心结果 summary table（如 MMCT 各方法 FPR 对比）能增强说服力，减少审稿人翻 appendix 的负担。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2 框架图中各方法框内的 FPR 数字（如 \\\"FPR ≈ 88%\\\"、\\\"FPR ≈ 2%\\\"）字号偏小，打印尺寸下可能模糊。建议适当放大框内文字或简化信息。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 热力图中的分数标注（\\\"0/8\\\"、\\\"5/8\\\" 等）和 diamond/star marker 偏小，但在 150dpi 渲染下仍可辨认。打印时建议确认清晰度。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"主文最后一页（第 8 页）内容充实：Figure 6 + §5 Discussion and Conclusion + Limitations 开头。页面利用率 >90%，良好。\"}, {\"severity\": \"info\", \"dimension\": \"page 29\", \"message\": \"末页（appendix 最后）Figure 10 + Figure 11 占据约 2/3 页面，底部约 1/3 空白。可接受（appendix 末页）。\"}, {\"severity\": \"info\", \"dimension\": \"page 9-10\", \"message\": \"参考文献格式统一，未发现 [?] 未解析引用或跳号。排版正常。\"}, {\"severity\": \"info\", \"dimension\": \"page 10-28\", \"message\": \"Appendix 表格均使用 booktabs 风格（无竖线），小数精度基本一致。部分表格有加粗最优值标注，但非所有表格都一致（如 Table 1、Table 2 无加粗标注）
…[truncated 369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1240 · 2026-05-24T15:10:57.402374+00:00_

Reviewer 1 交叉回应已收录。关键分歧点记录：

**R1 对 R2 的 4 条 REBUT：**
- W1：论文是 empirical systems paper，非方法论创新
- W5：Design Principle 贡献在序关系推导，非 trivial 观察
- W8：术语一致性问题
- Q3：SIGMA 对比的必要性

**并行任务状态：**
- 视觉审查：✅ 已完成（3 warning + 9 info，无 critical）
- 外部审稿：未请求

等待 Reviewer 2 对 Reviewer 1 审稿意见的交叉回应，收到后评估收敛性并合成最终报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 121

## Round 121

18 recorded events


### User

_source line 1241 · 2026-05-24T15:10:57.408618+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

## Strengths

**[AGREE] R1-S1**: 问题定义确实有价值。"何时可被检测到"比"是否发生"更有实用意义。但我在自己的审稿中指出（R2-W1），这一framing本质上是统计检验功效分析（power analysis）在新领域的应用，概念新颖性不应被高估。

**[AGREE] R1-S2**: 方法敏感性是本文最强贡献，我在 R2-S1 中同样将其列为首要优点。3%→92%的FPR跨度（§3.3, Table 1）是一个对社区有实质性警示价值的发现。

**[AGREE] R1-S3**: 14/15实验中的级联序一致性（§4.3, Appendix W）确实稳健。但我在 R2-W5 中补充了一个保留意见：entropy（连续统计量）先于distinct n-gram count（离散统计量）响应，在信息论层面可能是较为直观的结果。

**[AGREE] R1-S4**: Propositions 4-5 的形式化推导（Appendix X）增加了严谨性。但其核心假设——Assumption 3 (mode amplification)——较强，且结论的实质近似于"连续指标比离散指标对微小偏移更敏感"。

**[AGREE] R1-S5**: 附录的详尽程度在该领域确实罕见。Specification curve（Appendix E）、Shapley分解（Appendix P）、非平稳性鲁棒性（Appendix O）等分析展现了超出一般投稿水平的实证严谨性。

**[AGREE] R1-S6**: 诚实披露局限是学术诚信的体现。PermG FPR膨胀、α=0.60异常均在正文明确提及。

---

## Weaknesses

**[AGREE] R1-W1 (Critical): PermG FPR 膨胀**
同意这是一个严重问题。补充两点：

(1) R1 建议"用 DiffXCorr 重做相图"需要注意一个技术限制：论文§3.3（p.4）明确指出 DiffXCorr 是 *bidirectional* 的——它无法区分 forward 和 reverse precedence，因此不能直接替代 PermG 在 phase diagram 中的角色（phase diagram 依赖方向性检测来确认 entropy→diversity 的时序关系）。正确的替代方案应该是保持方向性约束的前提下改进 PermG 的置换分布估计（如增大置换次数从5000到50000，或使用 bootstrap 替代置换）。

(2) 更根本的问题是：null-control 的样本量太小（6 seeds × 6-pair basis = 36 pairs），导致 FPR 估计极不精确。CI [1.2%, 30.4%] 跨越了两个数量级，这意味着 PermG 的 FPR 可能是 1%（可接受），也可能是 30%（完全不可用）。这个不确定性是无法通过统计方法回避的——需要更多 null-control 实验。我在 R2 审稿中未将此列为独立问题，但 R1 的分析是正确的。

**[AGREE] R1-W2 (Critical): 实验范围过窄**
强烈同意。这与我的 R2-W3 完全一致。"Detectability Landscape" 这一标题暗示了广泛的覆盖，但实际上 landscape 仅在 Pythia-410M + WikiText-103 上绘制。跨架构验证（§4.5）仅在 α=1.0——最容易检测的条件——下进行，且 4/15 conditions 失败。标题应更准确地反映实际覆盖范围，例如 "Characterizing the Detectability Landscape of Iterative Model Collapse *on Pythia-410M*"。

**[AGREE] R1-W3 (Major): 幂律拟合缺乏信息量**
同意。γ 的 95% CI [0.64, 2.08] 跨越了定性不同的缩放行为（亚线性 vs. 超线性），这使得幂律模型无法提供有区分度的预测。β 参数的 MLE/CV 分歧进一步说明拟合不稳定。

补充一点：论文在 §3.4 承认了这些不确定性，但仍将幂律拟合作为主要贡献之一呈现。考虑到参数估计的不确定性，Figure 1 中的虚线边界更应被解读为"粗略的经验趋势"而非"可用于预测的定量模型"。论文对此的表述（p.5, "the precise exponent is a descriptive parameterization rather than a mechanistic prediction"）是合适的，但可能被读者忽略。

**[AGREE] R1-W4 (Major): α=0.60 异常被排除**
同意排除不利数据点是有问题的做法。论文承认了这一异常（Figure 1 中的星号标记，§3.4），但在拟合边界时将其排除。在仅有4个边界α值的情况下排除一个，对拟合结果的影响可能是根本性的。

R1 建议增加 α=0.55 和 α=0.65 的实验——这是直接可行且必要的。此外，α=0.60 异常是否与 SmolLM1.3B 在跨架构验证中的非单调行为（p.7, Figure 5）有关联，也值得探讨。

**[REBUT] R1-W5 (Major): K≥3 共识投票**
部分反驳。R1 指出 κ=0.185 表明方法间几乎无 agreement，且 MMCT FPR (16.7%) > PermG standalone (11.1%)。这些数值是正确的。

但 R1 的结论——"共识框架缺乏理论支撑"——忽略了论文 Algorithm 1（Appendix J）中 MMCT 使用 FPR-inverse weighting 而非简单多数投票的设计。低 FPR 方法（PermG, DiffXCorr）获得高权重，高 FPR 方法（NaiveXCor）获得低权重。论文在 §3.3 (p.3) 明确说明 "FPR-inverse weighting is used only in exploratory method ranking"，且 PermG 被选为最终推荐方法，MMCT 仅作为鲁棒性检查。

MMCT FPR 高于 PermG 的原因是合理的：高 FPR 方法（如 NaiveXCor 91.7%）在 null 条件下几乎总是 reject，即使权重低，其共现也会推高共识率。论文 Appendix R (p.21) 的 FPR 独立性分析（"cluster alignment"）讨论了这一机制。

不过，我同意 R1 的核心观点：K 的选择（K≥3 of 5）缺乏理论最优性证明。论文应提供不同 K 值下 MMCT 的 FPR/TPR 曲线。

**[AGREE] R1-W6 (Major): Cross-architecture 仅 α=1.0**
强烈同意。这与我的 R2-W3 和 R2-Q1 一致。α=1.0 是最 trivial 的检测条件——在这个条件下失败的架构（4/15）反而说明泛化性堪忧。Phase diagram 的核心贡献区（α ∈ [0.45, 0.75]）完全没有跨架构数据。

**[AGREE] R1-W7 (Major): 关键 α 值 seed 数量不足**
同意。检测边界（α ≈ 0.45-0.60）是论文最重要的贡献区域，但每个α值仅3 seeds。在此区域增加 seeds 至 ≥5 是成本合理且必要的。α=0.10 仅单 seed 也确实不足——虽然该条件预期检测能力为零，但确认这一点也需要多 seed 验证。

**[AGREE] R1-W8 (Minor): Canary 干预超出证据强度**
同意。这与我的 R2-W4 一致。Abstract 中 "substantially reduces peak perplexity" 基于 N=2 seeds、α=1.0 单一条件、post-hoc 选择的阈值（15%），不应使用 "substantially" 这一措辞。建议降级为 "preliminary proof-of-concept"。

**[REBUT] R1-W9 (Minor): Full replacement 限制生态效度**
部分反驳。论文并非仅使用 full replacement——§4.1 (p.5) 明确说明实验覆盖 α ∈ {0.10, 0.15, ..., 1.0}，即从 10% 混合到 100% 替换的 13 个级别。这正是"混合比例"实验设计，涵盖了 R1 所说的"数据累积"场景中的不同污染浓度。

但 R1 的关注点可能是 *训练范式* 本身：论文使用的是每代从头训练（train from scratch on mixture），而非增量式微调（continual fine-tuning on accumulating data）。后者确实更接近实际部署场景。论文 Limitations (p.8-9) 提及了这一限制。所以 R1 的核心关切（生态效度）是合理的，但 "full replacement" 这一表述不够精确。

---

## Questions

**[AGREE] R1-Q1**: 是的，MMCT FPR > PermG 很可能是因为高 FPR 方法（NaiveXCor 91.7%）在 null 条件下几乎 always reject，其投票与 PermG 共现推高了 K≥3 的达成率。Appendix R 的独立性分析可部分验证这一假设。

**[AGREE] R1-Q2**: 用 DiffXCorr 重绘 Figure 1 是有价值的鲁棒性检查。但如我在 R1-W1 回应中指出，DiffXCorr 是 bidirectional 的，重绘的 phase diagram 语义不同（检测"是否存在关联"而非"entropy 是否 precedes diversity"）。论文应同时提供两个版本以评估方向性对相变结构的影响。

**[AGREE] R1-Q3**: α=0.60 异常的 seed 一致性是判断其性质（系统性 vs. 随机波动）的关键。仅3 seeds 的情况下，1个异常 seed 就能产生非单调表象。

**[AGREE] R1-Q4**: 偏相关（控制 generation number）是标准的混淆因素检验，论文应在附录中报告。

**[AGREE] R1-Q5**: 纳入 T=5,15,20,25 的数据确实应收窄 γ 的 CI，但需注意短序列（T=5）的检测功效本身极低，可能引入新的噪声。

**[AGREE] R1-Q6**: 跨架构验证为何不在 α=0.50 进行——我在 R2-Q1 中提出了相同质疑。这是审稿意见的交叉验证点，说明两位审稿人独立得出了相同关切。

**[REBUT] R1-Q7**: AI 辅助写作是否影响不确定性表述——这一问题缺乏可操作性。论文已按要求披露了 AI 使用情况（p.28），且不确定性的表述质量应通过内容本身判断，而非推测工具的影响。除非有具体段落的不确定性表述存在问题，否则这一问题与论文质量无关。

---

## Missing References

**[REBUT] R1-Missing-Refs**: R1 称"未发现关键缺失引用"——我不同意。在 R2-W6 中，我指出了以下重要遗漏：

1. **Dakos et al. (2008, 2012)**: 早期预警信号领域的核心实证方法论贡献，与本文任务（从时间序列检测系统退化的早期信号）高度吻合，且论文已引用同领域的 Scheffer et al.，却遗漏了该领域最重要的方法论文
2. **Lenton et al. (2008)**: 气候 tipping elements 的奠基工作，论文使用了 tipping point 类比但未引用
3. **Guo et al. (2025, arXiv:2502.15654)**: "Machine-generated text detection prevents language model collapse"——与 canary detection 主题直接相关

此外，论文使用 Granger precedence 作为核心方法，但未讨论 Granger causality 的标准局限性（observational equivalence, Lucas critique 在干预场景下的相关性），而其引用的 Shojaie & Fox (2022) 的 §4 恰好讨论了这些限制。

---

## 总体评估一致性

R1 给出 3.0 (Findings)，与我的评分一致。核心共识点：

1. **方法论新颖性不足**：R1-W1/W2 与 R2-W1 指向同一问题
2. **泛化性不足**：R1-W2/W6 与 R2-W3 一致
3. **Canary 证据薄弱**：R1-W8 与 R2-W4 一致
4. **方法敏感性是最强贡献**：R1-S2 与 R2-S1 一致

两位审稿人独立得出 3.0 (Findings)，核心关切高度重叠，增强了评估的可靠性。


---

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 的逐条回应。总结：

- **14条 [AGREE]**：PermG FPR膨胀、实验范围窄、幂律拟合不稳定、α=0.60排除、跨架构仅α=1.0、seed不足、canary超出证据——与我的独立审稿高度重叠
- **3条 [REBUT]**：
  - W5（MMCT共识）：部分反驳——论文使用FPR-inverse weighting而非简单投票，MMCT仅作鲁棒性检查非主方法，但同意K选择缺乏理论依据
  - W9（full replacement）：部分反驳——论文覆盖α=0.10到1.0共13级混合比例，非仅full replacement，但训练范式（从头训练 vs. 增量微调）确实限制生态效度
  - Q7（AI影响不确定性表述）：缺乏可操作性，应通过内容判断
- **Missing References 补充**：R1称无关键缺失，我明确反驳并补充了Dakos et al.、Lenton et al.、Guo et al.三组遗漏引用

两位Reviewer独立给出3.0 (Findings)，核心关切一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1242 · 2026-05-24T15:11:51.319774+00:00_

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
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
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

_source line 1243 · 2026-05-24T15:11:51.370399+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1244 · 2026-05-24T15:11:55.787179+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1245 · 2026-05-24T15:11:56.640870+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Glob",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1246 · 2026-05-24T15:11:56.691420+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1247 · 2026-05-24T15:11:56.742008+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{graphicx}
13	\usepackage{booktabs}
14	\usepackage{subcaption}
15	\usepackage{algorithm}
16	\usepackage{algpseudocode}
17	\usepackage{amsthm}
18	\newtheorem{theorem}{Theorem}
19	\newtheorem{proposition}[theorem]{Proposition}
20	\newtheorem{designprinciple}[theorem]{Design Principle}
21	\theoremstyle{definition}
22	\newtheorem{assumption}[theorem]{Assumption}
23	
24	\title{Characterizing the Detectability Landscape of Iterative Model Collapse}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\maketitle
30	
31	\input{abstract}
32	\input{introduction}
33	\input{related_work}
34	\input{method}
35	\input{experiments}
36	\input{discussion}
37	\input{limitations}
38	\bibliography{references}
39	
40	\input{appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1248 · 2026-05-24T15:12:03.921057+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1249 · 2026-05-24T15:12:04.223423+00:00_

1	issues:
2	# ============================================================
3	# Round 1-11 历史 resolved — 保留跨轮次记录
4	# ============================================================
5	- id: "R1-N1"
6	  summary: "Ground-truth pairs 定义存在循环论证"
7	  category: method
8	  severity: critical
9	  status: resolved
10	  first_raised_round: 1
11	  last_seen_round: 1
12	  resolution: "Effect-size GT 重定义完成。"
13	  resolution_round: 1
14	
15	- id: "R1-N2"
16	  summary: "FPR=0% 标定仅基于单 seed"
17	  category: method
18	  severity: critical
19	  status: resolved
20	  first_raised_round: 1
21	  last_seen_round: 1
22	  resolution: "α=0.0 三 seed FPR 验证完成。"
23	  resolution_round: 1
24	
25	- id: "R1-N3"
26	  summary: "α=0.50 和 α=0.75 仅 1 seed"
27	  category: experiment
28	  severity: critical
29	  status: resolved
30	  first_raised_round: 1
31	  last_seen_round: 1
32	  resolution: "Multi-seed 补充完成。"
33	  resolution_round: 1
34	
35	- id: "R2-N1"
36	  summary: "核心方法论为计量经济学已有知识的直接迁移，新颖性有限"
37	  category: framing
38	  severity: critical
39	  status: resolved
40	  first_raised_round: 1
41	  last_seen_round: 2
42	  resolution: "Round 1 三层定位 reframe 完成。"
43	  resolution_round: 1
44	
45	- id: "R2-N2"
46	  summary: "α=0.75 multi-seed 实验未完成 + Appendix A 缺失"
47	  category: experiment
48	  severity: critical
49	  status: resolved
50	  first_raised_round: 1
51	  last_seen_round: 1
52	  resolution: "完成。"
53	  resolution_round: 1
54	
55	- id: "R2-N3"
56	  summary: "实验规模过窄"
57	  category: experiment
58	  severity: critical
59	  status: resolved
60	  first_raised_round: 1
61	  last_seen_round: 1
62	  resolution: "跨架构验证已扩展至 15 model-seed 组合。"
63	  resolution_round: 1
64	
65	- id: "R1-W1"
66	  summary: "Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致"
67	  category: writing
68	  severity: warning
69	  status: resolved
70	  first_raised_round: 1
71	  last_seen_round: 2
72	  resolution: "核心修复完成。"
73	  resolution_round: 1
74	
75	- id: "R1-W2"
76	  summary: "PermG 缺少 power analysis"
77	  category: metho
…[truncated 30766 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1250 · 2026-05-24T15:12:04.325460+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/abstract.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/abstract.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1251 · 2026-05-24T15:12:04.376098+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1252 · 2026-05-24T15:12:08.241457+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1253 · 2026-05-24T15:12:08.292773+00:00_

1	\begin{abstract}
2	Iterative training on model-generated text degrades distributional quality well before standard metrics flag collapse, yet detecting this degradation is difficult: the time series are short ($T{\leq}25$ generations), the signal grows sub-linearly with contamination fraction, and, as we show, the choice of statistical test alone can shift conclusions from universal detection to complete null.
3	We map the detectability landscape of this process on Pythia-410M across 13 contamination levels; cross-architecture evaluation at $\alpha{=}1.0$ supports forward detection in 11/15 conditions across five families (345M--6.9B), with four non-confirming conditions isolating distinct failure modes.
4	Permutation Granger causality (PermG) reveals a detection boundary consistent with power-law scaling in observation length and three confirmed regimes---blind, onset, detection---plus one unexplained non-monotonic anomaly, including a sharp onset where detection jumps from 0/8 to 6/8 within a 2-percentage-point interval.
5	Five methods applied to identical data yield null-control false positive rates from 3\% to 92\%, exposing method sensitivity as a primary concern.
6	Entropy Granger-precedes diversity collapse by ${\geq}1$ generation (14/15 experiments), providing a canary whose triggered cessation substantially reduces peak perplexity in a proof-of-concept demonstration ($N{=}2$, $\alpha{=}1.0$).
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1254 · 2026-05-24T15:16:53.100275+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distrib_canary_collapse",
  "issues_yaml": "issues:\n# ============================================================\n# Round 1-11 历史 resolved — 保留跨轮次记录\n# ============================================================\n- id: \"R1-N1\"\n  summary: \"Ground-truth pairs 定义存在循环论证\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Effect-size GT 重定义完成。\"\n  resolution_round: 1\n\n- id: \"R1-N2\"\n  summary: \"FPR=0% 标定仅基于单 seed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"α=0.0 三 seed FPR 验证完成。\"\n  resolution_round: 1\n\n- id: \"R1-N3\"\n  summary: \"α=0.50 和 α=0.75 仅 1 seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Multi-seed 补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-N1\"\n  summary: \"核心方法论为计量经济学已有知识的直接迁移，新颖性有限\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Round 1 三层定位 reframe 完成。\"\n  resolution_round: 1\n\n- id: \"R2-N2\"\n  summary: \"α=0.75 multi-seed 实验未完成 + Appendix A 缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-N3\"\n  summary: \"实验规模过窄\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"跨架构验证已扩展至 15 model-seed 组合。\"\n  resolution_round: 1\n\n- id: \"R1-W1\"\n  summary: \"Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"核心修复完成。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"PermG 缺少 power analysis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Appendix N power analysis 完成。\"\n  resolution_round: 1\n\n- id: \"R1-W3\"\n  summary: \"75% spurious-signal rate headline 依赖 underpowered T-Y\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W4\"\n  summary: \"α=0.75 单 seed borderline 结果不应出现在 abstract\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W5\"\n  summary: \"Toda-Yamamoto 纳入理由表述不充分\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W6\"\n  summary: \"可重复性信息不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"超参补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-W3\"\n  summary: \"Token entropy canary 仅在 α=1.0 验证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"缺少独立 Limitations section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W5\"\n  summary: \"缺少 AI Writing Disclosure\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W6\"\n  summary: \"缺少 canary→perplexity 为何 spurious 的深入解释\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF1\"\n  summary: \"遗漏 Granger & Newbold (1974)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF2\"\n  summary: \"遗漏 Hataya et al. (2023) 和 Seddik et al. (2024)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W1-old\"\n  summary: \"Citation key chen2025scales 与实际作者不匹配\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"F2-W3\"\n  summary: \"Section 3 承诺的三项附录内容缺失\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"附录内容补充完成。\"\n  resolution_round: 3\n\n- id: \"F2-W8\"\n  summary: \"格式不合规：未使用 ACL 模板\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"ACL 模板迁移完成。\"\n  resolution_round: 2\n\n- id: \"F2-REF1\"\n  summary: \"遗漏 arXiv:2502.15654\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF1\"\n  summary: \"遗漏 arXiv:2602.10531\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF2\"\n  summary: \"遗漏 arXiv:2505.19046\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF3\"\n  summary: \"遗漏 arXiv:2510.16657\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF5\"\n  summary: \"Appendix H CUSUM 未引用 Page (1954)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F4-REF1\"\n  summary: \"遗漏 Truong & Truong (2026)\"\n  category: reference\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"引用已添加并在 §1/§2 讨论。\"\n  resolution_round: 6\n\n- id: \"F4-REF3\"\n  summary: \"遗漏 Benjamini & Yekutieli (2001)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"§4 现引用 benjamini2001control。\"\n  resolution_round: 5\n\n- id: \"F2-REF3\"\n  summary: \"Dakos et al. (2012) + Schreiber (2000) + Phipson & Smyth (2010) 在 bib 中但正文未引用\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"引用补充完成。\"\n  resolution_round: 4\n\n- id: \"F6-W2\"\n  summary: \"页数可能超限\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"R8 PDF 审查确认主体 8 页合规。\"\n  resolution_round: 8\n\n- id: \"F2-W6b\"\n  summary: \"'Methodological pitfalls' 有 straw-man 倾向\"\n  category: framing\n  severity: major\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 8\n  resolution: \"全文已改为 'design considerations'。R8 fresh review 未再提及。\"\n  resolution_round: 8\n\n- id: \"F5-N2\"\n  summary: \"T=10 统计效力不足(power≈37%), sharp onset 可能是 power artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Power simulation 重写通过。Steepness comparison 写入正文。Dense α 证据额外支撑。\"\n  resolution_round: 9\n  first_raised_round: 5\n  last_seen_round: 9\n\n- id: \"F2-W5\"\n  summary: \"Token entropy → distinct-n 机械耦合 confound 未排除\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Metric structure 分析完成。讨论已添加。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 9\n\n- id: \"F2-W2\"\n  summary: \"Specification curve analysis 定位不精确\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Appendix E 已改称 'systematic robustness analysis'。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 8\n\n- id: \"F8-C2\"\n  summary: \"Discussion §6 过于简短(~100词)\"\n  category: writing\n  severity: major\n  status: resolved\n  resolution: \"Discussion 扩展至 20 行。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C3\"\n  summary: \"与 Schaeffer et al. (2025) '8 种 collapse 定义' 的关系讨论不充分\"\n  category: framing\n  severity: major\n  status: resolved\n  resolution: \"Schaeffer taxonomy 映射已添加到 related_work.tex。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C1\"\n  summary: \"Du & Tanaka-Ishii (2026) 引用三重错误\"\n  category: reference\n  severity: critical\n  status: resolved\n  resolution: \"§2 已修正。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"R9-C1\"\n  summary: \"FPR CI method.tex 内部矛盾\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"FPR=10% MMCT sensitivity analysis 完成。\"\n  resolution_round: 9\n  first_raised_round: 9\n  last_seen_round: 9\n\n- id: \"F8-N1\"\n  summary: \"BH-FDR 在强正回归依赖下适用性讨论不充分\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"PRDS 假设适用性讨论已添加。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 10\n\n- id: \"F8-REF1\"\n  summary: \"遗漏引用：online/continual learning 下 model collapse 检测\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"related_work.tex 已添加 scope 区分。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F2-W11\"\n  summary: \"α_c SE=0.006 低估真实 seed 不确定性\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"被 F2-W4b/F2-W6 的统计基础问题覆盖。\"\n  resolution_round: 11\n  first_raised_round: 2\n  last_seen_round: 10\n\n- id: \"F8-N2\"\n  summary: \"未讨论为何选择经典 permutation Granger 而非 neural Granger causality\"\n  category: method\n  severity: minor\n  status: resolved\n  resolution: \"§4 已添加 T≤25 理由。§2 引用 neural Granger 文献。\"\n  resolution_round: 11\n  first_raised_round: 8\n  last_seen_round: 11\n\n- id: \"R9-REF2\"\n  summary: \"遗漏引用：Steegen et al. (2016) multiverse analysis\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 steegen2016increasing。\"\n  resolution_round: 11\n  first_raised_round: 9\n  last_seen_round: 11\n\n- id: \"R10-REF2\"\n  summary: \"遗漏引用：Mitchell et al. (2023) DetectGPT\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 mitchell2023detectgpt。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-REF4\"\n  summary: \"遗漏引用：Padmakumar et al. (2024)\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 padmakumar2024writing。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n\n# ============================================================\n# 活跃 issues — Round 13\n# ============================================================\n\n- id: \"F3-J4\"\n  summary: \"PermG FPR 超出 nominal 5%，architecture-dependent\"\n  category: method\n  severity: critical\n  status: in_progress\n  resolution: \"R13: K≥3 FPR 从 0% 更正为 16.7%。GPT-2 50% FPR 在 §5.5 + Discussion + Limitations 标注。但 R13 审稿确认问题仍存在：null-control 仅 36 pairs，CI [1.2%, 30.4%] 跨两个数量级。R2 补充 DiffXCorr 替代方案的方向性限制。两位 Reviewer 共识 critical。\"\n  resolution_round: null\n  first_raised_round: 3\n  last_seen_round: 13\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 MF-1。6轮 mild hedging 失败。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 双方共识 critical。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 双方共识 critical。R2 补充技术细节：DiffXCorr bidirectional 不能替代 PermG 方向性，正确方案是增大置换次数或 bootstrap。null-control 36 pairs 使 FPR 估计本质上不精确。\"\n  action_items:\n    - round: 13\n      action: \"增加 null-control seeds 至 ≥12 使 FPR 估计 CI 收窄；或在正文报告保守版边界\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W4b\"\n  summary: \"幂律边界 α_c(T) 拟合基础薄弱\"\n  category: framing\n  severity: critical\n  status: in_progress\n  resolution: \"R13 论文修改：Abstract 删除 MAE=0.037 和 15/15，改为 'consistent with power-law scaling'。γ ∈ [0.64, 2.08] CI 全面报告。boundary 重新定位为 descriptive parametrization。R13 审稿确认降级方向正确，但 γ CI 仍跨越亚线性/超线性定性分界，Figure 1 虚线边界应为'粗略经验趋势'而非定量模型。\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 13\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 双方共识。γ CI [0.64, 2.08] 使幂律模型无区分度预测。β MLE/CV 分歧证实拟合不稳定。降级表述方向正确但 Figure 1 仍可能误导。\"\n  action_items:\n    - round: 13\n      action: \"Figure 1 caption 明确标注虚线为粗略经验趋势；考虑移除或降级幂律拟合作为独立贡献\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W2b\"\n  summary: \"'Detectability landscape' framing 承诺超过交付\"\n  category: framing\n  severity: critical\n  status: in_progress\n  resolution: \"R13 论文修改：Cross-arch 改为 'exploratory evaluation at single extreme condition α=1.0'。Abstract/Intro/Experiments 全面标注 scope。R13 审稿确认修改方向正确。R2 同意标题可保留但建议更精确地反映覆盖范围。两位 Reviewer 独立确认 landscape 仅 Pythia-410M + WikiText-103。\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 13\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 双方共识。R2 建议标题修改为含 'on Pythia-410M'。跨架构仅 α=1.0（最极端条件），4/15 失败。\"\n  action_items:\n    - round: 13\n      action: \"考虑标题加限定语；确保读者不会误解 landscape 覆盖范围\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W10\"\n  summary: \"Cross-architecture 'coupling preserved' 条件 post-hoc\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 13\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 与 F2-W2b 继续合并。跨架构仅 α=1.0 是最 trivial 条件，失败的 4/15 反而说明泛化性堪忧。\"\n\n- id: \"R11-N1\"\n  summary: \"统计功率 β=0.66 CI [0.24,0.78] 使检测边界定量解读不可靠\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 与 F2-W4b 继续合并。β 不可识别性使 boundary model 定量形式不确定。\"\n\n- id: \"F2-W7\"\n  summary: \"Intervention 实验薄弱\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 13\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 双方共识。Abstract 'substantially reduces peak perplexity' 基于 N=2/α=1.0/post-hoc threshold，不应用 'substantially'。建议降级为 'preliminary proof-of-concept'。R2 强调 CUSUM comparison 显示 simple threshold 同效，削弱 Granger 框架实用优势。\"\n  action_items:\n    - round: 13\n      action: \"Abstract 'substantially' 降级；从主要贡献剥离；明确 proof-of-concept 定位\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R12-N1\"\n  summary: \"Design Principle 'formal design rationale' 作为独立贡献 oversells\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 R1 rebut（mode amplification 下特定机制非公理），R2 同意 Propositions 4-5 增加严谨性但核心假设较强。交叉后共识：内容非 trivial 但 contribution framing 仍需降级。\"\n  action_items:\n    - round: 13\n      action: \"将 Contribution 2 降级为 'empirically validated ordering principle'\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-W1\"\n  summary: \"'3%-92%' FPR 范围含失效方法 NaiveXCorr\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: []\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 双方同意方法敏感性是最强贡献。3%-92% 全范围保留但需在正文首次出现时区分合理方法与失效方法。\"\n\n- id: \"R11-W2\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 R1 同意每α值仅3 seeds 不足，建议边界区域增至≥5。\"\n\n- id: \"R10-VIS1\"\n  summary: \"Table 1 / Figure 6 浮动超出 8 页主文边界\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2, visual_check]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [visual_check]\n      note: \"R13 视觉审查未单独报告页数超限但报告主文无 table（0 个 table），所有定量表格在 appendix。需确认是否已将 Table 1 移至 appendix。\"\n  action_items:\n    - round: 13\n      action: \"确认主文 8 页合规；至少一个核心结果 summary table 应在主文中\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R12-W1\"\n  summary: \"写作信息密度过高，关键 findings 淹没在数字洪流中\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: []\n      note: \"R13 未单独提及。视觉审查侧面印证：pages 5-6 连续纯文本。\"\n\n- id: \"R11-FMT1\"\n  summary: \"Abstract 脚注不标准\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n\n- id: \"R11-SYM1\"\n  summary: \"β 符号重用：统计功率 vs 幂律指数\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n\n- id: \"F5-N1\"\n  summary: \"核心方法是计量经济学标准技术的直接移植\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 13\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 R1 rebut（empirical systems paper 非方法论创新），R2 同意但称本质是 power analysis 迁移。交叉后共识：novelty 来自 method-sensitivity finding 和 phase-diagram framing，非技术方法本身。不可改变的天花板。\"\n\n- id: \"F5-W1\"\n  summary: \"Design Principles 数学深度有限\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 13\n  mentions:\n    - round: 5\n      reviewers: [2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 R2 同意 Propositions 4-5 增加严谨性但核心假设（Assumption 3 mode amplification）较强，结论接近'连续>离散'。R1 rebut：specific ordering 非 trivial。\"\n\n- id: \"F2-W1\"\n  summary: \"α=0.60 sync dip：mechanism unexplained\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 双方共识。R2 指出排除 α=0.60 在仅 4 个边界 α 值中排除一个是根本性影响。建议增加 α=0.55/0.65 实验。R2 进一步关联到 SmolLM1.3B 跨架构非单调行为。\"\n  action_items:\n    - round: 13\n      action: \"增加 α=0.55/0.65 实验以确认异常性质；或降级为 'three regimes + one anomaly'\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W6\"\n  summary: \"Detection boundary 验证不足\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 与 F2-W4b 继续合并。sync-dip 排除后仅有限 cells 可用。\"\n\n- id: \"R10-MF5\"\n  summary: \"'Five families (345M-6.9B)' 数字自洽性\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 继续确认：'five families' 给读者广泛可推广印象，与 F2-W2b scope 问题合并。\"\n\n- id: \"R10-SF2\"\n  summary: \"Data accumulation vs replacement paradigm 未讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: []\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 R2 rebut R1-W9：论文覆盖 α=0.10-1.0 非仅 full replacement。但训练范式（从头训练 vs 增量微调）限制生态效度。Limitations 已覆盖。\"\n\n- id: \"R10-SF3\"\n  summary: \"单一解码策略需定性讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-SF4\"\n  summary: \"方法敏感性 '3%-92%' framing\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-SF5\"\n  summary: \"Bivariate confounding\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-SF6\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-SF7\"\n  summary: \"3-4 seeds replication power 有限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 R1 同意检测边界区 3 seeds 不足，建议≥5。R2 同意。\"\n\n- id: \"R11-VIS2\"\n  summary: \"Pages 5-6 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [visual_check]\n    - round: 12\n      reviewers: [visual_check]\n    - round: 13\n      reviewers: [visual_check]\n      note: \"R13 视觉审查再次确认：pages 5-6 连续纯文本，Figures 3-5 堆积在 page 7。建议前移至少一个 figure。\"\n\n- id: \"F8-W2\"\n  summary: \"Figure 子图内文字偏小\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [visual_check]\n    - round: 12\n      reviewers: [visual_check]\n    - round: 13\n      reviewers: [visual_check]\n      note: \"R13 视觉审查确认 Figures 3-5 axis label 约 6-7pt，低于可读性阈值。Figure 2 框内数字偏小。\"\n\n- id: \"R10-REF3\"\n  summary: \"遗漏引用：Runge et al. (2019) PCMCI\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R9-m5\"\n  summary: \"Granger 'precedence' vs 'causality' 术语不一致\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n\n- id: \"R9-REF1\"\n  summary: \"遗漏引用：Gerstgrasser et al. (2024) data accumulation\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n\n- id: \"R10-m1\"\n  summary: \"Figure 3 y 轴标签含义不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-m2\"\n  summary: \"Table 2 'x/8' 列含义未定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-m3\"\n  summary: \"§5.1 前向引用缺上下文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-REF5\"\n  summary: \"遗漏引用：Montgomery SPC\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"F4-REF5\"\n  summary: \"bib first author mismatch: dey2024breaking\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 4\n  last_seen_round: 11\n\n- id: \"F2-W9b\"\n  summary: \"孤立 bib entries\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 2\n  last_seen_round: 8\n\n- id: \"F6-C2\"\n  summary: \"buffa2026entropy 引用标题不匹配\"\n  category: reference\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 8\n\n- id: \"F8-N3\"\n  summary: \"Appendix 关键验证内容应纳入正文\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"F8-N4\"\n  summary: \"predict-then-verify post-hoc adjustment 嫌疑\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"R12-REF1\"\n  summary: \"遗漏引用：Adams & MacKay (2007) Bayesian online changepoint detection\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-REF2\"\n  summary: \"遗漏引用：Papana et al. (2013) / Siggiridou & Kugiumtzis (2016) permutation Granger validation\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-W2\"\n  summary: \"Eq.1 sigmoid 上界 0.70 选择理由未说明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-W3\"\n  summary: \"α 采样间隔不均匀（0.10→0.25 跳跃）理由未解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-W4\"\n  summary: \"Schaeffer et al. 8 种 collapse 定义中本文使用哪种未明确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n# ============================================================\n# 新 issues — Round 13\n# ============================================================\n\n- id: \"R13-W1\"\n  summary: \"MMCT K≥3 共识框架 K 选择缺乏理论最优性证明\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1 指出 κ=0.185 方法间几乎无 agreement，MMCT FPR(16.7%) > PermG(11.1%)。R2 部分 rebut：FPR-inverse weighting 非简单投票，MMCT 仅作鲁棒性检查。但 R2 同意 K 选择缺乏理论依据。共识：论文应提供不同 K 值下 MMCT FPR/TPR 曲线。\"\n  action_items:\n    - round: 13\n      action: \"补充 K=2,3,4,5 下 MMCT FPR/TPR 对比；或将 MMCT 降级为纯附录内容\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R13-W2\"\n  summary: \"α=0.60 异常排除对幂律拟合的根本性影响\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"仅 4 个边界 α 值，排除 1 个对拟合结果影响根本性。R1 建议增加 α=0.55/0.65 实验。R2 补充可能与 SmolLM1.3B 非单调行为有关联。3 seeds 中 1 个异常即可产生非单调表象。与 F2-W1 和 F2-W4b 交叉。\"\n  action_items:\n    - round: 13\n      action: \"增加 α=0.55/0.65 实验验证；分析异常 seed 一致性\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R13-W3\"\n  summary: \"跨架构验证仅在 α=1.0 最极端条件进行\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立提出相同质疑：phase diagram 核心贡献区 α∈[0.45,0.75] 完全没有跨架构数据。α=1.0 是最 trivial 检测条件，此条件下失败 4/15 反而说明泛化性堪忧。与 F2-W2b 合并。\"\n\n- id: \"R13-W4\"\n  summary: \"Abstract 'substantially reduces peak perplexity' 超出证据强度\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"N=2 seeds, α=1.0 单一条件, post-hoc 15% 阈值。'substantially' 应降级为 'preliminary proof-of-concept'。与 F2-W7 合并。\"\n\n- id: \"R13-W5\"\n  summary: \"偏相关分析（控制 generation number）缺失\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 同意。Granger precedence 可能被 generation number 混淆。标准检验应在附录报告。\"\n\n- id: \"R13-REF1\"\n  summary: \"遗漏引用：Dakos et al. (2008, 2012) 早期预警信号核心实证方法论\"\n  category: reference\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"论文已引用 Scheffer et al. 却遗漏该领域最重要的方法论文。任务高度吻合：从时间序列检测系统退化的早期信号。需验证是否已在 bib 中。\"\n\n- id: \"R13-REF2\"\n  summary: \"遗漏引用：Lenton et al. (2008) 气候 tipping elements\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"论文使用 tipping point 类比但未引用该奠基工作。\"\n\n- id: \"R13-REF3\"\n  summary: \"Granger causality 标准局限性（observational equivalence, Lucas critique）未讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"论文引用的 Shojaie & Fox (2022) §4 恰好讨论了这些限制，但论文未提及。在 intervention 场景下 Lucas critique 的相关性值得讨论。\"\n\n- id: \"R13-VIS1\"\n  summary: \"主文 8 页 0 个 table，所有定量结果表格在 appendix\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [visual_check]\n      note: \"实证为主的论文在主文中应有至少一个核心结果 summary table。审稿人需翻 appendix 查看定量结果增加认知负担。\"\n\n- id: \"R13-VIS2\"\n  summary: \"前两页无任何 display item，Figure 1 直到第 3 页\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [visual_check]\n      note: \"审稿人前 2 分钟只看到文字，缺少视觉锚点。考虑 teaser figure。\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "issues_yaml": "issues:\n# ============================================================\n# Round 1-11 历史 resolved — 保留跨轮次记录\n# ============================================================\n- id: \"R1-N1\"\n  summary: \"Ground-truth pairs 定义存在循环论证\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Effect-size GT 重定义完成。\"\n  resolution_round: 1\n\n- id: \"R1-N2\"\n  summary: \"FPR=0% 标定仅基于单 seed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"α=0.0 三 seed FPR 验证完成。\"\n  resolution_round: 1\n\n- id: \"R1-N3\"\n  summary: \"α=0.50 和 α=0.75 仅 1 seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Multi-seed 补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-N1\"\n  summary: \"核心方法论为计量经济学已有知识的直接迁移，新颖性有限\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Round 1 三层定位 reframe 完成。\"\n  resolution_round: 1\n\n- id: \"R2-N2\"\n  summary: \"α=0.75 multi-seed 实验未完成 + Appendix A 缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-N3\"\n  summary: \"实验规模过窄\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"跨架构验证已扩展至 15 model-seed 组合。\"\n  resolution_round: 1\n\n- id: \"R1-W1\"\n  summary: \"Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"核心修复完成。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"PermG 缺少 power analysis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Appendix N power analysis 完成。\"\n  resolution_round: 1\n\n- id: \"R1-W3\"\n  summary: \"75% spurious-signal rate headline 依赖 underpowered T-Y\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W4\"\n  summary: \"α=0.75 单 seed borderline 结果不应出现在 abstract\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W5\"\n  summary: \"Toda-Yamamoto 纳入理由表述不充分\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W6\"\n  summary: \"可重复性信息不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"超参补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-W3\"\n  summary: \"Token entropy canary 仅在 α=1.0 验证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"缺少独立 Limitations section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W5\"\n  summary: \"缺少 AI Writing Disclosure\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W6\"\n  summary: \"缺少 canary→perplexity 为何 spurious 的深入解释\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF1\"\n  summary: \"遗漏 Granger & Newbold (1974)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF2\"\n  summary: \"遗漏 Hataya et al. (2023) 和 Seddik et al. (2024)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W1-old\"\n  summary: \"Citation key chen2025scales 与实际作者不匹配\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"F2-W3\"\n  summary: \"Section 3 承诺的三项附录内容缺失\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"附录内容补充完成。\"\n  resolution_round: 3\n\n- id: \"F2-W8\"\n  summary: \"格式不合规：未使用 ACL 模板\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"ACL 模板迁移完成。\"\n  resolution_round: 2\n\n- id: \"F2-REF1\"\n  summary: \"遗漏 arXiv:2502.15654\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF1\"\n  summary: \"遗漏 arXiv:2602.10531\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF2\"\n  summary: \"遗漏 arXiv:2505.19046\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF3\"\n  summary: \"遗漏 arXiv:2510.16657\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF5\"\n  summary: \"Appendix H CUSUM 未引用 Page (1954)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F4-REF1\"\n  summary: \"遗漏 Truong & Truong (2026)\"\n  category: reference\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"引用已添加并在 §1/§2 讨论。\"\n  resolution_round: 6\n\n- id: \"F4-REF3\"\n  summary: \"遗漏 Benjamini & Yekutieli (2001)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"§4 现引用 benjamini2001control。\"\n  resolution_round: 5\n\n- id: \"F2-REF3\"\n  summary: \"Dakos et al. (2012) + Schreiber (2000) + Phipson & Smyth (2010) 在 bib 中但正文未引用\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"引用补充完成。\"\n  resolution_round: 4\n\n- id: \"F6-W2\"\n  summary: \"页数可能超限\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"R8 PDF 审查确认主体 8 页合规。\"\n  resolution_round: 8\n\n- id: \"F2-W6b\"\n  summary: \"'Methodological pitfalls' 有 straw-man 倾向\"\n  category: framing\n  severity: major\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 8\n  resolution: \"全文已改为 'design considerations'。R8 fresh review 未再提及。\"\n  resolution_round: 8\n\n- id: \"F5-N2\"\n  summary: \"T=10 统计效力不足(power≈37%), sharp onset 可能是 power artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Power simulation 重写通过。Steepness comparison 写入正文。Dense α 证据额外支撑。\"\n  resolution_round: 9\n  first_raised_round: 5\n  last_seen_round: 9\n\n- id: \"F2-W5\"\n  summary: \"Token entropy → distinct-n 机械耦合 confound 未排除\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Metric structure 分析完成。讨论已添加。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 9\n\n- id: \"F2-W2\"\n  summary: \"Specification curve analysis 定位不精确\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Appendix E 已改称 'systematic robustness analysis'。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 8\n\n- id: \"F8-C2\"\n  summary: \"Discussion §6 过于简短(~100词)\"\n  category: writing\n  severity: major\n  status: resolved\n  resolution: \"Discussion 扩展至 20 行。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C3\"\n  summary: \"与 Schaeffer et al. (2025) '8 种 collapse 定义' 的关系讨论不充分\"\n  category: framing\n  severity: major\n  status: resolved\n  resolution: \"Schaeffer taxonomy 映射已添加到 related_work.tex。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C1\"\n  summary: \"Du & Tanaka-Ishii (2026) 引用三重错误\"\n  category: reference\n  severity: critical\n  status: resolved\n  resolution: \"§2 已修正。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"R9-C1\"\n  summary: \"FPR CI method.tex 内部矛盾\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"FPR=10% MMCT sensitivity analysis 完成。\"\n  resolution_round: 9\n  first_raised_round: 9\n  last_seen_round: 9\n\n- id: \"F8-N1\"\n  summary: \"BH-FDR 在强正回归依赖下适用性讨论不充分\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"PRDS 假设适用性讨论已添加。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 10\n\n- id: \"F8-REF1\"\n  summary: \"遗漏引用：online/continual learning 下 model collapse 检测\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"related_work.tex 已添加 scope 区分。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F2-W11\"\n  summary: \"α_c SE=0.006 低估真实 seed 不确定性\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"被 F2-W4b/F2-W6 的统计基础问题覆盖。\"\n  resolution_round: 11\n  first_raised_round: 2\n  last_seen_round: 10\n\n- id: \"F8-N2\"\n  summary: \"未讨论为何选择经典 permutation Granger 而非 neural Granger causality\"\n  category: method\n  severity: minor\n  status: resolved\n  resolution: \"§4 已添加 T≤25 理由。§2 引用 neural Granger 文献。\"\n  resolution_round: 11\n  first_raised_round: 8\n  last_seen_round: 11\n\n- id: \"R9-REF2\"\n  summary: \"遗漏引用：Steegen et al. (2016) multiverse analysis\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 steegen2016increasing。\"\n  resolution_round: 11\n  first_raised_round: 9\n  last_seen_round: 11\n\n- id: \"R10-REF2\"\n  summary: \"遗漏引用：Mitchell et al. (2023) DetectGPT\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 mitchell2023detectgpt。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-REF4\"\n  summary: \"遗漏引用：Padmakumar et al. (2024)\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 padmakumar2024writing。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n\n# ============================================================\n# 活跃 issues — Round 13\n# ============================================================\n\n- id: \"F3-J4\"\n  summary: \"PermG FPR 超出 nominal 5%，architecture-dependent\"\n  category: method\n  severity: critical\n  status: in_progress\n  resolution: \"R13: K≥3 FPR 从 0% 更正为 16.7%。GPT-2 50% FPR 在 §5.5 + Discussion + Limitations 标注。但 R13 审稿确认问题仍存在：null-control 仅 36 pairs，CI [1.2%, 30.4%] 跨两个数量级。R2 补充 DiffXCorr 替代方案的方向性限制。两位 Reviewer 共识 critical。\"\n  resolution_round: null\n  first_raised_round: 3\n  last_seen_round: 13\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 MF-1。6轮 mild hedging 失败。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 双方共识 critical。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 双方共识 critical。R2 补充技术细节：DiffXCorr bidirectional 不能替代 PermG 方向性，正确方案是增大置换次数或 bootstrap。null-control 36 pairs 使 FPR 估计本质上不精确。\"\n  action_items:\n    - round: 13\n      action: \"增加 null-control seeds 至 ≥12 使 FPR 估计 CI 收窄；或在正文报告保守版边界\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W4b\"\n  summary: \"幂律边界 α_c(T) 拟合基础薄弱\"\n  category: framing\n  severity: critical\n  status: in_progress\n  resolution: \"R13 论文修改：Abstract 删除 MAE=0.037 和 15/15，改为 'consistent with power-law scaling'。γ ∈ [0.64, 2.08] CI 全面报告。boundary 重新定位为 descriptive parametrization。R13 审稿确认降级方向正确，但 γ CI 仍跨越亚线性/超线性定性分界，Figure 1 虚线边界应为'粗略经验趋势'而非定量模型。\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 13\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 双方共识。γ CI [0.64, 2.08] 使幂律模型无区分度预测。β MLE/CV 分歧证实拟合不稳定。降级表述方向正确但 Figure 1 仍可能误导。\"\n  action_items:\n    - round: 13\n      action: \"Figure 1 caption 明确标注虚线为粗略经验趋势；考虑移除或降级幂律拟合作为独立贡献\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W2b\"\n  summary: \"'Detectability landscape' framing 承诺超过交付\"\n  category: framing\n  severity: critical\n  status: in_progress\n  resolution: \"R13 论文修改：Cross-arch 改为 'exploratory evaluation at single extreme condition α=1.0'。Abstract/Intro/Experiments 全面标注 scope。R13 审稿确认修改方向正确。R2 同意标题可保留但建议更精确地反映覆盖范围。两位 Reviewer 独立确认 landscape 仅 Pythia-410M + WikiText-103。\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 13\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 双方共识。R2 建议标题修改为含 'on Pythia-410M'。跨架构仅 α=1.0（最极端条件），4/15 失败。\"\n  action_items:\n    - round: 13\n      action: \"考虑标题加限定语；确保读者不会误解 landscape 覆盖范围\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W10\"\n  summary: \"Cross-architecture 'coupling preserved' 条件 post-hoc\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 13\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 与 F2-W2b 继续合并。跨架构仅 α=1.0 是最 trivial 条件，失败的 4/15 反而说明泛化性堪忧。\"\n\n- id: \"R11-N1\"\n  summary: \"统计功率 β=0.66 CI [0.24,0.78] 使检测边界定量解读不可靠\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 与 F2-W4b 继续合并。β 不可识别性使 boundary model 定量形式不确定。\"\n\n- id: \"F2-W7\"\n  summary: \"Intervention 实验薄弱\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 13\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 双方共识。Abstract 'substantially reduces peak perplexity' 基于 N=2/α=1.0/post-hoc threshold，不应用 'substantially'。建议降级为 'preliminary proof-of-concept'。R2 强调 CUSUM comparison 显示 simple threshold 同效，削弱 Granger 框架实用优势。\"\n  action_items:\n    - round: 13\n      action: \"Abstract 'substantially' 降级；从主要贡献剥离；明确 proof-of-concept 定位\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R12-N1\"\n  summary: \"Design Principle 'formal design rationale' 作为独立贡献 oversells\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 R1 rebut（mode amplification 下特定机制非公理），R2 同意 Propositions 4-5 增加严谨性但核心假设较强。交叉后共识：内容非 trivial 但 contribution framing 仍需降级。\"\n  action_items:\n    - round: 13\n      action: \"将 Contribution 2 降级为 'empirically validated ordering principle'\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-W1\"\n  summary: \"'3%-92%' FPR 范围含失效方法 NaiveXCorr\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: []\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 双方同意方法敏感性是最强贡献。3%-92% 全范围保留但需在正文首次出现时区分合理方法与失效方法。\"\n\n- id: \"R11-W2\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 R1 同意每α值仅3 seeds 不足，建议边界区域增至≥5。\"\n\n- id: \"R10-VIS1\"\n  summary: \"Table 1 / Figure 6 浮动超出 8 页主文边界\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2, visual_check]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [visual_check]\n      note: \"R13 视觉审查未单独报告页数超限但报告主文无 table（0 个 table），所有定量表格在 appendix。需确认是否已将 Table 1 移至 appendix。\"\n  action_items:\n    - round: 13\n      action: \"确认主文 8 页合规；至少一个核心结果 summary table 应在主文中\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R12-W1\"\n  summary: \"写作信息密度过高，关键 findings 淹没在数字洪流中\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: []\n      note: \"R13 未单独提及。视觉审查侧面印证：pages 5-6 连续纯文本。\"\n\n- id: \"R11-FMT1\"\n  summary: \"Abstract 脚注不标准\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n\n- id: \"R11-SYM1\"\n  summary: \"β 符号重用：统计功率 vs 幂律指数\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n\n- id: \"F5-N1\"\n  summary: \"核心方法是计量经济学标准技术的直接移植\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 13\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 R1 rebut（empirical systems paper 非方法论创新），R2 同意但称本质是 power analysis 迁移。交叉后共识：novelty 来自 method-sensitivity finding 和 phase-diagram framing，非技术方法本身。不可改变的天花板。\"\n\n- id: \"F5-W1\"\n  summary: \"Design Principles 数学深度有限\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 13\n  mentions:\n    - round: 5\n      reviewers: [2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 R2 同意 Propositions 4-5 增加严谨性但核心假设（Assumption 3 mode amplification）较强，结论接近'连续>离散'。R1 rebut：specific ordering 非 trivial。\"\n\n- id: \"F2-W1\"\n  summary: \"α=0.60 sync dip：mechanism unexplained\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 双方共识。R2 指出排除 α=0.60 在仅 4 个边界 α 值中排除一个是根本性影响。建议增加 α=0.55/0.65 实验。R2 进一步关联到 SmolLM1.3B 跨架构非单调行为。\"\n  action_items:\n    - round: 13\n      action: \"增加 α=0.55/0.65 实验以确认异常性质；或降级为 'three regimes + one anomaly'\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W6\"\n  summary: \"Detection boundary 验证不足\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 与 F2-W4b 继续合并。sync-dip 排除后仅有限 cells 可用。\"\n\n- id: \"R10-MF5\"\n  summary: \"'Five families (345M-6.9B)' 数字自洽性\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 继续确认：'five families' 给读者广泛可推广印象，与 F2-W2b scope 问题合并。\"\n\n- id: \"R10-SF2\"\n  summary: \"Data accumulation vs replacement paradigm 未讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: []\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 R2 rebut R1-W9：论文覆盖 α=0.10-1.0 非仅 full replacement。但训练范式（从头训练 vs 增量微调）限制生态效度。Limitations 已覆盖。\"\n\n- id: \"R10-SF3\"\n  summary: \"单一解码策略需定性讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-SF4\"\n  summary: \"方法敏感性 '3%-92%' framing\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-SF5\"\n  summary: \"Bivariate confounding\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-SF6\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-SF7\"\n  summary: \"3-4 seeds replication power 有限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 R1 同意检测边界区 3 seeds 不足，建议≥5。R2 同意。\"\n\n- id: \"R11-VIS2\"\n  summary: \"Pages 5-6 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [visual_check]\n    - round: 12\n      reviewers: [visual_check]\n    - round: 13\n      reviewers: [visual_check]\n      note: \"R13 视觉审查再次确认：pages 5-6 连续纯文本，Figures 3-5 堆积在 page 7。建议前移至少一个 figure。\"\n\n- id: \"F8-W2\"\n  summary: \"Figure 子图内文字偏小\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [visual_check]\n    - round: 12\n      reviewers: [visual_check]\n    - round: 13\n      reviewers: [visual_check]\n      note: \"R13 视觉审查确认 Figures 3-5 axis label 约 6-7pt，低于可读性阈值。Figure 2 框内数字偏小。\"\n\n- id: \"R10-REF3\"\n  summary: \"遗漏引用：Runge et al. (2019) PCMCI\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R9-m5\"\n  summary: \"Granger 'precedence' vs 'causality' 术语不一致\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n\n- id: \"R9-REF1\"\n  summary: \"遗漏引用：Gerstgrasser et al. (2024) data accumulation\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n\n- id: \"R10-m1\"\n  summary: \"Figure 3 y 轴标签含义不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-m2\"\n  summary: \"Table 2 'x/8' 列含义未定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-m3\"\n  summary: \"§5.1 前向引用缺上下文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-REF5\"\n  summary: \"遗漏引用：Montgomery SPC\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"F4-REF5\"\n  summary: \"bib first author mismatch: dey2024breaking\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 4\n  last_seen_round: 11\n\n- id: \"F2-W9b\"\n  summary: \"孤立 bib entries\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 2\n  last_seen_round: 8\n\n- id: \"F6-C2\"\n  summary: \"buffa2026entropy 引用标题不匹配\"\n  category: reference\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 8\n\n- id: \"F8-N3\"\n  summary: \"Appendix 关键验证内容应纳入正文\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"F8-N4\"\n  summary: \"predict-then-verify post-hoc adjustment 嫌疑\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"R12-REF1\"\n  summary: \"遗漏引用：Adams & MacKay (2007) Bayesian online changepoint detection\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-REF2\"\n  summary: \"遗漏引用：Papana et al. (2013) / Siggiridou & Kugiumtzis (2016) permutation Granger validation\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-W2\"\n  summary: \"Eq.1 sigmoid 上界 0.70 选择理由未说明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-W3\"\n  summary: \"α 采样间隔不均匀（0.10→0.25 跳跃）理由未解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-W4\"\n  summary: \"Schaeffer et al. 8 种 collapse 定义中本文使用哪种未明确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n# ============================================================\n# 新 issues — Round 13\n# ============================================================\n\n- id: \"R13-W1\"\n  summary: \"MMCT K≥3 共识框架 K 选择缺乏理论最优性证明\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1 指出 κ=0.185 方法间几乎无 agreement，MMCT FPR(16.7%) > PermG(11.1%)。R2 部分 rebut：FPR-inverse weighting 非简单投票，MMCT 仅作鲁棒性检查。但 R2 同意 K 选择缺乏理论依据。共识：论文应提供不同 K 值下 MMCT FPR/TPR 曲线。\"\n  action_items:\n    - round: 13\n      action: \"补充 K=2,3,4,5 下 MMCT FPR/TPR 对比；或将 MMCT 降级为纯附录内容\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R13-W2\"\n  summary: \"α=0.60 异常排除对幂律拟合的根本性影响\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"仅 4 个边界 α 值，排除 1 个对拟合结果影响根本性。R1 建议增加 α=0.55/0.65 实验。R2 补充可能与 SmolLM1.3B 非单调行为有关联。3 seeds 中 1 个异常即可产生非单调表象。与 F2-W1 和 F2-W4b 交叉。\"\n  action_items:\n    - round: 13\n      action: \"增加 α=0.55/0.65 实验验证；分析异常 seed 一致性\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R13-W3\"\n  summary: \"跨架构验证仅在 α=1.0 最极端条件进行\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立提出相同质疑：phase diagram 核心贡献区 α∈[0.45,0.75] 完全没有跨架构数据。α=1.0 是最 trivial 检测条件，此条件下失败 4/15 反而说明泛化性堪忧。与 F2-W2b 合并。\"\n\n- id: \"R13-W4\"\n  summary: \"Abstract 'substantially reduces peak perplexity' 超出证据强度\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"N=2 seeds, α=1.0 单一条件, post-hoc 15% 阈值。'substantially' 应降级为 'preliminary proof-of-concept'。与 F2-W7 合并。\"\n\n- id: \"R13-W5\"\n  summary: \"偏相关分析（控制 generation number）缺失\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 同意。Granger precedence 可能被 generation number 混淆。标准检验应在附录报告。\"\n\n- id: \"R13-REF1\"\n  summary: \"遗漏引用：Dakos et al. (2008, 2012) 早期预警信号核心实证方法论\"\n  category: reference\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"论文已引用 Scheffer et al. 却遗漏该领域最重要的方法论文。任务高度吻合：从时间序列检测系统退化的早期信号。需验证是否已在 bib 中。\"\n\n- id: \"R13-REF2\"\n  summary: \"遗漏引用：Lenton et al. (2008) 气候 tipping elements\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"论文使用 tipping point 类比但未引用该奠基工作。\"\n\n- id: \"R13-REF3\"\n  summary: \"Granger causality 标准局限性（observational equivalence, Lucas critique）未讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"论文引用的 Shojaie & Fox (2022) §4 恰好讨论了这些限制，但论文未提及。在 intervention 场景下 Lucas critique 的相关性值得讨论。\"\n\n- id: \"R13-VIS1\"\n  summary: \"主文 8 页 0 个 table，所有定量结果表格在 appendix\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [visual_check]\n      note: \"实证为主的论文在主文中应有至少一个核心结果 summary table。审稿人需翻 appendix 查看定量结果增加认知负担。\"\n\n- id: \"R13-VIS2\"\n  summary: \"前两页无任何 display item，Figure 1 直到第 3 页\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [visual_check]\n      note: \"审稿人前 2 分钟只看到文字，缺少视觉锚点。考虑 teaser figure。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 1255 · 2026-05-24T15:16:53.253578+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml\", \"bytes\": 28713}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 153
}
```

</details>

---
