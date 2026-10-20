# Director coordination — Part 9 of 9

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Conversation logs

[← Part 8](part-008.md) · [Transcript overview](../director-coordination.md) · [Structured JSON](../../../sessions/53/532e22af863d2a24e206.json)

## Round 219

### Tool call

_source line 2644 · 2026-05-23T05:33:20.750681+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "# Round 31 Review Issues — Fresh review (2 reviewers: R1 方法严谨性+实验设计, R2 新颖性+完整性+写作)\n# R31 is a fresh review; prior rounds' resolved/wont_fix issues carried over unchanged.\n\n# =============================================\n# Carried-over resolved issues (from prior rounds)\n# =============================================\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Wild cluster CI 修正且降级为 sensitivity analysis；non-clustered bootstrap 为主推断\"\n  resolution_round: 24\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 30\n  resolution: \"R30 移除 Cohen's d，精简至 4 个统计量，168 词\"\n  resolution_round: 30\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Ng 1999, Northcutt 2021, DivideMix 已添加\"\n  resolution_round: 24\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 24\n  resolution: \"§5 Non-triviality 段有效回应 novelty 质疑\"\n  resolution_round: 24\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组\"\n  resolution_round: 19\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"Limitations 新增 pure-strategy upper bound 段落\"\n  resolution_round: 24\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"术语全局修正为 text augmentation\"\n  resolution_round: 24\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"P-invariance 适用范围明确量化\"\n  resolution_round: 24\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"4B router 结论 qualified；完整统计处理\"\n  resolution_round: 24\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Router claim 从绝对否定改为有条件否定\"\n  resolution_round: 24\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"措辞软化 + effect size detection threshold 完整报告\"\n  resolution_round: 24\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 non-learnability 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R18-N1 解决\"\n  resolution_round: 24\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"'structurally determined' → 'empirically dominated'\"\n  resolution_round: 24\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 不显著问题\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Per-task 结果标注为 exploratory\"\n  resolution_round: 24\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entries + Webb 年份\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"清理完毕\"\n  resolution_round: 24\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman, Mihatsch, Natarajan\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"所有缺失引用已补充\"\n  resolution_round: 24\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Appendix Overview 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M4\"\n  summary: \"§3.1 术语首次出现未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"术语已修正并定义\"\n  resolution_round: 24\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 agreement 声明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Single annotator caveat 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"§5 已讨论\"\n  resolution_round: 24\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R17-M1 解决\"\n  resolution_round: 24\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"交叉引用指向 §2.1 operationalization\"\n  resolution_round: 24\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"Appendix B 加 circularity caveat\"\n  resolution_round: 24\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 讨论深度不足\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"引用已补全；8 页限制无法展开\"\n  resolution_round: 24\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语歧义\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"修正为 computation modes\"\n  resolution_round: 24\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"§3.1 binary structure 讨论充分\"\n  resolution_round: 24\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"72B decomposition 完整报告\"\n  resolution_round: 24\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"被 R20-N2 取代并解决\"\n  resolution_round: 24\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 未被引用\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"Appendix L 已引用\"\n  resolution_round: 24\n\n- id: \"R19-W1\"\n  summary: \"缺 penalty magnitude 实验验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"P-invariance by design 论证覆盖\"\n  resolution_round: 24\n\n- id: \"R19-N1\"\n  summary: \"Framework vs finding 定位不清\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 27\n  resolution: \"统一为 empirical analysis + reusable diagnostic methodology\"\n  resolution_round: 27\n\n- id: \"R26-N3\"\n  summary: \"Strawman framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 26\n  last_seen_round: 27\n  resolution: \"R27 验收确认修复完好\"\n  resolution_round: 27\n\n- id: \"R28-M2\"\n  summary: \"Pages 7-8 纯文本无 display item\"\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 28\n  last_seen_round: 31\n  resolution: \"8 页限制下无法插入 display item\"\n  resolution_round: 28\n  mentions:\n    - round: 31\n      source: \"Visual Check\"\n      note: \"R31 视觉审查再次标记 pages 7-8 纯文本无 figure/table，建议加 summary bar chart\"\n\n- id: \"R28-M4\"\n  summary: \"Figure 2 仅 11 点无 task name label\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 28\n  last_seen_round: 29\n  resolution: \"Figure 2 已缩至 0.38\\\\textwidth\"\n  resolution_round: 28\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 30\n  resolution: \"R30 确认正文 ≤8 页\"\n  resolution_round: 30\n\n- id: \"R29-N1\"\n  summary: \"正文超出 8 页限制（复发）\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 30\n  resolution: \"R30 确认正文 ≤8 页\"\n  resolution_round: 30\n\n- id: \"R27-N2\"\n  summary: \"DAF=90.4% framing 过度突出\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 30\n  resolution: \"R30: Intro 重构——降低 DAF 权重，突出 oracle degeneracy 96.3%、72B 5 int-pref、Reflexion DAF>100%。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R27-N3\"\n  summary: \"Deterministic strategy 实为 oracle access，跨环境含义不统一\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 30\n  resolution: \"R30: §2.1 加 umbrella term（privileged-information strategy）；Discussion 加 Δ_nd=2.84 oracle privilege 回应 + ALFWorld DAF=0% 对照。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R27-N4\"\n  summary: \"环境覆盖过窄\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 31\n  resolution: \"结构性限制。Limitations/hedging 已到位。Conclusion 加 future work。\"\n  resolution_round: 30\n  mentions:\n    - round: 31\n      source: \"R1-W1, R2-W3\"\n      note: \"R31 fresh review 再次将单一主环境标记为 critical——两位 Reviewer 共识认为需要至少第二个 death-dominated 环境验证\"\n\n- id: \"R27-W1\"\n  summary: \"Router negative result framing\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 30\n  resolution: \"R30: §3.5 title → 'Inconclusive Results'，正文 'inconclusive under current data regime'。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R27-W2\"\n  summary: \"Actionability 有限，Decision Framework 被埋\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 30\n  resolution: \"R30: Discussion 合并 oracle degeneracy 96.3% + Decision Framework 摘要 + action-level filter。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R27-W4\"\n  summary: \"Excluded tasks prescreening 样本量小\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 30\n  resolution: \"Anti-cherry-picking analysis 已到位。全 30 task types 列为 future work。\"\n  resolution_round: 30\n\n- id: \"R27-W5\"\n  summary: \"K=11 cluster bootstrap CI\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 30\n  resolution: \"R2 rebut 有效。论文已自我限定。\"\n  resolution_round: 30\n\n- id: \"R28-N1\"\n  summary: \"Episode-level vs step-level 粒度失配\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R29-R30 均未再提及，prior fix 有效\"\n  resolution_round: 30\n\n- id: \"R28-W1\"\n  summary: \"72B scaling 仅做 probe\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R30: 降级 'preliminary probe' + DAF CI [86.1%, 97.9%] + 修正 5 int-pref (非 0)。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R28-W2\"\n  summary: \"'Death' 术语限制 generality\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R29-R30 均未再提及\"\n  resolution_round: 30\n\n- id: \"R28-M1\"\n  summary: \"Missing references: hallucination detection, early exit\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R30: SelfCheckGPT + Kadavath 2022 + DeeBERT + PABEE 已加入 §4。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R28-M3\"\n  summary: \"Introduction/Discussion/Conclusion 重复度高\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R30: Discussion 压缩 3→2 段去重；Conclusion 扩展含 future work 且无与 Intro 重复。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R28-M5\"\n  summary: \"Related Work 缺 non-agent adaptive computation\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R30: DeeBERT + PABEE early exit positioning 句已加入 §4。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R29-W1\"\n  summary: \"Non-death 21.1% routing signal 来源未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 30\n  resolution: \"R30: Appendix U 加系统分析（三分类 + Table）+ §3.1 摘要句。诚实承认 20 个 labels 全部来自 find-non-living-thing。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R29-W2\"\n  summary: \"单一 death mechanism (focus on) 限制 generalizability\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 30\n  resolution: \"R30: Limitations 加 grounding ablation 定量估算 (+26.6pp→~+8pp) + future work。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R29-M1\"\n  summary: \"Missing references: FrugalGPT, AutoMix 等\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 30\n  resolution: \"R29 已添加。R30 确认存在。\"\n  resolution_round: 30\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 31\n  resolution: \"结构性——单一环境 + diagnostic contribution type。Findings 定位合理。\"\n  resolution_round: 30\n  mentions:\n    - round: 31\n      source: \"R2-W3\"\n      note: \"R31 再次标记 contribution type 对 Main Conference 偏弱，两位 Reviewer 共识 3.0 Findings\"\n\n- id: \"R30-W1\"\n  summary: \"'Deterministic' 术语跨环境含义不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 30\n  resolution: \"§2.1 加 umbrella term 括号说明（privileged-information strategy + 三环境 operationalizations）。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R30-W2\"\n  summary: \"Abstract 数字过密，Cohen's d 不适合 abstract\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 30\n  resolution: \"移除 d=3.02，精简至 4 个统计量，168 词。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R30-W3\"\n  summary: \"Grounding ablation 后未重新收集 counterfactual 计算 DAF\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 30\n  last_seen_round: 31\n  resolution: \"DDL 前不可行。Limitations 加定量估算 (+26.6pp→~+8pp) + future work。\"\n  resolution_round: 30\n  mentions:\n    - round: 31\n      source: \"R1-Q5, R2-Q5\"\n      note: \"R31 两位 Reviewer 均追问 grounding ablation 后 DAF 是否仍成立\"\n\n# =============================================\n# R31 新发现\n# =============================================\n\n- id: \"R31-N1\"\n  summary: \"单一主环境 + diagnostic-only 定位限制 Main Conference 级别\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-W1, R2-W1, R2-W3\"\n      note: \"[AGREE x2] 两位 Reviewer 共识：核心实证发现仅在 ScienceWorld 验证，cross-env probes 反证了 generalizability，contribution type 更适合 Findings。映射到历史 R27-N4（环境覆盖过窄）和 R16-N1（novelty deficit），属结构性限制。\"\n\n- id: \"R31-N2\"\n  summary: \"Oracle privilege 使 death avoidance 发现接近 tautology\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-W2\"\n      note: \"Deterministic 策略 = simulator forking（极强 oracle），death avoidance 本质上 = oracle prevents irreversible errors。真正非直觉的洞见是 Δ_nd≈2.84（non-death gap 极小），但论文将此作为 DAF 副产品而非核心发现呈现。映射到历史 R27-N3，R30 已加 umbrella term 和 Δ_nd 讨论，但 R31 fresh reviewer 认为仍不够突出。\"\n\n- id: \"R31-W1\"\n  summary: \"DAF 对 P 的单调依赖需更谨慎处理——headline 应用 label fraction\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-W4, R2-W2\"\n      note: \"[AGREE x2] DAF=δP/(δP+Δ_nd) 随 P 单调递增是数学事实。论文已在 §2.4 承认并以 label fraction 为 primary，但 Abstract/Intro/Conclusion 仍多处突出 DAF=90.4%。建议进一步降低 DAF 在 headline 位置的权重。映射到历史 R27-N2（DAF framing 过度突出），R30 已部分修复。\"\n\n- id: \"R31-W2\"\n  summary: \"K=11 cluster bootstrap 推断——应以非参数检验为主\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-W3\"\n      note: \"论文建议读者依赖非聚类 bootstrap CI 但同时承认 within-cluster correlation 存在——逻辑不自洽。建议将 permutation test / sign test 作为主要推断依据。映射到历史 R13-N2 和 R27-W5，prior rounds resolved 但 fresh reviewer 认为 messaging 仍有改进空间。\"\n\n- id: \"R31-W3\"\n  summary: \"Episode→step 粒度错配限制框架实用性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-W5\"\n      note: \"框架产出 episode-level labels 但 routing 需 step-level 决策。88% uninformative steps。实用价值收窄为 sanity check。映射到历史 R18-N1 和 R28-N1，prior rounds resolved 但 R31 fresh reviewer 认为仍需更明确定位。\"\n\n- id: \"R31-W4\"\n  summary: \"72B probe 缺 cross-model replication at scale\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-W6\"\n      note: \"7-9B 有三个模型族，但 72B 仅 Qwen2.5-72B 一个数据点。Intro 将 72B 与三个模型族并列可能高估 robustness。映射到历史 R28-W1，R30 已降级 'preliminary probe'。\"\n\n- id: \"R31-W5\"\n  summary: \"Appendix 过多（21 个, 15 页）正文依赖过重\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R2-W4\"\n      note: \"核心 claim 的支撑证据分散在 Appendix（K, M, Q, R），读者无法仅通过正文评估贡献。\"\n\n- id: \"R31-W6\"\n  summary: \"Related Work 缺 risk-sensitive RL / CVaR 文献\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R2-W5\"\n      note: \"CVaR optimization（Chow 2015, Tamar 2015）直接处理 trajectory-level catastrophic risk，与 death avoidance 高度相关。§4 未讨论。\"\n\n- id: \"R31-W7\"\n  summary: \"'Counterfactual' 术语使用松散\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R2-W6\"\n      note: \"方法更接近 matched-seed A/B testing 而非 Pearl (2009) structural counterfactual。需要在 §2.1 明确定义。\"\n\n- id: \"R31-W8\"\n  summary: \"Discussion section 过薄（~0.5 page，仅 2 个话题）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R2-W8\"\n      note: \"缺条件分析（when does death avoidance dominate?）和与 concurrent work 的对话。\"\n\n- id: \"R31-M1\"\n  summary: \"Abstract 信息密度仍偏高\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R2-M1\"\n      note: \"前 2 句 6+ 数值。映射到历史 R13-W5（R30 resolved），fresh reviewer 仍感觉偏密。\"\n\n- id: \"R31-M2\"\n  summary: \"Figure 1 配色偏素，Figure 2 axis label 偏小\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R2-M2, Visual Check\"\n      note: \"Figure 1 灰/米色为主缺对比度；Figure 2 legend 约 6-7pt 偏小。\"\n\n- id: \"R31-M3\"\n  summary: \"RTX 5090 硬件可能泄露作者身份\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-M6\"\n      note: \"如果 RTX 5090 尚未公开发售，使用此硬件可能违反 double-blind。\"\n\n- id: \"R31-M4\"\n  summary: \"SCI 在正文仅出现一次，与 Method 中的显著度不匹配\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-M5\"\n      note: \"SCI 列为框架三大组件之一但正文只用了一次。映射到历史 R13-W4（已降级到 Appendix），但 R31 认为 Method §2 中仍 over-prominent。\"\n\n- id: \"R31-M5\"\n  summary: \"Limitations 章节偏长（~1.5 页, 5 段）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-M1\"\n      note: \"内容全部是必要讨论，但对 ARR mandatory limitations 来说偏长。\"\n\n- id: \"R31-M6\"\n  summary: \"Missing references: AgentGym, OSWorld, Trial-and-Error, CVaR\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-R1/R2/R3, R2-R1/R2\"\n      note: \"AgentGym (Xi 2024), OSWorld (Xie 2024), Trial-and-Error (Wang 2024), Chow 2015 CVaR, Tamar 2015 CVaR\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "simgate-modular-routing",
    "issues_yaml": "# Round 31 Review Issues — Fresh review (2 reviewers: R1 方法严谨性+实验设计, R2 新颖性+完整性+写作)\n# R31 is a fresh review; prior rounds' resolved/wont_fix issues carried over unchanged.\n\n# =============================================\n# Carried-over resolved issues (from prior rounds)\n# =============================================\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Wild cluster CI 修正且降级为 sensitivity analysis；non-clustered bootstrap 为主推断\"\n  resolution_round: 24\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 30\n  resolution: \"R30 移除 Cohen's d，精简至 4 个统计量，168 词\"\n  resolution_round: 30\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Ng 1999, Northcutt 2021, DivideMix 已添加\"\n  resolution_round: 24\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 24\n  resolution: \"§5 Non-triviality 段有效回应 novelty 质疑\"\n  resolution_round: 24\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组\"\n  resolution_round: 19\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"Limitations 新增 pure-strategy upper bound 段落\"\n  resolution_round: 24\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"术语全局修正为 text augmentation\"\n  resolution_round: 24\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"P-invariance 适用范围明确量化\"\n  resolution_round: 24\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"4B router 结论 qualified；完整统计处理\"\n  resolution_round: 24\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Router claim 从绝对否定改为有条件否定\"\n  resolution_round: 24\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"措辞软化 + effect size detection threshold 完整报告\"\n  resolution_round: 24\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 non-learnability 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R18-N1 解决\"\n  resolution_round: 24\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"'structurally determined' → 'empirically dominated'\"\n  resolution_round: 24\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 不显著问题\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Per-task 结果标注为 exploratory\"\n  resolution_round: 24\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entries + Webb 年份\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"清理完毕\"\n  resolution_round: 24\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman, Mihatsch, Natarajan\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"所有缺失引用已补充\"\n  resolution_round: 24\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Appendix Overview 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M4\"\n  summary: \"§3.1 术语首次出现未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"术语已修正并定义\"\n  resolution_round: 24\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 agreement 声明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Single annotator caveat 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"§5 已讨论\"\n  resolution_round: 24\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R17-M1 解决\"\n  resolution_round: 24\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"交叉引用指向 §2.1 operationalization\"\n  resolution_round: 24\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"Appendix B 加 circularity caveat\"\n  resolution_round: 24\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 讨论深度不足\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"引用已补全；8 页限制无法展开\"\n  resolution_round: 24\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语歧义\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"修正为 computation modes\"\n  resolution_round: 24\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"§3.1 binary structure 讨论充分\"\n  resolution_round: 24\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"72B decomposition 完整报告\"\n  resolution_round: 24\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"被 R20-N2 取代并解决\"\n  resolution_round: 24\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 未被引用\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"Appendix L 已引用\"\n  resolution_round: 24\n\n- id: \"R19-W1\"\n  summary: \"缺 penalty magnitude 实验验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"P-invariance by design 论证覆盖\"\n  resolution_round: 24\n\n- id: \"R19-N1\"\n  summary: \"Framework vs finding 定位不清\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 27\n  resolution: \"统一为 empirical analysis + reusable diagnostic methodology\"\n  resolution_round: 27\n\n- id: \"R26-N3\"\n  summary: \"Strawman framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 26\n  last_seen_round: 27\n  resolution: \"R27 验收确认修复完好\"\n  resolution_round: 27\n\n- id: \"R28-M2\"\n  summary: \"Pages 7-8 纯文本无 display item\"\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 28\n  last_seen_round: 31\n  resolution: \"8 页限制下无法插入 display item\"\n  resolution_round: 28\n  mentions:\n    - round: 31\n      source: \"Visual Check\"\n      note: \"R31 视觉审查再次标记 pages 7-8 纯文本无 figure/table，建议加 summary bar chart\"\n\n- id: \"R28-M4\"\n  summary: \"Figure 2 仅 11 点无 task name label\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 28\n  last_seen_round: 29\n  resolution: \"Figure 2 已缩至 0.38\\\\textwidth\"\n  resolution_round: 28\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 30\n  resolution: \"R30 确认正文 ≤8 页\"\n  resolution_round: 30\n\n- id: \"R29-N1\"\n  summary: \"正文超出 8 页限制（复发）\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 30\n  resolution: \"R30 确认正文 ≤8 页\"\n  resolution_round: 30\n\n- id: \"R27-N2\"\n  summary: \"DAF=90.4% framing 过度突出\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 30\n  resolution: \"R30: Intro 重构——降低 DAF 权重，突出 oracle degeneracy 96.3%、72B 5 int-pref、Reflexion DAF>100%。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R27-N3\"\n  summary: \"Deterministic strategy 实为 oracle access，跨环境含义不统一\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 30\n  resolution: \"R30: §2.1 加 umbrella term（privileged-information strategy）；Discussion 加 Δ_nd=2.84 oracle privilege 回应 + ALFWorld DAF=0% 对照。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R27-N4\"\n  summary: \"环境覆盖过窄\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 31\n  resolution: \"结构性限制。Limitations/hedging 已到位。Conclusion 加 future work。\"\n  resolution_round: 30\n  mentions:\n    - round: 31\n      source: \"R1-W1, R2-W3\"\n      note: \"R31 fresh review 再次将单一主环境标记为 critical——两位 Reviewer 共识认为需要至少第二个 death-dominated 环境验证\"\n\n- id: \"R27-W1\"\n  summary: \"Router negative result framing\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 30\n  resolution: \"R30: §3.5 title → 'Inconclusive Results'，正文 'inconclusive under current data regime'。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R27-W2\"\n  summary: \"Actionability 有限，Decision Framework 被埋\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 30\n  resolution: \"R30: Discussion 合并 oracle degeneracy 96.3% + Decision Framework 摘要 + action-level filter。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R27-W4\"\n  summary: \"Excluded tasks prescreening 样本量小\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 30\n  resolution: \"Anti-cherry-picking analysis 已到位。全 30 task types 列为 future work。\"\n  resolution_round: 30\n\n- id: \"R27-W5\"\n  summary: \"K=11 cluster bootstrap CI\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 30\n  resolution: \"R2 rebut 有效。论文已自我限定。\"\n  resolution_round: 30\n\n- id: \"R28-N1\"\n  summary: \"Episode-level vs step-level 粒度失配\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R29-R30 均未再提及，prior fix 有效\"\n  resolution_round: 30\n\n- id: \"R28-W1\"\n  summary: \"72B scaling 仅做 probe\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R30: 降级 'preliminary probe' + DAF CI [86.1%, 97.9%] + 修正 5 int-pref (非 0)。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R28-W2\"\n  summary: \"'Death' 术语限制 generality\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R29-R30 均未再提及\"\n  resolution_round: 30\n\n- id: \"R28-M1\"\n  summary: \"Missing references: hallucination detection, early exit\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R30: SelfCheckGPT + Kadavath 2022 + DeeBERT + PABEE 已加入 §4。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R28-M3\"\n  summary: \"Introduction/Discussion/Conclusion 重复度高\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R30: Discussion 压缩 3→2 段去重；Conclusion 扩展含 future work 且无与 Intro 重复。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R28-M5\"\n  summary: \"Related Work 缺 non-agent adaptive computation\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R30: DeeBERT + PABEE early exit positioning 句已加入 §4。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R29-W1\"\n  summary: \"Non-death 21.1% routing signal 来源未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 30\n  resolution: \"R30: Appendix U 加系统分析（三分类 + Table）+ §3.1 摘要句。诚实承认 20 个 labels 全部来自 find-non-living-thing。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R29-W2\"\n  summary: \"单一 death mechanism (focus on) 限制 generalizability\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 30\n  resolution: \"R30: Limitations 加 grounding ablation 定量估算 (+26.6pp→~+8pp) + future work。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R29-M1\"\n  summary: \"Missing references: FrugalGPT, AutoMix 等\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 30\n  resolution: \"R29 已添加。R30 确认存在。\"\n  resolution_round: 30\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 31\n  resolution: \"结构性——单一环境 + diagnostic contribution type。Findings 定位合理。\"\n  resolution_round: 30\n  mentions:\n    - round: 31\n      source: \"R2-W3\"\n      note: \"R31 再次标记 contribution type 对 Main Conference 偏弱，两位 Reviewer 共识 3.0 Findings\"\n\n- id: \"R30-W1\"\n  summary: \"'Deterministic' 术语跨环境含义不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 30\n  resolution: \"§2.1 加 umbrella term 括号说明（privileged-information strategy + 三环境 operationalizations）。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R30-W2\"\n  summary: \"Abstract 数字过密，Cohen's d 不适合 abstract\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 30\n  resolution: \"移除 d=3.02，精简至 4 个统计量，168 词。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R30-W3\"\n  summary: \"Grounding ablation 后未重新收集 counterfactual 计算 DAF\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 30\n  last_seen_round: 31\n  resolution: \"DDL 前不可行。Limitations 加定量估算 (+26.6pp→~+8pp) + future work。\"\n  resolution_round: 30\n  mentions:\n    - round: 31\n      source: \"R1-Q5, R2-Q5\"\n      note: \"R31 两位 Reviewer 均追问 grounding ablation 后 DAF 是否仍成立\"\n\n# =============================================\n# R31 新发现\n# =============================================\n\n- id: \"R31-N1\"\n  summary: \"单一主环境 + diagnostic-only 定位限制 Main Conference 级别\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-W1, R2-W1, R2-W3\"\n      note: \"[AGREE x2] 两位 Reviewer 共识：核心实证发现仅在 ScienceWorld 验证，cross-env probes 反证了 generalizability，contribution type 更适合 Findings。映射到历史 R27-N4（环境覆盖过窄）和 R16-N1（novelty deficit），属结构性限制。\"\n\n- id: \"R31-N2\"\n  summary: \"Oracle privilege 使 death avoidance 发现接近 tautology\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-W2\"\n      note: \"Deterministic 策略 = simulator forking（极强 oracle），death avoidance 本质上 = oracle prevents irreversible errors。真正非直觉的洞见是 Δ_nd≈2.84（non-death gap 极小），但论文将此作为 DAF 副产品而非核心发现呈现。映射到历史 R27-N3，R30 已加 umbrella term 和 Δ_nd 讨论，但 R31 fresh reviewer 认为仍不够突出。\"\n\n- id: \"R31-W1\"\n  summary: \"DAF 对 P 的单调依赖需更谨慎处理——headline 应用 label fraction\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-W4, R2-W2\"\n      note: \"[AGREE x2] DAF=δP/(δP+Δ_nd) 随 P 单调递增是数学事实。论文已在 §2.4 承认并以 label fraction 为 primary，但 Abstract/Intro/Conclusion 仍多处突出 DAF=90.4%。建议进一步降低 DAF 在 headline 位置的权重。映射到历史 R27-N2（DAF framing 过度突出），R30 已部分修复。\"\n\n- id: \"R31-W2\"\n  summary: \"K=11 cluster bootstrap 推断——应以非参数检验为主\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-W3\"\n      note: \"论文建议读者依赖非聚类 bootstrap CI 但同时承认 within-cluster correlation 存在——逻辑不自洽。建议将 permutation test / sign test 作为主要推断依据。映射到历史 R13-N2 和 R27-W5，prior rounds resolved 但 fresh reviewer 认为 messaging 仍有改进空间。\"\n\n- id: \"R31-W3\"\n  summary: \"Episode→step 粒度错配限制框架实用性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-W5\"\n      note: \"框架产出 episode-level labels 但 routing 需 step-level 决策。88% uninformative steps。实用价值收窄为 sanity check。映射到历史 R18-N1 和 R28-N1，prior rounds resolved 但 R31 fresh reviewer 认为仍需更明确定位。\"\n\n- id: \"R31-W4\"\n  summary: \"72B probe 缺 cross-model replication at scale\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-W6\"\n      note: \"7-9B 有三个模型族，但 72B 仅 Qwen2.5-72B 一个数据点。Intro 将 72B 与三个模型族并列可能高估 robustness。映射到历史 R28-W1，R30 已降级 'preliminary probe'。\"\n\n- id: \"R31-W5\"\n  summary: \"Appendix 过多（21 个, 15 页）正文依赖过重\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R2-W4\"\n      note: \"核心 claim 的支撑证据分散在 Appendix（K, M, Q, R），读者无法仅通过正文评估贡献。\"\n\n- id: \"R31-W6\"\n  summary: \"Related Work 缺 risk-sensitive RL / CVaR 文献\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R2-W5\"\n      note: \"CVaR optimization（Chow 2015, Tamar 2015）直接处理 trajectory-level catastrophic risk，与 death avoidance 高度相关。§4 未讨论。\"\n\n- id: \"R31-W7\"\n  summary: \"'Counterfactual' 术语使用松散\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R2-W6\"\n      note: \"方法更接近 matched-seed A/B testing 而非 Pearl (2009) structural counterfactual。需要在 §2.1 明确定义。\"\n\n- id: \"R31-W8\"\n  summary: \"Discussion section 过薄（~0.5 page，仅 2 个话题）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R2-W8\"\n      note: \"缺条件分析（when does death avoidance dominate?）和与 concurrent work 的对话。\"\n\n- id: \"R31-M1\"\n  summary: \"Abstract 信息密度仍偏高\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R2-M1\"\n      note: \"前 2 句 6+ 数值。映射到历史 R13-W5（R30 resolved），fresh reviewer 仍感觉偏密。\"\n\n- id: \"R31-M2\"\n  summary: \"Figure 1 配色偏素，Figure 2 axis label 偏小\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R2-M2, Visual Check\"\n      note: \"Figure 1 灰/米色为主缺对比度；Figure 2 legend 约 6-7pt 偏小。\"\n\n- id: \"R31-M3\"\n  summary: \"RTX 5090 硬件可能泄露作者身份\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-M6\"\n      note: \"如果 RTX 5090 尚未公开发售，使用此硬件可能违反 double-blind。\"\n\n- id: \"R31-M4\"\n  summary: \"SCI 在正文仅出现一次，与 Method 中的显著度不匹配\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-M5\"\n      note: \"SCI 列为框架三大组件之一但正文只用了一次。映射到历史 R13-W4（已降级到 Appendix），但 R31 认为 Method §2 中仍 over-prominent。\"\n\n- id: \"R31-M5\"\n  summary: \"Limitations 章节偏长（~1.5 页, 5 段）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-M1\"\n      note: \"内容全部是必要讨论，但对 ARR mandatory limitations 来说偏长。\"\n\n- id: \"R31-M6\"\n  summary: \"Missing references: AgentGym, OSWorld, Trial-and-Error, CVaR\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - round: 31\n      source: \"R1-R1/R2/R3, R2-R1/R2\"\n      note: \"AgentGym (Xi 2024), OSWorld (Xie 2024), Trial-and-Error (Wang 2024), Chow 2015 CVaR, Tamar 2015 CVaR\""
  }
}
```

</details>

---


### Tool result

_source line 2645 · 2026-05-23T05:33:20.852005+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 24213}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2646 · 2026-05-23T05:35:44.699224+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "simgate-modular-routing",
  "report": "# Round 31 审稿报告\n\n**论文**：Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**目标 Venue**：EMNLP 2026（ARR May cycle, Long Paper）\n**审稿模式**：Fresh（无上轮记忆）\n**Reviewer 编排**：R1（方法严谨性+实验设计）、R2（新颖性+完整性+写作）\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual diagnostic framework，通过在相同初始条件下运行 internal（ReAct）和 deterministic 两种纯策略，将 routing signal 分解为 death-avoidance 和 non-death 两个成分。在 ScienceWorld（11 task types, 245 episodes）中，78.9% 的 non-tie routing labels 和 90.4% 的 performance gap（DAF）源于 death asymmetry，该 pattern 在三个 7-9B 模型族（Qwen/Llama/Gemma）上复现。Cross-environment probes（MATH: DAF=0%, ALFWorld: DAF=0%）显示 routing mechanism 因环境而异。论文定位为 diagnostic contribution。\n\n---\n\n## Strengths\n\n**[S1] 问题定位准确，填补方法论空白**（R1-S1, R2 agree）。现有 routing 工作直接训练 router 而不先诊断信号来源。\"先诊断再建模\" 范式填补了真正的方法论缺口。\n\n**[S2] 统计严谨性远超同 venue 平均水平**（R2-S2, R1-S3）。Episode-level bootstrap (B=10,000)、cluster bootstrap sensitivity (K=11)、wild cluster bootstrap、LOTO sensitivity、per-task CIs、8-seed robustness——这套 robustness pipeline 值得其他 empirical study 参考。\n\n**[S3] 异常诚恳的自我批评**（R1-S3, R2-S3）。论文主动承认了几乎所有潜在问题：K=11 局限、DAF 对 P 的单调依赖、router 结果不确定性、episode-level labeling 的粒度错配。这种透明度在 *ACL 投稿中罕见。\n\n**[S4] 跨模型验证设计合理**（R1-S4）。三个架构差异显著的 7-9B 模型族收敛于 DAF 88-90%（spread 2.2pp），排除了 model-specific artifact。\n\n**[S5] Anti-cherry-picking 分析有说服力**（R1-S5, R2-S4）。Excluded 19 个 task types 的平均 ΔDR (+38.2pp) 高于 included 11 个 (+28.7pp)，与 cherry-picking 假设预测方向相反。\n\n**[S6] 框架简洁可复用**（R1-S2, R2-S1）。DAF 和 labeling function 形式化完整，成功无修改应用于三个不同环境，诊断出三种不同 routing mechanism。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[N1] [critical] 单一主环境 + diagnostic-only 定位限制 Main Conference 级别**（R1-W1, R2-W1, R2-W3 共识）\n核心实证发现（78.9%, DAF=90.4%）完全来自 ScienceWorld 一个环境。MATH 和 ALFWorld 是 boundary probes 而非 death-dominance 验证。ScienceWorld 的 death 机制极为特殊（100% 来自单一 action `focus on`）。Diagnostic framework + single-environment finding 的 contribution type 更适合 Findings 而非 Main Conference。\n\n**[N2] [critical] Oracle privilege 使 death avoidance 发现接近 tautology**（R1-W2, R2 部分同意）\nDeterministic 策略 = simulator forking（极强 oracle privilege）。在此条件下，\"oracle prevents irreversible errors\" → death avoidance 主导 routing signal 在逻辑上是预期的。论文真正非直觉的洞见是 Δ_nd≈2.84（non-death gap 极小，仅占 9.6%），但被框架包装为 DAF 的副产品而非核心发现。论文已在 §2.1 加 umbrella term 和 §5 讨论 Δ_nd，但 fresh reviewer 认为仍需更突出。\n\n### Should-Fix（影响评分）\n\n**[W1] DAF 对 P 单调依赖——headline 应更侧重 label fraction**（R1-W4, R2-W2 共识）\nDAF = δP/(δP + Δ_nd) 随 P 单调递增是数学事实（P=10: 50.4%, P=100: 90.4%, P=500: 97.9%）。论文已在 §2.4 承认并以 label fraction 为 primary，但 Abstract/Intro/Conclusion 多处仍突出 DAF=90.4%。建议进一步降低 DAF 在 headline 位置的权重。\n\n**[W2] K=11 cluster bootstrap 推断——应以非参数检验为主**（R1-W3）\n论文建议读者依赖非聚类 bootstrap CI 但同时承认 within-cluster correlation 存在——逻辑不自洽。Permutation test (p=0.002)、sign test (p<0.001) 和 100% directional consistency 是更可靠的推断依据，应在正文中提升地位。\n\n**[W3] Episode→step 粒度错配限制框架实用性**（R1-W5）\n框架产出 episode-level labels 但 routing 需 step-level 决策。88% uninformative steps。框架实用价值收窄为 \"是否值得尝试 routing\" 的 sanity check，应更明确定位。\n\n**[W4] 72B probe 缺 cross-model replication at scale**（R1-W6）\n7-9B 有三个模型族 replication 但 72B 仅 Qwen2.5-72B。Intro 将两者并列可能高估 scaling robustness。\n\n**[W5] Appendix 过多（21 个, 15 页），核心证据分散**（R2-W4）\nPenalty sensitivity (K)、Decision Framework (R)、Threshold Routing (Q)、cross-model 完整结果 (M) 等核心 claim 支撑在 Appendix。读者无法仅通过正文 8 页评估贡献。\n\n**[W6] Related Work 缺 risk-sensitive RL / CVaR 文献**（R2-W5）\nCVaR optimization (Chow 2015, Tamar 2015) 直接处理 trajectory-level catastrophic risk，与 death avoidance 高度相关但未讨论。\n\n**[W7] \"Counterfactual\" 术语使用松散**（R2-W6）\n方法更接近 matched-seed A/B testing 而非 Pearl (2009) structural counterfactual。需在 §2.1 明确定义。\n\n**[W8] Discussion 过薄（~0.5 page, 2 个话题）**（R2-W8）\n缺少条件分析（when does death avoidance dominate?）和与 concurrent work（MTRouter, CogRouter, BAAR）的对话。\n\n---\n\n## Reviewer Consensus\n\n以下关键问题两位 Reviewer 达成共识：\n\n1. **[AGREE] Overall 3.0 (Findings)**：方法论可靠、分析透彻、自我批评诚恳，但单一主环境 + 预期内发现限制影响力。两位 Reviewer 独立给出相同评分。\n\n2. **[AGREE] 单一环境是核心局限**：缺少第二个 death-dominated 环境验证是接收为 Main Conference 的主要障碍。\n\n3. **[AGREE] DAF=90.4% 作为 headline 需降权**：label fraction (78.9%) 是更 robust 的 primary metric；DAF 随 P 单调递增部分是方法论产物。\n\n4. **[AGREE] 统计严谨性和诚实自评是突出优点**：21 个附录的 robustness analysis 和 \"Inconclusive Results\" 标注在同类工作中罕见。\n\n5. **[AGREE] 框架可复用性是实在贡献**：无修改应用于三个环境并诊断出不同 mechanism，具有方法论价值。\n\n---\n\n## Reviewer Divergence\n\n1. **Oracle privilege / tautology 的严重程度**：R1 将此列为 Must-Fix critical，认为 death avoidance 在 oracle-privileged 设定下接近同义反复；R2 将相关问题分散在 DAF circularity (W2) 和 contribution type (W3) 中，严重程度略低。Director 判断：R1 的分析更深入——如果将 Δ_nd≈2.84 提升为与 death dominance 并列的核心发现，可部分化解 tautology 质疑。\n\n2. **Counterfactual 术语**：R2 认为术语使用松散需修正；R1 未特别关注。Director 判断：这是 writing-level 问题，不影响接收决定，但值得在 revision 中处理。\n\n3. **Router training section 的空间**：R2 认为 \"inconclusive\" 结论占半页不值得；R1 认为负面结果汇报标准高是优点 (S6)。Director 判断：双方都有道理——如果能更深入分析 why routing is hard（而非仅报告 inconclusive），空间使用更合理。\n\n---\n\n## Questions（需要作者澄清）\n\n**[Q1]** （R1-Q1）Algorithm 1 中两个策略都 die 但 timing 不同时，是否有 pre-death partial scores 可利用？为什么不比较 death timing？\n\n**[Q2]** （R1-Q2）Label fraction（78.9%）的 95% CI 是多少？论文多处强调 label fraction 是 primary metric 但未报告其 CI。\n\n**[Q3]** （R1-Q3）Reflexion N=3 时 Δ_nd = -0.47（internal 略优于 deterministic in non-death episodes）是否削弱 \"deterministic 全面优于 internal\" 的叙事？\n\n**[Q4]** （R1-Q5, R2-Q5）Grounding ablation 后重新计算 DAF，death dominance 是否仍成立？如果简单的 action-space filtering 就能大幅削弱 death dominance，\"直接用 deterministic\" 的建议可能不是最佳策略。\n\n**[Q5]** （R2-Q1）如何 disentangle \"death as a cause of routing signal\" vs. \"death as downstream indicator of reasoning quality\"？Appendix N 的 failure categories B 和 D 暗示部分 death 源于 reasoning error 而非 unsafe action。\n\n**[Q6]** （R2-Q3）Frontier models（GPT-4o/Claude 3.5）在 ScienceWorld 上的 death rate 可能大幅降低。是否有 evidence 表明 death avoidance 在 frontier regime 下仍主导？\n\n---\n\n## Missing References\n\n1. **Risk-sensitive RL / CVaR**：Chow et al. (2015), Tamar et al. (2015) — 与 death avoidance 作为 tail-risk avoidance 直接相关（R2-R1/R2）\n2. **AgentGym** (Xi et al., 2024) — 多环境 agent 训练基准含 catastrophic failure 场景（R1-R1）\n3. **OSWorld** (Xie et al., 2024) — 有不可逆操作的 computer agent 环境，潜在的第二个 death-dominated 验证候选（R1-R2）\n4. **Trial-and-Error** (Wang et al., 2024) — LLM agent 在有 catastrophic action 环境中的试错学习，与 death avoidance 分析互补（R1-R3）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目未配置 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warning, 7 info, 0 critical）。主要发现：\n\n- **[warning] Pages 7-8 连续两页纯文本**，无 figure/table/equation 穿插，审稿人后半段会感到视觉单调。建议在 Discussion 加总结性 figure 或 Related Work 加小表格。\n- **[warning] 正文仅 4 个 display items（0.5/页）**，低于实证论文典型 5-8 个。核心分析结果缺可视化支撑，定量结论散落在行内文字中。\n- **[warning] 末页（p25）底部约 40% 空白**，低于 2/3 页面利用建议。\n- **[info] Figure 1 首页无 display item**，第一个视觉锚点在第 2 页。配色偏素（灰/米色），建议增加对比度。\n- **[info] Figure 2 axis label 约 6-7pt**，偏小。\n- **[info] 附录 13 页 vs 正文 8 页**（比例 1.6:1），审稿人可能质疑核心内容被挤出正文。\n- **[info] 无 LaTeX 渲染错误、未解析引用、margin 溢出。排版合规。**\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n两位 Reviewer 独立达成 3.0 共识。论文是一篇方法论扎实、分析透彻、自我批评诚恳的 diagnostic study。核心贡献——episode-level counterfactual diagnostic framework——简洁可复用，在三个环境中成功诊断出不同 routing mechanism。统计严谨性和 robustness analysis（21 个附录）超出同 venue 平均水平。\n\n但论文面临三个结构性限制：(1) 核心实证发现（death dominance）仅在 ScienceWorld 一个主环境验证，cross-env probes 反证了 generalizability；(2) 在 oracle-privileged 的 deterministic 策略下，death avoidance 主导 routing signal 直觉上可预期，真正非直觉的洞见（Δ_nd≈2.84）未被充分突出；(3) episode-level 诊断框架无法直接指导 step-level routing，实用性受限。\n\n**与 3.5 (Borderline Conference) 的差距**：如果论文能 (a) 在至少一个额外 death-dominated 环境验证（如 OSWorld、NetHack），(b) 将 Δ_nd≈0 的洞见提升为核心发现（而非 DAF 副产品），(c) 扩展 Discussion 包含条件分析和 concurrent work 对话，评分可上调。\n\n**格式合规**：正文 ≤8 页 ✅ | ACL template ✅ | Double-blind ✅ | Limitations section ✅（仅讨论，无新实验） | Ethics Statement ✅ | References 格式正确 ✅\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution (2) 将 72B probe 与三个模型族 replication 并列呈现——72B 仅一个模型 (Qwen2.5-72B)，应更明确标注 preliminary 性质\n- \"Death Avoidance as the Dominant Routing Signal\" 标题暗示通用性但 finding 仅在 ScienceWorld 成立\n\n### §2 Method\n- DAF 定义数学上干净（Eq. 3-4），但需在 §2.4 更明确区分 accounting decomposition 和 causal mechanism\n- \"Counterfactual\" 术语：论文引用 Pearl (2009) 但实际方法是 matched-seed strategy comparison，非 structural counterfactual reasoning\n- SCI 列为框架三大组件之一但正文仅用一次（SCI=0.2147），建议降低 Method 中的显著度\n\n### §3 Experiments\n- §3.1 Death Avoidance Decomposition：label fraction (78.9%) 的 CI 应在正文报告（目前只有 DAF CI）\n- §3.3 Agent Improvement Baselines：Reflexion Δ_nd<0 的含义值得在正文讨论——暗示 self-correction 改善了 non-death 表现\n- §3.4 Cross-Environment：作为 boundary probes 的定位是准确的，但 §1 contribution 措辞可能误导读者认为存在跨环境一致性\n- §3.5 Baselines：仅 3 行，作为独立小节不必要——可并入 §3.1\n- §3.6 Router Training：负面结果汇报质量高（S6），但缺乏 why routing is hard 的深入分析。半页 \"inconclusive\" 如果能转化为 actionable insight（如 what minimal signal would need to exist for routing to work）会更有价值\n\n### §4 Related Work\n- 缺 risk-sensitive RL / CVaR 文献（Chow 2015, Tamar 2015）和 catastrophic-failure agent environments（AgentGym, OSWorld, Trial-and-Error）\n- 与 MTRouter (Zhang et al., 2026c, ACL 2026) 的对比可更深入——MTRouter 是否隐式学会了 death avoidance？\n\n### §5 Discussion\n- 仅 ~0.5 page, 2 个话题。建议扩展：(a) 条件分析：在什么条件下 death avoidance 预期会/不会主导？(b) DAF 的 penalty sensitivity 对实际 routing 设计的影响；(c) 与 concurrent work 的 findings 互补关系\n- Δ_nd≈2.84 是真正非直觉的洞见，应在 Discussion 中专段讨论而非仅作为 decomposition 的数值结果\n\n### §6 Conclusion\n- 简洁但可扩展——future work 仅一句，建议具体化（哪些 death-prone environments？step-level extension 的可行路径？）\n\n### Limitations\n- 内容全面、诚实（5 段, ~1.5 页），但对 ARR mandatory limitations 偏长。Pure-strategy upper bound 段落尤其有价值。建议精简至 3 段，将 statistical limitations 的细节移至 Appendix。\n\n### Ethics Statement\n- ⚠️ RTX 5090 硬件：需确认是否已公开发售。如果是特定实验室的早期访问，可能泄露作者身份违反 double-blind。\n\n### Appendix\n- 21 个 appendix (A-U) 共 15 页。内容丰富但正文对 Appendix 依赖过重。建议将 penalty sensitivity (K) 和 Decision Framework (R) 的核心内容移入正文。",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "simgate-modular-routing",
    "report": "# Round 31 审稿报告\n\n**论文**：Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**目标 Venue**：EMNLP 2026（ARR May cycle, Long Paper）\n**审稿模式**：Fresh（无上轮记忆）\n**Reviewer 编排**：R1（方法严谨性+实验设计）、R2（新颖性+完整性+写作）\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual diagnostic framework，通过在相同初始条件下运行 internal（ReAct）和 deterministic 两种纯策略，将 routing signal 分解为 death-avoidance 和 non-death 两个成分。在 ScienceWorld（11 task types, 245 episodes）中，78.9% 的 non-tie routing labels 和 90.4% 的 performance gap（DAF）源于 death asymmetry，该 pattern 在三个 7-9B 模型族（Qwen/Llama/Gemma）上复现。Cross-environment probes（MATH: DAF=0%, ALFWorld: DAF=0%）显示 routing mechanism 因环境而异。论文定位为 diagnostic contribution。\n\n---\n\n## Strengths\n\n**[S1] 问题定位准确，填补方法论空白**（R1-S1, R2 agree）。现有 routing 工作直接训练 router 而不先诊断信号来源。\"先诊断再建模\" 范式填补了真正的方法论缺口。\n\n**[S2] 统计严谨性远超同 venue 平均水平**（R2-S2, R1-S3）。Episode-level bootstrap (B=10,000)、cluster bootstrap sensitivity (K=11)、wild cluster bootstrap、LOTO sensitivity、per-task CIs、8-seed robustness——这套 robustness pipeline 值得其他 empirical study 参考。\n\n**[S3] 异常诚恳的自我批评**（R1-S3, R2-S3）。论文主动承认了几乎所有潜在问题：K=11 局限、DAF 对 P 的单调依赖、router 结果不确定性、episode-level labeling 的粒度错配。这种透明度在 *ACL 投稿中罕见。\n\n**[S4] 跨模型验证设计合理**（R1-S4）。三个架构差异显著的 7-9B 模型族收敛于 DAF 88-90%（spread 2.2pp），排除了 model-specific artifact。\n\n**[S5] Anti-cherry-picking 分析有说服力**（R1-S5, R2-S4）。Excluded 19 个 task types 的平均 ΔDR (+38.2pp) 高于 included 11 个 (+28.7pp)，与 cherry-picking 假设预测方向相反。\n\n**[S6] 框架简洁可复用**（R1-S2, R2-S1）。DAF 和 labeling function 形式化完整，成功无修改应用于三个不同环境，诊断出三种不同 routing mechanism。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[N1] [critical] 单一主环境 + diagnostic-only 定位限制 Main Conference 级别**（R1-W1, R2-W1, R2-W3 共识）\n核心实证发现（78.9%, DAF=90.4%）完全来自 ScienceWorld 一个环境。MATH 和 ALFWorld 是 boundary probes 而非 death-dominance 验证。ScienceWorld 的 death 机制极为特殊（100% 来自单一 action `focus on`）。Diagnostic framework + single-environment finding 的 contribution type 更适合 Findings 而非 Main Conference。\n\n**[N2] [critical] Oracle privilege 使 death avoidance 发现接近 tautology**（R1-W2, R2 部分同意）\nDeterministic 策略 = simulator forking（极强 oracle privilege）。在此条件下，\"oracle prevents irreversible errors\" → death avoidance 主导 routing signal 在逻辑上是预期的。论文真正非直觉的洞见是 Δ_nd≈2.84（non-death gap 极小，仅占 9.6%），但被框架包装为 DAF 的副产品而非核心发现。论文已在 §2.1 加 umbrella term 和 §5 讨论 Δ_nd，但 fresh reviewer 认为仍需更突出。\n\n### Should-Fix（影响评分）\n\n**[W1] DAF 对 P 单调依赖——headline 应更侧重 label fraction**（R1-W4, R2-W2 共识）\nDAF = δP/(δP + Δ_nd) 随 P 单调递增是数学事实（P=10: 50.4%, P=100: 90.4%, P=500: 97.9%）。论文已在 §2.4 承认并以 label fraction 为 primary，但 Abstract/Intro/Conclusion 多处仍突出 DAF=90.4%。建议进一步降低 DAF 在 headline 位置的权重。\n\n**[W2] K=11 cluster bootstrap 推断——应以非参数检验为主**（R1-W3）\n论文建议读者依赖非聚类 bootstrap CI 但同时承认 within-cluster correlation 存在——逻辑不自洽。Permutation test (p=0.002)、sign test (p<0.001) 和 100% directional consistency 是更可靠的推断依据，应在正文中提升地位。\n\n**[W3] Episode→step 粒度错配限制框架实用性**（R1-W5）\n框架产出 episode-level labels 但 routing 需 step-level 决策。88% uninformative steps。框架实用价值收窄为 \"是否值得尝试 routing\" 的 sanity check，应更明确定位。\n\n**[W4] 72B probe 缺 cross-model replication at scale**（R1-W6）\n7-9B 有三个模型族 replication 但 72B 仅 Qwen2.5-72B。Intro 将两者并列可能高估 scaling robustness。\n\n**[W5] Appendix 过多（21 个, 15 页），核心证据分散**（R2-W4）\nPenalty sensitivity (K)、Decision Framework (R)、Threshold Routing (Q)、cross-model 完整结果 (M) 等核心 claim 支撑在 Appendix。读者无法仅通过正文 8 页评估贡献。\n\n**[W6] Related Work 缺 risk-sensitive RL / CVaR 文献**（R2-W5）\nCVaR optimization (Chow 2015, Tamar 2015) 直接处理 trajectory-level catastrophic risk，与 death avoidance 高度相关但未讨论。\n\n**[W7] \"Counterfactual\" 术语使用松散**（R2-W6）\n方法更接近 matched-seed A/B testing 而非 Pearl (2009) structural counterfactual。需在 §2.1 明确定义。\n\n**[W8] Discussion 过薄（~0.5 page, 2 个话题）**（R2-W8）\n缺少条件分析（when does death avoidance dominate?）和与 concurrent work（MTRouter, CogRouter, BAAR）的对话。\n\n---\n\n## Reviewer Consensus\n\n以下关键问题两位 Reviewer 达成共识：\n\n1. **[AGREE] Overall 3.0 (Findings)**：方法论可靠、分析透彻、自我批评诚恳，但单一主环境 + 预期内发现限制影响力。两位 Reviewer 独立给出相同评分。\n\n2. **[AGREE] 单一环境是核心局限**：缺少第二个 death-dominated 环境验证是接收为 Main Conference 的主要障碍。\n\n3. **[AGREE] DAF=90.4% 作为 headline 需降权**：label fraction (78.9%) 是更 robust 的 primary metric；DAF 随 P 单调递增部分是方法论产物。\n\n4. **[AGREE] 统计严谨性和诚实自评是突出优点**：21 个附录的 robustness analysis 和 \"Inconclusive Results\" 标注在同类工作中罕见。\n\n5. **[AGREE] 框架可复用性是实在贡献**：无修改应用于三个环境并诊断出不同 mechanism，具有方法论价值。\n\n---\n\n## Reviewer Divergence\n\n1. **Oracle privilege / tautology 的严重程度**：R1 将此列为 Must-Fix critical，认为 death avoidance 在 oracle-privileged 设定下接近同义反复；R2 将相关问题分散在 DAF circularity (W2) 和 contribution type (W3) 中，严重程度略低。Director 判断：R1 的分析更深入——如果将 Δ_nd≈2.84 提升为与 death dominance 并列的核心发现，可部分化解 tautology 质疑。\n\n2. **Counterfactual 术语**：R2 认为术语使用松散需修正；R1 未特别关注。Director 判断：这是 writing-level 问题，不影响接收决定，但值得在 revision 中处理。\n\n3. **Router training section 的空间**：R2 认为 \"inconclusive\" 结论占半页不值得；R1 认为负面结果汇报标准高是优点 (S6)。Director 判断：双方都有道理——如果能更深入分析 why routing is hard（而非仅报告 inconclusive），空间使用更合理。\n\n---\n\n## Questions（需要作者澄清）\n\n**[Q1]** （R1-Q1）Algorithm 1 中两个策略都 die 但 timing 不同时，是否有 pre-death partial scores 可利用？为什么不比较 death timing？\n\n**[Q2]** （R1-Q2）Label fraction（78.9%）的 95% CI 是多少？论文多处强调 label fraction 是 primary metric 但未报告其 CI。\n\n**[Q3]** （R1-Q3）Reflexion N=3 时 Δ_nd = -0.47（internal 略优于 deterministic in non-death episodes）是否削弱 \"deterministic 全面优于 internal\" 的叙事？\n\n**[Q4]** （R1-Q5, R2-Q5）Grounding ablation 后重新计算 DAF，death dominance 是否仍成立？如果简单的 action-space filtering 就能大幅削弱 death dominance，\"直接用 deterministic\" 的建议可能不是最佳策略。\n\n**[Q5]** （R2-Q1）如何 disentangle \"death as a cause of routing signal\" vs. \"death as downstream indicator of reasoning quality\"？Appendix N 的 failure categories B 和 D 暗示部分 death 源于 reasoning error 而非 unsafe action。\n\n**[Q6]** （R2-Q3）Frontier models（GPT-4o/Claude 3.5）在 ScienceWorld 上的 death rate 可能大幅降低。是否有 evidence 表明 death avoidance 在 frontier regime 下仍主导？\n\n---\n\n## Missing References\n\n1. **Risk-sensitive RL / CVaR**：Chow et al. (2015), Tamar et al. (2015) — 与 death avoidance 作为 tail-risk avoidance 直接相关（R2-R1/R2）\n2. **AgentGym** (Xi et al., 2024) — 多环境 agent 训练基准含 catastrophic failure 场景（R1-R1）\n3. **OSWorld** (Xie et al., 2024) — 有不可逆操作的 computer agent 环境，潜在的第二个 death-dominated 验证候选（R1-R2）\n4. **Trial-and-Error** (Wang et al., 2024) — LLM agent 在有 catastrophic action 环境中的试错学习，与 death avoidance 分析互补（R1-R3）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目未配置 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warning, 7 info, 0 critical）。主要发现：\n\n- **[warning] Pages 7-8 连续两页纯文本**，无 figure/table/equation 穿插，审稿人后半段会感到视觉单调。建议在 Discussion 加总结性 figure 或 Related Work 加小表格。\n- **[warning] 正文仅 4 个 display items（0.5/页）**，低于实证论文典型 5-8 个。核心分析结果缺可视化支撑，定量结论散落在行内文字中。\n- **[warning] 末页（p25）底部约 40% 空白**，低于 2/3 页面利用建议。\n- **[info] Figure 1 首页无 display item**，第一个视觉锚点在第 2 页。配色偏素（灰/米色），建议增加对比度。\n- **[info] Figure 2 axis label 约 6-7pt**，偏小。\n- **[info] 附录 13 页 vs 正文 8 页**（比例 1.6:1），审稿人可能质疑核心内容被挤出正文。\n- **[info] 无 LaTeX 渲染错误、未解析引用、margin 溢出。排版合规。**\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n两位 Reviewer 独立达成 3.0 共识。论文是一篇方法论扎实、分析透彻、自我批评诚恳的 diagnostic study。核心贡献——episode-level counterfactual diagnostic framework——简洁可复用，在三个环境中成功诊断出不同 routing mechanism。统计严谨性和 robustness analysis（21 个附录）超出同 venue 平均水平。\n\n但论文面临三个结构性限制：(1) 核心实证发现（death dominance）仅在 ScienceWorld 一个主环境验证，cross-env probes 反证了 generalizability；(2) 在 oracle-privileged 的 deterministic 策略下，death avoidance 主导 routing signal 直觉上可预期，真正非直觉的洞见（Δ_nd≈2.84）未被充分突出；(3) episode-level 诊断框架无法直接指导 step-level routing，实用性受限。\n\n**与 3.5 (Borderline Conference) 的差距**：如果论文能 (a) 在至少一个额外 death-dominated 环境验证（如 OSWorld、NetHack），(b) 将 Δ_nd≈0 的洞见提升为核心发现（而非 DAF 副产品），(c) 扩展 Discussion 包含条件分析和 concurrent work 对话，评分可上调。\n\n**格式合规**：正文 ≤8 页 ✅ | ACL template ✅ | Double-blind ✅ | Limitations section ✅（仅讨论，无新实验） | Ethics Statement ✅ | References 格式正确 ✅\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution (2) 将 72B probe 与三个模型族 replication 并列呈现——72B 仅一个模型 (Qwen2.5-72B)，应更明确标注 preliminary 性质\n- \"Death Avoidance as the Dominant Routing Signal\" 标题暗示通用性但 finding 仅在 ScienceWorld 成立\n\n### §2 Method\n- DAF 定义数学上干净（Eq. 3-4），但需在 §2.4 更明确区分 accounting decomposition 和 causal mechanism\n- \"Counterfactual\" 术语：论文引用 Pearl (2009) 但实际方法是 matched-seed strategy comparison，非 structural counterfactual reasoning\n- SCI 列为框架三大组件之一但正文仅用一次（SCI=0.2147），建议降低 Method 中的显著度\n\n### §3 Experiments\n- §3.1 Death Avoidance Decomposition：label fraction (78.9%) 的 CI 应在正文报告（目前只有 DAF CI）\n- §3.3 Agent Improvement Baselines：Reflexion Δ_nd<0 的含义值得在正文讨论——暗示 self-correction 改善了 non-death 表现\n- §3.4 Cross-Environment：作为 boundary probes 的定位是准确的，但 §1 contribution 措辞可能误导读者认为存在跨环境一致性\n- §3.5 Baselines：仅 3 行，作为独立小节不必要——可并入 §3.1\n- §3.6 Router Training：负面结果汇报质量高（S6），但缺乏 why routing is hard 的深入分析。半页 \"inconclusive\" 如果能转化为 actionable insight（如 what minimal signal would need to exist for routing to work）会更有价值\n\n### §4 Related Work\n- 缺 risk-sensitive RL / CVaR 文献（Chow 2015, Tamar 2015）和 catastrophic-failure agent environments（AgentGym, OSWorld, Trial-and-Error）\n- 与 MTRouter (Zhang et al., 2026c, ACL 2026) 的对比可更深入——MTRouter 是否隐式学会了 death avoidance？\n\n### §5 Discussion\n- 仅 ~0.5 page, 2 个话题。建议扩展：(a) 条件分析：在什么条件下 death avoidance 预期会/不会主导？(b) DAF 的 penalty sensitivity 对实际 routing 设计的影响；(c) 与 concurrent work 的 findings 互补关系\n- Δ_nd≈2.84 是真正非直觉的洞见，应在 Discussion 中专段讨论而非仅作为 decomposition 的数值结果\n\n### §6 Conclusion\n- 简洁但可扩展——future work 仅一句，建议具体化（哪些 death-prone environments？step-level extension 的可行路径？）\n\n### Limitations\n- 内容全面、诚实（5 段, ~1.5 页），但对 ARR mandatory limitations 偏长。Pure-strategy upper bound 段落尤其有价值。建议精简至 3 段，将 statistical limitations 的细节移至 Appendix。\n\n### Ethics Statement\n- ⚠️ RTX 5090 硬件：需确认是否已公开发售。如果是特定实验室的早期访问，可能泄露作者身份违反 double-blind。\n\n### Appendix\n- 21 个 appendix (A-U) 共 15 页。内容丰富但正文对 Appendix 依赖过重。建议将 penalty sensitivity (K) 和 Decision Framework (R) 的核心内容移入正文。",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.0"
  }
}
```

</details>

---


### Tool result

_source line 2647 · 2026-05-23T05:35:48.715745+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4016
}
```

</details>

---


### Assistant

_source line 2648 · 2026-05-23T05:35:59.758807+00:00_

Round 31 审稿完成。

**结论：Overall 3.0 (Findings)**，两位 Reviewer 独立共识。

核心判断：
- **方法论贡献扎实**：episode-level counterfactual framework 简洁可复用，统计严谨性和自我批评超出同 venue 平均水平
- **三个结构性限制拉低到 Findings**：(1) 核心发现仅 ScienceWorld 一个环境验证；(2) oracle-privileged deterministic 策略下 death avoidance 主导接近预期；(3) episode→step 粒度错配限制实用性
- **升级到 3.5 的路径**：增加第二个 death-dominated 环境验证 + 将 Δ_nd≈0 的非直觉洞见提升为核心发现 + 扩展 Discussion

审稿报告已投递给 Research Director，Issue Tracker 已同步更新（2 critical open, 8 warning open, 6 info open）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 220

## Round 220

2 recorded events


### User

_source line 2649 · 2026-05-23T05:35:59.764338+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix

**[AGREE] R1-W1: 单一主环境限制核心发现说服力**

同意。这与我的 W1（标题/Abstract 过度泛化）和 W3（contribution type 偏弱）高度一致。R1 进一步指出了一个我未明确提到的关键细节：Appendix N 显示 ScienceWorld 中 100% 的 death 来自单一 action pattern（`focus on`），这使得 death mechanism 更加 idiosyncratic——不仅是单一环境，而且是单一 failure mode。这进一步削弱了 "death avoidance as THE dominant routing signal" 这一泛化表述的说服力。

补充：我在 W1 中建议增加 NetHack 或 catastrophic-failure WebArena 作为第二个 death-prone environment。R1 没有给出具体的候选环境建议，但我认为关键需求是：一个 death mechanism 不同于 ScienceWorld 的 `focus on` pattern 的环境（如 health-based death、timeout-based failure、resource depletion），以验证 DAF dominance 不是 ScienceWorld-specific artifact。

---

**[AGREE] R1-W2: Deterministic 策略的 oracle privilege 使发现接近 tautology**

这是 R1 审稿中最有洞察力的一条，与我的 W2（DAF circularity）互补但更精确。

我的 W2 关注的是 DAF metric 本身的 accounting circularity（harsh penalty → mechanically high DAF）。R1 的 W2 更深一层：deterministic 策略使用 simulator forking（§2.1, Algorithm 1），这是一种 oracle-level 的 death avoidance 能力。因此 "deterministic avoids death, internal doesn't" 这个发现在逻辑上接近 tautology——拥有 perfect foresight 的策略当然能避免 catastrophic failure。

R1 正确指出了真正非直觉的发现是 Δ_nd ≈ 2.84（仅占 Δ_full 的 9.6%，§2.4, Eq. 4），即**移除 death 后两种策略性能几乎无差**。这意味着 internal reasoning 的"智慧"并不比 deterministic 的"机械执行"更好——唯一的差距来自 death。论文将此作为 DAF 分解的副产品呈现（§3.1 末尾），而非核心发现，是一个 framing 失误。

建议：论文应将 narrative 重心从 "DAF=90.4%, death dominates"（接近 tautological）转向 "Δ_nd ≈ 0, internal reasoning provides no advantage beyond death avoidance"（genuinely surprising），后者对 routing system design 的启示更深刻。

---

## Should-Fix

**[AGREE] R1-W3: K=11 cluster bootstrap 逻辑不自洽**

同意。论文在 Limitations（page 9, "Statistical limitations" 段落）承认 K=11 < 推荐阈值 K≥20-50（Cameron et al., 2008; Webb, 2023），但建议读者 "rely on the non-clustered bootstrap CI [81.1%, 99.0%]"。正如 R1 所说，这在逻辑上等价于"承认 within-cluster correlation 存在但建议忽略它"。

R1 建议的 permutation test 和 sign test 是合理的补救方向。实际上，论文在 Appendix E 已报告 exact permutation test（p=0.018）和 sign test（p=0.001），但主文仅引用 bootstrap CI。建议将 Appendix E 的 permutation test 结果提升到正文 §3.1 作为主要统计推断工具，bootstrap CI 降级为参考。

---

**[AGREE] R1-W4: DAF 对 penalty magnitude 的单调依赖**

完全同意。这与我的 W2 一致。Appendix K Table 12 清楚显示 DAF 从 P=1 的 14.8% 到 P=500 的 97.9% 单调递增。论文在 Abstract、Introduction、Conclusion 中反复使用 DAF=90.4% 作为 headline number，但这个数值高度依赖 P=100 这一特定 penalty setting。Label fraction（78.9%）不受 penalty magnitude 影响（因为它基于 episode-level preference 而非 score gap 大小），是更 robust 的 metric。

建议与 R1 一致：将 label fraction 78.9% 作为 primary metric，DAF=90.4% 降级为 supplementary measure，并在正文（不仅是 Appendix K）讨论 penalty sensitivity。

---

**[REBUT] R1-W5: Episode-level labeling 到 step-level routing 的粒度错配**

部分反驳。R1 说 "88% 的 step-level training data 是 uninformative" 和 "框架的实用价值收窄为 sanity check"——前半句有事实依据（§3.6 提到 60.3% pre-event neutral + uninformative steps），但后半句的 "sanity check" 评价过于 dismissive。

论文在 §2.3（page 3）和 Limitations（"Methodological constraints" 段落）已明确讨论了 episode-to-step granularity mismatch，并报告了量化数据：2,040 training steps 中仅 0.3% 有 strict directional conflict。问题不是 "direction error" 而是 "uninformative labels applied to neutral steps"——这是 granularity mismatch，不是 labeling error。

更重要的是，论文的 contribution 定位是 diagnostic framework 而非 routing method。Episode-level diagnosis 的价值在于回答 "should we invest in building a router at all?"（Appendix R Decision Framework），而非直接提供 step-level routing decisions。这个定位是合理的——如果 DAF > 75%，practitioner 应该先解决 death avoidance（如 action filtering, §3.3）再考虑 routing，而非直接训练 step-level router。

但我承认 R1 的 concern 有 merit：如果框架只能做 sanity check，那 contribution 确实偏弱。这与我的 W3（contribution type 对 Main Conference 偏弱）一致。

---

**[AGREE] R1-W6: 72B probe 缺少 cross-model replication**

同意。§3.3（Table 1）和 Introduction 将 "scaling to Qwen2.5-72B" 与 "三个 7-9B 模型族 replication" 并列呈现，暗示 scaling result 有类似的 robustness。但 72B 仅有 Qwen2.5-72B 一个模型，没有 Llama-70B 或其他 70B+ 模型的对照。Introduction（page 1）说 "72B scaling... reduces death rates but none closes the gap to deterministic safety" 但这只是单模型观察，不是 replicated finding。

---

## Minor

**[REBUT] R1-M1: Limitations 章节偏长（约 1.5 页）**

部分反驳。按 EMNLP 2026 规则，Limitations 不计入 8 页正文限制，前提是 "不包含 excessive additional content"。论文的 Limitations 有 5 个段落覆盖 5 个不同维度（environmental scope, methodological constraints, statistical limitations, pure-strategy upper bound, diagnostic scope），每段 substantive 且不含新实验/图表。考虑到论文的 diagnostic nature 和 single-environment limitation，详尽的自我评估是适当的——如果压缩可能反而被 reviewer 批评为 "insufficient discussion of limitations"。

但我承认可以更精简：pure-strategy upper bound 和 diagnostic scope 段落可以合并，减少到 3-4 段。

---

**[AGREE] R1-M2: Table 2 Trained Router 单一 seed**

同意。Table 2（page 5）的 Trained Router 行使用 seed 42，而正文 §3.6 描述了 4-8 seed 实验。Table 2 应报告 multi-seed 均值 ± std 以保持一致性。

---

**[AGREE] R1-M3: §2.1 deterministic 策略 oracle strength 差异**

同意。§2.1 列出三种 deterministic 策略（det-pref, int-pref, no-pref）但未明确区分 oracle strength 层级。这与 R1-W2 的 oracle privilege 问题相关——读者需要理解 simulator forking 的 privilege 程度才能判断 death avoidance 发现的 significance。

---

**[AGREE] R1-M4: Appendix N 单一标注者**

同意。Appendix N 的 failure mode taxonomy（5 categories, 105 death episodes）由单一标注者完成，无 inter-annotator agreement 报告。虽然这是 qualitative analysis（辅助性质），但至少应报告 annotation guideline 和 sample re-annotation 以确保一致性。

---

**[AGREE] R1-M5: SCI 在正文仅出现一次**

同意。SCI 在 Method §2（page 2）有显著定义和公式（引用 Appendix A），但在 Results §3 中仅在 §3.1 出现一次（"SCI = 0.21"），之后再未使用。如果 SCI 不是论文的核心 metric，应降低其在 Method 中的 prominence；如果是核心 metric，应在 cross-model 和 cross-environment 结果中也报告 SCI。

---

**[REBUT] R1-M6: RTX 5090 硬件泄露身份**

不同意这是 significant issue。RTX 5090 于 2025 年初发售，截至 2026 年已广泛可购。"4× RTX 6000 PRO (96GB)" 在多个大学和公司实验室中常见。双 GPU 配置（2×5090 + 4×6000 PRO）不足以唯一识别作者身份。ARR 的 double-blind 标准是 "reasonable effort to anonymize"，不要求隐藏硬件配置——多数 EMNLP 论文在 Ethics Statement 中报告 GPU 型号和训练时间。

---

## Questions

**[AGREE] R1-Q1: 两策略都 die 时为什么不比较 pre-death progress？**

好问题。论文将 both-dead episodes 归类为 no_preference（§2.3, Algorithm 1 line 11: "if d_int = 1 and d_det = 1 then ℓ ← no-pref [both dead]"）。但 death timing 不同时，一种策略可能在 die 前取得了更多进度（更多正确 state transitions）。比较 pre-death progress 可以揭示 "即使都会死，哪种策略的 reasoning quality 更高"——这对 step-level routing 有直接指导意义。

不过，ScienceWorld 中 both-dead episodes 数量可能有限。论文应报告 both-dead episode 的数量和 death timing 分布。

---

**[AGREE] R1-Q2: Label fraction 78.9% 的 95% CI 未报告**

同意，这是一个 reporting gap。论文对 DAF 报告了完整的 bootstrap CI（non-clustered [81.1%, 99.0%], clustered [73.3%, 100.0%]），但对 label fraction 78.9% 这一同样核心的 metric 未提供 CI。考虑到 n=95（non-tie episodes），binomial CI 可以直接计算。这是低成本高价值的补充。

---

**[AGREE] R1-Q3: Reflexion N=3 时 Δ_nd < 0 的含义**

好问题。如果 Reflexion N=3 使得 Δ_nd < 0（deterministic 在 non-death episodes 上反而更差），这意味着 Reflexion 的多轮 self-correction 特别提升了 internal 策略在"安全"episodes 中的表现——即 Reflexion 不仅减少了 death（降低 death rate），还改善了 non-death reasoning quality。这个 finding 如果成立，对 Reflexion 的机制理解有价值。论文应在 §3.3 或 Appendix H 中报告 Reflexion 各 N 值的 Δ_nd 分解。

---

**[REBUT] R1-Q4: 4B router 是否应考虑 task-type-aware routing？**

部分反驳。R1 的观察正确：§3.6 最后一段（page 7）和 Appendix I 显示 router 主要学到了 task-type classification 而非 within-task routing。但这恰恰支持了论文的核心论点——routing signal 高度集中于 task-type level（SCI=0.21 表示低集中度，但 Table 3/4 的 per-task analysis 显示 death-prone tasks 有明确的 routing preference，non-death tasks 无 preference）。

Task-type-aware routing 是一个 engineering optimization（给 router 提供 task type feature），不是对论文 diagnostic framework 的质疑。论文的贡献在于解释为什么 routing signal 存在/缺失，而非优化 routing 性能。不过我同意 R1 的隐含批评：如果 task-type identification 就足够 routing，那 episode-level diagnostic framework 的价值进一步收窄。

---

**[AGREE] R1-Q5: Grounding ablation 后重新计算 DAF**

同意这是必要的分析。Appendix O 报告 grounding ablation 将 death rate differential 从 +26.6pp 降低到约 +8pp，但未报告 post-ablation DAF。如果 ablation 后 DAF 仍 > 80%，说明 death avoidance 是 fundamental（与 grounding quality 无关）；如果 DAF 显著下降，说明 death avoidance 部分由 hallucination-induced grounding failure 驱动。这对理解 death avoidance 的 causal mechanism 至关重要——与 R1-W2 的 tautology 问题直接相关。

---

## Missing References

**[REBUT] R1-R1: AgentGym (Xi et al., 2024)**

AgentGym 是 multi-environment agent training platform，提供统一接口。与本文的 diagnostic framework 无直接方法论关联。论文已引用 ScienceWorld、ALFWorld、MATH 的原始环境论文。AgentGym 的价值在于 multi-environment 训练基础设施，但论文的 cross-environment probes 是 diagnostic 性质的（比较 routing signal composition），不是在多个环境上 jointly train router。加入 AgentGym 引用不会改变任何技术讨论。

---

**[REBUT] R1-R2: OS-Copilot / OSWorld (Xie et al., 2024)**

OSWorld 是 OS-level 交互环境。论文的 Related Work §4 "LLM Agent Environments and Reasoning" 已覆盖了代表性的 agent 环境（ScienceWorld, ALFWorld, MATH）。OSWorld 没有与 ScienceWorld 类似的 explicit death mechanism（OS-level tasks 的 failure mode 是 task incomplete 而非 agent death），因此对 death avoidance 讨论的贡献有限。如果论文扩展到更多环境（如 R1-W1 建议），OSWorld 可以作为 non-death-dominated environment 的额外 probe，但作为 related work 引用不是必须的。

---

**[AGREE] R1-R3: Trial-and-Error (Wang et al., 2024)**

同意这是一个有价值的遗漏引用。Trial-and-Error 研究 agent 从 failure 中学习，与论文的 death avoidance 发现直接相关——如果大部分 routing signal 来自 death avoidance，那么 Trial-and-Error 的 failure-driven learning 机制在 death-dominated 环境中可能特别有效（或特别无效，如果 death 是 binary 不可恢复的）。这个 connection 在 §4 "Safe RL and Causal Grounding" 或 §5 Discussion 中值得讨论。

---

## 总结

R1 的审稿意见整体高质量，多数 concerns 与我的独立审查一致。最有价值的贡献是 **W2（oracle privilege → tautology）**，这比我的 W2（DAF circularity）更精确地 pin down 了论文核心发现的 interpretive limitation。

**共识点**（R1 与 R2 一致）：
- 单一环境限制（R1-W1 ≈ R2-W1, R2-W3）
- DAF metric 的局限性（R1-W4 ≈ R2-W2）
- Contribution type 对 Main Conference 偏弱（隐含于 R1-W1/W2/W5 ≈ R2-W3）

**R1 独有的有价值观点**（我未覆盖）：
- W2 的 oracle privilege / tautology 视角
- W3 的 bootstrap 逻辑不自洽
- Q1 关于 both-dead episodes 的 pre-death progress
- Q5 关于 post-ablation DAF

**我不同意 R1 的点**：
- W5 的 "sanity check" 评价过于 dismissive（框架的 diagnostic value 超过 sanity check）
- R1/R2 missing reference（AgentGym、OSWorld 与本文方法论无直接关联）
- M6 的硬件身份泄露（RTX 5090 不足以识别作者）


---

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心共识：R1 和我（R2）在三个关键问题上一致——单一环境限制、DAF metric 局限性、Main Conference contribution 偏弱。R1 的 W2（oracle privilege → tautology）是最有价值的独立观点，比我的 DAF circularity 分析更精确。在 W5（episode-to-step 粒度错配）和 M6（硬件身份泄露）上我持不同意见。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[REBUT] R2-W1: 标题和 Abstract 过度泛化**

R2 认为标题 "Death Avoidance as the Dominant Routing Signal" 暗示通用发现。但标题完整形式包含副标题 "A Counterfactual Analysis on ScienceWorld"，明确限定了实证范围。更关键的是，Abstract 已做了清晰区分：(1) "Applying this framework to ScienceWorld (11 task types, 245 episodes), we find that 78.9%..."——实证发现明确绑定 ScienceWorld；(2) "Cross-environment probes on MATH and ALFWorld diagnose qualitatively different routing mechanisms"——主动展示不同环境有不同机制；(3) "The framework distinguishes methodological generality...from empirical generality (full quantitative validation on ScienceWorld only)"——最后一句直接承认 empirical generality 仅限 ScienceWorld。

标题遵循了 *ACL 常见的 "Phenomenon: Analysis on Environment" 模式（cf. "Language Models as Agent Models" → WebShop specific）。R2 要求加限定词的建议过于保守——读者阅读标题+副标题即可正确理解 scope。MATH 和 ALFWorld 上 DAF=0% 恰恰是论文的 **正面贡献**（框架能诊断不同机制），不是对标题的反驳。

不过，Introduction contribution (2) 中将三个环境并列呈现（"replicated across three 7-9B model families...and cross-environment probes (MATH, ALFWorld)"）确实可能误导读者。**建议作者在 contribution (2) 中更清晰地分层**，但标题本身无需修改。

**[AGREE] R2-W2: DAF 在 harsh-penalty 环境中的 circularity**

同意 DAF 随 P 单调递增是数学性质而非实证发现（§2.4 第4段、Appendix K Table 9 明确展示 DAF 从 P=0 的 7.4% 到 P=500 的 97.9%）。论文的 mitigation 是使用 penalty-independent 的 label fraction（78.9%）作为 primary metric——这一处理是正确的。

但我补充一点 R2 未提及的问题：即使 label fraction 78.9% 是 penalty-independent，它的含义也是 "在 95 个 non-tie episodes 中，75 个涉及 death asymmetry"——这本身就是 death-aware labeling 的直接统计。论文在 Appendix B 证明 Algorithm 1 的 death-first priority 等价于 pure score comparison（因为 P=100 > max partial score），所以没有实际的 circularity。真正的问题是 **DAF=90.4% 的呈现优先级**——我在自己的审稿中已建议将 Abstract/Conclusion 中的 headline 从 DAF 改为 label fraction（我的 W4）。

**[AGREE] R2-W3: Contribution type 对 Main Conference 偏弱**

同意这更适合 Findings。论文的贡献是 (1) 一个概念上直觉的诊断框架（episode-level A/B testing + score gap decomposition）和 (2) 一个 environment-specific 的实证发现。框架本身的方法论创新有限——核心操作是在两个策略下跑 paired episodes 然后分解 score gap，这在实验设计上是标准做法。

但我不同意 R2 将 MTRouter 作为对比标准——ARR reviewer guidelines 明确警告不要因为 "contribution type" 而惩罚分析性论文（Baglini precedent, reviewer guidelines Task 3 item H7: "don't penalize simplicity"）。论文的价值在于它提供了一个 *之前没有人做过的* 诊断视角，即使诊断方法本身并不复杂。复杂度不等于贡献度。

综合来看：Findings 级别合理（我的 Overall 也是 3.0），但理由应是 "单一环境验证 + 预期内发现"，而非 "方法不够复杂"。

---

### Should-Fix

**[REBUT] R2-W4: 21 个 Appendix 过多**

不同意这是 weakness。21 个 Appendix 恰恰反映了论文的thoroughness——这是 R2-W3 所批评的 "empirical finding" 类论文最应具备的品质。正文的核心 claim（78.9% label fraction, DAF=90.4%, cross-model DAF 88-90%, router failure）在正文中都有完整支撑：
- §3.1: death avoidance decomposition 的完整数据
- §3.2: cross-model 的 headline 结果（DAF + CI）
- §3.6: router training 的 key results

Appendix 提供的是 **robustness checks 和 supplementary details**（per-task breakdowns、sensitivity analysis、prompt templates 等），这正是 reviewer 期望看到的。如果作者删减 Appendix，R2 或其他 reviewer 可能反过来批评 "缺少 robustness analysis"。

唯一合理的建议是：Decision Framework（Appendix R）的核心内容可以在 Discussion 中简要呈现，因为它是框架的 practical takeaway。

**[AGREE] R2-W5: 缺少 CVaR-based risk-sensitive RL 文献**

同意。论文 Related Work §Safe RL and Causal Grounding 段落引用了 constrained MDPs（Altman 1999）、risk-sensitive RL（Mihatsch & Neuneier 2002）、safe RL（Garcia & Fernández 2015; Achiam et al. 2017）、shielding（Alshiekh et al. 2018），但缺少 **CVaR-based trajectory optimization**——Chow et al. (2015) 和 Tamar et al. (2015) 直接处理 trajectory-level catastrophic risk 的尾部分布，与论文的 death avoidance 主题高度相关。应在 Safe RL 段落中补充。

**[REBUT] R2-W6: "Counterfactual" 术语使用松散**

不同意。论文使用的 "counterfactual" 严格属于 Rubin potential outcomes framework（Related Work 中明确引用 Rubin 1974）。同一 task instance 在相同 random seed 下运行两个策略，观测 Y(treatment=internal) 和 Y(treatment=deterministic)——这在 causal inference 文献中就是 counterfactual comparison。论文已在 Related Work 中说明 "Our pure-strategy comparison is a simplified instance of the potential outcomes framework (Rubin, 1974), eliminating confounding without structural causal models (Pearl, 2009)"。

R2 的异议似乎假设 "counterfactual" 只能指 Pearl 意义下的 structural counterfactual reasoning（do-calculus, SCM）。但 Rubin potential outcomes 传统使用 "counterfactual" 已有 50+ 年历史，在经济学、流行病学、政策评估中是标准术语。论文的方法——matched-seed paired experiments with controlled assignment——甚至比通常的 "counterfactual" 研究更严格（无 unobserved confounders）。术语使用准确。

**[REBUT] R2-W7: Router Training "inconclusive" 占用空间**

强烈不同意。Router training section（§3.6）是论文最重要的贡献之一：

1. **负面结果本身就是 informative 的**——ARR guidelines 明确说 "don't penalize negative results"（H6）。6 个 router variants 在 3 个 model scales 上收敛于 near-chance accuracy，系统性排除了 capacity（0.6B→4B, Table 8）、data scarcity（25%-800% augmentation, Table 7）、label noise（death-proximal labeling, Appendix P）、task-type leakage（LOTO, Appendix P）。这种系统排查对社区的价值远大于一个 "our router achieves 65% accuracy" 的正面结果——它告诉后续工作者 **何时不应尝试 routing**。

2. R2 说 "没有深入分析为什么 routing 难以学习"——但 §3.6 给出了两个解释框架（Interpretation A: 88% uninformative noise from granularity mismatch; Interpretation B: signal is genuinely task-type-level with no step-level pattern），§5 Discussion §1 进一步分析了 structural mismatch。这不是 "没有分析"，而是分析后发现有两个同样合理的解释无法区分。

**[AGREE] R2-W8: Discussion 过薄**

同意。Discussion（§5）仅约半页，覆盖两个话题。缺少的重要讨论包括：(1) 论文发现对 concurrent routing work（CogRouter、ARES、MTRouter）的启示——这些方法在 death-dominated 环境中是否同样会失败？(2) death avoidance 与 safe RL 中 "constraint satisfaction" 的关系——是否可以用 constrained MDP 框架重新表述 routing 问题？(3) 框架在 non-binary failure（graded penalties）环境中的扩展——Limitations 提到了但 Discussion 没有展开。补充这些内容不需要新实验，但能显著提升论文的 scholarly depth。

---

### Minor

**[AGREE] R2-M1**: Abstract 确实数字偏多（78.9%, 245, 11, 7-9B, 50），但每个数字都有信息量。建议适当精简次要数字。

**[REBUT] R2-M2**: Figure 1 的布局实际上相当清晰——pipeline overview 用三个阶段（collection → labeling → analysis）展示了完整流程。从 PDF page 2 的渲染效果看，可读性没有问题。

**[AGREE] R2-M3**: Table 1 caption 确实过长，可将部分细节移至正文。

**[REBUT] R2-M4**: §3.5 Baselines 作为独立小节是合理的——Table 2 呈现了 5 个策略的对比（Always-Internal, Always-Deterministic, Random, Oracle, Trained Router），这是理解 oracle degeneracy 和 router 性能上界的关键。合并到其他 section 反而会模糊这些重要基线的定位。

---

### Questions

**[AGREE] R2-Q1: Death as cause vs downstream indicator**

这是 R2 提出的最深刻的问题。论文隐式地将 death 视为 routing signal 的 **来源**，但 death 也可能是 internal strategy 推理质量差的 **下游表现**——如果 internal strategy 的推理错误导致 death，那么 "death avoidance" 实际上是 "better reasoning quality" 的代理指标。

论文的 grounding ablation（Appendix O）部分回应了这一点：action-space filtering 将 death rate 从 48% 降到 29%（-19pp），但仍高于 deterministic 的 16.3%。这说明 death 不仅仅是 action-level 错误的结果，还涉及更深层的 trajectory-level reasoning failure（agents 进入需要 `focus on` 的 catastrophic states）。Failure mode analysis（Appendix N）显示 Category B（comprehension without grounding）占主导——agents 正确理解任务但无法将理解映射到 valid action primitives。这暗示 death 是 grounding failure 的下游表现，而非独立的 routing signal source。

作者应在 Discussion 中明确讨论这一 cause-vs-indicator 的区分，并承认框架当前无法区分两者。

**[REBUT] R2-Q2: 将框架应用于 MTRouter**

这个假设性问题的答案是可预测的：MTRouter 的 multi-turn setting 没有 catastrophic failure mechanism，所以 DAF=0%，routing signal 来自其他来源（reasoning depth, model capability tiers）。这恰恰说明论文框架的诊断价值——它能区分 death-dominated 和 non-death settings。但这不构成对论文的批评，因为论文从未声称 death avoidance 在所有 routing settings 中都主导。MATH 的 DAF=0%（§3.4）已经证明了框架在 non-death 环境中的诊断能力。

**[AGREE] R2-Q3: Frontier models 的 death rate**

有效的 concern。72B 的 death rate 从 42.9% 降到 30.6%，但 DAF 反而上升（92.4%），因为 deterministic 的 death rate 也降到 2.75%（§3.3）。趋势外推暗示 frontier models（GPT-4o/Claude）可能将 internal death rate 降到 <10%，此时 death asymmetry 可能不再主导。

但论文无法测试 proprietary models（double-blind + API 成本），且 72B 结果暗示即使 10× scaling 也不消除 death dominance。作者应在 Discussion 中讨论 "capability threshold" 假设：存在一个模型能力阈值，超过后 death rate 趋近零，death dominance 自然消失。Appendix R 的 Decision Framework 隐含了这一点（当 f_death < 50% 时推荐 router investment），但未显式与 scaling 联系。

**[AGREE] R2-Q4: Death penalty = 0 时的 DAF**

论文已回答：Appendix K Table 9 显示 P=0 时 DAF=7.4%，95% CI [-39.4%, 82.5%]——不显著。但 R2 的 deeper question 是：如果 death 仅意味着 early termination（score=0 而非 -100），label fraction 会如何变化？此时 75 个 death-asymmetric episodes 中，many 会变成 "both strategies get low scores" 的 no-preference 或小差异 labels。这将显著降低 label fraction。这进一步支持我在 W4 中的建议：**label fraction 比 DAF 更适合作为 primary metric**，但即使 label fraction 在 P=0 下也会改变（因为 death episodes 的 score gap 取决于 P）。

实际上，label fraction 是 penalty-independent 的——Algorithm 1 的 death-first priority 使用的是 death indicator（d=0 or 1），不依赖 P 的值。所以即使 P=0，只要 "death" 被定义为一个 binary event，78.9% 的 label fraction 不变。这是论文设计的一个重要优势，作者应更明确地强调。

**[AGREE] R2-Q5: Grounding ablation 后 DAF 是否仍高**

论文 Limitations §2 承认 "a full post-ablation counterfactual decomposition remains important future work"。这是一个关键的缺失实验。如果 action-space filtering 后 death rate 降到 29%（vs deterministic 的 16.3%），重新计算 DAF 将取决于新的 Δ_nd。如果 filtering 改善了 non-death performance（因为 agents 不再浪费 steps 在 dangerous actions 上），Δ_nd 可能增加，DAF 可能下降。但如果 filtering 只影响 death rate 而不影响 non-death performance，DAF 可能仍然很高。

这个实验不难做（只需在 filtering 条件下重新收集 paired episodes），作者应在修改稿中补充。

---

### Missing References

**[AGREE] R2-R1, R2-R2**: Chow et al. (2015) CVaR optimization 和 Tamar et al. (2015) CVaR via Sampling 应在 Safe RL 段落补充引用。Death avoidance 本质上是一个 tail-risk 问题，CVaR 文献直接相关。

**[REBUT] R2-R3**: Speculative decoding 已在 Related Work 中引用（"speculative decoding (Leviathan et al., 2023)"），见 Related Work §Adaptive Computation 第3段。R2 可能遗漏了这一引用。

---

### 总结

与 R2 的主要共识：
- DAF 的 P-dependency 是真实问题（R2-W2 ≈ 我的 W4）
- Contribution type 适合 Findings（R2-W3 ≈ 我的 Overall 3.0）
- Discussion 过薄（R2-W8 ≈ 我未单独提出但认同）
- CVaR 文献缺失（R2-W5, R2-R1, R2-R2）

与 R2 的主要分歧：
- **标题不构成 over-generalization**（R2-W1）：副标题和 Abstract 已充分限定 scope
- **21 个 Appendix 是优势而非劣势**（R2-W4）：反映了 thoroughness
- **"Counterfactual" 术语使用准确**（R2-W6）：Rubin potential outcomes 传统
- **Router training section 有重要价值**（R2-W7）：系统性负面结果是高价值贡献
- **Speculative decoding 已被引用**（R2-R3）

整体评估：R2 的审稿在 W1（标题）和 W6（术语）上过于严格，但在 W2（DAF circularity）、W8（Discussion 薄弱）和 Q1（cause vs indicator）上提出了有价值的深层问题。R2-Q1 是两份审稿中最深刻的方法论问题——论文需要在修改稿中明确回应。

---

[Reviewer 1 审稿结果]:
逐条回应已提交给 Review Director。

与 R2 在 6 个点上形成共识（DAF 的 P-dependency、Findings 定位、Discussion 薄弱、CVaR 文献缺失、Q1 cause-vs-indicator、grounding ablation 后缺少 DAF 重算），在 5 个点上提出反驳（标题 scope 已由副标题限定、Appendix 数量反映 thoroughness、"counterfactual" 术语准确属于 Rubin 传统、router negative result 有独立价值、speculative decoding 已被引用）。标注了 R2-Q1（death as cause vs downstream indicator）为两份审稿中最深刻的方法论问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2650 · 2026-05-23T05:36:38.248671+00:00_

交叉回应全部完成。关键共识和分歧已在已提交的审稿报告中覆盖。补充交叉回应中的几个重要细化：

**交叉回应新增共识**：
- R2-Q1（death as cause vs downstream indicator）被 R1 标注为"两份审稿中最深刻的方法论问题"——论文需在 Discussion 中明确回应
- 两位 Reviewer 均同意 grounding ablation 后重新计算 DAF 是低成本高价值的必要实验
- Label fraction 78.9% 的 95% CI 是 reporting gap，应补充

**交叉回应分歧**（记录但不改变评分）：
- **标题 scope**：R2 认为 overclaiming，R1 认为副标题 "on ScienceWorld" 已充分限定——Director 判断：标题本身可接受，但 Introduction contribution (2) 的并列呈现确实需要分层
- **Appendix 数量**：R2 认为过多，R1 认为反映 thoroughness 是优势——Director 判断：Appendix 内容有价值，但 Decision Framework (R) 核心内容应提入正文
- **"Counterfactual" 术语**：R2 认为松散，R1 以 Rubin potential outcomes 传统为由反驳——Director 判断：R1 论据更有说服力，论文已引用 Rubin (1974) 并明确区分
- **Router training section**：R2 认为占空间，R1 认为系统性负面结果是高价值贡献——Director 判断：内容有价值但需更深入分析 why routing is hard

审稿报告已投递，Overall 3.0 (Findings)，Issue Tracker 已同步更新至 Round 31。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 221

## Round 221

2 recorded events


### User

_source line 2651 · 2026-05-23T19:40:27.325573+00:00_

[RESET REQUEST] Research Reviewer 达到硬限
  触发原因：运行时长 16h0m
  本轮累计 24 条消息 / 16h 0min

⚠️ 你自己的 context 状态：已 24 条消息 / 16h 0min

请回复：
  [RESET AGENT]     只重置 Research Reviewer，你继续
  [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛）
  [DEFER Xm]        Xm 后再说
  [DENY <原因>]     不重置，让 Research Reviewer 继续带着上下文工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 2652 · 2026-05-23T19:40:39.104531+00:00_

[RESET BOTH]

Round 31 审稿已完成：报告已投递（Overall 3.0 Findings），Issue Tracker 已更新，视觉审查已纳入。无未完成工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 222

## Round 222

2 recorded events


### User

_source line 2653 · 2026-05-23T19:41:45.714057+00:00_

[SYSTEM] Research Reviewer 刚完成 context rotation (Loop 21)，已读取 handoff 并就绪。如有待办任务请立即分配。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 2654 · 2026-05-23T19:41:51.828418+00:00_

审稿报告已在上一轮完成并投递（Overall 3.0 Findings），无待办任务。Reviewer 无需分配新工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 223

## Round 223

60 recorded events


### User

_source line 2655 · 2026-05-25T21:13:26.047680+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main + Findings (ARR unified)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2656 · 2026-05-25T21:13:31.679193+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2657 · 2026-05-25T21:13:31.730170+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2658 · 2026-05-25T21:13:40.768177+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2659 · 2026-05-25T21:13:40.818938+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2660 · 2026-05-25T21:13:43.425101+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2661 · 2026-05-25T21:13:43.475708+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2662 · 2026-05-25T21:13:46.990043+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_get_project_overview",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_get_project_overview",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2663 · 2026-05-25T21:13:46.990469+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2664 · 2026-05-25T21:13:50.152446+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2665 · 2026-05-25T21:13:50.152913+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2666 · 2026-05-25T21:13:54.699210+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 2667 · 2026-05-25T21:13:56.054750+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (123 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| alfworld-llama-cross-model | Llama-3.1-8B on ALFWorld will show information asymmetry (not death) as the dominant routing mechanism, consistent with Qwen2.5-7B findings (25.9% det-preferred, DAF=0%), confirming the framework diagnoses environment-specific mechanisms regardless of model family. | — | — | — |\n| gemma-scienceworld-cross-model | Gemma-2-9B-it on ScienceWorld will show death dominance (DAF > 80%) consistent with Qwen2.5-7B (90.4%) and Llama-3.1-8B (88.2%), extending the cross-model-family evidence from 2 to 3 independent model families and strengthening the claim that death avoidance dominates routing signal regardless of model architecture. | — | — | — |\n\n## 待处理\n- llama-70b-cross-model: Llama-3.1-70B-Instruct on ScienceWorld will show death dominance (DAF>80%) consistent with Qwen2.5-72B (DAF=92.4%), extending the cross-model scaling evidence from 1 to 2 independent 70B-class model families and upgrading C3 (scaling) from single-model probe to cross-model-at-scale validation.（准备中）\n\n## 近期结论\n- **llama-70b-episodes** (success): Llama-3.1-70B-Instruct-AWQ on ScienceWorld will show dea
…[truncated 1780 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 2668 · 2026-05-25T21:13:56.607381+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2669 · 2026-05-25T21:13:57.009459+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata}  % optional per ACL template; not available in this TeX installation
11	\usepackage{graphicx}
12	\graphicspath{{figures/}}
13	\usepackage{booktabs}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{algorithm}
17	\usepackage{algorithmic}
18	\usepackage{caption}
19	\usepackage{tcolorbox}
20	\tcbuselibrary{listings,breakable}
21	
22	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 2pt}
23	\setlength{\floatsep}{6pt plus 2pt minus 2pt}
24	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
25	
26	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
27	
28	\author{Anonymous}
29	
30	\begin{document}
31	\maketitle
32	
33	\input{abstract}
34	\input{introduction}
35	\input{related_work}
36	\input{method}
37	\input{experiments}
38	\input{discussion}
39	\input{conclusion}
40	
41	\section*{Limitations}
42	Full quantitative validation (DAF, label fractions) is specific to ScienceWorld; MATH and ALFWorld serve as boundary probes, not comprehensive cross-environment validation. DAF depends on a fixed death penalty ($P{=}100$); environments with graded or stochastic failure severity would require extensions (Appendix~\ref{app:penalty}). The internal baseline uses single-pass ReAct~\citep{react-2023}; more aggressive self-correction (e.g., Tree-of-Thought) may further reduce death rates and alter the signal composition. With $K{=}11$ task-type clusters, cluster bootstrap yields wider CIs; wild cluster bootstrap ($p < 0.001$; Appendix~\ref{app:wild-cluster}) and 100\% directional consistency across all 28 death-prone tasks provide partial mitigation. Total compute was approximately 200 GPU-hours on consumer and workstation GPUs.
43	
44	\bibliography{references}
45	
46	\appendix
47	
48	\noindent\textbf{Appendix O
…[truncated 5789 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2670 · 2026-05-25T21:13:57.009830+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 2671 · 2026-05-25T21:14:07.505299+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"}]

I found some relevant information about EMNLP and related conferences for 2026, but the search r
…[truncated 1231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 10495
}
```

</details>

---


### Tool call

_source line 2672 · 2026-05-25T21:14:11.672568+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline page limit"
  }
}
```

</details>

---


### Tool call

_source line 2673 · 2026-05-25T21:14:12.074558+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit anonymity requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit anonymity requirements"
  }
}
```

</details>

---


### Tool result

_source line 2674 · 2026-05-25T21:14:17.408781+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

Based on the search results, here is the information about EMNLP 2026 call for papers:

**Submission Deadline:** The EMNLP 2026 paper submission deadline is May 25, 2026 at 23:59:59 (UTC-12). All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

**Page Limits:** The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Additionally, final versions of accepted papers will be give
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 5736
}
```

</details>

---


### Tool result

_source line 2675 · 2026-05-25T21:14:21.021860+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit anonymity requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"}]

Based on the search results, here's what I found regarding ACL Rolling Review 2026 submission guidelines:

## Page Limit

Papers should follow style guides and not go over the page limit (4 pages for short papers, 8 pages for long papers, excluding ethical considerations and limitations).

## Anonymity Requirements

Papers must not include authors' names and affiliations, and self-references that reveal the autho
…[truncated 1003 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 8947
}
```

</details>

---


### Tool call

_source line 2676 · 2026-05-25T21:14:42.508586+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2677 · 2026-05-25T21:14:42.508958+00:00_

1	\begin{abstract}
2	Adaptive computation routing, deciding when an LLM agent should rely on internal reasoning versus external verification, is a growing focus in agent design, yet the field lacks a principled way to diagnose what signal actually drives routing preferences. Without such diagnosis, practitioners cannot distinguish environments where learned routing adds genuine value from those where a trivial baseline suffices. We introduce an episode-level counterfactual framework that decomposes routing signal into mechanistic components by comparing pure-strategy outcomes before any router is built. Applied to ScienceWorld, the framework reveals that 78.9\% of non-tie routing labels trace to a single mechanism: \emph{death asymmetry}, where internal reasoning triggers catastrophic failure while the deterministic strategy survives. This dominance replicates across three model families (7B--70B); at 70B scale, death avoidance accounts for the entire performance gap. A trivial always-deterministic policy matches 96.3\% of oracle decisions, leaving negligible room for learned routing. Boundary probes on MATH and ALFWorld show the framework distinguishes qualitatively different signal sources, including environments where no routing signal exists\footnote{Code and data are available at \url{https://anonymous.4open.science/r/simgate-modular-routing-ED12/}.}.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2678 · 2026-05-25T21:14:42.659913+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2679 · 2026-05-25T21:14:42.660438+00:00_

1	\section{Introduction}
2	
3	\begin{figure*}[t]
4	\centering
5	\includegraphics[width=0.95\textwidth]{figures/pipeline_overview.pdf}
6	\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\ref{alg:labeling}.}
7	\label{fig:pipeline}
8	\end{figure*}
9	
10	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
11	Existing routing methods, whether inserting API calls by perplexity reduction~\citep{toolformer-2023}, decomposing tasks into tool-augmented programs~\citep{art-2023,chameleon-2023}, or adaptively selecting reasoning depths~\citep{cogrouter-2026,ares-2026} and model tiers~\citep{mtrouter-2026,budget-aware-routing-2026}, share an implicit assumption: that routing signal stems from diverse sources and a learned router can exploit it. But before training a router, we should understand what mechanistic signal drives the routing preference. If signal collapses to a single dominant mechanism, a learned step-level router may not be the right solution.
12	
13	We propose an \emph{episode-level counterfactual diagnostic framework} to address this prior question. The framework compares pure-strategy outcomes (internal-only vs.\ deterministic-only) and introduces the Death Avoidance Factor (DAF) to decompose the routing score gap into death-avoidance and non-death components (\S\ref{sec:collection}--\ref{sec:daf}). Operating at episode granularity is essential: per-step oracle labeling degenerates under sparse terminal rewards (97.4\% tie rate in ScienceWorld; \S\ref{sec:collection}).
14	
15	Applied to ScienceWorld~\citep{scienceworld-2022}, the framework reveals that \textbf{78.9\% of non-tie routing labels arise from death asymmetry}, where the internal strategy triggers a catastrophic failure while the deterministic strategy survives. This pattern re
…[truncated 1468 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2680 · 2026-05-25T21:14:42.710915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2681 · 2026-05-25T21:14:42.761767+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Our diagnostic framework (Figure~\ref{fig:pipeline}) quantifies what drives routing signal in interactive environments through two components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). A supplementary Signal Concentration Index (SCI; Appendix~\ref{app:sci}) measures whether signal is concentrated in a few task types. Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
5	
6	\subsection{Problem Setup}
7	\label{sec:problem-setup}
8	
9	Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\citep{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic} (${\tt det}$), which uses the same LLM to generate candidate actions but evaluates them through privileged environment feedback (ground-truth simulator state in ScienceWorld, code interpreter in MATH, admissible-action enumeration in ALFWorld; see \S\ref{sec:cross-env} for environment-specific operationalizations). Crucially, the deterministic strategy does not provide optimal actions; it reduces observation uncertainty by grounding the LLM's choices in verified environment state rather than predicted state. These qualitative differences affect what routing signals the framework can detect. A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \mathcal{M}$ selects which computation mode to use at each step; our
…[truncated 6428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2682 · 2026-05-25T21:14:47.584312+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2683 · 2026-05-25T21:14:48.086783+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=0.75\columnwidth]{figures/fig1_daf_scatter.pdf}
7	\caption{Per-task death rate differential vs.\ performance gap ($n{=}11$ task types). The near-perfect correlation ($r = 0.97$) is a structural consequence of death dominance (DAF $\to 1 \Rightarrow r \to 1$), not an independent finding. The sole outlier (\texttt{find-non-living-thing}, diamond marker) has zero deaths; its $\Delta_{\text{full}} = +9.58$ arises entirely from non-death score differences.}
8	\label{fig:decomposition}
9	\end{figure}
10	
11	\begin{table}[t]
12	\centering
13	\scriptsize
14	\resizebox{\columnwidth}{!}{%
15	\begin{tabular}{@{}lrr@{}}
16	\toprule
17	Condition & Death\% & $N$ \\
18	\midrule
19	Single-trial baseline & 42.9 & 245 \\
20	Reflexion ($3{\times}$) & 31.4 & 220 \\
21	Qwen2.5-72B ($10{\times}$) & 30.6 & 255 \\
22	Deterministic baseline & 16.3 & 245 \\
23	\midrule
24	\multicolumn{3}{@{}l}{\textit{10 death-prone tasks only:}} \\
25	Death-prone baseline & 48.0 & 200 \\
26	Retry ($5{\times}$) & 43.5 & 200 \\
27	\bottomrule
28	\end{tabular}}
29	\caption{Internal-strategy death rates under improvement methods. Top: all 11 tasks. Bottom: 10 death-prone tasks (\texttt{find-non-living-thing} excluded). No intervention approaches deterministic-level safety.}
30	\label{tab:agent-improvement}
31	\end{table}
32	
33	\begin{figure}[t]
34	\centering
35	\includegraphics[width=0.95\columnwidth]{figures/death_action_timeline.pdf}
36	\vspace{-2mm}
37	\caption{Action sequences for 6 representative death episodes. The fatal \texttt{focus on} (arrow) appears in final steps after long \texttt{connect} sequences (``connect loop $\to$ fatal focus'').}
38	\label{fig:death-timeline}
39	\end{figure}
40	
41	We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performa
…[truncated 12416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2684 · 2026-05-25T21:14:48.087285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2685 · 2026-05-25T21:14:48.489242+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Signal granularity and router failure.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property, but step-level features correlate weakly because death risk depends on multi-step trajectories. Six router variants (0.6B--4B) converge on near-chance balanced accuracy ($56$--$59\%$); leave-one-task-out degrades to $50.0\%$, suggesting the router captures only task-type identity rather than a learnable function of step-level observations. Scaling $10{\times}$ to 70B-class models does not attenuate this pattern (DAF $92$--$101\%$), and cross-model death-rate stability ($31$--$49\%$ across five models) confirms death vulnerability is a task-environment property, better addressed through action-space constraints (Appendix~\ref{app:grounding-ablation}) than learned routing policies.
6	
7	\paragraph{Failure mechanism.}
8	All 105 internal-strategy deaths trace to misuse of \texttt{focus on [object]}, ScienceWorld's answer-submission command, applied to irrelevant targets (rooms, doors, inventory items). The action distribution analysis (Figure~\ref{fig:death-action-dist}, Appendix~\ref{app:failure-modes}) shows that \texttt{focus on} is moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$), while Figure~\ref{fig:death-comparison} reveals that within death episodes both strategies exhibit comparable rates (${\sim}5\%$). The higher internal death count reflects more frequent entry into catastrophic states, not different action selection within those states. Among fatal \texttt{focus on} targets, \texttt{workshop} is the most frequent (20.0\%), followed by \texttt{inventory} (17.1\%) and \texttt{kitchen} (10.5\%), indicating a systematic object bias rather than random exploration. Action-space filtering that blocks \texttt{focus on} during the exploration phase reduces death by 19~pp with zero leaks and zero passthroughs 
…[truncated 2516 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2686 · 2026-05-25T21:14:48.489616+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2687 · 2026-05-25T21:14:48.540171+00:00_

1	\section{Related Work}
2	
3	\begin{figure*}[t]
4	\centering
5	\includegraphics[width=\textwidth]{figures/death_action_comparison.pdf}
6	\vspace{-2mm}
7	\caption{Non-\texttt{connect} action distribution comparison between internal (left) and deterministic (right) strategies within death episodes. Both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not different action selection within those states.}
8	\label{fig:death-comparison}
9	\end{figure*}
10	
11	\paragraph{Tool-Augmented Agents and Adaptive Routing.}
12	Methods for augmenting LLMs with external tools span self-supervised invocation~\citep{toolformer-2023,toolace-2025}, task-level decomposition~\citep{art-2023,chameleon-2023}, and RL-based tool selection~\citep{retool-2025,tool-learning-survey-2024}. Concurrent work examines \emph{when} to invoke tools: \citet{when2tool-2026} analyze accuracy--latency tradeoffs, \citet{tool-use-tax-2026} quantify invocation overhead, and \citet{to-call-or-not-2026,tool-overuse-illusion-2026} investigate overuse patterns. On the routing side, adaptive methods range from learned halting~\citep{graves2016act} and token-level recursion~\citep{mixture-of-recursions-2025} to per-step depth adjustment~\citep{cogrouter-2026,ares-2026} and multi-turn model selection~\citep{mtrouter-2026}. Model-selection routing~\citep{routellm-2024,frugalgpt-2023,automix-2024} optimizes \emph{which} model to invoke based on query difficulty; \citet{budget-aware-routing-2026} train episode-level routing under sparse rewards via counterfactual rollouts, the closest setting to ours, though they focus on learning the router rather than diagnosing what signal it captures. All these approaches presuppose that diverse routing signals exist; our decomposition reveals that in ScienceWorld, a single mechanism accounts for 78.9\% of routing labels.
13	
14	\paragraph{Counterfactua
…[truncated 2295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2688 · 2026-05-25T21:15:04.638168+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2689 · 2026-05-25T21:15:05.090430+00:00_

1	\section{Conclusion}
2	
3	Our episode-level counterfactual framework reveals that routing signal in ScienceWorld is dominated by a single mechanism: 78.9\% of non-tie labels trace to death asymmetry, a finding stable across three model families and two 70B-class models (DAF $92$--$101\%$). When routing signal collapses to catastrophic-failure avoidance, always-deterministic approaches oracle performance, and learned step-level routing offers limited additional value.
4	
5	The framework's diagnostic value extends beyond negative results. The practitioner decision procedure (Table~\ref{tab:decision-validation}) correctly classifies four distinct conditions, and boundary probes demonstrate that the same decomposition identifies qualitatively different signal sources without modification, suggesting utility as a general pre-routing diagnostic.
6	
7	Key open directions include validating death dominance in other catastrophic-failure environments (e.g., safety-critical robotics, irreversible web actions), developing hybrid approaches that combine action-space filtering for death-prone tasks with learned routing for non-death tasks, extending DAF to graded penalties and stochastic failure severity, and investigating whether the concentration of routing signal in a single mechanism generalizes to other agent benchmarks with asymmetric failure modes. More broadly, our results suggest that diagnosing signal composition \emph{before} training a router can save substantial compute by identifying when a simple fixed strategy already captures most of the available signal.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2690 · 2026-05-25T21:15:05.241466+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2691 · 2026-05-25T21:15:05.292117+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'simgate-modular-routing'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2692 · 2026-05-25T21:15:08.907196+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_32/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_32/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2693 · 2026-05-25T21:15:09.711755+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_32/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 2694 · 2026-05-25T21:15:09.812618+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/project_config.yaml 2>/dev/null | head -100",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/project_config.yaml 2>/dev/null | head -100",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2695 · 2026-05-25T21:15:09.913581+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2696 · 2026-05-25T21:15:17.781215+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10",
  "description": "List YAML config files in agent dir"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10",
    "description": "List YAML config files in agent dir"
  }
}
```

</details>

---


### Tool result

_source line 2697 · 2026-05-25T21:15:17.882135+00:00_

find: ‘/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/’: No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2698 · 2026-05-25T21:15:20.392455+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -maxdepth 3 -name \"project_config*\" -o -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -maxdepth 3 -name \"project_config*\" -o -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 2699 · 2026-05-25T21:15:20.443042+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2700 · 2026-05-25T21:15:26.818380+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 2701 · 2026-05-25T21:15:27.222348+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (123 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| alfworld-llama-cross-model | Llama-3.1-8B on ALFWorld will show information asymmetry (not death) as the dominant routing mechanism, consistent with Qwen2.5-7B findings (25.9% det-preferred, DAF=0%), confirming the framework diagnoses environment-specific mechanisms regardless of model family. | — | — | — |\n| gemma-scienceworld-cross-model | Gemma-2-9B-it on ScienceWorld will show death dominance (DAF > 80%) consistent with Qwen2.5-7B (90.4%) and Llama-3.1-8B (88.2%), extending the cross-model-family evidence from 2 to 3 independent model families and strengthening the claim that death avoidance dominates routing signal regardless of model architecture. | — | — | — |\n\n## 待处理\n- llama-70b-cross-model: Llama-3.1-70B-Instruct on ScienceWorld will show death dominance (DAF>80%) consistent with Qwen2.5-72B (DAF=92.4%), extending the cross-model scaling evidence from 1 to 2 independent 70B-class model families and upgrading C3 (scaling) from single-model probe to cross-model-at-scale validation.（准备中）\n\n## 近期结论\n- **llama-70b-episodes** (success): Llama-3.1-70B-Instruct-AWQ on ScienceWorld will show dea
…[truncated 1780 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 2702 · 2026-05-25T21:15:54.619179+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "simgate-modular-routing",
  "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "simgate-modular-routing",
    "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c"
  }
}
```

</details>

---


### Tool call

_source line 2703 · 2026-05-25T21:15:55.071214+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool call

_source line 2704 · 2026-05-25T21:15:55.523236+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
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

_source line 2705 · 2026-05-25T21:15:58.388047+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3768
}
```

</details>

---


### Tool result

_source line 2706 · 2026-05-25T21:15:58.438979+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3367
}
```

</details>

---


### Tool result

_source line 2707 · 2026-05-25T21:15:58.439504+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 2916
}
```

</details>

---


### Tool call

_source line 2708 · 2026-05-25T21:16:07.731202+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2709 · 2026-05-25T21:16:07.832693+00:00_

1	# Round 31 Review Issues — Fresh review (2 reviewers: R1 方法严谨性+实验设计, R2 新颖性+完整性+写作)
2	# R31 is a fresh review; prior rounds' resolved/wont_fix issues carried over unchanged.
3	
4	# =============================================
5	# Carried-over resolved issues (from prior rounds)
6	# =============================================
7	
8	- id: "R13-W1"
9	  summary: "正文篇幅严重不足 long paper 要求"
10	  category: format
11	  severity: warning
12	  status: resolved
13	  first_raised_round: 13
14	  last_seen_round: 14
15	  resolution: "正文已扩展至 8 页"
16	  resolution_round: 14
17	
18	- id: "R13-W2"
19	  summary: "Router 训练实验存在多个 confound"
20	  category: experiment
21	  severity: warning
22	  status: resolved
23	  first_raised_round: 13
24	  last_seen_round: 15
25	  resolution: "1.7B dip 有可检验假说，augmentation 术语修正，N 统一"
26	  resolution_round: 15
27	
28	- id: "R13-W3"
29	  summary: "Episode-level label → step-level training 的 mislabeling 未被量化"
30	  category: method
31	  severity: info
32	  status: resolved
33	  first_raised_round: 13
34	  last_seen_round: 14
35	  resolution: "Limitations 和 Appendix B 已充分量化"
36	  resolution_round: 14
37	
38	- id: "R13-W4"
39	  summary: "SCI 方法贡献与实际使用不成比例"
40	  category: method
41	  severity: info
42	  status: resolved
43	  first_raised_round: 13
44	  last_seen_round: 14
45	  resolution: "SCI 已降级到 Appendix A"
46	  resolution_round: 14
47	
48	- id: "R13-W7"
49	  summary: "Router negative results 解释不完整"
50	  category: experiment
51	  severity: warning
52	  status: resolved
53	  first_raised_round: 13
54	  last_seen_round: 15
55	  resolution: "Router 实验定位为 diagnostic probe"
56	  resolution_round: 15
57	
58	- id: "R13-m2"
59	  summary: "Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld"
60	  category: writing
61	  severity: warning
62	  status: resolved
63	  first_raised_round: 13
64	  last_seen_round: 16
65	  resolution: "Figure 3 已移除，数据在 Table 2 和正文中完整呈现"
66	  resolution_round: 16
67	
68	- id: "R13-m3"
69	  summary: "Reference 格式不统一 + orphan entries"
70	  category
…[truncated 25857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2710 · 2026-05-25T21:16:57.930275+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）\n\n### 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **论文路径**: `projects/simgate-modular-routing/docs/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_32/submitted.pdf`\n\n### 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，long paper 正文 8 页限制（不含 references、limitations、ethical considerations）\n- **匿名**: double-blind（论文不得包含作者信息，self-reference 需匿名化）\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查侧重：方法严谨性 + 实验有效性\n\n重点评估以下方面：\n\n1. **方法论**:\n   - DAF（Death Avoidance Factor）公式的推导是否严谨？分解假设是否成立？\n   - Episode-level counterfactual labeling 的设计是否合理？是否存在 circularity？\n   - DAF 对 penalty P 的单调依赖——论文如何处理这一问题？是否充分？\n   - \"Counterfactual\" 术语的使用是否与因果推断文献一致？\n\n2. **统计检验**:\n   - Bootstrap CI 的使用是否恰当？K=11 cluster 下的推断可靠性如何？\n   - 样本量（245 episodes, per-task n=20-40）是否足够支撑结论？\n   - 多重比较问题是否被处理？\n   - Cross-model 一致性的统计意义如何评估？\n\n3. **实验设计**:\n   - 11/30 task types 选择是否引入 selection bias？Anti-cherry-picking analysis 是否充分？\n   - Deterministic strategy 的 oracle privilege 是否使 death avoidance finding 接近 tautology？\n   - Cross-environment probes（MATH, ALFWorld）的深度和覆盖是否足够？\n   - Agent improvement baselines（Retry, Reflexion, 72B scaling）的设计是否公平？\n   - Router training 的 negative result 是否被充分论证？\n\n4. **格式合规**:\n   - 正文是否在 8 页限制内？\n   - 匿名是否合规（无作者信息、无去匿名化线索）？\n   - Limitations section 是否存在？\n\n请按 Strengths / Weaknesses / Questions / Missing References / Overall Assessment 结构输出审稿意见。每个 Weakness 标注严重程度（critical / warning / info）。给出 Overall Assessment 评分（用 EMNLP 2026 ARR 标准）和置信度（1-5）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "simgate-modular-routing",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）\n\n### 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **论文路径**: `projects/simgate-modular-routing/docs/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_32/submitted.pdf`\n\n### 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，long paper 正文 8 页限制（不含 references、limitations、ethical considerations）\n- **匿名**: double-blind（论文不得包含作者信息，self-reference 需匿名化）\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查侧重：方法严谨性 + 实验有效性\n\n重点评估以下方面：\n\n1. **方法论**:\n   - DAF（Death Avoidance Factor）公式的推导是否严谨？分解假设是否成立？\n   - Episode-level counterfactual labeling 的设计是否合理？是否存在 circularity？\n   - DAF 对 penalty P 的单调依赖——论文如何处理这一问题？是否充分？\n   - \"Counterfactual\" 术语的使用是否与因果推断文献一致？\n\n2. **统计检验**:\n   - Bootstrap CI 的使用是否恰当？K=11 cluster 下的推断可靠性如何？\n   - 样本量（245 episodes, per-task n=20-40）是否足够支撑结论？\n   - 多重比较问题是否被处理？\n   - Cross-model 一致性的统计意义如何评估？\n\n3. **实验设计**:\n   - 11/30 task types 选择是否引入 selection bias？Anti-cherry-picking analysis 是否充分？\n   - Deterministic strategy 的 oracle privilege 是否使 death avoidance finding 接近 tautology？\n   - Cross-environment probes（MATH, ALFWorld）的深度和覆盖是否足够？\n   - Agent improvement baselines（Retry, Reflexion, 72B scaling）的设计是否公平？\n   - Router training 的 negative result 是否被充分论证？\n\n4. **格式合规**:\n   - 正文是否在 8 页限制内？\n   - 匿名是否合规（无作者信息、无去匿名化线索）？\n   - Limitations section 是否存在？\n\n请按 Strengths / Weaknesses / Questions / Missing References / Overall Assessment 结构输出审稿意见。每个 Weakness 标注严重程度（critical / warning / info）。给出 Overall Assessment 评分（用 EMNLP 2026 ARR 标准）和置信度（1-5）。"
  }
}
```

</details>

---


### Tool result

_source line 2711 · 2026-05-25T21:17:15.784900+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17854
}
```

</details>

---


### Tool call

_source line 2712 · 2026-05-25T21:17:15.885603+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **论文路径**: `projects/simgate-modular-routing/docs/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_32/submitted.pdf`\n\n### 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，long paper 正文 8 页限制（不含 references、limitations、ethical considerations）\n- **匿名**: double-blind（论文不得包含作者信息，self-reference 需匿名化）\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查侧重：新颖性 + 完整性 + 写作质量\n\n重点评估以下方面：\n\n1. **新颖性与贡献定位**:\n   - 论文的核心贡献（counterfactual diagnostic framework + death dominance finding）对 EMNLP 社区的价值如何？\n   - 这是 Conference 级别还是 Findings 级别的贡献？\n   - 核心发现（death avoidance dominates routing）是否存在 triviality 风险——给定 deterministic strategy 有 oracle access，这个结论是否不够非直觉？\n   - 与 concurrent work（CogRouter, ARES, MTRouter, Budget-Aware Routing）的差异化定位是否清晰？\n\n2. **Related Work 覆盖**:\n   - Tool-augmented agents、adaptive routing、counterfactual methods、safe RL 四个方向的覆盖是否全面？\n   - 是否遗漏重要的相关工作？特别关注：risk-sensitive RL / CVaR optimization、agent safety evaluation、early exit / adaptive computation\n   - 与最近的 agent routing 工作的对比是否充分？\n\n3. **写作质量**:\n   - Abstract 是否在 200 词以内？信息密度是否合理？\n   - Introduction 的叙事逻辑是否清晰？是否有效建立了研究动机？\n   - Discussion 的深度是否足够？是否讨论了核心发现的条件和边界？\n   - 各章节之间是否有重复内容？\n   - 术语使用是否一致（特别是 \"counterfactual\"、\"deterministic\"、\"computation mode\" 等关键术语）？\n\n4. **论证完整性**:\n   - 核心 claim 是否在正文中得到充分支撑，还是过度依赖 Appendix？\n   - Appendix 数量和正文-Appendix 信息分配是否合理？\n   - Limitations section 是否存在且覆盖关键局限？是否符合 EMNLP 2026 要求（mandatory, 放在正文中，只需要覆盖 3 个点左右，不需要过长）？\n   - Conclusion 是否恰当总结贡献且不过度 claim？\n\n请按 Strengths / Weaknesses / Questions / Missing References / Overall Assessment 结构输出审稿意见。每个 Weakness 标注严重程度（critical / warning / info）。给出 Overall Assessment 评分（用 EMNLP 2026 ARR 标准）和置信度（1-5）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "simgate-modular-routing",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **论文路径**: `projects/simgate-modular-routing/docs/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_32/submitted.pdf`\n\n### 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，long paper 正文 8 页限制（不含 references、limitations、ethical considerations）\n- **匿名**: double-blind（论文不得包含作者信息，self-reference 需匿名化）\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查侧重：新颖性 + 完整性 + 写作质量\n\n重点评估以下方面：\n\n1. **新颖性与贡献定位**:\n   - 论文的核心贡献（counterfactual diagnostic framework + death dominance finding）对 EMNLP 社区的价值如何？\n   - 这是 Conference 级别还是 Findings 级别的贡献？\n   - 核心发现（death avoidance dominates routing）是否存在 triviality 风险——给定 deterministic strategy 有 oracle access，这个结论是否不够非直觉？\n   - 与 concurrent work（CogRouter, ARES, MTRouter, Budget-Aware Routing）的差异化定位是否清晰？\n\n2. **Related Work 覆盖**:\n   - Tool-augmented agents、adaptive routing、counterfactual methods、safe RL 四个方向的覆盖是否全面？\n   - 是否遗漏重要的相关工作？特别关注：risk-sensitive RL / CVaR optimization、agent safety evaluation、early exit / adaptive computation\n   - 与最近的 agent routing 工作的对比是否充分？\n\n3. **写作质量**:\n   - Abstract 是否在 200 词以内？信息密度是否合理？\n   - Introduction 的叙事逻辑是否清晰？是否有效建立了研究动机？\n   - Discussion 的深度是否足够？是否讨论了核心发现的条件和边界？\n   - 各章节之间是否有重复内容？\n   - 术语使用是否一致（特别是 \"counterfactual\"、\"deterministic\"、\"computation mode\" 等关键术语）？\n\n4. **论证完整性**:\n   - 核心 claim 是否在正文中得到充分支撑，还是过度依赖 Appendix？\n   - Appendix 数量和正文-Appendix 信息分配是否合理？\n   - Limitations section 是否存在且覆盖关键局限？是否符合 EMNLP 2026 要求（mandatory, 放在正文中，只需要覆盖 3 个点左右，不需要过长）？\n   - Conclusion 是否恰当总结贡献且不过度 claim？\n\n请按 Strengths / Weaknesses / Questions / Missing References / Overall Assessment 结构输出审稿意见。每个 Weakness 标注严重程度（critical / warning / info）。给出 Overall Assessment 评分（用 EMNLP 2026 ARR 标准）和置信度（1-5）。"
  }
}
```

</details>

---


### Tool result

_source line 2713 · 2026-05-25T21:17:17.196471+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1310
}
```

</details>

---


### Assistant

_source line 2714 · 2026-05-25T21:17:30.219449+00:00_

Round 1 审稿任务已分配：

| Reviewer | 侧重 | 状态 |
|----------|------|------|
| R1 | 方法严谨性 + 实验有效性 | 审稿中 |
| R2 | 新颖性 + 完整性 + 写作质量 | 审稿中 |
| 视觉审查 | 排版质量（非评分项） | 运行中 |
| 外部审稿 | 未配置 | N/A |

等待两位 Reviewer 返回独立审稿意见，收齐后进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 224

## Round 224

2 recorded events


### User

_source line 2715 · 2026-05-25T21:23:11.756299+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**审查侧重**: 新颖性 + 完整性 + 写作质量

---

## 总体评分
**Overall**: 3.0 — Findings（可被 Findings 接收）
**Confidence**: 4/5
**一句话总结**: 框架设计严谨、实验细致，但核心发现（death dominance）存在显著的 triviality 风险——在 deterministic strategy 拥有特权环境访问的设定下，该发现接近结构性必然而非深层洞见，贡献量级更适合 Findings 而非 Main Conference。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 方法论严谨，统计检验充分（bootstrap CI、leave-one-out、Spearman rank），paired counterfactual 设计控制了随机种子，消除了混杂变量。22个附录节体现了极高的自我验证标准。 |
| Excitement | 2/5 | 核心发现的 non-triviality 不充分。Deterministic strategy 拥有 privileged env feedback（Section 3.1），internal strategy 依赖 LLM 推理。在这种不对称信息访问下，death avoidance 主导路由信号接近于一个结构性推论而非反直觉发现。Cross-environment probes 有价值但太初步（MATH 和 ALFWorld 各只有一段分析）。 |
| Reproducibility | 4/5 | 代码通过 anonymous.4open.science 提供（footnote 1），超参数完整（Table 11），seed robustness 有验证（Appendix J）。Agent prompt templates 完整提供（Appendix T）。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心发现的 Triviality 风险未充分回应
- 具体位置：Section 3.4（DAF 定义）、Section 4.1（核心发现）、Section 5（Discussion）
- 问题：Deterministic strategy 具有 "privileged env feedback"（Section 3.1），能直接观察环境状态并通过模拟评估候选动作。Internal strategy 仅依赖 LLM chain-of-thought。在这种**根本性的信息不对称**下：(a) internal 策略更容易因幻觉/状态跟踪丢失而死亡；(b) deterministic 策略因 oracle-like access 而天然更安全。因此 death asymmetry 主导路由信号（78.9% 的 non-tie labels）在很大程度上是实验设计的结构性后果，而非关于 routing 本质的深层发现。
- 论文在 Section 3.4 承认 DAF 随 P 单调增加（DAF at P=0 为 0，P=100 时为 90.4%），但未充分讨论这意味着 "death dominance" 部分是惩罚参数的函数而非环境的内在属性。Appendix K 的 penalty sensitivity 分析虽然存在，但核心论证不应将 P=100 下的 DAF 直接等同于 "routing signal is death-dominated"，而应讨论在什么 P 范围内该结论成立。
- 为什么影响接收：如果核心 finding 可以从实验设计的结构性质先验推导，论文的贡献降级为"用框架验证了一个预期结论"，而非"揭示了一个新发现"。
- 建议修改方向：(1) 在 Discussion 中正面论证为什么该发现不是 trivial——例如，是否存在先验理由预期 non-death signal 也很强？(2) 增加一个 death penalty 不为固定值的环境（graded failure）的分析，展示框架在 DAF 不极端时的诊断价值。(3) 更谨慎地 frame contribution——从 "we discover death dominance" 转向 "we provide a framework that can quantify death dominance, and ScienceWorld happens to be death-dominated"。

**N2** [critical] Cross-Environment Probes 过于初步，无法支撑泛化性 Claim
- 具体位置：Section 4.4、Table 5、Figure 6
- 问题：论文在 Abstract 和 Introduction 中暗示框架具有跨环境泛化性（"Boundary probes on MATH and ALFWorld show the framework distinguishes qualitatively different signal sources"），但 MATH 分析仅基于 N=705 道题的 label 分布（Table 5），ALFWorld 仅 135 个游戏（Section 4.4），且两者都只报告了 label 分布而未做与 ScienceWorld 同等深度的分解分析（无 DAF 计算、无 per-task decomposition、无 robustness check）。
- MATH 的结论（"no routing signal"）来自 near-identical accuracy（73.5% vs 73.0%，Table 5），但未验证这是否因为 deterministic strategy 在 MATH 上定义不当（MATH 没有真正的"环境交互"），导致两种策略实际上近似等价。
- 为什么影响接收：Cross-environment probes 是论文第三个贡献点（"(3) Boundary probes"），但分析深度远不及 ScienceWorld，使这一贡献点显得单薄。
- 建议修改方向：(1) 对 ALFWorld 做完整的 DAF 分解和 per-task analysis（不仅是 label 分布）；(2) 讨论 MATH 的 deterministic strategy 设计是否合理，或明确承认 MATH probe 的局限性；(3) 降低 abstract/intro 中对泛化性的 claim 强度。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 附录体量异常，正文-附录信息分配需重新审视
- 具体位置：Appendix A-V（22个小节，14页）
- 问题：正文 8 页 + 附录 14 页，附录几乎是正文的两倍。部分关键分析被放入附录而正文仅一句引用：例如 Appendix K（penalty sensitivity）直接关系到 DAF 的解读，Appendix N（failure mode analysis）包含了理解 death mechanism 的关键定性分析，Appendix O（grounding ablation）直接回应了 "death dominance 是否可干预" 这一重要问题。
- 22 个附录节的存在给人一种"用细节量弥补核心贡献厚度"的印象。
- 建议：将 penalty sensitivity（K）、failure mode analysis（N）的核心结果提炼到正文 Discussion；将纯验证性的附录（D、E、F、G）合并精简。

**W2** [warning] 与 Concurrent Work 的差异化定位不够锐利
- 具体位置：Section 2（Related Work, paragraph 1）
- 问题：论文列举了 CogRouter、ARES、MTRouter、Budget-Aware Routing 等 concurrent work，但仅用一句话（"All these approaches presuppose that diverse routing signals exist"）概括差异。未逐一对比这些工作的核心假设与本文框架的区别。例如：RouteLLM（Section 2 引用）做的是 cost-quality tradeoff，本文做的是 mechanistic decomposition，二者的出发点和适用场景有何不同？这种差异化不清晰会让 reviewer 质疑贡献的独特性。
- 建议：增加一段 2-3 句的直接对比，说明本文框架与 routing optimization 工作在目标层面的本质差异（诊断 vs 优化）。

**W3** [warning] "Counterfactual" 术语的使用范围可进一步澄清
- 具体位置：Title、Abstract、Section 3
- 问题：论文标题用 "Counterfactual Analysis"，但框架本质上是一个 **paired controlled comparison**（同一任务实例、同一种子、不同策略）。在因果推断文献中，"counterfactual" 通常指单个单位在未实际接受的处理下的潜在结果（Rubin, 1974，论文已引用）。论文的设计更接近 randomized paired experiment。虽然用法不算错误（确实是 "what would have happened under the other strategy"），但正文未明确将自己的框架定位于 potential outcomes framework 的哪个位置，可能引起因果推断领域 reviewer 的疑虑。
- 建议：在 Section 3 开头或 footnote 中简要说明 "counterfactual" 在本文的具体含义及其与 Rubin causal model 的关系。

**W4** [warning] Router Training 实验（Section 4.6）结论跳跃
- 具体位置：Section 4.6、Appendix I
- 问题：Section 4.6 训练了一个 LoRA router 并发现 step-level balanced accuracy 为 56-59%（接近随机），episode-level evaluation 为 41.7 ± 2.25。论文据此结论 "this negative result is consistent with the death-dominance finding"。但这个推理有跳跃：router 表现差可能有多种原因（特征不够好、训练数据不足、模型容量不够），不能直接归因于 "death dominance makes routing unlearnable"。论文需要排除这些替代解释。
- 建议：增加一个控制实验——例如给 router 提供 death risk 作为额外特征，看是否能显著提升 routing 准确率。如果 death risk 特征足以让 router 达到高准确率，则进一步支持 death-dominance 的结论。

---

## 小问题（不影响接收）

- **Figure 1 可读性**：框架图信息密度高但字体偏小，右侧 "Death Avoidance Factor" 子图的 78.9% 标注与正文 DAF=90.4% 的关系未在图注中说明（一个是 label fraction，一个是 score fraction），可能引起混淆。
- **Table 2 的 D/I1/N 列**：列标题含义不够直观（Death-preferred / Internal-preferred / No-preference），建议在表注中简要定义。
- **Section 4.3 Agent Improvement Baselines**：Retry (N=5) 和 Reflexion (3×) 的实验仅报告 death rate 变化（Table 1），未报告这些 intervention 对 DAF 本身的影响——如果 Retry 降低了 death rate 但 DAF 保持高位，这会是一个更强的论证点。
- **Appendix V (Use of AI Assistants)**：声明使用了 Claude 作为 coding and writing assistant，符合 EMNLP 2026 要求。

---

## Missing References

论文的 Related Work（Section 2）在四个方向上的覆盖总体合理，但以下几个方向存在缺口：

1. **Risk-sensitive RL / CVaR optimization**：论文的核心发现是 death avoidance 主导 routing——这与 risk-sensitive RL 中的 CVaR (Conditional Value at Risk) optimization 直接相关。Tamar et al. (2015, "Policy Gradient for Coherent Risk Measures") 和 Dabney et al. (2018, "Implicit Quantile Networks") 提供了在决策中量化和优化 tail risk 的框架，与 death-avoidance routing 有直接理论联系。当前 Related Work 仅引用了 Garcia & Fernández (2015) 的 safe RL survey，未涉及 risk-sensitive RL 的具体方法。
2. **Adaptive computation / early exit**：论文引用了 Graves (2016) 和 mixture-of-recursions，但未引用 Adaptive Computation Time (ACT, Graves 2016 NIPS) 的后续工作，特别是 Universal Transformers (Dehghani et al., 2019) 和 CALM (Schuster et al., 2022)，这些工作在 "何时停止计算" 的决策上与 routing 有结构相似性。
3. **Agent failure taxonomy**：论文的 failure mode analysis（Appendix N）定义了 4 类错误（hallucination-induced、task-aware but lacking action grounding、action-selection quality、primitive dominance），但未引用近期的 agent failure taxonomy 工作，例如 Kambhampati et al. (2024) 或 Valmeekam et al. (2023) 关于 LLM planning failure 的分类研究。

---

## 主要优势

1. **框架设计简洁而有力**：DAF 的定义（Section 3.4）通过 score gap 分解将复杂的 routing 诊断问题转化为可计算的指标，数学表达清晰，物理含义直观。Episode-level labeling algorithm（Algorithm 1）的设计合理——先检查 death asymmetry，再比较 score，最后处理 tie。
2. **统计验证极其充分**：Bootstrap CI（Appendix E）、leave-one-out（Appendix G）、seed robustness（Appendix J）、correlation robustness（Appendix D）——每一个可能的统计质疑都有预先准备的回应。Spearman rank correlation ρ=0.986 (p=2.4×10⁻⁸) 极其有说服力。
3. **Practitioner Decision Framework（Table 6, Appendix R）有实际应用价值**：三步决策流程（collect → check death dominance → decide）为从业者提供了可操作的 routing 诊断工具，且 retrospective validation 正确分类了全部 4 个条件。
4. **写作质量整体优秀**：Abstract 控制在约 170 词（符合 200 词限制），Introduction 的叙事从 "routing is a growing focus" → "but no principled diagnosis" → "we introduce a framework" → "applied to ScienceWorld" 逻辑流畅。术语使用一致（internal/deterministic 贯穿全文）。
5. **Double-blind 合规**：论文标注 "Anonymous ACL submission"，代码通过 anonymous.4open.science 提供，未发现 self-citation 泄露。
6. **格式合规**：正文 8 页（含 Limitations），References 从第 9 页开始。Limitations 在正文中、Conclusion 之后，覆盖 3 个局限点，符合 EMNLP 2026 要求。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2716 · 2026-05-25T21:23:24.667379+00:00_

Reviewer 2 审稿意见已收到（3.0 Findings, 置信度 4/5）。等待 Reviewer 1 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 225

## Round 225

2 recorded events


### User

_source line 2717 · 2026-05-25T21:23:28.911894+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论摘要**：

- **Overall: 3.0（Findings）**，Confidence 4/5
- **Soundness 4/5** — 方法论严谨，统计检验充分
- **Excitement 2/5** — 核心发现存在显著 triviality 风险
- **Reproducibility 4/5** — 代码/数据/超参数完整

**两个 Critical 问题**：
1. Death dominance 的核心发现可能是实验设计的结构性后果（deterministic strategy 拥有 privileged env access），而非关于 routing 本质的深层洞见
2. Cross-environment probes（MATH/ALFWorld）分析深度远不及 ScienceWorld，无法充分支撑泛化性 claim

**四个 Warning 问题**：附录体量异常（14页/22节）、concurrent work 差异化不够锐利、"counterfactual" 术语定位可更精确、router training 负面结果的因果推理有跳跃

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2718 · 2026-05-25T21:23:36.443569+00:00_

Reviewer 2 审稿意见已收到（3.0 Findings, 2 critical + 4 warning）。等待 Reviewer 1 完成独立审稿后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 226

## Round 226

4 recorded events


### User

_source line 2719 · 2026-05-25T21:24:21.872625+00:00_

[Reviewer 1 审稿结果]:
API Error: {"type":"error","error":{"details":null,"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbPz4J9vJRHsSzpPzQYbZ"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2720 · 2026-05-25T21:24:51.321645+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）\n\n### 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **论文路径**: `projects/simgate-modular-routing/docs/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_32/submitted.pdf`\n\n### 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，long paper 正文 8 页限制（不含 references、limitations、ethical considerations）\n- **匿名**: double-blind（论文不得包含作者信息，self-reference 需匿名化）\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查侧重：方法严谨性 + 实验有效性\n\n重点评估以下方面：\n\n1. **方法论**:\n   - DAF（Death Avoidance Factor）公式的推导是否严谨？分解假设是否成立？\n   - Episode-level counterfactual labeling 的设计是否合理？是否存在 circularity？\n   - DAF 对 penalty P 的单调依赖——论文如何处理这一问题？是否充分？\n   - \"Counterfactual\" 术语的使用是否与因果推断文献一致？\n\n2. **统计检验**:\n   - Bootstrap CI 的使用是否恰当？K=11 cluster 下的推断可靠性如何？\n   - 样本量（245 episodes, per-task n=20-40）是否足够支撑结论？\n   - 多重比较问题是否被处理？\n   - Cross-model 一致性的统计意义如何评估？\n\n3. **实验设计**:\n   - 11/30 task types 选择是否引入 selection bias？Anti-cherry-picking analysis 是否充分？\n   - Deterministic strategy 的 oracle privilege 是否使 death avoidance finding 接近 tautology？\n   - Cross-environment probes（MATH, ALFWorld）的深度和覆盖是否足够？\n   - Agent improvement baselines（Retry, Reflexion, 72B scaling）的设计是否公平？\n   - Router training 的 negative result 是否被充分论证？\n\n4. **格式合规**:\n   - 正文是否在 8 页限制内？\n   - 匿名是否合规（无作者信息、无去匿名化线索）？\n   - Limitations section 是否存在？\n\n请按 Strengths / Weaknesses / Questions / Missing References / Overall Assessment 结构输出审稿意见。每个 Weakness 标注严重程度（critical / warning / info）。给出 Overall Assessment 评分（用 EMNLP 2026 ARR 标准）和置信度（1-5）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "simgate-modular-routing",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）\n\n### 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **论文路径**: `projects/simgate-modular-routing/docs/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_32/submitted.pdf`\n\n### 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，long paper 正文 8 页限制（不含 references、limitations、ethical considerations）\n- **匿名**: double-blind（论文不得包含作者信息，self-reference 需匿名化）\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查侧重：方法严谨性 + 实验有效性\n\n重点评估以下方面：\n\n1. **方法论**:\n   - DAF（Death Avoidance Factor）公式的推导是否严谨？分解假设是否成立？\n   - Episode-level counterfactual labeling 的设计是否合理？是否存在 circularity？\n   - DAF 对 penalty P 的单调依赖——论文如何处理这一问题？是否充分？\n   - \"Counterfactual\" 术语的使用是否与因果推断文献一致？\n\n2. **统计检验**:\n   - Bootstrap CI 的使用是否恰当？K=11 cluster 下的推断可靠性如何？\n   - 样本量（245 episodes, per-task n=20-40）是否足够支撑结论？\n   - 多重比较问题是否被处理？\n   - Cross-model 一致性的统计意义如何评估？\n\n3. **实验设计**:\n   - 11/30 task types 选择是否引入 selection bias？Anti-cherry-picking analysis 是否充分？\n   - Deterministic strategy 的 oracle privilege 是否使 death avoidance finding 接近 tautology？\n   - Cross-environment probes（MATH, ALFWorld）的深度和覆盖是否足够？\n   - Agent improvement baselines（Retry, Reflexion, 72B scaling）的设计是否公平？\n   - Router training 的 negative result 是否被充分论证？\n\n4. **格式合规**:\n   - 正文是否在 8 页限制内？\n   - 匿名是否合规（无作者信息、无去匿名化线索）？\n   - Limitations section 是否存在？\n\n请按 Strengths / Weaknesses / Questions / Missing References / Overall Assessment 结构输出审稿意见。每个 Weakness 标注严重程度（critical / warning / info）。给出 Overall Assessment 评分（用 EMNLP 2026 ARR 标准）和置信度（1-5）。"
  }
}
```

</details>

---


### Tool result

_source line 2721 · 2026-05-25T21:24:55.094494+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3772
}
```

</details>

---


### Assistant

_source line 2722 · 2026-05-25T21:24:58.404374+00:00_

Reviewer 1 任务已重新派发，等待返回。Reviewer 2 的意见（3.0 Findings）已收到并记录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 227

## Round 227

6 recorded events


### User

_source line 2723 · 2026-05-25T21:30:37.113346+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 框架设计合理且分析细致，但核心发现（78.9%）对 penalty P 的机械依赖削弱了结论的稳健性，且 deterministic strategy 的 oracle 特权使 death avoidance 发现的惊人程度打折扣。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | DAF 对 P 的单调依赖是根本性方法论问题；分解在高 P 下接近 tautology |
| Excitement | 3.5/5 | "先诊断再建 router" 的研究思路新颖且实用，但核心发现的信息量有限 |
| Reproducibility | 4/5 | 代码/数据匿名公开，环境设定清晰，但跨环境 probe 细节不足 |
| Overall Assessment | 3.5 | Borderline Conference — 方法论创新值得认可，但统计和可泛化性问题需解决 |

**Confidence**: 4/5

---

## 主要优势 (Strengths)

**S1. "先诊断再路由"范式具有方法论价值。** 大多数 routing 文献直接训练 router，本文提出先用 episode-level counterfactual 分解 routing signal 的组成成分（§1, §3）。即使 ScienceWorld 之外，这一思路也有指导意义——如果 death avoidance 占主导，就不需要复杂的学习型 router。

**S2. 实验设计的 paired structure 干净。** 同一 task instance、同一 seed 下运行两种策略（§3.1），消除了随机变异干扰，性能差异完全归因于 computation mode 选择。

**S3. 诚实报告 negative result。** Router 训练（§4.6, Appendix I）的失败结果没有被掩盖，反而被用来强化"death avoidance 是唯一可利用信号"这一论点。学术诚信值得肯定。

**S4. Appendix 的分析深度令人印象深刻。** Penalty sensitivity（App K）、cluster bootstrap sensitivity（App E）、leave-one-task-out（App G）、text augmentation ablation、failure mode analysis（App N）等分析远超正文深度，显示了审慎态度。

**S5. Practitioner decision framework（Table 6, App R）有实际价值。** 三阶段判断流程（pilot → dominance check → decision）提供了从诊断到行动的具体转化路径。

---

## Must-Fix 问题（影响接收决定）

**W1** [critical] **DAF 对 penalty P 的单调机械依赖——核心发现缺乏参数无关的稳健性**
- 具体位置：§3.4 Eq.(5), Appendix K Table 14-15
- 问题：DAF = Δ_dead/(Δ^P + Δ_dead)。当 P 从 0 增至 500 时，DAF 从 7.4% 单调增至 97.9%（Table 14）。论文使用 P=100（ScienceWorld 的 death penalty），得到 DAF≈90.4%。然而在 P=0 时 DAF 仅 7.4%——即不对 death 施加额外惩罚时，death avoidance 几乎不贡献 routing signal。标题中 "dominant" 是在特定 P 值下的结论，非 routing signal 的内在属性。
- Appendix K §16 右栏讨论了这点，论证"death 在 ScienceWorld 中是 catastrophic（score → 0），所以高 P 是结构性适当的"。但这混淆了两个不同问题：（a）ScienceWorld 中 death 的实际后果（score 确实归零），和（b）这是否意味着 death avoidance 是 routing signal 的本质。如果 death 天然导致 score=0，那么高 DAF 只是在重新表述"死了得不到分"这一显然事实。
- 为什么影响接收：这是论文的核心 claim。如果 DAF 本质上是 P 的函数而非 routing dynamics 的特征，framework 的 diagnostic 价值被严重削弱。
- 建议修改方向：（1）在正文中明确承认 DAF 的 P-dependence，而非仅在 Appendix 讨论；（2）提出 P-invariant 的替代指标（如 death-rate differential 本身，ΔDR = 28.7pp）；（3）重新框架为"death asymmetry 是最大的 routing-relevant 信号组件"而非"dominant signal"。

**W2** [critical] **Deterministic strategy 的 oracle 特权使 death avoidance 发现接近 tautology**
- 具体位置：§3.1, Table 1
- 问题：Deterministic strategy 通过 privileged environment access 直接读取 simulator state 生成 candidate actions（§3.1："the deterministic strategy does not provide special actions, it re-observes observation uncertainty by grounding the LLM's choices to verified environment state"）。其 death rate 为 16.3%，远低于 internal strategy 的 42.9%。这一差异在很大程度上是 oracle access 的直接后果——如果能直接看到环境状态，自然更容易避免致命行为。因此"routing signal 主要来自 death asymmetry"部分等价于"oracle access 帮助避免 death"，这并不令人惊讶。
- §5 Discussion 中部分回应（"signal granularity and router failure"），但没有直接面对 tautology 质疑。
- 为什么影响接收：降低了核心发现的信息量。如果 deterministic strategy 的优势主要来自 oracle access 避免 death，"death avoidance dominates routing signal" 只是重新包装了一个已知事实。
- 建议修改方向：（1）增加一个 non-oracle deterministic baseline（如 rule-based 但不访问 environment state 的策略）分离 oracle effect；（2）或更明确论证为什么这一看似 obvious 的发现仍然有社区价值——社区之前并未量化这一效应，且 practitioners 仍在为这类环境构建复杂 router。

**W3** [critical] **K=11 cluster bootstrap 的统计推断可靠性不足**
- 具体位置：§4.1, Appendix D-E
- 问题：Bootstrap CI 以 K=11 task types 为 cluster（Appendix E 明确承认 K=11 远低于推荐的 K≥20-50）。当 effective sample size 接近 K 而非 N=245 时，95% CI 的 coverage probability 可能严重偏离 nominal level。Appendix E 提到 "episodes within the same task type share environment dynamics, raising the concern that the effective sample size is closer to K (task types) than N (episodes)"，但仅以 leave-one-out（App G）作 robustness check，未提供 coverage simulation 或 permutation-based alternative。
- 11 个 task types 逐一检验 death dominance（Table 2），但未应用多重比较校正（Bonferroni/FDR）。Appendix D 的 sign test (p=0.002) 和 permutation test (p=0.002) 在 K=11 下的分辨力有限。
- 为什么影响接收：统计推断的可靠性直接影响 "78.9%" 这一数字的可信度。
- 建议修改方向：（1）增加 excluded tasks 数据以扩大 K；（2）报告 permutation-based CI 作为 bootstrap 补充；（3）明确讨论多重比较问题。

---

## Should-Fix 问题（影响评分但不一票否决）

**W4** [warning] **"Counterfactual" 术语使用与因果推断文献不完全一致**
- 具体位置：Title, §1, §3
- 问题：论文标题使用 "Counterfactual Analysis"，但实际设计更接近 paired comparison / crossover design。因果推断文献（Rubin 1974, Pearl 2009）中 counterfactual 指同一 unit 在未接受 treatment 下的潜在结果，通常不可观测。本文中两种策略同时运行在相同 task instance 上，两个结果都被观测——更接近 crossover design。论文引用了 Rubin (1974) 但连接松散。
- 更根本地，分解（death vs. non-death components）是 distributional decomposition 而非 causal decomposition——量化了多少 routing signal 归因于 death asymmetry，但没有识别 death 的原因。
- 建议：在 §3 开头明确区分 "counterfactual episode collection"（确实是 paired potential outcomes）与 "signal decomposition"（是 descriptive 而非 causal）。

**W5** [warning] **Cross-environment probes 是边界情况，缺乏中间验证**
- 具体位置：§4.4, Table 5
- 问题：MATH 没有 death 机制（DAF=0%），ALFWorld 没有 death 事件（death rate=0%, DAF=0%）。两个 probe 只验证了极端情况下的行为（全有 vs. 全无 death），没有测试 intermediate cases——例如 death rate 适中、或 penalty 为 graded（非 binary）的环境。Limitations（p.8）承认了这点，但 cross-environment validation 标准应更高。
- 建议：增加至少一个 death rate 在 20-40%、penalty 为 graded 的环境作为 intermediate probe。

**W6** [warning] **Router 负面结果可能反映训练不足而非信号缺失**
- 具体位置：§4.6, Appendix I, Table 11-12
- 问题：Router 使用 Qwen2.5-7B + LoRA（rank=8, 4 epochs），训练数据仅 245 episodes。Step-level balanced accuracy 42%（低于 random 50%），episode-level 47.1%。论文从此推断 "no exploitable signal beyond death avoidance"。
- 替代解释：（1）LoRA rank=8 可能不够；（2）训练数据太少（245 episodes, 有效 K=11 tasks）；（3）text-based input representation 可能不适合 routing decision。Appendix P capacity scaling（0.6B → 4B）显示 episode-level 仅 4B 勉强超过 random baseline，这更可能是 data insufficiency 而非 signal absence。
- 建议：明确区分 "no signal" 与 "signal not learnable with current setup"；报告 upper bound（如用 ground-truth labels 训练 oracle router 的 accuracy ceiling）。

**W7** [warning] **Anti-cherry-picking analysis 的论证存在盲区**
- 具体位置：Appendix C Table 7, Appendix S Table 22
- 问题：Table 7 显示 excluded tasks 的 mean ΔDR = +38.2pp > included tasks 的 +28.7pp，论文据此声称 task selection 不 bias toward death-dominance。但 Table 22 对 5 个 representative excluded tasks 验证（n=20）确认所有 5 个都是 death-dominated——包含它们只会增强 death dominance 结论，但不能证明 included tasks representative of full task space。如果全部 30 tasks 都 death-dominated，那说明问题在 ScienceWorld 本身，不应过度泛化为一般 agent routing phenomenon。
- 建议：在讨论中明确 included + excluded tasks 都显示 death dominance 是 ScienceWorld 的环境特征，不应过度泛化。

---

## 小问题（不影响接收）

**W8** [info] Figure 3 caption 声称 r=0.97 是 "structural consequence of death dominance"，但 Appendix D 报告 Spearman ρ=0.586，远低于 Pearson r=0.9065，说明关系的 monotonicity 不如 linearity 强，r=0.97 可能受极端值驱动。

**W9** [info] §3.4 Eq.(4) 的近似号 (≈)："The approximate residual is 29.60 − 29.37 = 0.23 (0.8% of Δ_full)"——缺乏在其他 P 值或 task subsets 下的 worst-case bound。

**W10** [info] Abstract 中 "708-scale" 似为排版错误，应为 "70B-scale"。

---

## Questions for Authors

**Q1.** 如果用 death-rate differential（ΔDR = 28.7pp）本身作为 routing signal 度量（P-invariant），核心结论是否改变？ΔDR 是否足以支撑 "death avoidance dominates" 的论断？

**Q2.** 是否尝试过 non-oracle deterministic baseline（如 rule-based 但不访问 environment state 的策略）？如果有，death asymmetry 是否仍然主导？

**Q3.** Table 12（App I）episode-level evaluation 使用 "always-det majority vote" 作为 baseline（47.1 ± 2.2 vs. 50.0），但 §4.5 的 always-deterministic baseline 在 oracle 比较中达到 96.3%。请澄清两个 evaluation protocol 的区别。

**Q4.** Appendix K Table 15 显示 Pearson r 在 P≤10 时不显著，P≥25 时显著。如何判断 P=100 不是 arbitrarily high value？是否存在一个 "natural" P 反映 death 在 task completion 中的实际 cost？

---

## Missing References

- Uesato et al., 2022. "Solving math word problems with process- and outcome-based feedback" — process/outcome-level routing decisions
- Lightman et al., 2023. "Let's Verify Step by Step" — process reward models 作为 episode-level routing 的替代
- Snell et al., 2024. "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Model Parameters" — 直接相关的 adaptive computation routing

---

## 格式合规

- **页数**：正文（§1-6）在 8 页内，Limitations 在第 8 页但不计入页数限制 ✓
- **匿名**："Anonymous ACL submission"，代码链接使用 anonymous.4open.science ✓
- **Limitations**：存在（第 8 页），覆盖 generalizability、penalty dependence、sample size 三个点 ✓
- **Abstract**：约 170 words，在 200-word 限制内 ✓
- **AI 使用声明**：Appendix V 披露使用 Claude ✓

---

## Overall Assessment 总结

**Overall**: 3.5 / 5 (Borderline Conference)
**Confidence**: 4 / 5

论文提出的 "先诊断 routing signal 再决定是否训练 router" 范式具有方法论创新。实验在 ScienceWorld 上执行细致，appendix 分析深度远超一般 submission。

但三个 critical 问题削弱了 contribution：（1）DAF 对 penalty P 的机械依赖使核心数字（78.9%）的稳健性存疑——改变 P 得到从 7.4% 到 97.9% 的任何值；（2）deterministic strategy 的 oracle 特权使 death avoidance 发现的惊人程度打折扣；（3）K=11 的 cluster bootstrap 推断统计上不够可靠。

如果作者能在 rebuttal 中（a）提出 P-invariant 替代度量并证明结论不变，（b）论证 oracle 特权不是 death asymmetry 的主要驱动力，（c）补充 permutation-based 推断，评分可提升至 4.0 (Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2724 · 2026-05-25T21:31:21.684621+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "## Step 2 — 交叉分享：Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Weakness/Question：\n- **[AGREE]**：同意并简要说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 评分\n**Overall**: 3.5 (Borderline Conference), Confidence 4/5\n**Soundness 3/5, Excitement 3.5/5, Reproducibility 4/5**\n\n### Reviewer 1 Strengths\nS1. \"先诊断再路由\"范式具有方法论价值。\nS2. 实验设计的 paired structure 干净。\nS3. 诚实报告 negative result。\nS4. Appendix 的分析深度令人印象深刻。\nS5. Practitioner decision framework（Table 6, App R）有实际价值。\n\n### Reviewer 1 Must-Fix (Critical)\n\n**W1** [critical] DAF 对 penalty P 的单调机械依赖——核心发现缺乏参数无关的稳健性\n- DAF = δP/(δP + Δ_nd)。P 从 0→500 时 DAF 从 7.4%→97.9%。P=0 时 DAF 仅 7.4%。标题中 \"dominant\" 是在特定 P 值下的结论。\n- 建议：正文承认 P-dependence；提出 P-invariant 替代指标（如 ΔDR=28.7pp）；重新框架为 \"death asymmetry 是最大的 routing-relevant 信号组件\"。\n\n**W2** [critical] Deterministic strategy 的 oracle 特权使 death avoidance 发现接近 tautology\n- Deterministic strategy 通过 privileged env access 直接读取 simulator state，death rate 16.3% vs internal 42.9%。\"routing signal 主要来自 death asymmetry\" 部分等价于 \"oracle access 帮助避免 death\"。\n- 建议：增加 non-oracle deterministic baseline 分离 oracle effect；或论证为什么 practitioners 仍在构建复杂 router。\n\n**W3** [critical] K=11 cluster bootstrap 的统计推断可靠性不足\n- K=11 远低于推荐的 K≥20-50。未应用多重比较校正。Appendix D 的 sign test/permutation test 在 K=11 下分辨力有限。\n- 建议：扩大 K；报告 permutation-based CI；讨论多重比较。\n\n### Reviewer 1 Should-Fix (Warning)\n\n**W4** [warning] \"Counterfactual\" 术语使用与因果推断文献不完全一致——更接近 paired comparison / crossover design。\n**W5** [warning] Cross-environment probes 只验证了极端情况（全有/全无 death），缺乏中间验证。\n**W6** [warning] Router 负面结果可能反映训练不足而非信号缺失（LoRA rank=8, 245 episodes）。\n**W7** [warning] Anti-cherry-picking analysis 的盲区：如果全部 30 tasks 都 death-dominated，问题在 ScienceWorld 本身。\n\n### Reviewer 1 Minor\n\nW8. Spearman ρ=0.586 vs Pearson r=0.97，r 可能受极端值驱动。\nW9. Eq.(4) 近似缺 worst-case bound。\nW10. Abstract \"708-scale\" 疑为排版错误。\n\n### Reviewer 1 Questions\n\nQ1. 如果用 ΔDR 本身作为 routing signal 度量（P-invariant），核心结论是否改变？\nQ2. 是否尝试过 non-oracle deterministic baseline？\nQ3. 请澄清 Table 12 和 §4.5 两个 evaluation protocol 的区别。\nQ4. 如何判断 P=100 不是 arbitrarily high value？\n\n### Reviewer 1 Missing References\n- Uesato et al., 2022 (process/outcome-based feedback)\n- Lightman et al., 2023 (process reward models)\n- Snell et al., 2024 (scaling test-time compute)\n\n---\n\n请对以上每个 W1-W10 和 Q1-Q4 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "simgate-modular-routing",
    "text": "## Step 2 — 交叉分享：Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Weakness/Question：\n- **[AGREE]**：同意并简要说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 评分\n**Overall**: 3.5 (Borderline Conference), Confidence 4/5\n**Soundness 3/5, Excitement 3.5/5, Reproducibility 4/5**\n\n### Reviewer 1 Strengths\nS1. \"先诊断再路由\"范式具有方法论价值。\nS2. 实验设计的 paired structure 干净。\nS3. 诚实报告 negative result。\nS4. Appendix 的分析深度令人印象深刻。\nS5. Practitioner decision framework（Table 6, App R）有实际价值。\n\n### Reviewer 1 Must-Fix (Critical)\n\n**W1** [critical] DAF 对 penalty P 的单调机械依赖——核心发现缺乏参数无关的稳健性\n- DAF = δP/(δP + Δ_nd)。P 从 0→500 时 DAF 从 7.4%→97.9%。P=0 时 DAF 仅 7.4%。标题中 \"dominant\" 是在特定 P 值下的结论。\n- 建议：正文承认 P-dependence；提出 P-invariant 替代指标（如 ΔDR=28.7pp）；重新框架为 \"death asymmetry 是最大的 routing-relevant 信号组件\"。\n\n**W2** [critical] Deterministic strategy 的 oracle 特权使 death avoidance 发现接近 tautology\n- Deterministic strategy 通过 privileged env access 直接读取 simulator state，death rate 16.3% vs internal 42.9%。\"routing signal 主要来自 death asymmetry\" 部分等价于 \"oracle access 帮助避免 death\"。\n- 建议：增加 non-oracle deterministic baseline 分离 oracle effect；或论证为什么 practitioners 仍在构建复杂 router。\n\n**W3** [critical] K=11 cluster bootstrap 的统计推断可靠性不足\n- K=11 远低于推荐的 K≥20-50。未应用多重比较校正。Appendix D 的 sign test/permutation test 在 K=11 下分辨力有限。\n- 建议：扩大 K；报告 permutation-based CI；讨论多重比较。\n\n### Reviewer 1 Should-Fix (Warning)\n\n**W4** [warning] \"Counterfactual\" 术语使用与因果推断文献不完全一致——更接近 paired comparison / crossover design。\n**W5** [warning] Cross-environment probes 只验证了极端情况（全有/全无 death），缺乏中间验证。\n**W6** [warning] Router 负面结果可能反映训练不足而非信号缺失（LoRA rank=8, 245 episodes）。\n**W7** [warning] Anti-cherry-picking analysis 的盲区：如果全部 30 tasks 都 death-dominated，问题在 ScienceWorld 本身。\n\n### Reviewer 1 Minor\n\nW8. Spearman ρ=0.586 vs Pearson r=0.97，r 可能受极端值驱动。\nW9. Eq.(4) 近似缺 worst-case bound。\nW10. Abstract \"708-scale\" 疑为排版错误。\n\n### Reviewer 1 Questions\n\nQ1. 如果用 ΔDR 本身作为 routing signal 度量（P-invariant），核心结论是否改变？\nQ2. 是否尝试过 non-oracle deterministic baseline？\nQ3. 请澄清 Table 12 和 §4.5 两个 evaluation protocol 的区别。\nQ4. 如何判断 P=100 不是 arbitrarily high value？\n\n### Reviewer 1 Missing References\n- Uesato et al., 2022 (process/outcome-based feedback)\n- Lightman et al., 2023 (process reward models)\n- Snell et al., 2024 (scaling test-time compute)\n\n---\n\n请对以上每个 W1-W10 和 Q1-Q4 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 2725 · 2026-05-25T21:31:46.546480+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24861
}
```

</details>

---


### Tool call

_source line 2726 · 2026-05-25T21:31:46.697573+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "## Step 2 — 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Weakness/Question：\n- **[AGREE]**：同意并简要说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 评分\n**Overall**: 3.0 (Findings), Confidence 4/5\n**Soundness 4/5, Excitement 2/5, Reproducibility 4/5**\n\n### Reviewer 2 Strengths\nS1. 框架设计简洁而有力（DAF 定义, Algorithm 1）。\nS2. 统计验证极其充分（Bootstrap CI, LOO, seed robustness, correlation robustness）。\nS3. Practitioner Decision Framework（Table 6, Appendix R）有实际应用价值。\nS4. 写作质量整体优秀，Abstract ~170 词，叙事逻辑流畅。\nS5. Double-blind 合规，格式合规。\n\n### Reviewer 2 Must-Fix (Critical)\n\n**N1** [critical] 核心发现的 Triviality 风险未充分回应\n- Deterministic strategy 有 privileged env feedback（§3.1），internal 仅靠 chain-of-thought。death asymmetry 主导路由信号在很大程度上是实验设计的结构性后果。\n- DAF 在 P=0 时为 0，P=100 时为 90.4%——\"death dominance\" 部分是惩罚参数的函数。\n- 建议：正面论证非 triviality；增加 graded failure 环境分析；从 \"discover death dominance\" 转向 \"provide framework that quantifies it\"。\n\n**N2** [critical] Cross-Environment Probes 过于初步\n- MATH 仅 N=795 的 label 分布，ALFWorld 仅 135 games，两者未做与 ScienceWorld 同等深度的分解。\n- MATH 的 \"no routing signal\" 可能因 deterministic strategy 设计不当。\n- 建议：ALFWorld 做完整 DAF 分解；讨论 MATH deterministic strategy 合理性；降低泛化性 claim。\n\n### Reviewer 2 Should-Fix (Warning)\n\n**W1** [warning] 附录体量异常（14 页/22 节），正文-附录信息分配需重新审视。关键分析（penalty sensitivity App K, failure mode App N, grounding ablation App O）被放入附录。\n**W2** [warning] 与 Concurrent Work 差异化定位不够锐利——仅用一句话概括差异。\n**W3** [warning] \"Counterfactual\" 术语使用范围可进一步澄清——更接近 paired controlled comparison。\n**W4** [warning] Router Training（§4.6）结论跳跃——router 表现差可能有多种原因（特征不够、数据不足、容量不够）。\n\n### Reviewer 2 Minor\n- Figure 1 可读性：78.9% 标注与 DAF=90.4% 关系未在图注说明。\n- Table 2 D/I/N 列标题不够直观。\n- §4.3 Agent Improvement 未报告 intervention 对 DAF 本身的影响。\n- Appendix V AI 使用声明合规。\n\n### Reviewer 2 Missing References\n1. Risk-sensitive RL / CVaR：Tamar et al. (2015), Dabney et al. (2018)\n2. Adaptive computation / early exit：Universal Transformers (Dehghani 2019), CALM (Schuster 2022)\n3. Agent failure taxonomy：Kambhampati et al. (2024), Valmeekam et al. (2023)\n\n---\n\n请对以上每个 N1-N2、W1-W4 和 Minor/Missing References 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "simgate-modular-routing",
    "text": "## Step 2 — 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Weakness/Question：\n- **[AGREE]**：同意并简要说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 评分\n**Overall**: 3.0 (Findings), Confidence 4/5\n**Soundness 4/5, Excitement 2/5, Reproducibility 4/5**\n\n### Reviewer 2 Strengths\nS1. 框架设计简洁而有力（DAF 定义, Algorithm 1）。\nS2. 统计验证极其充分（Bootstrap CI, LOO, seed robustness, correlation robustness）。\nS3. Practitioner Decision Framework（Table 6, Appendix R）有实际应用价值。\nS4. 写作质量整体优秀，Abstract ~170 词，叙事逻辑流畅。\nS5. Double-blind 合规，格式合规。\n\n### Reviewer 2 Must-Fix (Critical)\n\n**N1** [critical] 核心发现的 Triviality 风险未充分回应\n- Deterministic strategy 有 privileged env feedback（§3.1），internal 仅靠 chain-of-thought。death asymmetry 主导路由信号在很大程度上是实验设计的结构性后果。\n- DAF 在 P=0 时为 0，P=100 时为 90.4%——\"death dominance\" 部分是惩罚参数的函数。\n- 建议：正面论证非 triviality；增加 graded failure 环境分析；从 \"discover death dominance\" 转向 \"provide framework that quantifies it\"。\n\n**N2** [critical] Cross-Environment Probes 过于初步\n- MATH 仅 N=795 的 label 分布，ALFWorld 仅 135 games，两者未做与 ScienceWorld 同等深度的分解。\n- MATH 的 \"no routing signal\" 可能因 deterministic strategy 设计不当。\n- 建议：ALFWorld 做完整 DAF 分解；讨论 MATH deterministic strategy 合理性；降低泛化性 claim。\n\n### Reviewer 2 Should-Fix (Warning)\n\n**W1** [warning] 附录体量异常（14 页/22 节），正文-附录信息分配需重新审视。关键分析（penalty sensitivity App K, failure mode App N, grounding ablation App O）被放入附录。\n**W2** [warning] 与 Concurrent Work 差异化定位不够锐利——仅用一句话概括差异。\n**W3** [warning] \"Counterfactual\" 术语使用范围可进一步澄清——更接近 paired controlled comparison。\n**W4** [warning] Router Training（§4.6）结论跳跃——router 表现差可能有多种原因（特征不够、数据不足、容量不够）。\n\n### Reviewer 2 Minor\n- Figure 1 可读性：78.9% 标注与 DAF=90.4% 关系未在图注说明。\n- Table 2 D/I/N 列标题不够直观。\n- §4.3 Agent Improvement 未报告 intervention 对 DAF 本身的影响。\n- Appendix V AI 使用声明合规。\n\n### Reviewer 2 Missing References\n1. Risk-sensitive RL / CVaR：Tamar et al. (2015), Dabney et al. (2018)\n2. Adaptive computation / early exit：Universal Transformers (Dehghani 2019), CALM (Schuster 2022)\n3. Agent failure taxonomy：Kambhampati et al. (2024), Valmeekam et al. (2023)\n\n---\n\n请对以上每个 N1-N2、W1-W4 和 Minor/Missing References 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 2727 · 2026-05-25T21:31:48.028217+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1330
}
```

</details>

---


### Assistant

_source line 2728 · 2026-05-25T21:31:50.981440+00:00_

交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 228

## Round 228

2 recorded events


### User

_source line 2729 · 2026-05-25T21:31:53.477764+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**3.5 / 5（Borderline Conference）**，置信度 4/5。

三个 critical 问题：
1. **DAF 对 penalty P 的机械依赖**——P 从 0→500 时 DAF 从 7.4%→97.9%，核心数字 78.9% 并非参数无关的稳健结论
2. **Deterministic strategy 的 oracle 特权**使 death avoidance 发现接近 tautology——oracle access 天然避免 death，发现 routing signal 由 death asymmetry 主导并不令人惊讶
3. **K=11 cluster bootstrap** 远低于推荐的 K≥20-50，统计推断可靠性不足

四个 warning 级问题涉及"counterfactual"术语使用、cross-environment probe 仅覆盖边界情况、router 负面结果可能反映训练不足而非信号缺失、anti-cherry-picking 论证盲区。

如果 rebuttal 能提出 P-invariant 替代度量、分离 oracle effect、补充 permutation-based 推断，评分可提升至 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2730 · 2026-05-25T21:31:57.828667+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 229

## Round 229

18 recorded events


### User

_source line 2731 · 2026-05-25T21:33:21.842611+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 意见的逐条回应

---

### Must-Fix (Critical)

**[AGREE] R2-N1: 核心发现的 Triviality 风险**

同意，且这与我的 W1（DAF 对 P 的机械依赖）和 W2（oracle 特权 tautology）高度重叠。R2 准确识别了问题的两个维度：

（1）**P-dependence 维度**：DAF 在 P=0 时为 7.4%，P=100 时为 90.4%（Appendix K, Table 14），"death dominance" 的强度是惩罚参数的直接函数。论文的 headline number 78.9%（label fraction）虽然是 P-invariant 的，但 DAF 本身不是，而正文对两者的区分不够清晰。

（2）**Oracle privilege 维度**：deterministic strategy 的 death rate 16.3% vs. internal 的 42.9%（Table 1）在很大程度上源于 privileged environment access，而非 routing-relevant 的策略优势。

R2 的建议（从 "discover death dominance" 转向 "provide framework that quantifies it"）是恰当的 reframing——论文的真正贡献是 diagnostic framework 本身，而非 death dominance 这一具体发现。我补充建议作者提供 P-invariant 的替代度量（如 ΔDR = 28.7pp）作为主要证据。

**[AGREE] R2-N2: Cross-Environment Probes 过于初步**

同意主体判断，与我的 W5 一致。两个 probe 都是边界情况（MATH: 无 death，DAF=0%；ALFWorld: 无 death 事件，DAF=0%），缺乏中间验证。

但对 R2 的一个子论点持保留意见：R2 说 "MATH 的 'no routing signal' 可能因 deterministic strategy 设计不当"。从论文看，MATH 的 deterministic strategy 是 greedy decoding（T=0），internal 是 chain-of-thought（Table 5 注脚）。两者 accuracy 近乎相同（73.0% vs. 73.0%, Table 5），这不太像 strategy 设计失败，更像 MATH 本身确实不存在 routing signal（两种策略等效）。R2 此处的质疑缺乏具体证据。

R2 建议 ALFWorld 做完整 DAF 分解是合理的——ALFWorld 的 information asymmetry 机制（Table 5: Δ_int = -10.70）值得深入分析，而非仅报告 label 分布。

---

### Should-Fix (Warning)

**[AGREE] R2-W1: 附录体量异常，正文-附录信息分配需重审**

同意。14 页附录 / 22 节确实异常。关键的问题是：**Penalty sensitivity（App K）直接关系到核心 claim 的稳健性，应在正文讨论**。目前正文对 P-dependence 几乎一笔带过（§3.4 仅脚注提到 P*=100），读者需翻到第 16 页才能看到 DAF 随 P 变化的全貌。这不是"补充分析放附录"，而是"核心方法论问题被藏在附录"。

Failure mode analysis（App N）和 grounding ablation（App O）的重要性次之，放附录可接受。

**[REBUT] R2-W2: 与 Concurrent Work 差异化定位不够锐利**

部分不同意。§2 Related Work 第一段用了较大篇幅讨论 tool-augmented agents 和 adaptive routing 的现有工作（Schick et al., 2023; Zhang et al., 2025; Parashar et al., 2023; Lu et al., 2023 等），并明确指出 "All these approaches presuppose that diverse routing signal stems from diverse sources and a learned router can exploit it"（§2 最后一句），这就是论文与现有工作的核心差异——先诊断 signal 组成，而非直接学 router。

差异化确实可以更 sharp，但称之为 "仅一句话概括" 不太准确。建议在 §2 末尾增加一个显式的 comparison table 或 bullet list。

**[AGREE] R2-W3: "Counterfactual" 术语使用需进一步澄清**

同意，与我的 W4 完全一致。论文的 paired controlled comparison 设计确实可以观测两个 potential outcomes（因为 ScienceWorld 是确定性环境+固定 seed），这使得 "counterfactual" 的使用不算错误，但与因果推断文献（Rubin 1974, Pearl 2009）的标准用法存在偏差。distributional decomposition ≠ causal decomposition，论文应在 §3 开头明确区分。

**[AGREE] R2-W4: Router Training 结论跳跃**

同意，与我的 W6 一致。从 LoRA rank=8、245 episodes、Qwen2.5-7B 的单一配置得出 "no exploitable signal" 是过度推断。Appendix P 的 capacity scaling（0.6B → 4B）显示 episode-level accuracy 仅在 4B 时勉强超过 random baseline（50.0%），这更可能是 data/capacity insufficiency 而非 signal absence。

论文应区分 "no signal exists" 与 "signal not learnable with this setup"，后者是更准确的表述。

---

### Minor

**[AGREE]** Figure 1 可读性：78.9% 是 label fraction（Algorithm 1），DAF=90.4% 是 score gap fraction（Eq.5）。两个数字的关系确实应在图注或正文中明确说明，避免读者混淆。

**[AGREE]** Table 2 D/I/N 列标题：确实需要查 caption 才能理解。建议改为 Det/Int/NoPref 或在表头加脚注。

**[AGREE]** §4.3 Agent Improvement 未报告 intervention 对 DAF 的影响：Retry 和 Reflexion 改变了 death rate（Table 1: Retry 43.5%, Reflexion 31.4%），但未报告 DAF 是否同步变化。这会加强 "death avoidance 是 robust 的 routing signal" 或暴露其脆弱性，无论哪种结果都有信息量。

**[AGREE]** Appendix V AI 使用声明合规，无异议。

---

### Missing References

**[AGREE]** Risk-sensitive RL / CVaR（Tamar 2015, Dabney 2018）：death avoidance 与 risk-sensitive RL 的 tail-risk minimization 在概念上高度相关。论文将 death 视为 catastrophic failure，这正是 CVaR 优化的场景。值得在 §2 或 §5 中引用并讨论连接。

**[REBUT]** Adaptive computation / early exit（Universal Transformers, CALM）：这些工作关注模型内部的 layer-level early exit，与本文的 episode-level strategy routing 在抽象层次上有本质差异。引用无害，但缺失不构成显著缺陷。

**[AGREE]** Agent failure taxonomy（Kambhampati 2024, Valmeekam 2023）：与论文的 failure mode analysis（App N）直接相关。Kambhampati 等人对 LLM agent planning 局限性的分析（尤其是 hallucination-induced failure）可以为论文的 death cause taxonomy（Table 23）提供更广泛的理论锚点。

---

### 综合判断

R2 给出 Overall 3.0（Findings），我给出 3.5（Borderline Conference）。我们对主要问题高度一致：P-dependence、oracle tautology、cross-env 深度不足。分歧主要在 excitement——R2 给 2/5，我给 3.5/5。我认为 "先诊断再路由" 的范式 framing 本身有方法论贡献，即使 ScienceWorld 上的具体发现 information content 有限。

如果作者能 reframe contribution（从 "discovery" 到 "framework + quantification"）、在正文中正面处理 P-dependence、并补充 intermediate cross-env probe，我认为论文可达到 Conference 水平（4.0）。以当前形式，3.0-3.5 之间的评分是合理的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2732 · 2026-05-25T21:34:09.933618+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 2733 · 2026-05-25T21:34:09.986132+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 2734 · 2026-05-25T21:34:12.195183+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "get_external_review_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "get_external_review_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 2735 · 2026-05-25T21:34:12.245831+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2736 · 2026-05-25T21:34:15.257939+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 2737 · 2026-05-25T21:34:15.308607+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2738 · 2026-05-25T21:34:17.367128+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "visual check status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "visual check status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2739 · 2026-05-25T21:34:17.467888+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2740 · 2026-05-25T21:34:26.404715+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_post_to_reviewer",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_post_to_reviewer",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2741 · 2026-05-25T21:34:26.405124+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2742 · 2026-05-25T21:34:26.806690+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "submit_review_report update_review_issues read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "submit_review_report update_review_issues read_project_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 2743 · 2026-05-25T21:34:26.857358+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2744 · 2026-05-25T21:34:35.541967+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool call

_source line 2745 · 2026-05-25T21:34:35.542466+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 2746 · 2026-05-25T21:34:35.593269+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 2747 · 2026-05-25T21:34:35.593888+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T21:15:58.071645+00:00\", \"completed_at\": \"2026-05-25T21:18:47.943058+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"单页塞入 4 个 display items（Figure 3 + Figure 4 + Table 1 + Table 2），视觉极度拥挤。建议将 Table 2 移至 page 6 或合并 Figure 3/4 为 subfigure 以释放空间\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"单页包含 Figure 5 + Figure 6 + Table 5 共 3 个 display items，密度较高。与 page 5 连续形成\\\"图表密集带\\\"，审稿人可能感到信息过载\"}, {\"severity\": \"warning\", \"dimension\": \"page 3\", \"message\": \"Figure 2 条形图内的 axis label 和 legend 字号偏小（目测 ≤6pt），150 dpi 下已难辨认；打印或低分辨率屏幕阅读时可读性堪忧\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"Figure 4 action sequence 可视化中的文字标签（action 名称、step 编号）字号过小，信息密度高但可读性差\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 3 散点图为单栏宽度，数据点和标签拥挤。若改为 figure*（全宽）或适度增大字号，可读性会明显提升\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 framework 图整体清晰，但部分箭头和小字标注（如 Algorithm 1 引用标记）在缩小后不够醒目\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 3 和 Table 4 均使用 booktabs 风格（无竖线），最优值加粗标注——格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 6 使用 booktabs 风格，4/4 条件全部正确分类，呈现清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Limitations 段落简短（约 1/3 栏），符合 EMNLP 要求\"}, {\"severity\": \"info\", \"dimension\": \"page 9-10\", \"message\": \"References 排版正常，未见 [?] 未解析引用或格式不一致\"}, {\"severity\": \"info\", \"dimension\": \"page 11\", \"message\": \"Appendix 目录列出 A–T 共 20 个附录，条目清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Algorithm 1 伪代码框渲染正确，缩进和数学符号清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"公式 (1)–(5) 渲染正确，无 LaTeX 残留错误\"}, {\"severity\": \"info\", \"dimension\": \"page 20\", \"message\": \"页面下半部分有约 1/4 面积空白（Table 21/22 之后），但作为 appendix 
…[truncated 243 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 2748 · 2026-05-25T21:35:00.050223+00:00_

**R1 交叉回应已收到，收敛评估：**

| 问题 | R1 立场 | 共识 |
|------|---------|------|
| R2-N1 Triviality 风险 | AGREE | ✅ |
| R2-N2 Cross-env 不足 | AGREE（保留 MATH 子论点） | ✅ |
| R2-W1 附录体量/信息分配 | AGREE | ✅ |
| R2-W2 Concurrent work 定位 | REBUT（部分） | ⚠️ 分歧 |
| R2-W3 Counterfactual 术语 | AGREE | ✅ |
| R2-W4 Router 结论跳跃 | AGREE | ✅ |

评分：R1 = 3.5（Borderline Conference），R2 = 3.0（Findings）。R1 认为 3.0-3.5 区间合理。

**外部审稿**：未请求。
**视觉审查**：已完成（4 warnings / 0 critical），主要问题是 page 5 图表过度拥挤（4 个 display items）和部分 figure 字号偏小。

等待 Reviewer 2 对 Reviewer 1 意见的交叉回应，收齐后合成最终报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 230

## Round 230

14 recorded events


### User

_source line 2749 · 2026-05-25T21:35:01.345826+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- 与 R2 在 3 个 critical 问题（P-dependence、oracle tautology、cross-env 不足）上高度一致（均 AGREE）
- Should-Fix 中 W1/W3/W4 同意，W2（concurrent work 差异化）部分反驳——§2 的差异化不只是一句话
- Missing References 中 Risk-sensitive RL 和 Agent failure taxonomy 同意，Adaptive computation/early exit 反驳（抽象层次不同）
- 主要分歧在 Excitement：R2 给 2/5，我给 3.5/5——我认为 "先诊断再路由" 范式本身有方法论价值，即使具体发现的 information content 有限

---

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见

---

### Must-Fix (Critical)

**[AGREE] R1-W1: DAF 对 penalty P 的机械依赖**
同意这是核心问题。我在自己的 N1 中也独立提出了相同关切。Appendix K（Table 14）的数据非常明确：P=0 时 DAF=7.4%，P=1 时 14.8%，P=10 时 50.4%——DAF 的"dominance"是 P 的单调函数而非环境的固有属性。R1 建议的 ΔDR=28.7pp 作为 P-invariant 替代指标是合理的。补充一点：论文正文（Section 3.4, page 4）给出的 DAF 公式 DAF = 1 − Δ_nd/(Δ^P + Δ_nd) 在数学上就保证了 P→∞ 时 DAF→1，这意味着"death dominance"在高惩罚环境中是一个**数学必然**而非经验发现。这进一步支持了 R1 的判断。

**[AGREE] R1-W2: Oracle 特权使发现接近 tautology**
完全同意，这也是我的 N1 的核心论点。Deterministic strategy 通过 "privileged env feedback"（Section 3.1）直接读取 simulator state，构成了信息不对称的根源。Table 1（page 5）的 death rate 对比（internal 42.9% vs deterministic 16.3%）在这一设定下几乎是预期结果。R1 建议的 non-oracle deterministic baseline 是一个关键的控制实验——如果 non-oracle deterministic 的 death rate 接近 internal，则说明 death asymmetry 来自 oracle access 而非策略类型差异，这会从根本上改变发现的解读。

**[REBUT] R1-W3: K=11 cluster bootstrap 的统计推断**
R1 的统计关切有道理（K=11 确实低于 Cameron et al., 2008 推荐的 K≥20-50），但论文的主要推断并非建立在 cluster bootstrap 之上。几点证据：
1. 论文在 Appendix E（page 12）**主动承认**了 K=11 的局限："cluster bootstrap falls well below the K≥20-50 recommended for reliable inference"，并明确说明 cluster bootstrap 在此设定下反映 small-sample bias toward underestimation of variance, not tighter inference。
2. 核心推断使用的是 **episode-level bootstrap**（N=245 episodes），而非 task-level cluster bootstrap。Section 4.1（page 5）报告的 95% CI [70.7%, 87.05%] 是 episode-level bootstrap 的结果。
3. 补充统计检验包括：leave-one-out（Appendix G，Table 8 显示无单一任务类型是杠杆点）、per-task bootstrap CI（Appendix F，Table 10 显示聚合 death rates 在 N≥2 时 stabilize at 2.5 pp band）、sign test（Appendix D，permutation p=0.002）。
4. Pearson r=0.9065 的 permutation test（Appendix D）不依赖聚类结构。

因此，K=11 是 cluster-level robustness check 的已知局限，但**不是**论文核心推断链的瓶颈。R1 建议的多重比较校正是合理的改进方向，但当前统计证据的整体分量已足以支撑主要结论。

---

### Should-Fix (Warning)

**[AGREE] R1-W4: "Counterfactual" 术语**
同意。我在自己的 W3 中也独立指出了相同问题。论文的设计更准确的描述是 paired controlled comparison / crossover design（同一实例、同一种子、两种策略），而非严格的 Rubin potential outcomes 意义上的 counterfactual。虽然用法不算错误（确实回答了"如果用另一策略会怎样"），但一个 footnote 或 Section 3 开头的简短定位声明就能消除歧义。

**[AGREE] R1-W5: Cross-environment probes 缺乏中间验证**
同意，这与我的 N2 一致。ScienceWorld（death-dominated, DAF≈90%）、MATH（no signal, near-identical accuracy）、ALFWorld（information asymmetry, no death）构成了信号空间的三个极端。缺少一个 **intermediate case**——例如 death 存在但 DAF 在 30-60% 范围的环境——使得框架在中间地带的诊断能力未经验证。WebShop 或 InterCode 等有部分失败模式但不全是 catastrophic death 的环境可能是合适的候选。

**[AGREE] R1-W6: Router 负面结果可能反映训练不足**
同意，这与我的 W4 一致。LoRA rank=8 在 245 episodes（Table 11: batch size 4, 8 epochs, gradient accumulation 8）上训练，数据量和模型容量都很小。Section 4.6 从 router 失败直接推出 "consistent with death-dominance" 是一个 non sequitur——至少需要排除以下替代假设：(a) 特征表示不够（仅用 LLM hidden states 而非 task features）；(b) 数据不足（245 episodes 对 binary classification 而言非常少）；(c) 评估指标的天花板（episode-level balanced accuracy 的 random baseline 是多少？）。

**[REBUT] R1-W7: Anti-cherry-picking 盲区——全部 30 tasks 都 death-dominated**
R1 的担忧方向正确（如果整个环境都是 death-dominated，发现就是关于 ScienceWorld 而非 routing），但论文的 anti-cherry-picking analysis（Section 4, page 5）已经提供了部分回应：
1. 被排除的 19 tasks 的 mean ΔDR = +38.2pp **exceeding** included tasks 的 +28.7pp（Appendix C, page 12），说明排除的子集比保留的子集 death asymmetry 更强——这与 cherry-picking（选 death-dominated tasks）的假设相反。
2. 排除的唯一例外是 `grow-plant`（intrinsically safe, zero deaths in both strategies），说明排除标准是 methodology-driven（pipeline development contamination、redundancy、zero-progress tasks）而非 signal-driven。
3. 但 R1 的 deeper point 成立：**即使排除不是 cherry-picking，如果 ScienceWorld 作为整体就是 death-dominated 环境，那么发现的 scope 就是 "ScienceWorld is death-dominated"** 而非 "routing signal is generally death-dominated"。论文的 Limitations（page 8）承认了这一点，但 title 和 abstract 的 framing 仍然过强。

---

### Minor

**[AGREE] R1-W8: Spearman ρ=0.586 vs Pearson r=0.97 的差异**
这是一个重要的统计观察。正文 Figure 3（page 5）突出展示 r=0.97（"near-perfect correlation"），而 Appendix D（page 12）报告的 Spearman ρ=0.586 远低于此。Pearson r 对极端值敏感，K=11 个点中如果有 1-2 个高 death rate 任务（如 Table 2 中 `chemistry-mix` 的 Δ_int=+47.50），就可能驱动 r 的膨胀。ρ=0.586 虽然仍显著（p<0.05），但远不能称为 "near-perfect"。正文应报告两个相关系数并讨论差异。

**[AGREE] R1-W9: Eq.(4) 近似缺 worst-case bound**
同意这是一个技术缺口，但影响有限。Eq.(4) 的近似残差为 0.23（占 Δ_tot 的 0.8%），实际误差很小。然而，正式给出一个 bound（例如基于 death-conditional score 分布的 range）会强化论证的严谨性。

**[AGREE] R1-W10: "708-scale" 疑为排版错误**
Abstract 中 "three model families (7B-708B) at 708-scale" 确实令人困惑。论文使用的最大模型是 Qwen2.5-72B（Table 3, page 6），而非 708B。"708" 可能是 "70.8B" 的小数点丢失或 "70B" 的排版错误。Table 3 中的 "708" 出现在 "7-708 parameters" 列，进一步支持这是一个格式问题。需要更正。

---

### Questions

**[AGREE] R1-Q1: ΔDR 作为 P-invariant 指标**
ΔDR=28.7pp 确实是 P-invariant 的，且核心观察（death asymmetry 存在且 magnitude 大）在 ΔDR 框架下仍然成立。但 "78.9% of routing labels" 和 "DAF=90.4%" 这两个标志性数字都依赖于 P=100。如果论文将核心 claim 重新锚定在 ΔDR 上（"death rate differential accounts for the largest share of routing-relevant variation"），则对 P-dependence 的批评会大幅减弱，且结论本质不变。这是一个值得采纳的 reframing。

**[AGREE] R1-Q2: Non-oracle deterministic baseline**
如我在 W2 回应中所述，这是分离 oracle effect 与 strategy effect 的关键控制实验。一个可行的设计：deterministic strategy 仅使用 LLM 可观察到的信息（observation text）而非 simulator state，但仍使用 deterministic action selection logic。如果 non-oracle deterministic 的 death rate 接近 internal（~42.9%），则 death asymmetry 主要来自 oracle access；如果仍远低于 internal，则策略结构本身有独立的安全效果。

**[AGREE] R1-Q3: Table 12 vs §4.5 evaluation protocol**
Table 12（Appendix J, page 14）使用 6-seed cross-split evaluation（step-level 和 episode-level 两种协议），而 Section 4.5（page 7）的 baselines 是在固定 seed 上的 single-trial evaluation。这两个 protocol 的 accuracy 数字不直接可比——Table 12 的 47.1 ± 5.4% 是 cross-validated mean，而 Section 4.5 报告的 always-deterministic 96.3% 是 oracle-agreement rate 而非 balanced accuracy。正文确实需要更明确地区分这两个评估框架。

**[AGREE] R1-Q4: P=100 是否 arbitrarily high**
P=100 是 ScienceWorld 的**内置惩罚**（page 4: "P > 0 (P = 100 in ScienceWorld)"），不是作者的选择。ScienceWorld 的 score range 为 0-100，death 导致 score 归零，因此 P=100 意味着死亡抹去全部进度。但问题在于：ScienceWorld **选择了**一个极端的 all-or-nothing 惩罚结构，而论文将在这种极端结构下的发现泛化为关于 routing 的一般性结论。论文应明确讨论 P/max_score 比值对 DAF 的影响——在 P/max_score ≈ 1 时 death dominance 是预期的，在 P/max_score << 1 时可能不成立。

---

### Missing References

**[AGREE]** R1 建议的三篇引用均有直接相关性：
- **Uesato et al., 2022** (process vs outcome feedback)：与 step-level vs episode-level evaluation 的区分直接相关，论文的 Algorithm 1 实质上是一种 outcome-based labeling。
- **Lightman et al., 2023** (process reward models)：与 router 训练的 supervision signal 选择相关——如果 step-level labels 信息量更大，PRM-style supervision 可能改善 router 性能（回应 W6 的替代假设之一）。
- **Snell et al., 2024** (scaling test-time compute)：与 adaptive computation routing 的 compute-optimal 决策直接相关，且在 "何时分配更多推理资源" 的问题上提供了互补视角。

---

### 总结：R2 对 R1 意见的整体评估

R1 的三个 critical issues（W1 P-dependence、W2 oracle tautology、W3 cluster bootstrap）中，W1 和 W2 我**完全同意**——这是论文最根本的问题，我在自己的独立审稿中也作为 N1 提出。W3 我**部分反驳**——K=11 是 cluster bootstrap 的已知局限，但论文的核心推断不依赖于此。

R1 给出的 3.5（Borderline Conference）略高于我的 3.0（Findings）。差异主要在 Excitement：R1 给 3.5/5，我给 2/5。我认为在 oracle privilege + P-dependence 两个因素叠加下，核心发现的 novelty 受损程度更大，框架本身虽有方法论价值但贡献量级更适合 Findings。

---

[Reviewer 2 审稿结果]:
交叉回应已提交。对 R1 的 14 个点（W1-W10 + Q1-Q4）逐条给出了判断：

- **AGREE**：W1, W2, W4, W5, W6, W8, W9, W10, Q1-Q4 及全部 missing references（共 13 项）
- **REBUT**：W3（cluster bootstrap 非核心推断链瓶颈）、W7（部分反驳——anti-cherry-picking 数据不支持 cherry-picking 假设，但 deeper scope 问题成立）

两位 reviewer 在核心问题上高度一致：DAF 的 P-dependence 和 oracle privilege 下 death dominance 的 triviality 风险是最关键的弱点。主要分歧在 Excitement 维度——R1 给 3.5, 我给 2.0，我认为两个因素叠加后 novelty 受损更严重。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2750 · 2026-05-25T21:35:22.730944+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2751 · 2026-05-25T21:35:22.781665+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2752 · 2026-05-25T21:35:25.844759+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
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

_source line 2753 · 2026-05-25T21:35:25.896592+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2754 · 2026-05-25T21:35:32.273031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2755 · 2026-05-25T21:35:33.278490+00:00_

1	# Round 31 Review Issues — Fresh review (2 reviewers: R1 方法严谨性+实验设计, R2 新颖性+完整性+写作)
2	# R31 is a fresh review; prior rounds' resolved/wont_fix issues carried over unchanged.
3	
4	# =============================================
5	# Carried-over resolved issues (from prior rounds)
6	# =============================================
7	
8	- id: "R13-W1"
9	  summary: "正文篇幅严重不足 long paper 要求"
10	  category: format
11	  severity: warning
12	  status: resolved
13	  first_raised_round: 13
14	  last_seen_round: 14
15	  resolution: "正文已扩展至 8 页"
16	  resolution_round: 14
17	
18	- id: "R13-W2"
19	  summary: "Router 训练实验存在多个 confound"
20	  category: experiment
21	  severity: warning
22	  status: resolved
23	  first_raised_round: 13
24	  last_seen_round: 15
25	  resolution: "1.7B dip 有可检验假说，augmentation 术语修正，N 统一"
26	  resolution_round: 15
27	
28	- id: "R13-W3"
29	  summary: "Episode-level label → step-level training 的 mislabeling 未被量化"
30	  category: method
31	  severity: info
32	  status: resolved
33	  first_raised_round: 13
34	  last_seen_round: 14
35	  resolution: "Limitations 和 Appendix B 已充分量化"
36	  resolution_round: 14
37	
38	- id: "R13-W4"
39	  summary: "SCI 方法贡献与实际使用不成比例"
40	  category: method
41	  severity: info
42	  status: resolved
43	  first_raised_round: 13
44	  last_seen_round: 14
45	  resolution: "SCI 已降级到 Appendix A"
46	  resolution_round: 14
47	
48	- id: "R13-W7"
49	  summary: "Router negative results 解释不完整"
50	  category: experiment
51	  severity: warning
52	  status: resolved
53	  first_raised_round: 13
54	  last_seen_round: 15
55	  resolution: "Router 实验定位为 diagnostic probe"
56	  resolution_round: 15
57	
58	- id: "R13-m2"
59	  summary: "Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld"
60	  category: writing
61	  severity: warning
62	  status: resolved
63	  first_raised_round: 13
64	  last_seen_round: 16
65	  resolution: "Figure 3 已移除，数据在 Table 2 和正文中完整呈现"
66	  resolution_round: 16
67	
68	- id: "R13-m3"
69	  summary: "Reference 格式不统一 + orphan entries"
70	  category
…[truncated 25857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 2756 · 2026-05-25T21:35:33.280541+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2757 · 2026-05-25T21:35:33.331712+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2758 · 2026-05-25T21:46:24.943328+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "# Round 32 Review Issues — Fresh review (2 reviewers: R1 方法严谨性+实验设计, R2 新颖性+完整性+写作)\n# Updated after cross-response convergence. Prior rounds' resolved/wont_fix issues carried over.\n\n# =============================================\n# Carried-over resolved issues (from prior rounds)\n# =============================================\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Wild cluster CI 修正且降级为 sensitivity analysis；non-clustered bootstrap 为主推断\"\n  resolution_round: 24\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 30\n  resolution: \"R30 移除 Cohen's d，精简至 4 个统计量，168 词\"\n  resolution_round: 30\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Ng 1999, Northcutt 2021, DivideMix 已添加\"\n  resolution_round: 24\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 24\n  resolution: \"§5 Non-triviality 段有效回应 novelty 质疑\"\n  resolution_round: 24\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组\"\n  resolution_round: 19\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"Limitations 新增 pure-strategy upper bound 段落\"\n  resolution_round: 24\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"术语全局修正为 text augmentation\"\n  resolution_round: 24\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"P-invariance 适用范围明确量化\"\n  resolution_round: 24\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"4B router 结论 qualified；完整统计处理\"\n  resolution_round: 24\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Router claim 从绝对否定改为有条件否定\"\n  resolution_round: 24\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"措辞软化 + effect size detection threshold 完整报告\"\n  resolution_round: 24\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 non-learnability 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R18-N1 解决\"\n  resolution_round: 24\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"'structurally determined' → 'empirically dominated'\"\n  resolution_round: 24\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 不显著问题\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Per-task 结果标注为 exploratory\"\n  resolution_round: 24\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entries + Webb 年份\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"清理完毕\"\n  resolution_round: 24\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman, Mihatsch, Natarajan\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"所有缺失引用已补充\"\n  resolution_round: 24\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Appendix Overview 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M4\"\n  summary: \"§3.1 术语首次出现未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"术语已修正并定义\"\n  resolution_round: 24\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 agreement 声明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Single annotator caveat 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"§5 已讨论\"\n  resolution_round: 24\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R17-M1 解决\"\n  resolution_round: 24\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"交叉引用指向 §2.1 operationalization\"\n  resolution_round: 24\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"Appendix B 加 circularity caveat\"\n  resolution_round: 24\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 讨论深度不足\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"引用已补全；8 页限制无法展开\"\n  resolution_round: 24\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语歧义\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"修正为 computation modes\"\n  resolution_round: 24\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"§3.1 binary structure 讨论充分\"\n  resolution_round: 24\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"72B decomposition 完整报告\"\n  resolution_round: 24\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"被 R20-N2 取代并解决\"\n  resolution_round: 24\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 未被引用\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"Appendix L 已引用\"\n  resolution_round: 24\n\n- id: \"R19-W1\"\n  summary: \"缺 penalty magnitude 实验验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"P-invariance by design 论证覆盖\"\n  resolution_round: 24\n\n- id: \"R19-N1\"\n  summary: \"Framework vs finding 定位不清\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 27\n  resolution: \"统一为 empirical analysis + reusable diagnostic methodology\"\n  resolution_round: 27\n\n- id: \"R26-N3\"\n  summary: \"Strawman framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 26\n  last_seen_round: 27\n  resolution: \"R27 验收确认修复完好\"\n  resolution_round: 27\n\n- id: \"R28-M2\"\n  summary: \"Pages 7-8 纯文本无 display item\"\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 28\n  last_seen_round: 31\n  resolution: \"8 页限制下无法插入 display item\"\n  resolution_round: 28\n  mentions:\n    - round: 31\n      source: \"Visual Check\"\n      note: \"R31 视觉审查再次标记 pages 7-8 纯文本无 figure/table，建议加 summary bar chart\"\n\n- id: \"R28-M4\"\n  summary: \"Figure 2 仅 11 点无 task name label\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 28\n  last_seen_round: 29\n  resolution: \"Figure 2 已缩至 0.38\\\\textwidth\"\n  resolution_round: 28\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 30\n  resolution: \"R30 确认正文 ≤8 页\"\n  resolution_round: 30\n\n- id: \"R29-N1\"\n  summary: \"正文超出 8 页限制（复发）\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 30\n  resolution: \"R30 确认正文 ≤8 页\"\n  resolution_round: 30\n\n- id: \"R27-N2\"\n  summary: \"DAF=90.4% framing 过度突出\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 30\n  resolution: \"R30: Intro 重构——降低 DAF 权重，突出 oracle degeneracy 96.3%、72B 5 int-pref、Reflexion DAF>100%。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R27-N3\"\n  summary: \"Deterministic strategy 实为 oracle access，跨环境含义不统一\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 30\n  resolution: \"R30: §2.1 加 umbrella term（privileged-information strategy）；Discussion 加 Δ_nd=2.84 oracle privilege 回应 + ALFWorld DAF=0% 对照。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R27-N4\"\n  summary: \"环境覆盖过窄\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 32\n  resolution: \"结构性限制。Limitations/hedging 已到位。Conclusion 加 future work。\"\n  resolution_round: 30\n  mentions:\n    - round: 31\n      source: \"R1-W1, R2-W3\"\n      note: \"R31 fresh review 再次将单一主环境标记为 critical——两位 Reviewer 共识认为需要至少第二个 death-dominated 环境验证\"\n    - round: 32\n      source: \"R1-W5, R2-N2\"\n      note: \"R32 fresh review 两位 Reviewer 再次共识 [AGREE x2]：cross-env probes 仅覆盖极端（ScienceWorld/MATH/ALFWorld），缺中间验证（DAF 30-60%）\"\n\n- id: \"R27-W1\"\n  summary: \"Router negative result framing\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 30\n  resolution: \"R30: §3.5 title → 'Inconclusive Results'，正文 'inconclusive under current data regime'。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R27-W2\"\n  summary: \"Actionability 有限，Decision Framework 被埋\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 30\n  resolution: \"R30: Discussion 合并 oracle degeneracy 96.3% + Decision Framework 摘要 + action-level filter。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R27-W4\"\n  summary: \"Excluded tasks prescreening 样本量小\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 32\n  resolution: \"Anti-cherry-picking analysis 已到位。全 30 task types 列为 future work。\"\n  resolution_round: 30\n  mentions:\n    - round: 32\n      source: \"R1-W7 (R2 partial rebut)\"\n      note: \"R32 R1 质疑全 30 tasks 可能都是 death-dominated。R2 反驳 cherry-picking 指控（排除子集 ΔDR 更高）但同意 scope 限制。Director 判断：cherry-picking 不成立，但 scope 限制真实——回归 R27-N4。\"\n\n- id: \"R27-W5\"\n  summary: \"K=11 cluster bootstrap CI\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 30\n  resolution: \"R2 rebut 有效。论文已自我限定。\"\n  resolution_round: 30\n\n- id: \"R28-N1\"\n  summary: \"Episode-level vs step-level 粒度失配\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R29-R30 均未再提及，prior fix 有效\"\n  resolution_round: 30\n\n- id: \"R28-W1\"\n  summary: \"72B scaling 仅做 probe\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R30: 降级 'preliminary probe' + DAF CI [86.1%, 97.9%] + 修正 5 int-pref (非 0)。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R28-W2\"\n  summary: \"'Death' 术语限制 generality\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R29-R30 均未再提及\"\n  resolution_round: 30\n\n- id: \"R28-M1\"\n  summary: \"Missing references: hallucination detection, early exit\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R30: SelfCheckGPT + Kadavath 2022 + DeeBERT + PABEE 已加入 §4。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R28-M3\"\n  summary: \"Introduction/Discussion/Conclusion 重复度高\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R30: Discussion 压缩 3→2 段去重；Conclusion 扩展含 future work 且无与 Intro 重复。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R28-M5\"\n  summary: \"Related Work 缺 non-agent adaptive computation\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R30: DeeBERT + PABEE early exit positioning 句已加入 §4。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R29-W1\"\n  summary: \"Non-death 21.1% routing signal 来源未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 30\n  resolution: \"R30: Appendix U 加系统分析（三分类 + Table）+ §3.1 摘要句。诚实承认 20 个 labels 全部来自 find-non-living-thing。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R29-W2\"\n  summary: \"单一 death mechanism (focus on) 限制 generalizability\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 30\n  resolution: \"R30: Limitations 加 grounding ablation 定量估算 (+26.6pp→~+8pp) + future work。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R29-M1\"\n  summary: \"Missing references: FrugalGPT, AutoMix 等\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 30\n  resolution: \"R29 已添加。R30 确认存在。\"\n  resolution_round: 30\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 32\n  resolution: \"结构性——单一环境 + diagnostic contribution type。Findings 定位合理。\"\n  resolution_round: 30\n  mentions:\n    - round: 31\n      source: \"R2-W3\"\n      note: \"R31 再次标记 contribution type 对 Main Conference 偏弱，两位 Reviewer 共识 3.0 Findings\"\n    - round: 32\n      source: \"R1 Excitement 3.5/5, R2 Excitement 2/5\"\n      note: \"R32 两位 Reviewer 再次分歧：R1 认为诊断范式有方法论价值（3.5），R2 认为 oracle+P-dep 叠加后 novelty 受损严重（3.0）。Director 综合 3.0 Findings。\"\n\n- id: \"R30-W1\"\n  summary: \"'Deterministic' 术语跨环境含义不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 30\n  resolution: \"§2.1 加 umbrella term 括号说明（privileged-information strategy + 三环境 operationalizations）。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R30-W2\"\n  summary: \"Abstract 数字过密，Cohen's d 不适合 abstract\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 30\n  resolution: \"移除 d=3.02，精简至 4 个统计量，168 词。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R30-W3\"\n  summary: \"Grounding ablation 后未重新收集 counterfactual 计算 DAF\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 30\n  last_seen_round: 32\n  resolution: \"DDL 前不可行。Limitations 加定量估算 (+26.6pp→~+8pp) + future work。\"\n  resolution_round: 30\n  mentions:\n    - round: 31\n      source: \"R1-Q5, R2-Q5\"\n      note: \"R31 两位 Reviewer 均追问 grounding ablation 后 DAF 是否仍成立\"\n    - round: 32\n      source: \"R1, R2\"\n      note: \"R32 两位 Reviewer 再次在 Questions 中提及。仍为结构性限制。\"\n\n# =============================================\n# R31 issues (from prior round, updated with R32 status)\n# =============================================\n\n- id: \"R31-N1\"\n  summary: \"单一主环境 + diagnostic-only 定位限制 Main Conference 级别\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-W1, R2-W1, R2-W3\"\n      note: \"[AGREE x2] 两位 Reviewer 共识：核心实证发现仅在 ScienceWorld 验证，cross-env probes 反证了 generalizability，contribution type 更适合 Findings。映射到历史 R27-N4（环境覆盖过窄）和 R16-N1（novelty deficit），属结构性限制。\"\n    - round: 32\n      source: \"R1-W1/W2, R2-N1/N2\"\n      note: \"R32 两位 Reviewer 再次独立识别相同问题。交叉回应全部 [AGREE]。R1 补充 scope 问题：如果全部 30 tasks 都是 death-dominated，发现仅关于 ScienceWorld。\"\n\n- id: \"R31-N2\"\n  summary: \"Oracle privilege 使 death avoidance 发现接近 tautology\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-W2\"\n      note: \"Deterministic 策略 = simulator forking（极强 oracle），death avoidance 本质上 = oracle prevents irreversible errors。真正非直觉的洞见是 Δ_nd≈2.84（non-death gap 极小），但论文将此作为 DAF 副产品而非核心发现呈现。映射到历史 R27-N3，R30 已加 umbrella term 和 Δ_nd 讨论，但 R31 fresh reviewer 认为仍不够突出。\"\n    - round: 32\n      source: \"R1-W2, R2-N1 cross-response\"\n      note: \"R32 [AGREE x2]。R2 补充：non-oracle deterministic baseline 是分离 oracle effect 与 strategy effect 的关键控制实验。如果 non-oracle det 的 death rate 接近 internal（~42.9%），则 death asymmetry 主要来自 oracle access。\"\n\n- id: \"R31-W1\"\n  summary: \"DAF 对 P 的单调依赖需更谨慎处理——headline 应用 label fraction\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-W4, R2-W2\"\n      note: \"[AGREE x2] DAF=δP/(δP+Δ_nd) 随 P 单调递增是数学事实。论文已在 §2.4 承认并以 label fraction 为 primary，但 Abstract/Intro/Conclusion 仍多处突出 DAF=90.4%。建议进一步降低 DAF 在 headline 位置的权重。映射到历史 R27-N2（DAF framing 过度突出），R30 已部分修复。\"\n    - round: 32\n      source: \"R1-W1, R2-N1 cross-response\"\n      note: \"R32 [AGREE x2]。R2 补充数学论证：DAF 公式在 P→∞ 时 DAF→1 是数学必然而非经验发现。R1 建议 ΔDR=28.7pp 作为 P-invariant 替代指标，R2 同意。\"\n\n- id: \"R31-W2\"\n  summary: \"K=11 cluster bootstrap 推断——应以非参数检验为主\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-W3\"\n      note: \"论文建议读者依赖非聚类 bootstrap CI 但同时承认 within-cluster correlation 存在——逻辑不自洽。建议将 permutation test / sign test 作为主要推断依据。映射到历史 R13-N2 和 R27-W5，prior rounds resolved 但 fresh reviewer 认为 messaging 仍有改进空间。\"\n    - round: 32\n      source: \"R2 cross-response [REBUT]\"\n      note: \"R2 反驳：论文核心推断使用 episode-level bootstrap（N=245），cluster bootstrap 仅为 sensitivity analysis。论文在 Appendix E 已主动承认 K=11 局限。补充统计检验（LOO, sign test, permutation p=0.002）支撑充分。Director 判断：R2 rebut 有效，维持 warning 非 critical。\"\n\n- id: \"R31-W3\"\n  summary: \"Episode→step 粒度错配限制框架实用性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-W5\"\n      note: \"框架产出 episode-level labels 但 routing 需 step-level 决策。88% uninformative steps。实用价值收窄为 sanity check。映射到历史 R18-N1 和 R28-N1，prior rounds resolved 但 R31 fresh reviewer 认为仍需更明确定位。\"\n    - round: 32\n      source: \"R1-W5, R2-N2\"\n      note: \"R32 交叉回应中 R1 和 R2 均认为 cross-env probes 过于初步，ALFWorld 缺完整 DAF 分解，episode→step gap 仍未充分解决。\"\n\n- id: \"R31-W4\"\n  summary: \"72B probe 缺 cross-model replication at scale\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-W6\"\n      note: \"7-9B 有三个模型族，但 72B 仅 Qwen2.5-72B 一个数据点。Intro 将 72B 与三个模型族并列可能高估 robustness。映射到历史 R28-W1，R30 已降级 'preliminary probe'。\"\n    - round: 32\n      source: \"cross-response\"\n      note: \"R32 交叉回应中未被重点讨论，但 R1 在 W6 中再次提及 capacity scaling 不足。维持 warning。\"\n\n- id: \"R31-W5\"\n  summary: \"Appendix 过多（21 个, 15 页）正文依赖过重\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R2-W4\"\n      note: \"核心 claim 的支撑证据分散在 Appendix（K, M, Q, R），读者无法仅通过正文评估贡献。\"\n    - round: 32\n      source: \"R1 cross-response [AGREE]\"\n      note: \"R32 R1 同意。特别强调 Appendix K（P sensitivity）直接关系核心 claim 稳健性，应在正文讨论，而非藏在附录。\"\n\n- id: \"R31-W6\"\n  summary: \"Related Work 缺 risk-sensitive RL / CVaR 文献\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R2-W5\"\n      note: \"CVaR optimization（Chow 2015, Tamar 2015）直接处理 trajectory-level catastrophic risk，与 death avoidance 高度相关。§4 未讨论。\"\n    - round: 32\n      source: \"R1 cross-response [AGREE]\"\n      note: \"R1 同意 risk-sensitive RL 引用必要性。Dabney 2018 也应补充。Agent failure taxonomy（Kambhampati 2024, Valmeekam 2023）也获共识。\"\n\n- id: \"R31-W7\"\n  summary: \"'Counterfactual' 术语使用松散\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R2-W6\"\n      note: \"方法更接近 matched-seed A/B testing 而非 Pearl (2009) structural counterfactual。需要在 §2.1 明确定义。\"\n    - round: 32\n      source: \"R1 [AGREE], R2 [AGREE] cross-response\"\n      note: \"R32 [AGREE x2]。两位 Reviewer 共识：用法不算错误但与因果推断标准用法有偏差。建议 §3 开头加简短定位声明即可消除歧义。\"\n\n- id: \"R31-W8\"\n  summary: \"Discussion section 过薄（~0.5 page，仅 2 个话题）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R2-W8\"\n      note: \"缺条件分析（when does death avoidance dominate?）和与 concurrent work 的对话。\"\n    - round: 32\n      source: \"cross-response\"\n      note: \"R32 交叉回应中隐含：R2 建议 P/max_score 条件分析应在 Discussion 展开。\"\n\n- id: \"R31-M1\"\n  summary: \"Abstract 信息密度仍偏高\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R2-M1\"\n      note: \"前 2 句 6+ 数值。映射到历史 R13-W5（R30 resolved），fresh reviewer 仍感觉偏密。\"\n    - round: 32\n      source: \"cross-response\"\n      note: \"R32 未在交叉回应中重点讨论。维持 info。\"\n\n- id: \"R31-M2\"\n  summary: \"Figure 1 配色偏素，Figure 2 axis label 偏小\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R2-M2, Visual Check\"\n      note: \"Figure 1 灰/米色为主缺对比度；Figure 2 legend 约 6-7pt 偏小。\"\n    - round: 32\n      source: \"Visual Check\"\n      note: \"R32 视觉审查再次确认 Figure 2 axis label ≤6pt，Figure 4 文字标签也偏小。\"\n\n- id: \"R31-M3\"\n  summary: \"RTX 5090 硬件可能泄露作者身份\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-M6\"\n      note: \"如果 RTX 5090 尚未公开发售，使用此硬件可能违反 double-blind。\"\n    - round: 32\n      source: \"cross-response\"\n      note: \"R32 交叉回应中未讨论。维持 info。\"\n\n- id: \"R31-M4\"\n  summary: \"SCI 在正文仅出现一次，与 Method 中的显著度不匹配\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-M5\"\n      note: \"SCI 列为框架三大组件之一但正文只用了一次。映射到历史 R13-W4（已降级到 Appendix），但 R31 认为 Method §2 中仍 over-prominent。\"\n    - round: 32\n      source: \"cross-response\"\n      note: \"R32 交叉回应中未讨论。维持 info。\"\n\n- id: \"R31-M5\"\n  summary: \"Limitations 章节偏长（~1.5 页, 5 段）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-M1\"\n      note: \"内容全部是必要讨论，但对 ARR mandatory limitations 来说偏长。\"\n    - round: 32\n      source: \"cross-response\"\n      note: \"R32 交叉回应中未讨论。维持 info。\"\n\n- id: \"R31-M6\"\n  summary: \"Missing references: AgentGym, OSWorld, Trial-and-Error, CVaR\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-R1/R2/R3, R2-R1/R2\"\n      note: \"AgentGym (Xi 2024), OSWorld (Xie 2024), Trial-and-Error (Wang 2024), Chow 2015 CVaR, Tamar 2015 CVaR\"\n    - round: 32\n      source: \"R1, R2 cross-response\"\n      note: \"R32 交叉回应扩展缺失引用列表：+Uesato 2022 (process vs outcome), +Lightman 2023 (PRM), +Snell 2024 (scaling test-time compute), +Dabney 2018 (IQN), +Kambhampati 2024, +Valmeekam 2023 (agent failure taxonomy)。\"\n\n# =============================================\n# R32 新发现（交叉回应中首次出现或独立识别）\n# =============================================\n\n- id: \"R32-W1\"\n  summary: \"Router 训练负面结果过度推断——应区分 signal absence 与 learnability failure\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - round: 32\n      source: \"R1-W6, R2-W4\"\n      note: \"[AGREE x2] LoRA rank=8, 245 episodes, Qwen2.5-7B 单一配置。Appendix P capacity scaling 显示 4B 时 episode-level accuracy 才勉强超过 random。R2 列出三个替代假设：特征表示不够、数据不足、评估天花板。结论应从 'no signal' 改为 'signal not learnable with this setup'。\"\n\n- id: \"R32-W2\"\n  summary: \"Spearman ρ=0.586 vs Pearson r=0.97 巨大差异未报告\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - round: 32\n      source: \"R1-W8, R2 [AGREE]\"\n      note: \"正文 Figure 3 突出 r=0.97 ('near-perfect') 但 Appendix D 的 ρ=0.586 远低。Pearson r 对极端值敏感，K=11 中少数高 death rate 任务可能驱动膨胀。ρ=0.586 显著但远不能称为 near-perfect。正文应同时报告两个系数。\"\n\n- id: \"R32-M1\"\n  summary: \"'708-scale' 疑为排版错误（应为 '70B-scale'）\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - round: 32\n      source: \"R1-W10, R2 [AGREE]\"\n      note: \"Abstract 'three model families (7B-708B) at 708-scale' 中最大模型为 Qwen2.5-72B。708 可能是 70B 或 70.8B 的排版错误。\"\n\n- id: \"R32-M2\"\n  summary: \"Table 2 D/I/N 列标题不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - round: 32\n      source: \"R1, R2 [AGREE]\"\n      note: \"需查 caption 才能理解 D/I/N 含义。建议改为 Det/Int/NoPref 或加表头脚注。\"\n\n- id: \"R32-M3\"\n  summary: \"§4.3 未报告 Retry/Reflexion intervention 对 DAF 的影响\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - round: 32\n      source: \"R1 cross-response, R2 [AGREE]\"\n      note: \"Table 1 报告了 Retry (43.5%) 和 Reflexion (31.4%) 的 death rate，但未报告 DAF 是否同步变化。无论结果如何都有信息量——加强或暴露 death avoidance 作为 routing signal 的稳健性。\"\n\n- id: \"R32-M4\"\n  summary: \"Eq.(4) 近似缺 worst-case bound\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - round: 32\n      source: \"R1-W9, R2 [AGREE]\"\n      note: \"残差 0.23（占 Δ_tot 的 0.8%）虽小，但正式给出 bound（如基于 death-conditional score 分布 range）会强化论证严谨性。\"\n\n- id: \"R32-M5\"\n  summary: \"Pages 5 和 7 display item 密度过高\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - round: 32\n      source: \"Visual Check\"\n      note: \"Page 5: 4 个 display items（Figure 3 + Figure 4 + Table 1 + Table 2）；Page 7: 3 个（Figure 5 + Figure 6 + Table 5）。连续形成图表密集带。建议将 Table 2 移至 page 6。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "simgate-modular-routing",
    "issues_yaml": "# Round 32 Review Issues — Fresh review (2 reviewers: R1 方法严谨性+实验设计, R2 新颖性+完整性+写作)\n# Updated after cross-response convergence. Prior rounds' resolved/wont_fix issues carried over.\n\n# =============================================\n# Carried-over resolved issues (from prior rounds)\n# =============================================\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Wild cluster CI 修正且降级为 sensitivity analysis；non-clustered bootstrap 为主推断\"\n  resolution_round: 24\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 30\n  resolution: \"R30 移除 Cohen's d，精简至 4 个统计量，168 词\"\n  resolution_round: 30\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Ng 1999, Northcutt 2021, DivideMix 已添加\"\n  resolution_round: 24\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 24\n  resolution: \"§5 Non-triviality 段有效回应 novelty 质疑\"\n  resolution_round: 24\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组\"\n  resolution_round: 19\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"Limitations 新增 pure-strategy upper bound 段落\"\n  resolution_round: 24\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"术语全局修正为 text augmentation\"\n  resolution_round: 24\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"P-invariance 适用范围明确量化\"\n  resolution_round: 24\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"4B router 结论 qualified；完整统计处理\"\n  resolution_round: 24\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Router claim 从绝对否定改为有条件否定\"\n  resolution_round: 24\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"措辞软化 + effect size detection threshold 完整报告\"\n  resolution_round: 24\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 non-learnability 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R18-N1 解决\"\n  resolution_round: 24\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"'structurally determined' → 'empirically dominated'\"\n  resolution_round: 24\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 不显著问题\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Per-task 结果标注为 exploratory\"\n  resolution_round: 24\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entries + Webb 年份\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"清理完毕\"\n  resolution_round: 24\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman, Mihatsch, Natarajan\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"所有缺失引用已补充\"\n  resolution_round: 24\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Appendix Overview 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M4\"\n  summary: \"§3.1 术语首次出现未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"术语已修正并定义\"\n  resolution_round: 24\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 agreement 声明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Single annotator caveat 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"§5 已讨论\"\n  resolution_round: 24\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R17-M1 解决\"\n  resolution_round: 24\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"交叉引用指向 §2.1 operationalization\"\n  resolution_round: 24\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"Appendix B 加 circularity caveat\"\n  resolution_round: 24\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 讨论深度不足\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"引用已补全；8 页限制无法展开\"\n  resolution_round: 24\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语歧义\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"修正为 computation modes\"\n  resolution_round: 24\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"§3.1 binary structure 讨论充分\"\n  resolution_round: 24\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"72B decomposition 完整报告\"\n  resolution_round: 24\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"被 R20-N2 取代并解决\"\n  resolution_round: 24\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 未被引用\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"Appendix L 已引用\"\n  resolution_round: 24\n\n- id: \"R19-W1\"\n  summary: \"缺 penalty magnitude 实验验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"P-invariance by design 论证覆盖\"\n  resolution_round: 24\n\n- id: \"R19-N1\"\n  summary: \"Framework vs finding 定位不清\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 27\n  resolution: \"统一为 empirical analysis + reusable diagnostic methodology\"\n  resolution_round: 27\n\n- id: \"R26-N3\"\n  summary: \"Strawman framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 26\n  last_seen_round: 27\n  resolution: \"R27 验收确认修复完好\"\n  resolution_round: 27\n\n- id: \"R28-M2\"\n  summary: \"Pages 7-8 纯文本无 display item\"\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 28\n  last_seen_round: 31\n  resolution: \"8 页限制下无法插入 display item\"\n  resolution_round: 28\n  mentions:\n    - round: 31\n      source: \"Visual Check\"\n      note: \"R31 视觉审查再次标记 pages 7-8 纯文本无 figure/table，建议加 summary bar chart\"\n\n- id: \"R28-M4\"\n  summary: \"Figure 2 仅 11 点无 task name label\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 28\n  last_seen_round: 29\n  resolution: \"Figure 2 已缩至 0.38\\\\textwidth\"\n  resolution_round: 28\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 30\n  resolution: \"R30 确认正文 ≤8 页\"\n  resolution_round: 30\n\n- id: \"R29-N1\"\n  summary: \"正文超出 8 页限制（复发）\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 30\n  resolution: \"R30 确认正文 ≤8 页\"\n  resolution_round: 30\n\n- id: \"R27-N2\"\n  summary: \"DAF=90.4% framing 过度突出\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 30\n  resolution: \"R30: Intro 重构——降低 DAF 权重，突出 oracle degeneracy 96.3%、72B 5 int-pref、Reflexion DAF>100%。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R27-N3\"\n  summary: \"Deterministic strategy 实为 oracle access，跨环境含义不统一\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 30\n  resolution: \"R30: §2.1 加 umbrella term（privileged-information strategy）；Discussion 加 Δ_nd=2.84 oracle privilege 回应 + ALFWorld DAF=0% 对照。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R27-N4\"\n  summary: \"环境覆盖过窄\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 32\n  resolution: \"结构性限制。Limitations/hedging 已到位。Conclusion 加 future work。\"\n  resolution_round: 30\n  mentions:\n    - round: 31\n      source: \"R1-W1, R2-W3\"\n      note: \"R31 fresh review 再次将单一主环境标记为 critical——两位 Reviewer 共识认为需要至少第二个 death-dominated 环境验证\"\n    - round: 32\n      source: \"R1-W5, R2-N2\"\n      note: \"R32 fresh review 两位 Reviewer 再次共识 [AGREE x2]：cross-env probes 仅覆盖极端（ScienceWorld/MATH/ALFWorld），缺中间验证（DAF 30-60%）\"\n\n- id: \"R27-W1\"\n  summary: \"Router negative result framing\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 30\n  resolution: \"R30: §3.5 title → 'Inconclusive Results'，正文 'inconclusive under current data regime'。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R27-W2\"\n  summary: \"Actionability 有限，Decision Framework 被埋\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 30\n  resolution: \"R30: Discussion 合并 oracle degeneracy 96.3% + Decision Framework 摘要 + action-level filter。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R27-W4\"\n  summary: \"Excluded tasks prescreening 样本量小\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 32\n  resolution: \"Anti-cherry-picking analysis 已到位。全 30 task types 列为 future work。\"\n  resolution_round: 30\n  mentions:\n    - round: 32\n      source: \"R1-W7 (R2 partial rebut)\"\n      note: \"R32 R1 质疑全 30 tasks 可能都是 death-dominated。R2 反驳 cherry-picking 指控（排除子集 ΔDR 更高）但同意 scope 限制。Director 判断：cherry-picking 不成立，但 scope 限制真实——回归 R27-N4。\"\n\n- id: \"R27-W5\"\n  summary: \"K=11 cluster bootstrap CI\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 30\n  resolution: \"R2 rebut 有效。论文已自我限定。\"\n  resolution_round: 30\n\n- id: \"R28-N1\"\n  summary: \"Episode-level vs step-level 粒度失配\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R29-R30 均未再提及，prior fix 有效\"\n  resolution_round: 30\n\n- id: \"R28-W1\"\n  summary: \"72B scaling 仅做 probe\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R30: 降级 'preliminary probe' + DAF CI [86.1%, 97.9%] + 修正 5 int-pref (非 0)。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R28-W2\"\n  summary: \"'Death' 术语限制 generality\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R29-R30 均未再提及\"\n  resolution_round: 30\n\n- id: \"R28-M1\"\n  summary: \"Missing references: hallucination detection, early exit\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R30: SelfCheckGPT + Kadavath 2022 + DeeBERT + PABEE 已加入 §4。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R28-M3\"\n  summary: \"Introduction/Discussion/Conclusion 重复度高\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R30: Discussion 压缩 3→2 段去重；Conclusion 扩展含 future work 且无与 Intro 重复。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R28-M5\"\n  summary: \"Related Work 缺 non-agent adaptive computation\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"R30: DeeBERT + PABEE early exit positioning 句已加入 §4。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R29-W1\"\n  summary: \"Non-death 21.1% routing signal 来源未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 30\n  resolution: \"R30: Appendix U 加系统分析（三分类 + Table）+ §3.1 摘要句。诚实承认 20 个 labels 全部来自 find-non-living-thing。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R29-W2\"\n  summary: \"单一 death mechanism (focus on) 限制 generalizability\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 30\n  resolution: \"R30: Limitations 加 grounding ablation 定量估算 (+26.6pp→~+8pp) + future work。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R29-M1\"\n  summary: \"Missing references: FrugalGPT, AutoMix 等\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 30\n  resolution: \"R29 已添加。R30 确认存在。\"\n  resolution_round: 30\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 32\n  resolution: \"结构性——单一环境 + diagnostic contribution type。Findings 定位合理。\"\n  resolution_round: 30\n  mentions:\n    - round: 31\n      source: \"R2-W3\"\n      note: \"R31 再次标记 contribution type 对 Main Conference 偏弱，两位 Reviewer 共识 3.0 Findings\"\n    - round: 32\n      source: \"R1 Excitement 3.5/5, R2 Excitement 2/5\"\n      note: \"R32 两位 Reviewer 再次分歧：R1 认为诊断范式有方法论价值（3.5），R2 认为 oracle+P-dep 叠加后 novelty 受损严重（3.0）。Director 综合 3.0 Findings。\"\n\n- id: \"R30-W1\"\n  summary: \"'Deterministic' 术语跨环境含义不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 30\n  resolution: \"§2.1 加 umbrella term 括号说明（privileged-information strategy + 三环境 operationalizations）。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R30-W2\"\n  summary: \"Abstract 数字过密，Cohen's d 不适合 abstract\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 30\n  resolution: \"移除 d=3.02，精简至 4 个统计量，168 词。Reviewer 验收 PASS。\"\n  resolution_round: 30\n\n- id: \"R30-W3\"\n  summary: \"Grounding ablation 后未重新收集 counterfactual 计算 DAF\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 30\n  last_seen_round: 32\n  resolution: \"DDL 前不可行。Limitations 加定量估算 (+26.6pp→~+8pp) + future work。\"\n  resolution_round: 30\n  mentions:\n    - round: 31\n      source: \"R1-Q5, R2-Q5\"\n      note: \"R31 两位 Reviewer 均追问 grounding ablation 后 DAF 是否仍成立\"\n    - round: 32\n      source: \"R1, R2\"\n      note: \"R32 两位 Reviewer 再次在 Questions 中提及。仍为结构性限制。\"\n\n# =============================================\n# R31 issues (from prior round, updated with R32 status)\n# =============================================\n\n- id: \"R31-N1\"\n  summary: \"单一主环境 + diagnostic-only 定位限制 Main Conference 级别\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-W1, R2-W1, R2-W3\"\n      note: \"[AGREE x2] 两位 Reviewer 共识：核心实证发现仅在 ScienceWorld 验证，cross-env probes 反证了 generalizability，contribution type 更适合 Findings。映射到历史 R27-N4（环境覆盖过窄）和 R16-N1（novelty deficit），属结构性限制。\"\n    - round: 32\n      source: \"R1-W1/W2, R2-N1/N2\"\n      note: \"R32 两位 Reviewer 再次独立识别相同问题。交叉回应全部 [AGREE]。R1 补充 scope 问题：如果全部 30 tasks 都是 death-dominated，发现仅关于 ScienceWorld。\"\n\n- id: \"R31-N2\"\n  summary: \"Oracle privilege 使 death avoidance 发现接近 tautology\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-W2\"\n      note: \"Deterministic 策略 = simulator forking（极强 oracle），death avoidance 本质上 = oracle prevents irreversible errors。真正非直觉的洞见是 Δ_nd≈2.84（non-death gap 极小），但论文将此作为 DAF 副产品而非核心发现呈现。映射到历史 R27-N3，R30 已加 umbrella term 和 Δ_nd 讨论，但 R31 fresh reviewer 认为仍不够突出。\"\n    - round: 32\n      source: \"R1-W2, R2-N1 cross-response\"\n      note: \"R32 [AGREE x2]。R2 补充：non-oracle deterministic baseline 是分离 oracle effect 与 strategy effect 的关键控制实验。如果 non-oracle det 的 death rate 接近 internal（~42.9%），则 death asymmetry 主要来自 oracle access。\"\n\n- id: \"R31-W1\"\n  summary: \"DAF 对 P 的单调依赖需更谨慎处理——headline 应用 label fraction\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-W4, R2-W2\"\n      note: \"[AGREE x2] DAF=δP/(δP+Δ_nd) 随 P 单调递增是数学事实。论文已在 §2.4 承认并以 label fraction 为 primary，但 Abstract/Intro/Conclusion 仍多处突出 DAF=90.4%。建议进一步降低 DAF 在 headline 位置的权重。映射到历史 R27-N2（DAF framing 过度突出），R30 已部分修复。\"\n    - round: 32\n      source: \"R1-W1, R2-N1 cross-response\"\n      note: \"R32 [AGREE x2]。R2 补充数学论证：DAF 公式在 P→∞ 时 DAF→1 是数学必然而非经验发现。R1 建议 ΔDR=28.7pp 作为 P-invariant 替代指标，R2 同意。\"\n\n- id: \"R31-W2\"\n  summary: \"K=11 cluster bootstrap 推断——应以非参数检验为主\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-W3\"\n      note: \"论文建议读者依赖非聚类 bootstrap CI 但同时承认 within-cluster correlation 存在——逻辑不自洽。建议将 permutation test / sign test 作为主要推断依据。映射到历史 R13-N2 和 R27-W5，prior rounds resolved 但 fresh reviewer 认为 messaging 仍有改进空间。\"\n    - round: 32\n      source: \"R2 cross-response [REBUT]\"\n      note: \"R2 反驳：论文核心推断使用 episode-level bootstrap（N=245），cluster bootstrap 仅为 sensitivity analysis。论文在 Appendix E 已主动承认 K=11 局限。补充统计检验（LOO, sign test, permutation p=0.002）支撑充分。Director 判断：R2 rebut 有效，维持 warning 非 critical。\"\n\n- id: \"R31-W3\"\n  summary: \"Episode→step 粒度错配限制框架实用性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-W5\"\n      note: \"框架产出 episode-level labels 但 routing 需 step-level 决策。88% uninformative steps。实用价值收窄为 sanity check。映射到历史 R18-N1 和 R28-N1，prior rounds resolved 但 R31 fresh reviewer 认为仍需更明确定位。\"\n    - round: 32\n      source: \"R1-W5, R2-N2\"\n      note: \"R32 交叉回应中 R1 和 R2 均认为 cross-env probes 过于初步，ALFWorld 缺完整 DAF 分解，episode→step gap 仍未充分解决。\"\n\n- id: \"R31-W4\"\n  summary: \"72B probe 缺 cross-model replication at scale\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-W6\"\n      note: \"7-9B 有三个模型族，但 72B 仅 Qwen2.5-72B 一个数据点。Intro 将 72B 与三个模型族并列可能高估 robustness。映射到历史 R28-W1，R30 已降级 'preliminary probe'。\"\n    - round: 32\n      source: \"cross-response\"\n      note: \"R32 交叉回应中未被重点讨论，但 R1 在 W6 中再次提及 capacity scaling 不足。维持 warning。\"\n\n- id: \"R31-W5\"\n  summary: \"Appendix 过多（21 个, 15 页）正文依赖过重\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R2-W4\"\n      note: \"核心 claim 的支撑证据分散在 Appendix（K, M, Q, R），读者无法仅通过正文评估贡献。\"\n    - round: 32\n      source: \"R1 cross-response [AGREE]\"\n      note: \"R32 R1 同意。特别强调 Appendix K（P sensitivity）直接关系核心 claim 稳健性，应在正文讨论，而非藏在附录。\"\n\n- id: \"R31-W6\"\n  summary: \"Related Work 缺 risk-sensitive RL / CVaR 文献\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R2-W5\"\n      note: \"CVaR optimization（Chow 2015, Tamar 2015）直接处理 trajectory-level catastrophic risk，与 death avoidance 高度相关。§4 未讨论。\"\n    - round: 32\n      source: \"R1 cross-response [AGREE]\"\n      note: \"R1 同意 risk-sensitive RL 引用必要性。Dabney 2018 也应补充。Agent failure taxonomy（Kambhampati 2024, Valmeekam 2023）也获共识。\"\n\n- id: \"R31-W7\"\n  summary: \"'Counterfactual' 术语使用松散\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R2-W6\"\n      note: \"方法更接近 matched-seed A/B testing 而非 Pearl (2009) structural counterfactual。需要在 §2.1 明确定义。\"\n    - round: 32\n      source: \"R1 [AGREE], R2 [AGREE] cross-response\"\n      note: \"R32 [AGREE x2]。两位 Reviewer 共识：用法不算错误但与因果推断标准用法有偏差。建议 §3 开头加简短定位声明即可消除歧义。\"\n\n- id: \"R31-W8\"\n  summary: \"Discussion section 过薄（~0.5 page，仅 2 个话题）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R2-W8\"\n      note: \"缺条件分析（when does death avoidance dominate?）和与 concurrent work 的对话。\"\n    - round: 32\n      source: \"cross-response\"\n      note: \"R32 交叉回应中隐含：R2 建议 P/max_score 条件分析应在 Discussion 展开。\"\n\n- id: \"R31-M1\"\n  summary: \"Abstract 信息密度仍偏高\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R2-M1\"\n      note: \"前 2 句 6+ 数值。映射到历史 R13-W5（R30 resolved），fresh reviewer 仍感觉偏密。\"\n    - round: 32\n      source: \"cross-response\"\n      note: \"R32 未在交叉回应中重点讨论。维持 info。\"\n\n- id: \"R31-M2\"\n  summary: \"Figure 1 配色偏素，Figure 2 axis label 偏小\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R2-M2, Visual Check\"\n      note: \"Figure 1 灰/米色为主缺对比度；Figure 2 legend 约 6-7pt 偏小。\"\n    - round: 32\n      source: \"Visual Check\"\n      note: \"R32 视觉审查再次确认 Figure 2 axis label ≤6pt，Figure 4 文字标签也偏小。\"\n\n- id: \"R31-M3\"\n  summary: \"RTX 5090 硬件可能泄露作者身份\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-M6\"\n      note: \"如果 RTX 5090 尚未公开发售，使用此硬件可能违反 double-blind。\"\n    - round: 32\n      source: \"cross-response\"\n      note: \"R32 交叉回应中未讨论。维持 info。\"\n\n- id: \"R31-M4\"\n  summary: \"SCI 在正文仅出现一次，与 Method 中的显著度不匹配\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-M5\"\n      note: \"SCI 列为框架三大组件之一但正文只用了一次。映射到历史 R13-W4（已降级到 Appendix），但 R31 认为 Method §2 中仍 over-prominent。\"\n    - round: 32\n      source: \"cross-response\"\n      note: \"R32 交叉回应中未讨论。维持 info。\"\n\n- id: \"R31-M5\"\n  summary: \"Limitations 章节偏长（~1.5 页, 5 段）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-M1\"\n      note: \"内容全部是必要讨论，但对 ARR mandatory limitations 来说偏长。\"\n    - round: 32\n      source: \"cross-response\"\n      note: \"R32 交叉回应中未讨论。维持 info。\"\n\n- id: \"R31-M6\"\n  summary: \"Missing references: AgentGym, OSWorld, Trial-and-Error, CVaR\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - round: 31\n      source: \"R1-R1/R2/R3, R2-R1/R2\"\n      note: \"AgentGym (Xi 2024), OSWorld (Xie 2024), Trial-and-Error (Wang 2024), Chow 2015 CVaR, Tamar 2015 CVaR\"\n    - round: 32\n      source: \"R1, R2 cross-response\"\n      note: \"R32 交叉回应扩展缺失引用列表：+Uesato 2022 (process vs outcome), +Lightman 2023 (PRM), +Snell 2024 (scaling test-time compute), +Dabney 2018 (IQN), +Kambhampati 2024, +Valmeekam 2023 (agent failure taxonomy)。\"\n\n# =============================================\n# R32 新发现（交叉回应中首次出现或独立识别）\n# =============================================\n\n- id: \"R32-W1\"\n  summary: \"Router 训练负面结果过度推断——应区分 signal absence 与 learnability failure\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - round: 32\n      source: \"R1-W6, R2-W4\"\n      note: \"[AGREE x2] LoRA rank=8, 245 episodes, Qwen2.5-7B 单一配置。Appendix P capacity scaling 显示 4B 时 episode-level accuracy 才勉强超过 random。R2 列出三个替代假设：特征表示不够、数据不足、评估天花板。结论应从 'no signal' 改为 'signal not learnable with this setup'。\"\n\n- id: \"R32-W2\"\n  summary: \"Spearman ρ=0.586 vs Pearson r=0.97 巨大差异未报告\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - round: 32\n      source: \"R1-W8, R2 [AGREE]\"\n      note: \"正文 Figure 3 突出 r=0.97 ('near-perfect') 但 Appendix D 的 ρ=0.586 远低。Pearson r 对极端值敏感，K=11 中少数高 death rate 任务可能驱动膨胀。ρ=0.586 显著但远不能称为 near-perfect。正文应同时报告两个系数。\"\n\n- id: \"R32-M1\"\n  summary: \"'708-scale' 疑为排版错误（应为 '70B-scale'）\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - round: 32\n      source: \"R1-W10, R2 [AGREE]\"\n      note: \"Abstract 'three model families (7B-708B) at 708-scale' 中最大模型为 Qwen2.5-72B。708 可能是 70B 或 70.8B 的排版错误。\"\n\n- id: \"R32-M2\"\n  summary: \"Table 2 D/I/N 列标题不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - round: 32\n      source: \"R1, R2 [AGREE]\"\n      note: \"需查 caption 才能理解 D/I/N 含义。建议改为 Det/Int/NoPref 或加表头脚注。\"\n\n- id: \"R32-M3\"\n  summary: \"§4.3 未报告 Retry/Reflexion intervention 对 DAF 的影响\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - round: 32\n      source: \"R1 cross-response, R2 [AGREE]\"\n      note: \"Table 1 报告了 Retry (43.5%) 和 Reflexion (31.4%) 的 death rate，但未报告 DAF 是否同步变化。无论结果如何都有信息量——加强或暴露 death avoidance 作为 routing signal 的稳健性。\"\n\n- id: \"R32-M4\"\n  summary: \"Eq.(4) 近似缺 worst-case bound\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - round: 32\n      source: \"R1-W9, R2 [AGREE]\"\n      note: \"残差 0.23（占 Δ_tot 的 0.8%）虽小，但正式给出 bound（如基于 death-conditional score 分布 range）会强化论证严谨性。\"\n\n- id: \"R32-M5\"\n  summary: \"Pages 5 和 7 display item 密度过高\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - round: 32\n      source: \"Visual Check\"\n      note: \"Page 5: 4 个 display items（Figure 3 + Figure 4 + Table 1 + Table 2）；Page 7: 3 个（Figure 5 + Figure 6 + Table 5）。连续形成图表密集带。建议将 Table 2 移至 page 6。\""
  }
}
```

</details>

---


### Tool result

_source line 2759 · 2026-05-25T21:46:25.105284+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 30151}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 161
}
```

</details>

---


### Tool call

_source line 2760 · 2026-05-25T21:49:29.349331+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 32 审稿报告\n\n**Venue**: EMNLP 2026 (ARR)  |  **Reviewers**: 2  |  **Rounds**: 1（交叉回应后收敛）  |  **模式**: Fresh review\n\n---\n\n## Summary\n\n本文提出 Death Avoidance Framework (DAF)，用于诊断 LLM agent 多策略路由中的信号组成。通过在 ScienceWorld 环境中对 deterministic 和 internal 两种策略进行 matched-seed paired comparison，论文发现 78.9% 的路由标签由 death avoidance 驱动（DAF=90.4% at P=100），并在 3 个模型族（7B-72B）和 2 个 agent improvement 方法下验证了该发现的稳健性。论文还在 MATH 和 ALFWorld 进行了跨环境 probe，分别显示 no routing signal 和 information asymmetry-dominated signal。\n\n## Strengths\n\n**S1. \"先诊断再路由\"的范式价值**：不同于直接学习 router 的主流方法，论文提出先分解 routing signal 的组成——这一 diagnostic 视角具有独立的方法论贡献（R1 Excitement 3.5/5）。\n\n**S2. 实验设计严谨**：matched-seed paired comparison 设计、完整的 anti-cherry-picking 分析（排除的 19 个 task 的 ΔDR=+38.2pp > 保留的 +28.7pp）、多层统计检验（episode-level bootstrap CI、permutation test p=0.002、leave-one-out、sign test）。\n\n**S3. 多维稳健性验证**：3 个模型族（Qwen2.5/Llama-3.1/Gemma-2）、2 个 agent improvement 方法（Retry/Reflexion）、72B 规模 probe——核心发现在多维度下保持稳健。\n\n**S4. 负面结果的诚实报告**：router 训练失败（§3.5）和跨环境 probe 的零/弱信号结果（Table 5）均如实报告，而非隐藏或 spin 为正面发现。\n\n**S5. 材料完整性**：21 个附录提供了全面的补充分析、failure mode 分类、sensitivity analysis 和 ablation study。\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**[C1] 核心发现的 Triviality 风险——P-dependence + Oracle Privilege 双重叠加** [R1-W1, R1-W2, R2-N1; AGREE x2]\n\n论文的两个标志性数字（DAF=90.4%, label fraction=78.9%）受到两个独立因素的质疑：\n\n(a) **P-dependence**：DAF = 1 − Δ_nd/(Δ^P + Δ_nd) 在数学上保证 P→∞ 时 DAF→1。Appendix K 显示 P=0 时 DAF=7.4%，P=100 时 DAF=90.4%——\"death dominance\" 的强度是惩罚参数的单调函数而非环境的固有属性。虽然 label fraction 78.9% 是 P-invariant 的，但正文对两者的区分不够清晰，且 headline positions（Abstract/Intro）仍多处突出 DAF=90.4%。\n\n(b) **Oracle privilege**：deterministic strategy 通过 privileged simulator access（§3.1）直接读取环境状态，其 death rate 16.3% vs internal 的 42.9%（Table 1）在很大程度上源于信息不对称而非策略类型差异。缺少 non-oracle deterministic baseline 作为控制实验来分离 oracle effect 与 strategy effect。\n\n两个因素叠加后，核心发现接近 \"强 oracle 在高惩罚环境中避免灾难性失败\" 这一不言自明的结论。\n\n**建议**：(1) 将 headline claim 锚定在 P-invariant 指标（ΔDR=28.7pp）上；(2) 补充 non-oracle deterministic baseline；(3) 将贡献从 \"discover death dominance\" 重新定位为 \"provide diagnostic framework that quantifies routing signal composition\"。\n\n**[C2] 跨环境验证严重不足** [R1-W5, R2-N2; AGREE x2]\n\n三个环境仅覆盖信号空间的极端：ScienceWorld（death-dominated, DAF≈90%）、MATH（no signal, near-identical accuracy）、ALFWorld（information asymmetry, no death）。缺少中间验证——例如 death 存在但 DAF 在 30-60% 范围的环境。框架在中间地带的诊断能力未经检验。\n\nALFWorld 的 probe 尤其初步：仅报告 label 分布，未做完整 DAF 分解。考虑到 ALFWorld 的 Δ_int = -10.70（Table 5），其 information asymmetry 机制值得深入分析。\n\n如果 ScienceWorld 整体就是 death-dominated 环境（所有 30 个 task 的 ΔDR 均 >0），发现的 scope 可能仅为 \"ScienceWorld is death-dominated\" 而非 \"routing signal is generally death-dominated\"。\n\n### Should-Fix (Warning)\n\n**[W1] DAF 公式的 P-dependence 需在正文充分讨论** [R1-W1, R2-W1; AGREE x2]\n\nPenalty sensitivity analysis（Appendix K）直接关系到核心 claim 的稳健性。目前正文对 P-dependence 几乎一笔带过（§3.4 仅脚注提到 P*=100），读者需翻到第 16 页才能看到 DAF 随 P 变化的全貌。这不是补充分析，而是核心方法论问题被放在了附录中。建议将 Appendix K 核心结论移至正文 §3.4。\n\n**[W2] \"Counterfactual\" 术语使用松散** [R1-W4, R2-W3; AGREE x2]\n\n论文的 paired controlled comparison 设计（同一实例、同一种子、两种策略）在 ScienceWorld 的确定性环境中确实可以观测两个 potential outcomes，但 \"counterfactual\" 与因果推断文献（Rubin 1974, Pearl 2009）的标准用法存在偏差。distributional decomposition ≠ causal decomposition。建议在 §3 开头加简短定位声明。\n\n**[W3] Router 训练负面结果的过度推断** [R1-W6, R2-W4; AGREE x2]\n\n从 LoRA rank=8、245 episodes、Qwen2.5-7B 的单一配置得出 \"no exploitable signal\" 是过度推断。Appendix P 的 capacity scaling（0.6B → 4B）显示 episode-level accuracy 仅在 4B 时勉强超过 random baseline，这更可能是 data/capacity insufficiency 而非 signal absence。论文应区分 \"no signal exists\" 与 \"signal not learnable with this setup\"。替代假设包括：特征表示不够（仅 LLM hidden states）、数据不足（245 episodes 对 binary classification）、评估指标天花板。\n\n**[W4] 附录体量异常（21 节, ~15 页）** [R2-W1; R1 AGREE]\n\n关键的 Penalty sensitivity（App K）、Failure mode analysis（App N）、Grounding ablation（App O）直接关系核心 claim，但被放在附录深处。读者无法仅通过正文评估贡献的稳健性。建议将 App K 的核心结论移至正文 §3.4。\n\n**[W5] Spearman ρ=0.586 与 Pearson r=0.97 的巨大差异** [R1-W8; R2 AGREE]\n\n正文 Figure 3 突出展示 Pearson r=0.97（\"near-perfect correlation\"），但 Appendix D 的 Spearman ρ=0.586 远低于此。Pearson r 对极端值敏感，K=11 个点中少数高 death rate 任务（如 chemistry-mix Δ_int=+47.50）可能驱动 r 的膨胀。ρ=0.586 虽仍显著（p<0.05）但远不能称为 \"near-perfect\"。正文应同时报告两个相关系数并讨论差异原因。\n\n**[W6] Discussion 过薄** [R2-W8]\n\nDiscussion section（~0.5 页, 2 个话题）缺少关键讨论：(1) death avoidance 何时/何条件下 dominate（P/max_score 条件分析）；(2) 与 concurrent adaptive routing work 的对话；(3) 与 risk-sensitive RL / CVaR 的概念连接。\n\n**[W7] Related Work 缺 Risk-sensitive RL / CVaR 文献** [R2-W5; R1 AGREE]\n\nDeath avoidance 与 risk-sensitive RL 的 tail-risk minimization（CVaR, Tamar 2015; Chow 2015; Dabney 2018）在概念上高度相关——论文将 death 视为 catastrophic failure，正是 CVaR 优化的场景。§2 或 §5 应引用并讨论连接。Agent failure taxonomy（Kambhampati 2024, Valmeekam 2023）与 Appendix N 的 failure mode analysis 直接相关，也应引用。\n\n### Minor\n\n**[M1] \"708-scale\" 疑为排版错误** [R1-W10; R2 AGREE]\nAbstract 中 \"three model families (7B-708B) at 708-scale\" 中最大模型为 Qwen2.5-72B（Table 3）。\"708\" 可能是 \"70B\" 或 \"70.8B\" 的排版错误。需更正。\n\n**[M2] Table 2 D/I/N 列标题不直观** [R1; R2 AGREE]\n需查 caption 才能理解。建议改为 Det/Int/NoPref 或在表头加脚注。\n\n**[M3] §4.3 未报告 intervention 对 DAF 的影响** [R1; R2 AGREE]\nRetry 和 Reflexion 改变了 death rate（Table 1: Retry 43.5%, Reflexion 31.4%），但未报告 DAF 是否同步变化。这会加强或暴露 death avoidance 作为 routing signal 的稳健性/脆弱性，无论结果如何都有信息量。\n\n**[M4] Eq.(4) 近似缺 worst-case bound** [R1-W9; R2 AGREE]\n残差 0.23（占 Δ_tot 的 0.8%）虽小，但正式给出 bound（如基于 death-conditional score 分布 range）会强化论证严谨性。\n\n**[M5] Figure 2/4 字号偏小** [Visual Check; R1 noted]\nFigure 2 axis label 和 legend ≤6pt，Figure 4 action sequence 文字标签偏小，150 dpi 下已难辨认。\n\n**[M6] Pages 5/7 图表密度过高** [Visual Check]\nPage 5 包含 4 个 display items（Figure 3 + Figure 4 + Table 1 + Table 2），Page 7 包含 3 个（Figure 5 + Figure 6 + Table 5），连续形成\"图表密集带\"。建议将 Table 2 移至 page 6。\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上完全一致（AGREE x2）：\n\n1. **P-dependence + Oracle privilege 双重叠加**使核心发现接近 tautology（Critical）\n2. **跨环境验证仅覆盖极端**，缺少中间 case（Critical）\n3. **\"Counterfactual\" 术语**需明确定位（Warning）\n4. **Router 负面结果**可能反映训练不足而非信号缺失（Warning）\n5. **附录过重**，核心 claim 支撑材料被埋在附录中（Warning）\n6. **Spearman vs Pearson 差异**需在正文讨论（Warning）\n7. **Missing references**: Risk-sensitive RL/CVaR, Agent failure taxonomy, Uesato 2022, Lightman 2023, Snell 2024\n\n## Reviewer Divergence\n\n**[D1] K=11 Cluster Bootstrap（R1-W3 vs R2 REBUT）**\nR1 认为 K=11 低于推荐阈值（K≥20-50），cluster bootstrap CI 可能不可靠。R2 反驳——论文核心推断使用 episode-level bootstrap（N=245），cluster bootstrap 仅为 sensitivity analysis，且论文已在 Appendix E 主动承认其局限性。补充统计检验（LOO, sign test, permutation p=0.002）支撑充分。\n**Director 判断**：R2 的反驳有效。核心推断链不依赖 cluster bootstrap。维持 Warning 而非 Critical。\n\n**[D2] Anti-cherry-picking / Scope（R1-W7 vs R2 partial REBUT）**\nR1 质疑全部 30 tasks 可能都是 death-dominated，发现仅关于 ScienceWorld 而非 routing。R2 反驳——排除的 19 tasks 的 ΔDR (+38.2pp) > 保留的 (+28.7pp)，这与 cherry-picking 假设相反。但 R2 同意 deeper scope 问题成立：即使无 cherry-picking，如果 ScienceWorld 整体就是 death-dominated，发现的 scope 就是 \"ScienceWorld is death-dominated\"。\n**Director 判断**：cherry-picking 指控不成立，但 scope 限制真实——回归 C2（跨环境验证不足）。\n\n**[D3] Concurrent Work 差异化（R2-W2 vs R1 REBUT）**\nR2 认为与 concurrent work 差异化不够锐利。R1 反驳——§2 Related Work 的差异化讨论不只是一句话，已有较大篇幅区分 \"先诊断再路由\" vs \"直接学 router\" 的核心差异。\n**Director 判断**：R1 的反驳部分有效。差异化已有基础，但增加显式 comparison table 仍有价值。降级为建议而非 Weakness。\n\n**[D4] Excitement / Overall Score**\nR1 给 3.5（Borderline Conference），Excitement 3.5/5；R2 给 3.0（Findings），Excitement 2/5。\n分歧核心：R1 认为 \"先诊断再路由\" 范式本身有方法论贡献，即使具体发现 information content 有限；R2 认为 oracle + P-dependence 双重叠加后 novelty 受损严重，框架贡献量级更适合 Findings。\n**Director 判断**：采纳 3.0。两个 Critical 问题均获双方共识，Excitement 均值 2.75/5 低于 Conference 门槛，贡献类型在当前实证基础上更适合 Findings。\n\n## Questions\n\n**Q1. ΔDR 重新锚定**：如果将核心 claim 从 DAF=90.4% 重新锚定在 P-invariant 的 ΔDR=28.7pp 上，结论本质不变但对 P-dependence 批评的抵抗力大幅增强。作者是否愿意采纳？\n\n**Q2. Non-oracle deterministic baseline**：是否可以设计 non-oracle deterministic strategy（仅使用 LLM 可观察信息，deterministic action selection logic），以分离 oracle effect 与 strategy effect？如果 non-oracle deterministic 的 death rate 接近 internal（~42.9%），则 death asymmetry 主要来自 oracle access；如果仍远低于 internal，则策略结构本身有独立的安全效果。\n\n**Q3. Table 12 vs §4.5 评估协议差异**：Table 12 的 6-seed cross-split evaluation 与 §4.5 的固定 seed single-trial evaluation 的 accuracy 数字不直接可比——47.1±5.4%（cross-validated mean）vs always-deterministic 96.3%（oracle-agreement rate）。正文应更明确区分两个评估框架。\n\n**Q4. P=100 的环境特异性**：P=100 是 ScienceWorld 的内置惩罚（all-or-nothing, P/max_score ≈ 1），而非作者选择。论文应讨论 P/max_score 比值对 DAF 的影响——在 P/max_score ≈ 1 时 death dominance 是预期的，在 P/max_score << 1 时可能不成立。\n\n**Q5. Grounding ablation 后 DAF 重新计算**：当前 grounding ablation（Appendix O）仅报告 death rate 变化（+26.6pp → ~+8pp），未重新收集 counterfactual 计算 DAF。这是验证 \"death dominance vs grounding confusion\" 的关键缺失实验。\n\n## Missing References\n\n以下文献与论文主题直接相关但未被引用：\n\n1. **Risk-sensitive RL / CVaR**：Tamar et al. (2015) \"Optimizing the CVaR via Sampling\"; Chow et al. (2015) \"Risk-sensitive and robust decision-making\"; Dabney et al. (2018) \"Implicit quantile networks\"——death avoidance 本质是 tail-risk minimization\n2. **Agent failure taxonomy**：Kambhampati et al. (2024), Valmeekam et al. (2023)——LLM agent planning 局限性分析，与论文的 failure mode analysis（App N）直接相关\n3. **Process vs outcome feedback**：Uesato et al. (2022) \"Solving math word problems with process- and outcome-based feedback\"——Algorithm 1 实质是 outcome-based labeling\n4. **Process reward models**：Lightman et al. (2023) \"Let's Verify Step by Step\"——step-level supervision 可能改善 router 性能\n5. **Scaling test-time compute**：Snell et al. (2024)——adaptive computation routing 的 compute-optimal 决策\n\n注：Adaptive computation / early exit 文献（Universal Transformers, CALM）在抽象层次上与本文有本质差异（layer-level vs episode-level），引用非必要（R1 rebut 有效）。\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。**\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成**（耗时 ~3 分钟）\n\n| 严重度 | 位置 | 描述 |\n|--------|------|------|\n| ⚠️ Warning | Page 5 | 单页 4 个 display items（Figure 3 + Figure 4 + Table 1 + Table 2），视觉极度拥挤 |\n| ⚠️ Warning | Page 7 | 3 个 display items（Figure 5 + Figure 6 + Table 5），与 page 5 连续形成图表密集带 |\n| ⚠️ Warning | Page 3 | Figure 2 axis label 和 legend ≤6pt，低分辨率下难辨认 |\n| ⚠️ Warning | Page 5 | Figure 4 action sequence 文字标签字号过小 |\n| ℹ️ Info | Page 2 | Figure 1 framework 图整体清晰，部分箭头和小字标注缩小后不够醒目 |\n| ℹ️ Info | Page 5 | Figure 3 散点图单栏宽度，数据点拥挤，改为 figure* 全宽可提升可读性 |\n| ℹ️ Info | Page 6 | Table 3/4 booktabs 风格规范，最优值加粗 |\n| ℹ️ Info | Page 8 | Limitations 段落简短（~1/3 栏），符合 EMNLP 要求 |\n| ℹ️ Info | Pages 9-10 | References 排版正常，无未解析引用 |\n| ℹ️ Info | Page 11 | Appendix 目录 A-T 共 20 个附录，条目清晰 |\n| ℹ️ Info | Page 4 | Algorithm 1 伪代码和公式 (1)-(5) 渲染正确 |\n\n**统计**：0 Critical, 4 Warning, 11 Info\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3/5 | 2.5/5 | 2.5-3/5 |\n| Excitement | 3.5/5 | 2/5 | 2.5/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5 | 3.0 | **3.0** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**综合评分：3.0 (Findings)**\n\n**理由**：论文的 diagnostic framework 思路有方法论价值（S1），实验设计在给定设定下严谨（S2-S3），负面结果报告诚实（S4）。但两个结构性问题——(1) oracle privilege 使 death avoidance 发现接近预期结论（C1），(2) 单一主环境 + 极端跨环境 probe 无法支撑泛化性声明（C2）——从根本上限制了贡献的 novelty 和 scope。DAF 对 P 的数学单调依赖进一步削弱了标志性数字的说服力（W1）。\n\n论文适合作为 Findings 论文被接收，但需要在以下方面做出调整：(1) 贡献 reframing（diagnostic framework vs discovery）；(2) P-invariant 指标（ΔDR）作为 headline；(3) Spearman/Pearson 双报告；(4) 正文中正面处理 P-dependence。如果作者能进一步补充 non-oracle baseline 和 intermediate cross-env probe，论文可达到 Conference 水平（3.5-4.0）。\n\n两位 Reviewer 评分范围 3.0-3.5。Director 采纳 3.0 的主要权衡：(1) 两个 Critical 问题均获双方共识（AGREE x2）；(2) Excitement 均值 2.75/5 低于 Conference 门槛；(3) 贡献类型（diagnostic framework）在当前实证基础上更适合 Findings 定位。\n\n## Detailed Comments\n\n### §1 Introduction\n- \"708-scale\" 疑为排版错误，应为 \"70B-scale\"（M1）\n- DAF=90.4% 在 Introduction 中的突出程度应降低，考虑用 ΔDR=28.7pp 替代或并列展示（C1/W1）\n\n### §2 Method / Framework\n- \"Counterfactual\" 术语需在 §3 开头加定位声明——matched-seed paired comparison vs Rubin/Pearl counterfactual（W2）\n- SCI 在正文仅出现一次，与 Method 中的显著度不匹配——考虑进一步降级或在 Method 中缩减描述\n\n### §3 Results\n- Figure 3 应同时报告 Pearson r=0.97 和 Spearman ρ=0.586，并讨论差异原因（极端值敏感性）（W5）\n- Table 2 D/I/N 列标题改为 Det/Int/NoPref 或加表头脚注（M2）\n- §3.4 应将 Appendix K 的 P-sensitivity 核心结论（DAF 随 P 单调递增是数学必然）移入正文（W1/W4）\n- Eq.(4) 近似应给出 worst-case bound（M4）\n\n### §4 Analysis\n- §4.3 需补充 Retry/Reflexion 对 DAF 的影响——当前仅报告 death rate 变化（M3）\n- §4.5 需与 Table 12 的评估协议差异做明确区分——cross-validated mean vs oracle-agreement rate 不可比（Q3）\n- §4.6 Router 结论应从 \"no exploitable signal\" 改为 \"signal not learnable with this setup\"，并列出替代假设（W3）\n\n### §5 Discussion\n- 过薄（~0.5 页），需扩展（W6）：\n  - P/max_score 条件分析：何时 death avoidance dominate 是预期的 vs 有信息量的\n  - 与 CVaR / risk-sensitive RL 的概念连接\n  - 与 concurrent adaptive routing work 的对话\n  - Non-oracle deterministic baseline 的设计空间\n\n### Related Work (§4)\n- 补充 CVaR / risk-sensitive RL 文献（Tamar 2015, Chow 2015, Dabney 2018）（W7）\n- 补充 agent failure taxonomy（Kambhampati 2024, Valmeekam 2023）\n- 补充 process reward / test-time compute（Uesato 2022, Lightman 2023, Snell 2024）\n\n### Limitations\n- 长度适中（EMNLP 标准），但 5 段可适当精简至 3 段\n\n### Visual / Format\n- Page 5 图表密度过高——建议 Table 2 移至 page 6 或合并 Figure 3/4 为 subfigure（M6）\n- Figure 2 和 Figure 4 字号需增大至 ≥8pt（M5）\n- \"708\" 排版错误需更正（M1）",
  "project": "simgate-modular-routing",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 32 审稿报告\n\n**Venue**: EMNLP 2026 (ARR)  |  **Reviewers**: 2  |  **Rounds**: 1（交叉回应后收敛）  |  **模式**: Fresh review\n\n---\n\n## Summary\n\n本文提出 Death Avoidance Framework (DAF)，用于诊断 LLM agent 多策略路由中的信号组成。通过在 ScienceWorld 环境中对 deterministic 和 internal 两种策略进行 matched-seed paired comparison，论文发现 78.9% 的路由标签由 death avoidance 驱动（DAF=90.4% at P=100），并在 3 个模型族（7B-72B）和 2 个 agent improvement 方法下验证了该发现的稳健性。论文还在 MATH 和 ALFWorld 进行了跨环境 probe，分别显示 no routing signal 和 information asymmetry-dominated signal。\n\n## Strengths\n\n**S1. \"先诊断再路由\"的范式价值**：不同于直接学习 router 的主流方法，论文提出先分解 routing signal 的组成——这一 diagnostic 视角具有独立的方法论贡献（R1 Excitement 3.5/5）。\n\n**S2. 实验设计严谨**：matched-seed paired comparison 设计、完整的 anti-cherry-picking 分析（排除的 19 个 task 的 ΔDR=+38.2pp > 保留的 +28.7pp）、多层统计检验（episode-level bootstrap CI、permutation test p=0.002、leave-one-out、sign test）。\n\n**S3. 多维稳健性验证**：3 个模型族（Qwen2.5/Llama-3.1/Gemma-2）、2 个 agent improvement 方法（Retry/Reflexion）、72B 规模 probe——核心发现在多维度下保持稳健。\n\n**S4. 负面结果的诚实报告**：router 训练失败（§3.5）和跨环境 probe 的零/弱信号结果（Table 5）均如实报告，而非隐藏或 spin 为正面发现。\n\n**S5. 材料完整性**：21 个附录提供了全面的补充分析、failure mode 分类、sensitivity analysis 和 ablation study。\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**[C1] 核心发现的 Triviality 风险——P-dependence + Oracle Privilege 双重叠加** [R1-W1, R1-W2, R2-N1; AGREE x2]\n\n论文的两个标志性数字（DAF=90.4%, label fraction=78.9%）受到两个独立因素的质疑：\n\n(a) **P-dependence**：DAF = 1 − Δ_nd/(Δ^P + Δ_nd) 在数学上保证 P→∞ 时 DAF→1。Appendix K 显示 P=0 时 DAF=7.4%，P=100 时 DAF=90.4%——\"death dominance\" 的强度是惩罚参数的单调函数而非环境的固有属性。虽然 label fraction 78.9% 是 P-invariant 的，但正文对两者的区分不够清晰，且 headline positions（Abstract/Intro）仍多处突出 DAF=90.4%。\n\n(b) **Oracle privilege**：deterministic strategy 通过 privileged simulator access（§3.1）直接读取环境状态，其 death rate 16.3% vs internal 的 42.9%（Table 1）在很大程度上源于信息不对称而非策略类型差异。缺少 non-oracle deterministic baseline 作为控制实验来分离 oracle effect 与 strategy effect。\n\n两个因素叠加后，核心发现接近 \"强 oracle 在高惩罚环境中避免灾难性失败\" 这一不言自明的结论。\n\n**建议**：(1) 将 headline claim 锚定在 P-invariant 指标（ΔDR=28.7pp）上；(2) 补充 non-oracle deterministic baseline；(3) 将贡献从 \"discover death dominance\" 重新定位为 \"provide diagnostic framework that quantifies routing signal composition\"。\n\n**[C2] 跨环境验证严重不足** [R1-W5, R2-N2; AGREE x2]\n\n三个环境仅覆盖信号空间的极端：ScienceWorld（death-dominated, DAF≈90%）、MATH（no signal, near-identical accuracy）、ALFWorld（information asymmetry, no death）。缺少中间验证——例如 death 存在但 DAF 在 30-60% 范围的环境。框架在中间地带的诊断能力未经检验。\n\nALFWorld 的 probe 尤其初步：仅报告 label 分布，未做完整 DAF 分解。考虑到 ALFWorld 的 Δ_int = -10.70（Table 5），其 information asymmetry 机制值得深入分析。\n\n如果 ScienceWorld 整体就是 death-dominated 环境（所有 30 个 task 的 ΔDR 均 >0），发现的 scope 可能仅为 \"ScienceWorld is death-dominated\" 而非 \"routing signal is generally death-dominated\"。\n\n### Should-Fix (Warning)\n\n**[W1] DAF 公式的 P-dependence 需在正文充分讨论** [R1-W1, R2-W1; AGREE x2]\n\nPenalty sensitivity analysis（Appendix K）直接关系到核心 claim 的稳健性。目前正文对 P-dependence 几乎一笔带过（§3.4 仅脚注提到 P*=100），读者需翻到第 16 页才能看到 DAF 随 P 变化的全貌。这不是补充分析，而是核心方法论问题被放在了附录中。建议将 Appendix K 核心结论移至正文 §3.4。\n\n**[W2] \"Counterfactual\" 术语使用松散** [R1-W4, R2-W3; AGREE x2]\n\n论文的 paired controlled comparison 设计（同一实例、同一种子、两种策略）在 ScienceWorld 的确定性环境中确实可以观测两个 potential outcomes，但 \"counterfactual\" 与因果推断文献（Rubin 1974, Pearl 2009）的标准用法存在偏差。distributional decomposition ≠ causal decomposition。建议在 §3 开头加简短定位声明。\n\n**[W3] Router 训练负面结果的过度推断** [R1-W6, R2-W4; AGREE x2]\n\n从 LoRA rank=8、245 episodes、Qwen2.5-7B 的单一配置得出 \"no exploitable signal\" 是过度推断。Appendix P 的 capacity scaling（0.6B → 4B）显示 episode-level accuracy 仅在 4B 时勉强超过 random baseline，这更可能是 data/capacity insufficiency 而非 signal absence。论文应区分 \"no signal exists\" 与 \"signal not learnable with this setup\"。替代假设包括：特征表示不够（仅 LLM hidden states）、数据不足（245 episodes 对 binary classification）、评估指标天花板。\n\n**[W4] 附录体量异常（21 节, ~15 页）** [R2-W1; R1 AGREE]\n\n关键的 Penalty sensitivity（App K）、Failure mode analysis（App N）、Grounding ablation（App O）直接关系核心 claim，但被放在附录深处。读者无法仅通过正文评估贡献的稳健性。建议将 App K 的核心结论移至正文 §3.4。\n\n**[W5] Spearman ρ=0.586 与 Pearson r=0.97 的巨大差异** [R1-W8; R2 AGREE]\n\n正文 Figure 3 突出展示 Pearson r=0.97（\"near-perfect correlation\"），但 Appendix D 的 Spearman ρ=0.586 远低于此。Pearson r 对极端值敏感，K=11 个点中少数高 death rate 任务（如 chemistry-mix Δ_int=+47.50）可能驱动 r 的膨胀。ρ=0.586 虽仍显著（p<0.05）但远不能称为 \"near-perfect\"。正文应同时报告两个相关系数并讨论差异原因。\n\n**[W6] Discussion 过薄** [R2-W8]\n\nDiscussion section（~0.5 页, 2 个话题）缺少关键讨论：(1) death avoidance 何时/何条件下 dominate（P/max_score 条件分析）；(2) 与 concurrent adaptive routing work 的对话；(3) 与 risk-sensitive RL / CVaR 的概念连接。\n\n**[W7] Related Work 缺 Risk-sensitive RL / CVaR 文献** [R2-W5; R1 AGREE]\n\nDeath avoidance 与 risk-sensitive RL 的 tail-risk minimization（CVaR, Tamar 2015; Chow 2015; Dabney 2018）在概念上高度相关——论文将 death 视为 catastrophic failure，正是 CVaR 优化的场景。§2 或 §5 应引用并讨论连接。Agent failure taxonomy（Kambhampati 2024, Valmeekam 2023）与 Appendix N 的 failure mode analysis 直接相关，也应引用。\n\n### Minor\n\n**[M1] \"708-scale\" 疑为排版错误** [R1-W10; R2 AGREE]\nAbstract 中 \"three model families (7B-708B) at 708-scale\" 中最大模型为 Qwen2.5-72B（Table 3）。\"708\" 可能是 \"70B\" 或 \"70.8B\" 的排版错误。需更正。\n\n**[M2] Table 2 D/I/N 列标题不直观** [R1; R2 AGREE]\n需查 caption 才能理解。建议改为 Det/Int/NoPref 或在表头加脚注。\n\n**[M3] §4.3 未报告 intervention 对 DAF 的影响** [R1; R2 AGREE]\nRetry 和 Reflexion 改变了 death rate（Table 1: Retry 43.5%, Reflexion 31.4%），但未报告 DAF 是否同步变化。这会加强或暴露 death avoidance 作为 routing signal 的稳健性/脆弱性，无论结果如何都有信息量。\n\n**[M4] Eq.(4) 近似缺 worst-case bound** [R1-W9; R2 AGREE]\n残差 0.23（占 Δ_tot 的 0.8%）虽小，但正式给出 bound（如基于 death-conditional score 分布 range）会强化论证严谨性。\n\n**[M5] Figure 2/4 字号偏小** [Visual Check; R1 noted]\nFigure 2 axis label 和 legend ≤6pt，Figure 4 action sequence 文字标签偏小，150 dpi 下已难辨认。\n\n**[M6] Pages 5/7 图表密度过高** [Visual Check]\nPage 5 包含 4 个 display items（Figure 3 + Figure 4 + Table 1 + Table 2），Page 7 包含 3 个（Figure 5 + Figure 6 + Table 5），连续形成\"图表密集带\"。建议将 Table 2 移至 page 6。\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上完全一致（AGREE x2）：\n\n1. **P-dependence + Oracle privilege 双重叠加**使核心发现接近 tautology（Critical）\n2. **跨环境验证仅覆盖极端**，缺少中间 case（Critical）\n3. **\"Counterfactual\" 术语**需明确定位（Warning）\n4. **Router 负面结果**可能反映训练不足而非信号缺失（Warning）\n5. **附录过重**，核心 claim 支撑材料被埋在附录中（Warning）\n6. **Spearman vs Pearson 差异**需在正文讨论（Warning）\n7. **Missing references**: Risk-sensitive RL/CVaR, Agent failure taxonomy, Uesato 2022, Lightman 2023, Snell 2024\n\n## Reviewer Divergence\n\n**[D1] K=11 Cluster Bootstrap（R1-W3 vs R2 REBUT）**\nR1 认为 K=11 低于推荐阈值（K≥20-50），cluster bootstrap CI 可能不可靠。R2 反驳——论文核心推断使用 episode-level bootstrap（N=245），cluster bootstrap 仅为 sensitivity analysis，且论文已在 Appendix E 主动承认其局限性。补充统计检验（LOO, sign test, permutation p=0.002）支撑充分。\n**Director 判断**：R2 的反驳有效。核心推断链不依赖 cluster bootstrap。维持 Warning 而非 Critical。\n\n**[D2] Anti-cherry-picking / Scope（R1-W7 vs R2 partial REBUT）**\nR1 质疑全部 30 tasks 可能都是 death-dominated，发现仅关于 ScienceWorld 而非 routing。R2 反驳——排除的 19 tasks 的 ΔDR (+38.2pp) > 保留的 (+28.7pp)，这与 cherry-picking 假设相反。但 R2 同意 deeper scope 问题成立：即使无 cherry-picking，如果 ScienceWorld 整体就是 death-dominated，发现的 scope 就是 \"ScienceWorld is death-dominated\"。\n**Director 判断**：cherry-picking 指控不成立，但 scope 限制真实——回归 C2（跨环境验证不足）。\n\n**[D3] Concurrent Work 差异化（R2-W2 vs R1 REBUT）**\nR2 认为与 concurrent work 差异化不够锐利。R1 反驳——§2 Related Work 的差异化讨论不只是一句话，已有较大篇幅区分 \"先诊断再路由\" vs \"直接学 router\" 的核心差异。\n**Director 判断**：R1 的反驳部分有效。差异化已有基础，但增加显式 comparison table 仍有价值。降级为建议而非 Weakness。\n\n**[D4] Excitement / Overall Score**\nR1 给 3.5（Borderline Conference），Excitement 3.5/5；R2 给 3.0（Findings），Excitement 2/5。\n分歧核心：R1 认为 \"先诊断再路由\" 范式本身有方法论贡献，即使具体发现 information content 有限；R2 认为 oracle + P-dependence 双重叠加后 novelty 受损严重，框架贡献量级更适合 Findings。\n**Director 判断**：采纳 3.0。两个 Critical 问题均获双方共识，Excitement 均值 2.75/5 低于 Conference 门槛，贡献类型在当前实证基础上更适合 Findings。\n\n## Questions\n\n**Q1. ΔDR 重新锚定**：如果将核心 claim 从 DAF=90.4% 重新锚定在 P-invariant 的 ΔDR=28.7pp 上，结论本质不变但对 P-dependence 批评的抵抗力大幅增强。作者是否愿意采纳？\n\n**Q2. Non-oracle deterministic baseline**：是否可以设计 non-oracle deterministic strategy（仅使用 LLM 可观察信息，deterministic action selection logic），以分离 oracle effect 与 strategy effect？如果 non-oracle deterministic 的 death rate 接近 internal（~42.9%），则 death asymmetry 主要来自 oracle access；如果仍远低于 internal，则策略结构本身有独立的安全效果。\n\n**Q3. Table 12 vs §4.5 评估协议差异**：Table 12 的 6-seed cross-split evaluation 与 §4.5 的固定 seed single-trial evaluation 的 accuracy 数字不直接可比——47.1±5.4%（cross-validated mean）vs always-deterministic 96.3%（oracle-agreement rate）。正文应更明确区分两个评估框架。\n\n**Q4. P=100 的环境特异性**：P=100 是 ScienceWorld 的内置惩罚（all-or-nothing, P/max_score ≈ 1），而非作者选择。论文应讨论 P/max_score 比值对 DAF 的影响——在 P/max_score ≈ 1 时 death dominance 是预期的，在 P/max_score << 1 时可能不成立。\n\n**Q5. Grounding ablation 后 DAF 重新计算**：当前 grounding ablation（Appendix O）仅报告 death rate 变化（+26.6pp → ~+8pp），未重新收集 counterfactual 计算 DAF。这是验证 \"death dominance vs grounding confusion\" 的关键缺失实验。\n\n## Missing References\n\n以下文献与论文主题直接相关但未被引用：\n\n1. **Risk-sensitive RL / CVaR**：Tamar et al. (2015) \"Optimizing the CVaR via Sampling\"; Chow et al. (2015) \"Risk-sensitive and robust decision-making\"; Dabney et al. (2018) \"Implicit quantile networks\"——death avoidance 本质是 tail-risk minimization\n2. **Agent failure taxonomy**：Kambhampati et al. (2024), Valmeekam et al. (2023)——LLM agent planning 局限性分析，与论文的 failure mode analysis（App N）直接相关\n3. **Process vs outcome feedback**：Uesato et al. (2022) \"Solving math word problems with process- and outcome-based feedback\"——Algorithm 1 实质是 outcome-based labeling\n4. **Process reward models**：Lightman et al. (2023) \"Let's Verify Step by Step\"——step-level supervision 可能改善 router 性能\n5. **Scaling test-time compute**：Snell et al. (2024)——adaptive computation routing 的 compute-optimal 决策\n\n注：Adaptive computation / early exit 文献（Universal Transformers, CALM）在抽象层次上与本文有本质差异（layer-level vs episode-level），引用非必要（R1 rebut 有效）。\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。**\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成**（耗时 ~3 分钟）\n\n| 严重度 | 位置 | 描述 |\n|--------|------|------|\n| ⚠️ Warning | Page 5 | 单页 4 个 display items（Figure 3 + Figure 4 + Table 1 + Table 2），视觉极度拥挤 |\n| ⚠️ Warning | Page 7 | 3 个 display items（Figure 5 + Figure 6 + Table 5），与 page 5 连续形成图表密集带 |\n| ⚠️ Warning | Page 3 | Figure 2 axis label 和 legend ≤6pt，低分辨率下难辨认 |\n| ⚠️ Warning | Page 5 | Figure 4 action sequence 文字标签字号过小 |\n| ℹ️ Info | Page 2 | Figure 1 framework 图整体清晰，部分箭头和小字标注缩小后不够醒目 |\n| ℹ️ Info | Page 5 | Figure 3 散点图单栏宽度，数据点拥挤，改为 figure* 全宽可提升可读性 |\n| ℹ️ Info | Page 6 | Table 3/4 booktabs 风格规范，最优值加粗 |\n| ℹ️ Info | Page 8 | Limitations 段落简短（~1/3 栏），符合 EMNLP 要求 |\n| ℹ️ Info | Pages 9-10 | References 排版正常，无未解析引用 |\n| ℹ️ Info | Page 11 | Appendix 目录 A-T 共 20 个附录，条目清晰 |\n| ℹ️ Info | Page 4 | Algorithm 1 伪代码和公式 (1)-(5) 渲染正确 |\n\n**统计**：0 Critical, 4 Warning, 11 Info\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3/5 | 2.5/5 | 2.5-3/5 |\n| Excitement | 3.5/5 | 2/5 | 2.5/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5 | 3.0 | **3.0** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**综合评分：3.0 (Findings)**\n\n**理由**：论文的 diagnostic framework 思路有方法论价值（S1），实验设计在给定设定下严谨（S2-S3），负面结果报告诚实（S4）。但两个结构性问题——(1) oracle privilege 使 death avoidance 发现接近预期结论（C1），(2) 单一主环境 + 极端跨环境 probe 无法支撑泛化性声明（C2）——从根本上限制了贡献的 novelty 和 scope。DAF 对 P 的数学单调依赖进一步削弱了标志性数字的说服力（W1）。\n\n论文适合作为 Findings 论文被接收，但需要在以下方面做出调整：(1) 贡献 reframing（diagnostic framework vs discovery）；(2) P-invariant 指标（ΔDR）作为 headline；(3) Spearman/Pearson 双报告；(4) 正文中正面处理 P-dependence。如果作者能进一步补充 non-oracle baseline 和 intermediate cross-env probe，论文可达到 Conference 水平（3.5-4.0）。\n\n两位 Reviewer 评分范围 3.0-3.5。Director 采纳 3.0 的主要权衡：(1) 两个 Critical 问题均获双方共识（AGREE x2）；(2) Excitement 均值 2.75/5 低于 Conference 门槛；(3) 贡献类型（diagnostic framework）在当前实证基础上更适合 Findings 定位。\n\n## Detailed Comments\n\n### §1 Introduction\n- \"708-scale\" 疑为排版错误，应为 \"70B-scale\"（M1）\n- DAF=90.4% 在 Introduction 中的突出程度应降低，考虑用 ΔDR=28.7pp 替代或并列展示（C1/W1）\n\n### §2 Method / Framework\n- \"Counterfactual\" 术语需在 §3 开头加定位声明——matched-seed paired comparison vs Rubin/Pearl counterfactual（W2）\n- SCI 在正文仅出现一次，与 Method 中的显著度不匹配——考虑进一步降级或在 Method 中缩减描述\n\n### §3 Results\n- Figure 3 应同时报告 Pearson r=0.97 和 Spearman ρ=0.586，并讨论差异原因（极端值敏感性）（W5）\n- Table 2 D/I/N 列标题改为 Det/Int/NoPref 或加表头脚注（M2）\n- §3.4 应将 Appendix K 的 P-sensitivity 核心结论（DAF 随 P 单调递增是数学必然）移入正文（W1/W4）\n- Eq.(4) 近似应给出 worst-case bound（M4）\n\n### §4 Analysis\n- §4.3 需补充 Retry/Reflexion 对 DAF 的影响——当前仅报告 death rate 变化（M3）\n- §4.5 需与 Table 12 的评估协议差异做明确区分——cross-validated mean vs oracle-agreement rate 不可比（Q3）\n- §4.6 Router 结论应从 \"no exploitable signal\" 改为 \"signal not learnable with this setup\"，并列出替代假设（W3）\n\n### §5 Discussion\n- 过薄（~0.5 页），需扩展（W6）：\n  - P/max_score 条件分析：何时 death avoidance dominate 是预期的 vs 有信息量的\n  - 与 CVaR / risk-sensitive RL 的概念连接\n  - 与 concurrent adaptive routing work 的对话\n  - Non-oracle deterministic baseline 的设计空间\n\n### Related Work (§4)\n- 补充 CVaR / risk-sensitive RL 文献（Tamar 2015, Chow 2015, Dabney 2018）（W7）\n- 补充 agent failure taxonomy（Kambhampati 2024, Valmeekam 2023）\n- 补充 process reward / test-time compute（Uesato 2022, Lightman 2023, Snell 2024）\n\n### Limitations\n- 长度适中（EMNLP 标准），但 5 段可适当精简至 3 段\n\n### Visual / Format\n- Page 5 图表密度过高——建议 Table 2 移至 page 6 或合并 Figure 3/4 为 subfigure（M6）\n- Figure 2 和 Figure 4 字号需增大至 ≥8pt（M5）\n- \"708\" 排版错误需更正（M1）",
    "project": "simgate-modular-routing",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c"
  }
}
```

</details>

---


### Tool result

_source line 2761 · 2026-05-25T21:49:33.365575+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4016
}
```

</details>

---


### Assistant

_source line 2762 · 2026-05-25T21:49:56.072340+00:00_

Round 32 审稿报告已投递。

**结论：3.0 (Findings)**

两位 Reviewer 交叉回应后高度收敛，1 轮完成。核心共识：

| 类型 | 数量 | 关键项 |
|------|------|--------|
| Critical | 2 | P-dependence + oracle tautology; 跨环境验证不足 |
| Warning | 7 | 附录过重、counterfactual 术语、router 过度推断、Spearman/Pearson 差异、Discussion 过薄、CVaR 引用缺失、P-dependence 正文缺失 |
| Minor | 6 | 708-scale 排版错误、Table 2 标题、DAF intervention 影响等 |

**分歧**：R1 给 3.5（Borderline Conference），R2 给 3.0（Findings）。Excitement 分歧最大（3.5 vs 2.0）。Director 采纳 3.0——两个 Critical 共识 + Excitement 均值 2.75 低于 Conference 门槛。

**升级路径**：reframe 贡献（framework > discovery）+ ΔDR 替代 DAF 作为 headline + non-oracle baseline + 中间环境 probe → 可达 3.5-4.0。

Issue Tracker 已同步（R31 历史更新 + 7 个 R32 新条目）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---
