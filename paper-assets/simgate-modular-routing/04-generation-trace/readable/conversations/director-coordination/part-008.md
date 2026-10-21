# Director coordination — Part 8 of 9

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Conversation logs

[← Part 7](part-007.md) · [Transcript overview](../director-coordination.md) · [Part 9 →](part-009.md) · [Structured JSON](../../../sessions/53/532e22af863d2a24e206.json)

## Round 196

### Tool call

_source line 2346 · 2026-05-22T09:00:12.250429+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "# Round 28 Review Issues (fresh review, 2026-05-22)\n# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作)\n\n# =============================================\n# Carried-over resolved issues (from prior rounds)\n# =============================================\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Wild cluster CI 修正且降级为 sensitivity analysis；non-clustered bootstrap 为主推断\"\n  resolution_round: 24\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Abstract concept-first 重组，数字从 10+ 精简至 3-4 个\"\n  resolution_round: 24\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Ng 1999, Northcutt 2021, DivideMix 已添加并在正确位置引用\"\n  resolution_round: 24\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 24\n  resolution: \"§5 Non-triviality 段有效回应 novelty 质疑\"\n  resolution_round: 24\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组（Self-supervised, Token-level, Task-level, RL-based）\"\n  resolution_round: 19\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"Limitations 新增 pure-strategy upper bound 段落\"\n  resolution_round: 24\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"术语全局修正为 text augmentation\"\n  resolution_round: 24\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导：P=0 时 72% labels 退化为 ties\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"P-invariance 适用范围明确量化\"\n  resolution_round: 24\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"4B router 结论 qualified；完整统计处理\"\n  resolution_round: 24\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors + train/val split 不清晰\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Router claim 从绝对否定改为有条件否定\"\n  resolution_round: 24\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"措辞软化 + effect size detection threshold 完整报告\"\n  resolution_round: 24\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制——§6 Conclusion 起始于 page 9，有 desk reject 风险\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"正文收入 8 页\"\n  resolution_round: 24\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 'fundamental non-learnability' 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R18-N1 解决\"\n  resolution_round: 24\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim — r=0.97 correlation ≠ causal/structural\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"'structurally determined' → 'empirically dominated'\"\n  resolution_round: 24\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 导致 13/28 tasks 不显著，主文未标注为 exploratory\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Per-task 结果标注为 exploratory，power caveat 完整\"\n  resolution_round: 24\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entry + Webb 年份待核实\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"huang2022inner, selfcheckgpt-2023, wang2023voyager 已清理；Webb 2023 (CJE vol.56 no.3) 年份正确\"\n  resolution_round: 24\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman 1999, Mihatsch 2002, Natarajan 2013\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"所有缺失引用已补充\"\n  resolution_round: 24\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引（17 个 appendices A-R）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Appendix Overview with hyperlinks 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M4\"\n  summary: \"§3.1 '54 sole-identified labels' 首次出现未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"术语已修正并定义\"\n  resolution_round: 24\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 inter-annotator agreement 声明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Single annotator caveat 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern — implication 未讨论\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"§5 已讨论 focus on [object] 单一模式\"\n  resolution_round: 24\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R17-M1 解决\"\n  resolution_round: 24\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"§5.4 cross-env 段加交叉引用指向 §2.1 operationalization\"\n  resolution_round: 24\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"Appendix B 加 circularity caveat; Limitations 量化 0.3% 方向冲突 + 60.3% pre-event neutral\"\n  resolution_round: 24\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 引用和讨论深度不足\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"引用已补全；额外解释句因 8 页限制无法加入，现有措辞部分覆盖\"\n  resolution_round: 24\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Algorithm 1 术语修正为 computation modes\"\n  resolution_round: 24\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"§3.1 binary structure 讨论充分\"\n  resolution_round: 24\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"72B decomposition 完整报告\"\n  resolution_round: 24\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"被 R20-N2 取代并解决\"\n  resolution_round: 24\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"Appendix L 已引用\"\n  resolution_round: 24\n\n- id: \"R19-W1\"\n  summary: \"缺少 penalty magnitude 的实际实验验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"P-invariance by design 论证逻辑覆盖\"\n  resolution_round: 24\n\n- id: \"R27-N1\"\n  summary: \"正文超出 8 页限制——Conclusion 溢出到 page 9（R20-N1 复发）\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 27\n  resolution: \"§5 重组为 3 段，Figure 2 缩小，§3.1 correlation/sensitivity 压缩。Conclusion 在 page 8。\"\n  resolution_round: 27\n\n- id: \"R27-N2\"\n  summary: \"DAF=90.4% 部分是 P=100 penalty 的数学必然，Abstract/Title framing 过度突出\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 28\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：Abstract 78.9% 为 headline，DAF 降为 derived measure\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[AGREE x2] R27 修复部分有效——78.9% 确实是 headline，但 DAF=90.4% 仍在 Abstract 和 §3.1 中以核心数字出现。§2.4 将 DAF 标记为 derived penalty-dependent measure，但 P-sensitivity 的核心数字（P=10→50.4%, P=50→82.6%）仅在 Appendix K 中出现，主文未展示。\"\n  action_items:\n    - round: 28\n      action: \"§2.4 在定义 DAF 后增加 1-2 句正文讨论 P-sensitivity（至少引用 P=10 和 P=50 数值）；Abstract/Conclusion 进一步降低 DAF 的 prominence\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-N3\"\n  summary: \"Deterministic strategy 实为 oracle access，跨环境含义不统一，oracle confound 未分离\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 28\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：§2.1 inline 三环境 operationalization，§5 ¶2 双论据\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[AGREE x2] §2.1 已描述差异但 Conclusion 仍写 'the diagnostic procedure transfers'，未区分 procedure transferability vs operationalization consistency。三环境 'deterministic' 的信息优势程度差异巨大（oracle > code interpreter > admissible actions），当前表述暗示跨环境一致性高于实际水平。\"\n  action_items:\n    - round: 28\n      action: \"§3.4 开头或 Conclusion 增加限定：cross-environment probes 验证 diagnostic procedure 的可复用性，不是 'deterministic' 概念的一致性\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-N4\"\n  summary: \"环境覆盖过窄，generalization claims 超出证据——1 个主环境 + 2 个 boundary probes\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 28\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：Abstract/Conclusion 'preliminary evidence' + 区分 methodological vs empirical generality\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"本轮未单独提出，但 R2-N2 间接涉及——cross-env claims 需更精确限定。R27 修复基本有效。\"\n\n- id: \"R28-N1\"\n  summary: \"Episode-level labeling 与 step-level routing 的粒度失配——title/abstract scope 超出方法论覆盖范围\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R1 认为 critical（title 暗示 step-level routing 发现，实际是 episode-level outcome）；R2 REBUT 认为 'routing signal' ≠ 'routing decision'，episode-level 是 principled granularity，但同意 Abstract 应加 'episode-level' 限定词。双方最终共识：不影响 claim validity，但 framing 需更精确。\"\n  action_items:\n    - round: 28\n      action: \"Abstract 中在 '78.9% of non-tie routing labels' 前增加 'episode-level' 限定词\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W1\"\n  summary: \"Router negative result framing: signal-limited vs data-limited 未区分\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 28\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：§5 ¶1 双解释 + 1,350 估算\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE on severity] R1 认为架构简单性是主要限制（仅 Qwen3 0.6B-4B），R2 REBUT 认为 6 种 router 变体 + LOTO + death-proximal labeling 已足够。但双方 AGREE：paraphrase augmentation 不增加新 routing signal，signal-limited vs data-limited vs feature-limited 的区分尚不完全 conclusive。\"\n  action_items:\n    - round: 28\n      action: \"§3.6 或 §5 更对称地呈现两种解释，明确当前数据量不足以完全区分 signal-limited vs data-limited\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W2\"\n  summary: \"Actionability 有限——诊断出问题但'然后怎么办'回答不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 28\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：§5 ¶3 actionability 段完成\"\n    - round: 28\n      reviewers: [2]\n      note: \"R2-W4：缺少与 concurrent routing methods 的定性讨论——CogRouter/ARES/MTRouter 在 death-dominated 环境中是否遇到 signal collapse。R1 AGREE partially（定性讨论有价值，不需实验）。\"\n  action_items:\n    - round: 28\n      action: \"§5 或 §4 增加 2-3 句定性讨论 concurrent routing methods 在 death-dominated 环境中的预期表现\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W4\"\n  summary: \"Excluded tasks (63%) n=5 prescreening 样本量极小\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 28\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：§3 加 n=5 limitation 标注\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 主文仅一句话。对 analysis 论文 63% 排除率需更充分正文 justify。缺 taxonomic redundancy 的操作定义。建议至少在 §3 增加一段展示 Table 4 的 key numbers（excluded ΔDR=+38.2 > included +28.7 pp）。\"\n  action_items:\n    - round: 28\n      action: \"§3 增加一段：排除 tasks 的 ΔDR 更高 + taxonomic redundancy 操作定义\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W5\"\n  summary: \"K=11 cluster bootstrap: primary CI [81.1%, 99.0%] 可能 anti-conservative\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 28\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：§3.1 并列报告 clustered CI [73.3%, 100.0%]\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 论文处理得当（non-clustered 为主推断），但 Limitations 正文缺 Cameron et al. K≥20-50 建议的显式引用。Effect size d=3.02 缓解但不消除。\"\n  action_items:\n    - round: 28\n      action: \"Limitations Statistical limitations 段显式引用 Cameron et al. K≥20-50 建议\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R28-W1\"\n  summary: \"72B scaling 仅做 probe 而非完整 replication——缺 router training 和 SCI 分析\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 72B death rate 降到 30.6%，non-death signal 可能更 prominent。DAF=92.4% 反而更高（deterministic 也更安全），但未运行 router training 或 per-task decomposition 验证。\"\n  action_items:\n    - round: 28\n      action: \"Limitations 中明确 72B 实验 scope 限制；讨论更强模型下 non-death signal 是否可能超过 death signal\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R28-W2\"\n  summary: \"'Death' 术语限制 generality perception——binary failure vs graded failure 适用性未讨论\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Algorithm 1 依赖 binary death/alive 区分。当 failure 是 graded 时，death-first priority 不适用。Discussion/Limitations 缺少对 graded failure 的讨论。\"\n  action_items:\n    - round: 28\n      action: \"§5 或 Limitations 增加 1-2 句讨论 graded failure 场景下 framework 的调整（如设 failure threshold 二值化）\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R28-M1\"\n  summary: \"Missing references: Alshiekh et al. (2018) Safe RL via Shielding, Geifman & El-Yaniv (2017) Selective Classification, Schuster et al. (2022) CALM, Raposo et al. (2024) Mixture-of-Depths\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"Alshiekh 与 Appendix O action-space filtering 直接相关；Geifman 是 selective prediction 经典；Schuster CALM 和 Raposo MoD 是 non-agent adaptive computation baseline。\"\n\n- id: \"R28-M2\"\n  summary: \"Pages 7-8 连续两页纯文本无 display item\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n    - round: 28\n      reviewers: []\n      note: \"视觉审查发现。§3.6 Router Training 结果可考虑用小 table 呈现。\"\n\n- id: \"R28-M3\"\n  summary: \"§1 Introduction 'signal diversity can collapse' 重复出现\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n    - round: 28\n      reviewers: [2]\n      note: \"§1 para 5 和 contributions list item 2 措辞几乎相同。\"\n\n- id: \"R28-M4\"\n  summary: \"Figure 2 仅 11 点无 task name label，r=0.97 caveat 不够明确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 建议加 task name label 增加可读性。\"\n\n- id: \"R28-M5\"\n  summary: \"Related Work 缺 non-agent adaptive computation（early exit, speculative decoding, Mixture-of-Depths）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 论文引用 Graves (2016) 但跳过 CALM、Mixture-of-Depths 等更近的 non-agent adaptive computation 工作。\"\n\n# --- Structural / Long-standing ---\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit——方向可预期\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 28\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"Excitement 仍 2.5/5。结构性限制不可通过 writing fix 解决。Findings 定位确定。\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 Excitement 3/5。核心发现（death dominance in death-penalized env）具有可预测性。结构性限制持续存在。\"\n\n- id: \"R19-N1\"\n  summary: \"Framing 内在张力：framework vs finding 定位不清\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 27\n  resolution: \"N2+N4 修复间接解决——Abstract/Conclusion 统一为 empirical analysis + reusable diagnostic methodology。\"\n  resolution_round: 27\n\n- id: \"R26-N3\"\n  summary: \"'Contradicting the routing literature's implicit assumption' 是 strawman framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 26\n  last_seen_round: 27\n  resolution: \"R27 验收确认修复完好。\"\n  resolution_round: 27"
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
    "issues_yaml": "# Round 28 Review Issues (fresh review, 2026-05-22)\n# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作)\n\n# =============================================\n# Carried-over resolved issues (from prior rounds)\n# =============================================\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Wild cluster CI 修正且降级为 sensitivity analysis；non-clustered bootstrap 为主推断\"\n  resolution_round: 24\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Abstract concept-first 重组，数字从 10+ 精简至 3-4 个\"\n  resolution_round: 24\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Ng 1999, Northcutt 2021, DivideMix 已添加并在正确位置引用\"\n  resolution_round: 24\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 24\n  resolution: \"§5 Non-triviality 段有效回应 novelty 质疑\"\n  resolution_round: 24\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组（Self-supervised, Token-level, Task-level, RL-based）\"\n  resolution_round: 19\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"Limitations 新增 pure-strategy upper bound 段落\"\n  resolution_round: 24\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"术语全局修正为 text augmentation\"\n  resolution_round: 24\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导：P=0 时 72% labels 退化为 ties\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"P-invariance 适用范围明确量化\"\n  resolution_round: 24\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"4B router 结论 qualified；完整统计处理\"\n  resolution_round: 24\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors + train/val split 不清晰\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Router claim 从绝对否定改为有条件否定\"\n  resolution_round: 24\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"措辞软化 + effect size detection threshold 完整报告\"\n  resolution_round: 24\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制——§6 Conclusion 起始于 page 9，有 desk reject 风险\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"正文收入 8 页\"\n  resolution_round: 24\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 'fundamental non-learnability' 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R18-N1 解决\"\n  resolution_round: 24\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim — r=0.97 correlation ≠ causal/structural\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"'structurally determined' → 'empirically dominated'\"\n  resolution_round: 24\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 导致 13/28 tasks 不显著，主文未标注为 exploratory\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Per-task 结果标注为 exploratory，power caveat 完整\"\n  resolution_round: 24\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entry + Webb 年份待核实\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"huang2022inner, selfcheckgpt-2023, wang2023voyager 已清理；Webb 2023 (CJE vol.56 no.3) 年份正确\"\n  resolution_round: 24\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman 1999, Mihatsch 2002, Natarajan 2013\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"所有缺失引用已补充\"\n  resolution_round: 24\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引（17 个 appendices A-R）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Appendix Overview with hyperlinks 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M4\"\n  summary: \"§3.1 '54 sole-identified labels' 首次出现未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"术语已修正并定义\"\n  resolution_round: 24\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 inter-annotator agreement 声明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Single annotator caveat 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern — implication 未讨论\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"§5 已讨论 focus on [object] 单一模式\"\n  resolution_round: 24\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R17-M1 解决\"\n  resolution_round: 24\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"§5.4 cross-env 段加交叉引用指向 §2.1 operationalization\"\n  resolution_round: 24\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"Appendix B 加 circularity caveat; Limitations 量化 0.3% 方向冲突 + 60.3% pre-event neutral\"\n  resolution_round: 24\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 引用和讨论深度不足\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"引用已补全；额外解释句因 8 页限制无法加入，现有措辞部分覆盖\"\n  resolution_round: 24\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Algorithm 1 术语修正为 computation modes\"\n  resolution_round: 24\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"§3.1 binary structure 讨论充分\"\n  resolution_round: 24\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"72B decomposition 完整报告\"\n  resolution_round: 24\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"被 R20-N2 取代并解决\"\n  resolution_round: 24\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"Appendix L 已引用\"\n  resolution_round: 24\n\n- id: \"R19-W1\"\n  summary: \"缺少 penalty magnitude 的实际实验验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"P-invariance by design 论证逻辑覆盖\"\n  resolution_round: 24\n\n- id: \"R27-N1\"\n  summary: \"正文超出 8 页限制——Conclusion 溢出到 page 9（R20-N1 复发）\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 27\n  resolution: \"§5 重组为 3 段，Figure 2 缩小，§3.1 correlation/sensitivity 压缩。Conclusion 在 page 8。\"\n  resolution_round: 27\n\n- id: \"R27-N2\"\n  summary: \"DAF=90.4% 部分是 P=100 penalty 的数学必然，Abstract/Title framing 过度突出\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 28\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：Abstract 78.9% 为 headline，DAF 降为 derived measure\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[AGREE x2] R27 修复部分有效——78.9% 确实是 headline，但 DAF=90.4% 仍在 Abstract 和 §3.1 中以核心数字出现。§2.4 将 DAF 标记为 derived penalty-dependent measure，但 P-sensitivity 的核心数字（P=10→50.4%, P=50→82.6%）仅在 Appendix K 中出现，主文未展示。\"\n  action_items:\n    - round: 28\n      action: \"§2.4 在定义 DAF 后增加 1-2 句正文讨论 P-sensitivity（至少引用 P=10 和 P=50 数值）；Abstract/Conclusion 进一步降低 DAF 的 prominence\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-N3\"\n  summary: \"Deterministic strategy 实为 oracle access，跨环境含义不统一，oracle confound 未分离\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 28\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：§2.1 inline 三环境 operationalization，§5 ¶2 双论据\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[AGREE x2] §2.1 已描述差异但 Conclusion 仍写 'the diagnostic procedure transfers'，未区分 procedure transferability vs operationalization consistency。三环境 'deterministic' 的信息优势程度差异巨大（oracle > code interpreter > admissible actions），当前表述暗示跨环境一致性高于实际水平。\"\n  action_items:\n    - round: 28\n      action: \"§3.4 开头或 Conclusion 增加限定：cross-environment probes 验证 diagnostic procedure 的可复用性，不是 'deterministic' 概念的一致性\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-N4\"\n  summary: \"环境覆盖过窄，generalization claims 超出证据——1 个主环境 + 2 个 boundary probes\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 28\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：Abstract/Conclusion 'preliminary evidence' + 区分 methodological vs empirical generality\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"本轮未单独提出，但 R2-N2 间接涉及——cross-env claims 需更精确限定。R27 修复基本有效。\"\n\n- id: \"R28-N1\"\n  summary: \"Episode-level labeling 与 step-level routing 的粒度失配——title/abstract scope 超出方法论覆盖范围\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R1 认为 critical（title 暗示 step-level routing 发现，实际是 episode-level outcome）；R2 REBUT 认为 'routing signal' ≠ 'routing decision'，episode-level 是 principled granularity，但同意 Abstract 应加 'episode-level' 限定词。双方最终共识：不影响 claim validity，但 framing 需更精确。\"\n  action_items:\n    - round: 28\n      action: \"Abstract 中在 '78.9% of non-tie routing labels' 前增加 'episode-level' 限定词\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W1\"\n  summary: \"Router negative result framing: signal-limited vs data-limited 未区分\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 28\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：§5 ¶1 双解释 + 1,350 估算\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE on severity] R1 认为架构简单性是主要限制（仅 Qwen3 0.6B-4B），R2 REBUT 认为 6 种 router 变体 + LOTO + death-proximal labeling 已足够。但双方 AGREE：paraphrase augmentation 不增加新 routing signal，signal-limited vs data-limited vs feature-limited 的区分尚不完全 conclusive。\"\n  action_items:\n    - round: 28\n      action: \"§3.6 或 §5 更对称地呈现两种解释，明确当前数据量不足以完全区分 signal-limited vs data-limited\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W2\"\n  summary: \"Actionability 有限——诊断出问题但'然后怎么办'回答不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 28\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：§5 ¶3 actionability 段完成\"\n    - round: 28\n      reviewers: [2]\n      note: \"R2-W4：缺少与 concurrent routing methods 的定性讨论——CogRouter/ARES/MTRouter 在 death-dominated 环境中是否遇到 signal collapse。R1 AGREE partially（定性讨论有价值，不需实验）。\"\n  action_items:\n    - round: 28\n      action: \"§5 或 §4 增加 2-3 句定性讨论 concurrent routing methods 在 death-dominated 环境中的预期表现\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W4\"\n  summary: \"Excluded tasks (63%) n=5 prescreening 样本量极小\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 28\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：§3 加 n=5 limitation 标注\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 主文仅一句话。对 analysis 论文 63% 排除率需更充分正文 justify。缺 taxonomic redundancy 的操作定义。建议至少在 §3 增加一段展示 Table 4 的 key numbers（excluded ΔDR=+38.2 > included +28.7 pp）。\"\n  action_items:\n    - round: 28\n      action: \"§3 增加一段：排除 tasks 的 ΔDR 更高 + taxonomic redundancy 操作定义\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W5\"\n  summary: \"K=11 cluster bootstrap: primary CI [81.1%, 99.0%] 可能 anti-conservative\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 28\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：§3.1 并列报告 clustered CI [73.3%, 100.0%]\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 论文处理得当（non-clustered 为主推断），但 Limitations 正文缺 Cameron et al. K≥20-50 建议的显式引用。Effect size d=3.02 缓解但不消除。\"\n  action_items:\n    - round: 28\n      action: \"Limitations Statistical limitations 段显式引用 Cameron et al. K≥20-50 建议\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R28-W1\"\n  summary: \"72B scaling 仅做 probe 而非完整 replication——缺 router training 和 SCI 分析\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 72B death rate 降到 30.6%，non-death signal 可能更 prominent。DAF=92.4% 反而更高（deterministic 也更安全），但未运行 router training 或 per-task decomposition 验证。\"\n  action_items:\n    - round: 28\n      action: \"Limitations 中明确 72B 实验 scope 限制；讨论更强模型下 non-death signal 是否可能超过 death signal\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R28-W2\"\n  summary: \"'Death' 术语限制 generality perception——binary failure vs graded failure 适用性未讨论\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Algorithm 1 依赖 binary death/alive 区分。当 failure 是 graded 时，death-first priority 不适用。Discussion/Limitations 缺少对 graded failure 的讨论。\"\n  action_items:\n    - round: 28\n      action: \"§5 或 Limitations 增加 1-2 句讨论 graded failure 场景下 framework 的调整（如设 failure threshold 二值化）\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R28-M1\"\n  summary: \"Missing references: Alshiekh et al. (2018) Safe RL via Shielding, Geifman & El-Yaniv (2017) Selective Classification, Schuster et al. (2022) CALM, Raposo et al. (2024) Mixture-of-Depths\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"Alshiekh 与 Appendix O action-space filtering 直接相关；Geifman 是 selective prediction 经典；Schuster CALM 和 Raposo MoD 是 non-agent adaptive computation baseline。\"\n\n- id: \"R28-M2\"\n  summary: \"Pages 7-8 连续两页纯文本无 display item\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n    - round: 28\n      reviewers: []\n      note: \"视觉审查发现。§3.6 Router Training 结果可考虑用小 table 呈现。\"\n\n- id: \"R28-M3\"\n  summary: \"§1 Introduction 'signal diversity can collapse' 重复出现\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n    - round: 28\n      reviewers: [2]\n      note: \"§1 para 5 和 contributions list item 2 措辞几乎相同。\"\n\n- id: \"R28-M4\"\n  summary: \"Figure 2 仅 11 点无 task name label，r=0.97 caveat 不够明确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 建议加 task name label 增加可读性。\"\n\n- id: \"R28-M5\"\n  summary: \"Related Work 缺 non-agent adaptive computation（early exit, speculative decoding, Mixture-of-Depths）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 论文引用 Graves (2016) 但跳过 CALM、Mixture-of-Depths 等更近的 non-agent adaptive computation 工作。\"\n\n# --- Structural / Long-standing ---\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit——方向可预期\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 28\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"Excitement 仍 2.5/5。结构性限制不可通过 writing fix 解决。Findings 定位确定。\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 Excitement 3/5。核心发现（death dominance in death-penalized env）具有可预测性。结构性限制持续存在。\"\n\n- id: \"R19-N1\"\n  summary: \"Framing 内在张力：framework vs finding 定位不清\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 27\n  resolution: \"N2+N4 修复间接解决——Abstract/Conclusion 统一为 empirical analysis + reusable diagnostic methodology。\"\n  resolution_round: 27\n\n- id: \"R26-N3\"\n  summary: \"'Contradicting the routing literature's implicit assumption' 是 strawman framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 26\n  last_seen_round: 27\n  resolution: \"R27 验收确认修复完好。\"\n  resolution_round: 27"
  }
}
```

</details>

---


### Tool result

_source line 2347 · 2026-05-22T09:00:12.301684+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 21693}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2348 · 2026-05-22T09:02:25.445108+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 28 审稿报告 — simgate-modular-routing\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**Venue**: EMNLP 2026 (ARR May cycle), Interpretability and Analysis track\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1 方法严谨性+实验设计, R2 新颖性+完整性+写作）\n**交叉轮次**: 1 轮（关键问题达成共识，无需 Round 2）\n\n---\n\n## Summary\n\n论文提出 episode-level counterfactual diagnostic framework，通过对比 pure-strategy（internal-only vs deterministic-only）的 episode outcomes 来 decompose routing signal 的组成。应用于 ScienceWorld（11 task types, 245 episodes），发现 78.9% 的 non-tie routing labels 源于 death asymmetry（内部策略触发 -100 死亡惩罚而确定性策略存活）。Cross-model replication（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B-it）确认 DAF 88-90%（spread 2.2pp）。Router training（Qwen3 0.6B-4B）在 episode level 降至 chance 以下，报告为 diagnostic negative result。Cross-environment probes（MATH, ALFWorld）展示框架在无 death 环境中诊断不同 routing mechanism 的能力。\n\n---\n\n## Strengths\n\n1. **极其详尽的鲁棒性验证**（R1-S2, R2-S1）：20 个 appendix 覆盖 LOO、cluster bootstrap、wild bootstrap、penalty sensitivity、cross-model、cross-environment、capacity scaling、augmentation ablation 等——在 analysis track 论文中属顶级水平。\n2. **诚实的负面结果报告**（R1-S3, R2-S2）：Router training failure（episode-level balanced accuracy 47.1% < 50% chance）被完整报告而非隐藏，提供两种可能解释（signal-limited vs data-limited），附带 text augmentation、capacity scaling、death-proximal labeling 等排除实验。\n3. **Cross-model convergence**（R1-S4, R2-S4）：三个架构差异显著的 7-9B 模型家族 + 72B scaling 给出 DAF 88-92%（spread 2.2pp），有力排除模型特异性解释。\n4. **Penalty-independent 与 penalty-dependent 度量双轨报告**（R2-S3）：区分 label fraction (78.9%, P-invariant) 和 DAF (90.4%, P-dependent)，展示完整 P-sensitivity 曲线（Appendix K）。\n5. **Track fit 优秀**（R2-S5）：\"先诊断 routing signal 再决定是否训练 router\" 的理念与 Interpretability and Analysis track 高度匹配。\n6. **研究问题定义清晰**（R1-S1）：填补了 routing literature 中\"routing signal 到底由什么组成\"这一方法论空白。\n\n---\n\n## Weaknesses\n\n### Must-Fix（2 项，双方共识）\n\n**[AGREE x2] W-Critical-1: DAF 度量的 P-dependence 在主文中讨论不足**\n- 来源：R1-N2 + R2-N1（完全共识）\n- 问题：DAF = δP/(δP + Δ_nd) 随 P 单调递增（P=10→50.4%, P=50→82.6%, P=100→90.4%, P=200→94.9%），是数学必然而非纯实证发现。Appendix K 承认\"mathematical consequence\"，但主文 §2.4 仅标记 DAF 为 \"derived penalty-dependent measure\"，未展示 P-sensitivity 的任何数值。Abstract 虽以 78.9% 为 headline，但 DAF=90.4% 仍以核心数字地位出现。\n- 影响：Analysis track 论文的核心度量之一有数学 artifact 成分但主文透明度不足，可能导致读者高估 finding 的实证强度。\n- 建议：(1) §2.4 定义 DAF 后增加 1-2 句正文讨论 P-sensitivity（至少引用 P=10 和 P=50）；(2) Abstract/Conclusion 进一步降低 DAF 的 prominence。\n\n**[AGREE x2] W-Critical-2: \"Deterministic\" 跨环境含义不统一，transfer claim 需更精确限定**\n- 来源：R2-N2（R1 交叉时 AGREE）\n- 问题：三环境 \"deterministic\" 实现差异巨大（oracle simulator / code interpreter / admissible-action enumeration），信息优势程度不可比。§2.1 描述了差异但 Conclusion 仍写 \"the diagnostic procedure transfers\"，暗示跨环境一致性高于实际水平。\n- 影响：读者可能期望比论文实际提供的更强的泛化性。\n- 建议：Conclusion 或 §3.4 增加限定：cross-env probes 验证 diagnostic procedure 的可复用性，不是 \"deterministic computation\" 概念的一致性。\n\n### Should-Fix（7 项）\n\n**[AGREE x2] W1: 63% task type 排除率需在主文更充分 justify**\n- 来源：R1-W2 + R2-W1\n- 问题：主文 §3 仅一句话说明排除原因。缺 taxonomic redundancy 的操作定义。Anti-cherry-picking 数据（excluded ΔDR=+38.2 > included +28.7 pp）全在 appendix。\n- 建议：§3 增加一段展示 key numbers + taxonomic redundancy 定义。\n\n**[DIVERGENCE → warning] W2: Episode→step 粒度失配的 framing 精确性**\n- 来源：R1-N1（critical）vs R2 REBUT（warning）\n- R1 主张：Title/Abstract 暗示 step-level routing 发现，实际证据限于 episode-level outcome。\n- R2 反驳：\"Routing Signal\" ≠ \"Routing Decision\"；episode-level 是 sparse-reward 环境的 principled granularity（97.4% step ties）。但同意 Abstract 应加 \"episode-level\" 限定词。\n- 最终判定：降为 warning。Claim validity 不受影响，但 framing 可更精确。\n- 建议：Abstract 中 \"78.9% of non-tie routing labels\" 前增加 \"episode-level\"。\n\n**[AGREE with nuance x2] W3: Router negative result 的 signal-limited vs data-limited 区分不完全**\n- 来源：R1-W3 + R2-W2\n- R2 REBUT R1 的 \"架构简单\" 批评（6 种变体 + LOTO + death-proximal labeling），但 AGREE paraphrase augmentation 不增加新 routing signal，真实 episode-level scaling 未测试。\n- 建议：§5 更对称呈现两种解释，明确当前数据量不足以完全区分。\n\n**[AGREE x2] W4: K=11 cluster bootstrap 局限性未在主文充分标注**\n- 来源：R1-W1\n- 建议：Limitations 显式引用 Cameron et al. K≥20-50 建议。\n\n**[AGREE x2] W5: 72B scaling 仅做 probe 不够完整**\n- 来源：R1-W4\n- 建议：Limitations 中标注 72B scope 限制；讨论更强模型下 non-death signal 是否可能超过 death signal。\n\n**[AGREE x2] W6: \"Death\" 术语限制 generality — graded failure 适用性未讨论**\n- 来源：R2-W5\n- 建议：Discussion 增加 1-2 句讨论 graded failure 场景。\n\n**[AGREE partially] W7: 缺与 concurrent routing methods 的定性讨论**\n- 来源：R2-W4\n- 建议：§5 或 §4 增加 2-3 句讨论 CogRouter/ARES/MTRouter 在 death-dominated 环境中的预期表现。\n\n### Minor（5 项）\n\n- **M1**: Figure 2 仅 11 点无 task name label [AGREE x2]\n- **M2**: §1 Introduction \"signal diversity can collapse\" 重复出现 [R2]\n- **M3**: Pages 7-8 连续两页纯文本无 display item [视觉审查]\n- **M4**: Missing references: Alshiekh et al. (2018) Safe RL via Shielding, Geifman & El-Yaniv (2017) Selective Classification, Schuster et al. (2022) CALM, Raposo et al. (2024) Mixture-of-Depths [R1+R2 共 4 条]\n- **M5**: Related Work 缺 non-agent adaptive computation (early exit, speculative decoding) [R1-M6, R2 AGREE]\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成完全共识 [AGREE x2]：\n1. DAF P-dependence 是最需要作者回应的 critical issue（label fraction 应为 primary metric）\n2. \"Deterministic\" 跨环境语义不同需更精确限定 transfer claim\n3. 63% task 排除率需更充分正文 justify\n4. K=11 cluster bootstrap 局限需显式标注\n5. 72B 实验 scope 有限\n6. 论文鲁棒性验证水平在 analysis track 中属上乘（20 appendices）\n7. 负面结果报告（router failure）诚实且有价值\n8. Cross-model convergence（3 family, DAF 88-90%）有力排除模型特异性\n\n## Reviewer Divergence\n\n**Episode→step 粒度失配的严重程度**：\n- R1 评为 critical：Title/Abstract scope 超出方法论覆盖范围\n- R2 评为 minor framing issue：论文 claim 是关于 \"signal composition\" 而非 \"step-level decision\"，episode-level 是 principled granularity\n- R2 提供的反驳依据：(1) §2.2 论证了 97.4% step ties 使 episode-level 成为唯一有效粒度；(2) 61.2% no-preference 也是诊断信息；(3) §3.6 和 §5 已详细讨论 step-level router failure\n- **最终判定**：降为 warning —— claim validity 不受影响，但 Abstract 应加 \"episode-level\" 限定词\n\n**Limitations 长度**：\n- R2 评为 warning（5 段过长，建议压缩到 3 点）\n- R1 REBUT（analysis 论文的诚实 limitations 是优势而非缺陷，且不占页数限制）\n- **最终判定**：不列入 weakness — R1 理由充分，Limitations 内容均为必要 caveats\n\n**Router 架构简单性是否是负结论的主要限制**：\n- R1 评为 warning（仅测试 Qwen3 0.6B-4B + LoRA）\n- R2 REBUT（6 种变体收敛、LOTO 打回、death-proximal labeling 无效），但 AGREE scope 限定可更精确\n- **最终判定**：保留为 W3 的子问题，建议更对称呈现双解释\n\n---\n\n## Questions to Authors\n\n1. **P=0 下 78.9% label fraction 的稳定性**：论文声称 label fraction 是 P-invariant 的，但 §3.1 提到 54 个 \"sole-signal labels\" 在 P=0 时退化为 ties——这意味着 P=0 下 label fraction 会从 78.9% 降低。Algorithm 1 的 death-first priority 等价于隐式无穷大 penalty，这与 \"penalty-independent\" 叙事存在微妙张力。请澄清。\n2. **150 个 no_pref episodes 的 action sequence 相似度**：两策略在相同 outcome 下是否采取了相似路径？如果路径不同但结果相同，可能存在被 episode-level aggregation 掩盖的 step-level routing signal。\n3. **72B 条件下 non-death signal 是否增强**：72B 的 death rate 降至 30.6%，意味着更多 episodes 双方存活。$\\Delta_{\\text{nd}}$ 是否在 72B 上显著增大？如果是，death dominance 的 scale-robustness 结论是否需要 qualify？\n\n---\n\n## Missing References\n\n- Alshiekh et al., \"Safe Reinforcement Learning via Shielding\" (AAAI 2018) — Appendix O action-space filtering 本质是简化版 shield [R2, R1 AGREE]\n- Geifman & El-Yaniv, \"Selective Classification for Deep Neural Networks\" (NeurIPS 2017) — selective prediction 经典，与 routing/abstention 概念关联 [R2, R1 AGREE]\n- Schuster et al., \"Confident Adaptive Language Modeling\" (NeurIPS 2022) — non-agent adaptive computation baseline [R1, R2 AGREE]\n- Raposo et al., \"Mixture-of-Depths\" (ICML 2024) — per-token computation allocation [R1, R2 AGREE]\n\n---\n\n## External Review\n\n未请求（项目未配置 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成。3 warnings, 14 info。\n\n**Warnings**:\n1. **Pages 7-8 连续两页纯文本**：§3.6 (Router Training) + §4 (Related Work) + §5 (Discussion) + §6 (Conclusion) 无任何 display item，阅读节奏单调。建议 §3.6 router 结果可用小 table 呈现。\n2. **Page 9 Limitations 篇幅较大**：5 个子段落几乎填满整页。（但 Reviewer 圆桌讨论认为此内容均为必要 caveats，不建议删减。）\n3. **Page 24 末页空白**：附录末页仅约 1/4 内容，空间利用率低。\n\n**正面发现**：\n- 全文无 LaTeX 渲染错误、margin 溢出或 section heading 孤悬\n- 双栏排版间距均匀，行号完整（submission 格式正确）\n- 主体正文 8 页含 5 个 display items（Figure 1-3, Table 1-2），对诊断型论文属合理范围\n- 所有 table 使用 booktabs 风格，格式规范\n- Figure 3 使用 shaded error bands，可视化实践良好\n- 颜色语义跨图一致\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n**评分理由**：\n\n论文在 ScienceWorld 环境内做了一项极其详尽的诊断分析——20 个 appendix 的鲁棒性验证、3 个模型家族的 cross-model replication、router training 负结论的多层论证——在 methodological rigor 上无可挑剔。78.9% death-asymmetric label fraction 作为 penalty-independent 的核心发现是可靠的，cross-model convergence（spread 2.2pp）有力排除了模型特异性。\n\n但以下结构性限制将论文定位在 Findings 而非 main conference：\n\n1. **Excitement deficit（R1 3/5, R2 3/5）**：核心发现——在有 catastrophic failure 的环境中 death avoidance 主导 routing signal——具有一定的 a priori 可预测性。当一种策略有 oracle access 而另一种策略会\"死\"时，oracle 更安全是 expected 的。论文的贡献在于量化了这一直觉（78.9%）并系统排除了 alternative explanations，但 insight 的 surprise value 有限。\n2. **DAF 度量的数学 artifact**：核心度量之一（DAF=90.4%）部分由 P=100 的选择决定（P=10 时仅 50.4%），虽然 label fraction 提供了 P-invariant 的补充，但主文对 P-sensitivity 的透明度不足。\n3. **单环境主体验证**：完整验证仅在 ScienceWorld 上完成，MATH 和 ALFWorld 只是 boundary probes（且 \"deterministic\" 含义不可比）。框架的 methodological generality 合理，但 empirical generality 证据不足。\n4. **Actionability gap**：框架是 diagnostic 而非 prescriptive——诊断出 death dominance 后的 practical next step（除了 \"用 always-deterministic\"）不够清晰。\n\n综合两位 Reviewer 独立评分均为 3.5 (Borderline Conference)，考虑到 excitement deficit 是持续存在的结构性限制（从 Round 16 至今），且 Must-Fix 问题均为 framing 层面（可修但不改变核心 contribution 的 novelty），判定为 **3.0 (Findings)**——论文质量足以被 Findings 接收，但核心 contribution 的 novelty 和 generality 尚不足以推荐 main conference。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"signal diversity can collapse to a single dominant mechanism\" 在 para 5 和 contributions list item 2 中重复出现，措辞几乎相同——合并或删除一处。\n- Contributions 列表三项，每项内容过长（item 2 跨 3 行），建议精简。\n\n### §2 Method\n- §2.4 DAF 定义后应立即讨论 P-sensitivity，至少引用 P=10 (50.4%) 和 P=50 (82.6%)。当前叙事在此处建立了 DAF 的重要性，但读者要翻到 Appendix K 才发现 90.4% 有数学 artifact 成分。\n- §2.1 \"deterministic\" operationalization 差异已描述，但应更明确标注\"这些定性差异影响框架能检测到的 routing signal 类型\"不仅是 caveat，而是 cross-env 分析的核心前提。\n\n### §3 Experiments\n- §3 第一段 63% 排除率应展开。建议增加一段：(1) excluded tasks ΔDR=+38.2 > included +28.7 pp；(2) taxonomic redundancy 操作定义；(3) agent-floor tasks 排除的合理性。\n- §3.1 Figure 2 scatter plot：11 点 + r=0.97 的 structural consequence caveat 可以更 prominent（当前在 caption 末尾）。建议加 task name label。\n- §3.4 ALFWorld 分析仅一段话，作为三个 cross-env probes 之一显得单薄。至少应引用 Appendix L 的 Table/Figure。\n- §3.6 Router training 负结论 scope 可更精确——\"no step-level learnable signal exists under current architectures and data regime\" 中 \"current architectures\" 应明确列出（Qwen3 0.6B-4B with LoRA）。\n\n### §4 Related Work\n- 缺 non-agent adaptive computation 方向（early exit: CALM; per-token allocation: Mixture-of-Depths）。\n- Appendix O 的 action-space filtering 本质是 shielding——应引用 Alshiekh et al. (2018)。\n\n### §5 Discussion\n- Paragraph 1 \"signal-limited\" 解释应与 \"data-limited\" 更对称呈现。当前叙事倾向 signal-limited（Interpretation B），但 9 个 internal-preferred 样本 + paraphrase-only augmentation 不足以完全排除 data-limited。\n- 增加 2-3 句讨论 concurrent routing methods（CogRouter, ARES, MTRouter）在 death-dominated 环境中的预期表现。\n- 增加 1-2 句讨论 graded failure（非 binary death/alive）场景下框架的适用性。\n\n### §6 Conclusion\n- \"the diagnostic procedure transfers\" 需加限定：transfer 的是 procedure 而非 operationalization。\n\n### Limitations\n- Statistical limitations 段应显式引用 Cameron et al. (2008) K≥20-50 建议。\n- 增加 72B 实验 scope 限制的说明。",
  "project": "simgate-modular-routing",
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
    "report": "# Round 28 审稿报告 — simgate-modular-routing\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**Venue**: EMNLP 2026 (ARR May cycle), Interpretability and Analysis track\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1 方法严谨性+实验设计, R2 新颖性+完整性+写作）\n**交叉轮次**: 1 轮（关键问题达成共识，无需 Round 2）\n\n---\n\n## Summary\n\n论文提出 episode-level counterfactual diagnostic framework，通过对比 pure-strategy（internal-only vs deterministic-only）的 episode outcomes 来 decompose routing signal 的组成。应用于 ScienceWorld（11 task types, 245 episodes），发现 78.9% 的 non-tie routing labels 源于 death asymmetry（内部策略触发 -100 死亡惩罚而确定性策略存活）。Cross-model replication（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B-it）确认 DAF 88-90%（spread 2.2pp）。Router training（Qwen3 0.6B-4B）在 episode level 降至 chance 以下，报告为 diagnostic negative result。Cross-environment probes（MATH, ALFWorld）展示框架在无 death 环境中诊断不同 routing mechanism 的能力。\n\n---\n\n## Strengths\n\n1. **极其详尽的鲁棒性验证**（R1-S2, R2-S1）：20 个 appendix 覆盖 LOO、cluster bootstrap、wild bootstrap、penalty sensitivity、cross-model、cross-environment、capacity scaling、augmentation ablation 等——在 analysis track 论文中属顶级水平。\n2. **诚实的负面结果报告**（R1-S3, R2-S2）：Router training failure（episode-level balanced accuracy 47.1% < 50% chance）被完整报告而非隐藏，提供两种可能解释（signal-limited vs data-limited），附带 text augmentation、capacity scaling、death-proximal labeling 等排除实验。\n3. **Cross-model convergence**（R1-S4, R2-S4）：三个架构差异显著的 7-9B 模型家族 + 72B scaling 给出 DAF 88-92%（spread 2.2pp），有力排除模型特异性解释。\n4. **Penalty-independent 与 penalty-dependent 度量双轨报告**（R2-S3）：区分 label fraction (78.9%, P-invariant) 和 DAF (90.4%, P-dependent)，展示完整 P-sensitivity 曲线（Appendix K）。\n5. **Track fit 优秀**（R2-S5）：\"先诊断 routing signal 再决定是否训练 router\" 的理念与 Interpretability and Analysis track 高度匹配。\n6. **研究问题定义清晰**（R1-S1）：填补了 routing literature 中\"routing signal 到底由什么组成\"这一方法论空白。\n\n---\n\n## Weaknesses\n\n### Must-Fix（2 项，双方共识）\n\n**[AGREE x2] W-Critical-1: DAF 度量的 P-dependence 在主文中讨论不足**\n- 来源：R1-N2 + R2-N1（完全共识）\n- 问题：DAF = δP/(δP + Δ_nd) 随 P 单调递增（P=10→50.4%, P=50→82.6%, P=100→90.4%, P=200→94.9%），是数学必然而非纯实证发现。Appendix K 承认\"mathematical consequence\"，但主文 §2.4 仅标记 DAF 为 \"derived penalty-dependent measure\"，未展示 P-sensitivity 的任何数值。Abstract 虽以 78.9% 为 headline，但 DAF=90.4% 仍以核心数字地位出现。\n- 影响：Analysis track 论文的核心度量之一有数学 artifact 成分但主文透明度不足，可能导致读者高估 finding 的实证强度。\n- 建议：(1) §2.4 定义 DAF 后增加 1-2 句正文讨论 P-sensitivity（至少引用 P=10 和 P=50）；(2) Abstract/Conclusion 进一步降低 DAF 的 prominence。\n\n**[AGREE x2] W-Critical-2: \"Deterministic\" 跨环境含义不统一，transfer claim 需更精确限定**\n- 来源：R2-N2（R1 交叉时 AGREE）\n- 问题：三环境 \"deterministic\" 实现差异巨大（oracle simulator / code interpreter / admissible-action enumeration），信息优势程度不可比。§2.1 描述了差异但 Conclusion 仍写 \"the diagnostic procedure transfers\"，暗示跨环境一致性高于实际水平。\n- 影响：读者可能期望比论文实际提供的更强的泛化性。\n- 建议：Conclusion 或 §3.4 增加限定：cross-env probes 验证 diagnostic procedure 的可复用性，不是 \"deterministic computation\" 概念的一致性。\n\n### Should-Fix（7 项）\n\n**[AGREE x2] W1: 63% task type 排除率需在主文更充分 justify**\n- 来源：R1-W2 + R2-W1\n- 问题：主文 §3 仅一句话说明排除原因。缺 taxonomic redundancy 的操作定义。Anti-cherry-picking 数据（excluded ΔDR=+38.2 > included +28.7 pp）全在 appendix。\n- 建议：§3 增加一段展示 key numbers + taxonomic redundancy 定义。\n\n**[DIVERGENCE → warning] W2: Episode→step 粒度失配的 framing 精确性**\n- 来源：R1-N1（critical）vs R2 REBUT（warning）\n- R1 主张：Title/Abstract 暗示 step-level routing 发现，实际证据限于 episode-level outcome。\n- R2 反驳：\"Routing Signal\" ≠ \"Routing Decision\"；episode-level 是 sparse-reward 环境的 principled granularity（97.4% step ties）。但同意 Abstract 应加 \"episode-level\" 限定词。\n- 最终判定：降为 warning。Claim validity 不受影响，但 framing 可更精确。\n- 建议：Abstract 中 \"78.9% of non-tie routing labels\" 前增加 \"episode-level\"。\n\n**[AGREE with nuance x2] W3: Router negative result 的 signal-limited vs data-limited 区分不完全**\n- 来源：R1-W3 + R2-W2\n- R2 REBUT R1 的 \"架构简单\" 批评（6 种变体 + LOTO + death-proximal labeling），但 AGREE paraphrase augmentation 不增加新 routing signal，真实 episode-level scaling 未测试。\n- 建议：§5 更对称呈现两种解释，明确当前数据量不足以完全区分。\n\n**[AGREE x2] W4: K=11 cluster bootstrap 局限性未在主文充分标注**\n- 来源：R1-W1\n- 建议：Limitations 显式引用 Cameron et al. K≥20-50 建议。\n\n**[AGREE x2] W5: 72B scaling 仅做 probe 不够完整**\n- 来源：R1-W4\n- 建议：Limitations 中标注 72B scope 限制；讨论更强模型下 non-death signal 是否可能超过 death signal。\n\n**[AGREE x2] W6: \"Death\" 术语限制 generality — graded failure 适用性未讨论**\n- 来源：R2-W5\n- 建议：Discussion 增加 1-2 句讨论 graded failure 场景。\n\n**[AGREE partially] W7: 缺与 concurrent routing methods 的定性讨论**\n- 来源：R2-W4\n- 建议：§5 或 §4 增加 2-3 句讨论 CogRouter/ARES/MTRouter 在 death-dominated 环境中的预期表现。\n\n### Minor（5 项）\n\n- **M1**: Figure 2 仅 11 点无 task name label [AGREE x2]\n- **M2**: §1 Introduction \"signal diversity can collapse\" 重复出现 [R2]\n- **M3**: Pages 7-8 连续两页纯文本无 display item [视觉审查]\n- **M4**: Missing references: Alshiekh et al. (2018) Safe RL via Shielding, Geifman & El-Yaniv (2017) Selective Classification, Schuster et al. (2022) CALM, Raposo et al. (2024) Mixture-of-Depths [R1+R2 共 4 条]\n- **M5**: Related Work 缺 non-agent adaptive computation (early exit, speculative decoding) [R1-M6, R2 AGREE]\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成完全共识 [AGREE x2]：\n1. DAF P-dependence 是最需要作者回应的 critical issue（label fraction 应为 primary metric）\n2. \"Deterministic\" 跨环境语义不同需更精确限定 transfer claim\n3. 63% task 排除率需更充分正文 justify\n4. K=11 cluster bootstrap 局限需显式标注\n5. 72B 实验 scope 有限\n6. 论文鲁棒性验证水平在 analysis track 中属上乘（20 appendices）\n7. 负面结果报告（router failure）诚实且有价值\n8. Cross-model convergence（3 family, DAF 88-90%）有力排除模型特异性\n\n## Reviewer Divergence\n\n**Episode→step 粒度失配的严重程度**：\n- R1 评为 critical：Title/Abstract scope 超出方法论覆盖范围\n- R2 评为 minor framing issue：论文 claim 是关于 \"signal composition\" 而非 \"step-level decision\"，episode-level 是 principled granularity\n- R2 提供的反驳依据：(1) §2.2 论证了 97.4% step ties 使 episode-level 成为唯一有效粒度；(2) 61.2% no-preference 也是诊断信息；(3) §3.6 和 §5 已详细讨论 step-level router failure\n- **最终判定**：降为 warning —— claim validity 不受影响，但 Abstract 应加 \"episode-level\" 限定词\n\n**Limitations 长度**：\n- R2 评为 warning（5 段过长，建议压缩到 3 点）\n- R1 REBUT（analysis 论文的诚实 limitations 是优势而非缺陷，且不占页数限制）\n- **最终判定**：不列入 weakness — R1 理由充分，Limitations 内容均为必要 caveats\n\n**Router 架构简单性是否是负结论的主要限制**：\n- R1 评为 warning（仅测试 Qwen3 0.6B-4B + LoRA）\n- R2 REBUT（6 种变体收敛、LOTO 打回、death-proximal labeling 无效），但 AGREE scope 限定可更精确\n- **最终判定**：保留为 W3 的子问题，建议更对称呈现双解释\n\n---\n\n## Questions to Authors\n\n1. **P=0 下 78.9% label fraction 的稳定性**：论文声称 label fraction 是 P-invariant 的，但 §3.1 提到 54 个 \"sole-signal labels\" 在 P=0 时退化为 ties——这意味着 P=0 下 label fraction 会从 78.9% 降低。Algorithm 1 的 death-first priority 等价于隐式无穷大 penalty，这与 \"penalty-independent\" 叙事存在微妙张力。请澄清。\n2. **150 个 no_pref episodes 的 action sequence 相似度**：两策略在相同 outcome 下是否采取了相似路径？如果路径不同但结果相同，可能存在被 episode-level aggregation 掩盖的 step-level routing signal。\n3. **72B 条件下 non-death signal 是否增强**：72B 的 death rate 降至 30.6%，意味着更多 episodes 双方存活。$\\Delta_{\\text{nd}}$ 是否在 72B 上显著增大？如果是，death dominance 的 scale-robustness 结论是否需要 qualify？\n\n---\n\n## Missing References\n\n- Alshiekh et al., \"Safe Reinforcement Learning via Shielding\" (AAAI 2018) — Appendix O action-space filtering 本质是简化版 shield [R2, R1 AGREE]\n- Geifman & El-Yaniv, \"Selective Classification for Deep Neural Networks\" (NeurIPS 2017) — selective prediction 经典，与 routing/abstention 概念关联 [R2, R1 AGREE]\n- Schuster et al., \"Confident Adaptive Language Modeling\" (NeurIPS 2022) — non-agent adaptive computation baseline [R1, R2 AGREE]\n- Raposo et al., \"Mixture-of-Depths\" (ICML 2024) — per-token computation allocation [R1, R2 AGREE]\n\n---\n\n## External Review\n\n未请求（项目未配置 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成。3 warnings, 14 info。\n\n**Warnings**:\n1. **Pages 7-8 连续两页纯文本**：§3.6 (Router Training) + §4 (Related Work) + §5 (Discussion) + §6 (Conclusion) 无任何 display item，阅读节奏单调。建议 §3.6 router 结果可用小 table 呈现。\n2. **Page 9 Limitations 篇幅较大**：5 个子段落几乎填满整页。（但 Reviewer 圆桌讨论认为此内容均为必要 caveats，不建议删减。）\n3. **Page 24 末页空白**：附录末页仅约 1/4 内容，空间利用率低。\n\n**正面发现**：\n- 全文无 LaTeX 渲染错误、margin 溢出或 section heading 孤悬\n- 双栏排版间距均匀，行号完整（submission 格式正确）\n- 主体正文 8 页含 5 个 display items（Figure 1-3, Table 1-2），对诊断型论文属合理范围\n- 所有 table 使用 booktabs 风格，格式规范\n- Figure 3 使用 shaded error bands，可视化实践良好\n- 颜色语义跨图一致\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n**评分理由**：\n\n论文在 ScienceWorld 环境内做了一项极其详尽的诊断分析——20 个 appendix 的鲁棒性验证、3 个模型家族的 cross-model replication、router training 负结论的多层论证——在 methodological rigor 上无可挑剔。78.9% death-asymmetric label fraction 作为 penalty-independent 的核心发现是可靠的，cross-model convergence（spread 2.2pp）有力排除了模型特异性。\n\n但以下结构性限制将论文定位在 Findings 而非 main conference：\n\n1. **Excitement deficit（R1 3/5, R2 3/5）**：核心发现——在有 catastrophic failure 的环境中 death avoidance 主导 routing signal——具有一定的 a priori 可预测性。当一种策略有 oracle access 而另一种策略会\"死\"时，oracle 更安全是 expected 的。论文的贡献在于量化了这一直觉（78.9%）并系统排除了 alternative explanations，但 insight 的 surprise value 有限。\n2. **DAF 度量的数学 artifact**：核心度量之一（DAF=90.4%）部分由 P=100 的选择决定（P=10 时仅 50.4%），虽然 label fraction 提供了 P-invariant 的补充，但主文对 P-sensitivity 的透明度不足。\n3. **单环境主体验证**：完整验证仅在 ScienceWorld 上完成，MATH 和 ALFWorld 只是 boundary probes（且 \"deterministic\" 含义不可比）。框架的 methodological generality 合理，但 empirical generality 证据不足。\n4. **Actionability gap**：框架是 diagnostic 而非 prescriptive——诊断出 death dominance 后的 practical next step（除了 \"用 always-deterministic\"）不够清晰。\n\n综合两位 Reviewer 独立评分均为 3.5 (Borderline Conference)，考虑到 excitement deficit 是持续存在的结构性限制（从 Round 16 至今），且 Must-Fix 问题均为 framing 层面（可修但不改变核心 contribution 的 novelty），判定为 **3.0 (Findings)**——论文质量足以被 Findings 接收，但核心 contribution 的 novelty 和 generality 尚不足以推荐 main conference。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"signal diversity can collapse to a single dominant mechanism\" 在 para 5 和 contributions list item 2 中重复出现，措辞几乎相同——合并或删除一处。\n- Contributions 列表三项，每项内容过长（item 2 跨 3 行），建议精简。\n\n### §2 Method\n- §2.4 DAF 定义后应立即讨论 P-sensitivity，至少引用 P=10 (50.4%) 和 P=50 (82.6%)。当前叙事在此处建立了 DAF 的重要性，但读者要翻到 Appendix K 才发现 90.4% 有数学 artifact 成分。\n- §2.1 \"deterministic\" operationalization 差异已描述，但应更明确标注\"这些定性差异影响框架能检测到的 routing signal 类型\"不仅是 caveat，而是 cross-env 分析的核心前提。\n\n### §3 Experiments\n- §3 第一段 63% 排除率应展开。建议增加一段：(1) excluded tasks ΔDR=+38.2 > included +28.7 pp；(2) taxonomic redundancy 操作定义；(3) agent-floor tasks 排除的合理性。\n- §3.1 Figure 2 scatter plot：11 点 + r=0.97 的 structural consequence caveat 可以更 prominent（当前在 caption 末尾）。建议加 task name label。\n- §3.4 ALFWorld 分析仅一段话，作为三个 cross-env probes 之一显得单薄。至少应引用 Appendix L 的 Table/Figure。\n- §3.6 Router training 负结论 scope 可更精确——\"no step-level learnable signal exists under current architectures and data regime\" 中 \"current architectures\" 应明确列出（Qwen3 0.6B-4B with LoRA）。\n\n### §4 Related Work\n- 缺 non-agent adaptive computation 方向（early exit: CALM; per-token allocation: Mixture-of-Depths）。\n- Appendix O 的 action-space filtering 本质是 shielding——应引用 Alshiekh et al. (2018)。\n\n### §5 Discussion\n- Paragraph 1 \"signal-limited\" 解释应与 \"data-limited\" 更对称呈现。当前叙事倾向 signal-limited（Interpretation B），但 9 个 internal-preferred 样本 + paraphrase-only augmentation 不足以完全排除 data-limited。\n- 增加 2-3 句讨论 concurrent routing methods（CogRouter, ARES, MTRouter）在 death-dominated 环境中的预期表现。\n- 增加 1-2 句讨论 graded failure（非 binary death/alive）场景下框架的适用性。\n\n### §6 Conclusion\n- \"the diagnostic procedure transfers\" 需加限定：transfer 的是 procedure 而非 operationalization。\n\n### Limitations\n- Statistical limitations 段应显式引用 Cameron et al. (2008) K≥20-50 建议。\n- 增加 72B 实验 scope 限制的说明。",
    "project": "simgate-modular-routing",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.0"
  }
}
```

</details>

---


### Tool result

_source line 2349 · 2026-05-22T09:02:29.813180+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4368
}
```

</details>

---


### Assistant

_source line 2350 · 2026-05-22T09:02:38.900971+00:00_

**Round 28 审稿完成。**

报告已投递至 Research Director。核心结论：

- **Overall: 3.0 (Findings)**，R1/R2 独立评分均 3.5，综合 excitement deficit（结构性限制）和 DAF 数学 artifact 降为 3.0
- **2 个 Must-Fix**（双方共识）：DAF P-dependence 主文透明度不足；"deterministic" 跨环境语义不统一的 transfer claim 需限定
- **7 个 Should-Fix**：63% task 排除率正文不足、episode→step framing 精确性、router 负结论双解释对称性、K=11 标注、72B scope、"death" 术语 generality、concurrent methods 讨论
- **1 个分歧记录**：R1 认为 episode→step 粒度失配是 critical，R2 REBUT 认为 episode-level 是 principled granularity，最终降为 warning
- **结构性限制**：R16-N1（novelty/excitement deficit）持续 12 轮未解决，Findings 定位

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 197

## Round 197

64 recorded events


### User

_source line 2351 · 2026-05-22T22:49:29.116424+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (8 pages)
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

_source line 2352 · 2026-05-22T22:49:34.954881+00:00_

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

_source line 2353 · 2026-05-22T22:49:34.955847+00:00_

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
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2354 · 2026-05-22T22:49:40.880557+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
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

_source line 2355 · 2026-05-22T22:49:40.931179+00:00_

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

_source line 2356 · 2026-05-22T22:49:48.212858+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
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

_source line 2357 · 2026-05-22T22:49:48.214126+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 2358 · 2026-05-22T22:49:51.528171+00:00_

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

_source line 2359 · 2026-05-22T22:49:51.528569+00:00_

No matching deferred tools found

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

_source line 2360 · 2026-05-22T22:49:51.980557+00:00_

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

_source line 2361 · 2026-05-22T22:49:52.434885+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (121 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| alfworld-llama-cross-model | Llama-3.1-8B on ALFWorld will show information asymmetry (not death) as the dominant routing mechanism, consistent with Qwen2.5-7B findings (25.9% det-preferred, DAF=0%), confirming the framework diagnoses environment-specific mechanisms regardless of model family. | — | — | — |\n| gemma-scienceworld-cross-model | Gemma-2-9B-it on ScienceWorld will show death dominance (DAF > 80%) consistent with Qwen2.5-7B (90.4%) and Llama-3.1-8B (88.2%), extending the cross-model-family evidence from 2 to 3 independent model families and strengthening the claim that death avoidance dominates routing signal regardless of model architecture. | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **gemma-scienceworld-gpu0** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) observed with Qwen2.5-7B (DAF=90.4%) and Llama-3.1-8B (DAF=88.2%), confirming the diagnostic finding is model-agnostic across 3 model families.\n- **gemma-scienceworld-v4** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) ob
…[truncated 1790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 2362 · 2026-05-22T22:49:58.847549+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
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
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 2363 · 2026-05-22T22:49:58.847925+00:00_



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

_source line 2364 · 2026-05-22T22:50:00.355054+00:00_

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

_source line 2365 · 2026-05-22T22:50:00.456424+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\graphicspath{{figures/}}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{algorithm}
16	\usepackage{algorithmic}
17	\usepackage{tcolorbox}
18	\tcbuselibrary{listings,breakable}
19	
20	\hypersetup{pdfauthor={},pdftitle={}}
21	
22	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{abstract}
30	\input{introduction}
31	\input{method}
32	\input{experiments}
33	\input{related_work}
34	\input{discussion}
35	\input{conclusion}
36	
37	\section*{Limitations}
38	
39	\paragraph{Environmental scope.}
40	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct), though extended validation of representative excluded tasks confirms the pattern (Appendix~\ref{app:extended-validation}). The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface non-death-dominated signal that our current setup does not capture. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:cross-env}, \S\ref{sec:discussion}) provide preliminary supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct cross-model replication (11 task types, $N{=}220$; \S\ref{sec:cross-model}) shows death dominance replicates with direction consistency 10/10 while vulnerability magnitude varies ($+30.0$~pp vs.\ Qwen $+26.5$~pp), though both models are in the 7--8B parameter range; Qwen2.5-72B ($10{\times}$ scale) re
…[truncated 7304 chars]

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

_source line 2366 · 2026-05-22T22:50:07.589081+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR"
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
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool call

_source line 2367 · 2026-05-22T22:50:10.452003+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_29/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_29/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2368 · 2026-05-22T22:50:11.006172+00:00_

-rw-r--r-- 1 ubuntu ubuntu 598239 May 22 22:47 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_29/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 2369 · 2026-05-22T22:50:11.358494+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/*.tex",
  "description": "List all tex files in paper directory"
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
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/*.tex",
    "description": "List all tex files in paper directory"
  }
}
```

</details>

---


### Tool result

_source line 2370 · 2026-05-22T22:50:11.461074+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/responsibleNLPchecklist.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 2371 · 2026-05-22T22:50:15.628532+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 using the ARR (ACL Rolling Review) system:

## Paper Types and Scope
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Important Deadlines
The ARR submission deadline for long & short papers is May 25, 2026, with a reviewer registration deadline for ALL authors on May 27
…[truncated 1051 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 8039
}
```

</details>

---


### Tool call

_source line 2372 · 2026-05-22T22:50:24.891817+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract ALL submission guidelines: page limits (long paper, short paper), template requirements, anonymity rules, appendix rules, citation format, supplementary material rules, responsible NLP checklist requirements, and any other formatting requirements. Be comprehensive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract ALL submission guidelines: page limits (long paper, short paper), template requirements, anonymity rules, appendix rules, citation format, supplementary material rules, responsible NLP checklist requirements, and any other formatting requirements. Be comprehensive."
  }
}
```

</details>

---


### Tool call

_source line 2373 · 2026-05-22T22:50:25.496370+00:00_

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

_source line 2374 · 2026-05-22T22:50:26.300137+00:00_

1	\begin{abstract}
2	LLM agent routing (deciding when to rely on internal reasoning versus external tool use) is typically addressed by training routers directly, without first understanding what mechanistic signal drives the routing preference. This absence of diagnostic methods risks building routers atop confounded or trivial signal. We propose an episode-level counterfactual framework that compares pure-strategy outcomes (internal-only vs.\ deterministic-only) to decompose routing signal into its mechanistic components before any router is constructed. Applying this framework to ScienceWorld (11 task types, 245 episodes), we find that 78.9\% of non-tie episode-level routing labels arise from death asymmetry---a finding replicated across three architecturally distinct 7--9B model families (spread 2.2\,pp), revealing that in catastrophic-failure environments, signal diversity can collapse to a single dominant mechanism. Cross-environment probes on MATH and ALFWorld diagnose qualitatively different routing mechanisms (no extractable signal and information asymmetry, respectively), providing preliminary evidence of applicability beyond death-dominated settings. The framework distinguishes \emph{methodological generality} (applicable to any environment with paired episode outcomes) from \emph{empirical generality} (full quantitative validation on ScienceWorld only). A ${\sim}$50-episode diagnostic pilot provides preliminary build-vs-buy signal given large effect sizes ($d = 3.02$); environments with smaller effects may require larger samples.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 2375 · 2026-05-22T22:50:26.300756+00:00_

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

_source line 2376 · 2026-05-22T22:50:26.301131+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	In ScienceWorld \citep{scienceworld-2022}, a text-based science simulation, internal reasoning is error-prone, as the model may hallucinate state changes (e.g., that water has boiled when the stove was never activated), while deterministic external computation eliminates such errors via exact state transitions. The practical question: \emph{when should an agent route computation externally versus internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision: Toolformer \citep{toolformer-2023} inserts API calls by perplexity reduction; ART \citep{art-2023} decomposes tasks into tool-augmented programs; Chameleon \citep{chameleon-2023} selects heterogeneous modules per subtask; adaptive-computation methods route to different reasoning depths \citep{cogrouter-2026,ares-2026}, model tiers \citep{mtrouter-2026}, or episode-level model selection under sparse rewards \citep{budget-aware-routing-2026}; concurrent analyses further presuppose diverse routing signals~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026}. These approaches, which operate in non-catastrophic settings, share the assumption that routing signal stems from diverse sources and a learned router can exploit it---an assumption that remains untested: no prior work has decomposed what drives routing decisions in interactive environments.
7	
8	We propose a \emph{diagnostic framework} comprising (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95), a penalty-independent finding. Under 
…[truncated 2479 chars]

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

_source line 2377 · 2026-05-22T22:50:26.451968+00:00_

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

_source line 2378 · 2026-05-22T22:50:26.502827+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/pipeline_overview.pdf}
7	\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\ref{alg:labeling}.}
8	\label{fig:pipeline}
9	\end{figure}
10	
11	Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically (Appendix~\ref{app:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
12	
13	\subsection{Problem Setup}
14	\label{sec:problem-setup}
15	
16	Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\citep{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic} (${\tt det}$), a privileged-information strategy that eliminates observation uncertainty---instantiated as oracle simulator (ScienceWorld), code interpreter (MATH), or admissible-action enumeration (ALFWorld); these qualitative differences affect what routing signals the framework can detect. A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \math
…[truncated 7474 chars]

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


### Tool result

_source line 2379 · 2026-05-22T22:50:30.070157+00:00_

# EMNLP 2026 Submission Guidelines Summary

## Page Limits

**Long Papers:** "8 pages" with one additional page allowed in camera-ready versions (up to 9 pages total for addressing reviewer feedback)

**Short Papers:** "4 pages" with one additional page in final versions (up to 5 pages maximum)

## Template & Formatting

The call references ARR requirements but doesn't specify exact templates directly. Authors must "follow all of the ARR submission requirements" including paper formatting standards maintained at the ACL Rolling Review platform.

## Anonymity Rules

The conference maintains double-blind review. "Reviewers will not see authors, nor will authors see reviewers" during the process. However, authors may optionally make their anonymized submissions publicly visible. Notably, "there is no anonymity period requirement" following ACL and ARR policies.

## Supplementary Materials

"Optional Supplementary Materials" are permitted, including appendices, software, and data, governed by ARR guidelines.

## Other Requirements

Authors must provide:
- A limitations section
- Two-way anonymized review compliance
- The "responsible NLP research checklist"
- Adherence to ACL Publication Ethics Policy and ARR Ethics Policy
- Proper disclosure per ACL Disclosure Policy
- Writing assistance is permitted

## Authorship During Commitment

Author list modifications aren't permitted at commitment stage, though reordering authors is allowed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebFetch",
  "elapsed_ms": 5178
}
```

</details>

---


### Tool call

_source line 2380 · 2026-05-22T22:50:39.162619+00:00_

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

_source line 2381 · 2026-05-22T22:50:39.615436+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types (63\%) lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). Taxonomically redundant tasks share reward structure and action space, differing only in target entity (Appendix~\ref{app:per-task}). This scope limits generalizability: conclusions apply to the included subset, not to all ScienceWorld tasks. An anti-cherry-picking analysis confirms that death dominance holds in 18 of these 19 types, with a mean $\Delta\text{DR} = +38.2$\,pp exceeding the included tasks' $+28.7$\,pp (Appendix~\ref{app:per-task}). Extended validation at $n{=}20$ on five representative excluded tasks confirms this direction ($\overline{\Delta\text{DR}} = +32.0$\,pp; Appendix~\ref{app:extended-validation}). A reasoning-depth ablation ($n{=}120$) found no significant difference between internal strategy variants ($p > 0.26$; Appendix~\ref{app:ablations}). Prescreening used $n{=}5$ episodes per task type; directional consistency (18/19 types favoring deterministic) rather than point estimates drives the inclusion criterion.
5	
6	\subsection{Death Avoidance Decomposition}
7	\label{sec:death-decomp}
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=0.38\textwidth]{figures/fig1_daf_scatter.pdf}
12	\caption{Internal consistency check: per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$ (Spearman's $\rho = 0.986$; Appendix~\ref{app:per-task}), $p < 10^{-6}$, $n = 11$ task types. Since $\Delta_{\text{full}} \approx \delta P + \Delta_{\text{nd}}$ with $P$ constant, $r \to 1$ as DAF $\to 1$; the near-perfect correlation is a structural consequence of death dominance, not an independent finding (\S\ref{sec:death-decomp}).}
13	\label{fig:decomposition}
14	\end{figure}
15	
16	Of the 95 non-tie routing labels,
…[truncated 15006 chars]

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

_source line 2382 · 2026-05-22T22:50:39.615934+00:00_

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

_source line 2383 · 2026-05-22T22:50:40.118425+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}, spanning several functional categories.
5	Self-supervised methods learn tool invocation from loss signals \citep{toolformer-2023,toolace-2025}, token-level methods embed tools in the vocabulary \citep{toolkengpt-2023}, task-level decomposition routes subtasks to specialized modules \citep{art-2023,chameleon-2023}, and RL-based methods learn routing from reward \citep{retool-2025}.
6	All focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
7	Concurrent work examines \emph{when} to invoke tools: tool-call decisions correlate with uncertainty~\citep{tool-overuse-illusion-2026}, are encoded in hidden states~\citep{when2tool-2026}, impose a ``tool-use tax''~\citep{tool-use-tax-2026}, or follow necessity-utility-affordability logic~\citep{to-call-or-not-2026}. Our decomposition yields a concrete answer: 78.9\% of non-tie routing labels trace to catastrophic-failure prevention.
8	
9	\paragraph{Adaptive Computation and Routing.}
10	Adaptive routing traces back to learned halting policies \citep{graves2016act}. Mixture-of-Recursions \citep{mixture-of-recursions-2025} learns token-level recursion depths in the LLM era; concurrent work further diversifies routing granularity: CogRouter \citep{cogrouter-2026} adapts per-step depth, ARES \citep{ares-2026} selects effort levels, and MTRouter \citep{mtrouter-2026} addresses multi-turn settings.
11	RouteLLM \citep{routellm-2024} learns routers from preference data to select between strong and weak models.
12	Concurrently, \citet{budget-aware-routing-2026} train episode-level routing policies under sparse terminal rewards, the closest setting to ours; they optimize \emph{which} model to invoke, whereas we diagnose \emph{what} drives the routing decision.
13	Mixture-of-Experts architecture
…[truncated 2335 chars]

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

_source line 2384 · 2026-05-22T22:50:40.169111+00:00_

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

_source line 2385 · 2026-05-22T22:50:40.621446+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Signal granularity and router failure.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property (10/11 types carry death risk), but step-level features correlate weakly because death risk depends on multi-step trajectories. Six router variants (0.6B--4B, classification and generative) converge on near-chance step-level accuracy ($56$--$59\%$); this convergent failure is consistent with signal limitation; however, extreme class imbalance (90.5\% deterministic-preferred, only 9 internal-preferred episodes) makes a data-limited explanation equally plausible---distinguishing the two requires ${\sim}$1{,}350 paired episodes to obtain 50 minority-class samples. Cross-task-type transfer yields chance accuracy (49.2\%; Appendix~\ref{app:ablations}). Training on pure-strategy labels but deploying under mixed-strategy routing also introduces a distribution shift~\citep{dagger-2011}; the negative result may partly reflect this train--deploy mismatch. Concurrent routing methods (CogRouter, ARES, MTRouter) optimize step-level signals orthogonal to death avoidance; in death-dominated environments, this task-type-level binary signal is structurally inaccessible to step features.
6	
7	\paragraph{Non-triviality and oracle confound.}
8	While death dominance follows from the penalty structure (\S\ref{sec:daf}), two consequences were not predictable a priori: $10{\times}$ scaling to 72B fails to eliminate it (DAF${}= 92.4\%$), and Reflexion yields DAF${}>100\%$. All four interventions leave ${\geq}12$~pp residual gaps (Appendix~\ref{sec:threshold-routing}); cross-model DR stability ($36$--$43\%$) confirms death vulnerability is a task-environment property. An oracle confound arises: is the signal merely ``use the oracle''? Two observations argue otherwise: (a)~$\Delta_{\text{nd}} = 2.84$ (9.6\% of the total gap)---on non-death episodes, int
…[truncated 932 chars]

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

_source line 2386 · 2026-05-22T22:50:40.621958+00:00_

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

_source line 2387 · 2026-05-22T22:50:41.074176+00:00_

1	\section{Conclusion}
2	
3	In ScienceWorld, death avoidance alone accounts for 78.9\% of non-tie routing labels, replicated across three 7--9B model families (spread 2.2\,pp); our episode-level counterfactual framework diagnoses this before any router is built. Cross-environment probes provide preliminary evidence that the diagnostic procedure---though not the specific operationalization of ``deterministic''---transfers across environments with qualitatively different information asymmetries; a ${\sim}$50-episode pilot provides preliminary build-vs-buy signal given large effect sizes ($d = 3.02$). Future work should validate death dominance in additional catastrophic-failure environments and investigate whether lightweight death-prediction mechanisms can exploit this task-type-level binary structure without full step-level router training.
4	

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

_source line 2388 · 2026-05-22T22:50:42.832572+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract ALL formatting requirements for ARR submissions: page limits, template, anonymity policy, appendix rules, supplementary materials, responsible NLP checklist, citation format, font requirements, and any other formatting or content requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract ALL formatting requirements for ARR submissions: page limits, template, anonymity policy, appendix rules, supplementary materials, responsible NLP checklist, citation format, font requirements, and any other formatting or content requirements."
  }
}
```

</details>

---


### Tool result

_source line 2389 · 2026-05-22T22:50:49.972683+00:00_

# ARR Submission Formatting Requirements

## Page Limits

**Long Papers:** "up to eight (8) pages of content" plus unlimited references and space for required limitations section and optional ethical considerations section.

**Short Papers:** "up to four (4) pages of content" plus unlimited references and limitations/ethics sections.

Papers exceeding length requirements or missing the mandatory limitations section face desk rejection.

## Template & Style

Submissions must use "the official ACL style template" available on GitHub. Authors cannot modify these files or use templates from other conferences. Formatting must comply with "*ACL" conference guidelines regarding paper size, margins, and font restrictions. Non-compliant submissions are rejected without review.

## Anonymity Requirements

Papers must exclude author names, affiliations, and self-identifying references. Use construction like "Smith showed (Smith, 1991)" rather than "We previously showed." Avoid references to documents unavailable to reviewers. Supplementary materials and repository links must be anonymized. Violations result in desk rejection. Two-way anonymized review is enforced.

## Limitations Section (Required)

A dedicated "Limitations" section must appear before references without counting toward page limits. This section cannot introduce new methods, analysis, or results—only discuss constraints of presented work. Omitting this section triggers desk rejection.

## Appendices

Appendices follow references, don't count toward page limits, and must follow double-column formatting (with approved exceptions). Key technical content needed for assessment should be in the main paper, not appendices.

## Supplementary Materials

Authors may submit anonymized appendices, software (.tgz/.zip), or data (.tgz/.zip) separately. Cloud service links (Dropbox, Google Drive) are prohibited. Software via repositories must use anonymization services like Anonymous GitHub.

## Responsible NLP Checklist

"Au
…[truncated 477 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebFetch",
  "elapsed_ms": 7140
}
```

</details>

---


### Tool call

_source line 2390 · 2026-05-22T22:51:07.142032+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "review_issues.yaml",
  "max_chars": "5000"
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
    "file": "review_issues.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 2391 · 2026-05-22T22:51:07.795183+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 2392 · 2026-05-22T22:51:07.795657+00:00_

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

_source line 2393 · 2026-05-22T22:51:09.352360+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (121 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| alfworld-llama-cross-model | Llama-3.1-8B on ALFWorld will show information asymmetry (not death) as the dominant routing mechanism, consistent with Qwen2.5-7B findings (25.9% det-preferred, DAF=0%), confirming the framework diagnoses environment-specific mechanisms regardless of model family. | — | — | — |\n| gemma-scienceworld-cross-model | Gemma-2-9B-it on ScienceWorld will show death dominance (DAF > 80%) consistent with Qwen2.5-7B (90.4%) and Llama-3.1-8B (88.2%), extending the cross-model-family evidence from 2 to 3 independent model families and strengthening the claim that death avoidance dominates routing signal regardless of model architecture. | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **gemma-scienceworld-gpu0** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) observed with Qwen2.5-7B (DAF=90.4%) and Llama-3.1-8B (DAF=88.2%), confirming the diagnostic finding is model-agnostic across 3 model families.\n- **gemma-scienceworld-v4** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) ob
…[truncated 1790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1556
}
```

</details>

---


### Tool call

_source line 2394 · 2026-05-22T22:51:09.503434+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_29/submitted.pdf",
  "pages": "1-8"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_29/submitted.pdf",
    "pages": "1-8"
  }
}
```

</details>

---


### Tool result

_source line 2395 · 2026-05-22T22:51:10.158163+00:00_

PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_29/submitted.pdf (584.2KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 2396 · 2026-05-22T22:51:34.544305+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_29/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_29/submitted.pdf 2>/dev/null || echo \"pdfinfo not available\"",
  "description": "Check PDF page count"
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
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_29/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_29/submitted.pdf 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 2397 · 2026-05-22T22:51:35.548806+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Fri May 22 22:47:26 2026 UTC
ModDate:         Fri May 22 22:47:26 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           24
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       598239 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 2398 · 2026-05-22T22:51:36.454548+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Read existing review issues tracker"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Read existing review issues tracker"
  }
}
```

</details>

---


### Tool call

_source line 2399 · 2026-05-22T22:51:36.455105+00:00_

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


### Tool result

_source line 2400 · 2026-05-22T22:51:36.506310+00:00_

# Round 28 Review Issues (fresh review, 2026-05-22)
# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作)

# =============================================
# Carried-over resolved issues (from prior rounds)
# =============================================

- id: "R13-W1"
  summary: "正文篇幅严重不足 long paper 要求"
  category: format
  severity: warning
  status: resolved
  first_raised_round: 13
  last_seen_round: 14
  resolution: "正文已扩展至 8 页"
  resolution_round: 14

- id: "R13-W2"
  summary: "Router 训练实验存在多个 confound"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 13
  last_seen_round: 15
  resolution: "1.7B dip 有可检验假说，augmentation 术语修正，N 统一"
  resolution_round: 15

- id: "R13-W3"
  summary: "Episode-level label → step-level training 的 mislabeling 未被量化"
  category: method
  severity: info
  status: resolved
  first_raised_round: 13
  last_seen_round: 14
  resolution: "Limitations 和 Appendix B 已充分量化"
  resolution_round: 14

- id: "R13-W4"
  summary: "SCI 方法贡献与实际使用不成比例"
  category: method
  severity: info
  status: resolved
  first_raised_round: 13
  last_seen_round: 14
  resolution: "SCI 已降级到 Appendix A"
  resolution_round: 14

- id: "R13-W7"
  summary: "Router negative results 解释不完整"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 13
  last_seen_round: 15
  resolution: "Router 实验定位为 diagnostic probe"
  resolution_round: 15

- id: "R13-m2"
  summary: "Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld"
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 13
  last_seen_round: 16
  resolution: "Figure 3 已移除，数据在 Table 2 和正文中完整呈现"
  resolution_round: 16

- id: "R13-m3"
  summary: "Reference 格式不统一 + orphan entries"
  category: format
  severity: info
  status: resolved
  first_raised_round: 13
  last_seen_round: 15
  resolution: "Orphan entries 清理完毕，格式统一"
  resolution_round: 15

- id: "R14-W2"
  summary: "Concurrent work 讨论过于压缩"
  category: writing
  severity: info
  status: resolved
  first
…[truncated 21535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 2401 · 2026-05-22T22:51:36.506808+00:00_

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


### Tool call

_source line 2402 · 2026-05-22T22:52:16.385205+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -name \"*.yaml\" -path \"*/config*\" 2>/dev/null | head -5; find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -name \"config.yaml\" -o -name \"project.yaml\" -o -name \"settings.yaml\" 2>/dev/null | head -5",
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -name \"*.yaml\" -path \"*/config*\" 2>/dev/null | head -5; find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -name \"config.yaml\" -o -name \"project.yaml\" -o -name \"settings.yaml\" 2>/dev/null | head -5",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 2403 · 2026-05-22T22:52:16.488395+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/anonymous_code/configs/default.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 2404 · 2026-05-22T22:52:19.757877+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -maxdepth 3 -name \"*.yaml\" | xargs grep -l \"external_review\\|paperreview\" 2>/dev/null | head -5",
  "description": "Find files with external review config"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -maxdepth 3 -name \"*.yaml\" | xargs grep -l \"external_review\\|paperreview\" 2>/dev/null | head -5",
    "description": "Find files with external review config"
  }
}
```

</details>

---


### Tool result

_source line 2405 · 2026-05-22T22:52:19.858716+00:00_

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

_source line 2406 · 2026-05-22T22:52:23.924207+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -maxdepth 4 -name \"*.yaml\" | xargs grep -l \"external_review\\|paperreview\" 2>/dev/null | head -5; find /home/ubuntu/agent-ml-research -maxdepth 3 -name \"*.yaml\" | xargs grep -l \"external_review\\|paperreview\" 2>/dev/null | head -5",
  "description": "Find external review config broadly"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -maxdepth 4 -name \"*.yaml\" | xargs grep -l \"external_review\\|paperreview\" 2>/dev/null | head -5; find /home/ubuntu/agent-ml-research -maxdepth 3 -name \"*.yaml\" | xargs grep -l \"external_review\\|paperreview\" 2>/dev/null | head -5",
    "description": "Find external review config broadly"
  }
}
```

</details>

---


### Tool result

_source line 2407 · 2026-05-22T22:52:24.088750+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 164
}
```

</details>

---


### Tool call

_source line 2408 · 2026-05-22T22:52:43.331551+00:00_

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


### Tool result

_source line 2409 · 2026-05-22T22:53:06.479077+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23147
}
```

</details>

---


### Tool call

_source line 2410 · 2026-05-22T22:53:06.579916+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR May cycle)\n- **类别**: Long Paper (8 pages max main text, unlimited references)\n- **截止日期**: 2026-05-25\n- **模板**: ACL style, `\\usepackage[review]{acl}`\n- **匿名规则**: Double-blind\n- **Limitations**: 必须有（不计页数）\n- **Ethics**: 可选（不计页数）\n- **Responsible NLP Checklist**: 在 OpenReview 表单中填写，不在 PDF 中\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_29/submitted.pdf`\n\n## 你的审查侧重\n\n### 方法严谨性\n- Episode-level counterfactual labeling (Algorithm 1) 的设计是否合理？死亡优先规则是否引入 bias？\n- DAF 的数学定义和分解是否正确？DAF 与 P 的单调关系是否被充分讨论？\n- 78.9% label fraction (penalty-independent) vs DAF 90.4% (penalty-dependent) 的双指标体系是否恰当？\n- SCI (Signal Concentration Index) 作为补充指标的价值\n\n### 实验设计\n- 11/30 task types 选择（63% 排除）的 selection bias 是否被充分 justify？\n- N=245 episodes 的样本量是否足够？统计功效分析\n- 跨模型验证 (Qwen/Llama/Gemma 7-9B tier) 的设计合理性\n- 72B scaling probe 的实验 scope 是否足够？\n- Agent improvement baselines (Retry/Reflexion) 实验设计\n- Router training negative result 的解释——signal-limited vs data-limited 是否被公平呈现？\n- Cross-environment probes (MATH/ALFWorld) 的实验设计\n\n### 统计分析\n- Bootstrap CI 方法选择（episode-level vs cluster）\n- K=11 cluster bootstrap 的可靠性\n- Wild cluster bootstrap 补充分析\n- 效应量 Cohen's d=3.02 的解释\n- 多重比较校正（Bonferroni）的应用\n- McNemar test (MATH) 的适当性\n\n### 格式检查\n- 正文是否在 8 页内\n- Limitations section 是否存在且内容充分\n- 匿名合规性\n- 参考文献格式\n\n请按以下格式输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: [Critical/Major/Minor])\n4. **Questions** (需要作者回答的问题)\n5. **Missing References** (遗漏的重要相关工作)\n6. **Soundness** (1-5)\n7. **Excitement** (1-5)\n8. **Overall Assessment** (使用 EMNLP 2026 ARR 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit)\n9. **Confidence** (1-5)"
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
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR May cycle)\n- **类别**: Long Paper (8 pages max main text, unlimited references)\n- **截止日期**: 2026-05-25\n- **模板**: ACL style, `\\usepackage[review]{acl}`\n- **匿名规则**: Double-blind\n- **Limitations**: 必须有（不计页数）\n- **Ethics**: 可选（不计页数）\n- **Responsible NLP Checklist**: 在 OpenReview 表单中填写，不在 PDF 中\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_29/submitted.pdf`\n\n## 你的审查侧重\n\n### 方法严谨性\n- Episode-level counterfactual labeling (Algorithm 1) 的设计是否合理？死亡优先规则是否引入 bias？\n- DAF 的数学定义和分解是否正确？DAF 与 P 的单调关系是否被充分讨论？\n- 78.9% label fraction (penalty-independent) vs DAF 90.4% (penalty-dependent) 的双指标体系是否恰当？\n- SCI (Signal Concentration Index) 作为补充指标的价值\n\n### 实验设计\n- 11/30 task types 选择（63% 排除）的 selection bias 是否被充分 justify？\n- N=245 episodes 的样本量是否足够？统计功效分析\n- 跨模型验证 (Qwen/Llama/Gemma 7-9B tier) 的设计合理性\n- 72B scaling probe 的实验 scope 是否足够？\n- Agent improvement baselines (Retry/Reflexion) 实验设计\n- Router training negative result 的解释——signal-limited vs data-limited 是否被公平呈现？\n- Cross-environment probes (MATH/ALFWorld) 的实验设计\n\n### 统计分析\n- Bootstrap CI 方法选择（episode-level vs cluster）\n- K=11 cluster bootstrap 的可靠性\n- Wild cluster bootstrap 补充分析\n- 效应量 Cohen's d=3.02 的解释\n- 多重比较校正（Bonferroni）的应用\n- McNemar test (MATH) 的适当性\n\n### 格式检查\n- 正文是否在 8 页内\n- Limitations section 是否存在且内容充分\n- 匿名合规性\n- 参考文献格式\n\n请按以下格式输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: [Critical/Major/Minor])\n4. **Questions** (需要作者回答的问题)\n5. **Missing References** (遗漏的重要相关工作)\n6. **Soundness** (1-5)\n7. **Excitement** (1-5)\n8. **Overall Assessment** (使用 EMNLP 2026 ARR 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit)\n9. **Confidence** (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 2411 · 2026-05-22T22:53:23.028190+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16448
}
```

</details>

---


### Tool call

_source line 2412 · 2026-05-22T22:53:23.129070+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量 + Related Work 覆盖**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR May cycle)\n- **类别**: Long Paper (8 pages max main text, unlimited references)\n- **截止日期**: 2026-05-25\n- **模板**: ACL style, `\\usepackage[review]{acl}`\n- **匿名规则**: Double-blind\n- **Limitations**: 必须有（不计页数）\n- **Ethics**: 可选（不计页数）\n- **Responsible NLP Checklist**: 在 OpenReview 表单中填写，不在 PDF 中\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_29/submitted.pdf`\n\n## 你的审查侧重\n\n### 新颖性评估\n- 核心发现 (death avoidance dominates routing signal) 是否具有足够 novelty？\n- \"Death avoidance dominates in death-penalized environment\" 是否存在 triviality 风险？\n- 方法论贡献 (episode-level counterfactual framework) 是否有独立价值？\n- 与 concurrent routing work (CogRouter, ARES, MTRouter, budget-aware routing) 的区分度\n\n### 完整性检查\n- 论文结构是否完整（Abstract → Introduction → Method → Experiments → Related Work → Discussion → Conclusion → Limitations → Ethics）\n- 实验是否充分支撑所有 claims？\n- Contributions 列表与实际内容是否匹配？\n- Cross-environment probes 的 scope 是否与 claims 匹配？\n- Title/Abstract scope 是否与内容匹配？（episode-level vs step-level, methodological vs empirical generality）\n\n### 写作质量\n- 论文整体叙事结构和可读性\n- Abstract 是否准确反映核心发现？\n- Introduction 的 framing 和 motivation 是否清晰？\n- 术语一致性（computation modes, deterministic strategy, etc.）\n- 数字密度是否过高？\n- 信息重复和冗余\n- Figures/Tables 的质量和信息传递效率\n\n### Related Work 覆盖\n- Tool use / external computation 方向的覆盖是否充分？\n- Adaptive computation / routing 方向的引用\n- Counterfactual evaluation in RL 的覆盖\n- Safe RL / causal grounding 的引用\n- 遗漏的重要相关工作（特别是 2025-2026 concurrent work）\n- Non-agent adaptive computation (early exit, speculative decoding, MoD) 是否应覆盖？\n\n### 格式检查\n- 正文是否在 8 页内\n- Limitations section 质量\n- 匿名合规性\n\n请按以下格式输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: [Critical/Major/Minor])\n4. **Questions** (需要作者回答的问题)\n5. **Missing References** (遗漏的重要相关工作)\n6. **Soundness** (1-5)\n7. **Excitement** (1-5)\n8. **Overall Assessment** (使用 EMNLP 2026 ARR 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit)\n9. **Confidence** (1-5)"
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
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量 + Related Work 覆盖**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR May cycle)\n- **类别**: Long Paper (8 pages max main text, unlimited references)\n- **截止日期**: 2026-05-25\n- **模板**: ACL style, `\\usepackage[review]{acl}`\n- **匿名规则**: Double-blind\n- **Limitations**: 必须有（不计页数）\n- **Ethics**: 可选（不计页数）\n- **Responsible NLP Checklist**: 在 OpenReview 表单中填写，不在 PDF 中\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_29/submitted.pdf`\n\n## 你的审查侧重\n\n### 新颖性评估\n- 核心发现 (death avoidance dominates routing signal) 是否具有足够 novelty？\n- \"Death avoidance dominates in death-penalized environment\" 是否存在 triviality 风险？\n- 方法论贡献 (episode-level counterfactual framework) 是否有独立价值？\n- 与 concurrent routing work (CogRouter, ARES, MTRouter, budget-aware routing) 的区分度\n\n### 完整性检查\n- 论文结构是否完整（Abstract → Introduction → Method → Experiments → Related Work → Discussion → Conclusion → Limitations → Ethics）\n- 实验是否充分支撑所有 claims？\n- Contributions 列表与实际内容是否匹配？\n- Cross-environment probes 的 scope 是否与 claims 匹配？\n- Title/Abstract scope 是否与内容匹配？（episode-level vs step-level, methodological vs empirical generality）\n\n### 写作质量\n- 论文整体叙事结构和可读性\n- Abstract 是否准确反映核心发现？\n- Introduction 的 framing 和 motivation 是否清晰？\n- 术语一致性（computation modes, deterministic strategy, etc.）\n- 数字密度是否过高？\n- 信息重复和冗余\n- Figures/Tables 的质量和信息传递效率\n\n### Related Work 覆盖\n- Tool use / external computation 方向的覆盖是否充分？\n- Adaptive computation / routing 方向的引用\n- Counterfactual evaluation in RL 的覆盖\n- Safe RL / causal grounding 的引用\n- 遗漏的重要相关工作（特别是 2025-2026 concurrent work）\n- Non-agent adaptive computation (early exit, speculative decoding, MoD) 是否应覆盖？\n\n### 格式检查\n- 正文是否在 8 页内\n- Limitations section 质量\n- 匿名合规性\n\n请按以下格式输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: [Critical/Major/Minor])\n4. **Questions** (需要作者回答的问题)\n5. **Missing References** (遗漏的重要相关工作)\n6. **Soundness** (1-5)\n7. **Excitement** (1-5)\n8. **Overall Assessment** (使用 EMNLP 2026 ARR 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit)\n9. **Confidence** (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 2413 · 2026-05-22T22:53:24.655740+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1526
}
```

</details>

---


### Assistant

_source line 2414 · 2026-05-22T22:53:34.867198+00:00_

已完成：
- ✅ 视觉审查 Agent 已派发（与 Reviewer 并行）
- ✅ R1（方法严谨性 + 实验设计 + 统计分析）已分配
- ✅ R2（新颖性 + 完整性 + 写作质量 + Related Work）已分配
- ⏳ 外部审稿：未配置，跳过

等待两位 Reviewer 返回初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 198

## Round 198

2 recorded events


### User

_source line 2415 · 2026-05-22T22:58:33.336646+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计 + 统计分析

---

## 1. Summary

本文提出 episode-level counterfactual diagnostic framework，将 LLM agent routing signal 分解为 death avoidance 和 non-death 两个组成部分。在 ScienceWorld（11/30 task types, N=245 episodes）上发现 78.9% 的 non-tie routing labels 源自 death asymmetry（penalty-independent），DAF=90.4%（penalty-dependent at P=100）。训练的 router 在 episode-level 泛化上低于随机基线（47.1±2.2%）。跨模型（Llama-3.1-8B, Gemma-2-9B）和跨环境（MATH, ALFWorld）probes 提供初步支撑。核心贡献是诊断性的——在构建 learned router 之前应先检查 routing signal 是否被 catastrophic failure 所主导。

---

## 2. Strengths

**S1. 新颖且有价值的诊断视角。** 现有 routing 工作直接训练 router 而不先理解 routing signal 的构成。本文首次系统分解 routing signal，填补了一个重要的方法论空白。DAF 的数学定义（§2.4, Eq. 5）清晰，penalty-independent label fraction（78.9%）作为补充指标的选择也合理。

**S2. 极其详尽的统计分析。** 20 个 appendices（A–T）提供了罕见的深度：bootstrap CI、cluster-robust t-test、wild cluster bootstrap、exact permutation test、sign test、LOO correlation robustness（Table 5）、LOO DAF sensitivity（Table 7）、penalty sensitivity analysis（Table 12–13）。论文自觉标注了 K=11 cluster bootstrap 的局限性并推荐 non-clustered CI 作为 primary inference——这种统计自省在投稿论文中非常少见。

**S3. 诚实的负面结果报告。** Router 训练的 episode-level failure（47.1±2.2%, below chance）被详细呈现而非掩盖。step-level vs. episode-level evaluation 的 generalization gap 分析（Table 10）、text augmentation ablation（Table 11）、capacity scaling（Table 18）系统地排除了 data scarcity 和 model capacity 作为唯一解释。这种透明度增加了论文可信度。

**S4. Anti-cherry-picking 分析有说服力。** Table 4 显示 19 个被排除 task types 的 mean ΔDR=+38.2 pp 高于 included tasks 的 +28.7 pp。Extended validation（Appendix S, Table 21, n=20 per task）进一步确认 excluded tasks 的 DAF（0.991）高于 included tasks（0.904）。这有效排除了选择偏差的质疑。

**S5. 跨模型复现。** 三个 7–9B 模型家族（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B-it）在 ScienceWorld 上一致显示 death dominance，directional consistency 100%（10/10 death-prone tasks），internal vulnerability 近乎一致（~42% vs ~41% vs ~36%）。Table 17 的 consolidation table 是有效的 robustness evidence。

**S6. Algorithm 1 设计合理且假设明确。** Death-priority rule（lines 5–10）的有效条件——P 超过 maximum partial score——被明确标注（Assumption note, p.13）。ScienceWorld 满足此条件（P=100, max partial=100）。Labeling Quality Audit（Appendix B）验证了 zero tie-breaking labels，95 个训练 labels 全部 genuine。

**S7. Failure Mode Analysis 增加 mechanistic depth。** Appendix N 揭示 100% internal deaths 由同一 action pattern（`focus on [object]`）触发，提供了 actionable 的 mechanistic insight。Grounding ablation（Appendix O）量化了 prompt warning（-11 pp）和 action-space filtering（-19 pp）的效果。

---

## 3. Weaknesses

**W1 [Major] DAF 的 headline metric 对 penalty 的数学依赖性削弱了主要发现的 robustness。**
- 具体位置：§2.4 Eq. 5, Table 12（Appendix K）
- 问题：DAF = δP/(δP + Δ_nd) 是 P 的单调递增函数。Abstract 和 Introduction 的 headline 数字 DAF=90.4% 是在 P=100 下计算的。Table 12 显示在 P=0 时 DAF=7.4%，P=10 时 50.4%，P=25 时 70.7%。论文确实讨论了这一依赖性（§2.4 "DAF varies monotonically with P"；Appendix K "this is a mathematical consequence"），但 abstract/introduction 仍以 DAF=90.4% 为主导叙事，penalty-independent label fraction（78.9%）被置于次要位置。
- 影响：读者可能对 death avoidance 的 dominance 程度产生过度印象。DAF 的值取决于 ScienceWorld 的 specific reward structure（P=100 是环境默认值，不是理论上必然的），在其他 penalty structure 下 death avoidance 的 dominance 可能大幅降低。
- 建议：在 abstract/introduction 中将 penalty-independent label fraction（78.9%）作为 primary metric，DAF=90.4% 作为 penalty-specific supplement。明确标注 "at ScienceWorld's default P=100"。

**W2 [Major] 63% task exclusion rate 的 justification 虽合理但对 generalizability 有实质限制。**
- 具体位置：§3 第1段, Table 3–4（Appendix C）
- 问题：19/30 task types 被排除。三个排除类别（dev set 5, redundancy 7, agent floor 7）各自合理，但累积效应是分析仅基于 ScienceWorld 的 37% task coverage。"Agent capability floor" 排除的 7 个 tasks 的 task progress 为 near-zero，但这可能与 30-step budget 限制有关——论文承认 "increasing the step budget could surface non-death-dominated signal"（Limitations §1）。"Taxonomically redundant" 排除的 7 个 tasks 的判断标准不完全透明——如何定义 "family representative" 和 redundancy？
- 影响：虽然 Table 4 的 anti-cherry-picking analysis 有效排除了选择偏差（excluded tasks 更 death-dominant），但 37% coverage 限制了对 ScienceWorld 整体的 generalizability claim。
- 建议：明确 taxonomic redundancy 的判断标准（e.g., 共享 reward function structure？）。对 agent-floor tasks，报告在更长 step budget（e.g., 50, 100 steps）下是否出现 non-death routing signal。

**W3 [Major] Router negative result 可能是极端 class imbalance（9/245=3.7% internal-preferred）的 artifact，而非 routing signal 本身的 limitation。**
- 具体位置：§3.6, Table 10–11（Appendix J）
- 问题：在 245 episodes 中仅 9 个 internal-preferred（3.7%）。任何分类器在此 imbalance 下都倾向于 majority-class collapse。Text augmentation ablation（Table 11）仅做 paraphrase-based augmentation，不增加 genuine episodes。论文承认 "genuine episode-level scaling (collecting more counterfactual pairs) remains an open question"，但随即估算需要 ~1,350 paired episodes（5.5× expansion）便放弃探索。
- 影响：Router failure 被呈现为 "signal-limited" 结论（§3.6），但实际上 data-limited 的假设未被充分排除。在 3.7% minority rate 下，signal-limited vs. data-limited 是 underdetermined 的。
- 建议：(1) 明确标注 router failure 是 "under the current data regime (N=245, 3.7% minority)" 而非 "routing signal does not exist for learned routers in general"；(2) 讨论 selective collection strategy（只收集 death-free episodes）是否能提高 minority rate 以更公平地测试 router。

**W4 [Major] 跨环境 probes 的 "deterministic" computation mode 在三个环境中语义不同，限制了 cross-environment comparison 的 validity。**
- 具体位置：§3.4, Table 14（Appendix L）
- 问题：ScienceWorld deterministic = oracle simulator forking；MATH deterministic = Python code interpreter；ALFWorld deterministic = admissible-action enumeration。这三种 "deterministic" computation modes 在信息特权程度、计算成本和 failure mode 上完全不同。论文 Table 14 footnote 承认了这一点（"deterministic denotes qualitatively different computation modes"），但仍将三个环境的结果并列讨论并声称框架具有 cross-environment generality。
- 影响：MATH 的 "no routing signal" finding 不能直接与 ScienceWorld 的 "death-dominated signal" 对比，因为 code interpreter 和 oracle simulator 是不同类型的外部工具。ALFWorld 的 information asymmetry finding 是一个独立发现，但不直接验证 ScienceWorld 的 death dominance 机制。
- 建议：更谨慎地框定 cross-environment 结果：强调框架（counterfactual decomposition procedure）是通用的，而非具体 findings 可跨环境迁移。

**W5 [Minor] Cohen's d=3.02（Table 6, Appendix E）的解释需要更多 context。**
- 具体位置：Appendix E, Table 6
- 问题：d=3.02 是在 K=11 task-type clusters 上计算的。10/11 clusters 显示同方向（唯一例外是 zero-death task），directional consistency 近乎完美。此 effect size 虽然 numerically large，但更多反映 binary structure（death-prone tasks 几乎一致表现出 death asymmetry）而非 continuous effect 的 magnitude。
- 建议：加一句解释 d=3.02 reflects near-binary directional consistency rather than a graded effect magnitude。

**W6 [Minor] 单一 death mechanism（`focus on`）限制了 failure mode analysis 的 generalizability。**
- 具体位置：Appendix N
- 问题：所有 105 个 internal deaths 由同一 action pattern 触发。这是 ScienceWorld 特有的 API 设计问题（answer-submission action 被误用为 exploration action）。如果换一个 action space 设计（e.g., 将 `focus on` 从 exploration phase 移除），death rate 可能大幅降低。Grounding ablation（Appendix O）的 action-space filtering 已证实这一点（-19 pp）。
- 影响：论文的 general claim（"any environment with asymmetric fatal outcomes"）基于一个非常特定的 failure mechanism，generalizability 存疑。
- 建议：在 Discussion 中更明确区分 ScienceWorld-specific 的 `focus on` failure mode 和 general death avoidance framework 的适用范围。

**W7 [Minor] 72B scaling probe 的 scope 过窄。**
- 具体位置：§3.3, Table 1
- 问题：仅 Qwen2.5-72B 一个模型，没有 cross-model replication at scale（论文在 Limitations 中承认）。Death rate 从 42.9% 降至 30.6%，death dominance persists（DAF=92.4%），但这是单点数据，无法建立 scaling trend。N=255 episodes 是合理的，但仅一个 72B 模型的 evidence 不足以讨论 "scaling" implications。
- 建议：将 72B 结果定位为 "preliminary probe" 而非 scaling evidence；或增加 Llama-3.1-70B 作为 cross-model 验证。

---

## 4. Questions

**Q1.** Algorithm 1 的 death-priority rule 在 both-dead 情况下赋予 `no-pref` label（line 10），不区分 "both die at step 5" vs "both die at step 25"。在时间维度上是否丢失了有用的 routing signal？

**Q2.** Table 3 中 `find-non-living-thing` 的 n=40（两批收集），而其他 tasks n=20。这是否引入了 estimation precision 的不对称？为什么不对所有 tasks 收集 n=40？

**Q3.** Reflexion 实验（§3.3, Figure 3）在 N=3 后 death rate stabilizes at ~35%。为什么不测试 N>5？Is there a theoretical reason to expect no further improvement, or is this a computational budget constraint?

**Q4.** The practitioner decision framework（Appendix R, Table 20）的 thresholds（15 pp, 75%, 50%）仅有 4 个 retrospective data points 的 validation。这些 thresholds 的选择依据是什么？是否有 sensitivity analysis showing robustness to threshold perturbation？

**Q5.** DAF 定义中 Δ_nd = 2.84 是在 ScienceWorld 的 11 task types 上测量的 non-death score gap。这个值的 bootstrap CI 是多少？如果 Δ_nd 的 uncertainty 较大，DAF 的 interpretability 是否受影响？

---

## 5. Missing References

- **Safe RL literature**: 论文讨论 catastrophic failure 但未引用 safe reinforcement learning 的核心工作（e.g., Garcıa & Fernández 2015 已引用，但缺少 constrained MDP 如 Altman 1999 的引用——已包含于 references，这点收回）。
- **Routing/mixture-of-experts 在 inference-time 的工作**: 论文引用了 RouteLLM（Ong et al., 2024）和 CogRouter，但缺少 Hybrid LLM routing 的更早期工作如 **FrugalGPT (Chen et al., 2023)** 和 **AutoMix (Madaan et al., 2023)**，这些工作也涉及 cost-quality tradeoff routing。
- **Step-level routing 的 foundational work**: Options framework (Sutton et al., 1999) 或 hierarchical RL 中 temporal abstraction 的经典文献可能与 episode-level vs. step-level routing 的讨论相关。

---

## 6. 格式检查

- **正文页数**：8 页（p.1–p.8），符合 EMNLP 2026 long paper 8-page 限制。
- **Limitations**：存在，位于正文之后（p.9），覆盖 5 个方面（environmental scope, methodological constraints, statistical limitations, pure-strategy upper bound, diagnostic scope），内容充分。
- **Ethics Statement**：存在（p.10），覆盖数据来源、计算资源、代码发布计划。
- **匿名合规**：作者为 "Anonymous ACL submission"，PDF 中未发现去匿名化信息。`\hypersetup{pdfauthor={},pdftitle={}}` 已清空 PDF metadata。
- **`\usepackage[review]{acl}`**：已使用。
- **参考文献格式**：使用 `\bibliography{references}`，格式统一。
- **Responsible NLP Checklist**：未在 PDF 中出现，符合规定（在 OpenReview 表单中填写）。
- **无合规问题。**

---

## 7. 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 在 ScienceWorld 内部的分析极其充分（bootstrap CI, cluster-robust, LOO, penalty sensitivity），但 DAF 对 P 的数学依赖（W1）和 router failure 的 class imbalance confound（W3）削弱了两个核心 claim 的 robustness。跨环境 generalizability 受限于不同 "deterministic" mode 的不可比性（W4）。 |
| **Excitement** | 3.5/5 | "先诊断再构建" 的理念对 agent routing 社区有实质价值。但 findings 高度 environment-specific（单一 death mechanism），prescriptive value 有限（decision framework 仅 4 个 retrospective validation points）。框架的理论贡献（counterfactual decomposition）比具体实证 findings 更有持久价值。 |
| **Reproducibility** | 4/5 | Algorithm 1 明确，所有超参数公开（Table 16），prompt templates 完整提供（Appendix T），模型均为公开权重。但代码和数据 "upon acceptance" 发布，当前不可复现。 |
| **Confidence** | 4/5 | 我仔细阅读了全部 24 页（含 20 个 appendices），熟悉 agent routing、counterfactual inference 和 bootstrap 统计方法。对 ScienceWorld 环境的 domain-specific 细节不如 specialist 熟悉。 |

---

## 8. Overall Assessment

**Overall: 3.5 — Borderline Conference**

**一句话总结：** 一篇方法论上极其严谨的诊断性论文，提出了有价值的 counterfactual decomposition framework 并发现 death avoidance 主导 ScienceWorld routing signal，但 findings 的 generalizability 受限于单一环境的特定 death mechanism、DAF 对 penalty 的数学依赖、以及 router negative result 的 class imbalance confound。

**详细判断依据：**

*接收方向的论据*：(1) 框架新颖，填补了 "先诊断再构建 router" 的方法论空白；(2) 统计分析的深度和透明度在 agent routing 领域罕见；(3) 负面结果的诚实报告（router failure）对社区有警示价值；(4) 跨模型复现（3 families）增强了 ScienceWorld 内部发现的可信度。

*拒绝方向的论据*：(1) 核心 findings 与 ScienceWorld 的特定 death mechanism 紧密耦合，框架的 general utility 未被跨环境实证充分支持（W4）；(2) DAF=90.4% 的 headline 对 P 的数学依赖使 dominance 程度的 interpretation 不够 robust（W1）；(3) Router failure 的 "signal-limited" 结论在 3.7% minority rate 下 underdetermined（W3）；(4) 63% task exclusion 虽有合理 justification 但限制了 coverage（W2）。

总体而言，论文的方法论贡献（diagnostic framework）足以进入 Findings；如果 W1（DAF framing）和 W3（router failure interpretation）能在 camera-ready 中 addressed，Conference 接收也合理。

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

_source line 2416 · 2026-05-22T22:58:40.018548+00:00_

R1 审稿意见已收到。等待 R2 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 199

## Round 199

2 recorded events


### User

_source line 2417 · 2026-05-22T22:58:50.966144+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**总结：** Overall 3.5（Borderline Conference）。论文的 counterfactual diagnostic framework 新颖且统计分析极其详尽（20 个 appendices），跨模型复现（3 families）可信。主要问题：(1) DAF=90.4% 的 headline 对 penalty magnitude 有数学依赖，penalty-independent 的 78.9% 应作为 primary metric；(2) 63% task exclusion rate 虽有 anti-cherry-picking 证据但限制 coverage；(3) router failure 的 "signal-limited" 结论在 3.7% minority rate 下与 "data-limited" underdetermined；(4) 跨环境 "deterministic" mode 语义不同限制了 cross-environment comparison validity。框架的方法论贡献足以进入 Findings，若 W1/W3 在 camera-ready 中 addressed 则 Conference 接收合理。

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

_source line 2418 · 2026-05-22T22:59:04.519632+00:00_

R1 审稿已收到（Overall 3.5, Borderline Conference）。等待 R2 审稿完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 200

## Round 200

6 recorded events


### User

_source line 2419 · 2026-05-22T23:00:26.254088+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Round 1 (新颖性 + 完整性 + 写作质量 + Related Work 覆盖)

### 1. Summary

本文提出 episode-level counterfactual 框架诊断 LLM agent routing 信号。在 ScienceWorld 中发现 78.9% 非平局 routing 标签源于 death avoidance，提出 DAF 和 SCI 指标，覆盖 3 个 7–9B 模型家族和 MATH/ALFWorld 跨环境验证。

### 2. Strengths

**S1.** 问题定位精准：diagnostic vs. prescriptive routing 的差异化清晰，Section 5 中的 practitioner guidance（DAF≈0 → always-deterministic）有实用价值。

**S2.** 实验严谨：episode-level bootstrap (B=10,000)、3 模型家族 cross-model replication、4 intervention axes、sensitivity analysis (Appendix K)。

**S3.** 方法论有独立价值：Algorithm 1 + DAF/SCI 可复用，不依赖特定发现。

**S4.** Appendix 极详尽（16 页，A–T），可复现性高。

**S5.** 跨环境 probes 虽初步但 hedging 语言诚实（"preliminary evidence"）。

### 3. Weaknesses

**W1. [Critical] 正文超 8 页。** Sections 1–6 约 8.5 页（Discussion 延至 p.9 上半，Conclusion 结束于 p.9 中部）。EMNLP 2026 限 8 页，可能 desk reject。建议压缩 Section 4/5 或将 Figure 2 移至 appendix。

**W2. [Major] 核心发现 triviality 风险。** ScienceWorld 的 −100 death penalty 使 death-asymmetric episodes 自然携带不成比例的 score gap。DAF 随 P 单调递增是 mathematical consequence（Appendix K 自认）。论文需正面区分 "DAF 值 (penalty-dependent)" 和 "label fraction 78.9% (penalty-invariant)"，并论证后者的非平凡性。

**W3. [Major] Figure 2 近似恒等关系占正文空间。** r=0.97 的 scatter plot 是 DAF≈1 的可视化重述，作者自己说 "not an independent finding"。应移至 appendix。

**W4. [Major] Non-death component（21.1%）分析不足。** 78.9% death avoidance 之外的 routing signal 来自什么？SCI 显示集中在 top-3 task types 但无 mechanistic 解释。需 case study。

**W5. [Minor] 跨环境验证 scope 与泛化 claim 有张力。** MATH 和 ALFWorld 各仅 5-6 task types。Discussion 中 "framework's generality claim is methodological" 需更多证据或更谨慎措辞。

**W6. [Minor] 数字密度过高。** 几乎每段 3-5 个带 CI 的数字，Abstract 尤其严重。建议将 secondary statistics 移至 footnotes/appendix。

**W7. [Minor] Related Work 缺 non-agent adaptive computation。** 未覆盖 Mixture-of-Depths、speculative decoding 等共享动态计算分配思想的方向。

**W8. [Minor] Introduction 与 Conclusion contributions 列表近乎逐字重复。** 页数超限下应削减冗余。

### 4. Questions

**Q1.** DAF 值 (90.4%) vs label fraction (78.9%) 的区别和各自解读？这对 triviality 论证关键。

**Q2.** 19 个 excluded task types 是无信号还是样本不足？

**Q3.** Section 3.6 Trained Router 的 routing decision accuracy 是多少？

**Q4.** Router 使用什么特征？能否直接学到 "death-prone → deterministic" 映射？

**Q5.** "no prior work has decomposed routing decisions in interactive environments" 的 novelty claim 是否过强？

### 5. Missing References

- Mixture-of-Depths (Raposo et al., 2024)
- Speculative decoding (Leviathan et al., 2023; Chen et al., 2023)
- LATS (Zhou et al., 2024)
- Trial and Error (Wang et al., 2024)

### 6. Scoring

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 3.5/5 | 方法严谨但 DAF penalty-dependence 构成 artifact 风险 |
| Excitement | 2.5/5 | Diagnostic angle 新颖但核心发现 triviality 风险显著 |
| Reproducibility | 4/5 | 伪代码/prompts/seeds/超参数齐全 |

### 7. Overall Assessment

**3.0 — Findings**

方法论贡献有价值，实验执行扎实，但核心发现与环境奖励结构的近似循环论证关系、跨环境泛化证据薄弱、正文超页共同限制了 overall 评分。修复 (1) triviality 正面回应 (2) non-death signal 深化 (3) 页数 后可达 3.5。

### 8. Confidence: 4/5

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


### Tool call

_source line 2420 · 2026-05-22T23:00:58.140308+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每条 Weakness 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（完整原文）\n\n### Summary\n本文提出 episode-level counterfactual 框架诊断 LLM agent routing 信号。在 ScienceWorld 中发现 78.9% 非平局 routing 标签源于 death avoidance，提出 DAF 和 SCI 指标，覆盖 3 个 7–9B 模型家族和 MATH/ALFWorld 跨环境验证。\n\n### Strengths\nS1. 问题定位精准：diagnostic vs. prescriptive routing 的差异化清晰，Section 5 中的 practitioner guidance（DAF≈0 → always-deterministic）有实用价值。\nS2. 实验严谨：episode-level bootstrap (B=10,000)、3 模型家族 cross-model replication、4 intervention axes、sensitivity analysis (Appendix K)。\nS3. 方法论有独立价值：Algorithm 1 + DAF/SCI 可复用，不依赖特定发现。\nS4. Appendix 极详尽（16 页，A–T），可复现性高。\nS5. 跨环境 probes 虽初步但 hedging 语言诚实（\"preliminary evidence\"）。\n\n### Weaknesses\nW1. [Critical] 正文超 8 页。Sections 1–6 约 8.5 页（Discussion 延至 p.9 上半，Conclusion 结束于 p.9 中部）。EMNLP 2026 限 8 页，可能 desk reject。建议压缩 Section 4/5 或将 Figure 2 移至 appendix。\n\nW2. [Major] 核心发现 triviality 风险。ScienceWorld 的 −100 death penalty 使 death-asymmetric episodes 自然携带不成比例的 score gap。DAF 随 P 单调递增是 mathematical consequence（Appendix K 自认）。论文需正面区分 \"DAF 值 (penalty-dependent)\" 和 \"label fraction 78.9% (penalty-invariant)\"，并论证后者的非平凡性。\n\nW3. [Major] Figure 2 近似恒等关系占正文空间。r=0.97 的 scatter plot 是 DAF≈1 的可视化重述，作者自己说 \"not an independent finding\"。应移至 appendix。\n\nW4. [Major] Non-death component（21.1%）分析不足。78.9% death avoidance 之外的 routing signal 来自什么？SCI 显示集中在 top-3 task types 但无 mechanistic 解释。需 case study。\n\nW5. [Minor] 跨环境验证 scope 与泛化 claim 有张力。MATH 和 ALFWorld 各仅 5-6 task types。Discussion 中 \"framework's generality claim is methodological\" 需更多证据或更谨慎措辞。\n\nW6. [Minor] 数字密度过高。几乎每段 3-5 个带 CI 的数字，Abstract 尤其严重。建议将 secondary statistics 移至 footnotes/appendix。\n\nW7. [Minor] Related Work 缺 non-agent adaptive computation。未覆盖 Mixture-of-Depths、speculative decoding 等共享动态计算分配思想的方向。\n\nW8. [Minor] Introduction 与 Conclusion contributions 列表近乎逐字重复。页数超限下应削减冗余。\n\n### Questions\nQ1. DAF 值 (90.4%) vs label fraction (78.9%) 的区别和各自解读？这对 triviality 论证关键。\nQ2. 19 个 excluded task types 是无信号还是样本不足？\nQ3. Section 3.6 Trained Router 的 routing decision accuracy 是多少？\nQ4. Router 使用什么特征？能否直接学到 \"death-prone → deterministic\" 映射？\nQ5. \"no prior work has decomposed routing decisions in interactive environments\" 的 novelty claim 是否过强？\n\n### Missing References\n- Mixture-of-Depths (Raposo et al., 2024)\n- Speculative decoding (Leviathan et al., 2023; Chen et al., 2023)\n- LATS (Zhou et al., 2024)\n- Trial and Error (Wang et al., 2024)\n\n### Scoring\nSoundness: 3.5/5\nExcitement: 2.5/5\nReproducibility: 4/5\n\n### Overall: 3.0 — Findings\n### Confidence: 4/5"
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
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每条 Weakness 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（完整原文）\n\n### Summary\n本文提出 episode-level counterfactual 框架诊断 LLM agent routing 信号。在 ScienceWorld 中发现 78.9% 非平局 routing 标签源于 death avoidance，提出 DAF 和 SCI 指标，覆盖 3 个 7–9B 模型家族和 MATH/ALFWorld 跨环境验证。\n\n### Strengths\nS1. 问题定位精准：diagnostic vs. prescriptive routing 的差异化清晰，Section 5 中的 practitioner guidance（DAF≈0 → always-deterministic）有实用价值。\nS2. 实验严谨：episode-level bootstrap (B=10,000)、3 模型家族 cross-model replication、4 intervention axes、sensitivity analysis (Appendix K)。\nS3. 方法论有独立价值：Algorithm 1 + DAF/SCI 可复用，不依赖特定发现。\nS4. Appendix 极详尽（16 页，A–T），可复现性高。\nS5. 跨环境 probes 虽初步但 hedging 语言诚实（\"preliminary evidence\"）。\n\n### Weaknesses\nW1. [Critical] 正文超 8 页。Sections 1–6 约 8.5 页（Discussion 延至 p.9 上半，Conclusion 结束于 p.9 中部）。EMNLP 2026 限 8 页，可能 desk reject。建议压缩 Section 4/5 或将 Figure 2 移至 appendix。\n\nW2. [Major] 核心发现 triviality 风险。ScienceWorld 的 −100 death penalty 使 death-asymmetric episodes 自然携带不成比例的 score gap。DAF 随 P 单调递增是 mathematical consequence（Appendix K 自认）。论文需正面区分 \"DAF 值 (penalty-dependent)\" 和 \"label fraction 78.9% (penalty-invariant)\"，并论证后者的非平凡性。\n\nW3. [Major] Figure 2 近似恒等关系占正文空间。r=0.97 的 scatter plot 是 DAF≈1 的可视化重述，作者自己说 \"not an independent finding\"。应移至 appendix。\n\nW4. [Major] Non-death component（21.1%）分析不足。78.9% death avoidance 之外的 routing signal 来自什么？SCI 显示集中在 top-3 task types 但无 mechanistic 解释。需 case study。\n\nW5. [Minor] 跨环境验证 scope 与泛化 claim 有张力。MATH 和 ALFWorld 各仅 5-6 task types。Discussion 中 \"framework's generality claim is methodological\" 需更多证据或更谨慎措辞。\n\nW6. [Minor] 数字密度过高。几乎每段 3-5 个带 CI 的数字，Abstract 尤其严重。建议将 secondary statistics 移至 footnotes/appendix。\n\nW7. [Minor] Related Work 缺 non-agent adaptive computation。未覆盖 Mixture-of-Depths、speculative decoding 等共享动态计算分配思想的方向。\n\nW8. [Minor] Introduction 与 Conclusion contributions 列表近乎逐字重复。页数超限下应削减冗余。\n\n### Questions\nQ1. DAF 值 (90.4%) vs label fraction (78.9%) 的区别和各自解读？这对 triviality 论证关键。\nQ2. 19 个 excluded task types 是无信号还是样本不足？\nQ3. Section 3.6 Trained Router 的 routing decision accuracy 是多少？\nQ4. Router 使用什么特征？能否直接学到 \"death-prone → deterministic\" 映射？\nQ5. \"no prior work has decomposed routing decisions in interactive environments\" 的 novelty claim 是否过强？\n\n### Missing References\n- Mixture-of-Depths (Raposo et al., 2024)\n- Speculative decoding (Leviathan et al., 2023; Chen et al., 2023)\n- LATS (Zhou et al., 2024)\n- Trial and Error (Wang et al., 2024)\n\n### Scoring\nSoundness: 3.5/5\nExcitement: 2.5/5\nReproducibility: 4/5\n\n### Overall: 3.0 — Findings\n### Confidence: 4/5"
  }
}
```

</details>

---


### Tool result

_source line 2421 · 2026-05-22T23:01:56.730193+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 58589
}
```

</details>

---


### Tool call

_source line 2422 · 2026-05-22T23:01:57.234330+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每条 Weakness 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（完整原文）\n\n### Summary\n本文提出 episode-level counterfactual diagnostic framework，将 LLM agent routing signal 分解为 death avoidance 和 non-death 两个组成部分。在 ScienceWorld（11/30 task types, N=245 episodes）上发现 78.9% 的 non-tie routing labels 源自 death asymmetry（penalty-independent），DAF=90.4%（penalty-dependent at P=100）。训练的 router 在 episode-level 泛化上低于随机基线（47.1±2.2%）。跨模型（Llama-3.1-8B, Gemma-2-9B）和跨环境（MATH, ALFWorld）probes 提供初步支撑。核心贡献是诊断性的——在构建 learned router 之前应先检查 routing signal 是否被 catastrophic failure 所主导。\n\n### Strengths\nS1. 新颖且有价值的诊断视角。现有 routing 工作直接训练 router 而不先理解 routing signal 的构成。本文首次系统分解 routing signal，填补了一个重要的方法论空白。DAF 的数学定义（§2.4, Eq. 5）清晰，penalty-independent label fraction（78.9%）作为补充指标的选择也合理。\n\nS2. 极其详尽的统计分析。20 个 appendices（A–T）提供了罕见的深度：bootstrap CI、cluster-robust t-test、wild cluster bootstrap、exact permutation test、sign test、LOO correlation robustness（Table 5）、LOO DAF sensitivity（Table 7）、penalty sensitivity analysis（Table 12–13）。论文自觉标注了 K=11 cluster bootstrap 的局限性并推荐 non-clustered CI 作为 primary inference——这种统计自省在投稿论文中非常少见。\n\nS3. 诚实的负面结果报告。Router 训练的 episode-level failure（47.1±2.2%, below chance）被详细呈现而非掩盖。step-level vs. episode-level evaluation 的 generalization gap 分析（Table 10）、text augmentation ablation（Table 11）、capacity scaling（Table 18）系统地排除了 data scarcity 和 model capacity 作为唯一解释。这种透明度增加了论文可信度。\n\nS4. Anti-cherry-picking 分析有说服力。Table 4 显示 19 个被排除 task types 的 mean ΔDR=+38.2 pp 高于 included tasks 的 +28.7 pp。Extended validation（Appendix S, Table 21, n=20 per task）进一步确认 excluded tasks 的 DAF（0.991）高于 included tasks（0.904）。这有效排除了选择偏差的质疑。\n\nS5. 跨模型复现。三个 7–9B 模型家族（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B-it）在 ScienceWorld 上一致显示 death dominance，directional consistency 100%（10/10 death-prone tasks），internal vulnerability 近乎一致（~42% vs ~41% vs ~36%）。Table 17 的 consolidation table 是有效的 robustness evidence。\n\nS6. Algorithm 1 设计合理且假设明确。Death-priority rule（lines 5–10）的有效条件——P 超过 maximum partial score——被明确标注（Assumption note, p.13）。ScienceWorld 满足此条件（P=100, max partial=100）。Labeling Quality Audit（Appendix B）验证了 zero tie-breaking labels，95 个训练 labels 全部 genuine。\n\nS7. Failure Mode Analysis 增加 mechanistic depth。Appendix N 揭示 100% internal deaths 由同一 action pattern（focus on [object]）触发，提供了 actionable 的 mechanistic insight。Grounding ablation（Appendix O）量化了 prompt warning（-11 pp）和 action-space filtering（-19 pp）的效果。\n\n### Weaknesses\n\nW1 [Major] DAF 的 headline metric 对 penalty 的数学依赖性削弱了主要发现的 robustness。\n- 具体位置：§2.4 Eq. 5, Table 12（Appendix K）\n- 问题：DAF = δP/(δP + Δ_nd) 是 P 的单调递增函数。Abstract 和 Introduction 的 headline 数字 DAF=90.4% 是在 P=100 下计算的。Table 12 显示在 P=0 时 DAF=7.4%，P=10 时 50.4%，P=25 时 70.7%。论文确实讨论了这一依赖性（§2.4 \"DAF varies monotonically with P\"；Appendix K \"this is a mathematical consequence\"），但 abstract/introduction 仍以 DAF=90.4% 为主导叙事，penalty-independent label fraction（78.9%）被置于次要位置。\n- 影响：读者可能对 death avoidance 的 dominance 程度产生过度印象。\n- 建议：在 abstract/introduction 中将 penalty-independent label fraction（78.9%）作为 primary metric，DAF=90.4% 作为 penalty-specific supplement。\n\nW2 [Major] 63% task exclusion rate 的 justification 虽合理但对 generalizability 有实质限制。\n- 问题：19/30 task types 被排除。三个排除类别各自合理，但累积效应是分析仅基于 37% task coverage。\n- 建议：明确 taxonomic redundancy 的判断标准。对 agent-floor tasks，报告在更长 step budget 下是否出现 non-death routing signal。\n\nW3 [Major] Router negative result 可能是极端 class imbalance（9/245=3.7% internal-preferred）的 artifact，而非 routing signal 本身的 limitation。\n- 问题：在 245 episodes 中仅 9 个 internal-preferred（3.7%）。任何分类器在此 imbalance 下都倾向于 majority-class collapse。\n- 建议：明确标注 router failure 是 \"under the current data regime\" 而非 \"in general\"；讨论 selective collection strategy。\n\nW4 [Major] 跨环境 probes 的 \"deterministic\" computation mode 在三个环境中语义不同，限制了 cross-environment comparison 的 validity。\n- 问题：ScienceWorld deterministic = oracle simulator；MATH = code interpreter；ALFWorld = admissible-action enumeration。信息特权程度完全不同。\n- 建议：强调框架（procedure）是通用的，而非具体 findings 可跨环境迁移。\n\nW5 [Minor] Cohen's d=3.02 的解释需要更多 context。建议加一句解释 d=3.02 reflects near-binary directional consistency。\n\nW6 [Minor] 单一 death mechanism（focus on）限制了 failure mode analysis 的 generalizability。\n\nW7 [Minor] 72B scaling probe 的 scope 过窄。仅一个 72B 模型，无 cross-model replication at scale。\n\n### Questions\nQ1. Algorithm 1 的 death-priority rule 在 both-dead 情况下不区分死亡时间。是否丢失 signal？\nQ2. Table 3 中 find-non-living-thing 的 n=40 而其他 n=20，是否引入不对称？\nQ3. Reflexion N>5 是否有改善空间？\nQ4. Decision framework thresholds（15 pp, 75%, 50%）的选择依据？\nQ5. Δ_nd = 2.84 的 bootstrap CI 是多少？\n\n### Missing References\n- FrugalGPT (Chen et al., 2023)\n- AutoMix (Madaan et al., 2023)\n- Options framework (Sutton et al., 1999)\n\n### Scoring\nSoundness: 3.5/5\nExcitement: 3.5/5\nReproducibility: 4/5\nConfidence: 4/5\n\n### Overall: 3.5 — Borderline Conference"
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
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每条 Weakness 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（完整原文）\n\n### Summary\n本文提出 episode-level counterfactual diagnostic framework，将 LLM agent routing signal 分解为 death avoidance 和 non-death 两个组成部分。在 ScienceWorld（11/30 task types, N=245 episodes）上发现 78.9% 的 non-tie routing labels 源自 death asymmetry（penalty-independent），DAF=90.4%（penalty-dependent at P=100）。训练的 router 在 episode-level 泛化上低于随机基线（47.1±2.2%）。跨模型（Llama-3.1-8B, Gemma-2-9B）和跨环境（MATH, ALFWorld）probes 提供初步支撑。核心贡献是诊断性的——在构建 learned router 之前应先检查 routing signal 是否被 catastrophic failure 所主导。\n\n### Strengths\nS1. 新颖且有价值的诊断视角。现有 routing 工作直接训练 router 而不先理解 routing signal 的构成。本文首次系统分解 routing signal，填补了一个重要的方法论空白。DAF 的数学定义（§2.4, Eq. 5）清晰，penalty-independent label fraction（78.9%）作为补充指标的选择也合理。\n\nS2. 极其详尽的统计分析。20 个 appendices（A–T）提供了罕见的深度：bootstrap CI、cluster-robust t-test、wild cluster bootstrap、exact permutation test、sign test、LOO correlation robustness（Table 5）、LOO DAF sensitivity（Table 7）、penalty sensitivity analysis（Table 12–13）。论文自觉标注了 K=11 cluster bootstrap 的局限性并推荐 non-clustered CI 作为 primary inference——这种统计自省在投稿论文中非常少见。\n\nS3. 诚实的负面结果报告。Router 训练的 episode-level failure（47.1±2.2%, below chance）被详细呈现而非掩盖。step-level vs. episode-level evaluation 的 generalization gap 分析（Table 10）、text augmentation ablation（Table 11）、capacity scaling（Table 18）系统地排除了 data scarcity 和 model capacity 作为唯一解释。这种透明度增加了论文可信度。\n\nS4. Anti-cherry-picking 分析有说服力。Table 4 显示 19 个被排除 task types 的 mean ΔDR=+38.2 pp 高于 included tasks 的 +28.7 pp。Extended validation（Appendix S, Table 21, n=20 per task）进一步确认 excluded tasks 的 DAF（0.991）高于 included tasks（0.904）。这有效排除了选择偏差的质疑。\n\nS5. 跨模型复现。三个 7–9B 模型家族（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B-it）在 ScienceWorld 上一致显示 death dominance，directional consistency 100%（10/10 death-prone tasks），internal vulnerability 近乎一致（~42% vs ~41% vs ~36%）。Table 17 的 consolidation table 是有效的 robustness evidence。\n\nS6. Algorithm 1 设计合理且假设明确。Death-priority rule（lines 5–10）的有效条件——P 超过 maximum partial score——被明确标注（Assumption note, p.13）。ScienceWorld 满足此条件（P=100, max partial=100）。Labeling Quality Audit（Appendix B）验证了 zero tie-breaking labels，95 个训练 labels 全部 genuine。\n\nS7. Failure Mode Analysis 增加 mechanistic depth。Appendix N 揭示 100% internal deaths 由同一 action pattern（focus on [object]）触发，提供了 actionable 的 mechanistic insight。Grounding ablation（Appendix O）量化了 prompt warning（-11 pp）和 action-space filtering（-19 pp）的效果。\n\n### Weaknesses\n\nW1 [Major] DAF 的 headline metric 对 penalty 的数学依赖性削弱了主要发现的 robustness。\n- 具体位置：§2.4 Eq. 5, Table 12（Appendix K）\n- 问题：DAF = δP/(δP + Δ_nd) 是 P 的单调递增函数。Abstract 和 Introduction 的 headline 数字 DAF=90.4% 是在 P=100 下计算的。Table 12 显示在 P=0 时 DAF=7.4%，P=10 时 50.4%，P=25 时 70.7%。论文确实讨论了这一依赖性（§2.4 \"DAF varies monotonically with P\"；Appendix K \"this is a mathematical consequence\"），但 abstract/introduction 仍以 DAF=90.4% 为主导叙事，penalty-independent label fraction（78.9%）被置于次要位置。\n- 影响：读者可能对 death avoidance 的 dominance 程度产生过度印象。\n- 建议：在 abstract/introduction 中将 penalty-independent label fraction（78.9%）作为 primary metric，DAF=90.4% 作为 penalty-specific supplement。\n\nW2 [Major] 63% task exclusion rate 的 justification 虽合理但对 generalizability 有实质限制。\n- 问题：19/30 task types 被排除。三个排除类别各自合理，但累积效应是分析仅基于 37% task coverage。\n- 建议：明确 taxonomic redundancy 的判断标准。对 agent-floor tasks，报告在更长 step budget 下是否出现 non-death routing signal。\n\nW3 [Major] Router negative result 可能是极端 class imbalance（9/245=3.7% internal-preferred）的 artifact，而非 routing signal 本身的 limitation。\n- 问题：在 245 episodes 中仅 9 个 internal-preferred（3.7%）。任何分类器在此 imbalance 下都倾向于 majority-class collapse。\n- 建议：明确标注 router failure 是 \"under the current data regime\" 而非 \"in general\"；讨论 selective collection strategy。\n\nW4 [Major] 跨环境 probes 的 \"deterministic\" computation mode 在三个环境中语义不同，限制了 cross-environment comparison 的 validity。\n- 问题：ScienceWorld deterministic = oracle simulator；MATH = code interpreter；ALFWorld = admissible-action enumeration。信息特权程度完全不同。\n- 建议：强调框架（procedure）是通用的，而非具体 findings 可跨环境迁移。\n\nW5 [Minor] Cohen's d=3.02 的解释需要更多 context。建议加一句解释 d=3.02 reflects near-binary directional consistency。\n\nW6 [Minor] 单一 death mechanism（focus on）限制了 failure mode analysis 的 generalizability。\n\nW7 [Minor] 72B scaling probe 的 scope 过窄。仅一个 72B 模型，无 cross-model replication at scale。\n\n### Questions\nQ1. Algorithm 1 的 death-priority rule 在 both-dead 情况下不区分死亡时间。是否丢失 signal？\nQ2. Table 3 中 find-non-living-thing 的 n=40 而其他 n=20，是否引入不对称？\nQ3. Reflexion N>5 是否有改善空间？\nQ4. Decision framework thresholds（15 pp, 75%, 50%）的选择依据？\nQ5. Δ_nd = 2.84 的 bootstrap CI 是多少？\n\n### Missing References\n- FrugalGPT (Chen et al., 2023)\n- AutoMix (Madaan et al., 2023)\n- Options framework (Sutton et al., 1999)\n\n### Scoring\nSoundness: 3.5/5\nExcitement: 3.5/5\nReproducibility: 4/5\nConfidence: 4/5\n\n### Overall: 3.5 — Borderline Conference"
  }
}
```

</details>

---


### Tool result

_source line 2423 · 2026-05-22T23:01:58.665218+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1430
}
```

</details>

---


### Assistant

_source line 2424 · 2026-05-22T23:02:04.446350+00:00_

交叉分享已分发。等待 R1 和 R2 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 201

## Round 201

2 recorded events


### User

_source line 2425 · 2026-05-22T23:02:06.975766+00:00_

[Reviewer 2 审稿结果]:
审稿完成。核心判断：

- **Overall 3.0 (Findings)**：方法论框架（episode-level counterfactual + DAF/SCI）有独立价值，实验执行严谨，但核心发现"death avoidance dominates in death-penalized environment"存在 triviality 风险，跨环境泛化证据薄弱。
- **Critical issue**：正文约 8.5 页，超 EMNLP 2026 的 8 页限制。
- **最大可提升空间**：正面回应 triviality concern（区分 penalty-dependent DAF 值 vs. penalty-invariant label fraction）、深化 non-death signal 分析、修复页数，可望达 3.5。

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

_source line 2426 · 2026-05-22T23:02:12.427527+00:00_

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


## Round 202

## Round 202

2 recorded events


### User

_source line 2427 · 2026-05-22T23:04:02.774762+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 的逐条回应

---

### W1 [Critical] 正文超 8 页

**[AGREE] R2-W1:** 同意这是一个 desk reject 风险。从 PDF 排版看，Section 5 Discussion 占据了 page 8 的大部分篇幅，Section 6 Conclusion 延伸至 page 9 上方，之后才进入 Limitations。主文（Sections 1–6）约 8.3–8.5 页，超出 EMNLP 2026 的 8 页限制。R2 建议的 "压缩 Section 4/5 或移 Figure 2 至 appendix" 是可操作的。实际上 Section 4 Related Work 和 Section 5 Discussion 之间存在内容重叠（e.g., Discussion 中对 routing failure 的 mechanistic explanation 与 Related Work 中 safe RL 的讨论有交集），合并或压缩可行。这是 camera-ready 前必须修复的硬约束。

---

### W2 [Major] 核心发现 triviality 风险

**[AGREE] R2-W2:** 与我的 W1 一致。DAF=90.4% 是 P=100 下的数学结果，Table 12（Appendix K）明确展示了 DAF 从 P=0 的 7.4% 到 P=500 的 97.9% 的单调递增。论文自身在 Appendix K 承认 "this is a mathematical consequence of the decomposition (DAF = δP/(δP + Δ_nd)), not evidence of mechanism robustness"。

但需注意 R2 可能低估了 penalty-independent label fraction（78.9%）的非平凡性。78.9% 意味着：在完全不考虑 penalty 数值的情况下，仅看 binary death indicator（一方死亡、另一方存活），就已经解释了近 4/5 的 routing labels。这个指标不依赖 P，是纯粹的 event-level 统计。论文在 §3.1 和 §2.4 都讨论了两个指标的关系（"The label fraction, invariant to penalty magnitude, serves as the primary finding"），但 abstract/introduction 的叙事结构确实以 DAF=90.4% 为主导，需要调整优先级。

建议作者在 abstract 中将 "78.9% of non-tie routing labels arise from death asymmetry" 作为 headline finding，DAF=90.4% 作为 "at ScienceWorld's default penalty" 的补充。

---

### W3 [Major] Figure 2 近似恒等关系

**[REBUT] R2-W3:** 部分不同意将此定级为 Major。

R2 的论点是正确的：r=0.97 scatter plot 是 DAF≈1 的可视化重述，论文自己在 Figure 2 caption 中承认 "the near-perfect correlation is a structural consequence of death dominance, not an independent finding (§3.1)"。在页数超限（W1）的前提下，移至 appendix 是合理的空间优化。

但 Figure 2 有不可替代的 pedagogical 功能：它是论文 decomposition framework 的唯一可视化入口——读者通过这张图直觉理解 "per-task death rate differential 几乎完全解释 per-task score gap"。如果移除，Section 3.1 的核心论证将完全依赖 inline 数字（r=0.97, Spearman ρ=0.986），对非统计背景的读者不够直观。

建议：保留 Figure 2 但缩小尺寸（从 full-column 缩至 half-column），释放约 1/4 页空间用于解决 W1 的页数问题。这比完全移除的信息损失更小。

---

### W4 [Major] Non-death component（21.1%）分析不足

**[AGREE] R2-W4:** 同意这是论文的一个显著缺口。

78.9% death-driven labels 之外，剩余 21.1%（=20 个 score-comparison labels + 一些 death-free episodes 的 label）的 routing signal 来源未得到充分解释。具体而言：

1. **20 个 score-comparison labels**（Table 3, Appendix B）中 16 个 det-preferred、4 个 int-preferred，全部来自 both-survived episodes。论文仅报告 "score-comparison labels contribute negligible additional signal"（Appendix B），但未分析这 20 个 episode 中 deterministic 策略的 score advantage 来自什么——是 action grounding quality？exploration efficiency？task-specific domain knowledge？

2. **`find-non-living-thing`** 是唯一 zero-death task，贡献了全部 20 个 score-comparison episodes。Table 3 显示其 Δ_full=+9.58，但论文未 deep-dive 分析这个 task 中两种 strategies 的 qualitative 差异。

3. **SCI=0.2147**（Appendix A）表明 routing signal 相对分散（低 Gini coefficient），但论文称 "top-3 task types account for only 30.8% of total death-rate differential"——这说明 non-death signal 分布较均匀，但不解释 signal 的 mechanism。

一个简短的 case study（e.g., 分析 2-3 个 score-comparison episode 的 trajectory differences）即可大幅改善。

---

### W5 [Minor] 跨环境验证 scope 与泛化 claim 有张力

**[AGREE] R2-W5:** 与我的 W4 一致。三个环境的 "deterministic" computation mode 语义完全不同（§3.4, Table 14）：ScienceWorld=oracle simulator forking, MATH=code interpreter, ALFWorld=admissible-action enumeration。这限制了 cross-environment findings 的直接可比性。

但需公正指出：论文在 Limitations（§Environmental scope）中明确写道 "the framework's generality claim is methodological (the diagnostic procedure applies to any environment with asymmetric fatal outcomes), not empirical (the specific percentages may differ across environments)"。这个 hedging 是到位的。R2 要求 "更多证据或更谨慎措辞"——我认为措辞已经足够谨慎，关键缺失的是更多同质环境的验证（e.g., 另一个有 death mechanism 的环境，如 NetHack 或 Crafter）。

---

### W6 [Minor] 数字密度过高

**[REBUT] R2-W6:** 部分不同意。

对于一篇诊断性/分析性论文，precise quantification 是核心贡献的载体。如果将关键数字移至 footnotes/appendix，正文的 claim 将缺乏 inline evidence。例如 Abstract 中的 "78.9% of non-tie episode-level routing labels arise from death asymmetry" 和 "DAF reaches 90.4% (95% CI [81.1%, 99.0%])" 是不可省略的——前者是 penalty-independent headline，后者提供 uncertainty quantification。

但 R2 有一个合理的 point：某些 secondary statistics 可以压缩。例如 Abstract 中 "a finding replicated across three architecturally distinct 7–9B model families (spread 2.2 pp)" 的 "spread 2.2 pp" 可以移至正文。Section 3.1 中同时报告 bootstrap CI、Spearman ρ、LOO range 的 inline presentation 可以精简为保留 bootstrap CI，其余指向 appendix。

---

### W7 [Minor] Related Work 缺 non-agent adaptive computation

**[AGREE] R2-W7:** 同意 Mixture-of-Depths（Raposo et al., 2024）和 speculative decoding（Leviathan et al., 2023; Chen et al., 2023）是相关的 adaptive computation 工作。虽然它们在 token-level 而非 episode-level 操作，但共享 "动态分配计算资源" 的核心思想。论文的 Related Work（Section 4）覆盖了 "Tool Use and External Computation"、"Counterfactual Evaluation in RL"、"LLM Agent Environments"、"Safe RL and Causal Grounding"、"Adaptive Computation and Routing" 五个类别，最后一个类别（p.7–8）讨论了 RouteLLM、CogRouter、Mixture-of-Experts，但确实缺少 non-agent 的 adaptive depth/speculation 文献。一段简短的对比（"unlike token-level adaptive computation, our framework operates at the episode-level granularity"）即可。

LATS（Zhou et al., 2024）和 Trial and Error（Wang et al., 2024）是否遗漏需要进一步确认——论文引用了大量 agent 文献，可能以不同名称引用。

---

### W8 [Minor] Introduction 与 Conclusion contributions 列表重复

**[AGREE] R2-W8:** 同意。在页数超限（W1）的情况下，这种冗余尤其需要消除。Conclusion 的 contributions list 可以压缩为 1–2 句 forward-looking summary，将具体 contributions 仅保留在 Introduction。这可释放约 1/4 页空间。

---

### 对 R2 Questions 的补充意见

**Q1 (DAF vs label fraction):** 我在 W1 中已详细讨论。两个指标的区别是关键：label fraction 78.9% 是 penalty-invariant 的 event-level 统计，DAF 90.4% 是 penalty-dependent 的 score-weighted 指标。论文应更清晰地 primary/secondary 定位。

**Q2 (excluded tasks):** 我在 W2 中已讨论。Table 4（Appendix C）的 extended prescreening（Group B/C 各 n=5）和 Appendix S（n=20 extended validation）提供了合理 evidence，但 "agent floor" tasks 的排除可能与 step budget 有关（Limitations 承认），需进一步探索。

**Q3 (Trained Router accuracy):** 论文 §3.6 和 Appendix J 报告了详细数字：step-level 54.1±5.4%，episode-level 47.1±2.2%（below 50% chance）。End-to-end deployment（p.7）显示 router 将 97.0% episodes 分配给 deterministic，death rate 17.6%。

**Q4 (Router features):** 论文 Appendix I 说明 router 使用 step-level observation text 作为输入（SFT + LoRA on Qwen3-1.7B）。Leave-one-task-type-out evaluation（Appendix P）显示 blind routing collapses to always-deterministic，keyword-based variant achieves 62.9% only through task-identity leakage。这表明 router 无法学到 generalizable routing features，只能学到 task-type identity。

**Q5 (Novelty claim):** "no prior work has decomposed routing decisions in interactive environments" — 我认为这个 claim 基本成立但措辞可以更精确。现有 counterfactual evaluation 工作（Goyéniche et al., 2025; Gyevnár et al., 2025）在 agent 层面做 counterfactual analysis，但不针对 routing signal decomposition。建议修改为 "no prior work has systematically decomposed what drives routing preferences in interactive agent environments"。

---

### 对 R2 整体评分的评论

R2 给出 Overall 3.0（Findings），主要 concerns 是 triviality risk（W2）和 page limit（W1）。我的评估略高（3.5, Borderline Conference），原因是：
1. R2 的 Excitement 2.5 偏低——framework 的方法论价值超越了 ScienceWorld-specific findings，"先诊断再构建 router" 的理念对整个 agent routing 社区有指导意义。
2. W1（page limit）是 formatting issue，不影响学术贡献评估。
3. W2（triviality）被 78.9% penalty-independent label fraction 部分化解——这个数字不是 P 的函数。

但我同意 R2 的 W4（non-death component 分析不足）是一个 substantive gap，降低了论文的 completeness。

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

_source line 2428 · 2026-05-22T23:04:08.728571+00:00_

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


## Round 203

## Round 203

8 recorded events


### User

_source line 2429 · 2026-05-22T23:04:11.264898+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 逐条回应

### Weaknesses 回应

**[AGREE] R1-W1 (DAF penalty dependence):** 完全同意，与我的 W2 一致。Table 12 展示 DAF 从 P=0 时 7.4% 到 P=200 时 97.0% 单调递增，是数学必然。应将 penalty-independent label fraction (78.9%) 提升为 primary metric。

**[AGREE with nuance] R1-W2 (63% task exclusion):** 同意 scope 限制真实（37% coverage），但部分辩护：Table 4 和 Appendix S Table 21 的 anti-cherry-picking analysis 显示 excluded tasks 的 DAF (0.991) 高于 included (0.904)，排除是 conservative 的。支持 R1 要求明确 taxonomic redundancy 标准和长 step budget 测试。

**[REBUT] R1-W3 (Router failure = class imbalance artifact):** 倒果为因。9/245 的 extreme imbalance 是 death avoidance dominance 的直接表现（78.9% non-tie labels → deterministic-preferred），非 data collection bias。论文已通过 text augmentation (Table 11)、capacity scaling (Table 18) 排除 data scarcity/model capacity 为 sole explanation。Table 10 的 step-level vs episode-level gap (54.1% vs 17.1%) 揭示更根本的 generalization 问题。但同意应限定结论为 "under current data regime"。

**[AGREE] R1-W4 (跨环境 deterministic mode 语义不一致):** 强烈同意，与我的 W5 互补。三个环境的信息特权程度完全不同（oracle vs code interpreter vs admissible-action），不能 apple-to-apple 比较。

**[AGREE] R1-W5 (Cohen's d context):** d=3.02 反映 near-binary directional consistency，加一句 context 是 minimal effort 改进。

**[AGREE] R1-W6 (单一 death mechanism):** 100% deaths 由 focus on 触发，限制了 failure mode 的外部效度。

**[AGREE] R1-W7 (72B probe 窄):** 缺少 at-scale cross-model replication，应明确标注 limitation。

### R1 Missing References 意见
- FrugalGPT、AutoMix：同意重要遗漏，均为 LLM routing/cascading 系统。
- Options framework (Sutton 1999)：同意，episode-level temporal abstraction 的经典参考。

### 与我自身审稿的对比
**高度一致：** DAF penalty-dependence (R1-W1≈我W2)、跨环境 mode 不一致 (R1-W4≈我W5)。

**R1 未提及但我认为重要：** (1) 正文超 8 页 [Critical]；(2) Figure 2 近似恒等关系占正文空间；(3) Non-death component 21.1% 分析不足；(4) 数字密度过高。

**分歧：** R1 Overall 3.5 vs 我 3.0，核心差异在 Excitement (R1: 3.5 vs 我: 2.5)。R1 对 diagnostic framing novelty 评价更高，我对 triviality risk 权重更大。属于 reasonable disagreement。

**R1-W3 是唯一 REBUT：** Class imbalance 是 finding 的直接体现而非 artifact，但同意限定结论 scope。

---

[Reviewer 1 审稿结果]:
已完成对 Reviewer 2 全部 8 条 Weaknesses 的逐条回应，并对 5 个 Questions 提供了补充意见。汇总：

- **[AGREE]**: W1（页数超限）、W2（triviality risk，与我的 W1 一致）、W4（non-death 21.1% 分析不足）、W5（跨环境 scope）、W7（缺 non-agent adaptive computation 引用）、W8（intro/conclusion 重复）
- **[REBUT]**: W3（Figure 2 有 pedagogical 价值，建议缩小而非移除）、W6（数字密度是分析论文的必要特征，但 secondary stats 可精简）

对 R2 的 Overall 3.0 评分，我认为略低——78.9% penalty-independent finding 部分化解了 triviality concern，框架的方法论价值超越了环境特异性 findings。

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


### Tool call

_source line 2430 · 2026-05-22T23:04:32.840145+00:00_

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

_source line 2431 · 2026-05-22T23:04:32.942381+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T22:52:46.894822+00:00\", \"completed_at\": \"2026-05-22T22:57:14.128798+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 9\", \"message\": \"主文（Sections 1-6）超出 EMNLP 2026 的 8 页限制。Section 6 Conclusion 从第 9 页顶部开始，占左栏约 1/3。即使 Limitations 和 Ethics Statement 不计入页数，主文仍达约 8.2 页。需要压缩约 15-20 行才能回到 8 页以内。此问题可导致 desk reject。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 7-8\", \"message\": \"连续两页纯文本无 display item。Page 7（Section 3.6 Router Training + Section 4 Related Work 开头）和 Page 8（Section 5 Discussion 全文）均无 figure/table/equation 穿插，审稿人在此段会感到视觉疲劳。建议在 Discussion 中加一个小型 summary table 或将 Related Work 中的方法对比用表格呈现。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-9\", \"message\": \"主文 display items 偏少。9 页主文仅 3 figure + 2 table = 5 个 display items，对于实证为主的论文偏低（通常 5-8 个）。大量分析结果（如 per-task breakdown、cross-model replication）被推到 appendix，审稿人在主文中看不到。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（纯 Abstract + Introduction 文字），第一个 display item（Figure 1 pipeline 图）出现在第 2 页顶部。对 ACL 双栏格式来说这是标准布局，但 Figure 1 出现时机仍算及时，能帮助审稿人在前 2 页建立认知。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 pipeline 图有效传达核心方法论——从 Task Instance 到 Episode-Level Labeling 到 Death Decomposition Analysis 的流程清晰，颜色区分度好（绿/蓝/青），caption 自包含。作为第一个视觉锚点表现良好。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2 散点图（consistency check）尺寸偏小，但文字仍可读。轴标签字号约为正文的 65-70%，勉强达标。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3 折线图的 y 轴标签和 legend 字号偏小（约正文 60-65%），建议适当放大以提升可读性。\"}, {\"severity\": \"info\", \"dimension\": \"pages 5-6\", \"message\": \"Table 1 和 Table 2 未见对最优结果的明确加粗标注。建议对 best results 加粗，对 second-best 加下划线，并在 caption 中标注 ↑/↓ 方向。\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"附录页面表格密度极高（Tables 5-8 堆叠），字号较小但仍可读。附录可接受。\"}, {\"severity\": \"info\", \"dimen
…[truncated 479 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 2432 · 2026-05-22T23:08:01.305512+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "# Round 29 Review Issues (fresh review, 2026-05-22)\n# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作)\n\n# =============================================\n# Carried-over resolved issues (from prior rounds)\n# =============================================\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Wild cluster CI 修正且降级为 sensitivity analysis；non-clustered bootstrap 为主推断\"\n  resolution_round: 24\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Abstract concept-first 重组，数字从 10+ 精简至 3-4 个\"\n  resolution_round: 24\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Ng 1999, Northcutt 2021, DivideMix 已添加并在正确位置引用\"\n  resolution_round: 24\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 24\n  resolution: \"§5 Non-triviality 段有效回应 novelty 质疑\"\n  resolution_round: 24\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组（Self-supervised, Token-level, Task-level, RL-based）\"\n  resolution_round: 19\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"Limitations 新增 pure-strategy upper bound 段落\"\n  resolution_round: 24\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"术语全局修正为 text augmentation\"\n  resolution_round: 24\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导：P=0 时 72% labels 退化为 ties\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"P-invariance 适用范围明确量化\"\n  resolution_round: 24\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"4B router 结论 qualified；完整统计处理\"\n  resolution_round: 24\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors + train/val split 不清晰\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Router claim 从绝对否定改为有条件否定\"\n  resolution_round: 24\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"措辞软化 + effect size detection threshold 完整报告\"\n  resolution_round: 24\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制——§6 Conclusion 起始于 page 9，有 desk reject 风险\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"正文收入 8 页\"\n  resolution_round: 24\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 'fundamental non-learnability' 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R18-N1 解决\"\n  resolution_round: 24\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim — r=0.97 correlation ≠ causal/structural\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"'structurally determined' → 'empirically dominated'\"\n  resolution_round: 24\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 导致 13/28 tasks 不显著，主文未标注为 exploratory\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Per-task 结果标注为 exploratory，power caveat 完整\"\n  resolution_round: 24\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entries + Webb 年份待核实\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"huang2022inner, selfcheckgpt-2023, wang2023voyager 已清理；Webb 2023 (CJE vol.56 no.3) 年份正确\"\n  resolution_round: 24\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman 1999, Mihatsch 2002, Natarajan 2013\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"所有缺失引用已补充\"\n  resolution_round: 24\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引（17 个 appendices A-R）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Appendix Overview with hyperlinks 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M4\"\n  summary: \"§3.1 '54 sole-identified labels' 首次出现未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"术语已修正并定义\"\n  resolution_round: 24\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 inter-annotator agreement 声明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Single annotator caveat 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern — implication 未讨论\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"§5 已讨论 focus on [object] 单一模式\"\n  resolution_round: 24\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R17-M1 解决\"\n  resolution_round: 24\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"§5.4 cross-env 段加交叉引用指向 §2.1 operationalization\"\n  resolution_round: 24\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"Appendix B 加 circularity caveat; Limitations 量化 0.3% 方向冲突 + 60.3% pre-event neutral\"\n  resolution_round: 24\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 引用和讨论深度不足\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"引用已补全；额外解释句因 8 页限制无法加入，现有措辞部分覆盖\"\n  resolution_round: 24\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Algorithm 1 术语修正为 computation modes\"\n  resolution_round: 24\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"§3.1 binary structure 讨论充分\"\n  resolution_round: 24\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"72B decomposition 完整报告\"\n  resolution_round: 24\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"被 R20-N2 取代并解决\"\n  resolution_round: 24\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"Appendix L 已引用\"\n  resolution_round: 24\n\n- id: \"R19-W1\"\n  summary: \"缺少 penalty magnitude 的实际实验验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"P-invariance by design 论证逻辑覆盖\"\n  resolution_round: 24\n\n- id: \"R19-N1\"\n  summary: \"Framing 内在张力：framework vs finding 定位不清\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 27\n  resolution: \"N2+N4 修复间接解决——Abstract/Conclusion 统一为 empirical analysis + reusable diagnostic methodology。\"\n  resolution_round: 27\n\n- id: \"R26-N3\"\n  summary: \"'Contradicting the routing literature's implicit assumption' 是 strawman framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 26\n  last_seen_round: 27\n  resolution: \"R27 验收确认修复完好。\"\n  resolution_round: 27\n\n# =============================================\n# R27-R29 active issues\n# =============================================\n\n- id: \"R27-N2\"\n  summary: \"DAF=90.4% 部分是 P=100 penalty 的数学必然，Abstract/Title framing 过度突出\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 29\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：Abstract 78.9% 为 headline，DAF 降为 derived measure\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"部分有效——78.9% 确实是 headline，但 DAF=90.4% 仍以核心数字出现\"\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] §2.4 已添加 P-sensitivity 数值（P=10→50.4%, P=50→82.6%），但 Abstract 仍以 DAF=90.4% 作为主导叙事。78.9% penalty-independent label fraction 应为 headline，DAF 应标注 'at ScienceWorld default P=100'。R1 建议 Abstract 重排优先级。\"\n  action_items:\n    - round: 29\n      action: \"Abstract/Introduction 将 78.9% label fraction 作为 primary headline metric，DAF=90.4% 降为 'at P=100' 补充\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-N3\"\n  summary: \"Deterministic strategy 实为 oracle access，跨环境含义不统一，oracle confound 未分离\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 29\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：§2.1 inline 三环境 operationalization\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"Conclusion 仍写 'the diagnostic procedure transfers'，未区分 procedure vs operationalization\"\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Conclusion 修正为 'the diagnostic procedure—though not the specific operationalization of deterministic—transfers' 是进步，但三环境信息特权程度差异巨大（oracle > code interpreter > admissible actions），cross-environment findings 的直接可比性仍有限。\"\n  action_items:\n    - round: 29\n      action: \"§3.4 开头增加明确 caveat：三环境的 deterministic mode 信息特权程度不同，cross-environment results 验证 diagnostic procedure 的可复用性，不是 findings 的可迁移性\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-N4\"\n  summary: \"环境覆盖过窄，generalization claims 超出证据——1 个主环境 + 2 个 boundary probes\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 29\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：Abstract/Conclusion 'preliminary evidence' + 区分 methodological vs empirical generality\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"R27 修复基本有效\"\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Hedging 语言到位，但缺乏同质环境验证（另一个有 death mechanism 的环境如 NetHack/Crafter）。Limitations 已承认。\"\n\n- id: \"R27-W1\"\n  summary: \"Router negative result framing: signal-limited vs data-limited 未区分\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 29\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"signal-limited vs data-limited 区分尚不 conclusive\"\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R1 认为 class imbalance (9/245=3.7%) 是 confound，router failure 可能是 data-limited artifact。R2 REBUT：imbalance 是 death dominance 的直接表现非 collection bias，但同意限定结论 scope。共识：结论应标注 'under current data regime (N=245, 3.7% minority)'。\"\n  action_items:\n    - round: 29\n      action: \"§3.6 结论限定为 'under current data regime'；讨论 selective collection strategy 是否能提高 minority rate\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W2\"\n  summary: \"Actionability 有限——诊断出问题但'然后怎么办'回答不足\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 29\n  mentions:\n    - round: 28\n      reviewers: [2]\n      note: \"缺少与 concurrent routing methods 的定性讨论\"\n    - round: 29\n      reviewers: []\n      note: \"本轮未单独提及，但 R2 Q5 间接涉及。§5 ¶3 actionability 段已存在。\"\n\n- id: \"R27-W4\"\n  summary: \"Excluded tasks (63%) n=5 prescreening 样本量极小\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 29\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"主文仅一句话，63% 排除率需更充分 justify\"\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Anti-cherry-picking analysis (Table 4, Appendix S) 有效排除选择偏差（excluded ΔDR=+38.2 > included +28.7 pp），但 taxonomic redundancy 操作定义不透明，agent-floor tasks 与 step budget 限制的关系未探索。\"\n  action_items:\n    - round: 29\n      action: \"§3 明确 taxonomic redundancy 判断标准；讨论 agent-floor tasks 在更长 step budget 下是否出现 non-death signal\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W5\"\n  summary: \"K=11 cluster bootstrap: primary CI [81.1%, 99.0%] 可能 anti-conservative\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 29\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"Limitations 正文已引用 Cameron et al. K≥20-50 建议\"\n    - round: 29\n      reviewers: [1]\n      note: \"R1 认为处理得当（non-clustered 为主推断），Cohen's d=3.02 需加 context 说明反映 near-binary consistency\"\n\n- id: \"R28-N1\"\n  summary: \"Episode-level labeling 与 step-level routing 的粒度失配——title/abstract scope 超出方法论覆盖范围\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"Abstract 已添加 'episode-level' 限定词\"\n    - round: 29\n      reviewers: []\n      note: \"本轮未单独提及，prior fix 似乎有效\"\n\n- id: \"R28-W1\"\n  summary: \"72B scaling 仅做 probe 而非完整 replication——缺 router training 和 SCI 分析\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 72B 仅一个模型，无 cross-model replication at scale。应标注为 'preliminary probe'。\"\n  action_items:\n    - round: 29\n      action: \"将 72B 结果定位为 'preliminary probe'；Limitations 明确缺少 at-scale cross-model replication\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R28-W2\"\n  summary: \"'Death' 术语限制 generality perception——binary failure vs graded failure 适用性未讨论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"Limitations 已添加 graded failure / binary death assumption 讨论\"\n    - round: 29\n      reviewers: []\n      note: \"本轮未单独提及，prior fix 似乎有效\"\n\n- id: \"R28-M1\"\n  summary: \"Missing references: Alshiekh et al. (2018), Geifman & El-Yaniv (2017), CALM, MoD\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"Alshiekh 2018 已添加。R1 建议增加 FrugalGPT (Chen 2023)、AutoMix (Madaan 2023)、Options framework (Sutton 1999)。R2 建议 Mixture-of-Depths (Raposo 2024)。8 页限制下 Related Work 扩展空间有限。\"\n  action_items:\n    - round: 29\n      action: \"评估在 Related Work 中加入 FrugalGPT、AutoMix 引用的空间可行性\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R28-M2\"\n  summary: \"Pages 7-8 连续两页纯文本无 display item\"\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: []\n      note: \"视觉审查再次确认。8 页限制下无法在 pp.7-8 插入 display item。\"\n  resolution: \"8 页限制下无法在 pp.7-8 插入 display item，内容密度已最大化\"\n  resolution_round: 28\n\n- id: \"R28-M3\"\n  summary: \"§1 Introduction 'signal diversity can collapse' 重复出现\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: [2]\n      note: \"R2-W8：Introduction 与 Conclusion contributions 列表近乎逐字重复，页数超限下应削减冗余\"\n\n- id: \"R28-M4\"\n  summary: \"Figure 2 仅 11 点无 task name label，r=0.97 caveat 不够明确\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"R2 建议移至 appendix（Major）；R1 REBUT 认为有 pedagogical 价值，建议缩小（half-column）而非移除。\"\n  resolution: \"Figure 2 已缩至 0.38\\\\textwidth。R1 认为保留合理；如需解决页数可再缩或移至 appendix。\"\n  resolution_round: 28\n\n- id: \"R28-M5\"\n  summary: \"Related Work 缺 non-agent adaptive computation（early exit, speculative decoding, MoD）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 应至少加一句 positioning：'unlike token-level adaptive computation, our framework operates at episode-level granularity'\"\n\n# --- Structural / Long-standing ---\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit——方向可预期\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 29\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 Excitement 3/5\"\n    - round: 29\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3.5/5, R2 Excitement 2.5/5。核心发现（death dominance in death-penalized env）具有可预测性。R2 认为 triviality risk 显著；R1 认为 framework 的方法论价值部分化解。结构性限制持续存在。\"\n\n# =============================================\n# R29 new issues\n# =============================================\n\n- id: \"R29-N1\"\n  summary: \"正文超出 8 页限制（R20-N1/R27-N1 复发）——Conclusion 溢出至 page 9\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Sections 1-6 约 8.2-8.5 页，Conclusion 起始于 page 9。视觉审查确认。EMNLP 2026 限 8 页正文，desk reject 风险。R1 建议合并/压缩 §4-5（内容有交集），R2 建议移 Figure 2 至 appendix。R2-W8 指出 Introduction/Conclusion contributions 重复可释放空间。\"\n  action_items:\n    - round: 29\n      action: \"将正文压缩至 8 页内：(1) 压缩 Conclusion 为 2-3 句，删除重复 contributions 列表；(2) 缩小或移动 Figure 2；(3) 合并 §4/§5 中重叠内容\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R29-W1\"\n  summary: \"Non-death component (21.1%) 的 routing signal 来源未分析\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 20 个 score-comparison labels 全部来自 both-survived episodes，16 det-preferred / 4 int-preferred。find-non-living-thing 是唯一 zero-death task（n=40, Δ_full=+9.58），贡献全部 score-comparison episodes，但未 deep-dive 分析 trajectory differences。一个简短 case study（2-3 个 episode）即可大幅改善。\"\n  action_items:\n    - round: 29\n      action: \"Appendix 增加 non-death score-comparison episodes 的 case study（分析 find-non-living-thing 中两种策略的 qualitative 差异）\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R29-W2\"\n  summary: \"单一 death mechanism (focus on [object]) 限制 failure mode generalizability\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Appendix N 显示 100% internal deaths 由同一 action pattern 触发。这是 ScienceWorld API 特异性，action-space filtering (-19 pp, Appendix O) 已证实。但 general claim ('any environment with asymmetric fatal outcomes') 基于非常特定的 failure mechanism。\"\n  action_items:\n    - round: 29\n      action: \"Discussion 增加一句区分 ScienceWorld-specific failure mode 和 general death avoidance framework 适用范围\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R29-M1\"\n  summary: \"Missing references: FrugalGPT, AutoMix, Options framework, Mixture-of-Depths\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"R1: FrugalGPT (Chen 2023), AutoMix (Madaan 2023), Options framework (Sutton 1999)。R2: Mixture-of-Depths (Raposo 2024), speculative decoding (Leviathan 2023, Chen 2023)。LATS (Zhou 2024) 可能已以不同名称引用。\""
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
    "issues_yaml": "# Round 29 Review Issues (fresh review, 2026-05-22)\n# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作)\n\n# =============================================\n# Carried-over resolved issues (from prior rounds)\n# =============================================\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Wild cluster CI 修正且降级为 sensitivity analysis；non-clustered bootstrap 为主推断\"\n  resolution_round: 24\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Abstract concept-first 重组，数字从 10+ 精简至 3-4 个\"\n  resolution_round: 24\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Ng 1999, Northcutt 2021, DivideMix 已添加并在正确位置引用\"\n  resolution_round: 24\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 24\n  resolution: \"§5 Non-triviality 段有效回应 novelty 质疑\"\n  resolution_round: 24\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组（Self-supervised, Token-level, Task-level, RL-based）\"\n  resolution_round: 19\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"Limitations 新增 pure-strategy upper bound 段落\"\n  resolution_round: 24\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"术语全局修正为 text augmentation\"\n  resolution_round: 24\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导：P=0 时 72% labels 退化为 ties\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"P-invariance 适用范围明确量化\"\n  resolution_round: 24\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"4B router 结论 qualified；完整统计处理\"\n  resolution_round: 24\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors + train/val split 不清晰\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Router claim 从绝对否定改为有条件否定\"\n  resolution_round: 24\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"措辞软化 + effect size detection threshold 完整报告\"\n  resolution_round: 24\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制——§6 Conclusion 起始于 page 9，有 desk reject 风险\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"正文收入 8 页\"\n  resolution_round: 24\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 'fundamental non-learnability' 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R18-N1 解决\"\n  resolution_round: 24\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim — r=0.97 correlation ≠ causal/structural\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"'structurally determined' → 'empirically dominated'\"\n  resolution_round: 24\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 导致 13/28 tasks 不显著，主文未标注为 exploratory\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Per-task 结果标注为 exploratory，power caveat 完整\"\n  resolution_round: 24\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entries + Webb 年份待核实\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"huang2022inner, selfcheckgpt-2023, wang2023voyager 已清理；Webb 2023 (CJE vol.56 no.3) 年份正确\"\n  resolution_round: 24\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman 1999, Mihatsch 2002, Natarajan 2013\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"所有缺失引用已补充\"\n  resolution_round: 24\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引（17 个 appendices A-R）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Appendix Overview with hyperlinks 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M4\"\n  summary: \"§3.1 '54 sole-identified labels' 首次出现未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"术语已修正并定义\"\n  resolution_round: 24\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 inter-annotator agreement 声明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Single annotator caveat 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern — implication 未讨论\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"§5 已讨论 focus on [object] 单一模式\"\n  resolution_round: 24\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R17-M1 解决\"\n  resolution_round: 24\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"§5.4 cross-env 段加交叉引用指向 §2.1 operationalization\"\n  resolution_round: 24\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"Appendix B 加 circularity caveat; Limitations 量化 0.3% 方向冲突 + 60.3% pre-event neutral\"\n  resolution_round: 24\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 引用和讨论深度不足\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"引用已补全；额外解释句因 8 页限制无法加入，现有措辞部分覆盖\"\n  resolution_round: 24\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Algorithm 1 术语修正为 computation modes\"\n  resolution_round: 24\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"§3.1 binary structure 讨论充分\"\n  resolution_round: 24\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"72B decomposition 完整报告\"\n  resolution_round: 24\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"被 R20-N2 取代并解决\"\n  resolution_round: 24\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"Appendix L 已引用\"\n  resolution_round: 24\n\n- id: \"R19-W1\"\n  summary: \"缺少 penalty magnitude 的实际实验验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"P-invariance by design 论证逻辑覆盖\"\n  resolution_round: 24\n\n- id: \"R19-N1\"\n  summary: \"Framing 内在张力：framework vs finding 定位不清\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 27\n  resolution: \"N2+N4 修复间接解决——Abstract/Conclusion 统一为 empirical analysis + reusable diagnostic methodology。\"\n  resolution_round: 27\n\n- id: \"R26-N3\"\n  summary: \"'Contradicting the routing literature's implicit assumption' 是 strawman framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 26\n  last_seen_round: 27\n  resolution: \"R27 验收确认修复完好。\"\n  resolution_round: 27\n\n# =============================================\n# R27-R29 active issues\n# =============================================\n\n- id: \"R27-N2\"\n  summary: \"DAF=90.4% 部分是 P=100 penalty 的数学必然，Abstract/Title framing 过度突出\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 29\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：Abstract 78.9% 为 headline，DAF 降为 derived measure\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"部分有效——78.9% 确实是 headline，但 DAF=90.4% 仍以核心数字出现\"\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] §2.4 已添加 P-sensitivity 数值（P=10→50.4%, P=50→82.6%），但 Abstract 仍以 DAF=90.4% 作为主导叙事。78.9% penalty-independent label fraction 应为 headline，DAF 应标注 'at ScienceWorld default P=100'。R1 建议 Abstract 重排优先级。\"\n  action_items:\n    - round: 29\n      action: \"Abstract/Introduction 将 78.9% label fraction 作为 primary headline metric，DAF=90.4% 降为 'at P=100' 补充\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-N3\"\n  summary: \"Deterministic strategy 实为 oracle access，跨环境含义不统一，oracle confound 未分离\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 29\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：§2.1 inline 三环境 operationalization\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"Conclusion 仍写 'the diagnostic procedure transfers'，未区分 procedure vs operationalization\"\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Conclusion 修正为 'the diagnostic procedure—though not the specific operationalization of deterministic—transfers' 是进步，但三环境信息特权程度差异巨大（oracle > code interpreter > admissible actions），cross-environment findings 的直接可比性仍有限。\"\n  action_items:\n    - round: 29\n      action: \"§3.4 开头增加明确 caveat：三环境的 deterministic mode 信息特权程度不同，cross-environment results 验证 diagnostic procedure 的可复用性，不是 findings 的可迁移性\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-N4\"\n  summary: \"环境覆盖过窄，generalization claims 超出证据——1 个主环境 + 2 个 boundary probes\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 29\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：Abstract/Conclusion 'preliminary evidence' + 区分 methodological vs empirical generality\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"R27 修复基本有效\"\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Hedging 语言到位，但缺乏同质环境验证（另一个有 death mechanism 的环境如 NetHack/Crafter）。Limitations 已承认。\"\n\n- id: \"R27-W1\"\n  summary: \"Router negative result framing: signal-limited vs data-limited 未区分\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 29\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"signal-limited vs data-limited 区分尚不 conclusive\"\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R1 认为 class imbalance (9/245=3.7%) 是 confound，router failure 可能是 data-limited artifact。R2 REBUT：imbalance 是 death dominance 的直接表现非 collection bias，但同意限定结论 scope。共识：结论应标注 'under current data regime (N=245, 3.7% minority)'。\"\n  action_items:\n    - round: 29\n      action: \"§3.6 结论限定为 'under current data regime'；讨论 selective collection strategy 是否能提高 minority rate\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W2\"\n  summary: \"Actionability 有限——诊断出问题但'然后怎么办'回答不足\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 29\n  mentions:\n    - round: 28\n      reviewers: [2]\n      note: \"缺少与 concurrent routing methods 的定性讨论\"\n    - round: 29\n      reviewers: []\n      note: \"本轮未单独提及，但 R2 Q5 间接涉及。§5 ¶3 actionability 段已存在。\"\n\n- id: \"R27-W4\"\n  summary: \"Excluded tasks (63%) n=5 prescreening 样本量极小\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 29\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"主文仅一句话，63% 排除率需更充分 justify\"\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Anti-cherry-picking analysis (Table 4, Appendix S) 有效排除选择偏差（excluded ΔDR=+38.2 > included +28.7 pp），但 taxonomic redundancy 操作定义不透明，agent-floor tasks 与 step budget 限制的关系未探索。\"\n  action_items:\n    - round: 29\n      action: \"§3 明确 taxonomic redundancy 判断标准；讨论 agent-floor tasks 在更长 step budget 下是否出现 non-death signal\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W5\"\n  summary: \"K=11 cluster bootstrap: primary CI [81.1%, 99.0%] 可能 anti-conservative\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 29\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"Limitations 正文已引用 Cameron et al. K≥20-50 建议\"\n    - round: 29\n      reviewers: [1]\n      note: \"R1 认为处理得当（non-clustered 为主推断），Cohen's d=3.02 需加 context 说明反映 near-binary consistency\"\n\n- id: \"R28-N1\"\n  summary: \"Episode-level labeling 与 step-level routing 的粒度失配——title/abstract scope 超出方法论覆盖范围\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"Abstract 已添加 'episode-level' 限定词\"\n    - round: 29\n      reviewers: []\n      note: \"本轮未单独提及，prior fix 似乎有效\"\n\n- id: \"R28-W1\"\n  summary: \"72B scaling 仅做 probe 而非完整 replication——缺 router training 和 SCI 分析\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 72B 仅一个模型，无 cross-model replication at scale。应标注为 'preliminary probe'。\"\n  action_items:\n    - round: 29\n      action: \"将 72B 结果定位为 'preliminary probe'；Limitations 明确缺少 at-scale cross-model replication\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R28-W2\"\n  summary: \"'Death' 术语限制 generality perception——binary failure vs graded failure 适用性未讨论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"Limitations 已添加 graded failure / binary death assumption 讨论\"\n    - round: 29\n      reviewers: []\n      note: \"本轮未单独提及，prior fix 似乎有效\"\n\n- id: \"R28-M1\"\n  summary: \"Missing references: Alshiekh et al. (2018), Geifman & El-Yaniv (2017), CALM, MoD\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"Alshiekh 2018 已添加。R1 建议增加 FrugalGPT (Chen 2023)、AutoMix (Madaan 2023)、Options framework (Sutton 1999)。R2 建议 Mixture-of-Depths (Raposo 2024)。8 页限制下 Related Work 扩展空间有限。\"\n  action_items:\n    - round: 29\n      action: \"评估在 Related Work 中加入 FrugalGPT、AutoMix 引用的空间可行性\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R28-M2\"\n  summary: \"Pages 7-8 连续两页纯文本无 display item\"\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: []\n      note: \"视觉审查再次确认。8 页限制下无法在 pp.7-8 插入 display item。\"\n  resolution: \"8 页限制下无法在 pp.7-8 插入 display item，内容密度已最大化\"\n  resolution_round: 28\n\n- id: \"R28-M3\"\n  summary: \"§1 Introduction 'signal diversity can collapse' 重复出现\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: [2]\n      note: \"R2-W8：Introduction 与 Conclusion contributions 列表近乎逐字重复，页数超限下应削减冗余\"\n\n- id: \"R28-M4\"\n  summary: \"Figure 2 仅 11 点无 task name label，r=0.97 caveat 不够明确\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"R2 建议移至 appendix（Major）；R1 REBUT 认为有 pedagogical 价值，建议缩小（half-column）而非移除。\"\n  resolution: \"Figure 2 已缩至 0.38\\\\textwidth。R1 认为保留合理；如需解决页数可再缩或移至 appendix。\"\n  resolution_round: 28\n\n- id: \"R28-M5\"\n  summary: \"Related Work 缺 non-agent adaptive computation（early exit, speculative decoding, MoD）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 应至少加一句 positioning：'unlike token-level adaptive computation, our framework operates at episode-level granularity'\"\n\n# --- Structural / Long-standing ---\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit——方向可预期\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 29\n  mentions:\n    - round: 28\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 Excitement 3/5\"\n    - round: 29\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3.5/5, R2 Excitement 2.5/5。核心发现（death dominance in death-penalized env）具有可预测性。R2 认为 triviality risk 显著；R1 认为 framework 的方法论价值部分化解。结构性限制持续存在。\"\n\n# =============================================\n# R29 new issues\n# =============================================\n\n- id: \"R29-N1\"\n  summary: \"正文超出 8 页限制（R20-N1/R27-N1 复发）——Conclusion 溢出至 page 9\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Sections 1-6 约 8.2-8.5 页，Conclusion 起始于 page 9。视觉审查确认。EMNLP 2026 限 8 页正文，desk reject 风险。R1 建议合并/压缩 §4-5（内容有交集），R2 建议移 Figure 2 至 appendix。R2-W8 指出 Introduction/Conclusion contributions 重复可释放空间。\"\n  action_items:\n    - round: 29\n      action: \"将正文压缩至 8 页内：(1) 压缩 Conclusion 为 2-3 句，删除重复 contributions 列表；(2) 缩小或移动 Figure 2；(3) 合并 §4/§5 中重叠内容\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R29-W1\"\n  summary: \"Non-death component (21.1%) 的 routing signal 来源未分析\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 20 个 score-comparison labels 全部来自 both-survived episodes，16 det-preferred / 4 int-preferred。find-non-living-thing 是唯一 zero-death task（n=40, Δ_full=+9.58），贡献全部 score-comparison episodes，但未 deep-dive 分析 trajectory differences。一个简短 case study（2-3 个 episode）即可大幅改善。\"\n  action_items:\n    - round: 29\n      action: \"Appendix 增加 non-death score-comparison episodes 的 case study（分析 find-non-living-thing 中两种策略的 qualitative 差异）\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R29-W2\"\n  summary: \"单一 death mechanism (focus on [object]) 限制 failure mode generalizability\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Appendix N 显示 100% internal deaths 由同一 action pattern 触发。这是 ScienceWorld API 特异性，action-space filtering (-19 pp, Appendix O) 已证实。但 general claim ('any environment with asymmetric fatal outcomes') 基于非常特定的 failure mechanism。\"\n  action_items:\n    - round: 29\n      action: \"Discussion 增加一句区分 ScienceWorld-specific failure mode 和 general death avoidance framework 适用范围\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R29-M1\"\n  summary: \"Missing references: FrugalGPT, AutoMix, Options framework, Mixture-of-Depths\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"R1: FrugalGPT (Chen 2023), AutoMix (Madaan 2023), Options framework (Sutton 1999)。R2: Mixture-of-Depths (Raposo 2024), speculative decoding (Leviathan 2023, Chen 2023)。LATS (Zhou 2024) 可能已以不同名称引用。\""
  }
}
```

</details>

---


### Tool result

_source line 2433 · 2026-05-22T23:08:01.407363+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 23953}, \"error\": \"\"}"}

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

_source line 2434 · 2026-05-22T23:10:04.427129+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "simgate-modular-routing",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "report": "# Round 29 审稿报告 — simgate-modular-routing\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**Venue**: EMNLP 2026 (ARR May cycle), Long Paper (8 pages)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: R1 (方法严谨性+实验设计+统计分析), R2 (新颖性+完整性+写作质量+Related Work)\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual diagnostic framework，将 LLM agent routing signal 分解为 death avoidance 和 non-death 组成部分。在 ScienceWorld（11/30 task types, N=245 episodes）上发现 78.9% 的 non-tie routing labels 源自 death asymmetry（penalty-independent），DAF=90.4%（penalty-dependent, P=100）。跨模型验证（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B-it）显示 death dominance 在三个 7-9B 模型家族中一致复现（DAF 88-90%, spread 2.2 pp）。跨环境 probes（MATH, ALFWorld）诊断出定性不同的 routing mechanism。Router training（Qwen3 LoRA, 0.6B-4B）产生 negative result（episode-level 47.1±2.2%, below chance）。\n\n---\n\n## Strengths\n\n**S1. 新颖且有价值的诊断视角 [AGREE x2]。** \"先诊断再构建 router\" 的理念填补了方法论空白。现有 routing 工作（Toolformer, ART, Chameleon, CogRouter, ARES, MTRouter）直接训练 router 而不先理解 signal 构成。本文首次系统分解 routing signal。\n\n**S2. 极其详尽的统计分析 [AGREE x2]。** 20 个 appendices（A-T）提供罕见深度：bootstrap CI、cluster-robust t-test、wild cluster bootstrap、LOO robustness、penalty sensitivity。论文自觉标注 K=11 cluster bootstrap 局限并推荐 non-clustered CI 为主推断——这种统计自省极少见。\n\n**S3. 诚实的负面结果报告 [AGREE x2]。** Router failure（47.1±2.2%）被详细呈现，step-level vs episode-level gap 分析、text augmentation ablation、capacity scaling 系统排除了 data scarcity 和 model capacity 作为唯一解释。\n\n**S4. Anti-cherry-picking 分析有效 [AGREE x2]。** 19 个排除 task types 的 mean ΔDR=+38.2 pp 高于 included +28.7 pp（Table 4），Appendix S extended validation（n=20）确认 excluded DAF (0.991) > included (0.904)。选择偏差的质疑被有效排除。\n\n**S5. 跨模型复现可信 [AGREE x2]。** 三个 7-9B 模型家族 directional consistency 100%（10/10 death-prone tasks），internal vulnerability ~36-42%，Table 17 consolidation table 是有效 robustness evidence。\n\n**S6. Algorithm 1 设计合理 [R1]。** Death-priority rule 假设明确，Labeling Quality Audit（Appendix B）验证 zero tie-breaking labels。\n\n**S7. Hedging 语言诚实 [R2]。** Cross-environment probes 标注为 \"preliminary evidence\"，区分 methodological vs empirical generality。\n\n---\n\n## Weaknesses\n\n### Must-Fix (影响接收决定)\n\n**W1. [Critical, AGREE x2] 正文超出 8 页限制（R20-N1/R27-N1 复发）。** Sections 1-6 约 8.2-8.5 页，Conclusion 起始于 page 9。EMNLP 2026 限正文 8 页，有 desk reject 风险。视觉审查独立确认此问题。\n- 可操作方案：(1) 压缩 Conclusion 为 2-3 句（删除与 Introduction 重复的 contributions 列表），(2) 缩小 Figure 2 或移至 appendix，(3) 合并 §4/§5 中重叠内容。\n\n**W2. [Critical, AGREE x2] DAF=90.4% 作为 headline metric 对 penalty 有数学依赖。** DAF = δP/(δP + Δ_nd) 是 P 的单调递增函数——P=0 时 7.4%, P=10 时 50.4%, P=100 时 90.4%（Table 12）。Abstract/Introduction 仍以 DAF=90.4% 为主导叙事，penalty-independent label fraction（78.9%）被置于次要位置。§2.4 已讨论 P-sensitivity 但叙事优先级未调整。\n- 可操作方案：Abstract/Introduction 将 78.9% 作为 primary headline metric，DAF=90.4% 降为 \"at ScienceWorld's default P=100\" 的补充。\n\n### Should-Fix (提升论文质量)\n\n**W3. [Major, AGREE x2] 63% task exclusion rate 虽有 anti-cherry-picking 证据但限制 coverage。** 19/30 task types 被排除（dev 5, redundancy 7, agent floor 7），分析仅基于 37% task coverage。Taxonomic redundancy 的操作定义不透明，agent-floor tasks 与 30-step budget 限制的关系未探索。\n- 可操作方案：§3 明确 taxonomic redundancy 判断标准；讨论更长 step budget 下 agent-floor tasks 是否出现 non-death signal。\n\n**W4. [Major, AGREE x2] 跨环境 \"deterministic\" mode 语义不一致限制 cross-environment comparison。** ScienceWorld = oracle simulator, MATH = code interpreter, ALFWorld = admissible-action enumeration——信息特权程度完全不同。Conclusion 已修正为 \"the diagnostic procedure—though not the specific operationalization—transfers\"，但 §3.4 缺 explicit caveat。\n- 可操作方案：§3.4 开头增加 caveat，区分 procedure transferability 和 finding transferability。\n\n**W5. [Major, DIVERGENCE → consensus on scope] Router negative result 的解释。** R1 认为 class imbalance（9/245=3.7%）是 confound，failure 可能是 data-limited artifact。R2 REBUT：imbalance 是 death dominance 的直接表现非 collection bias，text augmentation/capacity scaling 已部分排除。共识：结论应限定为 \"under current data regime (N=245, 3.7% minority)\"。\n- 可操作方案：§3.6 结论限定 scope；讨论 selective collection strategy（只收集 death-free episodes）是否能提高 minority rate。\n\n**W6. [Major, AGREE x2] Non-death component (21.1%) 的 routing signal 来源未分析。** 20 个 score-comparison labels 全部来自 both-survived episodes，find-non-living-thing 是唯一 zero-death task（n=40, Δ_full=+9.58），但未 deep-dive 分析 trajectory differences。\n- 可操作方案：Appendix 增加 2-3 个 non-death episode 的 case study。\n\n### Nice-to-Fix (锦上添花)\n\n**W7. [Minor, AGREE x2] 72B scaling probe scope 过窄。** 仅一个 72B 模型，无 at-scale cross-model replication。应标注为 \"preliminary probe\"。\n\n**W8. [Minor, AGREE x2] 单一 death mechanism（focus on [object]）限制 failure mode 外部效度。** 100% internal deaths 由同一 action pattern 触发，是 ScienceWorld API 特异性。\n\n**W9. [Minor, DIVERGENCE] Figure 2 近似恒等关系。** R2 认为 Major（应移至 appendix 释放空间），R1 REBUT（有 pedagogical 价值，建议缩小而非移除）。如需解决 W1 页数问题，可作为释放空间的选项。\n\n**W10. [Minor, partial DIVERGENCE] 数字密度。** R2 认为过高，R1 部分辩护（分析论文需要 precise quantification），但同意 secondary stats 可精简。\n\n**W11. [Minor, AGREE x2] Related Work 缺 non-agent adaptive computation。** 未覆盖 Mixture-of-Depths、speculative decoding 等。一句 positioning 即可。\n\n**W12. [Minor, AGREE x2] Introduction/Conclusion contributions 列表重复。** 页数超限下应削减冗余。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成一致：\n\n1. **[AGREE]** DAF penalty dependence 是核心 framing 问题，78.9% 应为 primary metric\n2. **[AGREE]** 正文超页是 desk reject 风险\n3. **[AGREE]** 跨环境 deterministic mode 不可比\n4. **[AGREE]** Non-death 21.1% 分析缺失是 substantive gap\n5. **[AGREE]** Anti-cherry-picking analysis 有效排除了选择偏差\n6. **[AGREE]** 跨模型复现（3 families）可信\n7. **[AGREE]** 统计分析深度罕见且值得肯定\n8. **[AGREE]** Router failure 结论需限定 scope\n\n## Reviewer Divergence\n\n1. **[Figure 2 处理]** R2 建议移至 appendix (Major); R1 建议缩小保留 (Minor) — 取决于页数修复策略\n2. **[Router failure 本质]** R1 认为 class imbalance confound 更严重; R2 认为 imbalance 是 finding 的表现 — 共识：限定 scope\n3. **[Excitement]** R1: 3.5/5 (framework novelty 有持久价值); R2: 2.5/5 (triviality risk 显著) — reasonable disagreement\n4. **[数字密度]** R1 认为是分析论文必要特征; R2 认为过高影响可读性 — 共识：secondary stats 可精简\n\n---\n\n## Questions (需作者澄清)\n\n1. Algorithm 1 的 death-priority rule 在 both-dead 情况下不区分死亡时间。是否丢失了有用的 routing signal？\n2. Δ_nd = 2.84 的 bootstrap CI 是多少？如果 uncertainty 较大，DAF 的 interpretability 是否受影响？\n3. Decision framework（Appendix R）的 thresholds（15 pp, 75%, 50%）仅有 4 个 retrospective data points。选择依据和 sensitivity analysis？\n4. \"No prior work has decomposed routing decisions in interactive environments\" 是否过强？建议修改为 \"no prior work has systematically decomposed what drives routing preferences\"。\n5. 19 个 excluded task types 中的 agent-floor tasks：在更长 step budget（50, 100 steps）下是否出现 non-death routing signal？\n\n---\n\n## Missing References\n\n**R1 建议**:\n- FrugalGPT (Chen et al., 2023) — LLM routing/cascading\n- AutoMix (Madaan et al., 2023) — LLM routing/cascading\n- Options framework (Sutton et al., 1999) — temporal abstraction\n\n**R2 建议**:\n- Mixture-of-Depths (Raposo et al., 2024) — non-agent adaptive computation\n- Speculative decoding (Leviathan et al., 2023; Chen et al., 2023) — adaptive computation\n\n**共识**: 至少加一句 positioning 区分 token-level adaptive computation 和 episode-level diagnostic framework。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 完成\n\n| Severity | 发现 |\n|----------|------|\n| **Critical** | 主文超 8 页限制——Conclusion 从 page 9 开始，需压缩约 15-20 行 |\n| **Warning** | Pages 7-8 连续两页纯文本无 display item，审稿人视觉疲劳风险 |\n| **Warning** | 主文 display items 偏少（3 figure + 2 table = 5 个），大量结果推到 appendix |\n| **Info** | Figure 1 pipeline 图出现在 page 2 顶部，时机合理，颜色区分度好 |\n| **Info** | Figure 2 散点图尺寸偏小但文字仍可读 |\n| **Info** | 所有表格使用 booktabs 风格，排版专业整洁 |\n| **Info** | 全文无公式渲染错误、未解析引用或 margin 溢出 |\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n**Soundness**: 3.5/5 (R1: 3.5, R2: 3.5)\n**Excitement**: 3.0/5 (R1: 3.5, R2: 2.5)\n**Reproducibility**: 4.0/5 (R1: 4, R2: 4)\n**Confidence**: 4/5\n\n### 综合判断依据\n\n**接收方向的论据**:\n1. \"先诊断再构建 router\" 的方法论框架新颖，填补了 agent routing 领域的诊断性空白\n2. 统计分析的深度和透明度在该领域罕见（20 appendices, 多种 bootstrap 方法, LOO sensitivity）\n3. 跨模型复现（3 families, 7-9B tier）增强了 ScienceWorld 内发现的可信度\n4. 负面结果（router failure）的诚实报告对社区有警示价值\n5. Penalty-independent label fraction (78.9%) 是 robust 的核心发现\n\n**拒绝方向的论据**:\n1. **正文超页** [Critical]——desk reject 风险，优先修复\n2. **Triviality concern**——\"death avoidance dominates in death-penalized environment\" 具有可预测性（R2 Excitement 2.5/5），DAF 值对 P 的数学依赖加剧此印象\n3. **Cross-environment evidence 薄弱**——三环境的 \"deterministic\" mode 语义不同，仅 ScienceWorld 有完整验证\n4. **Non-death signal 分析缺失**——21.1% 的 routing signal 来源未解释\n5. **Router failure 解释 underdetermined**——signal-limited vs data-limited 在 3.7% minority rate 下无法区分\n\n### 定位建议\n\n论文的方法论贡献（counterfactual decomposition framework, DAF/SCI 指标）具有独立于具体发现的可复用价值，适合 **Findings** 接收。若能修复 W1（页数）、W2（DAF framing）、W6（non-death analysis），可升至 **3.5 Borderline Conference**。核心 Excitement 限制（triviality risk, 单一环境深度分析）是结构性的，难以通过 writing fix 解决。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 当前以 DAF=90.4% 为主导，应将 78.9% label fraction 提升为 headline\n- \"spread 2.2 pp\" 等 secondary stats 可移至正文\n\n### §1 Introduction\n- Contributions 列表与 Conclusion 近乎逐字重复，保留一处\n- \"no prior work has decomposed\" → \"no prior work has systematically decomposed what drives routing preferences\"\n\n### §2 Method\n- §2.4 DAF 定义后已包含 P-sensitivity 讨论，叙事层面到位\n- Algorithm 1 both-dead 情况的处理可在 footnote 中 justify\n\n### §3 Experiments\n- §3 开头明确 taxonomic redundancy 操作定义\n- §3.1 correlation/sensitivity 段中 Cohen's d=3.02 加一句 context（reflects near-binary consistency）\n- §3.4 开头加 caveat：三环境 deterministic mode 信息特权程度不同\n- §3.6 router failure 结论限定为 \"under current data regime\"\n\n### §4 Related Work\n- 加一句 non-agent adaptive computation positioning\n- 可考虑引用 FrugalGPT、AutoMix\n\n### §5 Discussion\n- 与 §4 有内容交集，合并/压缩可释放空间\n\n### §6 Conclusion\n- 压缩为 2-3 句 forward-looking summary，删除重复 contributions\n\n### Limitations\n- 内容充分（5 个方面），质量良好\n\n### Appendix\n- 增加 non-death episode case study（W6）\n- 考虑接收 Figure 2（如 R2 建议）以释放正文空间"
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
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "report": "# Round 29 审稿报告 — simgate-modular-routing\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**Venue**: EMNLP 2026 (ARR May cycle), Long Paper (8 pages)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: R1 (方法严谨性+实验设计+统计分析), R2 (新颖性+完整性+写作质量+Related Work)\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual diagnostic framework，将 LLM agent routing signal 分解为 death avoidance 和 non-death 组成部分。在 ScienceWorld（11/30 task types, N=245 episodes）上发现 78.9% 的 non-tie routing labels 源自 death asymmetry（penalty-independent），DAF=90.4%（penalty-dependent, P=100）。跨模型验证（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B-it）显示 death dominance 在三个 7-9B 模型家族中一致复现（DAF 88-90%, spread 2.2 pp）。跨环境 probes（MATH, ALFWorld）诊断出定性不同的 routing mechanism。Router training（Qwen3 LoRA, 0.6B-4B）产生 negative result（episode-level 47.1±2.2%, below chance）。\n\n---\n\n## Strengths\n\n**S1. 新颖且有价值的诊断视角 [AGREE x2]。** \"先诊断再构建 router\" 的理念填补了方法论空白。现有 routing 工作（Toolformer, ART, Chameleon, CogRouter, ARES, MTRouter）直接训练 router 而不先理解 signal 构成。本文首次系统分解 routing signal。\n\n**S2. 极其详尽的统计分析 [AGREE x2]。** 20 个 appendices（A-T）提供罕见深度：bootstrap CI、cluster-robust t-test、wild cluster bootstrap、LOO robustness、penalty sensitivity。论文自觉标注 K=11 cluster bootstrap 局限并推荐 non-clustered CI 为主推断——这种统计自省极少见。\n\n**S3. 诚实的负面结果报告 [AGREE x2]。** Router failure（47.1±2.2%）被详细呈现，step-level vs episode-level gap 分析、text augmentation ablation、capacity scaling 系统排除了 data scarcity 和 model capacity 作为唯一解释。\n\n**S4. Anti-cherry-picking 分析有效 [AGREE x2]。** 19 个排除 task types 的 mean ΔDR=+38.2 pp 高于 included +28.7 pp（Table 4），Appendix S extended validation（n=20）确认 excluded DAF (0.991) > included (0.904)。选择偏差的质疑被有效排除。\n\n**S5. 跨模型复现可信 [AGREE x2]。** 三个 7-9B 模型家族 directional consistency 100%（10/10 death-prone tasks），internal vulnerability ~36-42%，Table 17 consolidation table 是有效 robustness evidence。\n\n**S6. Algorithm 1 设计合理 [R1]。** Death-priority rule 假设明确，Labeling Quality Audit（Appendix B）验证 zero tie-breaking labels。\n\n**S7. Hedging 语言诚实 [R2]。** Cross-environment probes 标注为 \"preliminary evidence\"，区分 methodological vs empirical generality。\n\n---\n\n## Weaknesses\n\n### Must-Fix (影响接收决定)\n\n**W1. [Critical, AGREE x2] 正文超出 8 页限制（R20-N1/R27-N1 复发）。** Sections 1-6 约 8.2-8.5 页，Conclusion 起始于 page 9。EMNLP 2026 限正文 8 页，有 desk reject 风险。视觉审查独立确认此问题。\n- 可操作方案：(1) 压缩 Conclusion 为 2-3 句（删除与 Introduction 重复的 contributions 列表），(2) 缩小 Figure 2 或移至 appendix，(3) 合并 §4/§5 中重叠内容。\n\n**W2. [Critical, AGREE x2] DAF=90.4% 作为 headline metric 对 penalty 有数学依赖。** DAF = δP/(δP + Δ_nd) 是 P 的单调递增函数——P=0 时 7.4%, P=10 时 50.4%, P=100 时 90.4%（Table 12）。Abstract/Introduction 仍以 DAF=90.4% 为主导叙事，penalty-independent label fraction（78.9%）被置于次要位置。§2.4 已讨论 P-sensitivity 但叙事优先级未调整。\n- 可操作方案：Abstract/Introduction 将 78.9% 作为 primary headline metric，DAF=90.4% 降为 \"at ScienceWorld's default P=100\" 的补充。\n\n### Should-Fix (提升论文质量)\n\n**W3. [Major, AGREE x2] 63% task exclusion rate 虽有 anti-cherry-picking 证据但限制 coverage。** 19/30 task types 被排除（dev 5, redundancy 7, agent floor 7），分析仅基于 37% task coverage。Taxonomic redundancy 的操作定义不透明，agent-floor tasks 与 30-step budget 限制的关系未探索。\n- 可操作方案：§3 明确 taxonomic redundancy 判断标准；讨论更长 step budget 下 agent-floor tasks 是否出现 non-death signal。\n\n**W4. [Major, AGREE x2] 跨环境 \"deterministic\" mode 语义不一致限制 cross-environment comparison。** ScienceWorld = oracle simulator, MATH = code interpreter, ALFWorld = admissible-action enumeration——信息特权程度完全不同。Conclusion 已修正为 \"the diagnostic procedure—though not the specific operationalization—transfers\"，但 §3.4 缺 explicit caveat。\n- 可操作方案：§3.4 开头增加 caveat，区分 procedure transferability 和 finding transferability。\n\n**W5. [Major, DIVERGENCE → consensus on scope] Router negative result 的解释。** R1 认为 class imbalance（9/245=3.7%）是 confound，failure 可能是 data-limited artifact。R2 REBUT：imbalance 是 death dominance 的直接表现非 collection bias，text augmentation/capacity scaling 已部分排除。共识：结论应限定为 \"under current data regime (N=245, 3.7% minority)\"。\n- 可操作方案：§3.6 结论限定 scope；讨论 selective collection strategy（只收集 death-free episodes）是否能提高 minority rate。\n\n**W6. [Major, AGREE x2] Non-death component (21.1%) 的 routing signal 来源未分析。** 20 个 score-comparison labels 全部来自 both-survived episodes，find-non-living-thing 是唯一 zero-death task（n=40, Δ_full=+9.58），但未 deep-dive 分析 trajectory differences。\n- 可操作方案：Appendix 增加 2-3 个 non-death episode 的 case study。\n\n### Nice-to-Fix (锦上添花)\n\n**W7. [Minor, AGREE x2] 72B scaling probe scope 过窄。** 仅一个 72B 模型，无 at-scale cross-model replication。应标注为 \"preliminary probe\"。\n\n**W8. [Minor, AGREE x2] 单一 death mechanism（focus on [object]）限制 failure mode 外部效度。** 100% internal deaths 由同一 action pattern 触发，是 ScienceWorld API 特异性。\n\n**W9. [Minor, DIVERGENCE] Figure 2 近似恒等关系。** R2 认为 Major（应移至 appendix 释放空间），R1 REBUT（有 pedagogical 价值，建议缩小而非移除）。如需解决 W1 页数问题，可作为释放空间的选项。\n\n**W10. [Minor, partial DIVERGENCE] 数字密度。** R2 认为过高，R1 部分辩护（分析论文需要 precise quantification），但同意 secondary stats 可精简。\n\n**W11. [Minor, AGREE x2] Related Work 缺 non-agent adaptive computation。** 未覆盖 Mixture-of-Depths、speculative decoding 等。一句 positioning 即可。\n\n**W12. [Minor, AGREE x2] Introduction/Conclusion contributions 列表重复。** 页数超限下应削减冗余。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成一致：\n\n1. **[AGREE]** DAF penalty dependence 是核心 framing 问题，78.9% 应为 primary metric\n2. **[AGREE]** 正文超页是 desk reject 风险\n3. **[AGREE]** 跨环境 deterministic mode 不可比\n4. **[AGREE]** Non-death 21.1% 分析缺失是 substantive gap\n5. **[AGREE]** Anti-cherry-picking analysis 有效排除了选择偏差\n6. **[AGREE]** 跨模型复现（3 families）可信\n7. **[AGREE]** 统计分析深度罕见且值得肯定\n8. **[AGREE]** Router failure 结论需限定 scope\n\n## Reviewer Divergence\n\n1. **[Figure 2 处理]** R2 建议移至 appendix (Major); R1 建议缩小保留 (Minor) — 取决于页数修复策略\n2. **[Router failure 本质]** R1 认为 class imbalance confound 更严重; R2 认为 imbalance 是 finding 的表现 — 共识：限定 scope\n3. **[Excitement]** R1: 3.5/5 (framework novelty 有持久价值); R2: 2.5/5 (triviality risk 显著) — reasonable disagreement\n4. **[数字密度]** R1 认为是分析论文必要特征; R2 认为过高影响可读性 — 共识：secondary stats 可精简\n\n---\n\n## Questions (需作者澄清)\n\n1. Algorithm 1 的 death-priority rule 在 both-dead 情况下不区分死亡时间。是否丢失了有用的 routing signal？\n2. Δ_nd = 2.84 的 bootstrap CI 是多少？如果 uncertainty 较大，DAF 的 interpretability 是否受影响？\n3. Decision framework（Appendix R）的 thresholds（15 pp, 75%, 50%）仅有 4 个 retrospective data points。选择依据和 sensitivity analysis？\n4. \"No prior work has decomposed routing decisions in interactive environments\" 是否过强？建议修改为 \"no prior work has systematically decomposed what drives routing preferences\"。\n5. 19 个 excluded task types 中的 agent-floor tasks：在更长 step budget（50, 100 steps）下是否出现 non-death routing signal？\n\n---\n\n## Missing References\n\n**R1 建议**:\n- FrugalGPT (Chen et al., 2023) — LLM routing/cascading\n- AutoMix (Madaan et al., 2023) — LLM routing/cascading\n- Options framework (Sutton et al., 1999) — temporal abstraction\n\n**R2 建议**:\n- Mixture-of-Depths (Raposo et al., 2024) — non-agent adaptive computation\n- Speculative decoding (Leviathan et al., 2023; Chen et al., 2023) — adaptive computation\n\n**共识**: 至少加一句 positioning 区分 token-level adaptive computation 和 episode-level diagnostic framework。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 完成\n\n| Severity | 发现 |\n|----------|------|\n| **Critical** | 主文超 8 页限制——Conclusion 从 page 9 开始，需压缩约 15-20 行 |\n| **Warning** | Pages 7-8 连续两页纯文本无 display item，审稿人视觉疲劳风险 |\n| **Warning** | 主文 display items 偏少（3 figure + 2 table = 5 个），大量结果推到 appendix |\n| **Info** | Figure 1 pipeline 图出现在 page 2 顶部，时机合理，颜色区分度好 |\n| **Info** | Figure 2 散点图尺寸偏小但文字仍可读 |\n| **Info** | 所有表格使用 booktabs 风格，排版专业整洁 |\n| **Info** | 全文无公式渲染错误、未解析引用或 margin 溢出 |\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n**Soundness**: 3.5/5 (R1: 3.5, R2: 3.5)\n**Excitement**: 3.0/5 (R1: 3.5, R2: 2.5)\n**Reproducibility**: 4.0/5 (R1: 4, R2: 4)\n**Confidence**: 4/5\n\n### 综合判断依据\n\n**接收方向的论据**:\n1. \"先诊断再构建 router\" 的方法论框架新颖，填补了 agent routing 领域的诊断性空白\n2. 统计分析的深度和透明度在该领域罕见（20 appendices, 多种 bootstrap 方法, LOO sensitivity）\n3. 跨模型复现（3 families, 7-9B tier）增强了 ScienceWorld 内发现的可信度\n4. 负面结果（router failure）的诚实报告对社区有警示价值\n5. Penalty-independent label fraction (78.9%) 是 robust 的核心发现\n\n**拒绝方向的论据**:\n1. **正文超页** [Critical]——desk reject 风险，优先修复\n2. **Triviality concern**——\"death avoidance dominates in death-penalized environment\" 具有可预测性（R2 Excitement 2.5/5），DAF 值对 P 的数学依赖加剧此印象\n3. **Cross-environment evidence 薄弱**——三环境的 \"deterministic\" mode 语义不同，仅 ScienceWorld 有完整验证\n4. **Non-death signal 分析缺失**——21.1% 的 routing signal 来源未解释\n5. **Router failure 解释 underdetermined**——signal-limited vs data-limited 在 3.7% minority rate 下无法区分\n\n### 定位建议\n\n论文的方法论贡献（counterfactual decomposition framework, DAF/SCI 指标）具有独立于具体发现的可复用价值，适合 **Findings** 接收。若能修复 W1（页数）、W2（DAF framing）、W6（non-death analysis），可升至 **3.5 Borderline Conference**。核心 Excitement 限制（triviality risk, 单一环境深度分析）是结构性的，难以通过 writing fix 解决。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 当前以 DAF=90.4% 为主导，应将 78.9% label fraction 提升为 headline\n- \"spread 2.2 pp\" 等 secondary stats 可移至正文\n\n### §1 Introduction\n- Contributions 列表与 Conclusion 近乎逐字重复，保留一处\n- \"no prior work has decomposed\" → \"no prior work has systematically decomposed what drives routing preferences\"\n\n### §2 Method\n- §2.4 DAF 定义后已包含 P-sensitivity 讨论，叙事层面到位\n- Algorithm 1 both-dead 情况的处理可在 footnote 中 justify\n\n### §3 Experiments\n- §3 开头明确 taxonomic redundancy 操作定义\n- §3.1 correlation/sensitivity 段中 Cohen's d=3.02 加一句 context（reflects near-binary consistency）\n- §3.4 开头加 caveat：三环境 deterministic mode 信息特权程度不同\n- §3.6 router failure 结论限定为 \"under current data regime\"\n\n### §4 Related Work\n- 加一句 non-agent adaptive computation positioning\n- 可考虑引用 FrugalGPT、AutoMix\n\n### §5 Discussion\n- 与 §4 有内容交集，合并/压缩可释放空间\n\n### §6 Conclusion\n- 压缩为 2-3 句 forward-looking summary，删除重复 contributions\n\n### Limitations\n- 内容充分（5 个方面），质量良好\n\n### Appendix\n- 增加 non-death episode case study（W6）\n- 考虑接收 Figure 2（如 R2 建议）以释放正文空间"
  }
}
```

</details>

---


### Tool result

_source line 2435 · 2026-05-22T23:10:08.545784+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4118
}
```

</details>

---


### Assistant

_source line 2436 · 2026-05-22T23:10:22.371078+00:00_

**Round 29 审稿报告已投递。**

汇总：

| 维度 | 评分 |
|------|------|
| **Overall** | **3.0 — Findings** |
| Soundness | 3.5/5 |
| Excitement | 3.0/5 (R1: 3.5, R2: 2.5) |
| Reproducibility | 4.0/5 |

**关键 findings：**

1. **[Critical] 正文超 8 页**——Conclusion 溢出至 page 9，desk reject 风险。压缩 Conclusion + 合并 §4/§5 重叠内容可解决。
2. **[Critical] DAF framing**——90.4% 是 P=100 下的数学结果，78.9% penalty-independent label fraction 应作为 headline。
3. **[Major] 跨环境 deterministic mode 语义不一致**——三环境的信息特权程度完全不同，限制 cross-env comparison validity。
4. **[Major] Non-death 21.1% 分析缺失**——score-comparison episodes 缺 case study。
5. **[Major] Router failure 解释 underdetermined**——3.7% minority rate 下 signal-limited vs data-limited 无法区分。

**升分路径**：修复 W1（页数）+ W2（DAF framing）+ W6（non-death analysis）可达 3.5 Borderline Conference。Excitement 限制（triviality risk）是结构性的。

Issue tracker 已同步更新至 `review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 204

## Round 204

2 recorded events


### User

_source line 2437 · 2026-05-22T23:10:24.899678+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- 7 条 Weaknesses 中 **6 条 AGREE**（W1/W2/W4/W5/W6/W7），**1 条 REBUT**（W3）
- W3 的核心反驳：class imbalance 是 death avoidance dominance 的直接结果而非 data artifact，但同意应限定结论 scope
- R1 和我的主要共识在 DAF penalty-dependence 和跨环境 mode 语义不一致
- 主要分歧在 Overall 评分（R1: 3.5 vs 我: 3.0），源于对 triviality risk 的不同权重判断

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

_source line 2438 · 2026-05-22T23:10:41.262435+00:00_

Round 29 审稿完成。

**审稿报告已投递给 Research Director。**

汇总：
- **Overall: 3.0 (Findings)**
- R1: 3.5 (Borderline Conference), R2: 3.0 (Findings)
- Soundness 3.5, Excitement 3.0, Reproducibility 4.0

**Must-Fix (2)**：正文超 8 页（desk reject 风险）、DAF=90.4% 作为 headline 的 penalty 依赖性

**Should-Fix (4)**：63% task exclusion 的 taxonomic redundancy 定义不透明、跨环境 deterministic mode 不可比、router failure 结论需限定 scope、non-death 21.1% 分析缺失

**核心共识**：方法论框架（counterfactual decomposition + DAF/SCI）有独立可复用价值，统计分析深度罕见，跨模型复现可信。核心限制是 triviality risk（death dominance in death-penalized env）和单一环境深度分析的结构性 excitement deficit。

Issue tracker 已同步更新（`review_issues.yaml`）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 205

## Round 205

54 recorded events


### User

_source line 2439 · 2026-05-23T03:32:10.579098+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (8 pages)
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

_source line 2440 · 2026-05-23T03:32:16.809350+00:00_

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

_source line 2441 · 2026-05-23T03:32:16.860386+00:00_

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

_source line 2442 · 2026-05-23T03:32:25.801413+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
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
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2443 · 2026-05-23T03:32:25.801771+00:00_

No matching deferred tools found

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

_source line 2444 · 2026-05-23T03:32:29.568267+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2445 · 2026-05-23T03:32:29.619095+00:00_



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

_source line 2446 · 2026-05-23T03:32:34.087928+00:00_

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

_source line 2447 · 2026-05-23T03:32:35.999283+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (121 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| alfworld-llama-cross-model | Llama-3.1-8B on ALFWorld will show information asymmetry (not death) as the dominant routing mechanism, consistent with Qwen2.5-7B findings (25.9% det-preferred, DAF=0%), confirming the framework diagnoses environment-specific mechanisms regardless of model family. | — | — | — |\n| gemma-scienceworld-cross-model | Gemma-2-9B-it on ScienceWorld will show death dominance (DAF > 80%) consistent with Qwen2.5-7B (90.4%) and Llama-3.1-8B (88.2%), extending the cross-model-family evidence from 2 to 3 independent model families and strengthening the claim that death avoidance dominates routing signal regardless of model architecture. | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **gemma-scienceworld-gpu0** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) observed with Qwen2.5-7B (DAF=90.4%) and Llama-3.1-8B (DAF=88.2%), confirming the diagnostic finding is model-agnostic across 3 model families.\n- **gemma-scienceworld-v4** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) ob
…[truncated 1790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1911
}
```

</details>

---


### Tool call

_source line 2448 · 2026-05-23T03:32:36.150310+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2449 · 2026-05-23T03:32:36.502793+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\graphicspath{{figures/}}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{algorithm}
16	\usepackage{algorithmic}
17	\usepackage{tcolorbox}
18	\tcbuselibrary{listings,breakable}
19	
20	\hypersetup{pdfauthor={},pdftitle={}}
21	
22	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{abstract}
30	\input{introduction}
31	\input{method}
32	\input{experiments}
33	\input{related_work}
34	\input{discussion}
35	\input{conclusion}
36	
37	\section*{Limitations}
38	
39	\paragraph{Environmental scope.}
40	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct), though extended validation of representative excluded tasks confirms the pattern (Appendix~\ref{app:extended-validation}). The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface non-death-dominated signal that our current setup does not capture. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:cross-env}, \S\ref{sec:discussion}) provide preliminary supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct cross-model replication (11 task types, $N{=}220$; \S\ref{sec:cross-model}) shows death dominance replicates with direction consistency 10/10 while vulnerability magnitude varies ($+30.0$~pp vs.\ Qwen $+26.5$~pp), though both models are in the 7--8B parameter range; Qwen2.5-72B ($10{\times}$ scale) re
…[truncated 70810 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 2450 · 2026-05-23T03:32:36.955028+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
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

_source line 2451 · 2026-05-23T03:32:36.955401+00:00_



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

_source line 2452 · 2026-05-23T03:32:37.307077+00:00_

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

_source line 2453 · 2026-05-23T03:32:37.407833+00:00_

No matching deferred tools found

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

_source line 2454 · 2026-05-23T03:32:47.422740+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR"
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
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool call

_source line 2455 · 2026-05-23T03:32:48.930215+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 2456 · 2026-05-23T03:32:50.236501+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 1306
}
```

</details>

---


### Tool call

_source line 2457 · 2026-05-23T03:32:50.387628+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_30/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_30/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2458 · 2026-05-23T03:32:50.540264+00:00_

-rw-r--r-- 1 ubuntu ubuntu 602144 May 23 03:31 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_30/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool result

_source line 2459 · 2026-05-23T03:32:55.511034+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 with the ARR (ACL Rolling Review) process:

## Submission Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## ARR Submission Process

Papers must be submitted, at latest, by the ARR 2026 May cycle. The ARR submission deadline for long and short papers is May 25, 
…[truncated 937 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 8088
}
```

</details>

---


### Tool call

_source line 2460 · 2026-05-23T03:33:00.784851+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit template anonymity requirements site:2026.emnlp.org"
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
    "query": "EMNLP 2026 submission format page limit template anonymity requirements site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 2461 · 2026-05-23T03:33:01.136728+00:00_

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

_source line 2462 · 2026-05-23T03:33:01.188079+00:00_

1	# Round 29 Review Issues (fresh review, 2026-05-22)
2	# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作)
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
70	  category: format
71	  severity: info
72	  status: resolved
73	  first_raised_r
…[truncated 22680 chars]

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

_source line 2463 · 2026-05-23T03:33:02.243731+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/{abstract,introduction,method,experiments,related_work,discussion,conclusion}.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/{abstract,introduction,method,experiments,related_work,discussion,conclusion}.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 2464 · 2026-05-23T03:33:02.294428+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2465 · 2026-05-23T03:33:07.519962+00:00_

Web search results for query: "EMNLP 2026 submission format page limit template anonymity requirements site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"}]

Based on the search results from the EMNLP 2026 website, here's what I found regarding submission requirements:

## Anonymity Requirements

Following the ACL and ARR policies, there is no anonymity period requirement. However, the reviewing process will continue to be double-blind, with reviewers not seeing authors, nor will authors see reviewers and reviews on ARR. For the Industry Track specifically, submissions must neither include the authors' names nor their affiliations.

## Page Limits and Format

The search results mention specific page limit requirements for certain submission types. For example, proposals should use the ACL paper submission format and should not exceed 4 pages of content (plus one page for tutor biographies and unlimited pages for references). Additionally, authors are required to discu
…[truncated 630 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 6735
}
```

</details>

---


### Tool call

_source line 2466 · 2026-05-23T03:33:18.311370+00:00_

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

_source line 2467 · 2026-05-23T03:33:18.563501+00:00_

1	\begin{abstract}
2	LLM agent routing (deciding when to rely on internal reasoning versus external tool use) is typically addressed by training routers directly, without first understanding what mechanistic signal drives the routing preference. This absence of diagnostic methods risks building routers atop confounded or trivial signal. We propose an episode-level counterfactual framework that compares pure-strategy outcomes (internal-only vs.\ deterministic-only) to decompose routing signal into its mechanistic components before any router is constructed. Applying this framework to ScienceWorld (11 task types, 245 episodes), we find that 78.9\% of non-tie episode-level routing labels arise from death asymmetry---a finding replicated across three architecturally distinct 7--9B model families, revealing that in catastrophic-failure environments, signal diversity can collapse to a single dominant mechanism. Cross-environment probes on MATH and ALFWorld diagnose qualitatively different routing mechanisms (no extractable signal and information asymmetry, respectively), providing preliminary evidence of applicability beyond death-dominated settings. The framework distinguishes \emph{methodological generality} (applicable to any environment with paired episode outcomes) from \emph{empirical generality} (full quantitative validation on ScienceWorld only). A ${\sim}$50-episode pilot suffices for build-vs-buy decisions given large effect sizes ($d = 3.02$).
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 2468 · 2026-05-23T03:33:18.563899+00:00_

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

_source line 2469 · 2026-05-23T03:33:18.664585+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	In ScienceWorld \citep{scienceworld-2022}, a text-based science simulation, internal reasoning is error-prone, as the model may hallucinate state changes (e.g., that water has boiled when the stove was never activated), while deterministic external computation eliminates such errors via exact state transitions. The practical question: \emph{when should an agent route computation externally versus internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision: Toolformer \citep{toolformer-2023} inserts API calls by perplexity reduction; ART \citep{art-2023} decomposes tasks into tool-augmented programs; Chameleon \citep{chameleon-2023} selects heterogeneous modules per subtask; adaptive-computation methods route to different reasoning depths \citep{cogrouter-2026,ares-2026}, model tiers \citep{mtrouter-2026}, or episode-level model selection under sparse rewards \citep{budget-aware-routing-2026}; concurrent analyses further presuppose diverse routing signals~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026}. These approaches, which operate in non-catastrophic settings, share the assumption that routing signal stems from diverse sources and a learned router can exploit it---an assumption that remains untested: no prior work has systematically decomposed what drives routing preferences in interactive environments.
7	
8	We propose a \emph{diagnostic framework} comprising (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95), a penalty-independen
…[truncated 2187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2470 · 2026-05-23T03:33:19.066518+00:00_

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

_source line 2471 · 2026-05-23T03:33:19.518809+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/pipeline_overview.pdf}
7	\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\ref{alg:labeling}.}
8	\label{fig:pipeline}
9	\end{figure}
10	
11	Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically (Appendix~\ref{app:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
12	
13	\subsection{Problem Setup}
14	\label{sec:problem-setup}
15	
16	Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\citep{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic} (${\tt det}$), a privileged-information strategy that eliminates observation uncertainty---instantiated as oracle simulator (ScienceWorld), code interpreter (MATH), or admissible-action enumeration (ALFWorld); these qualitative differences affect what routing signals the framework can detect. A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \math
…[truncated 7474 chars]

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

_source line 2472 · 2026-05-23T03:33:19.519208+00:00_

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

_source line 2473 · 2026-05-23T03:33:20.524161+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types (63\%) lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). Taxonomically redundant tasks share identical action vocabularies, reward functions, and environmental dynamics, differing only in target entity; we retain one representative per family (Appendix~\ref{app:per-task}). This scope limits generalizability: conclusions apply to the included subset; increasing the 30-step budget might surface signal in excluded types (see Limitations). An anti-cherry-picking analysis confirms that death dominance holds in 18 of these 19 types, with a mean $\Delta\text{DR} = +38.2$\,pp exceeding the included tasks' $+28.7$\,pp (Appendix~\ref{app:per-task}). Extended validation at $n{=}20$ on five representative excluded tasks confirms this direction ($\overline{\Delta\text{DR}} = +32.0$\,pp; Appendix~\ref{app:extended-validation}). A reasoning-depth ablation ($n{=}120$) found no significant difference between internal strategy variants ($p > 0.26$; Appendix~\ref{app:ablations}). Prescreening used $n{=}5$ episodes per task type; directional consistency (18/19 types favoring deterministic) rather than point estimates drives the inclusion criterion.
5	
6	\subsection{Death Avoidance Decomposition}
7	\label{sec:death-decomp}
8	
9	
10	Of the 95 non-tie routing labels, 75 (78.9\%) arise from death asymmetry: the internal strategy triggers a catastrophic $-100$ penalty while the deterministic strategy survives. This penalty-independent label fraction is the primary diagnostic metric. Of these, 54 are sole-signal labels where death was the only discriminator; at $P{=}0$ these reduce to ties, but the labeling function itself is penalty-independent (Algorithm~\ref{alg:labeling}).
11	
12	Of 245 episodes, 150 (61.2\%) show no preference between strategies; routing is relevant in the r
…[truncated 14719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 2474 · 2026-05-23T03:33:20.524636+00:00_

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

_source line 2475 · 2026-05-23T03:33:21.027107+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}, spanning several functional categories.
5	Self-supervised methods learn tool invocation from loss signals \citep{toolformer-2023,toolace-2025}, token-level methods embed tools in the vocabulary \citep{toolkengpt-2023}, task-level decomposition routes subtasks to specialized modules \citep{art-2023,chameleon-2023}, and RL-based methods learn routing from reward \citep{retool-2025}.
6	All focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
7	Concurrent work examines \emph{when} to invoke tools: tool-call decisions correlate with uncertainty~\citep{tool-overuse-illusion-2026}, are encoded in hidden states~\citep{when2tool-2026}, impose a ``tool-use tax''~\citep{tool-use-tax-2026}, or follow necessity-utility-affordability logic~\citep{to-call-or-not-2026}. Our decomposition yields a concrete answer: 78.9\% of non-tie routing labels trace to catastrophic-failure prevention.
8	
9	\paragraph{Adaptive Computation and Routing.}
10	Adaptive routing traces back to learned halting policies \citep{graves2016act}. Mixture-of-Recursions \citep{mixture-of-recursions-2025} learns token-level recursion depths in the LLM era; concurrent work further diversifies routing granularity: CogRouter \citep{cogrouter-2026} adapts per-step depth, ARES \citep{ares-2026} selects effort levels, and MTRouter \citep{mtrouter-2026} addresses multi-turn settings; in death-dominated environments, the task-type-level binary signal is structurally inaccessible to these step-level approaches (\S\ref{sec:router-diagnostic}).
11	RouteLLM \citep{routellm-2024} learns routers from preference data to select between strong and weak models; cost-optimization routing (FrugalGPT~\citep{frugalgpt-2023}; AutoMix~\citep{automix-2024}) cascades queries across model tiers.
…[truncated 2817 chars]

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

_source line 2476 · 2026-05-23T03:33:21.077725+00:00_

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

_source line 2477 · 2026-05-23T03:33:21.178653+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Signal granularity and router failure.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property (10/11 types carry death risk), but step-level features correlate weakly because death risk depends on multi-step trajectories. Six router variants (0.6B--4B, classification and generative) converge on near-chance step-level accuracy ($56$--$59\%$); this convergent failure is consistent with signal limitation; however, extreme class imbalance (90.5\% deterministic-preferred, only 9 internal-preferred episodes) makes a data-limited explanation equally plausible---distinguishing the two requires ${\sim}$1{,}350 paired episodes to obtain 50 minority-class samples. Cross-task-type transfer yields chance accuracy (49.2\%; Appendix~\ref{app:ablations}). A train--deploy distribution shift~\citep{dagger-2011} may also contribute to the negative result.
6	
7	\paragraph{Non-triviality and oracle confound.}
8	While death dominance follows from the penalty structure (\S\ref{sec:daf}), two consequences were not predictable a priori: $10{\times}$ scaling to 72B fails to eliminate it (DAF${}= 92.4\%$), and Reflexion yields DAF${}>100\%$. All four interventions leave ${\geq}12$~pp residual gaps (Appendix~\ref{sec:threshold-routing}); cross-model DR stability ($36$--$43\%$) confirms death vulnerability is a task-environment property. An oracle confound (``is the signal merely use the oracle?'') is addressed by two observations: $\Delta_{\text{nd}} = 2.84$ (9.6\% of total gap)---internal reasoning provides almost no non-death advantage---and action-space filtering (Appendix~\ref{app:grounding-ablation}) reduces death rate by 19~pp while remaining far above deterministic safety.
9	
10	\paragraph{Practical implications and actionability.}
11	The penalty-invariant label fraction (78.9\%) is the primary diagnostic; DAF varies with $P$ (Appendix~\re
…[truncated 671 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2478 · 2026-05-23T03:33:21.179101+00:00_

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

_source line 2479 · 2026-05-23T03:33:21.279721+00:00_

1	\section{Conclusion}
2	
3	Our episode-level counterfactual framework reveals that 78.9\% of non-tie routing labels in ScienceWorld stem from death avoidance---replicated across three model families, persistent under $10{\times}$ scaling, and transferable to qualitatively different environments. Future work should validate this in additional catastrophic-failure settings and investigate lightweight death-prediction mechanisms that exploit task-type-level binary structure without full step-level router training.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2480 · 2026-05-23T03:33:39.656588+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "decisions.yaml",
  "max_chars": "3000"
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
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2481 · 2026-05-23T03:33:41.414322+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/decisions.yaml\", \"content\": \"_next_id: 134\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:25 UTC\\n  summary: 'MVP 方案: ScienceWorld 信号检测——验证确定性模拟是否在规则驱动任务上优于 LLM 内部推理'\\n  rationale: 12 天 deadline 下必须快速验证核心假设。ScienceWorld 是 primary track，其 JVM 后端提供精确的规则化状态转移，与\\n    LLM 近似推理的差距应该最大。选 5 task types × 10 episodes 的小规模 counterfactual 比较，不训练 router，纯信号检测。Pass\\n    标准 ≥2/5 task types >5pp，基于 ITP-R vs CogRouter 7.4pp 差距的量级。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:28 UTC\\n  summary: 采纳 Reviewer 全部 4 条 warning，修订 MVP 为 Phase 0 + Phase 1 两阶段方案\\n  rationale: Reviewer 指出 D001 方案 3 个操作层缺陷：(1) counterfactual 方法未明确——改为 episode-level\\n    3-way (always-internal / always-deterministic / oracle-routing)，oracle 作为 selective\\n    routing 上界；(2) N=10 统计功效不足——增加到 20 episodes/task type + bootstrap 90% CI；(3) kill\\n    criteria 不完整——增加 Phase 0 工程 gate、灰区 conditional pass、pre-register 5 task types\\n    (3S+1M+1W)。无额外 GPU 成本，仅设计层修正。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 07:43 UTC\\n  summary: GPU0 继续收集 baseline，GPU1 停下修复 tie-break + 致死动作过滤后重跑\\n  rationale: Fork 诊断发现两个方法论缺陷：(1) tie-break >= 使 95% delta=0 步骤 oracle 永远选 internal，oracle\\n    数据不可信；(2) 致死动作 (score=-100) 污染三条线。修 >= 为 >（oracle 仅在 deterministic 严格更优时介入）+ 致死动作过滤。不做\\n    N-step rollout——1-step 局限性是真实发现，MVP 应如实反映。GPU0 baseline 数据有效，不浪费已有进度。\\n  related_experiments:\\n  - exp_id: mvp-p1-gpu0\\n    role: baseline data, continue\\n  - exp_id: mvp-p1-gpu1-vllm\\n    role: kill, fix, rerun\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 08:13 UTC\\n  summary: MVP 判定 primary metric 改为 always-deterministic vs always-internal，oracle\\n    降为 supplementary\\n  rationale: 1-step lookahead 在稀疏 reward 下 95% 步骤 delta=0，任何 tie-break 都使 oracle 退化（>=\\n    → always-internal，> → always-determinis
…[truncated 1447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1757
}
```

</details>

---


### Tool call

_source line 2482 · 2026-05-23T03:33:41.415095+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_30/submitted.pdf",
  "pages": "1-9"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_30/submitted.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 2483 · 2026-05-23T03:33:42.018646+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_30/submitted.pdf (588KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 2484 · 2026-05-23T03:35:04.963739+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 审稿论文\n- 标题: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_30/submitted.pdf`\n- 目标 venue: **EMNLP 2026**（通过 ARR May 2026 cycle）\n- 投稿类别: Long Paper\n- Deadline: 2026-05-25\n\n## Venue 要求\n- 正文 8 页严格限制，references 无限制\n- Limitations 章节必须有（不计入页数限制，但不能含过多额外内容）\n- Ethical considerations 可选（不计入页数）\n- Double-blind 审稿（作者信息匿名）\n- ACL 模板\n- ARR Responsible NLP Checklist 在 OpenReview submission form 中填写（不在论文 PDF 中）\n\n## Overall Assessment 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查侧重\n1. **方法论严谨性**：counterfactual framework 的有效性、DAF 分解的数学合理性、episode-level labeling 的假设和局限\n2. **实验设计**：ScienceWorld 11/30 task types 的选择偏差问题、cross-model (Llama/Gemma/72B) 验证的充分性、router 训练实验的 confounds\n3. **统计分析**：bootstrap CI 可靠性（K=11 cluster 问题）、effect size 报告、multiple comparison 处理\n4. **可重复性**：实验描述是否充分、超参数报告是否完整\n5. **格式合规**：8 页限制、匿名性、模板使用\n\n## 输出格式\n请按以下结构输出审稿意见：\n```\n## Summary (2-3 句)\n\n## Strengths (逐条，标注 S1, S2, ...)\n\n## Weaknesses (逐条，标注 W1, W2, ...，每条标注 severity: critical/warning/info)\n- 对每个 weakness 给出具体证据（引用 Section/Table/Figure）\n\n## Questions (逐条，Q1, Q2, ...)\n\n## Missing References\n\n## Overall Assessment\n- Score: [用 EMNLP 2026 ARR 评分标准]\n- Confidence: [1-5]\n- Excitement: [1-5]\n- Soundness: [1-5]\n- 一句话总评\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "simgate-modular-routing",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 审稿论文\n- 标题: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_30/submitted.pdf`\n- 目标 venue: **EMNLP 2026**（通过 ARR May 2026 cycle）\n- 投稿类别: Long Paper\n- Deadline: 2026-05-25\n\n## Venue 要求\n- 正文 8 页严格限制，references 无限制\n- Limitations 章节必须有（不计入页数限制，但不能含过多额外内容）\n- Ethical considerations 可选（不计入页数）\n- Double-blind 审稿（作者信息匿名）\n- ACL 模板\n- ARR Responsible NLP Checklist 在 OpenReview submission form 中填写（不在论文 PDF 中）\n\n## Overall Assessment 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查侧重\n1. **方法论严谨性**：counterfactual framework 的有效性、DAF 分解的数学合理性、episode-level labeling 的假设和局限\n2. **实验设计**：ScienceWorld 11/30 task types 的选择偏差问题、cross-model (Llama/Gemma/72B) 验证的充分性、router 训练实验的 confounds\n3. **统计分析**：bootstrap CI 可靠性（K=11 cluster 问题）、effect size 报告、multiple comparison 处理\n4. **可重复性**：实验描述是否充分、超参数报告是否完整\n5. **格式合规**：8 页限制、匿名性、模板使用\n\n## 输出格式\n请按以下结构输出审稿意见：\n```\n## Summary (2-3 句)\n\n## Strengths (逐条，标注 S1, S2, ...)\n\n## Weaknesses (逐条，标注 W1, W2, ...，每条标注 severity: critical/warning/info)\n- 对每个 weakness 给出具体证据（引用 Section/Table/Figure）\n\n## Questions (逐条，Q1, Q2, ...)\n\n## Missing References\n\n## Overall Assessment\n- Score: [用 EMNLP 2026 ARR 评分标准]\n- Confidence: [1-5]\n- Excitement: [1-5]\n- Soundness: [1-5]\n- 一句话总评\n```"
  }
}
````

</details>

---


### Tool result

_source line 2485 · 2026-05-23T03:35:16.019146+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11055
}
```

</details>

---


### Tool call

_source line 2486 · 2026-05-23T03:35:16.170067+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 审稿论文\n- 标题: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_30/submitted.pdf`\n- 目标 venue: **EMNLP 2026**（通过 ARR May 2026 cycle）\n- 投稿类别: Long Paper\n- Deadline: 2026-05-25\n\n## Venue 要求\n- 正文 8 页严格限制，references 无限制\n- Limitations 章节必须有（不计入页数限制，但不能含过多额外内容）\n- Ethical considerations 可选（不计入页数）\n- Double-blind 审稿（作者信息匿名）\n- ACL 模板\n- ARR Responsible NLP Checklist 在 OpenReview submission form 中填写（不在论文 PDF 中）\n\n## Overall Assessment 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查侧重\n1. **新颖性和贡献**：核心发现（death avoidance dominates routing signal）的 novelty 程度、对 LLM agent routing 社区的贡献、是否存在 triviality 风险\n2. **Framing 和 claims**：Abstract/Title 与实际证据的匹配、generalization claims 是否超出数据支撑、\"framework\" vs \"empirical finding\" 的定位一致性\n3. **Related Work 完整性**：是否覆盖了 LLM routing、adaptive computation、safe RL、counterfactual evaluation 的关键工作；是否有重要遗漏\n4. **写作质量**：叙事连贯性、论证逻辑、术语一致性、段落组织、信息密度\n5. **完整性**：cross-environment 验证是否充分、limitations 讨论是否诚实和全面、actionability 是否到位\n\n## 输出格式\n请按以下结构输出审稿意见：\n```\n## Summary (2-3 句)\n\n## Strengths (逐条，标注 S1, S2, ...)\n\n## Weaknesses (逐条，标注 W1, W2, ...，每条标注 severity: critical/warning/info)\n- 对每个 weakness 给出具体证据（引用 Section/Table/Figure）\n\n## Questions (逐条，Q1, Q2, ...)\n\n## Missing References\n\n## Overall Assessment\n- Score: [用 EMNLP 2026 ARR 评分标准]\n- Confidence: [1-5]\n- Excitement: [1-5]\n- Soundness: [1-5]\n- 一句话总评\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "simgate-modular-routing",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 审稿论文\n- 标题: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_30/submitted.pdf`\n- 目标 venue: **EMNLP 2026**（通过 ARR May 2026 cycle）\n- 投稿类别: Long Paper\n- Deadline: 2026-05-25\n\n## Venue 要求\n- 正文 8 页严格限制，references 无限制\n- Limitations 章节必须有（不计入页数限制，但不能含过多额外内容）\n- Ethical considerations 可选（不计入页数）\n- Double-blind 审稿（作者信息匿名）\n- ACL 模板\n- ARR Responsible NLP Checklist 在 OpenReview submission form 中填写（不在论文 PDF 中）\n\n## Overall Assessment 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查侧重\n1. **新颖性和贡献**：核心发现（death avoidance dominates routing signal）的 novelty 程度、对 LLM agent routing 社区的贡献、是否存在 triviality 风险\n2. **Framing 和 claims**：Abstract/Title 与实际证据的匹配、generalization claims 是否超出数据支撑、\"framework\" vs \"empirical finding\" 的定位一致性\n3. **Related Work 完整性**：是否覆盖了 LLM routing、adaptive computation、safe RL、counterfactual evaluation 的关键工作；是否有重要遗漏\n4. **写作质量**：叙事连贯性、论证逻辑、术语一致性、段落组织、信息密度\n5. **完整性**：cross-environment 验证是否充分、limitations 讨论是否诚实和全面、actionability 是否到位\n\n## 输出格式\n请按以下结构输出审稿意见：\n```\n## Summary (2-3 句)\n\n## Strengths (逐条，标注 S1, S2, ...)\n\n## Weaknesses (逐条，标注 W1, W2, ...，每条标注 severity: critical/warning/info)\n- 对每个 weakness 给出具体证据（引用 Section/Table/Figure）\n\n## Questions (逐条，Q1, Q2, ...)\n\n## Missing References\n\n## Overall Assessment\n- Score: [用 EMNLP 2026 ARR 评分标准]\n- Confidence: [1-5]\n- Excitement: [1-5]\n- Soundness: [1-5]\n- 一句话总评\n```"
  }
}
````

</details>

---


### Tool result

_source line 2487 · 2026-05-23T03:35:17.834034+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1663
}
```

</details>

---


### Tool call

_source line 2488 · 2026-05-23T03:35:17.834533+00:00_

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

_source line 2489 · 2026-05-23T03:35:17.834833+00:00_

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


### Tool result

_source line 2490 · 2026-05-23T03:35:19.818227+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 1983
}
```

</details>

---


### Tool result

_source line 2491 · 2026-05-23T03:35:19.868930+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 2034
}
```

</details>

---


### Assistant

_source line 2492 · 2026-05-23T03:35:47.218292+00:00_

**Round 30 圆桌审稿已启动。**

| 项目 | 状态 |
|------|------|
| **投稿目标** | EMNLP 2026 (ARR May cycle), Long Paper, deadline 2026-05-25 |
| **论文** | "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld" |
| **PDF** | 已确认存在 (588KB, 9 pages: 正文 8p + Limitations 起始于 p9) |
| **匿名性** | ✓ Author = "Anonymous", `\usepackage[review]{acl}` |
| **Reviewer 1** | ✅ 已派发 — 方法严谨性 + 实验设计 |
| **Reviewer 2** | ✅ 已派发 — 新颖性 + 完整性 + 写作 |
| **视觉审查** | ✅ 已派发 (fire-and-forget) |
| **外部审稿** | ⬜ 未配置 (not_requested) |

等待两位 Reviewer 独立初审完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 206

## Round 206

44 recorded events


### User

_source line 2493 · 2026-05-23T03:40:11.890343+00:00_

[Reviewer 2 审稿结果]:
全部 24 页已阅读完毕。现在整理审稿意见。

---

[Reviewer 1 审稿结果]:
已完成论文全文阅读（正文8页 + Limitations/Ethics + 21页附录）。现在撰写审稿意见并提交。

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


### Tool call

_source line 2494 · 2026-05-23T03:40:46.497558+00:00_

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

_source line 2495 · 2026-05-23T03:40:46.498591+00:00_

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
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 2496 · 2026-05-23T03:40:50.318520+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_post_to_reviewer,director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,read_project_file,submit_review_report_to_research_director,update_review_issues",
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
    "query": "select:director_post_to_reviewer,director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,read_project_file,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2497 · 2026-05-23T03:40:50.369290+00:00_

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

_source line 2498 · 2026-05-23T03:40:54.185180+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
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
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2499 · 2026-05-23T03:40:54.185657+00:00_



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

_source line 2500 · 2026-05-23T03:41:22.180131+00:00_

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

_source line 2501 · 2026-05-23T03:41:23.536791+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (121 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| alfworld-llama-cross-model | Llama-3.1-8B on ALFWorld will show information asymmetry (not death) as the dominant routing mechanism, consistent with Qwen2.5-7B findings (25.9% det-preferred, DAF=0%), confirming the framework diagnoses environment-specific mechanisms regardless of model family. | — | — | — |\n| gemma-scienceworld-cross-model | Gemma-2-9B-it on ScienceWorld will show death dominance (DAF > 80%) consistent with Qwen2.5-7B (90.4%) and Llama-3.1-8B (88.2%), extending the cross-model-family evidence from 2 to 3 independent model families and strengthening the claim that death avoidance dominates routing signal regardless of model architecture. | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **gemma-scienceworld-gpu0** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) observed with Qwen2.5-7B (DAF=90.4%) and Llama-3.1-8B (DAF=88.2%), confirming the diagnostic finding is model-agnostic across 3 model families.\n- **gemma-scienceworld-v4** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) ob
…[truncated 1790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool call

_source line 2502 · 2026-05-23T03:41:23.537282+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "limit": "120"
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
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 2503 · 2026-05-23T03:41:23.587906+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\graphicspath{{figures/}}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{algorithm}
16	\usepackage{algorithmic}
17	\usepackage{tcolorbox}
18	\tcbuselibrary{listings,breakable}
19	
20	\hypersetup{pdfauthor={},pdftitle={}}
21	
22	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{abstract}
30	\input{introduction}
31	\input{method}
32	\input{experiments}
33	\input{related_work}
34	\input{discussion}
35	\input{conclusion}
36	
37	\section*{Limitations}
38	
39	\paragraph{Environmental scope.}
40	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct), though extended validation of representative excluded tasks confirms the pattern (Appendix~\ref{app:extended-validation}). The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface non-death-dominated signal that our current setup does not capture. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:cross-env}, \S\ref{sec:discussion}) provide preliminary supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct cross-model replication (11 task types, $N{=}220$; \S\ref{sec:cross-model}) shows death dominance replicates with direction consistency 10/10 while vulnerability magnitude varies ($+30.0$~pp vs.\ Qwen $+26.5$~pp), though both models are in the 7--8B parameter range; Qwen2.5-72B ($10{\times}$ scale) re
…[truncated 8431 chars]

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

_source line 2504 · 2026-05-23T03:41:35.348536+00:00_

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

_source line 2505 · 2026-05-23T03:41:35.499541+00:00_

1	\begin{abstract}
2	LLM agent routing (deciding when to rely on internal reasoning versus external tool use) is typically addressed by training routers directly, without first understanding what mechanistic signal drives the routing preference. This absence of diagnostic methods risks building routers atop confounded or trivial signal. We propose an episode-level counterfactual framework that compares pure-strategy outcomes (internal-only vs.\ deterministic-only) to decompose routing signal into its mechanistic components before any router is constructed. Applying this framework to ScienceWorld (11 task types, 245 episodes), we find that 78.9\% of non-tie episode-level routing labels arise from death asymmetry---a finding replicated across three architecturally distinct 7--9B model families, revealing that in catastrophic-failure environments, signal diversity can collapse to a single dominant mechanism. Cross-environment probes on MATH and ALFWorld diagnose qualitatively different routing mechanisms (no extractable signal and information asymmetry, respectively), providing preliminary evidence of applicability beyond death-dominated settings. The framework distinguishes \emph{methodological generality} (applicable to any environment with paired episode outcomes) from \emph{empirical generality} (full quantitative validation on ScienceWorld only). A ${\sim}$50-episode pilot suffices for build-vs-buy decisions given large effect sizes ($d = 3.02$).
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2506 · 2026-05-23T03:41:35.550128+00:00_

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

_source line 2507 · 2026-05-23T03:41:35.600783+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	In ScienceWorld \citep{scienceworld-2022}, a text-based science simulation, internal reasoning is error-prone, as the model may hallucinate state changes (e.g., that water has boiled when the stove was never activated), while deterministic external computation eliminates such errors via exact state transitions. The practical question: \emph{when should an agent route computation externally versus internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision: Toolformer \citep{toolformer-2023} inserts API calls by perplexity reduction; ART \citep{art-2023} decomposes tasks into tool-augmented programs; Chameleon \citep{chameleon-2023} selects heterogeneous modules per subtask; adaptive-computation methods route to different reasoning depths \citep{cogrouter-2026,ares-2026}, model tiers \citep{mtrouter-2026}, or episode-level model selection under sparse rewards \citep{budget-aware-routing-2026}; concurrent analyses further presuppose diverse routing signals~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026}. These approaches, which operate in non-catastrophic settings, share the assumption that routing signal stems from diverse sources and a learned router can exploit it---an assumption that remains untested: no prior work has systematically decomposed what drives routing preferences in interactive environments.
7	
8	We propose a \emph{diagnostic framework} comprising (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95), a penalty-independen
…[truncated 2187 chars]

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

_source line 2508 · 2026-05-23T03:41:49.134873+00:00_

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

_source line 2509 · 2026-05-23T03:41:49.887712+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/pipeline_overview.pdf}
7	\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\ref{alg:labeling}.}
8	\label{fig:pipeline}
9	\end{figure}
10	
11	Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically (Appendix~\ref{app:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
12	
13	\subsection{Problem Setup}
14	\label{sec:problem-setup}
15	
16	Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\citep{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic} (${\tt det}$), a privileged-information strategy that eliminates observation uncertainty---instantiated as oracle simulator (ScienceWorld), code interpreter (MATH), or admissible-action enumeration (ALFWorld); these qualitative differences affect what routing signals the framework can detect. A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \math
…[truncated 7474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 752
}
```

</details>

---


### Tool call

_source line 2510 · 2026-05-23T03:41:49.988679+00:00_

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

_source line 2511 · 2026-05-23T03:41:50.390729+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types (63\%) lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). Taxonomically redundant tasks share identical action vocabularies, reward functions, and environmental dynamics, differing only in target entity; we retain one representative per family (Appendix~\ref{app:per-task}). This scope limits generalizability: conclusions apply to the included subset; increasing the 30-step budget might surface signal in excluded types (see Limitations). An anti-cherry-picking analysis confirms that death dominance holds in 18 of these 19 types, with a mean $\Delta\text{DR} = +38.2$\,pp exceeding the included tasks' $+28.7$\,pp (Appendix~\ref{app:per-task}). Extended validation at $n{=}20$ on five representative excluded tasks confirms this direction ($\overline{\Delta\text{DR}} = +32.0$\,pp; Appendix~\ref{app:extended-validation}). A reasoning-depth ablation ($n{=}120$) found no significant difference between internal strategy variants ($p > 0.26$; Appendix~\ref{app:ablations}). Prescreening used $n{=}5$ episodes per task type; directional consistency (18/19 types favoring deterministic) rather than point estimates drives the inclusion criterion.
5	
6	\subsection{Death Avoidance Decomposition}
7	\label{sec:death-decomp}
8	
9	
10	Of the 95 non-tie routing labels, 75 (78.9\%) arise from death asymmetry: the internal strategy triggers a catastrophic $-100$ penalty while the deterministic strategy survives. This penalty-independent label fraction is the primary diagnostic metric. Of these, 54 are sole-signal labels where death was the only discriminator; at $P{=}0$ these reduce to ties, but the labeling function itself is penalty-independent (Algorithm~\ref{alg:labeling}).
11	
12	Of 245 episodes, 150 (61.2\%) show no preference between strategies; routing is relevant in the r
…[truncated 14719 chars]

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

_source line 2512 · 2026-05-23T03:41:50.541685+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "review_issues.yaml",
  "max_chars": "12000"
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
    "file": "review_issues.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 2513 · 2026-05-23T03:41:50.592452+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

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

_source line 2514 · 2026-05-23T03:42:00.551312+00:00_

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

_source line 2515 · 2026-05-23T03:42:01.053248+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}, spanning several functional categories.
5	Self-supervised methods learn tool invocation from loss signals \citep{toolformer-2023,toolace-2025}, token-level methods embed tools in the vocabulary \citep{toolkengpt-2023}, task-level decomposition routes subtasks to specialized modules \citep{art-2023,chameleon-2023}, and RL-based methods learn routing from reward \citep{retool-2025}.
6	All focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
7	Concurrent work examines \emph{when} to invoke tools: tool-call decisions correlate with uncertainty~\citep{tool-overuse-illusion-2026}, are encoded in hidden states~\citep{when2tool-2026}, impose a ``tool-use tax''~\citep{tool-use-tax-2026}, or follow necessity-utility-affordability logic~\citep{to-call-or-not-2026}. Our decomposition yields a concrete answer: 78.9\% of non-tie routing labels trace to catastrophic-failure prevention.
8	
9	\paragraph{Adaptive Computation and Routing.}
10	Adaptive routing traces back to learned halting policies \citep{graves2016act}. Mixture-of-Recursions \citep{mixture-of-recursions-2025} learns token-level recursion depths in the LLM era; concurrent work further diversifies routing granularity: CogRouter \citep{cogrouter-2026} adapts per-step depth, ARES \citep{ares-2026} selects effort levels, and MTRouter \citep{mtrouter-2026} addresses multi-turn settings; in death-dominated environments, the task-type-level binary signal is structurally inaccessible to these step-level approaches (\S\ref{sec:router-diagnostic}).
11	RouteLLM \citep{routellm-2024} learns routers from preference data to select between strong and weak models; cost-optimization routing (FrugalGPT~\citep{frugalgpt-2023}; AutoMix~\citep{automix-2024}) cascades queries across model tiers.
…[truncated 2817 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 2516 · 2026-05-23T03:42:01.053709+00:00_

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

_source line 2517 · 2026-05-23T03:42:01.961048+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Signal granularity and router failure.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property (10/11 types carry death risk), but step-level features correlate weakly because death risk depends on multi-step trajectories. Six router variants (0.6B--4B, classification and generative) converge on near-chance step-level accuracy ($56$--$59\%$); this convergent failure is consistent with signal limitation; however, extreme class imbalance (90.5\% deterministic-preferred, only 9 internal-preferred episodes) makes a data-limited explanation equally plausible---distinguishing the two requires ${\sim}$1{,}350 paired episodes to obtain 50 minority-class samples. Cross-task-type transfer yields chance accuracy (49.2\%; Appendix~\ref{app:ablations}). A train--deploy distribution shift~\citep{dagger-2011} may also contribute to the negative result.
6	
7	\paragraph{Non-triviality and oracle confound.}
8	While death dominance follows from the penalty structure (\S\ref{sec:daf}), two consequences were not predictable a priori: $10{\times}$ scaling to 72B fails to eliminate it (DAF${}= 92.4\%$), and Reflexion yields DAF${}>100\%$. All four interventions leave ${\geq}12$~pp residual gaps (Appendix~\ref{sec:threshold-routing}); cross-model DR stability ($36$--$43\%$) confirms death vulnerability is a task-environment property. An oracle confound (``is the signal merely use the oracle?'') is addressed by two observations: $\Delta_{\text{nd}} = 2.84$ (9.6\% of total gap)---internal reasoning provides almost no non-death advantage---and action-space filtering (Appendix~\ref{app:grounding-ablation}) reduces death rate by 19~pp while remaining far above deterministic safety.
9	
10	\paragraph{Practical implications and actionability.}
11	The penalty-invariant label fraction (78.9\%) is the primary diagnostic; DAF varies with $P$ (Appendix~\re
…[truncated 671 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 2518 · 2026-05-23T03:42:01.961553+00:00_

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

_source line 2519 · 2026-05-23T03:42:02.163882+00:00_

1	\section{Conclusion}
2	
3	Our episode-level counterfactual framework reveals that 78.9\% of non-tie routing labels in ScienceWorld stem from death avoidance---replicated across three model families, persistent under $10{\times}$ scaling, and transferable to qualitatively different environments. Future work should validate this in additional catastrophic-failure settings and investigate lightweight death-prediction mechanisms that exploit task-type-level binary structure without full step-level router training.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 2520 · 2026-05-23T03:42:02.164464+00:00_

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

_source line 2521 · 2026-05-23T03:42:02.216459+00:00_

1	# Round 29 Review Issues (fresh review, 2026-05-22)
2	# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作)
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
70	  category: format
71	  severity: info
72	  status: resolved
73	  first_raised_r
…[truncated 22680 chars]

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

_source line 2522 · 2026-05-23T03:42:28.429713+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
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

_source line 2523 · 2026-05-23T03:42:28.480675+00:00_



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

_source line 2524 · 2026-05-23T03:42:32.495582+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR"
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
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool result

_source line 2525 · 2026-05-23T03:42:39.730270+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 regarding the ARR process:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Submission Process through ARR

Papers must be submitted by the ARR 2026 May cycle, and papers that have received reviews and a meta-review from ARR may be committed t
…[truncated 902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 7234
}
```

</details>

---


### Tool call

_source line 2526 · 2026-05-23T03:42:43.864882+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit long paper short paper guidelines"
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
    "query": "ACL Rolling Review 2026 submission format page limit long paper short paper guidelines"
  }
}
```

</details>

---


### Tool result

_source line 2527 · 2026-05-23T03:42:50.148636+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit long paper short paper guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here is the information about ACL Rolling Review 2026 submission format guidelines:

## Paper Types and Page Limits

ACL Rolling Review (ARR) invites the submission of long and short papers on substantial, original, and unpublished research in all aspects of Computational Linguistics and Natural Language Processing.

### Long Papers
Review versions of 
…[truncated 1186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 6283
}
```

</details>

---


### Tool call

_source line 2528 · 2026-05-23T03:43:37.813168+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n### Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **Deadline**: 2026-05-25 (ARR submission)\n- **类型**: Long paper, 正文严格 8 页限制，references 无限，Limitations 和 Ethics 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind (`\\author{Anonymous}`)\n- **评分标准**: Overall Assessment 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`（入口文件，通过 `\\input{}` 引入各章节）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_30/submitted.pdf`\n- 各章节 .tex 文件在 `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/` 目录下：abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, discussion.tex, conclusion.tex\n- Appendices 在 main.tex 中（A-U 共 21 个 appendix sections）\n\n### 你的审查侧重：方法严谨性 + 实验设计 + 统计有效性\n\n请重点审查：\n\n1. **方法论严谨性**\n   - Episode-level counterfactual labeling 的设计是否合理？Algorithm 1 的 death-priority rule 是否引入 bias？\n   - DAF 指标定义是否 sound？DAF 对 penalty P 的单调依赖是否被充分讨论？\n   - 78.9% label fraction vs DAF=90.4% 的关系是否清晰？哪个是 primary metric？\n   - Pure-strategy comparison 的因果推断逻辑是否 valid？是否存在未讨论的 confound？\n\n2. **实验设计**\n   - 11/30 task types 的 prescreening 是否引入 selection bias？排除标准是否合理？\n   - N=245 episodes 的 sample size 是否足够？statistical power 如何？\n   - Cross-model validation (3 families, 7-9B) 的设计是否 convincing？72B scaling 是否 sufficient？\n   - Agent improvement baselines (Retry, Reflexion) 的设计是否公平？对照组设置是否合理？\n   - Cross-environment probes (MATH, ALFWorld) 的设计是否能支撑 generalization claims？\n   - Router training diagnostic 的实验设计是否完整？negative result 的解释是否 fair？\n\n3. **统计推断**\n   - Bootstrap CI 的计算是否正确？episode-level resampling 的合理性？\n   - Cluster bootstrap (K=11) 的可靠性？K<20 的问题是否被充分 caveat？\n   - Cohen's d = 3.02 的解读是否需要额外 context？\n   - Per-task analysis 的 statistical power (n=20) 是否足够？\n\n4. **格式合规**\n   - 正文是否严格在 8 页以内（Sections 1-6）？如果超出，标注为 CRITICAL\n   - 是否符合 ACL 模板要求？\n\n### 输出格式\n\n请按以下结构输出完整审稿意见（必须包含所有 section）：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n...\n\n## Weaknesses\nW1. [severity: critical/warning/info] ...\nW2. ...\n...\n\n## Questions\nQ1. ...\n...\n\n## Missing References\n（如有遗漏的重要相关工作）\n\n## Scores\n- Soundness: X/5\n- Excitement: X/5\n- Overall: X (使用 EMNLP 2026 评分标准)\n- Confidence: X/5\n\n## Detailed Comments\n（逐节详细意见）\n```\n\n**请直接输出完整审稿意见，不要只说\"已读完\"。**"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n### Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **Deadline**: 2026-05-25 (ARR submission)\n- **类型**: Long paper, 正文严格 8 页限制，references 无限，Limitations 和 Ethics 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind (`\\author{Anonymous}`)\n- **评分标准**: Overall Assessment 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`（入口文件，通过 `\\input{}` 引入各章节）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_30/submitted.pdf`\n- 各章节 .tex 文件在 `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/` 目录下：abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, discussion.tex, conclusion.tex\n- Appendices 在 main.tex 中（A-U 共 21 个 appendix sections）\n\n### 你的审查侧重：方法严谨性 + 实验设计 + 统计有效性\n\n请重点审查：\n\n1. **方法论严谨性**\n   - Episode-level counterfactual labeling 的设计是否合理？Algorithm 1 的 death-priority rule 是否引入 bias？\n   - DAF 指标定义是否 sound？DAF 对 penalty P 的单调依赖是否被充分讨论？\n   - 78.9% label fraction vs DAF=90.4% 的关系是否清晰？哪个是 primary metric？\n   - Pure-strategy comparison 的因果推断逻辑是否 valid？是否存在未讨论的 confound？\n\n2. **实验设计**\n   - 11/30 task types 的 prescreening 是否引入 selection bias？排除标准是否合理？\n   - N=245 episodes 的 sample size 是否足够？statistical power 如何？\n   - Cross-model validation (3 families, 7-9B) 的设计是否 convincing？72B scaling 是否 sufficient？\n   - Agent improvement baselines (Retry, Reflexion) 的设计是否公平？对照组设置是否合理？\n   - Cross-environment probes (MATH, ALFWorld) 的设计是否能支撑 generalization claims？\n   - Router training diagnostic 的实验设计是否完整？negative result 的解释是否 fair？\n\n3. **统计推断**\n   - Bootstrap CI 的计算是否正确？episode-level resampling 的合理性？\n   - Cluster bootstrap (K=11) 的可靠性？K<20 的问题是否被充分 caveat？\n   - Cohen's d = 3.02 的解读是否需要额外 context？\n   - Per-task analysis 的 statistical power (n=20) 是否足够？\n\n4. **格式合规**\n   - 正文是否严格在 8 页以内（Sections 1-6）？如果超出，标注为 CRITICAL\n   - 是否符合 ACL 模板要求？\n\n### 输出格式\n\n请按以下结构输出完整审稿意见（必须包含所有 section）：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n...\n\n## Weaknesses\nW1. [severity: critical/warning/info] ...\nW2. ...\n...\n\n## Questions\nQ1. ...\n...\n\n## Missing References\n（如有遗漏的重要相关工作）\n\n## Scores\n- Soundness: X/5\n- Excitement: X/5\n- Overall: X (使用 EMNLP 2026 评分标准)\n- Confidence: X/5\n\n## Detailed Comments\n（逐节详细意见）\n```\n\n**请直接输出完整审稿意见，不要只说\"已读完\"。**"
  }
}
````

</details>

---


### Tool result

_source line 2529 · 2026-05-23T03:43:56.432595+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18619
}
```

</details>

---


### Tool call

_source line 2530 · 2026-05-23T03:43:56.583659+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n### Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **Deadline**: 2026-05-25 (ARR submission)\n- **类型**: Long paper, 正文严格 8 页限制，references 无限，Limitations 和 Ethics 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind (`\\author{Anonymous}`)\n- **评分标准**: Overall Assessment 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`（入口文件，通过 `\\input{}` 引入各章节）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_30/submitted.pdf`\n- 各章节 .tex 文件在 `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/` 目录下：abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, discussion.tex, conclusion.tex\n- Appendices 在 main.tex 中（A-U 共 21 个 appendix sections）\n\n### 你的审查侧重：新颖性 + 完整性 + 写作质量 + Related Work\n\n请重点审查：\n\n1. **新颖性与贡献**\n   - 核心发现（78.9% death asymmetry）的 novelty 如何？是否 \"obvious in hindsight\"？\n   - Counterfactual diagnostic framework 作为方法论贡献的价值如何？\n   - 论文的 framing 是否清晰区分了 methodological generality 和 empirical generality？\n   - 对 routing/tool-use 社区的实际影响和 actionability 如何？\n   - 与 existing routing literature 的差异化 positioning 是否 convincing？\n\n2. **完整性**\n   - 论文是否充分讨论了 limitations？是否有重要的未讨论的限制？\n   - Cross-environment validation 是否足以支撑论文的 claims？覆盖范围是否足够？\n   - 是否有缺失的 ablation studies 或 analysis？\n   - Non-death component (21.1% of labels) 的来源是否被充分分析？\n\n3. **写作质量**\n   - Abstract 是否清晰传达核心贡献？是否有数字堆砌？\n   - Introduction 的 motivation 和 contributions 陈述是否 clear and compelling？\n   - 正文的叙事流是否连贯？各 section 之间的逻辑连接是否顺畅？\n   - 术语使用是否一致？（如 \"computation mode\", \"deterministic\", \"death\" 等关键概念）\n   - Conclusion 是否简洁有力？是否与 Introduction 重复过多？\n\n4. **Related Work**\n   - 相关工作覆盖是否全面？是否遗漏了重要的相关论文？\n   - 特别关注：tool use routing, adaptive computation, safe RL, counterfactual evaluation, LLM agent 领域\n   - 与 concurrent work (2026 papers) 的 positioning 是否 fair and accurate？\n   - 是否缺少 non-agent adaptive computation 方向的讨论（如 early exit, speculative decoding, MoD）？\n\n5. **格式与排版**\n   - 正文是否严格在 8 页以内？如果超出，标注为 CRITICAL\n   - Figure/Table 的使用是否有效？caption 是否 informative？\n   - 引用格式是否统一？是否有 orphan bib entries？\n\n### 输出格式\n\n请按以下结构输出完整审稿意见（必须包含所有 section）：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n...\n\n## Weaknesses\nW1. [severity: critical/warning/info] ...\nW2. ...\n...\n\n## Questions\nQ1. ...\n...\n\n## Missing References\n（如有遗漏的重要相关工作）\n\n## Scores\n- Soundness: X/5\n- Excitement: X/5\n- Overall: X (使用 EMNLP 2026 评分标准)\n- Confidence: X/5\n\n## Detailed Comments\n（逐节详细意见）\n```\n\n**请直接输出完整审稿意见，不要只说\"已读完\"。**"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n### Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **Deadline**: 2026-05-25 (ARR submission)\n- **类型**: Long paper, 正文严格 8 页限制，references 无限，Limitations 和 Ethics 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind (`\\author{Anonymous}`)\n- **评分标准**: Overall Assessment 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`（入口文件，通过 `\\input{}` 引入各章节）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_30/submitted.pdf`\n- 各章节 .tex 文件在 `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/` 目录下：abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, discussion.tex, conclusion.tex\n- Appendices 在 main.tex 中（A-U 共 21 个 appendix sections）\n\n### 你的审查侧重：新颖性 + 完整性 + 写作质量 + Related Work\n\n请重点审查：\n\n1. **新颖性与贡献**\n   - 核心发现（78.9% death asymmetry）的 novelty 如何？是否 \"obvious in hindsight\"？\n   - Counterfactual diagnostic framework 作为方法论贡献的价值如何？\n   - 论文的 framing 是否清晰区分了 methodological generality 和 empirical generality？\n   - 对 routing/tool-use 社区的实际影响和 actionability 如何？\n   - 与 existing routing literature 的差异化 positioning 是否 convincing？\n\n2. **完整性**\n   - 论文是否充分讨论了 limitations？是否有重要的未讨论的限制？\n   - Cross-environment validation 是否足以支撑论文的 claims？覆盖范围是否足够？\n   - 是否有缺失的 ablation studies 或 analysis？\n   - Non-death component (21.1% of labels) 的来源是否被充分分析？\n\n3. **写作质量**\n   - Abstract 是否清晰传达核心贡献？是否有数字堆砌？\n   - Introduction 的 motivation 和 contributions 陈述是否 clear and compelling？\n   - 正文的叙事流是否连贯？各 section 之间的逻辑连接是否顺畅？\n   - 术语使用是否一致？（如 \"computation mode\", \"deterministic\", \"death\" 等关键概念）\n   - Conclusion 是否简洁有力？是否与 Introduction 重复过多？\n\n4. **Related Work**\n   - 相关工作覆盖是否全面？是否遗漏了重要的相关论文？\n   - 特别关注：tool use routing, adaptive computation, safe RL, counterfactual evaluation, LLM agent 领域\n   - 与 concurrent work (2026 papers) 的 positioning 是否 fair and accurate？\n   - 是否缺少 non-agent adaptive computation 方向的讨论（如 early exit, speculative decoding, MoD）？\n\n5. **格式与排版**\n   - 正文是否严格在 8 页以内？如果超出，标注为 CRITICAL\n   - Figure/Table 的使用是否有效？caption 是否 informative？\n   - 引用格式是否统一？是否有 orphan bib entries？\n\n### 输出格式\n\n请按以下结构输出完整审稿意见（必须包含所有 section）：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n...\n\n## Weaknesses\nW1. [severity: critical/warning/info] ...\nW2. ...\n...\n\n## Questions\nQ1. ...\n...\n\n## Missing References\n（如有遗漏的重要相关工作）\n\n## Scores\n- Soundness: X/5\n- Excitement: X/5\n- Overall: X (使用 EMNLP 2026 评分标准)\n- Confidence: X/5\n\n## Detailed Comments\n（逐节详细意见）\n```\n\n**请直接输出完整审稿意见，不要只说\"已读完\"。**"
  }
}
````

</details>

---


### Tool result

_source line 2531 · 2026-05-23T03:43:58.308263+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1724
}
```

</details>

---


### Tool call

_source line 2532 · 2026-05-23T03:43:58.308768+00:00_

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

_source line 2533 · 2026-05-23T03:43:59.368139+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "simgate-modular-routing",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_30/submitted.pdf",
  "venue": "EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "simgate-modular-routing",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_30/submitted.pdf",
    "venue": "EMNLP 2026"
  }
}
```

</details>

---


### Tool result

_source line 2534 · 2026-05-23T03:44:01.061645+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 2752
}
```

</details>

---


### Tool result

_source line 2535 · 2026-05-23T03:44:01.814715+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 2446
}
```

</details>

---


### Assistant

_source line 2536 · 2026-05-23T03:44:12.427331+00:00_

Round 30 圆桌审稿已启动，所有任务并行派发完毕：

| 任务 | 状态 |
|------|------|
| **Reviewer 1**（方法严谨性 + 实验设计 + 统计） | ✅ 已派发，等待返回 |
| **Reviewer 2**（新颖性 + 完整性 + 写作 + Related Work） | ✅ 已派发，等待返回 |
| **视觉审查 Agent** | ✅ 已启动，与 Reviewer 并行 |
| **外部审稿（Stanford Agentic Reviewer）** | ✅ 已请求，8h 后自动提醒 |

**Venue 确认**：EMNLP 2026 via ARR May 2026 cycle，deadline 5月25日。Long paper 8页正文 + unlimited references，Limitations/Ethics 不计入页数。ACL 模板，double-blind。本轮 ARR May cycle 与 AACL 共享，需在提交时声明目标会议（binding）。

等待两位 Reviewer 返回初审意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 207

## Round 207

2 recorded events


### User

_source line 2537 · 2026-05-23T03:49:08.192525+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 完整审稿意见

**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**Venue**: EMNLP 2026 via ACL Rolling Review

---

## Summary

本文提出一个 episode-level counterfactual diagnostic framework，用于在构建路由器之前分析 LLM agent 路由信号的机制组成。在 ScienceWorld 环境中（11 个任务类型，245 个 episode），作者发现 78.9% 的非平局路由标签来源于"死亡不对称"——内部推理策略触发灾难性失败（-100 惩罚），而确定性策略存活。该发现在三个 7-9B 模型族中复现（DAF 88-90%），并通过 MATH（无路由信号）和 ALFWorld（信息不对称）进行了跨环境探测。Step-level router 训练实验得到接近随机的结果，证实信号是 task-type-level 的二元属性。

---

## Strengths

**S1. 方法论贡献有价值。** "先诊断再构建"的思路在 routing 文献中是一个有意义的缺口填补。大多数 routing 工作直接训练 router 而不分析底层信号组成，本文的 counterfactual decomposition framework 提供了一个系统化的诊断工具（Section 2）。

**S2. 统计分析异常严谨。** 论文在统计方法上投入了大量精力：episode-level bootstrap（B=10,000）、cluster-robust inference（K=11）、wild cluster bootstrap、leave-one-task-out sensitivity、Cohen's d = 3.02。对小样本聚类推断的局限性（K < 20-50 阈值）有诚实的披露（Section 3.1, Appendix E）。这种统计自觉性在 NLP 论文中罕见。

**S3. 跨模型复现令人信服。** 三个架构不同的模型族（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B-it）在 DAF 上收敛于 88-90%（spread 仅 2.2pp），且 10× scaling 到 72B 未消除 death dominance（DAF = 92.4%）。这排除了 model-specific 的解释（Section 3.2, Table in Appendix M）。

**S4. 自我批判性极强。** Limitations 部分（约 1.5 页）极其详尽，主动讨论了环境范围、方法论约束、统计局限、纯策略上界和诊断范围。论文反复区分"方法论通用性"与"经验通用性"，不过度宣称。Section 2.4 中 DAF 随 P 单调递增是"数学后果而非经验发现"的声明体现了罕见的学术诚实。

**S5. 负面结果的诊断价值。** Router 训练的负面结果（Section 3.6）被转化为诊断性发现：step-level signal 不存在不是因为 router 架构不足，而是因为 death avoidance 是 task-type-level 的二元信号，结构上不可被 step-level features 捕获。Leave-one-task-type-out 降至 chance（49.2%）提供了决定性证据。

**S6. Anti-cherry-picking 论证充分。** 排除的 19 个任务类型的 death asymmetry（ΔDR = +38.2pp）高于包含的 11 个（+28.7pp），排除了选择性报告的嫌疑（Appendix C, Table 2 in appendix）。

---

## Weaknesses

**W1. [critical] 核心发现的新颖性存疑——"death dominates in death-penalty environments" 在一定程度上是同义反复。**

- 具体位置：Section 2.4, Equation (4)
- 问题：DAF 的数学结构 δP/(δP + Δ_nd) 表明，只要 P 足够大且 δ > 0，DAF 就会趋近于 1——这是代数必然性，不是经验发现。论文自己承认这一点（"a mathematical consequence rather than an empirical finding"）。核心问题是：当环境有 catastrophic failure（-100 penalty）而两种策略的死亡率不同时，死亡必然主导得分差异——这在 P=100 的设定下近乎不言自明。论文试图通过两个"非显然"的发现来挽救新颖性：(a) 10× scaling 未消除 death dominance；(b) Reflexion 使 DAF > 100%。但 (a) 只是说 72B 仍然比 oracle simulator 更容易犯致命错误——这并不令人意外，因为 deterministic 策略拥有 ground-truth state access 的特权；(b) DAF > 100% 是数学构造的后果（Δ_nd < 0 时自动成立），不构成独立发现。
- 真正有新颖性的是 **penalty-invariant label fraction (78.9%)**——但论文的标题、framing 和叙事重心都放在了 DAF 上，而非 label fraction。
- 建议：重构叙事，将 label fraction 而非 DAF 作为主要指标。更重要的是，需要论证为什么 78.9% 这个数字本身是非显然的——而不仅仅是"大"。

**W2. [critical] "Deterministic" 策略的特权性质严重限制了发现的通用性。**

- 具体位置：Section 2.1, Section 3.4
- 问题：ScienceWorld 中的 "deterministic" 策略是一个 **oracle simulator with ground-truth state access**——它可以 fork 模拟器来评估候选动作。这不是实际系统中可用的工具调用，而是一个 privileged information baseline。死亡率差异（42.9% vs. 16.3%）在很大程度上可以归因于信息不对称（一个策略可以"预见"动作后果，另一个不能），而非内在的 "routing signal" 属性。ALFWorld 的分析实际上证实了这一点——论文自己诊断 ALFWorld 的信号为 "information asymmetry"（Section 3.4）。ScienceWorld 的信号是否同样主要是 information asymmetry（表现为 death avoidance）？论文没有充分区分 "death avoidance" 和 "information privilege"。
- 为什么影响接收：如果 death avoidance 主要是 oracle privilege 的后果，那么 "routing signal is death-dominated" 的结论就变成了 "给了特权信息当然更不容易死"——这降低了论文对 routing 社区的实际指导意义。
- 建议：明确讨论 deterministic 策略的信息特权与 death avoidance 之间的关系。考虑测试一个 non-privileged 的外部工具（如 RAG-augmented strategy）来分离信息特权效应。

**W3. [critical] 环境覆盖过窄，跨环境 "probes" 无法支撑通用性主张。**

- 具体位置：Section 3.4, Abstract, Introduction
- 问题：MATH 的结果是 "no routing signal"（几乎无差异），ALFWorld 的结果是 "information asymmetry, not death"——两者都没有复现核心发现（death dominance）。论文号称提供 "preliminary evidence of applicability beyond death-dominated settings"，但实际上两个探测性环境都没有验证 framework 能在另一个 death-dominant 环境中诊断出 death dominance。要证明 framework 的通用性，需要至少一个 **不同于 ScienceWorld 的 catastrophic-failure 环境**（如 NetHack, Crafter, BabyAI with death mechanics）来展示 framework 的可复现性。
- 为什么影响接收：Abstract 和 Introduction 的 framing 暗示了比实际证据更强的通用性。"applicable to any environment with paired episode outcomes" 是方法论声明，但读者会期望至少一个确认性案例。
- 建议：(a) 降低通用性 claim 的措辞强度；(b) 或者增加一个有 death mechanics 的不同环境的验证。

**W4. [warning] Non-death component (21.1% of labels) 分析不足。**

- 具体位置：Section 3.1, Appendix U
- 问题：20 个 non-death routing labels 中有 16 个 deterministic-preferred、4 个 internal-preferred。这些 label 的来源是什么？是 score-comparison labels（两者都存活但得分不同）。Appendix U 的 case study 仅分析了一个任务类型（find-non-living-thing）下的 Gemma-2 数据，且是定性的。论文未系统分析这 20 个 label 的分布特征、与任务属性的关系、以及它们是否也受 information asymmetry 驱动。
- 建议：对全部 20 个 non-death labels 进行系统分析——它们分布在哪些任务类型？score 差异的来源是什么（hallucination vs. suboptimal action selection vs. random variance）？

**W5. [warning] Abstract 数字过密，可读性差。**

- 具体位置：Abstract
- 问题：Abstract 在 ~200 词内包含了以下数字：78.9%, 90.4%, 81.1%, 99.0%, 97.4%, 50, 3.02——共 7 个统计量。这对首次阅读的 reviewer 造成认知负担。"d = 3.02" 出现在 abstract 中尤其突兀——Cohen's d 通常不在 abstract 报告。
- 建议：精简到 2-3 个关键数字（78.9% label fraction, 跨模型复现范围, 以及一个 cross-environment 对比数字）。将 95% CI 和 Cohen's d 移至正文。

**W6. [warning] Discussion 和 Conclusion 与 Introduction 存在显著重复。**

- 具体位置：Section 1 (para 3-4), Section 5, Section 6
- 问题：78.9% 的核心发现在论文中被重复了至少 7 次（Abstract, Introduction para 3, Introduction contributions, Section 3.1, Discussion, Conclusion, Related Work）。Conclusion（仅 3 句话）几乎完全重复了 Introduction 的 contributions 列表。Discussion 的前两段也大量重复了 Experiments 的内容。
- 建议：Conclusion 应该提供更多前瞻性内容（future directions 的具体路径），而非重述发现。Discussion 应更侧重 implications 而非重述结果。

**W7. [warning] 单一失败模式（focus on）削弱了 "death avoidance" 概念的一般性。**

- 具体位置：Appendix N
- 问题：所有 105 个 internal-strategy deaths（100%）都由同一个动作模式触发：`focus on [object]`。这意味着 ScienceWorld 中的 "death avoidance" 实质上是 "避免误用一个特定的提交答案动作"——一个非常具体的 grounding failure，而非一般意义上的 catastrophic failure avoidance。Grounding ablation（Appendix O）通过简单的 action-space filtering 就将死亡率降低了 19pp。如果一个简单的黑名单就能部分解决问题，那么 "death avoidance dominates routing signal" 的叙事就变成了 "一个可修复的 grounding bug 主导了路由信号"。
- 建议：在正文中明确讨论这一点（目前只在 Appendix N），并考虑在 action-filtering 后重新计算 DAF——如果 filtering 后 death dominance 显著下降，这实际上是一个更有趣的发现。

**W8. [warning] 术语 "deterministic" 可能产生误导。**

- 具体位置：Section 2.1
- 问题：在标准 CS 术语中，"deterministic" 意味着"给定相同输入产生相同输出"。但论文中的 "deterministic strategy" 实际上是一个 oracle simulator forking strategy——它的 "deterministic" 性质来自于可以用模拟器精确评估候选动作。在 MATH 中它是 code interpreter，在 ALFWorld 中是 admissible-action enumeration。三个环境中 "deterministic" 的含义完全不同。论文在 Section 2.1 有简短说明，但 Table 3 的 caption 和 Figure 3 仍可能造成混淆。
- 建议：考虑使用 "privileged" 或 "oracle-assisted" 替代 "deterministic"，或在首次定义时更明确地说明这是一个 umbrella term。

**W9. [info] 部分 2026 concurrent work 引用需读者自行验证。**

- 具体位置：Section 1, Section 4
- 问题：论文引用了多篇 2026 年 concurrent work（cogrouter-2026, ares-2026, mtrouter-2026, budget-aware-routing-2026, when2tool-2026, tool-use-tax-2026, to-call-or-not-2026, axis-2026, cso-2026, salt-2026）。这些引用的存在性和准确性无法在审稿过程中完全验证。
- 建议：确保所有 2026 引用有公开可访问的预印本链接（arXiv 或类似平台）。

---

## Questions

**Q1.** 如果将 ScienceWorld 的 death penalty 设为 P=0（即死亡仅意味着 episode 失败，得分为 0 而非 -100），label fraction 是否会发生变化？论文声称 label fraction 是 penalty-invariant 的（因为 Algorithm 1 的 death-priority rule 不依赖 P 的具体值），但如果 P=0，死亡 episode 的得分就是 0 而非 -100，此时 "both-alive score comparison" 可能产生不同的 label 分布。请澄清。

**Q2.** 论文报告 97.4% 的 step-level tie rate（Section 2.2），但这是在 ScienceWorld sparse-reward 环境中。如果环境提供 dense intermediate rewards（如 Crafter, Minecraft），framework 是否仍然需要 episode-level 比较？论文的方法论似乎隐含假设了 sparse rewards。

**Q3.** Gemma-2-9B-it 的跨模型验证（Section 3.2）报告 DAF = 89.7%，但排除 find-non-living-thing 后 DAF = 99.9% [99.7, 100.0]——这个巨大的跳跃是否意味着 DAF 对单个 zero-death 任务极度敏感？如果 Gemma-2 数据中恰好有两个 zero-death 任务，DAF 会如何变化？

**Q4.** 论文使用 T_max = 30 steps，并承认 19 个排除的任务类型"因为两种策略通常在 30 步内超时"而缺乏路由信号（Limitations）。如果增加步数预算（如 T_max = 100），是否可能在这些任务中发现 non-death-dominated signal？这是否是该 framework 的一个结构性盲点？

**Q5.** Section 3.6 报告 task-type-only classifier（logistic regression on one-hot task identity）达到 64.7% balanced accuracy。这是否意味着如果 deployment 时知道 task type，一个简单的 lookup table 就足以替代任何 learned router？论文对此的 practical implication 是什么？

---

## Missing References

1. **Hallucination detection/mitigation 文献缺失。** 论文的核心发现是 internal reasoning 的 hallucination 导致 catastrophic failure，但 Related Work 完全没有讨论 LLM hallucination detection 和 mitigation 的大量文献（如 Manakul et al., 2023 "SelfCheckGPT"; Mundler et al., 2024 "Self-contradictory hallucinations"；Ji et al., 2023 survey）。连接这一文献有助于 contextualize death avoidance 作为 hallucination failure mode 的一个特例。

2. **Non-agent adaptive computation 讨论过于简略。** Mixture-of-Depths (Raposo et al., 2024) 和 speculative decoding (Leviathan et al., 2023) 各仅被引用一次。Early exit networks（如 DeeBERT, PABEE）、dynamic neural networks survey (Han et al., 2021) 完全缺失。论文应更明确地将自己定位在 adaptive computation 的谱系中。

3. **环境设计与 reward shaping 文献。** 论文发现 death penalty 的大小直接影响 DAF（Appendix K），这与 reward shaping 文献（Ng et al., 1999——已引用；Eschmann et al., 2021）高度相关。更深入的讨论有助于 contextualize penalty sensitivity 的发现。

---

## Scores

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论严谨，统计分析充分，但核心发现的 tautological 性质（高惩罚环境中死亡主导得分差异）以及 deterministic 策略的 oracle 特权限制了 claim 的强度 |
| Excitement | 2.5/5 | 框架本身有价值，但核心发现范围窄、actionability 有限（结论基本是"直接用 deterministic"），且主要限于一个环境 |
| Reproducibility | 4/5 | 代码和数据承诺公开，prompt templates 完整提供（Appendix T），实验细节充分 |
| Overall | **3.0** (Findings) | 方法论贡献达到 Findings 水准——framework 有用，统计分析示范性好，但核心发现的新颖性和影响力不足以支撑主会议接收。环境覆盖过窄（实质上只有 ScienceWorld 的一个发现），跨环境探测未确认核心机制的可复现性 |
| Confidence | 4/5 | 仔细阅读了全部 8 页正文、Limitations、Ethics、以及全部 21 个附录的 LaTeX 源码 |

---

## Detailed Comments

### Abstract
- 数字密度过高（7 个统计量），建议精简至 3 个核心数字
- "d = 3.02" 不适合出现在 abstract
- "methodological generality" vs. "empirical generality" 的区分在 abstract 中过于压缩，建议在 introduction 展开而非 abstract 压缩

### Introduction (Section 1)
- Motivation 清晰：per-step oracle 在 sparse reward 下退化（97.4% tie rate）是一个好的切入点
- 第 3 段（核心发现）和第 5 段（contributions）重复度高
- "78.9% of non-tie episode-level routing labels arise from death asymmetry" 作为核心 claim 准确但需要更好地建立 non-triviality
- Contributions 列表格式良好，(1) 和 (2) 区分清楚

### Method (Section 2)
- 整体写得清晰，形式化程度恰当
- Algorithm 1 放在 Appendix B 而非正文是合理的，但 Section 2.3 的文字描述应更明确 death-priority rule 的 justification
- DAF 的数学推导（Section 2.4）是论文最强的部分——公式简洁，假设透明
- 但 Section 2.4 的最后一段（"Scope of episode-level analysis"）感觉是从 Limitations 搬来的，放在 Method 中节奏不佳

### Experiments (Section 3)
- Section 3.1 (Death Avoidance Decomposition): 核心结果呈现清晰
- Section 3.2 (Cross-Model): 最强的验证实验，三个模型族的收敛有说服力
- Section 3.3 (Agent Improvement): Reflexion 使 DAF > 100% 是一个有趣的发现，但叙述可以更简洁
- Section 3.4 (Cross-Environment): 如前述，两个探测性环境都未复现核心机制，降低了论文整体的 generality claim
- Section 3.5 (Baselines): Table 2 中 Oracle 仅比 Always-Deterministic 好 2.89 分（-6.58 vs -9.47），这个 "oracle degeneracy" 是强证据
- Section 3.6 (Router Training): 负面结果的呈现方式很好——不是 "we failed" 而是 "the signal structure precludes success"

### Related Work (Section 4)
- 组织合理（5 个 paragraph，覆盖 tool use, adaptive computation, counterfactual RL, agent environments, safe RL）
- 如 Missing References 所述，缺少 hallucination 和 non-agent adaptive computation 文献
- Concurrent work 的 positioning 总体公平

### Discussion (Section 5)
- "Signal granularity and router failure" 段落有价值
- "Non-triviality and oracle confound" 段落正确地预判了 W2 的批评但未充分回应
- "Practical implications" 段落的 actionability 有限——"when f_death > 75%, always-deterministic matches learned alternatives" 是有用的但过于保守

### Conclusion (Section 6)
- 仅 3 句话，过于简短
- 建议增加具体的 future work 方向（如哪些环境最有潜力验证 framework、step-level death prediction 的可能路径）

### Figures and Tables
- Figure 1 (pipeline overview): 清晰有效
- Figure 2 (dose-response): 信息量大，legend 和 horizontal baselines 提供了好的比较
- Table 1 (agent improvement): 结构清晰
- Table 2 (baselines): 有效
- Figure 3 (cross-environment label distribution, in appendix): 有信息量但 caption 可以更 self-contained

### 格式合规
- 正文 8 页（Sections 1-6），Limitations 从第 9 页开始，References 从第 10 页开始——**符合 EMNLP 2026 8 页限制**
- 使用 `\usepackage[review]{acl}` 和 `\author{Anonymous}`——**符合 double-blind 要求**
- 引用格式一致（\citep / \citet 使用正确）

---

## 总体评分

**Overall: 3.0 (Findings)**

**一句话总结**: 方法论框架有价值且统计分析示范性好，但核心发现（高惩罚环境中死亡主导路由信号）的新颖性有限，环境覆盖过窄（实质一个环境），且 deterministic 策略的 oracle 特权使 "routing signal" 的解读变得模糊。

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

_source line 2538 · 2026-05-23T03:49:27.838270+00:00_

Reviewer 2 审稿意见已收到。核心评分：Overall 3.0 (Findings)，Soundness 3.5，Excitement 2.5。

主要发现：3 个 critical weaknesses（novelty tautology、oracle privilege confound、环境覆盖窄），4 个 warning-level issues（non-death 分析不足、abstract 数字过密、重复、单一失败模式）。

格式方面 Reviewer 2 判定正文在 8 页以内——这与历史 issue tracker（R29-N1: page overflow）有出入，需要在交叉分享阶段关注。

等待 Reviewer 1 提交审稿意见，收到后进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 208

## Round 208

2 recorded events


### User

_source line 2539 · 2026-05-23T03:49:30.493706+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**。

主要理由：
- **3 个 critical 问题**：(1) 核心发现的新颖性存疑——高惩罚环境中死亡主导得分差异近乎同义反复；(2) deterministic 策略的 oracle 特权使 "routing signal" 与 "information privilege" 难以分离；(3) 跨环境覆盖过窄，两个探测性环境均未复现核心机制。
- **主要优势**：方法论框架有价值，统计分析严谨（bootstrap/cluster-robust/LOO），跨模型复现（3 个 7-9B 模型族 DAF 88-90%）令人信服，自我批判性极强。
- **写作问题**：Abstract 数字过密，Introduction/Discussion/Conclusion 重复度高，"deterministic" 术语可能误导。
- **缺失引用**：hallucination detection 文献、non-agent adaptive computation（early exit 等）、reward shaping 文献。

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

_source line 2540 · 2026-05-23T03:49:40.031101+00:00_

Reviewer 2 审稿意见已收到（Overall 3.0 / Findings）。等待 Reviewer 1 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 209

## Round 209

6 recorded events


### User

_source line 2541 · 2026-05-23T03:53:40.966299+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 完整审稿意见 (Round 1)

**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**Venue**: EMNLP 2026 via ACL Rolling Review (ARR)

---

## Summary

本文提出了一个 episode-level counterfactual 诊断框架，用于分析 LLM agent routing signal（何时使用内部推理 vs. 外部工具）的构成。将该框架应用于 ScienceWorld（11/30 task types，245 episodes，Qwen2.5-7B），发现 78.9%（75/95）的 non-tie routing labels 源自 death asymmetry——内部策略因幻觉导致的 catastrophic failure 频率远高于 deterministic oracle。Death Avoidance Factor (DAF) 在 P=100 时达 90.4%。跨模型复制（3 families, 7-9B）、agent improvement baselines（Retry, Reflexion, 72B scaling）、跨环境探测（MATH 无信号；ALFWorld 信息不对称）提供了支撑。

---

## Strengths

**S1. 方法论上的 episode-level counterfactual 设计优雅有效。** Per-step oracle 在 sparse-reward 环境下退化为 97.4% 平局率（§2.2），这一观察本身就是方法论贡献。通过在相同初始条件（same random seed）下运行两种 pure strategies，框架干净地隔离了 computation mode 作为唯一变量。

**S2. 透明度和鲁棒性检验极其充分。** 21 个 Appendix (A–U) 涵盖 labeling quality audit (B), cluster bootstrap sensitivity (E), leave-one-task-out (G), seed robustness (J), penalty sensitivity (K), failure mode analysis (N), grounding ablation (O), extended validation (S) 等。这种严谨程度在同类工作中罕见。

**S3. Claims 与证据的校准非常审慎。** 论文明确区分 methodological generality 与 empirical generality（Abstract, §1），将 MATH/ALFWorld 定位为 "boundary probes" 而非 cross-domain validation（§3.4），并以 label fraction (78.9%) 而非 DAF (90.4%) 作为 primary penalty-invariant metric（§2.4）。Limitations 部分涵盖 5 个维度，坦诚到位。

**S4. 跨模型复制强劲。** Qwen2.5-7B、Llama-3.1-8B、Gemma-2-9B-it 三个架构不同的模型 family 收敛于 DAF 88–90%（spread 仅 2.2pp），death-prone tasks 方向一致性 10/10（§3.2）。这有力排除了 model-specific 解释。

**S5. Router training negative result 的报告方式值得称赞。** §3.6 对 step-level router 失败提供了两种平衡的解释（noise-dominated labels vs. genuine non-learnability），没有过度解读或回避。

**S6. Oracle degeneracy 观察有力。** Always-deterministic 匹配 96.3% 的 oracle 决策（§3.5），直接表明在 ScienceWorld 中 routing 的 value 极为有限。这是一个重要的实证发现。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1. [critical] 核心发现的新颖性受限——death dominance 部分是环境设计的数学必然，而非经验发现。**
- ScienceWorld 施加 P=100 死亡惩罚，internal strategy 因幻觉进入灾难状态死亡率 42.9%（vs. oracle 16.3%）。在 P=100 >> 典型 non-death 分数差（Δ_nd≈2.84）的条件下，death 支配 score gap 是解析可预测的。
- 论文承认这一点（§2.4: "DAF increases monotonically with P, a mathematical consequence rather than an empirical finding"），并使用 penalty-invariant label fraction 作为 primary metric。但 78.9% label fraction 本身也部分是 Algorithm 1 的设计后果：death-priority rule *保证*任何单方死亡 episode 被分类为 death-determined。因此 78.9% 本质上测量的是 "多少比例的 episodes 恰好一方策略死亡"——比框架所暗示的更简单的统计量。
- **影响**: 论文将概念贡献定位为 "decomposing routing signal into mechanistic components"，但 decomposition 本质上可归结为一个 death-rate asymmetry 的度量。DAF、SCI 等概念可能构成 methodological overengineering。
- **建议**: (1) 在 Introduction 中更直接地将 78.9% 描述为 "death-rate asymmetry 的频率"，减少 framework 的认知负荷；(2) 强化论文对 "为什么事先不可预测" 的论证（当前 §5 "Non-triviality and oracle confound" 部分有讨论但不够突出——特别是 72B 不减少 DAF 和 Reflexion 产生 DAF>100% 的发现确实 non-trivial，应更早呈现）。
- 具体位置：§2.4, §3.1, §5, Abstract

**N2. [critical] 诊断与处方之间的实际差距限制了影响力。**
- 论文明确声明是 diagnostic 而非 prescriptive（Limitations）。但从诊断中得出的实际建议——"在 death-dominated 环境中使用 always-deterministic"——是平凡的，不需要本框架来推导。
- 更核心的问题是：oracle margin 仅为 2.89 分（Table 2），意味着完美 router 几乎不超过 always-deterministic。这表明在 ScienceWorld 中 routing 本身 low-value，削弱了 routing signal 分析的动机。
- Practitioner Decision Framework（Appendix R, Table 20）有用但薄弱——4 个条件基于 DAF 阈值（50%, 75%），但这些阈值看起来 arbitrary（无 sensitivity analysis）。
- **影响**: EMNLP 读者期望 diagnostic 论文提供 actionable insight。当前版本中，最有价值的 actionable finding 是 "50-episode pilot 足以做 build-vs-buy 决策"（Appendix R），但这被埋在 appendix 中。
- **建议**: (1) 将 Decision Framework 从 Appendix R 提升到正文 Discussion 中；(2) 更深入讨论 oracle degeneracy（§3.5）的实际意义——routing 在 ScienceWorld 中价值极低本身是一个重要发现；(3) 明确讨论：如果 death 是可预测的（Failure Mode Analysis 显示所有死亡源自 `focus on` action），那么一个简单的 action-level filter 是否足以替代 router？
- 具体位置：§3.5, §5, Appendix R

### Should-Fix 问题（影响评分但不一票否决）

**W1. [warning] Cluster bootstrap K=11 低于推荐阈值，影响不确定性量化的可靠性。**
- K=11 task-type clusters 远低于 Cameron et al. (2008) 和 Webb (2023) 推荐的 K≥20–50。Cluster-robust CI [73.3%, 100.0%] vs. non-clustered [81.1%, 99.0%]。
- Cohen's d=3.02 是极端效应量（社会科学 >99.9th percentile）——这很可能反映 task-type 内的高度相关二值结构（10/11 death-prone types 全部 100% death-asymmetry labels），而非 genuinely massive effect。论文应更明确地 contextualize 这一数值。
- 论文提供了多种 supplementary analyses（non-clustered bootstrap, directional consistency, seed replication）来缓解这一问题，这是好的。但应更清楚地引导读者以 non-clustered CI 为 recommended primary inference。
- 具体位置：§3.1, Limitations (Statistical limitations)
- 建议：在 §3.1 中添加一句明确推荐："Given K=11 < 20, we recommend the non-clustered bootstrap CI [81.1%, 99.0%] as the primary uncertainty estimate."

**W2. [warning] 72B scaling 证据不足以支撑 "persistent under 10× scaling" 的 claim。**
- 仅测试了 Qwen2.5-72B（单一模型、单一 family）。无 Llama 或 Gemma 的大规模对应版本。一个数据点无法建立 scaling trend。
- DAF 从 90.4% 增到 92.4%——但未报告 72B DAF 的 bootstrap CI。这一 2pp 变化在统计上可能不显著。
- Conclusion 和 Abstract 中的 "persistent under 10× scaling" 基于 single model replication，过于绝对。
- 具体位置：§3.3, Conclusion, Abstract
- 建议：降低 claim 强度，改为 "a preliminary 72B probe suggests persistence" 或类似措辞。

**W3. [warning] Router training negative result 可能被 extreme class imbalance 混淆，而非反映 fundamental non-learnability。**
- 90.5% 的 non-tie labels 为 deterministic-preferred（86/95），仅 9 个 internal-preferred episodes。标准学习理论预测在 90%+ class imbalance 和 n=95 下 near-chance performance。
- 论文讨论了这一点（§5: "distinguishing the two requires ~1,350 paired episodes"），但当前证据无法分离 data limitation 和 signal limitation 两种解释。
- §3.6 中 interpretation B（non-learnability）的论证依赖于 text augmentation 无改善和 LOTO 退化到 chance——但前者可能是 augmentation 方法的问题，后者是 task-type-level constant signal 的预期行为（并不能区分 data vs. signal limitation）。
- 具体位置：§3.6, §5
- 建议：更明确地将 negative result frame 为 "inconclusive under current data regime"，避免倾向 interpretation B。

**W4. [warning] 跨环境探测提供的框架泛化性证据有限。**
- MATH：84.4% no-preference，无 routing signal——仅确认框架在无信号时不产生误报，但未正面验证 decomposition 能力。
- ALFWorld：仅 35（Qwen）和 16（Llama）个 non-tie labels。样本量太小，对 "information asymmetry" 的刻画信心有限。
- 两个环境都未展示框架将 routing signal decompose 为 *多个* contributing mechanisms 的能力——这才是 decomposition capability 的最强测试。
- 具体位置：§3.4
- 建议：明确这一限制。如果能找到一个同时存在 death avoidance 和 non-death routing signal 的环境（如修改 ScienceWorld 降低 P 或增加 non-death 信号），将大幅增强框架的说服力。

### 小问题（不影响接收）

- §2.4 的 approximation residual (0.23, 0.8%) 讨论了何时近似成立，但未讨论何时会 break down。如果 s_surv 不远小于 P（如软惩罚环境），近似误差会如何变化？
- §3.1 中 61.2% episodes 为 no-preference——大多数 episodes 不区分策略。框架的 findings 由 38.8%（95 episodes）驱动。这一 base rate 应在正文中更突出讨论。
- Table 2（§3.5）的 Trained Router 结果（-10.70）用了 single seed (42)，而其他 baselines 用了 full episode set。公平性存疑。
- SCI=0.2147（Appendix A）的解释价值有限——10/11 task types 都有 death dominance 时，低 concentration 是显然的。
- Figure 1 的 pipeline 图清晰但可以更紧凑。
- 部分 appendix 内容（如 Appendix T: Agent Prompt Templates）对审稿不是必需的，但对 reproducibility 有价值。

---

## Questions

**Q1.** 如果包含全部 30 种 ScienceWorld task types（含 19 种 excluded），label fraction 如何变化？即使 excluded types 多为 no-preference，是否有 type 产生 non-death non-tie labels 从而降低 78.9%？

**Q2.** Failure Mode Analysis（Appendix N）显示所有 105 次 internal-strategy deaths 都由 `focus on` action 触发。这意味着 "death avoidance signal" 可以更精确地描述为 "focus-on avoidance"？`focus on` 操作中多大比例导致死亡？简单的 action-level filter 能否替代 router？

**Q3.** Grounding Ablation（Appendix O）显示 action-space filtering 减少 death 19pp。在 grounding 之后，框架的诊断结论是否改变？death 是否仍然 dominate？

**Q4.** Algorithm 1 的 death-priority rule 在二值 catastrophic failure 环境中合理，但 §5 讨论了 graded penalties 的 extension。如果将 death-priority rule 替换为 continuous severity weighting，现有结论是否 robust？

**Q5.** Oracle degeneracy（96.3% 的 oracle 决策匹配 always-deterministic）是否意味着 ScienceWorld 根本不适合作为 routing research 的 testbed？这一发现对论文的 motivation 有何影响？

---

## Missing References

无 critical omissions。相关工作覆盖全面，包含多篇 2026 concurrent work。Minor suggestions:
- LLM 不确定性估计（如 Kadavath et al., 2022, "Language models (mostly) know what they know"）可强化关于何时内部推理 recognize 自身 failure risk 的讨论。
- MoE 架构中 token-level routing 的学习文献（beyond Switch Transformer/GShard）可为 granularity 讨论提供更多 context。

---

## Scores

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 4/5 | Strong: 方法论严谨，counterfactual 设计 sound，exhaustive robustness checks。主要 caveat 在 cluster bootstrap K=11 和 scaling 证据单薄。 |
| **Excitement** | 3/5 | Interesting: 诊断框架有方法论价值，但核心发现（death dominance）在 catastrophic-failure 环境中部分可预测；limited novelty + limited actionability 制约 excitement。|
| **Reproducibility** | 4/5 | Mostly reproducible: 所有环境和模型公开可用，Appendix T 提供完整 prompt templates，承诺代码/数据开源。 |
| **Overall** | 3.5 (Borderline Conference) | 方法论贡献 solid、执行 thorough、跨模型复制 strong，但 (1) 核心发现新颖性受限（环境设计的数学后果 vs. 经验发现），(2) diagnostic-only 无 prescriptive insight，(3) 单环境 quantitative validation。如果作者能在 rebuttal 中加强 novelty 论证（特别是突出 non-trivial 发现如 72B 不减少 DAF、Reflexion DAF>100%）和 actionability（将 Decision Framework 提升到正文），可考虑提升至 4 (Conference)。|
| **Confidence** | 4/5 | Quite sure: 仔细审查了方法论、统计推断、所有 appendices，熟悉 routing/agent/counterfactual 相关文献。 |

---

## 一句话总结

方法论严谨的诊断框架在 ScienceWorld 上精确量化了 death dominance 对 routing signal 的支配性，但核心发现的新颖性（部分为环境设计的数学后果）和 practical impact（diagnostic-only, 无 actionable prescription）限制了 excitement。

---

## Detailed Comments（逐节）

### Abstract
- 清晰准确，claim 与证据匹配。"revealing that in catastrophic-failure environments, signal diversity can collapse to a single dominant mechanism" 稍显循环——catastrophic-failure 环境中信号被 catastrophic failure 支配是 expected 的。

### Section 1 (Introduction)
- "no prior work has systematically decomposed what drives routing preferences" 是好的 motivation。97.4% per-step tie rate 的观察有效地推动了 episode-level 分析。
- Paragraph 2 的 related work positioning（Toolformer, ART, Chameleon, CogRouter, ARES, etc.）简洁到位。
- Contributions 总结清晰，label fraction 和 DAF 同时呈现，但未在此处说明哪个是 primary（在 §2.4 才阐明）。建议在此处就指明 78.9% label fraction 是 primary metric。

### Section 2 (Method)
- §2.1: Problem setup 形式化干净。两种 computation mode 的定义清晰。
- §2.2: Per-step degeneracy (97.4%) 的发现是重要的方法论贡献。
- §2.3: Algorithm 1 的 death-priority rule 在 binary catastrophic failure 下合理。但 §2.3 正文仅简述 labeling 逻辑，完整 algorithm 在 Appendix B——对理解论文核心方法需翻到 page 13，reading flow 稍受影响。
- §2.4: DAF 定义清晰，近似 residual (0.8%) 的报告增加可信度。"Relationship between DAF and label fraction" 段落是必要的但应更早出现。"Scope of episode-level analysis" 段落有效预防了 "为什么不用 step-level" 的质疑。

### Section 3 (Experiments)
- §3.1: Prescreening (11/30 types) 的 justification 充分，anti-cherry-picking analysis (Appendix S) 有力。
- §3.1: 150/245 (61.2%) no-preference 是重要的 base rate——意味着大多数 episodes 两种策略表现相同。这削弱了 routing 在 ScienceWorld 中的整体 value。建议在正文更突出讨论。
- §3.2: 跨模型复制是论文最强的贡献之一。DAF 88-90% 的窄幅收敛令人信服。
- §3.3: Reflexion DAF>100% 的解释清晰（self-correction 在 non-death episodes 略优于 oracle，但 death gap 仍在）。72B 的 DAF 增加（90.4%→92.4%）因 deterministic 也变更安全，是 insightful observation。
- §3.4: MATH 和 ALFWorld 作为 boundary probes 定位准确。ALFWorld 的 non-tie labels 数量太少（35, 16）是客观限制。
- §3.5: Oracle degeneracy (96.3%) 应在论文中获得更多 attention——这是一个 striking finding，直接影响对 routing value 的判断。
- §3.6: Router training diagnostic 的呈现密度高。建议添加 summary table 列出所有 router configurations 和结果。两种 interpretation 的平衡讨论值得肯定。

### Section 4 (Related Work)
- 全面且组织良好。Safe RL 连接合适但可扩展——death-avoidance finding 对 constrained optimization in agent training 有直接启示。

### Section 5 (Discussion)
- "Non-triviality and oracle confound" 有效回应了最自然的反对意见（Δ_nd=2.84, 仅占 gap 的 9.6%）。
- "Practical implications" 段过于简短。建议将 Appendix R 的 Decision Framework 内容部分移入此处。
- 缺少对 Q2（`focus on` as sole death trigger）和 Q3（grounding 后的诊断变化）的正面讨论。

### Limitations
- 异常全面。5 个 limitation paragraphs 均 substantive 且 honest。
- "Pure-strategy upper bound" 观点重要：DAF=90.4% 是 mixed routing 下 death avoidance 贡献的 upper bound。建议在正文 §5 中也提及。

### Appendices
- 质量高且组织清晰。Appendix Overview 提供了 21 个 section 的导航。
- Appendix K (Penalty Sensitivity) 直接回应了 DAF 对 P 依赖的问题，展示完整 DAF curve。
- Appendix N (Failure Mode Analysis) 提供了 `focus on` 作为唯一 death trigger 的详细证据——这是论文最 actionable 的发现之一，应在正文中更突出。
- Appendix R (Decision Framework) 如前述，应部分提升至正文。

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

_source line 2542 · 2026-05-23T03:54:43.884709+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Step 2 — 交叉分享：请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]**：同意该观点，并简要说明理由\n- **[REBUT]**：不同意，提供证据（cite 具体 Section/Table/Figure/Appendix）\n\n特别关注你们的分歧点：Reviewer 2 给了 Overall 3.0 (Findings)，你给了 3.5 (Borderline Conference)。请说明你是否在看完 R2 的意见后调整你的评分。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Summary\n本文提出一个 episode-level counterfactual diagnostic framework，用于在构建路由器之前分析 LLM agent 路由信号的机制组成。在 ScienceWorld 环境中（11 个任务类型，245 个 episodes），作者发现 78.9% 的非平局路由标签来源于\"死亡不对称\"——内部推理策略触发灾难性失败（-100 惩罚），而确定性策略存活。该发现在三个 7-9B 模型族中复现（DAF 88-90%），并通过 MATH（无路由信号）和 ALFWorld（信息不对称）进行了跨环境探测。Step-level router 训练实验得到接近随机的结果，证实信号是 task-type-level 的二元属性。\n\n### Strengths\nS1. 方法论贡献有价值——\"先诊断再构建\"的思路在 routing 文献中是一个有意义的缺口填补。\nS2. 统计分析异常严谨（bootstrap/cluster-robust/LOO/wild cluster/Cohen's d）。\nS3. 跨模型复现令人信服（3 families, DAF 88-90%, spread 2.2pp）。\nS4. 自我批判性极强——Limitations 约 1.5 页，反复区分方法论与经验通用性。\nS5. 负面结果的诊断价值——router failure 被转化为对信号结构的洞察。\nS6. Anti-cherry-picking 论证充分。\n\n### Weaknesses\n\n**W1. [critical] 核心发现的新颖性存疑——\"death dominates in death-penalty environments\" 在一定程度上是同义反复。**\n- DAF = δP/(δP + Δ_nd)，只要 P 足够大且 δ > 0，DAF 趋近 1 是代数必然。\n- 78.9% label fraction 也部分是 Algorithm 1 death-priority rule 的设计后果。\n- 真正有新颖性的是 penalty-invariant label fraction (78.9%)，但标题、framing 重心在 DAF。\n- 建议重构叙事，label fraction 而非 DAF 作为主要指标，并论证 78.9% 为何 non-trivial。\n\n**W2. [critical] \"Deterministic\" 策略的特权性质严重限制了发现的通用性。**\n- ScienceWorld 的 deterministic 是 oracle simulator with ground-truth state access。\n- 死亡率差异可归因于信息不对称，而非内在的 routing signal 属性。\n- ALFWorld 分析诊断为 \"information asymmetry\"——ScienceWorld 是否也主要如此？\n- 建议讨论 death avoidance 与 information privilege 的关系，或测试 non-privileged 外部工具。\n\n**W3. [critical] 环境覆盖过窄，跨环境 \"probes\" 无法支撑通用性主张。**\n- MATH 无信号，ALFWorld 信号不同——都未复现 death dominance。\n- 需要至少一个不同的 catastrophic-failure 环境来验证框架。\n\n**W4. [warning] Non-death component (21.1% of labels) 分析不足。**\n- 20 个 non-death labels 未系统分析来源（hallucination vs. suboptimal action vs. random variance）。\n\n**W5. [warning] Abstract 数字过密（7 个统计量），可读性差。Cohen's d 不应在 abstract。**\n\n**W6. [warning] Discussion/Conclusion 与 Introduction 重复度高。Conclusion 仅 3 句过于简短。**\n\n**W7. [warning] 100% deaths 来自 focus on 单一模式——grounding ablation 降 19pp，说明 \"death avoidance\" 实质上是一个可修复的 grounding bug。**\n\n**W8. [warning] \"deterministic\" 术语可能误导——三个环境含义完全不同，建议用 \"privileged\" 或 \"oracle-assisted\"。**\n\n**W9. [info] 部分 2026 concurrent work 引用需读者自行验证。**\n\n### Questions\nQ1. P=0 时 label fraction 是否变化？\nQ2. Dense-reward 环境下 framework 是否仍需 episode-level？\nQ3. Gemma-2 排除 find-non-living-thing 后 DAF 从 89.7% 跳到 99.9%——对单个 zero-death 任务极度敏感？\nQ4. T_max=100 是否能在 excluded tasks 中发现 non-death signal？\nQ5. Task-type classifier 64.7% balanced accuracy——是否 lookup table 足以替代 router？\n\n### Missing References\n1. Hallucination detection/mitigation 文献完全缺失\n2. Non-agent adaptive computation 讨论过于简略\n3. Reward shaping 文献（Eschmann et al., 2021）\n\n### Scores\nSoundness 3.5/5, Excitement 2.5/5, Overall 3.0 (Findings), Confidence 4/5\n\n---\n\n**请逐条回应上述所有 Weaknesses (W1-W9)、Questions (Q1-Q5)、Missing References，并说明是否调整你的 Overall 评分。**"
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
    "text": "## Step 2 — 交叉分享：请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]**：同意该观点，并简要说明理由\n- **[REBUT]**：不同意，提供证据（cite 具体 Section/Table/Figure/Appendix）\n\n特别关注你们的分歧点：Reviewer 2 给了 Overall 3.0 (Findings)，你给了 3.5 (Borderline Conference)。请说明你是否在看完 R2 的意见后调整你的评分。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Summary\n本文提出一个 episode-level counterfactual diagnostic framework，用于在构建路由器之前分析 LLM agent 路由信号的机制组成。在 ScienceWorld 环境中（11 个任务类型，245 个 episodes），作者发现 78.9% 的非平局路由标签来源于\"死亡不对称\"——内部推理策略触发灾难性失败（-100 惩罚），而确定性策略存活。该发现在三个 7-9B 模型族中复现（DAF 88-90%），并通过 MATH（无路由信号）和 ALFWorld（信息不对称）进行了跨环境探测。Step-level router 训练实验得到接近随机的结果，证实信号是 task-type-level 的二元属性。\n\n### Strengths\nS1. 方法论贡献有价值——\"先诊断再构建\"的思路在 routing 文献中是一个有意义的缺口填补。\nS2. 统计分析异常严谨（bootstrap/cluster-robust/LOO/wild cluster/Cohen's d）。\nS3. 跨模型复现令人信服（3 families, DAF 88-90%, spread 2.2pp）。\nS4. 自我批判性极强——Limitations 约 1.5 页，反复区分方法论与经验通用性。\nS5. 负面结果的诊断价值——router failure 被转化为对信号结构的洞察。\nS6. Anti-cherry-picking 论证充分。\n\n### Weaknesses\n\n**W1. [critical] 核心发现的新颖性存疑——\"death dominates in death-penalty environments\" 在一定程度上是同义反复。**\n- DAF = δP/(δP + Δ_nd)，只要 P 足够大且 δ > 0，DAF 趋近 1 是代数必然。\n- 78.9% label fraction 也部分是 Algorithm 1 death-priority rule 的设计后果。\n- 真正有新颖性的是 penalty-invariant label fraction (78.9%)，但标题、framing 重心在 DAF。\n- 建议重构叙事，label fraction 而非 DAF 作为主要指标，并论证 78.9% 为何 non-trivial。\n\n**W2. [critical] \"Deterministic\" 策略的特权性质严重限制了发现的通用性。**\n- ScienceWorld 的 deterministic 是 oracle simulator with ground-truth state access。\n- 死亡率差异可归因于信息不对称，而非内在的 routing signal 属性。\n- ALFWorld 分析诊断为 \"information asymmetry\"——ScienceWorld 是否也主要如此？\n- 建议讨论 death avoidance 与 information privilege 的关系，或测试 non-privileged 外部工具。\n\n**W3. [critical] 环境覆盖过窄，跨环境 \"probes\" 无法支撑通用性主张。**\n- MATH 无信号，ALFWorld 信号不同——都未复现 death dominance。\n- 需要至少一个不同的 catastrophic-failure 环境来验证框架。\n\n**W4. [warning] Non-death component (21.1% of labels) 分析不足。**\n- 20 个 non-death labels 未系统分析来源（hallucination vs. suboptimal action vs. random variance）。\n\n**W5. [warning] Abstract 数字过密（7 个统计量），可读性差。Cohen's d 不应在 abstract。**\n\n**W6. [warning] Discussion/Conclusion 与 Introduction 重复度高。Conclusion 仅 3 句过于简短。**\n\n**W7. [warning] 100% deaths 来自 focus on 单一模式——grounding ablation 降 19pp，说明 \"death avoidance\" 实质上是一个可修复的 grounding bug。**\n\n**W8. [warning] \"deterministic\" 术语可能误导——三个环境含义完全不同，建议用 \"privileged\" 或 \"oracle-assisted\"。**\n\n**W9. [info] 部分 2026 concurrent work 引用需读者自行验证。**\n\n### Questions\nQ1. P=0 时 label fraction 是否变化？\nQ2. Dense-reward 环境下 framework 是否仍需 episode-level？\nQ3. Gemma-2 排除 find-non-living-thing 后 DAF 从 89.7% 跳到 99.9%——对单个 zero-death 任务极度敏感？\nQ4. T_max=100 是否能在 excluded tasks 中发现 non-death signal？\nQ5. Task-type classifier 64.7% balanced accuracy——是否 lookup table 足以替代 router？\n\n### Missing References\n1. Hallucination detection/mitigation 文献完全缺失\n2. Non-agent adaptive computation 讨论过于简略\n3. Reward shaping 文献（Eschmann et al., 2021）\n\n### Scores\nSoundness 3.5/5, Excitement 2.5/5, Overall 3.0 (Findings), Confidence 4/5\n\n---\n\n**请逐条回应上述所有 Weaknesses (W1-W9)、Questions (Q1-Q5)、Missing References，并说明是否调整你的 Overall 评分。**"
  }
}
```

</details>

---


### Tool result

_source line 2543 · 2026-05-23T03:55:16.885428+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 33000
}
```

</details>

---


### Tool call

_source line 2544 · 2026-05-23T03:55:17.086883+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Step 2 — 交叉分享：请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]**：同意该观点，并简要说明理由\n- **[REBUT]**：不同意，提供证据（cite 具体 Section/Table/Figure/Appendix）\n\n特别关注你们的分歧点：Reviewer 1 给了 Overall 3.5 (Borderline Conference)，你给了 3.0 (Findings)。请说明你是否在看完 R1 的意见后调整你的评分。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Summary\n本文提出了一个 episode-level counterfactual 诊断框架，用于分析 LLM agent routing signal 的构成。将该框架应用于 ScienceWorld（11/30 task types，245 episodes，Qwen2.5-7B），发现 78.9%（75/95）的 non-tie routing labels 源自 death asymmetry。DAF 在 P=100 时达 90.4%。跨模型复制（3 families, 7-9B）、agent improvement baselines、跨环境探测提供了支撑。\n\n### Strengths\nS1. Episode-level counterfactual 设计优雅——per-step 97.4% tie rate 本身是方法论贡献。\nS2. 透明度和鲁棒性检验极充分（21 个 Appendix）。\nS3. Claims 与证据的校准审慎（methodological vs. empirical generality）。\nS4. 跨模型复制强劲（3 families, DAF 88-90%）。\nS5. Router training negative result 报告方式平衡。\nS6. Oracle degeneracy（96.3%）是 striking finding。\n\n### Must-Fix 问题\n\n**N1. [critical] 核心发现新颖性受限——death dominance 部分是环境设计的数学必然。**\n- P=100 >> Δ_nd≈2.84 条件下，death 支配 score gap 是解析可预测的。\n- 78.9% label fraction 本质上测量 \"多少比例的 episodes 恰好一方策略死亡\"——比框架所暗示的更简单。\n- DAF、SCI 可能构成 methodological overengineering。\n- 建议：(1) 更直接描述 78.9% 为 death-rate asymmetry 频率；(2) 强化 non-trivial 发现（72B 不减少 DAF、Reflexion DAF>100%）的呈现。\n\n**N2. [critical] 诊断与处方之间的实际差距限制影响力。**\n- \"在 death-dominated 环境中使用 always-deterministic\" 是平凡建议。\n- Oracle margin 仅 2.89 分——routing 在 ScienceWorld 中 low-value。\n- Decision Framework（Appendix R）有用但被埋在 appendix。\n- 建议：(1) 将 Decision Framework 提升到正文；(2) 更深入讨论 oracle degeneracy 的意义；(3) 讨论 action-level filter vs. router。\n\n### Should-Fix 问题\n\n**W1. [warning] Cluster bootstrap K=11 低于推荐阈值。**\n- Cohen's d=3.02 可能反映 binary structure 而非 massive effect。\n- 建议明确推荐 non-clustered CI 为 primary inference。\n\n**W2. [warning] 72B scaling 证据不足——单一模型、无 bootstrap CI、\"persistent under 10× scaling\" 过于绝对。**\n\n**W3. [warning] Router negative result 可能被 extreme class imbalance 混淆（90.5% det-preferred）。**\n- 建议 frame 为 \"inconclusive under current data regime\"。\n\n**W4. [warning] 跨环境探测提供的框架泛化性证据有限。**\n- MATH 仅确认无误报，ALFWorld non-tie labels 太少（35, 16）。\n- 两个环境都未展示框架 decompose 多种机制的能力。\n\n### 小问题\n- §2.4 近似 break down 条件未讨论\n- 61.2% no-preference base rate 应更突出\n- Table 2 Trained Router 用 single seed vs. full episode set，公平性存疑\n- SCI=0.2147 在 10/11 death-dominant 时解释价值有限\n\n### Questions\nQ1. 包含全部 30 种 task types 后 label fraction 如何变化？\nQ2. focus on 作为唯一 death trigger——简单 action filter 能否替代 router？\nQ3. Grounding ablation 后框架诊断是否改变？\nQ4. Death-priority rule 替换为 continuous severity weighting 后结论是否 robust？\nQ5. Oracle degeneracy 是否意味着 ScienceWorld 不适合作为 routing testbed？\n\n### Missing References\n- LLM 不确定性估计（Kadavath et al., 2022）\n- MoE token-level routing 文献\n（无 critical omissions）\n\n### Scores\nSoundness 4/5, Excitement 3/5, Overall 3.5 (Borderline Conference), Confidence 4/5\n\n---\n\n**请逐条回应上述所有 Must-Fix (N1-N2)、Should-Fix (W1-W4)、小问题、Questions (Q1-Q5)、Missing References，并说明是否调整你的 Overall 评分。**"
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
    "text": "## Step 2 — 交叉分享：请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]**：同意该观点，并简要说明理由\n- **[REBUT]**：不同意，提供证据（cite 具体 Section/Table/Figure/Appendix）\n\n特别关注你们的分歧点：Reviewer 1 给了 Overall 3.5 (Borderline Conference)，你给了 3.0 (Findings)。请说明你是否在看完 R1 的意见后调整你的评分。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Summary\n本文提出了一个 episode-level counterfactual 诊断框架，用于分析 LLM agent routing signal 的构成。将该框架应用于 ScienceWorld（11/30 task types，245 episodes，Qwen2.5-7B），发现 78.9%（75/95）的 non-tie routing labels 源自 death asymmetry。DAF 在 P=100 时达 90.4%。跨模型复制（3 families, 7-9B）、agent improvement baselines、跨环境探测提供了支撑。\n\n### Strengths\nS1. Episode-level counterfactual 设计优雅——per-step 97.4% tie rate 本身是方法论贡献。\nS2. 透明度和鲁棒性检验极充分（21 个 Appendix）。\nS3. Claims 与证据的校准审慎（methodological vs. empirical generality）。\nS4. 跨模型复制强劲（3 families, DAF 88-90%）。\nS5. Router training negative result 报告方式平衡。\nS6. Oracle degeneracy（96.3%）是 striking finding。\n\n### Must-Fix 问题\n\n**N1. [critical] 核心发现新颖性受限——death dominance 部分是环境设计的数学必然。**\n- P=100 >> Δ_nd≈2.84 条件下，death 支配 score gap 是解析可预测的。\n- 78.9% label fraction 本质上测量 \"多少比例的 episodes 恰好一方策略死亡\"——比框架所暗示的更简单。\n- DAF、SCI 可能构成 methodological overengineering。\n- 建议：(1) 更直接描述 78.9% 为 death-rate asymmetry 频率；(2) 强化 non-trivial 发现（72B 不减少 DAF、Reflexion DAF>100%）的呈现。\n\n**N2. [critical] 诊断与处方之间的实际差距限制影响力。**\n- \"在 death-dominated 环境中使用 always-deterministic\" 是平凡建议。\n- Oracle margin 仅 2.89 分——routing 在 ScienceWorld 中 low-value。\n- Decision Framework（Appendix R）有用但被埋在 appendix。\n- 建议：(1) 将 Decision Framework 提升到正文；(2) 更深入讨论 oracle degeneracy 的意义；(3) 讨论 action-level filter vs. router。\n\n### Should-Fix 问题\n\n**W1. [warning] Cluster bootstrap K=11 低于推荐阈值。**\n- Cohen's d=3.02 可能反映 binary structure 而非 massive effect。\n- 建议明确推荐 non-clustered CI 为 primary inference。\n\n**W2. [warning] 72B scaling 证据不足——单一模型、无 bootstrap CI、\"persistent under 10× scaling\" 过于绝对。**\n\n**W3. [warning] Router negative result 可能被 extreme class imbalance 混淆（90.5% det-preferred）。**\n- 建议 frame 为 \"inconclusive under current data regime\"。\n\n**W4. [warning] 跨环境探测提供的框架泛化性证据有限。**\n- MATH 仅确认无误报，ALFWorld non-tie labels 太少（35, 16）。\n- 两个环境都未展示框架 decompose 多种机制的能力。\n\n### 小问题\n- §2.4 近似 break down 条件未讨论\n- 61.2% no-preference base rate 应更突出\n- Table 2 Trained Router 用 single seed vs. full episode set，公平性存疑\n- SCI=0.2147 在 10/11 death-dominant 时解释价值有限\n\n### Questions\nQ1. 包含全部 30 种 task types 后 label fraction 如何变化？\nQ2. focus on 作为唯一 death trigger——简单 action filter 能否替代 router？\nQ3. Grounding ablation 后框架诊断是否改变？\nQ4. Death-priority rule 替换为 continuous severity weighting 后结论是否 robust？\nQ5. Oracle degeneracy 是否意味着 ScienceWorld 不适合作为 routing testbed？\n\n### Missing References\n- LLM 不确定性估计（Kadavath et al., 2022）\n- MoE token-level routing 文献\n（无 critical omissions）\n\n### Scores\nSoundness 4/5, Excitement 3/5, Overall 3.5 (Borderline Conference), Confidence 4/5\n\n---\n\n**请逐条回应上述所有 Must-Fix (N1-N2)、Should-Fix (W1-W4)、小问题、Questions (Q1-Q5)、Missing References，并说明是否调整你的 Overall 评分。**"
  }
}
```

</details>

---


### Tool result

_source line 2545 · 2026-05-23T03:55:18.448040+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1361
}
```

</details>

---


### Assistant

_source line 2546 · 2026-05-23T03:55:21.804430+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 210

## Round 210

2 recorded events


### User

_source line 2547 · 2026-05-23T03:55:24.431676+00:00_

[Reviewer 1 审稿结果]:
审稿意见已完整提交给 Review Director。

**审稿结论摘要**：

- **Overall**: 3.5 (Borderline Conference)
- **Soundness**: 4/5 — 方法论严谨，counterfactual 设计 sound，robustness checks 充分
- **Excitement**: 3/5 — 框架有方法论价值，但核心发现新颖性受限（death dominance 部分为环境设计的数学后果）
- **Confidence**: 4/5

**两个 Critical Issues**：
1. 核心发现的新颖性受限——78.9% label fraction 本质是 "多少 episodes 恰好一方策略死亡" 的频率统计，DAF 在 P=100 下 mechanically high；建议强化 non-trivial findings（72B 不减少 DAF、Reflexion DAF>100%）的呈现
2. Diagnostic-only 无 prescriptive insight——oracle margin 仅 2.89 分表明 routing 在 ScienceWorld 中 value 极低；建议将 Decision Framework 从 Appendix R 提升到正文

**主要优势**：跨模型复制（3 families, DAF 88-90%）、21 个 appendix 的 exceptional thoroughness、honest negative result reporting。

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

_source line 2548 · 2026-05-23T03:55:36.039436+00:00_

Reviewer 1 交叉回应已收到，维持 3.5 (Borderline Conference)。等待 Reviewer 2 交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 211

## Round 211

2 recorded events


### User

_source line 2549 · 2026-05-23T03:57:20.961302+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 Reviewer 2 审稿意见

---

### Weaknesses 逐条回应

**[AGREE] R2-W1: 核心发现新颖性存疑——death dominance 在 death-penalty 环境中部分是同义反复。**
同意这是论文的主要弱点。我在 N1 中提出了几乎相同的观点。补充两点：
1. 论文实际上已经将 label fraction (78.9%) 作为 primary metric（§2.4: "We treat the label fraction (78.9%) as the primary, penalty-invariant diagnostic"），但标题和 framing 确实过于偏重 DAF。
2. 不过，R2 说 "78.9% 也是 Algorithm 1 death-priority rule 的设计后果" 需要精确化——Algorithm 1 保证单方死亡 episode 被分类为 death-determined，但 78.9% 不是 tautological：如果两种策略死亡率接近（δ→0），death-asymmetric episodes 会很少，78.9% 会很低。78.9% 的 non-trivial content 在于 δ=26.6pp（42.9% vs. 16.3%）这个经验事实。论文应更清楚地论证这一点。

**[PARTIALLY AGREE] R2-W2: "Deterministic" 策略的特权性质限制发现通用性。**
R2 提出了一个我没有充分展开的好问题：ScienceWorld 的 death avoidance 是否本质上也是 information asymmetry（如 ALFWorld）？

同意的部分：deterministic strategy 确实是 privileged oracle，死亡率差异部分归因于信息不对称。这一混淆是真实的方法论限制。

不同意的部分：论文在 §5 "Non-triviality and oracle confound" 中提供了关键证据——Δ_nd = 2.84（仅占 full gap 的 9.6%）。如果信息特权是普遍优势而非特定于死亡避免，我们应期望 Δ_nd 也很大。Δ_nd 极小说明 oracle 的优势*集中在*死亡避免上，而非广泛的信息优势。此外，ALFWorld 框架诊断结果为 DAF=0%（§3.4），表明框架能区分 "death avoidance" 和 "information asymmetry" 两种不同机制。

建议作者在 rebuttal 中更突出 Δ_nd = 2.84 这一证据来回应此 concern。

**[PARTIALLY AGREE] R2-W3: 环境覆盖过窄。**
同意这是限制。但我认为 R2 的要求（"至少一个不同的 catastrophic-failure 环境"）稍显苛刻，因为：
1. 论文标题明确限定为 ScienceWorld（"A Counterfactual Analysis on ScienceWorld"）；
2. 论文反复区分 methodological generality 和 empirical generality（Abstract, §1, Limitations）；
3. MATH 和 ALFWorld 验证的是*框架的可复用性*，不是*发现的迁移性*。

该限制确实影响 excitement，但不应被视为 soundness 问题。

**[AGREE] R2-W4: Non-death component (21.1%) 分析不足。**
这是我遗漏的有效观点。20 个 non-death non-tie labels 的来源未被系统分析。仅有一个 case study（Appendix U: find-non-living-thing，Δ_nd=+9.58）。如果能对这 20 个 labels 进行 failure mode decomposition（类似 Appendix N 对 death labels 的分析），将大幅增强框架的 decomposition 价值。

**[AGREE] R2-W5: Abstract 数字过密。**
同意。7 个统计量对 abstract 来说过于密集。Cohen's d=3.02 不应出现在 abstract——它需要 K=11 的 context 才能正确解读（§3.1），放在 abstract 中 misleading。

**[AGREE] R2-W6: Discussion/Conclusion 重复度高，Conclusion 过短。**
同意。Conclusion 仅 3 句话，缺少对框架更广泛意义的 forward-looking 讨论。Discussion §5 与 Introduction §1 在 framing 上有明显重复。

**[PARTIALLY AGREE] R2-W7: 100% deaths 来自 focus on → 可修复的 grounding bug。**
同意观察本身正确且重要——Appendix N 确认所有 105 次死亡源自 `focus on`，Appendix O 的 grounding ablation 降低 death 19pp。这是论文最 actionable 的发现之一。

但 "可修复的 grounding bug" 过于简化：
1. Grounding ablation 后死亡率仍为 ~29%（vs. deterministic 16.3%），gap 仍有 ~13pp（Appendix O）。Grounding 不能完全消除问题。
2. `focus on` 不是简单的 invalid action——它在非死亡上下文中是合法操作（Appendix N: "focus on is in the action space"）。死亡发生在特定 *state-action sequence* 中，不仅是单一 action。
3. 框架的价值在于*诊断*这一结构，即使修复路径相对简单。

**[AGREE] R2-W8: "Deterministic" 术语可能误导。**
完全同意。三个环境中 "deterministic" 含义完全不同（ScienceWorld: ground-truth simulator; MATH: code interpreter; ALFWorld: admissible-action enumeration）。"Privileged" 或 "oracle-assisted" 更准确，且能自然引导读者思考信息特权的角色（与 W2 相关）。

**[AGREE] R2-W9: 2026 concurrent work 引用。**
Info-level concern，同意。无法验证 preprint 引用的准确性，但这是 fast-moving field 的常见问题。

---

### Questions 逐条回应

**R2-Q1: P=0 时 label fraction 是否变化？**
不变化。Algorithm 1 的 death-priority rule 检查 death status（d(τ) ∈ {0,1}），不检查 scores。§2.4 明确说明："the labeling function itself is penalty-independent (Algorithm 1)"。§3.1 中 "at P=0 these reduce to ties" 指的是*如果去掉 death-priority rule*的假设情境，不是 Algorithm 1 的实际行为。78.9% 在任何 P 下都相同。

**R2-Q2: Dense-reward 环境下 framework 是否仍需 episode-level？**
好问题。在 dense-reward 环境中 per-step oracle 可能有效（每步都有 informative reward signal），episode-level 可能不是 necessary granularity。框架的 episode-level 设计是针对 sparse-reward 退化（97.4% per-step tie rate, §2.2）的解决方案，不是 universal prescription。论文应在 §2.2 中更明确说明适用条件。

**R2-Q3: Gemma-2 排除 find-non-living-thing 后 DAF 89.7%→99.9% 的敏感性。**
有效观察，但这是框架正确诊断二元结构的表现而非缺陷：10/11 death-prone types 产生 100% death-asymmetry labels，唯一例外是 find-non-living-thing（0% death, Δ_nd=+9.58）。移除唯一例外使 DAF→100% 是数学必然。这实际上*加强*了论文的 "binary property" 论断（§3.1: "the framework diagnoses a binary property"）。但我同意这种敏感性应在正文中明确讨论。

**R2-Q4: T_max=100 是否能在 excluded tasks 中发现 non-death signal？**
有趣的实验建议。论文在 Limitations 中承认 "increasing the step budget could surface non-death-dominated signal"，但未实际测试。T_max=100 可能允许 agent 在当前超时的 task types 中完成任务，potentially surfacing non-death routing signal。这是一个 constructive suggestion。

**R2-Q5: Task-type classifier 64.7% → lookup table 替代 router？**
论文已在 §3.6 回应：LOTO 下 classifier 退化到 50.0%。所以它只学到了 task-type identity，没有 cross-task generalizable signal。作为 lookup table 它 "works" within seen types，但这正是论文的 point——signal 是 task-type-level binary property，不是可泛化的 routing feature。

---

### Missing References 回应

**1. Hallucination detection/mitigation 文献缺失。**
[PARTIALLY AGREE] 论文讨论了 hallucination 作为 death 的机制（§1: "the model may hallucinate state changes"），但未引用 hallucination detection 文献。考虑到 "death avoidance" 实质上是 "hallucination-induced catastrophic failure avoidance"，引用这方面工作（如 Kadavath et al., 2022; Manakul et al., 2023）可以强化论文的实际意义讨论。但这不是 critical omission——论文的焦点是 routing signal decomposition，不是 hallucination mitigation。

**2. Non-agent adaptive computation 讨论过于简略。**
[PARTIALLY AGREE] §4 已引用 Mixture-of-Depths, speculative decoding, Switch Transformer, GShard。但 R2 的 concern 可能指向更广泛的 adaptive computation 文献（如 early exiting, conditional computation）。这些与论文的 granularity discussion 相关但不 critical。

**3. Reward shaping 文献 (Eschmann et al., 2021)。**
[NEUTRAL] 与 penalty structure 如何影响 signal 相关，但论文已通过 Appendix K (Penalty Sensitivity) 实证分析了 P 的影响。引用 reward shaping 理论工作可以提供更强的理论锚点，但不是必需的。

---

### 评分调整评估

阅读 R2 意见后，我识别了以下我遗漏的有效 concerns：
1. **W4 (non-death labels 分析不足)** — 21.1% 的 non-death routing labels 未被系统分析，削弱了 "decomposition" 的完整性。
2. **W8 (terminology)** — "deterministic" 术语确实 misleading，且与 W2 的信息特权 concern 相关联。
3. **W2 的深度** — information privilege confound 比我 initially assessed 的更 nuanced。虽然 Δ_nd=2.84 提供了 partial defense，但无法完全排除 oracle advantage 集中在 dangerous situations 的可能。

但 R2 在以下方面过于严厉：
1. **Novelty (W1)** — R2 接近 "tautological" 的定性过强。78.9% 的经验内容是 δ=26.6pp，这不是 trivially predictable。
2. **环境覆盖 (W3)** — 论文标题和全文已明确 scope 到 ScienceWorld，MATH/ALFWorld 是 boundary probes 而非 validation。要求另一个 catastrophic-failure 环境对 single paper scope 来说过高。
3. **Grounding bug (W7)** — "可修复" 过于乐观，grounding 后仍有 ~13pp gap。

**最终评分：维持 Overall 3.5 (Borderline Conference)，不调整。**

理由：
- R2 的 W4 和 W8 是 valid new concerns，但属 should-fix 级别，不改变 overall picture。
- 论文的核心优势（methodological rigor, cross-model replication, transparent negative result, extensive robustness checks）仍然 solid。
- R2 的 Excitement 2.5/5 我认为偏低——框架的方法论贡献有 reuse value，router training negative result 对社区有信息量。
- 但 R2 的 novelty concern（我也提出了）确实阻止我给 4.0 (Conference)。

如果作者在 rebuttal 中能：(1) 补充 non-death labels 的系统分析，(2) 更突出 Δ_nd=2.84 对 oracle confound 的回应，(3) 将 Decision Framework 提升到正文——我会考虑将评分提升至 3.5-4.0 之间。

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

_source line 2550 · 2026-05-23T03:57:33.322401+00:00_

Reviewer 1 交叉回应已收到，维持 3.5 (Borderline Conference)。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 212

## Round 212

2 recorded events


### User

_source line 2551 · 2026-05-23T03:57:35.871396+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心判断：R2 的 W4（non-death labels 分析不足）和 W8（terminology misleading）是我遗漏的有效 concerns，但 R2 在 novelty（接近 tautological 定性过强）和环境覆盖要求上偏严。维持 Overall 3.5 (Borderline Conference) 不调整。主要分歧在 Excitement：R2 给 2.5，我给 3——我认为方法论框架的 reuse value 和 router training negative result 的信息量值得 3 分。

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

_source line 2552 · 2026-05-23T03:57:41.342962+00:00_

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


## Round 213

## Round 213

12 recorded events


### User

_source line 2553 · 2026-05-23T03:57:43.618854+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1

---

### Must-Fix 问题

**[AGREE] R1-N1: 核心发现新颖性受限——death dominance 部分是数学必然。**

完全同意，这与我的 W1 (critical) 高度一致。R1 的表述更精炼——"78.9% label fraction 本质上测量'多少比例的 episodes 恰好一方策略死亡'——比框架所暗示的更简单"——我认为这是对该问题最准确的一句话概括。

补充我的 W1 中的额外论点：DAF 的公式结构 δP/(δP + Δ_nd) 在 P=100, Δ_nd=2.84 的条件下几乎注定给出 >90% 的值。论文自己在 Section 2.4 承认这是 "a mathematical consequence rather than an empirical finding"。R1 建议 "更直接描述 78.9% 为 death-rate asymmetry 频率" 是正确的方向。

但我想补充一点 R1 未提及的：**论文对 DAF 和 SCI 的 methodological overengineering（R1 用语）实际上可能是防御性写作的结果**——作者预见到 "这不是显而易见的吗" 这类批评，用大量形式化指标来包装一个本质上简单的发现。这种写作策略反而适得其反，增加了认知负担而未增加新颖性。

**[AGREE] R1-N2: 诊断与处方之间的实际差距限制影响力。**

同意，且我在 Excitement 评分（2.5/5）中已将此作为主要扣分理由。R1 的具体建议很有建设性：

1. **将 Decision Framework 提升到正文**——同意。Appendix R 的三阶段决策框架（pilot collection → death dominance check → decision）是论文最具 actionability 的贡献，但被埋在第 18 个 appendix 中。如果放入正文，论文从 "diagnostic finding" 升级为 "diagnostic + prescriptive framework"，影响力会显著提升。

2. **更深入讨论 oracle degeneracy**——同意。Oracle margin 仅 2.89 分（Table 2: -6.58 vs -9.47）意味着即使有完美路由知识，在 ScienceWorld 中 routing 的价值上限极低。这实际上是论文最具 practical significance 的发现之一（"不要在这个环境上花时间训练 router"），但在正文中被低估了。

3. **讨论 action-level filter vs. router**——同意，且与我的 W7 相呼应。Appendix O 表明 action-space filtering 降低死亡率 19pp，成本远低于 router training。这进一步削弱了 learned routing 在此环境的价值。

---

### Should-Fix 问题

**[REBUT] R1-W1: Cluster bootstrap K=11 低于推荐阈值。**

论文已经充分处理了这一问题。Section 3.1 明确写道："readers should rely on the non-clustered episode-level bootstrap ([81.1%, 99.0%])"。Appendix E 进一步声明 "We retain this analysis for transparency; readers should rely on the non-clustered episode-level bootstrap (§3.1) as the primary inference"。Cohen's d=3.02 附有 "interpret cautiously given K=11 task types" 的限定语（Section 3.1）。

R1 说 "Cohen's d=3.02 可能反映 binary structure 而非 massive effect"——这是一个 valid 的 statistical nuance，但论文在 Appendix E 中已经用 "The high within-task consistency of death patterns (all-or-nothing per task type) suggests high ICC" 间接回应了这一点。d=3.02 确实反映的是 binary structure（10/11 task types death-dominant），而非连续效应量——但论文的核心 claim 正是关于这种 binary structure 的，所以这不构成对论文的批评。

**建议：不需要额外修改**，现有的自我限定已足够。

**[AGREE] R1-W2: 72B scaling 证据不足。**

同意。Section 3.3 报告 72B DAF = 92.4%，但未提供 bootstrap CI。Appendix M Table 中 72B 行的 DAF 95% CI 列标注为 "---"。论文在 Limitations 中承认 "The 72B probe is limited to a single model without cross-model replication at scale"，但 Introduction 中 "persistent under 10× scaling" 的措辞确实过于绝对。

补充：72B 的 deterministic 策略也是独立收集的（Section 3.3: "both strategies independently collected at 72B, 255 episodes"），这意味着 72B 的 δ 和 Δ_nd 都是重新计算的，不是从 7B 数据推断的——这增加了 72B 结果的可信度，但单模型、无 CI 的问题仍然存在。

**[AGREE] R1-W3: Router negative result 可能被 extreme class imbalance 混淆。**

部分同意。论文在 Section 3.6 试图论证 imbalance 是 death dominance 的后果而非独立 confound（"The minority rate is a direct consequence of death dominance"），但 R1 的观点有道理：90.5% 的 class imbalance 意味着在 95 个 training labels 中只有 9 个 internal-preferred——如此稀少的正例可能使任何分类器都无法学习，不论底层信号是否存在。

论文在 Appendix J (Table 6) 的 text augmentation ablation 显示 25%-800% 的数据量变化（但保持 imbalance）未改善性能，但这不能区分 "signal doesn't exist" 和 "signal exists but drowns in imbalance"——正如 R1 所述。Section 5 (Discussion) 提到需要 ~1,350 paired episodes 来获得 50 个 minority-class samples，说明作者认识到这个问题。

R1 建议 frame 为 "inconclusive under current data regime" 是合理的。但论文目前的 framing（Section 3.6 标题 "A Preliminary Negative Result"）已经部分实现了这种 hedging。

**[AGREE] R1-W4: 跨环境探测提供的框架泛化性证据有限。**

强烈同意，这与我的 W3 (critical) 一致。R1 的表述更精准："两个环境都未展示框架 decompose 多种机制的能力"。

补充我的 W3 中的核心论点：要验证 framework 的通用性，最有力的证据是在另一个有 catastrophic failure 的环境（如 NetHack, Crafter）中复现 death dominance 的诊断。MATH 和 ALFWorld 只展示了 framework 不会 false-positive（MATH）和能检测 information asymmetry（ALFWorld），但没有展示 true-positive replication。

---

### 小问题

**[AGREE] §2.4 近似 break down 条件未讨论。**
Equation (4) Δ_full ≈ δ·P + Δ_nd 的近似残差为 0.23（0.8% of Δ_full），在 ScienceWorld 中误差很小。但论文未讨论什么条件下这个近似会失效——例如当 s̄_surv 不远小于 P 时（某些环境中存活策略的平均分可能接近 P）。这是一个 minor 但 valid 的点。

**[AGREE] 61.2% no-preference base rate 应更突出。**
同意。150/245 episodes 无路由偏好意味着大多数 episode 中两种策略表现相似或都死亡。这个高 base rate 值得在 Section 3.1 更早提及，因为它 contextualizes 了 "routing is only relevant in 38.8% of cases" 这一重要限定。

**[AGREE] Table 2 Trained Router 用 single seed vs. full episode set 公平性存疑。**
Table 2 caption 标注了 "†Single random seed (42)"。Appendix J 提供了 8-seed 分析，但 Table 2 只用了一个 seed 的结果。虽然 footnote 存在，主表中应使用多 seed 结果或标注更醒目。

**[REBUT] SCI=0.2147 在 10/11 death-dominant 时解释价值有限。**
R1 认为 SCI 在几乎所有 task types 都 death-dominant 时价值有限。但 SCI 实际上回答的是一个不同的问题："death-rate differential 是集中在少数 task types 还是分散的？" SCI=0.2147（低集中度）+ top-3 仅占 39.8%（Section 3.1）说明 death dominance 是系统性的而非被个别 outlier task 驱动。这对 anti-cherry-picking 论证有补充价值。不过 R1 的 "methodological overengineering" 批评在 SCI 上是合理的——一个简单的 "all 10 death-prone tasks show positive ΔDR" 就足以传达同样信息。

---

### Questions

**[AGREE] R1-Q1: 包含全部 30 种 task types 后 label fraction 如何变化？**
好问题。Appendix C (Table 2) 显示排除的 19 个任务中 18 个有 positive death asymmetry（mean ΔDR = +38.2pp > included +28.7pp）。如果全部包含，label fraction 很可能≥78.9%（因为排除任务更 death-dominant）。但 7/19 是 agent-floor tasks（两种策略都近零进展），可能产生大量 both-dead no-preference labels。论文应该报告这个数字。

**[AGREE] R1-Q2: focus on 作为唯一 death trigger——简单 action filter 能否替代 router？**
这与我的 W7 高度相关。Appendix O 表明 action-space filtering 降低死亡率 19pp（48% → 29%），且 zero-passthrough rate 说明 `focus on` 是 shallow behavioral pattern。这意味着一个简单的规则（"block focus on during exploration"）就能获得 router 训练的大部分收益。论文应该更 prominently 讨论这一替代方案。

**[AGREE] R1-Q3: Grounding ablation 后框架诊断是否改变？**
很好的问题。如果 action-filtering 后重新收集 counterfactual episodes 并计算 DAF，我预期 DAF 会显著下降（因为 δ 下降）。但论文没有做这个实验——Appendix O 只报告了 filtering 后的死亡率变化，没有重新运行 counterfactual decomposition。**这是一个重要的缺失实验**，因为它直接测试 "death dominance 是否可以通过简单干预消除"。

**[REBUT] R1-Q4: Death-priority rule 替换为 continuous severity weighting 后结论是否 robust？**
论文在 Limitations 中承认 "environments with graded penalties would require modifying Algorithm 1's death-priority rule to a continuous severity weighting"。但在 ScienceWorld 中这个问题不存在：death 是 binary（score = -100 vs. ≥ 0），没有 graded severity。对于 ScienceWorld 的结论，death-priority rule 是 justified 的（Appendix B note: "death yields a fixed -100 regardless of timing"）。这个问题更像是对 future work 的建议，而非对当前结论的质疑。

**[AGREE] R1-Q5: Oracle degeneracy 是否意味着 ScienceWorld 不适合作为 routing testbed？**
这是一个尖锐但重要的问题。Oracle margin 仅 2.89 分（Table 2），96.3% 的 oracle 决策匹配 always-deterministic。这意味着在 ScienceWorld 中，routing 问题本身是 low-value 的——即使有完美路由知识也几乎无法超越简单基线。论文将此 frame 为 "finding"（oracle degeneracy），但更深层的含义是：**ScienceWorld 可能不是研究 routing 的理想环境**，因为 routing decision 在此环境中几乎不 matter。论文应该更直接地讨论这一 meta-level implication。

---

### Missing References

**[AGREE] LLM 不确定性估计（Kadavath et al., 2022）。**
同意。如果 agent 能在 step-level 估计自己 hallucinate 的概率，那么 death prediction（进而 routing）可能变得可行。这与论文 Section 5 Discussion 中 "lightweight death-prediction mechanisms" 的 future work 方向直接相关。

**[REBUT] MoE token-level routing 文献。**
R1 标注 "无 critical omissions"。论文在 Section 4 已引用 Switch Transformer (Fedus et al., 2022) 和 GShard (Lepikhin et al., 2021)，并明确区分了 token-level compute allocation 和 episode-level routing signal decomposition。MoE routing 的 mechanism 与本文的诊断框架差异过大，更多引用不会增加论文的 positioning 清晰度。

---

### 评分调整分析

R1 给 Overall 3.5 (Borderline Conference)，我给 3.0 (Findings)。0.5 分差异的主要来源：

| 维度 | R1 | R2 (我) | 差异来源 |
|------|-----|---------|---------|
| Soundness | 4/5 | 3.5/5 | 我的 W2 (deterministic 策略的 oracle 特权) 是 R1 未提及的关键分歧——oracle privilege 使 "routing signal" 的解读变得模糊 |
| Excitement | 3/5 | 2.5/5 | 我认为 actionability 更低（结论是 "use deterministic"），R1 也认同 N2 但扣分较轻 |

**R1 未提及但我认为重要的问题：**

1. **W2 (critical): Deterministic 策略的 oracle 特权。** R1 完全没有讨论 deterministic 策略是 oracle simulator with ground-truth state access 这一事实。这是我 Soundness 扣分的主要原因——当一方策略拥有完美信息特权时，"death avoidance dominates routing signal" 可能只是 "information privilege prevents catastrophic errors" 的换一种说法。ALFWorld 的分析（Section 3.4）甚至自己诊断出了 "information asymmetry"，但论文没有讨论 ScienceWorld 的 death avoidance 是否同样本质上是 information asymmetry。

2. **W7 (warning): 单一失败模式（100% deaths from `focus on`）。** R1 在 Q2 中间接触及但未作为 weakness 提出。所有 105 个死亡都由同一个动作触发，使 "death avoidance" 实质上变成 "避免一个特定的 grounding failure"。

3. **W8 (warning): "Deterministic" 术语的误导性。** 在三个环境中含义完全不同，R1 未提及。

**R1 提出但我认为不够重要的问题：**

R1-W1 (Cluster bootstrap K=11)：论文已充分处理，不应是 should-fix。

### 最终评分

**我维持 Overall 3.0 (Findings)**，不做调整。

理由：R1 的建设性建议（Decision Framework 提升到正文、更深入讨论 oracle degeneracy）如果采纳会提升论文质量，但不改变我的核心判断——(1) 核心发现的新颖性有限（R1 和我都同意的 N1/W1），(2) deterministic 策略的 oracle 特权使 claim 的通用性存疑（我的 W2，R1 未提及但未 rebut），(3) 环境覆盖过窄（R1 和我都同意的 W4/W3）。这三个问题中任何一个单独可能不足以降到 Findings，但合在一起将论文限制在 Findings 水准：方法论有价值但核心发现的 scope 和 impact 不足以进入主会议。

R1 的 3.5 评分可能源于对 methodological contribution 的更高估值（Soundness 4/5），以及未考虑 oracle privilege 的影响。如果 R1 考虑了 W2（deterministic = oracle privilege），Soundness 可能会降至 3.5，Overall 可能降至 3.0-3.5 之间。

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


### Tool call

_source line 2554 · 2026-05-23T03:58:10.777978+00:00_

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


### Tool call

_source line 2555 · 2026-05-23T03:58:10.929157+00:00_

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


### Tool result

_source line 2556 · 2026-05-23T03:58:10.929752+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T03:43:59.570905+00:00\", \"completed_at\": \"2026-05-23T03:47:40.143917+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 7-8\", \"message\": \"Related Work（p7 全页）+ Discussion/Conclusion（p8 全页）连续 2 页纯文字无任何 display item，视觉节奏单调。审稿人翻到这里可能产生\\\"wall of text\\\"疲劳感。建议：可在 Discussion 中加一个 summary figure 或将 Related Work 中的方法对比做成小表格\"}, {\"severity\": \"info\", \"dimension\": \"page 1-8\", \"message\": \"主文 8 页仅 4 个 display items（2 figure + 2 table），对于实证为主的论文偏低（推荐 5-8 个）。大量实验数据被推到 Appendix。审稿人可能感觉主文\\\"证据密度\\\"不足。建议：考虑从 Appendix 提升 1-2 个关键表格/图到主文（如 per-task decomposition Table 3 的精简版，或 cross-environment Figure 4）\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点。Figure 1 出现在 page 2 尚在 3 页窗口内，但 page 1 全文字可能让审稿人第一印象偏\\\"理论/分析\\\"而非\\\"方法+实验\\\"。如果希望强化实证印象，可考虑将 Figure 1 提前至 page 1 底部（需压缩 Abstract 或 Introduction 首段）\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2（death rate vs. trial count）仅有 2 条线（Retry, Reflection），图面较空。可考虑合并更多信息（如加 confidence band 或标注关键阈值线）提高信息密度\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Table 3 和 Table 4 列数较多（7-8 列），字号偏小，在打印状态下可读性可能受影响。建议检查 print-size 下字号是否 ≥ 8pt\"}, {\"severity\": \"info\", \"dimension\": \"page 21\", \"message\": \"Figure 6 的 step-by-step action sequence 标注箭头内文字较小，在缩放/打印下可能难以辨认。建议加大标注字号或简化标注\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 使用 booktabs 风格，格式规范。最优结果已加粗标注（Trained Router 行）。格式合规\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Algorithm 1 伪代码格式清晰，缩进层次分明\"}, {\"severity\": \"info\", \"dimension\": \"page 19\", \"message\": \"Figure 4 跨环境对比条形图颜色区分度好（绿/橙/灰三色），caption 自包含\"}, {\"severity\": \"info\", \"dimension\": \"page 10-12\", \"message\": \"References 格式统一，未见 [?] 未解析引用或格式不一致\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"公式渲染正确（pp.3-4 的数学推导无乱码），无 over
…[truncated 224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 2557 · 2026-05-23T03:58:10.980474+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_30/submitted.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-23T03:44:01.757798+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_f6bffc7e8351600df8091f08a63cd5a0\"}, \"error\": null, \"metadata\": {}}"}

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


### Tool call

_source line 2558 · 2026-05-23T03:59:15.185194+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
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

_source line 2559 · 2026-05-23T03:59:15.235933+00:00_



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

_source line 2560 · 2026-05-23T04:05:49.948513+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "# Round 30 Review Issues (fresh review, 2026-05-23)\n# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作)\n\n# =============================================\n# Carried-over resolved issues (from prior rounds)\n# =============================================\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Wild cluster CI 修正且降级为 sensitivity analysis；non-clustered bootstrap 为主推断\"\n  resolution_round: 24\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Abstract concept-first 重组，数字从 10+ 精简至 3-4 个\"\n  resolution_round: 24\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Ng 1999, Northcutt 2021, DivideMix 已添加并在正确位置引用\"\n  resolution_round: 24\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 24\n  resolution: \"§5 Non-triviality 段有效回应 novelty 质疑\"\n  resolution_round: 24\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组（Self-supervised, Token-level, Task-level, RL-based）\"\n  resolution_round: 19\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"Limitations 新增 pure-strategy upper bound 段落\"\n  resolution_round: 24\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"术语全局修正为 text augmentation\"\n  resolution_round: 24\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导：P=0 时 72% labels 退化为 ties\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"P-invariance 适用范围明确量化\"\n  resolution_round: 24\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"4B router 结论 qualified；完整统计处理\"\n  resolution_round: 24\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors + train/val split 不清晰\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Router claim 从绝对否定改为有条件否定\"\n  resolution_round: 24\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"措辞软化 + effect size detection threshold 完整报告\"\n  resolution_round: 24\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 'fundamental non-learnability' 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R18-N1 解决\"\n  resolution_round: 24\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim — r=0.97 correlation ≠ causal/structural\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"'structurally determined' → 'empirically dominated'\"\n  resolution_round: 24\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 导致 13/28 tasks 不显著，主文未标注为 exploratory\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Per-task 结果标注为 exploratory，power caveat 完整\"\n  resolution_round: 24\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entries + Webb 年份待核实\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"huang2022inner, selfcheckgpt-2023, wang2023voyager 已清理；Webb 2023 (CJE vol.56 no.3) 年份正确\"\n  resolution_round: 24\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman 1999, Mihatsch 2002, Natarajan 2013\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"所有缺失引用已补充\"\n  resolution_round: 24\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引（17 个 appendices A-R）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Appendix Overview with hyperlinks 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M4\"\n  summary: \"§3.1 '54 sole-identified labels' 首次出现未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"术语已修正并定义\"\n  resolution_round: 24\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 inter-annotator agreement 声明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Single annotator caveat 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern — implication 未讨论\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"§5 已讨论 focus on [object] 单一模式\"\n  resolution_round: 24\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R17-M1 解决\"\n  resolution_round: 24\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"§5.4 cross-env 段加交叉引用指向 §2.1 operationalization\"\n  resolution_round: 24\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"Appendix B 加 circularity caveat; Limitations 量化 0.3% 方向冲突 + 60.3% pre-event neutral\"\n  resolution_round: 24\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 引用和讨论深度不足\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"引用已补全；额外解释句因 8 页限制无法加入，现有措辞部分覆盖\"\n  resolution_round: 24\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Algorithm 1 术语修正为 computation modes\"\n  resolution_round: 24\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"§3.1 binary structure 讨论充分\"\n  resolution_round: 24\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"72B decomposition 完整报告\"\n  resolution_round: 24\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"被 R20-N2 取代并解决\"\n  resolution_round: 24\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"Appendix L 已引用\"\n  resolution_round: 24\n\n- id: \"R19-W1\"\n  summary: \"缺少 penalty magnitude 的实际实验验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"P-invariance by design 论证逻辑覆盖\"\n  resolution_round: 24\n\n- id: \"R19-N1\"\n  summary: \"Framing 内在张力：framework vs finding 定位不清\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 27\n  resolution: \"N2+N4 修复间接解决——Abstract/Conclusion 统一为 empirical analysis + reusable diagnostic methodology。\"\n  resolution_round: 27\n\n- id: \"R26-N3\"\n  summary: \"'Contradicting the routing literature's implicit assumption' 是 strawman framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 26\n  last_seen_round: 27\n  resolution: \"R27 验收确认修复完好。\"\n  resolution_round: 27\n\n- id: \"R28-M2\"\n  summary: \"Pages 7-8 连续两页纯文本无 display item\"\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"8 页限制下无法在 pp.7-8 插入 display item，内容密度已最大化\"\n  resolution_round: 28\n  mentions:\n    - round: 30\n      reviewers: []\n      note: \"视觉审查再次标记 pp.7-8 wall of text，但 8 页限制下仍为 wont_fix\"\n\n- id: \"R28-M4\"\n  summary: \"Figure 2 仅 11 点无 task name label，r=0.97 caveat 不够明确\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 28\n  last_seen_round: 29\n  resolution: \"Figure 2 已缩至 0.38\\\\textwidth。R1 认为保留合理；如需解决页数可再缩或移至 appendix。\"\n  resolution_round: 28\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制——§6 Conclusion 起始于 page 9，有 desk reject 风险\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 30\n  resolution: \"R30 Reviewer 2 确认正文 Sections 1-6 在 8 页以内，符合 EMNLP 2026 要求\"\n  resolution_round: 30\n\n- id: \"R29-N1\"\n  summary: \"正文超出 8 页限制（R20-N1 复发）——Conclusion 溢出至 page 9\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 30\n  resolution: \"R30 Reviewer 2 确认正文 Sections 1-6 在 8 页以内，Limitations 从第 9 页开始，符合 EMNLP 2026 要求\"\n  resolution_round: 30\n\n# =============================================\n# Active issues (R27-R30)\n# =============================================\n\n- id: \"R27-N2\"\n  summary: \"DAF=90.4% 部分是 P=100 penalty 的数学必然，Abstract/Title framing 过度突出\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 30\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：Abstract 78.9% 为 headline，DAF 降为 derived measure\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"部分有效——78.9% 确实是 headline，但 DAF=90.4% 仍以核心数字出现\"\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Abstract 已无 DAF=90.4%，仅 Introduction 需微调加 P=100 限定词\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 论文已将 label fraction 作为 primary metric (§2.4)，但标题和 framing 重心仍偏 DAF。R1: '78.9% 本质上测量 death-rate asymmetry 频率'。R2: DAF/SCI 可能构成 methodological overengineering。建议更直接描述 78.9% 并突出 non-trivial findings (72B, Reflexion DAF>100%)。\"\n  action_items:\n    - round: 30\n      action: \"重构叙事：(1) 更直接描述 78.9% 为 death-rate asymmetry 频率；(2) 突出 72B 不减少 DAF 和 Reflexion DAF>100% 作为 non-trivial findings；(3) 降低 DAF 在标题/framing 中的权重\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-N3\"\n  summary: \"Deterministic strategy 实为 oracle access，跨环境含义不统一，oracle confound 未分离\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 30\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：§2.1 inline 三环境 operationalization\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"Conclusion 仍写 'the diagnostic procedure transfers'，未区分 procedure vs operationalization\"\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] §3.4 缺 explicit caveat 区分 procedure vs finding transferability\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R2 [critical]: death avoidance 可能本质上是 information privilege，ScienceWorld 与 ALFWorld 可能是同一机制。R1 [partially agree]: Δ_nd=2.84 (9.6% of gap) 说明 oracle 优势集中在 death avoidance 而非广泛信息优势。Director: Δ_nd 提供部分但非完全回应。\"\n  action_items:\n    - round: 30\n      action: \"正文中明确讨论 death avoidance vs information privilege 的关系，突出 Δ_nd=2.84 作为回应证据\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-N4\"\n  summary: \"环境覆盖过窄，generalization claims 超出证据——1 个主环境 + 2 个 boundary probes\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Hedging 语言到位，Limitations 已承认。结构性限制。\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 两个 boundary probes 均未复现核心机制，未展示 decompose 多种 mechanisms 的能力。R1: 论文标题已限定 ScienceWorld，要求苛刻但确实限制 excitement。\"\n\n- id: \"R27-W1\"\n  summary: \"Router negative result framing: signal-limited vs data-limited 未区分\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE→consensus] 限定结论 scope 为 'under current data regime'\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE] R1: 90.5% imbalance + n=95 使任何分类器都可能失败，不论信号是否存在。R2 partially agrees。建议 frame 为 'inconclusive under current data regime'。论文标题 'Preliminary Negative Result' 已部分 hedge。\"\n  action_items:\n    - round: 30\n      action: \"§3.6 正文明确 frame 为 'inconclusive under current data regime'，加显式因果链（imbalance 是 death dominance 后果非 confound）\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W2\"\n  summary: \"Actionability 有限——诊断出问题但'然后怎么办'回答不足\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: []\n      note: \"本轮未单独提及。§5 actionability 段已存在。\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE] R1 升级为 critical (N2): oracle margin 仅 2.89 分表明 routing 在 ScienceWorld 中 value 极低。Decision Framework (Appendix R) 有用但被埋在 appendix。R2 同意：'use deterministic' 是平凡建议。建议 Decision Framework 提升到正文。\"\n  action_items:\n    - round: 30\n      action: \"将 Decision Framework (Appendix R) 核心内容提升到正文 §5 Discussion；深入讨论 oracle degeneracy (96.3%) 的 practical significance；讨论 action-level filter vs router\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W4\"\n  summary: \"Excluded tasks (63%) n=5 prescreening 样本量极小\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Taxonomic redundancy 操作定义不透明\"\n    - round: 30\n      reviewers: [1]\n      note: \"R1-Q1: 如果包含全部 30 种 task types 后 label fraction 如何变化？R2 交叉回应同意这是好问题。\"\n\n- id: \"R27-W5\"\n  summary: \"K=11 cluster bootstrap: primary CI [81.1%, 99.0%] 可能 anti-conservative\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1]\n      note: \"处理得当。Cohen's d=3.02 需加 context。\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R1 keeps as warning; R2 rebuts—论文已推荐 non-clustered CI 为主，Appendix E 有 transparency statement，不需额外修改。Director: R2 rebut 有效，论文自我限定已足够。降为 info。\"\n\n- id: \"R28-N1\"\n  summary: \"Episode-level labeling 与 step-level routing 的粒度失配——title/abstract scope 超出方法论覆盖范围\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: []\n      note: \"本轮未单独提及，prior fix 有效\"\n    - round: 30\n      reviewers: []\n      note: \"本轮未提及，prior fix 有效\"\n\n- id: \"R28-W1\"\n  summary: \"72B scaling 仅做 probe 而非完整 replication——缺 router training 和 SCI 分析\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 应标注为 'preliminary probe'\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 单一模型、无 bootstrap CI。R1: 'persistent under 10× scaling' 过于绝对。R2: 72B 两种策略均独立收集增加可信度，但单模型无 CI 问题仍在。\"\n  action_items:\n    - round: 30\n      action: \"§3.3 降级为 'preliminary probe'；补充 72B DAF bootstrap CI；Introduction/Conclusion 措辞改为 'a preliminary 72B probe suggests persistence'\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R28-W2\"\n  summary: \"'Death' 术语限制 generality perception——binary failure vs graded failure 适用性未讨论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: []\n      note: \"本轮未单独提及，prior fix 有效\"\n    - round: 30\n      reviewers: []\n      note: \"本轮未单独提及\"\n\n- id: \"R28-M1\"\n  summary: \"Missing references: Alshiekh et al. (2018), Geifman & El-Yaniv (2017), CALM, MoD\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"R1: FrugalGPT, AutoMix, Options framework。R2: MoD, speculative decoding。\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"R2: 缺 hallucination detection/mitigation 文献（Manakul 2023, Kadavath 2022）；non-agent adaptive computation（early exit, PABEE）讨论过简。R1: LLM 不确定性估计（Kadavath 2022）可强化 future work。R1 partially agrees hallucination refs。\"\n  action_items:\n    - round: 30\n      action: \"§4 加 hallucination detection 引用 + positioning 句；加 non-agent adaptive computation (early exit, PABEE) 引用\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R28-M3\"\n  summary: \"§1 Introduction 'signal diversity can collapse' 重复出现\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [2]\n      note: \"Introduction 与 Conclusion contributions 重复，页数超限下应削减\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 78.9% 在论文中重复至少 7 次。Conclusion 仅 3 句过于简短，缺前瞻性内容。Introduction/Discussion/Conclusion 重复度高。\"\n  action_items:\n    - round: 30\n      action: \"Conclusion 增加具体 future work 方向；削减与 Introduction 的重复内容\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R28-M5\"\n  summary: \"Related Work 缺 non-agent adaptive computation（early exit, speculative decoding, MoD）\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 加 1 句 positioning\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE] R2: early exit networks (DeeBERT, PABEE), dynamic networks survey 完全缺失。§4 已引用 MoD 和 speculative decoding 但仅各一次。\"\n\n- id: \"R29-W1\"\n  summary: \"Non-death component (21.1%) 的 routing signal 来源未分析\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 29\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] find-non-living-thing case study 即可大幅改善\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 20 个 non-death non-tie labels 未系统分析来源（hallucination vs suboptimal action vs random variance）。仅 Appendix U 一个 case study。R1: 对全部 20 个 labels 进行 failure mode decomposition 将大幅增强框架 decomposition 价值。\"\n  action_items:\n    - round: 30\n      action: \"对 20 个 non-death labels 进行系统分析：分布特征、任务属性关系、score 差异来源分类\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R29-W2\"\n  summary: \"单一 death mechanism (focus on [object]) 限制 failure mode generalizability\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 29\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 100% deaths 由同一 action pattern。Discussion 应区分 ScienceWorld-specific 和 general framework。\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[PARTIALLY AGREE] R2: grounding ablation 降 19pp，'death avoidance' 实质上是可修复的 grounding bug。R1 rebuts: grounding 后仍 ~29% vs 16.3%，gap ~13pp；focus on 在非死亡上下文中合法。但 R2 指出缺失实验：grounding ablation 后重新收集 counterfactual 并计算 DAF。\"\n  action_items:\n    - round: 30\n      action: \"Discussion 区分 ScienceWorld-specific failure mode 和 general framework；考虑 grounding ablation 后重新计算 DAF 的实验\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R29-M1\"\n  summary: \"Missing references: FrugalGPT, AutoMix, Options framework, Mixture-of-Depths\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 29\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"FrugalGPT + AutoMix 是 LLM routing 直接竞品，必须引用\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"R30 论文已引用 FrugalGPT, AutoMix, MoD, speculative decoding（§4 Related Work 确认）。但 early exit 和 hallucination detection 仍缺。\"\n\n# --- Structural / Long-standing ---\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit——方向可预期\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3.5/5, R2 Excitement 2.5/5。结构性限制，无法通过写作修复。\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 Excitement 2.5/5。持续的结构性限制。\"\n\n# =============================================\n# R30 new issues\n# =============================================\n\n- id: \"R30-W1\"\n  summary: \"'Deterministic' 术语跨环境含义不一致——三个环境含义完全不同，misleading\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE x2] ScienceWorld: ground-truth simulator; MATH: code interpreter; ALFWorld: admissible-action enumeration。R2 建议 'privileged' 或 'oracle-assisted'。R1 完全同意。\"\n  action_items:\n    - round: 30\n      action: \"考虑用 'privileged' 或 'oracle-assisted' 替代 'deterministic'，或在首次定义时更明确说明 umbrella term 性质\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R30-W2\"\n  summary: \"Abstract 仍有 7 个统计量，Cohen's d=3.02 不适合出现在 abstract\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 7 个统计量在 ~200 词 abstract 中过密。Cohen's d 需 K=11 context 才能正确解读，放在 abstract 中 misleading。建议精简至 2-3 个核心数字。\"\n  action_items:\n    - round: 30\n      action: \"Abstract 精简至 2-3 个核心数字（78.9% label fraction, 跨模型范围, cross-environment 对比）；移除 Cohen's d\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R30-W3\"\n  summary: \"Grounding ablation 后未重新收集 counterfactual 计算 DAF——关键缺失实验\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n    - round: 30\n      reviewers: [2]\n      note: \"R2 cross-response to R1-Q3: Appendix O 仅报告 filtering 后死亡率变化，没有重新运行 counterfactual decomposition。直接测试 'death dominance 是否可通过简单干预消除'。\"\n  action_items:\n    - round: 30\n      action: \"考虑 grounding ablation 后重新收集 counterfactual episodes 并计算 DAF（如不可行，在 Limitations 中讨论）\"\n      assigned_to: main_agent\n      status: open"
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
    "issues_yaml": "# Round 30 Review Issues (fresh review, 2026-05-23)\n# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作)\n\n# =============================================\n# Carried-over resolved issues (from prior rounds)\n# =============================================\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Wild cluster CI 修正且降级为 sensitivity analysis；non-clustered bootstrap 为主推断\"\n  resolution_round: 24\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Abstract concept-first 重组，数字从 10+ 精简至 3-4 个\"\n  resolution_round: 24\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Ng 1999, Northcutt 2021, DivideMix 已添加并在正确位置引用\"\n  resolution_round: 24\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 24\n  resolution: \"§5 Non-triviality 段有效回应 novelty 质疑\"\n  resolution_round: 24\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组（Self-supervised, Token-level, Task-level, RL-based）\"\n  resolution_round: 19\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"Limitations 新增 pure-strategy upper bound 段落\"\n  resolution_round: 24\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"术语全局修正为 text augmentation\"\n  resolution_round: 24\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导：P=0 时 72% labels 退化为 ties\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"P-invariance 适用范围明确量化\"\n  resolution_round: 24\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"4B router 结论 qualified；完整统计处理\"\n  resolution_round: 24\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors + train/val split 不清晰\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Router claim 从绝对否定改为有条件否定\"\n  resolution_round: 24\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"措辞软化 + effect size detection threshold 完整报告\"\n  resolution_round: 24\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 'fundamental non-learnability' 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R18-N1 解决\"\n  resolution_round: 24\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim — r=0.97 correlation ≠ causal/structural\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"'structurally determined' → 'empirically dominated'\"\n  resolution_round: 24\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 导致 13/28 tasks 不显著，主文未标注为 exploratory\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Per-task 结果标注为 exploratory，power caveat 完整\"\n  resolution_round: 24\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entries + Webb 年份待核实\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"huang2022inner, selfcheckgpt-2023, wang2023voyager 已清理；Webb 2023 (CJE vol.56 no.3) 年份正确\"\n  resolution_round: 24\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman 1999, Mihatsch 2002, Natarajan 2013\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"所有缺失引用已补充\"\n  resolution_round: 24\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引（17 个 appendices A-R）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Appendix Overview with hyperlinks 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M4\"\n  summary: \"§3.1 '54 sole-identified labels' 首次出现未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"术语已修正并定义\"\n  resolution_round: 24\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 inter-annotator agreement 声明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Single annotator caveat 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern — implication 未讨论\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"§5 已讨论 focus on [object] 单一模式\"\n  resolution_round: 24\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R17-M1 解决\"\n  resolution_round: 24\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"§5.4 cross-env 段加交叉引用指向 §2.1 operationalization\"\n  resolution_round: 24\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"Appendix B 加 circularity caveat; Limitations 量化 0.3% 方向冲突 + 60.3% pre-event neutral\"\n  resolution_round: 24\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 引用和讨论深度不足\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"引用已补全；额外解释句因 8 页限制无法加入，现有措辞部分覆盖\"\n  resolution_round: 24\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Algorithm 1 术语修正为 computation modes\"\n  resolution_round: 24\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"§3.1 binary structure 讨论充分\"\n  resolution_round: 24\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"72B decomposition 完整报告\"\n  resolution_round: 24\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"被 R20-N2 取代并解决\"\n  resolution_round: 24\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"Appendix L 已引用\"\n  resolution_round: 24\n\n- id: \"R19-W1\"\n  summary: \"缺少 penalty magnitude 的实际实验验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"P-invariance by design 论证逻辑覆盖\"\n  resolution_round: 24\n\n- id: \"R19-N1\"\n  summary: \"Framing 内在张力：framework vs finding 定位不清\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 27\n  resolution: \"N2+N4 修复间接解决——Abstract/Conclusion 统一为 empirical analysis + reusable diagnostic methodology。\"\n  resolution_round: 27\n\n- id: \"R26-N3\"\n  summary: \"'Contradicting the routing literature's implicit assumption' 是 strawman framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 26\n  last_seen_round: 27\n  resolution: \"R27 验收确认修复完好。\"\n  resolution_round: 27\n\n- id: \"R28-M2\"\n  summary: \"Pages 7-8 连续两页纯文本无 display item\"\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 28\n  last_seen_round: 30\n  resolution: \"8 页限制下无法在 pp.7-8 插入 display item，内容密度已最大化\"\n  resolution_round: 28\n  mentions:\n    - round: 30\n      reviewers: []\n      note: \"视觉审查再次标记 pp.7-8 wall of text，但 8 页限制下仍为 wont_fix\"\n\n- id: \"R28-M4\"\n  summary: \"Figure 2 仅 11 点无 task name label，r=0.97 caveat 不够明确\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 28\n  last_seen_round: 29\n  resolution: \"Figure 2 已缩至 0.38\\\\textwidth。R1 认为保留合理；如需解决页数可再缩或移至 appendix。\"\n  resolution_round: 28\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制——§6 Conclusion 起始于 page 9，有 desk reject 风险\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 30\n  resolution: \"R30 Reviewer 2 确认正文 Sections 1-6 在 8 页以内，符合 EMNLP 2026 要求\"\n  resolution_round: 30\n\n- id: \"R29-N1\"\n  summary: \"正文超出 8 页限制（R20-N1 复发）——Conclusion 溢出至 page 9\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 30\n  resolution: \"R30 Reviewer 2 确认正文 Sections 1-6 在 8 页以内，Limitations 从第 9 页开始，符合 EMNLP 2026 要求\"\n  resolution_round: 30\n\n# =============================================\n# Active issues (R27-R30)\n# =============================================\n\n- id: \"R27-N2\"\n  summary: \"DAF=90.4% 部分是 P=100 penalty 的数学必然，Abstract/Title framing 过度突出\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 30\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：Abstract 78.9% 为 headline，DAF 降为 derived measure\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"部分有效——78.9% 确实是 headline，但 DAF=90.4% 仍以核心数字出现\"\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Abstract 已无 DAF=90.4%，仅 Introduction 需微调加 P=100 限定词\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 论文已将 label fraction 作为 primary metric (§2.4)，但标题和 framing 重心仍偏 DAF。R1: '78.9% 本质上测量 death-rate asymmetry 频率'。R2: DAF/SCI 可能构成 methodological overengineering。建议更直接描述 78.9% 并突出 non-trivial findings (72B, Reflexion DAF>100%)。\"\n  action_items:\n    - round: 30\n      action: \"重构叙事：(1) 更直接描述 78.9% 为 death-rate asymmetry 频率；(2) 突出 72B 不减少 DAF 和 Reflexion DAF>100% 作为 non-trivial findings；(3) 降低 DAF 在标题/framing 中的权重\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-N3\"\n  summary: \"Deterministic strategy 实为 oracle access，跨环境含义不统一，oracle confound 未分离\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 30\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 修复：§2.1 inline 三环境 operationalization\"\n    - round: 28\n      reviewers: [1, 2]\n      note: \"Conclusion 仍写 'the diagnostic procedure transfers'，未区分 procedure vs operationalization\"\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] §3.4 缺 explicit caveat 区分 procedure vs finding transferability\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R2 [critical]: death avoidance 可能本质上是 information privilege，ScienceWorld 与 ALFWorld 可能是同一机制。R1 [partially agree]: Δ_nd=2.84 (9.6% of gap) 说明 oracle 优势集中在 death avoidance 而非广泛信息优势。Director: Δ_nd 提供部分但非完全回应。\"\n  action_items:\n    - round: 30\n      action: \"正文中明确讨论 death avoidance vs information privilege 的关系，突出 Δ_nd=2.84 作为回应证据\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-N4\"\n  summary: \"环境覆盖过窄，generalization claims 超出证据——1 个主环境 + 2 个 boundary probes\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Hedging 语言到位，Limitations 已承认。结构性限制。\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 两个 boundary probes 均未复现核心机制，未展示 decompose 多种 mechanisms 的能力。R1: 论文标题已限定 ScienceWorld，要求苛刻但确实限制 excitement。\"\n\n- id: \"R27-W1\"\n  summary: \"Router negative result framing: signal-limited vs data-limited 未区分\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE→consensus] 限定结论 scope 为 'under current data regime'\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE] R1: 90.5% imbalance + n=95 使任何分类器都可能失败，不论信号是否存在。R2 partially agrees。建议 frame 为 'inconclusive under current data regime'。论文标题 'Preliminary Negative Result' 已部分 hedge。\"\n  action_items:\n    - round: 30\n      action: \"§3.6 正文明确 frame 为 'inconclusive under current data regime'，加显式因果链（imbalance 是 death dominance 后果非 confound）\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W2\"\n  summary: \"Actionability 有限——诊断出问题但'然后怎么办'回答不足\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: []\n      note: \"本轮未单独提及。§5 actionability 段已存在。\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE] R1 升级为 critical (N2): oracle margin 仅 2.89 分表明 routing 在 ScienceWorld 中 value 极低。Decision Framework (Appendix R) 有用但被埋在 appendix。R2 同意：'use deterministic' 是平凡建议。建议 Decision Framework 提升到正文。\"\n  action_items:\n    - round: 30\n      action: \"将 Decision Framework (Appendix R) 核心内容提升到正文 §5 Discussion；深入讨论 oracle degeneracy (96.3%) 的 practical significance；讨论 action-level filter vs router\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W4\"\n  summary: \"Excluded tasks (63%) n=5 prescreening 样本量极小\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Taxonomic redundancy 操作定义不透明\"\n    - round: 30\n      reviewers: [1]\n      note: \"R1-Q1: 如果包含全部 30 种 task types 后 label fraction 如何变化？R2 交叉回应同意这是好问题。\"\n\n- id: \"R27-W5\"\n  summary: \"K=11 cluster bootstrap: primary CI [81.1%, 99.0%] 可能 anti-conservative\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1]\n      note: \"处理得当。Cohen's d=3.02 需加 context。\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R1 keeps as warning; R2 rebuts—论文已推荐 non-clustered CI 为主，Appendix E 有 transparency statement，不需额外修改。Director: R2 rebut 有效，论文自我限定已足够。降为 info。\"\n\n- id: \"R28-N1\"\n  summary: \"Episode-level labeling 与 step-level routing 的粒度失配——title/abstract scope 超出方法论覆盖范围\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: []\n      note: \"本轮未单独提及，prior fix 有效\"\n    - round: 30\n      reviewers: []\n      note: \"本轮未提及，prior fix 有效\"\n\n- id: \"R28-W1\"\n  summary: \"72B scaling 仅做 probe 而非完整 replication——缺 router training 和 SCI 分析\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 应标注为 'preliminary probe'\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 单一模型、无 bootstrap CI。R1: 'persistent under 10× scaling' 过于绝对。R2: 72B 两种策略均独立收集增加可信度，但单模型无 CI 问题仍在。\"\n  action_items:\n    - round: 30\n      action: \"§3.3 降级为 'preliminary probe'；补充 72B DAF bootstrap CI；Introduction/Conclusion 措辞改为 'a preliminary 72B probe suggests persistence'\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R28-W2\"\n  summary: \"'Death' 术语限制 generality perception——binary failure vs graded failure 适用性未讨论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: []\n      note: \"本轮未单独提及，prior fix 有效\"\n    - round: 30\n      reviewers: []\n      note: \"本轮未单独提及\"\n\n- id: \"R28-M1\"\n  summary: \"Missing references: Alshiekh et al. (2018), Geifman & El-Yaniv (2017), CALM, MoD\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"R1: FrugalGPT, AutoMix, Options framework。R2: MoD, speculative decoding。\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"R2: 缺 hallucination detection/mitigation 文献（Manakul 2023, Kadavath 2022）；non-agent adaptive computation（early exit, PABEE）讨论过简。R1: LLM 不确定性估计（Kadavath 2022）可强化 future work。R1 partially agrees hallucination refs。\"\n  action_items:\n    - round: 30\n      action: \"§4 加 hallucination detection 引用 + positioning 句；加 non-agent adaptive computation (early exit, PABEE) 引用\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R28-M3\"\n  summary: \"§1 Introduction 'signal diversity can collapse' 重复出现\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [2]\n      note: \"Introduction 与 Conclusion contributions 重复，页数超限下应削减\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 78.9% 在论文中重复至少 7 次。Conclusion 仅 3 句过于简短，缺前瞻性内容。Introduction/Discussion/Conclusion 重复度高。\"\n  action_items:\n    - round: 30\n      action: \"Conclusion 增加具体 future work 方向；削减与 Introduction 的重复内容\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R28-M5\"\n  summary: \"Related Work 缺 non-agent adaptive computation（early exit, speculative decoding, MoD）\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 加 1 句 positioning\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE] R2: early exit networks (DeeBERT, PABEE), dynamic networks survey 完全缺失。§4 已引用 MoD 和 speculative decoding 但仅各一次。\"\n\n- id: \"R29-W1\"\n  summary: \"Non-death component (21.1%) 的 routing signal 来源未分析\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 29\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] find-non-living-thing case study 即可大幅改善\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 20 个 non-death non-tie labels 未系统分析来源（hallucination vs suboptimal action vs random variance）。仅 Appendix U 一个 case study。R1: 对全部 20 个 labels 进行 failure mode decomposition 将大幅增强框架 decomposition 价值。\"\n  action_items:\n    - round: 30\n      action: \"对 20 个 non-death labels 进行系统分析：分布特征、任务属性关系、score 差异来源分类\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R29-W2\"\n  summary: \"单一 death mechanism (focus on [object]) 限制 failure mode generalizability\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 29\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 100% deaths 由同一 action pattern。Discussion 应区分 ScienceWorld-specific 和 general framework。\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[PARTIALLY AGREE] R2: grounding ablation 降 19pp，'death avoidance' 实质上是可修复的 grounding bug。R1 rebuts: grounding 后仍 ~29% vs 16.3%，gap ~13pp；focus on 在非死亡上下文中合法。但 R2 指出缺失实验：grounding ablation 后重新收集 counterfactual 并计算 DAF。\"\n  action_items:\n    - round: 30\n      action: \"Discussion 区分 ScienceWorld-specific failure mode 和 general framework；考虑 grounding ablation 后重新计算 DAF 的实验\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R29-M1\"\n  summary: \"Missing references: FrugalGPT, AutoMix, Options framework, Mixture-of-Depths\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 29\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"FrugalGPT + AutoMix 是 LLM routing 直接竞品，必须引用\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"R30 论文已引用 FrugalGPT, AutoMix, MoD, speculative decoding（§4 Related Work 确认）。但 early exit 和 hallucination detection 仍缺。\"\n\n# --- Structural / Long-standing ---\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit——方向可预期\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 30\n  mentions:\n    - round: 29\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3.5/5, R2 Excitement 2.5/5。结构性限制，无法通过写作修复。\"\n    - round: 30\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 Excitement 2.5/5。持续的结构性限制。\"\n\n# =============================================\n# R30 new issues\n# =============================================\n\n- id: \"R30-W1\"\n  summary: \"'Deterministic' 术语跨环境含义不一致——三个环境含义完全不同，misleading\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE x2] ScienceWorld: ground-truth simulator; MATH: code interpreter; ALFWorld: admissible-action enumeration。R2 建议 'privileged' 或 'oracle-assisted'。R1 完全同意。\"\n  action_items:\n    - round: 30\n      action: \"考虑用 'privileged' 或 'oracle-assisted' 替代 'deterministic'，或在首次定义时更明确说明 umbrella term 性质\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R30-W2\"\n  summary: \"Abstract 仍有 7 个统计量，Cohen's d=3.02 不适合出现在 abstract\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n    - round: 30\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 7 个统计量在 ~200 词 abstract 中过密。Cohen's d 需 K=11 context 才能正确解读，放在 abstract 中 misleading。建议精简至 2-3 个核心数字。\"\n  action_items:\n    - round: 30\n      action: \"Abstract 精简至 2-3 个核心数字（78.9% label fraction, 跨模型范围, cross-environment 对比）；移除 Cohen's d\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R30-W3\"\n  summary: \"Grounding ablation 后未重新收集 counterfactual 计算 DAF——关键缺失实验\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n    - round: 30\n      reviewers: [2]\n      note: \"R2 cross-response to R1-Q3: Appendix O 仅报告 filtering 后死亡率变化，没有重新运行 counterfactual decomposition。直接测试 'death dominance 是否可通过简单干预消除'。\"\n  action_items:\n    - round: 30\n      action: \"考虑 grounding ablation 后重新收集 counterfactual episodes 并计算 DAF（如不可行，在 Limitations 中讨论）\"\n      assigned_to: main_agent\n      status: open"
  }
}
```

</details>

---


### Tool result

_source line 2561 · 2026-05-23T04:05:50.100423+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 26337}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2562 · 2026-05-23T04:08:50.675555+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "simgate-modular-routing",
  "report": "# Round 30 审稿报告 — simgate-modular-routing\n\n**论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计；R2: 新颖性+完整性+写作）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮收敛，核心问题达成共识）\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual diagnostic framework，用于分析 LLM agent routing signal 的机制组成。在 ScienceWorld 环境（11/30 task types，245 episodes）中发现 78.9% 的 non-tie routing labels 源自 death asymmetry，DAF 在 P=100 下达 90.4%。跨模型复制（3 个 7-9B 模型族，DAF 88-90%）、agent improvement baselines（Retry, Reflexion, 72B）、跨环境探测（MATH 无信号、ALFWorld 信息不对称）提供支撑。Step-level router 训练得到接近随机的结果，框架诊断其原因为 death avoidance 是 task-type-level 二元信号。\n\n## Strengths\n\n**S1. 方法论设计优雅有效。** [R1-S1, R2-S1; AGREE] Per-step oracle 在 sparse-reward 环境下退化为 97.4% 平局率的观察本身是方法论贡献。Episode-level counterfactual comparison 在相同初始条件下运行，干净隔离 computation mode 为唯一变量。\"先诊断再构建\"的思路填补了 routing 文献中的重要缺口。\n\n**S2. 统计分析严谨且透明度极高。** [R1-S2, R2-S2; AGREE] 21 个 Appendix (A-U) 覆盖 labeling quality audit、cluster bootstrap sensitivity、leave-one-task-out、seed robustness、penalty sensitivity、failure mode analysis、grounding ablation、extended validation 等。对小样本聚类推断局限性（K < 20-50）的诚实披露在 NLP 论文中罕见。\n\n**S3. 跨模型复制令人信服。** [R1-S4, R2-S3; AGREE] 三个架构不同的模型族（Qwen2.5-7B、Llama-3.1-8B、Gemma-2-9B-it）收敛于 DAF 88-90%（spread 仅 2.2pp），10× scaling 到 72B 未消除 death dominance（DAF = 92.4%），有力排除 model-specific 解释。\n\n**S4. Claims 与证据校准审慎。** [R1-S3, R2-S4; AGREE] 论文反复区分 methodological generality 与 empirical generality，将 MATH/ALFWorld 定位为 boundary probes 而非 cross-domain validation，以 label fraction (78.9%) 而非 DAF 作为 primary metric。Limitations 部分（约 1.5 页）极其详尽，自我批判性极强。\n\n**S5. 负面结果的诊断价值。** [R1-S5, R2-S5; AGREE] Router 训练失败被转化为对信号结构的洞察：step-level signal 不存在因为 death avoidance 是 task-type-level 二元信号。两种平衡解释（noise-dominated vs. non-learnability）的呈现方式值得称赞。\n\n**S6. Oracle degeneracy 与 anti-cherry-picking 论证。** [R1-S6, R2-S6; AGREE] Always-deterministic 匹配 96.3% 的 oracle 决策，直接表明 routing 在 ScienceWorld 中价值极低——这本身是重要实证发现。排除的 19 个任务 ΔDR (+38.2pp) 高于包含的 11 个 (+28.7pp)，排除选择性报告嫌疑。\n\n## Weaknesses\n\n### Critical\n\n**C1. 核心发现新颖性受限——death dominance 部分是环境设计的数学必然。** [R1-N1, R2-W1; AGREE]\n\nDAF = δP/(δP + Δ_nd) 在 P=100 >> Δ_nd=2.84 条件下 mechanically >90%——论文自己承认是 \"mathematical consequence rather than empirical finding\"（§2.4）。78.9% label fraction 虽然 penalty-invariant，但本质上测量\"多少比例的 episodes 恰好一方策略死亡\"（R1 表述）——比框架暗示的更简单的频率统计。\n\nR1 指出：78.9% 的 non-trivial content 在于 δ=26.6pp（42.9% vs. 16.3%）这个经验事实，但论文未充分论证这一差异为何不可事先预期。论文用大量形式化指标（DAF、SCI）包装了一个相对简单的发现，可能构成 methodological overengineering（R1 用语）。R2 补充：这种防御性写作策略增加了认知负担而未增加新颖性。\n\n真正 non-trivial 的发现——72B 不减少 DAF、Reflexion 使 DAF>100%——在论文中被置于次要位置。两位 Reviewer 均建议将这些发现提前并突出呈现。\n\n**C2. 诊断与处方之间的实际差距限制影响力。** [R1-N2, R2 agrees]\n\n从诊断得出的实际建议——\"在 death-dominated 环境中使用 always-deterministic\"——是平凡结论，不需要本框架推导。Oracle margin 仅 2.89 分（Table 2: -6.58 vs -9.47），意味着 routing 在 ScienceWorld 中 value 上限极低，进一步削弱了 routing signal 分析的动机。\n\n最具 actionability 的贡献——Decision Framework（Appendix R）和 \"50-episode pilot suffices for build-vs-buy decisions\"——被埋在 appendix 中。两位 Reviewer 均建议将 Decision Framework 提升到正文 Discussion。\n\n### Warning\n\n**W1. [DIVERGENCE] Deterministic 策略的 oracle 特权使 \"routing signal\" 解读模糊。** [R2-W2 critical; R1 partially agrees as warning]\n\nScienceWorld 的 deterministic 策略是 oracle simulator with ground-truth state access——privileged information baseline，非实际可用工具。R2 核心论点：死亡率差异可归因于信息不对称，\"routing signal is death-dominated\" 可能只是 \"information privilege prevents catastrophic errors\" 的换一种说法。ALFWorld 分析诊断为 \"information asymmetry\"（§3.4）——ScienceWorld 是否同样如此？\n\nR1 提供 partial defense：Δ_nd = 2.84（仅 9.6% of full gap）说明 oracle 优势集中在死亡避免上，而非广泛信息优势。框架能区分两种机制（ScienceWorld DAF=90.4% vs. ALFWorld DAF=0%）。\n\nDirector 判断：R2 的 concern 有效但 R1 的 Δ_nd 证据提供了部分回应。论文应在正文中更明确讨论此问题。Severity 维持 warning。\n\n**W2. 环境覆盖过窄，跨环境 probes 未复现核心机制。** [R1-W4, R2-W3; AGREE]\n\nMATH 无 routing signal，ALFWorld 信号来源不同——都未复现 death dominance。两个环境都未展示框架将 routing signal decompose 为多种 contributing mechanisms 的能力（R1 表述更精准）。R1 注意到论文标题已限定 ScienceWorld，但 R2 指出至少一个不同 catastrophic-failure 环境（如 NetHack, Crafter）的验证将大幅增强说服力。\n\n**W3. Non-death component (21.1% of labels) 分析不足。** [R2-W4, R1 agrees]\n\n20 个 non-death non-tie labels 的来源未系统分析。仅 Appendix U 一个 case study（find-non-living-thing）。未分析 labels 的分布特征、任务属性关系、score 差异来源（hallucination vs. suboptimal action vs. random variance）。R1 指出对全部 20 个 labels 的 failure mode decomposition 将大幅增强框架 decomposition 价值。\n\n**W4. 72B scaling 证据不足以支撑 \"persistent under 10× scaling\"。** [R1-W2, R2 agrees]\n\n单一模型（Qwen2.5-72B）、单一 family、未报告 72B DAF bootstrap CI。Introduction 和 Conclusion 中 \"persistent under 10× scaling\" 过于绝对。建议降级为 \"a preliminary 72B probe suggests persistence\"。\n\n**W5. Router negative result 可能被 extreme class imbalance 混淆。** [R1-W3, R2 partially agrees]\n\n90.5% det-preferred，仅 9 个 internal-preferred episodes。Text augmentation 无改善和 LOTO 退化到 chance 不能区分 data limitation 和 signal limitation。建议 frame 为 \"inconclusive under current data regime\"。论文标题 \"A Preliminary Negative Result\" 已部分 hedge。\n\n**W6. \"Deterministic\" 术语跨环境含义不一致。** [R2-W8, R1 agrees]\n\nScienceWorld: ground-truth simulator；MATH: code interpreter；ALFWorld: admissible-action enumeration。三个环境中 \"deterministic\" 含义完全不同。\"Privileged\" 或 \"oracle-assisted\" 更准确，且能引导读者思考信息特权的角色。\n\n**W7. 100% deaths 来自 focus on 单一模式——削弱 \"death avoidance\" 概念的一般性。** [R2-W7, R1 partially agrees]\n\nAppendix N 确认所有 105 次死亡由同一动作触发。Grounding ablation 降低 death 19pp（Appendix O）。R1 反驳：grounding 后死亡率仍 ~29%（vs. deterministic 16.3%），gap 仍 ~13pp；focus on 在非死亡上下文中是合法操作。但 R2 在交叉回应中指出关键缺失实验：grounding ablation 后重新收集 counterfactual episodes 并计算 DAF——直接测试 \"death dominance 是否可通过简单干预消除\"。\n\n**W8. Abstract 数字过密，可读性差。** [R2-W5, R1 agrees]\n\n7 个统计量在 ~200 词 abstract 中。Cohen's d=3.02 不应出现在 abstract——需 K=11 context 才能正确解读。建议精简至 2-3 个核心数字。\n\n**W9. Discussion/Conclusion 与 Introduction 重复度高。** [R2-W6, R1 agrees]\n\n78.9% 在论文中重复至少 7 次。Conclusion 仅 3 句，缺前瞻性内容。Discussion 前两段大量重复 Experiments 内容。Conclusion 应提供具体 future work 方向。\n\n### Info\n\n**I1.** 61.2% no-preference base rate 应更突出——routing 仅在 38.8% cases 中 relevant。[R1, R2 agrees]\n\n**I2.** Table 2 Trained Router 用 single seed (42) vs. full episode set，公平性存疑。[R1, R2 agrees]\n\n**I3.** §2.4 DAF 近似 break down 条件未讨论——当 s̄_surv 不远小于 P 时近似误差如何变化。[R1, R2 agrees]\n\n## Reviewer Consensus\n\n以下问题双方明确达成 [AGREE]：\n\n1. **核心发现新颖性受限**（C1）——death dominance 在 P=100 环境中部分是数学/设计后果，论文需更清楚论证 non-triviality\n2. **Actionability 不足**（C2）——Decision Framework 应提升到正文，oracle degeneracy 的实际意义需深入讨论\n3. **环境覆盖过窄**（W2）——两个 boundary probes 均未复现核心机制\n4. **Non-death labels 分析不足**（W3）——21.1% 的非死亡 labels 需系统分析\n5. **72B scaling 证据单薄**（W4）——单模型、无 CI，claim 应降级\n6. **\"Deterministic\" 术语误导**（W6）——跨环境含义完全不同\n7. **Abstract 数字过密**（W8）——Cohen's d 不适合 abstract\n8. **Introduction/Discussion/Conclusion 重复**（W9）\n9. **方法论贡献有价值**（S1-S6）——统计严谨性、跨模型复制、透明度均获高度认可\n\n## Reviewer Divergence\n\n**1. Oracle privilege confound（W1）**\n- R2 [critical]：deterministic 策略的 oracle 特权使 \"routing signal\" 与 \"information privilege\" 不可分离；ScienceWorld 的 death avoidance 可能本质上就是 information asymmetry\n- R1 [partially agree, warning]：Δ_nd = 2.84（9.6% of gap）说明 oracle 优势集中在死亡避免而非广泛信息优势；框架能区分两种机制（DAF=90.4% vs. DAF=0%）\n- **Director 判断**：R2 的 concern 有效但 R1 的 Δ_nd 证据提供了部分回应。Severity 维持 warning。\n\n**2. Cluster bootstrap K=11**\n- R1 [warning]：K=11 低于推荐阈值，Cohen's d=3.02 可能反映 binary structure\n- R2 [rebut]：论文已充分处理——§3.1 已推荐 non-clustered CI 为主，Appendix E 有 transparency statement\n- **Director 判断**：R2 rebut 有效。不作为报告 weakness 列出。\n\n**3. Excitement 评分**\n- R1：3/5（方法论 reuse value + router negative result 信息量）\n- R2：2.5/5（actionability 低，结论基本是 \"use deterministic\"）\n- **Director 判断**：倾向 R2——核心发现的 scope 和 impact 确实有限。\n\n## Questions\n\n**Q1.** 包含全部 30 种 ScienceWorld task types 后 label fraction 如何变化？[R1-Q1, R2 agrees important]\n\n**Q2.** 所有 105 次死亡都由 `focus on` 触发——简单 action-level filter 能否替代 router？Grounding ablation 后重新计算 DAF，death dominance 是否仍存在？[R1-Q2/Q3, R2-W7/cross-response]\n\n**Q3.** Gemma-2 排除 find-non-living-thing 后 DAF 从 89.7% 跳到 99.9%——DAF 对单个 zero-death 任务极度敏感？[R2-Q3]\n\n**Q4.** T_max=100 是否能在 excluded tasks 中发现 non-death-dominated signal？[R2-Q4]\n\n**Q5.** Oracle degeneracy（96.3%）是否意味着 ScienceWorld 不适合作为 routing 研究的 testbed？[R1-Q5, R2 agrees sharp and important]\n\n**Q6.** Dense-reward 环境下 framework 是否仍需 episode-level 比较？[R2-Q2]\n\n**Q7.** Task-type classifier 64.7% balanced accuracy——lookup table 足以替代 router？[R2-Q5]\n\n## Missing References\n\n**R2 指出，R1 partially agrees：**\n1. **Hallucination detection/mitigation 文献**：核心发现涉及 hallucination-induced catastrophic failure，但 Related Work 完全未讨论（Manakul et al., 2023 \"SelfCheckGPT\"; Kadavath et al., 2022 \"Language models know what they know\"）\n2. **Non-agent adaptive computation**：early exit networks（DeeBERT, PABEE）、dynamic neural networks survey（Han et al., 2021）完全缺失\n3. **LLM 不确定性估计**（Kadavath et al., 2022）：与 step-level death prediction future work 直接相关\n\n**R1 指出：** 无 critical omissions。MoE 和 safe RL 覆盖全面。FrugalGPT、AutoMix 已在 §4 引用。\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：pending（未返回）**\n\n外部审稿请求已于 2026-05-23T03:44 发出，截至报告提交时尚未收到结果。\n\n## Visual Layout Check（非评分项）\n\n**状态：done**（耗时约 4 分钟，0 critical / 1 warning / 11 info）\n\n主要发现：\n- **[warning]** Pages 7-8（Related Work + Discussion/Conclusion）连续 2 页纯文字无 display item，\"wall of text\" 疲劳感\n- **[info]** 主文 8 页仅 4 个 display items（2 figure + 2 table），对实证论文偏低（推荐 5-8），大量数据推到 Appendix\n- **[info]** Page 1 无视觉锚点，Figure 1 在 page 2\n- **[info]** Figure 2 图面较空（仅 2 条线）\n- **[info]** 公式渲染正确，无 overfull hbox，所有表格 booktabs 统一，引用格式统一无未解析\n\n## Overall Assessment\n\n### 评分汇总\n\n| 维度 | R1 | R2 | Director 综合 |\n|------|-----|-----|--------------|\n| Soundness | 4/5 | 3.5/5 | 3.5/5 |\n| Excitement | 3/5 | 2.5/5 | 2.5/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5 (Borderline Conference) | 3.0 (Findings) | **3.0 (Findings)** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n### Overall: 3.0 (Findings)\n\n方法论框架有价值——episode-level counterfactual decomposition 填补了 routing 文献中\"先诊断再构建\"的缺口，统计分析严谨程度（21 个 appendix、多层 robustness checks）在同类工作中罕见，跨模型复制（3 个 7-9B 模型族 DAF 88-90%）令人信服。\n\n但三个问题合力将论文限制在 Findings 水准：\n\n1. **核心发现新颖性受限**（C1, 两位 Reviewer 一致同意）：78.9% label fraction 本质上是 death-rate asymmetry 的频率统计，DAF 在 P=100 条件下 mechanically >90%。论文用大量形式化指标包装了一个相对简单的经验观察。虽然 72B 不减少 DAF 和 Reflexion DAF>100% 确实 non-trivial，但这些发现在论文中被置于次要位置。\n\n2. **影响力有限**（C2, 两位 Reviewer 一致同意）：诊断结论（\"use always-deterministic\"）是平凡的；oracle margin 仅 2.89 分表明 routing 在 ScienceWorld 中价值极低；最具 actionability 的 Decision Framework 被埋在 Appendix R。\n\n3. **环境覆盖过窄**（W2, 两位 Reviewer 一致同意）：实质上只有 ScienceWorld 一个定量发现，两个 boundary probes 都未复现核心机制。框架的 decomposition 能力未得到正面验证。\n\n### 提升路径\n\n修订中如能做到以下 4 点，评分有望提升至 **3.5 (Borderline Conference)**：\n1. 将 Decision Framework 提升到正文，强化 actionability 讨论\n2. 在 abstract/intro 突出 non-trivial findings（72B persistence、Reflexion DAF>100%、oracle degeneracy）\n3. 对 non-death labels 进行系统分析\n4. 更明确讨论 oracle privilege confound（突出 Δ_nd=2.84 作为回应证据）\n\n要达到 **4.0 (Conference)** 还需至少一个额外 catastrophic-failure 环境的验证。\n\n## Detailed Comments\n\n### Abstract\n- 数字密度过高（7 个统计量），建议精简至 2-3 个核心数字\n- Cohen's d=3.02 不应出现在 abstract——需 K=11 context\n- \"methodological generality\" vs. \"empirical generality\" 区分在 abstract 过于压缩\n\n### Section 1 (Introduction)\n- 97.4% per-step tie rate 是好的切入点\n- Contributions (1) 和 (2) 区分清楚，但未指明哪个是 primary metric——建议在此处指明 78.9% label fraction 为 primary\n- \"signal diversity can collapse to a single dominant mechanism\" 稍显循环——catastrophic-failure 环境中信号被 catastrophic failure 支配是 expected 的\n- 第 3 段（核心发现）和第 5 段（contributions）重复度高\n\n### Section 2 (Method)\n- 形式化程度恰当，counterfactual 设计干净\n- Algorithm 1 放 Appendix B 合理，但正文应更明确 death-priority rule 的 justification\n- DAF 推导清晰，近似 residual (0.8%) 报告增加可信度\n- §2.4 末尾 \"Scope of episode-level analysis\" 段落放在 Method 中节奏不佳，更像 Limitations 内容\n\n### Section 3 (Experiments)\n- §3.1: 61.2% no-preference base rate 应更早/更突出——routing 仅在 38.8% cases 中 relevant\n- §3.2 (Cross-Model): 论文最强贡献之一\n- §3.3 (Agent Improvement): 72B 应标注为 \"preliminary probe\"，补充 bootstrap CI\n- §3.4 (Cross-Environment): 两个 probes 未复现核心机制，降低 generality claim\n- §3.5 (Baselines): Oracle degeneracy 96.3% 是重要发现，应获得更多 attention\n- §3.6 (Router Training): Frame 为 \"inconclusive under current data regime\"；添加 summary table\n\n### Section 4 (Related Work)\n- 组织合理，5 个 paragraph 覆盖主要方向\n- 缺少 hallucination detection/mitigation 文献和 non-agent adaptive computation（early exit 等）\n\n### Section 5 (Discussion)\n- \"Non-triviality and oracle confound\" 有效但不够突出\n- \"Practical implications\" 过于简短——应纳入 Decision Framework（Appendix R）内容\n- 缺少对 `focus on` 单一 death trigger 和 grounding ablation 的正面讨论\n- 应讨论 death avoidance vs. information privilege 的关系\n\n### Section 6 (Conclusion)\n- 仅 3 句话，过于简短\n- 应增加具体 future work 方向\n\n### Limitations\n- 异常全面（5 个维度，约 1.5 页），\"Pure-strategy upper bound\" 观点重要\n\n### 格式合规\n- **正文 Sections 1-6 在 8 页以内——符合 EMNLP 2026 要求 ✓**\n- ACL review 模板 + Anonymous author——符合 double-blind 要求 ✓\n- 引用格式统一 ✓",
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
    "project": "simgate-modular-routing",
    "report": "# Round 30 审稿报告 — simgate-modular-routing\n\n**论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计；R2: 新颖性+完整性+写作）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮收敛，核心问题达成共识）\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual diagnostic framework，用于分析 LLM agent routing signal 的机制组成。在 ScienceWorld 环境（11/30 task types，245 episodes）中发现 78.9% 的 non-tie routing labels 源自 death asymmetry，DAF 在 P=100 下达 90.4%。跨模型复制（3 个 7-9B 模型族，DAF 88-90%）、agent improvement baselines（Retry, Reflexion, 72B）、跨环境探测（MATH 无信号、ALFWorld 信息不对称）提供支撑。Step-level router 训练得到接近随机的结果，框架诊断其原因为 death avoidance 是 task-type-level 二元信号。\n\n## Strengths\n\n**S1. 方法论设计优雅有效。** [R1-S1, R2-S1; AGREE] Per-step oracle 在 sparse-reward 环境下退化为 97.4% 平局率的观察本身是方法论贡献。Episode-level counterfactual comparison 在相同初始条件下运行，干净隔离 computation mode 为唯一变量。\"先诊断再构建\"的思路填补了 routing 文献中的重要缺口。\n\n**S2. 统计分析严谨且透明度极高。** [R1-S2, R2-S2; AGREE] 21 个 Appendix (A-U) 覆盖 labeling quality audit、cluster bootstrap sensitivity、leave-one-task-out、seed robustness、penalty sensitivity、failure mode analysis、grounding ablation、extended validation 等。对小样本聚类推断局限性（K < 20-50）的诚实披露在 NLP 论文中罕见。\n\n**S3. 跨模型复制令人信服。** [R1-S4, R2-S3; AGREE] 三个架构不同的模型族（Qwen2.5-7B、Llama-3.1-8B、Gemma-2-9B-it）收敛于 DAF 88-90%（spread 仅 2.2pp），10× scaling 到 72B 未消除 death dominance（DAF = 92.4%），有力排除 model-specific 解释。\n\n**S4. Claims 与证据校准审慎。** [R1-S3, R2-S4; AGREE] 论文反复区分 methodological generality 与 empirical generality，将 MATH/ALFWorld 定位为 boundary probes 而非 cross-domain validation，以 label fraction (78.9%) 而非 DAF 作为 primary metric。Limitations 部分（约 1.5 页）极其详尽，自我批判性极强。\n\n**S5. 负面结果的诊断价值。** [R1-S5, R2-S5; AGREE] Router 训练失败被转化为对信号结构的洞察：step-level signal 不存在因为 death avoidance 是 task-type-level 二元信号。两种平衡解释（noise-dominated vs. non-learnability）的呈现方式值得称赞。\n\n**S6. Oracle degeneracy 与 anti-cherry-picking 论证。** [R1-S6, R2-S6; AGREE] Always-deterministic 匹配 96.3% 的 oracle 决策，直接表明 routing 在 ScienceWorld 中价值极低——这本身是重要实证发现。排除的 19 个任务 ΔDR (+38.2pp) 高于包含的 11 个 (+28.7pp)，排除选择性报告嫌疑。\n\n## Weaknesses\n\n### Critical\n\n**C1. 核心发现新颖性受限——death dominance 部分是环境设计的数学必然。** [R1-N1, R2-W1; AGREE]\n\nDAF = δP/(δP + Δ_nd) 在 P=100 >> Δ_nd=2.84 条件下 mechanically >90%——论文自己承认是 \"mathematical consequence rather than empirical finding\"（§2.4）。78.9% label fraction 虽然 penalty-invariant，但本质上测量\"多少比例的 episodes 恰好一方策略死亡\"（R1 表述）——比框架暗示的更简单的频率统计。\n\nR1 指出：78.9% 的 non-trivial content 在于 δ=26.6pp（42.9% vs. 16.3%）这个经验事实，但论文未充分论证这一差异为何不可事先预期。论文用大量形式化指标（DAF、SCI）包装了一个相对简单的发现，可能构成 methodological overengineering（R1 用语）。R2 补充：这种防御性写作策略增加了认知负担而未增加新颖性。\n\n真正 non-trivial 的发现——72B 不减少 DAF、Reflexion 使 DAF>100%——在论文中被置于次要位置。两位 Reviewer 均建议将这些发现提前并突出呈现。\n\n**C2. 诊断与处方之间的实际差距限制影响力。** [R1-N2, R2 agrees]\n\n从诊断得出的实际建议——\"在 death-dominated 环境中使用 always-deterministic\"——是平凡结论，不需要本框架推导。Oracle margin 仅 2.89 分（Table 2: -6.58 vs -9.47），意味着 routing 在 ScienceWorld 中 value 上限极低，进一步削弱了 routing signal 分析的动机。\n\n最具 actionability 的贡献——Decision Framework（Appendix R）和 \"50-episode pilot suffices for build-vs-buy decisions\"——被埋在 appendix 中。两位 Reviewer 均建议将 Decision Framework 提升到正文 Discussion。\n\n### Warning\n\n**W1. [DIVERGENCE] Deterministic 策略的 oracle 特权使 \"routing signal\" 解读模糊。** [R2-W2 critical; R1 partially agrees as warning]\n\nScienceWorld 的 deterministic 策略是 oracle simulator with ground-truth state access——privileged information baseline，非实际可用工具。R2 核心论点：死亡率差异可归因于信息不对称，\"routing signal is death-dominated\" 可能只是 \"information privilege prevents catastrophic errors\" 的换一种说法。ALFWorld 分析诊断为 \"information asymmetry\"（§3.4）——ScienceWorld 是否同样如此？\n\nR1 提供 partial defense：Δ_nd = 2.84（仅 9.6% of full gap）说明 oracle 优势集中在死亡避免上，而非广泛信息优势。框架能区分两种机制（ScienceWorld DAF=90.4% vs. ALFWorld DAF=0%）。\n\nDirector 判断：R2 的 concern 有效但 R1 的 Δ_nd 证据提供了部分回应。论文应在正文中更明确讨论此问题。Severity 维持 warning。\n\n**W2. 环境覆盖过窄，跨环境 probes 未复现核心机制。** [R1-W4, R2-W3; AGREE]\n\nMATH 无 routing signal，ALFWorld 信号来源不同——都未复现 death dominance。两个环境都未展示框架将 routing signal decompose 为多种 contributing mechanisms 的能力（R1 表述更精准）。R1 注意到论文标题已限定 ScienceWorld，但 R2 指出至少一个不同 catastrophic-failure 环境（如 NetHack, Crafter）的验证将大幅增强说服力。\n\n**W3. Non-death component (21.1% of labels) 分析不足。** [R2-W4, R1 agrees]\n\n20 个 non-death non-tie labels 的来源未系统分析。仅 Appendix U 一个 case study（find-non-living-thing）。未分析 labels 的分布特征、任务属性关系、score 差异来源（hallucination vs. suboptimal action vs. random variance）。R1 指出对全部 20 个 labels 的 failure mode decomposition 将大幅增强框架 decomposition 价值。\n\n**W4. 72B scaling 证据不足以支撑 \"persistent under 10× scaling\"。** [R1-W2, R2 agrees]\n\n单一模型（Qwen2.5-72B）、单一 family、未报告 72B DAF bootstrap CI。Introduction 和 Conclusion 中 \"persistent under 10× scaling\" 过于绝对。建议降级为 \"a preliminary 72B probe suggests persistence\"。\n\n**W5. Router negative result 可能被 extreme class imbalance 混淆。** [R1-W3, R2 partially agrees]\n\n90.5% det-preferred，仅 9 个 internal-preferred episodes。Text augmentation 无改善和 LOTO 退化到 chance 不能区分 data limitation 和 signal limitation。建议 frame 为 \"inconclusive under current data regime\"。论文标题 \"A Preliminary Negative Result\" 已部分 hedge。\n\n**W6. \"Deterministic\" 术语跨环境含义不一致。** [R2-W8, R1 agrees]\n\nScienceWorld: ground-truth simulator；MATH: code interpreter；ALFWorld: admissible-action enumeration。三个环境中 \"deterministic\" 含义完全不同。\"Privileged\" 或 \"oracle-assisted\" 更准确，且能引导读者思考信息特权的角色。\n\n**W7. 100% deaths 来自 focus on 单一模式——削弱 \"death avoidance\" 概念的一般性。** [R2-W7, R1 partially agrees]\n\nAppendix N 确认所有 105 次死亡由同一动作触发。Grounding ablation 降低 death 19pp（Appendix O）。R1 反驳：grounding 后死亡率仍 ~29%（vs. deterministic 16.3%），gap 仍 ~13pp；focus on 在非死亡上下文中是合法操作。但 R2 在交叉回应中指出关键缺失实验：grounding ablation 后重新收集 counterfactual episodes 并计算 DAF——直接测试 \"death dominance 是否可通过简单干预消除\"。\n\n**W8. Abstract 数字过密，可读性差。** [R2-W5, R1 agrees]\n\n7 个统计量在 ~200 词 abstract 中。Cohen's d=3.02 不应出现在 abstract——需 K=11 context 才能正确解读。建议精简至 2-3 个核心数字。\n\n**W9. Discussion/Conclusion 与 Introduction 重复度高。** [R2-W6, R1 agrees]\n\n78.9% 在论文中重复至少 7 次。Conclusion 仅 3 句，缺前瞻性内容。Discussion 前两段大量重复 Experiments 内容。Conclusion 应提供具体 future work 方向。\n\n### Info\n\n**I1.** 61.2% no-preference base rate 应更突出——routing 仅在 38.8% cases 中 relevant。[R1, R2 agrees]\n\n**I2.** Table 2 Trained Router 用 single seed (42) vs. full episode set，公平性存疑。[R1, R2 agrees]\n\n**I3.** §2.4 DAF 近似 break down 条件未讨论——当 s̄_surv 不远小于 P 时近似误差如何变化。[R1, R2 agrees]\n\n## Reviewer Consensus\n\n以下问题双方明确达成 [AGREE]：\n\n1. **核心发现新颖性受限**（C1）——death dominance 在 P=100 环境中部分是数学/设计后果，论文需更清楚论证 non-triviality\n2. **Actionability 不足**（C2）——Decision Framework 应提升到正文，oracle degeneracy 的实际意义需深入讨论\n3. **环境覆盖过窄**（W2）——两个 boundary probes 均未复现核心机制\n4. **Non-death labels 分析不足**（W3）——21.1% 的非死亡 labels 需系统分析\n5. **72B scaling 证据单薄**（W4）——单模型、无 CI，claim 应降级\n6. **\"Deterministic\" 术语误导**（W6）——跨环境含义完全不同\n7. **Abstract 数字过密**（W8）——Cohen's d 不适合 abstract\n8. **Introduction/Discussion/Conclusion 重复**（W9）\n9. **方法论贡献有价值**（S1-S6）——统计严谨性、跨模型复制、透明度均获高度认可\n\n## Reviewer Divergence\n\n**1. Oracle privilege confound（W1）**\n- R2 [critical]：deterministic 策略的 oracle 特权使 \"routing signal\" 与 \"information privilege\" 不可分离；ScienceWorld 的 death avoidance 可能本质上就是 information asymmetry\n- R1 [partially agree, warning]：Δ_nd = 2.84（9.6% of gap）说明 oracle 优势集中在死亡避免而非广泛信息优势；框架能区分两种机制（DAF=90.4% vs. DAF=0%）\n- **Director 判断**：R2 的 concern 有效但 R1 的 Δ_nd 证据提供了部分回应。Severity 维持 warning。\n\n**2. Cluster bootstrap K=11**\n- R1 [warning]：K=11 低于推荐阈值，Cohen's d=3.02 可能反映 binary structure\n- R2 [rebut]：论文已充分处理——§3.1 已推荐 non-clustered CI 为主，Appendix E 有 transparency statement\n- **Director 判断**：R2 rebut 有效。不作为报告 weakness 列出。\n\n**3. Excitement 评分**\n- R1：3/5（方法论 reuse value + router negative result 信息量）\n- R2：2.5/5（actionability 低，结论基本是 \"use deterministic\"）\n- **Director 判断**：倾向 R2——核心发现的 scope 和 impact 确实有限。\n\n## Questions\n\n**Q1.** 包含全部 30 种 ScienceWorld task types 后 label fraction 如何变化？[R1-Q1, R2 agrees important]\n\n**Q2.** 所有 105 次死亡都由 `focus on` 触发——简单 action-level filter 能否替代 router？Grounding ablation 后重新计算 DAF，death dominance 是否仍存在？[R1-Q2/Q3, R2-W7/cross-response]\n\n**Q3.** Gemma-2 排除 find-non-living-thing 后 DAF 从 89.7% 跳到 99.9%——DAF 对单个 zero-death 任务极度敏感？[R2-Q3]\n\n**Q4.** T_max=100 是否能在 excluded tasks 中发现 non-death-dominated signal？[R2-Q4]\n\n**Q5.** Oracle degeneracy（96.3%）是否意味着 ScienceWorld 不适合作为 routing 研究的 testbed？[R1-Q5, R2 agrees sharp and important]\n\n**Q6.** Dense-reward 环境下 framework 是否仍需 episode-level 比较？[R2-Q2]\n\n**Q7.** Task-type classifier 64.7% balanced accuracy——lookup table 足以替代 router？[R2-Q5]\n\n## Missing References\n\n**R2 指出，R1 partially agrees：**\n1. **Hallucination detection/mitigation 文献**：核心发现涉及 hallucination-induced catastrophic failure，但 Related Work 完全未讨论（Manakul et al., 2023 \"SelfCheckGPT\"; Kadavath et al., 2022 \"Language models know what they know\"）\n2. **Non-agent adaptive computation**：early exit networks（DeeBERT, PABEE）、dynamic neural networks survey（Han et al., 2021）完全缺失\n3. **LLM 不确定性估计**（Kadavath et al., 2022）：与 step-level death prediction future work 直接相关\n\n**R1 指出：** 无 critical omissions。MoE 和 safe RL 覆盖全面。FrugalGPT、AutoMix 已在 §4 引用。\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：pending（未返回）**\n\n外部审稿请求已于 2026-05-23T03:44 发出，截至报告提交时尚未收到结果。\n\n## Visual Layout Check（非评分项）\n\n**状态：done**（耗时约 4 分钟，0 critical / 1 warning / 11 info）\n\n主要发现：\n- **[warning]** Pages 7-8（Related Work + Discussion/Conclusion）连续 2 页纯文字无 display item，\"wall of text\" 疲劳感\n- **[info]** 主文 8 页仅 4 个 display items（2 figure + 2 table），对实证论文偏低（推荐 5-8），大量数据推到 Appendix\n- **[info]** Page 1 无视觉锚点，Figure 1 在 page 2\n- **[info]** Figure 2 图面较空（仅 2 条线）\n- **[info]** 公式渲染正确，无 overfull hbox，所有表格 booktabs 统一，引用格式统一无未解析\n\n## Overall Assessment\n\n### 评分汇总\n\n| 维度 | R1 | R2 | Director 综合 |\n|------|-----|-----|--------------|\n| Soundness | 4/5 | 3.5/5 | 3.5/5 |\n| Excitement | 3/5 | 2.5/5 | 2.5/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5 (Borderline Conference) | 3.0 (Findings) | **3.0 (Findings)** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n### Overall: 3.0 (Findings)\n\n方法论框架有价值——episode-level counterfactual decomposition 填补了 routing 文献中\"先诊断再构建\"的缺口，统计分析严谨程度（21 个 appendix、多层 robustness checks）在同类工作中罕见，跨模型复制（3 个 7-9B 模型族 DAF 88-90%）令人信服。\n\n但三个问题合力将论文限制在 Findings 水准：\n\n1. **核心发现新颖性受限**（C1, 两位 Reviewer 一致同意）：78.9% label fraction 本质上是 death-rate asymmetry 的频率统计，DAF 在 P=100 条件下 mechanically >90%。论文用大量形式化指标包装了一个相对简单的经验观察。虽然 72B 不减少 DAF 和 Reflexion DAF>100% 确实 non-trivial，但这些发现在论文中被置于次要位置。\n\n2. **影响力有限**（C2, 两位 Reviewer 一致同意）：诊断结论（\"use always-deterministic\"）是平凡的；oracle margin 仅 2.89 分表明 routing 在 ScienceWorld 中价值极低；最具 actionability 的 Decision Framework 被埋在 Appendix R。\n\n3. **环境覆盖过窄**（W2, 两位 Reviewer 一致同意）：实质上只有 ScienceWorld 一个定量发现，两个 boundary probes 都未复现核心机制。框架的 decomposition 能力未得到正面验证。\n\n### 提升路径\n\n修订中如能做到以下 4 点，评分有望提升至 **3.5 (Borderline Conference)**：\n1. 将 Decision Framework 提升到正文，强化 actionability 讨论\n2. 在 abstract/intro 突出 non-trivial findings（72B persistence、Reflexion DAF>100%、oracle degeneracy）\n3. 对 non-death labels 进行系统分析\n4. 更明确讨论 oracle privilege confound（突出 Δ_nd=2.84 作为回应证据）\n\n要达到 **4.0 (Conference)** 还需至少一个额外 catastrophic-failure 环境的验证。\n\n## Detailed Comments\n\n### Abstract\n- 数字密度过高（7 个统计量），建议精简至 2-3 个核心数字\n- Cohen's d=3.02 不应出现在 abstract——需 K=11 context\n- \"methodological generality\" vs. \"empirical generality\" 区分在 abstract 过于压缩\n\n### Section 1 (Introduction)\n- 97.4% per-step tie rate 是好的切入点\n- Contributions (1) 和 (2) 区分清楚，但未指明哪个是 primary metric——建议在此处指明 78.9% label fraction 为 primary\n- \"signal diversity can collapse to a single dominant mechanism\" 稍显循环——catastrophic-failure 环境中信号被 catastrophic failure 支配是 expected 的\n- 第 3 段（核心发现）和第 5 段（contributions）重复度高\n\n### Section 2 (Method)\n- 形式化程度恰当，counterfactual 设计干净\n- Algorithm 1 放 Appendix B 合理，但正文应更明确 death-priority rule 的 justification\n- DAF 推导清晰，近似 residual (0.8%) 报告增加可信度\n- §2.4 末尾 \"Scope of episode-level analysis\" 段落放在 Method 中节奏不佳，更像 Limitations 内容\n\n### Section 3 (Experiments)\n- §3.1: 61.2% no-preference base rate 应更早/更突出——routing 仅在 38.8% cases 中 relevant\n- §3.2 (Cross-Model): 论文最强贡献之一\n- §3.3 (Agent Improvement): 72B 应标注为 \"preliminary probe\"，补充 bootstrap CI\n- §3.4 (Cross-Environment): 两个 probes 未复现核心机制，降低 generality claim\n- §3.5 (Baselines): Oracle degeneracy 96.3% 是重要发现，应获得更多 attention\n- §3.6 (Router Training): Frame 为 \"inconclusive under current data regime\"；添加 summary table\n\n### Section 4 (Related Work)\n- 组织合理，5 个 paragraph 覆盖主要方向\n- 缺少 hallucination detection/mitigation 文献和 non-agent adaptive computation（early exit 等）\n\n### Section 5 (Discussion)\n- \"Non-triviality and oracle confound\" 有效但不够突出\n- \"Practical implications\" 过于简短——应纳入 Decision Framework（Appendix R）内容\n- 缺少对 `focus on` 单一 death trigger 和 grounding ablation 的正面讨论\n- 应讨论 death avoidance vs. information privilege 的关系\n\n### Section 6 (Conclusion)\n- 仅 3 句话，过于简短\n- 应增加具体 future work 方向\n\n### Limitations\n- 异常全面（5 个维度，约 1.5 页），\"Pure-strategy upper bound\" 观点重要\n\n### 格式合规\n- **正文 Sections 1-6 在 8 页以内——符合 EMNLP 2026 要求 ✓**\n- ACL review 模板 + Anonymous author——符合 double-blind 要求 ✓\n- 引用格式统一 ✓",
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

_source line 2563 · 2026-05-23T04:08:54.743346+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4067
}
```

</details>

---


### Assistant

_source line 2564 · 2026-05-23T04:09:07.086450+00:00_

Round 30 审稿完成。

**Overall: 3.0 (Findings)**

报告已投递给 Research Director。核心结论：

- **两位 Reviewer 一致同意的 2 个 critical 问题**：(1) 核心发现新颖性受限——78.9% 本质上是 death-rate asymmetry 频率统计，DAF 在 P=100 下 mechanically high；(2) actionability 有限——诊断结论平凡，Decision Framework 被埋在 appendix
- **主要分歧**：oracle privilege confound（R2 critical vs R1 warning）、Excitement（R2: 2.5 vs R1: 3）
- **提升路径**：Decision Framework 提升正文 + 突出 non-trivial findings + non-death labels 系统分析 + oracle privilege 正面讨论 → 可达 3.5；额外 catastrophic-failure 环境验证 → 可达 4.0
- **格式合规**：正文 8 页 ✓，double-blind ✓
- **外部审稿**：pending
- **视觉审查**：done（1 warning: pp.7-8 wall of text）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 214

## Round 214

2 recorded events


### User

_source line 2565 · 2026-05-23T04:09:09.688299+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。核心结论：与 R1 在大多数问题上达成一致（N1 新颖性受限、N2 诊断-处方差距、W2 72B证据不足、W4 跨环境覆盖窄），但我维持 3.0 (Findings) 不做上调——主要因为 R1 未讨论的 deterministic 策略 oracle 特权问题（我的 W2 critical）和单一失败模式问题（我的 W7），这两个问题合在一起进一步限制了论文 claim 的通用性。

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

_source line 2566 · 2026-05-23T04:09:19.190462+00:00_

Round 30 审稿已完成。报告已投递给 Research Director。

**最终结论：Overall 3.0 (Findings)**

- R1: 3.5 (Borderline Conference)，交叉后维持
- R2: 3.0 (Findings)，交叉后维持
- Director 综合：3.0 (Findings)

两位 Reviewer 在核心问题上达成共识：(1) 发现新颖性受限，(2) actionability 不足，(3) 环境覆盖过窄。分歧在 oracle privilege confound 的权重上（R2 视为 critical，R1 视为 warning）。Issue Tracker 已同步更新，外部审稿仍 pending，视觉审查已完成并纳入报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 215

## Round 215

58 recorded events


### User

_source line 2567 · 2026-05-23T05:17:46.958681+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (8 pages)
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

_source line 2568 · 2026-05-23T05:17:52.458090+00:00_

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

_source line 2569 · 2026-05-23T05:17:52.559546+00:00_

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
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2570 · 2026-05-23T05:17:56.076724+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch",
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
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2571 · 2026-05-23T05:17:56.077209+00:00_



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

_source line 2572 · 2026-05-23T05:18:00.972771+00:00_

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

_source line 2573 · 2026-05-23T05:18:01.073599+00:00_

No matching deferred tools found

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

_source line 2574 · 2026-05-23T05:18:03.435123+00:00_

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

_source line 2575 · 2026-05-23T05:18:03.937849+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (121 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| alfworld-llama-cross-model | Llama-3.1-8B on ALFWorld will show information asymmetry (not death) as the dominant routing mechanism, consistent with Qwen2.5-7B findings (25.9% det-preferred, DAF=0%), confirming the framework diagnoses environment-specific mechanisms regardless of model family. | — | — | — |\n| gemma-scienceworld-cross-model | Gemma-2-9B-it on ScienceWorld will show death dominance (DAF > 80%) consistent with Qwen2.5-7B (90.4%) and Llama-3.1-8B (88.2%), extending the cross-model-family evidence from 2 to 3 independent model families and strengthening the claim that death avoidance dominates routing signal regardless of model architecture. | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **gemma-scienceworld-gpu0** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) observed with Qwen2.5-7B (DAF=90.4%) and Llama-3.1-8B (DAF=88.2%), confirming the diagnostic finding is model-agnostic across 3 model families.\n- **gemma-scienceworld-v4** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) ob
…[truncated 1790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2576 · 2026-05-23T05:18:03.938314+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "file": "config.yaml"
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
    "file": "config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2577 · 2026-05-23T05:18:05.043152+00:00_

Error executing tool read_project_file: 1 validation error for read_project_fileArguments
project
  Field required [type=missing, input_value={'file': 'config.yaml'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 2578 · 2026-05-23T05:18:05.194136+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2579 · 2026-05-23T05:18:06.368482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "limit": "80"
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
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 2580 · 2026-05-23T05:18:06.477061+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\graphicspath{{figures/}}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{algorithm}
16	\usepackage{algorithmic}
17	\usepackage{tcolorbox}
18	\tcbuselibrary{listings,breakable}
19	
20	\hypersetup{pdfauthor={},pdftitle={}}
21	
22	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{abstract}
30	\input{introduction}
31	\input{method}
32	\input{experiments}
33	\input{related_work}
34	\input{discussion}
35	\input{conclusion}
36	
37	\section*{Limitations}
38	
39	\paragraph{Environmental scope.}
40	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct), though extended validation of representative excluded tasks confirms the pattern (Appendix~\ref{app:extended-validation}). The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface non-death-dominated signal that our current setup does not capture. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:cross-env}, \S\ref{sec:discussion}) provide preliminary supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct cross-model replication (11 task types, $N{=}220$; \S\ref{sec:cross-model}) shows death dominance replicates with direction consistency 10/10 while vulnerability magnitude varies ($+30.0$~pp vs.\ Qwen $+26.5$~pp), though both models are in the 7--8B parameter range; Qwen2.5-72B ($10{\times}$ scale) re
…[truncated 6576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 108
}
```

</details>

---


### Tool result

_source line 2581 · 2026-05-23T05:18:10.809362+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found relevant information about EMNLP 2026 submission guidelines and ARR procedures. Here's wha
…[truncated 1316 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 5615
}
```

</details>

---


### Tool call

_source line 2582 · 2026-05-23T05:18:18.290619+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "offset": "80",
  "limit": "50"
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
    "offset": "80",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 2583 · 2026-05-23T05:18:19.746822+00:00_

80	\hyperref[app:decision-framework]{R.~Decision Framework} $\cdot$
81	\hyperref[app:extended-validation]{S.~Extended Validation} $\cdot$
82	\hyperref[app:prompt-templates]{T.~Agent Prompt Templates} $\cdot$
83	\hyperref[app:non-death-case-study]{U.~Non-Death Episode Case Study}
84	
85	\section{Signal Concentration Index}
86	\label{app:sci}
87	
88	Let $K$ denote the number of task types and $c_k$ the contribution of task type $k$ to the aggregate routing signal, defined as the fraction of total death-rate differential attributable to task $k$:
89	\begin{equation}
90	    c_k = \frac{n_k \cdot \delta_k}{\sum_{j=1}^{K} n_j \cdot \delta_j}
91	\end{equation}
92	where $n_k$ is the number of episodes and $\delta_k = d_k^{\tt int} - d_k^{\tt det}$ is the per-task death-rate differential. The SCI is the Gini coefficient over $\{c_1, \ldots, c_K\}$:
93	\begin{equation}
94	    \text{SCI} = \frac{\sum_{i=1}^K \sum_{j=1}^K |c_i - c_j|}{2K \sum_{k=1}^K c_k}
95	\end{equation}
96	
97	\section{Labeling Quality Audit}
98	\label{app:labeling}
99	
100	\begin{algorithm}[t]
101	\caption{Episode-Level Counterfactual Labeling}
102	\label{alg:labeling}
103	\begin{algorithmic}[1]
104	\REQUIRE Task instance $t$, computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$
105	\ENSURE Label $\ell \in \{{\tt det\text{-}pref}, {\tt int\text{-}pref}, {\tt no\text{-}pref}\}$
106	\FOR{each $m \in \mathcal{M}$}
107	    \STATE Run episode $\tau_m$ with pure-strategy $m$
108	    \STATE Record score $s_m$ and death indicator $d_m$
109	\ENDFOR
110	\IF{$d_{\tt int} = 1$ \AND $d_{\tt det} = 0$}
111	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{death asymmetry}
112	\ELSIF{$d_{\tt int} = 0$ \AND $d_{\tt det} = 1$}
113	    \STATE $\ell \leftarrow {\tt int\text{-}pref}$ \COMMENT{death asymmetry}
114	\ELSIF{$d_{\tt int} = d_{\tt det} = 1$}
115	    \STATE $\ell \leftarrow {\tt no\text{-}pref}$ \COMMENT{both dead}
116	\ELSIF{$s_{\tt det} > s_{\tt int}$}
117	    \STATE $\ell \leftarrow {\tt det\text{-
…[truncated 813 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 2584 · 2026-05-23T05:18:19.797548+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limits author instructions"
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
    "query": "ACL Rolling Review 2026 submission guidelines page limits author instructions"
  }
}
```

</details>

---


### Tool call

_source line 2585 · 2026-05-23T05:18:20.250212+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "config.yaml"
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
    "file": "config.yaml"
  }
}
```

</details>

---


### Tool call

_source line 2586 · 2026-05-23T05:18:20.802687+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 2587 · 2026-05-23T05:18:25.874875+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limits author instructions"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"}]

Based on the search results, here are the key ACL Rolling Review 2026 submission guidelines regarding page limits and author instructions:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Short papers may consist of up to four (4) pages of content, plus unlimited pages of references.

## Limitations Section

Authors are required to discuss the limitations of their work in a dedicate
…[truncated 1011 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 6077
}
```

</details>

---


### Tool result

_source line 2588 · 2026-05-23T05:18:25.875446+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5625
}
```

</details>

---


### Tool result

_source line 2589 · 2026-05-23T05:18:25.926023+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 5123
}
```

</details>

---


### Tool call

_source line 2590 · 2026-05-23T05:18:30.896409+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 Budapest ARR commitment deadline submission"
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
    "query": "EMNLP 2026 Budapest ARR commitment deadline submission"
  }
}
```

</details>

---


### Tool call

_source line 2591 · 2026-05-23T05:18:31.499151+00:00_

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

_source line 2592 · 2026-05-23T05:18:31.901660+00:00_

1	# Round 30 Review Issues — R30 fixes verified, all PASS
2	# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作)
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
70	  category: format
71	  severity: info
72	  status: resolved
73	  first_rais
…[truncated 18900 chars]

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

_source line 2593 · 2026-05-23T05:18:32.253609+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/abstract.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/abstract.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 2594 · 2026-05-23T05:18:32.354444+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 2595 · 2026-05-23T05:18:38.703540+00:00_

Web search results for query: "EMNLP 2026 Budapest ARR commitment deadline submission"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.1616 Confs: Workshop at EMNLP 2026: Multimodal Interaction in Face-to-Face Dialogue (Hungary)","url":"https://linguistlist.org/issues/37/1616/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"LINGUIST List 37.1702 Confs: 13th Web-as-Corpus Workshop @ EMNLP 2026 (Hungary)","url":"https://linguistlist.org/issues/37/1702/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here are the key details about EMNLP 2026 in Budapest:

## Conference Details
The 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026) will be held in Budapest, Hungary from October 24th to October 29th, 2026.

## Important ARR-Related Deadlines
The ARR submission deadline for long & short papers is May 25, 2026, the reviewer registration deadline for all authors is May 27, 2026, author response and author-reviewer discussion runs July 7 - July 13
…[truncated 741 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 7807
}
```

</details>

---


### Tool call

_source line 2596 · 2026-05-23T05:18:44.075143+00:00_

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

_source line 2597 · 2026-05-23T05:18:44.075530+00:00_

1	\begin{abstract}
2	LLM agent routing (deciding when to rely on internal reasoning versus external tool use) is typically addressed by training routers directly, without first understanding what mechanistic signal drives the routing preference. This absence of diagnostic methods risks building routers atop confounded or trivial signal. We propose an episode-level counterfactual framework that compares pure-strategy outcomes (internal-only vs.\ deterministic-only) to decompose routing signal into its mechanistic components before any router is constructed. Applying this framework to ScienceWorld (11 task types, 245 episodes), we find that 78.9\% of non-tie episode-level routing labels arise from death asymmetry---a finding replicated across three architecturally distinct 7--9B model families, revealing that in catastrophic-failure environments, signal diversity can collapse to a single dominant mechanism. Cross-environment probes on MATH and ALFWorld diagnose qualitatively different routing mechanisms (no extractable signal and information asymmetry, respectively), providing preliminary evidence of applicability beyond death-dominated settings. The framework distinguishes \emph{methodological generality} (applicable to any environment with paired episode outcomes) from \emph{empirical generality} (full quantitative validation on ScienceWorld only). A ${\sim}$50-episode pilot suffices for build-vs-buy decisions.
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

_source line 2598 · 2026-05-23T05:18:44.477149+00:00_

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

_source line 2599 · 2026-05-23T05:18:45.180556+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	In ScienceWorld \citep{scienceworld-2022}, a text-based science simulation, internal reasoning is error-prone, as the model may hallucinate state changes (e.g., that water has boiled when the stove was never activated), while deterministic external computation eliminates such errors via exact state transitions. The practical question: \emph{when should an agent route computation externally versus internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision: Toolformer \citep{toolformer-2023} inserts API calls by perplexity reduction; ART \citep{art-2023} decomposes tasks into tool-augmented programs; Chameleon \citep{chameleon-2023} selects heterogeneous modules per subtask; adaptive-computation methods route to different reasoning depths \citep{cogrouter-2026,ares-2026}, model tiers \citep{mtrouter-2026}, or episode-level model selection under sparse rewards \citep{budget-aware-routing-2026}; concurrent analyses further presuppose diverse routing signals~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026}. These approaches, which operate in non-catastrophic settings, share the assumption that routing signal stems from diverse sources and a learned router can exploit it---an assumption that remains untested: no prior work has systematically decomposed what drives routing preferences in interactive environments.
7	
8	We propose a \emph{diagnostic framework} comprising (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95), a penalty-independen
…[truncated 2400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 2600 · 2026-05-23T05:18:45.683073+00:00_

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

_source line 2601 · 2026-05-23T05:18:45.683528+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/pipeline_overview.pdf}
7	\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\ref{alg:labeling}.}
8	\label{fig:pipeline}
9	\end{figure}
10	
11	Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically (Appendix~\ref{app:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
12	
13	\subsection{Problem Setup}
14	\label{sec:problem-setup}
15	
16	Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\citep{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic} (${\tt det}$), a privileged-information strategy (an umbrella term: ground-truth simulator access in ScienceWorld, code interpreter in MATH, admissible-action enumeration in ALFWorld---see \S\ref{sec:cross-env} for environment-specific operationalizations) that eliminates observation uncertainty; these qualitative differences affect what routing signals 
…[truncated 7562 chars]

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

_source line 2602 · 2026-05-23T05:18:45.683734+00:00_

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

_source line 2603 · 2026-05-23T05:18:46.085812+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types (63\%) lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). Taxonomically redundant tasks share identical action vocabularies, reward functions, and environmental dynamics, differing only in target entity; we retain one representative per family (Appendix~\ref{app:per-task}). This scope limits generalizability: conclusions apply to the included subset; increasing the 30-step budget might surface signal in excluded types (see Limitations). An anti-cherry-picking analysis confirms that death dominance holds in 18 of these 19 types, with a mean $\Delta\text{DR} = +38.2$\,pp exceeding the included tasks' $+28.7$\,pp (Appendix~\ref{app:per-task}). Extended validation at $n{=}20$ on five representative excluded tasks confirms this direction ($\overline{\Delta\text{DR}} = +32.0$\,pp; Appendix~\ref{app:extended-validation}). A reasoning-depth ablation ($n{=}120$) found no significant difference between internal strategy variants ($p > 0.26$; Appendix~\ref{app:ablations}). Prescreening used $n{=}5$ episodes per task type; directional consistency (18/19 types favoring deterministic) rather than point estimates drives the inclusion criterion.
5	
6	\subsection{Death Avoidance Decomposition}
7	\label{sec:death-decomp}
8	
9	
10	Of the 95 non-tie routing labels, 75 (78.9\%) arise from death asymmetry: the internal strategy triggers a catastrophic $-100$ penalty while the deterministic strategy survives. This penalty-independent label fraction is the primary diagnostic metric. Of these, 54 are sole-signal labels where death was the only discriminator; at $P{=}0$ these reduce to ties, but the labeling function itself is penalty-independent (Algorithm~\ref{alg:labeling}).
11	
12	Of 245 episodes, 150 (61.2\%) show no preference between strategies; routing is relevant in the r
…[truncated 15041 chars]

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

_source line 2604 · 2026-05-23T05:18:46.236953+00:00_

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

_source line 2605 · 2026-05-23T05:18:46.538779+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}, spanning several functional categories.
5	Self-supervised methods learn tool invocation from loss signals \citep{toolformer-2023,toolace-2025}, token-level methods embed tools in the vocabulary \citep{toolkengpt-2023}, task-level decomposition routes subtasks to specialized modules \citep{art-2023,chameleon-2023}, and RL-based methods learn routing from reward \citep{retool-2025}.
6	All focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
7	Concurrent work examines \emph{when} to invoke tools: tool-call decisions correlate with uncertainty~\citep{tool-overuse-illusion-2026}, are encoded in hidden states~\citep{when2tool-2026}, impose a ``tool-use tax''~\citep{tool-use-tax-2026}, or follow necessity-utility-affordability logic~\citep{to-call-or-not-2026}. Our decomposition yields a concrete answer: 78.9\% of non-tie routing labels trace to catastrophic-failure prevention.
8	
9	\paragraph{Adaptive Computation and Routing.}
10	Adaptive routing traces back to learned halting policies \citep{graves2016act}. Mixture-of-Recursions \citep{mixture-of-recursions-2025} learns token-level recursion depths in the LLM era; concurrent work further diversifies routing granularity: CogRouter \citep{cogrouter-2026} adapts per-step depth, ARES \citep{ares-2026} selects effort levels, and MTRouter \citep{mtrouter-2026} addresses multi-turn settings; in death-dominated environments, the task-type-level binary signal is structurally inaccessible to these step-level approaches (\S\ref{sec:router-diagnostic}).
11	RouteLLM \citep{routellm-2024} learns routers from preference data to select between strong and weak models; cost-optimization routing (FrugalGPT~\citep{frugalgpt-2023}; AutoMix~\citep{automix-2024}) cascades queries across model tiers.
…[truncated 3062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2606 · 2026-05-23T05:18:46.539264+00:00_

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

_source line 2607 · 2026-05-23T05:18:46.840785+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Signal granularity and router failure.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property, but step-level features correlate weakly because death risk depends on multi-step trajectories. Six router variants converge on near-chance accuracy ($56$--$59\%$), consistent with signal limitation, though extreme class imbalance (3.7\% minority class) and train--deploy distribution shift~\citep{dagger-2011} make a data-limited explanation equally plausible. Two consequences were not predictable a priori: $10{\times}$ scaling to 72B fails to eliminate death dominance (DAF${}=92.4\%$, 5 internal-preferred vs.\ 9 at 7B), and Reflexion yields DAF${}>100\%$; cross-model DR stability ($36$--$43\%$) confirms death vulnerability is a task-environment property.
6	
7	\paragraph{Oracle degeneracy and practical implications.}
8	Always-deterministic matches 96.3\% of oracle decisions (\S\ref{sec:baselines}), capping any router's marginal value at 2.89 points. Oracle access is the precondition for death avoidance, but $\Delta_{\text{nd}} = 2.84$ (9.6\% of total gap) shows the advantage concentrates almost entirely in death episodes rather than reflecting broad information privilege; ALFWorld (DAF${=}0\%$) confirms the framework diagnoses a qualitatively different mechanism under different oracle configurations. This motivates a practical heuristic: a ${\sim}$50-episode pilot computing label fraction determines whether always-deterministic suffices ($f_{\text{death}} > 75\%$) or router investment is warranted (Appendix~\ref{app:decision-framework}). For ScienceWorld specifically, action-space filtering reduces death rate by 19~pp (Appendix~\ref{app:grounding-ablation}). While all observed deaths stem from a single action pattern (\texttt{focus on}; Appendix~\ref{app:failure-modes}), the decomposition applies to any environment with asymme
…[truncated 27 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2608 · 2026-05-23T05:18:46.841233+00:00_

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

_source line 2609 · 2026-05-23T05:18:46.892224+00:00_

1	\section{Conclusion}
2	
3	Our episode-level counterfactual framework reveals that 78.9\% of non-tie routing labels in ScienceWorld stem from death avoidance---replicated across three model families and persistent under $10{\times}$ scaling (DAF${}=92.4\%$). Future work should validate this in additional catastrophic-failure settings and investigate targeted episode collection to resolve the router's inconclusive result.
4	

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

_source line 2610 · 2026-05-23T05:18:53.169399+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EMNLP 2026\" call for papers main conference long short paper page limit template anonymity"
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
    "query": "\"EMNLP 2026\" call for papers main conference long short paper page limit template anonymity"
  }
}
```

</details>

---


### Tool call

_source line 2611 · 2026-05-23T05:18:55.027219+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 2612 · 2026-05-23T05:18:55.128135+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 2613 · 2026-05-23T05:19:04.366734+00:00_

Web search results for query: ""EMNLP 2026" call for papers main conference long short paper page limit template anonymity"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"NLP - EMNLP 2026 Call for Main Conference Papers. https ...","url":"https://www.facebook.com/NLPScholorship/photos/emnlp-2026-call-for-main-conference-papershttps2026emnlporg/972708278685089/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Now let me search for more specific details about page limits and templates:

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for
…[truncated 3602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 11197
}
```

</details>

---


### Tool call

_source line 2614 · 2026-05-23T05:19:13.103336+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 2615 · 2026-05-23T05:19:13.305352+00:00_

&lt;persisted-output>
Output too large (82.1KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing--claude-sessions-review-director-19d7e797/57ef87cf-ca26-4d3e-b455-6f55ee1e881e/tool-results/toolu_01DCjhG33wRx4CBgEaPsfpui.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_14.md:150:外部审稿：未请求（项目未启用 paperreview.ai）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_9.md:156:外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_8.md:102:外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_16.md:170:未配置外部审稿（`external_review.paperreview_ai.enabled` 未启用）。无外部审稿结果。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_25.md:138:外部审稿：未请求（项目配置未启用 paperreview.ai）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_17.md:133:外部审稿：未配置（项目 config 中无 `external_review.paperreview_ai.enabled` 设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_12.md:139:外部审稿：未请求（项目未配置 external_review.paperreview_ai.enabled）
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_23.md:164:未请求（项目未配置 external_review.paperreview_ai）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_4.md:143:项目未配置外部审稿（paperreview.ai），本轮无外部审稿结果。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifac
…[truncated 301 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 2616 · 2026-05-23T05:19:13.456443+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent"
  }
}
```

</details>

---


### Tool result

_source line 2617 · 2026-05-23T05:19:14.059825+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_director_19d7e797.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 2618 · 2026-05-23T05:19:39.940791+00:00_

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


### Tool result

_source line 2619 · 2026-05-23T05:19:57.315346+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 17374
}
```

</details>

---


### Tool call

_source line 2620 · 2026-05-23T05:19:57.466329+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "31",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页（double-column ACL format），references 无限，Limitations 和 Ethics 不计入页数\n- **匿名规则**: Double-blind\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **评分标准**: Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit）\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_31/submitted.pdf`\n\n## 审查侧重\n\n请重点审查以下方面：\n\n1. **Counterfactual framework 方法论**：episode-level labeling 的合理性、death-aware priority 的假设条件、DAF 定义的数学严谨性\n2. **统计推断**：bootstrap CI 的有效性、K=11 cluster 问题、wild cluster bootstrap 的适用性、per-task n=20 的统计功效\n3. **实验设计**：prescreening 11/30 task types 的 selection bias、cross-model validation（3 个 7-9B family + 72B probe）的充分性、agent improvement baselines 的设计\n4. **Router diagnostic**：step-level vs episode-level granularity mismatch 的分析、inconclusive framing 的合理性、LOTO 分析的解释\n5. **Cross-environment probes**：MATH 和 ALFWorld 作为 boundary probe 的定位、oracle privilege 差异的处理\n6. **格式合规**：正文是否 ≤8 页、Limitations 是否仅含讨论（无新实验/图表）、double-blind 是否完整\n\n输出格式：\n- **Summary**（2-3 句概述）\n- **Strengths**（逐条，标注 [S1], [S2], ...）\n- **Weaknesses**（逐条，标注 [W1], [W2], ...，分 Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者澄清的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Overall Assessment**（评分 + 置信度 + 简要理由）"
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
    "round_number": "31",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页（double-column ACL format），references 无限，Limitations 和 Ethics 不计入页数\n- **匿名规则**: Double-blind\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **评分标准**: Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit）\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_31/submitted.pdf`\n\n## 审查侧重\n\n请重点审查以下方面：\n\n1. **Counterfactual framework 方法论**：episode-level labeling 的合理性、death-aware priority 的假设条件、DAF 定义的数学严谨性\n2. **统计推断**：bootstrap CI 的有效性、K=11 cluster 问题、wild cluster bootstrap 的适用性、per-task n=20 的统计功效\n3. **实验设计**：prescreening 11/30 task types 的 selection bias、cross-model validation（3 个 7-9B family + 72B probe）的充分性、agent improvement baselines 的设计\n4. **Router diagnostic**：step-level vs episode-level granularity mismatch 的分析、inconclusive framing 的合理性、LOTO 分析的解释\n5. **Cross-environment probes**：MATH 和 ALFWorld 作为 boundary probe 的定位、oracle privilege 差异的处理\n6. **格式合规**：正文是否 ≤8 页、Limitations 是否仅含讨论（无新实验/图表）、double-blind 是否完整\n\n输出格式：\n- **Summary**（2-3 句概述）\n- **Strengths**（逐条，标注 [S1], [S2], ...）\n- **Weaknesses**（逐条，标注 [W1], [W2], ...，分 Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者澄清的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Overall Assessment**（评分 + 置信度 + 简要理由）"
  }
}
```

</details>

---


### Tool result

_source line 2621 · 2026-05-23T05:20:09.547389+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12081
}
```

</details>

---


### Tool call

_source line 2622 · 2026-05-23T05:20:09.698335+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "31",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页（double-column ACL format），references 无限，Limitations 和 Ethics 不计入页数\n- **匿名规则**: Double-blind\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **评分标准**: Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit）\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_31/submitted.pdf`\n\n## 审查侧重\n\n请重点审查以下方面：\n\n1. **Novelty 评估**：counterfactual diagnostic framework 的创新程度、\"death avoidance dominates routing\" 这一 finding 是否 obvious-in-hindsight、对比 concurrent work（CogRouter, ARES, MTRouter, budget-aware-routing 等）的差异化定位\n2. **Contribution framing**：论文将自己定位为 \"diagnostic framework + empirical finding\"，这在 EMNLP 的 contribution type 中是否足够？单一环境（ScienceWorld）+ diagnostic contribution 是否够 Main Conference 还是 Findings？\n3. **Related Work 覆盖**：是否遗漏了重要的相关工作（safe RL、tool use、adaptive computation、counterfactual evaluation）、concurrent work 的处理是否公平\n4. **写作质量**：Abstract 信息密度、Introduction 叙事逻辑、Method 清晰度、Discussion 深度、Conclusion 是否完整\n5. **完整性**：论文是否自洽？各 section 之间是否有逻辑断裂？claim 与 evidence 的匹配程度？\n6. **Limitations 质量**：是否诚实覆盖主要局限性、是否含新实验/图表（违规）\n7. **Appendix 使用**：21 个 appendix 是否过多？正文对 appendix 的依赖是否过度？\n\n输出格式：\n- **Summary**（2-3 句概述）\n- **Strengths**（逐条，标注 [S1], [S2], ...）\n- **Weaknesses**（逐条，标注 [W1], [W2], ...，分 Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者澄清的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Overall Assessment**（评分 + 置信度 + 简要理由）"
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
    "round_number": "31",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页（double-column ACL format），references 无限，Limitations 和 Ethics 不计入页数\n- **匿名规则**: Double-blind\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **评分标准**: Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit）\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_31/submitted.pdf`\n\n## 审查侧重\n\n请重点审查以下方面：\n\n1. **Novelty 评估**：counterfactual diagnostic framework 的创新程度、\"death avoidance dominates routing\" 这一 finding 是否 obvious-in-hindsight、对比 concurrent work（CogRouter, ARES, MTRouter, budget-aware-routing 等）的差异化定位\n2. **Contribution framing**：论文将自己定位为 \"diagnostic framework + empirical finding\"，这在 EMNLP 的 contribution type 中是否足够？单一环境（ScienceWorld）+ diagnostic contribution 是否够 Main Conference 还是 Findings？\n3. **Related Work 覆盖**：是否遗漏了重要的相关工作（safe RL、tool use、adaptive computation、counterfactual evaluation）、concurrent work 的处理是否公平\n4. **写作质量**：Abstract 信息密度、Introduction 叙事逻辑、Method 清晰度、Discussion 深度、Conclusion 是否完整\n5. **完整性**：论文是否自洽？各 section 之间是否有逻辑断裂？claim 与 evidence 的匹配程度？\n6. **Limitations 质量**：是否诚实覆盖主要局限性、是否含新实验/图表（违规）\n7. **Appendix 使用**：21 个 appendix 是否过多？正文对 appendix 的依赖是否过度？\n\n输出格式：\n- **Summary**（2-3 句概述）\n- **Strengths**（逐条，标注 [S1], [S2], ...）\n- **Weaknesses**（逐条，标注 [W1], [W2], ...，分 Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者澄清的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Overall Assessment**（评分 + 置信度 + 简要理由）"
  }
}
```

</details>

---


### Tool result

_source line 2623 · 2026-05-23T05:20:11.121854+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1423
}
```

</details>

---


### Assistant

_source line 2624 · 2026-05-23T05:20:15.981274+00:00_

Round 31 审稿已启动：

- **视觉审查 Agent**：已派发（fire-and-forget）
- **Reviewer 1**（方法严谨性 + 实验设计）：已分配
- **Reviewer 2**（新颖性 + 完整性 + 写作）：已分配
- **外部审稿**：未配置，跳过

等待两位 Reviewer 返回初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 216

## Round 216

2 recorded events


### User

_source line 2625 · 2026-05-23T05:27:37.019195+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：Death Avoidance as the Dominant Routing Signal

## Summary

本文提出 episode-level counterfactual diagnostic framework，通过比较 internal（ReAct）和 deterministic 两种纯策略在相同初始条件下的表现，将 routing signal 分解为 death-avoidance 和 non-death 两个成分。核心发现：在 ScienceWorld 中 78.9% 的 non-tie routing labels 和 90.4% 的 performance gap（DAF）源于 death asymmetry。Cross-environment probes（MATH、ALFWorld）表明该发现是环境特异性的。论文定位为 diagnostic contribution 而非新 routing 方法。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3/5 (Acceptable) | 方法论正确，bootstrap CI 充分，但 DAF 分解在 death-dominated 环境中有 circularity 问题（§2.4 + Appendix K）；cross-environment probes 反证了 finding 的 generalizability |
| **Excitement** | 2/5 (Potentially Interesting) | Diagnostic perspective 有价值，但 finding 在 harsh-penalty 环境中较 intuitive；single-environment + non-prescriptive 定位限制了 impact |
| **Reproducibility** | 4/5 (Mostly reproducible) | 代码/数据承诺 release，hyperparameters 详尽（Appendix I, Table 9），prompt templates 完整（Appendix T），bootstrap 细节充分 |
| **Confidence** | 4/5 | 熟悉 LLM agent routing 和 counterfactual evaluation 文献，仔细检查了核心 claims |

---

## Strengths

**[S1] 精确且可复现的分析框架。** DAF（§2.4, Eq. 3-4）和 SCI（Appendix A, Eq. 7）定义清晰，labeling function（§2.3, Eq. 2）形式化完整。Algorithm 1（page 13）给出了完整的 labeling pipeline。任何有 binary success/failure 的 interactive environment 都可以直接套用这套框架。

**[S2] 统计严谨性远超同 venue 平均水平。** Episode-level bootstrap resampling（B=10,000），percentile-based 95% CI，cluster bootstrap sensitivity（Appendix E, K=11 clusters），wild cluster bootstrap（Appendix E），Leave-One-Task-Out sensitivity（Appendix G），per-task confidence intervals（Appendix F）——这套 robustness checking pipeline 值得其他 empirical study 参考。

**[S3] 诚实的自我评估。** Cross-environment probes（§3.4）坦诚地展示了 MATH 上 DAF=0（无 death mechanism）、ALFWorld 上 deterministic advantage 来自 information asymmetry 而非 death avoidance。Limitations section 涵盖了 environmental scope、statistical limitations、diagnostic scope 等 5 个段落，坦承了 single-environment 局限和 DAF 对 penalty magnitude 的敏感性。这种诚实在 routing 文献中不常见。

**[S4] Anti-cherry-picking 验证设计周到。** 19 个 excluded task types 的系统分析（§3.1, Appendix C Table 3-4, Appendix S Table 21）证明 exclusion 不是选择性报告——被排除的 task types 实际上 death-dominated 程度更高（excluded-task aggregate DAF=0.991 > included-task DAF=0.904），消除了 cherry-picking 嫌疑。

**[S5] 实用的 Decision Framework。** Appendix R 提供了三阶段判断流程（pilot collection → death dominance check → decision），虽然简短但对 practitioner 有直接指导意义。Appendix Q 的 threshold routing analysis 也有实际价值。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**[W1] [critical] 标题和 Abstract 过度泛化，与 cross-environment evidence 矛盾**
- 具体位置：Title, Abstract (page 1), §3.4 (page 6), §5 (page 8)
- 问题：Title "Death Avoidance as the Dominant Routing Signal" 暗示这是一个通用发现。Abstract 开头说 "we propose an episode-level counterfactual framework" 然后直接给出 78.9%/DAF=90.4% 数据，读者自然理解为这是 framework 的一般性结论。但 §3.4 的 cross-environment probes 明确显示：MATH 上 DAF=0%（无 death mechanism），ALFWorld 上 DAF=0%（deterministic advantage 来自 information asymmetry）。这意味着 "death avoidance as the dominant routing signal" 仅在 ScienceWorld 这一个有 harsh binary death penalty 的环境中成立。
- 为什么影响接收：这构成了 overclaiming。一个 environment-specific finding 被 framed as a general insight 是 reviewer 的常见拒稿理由。
- 建议修改方向：(1) Title 加限定词（如 "...on ScienceWorld" 已有，但 "as the Dominant Routing Signal" 仍暗示通用性）；(2) Abstract 中尽早说明 cross-environment 结果显示 mechanism 不同；(3) 考虑将 contribution 重新定位为 "the framework reveals that routing signal composition is environment-dependent, with death avoidance dominating in catastrophic-failure environments"

**[W2] [critical] DAF 分解在 harsh-penalty 环境中有 circularity**
- 具体位置：§2.4 (page 3, Eq. 3-4), Appendix K (page 18, Table 12)
- 问题：DAF 将 episodes 按 death status 分区，然后计算 death-asymmetric episodes 对 total gap 的贡献比例。在 ScienceWorld 中，death penalty 是 -100（score 归零），这意味着任何 death episode 的 score gap 必然 ≥ 对方策略的 surviving score。当 death rate 差异大时（internal 42.9% vs deterministic 0%），DAF 机械性地趋向高值——这部分是 decomposition methodology 的产物，部分是 genuine causal mechanism。Appendix K 的 penalty sensitivity analysis（Table 12）显示 DAF 随 penalty 单调递增，DAF_min remains fixed——这进一步表明 DAF 的绝对值高度依赖环境的 penalty structure 而非 routing mechanism 本身。
- 为什么影响接收：如果核心 metric 的高值部分是方法论人工产物，那么 78.9%/90.4% 这些数字的 interpretive value 被削弱。论文需要更清晰地区分 "DAF measures the accounting share of death episodes" 和 "death avoidance is causally the dominant routing mechanism"。
- 建议修改方向：(1) 在 §2.4 中明确讨论 DAF 的 accounting nature vs. causal interpretation；(2) 提供一个 environment-independent 的 metric（如 normalized DAF 或 per-episode causal mediation analysis）；(3) 正文（而非仅 Appendix K）讨论 penalty sensitivity

**[W3] [critical] Contribution type 对 Main Conference 偏弱**
- 具体位置：§1 (page 1, "Our contribution"), §6 (page 8)
- 问题：论文明确将自身定位为 "diagnostic framework + empirical finding"。Framework 本身是 straightforward 的策略对比 + 按 death status 分区——方法论创新有限。Empirical finding（death avoidance dominates）仅在 ScienceWorld 一个环境中成立，且在 harsh penalty 下较 intuitive。对比同期被 ACL 2026 Main Conference 接收的 MTRouter（Zhang et al., 2026c），后者在 ScienceWorld 上实现了超越 GPT-5 的性能并降低 58.7% 成本——prescriptive contribution 显著更强。
- 为什么影响接收：ARR 的 Overall Assessment 评分标准明确区分 Conference（"could be accepted to an *ACL conference"）和 Findings（soundness + reproducibility 为主要标准）。Diagnostic finding without prescriptive follow-through + single-environment scope 更适合 Findings 定位。
- 建议修改方向：(1) 增加至少一个 death-prone environment（如带 health system 的 NetHack、catastrophic failure 的 WebArena）的验证；(2) 或者将 Decision Framework（Appendix R）扩展为正文 section 并进行前瞻性验证（不仅是 post-hoc）

### Should-Fix 问题（影响评分但不一票否决）

**[W4] [warning] 21 个 Appendix（A-U）过多，正文对 Appendix 依赖过重**
- 具体位置：Pages 13-25, 正文中频繁出现 "see Appendix X"
- 问题：Appendix 占 15 页，几乎是正文（8 页）的两倍。多个核心 claim 的支撑证据在 Appendix 中：DAF 的 penalty sensitivity（Appendix K）、Decision Framework（Appendix R）、Threshold Routing（Appendix Q）、cross-model 完整结果（Appendix M）。读者无法仅通过正文 8 页评估论文的核心贡献。部分 Appendix 内容边际价值低（如 Appendix T Agent Prompt Templates 占 2 页，Appendix U 单个 case study）。
- 建议：将 penalty sensitivity（K）和 Decision Framework（R）的核心内容移入正文 Discussion 或 Method section；合并低价值 Appendix；将 prompt templates 作为 supplementary material 而非 Appendix

**[W5] [warning] Related Work 缺少 risk-sensitive RL 文献**
- 具体位置：§4 (page 7-8), "Safe RL and Causal Grounding" 段落
- 问题：论文的核心发现是关于 catastrophic failure avoidance 主导 routing signal。Risk-sensitive RL 文献（CVaR-based optimization, e.g., Chow et al. 2015; Tamar et al. 2015; iterated CVaR RL）直接处理 trajectory-level catastrophic risk，与本文的 death avoidance 机制高度相关。论文只引用了 Garcia and Fernandez (2015) 的 survey 和 Moldovan and Abbeel (2012)，但未讨论 CVaR 框架如何 formalize 本文发现的 death-avoidance routing preference。
- 建议：在 §4 "Safe RL and Causal Grounding" 段落增加 risk-sensitive RL / CVaR optimization 的讨论，说明 death avoidance 可被视为 CVaR optimization 在 routing context 的特例

**[W6] [warning] "Counterfactual" 术语使用松散**
- 具体位置：Title, §1 (page 1), §2 (page 2)
- 问题：论文频繁使用 "counterfactual" 一词并引用 Pearl (2009)。但实际方法是在相同初始条件下运行两种策略并比较结果——这更接近 randomized controlled experiment / A/B testing 而非 structural causal model 意义下的 counterfactual reasoning（后者需要推断 "如果对同一 trajectory 使用不同策略会怎样"）。Pearl (2009) 的 counterfactual 要求在同一 structural equation 下改变 intervention，而非在同一 seed 下独立运行两个 trajectory。
- 建议：降低 "counterfactual" 的使用强度，或在 §2.1 明确定义本文的 "counterfactual" 仅指 "matched-seed strategy comparison"，区别于 causal inference 中的 structural counterfactual

**[W7] [warning] Router Training 结论 "inconclusive" 占用空间**
- 具体位置：§3.6 (page 7), Appendix I (page 16-17)
- 问题：§3.6 花了约半页讨论 router training（step-level vs episode-level, LoRA, text augmentation），但结论是 "inconclusive"——router 的 balanced accuracy 接近 chance level。这个 negative result 本身有价值，但 (1) 没有深入分析为什么 routing 难以学习（是 label noise？signal稀疏？feature representation？），(2) 作为 diagnostic paper 的 contribution，router training failure 不是核心 message。
- 建议：要么深入分析 routing 为何难以学习（增加 error analysis），要么压缩到 1-2 句话在 Discussion 中提及

**[W8] [warning] Discussion section 过薄**
- 具体位置：§5 (page 8), 仅 ~0.5 page
- 问题：Discussion 仅覆盖两个话题（signal granularity + oracle degeneracy），缺少对以下重要问题的讨论：(1) 在什么条件下 death avoidance 预期会/不会主导 routing signal？(2) DAF 的 penalty sensitivity 对实际 routing system 设计的影响；(3) 与 concurrent work（MTRouter, CogRouter, BAAR）的 findings 如何互补？
- 建议：扩展 Discussion 至 1 page，加入 "When does death avoidance dominate?" 的条件分析和与 concurrent work 的对话

### Minor 问题（不影响接收）

**[M1]** Abstract 在读者缺乏上下文时堆砌数字（78.9%, DAF=90.4%, 72B, ±2.81, 97.4%, §2.2, §3.3）——前 2 句即出现 6+ 个数值，信息密度过高。建议精简为 2-3 个关键数字，其余移至正文。

**[M2]** Figure 1 的 pipeline 图信息密度高但布局拥挤。"Death Decomposition Analysis" 框中的公式（Δ_da = ΔP × δ_da）在小字号下难以辨认。建议增大 Figure 或简化内部公式。

**[M3]** Table 1（page 5）的 caption 信息过载——同时说明 top/bottom 两组实验、所有 interventions、scale 说明，可拆分为两个 table 或简化 caption。

**[M4]** §3.5 "Baselines" 小节标题下只有一段关于 always-deterministic baseline 的简短说明（约 3 行），作为独立小节似乎不必要——可以并入 §3.3 或 §3.1。

---

## Questions（需要作者澄清）

**Q1.** DAF 的分解将 death-asymmetric episodes 的 全部 gap 归因于 death avoidance。但 death 可能是 poor reasoning 的下游后果（symptom）而非独立的 failure mechanism（cause）。Failure Mode Analysis（Appendix N）的 Category B（"comprehension without grounding"）和 Category D（"genuine attempts with execution failure"）暗示部分 death 源于 reasoning error 而非 unsafe action。你如何 disentangle "death as a cause of routing signal" vs. "death as a downstream indicator of reasoning quality"？

**Q2.** MTRouter（Zhang et al., 2026c, ACL 2026 accepted）在 ScienceWorld 上训练了 cost-aware multi-turn router。如果将你的 diagnostic framework 应用于 MTRouter 的 routing decisions，DAF 是否仍然主导？MTRouter 是否已经隐式地学会了 death avoidance？

**Q3.** 论文使用 Qwen2.5-7B 作为主 backbone，72B scaling 仍显示 death dominance。但 frontier models（如 GPT-4o/Claude 3.5）在 ScienceWorld 上的表现可能完全不同——death rate 可能大幅降低。你是否有 evidence 表明 death avoidance 在 frontier-model regime 下仍然主导？

**Q4.** Appendix K（Table 12）显示 DAF 随 penalty magnitude 单调递增。如果将 death penalty 设为 0（即 death 仅导致 episode 提前终止但不额外扣分），DAF 会下降到什么水平？这个 hypothetical 能否帮助区分 "penalty amplification" 和 "genuine death avoidance signal"？

**Q5.** Grounding Ablation（Appendix O）显示加入 grounding prompt 后 death rate 下降但 DAF 仍高。这是否意味着 death avoidance 是 fundamental（与 grounding 无关）还是 grounding ablation 力度不够？

---

## Missing References

1. **Risk-sensitive RL / CVaR optimization**：Chow et al. (2015) "Risk-Sensitive and Robust Decision-Making via CVaR Optimization"；Tamar et al. (2015) "Optimizing the CVaR via Sampling"——与 death avoidance 作为 tail-risk avoidance 直接相关
2. **Reward shaping for sparse terminal rewards**：Ng et al. (1999) 已引用，但 ARES (attention-based reward shaping, 2025) 和 potential-based shaping 在 agent routing 中的应用未讨论
3. **Speculative decoding 与 adaptive computation 的 routing 视角**：论文提到 Leviathan et al. (2023) 但未深入讨论 speculative verification 和 routing fallback 的类比关系

---

## Overall Assessment

**Overall**: 3.0 (Findings)
**Confidence**: 4/5

**理由**：本文是一篇 well-executed 的 diagnostic study，统计严谨性突出（[S2]），self-assessment 诚实（[S3]），framework 定义精确（[S1]）。但核心贡献有三个结构性限制：(1) central finding（death avoidance dominates）仅在 ScienceWorld 一个环境中成立，cross-environment probes 反证了 generalizability（[W1]）；(2) DAF metric 在 harsh-penalty 环境中有 circularity，绝对值部分是方法论产物（[W2]）；(3) diagnostic-only 定位 + single-environment scope 对 Main Conference 偏弱，但 soundness 和 reproducibility 达到 Findings 标准（[W3]）。

与 3.5（Borderline Conference）的差距在于：如果论文能在至少一个额外的 death-prone environment 验证 finding（如 NetHack、catastrophic-failure WebArena），或提供 DAF 的 causal mediation analysis 区分 accounting effect 和 genuine mechanism，分数可以上调。

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| 页数限制（正文 ≤8 页） | ✅ 合规 | 正文（Abstract-Conclusion）恰好 8 页 |
| ACL format template | ✅ 合规 | `\usepackage[review]{acl}` |
| Double-blind | ✅ 合规 | Author = "Anonymous"，正文无自引 |
| Limitations section | ✅ 合规 | 正文有且仅有一个 `\section*{Limitations}`，Appendix 无重复 |
| Ethics Statement | ✅ 合规 | 在 Limitations 之后，包含 computational cost |
| ARR Checklist | ✅ 合规 | 未嵌入 PDF（应在 OpenReview form 中填写），LaTeX 中有准备文件 |
| References | ✅ 合规 | 无页数限制，格式正确 |


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

_source line 2626 · 2026-05-23T05:27:43.797170+00:00_

Reviewer 2 的审稿意见已收到。等待 Reviewer 1 的审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 217

## Round 217

2 recorded events


### User

_source line 2627 · 2026-05-23T05:28:00.255715+00:00_

[Reviewer 2 审稿结果]:
审稿完成。核心结论：

- **Overall 3.0 (Findings)**，Confidence 4/5
- 3 个 Must-Fix：标题/Abstract 过度泛化与 cross-environment evidence 矛盾、DAF 在 harsh-penalty 环境中有 circularity、diagnostic-only + single-environment 对 Main Conference 偏弱
- 5 个 Should-Fix：Appendix 过多且正文依赖过重、缺 risk-sensitive RL 文献、counterfactual 术语松散、router training "inconclusive" 占空间、Discussion 过薄
- 4 个 Minor：Abstract 数字堆砌、Figure 1 拥挤、Table 1 caption 过载、§3.5 独立小节不必要
- 格式全部合规（8 页正文、double-blind、单一 Limitations section、Ethics Statement 完整）

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

_source line 2628 · 2026-05-23T05:28:05.485223+00:00_

Reviewer 2 意见已收到。等待 Reviewer 1 完成初审后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 218

## Round 218

6 recorded events


### User

_source line 2629 · 2026-05-23T05:28:06.991291+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性 + 实验设计

**论文**：Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 方法论贡献扎实但发现范围有限——诊断框架可复用，但核心实证发现（death dominance）仅在 ScienceWorld 一个主环境验证，且在有灾难性惩罚的环境中 death-avoidance 主导 routing signal 在直觉上并非意外。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 框架定义清晰、数学推导正确；但 K=11 cluster bootstrap 的统计推断有结构性局限，DAF 对 P 的单调依赖需要更谨慎地解读 |
| Excitement | 3/5 | 问题定位好（先诊断再建 router），但核心发现（death-penalty 环境中 death avoidance 主导信号）的惊喜程度有限；实用启示集中在"直接用 deterministic"这一简单结论 |
| Reproducibility | 4/5 | 环境版本（ScienceWorld v1.2.3）、超参数、模型版本、随机种子均有清晰记录；Appendix T 包含完整 prompt 模板；承诺 acceptance 后释放代码 |
| Overall Assessment | 3.0/5 | Findings 级别——方法论可靠、分析透彻、自我批评诚恳，但单一主环境 + 预期内发现限制了影响力 |
| Confidence | 4/5 | 仔细通读全文及所有附录；熟悉 agent routing、counterfactual evaluation、bootstrap inference 相关文献 |

---

## 主要优势

**[S1] 问题定位准确且方法论缺口明确**。现有 routing 工作（Toolformer、ART、Chameleon、CogRouter 等）直接训练 router 而不先诊断信号来源。论文提出的 "先诊断再建模" 范式填补了真正的方法论空白（§1, Introduction 第2-3段）。

**[S2] 框架设计简洁且可复用**。Episode-level counterfactual labeling（Algorithm 1, Appendix B）和 DAF 分解在数学上干净，且成功应用于三个不同环境（ScienceWorld/MATH/ALFWorld），无需修改框架本身——MATH 诊断出 "无信号"（§3.4, McNemar p=0.81），ALFWorld 诊断出 "信息不对称"（DAF=0%），与 ScienceWorld 的 "death dominance" 形成有意义的对比。

**[S3] 异常诚恳的自我批评和稳健性分析**。论文主动承认了几乎所有潜在问题：K=11 cluster 问题（§Limitations para 3, Appendix E）、DAF 对 P 的单调依赖（§2.4, Appendix K）、router 结果的不确定性（§3.6 明确标注 "Inconclusive Results"）、episode-level labeling 的粒度错配（§2.4 Scope 段落）。这种透明度在 *ACL 投稿中罕见且值得肯定。

**[S4] 跨模型验证设计合理**。三个架构差异显著的 7-9B 模型族（Qwen2.5-7B/Llama-3.1-8B/Gemma-2-9B-it）收敛于 DAF 88-90%（spread 仅 2.2pp），方向一致性 10/10（§3.2, Appendix M, Table 7）。这排除了 model-specific artifact 的解释。

**[S5] Anti-cherry-picking 分析有说服力**。被排除的 19 个 task type 的平均 ΔDR（+38.2pp）高于入选的 11 个（+28.7pp），与 cherry-picking 假设预测方向相反（Table 4, Appendix C）。Extended validation（n=20, 5 个代表性 excluded tasks, Appendix S）进一步确认。

**[S6] 负面结果的汇报标准高**。Router 训练失败（§3.6）不是简单一句 "didn't work"：论文提供了 8-seed cross-split evaluation（Table 6）、step-level vs episode-level 对比、text augmentation ablation（Table 7, 25%-800% 范围）、capacity scaling（0.6B/1.7B/4B, Table 8）、LOTO analysis，系统性排除了各种解释。

---

## Must-Fix 问题（影响接收决定）

**[W1] [critical] 单一主环境限制了核心发现的说服力**
- 具体位置：§3 全节，§6 Conclusion
- 问题：论文的核心实证发现（78.9% label fraction, DAF=90.4%）完全来自 ScienceWorld 一个环境。MATH 和 ALFWorld 被明确定位为 "boundary probes"（§3.4 首句），不构成对 death-dominance 发现的验证——MATH 没有 death（负对照），ALFWorld 没有 death mechanism 但有不同类型的信号（正对照的不同机制）。论文声称的 "methodological generality" 与 "empirical generality" 的区分是合理的，但缺少**第二个 death-dominated 环境**来验证框架在不同灾难性失败模式下的表现。例如：WebShop 中的不可逆购买错误、Minecraft agent 的不可逆资源消耗、或其他有 catastrophic failure 但不同于 ScienceWorld 的 focus-on 机制的环境。
- 为什么影响接收：Abstract 声称框架 "applies to any environment with asymmetric fatal outcomes"，但这只是 methodological claim，没有实证支持。唯一有 death 的环境就是 ScienceWorld，而 ScienceWorld 的 death 机制极为特殊（100% 的 death 来自单一 action `focus on`，Appendix N）。如果 death 机制更多样化，DAF 分解的行为可能不同。
- 建议修改方向：增加至少一个具有不同 catastrophic failure 机制的环境（不需要完整的 245 episodes，§Appendix R 的 ~50-episode pilot 即可）；或者更明确地将论文定位为 ScienceWorld-specific 分析而非通用框架。

**[W2] [critical] Deterministic 策略的 oracle privilege 使 "death avoidance" 发现的意义需更深入讨论**
- 具体位置：§2.1 Problem Setup, §5 Discussion
- 问题：ScienceWorld 的 deterministic 策略使用 **simulator forking**——直接访问 ground-truth 环境状态来评估候选 action（§2.1, Appendix T 的 prompt 模板显示 deterministic 只是让 LLM rank 候选 action，然后由 simulator 评估）。这是极强的 oracle 特权。ALFWorld 的 "deterministic" 是 admissible-action enumeration，MATH 的是 code interpreter——三个环境的 "deterministic" 含义完全不同。论文在 §3.4 首段正确指出这是 "boundary probes" 而非 cross-domain validation，但在 Introduction 第5段的 contribution (2) 中，将三个环境并列呈现可能误导读者认为存在跨环境一致性。
- 更深层的问题：在 ScienceWorld 中，deterministic 策略的 death rate（16.3%）之所以低，是因为 simulator forking 允许 agent 在执行前试探 action 的后果。这意味着 "death avoidance" 实质上等价于 "oracle information access prevents irreversible errors"，这在逻辑上是预期的。论文的真正发现——非 death episodes 中两策略性能几乎无差（Δ_nd=2.84, 仅占 Δ_full 的 9.6%）——才是非直觉的洞见，但论文将此作为 DAF 分解的副产品呈现，而非核心发现。
- 为什么影响接收：如果读者认为核心发现是 "在有 catastrophic failure 的环境中，避免 catastrophic failure 主导 routing signal"，这接近于同义反复（tautology）。论文需要更清晰地论证为什么这是非平凡的发现。
- 建议修改方向：（1）重构叙事：将 "非 death episodes 中 deterministic 几乎无优势"（Δ_nd≈2.84）提升为与 death dominance 并列的核心发现，而非 DAF 的推论；（2）明确讨论 oracle privilege 的不同程度（simulator forking vs admissible actions vs code interpreter）如何影响 DAF 分解的解释；（3）在 Discussion 中增加一个反事实论证：如果 deterministic 策略不是 oracle-privileged（例如只提供 action syntax checking 而非 outcome prediction），death avoidance 的主导地位是否仍成立？

---

## Should-Fix 问题（影响评分但不一票否决）

**[W3] [warning] K=11 cluster bootstrap 的统计功效不足，建议的补救措施（依赖非聚类 bootstrap）逻辑上不自洽**
- 具体位置：§3.1 Sensitivity 段落, Appendix E
- 问题：论文正确指出 K=11 远低于 cluster-robust 推断的推荐阈值（K≥20-50, Cameron 2008, Webb 2023）。但随后建议读者 "rely on the non-clustered bootstrap CI ([81.1%, 99.0%])"（Limitations §3）——这等于承认 episodes 在 task type 内有相关性（这是做 cluster bootstrap 的原因），但又建议忽略这种相关性。如果 within-cluster correlation 确实存在（论文自己承认 "episodes within the same task type share environment dynamics"），那么非聚类 bootstrap 的 CI 是 anti-conservative 的。
- 具体数值矛盾：非聚类 CI = [81.1%, 99.0%]，聚类 CI = [73.3%, 100.0%]。差距不大，但原则上非聚类 CI 不应被推荐为 "primary inference"。
- 论文的部分缓解措施是有效的：100% directional consistency across all 28 death-prone tasks（Appendix F）、exact permutation test p=0.002（Table 5）、sign test p<0.001。这些非参数检验不假设 independence，因此更可靠。
- 建议修改方向：（1）将叙述重心从 bootstrap CI 转向非参数检验（permutation test、sign test），这些在小 K 下更合理；（2）删除"readers should rely on the non-clustered bootstrap CI" 的建议，改为承认两种 CI 都有局限，以非参数检验为主要推断依据。

**[W4] [warning] DAF 对 penalty magnitude P 的单调依赖使其作为 "诊断指标" 的价值打折**
- 具体位置：§2.4, Appendix K (Table 9, Table 10)
- 问题：DAF = δP/(δP + Δ_nd) 数学上随 P 单调递增。在 P=10 时 DAF=50.4%，在 P=100 时 DAF=90.4%，在 P=500 时 DAF=97.9%（Table 9）。论文在 §2.4 第4段和 Limitations 中承认这是 "mathematical consequence rather than empirical finding"，并将 label fraction（78.9%）作为 primary metric。这是正确的做法。
- 但论文在多处仍以 DAF=90.4% 为 headline number（Abstract: "DAF=90.4%"; Introduction: "DAF 88-90%"; Conclusion: "DAF=92.4%"），给读者的第一印象是一个高度 death-dominated 的定量指标，而实际上这个数字高度依赖 P 的选择。在 §2.4 提出的 penalty-independent label fraction（78.9%）才是更 robust 的指标。
- 建议修改方向：在 Abstract 和 Conclusion 中用 label fraction（78.9%）替代 DAF（90.4%）作为 primary headline。DAF 可以保留为补充指标，但不应在读者第一接触的位置出现。（注：论文已在 Abstract 中提到 78.9%——"we find that 78.9% of non-tie episode-level routing labels arise from death asymmetry"——但 DAF=90.4% 也在 Introduction contribution (2) 中突出出现。）

**[W5] [warning] Episode-level labeling 到 step-level routing 的粒度错配（granularity mismatch）限制了框架的实用性**
- 具体位置：§2.4 Scope 段落, §3.6, §5 第1段
- 问题：框架产出 episode-level labels（每个 episode 一个 routing preference），但实际 routing 需要 step-level 决策。论文承认 88% 的 step-level training data 是 uninformative（60.3% pre-event neutral + 27.4% post-event, §3.6），且仅 0.3% 有 directional conflict。这意味着框架本质上是一个 **诊断工具**，不是 router 训练的 label source。论文在 §5 和 Limitations 中承认了这一点。
- 但这引出一个根本性问题：如果框架产生的 labels 不能训练 step-level router，那么它对 "build-vs-buy decision"（Appendix R）的指导意义就限于 "是否值得尝试 routing"——答案几乎总是 "不值得"（在 death-dominated 环境中），这使框架的实用价值收窄为一个 sanity check。
- 建议修改方向：更明确地将框架定位为 "环境诊断工具" 而非 "router 开发流程的第一步"，并讨论如何扩展框架以产生 step-level routing labels（例如，通过 step-level counterfactual rollouts 而非 episode-level 比较）。

**[W6] [warning] 72B probe 缺少 cross-model replication at scale**
- 具体位置：§3.3, Limitations §1
- 问题：7-9B tier 有三个模型族的 replication（§3.2），但 72B probe 仅使用 Qwen2.5-72B 一个模型（§3.3, N=255）。论文声称 "10× scaling does not eliminate death dominance"（DAF=92.4%），但这仅基于 Qwen 模型族的一个数据点。Llama-3.1-70B 或 Gemma-2-27B 的行为可能不同，尤其考虑到 7-9B tier 中不同模型的 deterministic death rate 存在显著差异（Qwen 16.3% vs Llama 11.4%, Table 7）。
- Limitations §1 承认 "72B probe is limited to a single model without cross-model replication at scale"，这是诚实的，但 Introduction contribution (2) 仍将 "preliminary 10× scaling probe" 与三个模型族的 replication 并列，可能给读者高估 scaling result 的 robustness。
- 建议修改方向：在 Introduction 中更明确地标注 72B 结果的 preliminary 性质，或增加至少一个不同家族的 70B+ 模型（Llama-3.1-70B）的 pilot。

---

## 小问题（不影响接收）

**[M1]** Limitations 章节（page 9-10）包含 5 个详细段落，约占 1.5 页。虽然内容全部是必要的讨论（无新实验/图表），但对于 ARR 的 "mandatory limitations" 来说偏长。建议精简为 3 个核心段落，将部分细节移至 Appendix。

**[M2]** Table 2（§3.5）的 "Trained Router†" 行只使用了单一 random seed (42)，而其他策略使用了完整 episode set。虽然附录提供了 8-seed 分析，但正文表格中单 seed 结果的呈现可能产生误导。建议在正文中标注 8-seed 均值。

**[M3]** §2.1 Problem Setup 将 "deterministic" 定义为 umbrella term（simulator forking / code interpreter / admissible actions），但这三者的 information privilege 差异巨大。建议在 §2.1 中增加一个简短的层级说明（例如按 oracle strength 排序），帮助读者理解 cross-environment 比较的限制。

**[M4]** Appendix N 的 failure mode taxonomy（A/B/D/E categories）由单一标注者完成，无 inter-annotator agreement。论文承认了这一点，但标注为 "qualitative illustrations" 仍然是一个小弱点。

**[M5]** SCI（Signal Concentration Index, Appendix A）在正文（§3.1）中只出现了一次（SCI=0.2147），之后再未使用。如果 SCI 不是核心贡献，建议降低其在 Method §2 中的显著度（目前列为框架三大组件之一）。

**[M6]** 论文在 Ethics Statement 中提到使用 NVIDIA RTX 5090——截至 2026 年中此 GPU 是否已正式发售需要确认。如果尚未公开发售，使用此硬件可能泄露作者身份（特定实验室的早期访问）。需要检查是否违反 double-blind 政策。

---

## Questions（需要作者澄清）

**[Q1]** Algorithm 1 第9行：当两个策略都 die 时标记为 no-preference。但 ScienceWorld 中 death 可能发生在不同时间步，如果一个策略在 step 5 die 而另一个在 step 25 die，它们可能积累了不同的 partial progress。为什么不比较 death timing 或 pre-death progress？论文声称 "death yields a fixed -100 regardless of timing"（Appendix B 注释），但是否有 pre-death partial scores 可以利用？

**[Q2]** §3.1 报告 DAF 的 95% CI 为 [81.1%, 99.0%]（non-clustered），但 label fraction 的 95% CI 是多少？论文多处强调 label fraction 是 primary metric，但似乎从未报告过它的 confidence interval。

**[Q3]** §3.3 报告 Reflexion N=3 时 Δ_nd = -0.47，使 DAF > 100%。这个 Δ_nd < 0 意味着在非 death episodes 中，Reflexion agent 的 internal strategy 反而略优于 deterministic。这是否暗示 Reflexion 特别改善了 internal strategy 在非 death 情境下的表现？如果是，这是否削弱了 "deterministic 策略全面优于 internal" 的叙事？

**[Q4]** §3.6 中 4B model 的 episode-level balanced accuracy 为 59.0%±1.9%。但 LOTO 分析（Appendix P）显示 LOTO 下降到 50.0%。这意味着 4B 的 59% 完全来自 task-type identification。论文是否考虑过使用 task-type 信息作为显式特征（而非依赖模型隐式学习），测试 task-type-aware routing 的效果？

**[Q5]** Grounding ablation（Appendix O）显示 action-space filtering 将 death rate 从 48.0% 降至 29.0%（-19pp）。这个干预不依赖 oracle access。如果在 internal strategy 上应用此 filtering 然后重新计算 DAF，death dominance 是否仍然成立？这个反事实对于论文的实际启示很重要：如果简单的 action-space filtering 就能大幅削弱 death dominance，那么 "直接用 deterministic" 的建议可能不是最佳策略。

---

## Missing References

**[R1]** AgentGym (Xi et al., 2024) 提供了多环境 agent 训练基准，包含 catastrophic failure 场景，与论文的跨环境分析相关。

**[R2]** OS-Copilot / OSWorld (Xie et al., 2024) 提供了具有不可逆操作（文件删除、系统配置）的 computer agent 环境，是论文所需的 "第二个 death-dominated 环境" 的候选。

**[R3]** Trial-and-Error (Wang et al., 2024, "Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents") 讨论了 LLM agent 在有 catastrophic action 的环境中如何通过试错学习，与论文的 death avoidance 分析互补。

---

## 总评

这是一篇方法论扎实、分析透彻、自我批评诚恳的诊断性分析论文。核心贡献——episode-level counterfactual 诊断框架——是简洁且可复用的。但论文面临两个根本性挑战：(1) 核心实证发现（death dominance）仅在一个主环境验证，且该发现在有强 penalty 的环境中直觉上可预期；(2) 框架的实用性受限于 episode-level → step-level 的粒度错配，使其更像一个 "是否值得 routing" 的 sanity check，而非 routing system 开发的基础工具。

尽管如此，论文在多个方面超出了同类工作的标准：跨模型验证（3 个模型族）、反选择偏差分析（anti-cherry-picking）、router 失败的系统性排查（6 个变体）、以及对 inconclusive results 的诚恳汇报。这些品质使论文适合作为 Findings 论文。

要提升到 Conference 级别，需要至少一个额外的 death-dominated 环境验证，并重构叙事将 Δ_nd ≈ 0 的洞见（而非 DAF=90.4%）置于核心。

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

_source line 2630 · 2026-05-23T05:28:50.885055+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "31",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Weakness、Question 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的完整审稿意见\n\n### Must-Fix\n\n**[W1] [critical] 单一主环境限制了核心发现的说服力**\n论文的核心实证发现（78.9% label fraction, DAF=90.4%）完全来自 ScienceWorld 一个环境。MATH 和 ALFWorld 被明确定位为 \"boundary probes\"（§3.4 首句），不构成对 death-dominance 发现的验证。缺少第二个 death-dominated 环境来验证框架在不同灾难性失败模式下的表现。ScienceWorld 的 death 机制极为特殊（100% 的 death 来自单一 action `focus on`，Appendix N）。\n\n**[W2] [critical] Deterministic 策略的 oracle privilege 使 \"death avoidance\" 发现的意义需更深入讨论**\nScienceWorld 的 deterministic 策略使用 simulator forking——极强的 oracle 特权。在 ScienceWorld 中 death avoidance 实质上等价于 \"oracle information access prevents irreversible errors\"，这在逻辑上是预期的。论文的真正发现——非 death episodes 中两策略性能几乎无差（Δ_nd=2.84, 仅占 Δ_full 的 9.6%）——才是非直觉的洞见，但论文将此作为 DAF 分解的副产品呈现，而非核心发现。需要更清晰地论证为什么这不是同义反复（tautology）。\n\n### Should-Fix\n\n**[W3] [warning] K=11 cluster bootstrap 的统计功效不足，建议的补救措施逻辑上不自洽**\n论文承认 K=11 远低于推荐阈值（K≥20-50），但建议读者依赖非聚类 bootstrap CI——这等于承认 within-cluster correlation 存在但又建议忽略它。建议将重心转向非参数检验（permutation test、sign test）。\n\n**[W4] [warning] DAF 对 penalty magnitude P 的单调依赖使其作为诊断指标的价值打折**\nDAF 数学上随 P 单调递增（P=10: 50.4%, P=100: 90.4%, P=500: 97.9%）。论文在多处仍以 DAF=90.4% 为 headline number，但 label fraction（78.9%）才更 robust。\n\n**[W5] [warning] Episode-level labeling 到 step-level routing 的粒度错配限制了框架的实用性**\n框架产出 episode-level labels 但实际 routing 需要 step-level 决策。88% 的 step-level training data 是 uninformative。框架的实用价值收窄为 sanity check。\n\n**[W6] [warning] 72B probe 缺少 cross-model replication at scale**\n7-9B 有三个模型族 replication，但 72B 仅使用 Qwen2.5-72B 一个模型。Introduction 将 72B 与三个模型族并列可能高估 scaling result 的 robustness。\n\n### Minor\n\n**[M1]** Limitations 章节偏长（约 1.5 页）。\n**[M2]** Table 2 Trained Router 行单一 seed (42)，建议标注 8-seed 均值。\n**[M3]** §2.1 三种 deterministic 策略的 oracle strength 差异需层级说明。\n**[M4]** Appendix N failure mode taxonomy 单一标注者，无 inter-annotator agreement。\n**[M5]** SCI 在正文仅出现一次，与 Method §2 中的显著度不匹配。\n**[M6]** RTX 5090 硬件可能泄露作者身份。\n\n### Questions\n\n**[Q1]** 两个策略都 die 但 death timing 不同时，为什么不比较 pre-death progress？\n**[Q2]** Label fraction 的 95% CI 是多少？论文未报告。\n**[Q3]** Reflexion N=3 时 Δ_nd < 0 是否暗示 Reflexion 特别改善了 internal 非 death 表现？\n**[Q4]** 4B router 的 59% 完全来自 task-type identification，是否考虑过 task-type-aware routing？\n**[Q5]** Grounding ablation 后重新计算 DAF，death dominance 是否仍成立？\n\n### Missing References\n\n**[R1]** AgentGym (Xi et al., 2024)\n**[R2]** OS-Copilot / OSWorld (Xie et al., 2024)\n**[R3]** Trial-and-Error (Wang et al., 2024)\n\n---\n\n请逐条回应。"
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
    "round_number": "31",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Weakness、Question 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的完整审稿意见\n\n### Must-Fix\n\n**[W1] [critical] 单一主环境限制了核心发现的说服力**\n论文的核心实证发现（78.9% label fraction, DAF=90.4%）完全来自 ScienceWorld 一个环境。MATH 和 ALFWorld 被明确定位为 \"boundary probes\"（§3.4 首句），不构成对 death-dominance 发现的验证。缺少第二个 death-dominated 环境来验证框架在不同灾难性失败模式下的表现。ScienceWorld 的 death 机制极为特殊（100% 的 death 来自单一 action `focus on`，Appendix N）。\n\n**[W2] [critical] Deterministic 策略的 oracle privilege 使 \"death avoidance\" 发现的意义需更深入讨论**\nScienceWorld 的 deterministic 策略使用 simulator forking——极强的 oracle 特权。在 ScienceWorld 中 death avoidance 实质上等价于 \"oracle information access prevents irreversible errors\"，这在逻辑上是预期的。论文的真正发现——非 death episodes 中两策略性能几乎无差（Δ_nd=2.84, 仅占 Δ_full 的 9.6%）——才是非直觉的洞见，但论文将此作为 DAF 分解的副产品呈现，而非核心发现。需要更清晰地论证为什么这不是同义反复（tautology）。\n\n### Should-Fix\n\n**[W3] [warning] K=11 cluster bootstrap 的统计功效不足，建议的补救措施逻辑上不自洽**\n论文承认 K=11 远低于推荐阈值（K≥20-50），但建议读者依赖非聚类 bootstrap CI——这等于承认 within-cluster correlation 存在但又建议忽略它。建议将重心转向非参数检验（permutation test、sign test）。\n\n**[W4] [warning] DAF 对 penalty magnitude P 的单调依赖使其作为诊断指标的价值打折**\nDAF 数学上随 P 单调递增（P=10: 50.4%, P=100: 90.4%, P=500: 97.9%）。论文在多处仍以 DAF=90.4% 为 headline number，但 label fraction（78.9%）才更 robust。\n\n**[W5] [warning] Episode-level labeling 到 step-level routing 的粒度错配限制了框架的实用性**\n框架产出 episode-level labels 但实际 routing 需要 step-level 决策。88% 的 step-level training data 是 uninformative。框架的实用价值收窄为 sanity check。\n\n**[W6] [warning] 72B probe 缺少 cross-model replication at scale**\n7-9B 有三个模型族 replication，但 72B 仅使用 Qwen2.5-72B 一个模型。Introduction 将 72B 与三个模型族并列可能高估 scaling result 的 robustness。\n\n### Minor\n\n**[M1]** Limitations 章节偏长（约 1.5 页）。\n**[M2]** Table 2 Trained Router 行单一 seed (42)，建议标注 8-seed 均值。\n**[M3]** §2.1 三种 deterministic 策略的 oracle strength 差异需层级说明。\n**[M4]** Appendix N failure mode taxonomy 单一标注者，无 inter-annotator agreement。\n**[M5]** SCI 在正文仅出现一次，与 Method §2 中的显著度不匹配。\n**[M6]** RTX 5090 硬件可能泄露作者身份。\n\n### Questions\n\n**[Q1]** 两个策略都 die 但 death timing 不同时，为什么不比较 pre-death progress？\n**[Q2]** Label fraction 的 95% CI 是多少？论文未报告。\n**[Q3]** Reflexion N=3 时 Δ_nd < 0 是否暗示 Reflexion 特别改善了 internal 非 death 表现？\n**[Q4]** 4B router 的 59% 完全来自 task-type identification，是否考虑过 task-type-aware routing？\n**[Q5]** Grounding ablation 后重新计算 DAF，death dominance 是否仍成立？\n\n### Missing References\n\n**[R1]** AgentGym (Xi et al., 2024)\n**[R2]** OS-Copilot / OSWorld (Xie et al., 2024)\n**[R3]** Trial-and-Error (Wang et al., 2024)\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 2631 · 2026-05-23T05:29:18.843295+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27958
}
```

</details>

---


### Tool call

_source line 2632 · 2026-05-23T05:29:19.044597+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "31",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Weakness、Question 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的完整审稿意见\n\n### Must-Fix\n\n**[W1] [critical] 标题和 Abstract 过度泛化，与 cross-environment evidence 矛盾**\nTitle \"Death Avoidance as the Dominant Routing Signal\" 暗示通用发现。但 §3.4 cross-environment probes 显示 MATH 上 DAF=0%、ALFWorld 上 DAF=0%。仅在 ScienceWorld 一个环境中成立。建议 Title 加限定词或重新定位 contribution。\n\n**[W2] [critical] DAF 分解在 harsh-penalty 环境中有 circularity**\nDAF 将 death-asymmetric episodes 的全部 gap 归因于 death avoidance。当 death penalty=-100 且 death rate 差异大时，DAF 机械性趋向高值——部分是方法论产物。Appendix K 的 penalty sensitivity 显示 DAF 随 P 单调递增。需要区分 accounting effect 和 genuine mechanism。\n\n**[W3] [critical] Contribution type 对 Main Conference 偏弱**\nDiagnostic framework + empirical finding 的定位。Framework 本身方法论创新有限，empirical finding 仅在一个环境中成立且 intuitive。对比 MTRouter（ACL 2026）prescriptive contribution 显著更强。更适合 Findings。\n\n### Should-Fix\n\n**[W4] [warning] 21 个 Appendix（A-U）过多，正文对 Appendix 依赖过重**\nAppendix 占 15 页，几乎是正文两倍。核心 claim 支撑证据在 Appendix：DAF penalty sensitivity（K）、Decision Framework（R）、Threshold Routing（Q）、cross-model 完整结果（M）。\n\n**[W5] [warning] Related Work 缺少 risk-sensitive RL 文献**\nCVaR-based optimization（Chow et al. 2015; Tamar et al. 2015）直接处理 trajectory-level catastrophic risk，与 death avoidance 高度相关。\n\n**[W6] [warning] \"Counterfactual\" 术语使用松散**\n方法更接近 matched-seed A/B testing 而非 Pearl (2009) 意义下的 structural counterfactual reasoning。\n\n**[W7] [warning] Router Training 结论 \"inconclusive\" 占用空间**\n半页讨论 router training 但结论是 inconclusive。没有深入分析为什么 routing 难以学习。\n\n**[W8] [warning] Discussion section 过薄**\n仅覆盖两个话题（signal granularity + oracle degeneracy），缺少条件分析和与 concurrent work 的对话。\n\n### Minor\n\n**[M1]** Abstract 数字堆砌。\n**[M2]** Figure 1 布局拥挤。\n**[M3]** Table 1 caption 信息过载。\n**[M4]** §3.5 Baselines 作为独立小节不必要。\n\n### Questions\n\n**[Q1]** 如何 disentangle \"death as a cause of routing signal\" vs. \"death as a downstream indicator of reasoning quality\"?\n**[Q2]** 如果将 diagnostic framework 应用于 MTRouter 的 routing decisions，DAF 是否仍主导？\n**[Q3]** Frontier models（GPT-4o/Claude 3.5）在 ScienceWorld 上的 death rate 可能大幅降低。是否有 evidence 表明 death avoidance 在 frontier regime 下仍主导？\n**[Q4]** 如果将 death penalty 设为 0（death 仅导致提前终止不额外扣分），DAF 会降到什么水平？\n**[Q5]** Grounding ablation 后 DAF 仍高是否意味着 death avoidance 是 fundamental 还是 ablation 力度不够？\n\n### Missing References\n\n**[R1]** Chow et al. (2015) CVaR optimization\n**[R2]** Tamar et al. (2015) CVaR via Sampling\n**[R3]** Speculative decoding 与 routing fallback 的类比\n\n---\n\n请逐条回应。"
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
    "round_number": "31",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Weakness、Question 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的完整审稿意见\n\n### Must-Fix\n\n**[W1] [critical] 标题和 Abstract 过度泛化，与 cross-environment evidence 矛盾**\nTitle \"Death Avoidance as the Dominant Routing Signal\" 暗示通用发现。但 §3.4 cross-environment probes 显示 MATH 上 DAF=0%、ALFWorld 上 DAF=0%。仅在 ScienceWorld 一个环境中成立。建议 Title 加限定词或重新定位 contribution。\n\n**[W2] [critical] DAF 分解在 harsh-penalty 环境中有 circularity**\nDAF 将 death-asymmetric episodes 的全部 gap 归因于 death avoidance。当 death penalty=-100 且 death rate 差异大时，DAF 机械性趋向高值——部分是方法论产物。Appendix K 的 penalty sensitivity 显示 DAF 随 P 单调递增。需要区分 accounting effect 和 genuine mechanism。\n\n**[W3] [critical] Contribution type 对 Main Conference 偏弱**\nDiagnostic framework + empirical finding 的定位。Framework 本身方法论创新有限，empirical finding 仅在一个环境中成立且 intuitive。对比 MTRouter（ACL 2026）prescriptive contribution 显著更强。更适合 Findings。\n\n### Should-Fix\n\n**[W4] [warning] 21 个 Appendix（A-U）过多，正文对 Appendix 依赖过重**\nAppendix 占 15 页，几乎是正文两倍。核心 claim 支撑证据在 Appendix：DAF penalty sensitivity（K）、Decision Framework（R）、Threshold Routing（Q）、cross-model 完整结果（M）。\n\n**[W5] [warning] Related Work 缺少 risk-sensitive RL 文献**\nCVaR-based optimization（Chow et al. 2015; Tamar et al. 2015）直接处理 trajectory-level catastrophic risk，与 death avoidance 高度相关。\n\n**[W6] [warning] \"Counterfactual\" 术语使用松散**\n方法更接近 matched-seed A/B testing 而非 Pearl (2009) 意义下的 structural counterfactual reasoning。\n\n**[W7] [warning] Router Training 结论 \"inconclusive\" 占用空间**\n半页讨论 router training 但结论是 inconclusive。没有深入分析为什么 routing 难以学习。\n\n**[W8] [warning] Discussion section 过薄**\n仅覆盖两个话题（signal granularity + oracle degeneracy），缺少条件分析和与 concurrent work 的对话。\n\n### Minor\n\n**[M1]** Abstract 数字堆砌。\n**[M2]** Figure 1 布局拥挤。\n**[M3]** Table 1 caption 信息过载。\n**[M4]** §3.5 Baselines 作为独立小节不必要。\n\n### Questions\n\n**[Q1]** 如何 disentangle \"death as a cause of routing signal\" vs. \"death as a downstream indicator of reasoning quality\"?\n**[Q2]** 如果将 diagnostic framework 应用于 MTRouter 的 routing decisions，DAF 是否仍主导？\n**[Q3]** Frontier models（GPT-4o/Claude 3.5）在 ScienceWorld 上的 death rate 可能大幅降低。是否有 evidence 表明 death avoidance 在 frontier regime 下仍主导？\n**[Q4]** 如果将 death penalty 设为 0（death 仅导致提前终止不额外扣分），DAF 会降到什么水平？\n**[Q5]** Grounding ablation 后 DAF 仍高是否意味着 death avoidance 是 fundamental 还是 ablation 力度不够？\n\n### Missing References\n\n**[R1]** Chow et al. (2015) CVaR optimization\n**[R2]** Tamar et al. (2015) CVaR via Sampling\n**[R3]** Speculative decoding 与 routing fallback 的类比\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 2633 · 2026-05-23T05:29:20.403185+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1358
}
```

</details>

---


### Assistant

_source line 2634 · 2026-05-23T05:29:22.704887+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 219

## Round 219

12 recorded events


### User

_source line 2635 · 2026-05-23T05:29:25.317980+00:00_

[Reviewer 1 审稿结果]:
审稿完成，已提交给 Review Director。

核心判断：**Overall 3.0（Findings 级别）**。

关键发现：
- 方法论框架（episode-level counterfactual + DAF 分解）设计简洁、可复用，是实在的贡献
- 但核心实证发现（death dominance, DAF=90.4%）仅在 ScienceWorld 一个主环境验证，且在 catastrophic-penalty 环境中该发现直觉上可预期
- 提出了 2 个 Must-Fix（单一主环境、oracle privilege 使发现接近 tautology）和 4 个 Should-Fix（K=11 统计推断、DAF 对 P 的依赖、episode→step 粒度错配、72B 无 cross-model replication）
- 论文最突出的优点是异常诚恳的自我批评和全面的稳健性分析（21 个附录）

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

_source line 2636 · 2026-05-23T05:29:53.010083+00:00_

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

_source line 2637 · 2026-05-23T05:29:53.060892+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T05:19:43.559685+00:00\", \"completed_at\": \"2026-05-23T05:23:53.176936+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 7-8\", \"message\": \"连续两页纯文本（Baselines 尾部 → Related Work → Discussion → Conclusion），无任何 figure/table/equation 穿插，审稿人在论文后半段会感到视觉单调。考虑在 Discussion 中加一个总结性 figure（如 DAF 分解的 summary bar chart）或将 Related Work 中的方法对比以小表格呈现。\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"主体正文 8 页仅有 4 个 display items（Figure 1, Table 1, Figure 2, Table 2），密度 0.5/页，低于实证论文典型的 5-8 个。核心分析结果（如 death avoidance decomposition、cross-environment 对比）缺少可视化支撑，大量定量结论散落在行内文字中，审稿人需要逐行 parse 数字。\"}, {\"severity\": \"warning\", \"dimension\": \"page 25\", \"message\": \"末页内容仅填充约 60%，Table 22 及其后续文字结束后底部约 40% 空白。低于 2/3 页面利用建议。可考虑将部分后续 appendix 表格前移或合并内容。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item，第一个视觉锚点（Figure 1 pipeline 图）出现在第 2 页右上角。在 3 页内出现，符合基线要求，但若能将 Figure 1 上提至第 1 页底部或右栏将显著增强第一印象。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（pipeline 图）整体清晰，caption 自包含，能传达核心 framework。但配色偏素（灰/米色为主），作为论文唯一的概念图，可适当增加对比度或用颜色区分 internal vs. deterministic 路径以强化视觉冲击力。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2 的 axis label 和 legend 文字相对正文偏小（估计约 6-7pt），在打印或缩放阅读时可能略吃力。建议放大至 ≥8pt。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 使用 booktabs 风格，格式规范。但最优结果的加粗标注不够醒目——建议检查 bold 是否一致应用于所有对比列的最优值。\"}, {\"severity\": \"info\", \"dimension\": \"page 13-25\", \"message\": \"附录 13 页（A-U 共 21 个 section）vs 正文 8 页，比例约 1.6:1。附录承载了大量关键验证（cross-model、ablation、sensitivity），审稿人可能质疑是否有核心内容被挤出正文。\"}, {\"severity\": \"info\", \"dimension\": \"page 19\", \"message\": \"单页包含 3 个表格（Tables 13-15）+ 1 个 figure（Figure 4），排版偏紧凑但内容均可读，无溢出。\"}, {\"severity\": \"info\", \"dimension\": \"page 1-9\", \"message\": \"未发现 LaTeX 渲染错误、未解析引用 [?]、margin 溢出、sec
…[truncated 136 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2638 · 2026-05-23T05:29:53.111548+00:00_

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


### Tool result

_source line 2639 · 2026-05-23T05:29:53.162133+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2640 · 2026-05-23T05:30:21.645883+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:update_review_issues,submit_review_report_to_research_director",
  "max_results": "2"
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
    "query": "select:update_review_issues,submit_review_report_to_research_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 2641 · 2026-05-23T05:30:21.696523+00:00_

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
